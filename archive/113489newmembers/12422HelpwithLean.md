---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/12422HelpwithLean.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [Help with Lean](https://leanprover-community.github.io/archive/113489newmembers/12422HelpwithLean.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Ken Roe (Jul 10 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Help%20with%20Lean/near/129411503):
<p>I just started using Lean.  Can someone help me by telling me what I need to replace "sorry" with to prove this theorem:</p>
<p>def beq_nat : ℕ → ℕ → bool<br>
| beq_nat 0 0 := tt<br>
| beq_nat (x+1) (y+1) := (beq_nat x y)<br>
| beq_nat a b := ff</p>
<p>example : beq_nat 3 3=tt := by sorry.</p>

#### [ Kenny Lau (Jul 10 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Help%20with%20Lean/near/129411598):
<p>your definition does not compile</p>

#### [ Patrick Massot (Jul 10 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Help%20with%20Lean/near/129411605):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">beq_nat</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">bool</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">tt</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">x</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="n">y</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="n">beq_nat</span> <span class="n">x</span> <span class="n">y</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">a</span> <span class="n">b</span> <span class="o">:=</span> <span class="n">ff</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">beq_nat</span> <span class="mi">3</span> <span class="mi">3</span><span class="bp">=</span><span class="n">tt</span> <span class="o">:=</span> <span class="n">rfl</span>
</pre></div>

#### [ Patrick Massot (Jul 10 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Help%20with%20Lean/near/129411633):
<p>strange definition</p>

#### [ Kenny Lau (Jul 10 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Help%20with%20Lean/near/129411644):
<p>I don't think it's strange</p>

#### [ Kenny Lau (Jul 10 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Help%20with%20Lean/near/129411649):
<p>it's a viable way to prove that equality is decidable</p>

#### [ Patrick Massot (Jul 10 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Help%20with%20Lean/near/129411658):
<p>it's less efficient than using the maths preamble</p>

#### [ Ken Roe (Jul 10 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Help%20with%20Lean/near/129411729):
<p>I get the following using "rfl":</p>
<p>impHeap.lean:35:28: error<br>
type mismatch, term<br>
  rfl<br>
has type<br>
  ?m_2 = ?m_2<br>
but is expected to have type<br>
  beq_nat 3 3 = tt</p>

#### [ Kenny Lau (Jul 10 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Help%20with%20Lean/near/129411741):
<p>we changed the definition</p>

#### [ Kenny Lau (Jul 10 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Help%20with%20Lean/near/129411747):
<p>your original definition does not compile</p>

#### [ Ken Roe (Jul 10 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Help%20with%20Lean/near/129411943):
<p>How do I fix the definition?</p>

#### [ Patrick Massot (Jul 10 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Help%20with%20Lean/near/129411945):
<p>see my message</p>

#### [ Kenny Lau (Jul 10 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Help%20with%20Lean/near/129411946):
<p>we already gave you the new definition</p>

#### [ Kenny Lau (Jul 10 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Help%20with%20Lean/near/129411966):
<blockquote>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">beq_nat</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">bool</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">tt</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">x</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="n">y</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="n">beq_nat</span> <span class="n">x</span> <span class="n">y</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">a</span> <span class="n">b</span> <span class="o">:=</span> <span class="n">ff</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">beq_nat</span> <span class="mi">3</span> <span class="mi">3</span><span class="bp">=</span><span class="n">tt</span> <span class="o">:=</span> <span class="n">rfl</span>
</pre></div>


</blockquote>
<p><span class="emoji emoji-261d" title="point up">:point_up:</span> <a href="#narrow/stream/113489-new-members/subject/Help.20with.20Lean/near/129411605" title="#narrow/stream/113489-new-members/subject/Help.20with.20Lean/near/129411605">https://leanprover.zulipchat.com/#narrow/stream/113489-new-members/subject/Help.20with.20Lean/near/129411605</a></p>

#### [ Ken Roe (Jul 10 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Help%20with%20Lean/near/129412219):
<p>Thanks--didn't notice they were different.  It appears the syntax for recursive definitions changed from Lean 2.0.  This definition (copied from the Lean 2.0 tutorial) also fails:</p>
<p>definition fib : nat → nat<br>
| fib 0     := 1<br>
| fib 1     := 1<br>
| fib (a+2) := fib (a+1) + fib a</p>

#### [ Kenny Lau (Jul 10 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Help%20with%20Lean/near/129412223):
<p>how old is Lean 2.0 lol</p>

#### [ Kenny Lau (Jul 10 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Help%20with%20Lean/near/129412266):
<p>I don't think I ever used Lean 2.0</p>

#### [ Kenny Lau (Jul 10 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Help%20with%20Lean/near/129412274):
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">fib</span> <span class="o">:</span> <span class="n">nat</span> <span class="bp">→</span> <span class="n">nat</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="o">:=</span> <span class="mi">1</span>
<span class="bp">|</span> <span class="mi">1</span> <span class="o">:=</span> <span class="mi">1</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">a</span><span class="bp">+</span><span class="mi">2</span><span class="o">)</span> <span class="o">:=</span> <span class="n">fib</span> <span class="o">(</span><span class="n">a</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="bp">+</span> <span class="n">fib</span> <span class="n">a</span>
</pre></div>

#### [ Patrick Massot (Jul 10 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Help%20with%20Lean/near/129416618):
<p>You shouldn't be reading anything written for Lean 2. This is all difficult enough without adding this layer of confusion. Reading <a href="https://leanprover.github.io/theorem_proving_in_lean/" target="_blank" title="https://leanprover.github.io/theorem_proving_in_lean/">https://leanprover.github.io/theorem_proving_in_lean/</a> will already bring you a long way</p>


{% endraw %}
