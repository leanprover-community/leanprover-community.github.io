---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/74298filters.html
---

## Stream: [general](index.html)
### Topic: [filters](74298filters.html)

---


{% raw %}
#### [ Rohan Mitta (Sep 05 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filters/near/133377621):
<p>Hi,</p>
<p>I'm attempting to prove a proposition from a Topology book and am getting stuck using filters, which I'm not very comfortable with in lean. Can anyone help me with the first sorry? I'm pretty sure that step is true due to the uniform continuity of f but I can't figure out what to do with it.</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">topology</span><span class="bp">.</span><span class="n">topological_space</span>
<span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">topology</span><span class="bp">.</span><span class="n">continuity</span>
<span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">metric_space</span>
<span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">topology</span><span class="bp">.</span><span class="n">uniform_space</span>
<span class="kn">import</span> <span class="n">order</span><span class="bp">.</span><span class="n">filter</span>

<span class="n">noncomputable</span> <span class="n">theory</span>

<span class="kn">theorem</span> <span class="n">complete_iff_of_uniform_cts_bij</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">metric_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">metric_space</span> <span class="n">β</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span>
    <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">Hf</span> <span class="o">:</span> <span class="n">uniform_continuous</span> <span class="n">f</span><span class="o">)</span> <span class="o">(</span><span class="n">Hg</span> <span class="o">:</span> <span class="n">uniform_continuous</span> <span class="n">g</span><span class="o">)</span> <span class="o">(</span><span class="n">left_inv</span> <span class="o">:</span> <span class="n">function</span><span class="bp">.</span><span class="n">left_inverse</span> <span class="n">g</span> <span class="n">f</span><span class="o">)</span>
    <span class="o">(</span><span class="n">right_inv</span> <span class="o">:</span> <span class="n">function</span><span class="bp">.</span><span class="n">right_inverse</span> <span class="n">g</span> <span class="n">f</span><span class="o">)</span> <span class="o">:</span> <span class="n">complete_space</span> <span class="n">α</span> <span class="bp">↔</span> <span class="n">complete_space</span> <span class="n">β</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">split</span><span class="o">,</span>
    <span class="n">intro</span> <span class="n">H1</span><span class="o">,</span>
    <span class="n">cases</span> <span class="n">H1</span><span class="o">,</span> <span class="n">split</span><span class="o">,</span>
    <span class="n">intros</span> <span class="n">filt</span> <span class="n">Hfilt</span><span class="o">,</span>

    <span class="k">have</span> <span class="n">H2</span> <span class="o">:=</span> <span class="n">H1</span> <span class="o">(</span><span class="n">cauchy_map</span> <span class="n">Hg</span> <span class="n">Hfilt</span><span class="o">),</span>
    <span class="n">cases</span> <span class="n">H2</span> <span class="k">with</span> <span class="n">x</span> <span class="n">H_converges_to_x</span><span class="o">,</span>
    <span class="n">existsi</span> <span class="n">f</span> <span class="n">x</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">filter</span><span class="bp">.</span><span class="n">map_le_iff_le_vmap</span> <span class="n">at</span> <span class="n">H_converges_to_x</span><span class="o">,</span>
    <span class="k">have</span> <span class="n">Hmaps</span> <span class="o">:=</span> <span class="n">filter</span><span class="bp">.</span><span class="n">map_eq_vmap_of_inverse</span> <span class="o">(</span><span class="n">function</span><span class="bp">.</span><span class="n">id_of_right_inverse</span> <span class="n">right_inv</span><span class="o">)</span> <span class="o">(</span><span class="n">function</span><span class="bp">.</span><span class="n">id_of_left_inverse</span> <span class="n">left_inv</span><span class="o">),</span>
    <span class="n">rw</span> <span class="err">←</span> <span class="n">Hmaps</span> <span class="n">at</span> <span class="n">H_converges_to_x</span><span class="o">,</span>
    <span class="k">have</span> <span class="n">H3</span> <span class="o">:</span> <span class="n">filter</span><span class="bp">.</span><span class="n">map</span> <span class="n">f</span> <span class="o">(</span><span class="n">nhds</span> <span class="n">x</span><span class="o">)</span> <span class="bp">=</span> <span class="n">nhds</span> <span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">),</span>

      <span class="n">sorry</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">H3</span> <span class="n">at</span> <span class="n">H_converges_to_x</span><span class="o">,</span> <span class="n">exact</span> <span class="n">H_converges_to_x</span><span class="o">,</span>
  <span class="n">sorry</span><span class="o">,</span>

