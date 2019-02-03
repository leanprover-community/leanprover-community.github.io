---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/72163convinsum.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [conv in sum](https://leanprover-community.github.io/archive/113488general/72163convinsum.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Morenikeji Neri (Aug 01 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20in%20sum/near/130723162):
<p>I would like to show</p>
<div class="codehilite"><pre><span></span><span class="n">finset</span><span class="bp">.</span><span class="n">sum</span> <span class="n">finset</span><span class="bp">.</span><span class="n">univ</span>  <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">μ</span> <span class="o">:</span> <span class="n">S</span> <span class="n">n</span><span class="o">),</span> <span class="n">e</span> <span class="o">(</span><span class="n">ρ</span><span class="bp">.</span><span class="n">to_fun</span><span class="o">)</span> <span class="bp">*</span> <span class="n">e</span> <span class="o">(</span><span class="n">μ</span><span class="bp">.</span><span class="n">to_fun</span><span class="o">)</span> <span class="bp">*</span> <span class="n">finset</span><span class="bp">.</span><span class="n">prod</span> <span class="n">finset</span><span class="bp">.</span><span class="n">univ</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">fin</span> <span class="n">n</span><span class="o">),</span> <span class="n">A</span> <span class="o">(</span><span class="n">μ</span><span class="bp">.</span><span class="n">to_fun</span> <span class="n">i</span><span class="o">)</span> <span class="n">i</span><span class="o">))</span> <span class="bp">=</span> <span class="n">finset</span><span class="bp">.</span><span class="n">sum</span> <span class="n">finset</span><span class="bp">.</span><span class="n">univ</span>
      <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">μ</span> <span class="o">:</span> <span class="n">S</span> <span class="n">n</span><span class="o">),</span> <span class="n">e</span> <span class="o">(</span><span class="n">ρ</span><span class="bp">.</span><span class="n">to_fun</span><span class="o">)</span> <span class="bp">*</span> <span class="o">(</span><span class="n">e</span> <span class="o">(</span><span class="n">μ</span><span class="bp">.</span><span class="n">to_fun</span><span class="o">)</span> <span class="bp">*</span> <span class="n">finset</span><span class="bp">.</span><span class="n">prod</span> <span class="n">finset</span><span class="bp">.</span><span class="n">univ</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">fin</span> <span class="n">n</span><span class="o">),</span> <span class="n">A</span> <span class="o">(</span><span class="n">μ</span><span class="bp">.</span><span class="n">to_fun</span> <span class="n">i</span><span class="o">)</span> <span class="n">i</span><span class="o">)))</span>
</pre></div>


<p>where multiplication is in a comm_ring hence is associative, however I cannot use conv as it cannot synthesis μ.to_fun as it is a function. Any tips?</p>

#### [ Morenikeji Neri (Aug 01 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20in%20sum/near/130725250):
<p>all sorted</p>

#### [ Simon Hudon (Aug 01 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/conv%20in%20sum/near/130725742):
<p>I recommend you make a minimal working example so that people can have a look inside of a Lean session. </p>
<p>I think <code>congr' 1, ext, rw mul_assoc</code> could help.</p>


{% endraw %}
