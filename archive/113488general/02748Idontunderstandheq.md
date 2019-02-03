---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/02748Idontunderstandheq.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [I don't understand heq](https://leanprover-community.github.io/archive/113488general/02748Idontunderstandheq.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Apr 14 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20don%27t%20understand%20heq/near/125071940):
<p>Here's a self-contained extract from <code>analysis/topology/topological.space_lean</code>:</p>

#### [ Kevin Buzzard (Apr 14 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20don%27t%20understand%20heq/near/125071981):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">topology</span><span class="bp">.</span><span class="n">topological_space</span>
<span class="kn">open</span> <span class="n">topological_space</span>
<span class="n">universes</span> <span class="n">u</span> <span class="n">v</span> <span class="n">w</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">{</span><span class="n">ι</span> <span class="o">:</span> <span class="n">Sort</span> <span class="n">w</span><span class="o">}</span> <span class="o">{</span><span class="n">a</span> <span class="n">a₁</span> <span class="n">a₂</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">s</span> <span class="n">s₁</span> <span class="n">s₂</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">p</span> <span class="n">p₁</span> <span class="n">p₂</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span>
<span class="kn">variables</span> <span class="o">[</span><span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span>

<span class="kn">lemma</span> <span class="n">is_open_Union_orig</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">ι</span> <span class="bp">→</span> <span class="n">set</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span><span class="n">i</span><span class="o">,</span> <span class="n">is_open</span> <span class="o">(</span><span class="n">f</span> <span class="n">i</span><span class="o">))</span> <span class="o">:</span> <span class="n">is_open</span> <span class="o">(</span><span class="err">⋃</span><span class="n">i</span><span class="o">,</span> <span class="n">f</span> <span class="n">i</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">is_open_sUnion</span> <span class="err">$</span> <span class="k">assume</span> <span class="n">t</span> <span class="bp">⟨</span><span class="n">i</span><span class="o">,</span> <span class="o">(</span><span class="n">heq</span> <span class="o">:</span> <span class="n">t</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">i</span><span class="o">)</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">heq</span><span class="bp">.</span><span class="n">symm</span> <span class="bp">▸</span> <span class="n">h</span> <span class="n">i</span>

<span class="kn">lemma</span> <span class="n">is_open_Union&#39;</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">ι</span> <span class="bp">→</span> <span class="n">set</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span><span class="n">i</span><span class="o">,</span> <span class="n">is_open</span> <span class="o">(</span><span class="n">f</span> <span class="n">i</span><span class="o">))</span> <span class="o">:</span> <span class="n">is_open</span> <span class="o">(</span><span class="err">⋃</span><span class="n">i</span><span class="o">,</span> <span class="n">f</span> <span class="n">i</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">refine</span> <span class="n">is_open_sUnion</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">intro</span> <span class="n">t</span><span class="o">,</span>
  <span class="n">intro</span> <span class="n">Ht</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">Ht</span> <span class="k">with</span> <span class="n">i</span> <span class="n">Hi</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">eq</span><span class="bp">.</span><span class="n">symm</span> <span class="n">Hi</span> <span class="bp">▸</span> <span class="n">h</span> <span class="n">i</span><span class="o">,</span>
<span class="kn">end</span>

<span class="kn">lemma</span> <span class="n">is_open_Union&#39;&#39;</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">ι</span> <span class="bp">→</span> <span class="n">set</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span><span class="n">i</span><span class="o">,</span> <span class="n">is_open</span> <span class="o">(</span><span class="n">f</span> <span class="n">i</span><span class="o">))</span> <span class="o">:</span> <span class="n">is_open</span> <span class="o">(</span><span class="err">⋃</span><span class="n">i</span><span class="o">,</span> <span class="n">f</span> <span class="n">i</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">is_open_sUnion</span> <span class="err">$</span> <span class="k">assume</span> <span class="n">t</span> <span class="bp">⟨</span><span class="n">i</span><span class="o">,</span> <span class="o">(</span><span class="n">rfl</span> <span class="o">:</span> <span class="n">t</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">i</span><span class="o">)</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">eq</span><span class="bp">.</span><span class="n">symm</span> <span class="bp">▸</span> <span class="n">h</span> <span class="n">i</span> <span class="c1">-- doesn&#39;t compile</span>
</pre></div>

#### [ Kevin Buzzard (Apr 14 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20don%27t%20understand%20heq/near/125071983):
<p>well, the first lemma is the extract -- it's called <code>is_open_Union</code> in the actual file.</p>

#### [ Kevin Buzzard (Apr 14 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20don%27t%20understand%20heq/near/125071988):
<p>I should perhaps say <code>lemma is_open_sUnion {s : set (set α)} (h : ∀t ∈ s, is_open t) : is_open (⋃₀ s)</code></p>

#### [ Kevin Buzzard (Apr 14 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20don%27t%20understand%20heq/near/125071992):
<p>So I realised I didn't really understand the mathlib proof of <code>is_open_Union_orig</code> (which is the proof given in the extract above, with its <code>heq</code>)</p>

#### [ Kevin Buzzard (Apr 14 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20don%27t%20understand%20heq/near/125072033):
<p>so I proved the lemma "in the same way", in tactic mode</p>

#### [ Kevin Buzzard (Apr 14 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20don%27t%20understand%20heq/near/125072034):
<p>and that's <code>is_open_Union'</code></p>

#### [ Kevin Buzzard (Apr 14 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20don%27t%20understand%20heq/near/125072035):
<p>and everything works fine with eq</p>

#### [ Kevin Buzzard (Apr 14 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20don%27t%20understand%20heq/near/125072043):
<p>Oh -- got it:</p>

#### [ Kevin Buzzard (Apr 14 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20don%27t%20understand%20heq/near/125072045):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">is_open_Union&#39;&#39;</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">ι</span> <span class="bp">→</span> <span class="n">set</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span><span class="n">i</span><span class="o">,</span> <span class="n">is_open</span> <span class="o">(</span><span class="n">f</span> <span class="n">i</span><span class="o">))</span> <span class="o">:</span> <span class="n">is_open</span> <span class="o">(</span><span class="err">⋃</span><span class="n">i</span><span class="o">,</span> <span class="n">f</span> <span class="n">i</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">is_open_sUnion</span> <span class="err">$</span> <span class="k">assume</span> <span class="n">t</span> <span class="bp">⟨</span><span class="n">i</span><span class="o">,</span> <span class="o">(</span><span class="n">eq</span> <span class="o">:</span> <span class="n">t</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">i</span><span class="o">)</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">eq</span><span class="bp">.</span><span class="n">symm</span> <span class="bp">▸</span> <span class="n">h</span> <span class="n">i</span>
</pre></div>

#### [ Kevin Buzzard (Apr 14 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20don%27t%20understand%20heq/near/125072085):
<p>What's with this <code>heq</code> in the mathlib version?</p>

#### [ Kevin Buzzard (Apr 14 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20don%27t%20understand%20heq/near/125072130):
<p>Oh!</p>

#### [ Kevin Buzzard (Apr 14 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20don%27t%20understand%20heq/near/125072131):
<p>Got it :-)</p>

#### [ Kevin Buzzard (Apr 14 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20don%27t%20understand%20heq/near/125072132):
<p><code>heq</code> has nothing to do with <code>heq</code>, it's just a variable name :-)</p>

#### [ Kevin Buzzard (Apr 14 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/I%20don%27t%20understand%20heq/near/125072138):
<p>Oh OK, so I do understand this particular use of heq, we're calling a variable by the same name as a Lean function :-)</p>


{% endraw %}
