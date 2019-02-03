---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/25708triviallyfalse.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [trivially false](https://leanprover-community.github.io/archive/113488general/25708triviallyfalse.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Aug 04 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trivially%20false/near/130883663):
<p>Am I supposed to resolve situations like</p>
<div class="codehilite"><pre><span></span>H : (1 / 2).denom = 1
⊢ false
</pre></div>


<p>with <code>revert H,exact dec_trivial</code> or is there some less clunky way where I apply something to H directly?</p>

#### [ Mario Carneiro (Aug 04 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trivially%20false/near/130883713):
<p>I use <code>absurd H dec_trivial</code> for this kind of thing</p>

#### [ Kevin Buzzard (Aug 04 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trivially%20false/near/130883727):
<p>Thanks</p>

#### [ Kenny Lau (Aug 04 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trivially%20false/near/130883827):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">rat</span>

<span class="kn">theorem</span> <span class="n">test</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="o">(</span><span class="mi">1</span> <span class="bp">/</span> <span class="mi">2</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">)</span><span class="bp">.</span><span class="n">denom</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:</span> <span class="n">false</span> <span class="o">:=</span>
<span class="n">nat</span><span class="bp">.</span><span class="n">no_confusion</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">succ_inj</span> <span class="n">H</span><span class="o">)</span>
</pre></div>

#### [ Kenny Lau (Aug 04 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trivially%20false/near/130883896):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> interestingly <code>cases</code> fails on <code>H</code> or on <code>nat.succ_inj H</code>, and so does <code>injections with H</code></p>

#### [ Kevin Buzzard (Aug 04 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trivially%20false/near/130883927):
<p>ha ha, I'll let you know the next time I'm in this situation Kenny and you can come up with some bespoke solution for me :-)</p>

#### [ Mario Carneiro (Aug 04 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trivially%20false/near/130883999):
<p>I get timeouts on everything that does something equivalent to cases on H, even <code>match H with end</code> times out</p>

#### [ Mario Carneiro (Aug 04 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trivially%20false/near/130884058):
<p><code>match (show 2 = 1, from H) with end</code> works, and other equivalent things</p>

#### [ Mario Carneiro (Aug 04 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trivially%20false/near/130884100):
<p>it must be unfolding things in a weird order</p>


{% endraw %}
