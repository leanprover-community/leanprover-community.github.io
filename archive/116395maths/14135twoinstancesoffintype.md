---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/14135twoinstancesoffintype.html
---

## Stream: [maths](index.html)
### Topic: [two instances of fintype](14135twoinstancesoffintype.html)

---


{% raw %}
#### [ Casper Putz (Jan 18 2019 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/two%20instances%20of%20fintype/near/156362890):
<p>Hi, I have the following code where I explicitely constructed an equivalence between two types <code>α</code> and <code>β → γ</code>, and all types are fintypes. I want to conclude that <code>α.card = γ.card ^ β.card</code> but I have a problem with instances. I would like to something like this:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">fintype</span>
<span class="kn">open</span> <span class="n">fintype</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span>
<span class="kn">variables</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">β</span><span class="o">]</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">γ</span><span class="o">]</span>
<span class="kn">variables</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">α</span><span class="o">]</span>
<span class="kn">variables</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="err">≃</span> <span class="o">(</span><span class="n">β</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">))</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">card</span> <span class="n">α</span> <span class="bp">=</span> <span class="n">card</span> <span class="n">γ</span> <span class="err">^</span> <span class="n">card</span> <span class="n">β</span> <span class="o">:=</span>
<span class="k">calc</span> <span class="n">card</span> <span class="n">α</span> <span class="bp">=</span> <span class="bp">@</span><span class="n">card</span> <span class="o">(</span><span class="n">β</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">)</span> <span class="o">(</span><span class="n">of_equiv</span> <span class="n">α</span> <span class="n">f</span><span class="o">)</span> <span class="o">:</span> <span class="n">eq</span><span class="bp">.</span><span class="n">symm</span> <span class="err">$</span> <span class="n">of_equiv_card</span> <span class="n">f</span>
        <span class="bp">...</span> <span class="bp">=</span> <span class="n">card</span> <span class="n">γ</span> <span class="err">^</span> <span class="n">card</span> <span class="n">β</span> <span class="o">:</span> <span class="n">card_fun</span>
</pre></div>


<p>The problem is I have two different instances of <code>fintype (β → γ) </code>. The one coming from <code>fintype.of_equiv</code> (which <code>of_equiv_card</code> uses) and one coming from <code>pi.fintype</code> (which <code>card_fun</code> uses).  How could I solve this? Or should I try a completely different route?</p>

#### [ Chris Hughes (Jan 18 2019 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/two%20instances%20of%20fintype/near/156363177):
<p>Something like this?</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="n">card</span> <span class="n">α</span> <span class="bp">=</span> <span class="n">card</span> <span class="n">β</span> <span class="err">^</span> <span class="n">card</span> <span class="n">γ</span> <span class="o">:=</span>
<span class="k">calc</span> <span class="n">card</span> <span class="n">α</span> <span class="bp">=</span> <span class="bp">@</span><span class="n">card</span> <span class="o">(</span><span class="n">β</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">)</span> <span class="o">(</span><span class="n">of_equiv</span> <span class="n">α</span> <span class="n">f</span><span class="o">)</span> <span class="o">:</span> <span class="n">eq</span><span class="bp">.</span><span class="n">symm</span> <span class="err">$</span> <span class="n">of_equiv_card</span> <span class="n">f</span>
        <span class="bp">...</span> <span class="bp">=</span> <span class="n">card</span> <span class="o">(</span><span class="n">β</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">)</span> <span class="o">:</span> <span class="k">by</span> <span class="n">congr</span>
        <span class="bp">...</span> <span class="bp">=</span> <span class="n">card</span> <span class="n">γ</span> <span class="err">^</span> <span class="n">card</span> <span class="n">β</span> <span class="o">:</span> <span class="n">card_fun</span>
</pre></div>

#### [ Casper Putz (Jan 18 2019 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/two%20instances%20of%20fintype/near/156363562):
<p>Yes! I also needed <code>[decidable_eq β]</code>, but then it worked :). Thanks!</p>


{% endraw %}
