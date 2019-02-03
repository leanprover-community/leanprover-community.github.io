---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/77891ratmkeq.html
---

## Stream: [general](index.html)
### Topic: [rat.mk_eq](77891ratmkeq.html)

---


{% raw %}
#### [ Kenny Lau (Apr 25 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rat.mk_eq/near/125675114):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">mk_eq</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="n">d</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">}</span> <span class="o">(</span><span class="n">hb</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">≠</span> <span class="mi">0</span><span class="o">)</span> <span class="o">(</span><span class="n">hd</span> <span class="o">:</span> <span class="n">d</span> <span class="bp">≠</span> <span class="mi">0</span><span class="o">),</span>
  <span class="n">a</span> <span class="bp">/.</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">c</span> <span class="bp">/.</span> <span class="n">d</span> <span class="bp">↔</span> <span class="n">a</span> <span class="bp">*</span> <span class="n">d</span> <span class="bp">=</span> <span class="n">c</span> <span class="bp">*</span> <span class="n">b</span> <span class="o">:=</span>
<span class="n">suffices</span> <span class="bp">∀</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="n">d</span> <span class="n">hb</span> <span class="n">hd</span><span class="o">,</span> <span class="n">mk_pnat</span> <span class="n">a</span> <span class="bp">⟨</span><span class="n">b</span><span class="o">,</span> <span class="n">hb</span><span class="bp">⟩</span> <span class="bp">=</span> <span class="n">mk_pnat</span> <span class="n">c</span> <span class="bp">⟨</span><span class="n">d</span><span class="o">,</span> <span class="n">hd</span><span class="bp">⟩</span> <span class="bp">↔</span> <span class="n">a</span> <span class="bp">*</span> <span class="n">d</span> <span class="bp">=</span> <span class="n">c</span> <span class="bp">*</span> <span class="n">b</span><span class="o">,</span>
<span class="o">[</span><span class="bp">...</span><span class="o">]</span>
</pre></div>

#### [ Kenny Lau (Apr 25 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rat.mk_eq/near/125675152):
<p>the one in <code>suffices</code> is what I need T_T</p>

#### [ Mario Carneiro (Apr 25 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rat.mk_eq/near/125680601):
<p>Just rewrite <code>mk_pnat</code> into <code>/.</code>, they are equal</p>

#### [ Kenny Lau (Apr 25 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rat.mk_eq/near/125680649):
<p>this is what I did at the end:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">rat</span><span class="bp">.</span><span class="n">mk_pnat_eq_iff</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="n">d</span><span class="o">)</span> <span class="o">:</span> <span class="n">rat</span><span class="bp">.</span><span class="n">mk_pnat</span> <span class="n">a</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">rat</span><span class="bp">.</span><span class="n">mk_pnat</span> <span class="n">c</span> <span class="n">d</span> <span class="bp">↔</span> <span class="n">a</span> <span class="bp">*</span> <span class="n">d</span> <span class="bp">=</span> <span class="n">c</span> <span class="bp">*</span> <span class="n">b</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">cases</span> <span class="n">b</span> <span class="k">with</span> <span class="n">b</span> <span class="n">hb</span><span class="o">,</span> <span class="n">cases</span> <span class="n">d</span> <span class="k">with</span> <span class="n">d</span> <span class="n">hd</span><span class="o">,</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">rat</span><span class="bp">.</span><span class="n">mk_pnat_eq</span><span class="o">],</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">rat</span><span class="bp">.</span><span class="n">mk_eq</span><span class="o">],</span>
  <span class="n">exact</span> <span class="n">ne_of_gt</span> <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">coe_nat_pos</span><span class="bp">.</span><span class="mi">2</span> <span class="n">hb</span><span class="o">),</span>
  <span class="n">exact</span> <span class="n">ne_of_gt</span> <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">coe_nat_pos</span><span class="bp">.</span><span class="mi">2</span> <span class="n">hd</span><span class="o">),</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Apr 25 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rat.mk_eq/near/125680667):
<p>this part of the code is not going to be PR'd so the neatness of the proof doesn't really matter ot me</p>

#### [ Kenny Lau (Apr 25 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rat.mk_eq/near/125680671):
<p>but I did write a whole bunch of lemmas in the meantime</p>

#### [ Mario Carneiro (Apr 25 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rat.mk_eq/near/125680795):
<p>The real question is why are you dealing with <code>mk_pnat</code>? The interface should let you just use field operations and avoid <code>mk</code> entirely</p>

#### [ Kenny Lau (Apr 25 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rat.mk_eq/near/125680800):
<p>oh, <code>mk_pnat</code> is not intended to be used?</p>

#### [ Kenny Lau (Apr 25 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rat.mk_eq/near/125680838):
<p>I used it because I am using <code>pnat</code></p>

#### [ Kenny Lau (Apr 25 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rat.mk_eq/near/125680843):
<p>or are you going to tell me that <code>pnat</code> is not to be used either</p>

#### [ Mario Carneiro (Apr 25 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rat.mk_eq/near/125680914):
<p>Just use <code>n / d</code> where <code>d : N+</code></p>

#### [ Mario Carneiro (Apr 25 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rat.mk_eq/near/125680991):
<p>The only reason you might want <code>mk_pnat</code> is if you care about the efficiency of computing this value (this will translate <code>d</code> to rat by adding ones)</p>


{% endraw %}
