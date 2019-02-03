---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/59310Perfectfield.html
---

## Stream: [maths](index.html)
### Topic: [Perfect field](59310Perfectfield.html)

---


{% raw %}
#### [ Kenny Lau (Oct 17 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfect%20field/near/135957480):
<p>Currently this is my definition:</p>
<div class="codehilite"><pre><span></span><span class="c">/-</span><span class="cm">- A perfect field is a field of characteristic p that has p-th root. -/</span>
<span class="n">class</span> <span class="n">perfect_field</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">field</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">[</span><span class="n">char_p</span> <span class="n">α</span> <span class="n">p</span><span class="o">]</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">pth_root</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span>
<span class="o">(</span><span class="n">frobenius_pth_root</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">frobenius</span> <span class="n">α</span> <span class="n">p</span> <span class="o">(</span><span class="n">pth_root</span> <span class="n">x</span><span class="o">)</span> <span class="bp">=</span> <span class="n">x</span><span class="o">)</span>
</pre></div>

#### [ Kenny Lau (Oct 17 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfect%20field/near/135957484):
<p>Do you guys have a better suggestion?</p>

#### [ Kenny Lau (Oct 17 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfect%20field/near/135957489):
<p>My idea is that we can change the definition once we have enough theory about separable polynomials.</p>

#### [ Kenny Lau (Oct 17 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfect%20field/near/135957495):
<p>And go with this definition for now.</p>

#### [ Mario Carneiro (Oct 17 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfect%20field/near/135990765):
<p>use <code>discrete_field</code></p>

#### [ Mario Carneiro (Oct 17 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfect%20field/near/135990773):
<p><code>field</code> is deprecated</p>


{% endraw %}
