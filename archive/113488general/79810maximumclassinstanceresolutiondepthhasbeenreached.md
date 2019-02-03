---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/79810maximumclassinstanceresolutiondepthhasbeenreached.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [maximum class-instance resolution depth has been reached](https://leanprover-community.github.io/archive/113488general/79810maximumclassinstanceresolutiondepthhasbeenreached.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Apr 24 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627176):
<p>I was writing some random universal property code</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627183):
<p>and I got the good old "maximum class-instance resolution depth has been reached" error</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627184):
<p>and we all know what that means</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627185):
<p>so I restarted Lean</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627186):
<p>and I got the error again.</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627188):
<p><em>sigh</em></p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627192):
<p>so I guess I know what that means</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627194):
<p>and I decided I'd made some sort of error with my types</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627201):
<p>so I carefully wrote down the types of everything in my statement</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627202):
<p>and managed to make sure that everything really had the type I thought it would have</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627203):
<p>and I restarted Lean</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627207):
<p>and I got the error again.</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627208):
<p><em>sigh</em></p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627212):
<p>The error in its Lean 3.4 form says</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627217):
<div class="codehilite"><pre><span></span>maximum class-instance resolution depth has been reached (the limit can be increased by setting option &#39;class.instance_max_depth&#39;) (the class-instance resolution trace can be visualized by setting option &#39;trace.class_instances&#39;)
</pre></div>

#### [ Kevin Buzzard (Apr 24 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627263):
<p>so I figured that it was about time I read the error properly</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627272):
<p>and I realised it was hard for me to increase the max_depth</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627275):
<p>because I didn't know what it currently was</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627285):
<p>so I looked at the trace</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627288):
<p>and it was really long</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627290):
<p>and complicated</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627294):
<p>and I spent some time trying to understand it</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627301):
<p>and in total spent over half an hour on this issue</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627302):
<p>before it occurred to me</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627304):
<p>that actually</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627307):
<p>maybe</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627313):
<p>the maximum class-instance resolution depth <em>had</em> been reached!</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627325):
<p>So I wrote <code>set_option class.instance_max_depth 100</code></p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627326):
<p>and the error went away!</p>

#### [ Kenny Lau (Apr 24 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627387):
<p>lol</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627390):
<p>So I came to the conclusion</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627397):
<p>that either my code is really really cool and I am using type class resolution like a pro now</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627398):
<p>or</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627399):
<p>maybe my code is really really bad</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627428):
<p>and anyone who needs to change the default setting of the max class-instance resolution might want to take a look at what they're doing and how they're doing it.</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627491):
<p>And one thing that occured to me was that I might be being sloppy with the difference between proofs and data</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627503):
<p>but this might not be relevant, I'm not sure.</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627506):
<p>Here's a structure:</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627513):
<div class="codehilite"><pre><span></span><span class="c1">-- Here is the way KMB wants to package all these things together.</span>
<span class="kn">structure</span> <span class="n">is_unique_R_alg_hom</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">w</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">β</span><span class="o">]</span>
<span class="o">(</span><span class="n">sα</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">sβ</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">sα</span><span class="o">]</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">sβ</span><span class="o">]</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">f</span><span class="o">]</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">R_alg_hom</span> <span class="o">:</span> <span class="n">sβ</span> <span class="bp">=</span> <span class="n">f</span> <span class="err">∘</span> <span class="n">sα</span><span class="o">)</span>
<span class="o">(</span><span class="n">is_unique</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">g</span><span class="o">],</span> <span class="n">sβ</span> <span class="bp">=</span> <span class="n">g</span> <span class="err">∘</span> <span class="n">sα</span> <span class="bp">→</span> <span class="n">g</span> <span class="bp">=</span> <span class="n">f</span><span class="o">)</span>
</pre></div>

#### [ Kevin Buzzard (Apr 24 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627516):
<p>You make an instance of that structure by giving two proofs.</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627567):
<p>But the structure turns out to be a Type.</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627576):
<p>I could have rewritten this as <code>is_unique_R_alg_hom blah := proof1 and proof2</code></p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627579):
<p>and then it would be a Prop.</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627604):
<p>Should I change this, or does it not make a difference to anything?</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627619):
<p>And is it completely unrelated to the max class-instance resolution?</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627672):
<p>Oh I seem to just be able to make the structure a Prop anyway</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627773):
<p>aah, and now I don't need <code>set_option class.instance_max_depth 52</code> (for 52 was the min to make it work)</p>

