---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/75082solvebyelim.html
---

## Stream: [general](index.html)
### Topic: [solve_by_elim](75082solvebyelim.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Mar 09 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123468417):
@**Simon Hudon**, the new solve_by_elim is really nice, and now I’d like it to do even more. I know that there is a mechanism to pass arbitrary assumptions, rather than using local context, and perhaps I should just use that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Mar 09 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123468426):
But a particular thing I find myself using frequently now is applying eq.symm to various things in the context, before solve_by_elim can do its thing.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 09 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123468582):
That's interesting. Maybe I could add `cc` to `solve_by_elim`. In terms of performance, I don't know what kind of slow down that would be but maybe this could be enabled by `solve_by_elim!`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Mar 09 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123468654):
The other thing I'm finding I have to do is replace a hypothesis `h : f = g` with `funext` applied to it, to get `h' : \forall x : X, f x = g x`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 09 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123468659):
Can you try something for me? Write:

```
meta def my_solve_by_elim (asms : option (list expr) := none)  : opt_param ℕ 3 → tactic unit
| 0 := done
| (succ n) :=
apply_assumption asms $ cc <|> my_solve_by_elim n
```

and tell me if that does the job

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Mar 09 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123468660):
Again, it would be nice to automate a bit.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Mar 09 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123468663):
I'll investigate, thanks.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 09 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123468795):
For the second bit, maybe adding `simp [function.funext_iff] at *` before `solve_by_elim` would help.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 09 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123468807):
(`function.funext_iff` is a new theorem in `mathlib`)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Mar 09 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123468920):
(ha, I'd actually just written `funext_iff` myself)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Mar 09 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123469450):
No, `cc` doesn't seem to help here.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 09 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123469466):
Can you should me a situation where the issue arises?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Mar 09 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123469512):
Oh -- a bug in solve_by_elim: the recursive call doesn't pass the arguments asms.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Mar 09 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123469531):
Well, maybe this is too trivial ... :-)
```lean
lemma f {α} (a b : α) (p : a = b) : b = a :=
begin
  my_solve_by_elim
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 09 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123469532):
It doesn't need to because it's declared on the left of `:`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Mar 09 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123469535):
ah, great, sorry.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 09 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123469596):
This example could be handled by `cc` on its own

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Mar 09 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123469598):
I guess it's obviously not going to help here...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 09 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123469736):
what does `solve_by_elim` do?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Mar 09 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123469744):
repeatedly tries to apply hypotheses, discharging new goals created by `apply` by calling itself

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Mar 09 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123469746):
(i.e. discharging them by matching against other hypotheses)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 09 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123469801):
@**Scott Morrison** Can you show me something that `cc` doesn't solve?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Mar 09 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123469857):
I'll have to look further. I'll try to see how much `cc` and `solve_by_elim` together let me automate, and get back to you if I find such an example.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 09 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123469863):
cool :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 09 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123469907):
btw, have you tried `tauto`? Does it help?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Mar 09 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123469930):
no, I haven't looked much at tauto yet. I already have tactics that do a lot of automatic `cases`, so I'm guessing it won't help much?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Mar 09 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123469990):
The other pattern I have all the time is: a hypothesis `p : x = y`, where `x` and `y` are terms of some structure type `S`, then I go: `have p' := congr_arg S.f p, solve_by_elim`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Mar 09 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123470004):
It would be lovely to handle that automatically... that is, not just apply hypotheses, but apply structure fields `congr_arg`d over hypotheses.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 09 2018 at 01:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123470117):
That's an interesting case. It's a bit like funext_iff which we talked about earlier in that we infer the equality of the parts from the equality of the whole. I feel like there's probably a greek-letter-reduction for that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 09 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123470312):
I'm wondering if `congr_arg` / `funext_iff` / `cc` might be the best combination

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Mar 09 2018 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123470376):
I'm not sure what you mean. I guess what I'm hoping for it some automation for finding the correct applications of `congr_arg`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Mar 09 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123470431):
(i.e. work out for itself what the field `S.f` should be in my example above: `have p' := congr_arg S.f p`.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 09 2018 at 01:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123470446):
If I see `x = y` where `x` and `y` are functions, I'd specialize `∀ i, x i = y i` for every `i` such that `x i` appears in the context. Same thing `y`. I'd do the same with the fields of structure types

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 09 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123470504):
I'll write something, make a PR to mathlib and send you a link. How about that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Mar 09 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123470518):
sounds amazing :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 09 2018 at 02:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/123471150):
Do you have an example where that would be useful? All the examples I can think of can be handled directly by `cc`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Apr 13 2018 at 05:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125017118):
`cc` successfully solves
````
example {α β : Type} (f g : α → β) (w : g = f) (y : α) : f y = g y := by cc
````
but not
````
example {α β : Type} (f g : α → β) (w : (λ x, g x) = (λ x, f x)) (y : α) : f y = g y := by cc
````
Does anyone see some slight generalisation of `cc` (and/or possibly `solve_by_elim`) that can handle the second case?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Apr 13 2018 at 05:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125017465):
This example is unnecessarily complicated, sorry: even this pair:
````
example {α β : Type} (f g : α → β) (w : f = g) (y : α) : f y = g y := by cc -- success
example {α β : Type} (f g : α → β) (w : (λ x, f x) = (λ x, g x)) (y : α) : f y = g y := by cc -- FAIL
````

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Apr 13 2018 at 05:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125017472):
shows what's going on

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 13 2018 at 05:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125017524):
What happens if you call `simp` on `w` before `cc`? If it does eta reduction, then `cc` should succeed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Apr 13 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125017540):
That does work, but only because my MWE is too M!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Apr 13 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125017603):
Maybe 
````
example {α : Type} (f g : α → α) (w : (λ x, f (f x)) = (λ x, g (g x))) (y : α) : f (f y) = g (g y) :=
````
shows more of what I want.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 13 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125017605):
That sounds like my conversations with my advisor: "- what are you looking at now? - Large scale software. - Cool, do you have a small example to illustrate your idea? - ..."

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 13 2018 at 06:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125017708):
scott, you are talking higher order matching here. It's very unlikely you will get something as powerful as what you are envisioning. Your best bet is to apply (reverse) funext on your hypotheses to turn it into a first order problem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 13 2018 at 06:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125017711):
By reverse funext, do you mean `congr_fun`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 13 2018 at 06:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125017722):
yes, with some beta postprocessing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 13 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125017788):
Maybe @**Scott Morrison** would be satisfied with converting `f (f x)` to `(f o f) x`. Then `simp, cc` would be good enough.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 13 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125018251):
My point is that if `\forall x, f (f x) = g (g x)` was in the context instead of the lambda equality, I think cc would get it... maybe. (Honestly I don't understand how cc works, and I never trust it for anything significant.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 13 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125018302):
It seems to work a bit like the ematching feature of smt solvers, doesn't it? I wouldn't count on it to do any specialization

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Apr 13 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125018404):
@**Mario Carneiro**, thanks, this had been my past solution, but I'd been a bit worried by it. I'll leave it in place for now.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 13 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125018449):
@**Scott Morrison** Can you elaborate on why you prefer the equality between lambda terms?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Apr 13 2018 at 07:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125020210):
It’s just that the earlier steps of my automation are giving my equalities
between lambdas as hypotheses, and I’m having trouble automatically always
getting these into a form that cc / solve_by_elim / rewrite_search can deal
with. I think just replacing hypotheses which are equations between
functions types with foralls will do the job, and doesn’t seem to cause
problems elsewhere.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Apr 13 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125022906):
Congruence closure (`cc`) performs purely equational reasoning via congruences.  It can prove `a=b, c=b |- f a = f c`, but that's essentially it.  One nice feature is that since it uses the congruence lemmas, it effectively ignores subsingleton arguments.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Apr 13 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125022965):
It definitely won't solve ` forall x, f x = g x |- f a = g a` or `fun x, f x = g x |- f a = g a`.  (They're clearly equivalent via funext, as you've observed.)  If you solve such problems, then you have a first-order prover---and this is out of scope for `cc`.  Congruence closure is supposed to be fast, predictable, and well, do congruence closure (and not general first-order proving).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Apr 13 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125023122):
Re: E-matching.  Yes, you can solve the example with `forall x, f x = g x` using it (I think `by[smt] eblast` should do it).  What E-matching does is that it heuristically generates instances of universally quantified formulas (I think the `ematch` tactic uses the local context and lemmas tagged `[ematch]`).   In the example it would generate the instance `f y = g y`, and with this instance `cc` can solve the goal.  The instance `f y = g y` is generated because the *trigger* `f ?m_1` (in this example the lhs of the lemma)  E-*matches* a currently known subterm, namely `f y` (the lhs of the target in the example).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Apr 18 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125222682):
@**Simon Hudon**, how would you feel about generalising the definition of `solve_by_elim` to 
````lean
meta def solve_by_elim (asms : option (list expr) := none) (discharger : tactic unit := tactic.done) : opt_param ℕ 3 → tactic unit
| 0     := tactic.done
| (n+1) := discharger <|> (tactic.interactive.apply_assumption asms $ solve_by_elim n)
````
I find myself using this as `solve_by_elim none cc` frequently and it's very helpful.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125223029):
Won't you have to write this as `tactic.cc` in an interactive tactic script?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 18 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125223045):
I like it. Let's switch the order of `asms` and `discharger` though.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 18 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125223109):
@**Mario Carneiro** Why? `cc` is also in `tactic.interactive`, no?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125223202):
but if it's not being parsed in interactive mode, you have to use the right namespace

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125223249):
one option is to have an `itactic` for the discharger, then you can write `{cc}` or some other tactic block

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 18 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125223254):
Right. Alternatively, we can provide a variant such as `solve_by_elim_with { cc }` with a `itactic` argument (and a better name)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125223261):
I think you can still make it optional

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 18 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125223279):
No because `itactic` doesn't use the same parsing framework as everything else

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125223288):
Have you used `asms`? I think it needs a parser

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 18 2018 at 01:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125223349):
If we don't want multiple tactic names, we'd have to live with `solve_by_elim { }` when we don't use that feature.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 18 2018 at 01:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125223360):
or stick with just passing a regular tactic and live with ``solve_by_elim `[cc]``

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 18 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125223417):
```quote
Have you used `asms`? I think it needs a parser
```
I haven't used it in interactive mode. I think similarly to the options that you can feed `simp` (e.g. `{ single_pass := tt }`) you can give it a literal as an expression

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Apr 20 2018 at 03:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/125335574):
@**Simon Hudon** just checking -- should I PR this, or would you prefer to do it? I'm happy either way.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 23 2018 at 04:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/128504293):
Hi @SimonHudon, I'm finding often `solve_by_elim` would succeed, except for the fact that an applicable equation needs to be wrapped in `eq.symm` first. In this case, `{discharger := cc}` works, but this tends to be very expensive and I'd really like to avoid it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 23 2018 at 04:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/128504299):
It's certainly possible to pass a more limited discharger, that just tries to apply hypotheses backwards, but I'm wondering what you think about building this behaviour in?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 23 2018 at 04:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/128504331):
(e.g. by writing a version of `apply` that knows about symmetric relations, and then using that --- I'd be happy to implement if you thought this was reasonable behaviour)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 23 2018 at 04:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/128504349):
I think that's feasible. We could probably define it as `sym_apply (r) := apply r <|> (symmetry >> apply r)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 23 2018 at 04:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/128504366):
oh, that's much sneakier than what I had in mind

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 23 2018 at 04:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/128504392):
Currently in `apply_assumption` you do an initial filtering step by `find_matching_head`, and I guess this wouldn't be viable.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 23 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/128504400):
Do you know if this actually saves much time? I'd hope that `apply` returns very quickly on anything `find_matching_head` had discarded.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 23 2018 at 04:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/128504510):
You're right. I have a feeling we could get rid of the filtering. I'm not sure that testing the assumptions is any faster than just applying them

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 23 2018 at 04:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/128504515):
It might actually be slower because we might be doing the same work twice

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 23 2018 at 04:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/128504570):
I naively copied the behavior of `assumption` when I wrote that tactic. I didn't spend too much time thinking of the performances. It might be interesting to remove the filtering and measure the performances before adding the symmetry

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 23 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/128504777):
The other thing I'm wondering is if we should try every assumption directly first and only then try symmetry or try symmetry as we go. The upside of the first approach is that when you don't need symmetry, you get better performances. The downside is that you can't say that the tactic applies "the first assumption that matches" anymore. If assumption 11 matches directly and assumption 2 matches modulo symmetry, which one do we want the tactic to pick?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 23 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/128504778):
Hmm... my preference is to just make the change. :-) We do need some better tools for measuring performance. I know I neglect doing it, and then suffer for it later. (e.g. just now realising that letting solve_by_elim call `cc` can be very expensive)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 23 2018 at 04:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/128504831):
I would prefer just making the change too. I guess the rest is for extra credits :D

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 23 2018 at 04:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/128504832):
interesting... my inclination is to try symmetry as we go. When we're using `apply`, the semantic difference between `a=b` and `b=a` has pretty much disappeared.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 23 2018 at 04:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/128504837):
In that case, https://github.com/leanprover/mathlib/pull/164

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 23 2018 at 04:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/128504879):
I prefer that too. And my intuition is that the difference in performances will be unnoticeable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 23 2018 at 04:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/128504886):
That was fast!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 23 2018 at 04:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/128504899):
The added benefit is the code gets shorter and neater :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 23 2018 at 04:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/128504904):
Would you care to add a test case?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 23 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/solve_by_elim/near/128504957):
Sure!


{% endraw %}
