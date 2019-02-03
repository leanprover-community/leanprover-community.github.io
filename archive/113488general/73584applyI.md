---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/73584applyI.html
---

## Stream: [general](index.html)
### Topic: [applyI](73584applyI.html)

---


{% raw %}
#### [ Reid Barton (Sep 07 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/applyI/near/133495991):
<p>Is there a variant on apply or refine which turns <code>[...]</code> arguments which couldn't be solved into new goals?</p>

#### [ Simon Hudon (Sep 07 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/applyI/near/133496017):
<p>What are <code>[...]</code> arguments?</p>

#### [ Reid Barton (Sep 07 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/applyI/near/133496109):
<p>Class arguments</p>

#### [ Reid Barton (Sep 07 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/applyI/near/133496113):
<p>Or instances rather</p>

#### [ Johannes Hölzl (Sep 07 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/applyI/near/133496114):
<p><code>apply_with</code> allows you to provide a <code>apply_cfg</code> structure. I think <code>{ instances := ff }</code>should add them to the goals.</p>

#### [ Reid Barton (Sep 07 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/applyI/near/133496119):
<p>Ooh</p>

#### [ Reid Barton (Sep 07 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/applyI/near/133496402):
<p>Yes, it worked.</p>

#### [ Kevin Buzzard (Sep 07 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/applyI/near/133498215):
<p>Does <code>convert</code> work? I'm a big convert to <code>convert</code>. It seems to allow me to write proofs forwards like a mathematician would. "This term is actually the answer; I'll now pick up the pieces".</p>

#### [ Reid Barton (Sep 07 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/applyI/near/133498553):
<p>Huh, it does!</p>

#### [ Reid Barton (Sep 07 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/applyI/near/133498721):
<p>That's really good to know--I already wrote a couple "backwards" proofs involving instances (which I think are really forwards, in the sense that you are building up new known statements from old ones, rather than breaking down the goal) and I was annoyed that I couldn't write them in the normal fashion.</p>

#### [ Kevin Buzzard (Sep 07 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/applyI/near/133498749):
<p>How long has <code>convert</code> existed? I can't believe I didn't notice it wasn't there. I only found it was there about a week ago and now I kind of feel stupid that I hadn't realised that I wanted it.</p>

#### [ Reid Barton (Sep 07 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/applyI/near/133498793):
<p>For example</p>
<div class="codehilite"><pre><span></span><span class="k">begin</span>
  <span class="n">letI</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="n">K</span> <span class="err">↝</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">),</span> <span class="n">is_iso</span> <span class="o">(</span><span class="n">colimit</span><span class="bp">.</span><span class="n">pre</span> <span class="n">A</span> <span class="o">(</span><span class="n">F</span><span class="bp">.</span><span class="n">comp</span> <span class="n">G</span><span class="o">))</span> <span class="o">:=</span>
  <span class="k">begin</span> <span class="n">intro</span> <span class="n">A</span><span class="o">,</span> <span class="n">rw</span> <span class="n">colimit</span><span class="bp">.</span><span class="n">pre_comp</span><span class="o">,</span> <span class="n">apply_instance</span><span class="o">,</span> <span class="kn">end</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">is_cofinal_of_induced_is_iso</span>
<span class="kn">end</span>
</pre></div>


<p>is now</p>
<div class="codehilite"><pre><span></span><span class="k">begin</span>
  <span class="n">convert</span> <span class="n">is_cofinal_of_induced_is_iso</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">intro</span> <span class="n">A</span><span class="o">,</span> <span class="n">rw</span> <span class="n">colimit</span><span class="bp">.</span><span class="n">pre_comp</span><span class="o">,</span> <span class="n">apply_instance</span>
<span class="kn">end</span>
</pre></div>

#### [ Johan Commelin (Sep 07 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/applyI/near/133498834):
<p><a href="#narrow/stream/116395-maths/subject/ZFC.20equality/near/127216190" title="#narrow/stream/116395-maths/subject/ZFC.20equality/near/127216190">https://leanprover.zulipchat.com/#narrow/stream/116395-maths/subject/ZFC.20equality/near/127216190</a><br>
We need better documentation!</p>

#### [ Reid Barton (Sep 07 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/applyI/near/133498835):
<p>April<br>
<a href="#narrow/stream/113488-general/subject/apply.20with.20new.20equality.20goals/near/125558382" title="#narrow/stream/113488-general/subject/apply.20with.20new.20equality.20goals/near/125558382">https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/apply.20with.20new.20equality.20goals/near/125558382</a></p>

#### [ Reid Barton (Sep 07 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/applyI/near/133502820):
<p>Maybe it would still be good to have an <code>applyI</code> tactic which is just <code>apply</code> with <code>{ instances := ff }</code>, though.</p>

#### [ Kenny Lau (Sep 07 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/applyI/near/133503124):
<p>maybe we should have 32768 names for our 15 boolean configurations of <code>simp</code></p>

#### [ Patrick Massot (Sep 07 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/applyI/near/133503487):
<p>Indeed I would love to read more examples of using convert.</p>


{% endraw %}
