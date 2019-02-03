---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/10846RFCoperatornorm.html
---

## Stream: [new members](index.html)
### Topic: [RFC: operator norm](10846RFCoperatornorm.html)

---


{% raw %}
#### [ Jan-David Salchow (Dec 28 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/RFC%3A%20operator%20norm/near/152676704):
<p>I've been playing with the space of bounded linear maps between normed space, see <a href="https://github.com/jdsalchow/mathlib/blob/calculus/analysis/functional/operator_norm.lean" target="_blank" title="https://github.com/jdsalchow/mathlib/blob/calculus/analysis/functional/operator_norm.lean">https://github.com/jdsalchow/mathlib/blob/calculus/analysis/functional/operator_norm.lean</a></p>
<p>Before splitting this up into smaller pieces and creating a PR, I thought I better ask for comments. So, comments anybody?</p>

#### [ Kevin Buzzard (Dec 29 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/RFC%3A%20operator%20norm/near/152679652):
<p><code>local attribute[instance] classical.prop_decidable</code> -- people often go for <code>local attribute [instance, priority 0] classical.prop_decidable</code> nowadays because it is less likely to break proofs that actually rely on decidability. This might well not be an issue in this code though.</p>

#### [ Jan-David Salchow (Dec 29 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/RFC%3A%20operator%20norm/near/152699240):
<p>Is there a way to forget a local attribute when it's not needed anymore?</p>

#### [ Chris Hughes (Dec 29 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/RFC%3A%20operator%20norm/near/152699337):
<p>put it inside a section</p>


{% endraw %}