#### [ Chris Hughes (Apr 24 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627776):
<p>Probably best to make it a Prop, to avoid issues with not recognizing that two instances of the same thing are equal.</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627779):
<p>because I seem to have forgotten things</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627801):
<p>Whyever would Lean make a structure whose constructor involved giving two proofs into a type??</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627865):
<p>Probably also best to make it into a Prop, because then I don't need to change a max depth to 52</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627989):
<p>no, the error is back</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125627992):
<p>I am still getting used to new lean in VS Code</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125628001):
<p>OK so my question remains</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125628044):
<div class="codehilite"><pre><span></span><span class="kn">set_option</span> <span class="n">class</span><span class="bp">.</span><span class="n">instance_max_depth</span> <span class="mi">52</span> <span class="c1">-- !!</span>
<span class="c">/-</span><span class="cm">- universal property of inverting one element and then another -/</span>
<span class="kn">theorem</span> <span class="n">away_away_universal_property</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">R</span><span class="o">)</span>
<span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">loc</span> <span class="n">R</span> <span class="o">(</span><span class="n">powers</span> <span class="n">f</span><span class="o">))</span> <span class="o">{</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">γ</span><span class="o">]</span> <span class="o">(</span><span class="n">sγ</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">)</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">sγ</span><span class="o">]</span> <span class="o">(</span><span class="n">Hf</span> <span class="o">:</span> <span class="n">is_unit</span> <span class="o">(</span><span class="n">sγ</span> <span class="n">f</span><span class="o">))</span>
<span class="o">(</span><span class="n">Hg</span> <span class="o">:</span> <span class="n">is_unit</span> <span class="o">(</span><span class="n">away</span><span class="bp">.</span><span class="n">extend_map_of_im_unit</span> <span class="n">sγ</span> <span class="n">Hf</span> <span class="n">g</span><span class="o">))</span> <span class="o">:</span>
<span class="n">is_unique_R_alg_hom</span>
  <span class="o">((</span><span class="n">of_comm_ring</span> <span class="o">(</span><span class="n">loc</span> <span class="n">R</span> <span class="o">(</span><span class="n">powers</span> <span class="n">f</span><span class="o">))</span> <span class="o">(</span><span class="n">powers</span> <span class="n">g</span><span class="o">))</span> <span class="err">∘</span> <span class="o">(</span><span class="n">of_comm_ring</span> <span class="n">R</span> <span class="o">(</span><span class="n">powers</span> <span class="n">f</span><span class="o">)))</span>
  <span class="n">sγ</span>
  <span class="o">(</span><span class="n">away</span><span class="bp">.</span><span class="n">extend_map_of_im_unit</span> <span class="o">(</span><span class="n">away</span><span class="bp">.</span><span class="n">extend_map_of_im_unit</span> <span class="n">sγ</span> <span class="n">Hf</span><span class="o">)</span> <span class="n">Hg</span><span class="o">)</span>
    <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Kevin Buzzard (Apr 24 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125628048):
<p>Is that first line evidence that I am doing something wrong?</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125628155):
<p>If I <code>set_option trace.class_instances true</code></p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125628159):
<p>then I get things like <a href="https://gist.github.com/kbuzzard/2a135ef1486fc55c3b4c70ca11cf50b4" target="_blank" title="https://gist.github.com/kbuzzard/2a135ef1486fc55c3b4c70ca11cf50b4">https://gist.github.com/kbuzzard/2a135ef1486fc55c3b4c70ca11cf50b4</a></p>

