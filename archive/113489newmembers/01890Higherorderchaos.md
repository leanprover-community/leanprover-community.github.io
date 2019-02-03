---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/01890Higherorderchaos.html
---

## Stream: [new members](index.html)
### Topic: [Higher order chaos](01890Higherorderchaos.html)

---


{% raw %}
#### [ Ken Roe (Jul 15 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129679786):
<p>I was experimenting with lambda reductions.  Can someone help me complete the following theorem:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">testit</span><span class="o">:</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">x</span><span class="o">,</span> <span class="o">((</span><span class="bp">λ</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="o">(</span><span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)),</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">)</span><span class="bp">+</span><span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">)))</span>
                         <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="n">x</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">→</span> <span class="mi">3</span><span class="bp">=</span><span class="mi">4</span> <span class="o">:=</span>
<span class="k">begin</span>
    <span class="n">intro</span><span class="o">,</span> <span class="n">cases</span> <span class="n">a</span><span class="o">,</span><span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>


<p>What should replace the "sorry"?</p>

#### [ Mario Carneiro (Jul 15 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129680026):
<p>here's a proof:</p>
<div class="codehilite"><pre><span></span>theorem testit: (∃ x, ((λ (f : (ℕ → ℕ)), (λ (x:ℕ), (f x)+(f x)))
                         (λ (x:ℕ), x+1)) x = 1) → 3=4 :=
begin
    intro, cases a,
    dsimp at a_h,
    rw [add_assoc, add_left_comm 1] at a_h,
    cases a_h
end
</pre></div>

#### [ Kevin Buzzard (Jul 15 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129696201):
<p>Here's a more fleshed-out argument:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">testit</span><span class="o">:</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">x</span><span class="o">,</span> <span class="o">((</span><span class="bp">λ</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="o">(</span><span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)),</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">)</span><span class="bp">+</span><span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">)))</span>
                         <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="n">x</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">→</span> <span class="mi">3</span><span class="bp">=</span><span class="mi">4</span> <span class="o">:=</span>
<span class="k">begin</span>
    <span class="n">intro</span><span class="o">,</span> <span class="n">cases</span> <span class="n">a</span> <span class="k">with</span> <span class="n">n</span> <span class="n">Hn</span><span class="o">,</span> <span class="c1">-- name the hypotheses</span>
    <span class="n">exfalso</span><span class="o">,</span> <span class="c1">-- we&#39;re going to prove by contradiction</span>
    <span class="n">change</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">+</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">1</span> <span class="n">at</span> <span class="n">Hn</span><span class="o">,</span> <span class="c1">-- instead of dsimp do the definitional rewrite yourself</span>
    <span class="n">rw</span> <span class="err">←</span><span class="n">add_assoc</span> <span class="n">at</span> <span class="n">Hn</span><span class="o">,</span> <span class="c1">-- Hn now n + 1 + n + 1 = 1</span>
    <span class="n">rw</span> <span class="err">←</span><span class="n">add_right_comm</span> <span class="n">n</span> <span class="n">at</span> <span class="n">Hn</span><span class="o">,</span> <span class="c1">-- Hn now (n + n) + 1 + 1 = 1</span>
    <span class="k">have</span> <span class="n">H₂</span> <span class="o">:=</span> <span class="n">nat</span><span class="bp">.</span><span class="n">succ</span><span class="bp">.</span><span class="n">inj</span> <span class="n">Hn</span><span class="o">,</span> <span class="c1">-- H₂ now (n+n)+1=0</span>
    <span class="n">exact</span> <span class="n">nat</span><span class="bp">.</span><span class="n">succ_ne_zero</span> <span class="bp">_</span> <span class="n">H₂</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Jul 15 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129696426):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">testit</span><span class="o">:</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">x</span><span class="o">,</span> <span class="o">((</span><span class="bp">λ</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="o">(</span><span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)),</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">)</span><span class="bp">+</span><span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">)))</span>
                         <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="n">x</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">→</span> <span class="mi">3</span><span class="bp">=</span><span class="mi">4</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">h</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cases_on</span> <span class="n">x</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">H</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">no_confusion</span> <span class="err">$</span> <span class="n">nat</span><span class="bp">.</span><span class="n">succ_inj</span> <span class="n">H</span><span class="o">)</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">n</span> <span class="n">H</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">no_confusion</span> <span class="err">$</span> <span class="n">nat</span><span class="bp">.</span><span class="n">succ_inj</span> <span class="n">H</span><span class="o">)</span> <span class="n">h</span>