<span class="kn">end</span>
</pre></div>

#### [ Reid Barton (Sep 05 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filters/near/133378115):
<p>H3 must be true because <code>nhds</code> only depends on the topology and f and g are homeomorphisms.<br>
One direction of the equality will be from continuous.tendsto. The other one should require the continuity of g</p>

#### [ Johannes Hölzl (Sep 05 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filters/near/133378211):
<p>Also, you have an uniform isomorphism (i.e. <code>f</code> with <code>g</code> as inverse). This implies that it is an topological <code>embedding</code>, a <code>dense_embedding</code> and <code>uniform_embedding</code>. If you look for them this should give you enough rules to prove your statement.</p>

#### [ Reid Barton (Sep 05 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filters/near/133378251):
<p>... plus either left_inv or right_inv, and filter.map_map</p>

#### [ Patrick Massot (Sep 05 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filters/near/133378669):
<p><span class="user-mention" data-user-id="120559">@Rohan Mitta</span> don't listen to them, you were almost done. Stating only only implication since the other one follows by symmetry:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">complete_iff_of_uniform_cts_bij</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">metric_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">metric_space</span> <span class="n">β</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span>
    <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">Hf</span> <span class="o">:</span> <span class="n">uniform_continuous</span> <span class="n">f</span><span class="o">)</span> <span class="o">(</span><span class="n">Hg</span> <span class="o">:</span> <span class="n">uniform_continuous</span> <span class="n">g</span><span class="o">)</span> <span class="o">(</span><span class="n">left_inv</span> <span class="o">:</span> <span class="n">function</span><span class="bp">.</span><span class="n">left_inverse</span> <span class="n">g</span> <span class="n">f</span><span class="o">)</span>
    <span class="o">(</span><span class="n">right_inv</span> <span class="o">:</span> <span class="n">function</span><span class="bp">.</span><span class="n">right_inverse</span> <span class="n">g</span> <span class="n">f</span><span class="o">)</span> <span class="o">:</span> <span class="n">complete_space</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">complete_space</span> <span class="n">β</span> <span class="o">:=</span>
<span class="k">begin</span>

  <span class="n">intro</span> <span class="n">H1</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">H1</span><span class="o">,</span> <span class="n">split</span><span class="o">,</span>
  <span class="n">intros</span> <span class="n">filt</span> <span class="n">Hfilt</span><span class="o">,</span>

  <span class="k">have</span> <span class="n">H2</span> <span class="o">:=</span> <span class="n">H1</span> <span class="o">(</span><span class="n">cauchy_map</span> <span class="n">Hg</span> <span class="n">Hfilt</span><span class="o">),</span>
  <span class="n">cases</span> <span class="n">H2</span> <span class="k">with</span> <span class="n">x</span> <span class="n">H_converges_to_x</span><span class="o">,</span>
  <span class="n">existsi</span> <span class="n">f</span> <span class="n">x</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">filter</span><span class="bp">.</span><span class="n">map_le_iff_le_vmap</span> <span class="n">at</span> <span class="n">H_converges_to_x</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">Hmaps</span> <span class="o">:=</span> <span class="n">filter</span><span class="bp">.</span><span class="n">map_eq_vmap_of_inverse</span> <span class="o">(</span><span class="n">function</span><span class="bp">.</span><span class="n">id_of_right_inverse</span> <span class="n">right_inv</span><span class="o">)</span> <span class="o">(</span><span class="n">function</span><span class="bp">.</span><span class="n">id_of_left_inverse</span> <span class="n">left_inv</span><span class="o">),</span>
  <span class="n">rw</span> <span class="err">←</span> <span class="n">Hmaps</span> <span class="n">at</span> <span class="n">H_converges_to_x</span><span class="o">,</span>
  <span class="k">have</span> <span class="o">:=</span> <span class="n">continuous</span><span class="bp">.</span><span class="n">tendsto</span> <span class="n">Hf</span><span class="bp">.</span><span class="n">continuous</span> <span class="n">x</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">le_trans</span> <span class="n">H_converges_to_x</span> <span class="n">this</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Sep 05 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filters/near/133378866):