#### [ Chris Hughes (Apr 24 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125628161):
<p>How deep do you have to go if you try to do type class inference by hand? Maybe it's just a really hard type class inference problem, that requires that depth?</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125628162):
<p>I don't think it's hard</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125628205):
<p>I compose two ring homomorphisms</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125628209):
<p>and I want the result to be a ring homomorphism</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125628238):
<p>It's difficult to know where the exact problem is</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125628251):
<p>because when I set trace.class_instances true pretty much everything gets underlined in green</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125628255):
<p>and if I let it be 51</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125628305):
<p>then the name of the theorem gets underlined in red</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125628350):
<p>The biggest number I can find in brackets is (14)</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125628352):
<div class="codehilite"><pre><span></span>[class_instances] (14) ?x_314 : discrete_linear_ordered_field R := rat.discrete_linear_ordered_field
</pre></div>

#### [ Kevin Buzzard (Apr 24 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125628356):
<p>the mind boggles</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125628401):
<p>why is Lean wondering if my ring is a discrete linear ordered field?</p>

#### [ Andrew Ashworth (Apr 24 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125631291):
<p>because type class instance search is really dumb,  it's basically searching the graph of all paths that might reach your proof</p>

#### [ Andrew Ashworth (Apr 24 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125631353):
<p>the more definitions and lemmas that you use with nested type class arguments, the bigger you'll need to set the search depth to</p>

#### [ Kevin Buzzard (Apr 24 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125631548):
<p>So are you saying that there is a non-zero chance that I might actually have to set the search depth to 52 and this doesn't just mean that my code is crappy?</p>

#### [ Andrew Ashworth (Apr 24 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125631768):
<p>in most cs applications the type class tree search is going to be somewhat shallow</p>

#### [ Kevin Buzzard (Apr 24 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125631782):
<p>I am pushing it</p>

#### [ Kevin Buzzard (Apr 24 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125631784):
<p>but I didn't realise I was pushing that hard</p>

#### [ Andrew Ashworth (Apr 24 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125631789):
<p>if you think it's going to be super deep, i wouldn't use type class search</p>

#### [ Kevin Buzzard (Apr 24 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125631794):
<p>I didn't think it was going to be super deep</p>

#### [ Kevin Buzzard (Apr 24 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125631798):
<p>I am surprised that I need 52</p>

#### [ Kevin Buzzard (Apr 24 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125631847):
<p>in the sense that I thought that all I was doing was trying to get Lean to spot that (a) the output of some function is a ring homomorphism and (b) the composite of two ring homomorphisms is a ring homomorphism</p>

#### [ Kevin Buzzard (Apr 24 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125631852):
<p>I don't understand how to find out where the pushing is occurring</p>

#### [ Reid Barton (Apr 24 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125631853):
<p>I wonder whether you actually need 52, or it's going off in some other unsuccessful part of the search that needs depth 52</p>

#### [ Kevin Buzzard (Apr 24 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125631856):
<p>I don't know how to find out</p>

#### [ Reid Barton (Apr 24 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125631861):
<p>Me neither</p>

#### [ Kevin Buzzard (Apr 24 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125631863):
<p>I put the debugging on and am immediately swimming in output</p>

#### [ Patrick Massot (Apr 24 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125632444):
<p>Maybe have a look at <a href="https://github.com/leanprover/mathlib/blob/master/data/real/basic.lean#L74" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/data/real/basic.lean#L74">https://github.com/leanprover/mathlib/blob/master/data/real/basic.lean#L74</a></p>

#### [ Patrick Massot (Apr 24 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125632453):
<p>Sometimes you can help the type class resolution algorithm</p>

#### [ Patrick Massot (Apr 24 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125632460):
<p>By precomputing some shortcut</p>

#### [ Patrick Massot (Apr 24 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125632465):
<p>I have no idea if this applies in your case</p>

#### [ Mario Carneiro (Apr 24 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125632645):
<p>Do you have something I can test here myself?</p>

#### [ Kevin Buzzard (Apr 24 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125633311):
<p>I have a MWE but it didn't need 52</p>

#### [ Kevin Buzzard (Apr 24 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125633314):
<p>:P</p>

#### [ Kevin Buzzard (Apr 24 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125633460):
<p>I can point you to a theorem in lean-stacks-project if that's what you mean</p>

