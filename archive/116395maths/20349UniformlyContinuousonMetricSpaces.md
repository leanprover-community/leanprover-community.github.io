---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/20349UniformlyContinuousonMetricSpaces.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [Uniformly Continuous on Metric Spaces](https://leanprover-community.github.io/archive/116395maths/20349UniformlyContinuousonMetricSpaces.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Rohan Mitta (Sep 26 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Uniformly%20Continuous%20on%20Metric%20Spaces/near/134666418):
<p>Have I formalised this right and is it in mathlib?</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">metric_space</span>

<span class="kn">example</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">metric_space</span> <span class="n">X</span><span class="o">]</span> <span class="o">[</span><span class="n">metric_space</span> <span class="n">Y</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">Y</span><span class="o">)</span> <span class="o">:</span>
<span class="n">uniform_continuous</span> <span class="n">f</span> <span class="bp">↔</span> <span class="bp">∀</span> <span class="n">ε</span><span class="o">,</span> <span class="n">ε</span> <span class="bp">&gt;</span> <span class="mi">0</span> <span class="bp">→</span> <span class="bp">∃</span> <span class="n">δ</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">δ</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">),</span> <span class="bp">∀</span> <span class="n">x₁</span> <span class="n">x₂</span> <span class="o">:</span> <span class="n">X</span><span class="o">,</span>
  <span class="n">dist</span> <span class="n">x₁</span> <span class="n">x₂</span> <span class="bp">&lt;</span> <span class="n">δ</span> <span class="bp">→</span> <span class="n">dist</span> <span class="o">(</span><span class="n">f</span> <span class="n">x₁</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="n">x₂</span><span class="o">)</span> <span class="bp">&lt;</span> <span class="n">ε</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Johannes Hölzl (Sep 26 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Uniformly%20Continuous%20on%20Metric%20Spaces/near/134666547):
<p>looks good to me, and I don't think we have it in mathlib yet</p>

#### [ Johannes Hölzl (Sep 26 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Uniformly%20Continuous%20on%20Metric%20Spaces/near/134666569):
<p>sorry, just found it <code>uniform_continuous_of_metric </code></p>

#### [ Kevin Buzzard (Sep 26 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Uniformly%20Continuous%20on%20Metric%20Spaces/near/134666760):
<p>Thanks Johannes!</p>

#### [ Patrick Massot (Sep 26 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Uniformly%20Continuous%20on%20Metric%20Spaces/near/134668357):
<p>Rohan, note that <code>∀ ε, ε &gt; 0</code> can be written <code>∀ ε &gt; 0</code> like you would do on paper</p>

#### [ Patrick Massot (Sep 26 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Uniformly%20Continuous%20on%20Metric%20Spaces/near/134668427):
<p>Lean will parse that exactly as you originally wrote</p>

#### [ Rohan Mitta (Sep 26 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Uniformly%20Continuous%20on%20Metric%20Spaces/near/134668976):
<p>Thanks everyone!</p>

#### [ Kenny Lau (Sep 26 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Uniformly%20Continuous%20on%20Metric%20Spaces/near/134673009):
<blockquote>
<p>Lean will parse that exactly as you originally wrote</p>
</blockquote>
<p>well not exactly...</p>


{% endraw %}
