---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/90813Provingbasicinequalitiesofnaturalnumbers.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [Proving basic inequalities of natural numbers](https://leanprover-community.github.io/archive/113489newmembers/90813Provingbasicinequalitiesofnaturalnumbers.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Sebastian Zimmer (Oct 13 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20basic%20inequalities%20of%20natural%20numbers/near/135737118):
<p>linarith doesn't seem to be good enough to prove this basic inequality</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">simple_order_lemma</span> <span class="o">(</span><span class="n">k</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">h1</span> <span class="o">:</span> <span class="n">k</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">)</span> <span class="o">(</span><span class="n">h2</span> <span class="o">:</span> <span class="bp">¬</span> <span class="n">k</span> <span class="bp">&gt;</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:</span> <span class="n">k</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span> <span class="k">begin</span>
<span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>

#### [ Sebastian Zimmer (Oct 13 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20basic%20inequalities%20of%20natural%20numbers/near/135737158):
<p>What's the best way of proving this sort of result?</p>

#### [ Kenny Lau (Oct 13 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20basic%20inequalities%20of%20natural%20numbers/near/135737269):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">nat</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">lemma</span> <span class="n">simple_order_lemma</span> <span class="o">(</span><span class="n">k</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">h1</span> <span class="o">:</span> <span class="n">k</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">)</span> <span class="o">(</span><span class="n">h2</span> <span class="o">:</span> <span class="bp">¬</span> <span class="n">k</span> <span class="bp">&gt;</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:</span> <span class="n">k</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">dec_trivial</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">k</span><span class="o">,</span> <span class="n">k</span> <span class="bp">≤</span> <span class="mi">1</span> <span class="bp">→</span> <span class="n">k</span> <span class="bp">&gt;</span> <span class="mi">0</span> <span class="bp">→</span> <span class="n">k</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span> <span class="n">k</span> <span class="o">(</span><span class="n">le_of_not_gt</span> <span class="n">h2</span><span class="o">)</span> <span class="n">h1</span>
</pre></div>

#### [ Kenny Lau (Oct 13 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20basic%20inequalities%20of%20natural%20numbers/near/135737317):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">simple_order_lemma</span> <span class="o">(</span><span class="n">k</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">h1</span> <span class="o">:</span> <span class="n">k</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">)</span> <span class="o">(</span><span class="n">h2</span> <span class="o">:</span> <span class="bp">¬</span> <span class="n">k</span> <span class="bp">&gt;</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:</span> <span class="n">k</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">have</span> <span class="n">h3</span> <span class="o">:=</span> <span class="n">le_of_not_gt</span> <span class="n">h2</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">h3</span> <span class="k">with</span> <span class="n">h3</span> <span class="n">h3</span><span class="o">,</span> <span class="o">{</span><span class="n">refl</span><span class="o">},</span>
  <span class="n">cases</span> <span class="n">h3</span><span class="o">,</span> <span class="n">cases</span> <span class="n">h1</span>
<span class="kn">end</span>
</pre></div>

#### [ Sebastian Zimmer (Oct 13 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20basic%20inequalities%20of%20natural%20numbers/near/135737406):
<p>Thanks, I would have never thought of that first solution.</p>


{% endraw %}
