---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/53094bugwithsimpeditorsnotenotabug.html
---

## [general](index.html)
### [bug with simp (editor's note: not a bug)](53094bugwithsimpeditorsnotenotabug.html)

#### [Kenny Lau (Mar 06 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bug%20with%20simp%20%28editor%27s%20note%3A%20not%20a%20bug%29/near/123327630):
```
import algebra.linear_algebra.basic

variables (α β : Type) [ring α] [module α β]

example (v : lc α β) (h : v 0 = 0) : sorry :=
begin
  simp [lc] at v,
end
```

#### [Kenny Lau (Mar 06 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bug%20with%20simp%20%28editor%27s%20note%3A%20not%20a%20bug%29/near/123327634):
```
α β : Type,
_inst_1 : ring α,
_inst_2 : module α β,
v : lc α β,
h : ⇑v 0 = 0,
v : β →₀ α
⊢ sorry
```

#### [Kenny Lau (Mar 06 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bug%20with%20simp%20%28editor%27s%20note%3A%20not%20a%20bug%29/near/123327637):
the bug is that it creates another `v`

#### [Reid Barton (Mar 06 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bug%20with%20simp%20%28editor%27s%20note%3A%20not%20a%20bug%29/near/123328368):
I think it has to do with the fact that the hypothesis `h` depends on `v`, but I'm not sure what you're supposed to do about that

#### [Reid Barton (Mar 06 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bug%20with%20simp%20%28editor%27s%20note%3A%20not%20a%20bug%29/near/123328469):
`dsimp` works

#### [Mario Carneiro (Mar 06 2018 at 03:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bug%20with%20simp%20%28editor%27s%20note%3A%20not%20a%20bug%29/near/123330492):
Yeah, this is not a bug. The new `v` cannot necessarily take the place of the old `v` in `h`

#### [Mario Carneiro (Mar 06 2018 at 03:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bug%20with%20simp%20%28editor%27s%20note%3A%20not%20a%20bug%29/near/123330505):
`dsimp` allows this because the rewrite is definitional, so the new `v` has the same type as the old one, but if it's merely a propositionally equal type, then you may have to replace `v` with `cast v <ugly proof>` in uses of `v`

#### [Scott Morrison (Mar 06 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bug%20with%20simp%20%28editor%27s%20note%3A%20not%20a%20bug%29/near/123335508):
It would be nice if there was either a mode for simp, or just a cousin, that was much more aggressive about replacing later appearances of the simplified hypothesis, even if it required casts. I run into this fairly often.

#### [Scott Morrison (Mar 06 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bug%20with%20simp%20%28editor%27s%20note%3A%20not%20a%20bug%29/near/123335548):
Very often a step or two later the cast itself becomes easy to simplify, and you're back on safe ground.

#### [Mario Carneiro (Mar 06 2018 at 06:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bug%20with%20simp%20%28editor%27s%20note%3A%20not%20a%20bug%29/near/123335626):
I think you can achieve this effect by reverting the dependent hypotheses

#### [Mario Carneiro (Mar 06 2018 at 07:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bug%20with%20simp%20%28editor%27s%20note%3A%20not%20a%20bug%29/near/123337049):
But in my experience `cast`s are a pain to get rid of. What kind of proof strategy causes them to be "easy to simplify"?

#### [Scott Morrison (Mar 06 2018 at 07:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bug%20with%20simp%20%28editor%27s%20note%3A%20not%20a%20bug%29/near/123337471):
At some point I'll try to come up with a full example. But I've certainly found situations where "almost trivial" lemmas such as 
```lean
lemma {u₁ u₂} parallel_transport_for_trivial_bundles {α : Sort u₁} {a b : α} {β : Sort u₂} (p : a = b) (x : β) : @eq.rec α a (λ a, β) x b p = x :=
begin
induction p,
simp,
end
```
cause `@eq.rec`s to vanish away again. Right now I have to deal with some jet lag.

