---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/16498generatingallapps.html
---

## [general](index.html)
### [generating all `app`s](16498generatingallapps.html)

#### [Scott Morrison (Apr 25 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125644011):
Say I have an `e : expr`, which is probably some function type, and some other collection of `A : list expr`, and I would like to find all ways of plugging something from `A` into the next argument of `e`. Should I:
1) Actually look at what type `e` is, in particular the type of its first argument, and then look through `A` checking if there is anything of that type?
2) Just invoking `mk_app e [a]` for each `a` in `A`, and collect whatever succeeds?

#### [Scott Morrison (Apr 25 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125644133):
Option 2) is obviously much easier to write, I'm just wondering if I should expect that it is going to be way slower, or something.

#### [Simon Hudon (Apr 25 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125645974):
It might be worth experimenting but I don't think 2) would be any slower than 1)

#### [Scott Morrison (Apr 25 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125649582):
err... `mk_app` takes a `name` and a `list expr` worth of arguments. If I just have `a b : expr`, what's the idiomatic way to apply `a` to `b`, inferring implicit arguments and typechecking?

#### [Simon Hudon (Apr 25 2018 at 03:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125649764):
I think `type_check (a b)` might do the trick. You can also postpone type checking until you actually use those expressions.

#### [Scott Morrison (Apr 25 2018 at 03:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125650082):
Are there some backticks missing in your suggestion there?

#### [Scott Morrison (Apr 25 2018 at 03:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125650086):
I haven't quite internalised quoting and antiquoting ...

#### [Simon Hudon (Apr 25 2018 at 03:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125650146):
In this case, I'm just using the fact that `expr` has a `has_coe_to_fun` instance so you can use an expr as a function and it just wraps it in a `expr.app`

#### [Scott Morrison (Apr 25 2018 at 03:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125650266):
I think I can also use something like ```try_core (to_expr ``(%%e %%f))```.

#### [Simon Hudon (Apr 25 2018 at 03:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125650448):
Yes I think that's right. It might be slower because your going from `expr` to `pexpr` and back.

#### [Simon Hudon (Apr 25 2018 at 03:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125650508):
Depending on what you do with the expressions after, you might be able to do better than my proposal. Whatever you do with the resulting expression might need to be type checked again so you could just return `a b` with the understanding that it might eventually fail to type check

#### [Mario Carneiro (Apr 25 2018 at 04:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125651850):
How did you get `a` in your application `a b`? Lean works at the application list level (i.e. `f a1 a2 ... an`) when it does implicits and such

#### [Mario Carneiro (Apr 25 2018 at 04:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125652123):
I think the fastest option is to whnf the type of a to a Pi type, get its binding domain, and then `unify` it with the type of `b \in A` for each `b`. That way you minimize the amount for repeated work for failures and don't have to check more than you need to (`type_check` will go through the whole term)

#### [Simon Hudon (Apr 25 2018 at 04:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125652179):
Interesting! So option 1). I went the other way because I think this work will have to be done by the type checker and since that's done in C++, I would think it would be faster than anything you'd come up with.

#### [Mario Carneiro (Apr 25 2018 at 04:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125652189):
`type_check` is never done in C++, it's only for debugging

#### [Mario Carneiro (Apr 25 2018 at 04:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125652192):
it's all incremental in the C++ stuff

#### [Mario Carneiro (Apr 25 2018 at 04:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125652235):
In scott's case the `a` is constant but the `b` changes, so it makes sense to precompute it

#### [Simon Hudon (Apr 25 2018 at 04:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125652241):
Good point

#### [Mario Carneiro (Apr 25 2018 at 04:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125652253):
I'm guessing that Scott is building a search algorithm that just strings everything together that's well typed (trying to prove the five lemma maybe?) and for that this will be a really hot path so quick failure is important

#### [Mario Carneiro (Apr 25 2018 at 04:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125652352):
Option 2 would possibly have worked, but it's not type correct as scott points out and there's no immediate fix, lean isn't optimized for this kind of checking

#### [Scott Morrison (Apr 25 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125665542):
I'm going to defer trying @**Mario Carneiro**'s suggested fastest option, as I'm not confident playing with binding domains yet.

