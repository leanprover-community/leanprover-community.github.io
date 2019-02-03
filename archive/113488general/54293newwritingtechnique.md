---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/54293newwritingtechnique.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [new writing technique](https://leanprover-community.github.io/archive/113488general/54293newwritingtechnique.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Jul 04 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20writing%20technique/near/129102181):
<p>I've found a nice new trick to write obfuscated^W concise code:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">chart_chart_inv</span> <span class="o">{</span><span class="n">φ</span> <span class="o">:</span> <span class="n">chart</span> <span class="n">X</span><span class="o">}</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">φ</span><span class="bp">.</span><span class="n">target</span><span class="o">}</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">φ</span><span class="bp">.</span><span class="n">range</span> <span class="bp">→</span> <span class="n">φ</span> <span class="o">(</span><span class="n">φ</span><span class="bp">.</span><span class="n">inv</span> <span class="n">x</span><span class="o">)</span> <span class="bp">=</span> <span class="n">x</span>
<span class="bp">|</span> <span class="bp">⟨</span><span class="n">y</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">y_in</span><span class="o">,</span> <span class="n">φ_y</span><span class="bp">⟩⟩</span> <span class="o">:=</span> <span class="n">inv_fun_on_eq</span> <span class="bp">⟨</span><span class="n">y</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">y_in</span><span class="o">,</span> <span class="n">φ_y</span><span class="bp">⟩⟩</span>
</pre></div>

#### [ Patrick Massot (Jul 04 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20writing%20technique/near/129102241):
<p>Why not writing <code>assume H, inv_fun_on_eq H</code>? Well, the sequences of pointy brackets in the pattern matching and body don't represent the same (anonymized) constructor.</p>

#### [ Simon Hudon (Jul 04 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20writing%20technique/near/129102445):
<p>Would it make you happy if Lean gave you a warning about using the anonymous constructors in disjoint expressions to build expressions of different types?</p>

#### [ Patrick Massot (Jul 04 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20writing%20technique/near/129102464):
<p>I don't know.</p>

#### [ Patrick Massot (Jul 04 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20writing%20technique/near/129102472):
<p>I'm not complaining about anything.</p>

#### [ Patrick Massot (Jul 04 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20writing%20technique/near/129102520):
<p>I do think that if I read this code later than a few days away from now, I'll be thinking WTF?</p>

#### [ Simon Hudon (Jul 04 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20writing%20technique/near/129102522):
<p>Sorry, I'm highjacking your conversation. I've been saying for a while that we need a linter tool to find dubious code</p>

#### [ Simon Hudon (Jul 04 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20writing%20technique/near/129102528):
<p>And I'm wondering how to define "dubious code"</p>

#### [ Chris Hughes (Jul 04 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20writing%20technique/near/129102619):
<p>Maybe the type of the two <code>⟨y, ⟨y_in, φ_y⟩⟩</code>s is different.</p>

#### [ Simon Hudon (Jul 04 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20writing%20technique/near/129102865):
<p>Yes, that's what Patrick was pointing out</p>

#### [ Patrick Massot (Jul 04 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20writing%20technique/near/129103273):
<p>Here is a minimized example for the curious readers:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">set</span><span class="bp">.</span><span class="n">basic</span>
<span class="kn">open</span> <span class="n">set</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∃</span><span class="n">a</span><span class="err">∈</span><span class="n">s</span><span class="o">,</span> <span class="n">f</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">b</span><span class="o">)</span> <span class="o">:</span> <span class="n">b</span> <span class="err">∈</span> <span class="n">f</span> <span class="err">&#39;&#39;</span> <span class="n">s</span>  <span class="o">:=</span>
<span class="k">begin</span>
  <span class="c1">-- rw mem_image, exact h,</span>
  <span class="c1">-- rw mem_image_eq, exact h,</span>
  <span class="n">rw</span> <span class="n">mem_image</span><span class="o">,</span>
  <span class="n">rcases</span> <span class="n">h</span> <span class="k">with</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">b</span><span class="o">,</span> <span class="n">c</span><span class="bp">⟩⟩</span><span class="o">,</span>
  <span class="n">exact</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">b</span><span class="o">,</span> <span class="n">c</span><span class="bp">⟩⟩</span>
<span class="kn">end</span>
</pre></div>


<p>The two commented out lines are nice tries that don't work.</p>

#### [ Patrick Massot (Jul 04 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20writing%20technique/near/129103278):
<p>And it's in tactic mode so you can see everything</p>

#### [ Patrick Massot (Jul 04 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20writing%20technique/near/129103357):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Is there a variation on <code>mem_image</code> that I'm missing here?</p>

#### [ Mario Carneiro (Jul 04 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20writing%20technique/near/129104411):
<p>I see nothing wrong with <code>chart_inv_inv</code></p>

#### [ Mario Carneiro (Jul 04 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20writing%20technique/near/129104523):
<div class="codehilite"><pre><span></span>example (α β : Type) (s : set α) (f : α → β) (b) (h : ∃a∈s, f a = b) : b ∈ f &#39;&#39; s  :=
by simpa using h
</pre></div>

#### [ Patrick Massot (Jul 04 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20writing%20technique/near/129104604):
<p>How does this work? What is <code>simpa</code> magically doing here? I know <code>mem_image</code> is a simp lemma. And then?</p>

#### [ Chris Hughes (Jul 04 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20writing%20technique/near/129104678):
<p><code>∃ (H : a ∈ s), f a = b ==&gt; a ∈ s ∧ f a = b</code> <code> exists_prop</code></p>


{% endraw %}
