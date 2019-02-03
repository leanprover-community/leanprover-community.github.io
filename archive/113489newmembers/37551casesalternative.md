---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/37551casesalternative.html
---

## Stream: [new members](index.html)
### Topic: [cases alternative](37551casesalternative.html)

---


{% raw %}
#### [ Sarah Mameche (Dec 18 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/cases%20alternative/near/152139969):
<p>Hi, using <code>cases</code> on an hypothesis sometimes gives me really huge terms in the resulting hypotheses. It's happened if the hypothesis contains recursive definitions, and I fixed it in one case by marking the definition as <code>irreducible</code>.<br>
However, now I get the same problem for the definition</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">Fin</span> <span class="o">:</span> <span class="n">nat</span> <span class="bp">→</span> <span class="kt">Type</span>
  <span class="bp">|</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">empty</span>
  <span class="bp">|</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="n">option</span> <span class="o">(</span><span class="n">Fin</span> <span class="n">n</span><span class="o">)</span>
</pre></div>


<p>as soon as I call cases on something like <code>x: Fin (n+1)</code>. In Coq, this goes through, so I guess it has something to do with definitions being compiled to recursors? Is there another way to use cases without unfolding the definition/getting this huge expression? (Marking Fin as irreducible didn't work because I want to match on it in other proofs)</p>

#### [ Kevin Buzzard (Dec 18 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/cases%20alternative/near/152143374):
<p>Definitions made with the equation compiler in Lean can sometimes come out quite unwieldy. Does it make any difference if you just apply the recursor directly?</p>

#### [ Kevin Buzzard (Dec 18 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/cases%20alternative/near/152143471):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">Fin&#39;</span> <span class="o">:</span> <span class="n">nat</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">n</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">n</span> <span class="o">(</span><span class="n">empty</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">n</span> <span class="n">Fn</span><span class="o">,</span> <span class="n">option</span> <span class="n">Fn</span><span class="o">)</span>
</pre></div>

#### [ Chris Hughes (Dec 18 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/cases%20alternative/near/152143723):
<p>A definition like this one in <code>number_theory/dioph</code> is probably easier to use, and gives a similar induction principle</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">fin2</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">fz</span> <span class="o">{</span><span class="n">n</span><span class="o">}</span> <span class="o">:</span> <span class="n">fin2</span> <span class="o">(</span><span class="n">succ</span> <span class="n">n</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">fs</span> <span class="o">{</span><span class="n">n</span><span class="o">}</span> <span class="o">:</span> <span class="n">fin2</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">fin2</span> <span class="o">(</span><span class="n">succ</span> <span class="n">n</span><span class="o">)</span>
</pre></div>

#### [ Sarah Mameche (Dec 19 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/cases%20alternative/near/152145711):
<p>That helped, thanks!</p>


{% endraw %}
