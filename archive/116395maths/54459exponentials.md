---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/54459exponentials.html
---

## Stream: [maths](index.html)
### Topic: [exponentials](54459exponentials.html)

---


{% raw %}
#### [ Kenny Lau (Apr 27 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/exponentials/near/125775813):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> what happened to your PR's about exp?</p>

#### [ Chris Hughes (Apr 27 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/exponentials/near/125779790):
<p>I made this PR <a href="https://github.com/leanprover/mathlib/pull/61" target="_blank" title="https://github.com/leanprover/mathlib/pull/61">https://github.com/leanprover/mathlib/pull/61</a> in Feb, which is a necessary part of exp, and it hasn't been closed or accepted essentially because I didn't use filters, I used <code>cau_seq</code> as defined in <code>data.real.cau_seq</code>. I might have to rewrite it using filters over the summer.</p>

#### [ Kenny Lau (Apr 27 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/exponentials/near/125779805):
<p>I'm also trying to learn how filters define limit :D</p>

#### [ Kenny Lau (Apr 27 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/exponentials/near/125779817):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">const</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">Y</span><span class="o">)</span> <span class="o">:</span> <span class="n">tendsto</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span> <span class="o">:</span> <span class="n">X</span><span class="o">,</span> <span class="n">y</span><span class="o">)</span> <span class="o">(</span><span class="n">nhds</span> <span class="n">x</span><span class="o">)</span> <span class="o">(</span><span class="n">nhds</span> <span class="n">y</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">B</span> <span class="n">HB</span> <span class="n">FX</span> <span class="n">HF1</span><span class="o">,</span> <span class="n">HF1</span> <span class="bp">_</span> <span class="bp">⟨</span><span class="n">set</span><span class="bp">.</span><span class="n">univ</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span> <span class="err">$</span> <span class="n">univ_mem_sets&#39;</span> <span class="err">$</span>
<span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="k">show</span> <span class="n">y</span> <span class="err">∈</span> <span class="n">B</span><span class="o">,</span> <span class="k">from</span> <span class="n">mem_of_nhds</span> <span class="n">HB</span>
</pre></div>


<p>This was an exercise I set to myself (I know it's in mathlib already)</p>


{% endraw %}
