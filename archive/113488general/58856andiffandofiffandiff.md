---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/58856andiffandofiffandiff.html
---

## Stream: [general](index.html)
### Topic: [and_iff_and_of_iff_and_iff](58856andiffandofiffandiff.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 03 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/and_iff_and_of_iff_and_iff/near/135087802):
Would this be a useful lemma for mathlib? If so, where should it go? I currently solve this by `split; intros; split,` but that is a bit of a hack, and creates 4 goals where usually 2 should suffice.
```lean
theorem and_iff_and_of_iff_and_iff {P1 P2 Q1 Q2 : Prop} (H : (P1 \iff Q1) \and (P2 \iff Q2)) :
(P1 \and P2) \iff (Q1 \and Q2) := sorry
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 03 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/and_iff_and_of_iff_and_iff/near/135087872):
This looks like `and_congr`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 03 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/and_iff_and_of_iff_and_iff/near/135087981):
Cool, I'll use that! Is there a way that I could have discovered that name myself?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Oct 03 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/and_iff_and_of_iff_and_iff/near/135088008):
I also had trouble finding that. Like me, Johan may have been look for something `iff`-named instead of `and`- and `congr`-named.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Oct 03 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/and_iff_and_of_iff_and_iff/near/135088104):
I probably tried `git grep 'and.*iff'` and `git grep 'iff.*and'`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 03 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/and_iff_and_of_iff_and_iff/near/135088105):
That's true. This is a special pattern, like `ext`. `congr` lemmas mean if the inputs are equal then a function applied to those inputs is equal

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 03 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/and_iff_and_of_iff_and_iff/near/135088176):
There are similar theorems for all the propositional functions, and for regular functions `congr` the tactic will often generate these on the fly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 03 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/and_iff_and_of_iff_and_iff/near/135088308):
You will also find custom `congr` lemmas for things like `list.map_congr`, where we want to insert an additional assumption into the hypothesis (if `\all x \in l, f x = g x` then `map f l = map g l`)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 03 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/and_iff_and_of_iff_and_iff/near/135088324):
so many higher order functions have some kind of altered `congr` lemma

