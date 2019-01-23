---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/04500subsetreflweirdness.html
---

## Stream: [general](index.html)
### Topic: [subset refl weirdness](04500subsetreflweirdness.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 04 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20refl%20weirdness/near/126108434):
Is this a bug?
```lean
set_option pp.all true
example {α : Type} (s : set α) : s ⊆ s := by refl
/-
error: invalid apply tactic, failed to unify
  @has_subset.subset.{0} (set.{0} α) (@set.has_subset.{0} α) s s
with
  @has_subset.subset.{?l_1} (list.{?l_1} ?m_2) (@list.has_subset.{?l_1} ?m_2) ?m_3 ?m_3
state:
α : Type,
s : set.{0} α
⊢ @has_subset.subset.{0} (set.{0} α) (@set.has_subset.{0} α) s s
-/
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 04 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20refl%20weirdness/near/126108665):
I guess this actually does not exist anywhere...?
```lean
@[refl] lemma set.subset.refl {α : Type u} (s : set α) : s ⊆ s := λ x, id
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (May 04 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20refl%20weirdness/near/126108698):
You're probably right. You can try:

```
local attribute [refl] set.subset.refl -- if that's the name of the appropriate lemma
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (May 04 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20refl%20weirdness/near/126108701):
Then your proof will work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 04 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20refl%20weirdness/near/126108905):
Ah, the lemma does exist in mathlib, but without `@[refl]`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 05 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20refl%20weirdness/near/126115996):
The proof of a refl lemma is often `rfl`, and conversely any proof which is proved with `rfl` is I think automatically tagged `@[refl]`, but because the proof wasn't rfl here the tag is needed.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (May 05 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20refl%20weirdness/near/126116079):
`rfl` is only for reflexivity of equality and the tag comes from the fact that `rfl` implies that the two terms are definitionally equal. But if we're talking of reflexivity of other relations than equality, it doesn't imply anything with regards to definitional equality

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 05 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20refl%20weirdness/near/126116346):
I just tried my theory and the lemma I proved with rfl was tagged `@[_refl_lemma]` not `@[refl]`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (May 05 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20refl%20weirdness/near/126151045):
`@[refl]` means it's a proof that a relation is reflexive and is for the `refl` tactic. `@[_refl_lemma]` means it's a proof of equality proved using `rfl` for the `dsimp` tactic.


{% endraw %}
