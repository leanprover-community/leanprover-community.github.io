---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/07070Hardbutobviouslemma.html
---

## Stream: [general](index.html)
### Topic: [Hard but obvious lemma](07070Hardbutobviouslemma.html)

---


{% raw %}
#### [ Chris Hughes (Jun 23 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hard%20but%20obvious%20lemma/near/128498549):
<p>How to prove this? I don't need it, I'm just curious.</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="n">Sort</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">γ</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">Sort</span> <span class="n">v</span><span class="o">}</span> <span class="o">{</span><span class="n">δ</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">Sort</span> <span class="n">v</span><span class="o">}</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="bp">Π</span> <span class="n">a</span><span class="o">,</span> <span class="n">γ</span> <span class="n">a</span><span class="o">}</span> <span class="o">{</span><span class="n">g</span> <span class="o">:</span> <span class="bp">Π</span> <span class="n">b</span><span class="o">,</span> <span class="n">δ</span> <span class="n">b</span><span class="o">}</span>
  <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">b</span> <span class="o">:</span> <span class="n">β</span><span class="o">}</span> <span class="o">(</span><span class="n">hfg</span> <span class="o">:</span> <span class="n">f</span> <span class="bp">==</span> <span class="n">g</span><span class="o">)</span> <span class="o">(</span><span class="n">hab</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">==</span> <span class="n">b</span><span class="o">)</span> <span class="o">:</span> <span class="n">f</span> <span class="n">a</span> <span class="bp">==</span> <span class="n">g</span> <span class="n">b</span> <span class="o">:=</span>
</pre></div>

#### [ Simon Hudon (Jun 23 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hard%20but%20obvious%20lemma/near/128498682):
<p>I think there’s a meta theorem that says it can’t be proved in DTT</p>

#### [ Simon Hudon (Jun 23 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hard%20but%20obvious%20lemma/near/128498686):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span></p>

#### [ Chris Hughes (Jun 23 2018 at 01:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hard%20but%20obvious%20lemma/near/128498834):
<p>In that case, same question for</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="n">Sort</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">γ</span> <span class="n">δ</span> <span class="o">:</span> <span class="n">Sort</span> <span class="n">v</span><span class="o">}</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">}</span> <span class="o">{</span><span class="n">g</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">δ</span><span class="o">}</span>
  <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">b</span> <span class="o">:</span> <span class="n">β</span><span class="o">}</span> <span class="o">(</span><span class="n">hfg</span> <span class="o">:</span> <span class="n">f</span> <span class="bp">==</span> <span class="n">g</span><span class="o">)</span> <span class="o">(</span><span class="n">hab</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">==</span> <span class="n">b</span><span class="o">)</span> <span class="o">:</span> <span class="n">f</span> <span class="n">a</span> <span class="bp">==</span> <span class="n">g</span> <span class="n">b</span>
</pre></div>

#### [ Simon Hudon (Jun 23 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hard%20but%20obvious%20lemma/near/128499127):
<p>I think you would need an equality <code>α = β</code> and <code>γ = δ</code>  for this to be provable. Then, you can deduce <code>f = g</code>. I saw the theorem in a talk by Cody Roux. If I remember correctly, when you want to prove <code>f x₀ .. xᵢ = g y₀ .. yᵢ</code>, from <code>x₀ == y₀</code> .. <code>xᵢ == yᵢ</code>, you need <code>f = g</code> for the statement to be provable.</p>

#### [ Mario Carneiro (Jun 23 2018 at 04:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hard%20but%20obvious%20lemma/near/128505009):
<p>Leo has a whole paper on how he works around the unprovability of this theorem</p>

#### [ Mario Carneiro (Jun 23 2018 at 04:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hard%20but%20obvious%20lemma/near/128505013):
<p>(co-authored with Cody IIRC)</p>

#### [ Mario Carneiro (Jun 23 2018 at 04:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hard%20but%20obvious%20lemma/near/128505054):
<p>Although I think the actual unprovability is only folklore, I don't know an explicit proof although there is probably a way to modify the set model to get it</p>

#### [ Simon Hudon (Jun 23 2018 at 04:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hard%20but%20obvious%20lemma/near/128505074):
<p>He basically generates all the relevant theorems right? I think that's what <code>congr</code> does for <code>heq</code> goals</p>

#### [ Mario Carneiro (Jun 23 2018 at 04:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hard%20but%20obvious%20lemma/near/128505091):
<p>yes, he's implemented a tactic meta-theorem for the version you stated</p>


{% endraw %}
