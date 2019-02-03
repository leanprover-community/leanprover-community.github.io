---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/98412Unfoldingdefinitionswithmatch.html
---

## Stream: [new members](index.html)
### Topic: [Unfolding definitions with match](98412Unfoldingdefinitionswithmatch.html)

---


{% raw %}
#### [ Ken Roe (Jul 25 2018 at 01:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Unfolding%20definitions%20with%20match/near/130244220):
<p>I'm trying to prove the following:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">evv</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span><span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">y</span><span class="o">:</span> <span class="bp">ℕ</span><span class="o">):=</span>
    <span class="k">match</span> <span class="n">x</span> <span class="n">y</span> <span class="k">with</span>
    <span class="bp">|</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">tt</span>
    <span class="bp">|</span> <span class="mi">1</span> <span class="o">:=</span> <span class="n">ff</span>
    <span class="bp">|</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">tt</span>
    <span class="kn">end</span>

<span class="kn">theorem</span> <span class="n">test</span><span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span> <span class="o">(</span><span class="n">f</span><span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">f</span> <span class="n">x</span><span class="bp">=</span><span class="mi">1</span> <span class="bp">→</span> <span class="n">evv</span> <span class="n">f</span> <span class="n">x</span> <span class="o">:=</span>
<span class="k">begin</span>
    <span class="n">intros</span><span class="o">,</span> <span class="n">unfold</span> <span class="n">evv</span><span class="o">,</span> <span class="bp">...</span>
<span class="kn">end</span>
</pre></div>


<p>At the point of the "...", I have the following state:</p>
<div class="codehilite"><pre><span></span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span>
<span class="n">f</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">,</span>
<span class="n">a</span> <span class="o">:</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span>
<span class="err">⊢</span> <span class="err">↥</span><span class="o">(</span><span class="n">evv</span><span class="bp">._</span><span class="n">match_1</span> <span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">))</span>
</pre></div>


<p>How do I complete the theorem?</p>

#### [ Ken Roe (Jul 25 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Unfolding%20definitions%20with%20match/near/130244421):
<p>I was using quotation, however, I would like to find a way to construct the expression without the quotation.</p>

#### [ Kevin Buzzard (Jul 25 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Unfolding%20definitions%20with%20match/near/130244494):
<p>Your theorem is false so it's hard to complete.</p>

#### [ Kevin Buzzard (Jul 25 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Unfolding%20definitions%20with%20match/near/130244551):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">test</span><span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span> <span class="o">(</span><span class="n">f</span><span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">f</span> <span class="n">x</span><span class="bp">=</span><span class="mi">1</span> <span class="bp">→</span> <span class="n">evv</span> <span class="n">f</span> <span class="n">x</span> <span class="o">:=</span>
<span class="k">begin</span>
    <span class="n">intros</span><span class="o">,</span>
    <span class="n">unfold</span> <span class="n">evv</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">a</span><span class="o">,</span>
    <span class="n">simp</span> <span class="n">only</span> <span class="o">[</span><span class="n">evv</span><span class="bp">._</span><span class="n">match_1</span><span class="o">],</span>
    <span class="c1">-- suffices to prove ff</span>
    <span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Jul 25 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Unfolding%20definitions%20with%20match/near/130244565):
<p>The arrow business is because you are talking about booleans as if they're propositions, so a coercion is happening.</p>

#### [ Chris Hughes (Jul 25 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Unfolding%20definitions%20with%20match/near/130244705):
<p>It wasn't true so I changed it.</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">test</span><span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span> <span class="o">(</span><span class="n">f</span><span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">f</span> <span class="n">x</span><span class="bp">=</span><span class="mi">0</span> <span class="bp">→</span> <span class="n">evv</span> <span class="n">f</span> <span class="n">x</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">intros</span><span class="o">,</span>
  <span class="n">unfold</span> <span class="n">evv</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">a</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">rfl</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


{% endraw %}
