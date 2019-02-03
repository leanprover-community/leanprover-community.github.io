---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/23264noobquestionaboutcardinal.html
---

## Stream: [new members](index.html)
### Topic: [noob question about cardinal](23264noobquestionaboutcardinal.html)

---


{% raw %}
#### [ Kenny Lau (Sep 13 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%20about%20cardinal/near/133871212):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">set_theory</span><span class="bp">.</span><span class="n">cardinal</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">(</span><span class="n">S</span> <span class="n">T</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span>
  <span class="o">(</span><span class="n">HS</span> <span class="o">:</span> <span class="n">set</span><span class="bp">.</span><span class="n">finite</span> <span class="n">S</span><span class="o">)</span> <span class="o">(</span><span class="n">HT</span> <span class="o">:</span> <span class="n">set</span><span class="bp">.</span><span class="n">finite</span> <span class="n">T</span><span class="o">)</span>
  <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">finset</span><span class="bp">.</span><span class="n">card</span> <span class="o">(</span><span class="n">set</span><span class="bp">.</span><span class="n">finite</span><span class="bp">.</span><span class="n">to_finset</span> <span class="n">HS</span><span class="o">)</span> <span class="bp">≤</span> <span class="n">finset</span><span class="bp">.</span><span class="n">card</span> <span class="o">(</span><span class="n">set</span><span class="bp">.</span><span class="n">finite</span><span class="bp">.</span><span class="n">to_finset</span> <span class="n">HT</span><span class="o">))</span> <span class="o">:</span>
  <span class="n">cardinal</span><span class="bp">.</span><span class="n">mk</span> <span class="n">S</span> <span class="bp">≤</span> <span class="n">cardinal</span><span class="bp">.</span><span class="n">mk</span> <span class="n">T</span> <span class="o">:=</span>
<span class="n">sorry</span>
</pre></div>

#### [ Chris Hughes (Sep 13 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%20about%20cardinal/near/133873000):
<div class="codehilite"><pre><span></span><span class="kn">open</span> <span class="n">cardinal</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">(</span><span class="n">S</span> <span class="n">T</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span>
  <span class="o">(</span><span class="n">HS</span> <span class="o">:</span> <span class="n">set</span><span class="bp">.</span><span class="n">finite</span> <span class="n">S</span><span class="o">)</span> <span class="o">(</span><span class="n">HT</span> <span class="o">:</span> <span class="n">set</span><span class="bp">.</span><span class="n">finite</span> <span class="n">T</span><span class="o">)</span>
  <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">finset</span><span class="bp">.</span><span class="n">card</span> <span class="o">(</span><span class="n">set</span><span class="bp">.</span><span class="n">finite</span><span class="bp">.</span><span class="n">to_finset</span> <span class="n">HS</span><span class="o">)</span> <span class="bp">≤</span> <span class="n">finset</span><span class="bp">.</span><span class="n">card</span> <span class="o">(</span><span class="n">set</span><span class="bp">.</span><span class="n">finite</span><span class="bp">.</span><span class="n">to_finset</span> <span class="n">HT</span><span class="o">))</span> <span class="o">:</span>
  <span class="n">cardinal</span><span class="bp">.</span><span class="n">mk</span> <span class="n">S</span> <span class="bp">≤</span> <span class="n">cardinal</span><span class="bp">.</span><span class="n">mk</span> <span class="n">T</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">haveI</span> <span class="o">:=</span> <span class="n">classical</span><span class="bp">.</span><span class="n">choice</span> <span class="n">HS</span><span class="o">,</span>
  <span class="n">haveI</span> <span class="o">:=</span> <span class="n">classical</span><span class="bp">.</span><span class="n">choice</span> <span class="n">HT</span><span class="o">,</span>
  <span class="n">rwa</span> <span class="o">[</span><span class="n">fintype_card</span> <span class="n">S</span><span class="o">,</span> <span class="n">fintype_card</span> <span class="n">T</span><span class="o">,</span> <span class="n">nat_cast_le</span><span class="o">,</span>
    <span class="n">set</span><span class="bp">.</span><span class="n">card_fintype_of_finset&#39;</span> <span class="o">(</span><span class="n">set</span><span class="bp">.</span><span class="n">finite</span><span class="bp">.</span><span class="n">to_finset</span> <span class="n">HS</span><span class="o">),</span>
    <span class="n">set</span><span class="bp">.</span><span class="n">card_fintype_of_finset&#39;</span> <span class="o">(</span><span class="n">set</span><span class="bp">.</span><span class="n">finite</span><span class="bp">.</span><span class="n">to_finset</span> <span class="n">HT</span><span class="o">)]</span><span class="bp">;</span>
  <span class="n">simp</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Sep 13 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%20about%20cardinal/near/133873086):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">set_theory</span><span class="bp">.</span><span class="n">cardinal</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">(</span><span class="n">S</span> <span class="n">T</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span>
  <span class="o">(</span><span class="n">HS</span> <span class="o">:</span> <span class="n">set</span><span class="bp">.</span><span class="n">finite</span> <span class="n">S</span><span class="o">)</span> <span class="o">(</span><span class="n">HT</span> <span class="o">:</span> <span class="n">set</span><span class="bp">.</span><span class="n">finite</span> <span class="n">T</span><span class="o">)</span>
  <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">finset</span><span class="bp">.</span><span class="n">card</span> <span class="o">(</span><span class="n">set</span><span class="bp">.</span><span class="n">finite</span><span class="bp">.</span><span class="n">to_finset</span> <span class="n">HS</span><span class="o">)</span> <span class="bp">≤</span> <span class="n">finset</span><span class="bp">.</span><span class="n">card</span> <span class="o">(</span><span class="n">set</span><span class="bp">.</span><span class="n">finite</span><span class="bp">.</span><span class="n">to_finset</span> <span class="n">HT</span><span class="o">))</span> <span class="o">:</span>
  <span class="n">cardinal</span><span class="bp">.</span><span class="n">mk</span> <span class="n">S</span> <span class="bp">≤</span> <span class="n">cardinal</span><span class="bp">.</span><span class="n">mk</span> <span class="n">T</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">tactic</span><span class="bp">.</span><span class="n">unfreeze_local_instances</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">HS</span><span class="o">,</span> <span class="n">cases</span> <span class="n">HT</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">cardinal</span><span class="bp">.</span><span class="n">fintype_card</span><span class="o">,</span> <span class="n">cardinal</span><span class="bp">.</span><span class="n">fintype_card</span><span class="o">,</span> <span class="n">cardinal</span><span class="bp">.</span><span class="n">nat_cast_le</span><span class="o">],</span>
  <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">fintype</span><span class="bp">.</span><span class="n">card_coe</span><span class="o">,</span> <span class="err">←</span> <span class="n">fintype</span><span class="bp">.</span><span class="n">card_coe</span><span class="o">]</span> <span class="n">at</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">convert</span> <span class="n">H</span><span class="bp">;</span>
  <span class="o">{</span> <span class="n">ext</span> <span class="n">z</span><span class="o">,</span> <span class="n">rw</span> <span class="o">[</span><span class="n">finset</span><span class="bp">.</span><span class="n">mem_coe</span><span class="o">,</span> <span class="n">set</span><span class="bp">.</span><span class="n">finite</span><span class="bp">.</span><span class="n">mem_to_finset</span><span class="o">]</span> <span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Sep 13 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/noob%20question%20about%20cardinal/near/133873150):
<p>anyway why do we need so many lines</p>


{% endraw %}
