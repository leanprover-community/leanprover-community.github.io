---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/66487TypevsType.html
---

## Stream: [general](index.html)
### Topic: [Type* vs Type _](66487TypevsType.html)

---


{% raw %}
#### [ Patrick Massot (Apr 26 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Type%2A%20vs%20Type%20_/near/125719177):
<p>What's the difference between <code>(a: Type*)</code> and <code>(a: Type _)</code>?</p>

#### [ Gabriel Ebner (Apr 26 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Type%2A%20vs%20Type%20_/near/125719646):
<p>They both mean the same as <code>(a: Sort (_+1))</code> and <code>(a: Type.{_})</code>.</p>

#### [ Patrick Massot (Apr 26 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Type%2A%20vs%20Type%20_/near/125719765):
<p>So, we have lots of ways to confuse new users...</p>

#### [ Kevin Buzzard (Apr 26 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Type%2A%20vs%20Type%20_/near/125732578):
<p>On the other hand I ran into an example recently where just calling things "Type u", "Type v", "Type w"... seemed to have a different effect to calling them all "Type *". I hope I starred that post because I thought it was worth following up and I didn't do it at the time...</p>

#### [ Kevin Buzzard (Apr 26 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Type%2A%20vs%20Type%20_/near/125732658):
<p><a href="#narrow/stream/113488-general/topic/universe.20issues" title="#narrow/stream/113488-general/topic/universe.20issues">https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/universe.20issues</a></p>

#### [ Kevin Buzzard (Apr 26 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Type%2A%20vs%20Type%20_/near/125732669):
<p>Me being burned by <code>Type *</code></p>

#### [ Patrick Massot (Apr 26 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Type%2A%20vs%20Type%20_/near/125732683):
<p>I can tell you another example: the group instance on <code>perm X</code></p>

#### [ Patrick Massot (Apr 26 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Type%2A%20vs%20Type%20_/near/125732729):
<p>But this is orthogonal to my question</p>

#### [ Sean Leather (Apr 27 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Type%2A%20vs%20Type%20_/near/125780058):
<blockquote>
<p>But this is orthogonal to my question</p>
</blockquote>
<p>I would say it's more of a footnote (<code>*</code>) to your question.</p>


{% endraw %}
