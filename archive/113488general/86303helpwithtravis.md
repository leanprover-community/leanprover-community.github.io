---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/86303helpwithtravis.html
---

## Stream: [general](index.html)
### Topic: [help with travis](86303helpwithtravis.html)

---


{% raw %}
#### [ Scott Morrison (Oct 14 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/help%20with%20travis/near/135790347):
<p>Hmm, a strange error:</p>
<div class="codehilite"><pre><span></span>&gt; lean --make .
&gt; lean --make test
&gt; lean --recursive --export=mathlib.txt
&lt;unknown&gt;:1:1: error: invalid object declaration, environment already has an object named &#39;category_theory.limits.category_theory.limits.has_limits._proof_1&#39;
</pre></div>

#### [ Scott Morrison (Oct 14 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/help%20with%20travis/near/135790352):
<p>How come it doesn't complain with <code>lean --make</code>?</p>

#### [ Scott Morrison (Oct 14 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/help%20with%20travis/near/135790362):
<p>Is this that two files, which are never imported in the same place, have the same named definition? And this isn't detected until the last run of lean?</p>

#### [ Scott Morrison (Oct 14 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/help%20with%20travis/near/135790418):
<p>(Doesn't matter too much, there was an instance that should have been a def anyway, that should solve this.)</p>

#### [ Simon Hudon (Oct 14 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/help%20with%20travis/near/135790980):
<blockquote>
<p>Is this that two files, which are never imported in the same place, have the same named definition? And this isn't detected until the last run of lean?</p>
</blockquote>
<p>That's right</p>


{% endraw %}