#### [Scott Morrison (Apr 25 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125665550):
In the meantime, it seems that when I try ```to_expr ``(%%e %%f)```, Lean doesn't manage to fill in implicit arguments.

#### [Scott Morrison (Apr 25 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125665598):
Is this expected? Is there a good way to do this? I'll try to come up with a MWE now.

#### [Scott Morrison (Apr 25 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125666920):
It seems that the problem is that ```to_expr ``(%%e %%f)``` is over-eager about implicit arguments.

#### [Scott Morrison (Apr 25 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125666928):
Say `e` represented something with a explicit argument then an implicit argument.

#### [Scott Morrison (Apr 25 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125666937):
Then ```to_expr ``(%%e %%f)``` produces not `e f` but `e f ?m_1`.

#### [Scott Morrison (Apr 25 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125667061):
````lean
axiom f : ℕ → Type
def g (n : ℕ) {k : ℕ} (x : f k) := n

set_option pp.implicit true
example : true :=
begin
  do e ← to_expr ```(g),
     f ← to_expr ```(57),
     to_expr ```(%%e %%f) >>= pp >>= trace
end
````

#### [Scott Morrison (Apr 25 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125667066):
produces `@g 57 ?m_1`

#### [Scott Morrison (Apr 25 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125667074):
But I'd really like it to just produce `g 57`.

#### [Scott Morrison (Apr 25 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125667526):
Hmm... I think this one is above my pay-grade for now. If anyone would like to help write a 
````lean
meta def apps (e : expr) (F : list expr) : tactic (list expr) :=
````
that actually works (i.e. return a list of all ways to plug in an `f ∈ F` as the next explicit argument of `e`) that would be wonderful.

#### [Scott Morrison (Apr 25 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125667530):
My current implementation is 
`do l ← F.mmap $ λ f, (do r ← try_core (to_expr ```(%%e %%f)), return r.to_list), return l.join`

#### [Scott Morrison (Apr 25 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125667550):
But that suffers from the problem explained above. Mario suggested to me that I first inspect `e`, find the first explicit binder in it, and try to unify it with each element of `F`.

#### [Scott Morrison (Apr 25 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125667610):
Unfortunately I don't know what I'm meant to do with any earlier implicit binders I find before the first explicit one, or how they would end up getting assigned by unification.

#### [Simon Hudon (Apr 25 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125671135):
When you encounter implicit binders, create a meta variable and use it as a parameter.

#### [Scott Morrison (Apr 25 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125671191):
@**Simon Hudon** do you know of examples of this I can look at? I got pretty confused dealing with binders. :-(

#### [Simon Hudon (Apr 25 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125671468):
Sure, have a look at https://github.com/leanprover/mathlib/blob/master/tactic/basic.lean#L100-L105

#### [Scott Morrison (Apr 25 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125672334):
Okay, that's helpful. Do you know if there is any existing code  that instead of just producing `expr.app e f`, produces `e`, with `f` stuck into the first explicit argument of `e` (and any earlier implicit arguments filled)?

#### [Simon Hudon (Apr 25 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125672812):
I'm sure I have something like that around. Let's see ...

#### [Simon Hudon (Apr 25 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125673275):
Actually, I can't find exactly that but let me sketch something for you

#### [Scott Morrison (Apr 25 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125673562):
Thank you! I better go to sleep now, but I'll look forward to seeing your answer when I'm back.

#### [Simon Hudon (Apr 25 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125673600):
Hopefully, this catches you before sleep does:

```lean
meta def mk_app_aux : expr → expr → expr → tactic expr 
 | f (expr.pi n binder_info.default d b) arg := do
   infer_type arg >>= unify d,
   return $ f arg
 | f (expr.pi n _ d b) arg := do
   v ← mk_meta_var d,
   t ← whnf (b.instantiate_var v),
   mk_app_aux (f v) t arg
 | e _ _ := return e

meta def mk_app' (f arg : expr) : tactic expr := 
do t ← infer_type f >>= whnf,
   mk_app_aux f t arg
```

#### [Scott Morrison (Apr 25 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125674417):
Perfect.

#### [Scott Morrison (Apr 25 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generating%20all%20%60app%60s/near/125674504):
(I changed `| e _ _ := return e` to `| e _ _ := failed`)