<span class="kn">theorem</span> <span class="n">testit&#39;</span><span class="o">:</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">x</span><span class="o">,</span> <span class="o">((</span><span class="bp">λ</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="o">(</span><span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)),</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">)</span><span class="bp">+</span><span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">)))</span>
                         <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="n">x</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">→</span> <span class="mi">3</span><span class="bp">=</span><span class="mi">4</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">h</span><span class="bp">⟩</span><span class="o">,</span> <span class="k">by</span> <span class="n">cases</span> <span class="n">x</span><span class="bp">;</span> <span class="k">from</span> <span class="n">nat</span><span class="bp">.</span><span class="n">no_confusion</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">succ_inj</span> <span class="n">h</span><span class="o">)</span>

<span class="kn">theorem</span> <span class="n">testit&#39;&#39;</span><span class="o">:</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">x</span><span class="o">,</span> <span class="o">((</span><span class="bp">λ</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="o">(</span><span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)),</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">)</span><span class="bp">+</span><span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">)))</span>
                         <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="n">x</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">→</span> <span class="mi">3</span><span class="bp">=</span><span class="mi">4</span>
<span class="bp">|</span> <span class="bp">⟨</span><span class="mi">0</span><span class="o">,</span> <span class="n">h</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">nat</span><span class="bp">.</span><span class="n">no_confusion</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">succ_inj</span> <span class="n">h</span><span class="o">)</span>
</pre></div>

#### [ Patrick Massot (Jul 15 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129696429):
<p>Now let's go for a more mathlib version:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">ring</span>

<span class="kn">theorem</span> <span class="n">testit</span><span class="o">:</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">x</span><span class="o">,</span> <span class="o">((</span><span class="bp">λ</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="o">(</span><span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)),</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">)</span><span class="bp">+</span><span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">)))</span>
                         <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="n">x</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">→</span> <span class="mi">3</span><span class="bp">=</span><span class="mi">4</span> <span class="o">:=</span>
<span class="k">begin</span>
    <span class="n">rintro</span> <span class="bp">⟨</span><span class="n">n</span><span class="o">,</span> <span class="n">Hn</span><span class="bp">⟩</span><span class="o">,</span> <span class="c1">-- name the hypotheses</span>
    <span class="n">by_contradiction</span><span class="o">,</span> <span class="c1">-- we&#39;re going to prove by contradiction</span>
    <span class="n">change</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">+</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">1</span> <span class="n">at</span> <span class="n">Hn</span><span class="o">,</span> <span class="c1">-- instead of dsimp do the definitional rewrite yourself</span>
    <span class="n">rw</span> <span class="o">(</span><span class="k">show</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">+</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">2</span><span class="bp">*</span><span class="n">n</span><span class="bp">+</span><span class="mi">2</span><span class="o">,</span> <span class="k">by</span> <span class="n">ring</span><span class="o">)</span> <span class="n">at</span> <span class="n">Hn</span><span class="o">,</span>
    <span class="k">have</span> <span class="n">H₂</span> <span class="o">:=</span> <span class="n">nat</span><span class="bp">.</span><span class="n">succ</span><span class="bp">.</span><span class="n">inj</span> <span class="n">Hn</span><span class="o">,</span> <span class="c1">-- H₂ now 2*n+1=0</span>
    <span class="n">exact</span> <span class="n">nat</span><span class="bp">.</span><span class="n">succ_ne_zero</span> <span class="bp">_</span> <span class="n">H₂</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Jul 15 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129696430):
<p>I believe my last version would be the mathlib version :P</p>

#### [ Patrick Massot (Jul 15 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129696469):
<p>I meant using mathlib tactics. Note the use of <code>rintro</code> to squash Kevin's first two lines into one, and the use of <code>ring</code> for the computation</p>

#### [ Kenny Lau (Jul 15 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129696475):
<p>obfuscated version:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">testit&#39;&#39;</span><span class="o">:</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">x</span><span class="o">,</span> <span class="o">((</span><span class="bp">λ</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="o">(</span><span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)),</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">)</span><span class="bp">+</span><span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">)))</span>
                         <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="n">x</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">→</span> <span class="mi">3</span><span class="bp">=</span><span class="mi">4</span>
