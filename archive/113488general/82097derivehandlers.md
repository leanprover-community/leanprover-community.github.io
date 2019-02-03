---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/82097derivehandlers.html
---

## Stream: [general](index.html)
### Topic: [derive handlers](82097derivehandlers.html)

---


{% raw %}
#### [ Simon Hudon (Aug 31 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/derive%20handlers/near/133148060):
<p>I'm writing a derive handler,  and while testing it on my third example, I get the following error:</p>
<div class="codehilite"><pre><span></span>declaration contains macro with trust-level higher than the one allowed (possible solution: unfold macro, or increase trust-level)
</pre></div>


<p>But the term that my handler produces contains no macros that I can see (I'm using <code>expr.fold</code> to enumerate them). Has anyone seen this before?</p>

#### [ Simon Hudon (Aug 31 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/derive%20handlers/near/133148298):
<p>Update: I checked a part of the derived term which produces <code>perm_ac</code> and <code>ac_app</code></p>

#### [ Simon Hudon (Aug 31 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/derive%20handlers/near/133149243):
<p>Update 2: I wrote a tactic <code>expand_untrusted</code> that takes care of those macros. It solves the problem. I'm surprised <code>instance_derive_handler</code> doesn't do that by default</p>


{% endraw %}
