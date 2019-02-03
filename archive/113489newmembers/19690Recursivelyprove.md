---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/19690Recursivelyprove.html
---

## Stream: [new members](index.html)
### Topic: [Recursively prove](19690Recursivelyprove.html)

---


{% raw %}
#### [ AHan (Nov 03 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Recursively%20prove/near/137105029):
<p>Sorry, this might seems to be stupid, but I just can't figure out how to prove the problem inductively....</p>
<p><code>lemma add_nat_ge_self {a :  ℕ} (b : ℕ) : a + b ≥ b :=
  match b with
  | 0 := begin simp, apply nat.zero_le end
  | succ n := sorry</code></p>

#### [ Mario Carneiro (Nov 03 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Recursively%20prove/near/137107106):
<p>In lean we write inductive definitions by pattern matching in the definition itself, not using match blocks like coq</p>

#### [ Mario Carneiro (Nov 03 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Recursively%20prove/near/137107116):
<div class="codehilite"><pre><span></span>lemma add_nat_ge_self {a :  ℕ} : ∀(b : ℕ), a + b ≥ b
| 0 := begin simp, apply nat.zero_le end
| (succ n) := sorry
</pre></div>

#### [ Mario Carneiro (Nov 03 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Recursively%20prove/near/137107156):
<p>at the <code>sorry</code> you should now have access to <code>add_nat_ge_self</code> which you can apply recursively</p>

#### [ Bryan Gin-ge Chen (Nov 03 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Recursively%20prove/near/137113734):
<p>What Mario wrote is cleaner but I want to point out that the following is probably what you were going for:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">add_nat_ge_self</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span>  <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">b</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">+</span> <span class="n">b</span> <span class="bp">≥</span> <span class="n">b</span> <span class="o">:=</span>
  <span class="k">match</span> <span class="n">a</span><span class="o">,</span> <span class="n">b</span> <span class="k">with</span>
  <span class="bp">|</span> <span class="n">a</span><span class="o">,</span> <span class="mi">0</span> <span class="o">:=</span> <span class="k">begin</span> <span class="n">simp</span><span class="o">,</span> <span class="n">apply</span> <span class="n">nat</span><span class="bp">.</span><span class="n">zero_le</span> <span class="kn">end</span>
  <span class="bp">|</span> <span class="n">a</span><span class="o">,</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>
  <span class="kn">end</span>
</pre></div>

#### [ Mario Carneiro (Nov 03 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Recursively%20prove/near/137113794):
<p>well if you write it like that you won't be able to fill in the <code>sorry</code> because you don't have access to the recursive function</p>

#### [ Bryan Gin-ge Chen (Nov 03 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Recursively%20prove/near/137114175):
<p>It's there, but it gets a funny name:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">add_nat_ge_self</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span>  <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">b</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">+</span> <span class="n">b</span> <span class="bp">≥</span> <span class="n">b</span> <span class="o">:=</span>
<span class="k">match</span> <span class="n">a</span><span class="o">,</span> <span class="n">b</span> <span class="k">with</span>
<span class="bp">|</span> <span class="n">a</span><span class="o">,</span> <span class="mi">0</span> <span class="o">:=</span> <span class="k">begin</span> <span class="n">simp</span><span class="o">,</span> <span class="n">apply</span> <span class="n">nat</span><span class="bp">.</span><span class="n">zero_le</span> <span class="kn">end</span>
<span class="bp">|</span> <span class="n">a</span><span class="o">,</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span> <span class="k">begin</span>
  <span class="n">refine</span> <span class="n">nat</span><span class="bp">.</span><span class="n">succ_le_succ</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">exact</span> <span class="bp">_</span><span class="n">match</span> <span class="n">a</span> <span class="n">n</span>
<span class="kn">end</span>
<span class="kn">end</span>
</pre></div>

#### [ Bryan Gin-ge Chen (Nov 03 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Recursively%20prove/near/137114468):
<p>And I guess you only get access to it if you go into tactic mode; i.e. I can't remove the <code>by exact</code> below:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">add_nat_ge_self</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span>  <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">b</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">+</span> <span class="n">b</span> <span class="bp">≥</span> <span class="n">b</span> <span class="o">:=</span>
<span class="k">match</span> <span class="n">a</span><span class="o">,</span> <span class="n">b</span> <span class="k">with</span>
<span class="bp">|</span> <span class="n">a</span><span class="o">,</span> <span class="mi">0</span> <span class="o">:=</span> <span class="k">begin</span> <span class="n">simp</span><span class="o">,</span> <span class="n">apply</span> <span class="n">nat</span><span class="bp">.</span><span class="n">zero_le</span> <span class="kn">end</span>
<span class="bp">|</span> <span class="n">a</span><span class="o">,</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span> <span class="n">nat</span><span class="bp">.</span><span class="n">succ_le_succ</span> <span class="o">(</span><span class="k">by</span> <span class="n">exact</span> <span class="bp">_</span><span class="n">match</span> <span class="n">a</span> <span class="n">n</span><span class="o">)</span>
<span class="kn">end</span>
</pre></div>

#### [ AHan (Nov 04 2018 at 04:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Recursively%20prove/near/137140650):
<p>Oh!! Thanks a lot for the explanation!!</p>


{% endraw %}