<span class="bp">|</span> <span class="bp">⟨</span><span class="mi">0</span><span class="o">,</span> <span class="n">h</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">congr_arg</span> <span class="o">((</span><span class="bp">+</span><span class="o">)</span><span class="mi">2</span><span class="o">)</span> <span class="n">h</span><span class="bp">.</span><span class="n">symm</span>
</pre></div>

#### [ Patrick Massot (Jul 15 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129696476):
<p>I also replaced <code>exfalso</code> by <code>by_contradiction</code>. Here it buys you nothing but it's more powerful in general, so let's remember that one.</p>

#### [ Mario Carneiro (Jul 15 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129696584):
<p>I prefer:</p>
<div class="codehilite"><pre><span></span>theorem testit&#39;&#39;: (∃ x, ((λ (f : (ℕ → ℕ)), (λ (x:ℕ), (f x)+(f x)))
                         (λ (x:ℕ), x+1)) x = 1) → 3=4
| ⟨0, h⟩ := by cases h
</pre></div>

#### [ Kenny Lau (Jul 15 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129696589):
<p>nice</p>

#### [ Mario Carneiro (Jul 15 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129696590):
<p>the match against <code>0</code> at the beginning is clever</p>

#### [ Mario Carneiro (Jul 15 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129696631):
<p>(but of course none of these is the mathlib version because the statement is ridiculous)</p>

#### [ Patrick Massot (Jul 15 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129696640):
<p>Again, my "mathlib version" story was only about rewriting Kevin's proof in the same spirit but using more mathlib power</p>

#### [ Patrick Massot (Jul 15 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129696642):
<p>Anyway, hopefully Ken will be able to learn many things from this discussion</p>

#### [ Mario Carneiro (Jul 15 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129696702):
<p>I think lean golf is a nice way to learn new tricks, although its actual applicability is debatable</p>

#### [ Patrick Massot (Jul 15 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129696706):
<p>Actually I'd like to be sure I understand your trick. You let the equation compiler do the job of checking that 0 is the only possibility for x, right?</p>

#### [ Kenny Lau (Jul 15 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129696717):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">logic</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">theorem</span> <span class="n">testit</span><span class="o">:</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">x</span><span class="o">,</span> <span class="o">((</span><span class="bp">λ</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="o">(</span><span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)),</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">)</span><span class="bp">+</span><span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">)))</span>
                         <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="n">x</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">→</span> <span class="mi">3</span><span class="bp">=</span><span class="mi">4</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">simp</span><span class="bp">;</span> <span class="n">intros</span> <span class="n">x</span> <span class="n">H</span><span class="bp">;</span> <span class="n">cases</span> <span class="n">H</span>
</pre></div>

#### [ Mario Carneiro (Jul 15 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129696756):
<p>Right. The equation compiler figures out a sequence of case splits that produce the cases that I give. Since I wrote <code>0</code> instead of <code>n</code> for the first thing, it deduces that we have a case split on the nat, but that requires a second branch, for <code>&lt;succ n, h&gt;</code>. But here <code>h</code> has a type like <code>succ stuff = 0</code>, so it does a second case split on <code>h</code> and deduces that this case is impossible</p>

#### [ Patrick Massot (Jul 15 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129696763):
<p>Ok, this is what I thought. Well done, equation compiler!</p>

#### [ Mario Carneiro (Jul 15 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129696803):
<p>I like to take advantage of this for doing things like pattern matching on <code>l : list A</code> and <code>h : length l = 2</code> and only providing a case for <code>[a, b], _</code></p>

#### [ Kenny Lau (Jul 15 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129696805):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">testit</span><span class="o">:</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">x</span><span class="o">,</span> <span class="o">((</span><span class="bp">λ</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="o">(</span><span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)),</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">)</span><span class="bp">+</span><span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">)))</span>
                         <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="n">x</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">→</span> <span class="mi">3</span><span class="bp">=</span><span class="mi">4</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">H</span><span class="bp">⟩</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span> <span class="n">at</span> <span class="n">H</span><span class="bp">;</span> <span class="n">cases</span> <span class="n">H</span>
</pre></div>

#### [ Kevin Buzzard (Jul 15 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129696815):
<p>I like the way that the title of this thread was once a bit of an overstatement but has now become true. Something here for everyone now :-)</p>

