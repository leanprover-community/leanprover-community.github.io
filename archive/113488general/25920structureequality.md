---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/25920structureequality.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [structure equality](https://leanprover-community.github.io/archive/113488general/25920structureequality.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Jul 06 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality/near/129218426):
<p>How do we prove equality of two terms whose type is a structure mixing data and Prop? I would like to prove each data holding field matches. I thought this has something to do with <code>no_confusion</code> but I can't get it to work.</p>

#### [ Patrick Massot (Jul 06 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality/near/129218697):
<p>Hum, it seems I can uses cases to access stuff here again.</p>

#### [ Chris Hughes (Jul 06 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality/near/129218843):
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">thing</span> <span class="o">:=</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">b</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="n">d</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">thing</span><span class="bp">.</span><span class="n">mk</span> <span class="n">a</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">thing</span><span class="bp">.</span><span class="n">mk</span> <span class="n">c</span> <span class="n">d</span> <span class="o">:=</span>
<span class="k">begin</span>
   <span class="n">rw</span> <span class="n">thing</span><span class="bp">.</span><span class="n">mk</span><span class="bp">.</span><span class="n">inj_eq</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p><code>simp</code> also works.</p>

#### [ Chris Hughes (Jul 06 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality/near/129218950):
<p>I'm not sure what to do if you haven't done cases.</p>

#### [ Simon Hudon (Jul 06 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality/near/129219284):
<p>You can also use <code>congr</code> or <code>congr'</code></p>

#### [ Chris Hughes (Jul 06 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality/near/129219344):
<p>What's the difference between <code>congr</code> and <code>congr'</code>?</p>

#### [ Simon Hudon (Jul 06 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality/near/129219395):
<p><code>congr'</code> takes an argument like <code>congr' 3</code> to ask for three iterations of congruence. <code>congr</code> just keeps going until it can't anymore. Often, <code>congr</code> goes too far</p>

#### [ Patrick Massot (Jul 06 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality/near/129221654):
<p>Thanks Chris and Simon. <code>congr</code> and <code>simp</code> do nothing, <code>cases</code> both sides and <code>rw pequiv.mk.inj_eq ; cc</code> did the trick</p>

#### [ Simon Hudon (Jul 06 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality/near/129221846):
<p>Sorry, I didn't mention, in either case, you need to <code>cases</code> both sides</p>

#### [ Patrick Massot (Jul 06 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality/near/129222086):
<p>Correction, after cases both sides, <code>congr ; cc</code> also works</p>

#### [ Patrick Massot (Jul 06 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality/near/129222164):
<p>and <code>congr ; tauto</code> of course</p>

#### [ Simon Hudon (Jul 06 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality/near/129222707):
<p>I'm wrapping up a round of optimization of <code>tauto</code>. When it works, it should be faster than <code>cc</code></p>

#### [ Simon Hudon (Jul 06 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality/near/129222733):
<p>(and now, it should work more often than before)</p>

#### [ Patrick Massot (Jul 06 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20equality/near/129222738):
<p>Great!</p>


{% endraw %}
