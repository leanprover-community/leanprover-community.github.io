---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/84032Provinglemmawithoutdoingpatternmatching.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Proving lemma without doing pattern matching](https://leanprover-community.github.io/archive/113488general/84032Provinglemmawithoutdoingpatternmatching.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ petercommand (Jan 14 2019 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proving%20lemma%20without%20doing%20pattern%20matching/near/155091905):
<div class="codehilite"><pre><span></span>lemma eq.subst&#39; {α : Sort u} {a b : α} {P : Π (m: α), (m = a) ∨ (m = b) → Prop}
    (h₁ : a = b) (h₂ : P a (or.inl rfl)) : P b (or.inr rfl) := by cases h₁; assumption
</pre></div>


<p>Is it possible to prove this lemma with eliminators without doing pattern matching?</p>

#### [ petercommand (Jan 14 2019 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proving%20lemma%20without%20doing%20pattern%20matching/near/155091997):
<p>In this example, I am trying to prove a variant of the traditional Leibniz equality (subst)</p>

#### [ Patrick Massot (Jan 14 2019 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proving%20lemma%20without%20doing%20pattern%20matching/near/155092468):
<p>Of course it's possible, this is what Lean does in the end. You can <code>#print eq.subst'</code>. Or am I missing something?</p>

#### [ petercommand (Jan 14 2019 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proving%20lemma%20without%20doing%20pattern%20matching/near/155094669):
<p>You are right, it's just that I need to <code>set_option pp.implicit true</code> before <code>#print eq.subst'</code></p>

#### [ petercommand (Jan 14 2019 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proving%20lemma%20without%20doing%20pattern%20matching/near/155094961):
<p>I thought the generated program doesn't typecheck</p>

#### [ Patrick Massot (Jan 16 2019 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proving%20lemma%20without%20doing%20pattern%20matching/near/155271925):
<p>(deleted)</p>


{% endraw %}
