---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/13114thisandthatorstructure.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [this and that, or structure?](https://leanprover-community.github.io/archive/113488general/13114thisandthatorstructure.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Apr 20 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125377318):
<p>I notice that in our schemes work, Kenny and I independently defined the concept of an open immersion between topological spaces.</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125377327):
<p>I wrote</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125377411):
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">open_immersion</span>
  <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">Tα</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span>
  <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">Tβ</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">β</span><span class="o">]</span>
  <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">fcont</span> <span class="o">:</span> <span class="n">continuous</span> <span class="n">f</span><span class="o">)</span>
<span class="o">(</span><span class="n">finj</span> <span class="o">:</span> <span class="n">function</span><span class="bp">.</span><span class="n">injective</span> <span class="n">f</span><span class="o">)</span>
<span class="o">(</span><span class="n">fopens</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">U</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">,</span> <span class="n">is_open</span> <span class="n">U</span> <span class="bp">↔</span> <span class="n">is_open</span> <span class="o">(</span><span class="n">f</span> <span class="err">&#39;&#39;</span> <span class="n">U</span><span class="o">))</span>
</pre></div>

#### [ Kevin Buzzard (Apr 20 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125377452):
<p>Kenny wrote</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125377475):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">topological_space</span><span class="bp">.</span><span class="n">open_immersion</span> <span class="o">{</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">[</span><span class="n">tX</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">X</span><span class="o">]</span> <span class="o">[</span><span class="n">tY</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">Y</span><span class="o">]</span> <span class="o">(</span><span class="n">φ</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">Y</span><span class="o">)</span> <span class="o">:=</span>
  <span class="n">continuous</span> <span class="n">φ</span> <span class="bp">∧</span>
  <span class="n">function</span><span class="bp">.</span><span class="n">injective</span> <span class="n">φ</span> <span class="bp">∧</span>
  <span class="bp">∀</span> <span class="n">U</span> <span class="o">:</span> <span class="n">set</span> <span class="n">X</span><span class="o">,</span> <span class="n">tX</span><span class="bp">.</span><span class="n">is_open</span> <span class="n">U</span> <span class="bp">→</span> <span class="n">tY</span><span class="bp">.</span><span class="n">is_open</span> <span class="o">(</span><span class="n">set</span><span class="bp">.</span><span class="n">image</span> <span class="n">φ</span> <span class="n">U</span><span class="o">)</span>
</pre></div>

#### [ Kevin Buzzard (Apr 20 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125377929):
<p>I don't think it would be too taxing to check that these two props were equivalent.</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125378082):
<p>But I think there's an argument for putting this basic notion into mathlib</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125378100):
<p>and before I wrote the PR</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125378262):
<p>I realised I was going to have to understand better</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125378523):
<p>about the relative advantages / disadvantages between chaining "and" vs making a structure</p>

#### [ Kenny Lau (Apr 20 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125379302):
<p><a href="https://github.com/kbuzzard/lean-stacks-project/commit/a3e4acc5b443f02c1decf3db32260ff28e4dd855#diff-ad019596efa140984bbb88e365b57df7" target="_blank" title="https://github.com/kbuzzard/lean-stacks-project/commit/a3e4acc5b443f02c1decf3db32260ff28e4dd855#diff-ad019596efa140984bbb88e365b57df7">https://github.com/kbuzzard/lean-stacks-project/commit/a3e4acc5b443f02c1decf3db32260ff28e4dd855#diff-ad019596efa140984bbb88e365b57df7</a></p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125379303):
<p>They're both props, the structure version has the feature that it demands that you spell out which term is doing which of the three jobs that need doing, which may or may not be a good thing, and the "and" approach lets you write more compact code, constructing instances with pointy brackets, which may or may not be a good thing</p>

#### [ Kenny Lau (Apr 20 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125379310):
<p>you wrote both definitions</p>

#### [ Mario Carneiro (Apr 20 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125379590):
<p>You can use pointy brackets with either definition</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125379698):
<p>You're right Kenny, thanks.</p>

#### [ Mario Carneiro (Apr 20 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125379812):
<p>All structure instances, in fact, can be written with pointy brackets instead of structure notation</p>

#### [ Mario Carneiro (Apr 20 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125380086):
<p>it's just that this is harder to read when there are many properties since order matters</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125380341):
<p>Were you to be getting a mathlib PR with a definition of an open immersion</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125380367):
<p>which would you prefer?</p>

#### [ Mario Carneiro (Apr 20 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125380414):
<p>the structure, I think</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125380548):
<p>OK thanks</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125381058):
<p>Sorry Kenny, I could see that you had done the hard work in that tag (supplying the proof of the result below) so just assumed you'd written the definition.</p>

#### [ Patrick Massot (Apr 20 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125382019):
<blockquote>
<p>you wrote both definitions</p>
</blockquote>
<p>Ooohh, I never realized Kenny is only one schizophrenic identity of Kevin. That explains soo much...</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125382178):
<p>Our secret is out Kenny! Or should I say, Mr Hyde...</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125382277):
<p>In fact the far more mundane truth is that I write code, forget, and then write code again.</p>

#### [ Kenny Lau (Apr 20 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125382278):
<p>right, I'm the constructivist version of Kevin</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125382304):
<p>ha ha</p>

#### [ Patrick Massot (Apr 20 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125383630):
<p>Yeah, the story of a first year working in scheme theory was sort of believable, but the constructivism stuff I should have realize this was completely impossible</p>

#### [ Gabriel Ebner (Apr 20 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125384461):
<blockquote>
<p>You can use pointy brackets with either definition</p>
</blockquote>
<p>OTOH, curly braces work much more nicely with the structure.  That is, you can write <code>{fcont := _, finj := _, fopens := _}</code>.  While with <code>∧</code>, you'd need <code>{left := _, right := {left := _, right := _}}</code>.</p>

#### [ Kevin Buzzard (Apr 20 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/this%20and%20that%2C%20or%20structure%3F/near/125391137):
<p>so <code>\and</code> is redundant in Lean ;-)</p>


{% endraw %}
