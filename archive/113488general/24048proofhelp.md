---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/24048proofhelp.html
---

## Stream: [general](index.html)
### Topic: [proof help](24048proofhelp.html)

---


{% raw %}
#### [ Scott Morrison (Oct 03 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20help/near/135084627):
<p>How does one prove <code>1 = n + 1 - n</code>, without getting your hands dirty? Do we have anything that can help with <code>nat.sub</code>?</p>

#### [ Johan Commelin (Oct 03 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20help/near/135084745):
<p>Can't <code>linarith</code> do these by now?</p>

#### [ Johan Commelin (Oct 03 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20help/near/135084815):
<div class="codehilite"><pre><span></span>git grep &quot;. + . - .&quot;
algebra/group.lean:  lemma add_sub_cancel&#39; (a b : α) : a + b - a = b :=
algebra/ring.lean:      ... ↔ a * e + c - b * e = d : iff.intro (λ h, begin simp [h] end) (λ h,
data/list/basic.lean:  reverse (range&#39; s n) = map (λ i, s + n - 1 - i) (range n)
data/multiset.lean:theorem add_sub_cancel_left (s : multiset α) : ∀ t, s + t - s = t :=
data/multiset.lean:theorem add_sub_cancel (s t : multiset α) : s + t - t = s :=
data/multiset.lean:by simpa [(∪), union, eq_comm] using show s + u - (t + u) = s - t,
data/nat/basic.lean:          ...     ≤ n + m - n      : nat.sub_le_sub_right this n
data/nat/prime.lean:    sqrt n - k &lt; sqrt n + 2 - k :=
data/nat/prime.lean:    λ _ _, `[exact ⟨_, measure_wf (λ k, sqrt n + 2 - k)⟩]}
data/nat/prime.lean:    λ _ _, `[exact ⟨_, measure_wf (λ k, sqrt n + 2 - k)⟩]}
data/padics/padic_norm.lean:   padic_norm hp q = padic_norm hp (q + r - r) : by congr; ring
data/padics/padic_rationals.lean:    show lim_zero (f + g - g), by simpa using hf },
data/padics/padic_rationals.lean:    show lim_zero (f + g - f), by  simpa [add_sub_cancel&#39;] using hg },
docs/naming.md:pattern. For that, we make do as best we can. For example, `a + b - b = a`
group_theory/subgroup.lean:(normal : ∀ n ∈ s, ∀ g : α, g + n - g ∈ s)
set_theory/ordinal.lean:theorem add_sub_cancel (a b : ordinal) : a + b - a = b :=
set_theory/ordinal.lean:theorem add_sub_add_cancel (a b c : ordinal) : a + b - (a + c) = b - c :=
tests/linarith.lean:        (h4 : a + b - c &lt; 3)  : false :=
tests/linarith.lean:example (a b c : ℚ) (h2 : (2 : ℚ) &gt; 3)  : a + b - c ≥ 3 :=
tests/ring.lean:example {α} [comm_ring α] (x y : α) : x + y + y - x = 2 * y := by ring
</pre></div>

#### [ Scott Morrison (Oct 03 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20help/near/135084854):
<p>No, linarith doesn't help.</p>

#### [ Johan Commelin (Oct 03 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20help/near/135084859):
<p>Or even better:</p>
<div class="codehilite"><pre><span></span>git grep &quot;. + . - .&quot; | grep nat
data/nat/basic.lean:          ...     ≤ n + m - n      : nat.sub_le_sub_right this n
data/nat/prime.lean:    sqrt n - k &lt; sqrt n + 2 - k :=
data/nat/prime.lean:    λ _ _, `[exact ⟨_, measure_wf (λ k, sqrt n + 2 - k)⟩]}
data/nat/prime.lean:    λ _ _, `[exact ⟨_, measure_wf (λ k, sqrt n + 2 - k)⟩]}
</pre></div>

#### [ Scott Morrison (Oct 03 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20help/near/135084861):
<p>For it to deal with subtraction on natural numbers it would have to break into cases.</p>

#### [ Johan Commelin (Oct 03 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20help/near/135084866):
<p>That first result looks promising</p>

#### [ Johan Commelin (Oct 03 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20help/near/135084876):
<p><code>nat.add_sub_cancel_left</code></p>

#### [ Johan Commelin (Oct 03 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20help/near/135084877):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> Is <span class="emoji emoji-2b06" title="up">:up:</span> what you need?</p>

#### [ Scott Morrison (Oct 03 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20help/near/135084922):
<p>Yeah, but even that requires using commutativity of addition first.</p>

#### [ Scott Morrison (Oct 03 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20help/near/135084926):
<p>Too gross for me. :-)</p>

#### [ Johan Commelin (Oct 03 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20help/near/135084986):
<p>They don't need that over here:</p>
<div class="codehilite"><pre><span></span>git grep -A1 &quot;. + . - .&quot; | grep -A1 nat | head -2
data/nat/basic.lean:          ...     ≤ n + m - n      : nat.sub_le_sub_right this n
data/nat/basic.lean-          ...     = m              : by rw nat.add_sub_cancel_left,
</pre></div>

#### [ Johan Commelin (Oct 03 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20help/near/135084992):
<p>Seems like <code>rw</code> will do the job.</p>

#### [ Kevin Buzzard (Oct 03 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20help/near/135085692):
<p>All of these lemmas are in Lean or mathlib I think. I've extensively used subtraction on nats and am not aware of any holes.</p>


{% endraw %}