#### [ Kevin Buzzard (Jul 15 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129697094):
<blockquote>
<p>Actually I'd like to be sure I understand your trick. </p>
</blockquote>
<p>I'm still struggling with the <code>cases a_h</code> line in the very first proof <span class="emoji emoji-1f923" title="rolling on the floor laughing">:rolling_on_the_floor_laughing:</span></p>
<p><code>cases</code> seems to be much more powerful than I'd realised. Applied to <code>n + (n + (1 + 1)) = 1</code> it realises that both nats are <code>succ (something)</code> so reduces to <code>succ (n+n)=0</code> and then tries again, realises that the nats are made with different constructors this time, and solves the goal. At least that's my understanding of what's going on.</p>

#### [ Kevin Buzzard (Jul 15 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129697236):
<blockquote>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">testit</span><span class="o">:</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">x</span><span class="o">,</span> <span class="o">((</span><span class="bp">λ</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="o">(</span><span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)),</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">)</span><span class="bp">+</span><span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">)))</span>
                         <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="n">x</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">→</span> <span class="mi">3</span><span class="bp">=</span><span class="mi">4</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">H</span><span class="bp">⟩</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span> <span class="n">at</span> <span class="n">H</span><span class="bp">;</span> <span class="n">cases</span> <span class="n">H</span>
</pre></div>


</blockquote>
<p>You lose a point for proof instability</p>

#### [ Kevin Buzzard (Jul 15 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129697237):
<p>When Leo removes <code>add_assoc</code> from simp you're in trouble</p>

#### [ Kenny Lau (Jul 15 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129697238):
<p>you sound like Mario</p>

#### [ Kevin Buzzard (Jul 15 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129697240):
<p>I'm practising.</p>

#### [ Kenny Lau (Jul 15 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129697246):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">testit</span><span class="o">:</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">x</span><span class="o">,</span> <span class="o">((</span><span class="bp">λ</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="o">(</span><span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)),</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">)</span><span class="bp">+</span><span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">)))</span>
                         <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="n">x</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">→</span> <span class="mi">3</span><span class="bp">=</span><span class="mi">4</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">H</span><span class="bp">⟩</span><span class="o">,</span> <span class="k">by</span> <span class="n">cases</span> <span class="n">x</span><span class="bp">;</span> <span class="n">injections</span>
</pre></div>

#### [ Kevin Buzzard (Jul 15 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129697293):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">testit4</span><span class="o">:</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">x</span><span class="o">,</span> <span class="o">((</span><span class="bp">λ</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="o">(</span><span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)),</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">)</span><span class="bp">+</span><span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">)))</span>
                         <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="n">x</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">→</span> <span class="mi">3</span><span class="bp">=</span><span class="mi">4</span>
<span class="bp">|</span> <span class="bp">⟨</span><span class="mi">0</span><span class="o">,</span> <span class="n">H</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">injections</span>
</pre></div>

#### [ Mario Carneiro (Jul 15 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129697294):
<p>yes, <code>cases</code> basically has <code>injection</code> built in</p>

#### [ Kevin Buzzard (Jul 15 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129697296):
<p>I don't think I'd internalised that before.</p>

#### [ Mario Carneiro (Jul 15 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129697336):
<p>That's what makes doing cases on an inductive predicate so powerful (like Coq's <code>inversion</code> tactic)</p>

#### [ Mario Carneiro (Jul 15 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129697339):
<p>because it can skip all the cases where the indices don't match up</p>

#### [ Kevin Buzzard (Jul 15 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129697344):
<p>That's funny, because last week my son discovered this. IIRC <code>inversion</code> is introduced in Software Foundations well after <code>cases</code> and in Lean you can just do cases anyway. I think that when I did those exercises in Lean myself I was still at the "let's try <code>cases;simp</code> and see if it works" stage.</p>

#### [ Kevin Buzzard (Jul 15 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129697434):
<p>In my experiments trying to understand <code>cases</code> on <code>eq</code> I found that it could be used to do a rewrite for either the left or the right hand side (<code>cases a = blah</code> and <code>cases blah = a</code> both remove <code>a</code> and substitute <code>blah</code> everywhere). The only disconcerting thing is that the order of the hypotheses gets randomised a bit (presumably because they're reverted and then unreverted under the hood or something)</p>


{% endraw %}
