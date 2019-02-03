---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/66476tipforfillinginholes.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [tip for filling in holes](https://leanprover-community.github.io/archive/113488general/66476tipforfillinginholes.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Apr 20 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tip%20for%20filling%20in%20holes/near/125425455):
<p>Sometimes in Lean you sit down to write a definition or a theorem, knowing that it will be really easy and fun. I was just in that situation. I need to write down some maps between localized rings and prove that they have some properties, but now I know that the localization interface is excellent and that pretty much every single one of my proofs will look like <code>name_of_function _ _ _ _ _</code>.</p>

#### [ Kevin Buzzard (Apr 20 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tip%20for%20filling%20in%20holes/near/125425597):
<p>However, I have run into an unexpected annoyance.</p>

#### [ Kevin Buzzard (Apr 20 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tip%20for%20filling%20in%20holes/near/125425716):
<p>Here is my skeleton set-up.</p>

#### [ Kevin Buzzard (Apr 20 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tip%20for%20filling%20in%20holes/near/125425811):
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">localization</span><span class="bp">.</span><span class="n">loc_loc_is_loc</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">{</span><span class="n">f</span> <span class="n">g</span> <span class="o">:</span> <span class="n">R</span><span class="o">}</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">Spec</span><span class="bp">.</span><span class="n">D&#39;</span> <span class="n">g</span> <span class="err">⊆</span> <span class="n">Spec</span><span class="bp">.</span><span class="n">D&#39;</span> <span class="n">f</span><span class="o">)</span> <span class="o">:</span>
<span class="o">(</span><span class="n">localization</span><span class="bp">.</span><span class="n">away</span> <span class="n">g</span><span class="o">)</span> <span class="err">≃ᵣ</span> <span class="n">localization</span><span class="bp">.</span><span class="n">away</span> <span class="o">(</span><span class="n">localization</span><span class="bp">.</span><span class="n">of_comm_ring</span> <span class="n">R</span> <span class="o">(</span><span class="n">powers</span> <span class="n">f</span><span class="o">)</span> <span class="n">g</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">to_fun</span> <span class="o">:=</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">inv_fun</span> <span class="o">:=</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">left_inv</span> <span class="o">:=</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">right_inv</span> <span class="o">:=</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">is_ring_hom</span> <span class="o">:=</span> <span class="bp">_</span>
<span class="o">}</span>
</pre></div>

#### [ Kevin Buzzard (Apr 20 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tip%20for%20filling%20in%20holes/near/125426022):
<p>The idea now is that I just fill in all the holes one by one.</p>

#### [ Kevin Buzzard (Apr 20 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tip%20for%20filling%20in%20holes/near/125426090):
<p>But I want the holes to have red squiggles under them!</p>

#### [ Kevin Buzzard (Apr 20 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tip%20for%20filling%20in%20holes/near/125426138):
<p>And for some reason, only the last one does</p>

#### [ Kevin Buzzard (Apr 20 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tip%20for%20filling%20in%20holes/near/125426449):
<p>and the associated complaint is full of metavariables</p>

#### [ Kevin Buzzard (Apr 20 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tip%20for%20filling%20in%20holes/near/125426465):
<p>because it depends on some earlier holes</p>

#### [ Kenny Lau (Apr 20 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tip%20for%20filling%20in%20holes/near/125426472):
<p>begin end</p>

#### [ Kevin Buzzard (Apr 20 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tip%20for%20filling%20in%20holes/near/125426501):
<p>and then remove it later?</p>

#### [ Kevin Buzzard (Apr 20 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tip%20for%20filling%20in%20holes/near/125426565):
<p>because it's a def</p>

#### [ Kenny Lau (Apr 20 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tip%20for%20filling%20in%20holes/near/125426587):
<p>i just fill in stuff in front of begin end</p>

#### [ Kenny Lau (Apr 20 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tip%20for%20filling%20in%20holes/near/125426641):
<p>I mean, replace your _ with begin end</p>

#### [ Kenny Lau (Apr 20 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tip%20for%20filling%20in%20holes/near/125426744):
<p>I can show you that in person next week ^^</p>

#### [ Kevin Buzzard (Apr 20 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tip%20for%20filling%20in%20holes/near/125426832):
<p><code>begin exact _ end</code></p>

#### [ Kevin Buzzard (Apr 20 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tip%20for%20filling%20in%20holes/near/125426834):
<p>:-)</p>

#### [ Kevin Buzzard (Apr 20 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tip%20for%20filling%20in%20holes/near/125426835):
<p>Many thanks Kenny!</p>

#### [ Kevin Buzzard (Apr 20 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tip%20for%20filling%20in%20holes/near/125427174):
<p>I feel like there are so many little tips like this, and it's unclear to me where they should be put.</p>

#### [ Kenny Lau (Apr 20 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tip%20for%20filling%20in%20holes/near/125427447):
<p>you don’t need exact _</p>


{% endraw %}