#### [ Kevin Buzzard (Apr 24 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125633469):
<p>line 138 of tag01HR.lean</p>

#### [ Kevin Buzzard (Apr 24 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125633498):
<p><a href="https://github.com/kbuzzard/lean-stacks-project" target="_blank" title="https://github.com/kbuzzard/lean-stacks-project">https://github.com/kbuzzard/lean-stacks-project</a></p>

#### [ Kevin Buzzard (Apr 24 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125633510):
<p>wait</p>

#### [ Kevin Buzzard (Apr 24 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125633511):
<p>I need to push</p>

#### [ Kevin Buzzard (Apr 24 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125633590):
<p><a href="https://github.com/kbuzzard/lean-stacks-project/blob/179ff95b6bd8d4998e1a007b2e8942179d9e24a8/src/tag01HR.lean#L138" target="_blank" title="https://github.com/kbuzzard/lean-stacks-project/blob/179ff95b6bd8d4998e1a007b2e8942179d9e24a8/src/tag01HR.lean#L138">https://github.com/kbuzzard/lean-stacks-project/blob/179ff95b6bd8d4998e1a007b2e8942179d9e24a8/src/tag01HR.lean#L138</a></p>

#### [ Kevin Buzzard (Apr 24 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125633753):
<p>Thanks for pointing that out Patrick. I don't know if this applies in my situation because I have no idea what the problem is. I didn't think I was doing anything too weird.</p>

#### [ Kevin Buzzard (Apr 24 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125633780):
<p>PS <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I commented everything out from line 171 onwards (I mention this because it's not so easy to spot in VS Code)</p>

#### [ Mario Carneiro (Apr 24 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125637889):
<p>By the way another way to comment everything out after a certain point is <code>#exit</code>, which also causes a notification so it's not so hard to spot</p>

#### [ Kevin Buzzard (Apr 25 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125643878):
<p>woohoo</p>

#### [ Kevin Buzzard (Apr 25 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125643888):
<p>new record</p>

#### [ Kevin Buzzard (Apr 25 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125643894):
<div class="codehilite"><pre><span></span><span class="n">noncomputable</span> <span class="kn">definition</span> <span class="n">loc_is_loc_loc</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="n">g</span> <span class="o">:</span> <span class="n">R</span><span class="o">)</span> <span class="o">:</span>
<span class="n">R_alg_equiv</span>
  <span class="o">((</span><span class="n">of_comm_ring</span> <span class="o">(</span><span class="n">loc</span> <span class="n">R</span> <span class="o">(</span><span class="n">powers</span> <span class="n">f</span><span class="o">))</span> <span class="o">(</span><span class="n">powers</span> <span class="o">(</span><span class="n">of_comm_ring</span> <span class="n">R</span> <span class="o">(</span><span class="n">powers</span> <span class="n">f</span><span class="o">)</span> <span class="n">g</span><span class="o">)))</span>
  <span class="err">∘</span> <span class="o">(</span><span class="n">of_comm_ring</span> <span class="n">R</span> <span class="o">(</span><span class="n">powers</span> <span class="n">f</span><span class="o">)))</span>
  <span class="o">(</span><span class="n">of_comm_ring</span> <span class="n">R</span> <span class="o">(</span><span class="n">powers</span> <span class="o">(</span><span class="n">f</span> <span class="bp">*</span> <span class="n">g</span><span class="o">)))</span> <span class="o">:=</span>
</pre></div>

#### [ Kevin Buzzard (Apr 25 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125643897):
<p>proof that <code>R[1/f][1/g] = R[1/fg]</code></p>

#### [ Kevin Buzzard (Apr 25 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125643904):
<p><code>set_option class.instance_max_depth 93</code></p>

#### [ Kevin Buzzard (Apr 25 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125643905):
<p>:-)</p>

#### [ Kevin Buzzard (Apr 25 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125643910):
<p>I don't like the way this is going...</p>

#### [ Kevin Buzzard (Apr 25 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125644005):
<p>Here's the proof:</p>

