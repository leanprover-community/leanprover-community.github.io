---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/91735isidealnegiff.html
---

## Stream: [maths](index.html)
### Topic: [is_ideal.neg_iff](91735isidealnegiff.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 06 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_ideal.neg_iff/near/135313777):
```lean
import ring_theory.ideals

variables {α : Type} [comm_ring α] (N : set α) [is_ideal N]
example (a : α) (h : a ∈ N) : -a ∈ N :=
begin
  -- rwa is_ideal.neg_iff at h, 
  rwa @is_ideal.neg_iff _ _ _ N _ at h,  
end
```
Why can't I use the first line?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 06 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_ideal.neg_iff/near/135313787):
Looks like it makes that lemma unusable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 06 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_ideal.neg_iff/near/135313830):
Recall `lemma neg_iff {S : set α} [is_ideal S] : a ∈ S ↔ -a ∈ S := ⟨is_submodule.neg, λ h, neg_neg a ▸ is_submodule.neg h⟩`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Oct 06 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_ideal.neg_iff/near/135313839):
The set should be explicit. I'm not sure why it happens, but it's the same with `rw`s for `is_group_hom`, the function that is a `group_hom` needs to be given explicitly.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 06 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_ideal.neg_iff/near/135313939):
So you suggest modifying the binder in the statement of the lemma?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 06 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_ideal.neg_iff/near/135314381):
Maybe it's because `a ∈ S` is really just `S a`, that is, a variable function applied to a variable argument. Lean is probably unwilling to try to guess both the function and the argument.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 06 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_ideal.neg_iff/near/135314387):
But it shouldn't be unfolding this at all, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 06 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is_ideal.neg_iff/near/135314392):
Yeah that part I am not sure about.


{% endraw %}
