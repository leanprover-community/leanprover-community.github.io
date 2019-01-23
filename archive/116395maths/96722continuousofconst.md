---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/96722continuousofconst.html
---

## Stream: [maths](index.html)
### Topic: [continuous_of_const](96722continuousofconst.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 17 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous_of_const/near/152017837):
This is very much related to my question in the https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/Empty.20or.20not.20empty/near/152017713, but has some (tiny) math content. Can anyone golf the following ridiculous lemma?
```lean
lemma continuous_of_const {α : Type*} {β : Type*} [topological_space α] [topological_space β] {f : α → β} (h : ∀a b, f a = f b) :
  continuous f :=
begin
  by_cases H : ∃ x : α, true,
  { cases H with a,
    rw show f = λ x, f a, by ext x; rw h,
    exact continuous_const },
  { intros U Uin,
    convert is_open_empty,
    rw set.eq_empty_iff_forall_not_mem,
    intro x, 
    exfalso,
    exact H ⟨x, trivial⟩ }
end
```
@Kenny, can you can rid of axiom of choice here? I don't even know where it crops in.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 17 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous_of_const/near/152017862):
Of course you need to import `analysis.topology.topological_space`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 17 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous_of_const/near/152018202):
I don't think I can do much regarding axiom of choice

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 17 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous_of_const/near/152018645):
```lean
import analysis.topology.continuity

lemma continuous_of_const {α : Type*} {β : Type*} [topological_space α] [topological_space β] {f : α → β} (h : ∀a b, f a = f b) :
  continuous f :=
λ s _, classical.by_cases
  (λ hs : f ⁻¹' s = ∅, hs.symm ▸ is_open_empty)
  (λ hs : f ⁻¹' s ≠ ∅, let ⟨y, hy⟩ := set.exists_mem_of_ne_empty hs in
    have set.univ = f ⁻¹' s, from eq.symm $ set.eq_univ_of_forall $ λ x,
      show f x ∈ s, from h y x ▸ hy,
    this ▸ is_open_univ)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 17 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous_of_const/near/152018872):
Nice effort, but it doesn't change much (about the same length, same axioms)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 17 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous_of_const/near/152018977):
isn't there a lemma that says a constant proposition is open?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 17 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous_of_const/near/152018987):
`is_open_const`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 17 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous_of_const/near/152019040):
but this is a different formulation of "constant"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 17 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous_of_const/near/152019054):
right, but it is the one you want here, I think

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 17 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous_of_const/near/152019083):
it doesn't avoid LEM (because it's used in the proof) but you can defer the case splitting to it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 17 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous_of_const/near/152019353):
```lean
lemma continuous_of_const {α : Type*} {β : Type*}
  [topological_space α] [topological_space β]
  {f : α → β} (h : ∀a b, f a = f b) :
  continuous f :=
λ s _, by convert @is_open_const _ _ (∃ a, f a ∈ s); exact
  set.ext (λ a, ⟨λ fa, ⟨_, fa⟩,
    λ ⟨b, fb⟩, show f a ∈ s, from h b a ▸ fb⟩)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 17 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous_of_const/near/152019362):
nice

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 17 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous_of_const/near/152019456):
I have a long way to go before becoming a true obfuscation master...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 17 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous_of_const/near/152019513):
Thanks anyway!


{% endraw %}
