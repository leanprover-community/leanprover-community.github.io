---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/45033Sillyfunctiononthereals.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [Silly function on the reals](https://leanprover-community.github.io/archive/116395maths/45033Sillyfunctiononthereals.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Chris Hughes (Jul 28 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Silly%20function%20on%20the%20reals/near/130481903):
<p>I overheard people talking about this function the other day. Can anyone prove its existence?</p>

#### [ Chris Hughes (Jul 28 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Silly%20function%20on%20the%20reals/near/130481906):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">lemma</span> <span class="n">silly_function</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">f</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">→</span> <span class="n">ℝ</span><span class="o">,</span> <span class="bp">∀</span> <span class="n">x</span> <span class="n">y</span> <span class="n">a</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">,</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="n">y</span> <span class="bp">→</span> <span class="bp">∃</span> <span class="n">z</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">,</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="n">z</span> <span class="bp">∧</span> <span class="n">z</span> <span class="bp">&lt;</span> <span class="n">y</span> <span class="bp">∧</span> <span class="n">f</span> <span class="n">z</span> <span class="bp">=</span> <span class="n">a</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Kenny Lau (Jul 28 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Silly%20function%20on%20the%20reals/near/130481954):
<p>that's the Conway base-13 function</p>

#### [ Kevin Buzzard (Jul 28 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Silly%20function%20on%20the%20reals/near/130482878):
<p>[other functions with this property are available]</p>

#### [ Kevin Buzzard (Jul 28 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Silly%20function%20on%20the%20reals/near/130482926):
<p><a href="https://en.wikipedia.org/wiki/Conway_base_13_function" target="_blank" title="https://en.wikipedia.org/wiki/Conway_base_13_function">https://en.wikipedia.org/wiki/Conway_base_13_function</a> . It's an extreme counterexample to "is the converse of the intermediate value theorem true?"</p>


{% endraw %}
