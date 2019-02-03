---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/49265alternativedefinitionoflistisprefix.html
---

## Stream: [general](index.html)
### Topic: [alternative definition of list.is_prefix](49265alternativedefinitionoflistisprefix.html)

---


{% raw %}
#### [ Kenny Lau (Apr 19 2018 at 05:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/alternative%20definition%20of%20list.is_prefix/near/125285727):
<p>Could we have a subtype instead of an existential here, as the data is lost in the latter?</p>

#### [ Kenny Lau (Apr 19 2018 at 05:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/alternative%20definition%20of%20list.is_prefix/near/125285728):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span></p>

#### [ Mario Carneiro (Apr 19 2018 at 05:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/alternative%20definition%20of%20list.is_prefix/near/125285742):
<p>the data isn't lost, you can recover it by dropping the first <code>n</code> elements of the larger list</p>

#### [ Mario Carneiro (Apr 19 2018 at 05:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/alternative%20definition%20of%20list.is_prefix/near/125285743):
<p>where <code>n</code> is the length of the smaller list</p>

#### [ Kenny Lau (Apr 19 2018 at 05:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/alternative%20definition%20of%20list.is_prefix/near/125285744):
<p>right, but has this been done in mathlib?</p>

#### [ Mario Carneiro (Apr 19 2018 at 05:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/alternative%20definition%20of%20list.is_prefix/near/125285745):
<p>The existential is used because I want it to be a prop</p>

#### [ Kenny Lau (Apr 19 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/alternative%20definition%20of%20list.is_prefix/near/125285784):
<p>I mean, the choice function for this existential isn't in mathlib</p>

#### [ Mario Carneiro (Apr 19 2018 at 05:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/alternative%20definition%20of%20list.is_prefix/near/125286245):
<div class="codehilite"><pre><span></span>theorem prefix_iff_eq_append (l₁ l₂ : list α) : l₁ &lt;+: l₂ ↔ l₁ ++ drop (length l₁) l₂ = l₂ :=
⟨λ h, let ⟨r, e⟩ := h in begin
  rwa append_inj_right ((take_append_drop (length l₁) l₂).trans e.symm) _,
  simp [min_eq_left, length_le_of_sublist (sublist_of_prefix h)],
end, λ e, ⟨_, e⟩⟩

theorem suffix_iff_eq_append (l₁ l₂ : list α) : l₁ &lt;:+ l₂ ↔ take (length l₂ - length l₁) l₂ ++ l₁ = l₂ :=
⟨λ ⟨r, e⟩, begin
  rwa append_inj_left ((take_append_drop (length l₂ - length l₁) l₂).trans e.symm) _,
  simp [min_eq_left, nat.sub_le, e.symm],
  apply nat.add_sub_cancel_left
end, λ e, ⟨_, e⟩⟩
</pre></div>


{% endraw %}
