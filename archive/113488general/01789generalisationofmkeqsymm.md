---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/01789generalisationofmkeqsymm.html
---

## Stream: [general](index.html)
### Topic: [generalisation of mk_eq_symm](01789generalisationofmkeqsymm.html)

---

#### [Scott Morrison (Mar 16 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123790494):
I am really struggling to write a tactic that "does mk_eq_symm, but even inside binders". I would like to have something that given `h : \forall x : X, f x = g x`, spits back `\forall x : X, g x = f x`. Can anyone point me in the right direction?

#### [Scott Morrison (Mar 16 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123790545):
(I need this to work its way through arbitrarily many binders, possibly zero.)

#### [Scott Morrison (Mar 16 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123790763):
So far I have
````lean
meta def mk_eq_symm_under_binders_aux : expr → expr → tactic expr
| e (expr.pi n bi d b) := do
                             b' ← mk_eq_symm_under_binders_aux (expr.app e b) b,
                             pure (expr.lam n bi d b')
| e t := mk_eq_symm e

meta def mk_eq_symm_under_binders : expr → tactic expr
| e := do t ← infer_type e, mk_eq_symm_under_binders_aux e t
````

#### [Kevin Buzzard (Mar 16 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123790818):
Whilst of course I can't help, the recent thread here about using rw really opened my eyes to how this sort of thing wasn't "happening by default" as it were. I am still a little unclear about why `eq.symm` can't be used directly but this is probably just my poor understanding of the notion of equality in type theory. If I had write a tactic proof which did this I would just continually apply conv to everything.

#### [Scott Morrison (Mar 16 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791017):
Yes! I know how to achieve this with `conv`. I need this tactic in service of my "rewrite searching" tactic, unfortunately, so a human isn't available to help direct the `conv`. I need to be able to determine if a rewrite is applying to the entire expression, or just a subexpression, but the only way to ask Lean to rewrite an entire expression seems to be via `simp_lemmas.rewrite`, which doesn't provide a facility for applying the rule in reverse, so I'm going to have to build the reverse rule myself.

#### [Scott Morrison (Mar 16 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791083):
But what I have above is stupid. The `expr.app e b` is silly, it's not `b` that I'm meant to put in there, it's.... something. :-)

#### [Kevin Buzzard (Mar 16 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791084):
I am a little disappointed that something like `repeat {by conv in (_ = _) {rw eq.symm}}` doesn't work in tactic mode :-)

#### [Kevin Buzzard (Mar 16 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791093):
Or, more precisely, that I couldn't get it to work :-)

#### [Mario Carneiro (Mar 16 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791337):
I wrote an extremely similar tactic for `alias`

#### [Scott Morrison (Mar 16 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791338):
I think my fundamental difficulty is I don't know how to construct an `expr.lam`.

#### [Scott Morrison (Mar 16 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791345):
I will look at `alias`!

#### [Mario Carneiro (Mar 16 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791349):
```
meta def mk_iff_mp_app (iffmp : name) : expr → (nat → expr) → tactic expr
| (expr.pi n bi e t) f := expr.lam n bi e <$> mk_iff_mp_app t (λ n, f (n+1) (expr.var n))
| `(%%a ↔ %%b) f := pure $ @expr.const tt iffmp [] a b (f 0)
| _ f := fail "Target theorem must have the form `Π x y z, a ↔ b`"
```

#### [Scott Morrison (Mar 16 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791350):
e.g., if I have `f : \nat \to \nat`, how to I construct the `expr` for `\lambda n, f (n+1)`?

#### [Mario Carneiro (Mar 16 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791390):
That tactic directly constructs a proof of `\forall x y z, a -> b` from `\forall x y z, a <-> b`

#### [Mario Carneiro (Mar 16 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791405):
I don't think it even needs to be a tactic (I only used a tactic in that case so I could fail with a nice error message)

#### [Scott Morrison (Mar 16 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791446):
So how does `expr.var` work?

#### [Scott Morrison (Mar 16 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791447):
That has me confused.

#### [Mario Carneiro (Mar 16 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791450):
`expr.var` is a de bruijn variable

#### [Mario Carneiro (Mar 16 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791456):
so `\forall x y z, x = y` becomes roughly `pi "x" (pi "y" (pi "z" (app (app (const "eq") (var 2)) (var 1)))`

#### [Mario Carneiro (Mar 16 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791506):
the number counts how many binders back the variable is

#### [Scott Morrison (Mar 16 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791513):
I see. (Or, at least I can imagine writing voodoo code based on what I see. :-)

#### [Mario Carneiro (Mar 16 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791558):
I have an aversion to writing code that has suboptimal asymptotics, so I may have been too clever in the definition there, what with the accumulation function and all

#### [Mario Carneiro (Mar 16 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791609):
Also, I don't think you will be able to use `mk_eq_symm` in the function

#### [Kevin Buzzard (Mar 16 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791613):
I guess one question for Scott then is whether he is likely to be applying his tactic to terms built from strings of length 10^10 :-)

#### [Scott Morrison (Mar 16 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791616):
What will go wrong with `mk_eq_symm`?

#### [Mario Carneiro (Mar 16 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791617):
because when you are working on an expr manually like this, you have to deal with open terms, and tactics don't like open terms

#### [Mario Carneiro (Mar 16 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791624):
open meaning containing an unbound `var`

#### [Scott Morrison (Mar 16 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791625):
(Or you can let me find out for myself in a minute or two..)

#### [Scott Morrison (Mar 16 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791628):
I see. But I can just build it directly myself?

#### [Scott Morrison (Mar 16 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791630):
(as you did in your example)

#### [Mario Carneiro (Mar 16 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791670):
yes

#### [Kevin Buzzard (Mar 16 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791690):
Is it just a coincidence that Mario posted code with the line `lam n, f (n+1)` seconds before Scott asked about how to construct the `expr` for `lam n, f (n+1)`?

#### [Scott Morrison (Mar 16 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791736):
apparently yes :-)

#### [Scott Morrison (Mar 16 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791740):
They have nothing to do with each other. :-)

#### [Scott Morrison (Mar 16 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791741):
(and wow, this looks like it may be working!)

#### [Kevin Buzzard (Mar 16 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791747):
I thought so but I thought I'd ask as I am frantically cut-and-pasting into a text file and just wanted to check that zulip didn't have some "slightly re-order the messages" functionality

#### [Kevin Buzzard (Mar 16 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791810):
It's about time I learnt something about tactics and one way of learning is to write some docs.

#### [Scott Morrison (Mar 16 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791850):
Thank you all! Things are looking good here. :-) `all_rewrites` seems to be working, finding lots of rewrites that `rw` itself can't see.

#### [Kevin Buzzard (Mar 16 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791853):
Can you post what you wrote?

#### [Kevin Buzzard (Mar 16 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791854):
[if you're happy to do so of course!]

#### [Scott Morrison (Mar 16 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791855):
It's probably slow as molasses ... but that's a different problem.

#### [Scott Morrison (Mar 16 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791902):
```lean
meta def mk_eq_symm_under_binders_aux : expr → (nat → expr) → tactic expr
| (expr.pi n bi d b) f := expr.lam n bi d <$> mk_eq_symm_under_binders_aux b (λ n, f (n+1) (expr.var n))
| `(%%a = %%b) e := mk_eq_symm (e 0)
| _ _ := fail "expression must have the form `Π x y z, a = b`"

meta def mk_eq_symm_under_binders : expr → tactic expr
| e := do t ← infer_type e, mk_eq_symm_under_binders_aux t (λ _, e)
```

#### [Scott Morrison (Mar 16 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791903):
That's just the `mk_eq_symm_under_binders` part.

#### [Scott Morrison (Mar 16 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791907):
Then there's
```lean
meta def rewrite_entire (r : (expr × bool)) (e : expr) : tactic (expr × expr) :=
do let sl := simp_lemmas.mk,
   r' ← if r.2 then mk_eq_symm_under_binders r.1 else pure r.1,
   sl ← sl.add r',
   sl.rewrite e
```

#### [Scott Morrison (Mar 16 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791924):
which given `r`, a rule and a `bool` flag indicating whether to use the rule in reverse, and an expression `e`, either rewrite the entire expression `e` using the rule, returning the replacement and the proof, or fails.

#### [Kevin Buzzard (Mar 16 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791965):
Now I will tell my students to alias rw to this and they will never have to worry about why it used to sometimes fail :-)

#### [Scott Morrison (Mar 16 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791971):
And then there's https://gist.github.com/semorrison/9b3a0f42fbd697d562a8b6daa960f14e

#### [Scott Morrison (Mar 16 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791976):
for the actual implementation of `all_rewrites`

#### [Scott Morrison (Mar 16 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123791977):
which still needs a little more wrapper before you can use it in interactive mode...

#### [Kevin Buzzard (Mar 16 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalisation%20of%20mk_eq_symm/near/123792018):
Thanks for this. I know I could just try to learn tactics by reading the tactic code in core Lean etc but the problem with doing that is that it can often be pretty hard-core. It's like trying to learn Lean by reading core lean and instantly finding opt_params everywhere with no explanation as to what they are.

