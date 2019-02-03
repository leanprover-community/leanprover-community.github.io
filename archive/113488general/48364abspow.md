---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/48364abspow.html
---

## Stream: [general](index.html)
### Topic: [abs_pow](48364abspow.html)

---


{% raw %}
#### [ Kenny Lau (May 03 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/abs_pow/near/126016992):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">abs_pow</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">decidable_linear_ordered_comm_ring</span> <span class="n">α</span><span class="o">]</span>
  <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">nat</span><span class="o">)</span> <span class="o">:</span> <span class="n">abs</span> <span class="o">(</span><span class="n">x</span><span class="err">^</span><span class="n">n</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="n">abs</span> <span class="n">x</span><span class="o">)</span><span class="err">^</span><span class="n">n</span> <span class="o">:=</span>
<span class="n">nat</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">n</span> <span class="n">abs_one</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">n</span> <span class="n">ih</span><span class="o">,</span> <span class="o">(</span><span class="n">abs_mul</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="n">trans</span> <span class="err">$</span> <span class="n">congr_arg</span> <span class="bp">_</span> <span class="n">ih</span>
</pre></div>

#### [ Kenny Lau (May 03 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/abs_pow/near/126016994):
<p>but we all know what the answer is</p>

#### [ Kenny Lau (May 03 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/abs_pow/near/126016995):
<p>this thing is in core</p>

#### [ Mario Carneiro (May 03 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/abs_pow/near/126017097):
<p>Kenny, you need to work on making your issues more explicit. These code snippets don't speak for themselves</p>

#### [ Kenny Lau (May 03 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/abs_pow/near/126017150):
<p>oh sorry</p>

#### [ Kenny Lau (May 03 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/abs_pow/near/126017152):
<p>I mean, we should add this in our library</p>

#### [ Chris Hughes (May 03 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/abs_pow/near/126034375):
<p>I think it's called pow_abs in mathlib</p>

#### [ Kenny Lau (May 03 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/abs_pow/near/126034378):
<p>oh</p>

#### [ Kenny Lau (May 03 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/abs_pow/near/126034379):
<p>aha</p>

#### [ Kenny Lau (May 03 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/abs_pow/near/126034387):
<p>very consistent naming</p>


{% endraw %}
