---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/17447readablesubquotients.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [readable subquotients](https://leanprover-community.github.io/archive/113488general/17447readablesubquotients.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Oct 01 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/readable%20subquotients/near/134968883):
<p>So, let me return to my original question.</p>

#### [ Johan Commelin (Oct 01 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/readable%20subquotients/near/134968900):
<p>I've got</p>
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">Spa</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="n">Huber_pair</span><span class="o">)</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">Spv</span> <span class="n">A</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">Spv</span><span class="bp">.</span><span class="n">lift</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">v</span><span class="o">,</span> <span class="n">v</span><span class="bp">.</span><span class="n">is_continuous</span> <span class="bp">∧</span> <span class="bp">∀</span> <span class="n">r</span><span class="o">,</span> <span class="n">r</span> <span class="err">∈</span> <span class="n">A</span><span class="err">⁺</span> <span class="bp">→</span> <span class="n">v</span><span class="bp">.</span><span class="n">val</span><span class="bp">.</span><span class="n">val</span> <span class="n">r</span> <span class="bp">≤</span> <span class="mi">1</span><span class="o">)</span>
<span class="o">(</span><span class="bp">λ</span> <span class="n">v₁</span> <span class="n">v₂</span> <span class="n">heq</span><span class="o">,</span> <span class="n">sorry</span><span class="o">)</span>

<span class="c1">-- fake</span>
<span class="kn">definition</span> <span class="n">Spa&#39;</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="n">Huber_pair</span><span class="o">)</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">Spv</span> <span class="n">A</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span><span class="n">v</span> <span class="o">:</span> <span class="n">Spv</span> <span class="n">A</span> <span class="bp">|</span> <span class="n">v</span><span class="bp">.</span><span class="n">is_continuous</span> <span class="bp">∧</span> <span class="bp">∀</span> <span class="n">r</span><span class="o">,</span> <span class="n">r</span> <span class="err">∈</span> <span class="n">A</span><span class="err">⁺</span> <span class="bp">→</span> <span class="n">v</span><span class="bp">.</span><span class="n">val</span><span class="bp">.</span><span class="n">val</span> <span class="n">r</span> <span class="bp">≤</span> <span class="mi">1</span><span class="o">}</span>
<span class="n">which_is_well_defined</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">v₁</span> <span class="n">v₂</span> <span class="n">heq</span><span class="o">,</span> <span class="n">sorry</span><span class="o">)</span>
</pre></div>

#### [ Johan Commelin (Oct 01 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/readable%20subquotients/near/134968965):
<p>Maybe it is really minor to people who have seen Lean for 367 days in the last year, but I think <code>Spa'</code> is a lot more readable than <code>Spa</code>.</p>

#### [ Johan Commelin (Oct 01 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/readable%20subquotients/near/134969006):
<p>Of course any mathematician who takes a first look is already brain-blocked by <code>set (Spv A)</code>, which means "subset" instead of "set". But never mind...</p>

#### [ Kevin Buzzard (Oct 01 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/readable%20subquotients/near/134974894):
<p>Can't you put the work into the definition of <code>v.is_continuous</code>?</p>

#### [ Johan Commelin (Oct 01 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/readable%20subquotients/near/134975038):
<p>I'm not sure if that would help. Or do you mean that you want to define <code>Spa</code> as intersection of two subsets? Namely <code>Cont</code> and the other condition.</p>

#### [ Johan Commelin (Oct 01 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/readable%20subquotients/near/134975061):
<p>Still feels like moving the problem around...</p>


{% endraw %}
