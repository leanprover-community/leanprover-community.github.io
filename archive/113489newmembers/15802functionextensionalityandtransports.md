---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/15802functionextensionalityandtransports.html
---

## Stream: [new members](index.html)
### Topic: [function extensionality and transports](15802functionextensionalityandtransports.html)

---


{% raw %}
#### [ Edward Ayers (Aug 08 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/function%20extensionality%20and%20transports/near/131125621):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">my_ext</span>
    <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span><span class="kt">Type</span><span class="o">)</span>
      <span class="o">(</span><span class="n">P</span> <span class="n">Q</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">-&gt;</span> <span class="kt">Type</span><span class="o">)</span>
      <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">P</span> <span class="n">a</span> <span class="o">)</span>
      <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">Q</span> <span class="n">a</span><span class="o">)</span>
      <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">P</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">Q</span> <span class="n">a</span><span class="o">),</span>
        <span class="o">(</span><span class="bp">∀</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="o">((</span><span class="n">p</span> <span class="n">a</span><span class="o">)</span> <span class="bp">▸</span> <span class="o">(</span><span class="n">f</span> <span class="n">a</span><span class="o">))</span> <span class="bp">=</span> <span class="n">g</span> <span class="n">a</span><span class="o">)</span>
        <span class="bp">-&gt;</span> <span class="o">((</span><span class="n">funext</span> <span class="n">p</span><span class="o">)</span> <span class="bp">▸</span> <span class="n">f</span><span class="o">)</span> <span class="bp">=</span> <span class="n">g</span>
    <span class="o">:=</span> <span class="k">by</span> <span class="n">sorry</span>
</pre></div>


<p>Some questions:<br>
1. How do I get the transport triangles to work? I get the same error if I reverse the arguments so I don't even know if I'm using it the right way round<br>
2. How do I prove it?<br>
3. Is it crazy to want to do this?</p>

#### [ Chris Hughes (Aug 08 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/function%20extensionality%20and%20transports/near/131125836):
<p>The triangles are for <code>eq.subst</code> which can only make proofs, not data. You have to use <code>eq.rec</code> I think. You could also use heq <code>==</code></p>

#### [ Mario Carneiro (Aug 08 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/function%20extensionality%20and%20transports/near/131126052):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">my_ext</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span><span class="kt">Type</span><span class="o">)</span>
  <span class="o">(</span><span class="n">P</span> <span class="n">Q</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">-&gt;</span> <span class="kt">Type</span><span class="o">)</span>
  <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">P</span> <span class="n">a</span> <span class="o">)</span>
  <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">Q</span> <span class="n">a</span><span class="o">)</span>
  <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">P</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">Q</span> <span class="n">a</span><span class="o">)</span> <span class="o">:</span>
    <span class="o">(</span><span class="bp">∀</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">rec_on</span> <span class="o">(</span><span class="n">p</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="n">a</span><span class="o">)</span> <span class="o">:</span> <span class="n">Q</span> <span class="n">a</span><span class="o">)</span> <span class="bp">=</span> <span class="n">g</span> <span class="n">a</span><span class="o">)</span>
    <span class="bp">-&gt;</span> <span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">rec_on</span> <span class="o">(</span><span class="n">funext</span> <span class="n">p</span> <span class="o">:</span> <span class="n">P</span> <span class="bp">=</span> <span class="n">Q</span><span class="o">)</span> <span class="n">f</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">Q</span> <span class="n">a</span><span class="o">)</span> <span class="bp">=</span> <span class="n">g</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">cases</span> <span class="o">(</span><span class="n">funext</span> <span class="n">p</span> <span class="o">:</span> <span class="n">P</span> <span class="bp">=</span> <span class="n">Q</span><span class="o">)</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">funext</span>
</pre></div>


{% endraw %}
