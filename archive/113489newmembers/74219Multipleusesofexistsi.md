---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/74219Multipleusesofexistsi.html
---

## Stream: [new members](index.html)
### Topic: [Multiple uses of existsi](74219Multipleusesofexistsi.html)

---


{% raw %}
#### [ Calle Sönne (Nov 20 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Multiple%20uses%20of%20existsi/near/148043024):
<p>I have the following goal:</p>
<div class="codehilite"><pre><span></span><span class="bp">∃</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">s</span> <span class="err">∈</span> <span class="n">S</span><span class="o">),</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">k</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">k</span> <span class="err">∈</span> <span class="n">S</span> <span class="bp">→</span> <span class="n">s</span> <span class="bp">≤</span> <span class="n">k</span>
</pre></div>


<p>Now I have an element s which has all required properties to prove this goal. I would like to provide this s using existsi. Of course I also have to provide the fact that s is in S (my hypothesis Hs). However using existsi s Hs doesnt seem to work, and I need to call existsi two times. That is existsi s, existsi Hs. Is there anyway to make this into a one-liner?</p>

#### [ Johan Commelin (Nov 20 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Multiple%20uses%20of%20existsi/near/148043187):
<p><code>refine \&lt;s, Hs, _\&gt;</code></p>

#### [ Rob Lewis (Nov 20 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Multiple%20uses%20of%20existsi/near/148043189):
<p><code>existsi</code> takes an expression or a list of expressions. Try <code>existsi [s, Hs]</code>.</p>

#### [ Calle Sönne (Nov 20 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Multiple%20uses%20of%20existsi/near/148044104):
<p>Thank you! Both methods worked fine :). What would be the pro of using refine instead of existsi? That its more general?</p>

#### [ Johan Commelin (Nov 20 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Multiple%20uses%20of%20existsi/near/148044259):
<p>See also <a href="#narrow/stream/113488-general/subject/.60existsi.60.20is.20so.20dumb" title="#narrow/stream/113488-general/subject/.60existsi.60.20is.20so.20dumb">https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/.60existsi.60.20is.20so.20dumb</a></p>

#### [ Calle Sönne (Nov 20 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Multiple%20uses%20of%20existsi/near/148044703):
<p>Thanks :)</p>

#### [ Kevin Buzzard (Nov 21 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Multiple%20uses%20of%20existsi/near/148078885):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">easy</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">x</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">,</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">x</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="c1">--  existsi 23, -- lean says &quot;that&#39;s not an integer!&quot;</span>
    <span class="n">refine</span> <span class="bp">⟨</span><span class="mi">23</span><span class="o">,</span><span class="bp">_⟩</span><span class="o">,</span> <span class="c1">-- works fine</span>
    <span class="n">refl</span>
<span class="kn">end</span>
</pre></div>


<p>I have almost given up on <code>existsi</code>, it doesn't try hard enough.</p>


{% endraw %}
