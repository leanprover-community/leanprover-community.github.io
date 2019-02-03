---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/50743autoparamininstance.html
---

## Stream: [general](index.html)
### Topic: [autoparam in instance](50743autoparamininstance.html)

---


{% raw %}
#### [ Patrick Massot (Dec 18 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/autoparam%20in%20instance/near/152102423):
<p>Is it possible to use autoparam in instances? I have a <code>is_add_group_hom</code> instance that never triggers, probably because is it contains a continuity assumption. The following doesn't seem to help:</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">sep_quot</span><span class="bp">.</span><span class="n">is_add_group_hom_lift</span> <span class="o">[</span><span class="n">separated</span> <span class="n">β</span><span class="o">]</span>  <span class="o">(</span><span class="n">hf</span> <span class="o">:</span> <span class="n">continuous</span> <span class="n">f</span> <span class="bp">.</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">assumption</span><span class="o">)</span> <span class="o">:</span> <span class="n">is_add_group_hom</span> <span class="o">(</span><span class="n">sep_quot</span><span class="bp">.</span><span class="n">lift</span> <span class="n">f</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">...</span>
</pre></div>

#### [ Johan Commelin (Dec 18 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/autoparam%20in%20instance/near/152102640):
<p>Isn't this evidence that <code>continuous</code> should be a class?</p>

#### [ Patrick Massot (Dec 18 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/autoparam%20in%20instance/near/152102647):
<p>Of course this also came to my mind</p>

#### [ Patrick Massot (Dec 18 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/autoparam%20in%20instance/near/152102650):
<p>Here it would clearly help</p>

#### [ Johan Commelin (Dec 18 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/autoparam%20in%20instance/near/152102776):
<p>/me doesn't know why group homs should be a class and continuous maps not...</p>

#### [ Gabriel Ebner (Dec 18 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/autoparam%20in%20instance/near/152102875):
<blockquote>
<p>Is it possible to use autoparam in instances?</p>
</blockquote>
<p>No, auto_params are handled by the elaborator.  Type class instance synthesis does not know about auto_param (or optional parameters).</p>

#### [ Patrick Massot (Dec 18 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/autoparam%20in%20instance/near/152102895):
<p>Thanks Gabriel</p>

#### [ Kenny Lau (Dec 18 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/autoparam%20in%20instance/near/152104969):
<p>neither should be a class</p>

#### [ Kenny Lau (Dec 18 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/autoparam%20in%20instance/near/152104973):
<p>not group homs. not continuous maps. not linear maps.</p>

#### [ Johan Commelin (Dec 18 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/autoparam%20in%20instance/near/152105038):
<p>So... what <em>should</em> be a class?</p>

#### [ Kenny Lau (Dec 18 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/autoparam%20in%20instance/near/152105320):
<p>groups and topological spaces and modules?</p>

#### [ Johan Commelin (Dec 18 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/autoparam%20in%20instance/near/152105378):
<p>Why???</p>

#### [ Kenny Lau (Dec 18 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/autoparam%20in%20instance/near/152105431):
<p>how is it done in your category theory?</p>

#### [ Kevin Buzzard (Dec 18 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/autoparam%20in%20instance/near/152106769):
<p>Continuous maps not a class -- Johannes has explained this before on this forum, although I have never really internalised the issue.</p>


{% endraw %}
