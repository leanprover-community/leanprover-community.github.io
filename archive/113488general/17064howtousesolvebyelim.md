---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/17064howtousesolvebyelim.html
---

## Stream: [general](index.html)
### Topic: [how to use `solve_by_elim`](17064howtousesolvebyelim.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Aug 17 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20%60solve_by_elim%60/near/132313630):
What is the syntax for giving `solve_by_elim` a discharger. I tried ``solve_by_elim `[cc] `` like the docs suggest, but I couldn't get it to work.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 17 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20%60solve_by_elim%60/near/132313735):
That would be a case of outdated documentation. Try ``solve_by_elim { discharger := `[cc] }``

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 17 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20%60solve_by_elim%60/near/132314890):
I just updated it. https://github.com/leanprover/mathlib/pull/266

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 09 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20%60solve_by_elim%60/near/133587653):
Hi @**Simon Hudon**, I proposed a further modification to `solve_by_elim` at https://github.com/leanprover/mathlib/pull/324. I'd be interested in your opinion sometime.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 09 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20%60solve_by_elim%60/near/133587655):
It's essentially just an extra option to make it convenient to add `congr_fun` and `congr_arg` to the assumptions.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 09 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20%60solve_by_elim%60/near/133587801):
Cool idea!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 25 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20%60solve_by_elim%60/near/134573606):
Thanks, @**Simon Hudon** and @**Reid Barton** for looking at my proposed changes to `solve_by_elim`. I've just pushed another change that make it quite a bit more usable --- it's now quite like the syntax for adding and removing lemmas from `simp`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 25 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20%60solve_by_elim%60/near/134573610):
https://github.com/leanprover/mathlib/pull/324

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 25 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20%60solve_by_elim%60/near/134574016):
What's the attribute name?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 25 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20%60solve_by_elim%60/near/134578415):
Oh -- there's no attribute that is automatically hooked into `solve_by_elim`, although we could do that!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 25 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20%60solve_by_elim%60/near/134578467):
You can write `solve_by_elim [f, a]`, where `f` is a lemma, and `a` is an attribute, it will will look up all lemmas tagged with `a`, and then use the local context, `f`, and those `a`-lemmas.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 25 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20%60solve_by_elim%60/near/134578473):
You can also write `solve_by_elim only [f, a]` to not include the local context.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 25 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20%60solve_by_elim%60/near/134578564):
Actually, now I see what you did and it might be better to refrain from having a default `solve_by_elim` attribute, at least for now. We're battling the huge size of the `simp` list at the moment, maybe we can avoid or at least postpone the same situation for `solve_by_elim` and other attribute-based tactics.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 06 2018 at 03:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20%60solve_by_elim%60/near/135292325):
Hi @**Simon Hudon**, I noticed what I think is a bug, or at least suboptimal behaviour in solve_by_elim, preventing successful backtracking when an `apply` generates multiple subgoals:
```
example {α : Type} (r : α → α → Prop) (f : α → α → α)
  (l : ∀ a b c : α, r a b → r a (f b c) → r a c)
  (a b c : α) (h₁ : r a b) (h₂ : r a (f b c)) : r a c :=
begin
  -- solve_by_elim ought to work here:
  have w : r a c,
  { apply l,
    apply h₁,
    apply h₂ },
  clear w,
  -- sadly, it doesn't, because of the way we recurse to subgoals.
  solve_by_elim,
  -- (Once solve_by_elim successfully uses h₂ on the first goal, it can't
  -- backtrack after realising that was a bad idea.)
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 06 2018 at 03:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20%60solve_by_elim%60/near/135292330):
There's an easy fix, but I thought I'd check if you agreed it warrants fixing before I PR it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 06 2018 at 03:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20%60solve_by_elim%60/near/135292921):
It looks like your proof of `w` is the only path that `solve_by_elim` can take. Can you show me the mistaken approach it tries?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 06 2018 at 04:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20%60solve_by_elim%60/near/135295040):
It can trying applying h2 first. That succeeds, but then it has no where to go, and it fails to backtrack.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 06 2018 at 04:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20%60solve_by_elim%60/near/135295082):
(Because with multiple sub goals solve_by_elim currently uses `;` to recurse into them, it can’t backtrack across multiple sub goals.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 06 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20%60solve_by_elim%60/near/135295134):
That is, it tries:
```
apply l,
apply h2
```
And then is faced with the goal `r a (f (f b c) ?m)` and can’t proceed.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 06 2018 at 04:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20%60solve_by_elim%60/near/135295233):
Ah! I see! How do you suggest to solve this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 06 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20to%20use%20%60solve_by_elim%60/near/135298736):
It's pretty easy: see https://github.com/leanprover/mathlib/pull/393/commits/3fab845ccdfb081febf09821c4c1e43dbb82f75b

