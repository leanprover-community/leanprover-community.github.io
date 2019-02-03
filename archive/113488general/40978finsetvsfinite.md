---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/40978finsetvsfinite.html
---

## Stream: [general](index.html)
### Topic: [finset vs finite](40978finsetvsfinite.html)

---


{% raw %}
#### [ Johan Commelin (Sep 28 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20vs%20finite/near/134824142):
<p>What are the pros and cons of finset vs finite? I'm quite confused how to move back and forth between the two. Related: Should there be a lemma that every set of a fintype is finite? Maybe it is even there, but I couldn't find it.</p>

#### [ Johan Commelin (Sep 28 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20vs%20finite/near/134824963):
<p>Aaah, <code>finite_mem_finset</code> can help me.</p>

#### [ Rob Lewis (Jan 31 2019 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20vs%20finite/near/157307967):
<p>I just found this looking for an answer to my question, which is basically the same as Johan's from September: is there a canonical way to carve a <code>finset</code> out of a <code>fintype</code>? Something like <code>def sep {α} [fintype α] (P : α → Prop) : finset α</code>?</p>

#### [ Johannes Hölzl (Jan 31 2019 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20vs%20finite/near/157308046):
<p>Currently we only have <code>finset.univ.filter</code></p>

#### [ Kenny Lau (Jan 31 2019 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20vs%20finite/near/157308048):
<p>finset.univ.filter</p>

#### [ Rob Lewis (Jan 31 2019 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finset%20vs%20finite/near/157308110):
<p>That'll work, thanks.</p>


{% endraw %}
