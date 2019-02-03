---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/55185Proptobool.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [Prop to bool](https://leanprover-community.github.io/archive/113489newmembers/55185Proptobool.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Olli (Sep 11 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prop%20to%20bool/near/133728628):
<p>I'm sure this will be covered later in the book, but I was wondering if there is a quick explanation for why I can't turn this <code>prime</code> Prop into a bool?</p>
<div class="codehilite"><pre><span></span><span class="kn">namespace</span> <span class="n">hidden</span>

<span class="kn">open</span> <span class="n">classical</span>
<span class="kn">open</span> <span class="n">decidable</span>
<span class="n">local</span> <span class="n">attribute</span> <span class="o">[</span><span class="kn">instance</span><span class="o">]</span> <span class="n">prop_decidable</span>

<span class="n">def</span> <span class="n">divides</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="bp">∃</span> <span class="n">k</span><span class="o">,</span> <span class="n">m</span> <span class="bp">*</span> <span class="n">k</span> <span class="bp">=</span> <span class="n">n</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">has_dvd</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">divides</span><span class="bp">⟩</span>

<span class="kn">variables</span> <span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span>

<span class="n">def</span> <span class="n">prime</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="n">n</span> <span class="bp">≥</span> <span class="mi">2</span> <span class="bp">∧</span> <span class="bp">∀</span> <span class="n">k</span><span class="o">,</span> <span class="n">k</span> <span class="err">∣</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">k</span> <span class="bp">=</span> <span class="mi">1</span> <span class="bp">∨</span> <span class="n">k</span> <span class="bp">=</span> <span class="n">n</span>

<span class="bp">#</span><span class="n">reduce</span> <span class="n">prime</span> <span class="mi">5</span>
<span class="c1">-- nat.less_than_or_equal 2 5 ∧ ∀ (k : ℕ), (∃ (k_1 : ℕ), nat.mul k k_1 = 5) → k = 1 ∨ k = 5</span>

<span class="bp">#</span><span class="kn">eval</span> <span class="n">to_bool</span> <span class="err">$</span> <span class="n">prime</span> <span class="mi">5</span>
<span class="c1">-- code generation failed, VM does not have code for &#39;classical.choice&#39;</span>

<span class="kn">end</span> <span class="n">hidden</span>
</pre></div>

#### [ Kenny Lau (Sep 11 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prop%20to%20bool/near/133729533):
<p>if you remove <code>local attribute [instance] prop_decidable</code> then it should be fine</p>

#### [ Olli (Sep 11 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prop%20to%20bool/near/133729720):
<p>I get:</p>
<div class="codehilite"><pre><span></span>failed to synthesize type class instance for
m n : ℕ
⊢ decidable (prime 5)
</pre></div>

#### [ Chris Hughes (Sep 11 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prop%20to%20bool/near/133729749):
<p>You need <code>prime</code> to be a decidable proposition.</p>

#### [ Chris Hughes (Sep 11 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prop%20to%20bool/near/133729757):
<p>Lean doesn't know how to check whether 5 is prime.</p>

#### [ Kenny Lau (Sep 11 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prop%20to%20bool/near/133729766):
<p>oh, he defined prime by himself</p>

#### [ Kenny Lau (Sep 11 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prop%20to%20bool/near/133729769):
<p>I didn't notice</p>

#### [ Chris Hughes (Sep 11 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prop%20to%20bool/near/133729814):
<p>But it does know how to decide for the library definition of prime, so it should work for that.</p>

#### [ Olli (Sep 11 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prop%20to%20bool/near/133729861):
<p>I found a definition for <code>prime</code> in mathlib but nothing for it in the core library</p>

#### [ Chris Hughes (Sep 11 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prop%20to%20bool/near/133729875):
<p>There isn't one in core.</p>

#### [ Kevin Buzzard (Sep 11 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prop%20to%20bool/near/133731851):
<p>If you're going to roll your own <code>prime</code> then to do what you want to do you're also going to have to roll your own <code>prime.decidable</code> function giving an algorithm for testing primality. This is a good exercise; the way to do it is perhaps to search the source code for example of proofs of decidability, then figure out how to prove the key lemma (if n&gt;=1 and k divides n then k&lt;=n) and then write the algorithm. If you don't make it efficient then that's OK, you will have trouble working out if 617 is prime, but on the other hand at least the code will work (or it might give you a time-out the moment the numbers get too large to do on your fingers :-) )</p>

#### [ Olli (Sep 11 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prop%20to%20bool/near/133732019):
<p>yeah I think I should finish a few more chapters before attempting that</p>

#### [ Kevin Buzzard (Sep 11 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prop%20to%20bool/near/133734843):
<p>or use mathlib's <code>prime</code> :-)</p>


{% endraw %}
