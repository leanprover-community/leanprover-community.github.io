---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/96433Tactictonotactic.html
---

## Stream: [general](index.html)
### Topic: [Tactic to no tactic](96433Tactictonotactic.html)

---


{% raw %}
#### [ Nima (Apr 21 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20to%20no%20tactic/near/125479107):
<p>Is there an easy way to re-write the last function without using tactic?</p>
<div class="codehilite"><pre><span></span><span class="kn">section</span>
<span class="kn">parameters</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">[</span><span class="n">decidable</span> <span class="n">p</span><span class="o">]</span>
<span class="n">def</span> <span class="n">cnd₁</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="n">def</span> <span class="n">cnd₂</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="n">def</span> <span class="kn">check</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="k">if</span> <span class="n">p</span> <span class="k">then</span> <span class="n">cnd₁</span> <span class="k">else</span> <span class="n">cnd₂</span>
<span class="n">def</span> <span class="n">f₁</span> <span class="o">(</span><span class="n">c</span><span class="o">:</span><span class="n">cnd₁</span><span class="o">)</span> <span class="o">:</span> <span class="n">nat</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="n">def</span> <span class="n">f₂</span> <span class="o">(</span><span class="n">c</span><span class="o">:</span><span class="n">cnd₂</span><span class="o">)</span> <span class="o">:</span> <span class="n">nat</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="n">def</span> <span class="n">f</span>  <span class="o">(</span><span class="n">c</span><span class="o">:</span><span class="kn">check</span><span class="o">):</span> <span class="n">nat</span> <span class="o">:=</span> <span class="c1">-- if p then f₁ cnd₁ else f₂ cnd₂</span>
<span class="k">begin</span>
  <span class="n">by_cases</span> <span class="n">p</span> <span class="bp">;</span> <span class="n">simp</span> <span class="o">[</span><span class="kn">check</span><span class="o">,</span><span class="n">h</span><span class="o">]</span> <span class="n">at</span> <span class="n">c</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">f₁</span> <span class="n">c</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">f₂</span> <span class="n">c</span><span class="o">,</span>
<span class="kn">end</span>
<span class="kn">end</span>
</pre></div>

#### [ Mario Carneiro (Apr 21 2018 at 05:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20to%20no%20tactic/near/125479500):
<div class="codehilite"><pre><span></span>theorem check_of_p (h : p) : check ↔ cnd₁ := iff_of_eq (if_pos h)
theorem check_of_not_p (h : ¬ p) : check ↔ cnd₂ := iff_of_eq (if_neg h)

def f (c:check) : nat :=
if h : p then
  f₁ ((check_of_p h).1 c)
else
  f₂ ((check_of_not_p h).1 c)
</pre></div>

#### [ Nima (Apr 21 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20to%20no%20tactic/near/125481942):
<p>Thank you, <code>if_pos</code> and <code>if_neg</code> are what I was looking for.</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">f&#39;</span> <span class="o">(</span><span class="n">c</span><span class="o">:</span><span class="kn">check</span><span class="o">):</span> <span class="n">nat</span> <span class="o">:=</span>
  <span class="k">if</span> <span class="n">h</span><span class="o">:</span><span class="n">p</span> <span class="k">then</span> <span class="n">f₁</span> <span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">mp</span> <span class="o">(</span><span class="n">if_pos</span> <span class="n">h</span><span class="o">)</span> <span class="n">c</span><span class="o">)</span>
  <span class="k">else</span>        <span class="n">f₁</span> <span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">mp</span> <span class="o">(</span><span class="n">if_neg</span> <span class="n">h</span><span class="o">)</span> <span class="n">c</span><span class="o">)</span>
</pre></div>

#### [ Kenny Lau (Apr 21 2018 at 07:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20to%20no%20tactic/near/125482384):
<p>Nima beats Mario</p>

#### [ Mario Carneiro (Apr 21 2018 at 07:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20to%20no%20tactic/near/125482438):
<p>I wrote it that way for a reason. You should not rely on definitional expansion in this way as it is brittle. The point of the lemma is to isolate the unfolding of <code>check</code> so that this isn't happening in an ambiguous context</p>

#### [ Mario Carneiro (Apr 21 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20to%20no%20tactic/near/125482447):
<p>The usage of <code>iff</code> is by convention since these are propositions</p>


{% endraw %}