#### [ Kevin Buzzard (Apr 25 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125644007):
<div class="codehilite"><pre><span></span><span class="n">R_alg_equiv_of_unique_homs</span>
  <span class="o">(</span><span class="n">away_away_universal_property&#39;</span> <span class="n">f</span> <span class="n">g</span> <span class="o">(</span><span class="n">of_comm_ring</span> <span class="n">R</span> <span class="o">(</span><span class="n">powers</span> <span class="o">(</span><span class="n">f</span> <span class="bp">*</span> <span class="n">g</span><span class="o">)))</span>
    <span class="o">(</span><span class="n">unit_of_loc_more_left</span> <span class="n">f</span> <span class="n">g</span><span class="o">)</span> <span class="c1">-- proof that f is aunit in R[1/fg]</span>
    <span class="o">(</span><span class="n">unit_of_loc_more_right</span> <span class="n">f</span> <span class="n">g</span><span class="o">)</span> <span class="c1">-- proof that g is a unit in R[1/fg]</span>
  <span class="o">)</span>
  <span class="o">(</span><span class="n">away_universal_property</span> <span class="o">(</span><span class="n">f</span><span class="bp">*</span><span class="n">g</span><span class="o">)</span>
    <span class="o">((</span><span class="n">of_comm_ring</span> <span class="o">(</span><span class="n">loc</span> <span class="n">R</span> <span class="o">(</span><span class="n">powers</span> <span class="n">f</span><span class="o">))</span> <span class="o">(</span><span class="n">powers</span> <span class="o">(</span><span class="n">of_comm_ring</span> <span class="n">R</span> <span class="o">(</span><span class="n">powers</span> <span class="n">f</span><span class="o">)</span> <span class="n">g</span><span class="o">)))</span>
      <span class="err">∘</span> <span class="o">(</span><span class="n">of_comm_ring</span> <span class="n">R</span> <span class="o">(</span><span class="n">powers</span> <span class="n">f</span><span class="o">)))</span>
    <span class="o">(</span><span class="n">tag01HR</span><span class="bp">.</span><span class="n">unitfg</span> <span class="n">f</span> <span class="n">g</span><span class="o">)</span> <span class="c1">-- proof that fg is a unit in R[1/f][1/g]</span>
  <span class="o">)</span>
  <span class="o">(</span><span class="n">away_away_universal_property&#39;</span> <span class="n">f</span> <span class="n">g</span> <span class="o">((</span><span class="n">of_comm_ring</span> <span class="o">(</span><span class="n">loc</span> <span class="n">R</span> <span class="o">(</span><span class="n">powers</span> <span class="n">f</span><span class="o">))</span> <span class="o">(</span><span class="n">powers</span> <span class="o">(</span><span class="n">of_comm_ring</span> <span class="n">R</span> <span class="o">(</span><span class="n">powers</span> <span class="n">f</span><span class="o">)</span> <span class="n">g</span><span class="o">)))</span> <span class="err">∘</span> <span class="o">(</span><span class="n">of_comm_ring</span> <span class="n">R</span> <span class="o">(</span><span class="n">powers</span> <span class="n">f</span><span class="o">)))</span>
    <span class="o">(</span><span class="n">tag01HR</span><span class="bp">.</span><span class="n">unitf</span> <span class="n">f</span> <span class="n">g</span><span class="o">)</span> <span class="c1">-- proof that f is a unit in R[1/f][1/g]</span>
    <span class="o">(</span><span class="n">tag01HR</span><span class="bp">.</span><span class="n">unitg</span> <span class="n">f</span> <span class="n">g</span><span class="o">)</span> <span class="c1">-- proof that g is a unit in R[1/f][1/g]</span>
  <span class="o">)</span>
  <span class="o">(</span><span class="n">id_unique_R_alg_from_loc</span> <span class="bp">_</span><span class="o">)</span>
</pre></div>

#### [ Kevin Buzzard (Apr 25 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/maximum%20class-instance%20resolution%20depth%20has%20been%20reached/near/125644009):
<p>All universal properties</p>


{% endraw %}