<p>Thanks all of you (I'm sitting next to Rohan)</p>

#### [ Rohan Mitta (Sep 05 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filters/near/133378965):
<p>Amazing, thanks everyone!</p>

#### [ Patrick Massot (Sep 05 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filters/near/133379170):
<p>Small cleanup:</p>
<div class="codehilite"><pre><span></span><span class="kn">open</span> <span class="n">function</span>
<span class="kn">theorem</span> <span class="n">complete_iff_of_uniform_cts_bij</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">metric_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">metric_space</span> <span class="n">β</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span>
    <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">Hf</span> <span class="o">:</span> <span class="n">uniform_continuous</span> <span class="n">f</span><span class="o">)</span> <span class="o">(</span><span class="n">Hg</span> <span class="o">:</span> <span class="n">uniform_continuous</span> <span class="n">g</span><span class="o">)</span> <span class="o">(</span><span class="n">left_inv</span> <span class="o">:</span> <span class="n">function</span><span class="bp">.</span><span class="n">left_inverse</span> <span class="n">g</span> <span class="n">f</span><span class="o">)</span>
    <span class="o">(</span><span class="n">right_inv</span> <span class="o">:</span> <span class="n">function</span><span class="bp">.</span><span class="n">right_inverse</span> <span class="n">g</span> <span class="n">f</span><span class="o">)</span> <span class="o">:</span> <span class="n">complete_space</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">complete_space</span> <span class="n">β</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">rintro</span> <span class="bp">⟨</span><span class="n">H1</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">split</span><span class="o">,</span>
  <span class="n">intros</span> <span class="n">filt</span> <span class="n">Hfilt</span><span class="o">,</span>

  <span class="n">cases</span> <span class="n">H1</span> <span class="o">(</span><span class="n">cauchy_map</span> <span class="n">Hg</span> <span class="n">Hfilt</span><span class="o">)</span> <span class="k">with</span> <span class="n">x</span> <span class="n">H_converges_to_x</span><span class="o">,</span>
  <span class="n">existsi</span> <span class="n">f</span> <span class="n">x</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">filter</span><span class="bp">.</span><span class="n">map_le_iff_le_vmap</span><span class="o">,</span>
      <span class="err">←</span><span class="n">filter</span><span class="bp">.</span><span class="n">map_eq_vmap_of_inverse</span> <span class="o">(</span><span class="n">id_of_right_inverse</span> <span class="n">right_inv</span><span class="o">)</span> <span class="o">(</span><span class="n">id_of_left_inverse</span> <span class="n">left_inv</span><span class="o">)]</span> <span class="n">at</span> <span class="n">H_converges_to_x</span><span class="o">,</span>

  <span class="n">exact</span> <span class="n">le_trans</span> <span class="n">H_converges_to_x</span> <span class="o">(</span><span class="n">continuous</span><span class="bp">.</span><span class="n">tendsto</span> <span class="n">Hf</span><span class="bp">.</span><span class="n">continuous</span> <span class="n">x</span><span class="o">)</span>
<span class="kn">end</span>
</pre></div>

#### [ Johannes Hölzl (Sep 05 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filters/near/133379874):
<p>Thanks Patrick to actually look at the proof (obviously, I didn't ...)</p>


{% endraw %}
