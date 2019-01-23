---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/85479leminofmem.html
---

## Stream: [general](index.html)
### Topic: [le_min_of_mem](85479leminofmem.html)

---


{% raw %}
#### [ Kenny Lau (Jul 28 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le_min_of_mem/near/130485616):
```lean
theorem le_min_of_mem {s : finset α} {a b : α} (h₁ : b ∈ s) (h₂ : a ∈ s.min) : a ≤ b :=
by rcases @inf_le (with_top α) _ _ _ _ _ _ _ h₁ _ rfl with ⟨b', hb, ab⟩;
   cases h₂.symm.trans hb; assumption
```

#### [ Kenny Lau (Jul 28 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le_min_of_mem/near/130485617):
looks like `min_le_of_mem` to me

#### [ Chris Hughes (Jul 28 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le_min_of_mem/near/130485669):
PR it.

#### [ Chris Hughes (Jul 28 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/le_min_of_mem/near/130485715):
my guess is someone copied the name `le_max_of_mem` and didn't notice the word order needed changing


{% endraw %}
