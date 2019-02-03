---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/01810natsubtraction.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [nat subtraction](https://leanprover-community.github.io/archive/113489newmembers/01810natsubtraction.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Thomas (Dec 22 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152392979):
<p>I am a bit confused by the results of the following:</p>
<p>constants m n : ℕ<br>
#check m - n<br>
#eval 5 - 6</p>
<p>The check reports a natural number. The eval returns 0.</p>
<p>example (Q : ℕ → Prop) (m : ℕ) : (∀ n : ℕ, Q n) → ( ∀ n : ℕ, Q (n - m) ) :=<br>
    assume a1 : ∀ n : ℕ, Q n,<br>
        assume n : ℕ,<br>
        show Q (n - m), from a1 (n - m)</p>
<p>I did not expect that the substitution in the last line would be allowed, since n - m might not be a natural number.</p>

#### [ Johan Commelin (Dec 22 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152393031):
<p><code>n - m</code> is always a natural number. It is zero when you expect it to be negative.</p>

#### [ Kevin Buzzard (Dec 22 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152393174):
<p><code>-</code> is defined on <code>nat</code> for convenience, it's not the mathematical <code>-</code>. If you want to allow negative numbers, use <code>int</code>.</p>

#### [ Patrick Thomas (Dec 22 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152393219):
<p>Is there a way to override that? It does not seem like the proof I posted should be valid. I would like it to require that m &lt;= n.</p>

#### [ Kevin Buzzard (Dec 22 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152393233):
<p>I don't know what you mean by "override". You can't change the definition of <code>nat.sub</code> but you could define a new function if you like and I guess you could even redefine the notation <code>-</code> on <code>nat</code> to mean your new function. What do you actually want?</p>

#### [ Kevin Buzzard (Dec 22 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152393290):
<p>Remember that every function has to have a well-defined source and target type. <code>nat.sub</code> takes two nats and returns a nat.</p>

#### [ Patrick Thomas (Dec 22 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152393347):
<p>I guess I am just uncomfortable that the proof I posted is valid. It seems that it should require m &lt;= n.</p>

#### [ Kevin Buzzard (Dec 22 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152393353):
<p>Your example is about a function called <code>nat.sub</code></p>

#### [ Kevin Buzzard (Dec 22 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152393355):
<p>because you used the notation <code>-</code> on naturals and that's what it expands to</p>

#### [ Kevin Buzzard (Dec 22 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152393394):
<p>Whether or not you're uncomfortable, Lean is just doing what you told it to do. You still haven't made clear to me what you expect to happen.</p>

#### [ Kevin Buzzard (Dec 22 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152393410):
<p>You can change definitions or change notation or define new functions, you can make Lean behave the way you want it to behave, but your example as it stands is behaving normally because computer scientists had reasons for defining nat.sub the way they did.</p>

#### [ Kevin Buzzard (Dec 22 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152393424):
<p>Your example is <em>not</em> about usual mathematician's subtraction.</p>

#### [ Patrick Thomas (Dec 22 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152393472):
<p>Is there an existing function I could use to make it the usual mathematician's subtraction?</p>

#### [ Kevin Buzzard (Dec 22 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152393475):
<p><code>int.sub</code></p>

#### [ Kevin Buzzard (Dec 22 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152393488):
<p>This takes two ints and returns the int that you think it should return.</p>

#### [ Patrick Thomas (Dec 22 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152393546):
<p>I see. Thank you.</p>

#### [ Kevin Buzzard (Dec 22 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152393591):
<p>But note that a nat is not an int -- there is a function from nat to int which to a mathematician is "the obvious inclusion". In computer science nat and int are two different types and there's a map from nat to int which you have to somehow invoke, which makes things a little more complicated than a mathematician would feel that they should be.</p>

#### [ Kevin Buzzard (Dec 22 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152393599):
<p>NB notation for <code>int.sub</code> is just <code>-</code> again -- you just have to remember to feed ints to it and not nats. The notation <code>-</code> just figures out which <code>blah.sub</code> it should expand to depending on what you feed it.</p>

#### [ Kevin Buzzard (Dec 22 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152393602):
<div class="codehilite"><pre><span></span><span class="bp">#</span><span class="kn">eval</span> <span class="o">(</span><span class="mi">5</span> <span class="bp">-</span> <span class="mi">6</span><span class="o">)</span> <span class="c1">-- 0</span>
<span class="bp">#</span><span class="kn">eval</span> <span class="o">((</span><span class="mi">5</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="bp">-</span> <span class="mi">6</span><span class="o">)</span> <span class="c1">-- -1</span>
</pre></div>

#### [ Kevin Buzzard (Dec 22 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152393647):
<p><code>(5 : ℤ)</code> means "I mean the integer 5". The default 5 is the natural number 5.</p>

#### [ Patrick Thomas (Dec 22 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152393752):
<p>So in the example I posted I should introduce the assumption m &lt;= n and use it to show that 'int.sub_nat_nat n m' is a natural number, then use 'a1 (int.sub_nat_nat n m)'?</p>

#### [ Johan Commelin (Dec 22 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152393948):
<p>It's not so easy. Your function will return an <code>int</code>, which is never a <code>nat</code>.</p>

#### [ Johan Commelin (Dec 22 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152393957):
<p>You could however use a function that turns an <code>int</code> into a <code>nat</code>. But it will give you garbage for negative integers.</p>

#### [ Johan Commelin (Dec 22 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152393968):
<p>Alternatively, you can continue using natural numbers. And you can prove that it gives the "correct" result when <code>m &lt;= n</code>. (Such proofs already exist in mathlib.)</p>

#### [ Johan Commelin (Dec 22 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152394015):
<p>And then you just live with the fact that you also proved something else, something garbage. But who cares.</p>

#### [ Kevin Buzzard (Dec 22 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152395321):
<blockquote>
<p>and use it to show that <code>int.sub_nat_nat n m</code> is a natural number</p>
</blockquote>
<p>You have a misconception about what is going on. The integer 4 is <em>not</em> a natural number, it is a non-negative integer. It is a term of type int, and because in type theory every term has at most one type, the integer 4 is not a natural number; indeed in type theory it does not even make sense to ask whether the integer 4 and the natural number 4 are equal -- terms of different types cannot be equal.</p>

#### [ Kevin Buzzard (Dec 22 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152395333):
<p>On the other hand there is a map from the natural numbers to the integers, and a map (the absolute value function) from the integers to the naturals, so you can move between them -- but the moving has to be done.</p>

#### [ Kevin Buzzard (Dec 22 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152395375):
<p>In particular, <code>a1 x</code> will never work if <code>a1</code> is expecting a natural and <code>x</code> is an integer, even if <code>x</code> is non-negative.</p>

#### [ Patrick Thomas (Dec 22 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152397122):
<p>So there is a function that takes a positive integer and returns a natural number?</p>

#### [ Johan Commelin (Dec 22 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152397163):
<p>No, same reason as above.</p>

#### [ Kevin Buzzard (Dec 22 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152397166):
<p><code>int.nat_abs</code> takes an arbitrary integer and returns a natural number.</p>

#### [ Kevin Buzzard (Dec 22 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152397175):
<p>and if you feed it a non-negative integer, it will return the corresponding natural number.</p>

#### [ Kevin Buzzard (Dec 22 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152397230):
<p>Type theory likes total functions, and this is a bit weird for mathematicians. For example the square root function just goes from the reals to the reals -- if you feed it a non-negative real then it returns its non-negative square root, and if you feed it a negative real then it just returns some junk, maybe 0, maybe the square root of the absolute value -- as a mathematician I don't care what it returns because I never apply this function unless the input is non-negative. It's just a different way of looking at things. Took me a while to get used to.</p>

#### [ Patrick Thomas (Dec 22 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152398558):
<p>Would this be a better approach then:<br>
example (Q : ℤ → Prop) (m : ℤ) (m ≥ 0) : (∀ n : ℤ, (n ≥ 0) → Q n) → ( ∀ n : ℤ, (n ≥ m) → Q (n - m) ) := ...</p>

#### [ Johan Commelin (Dec 22 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152398876):
<p>The better approach is to accept the fact that your theorem might have some garbage edge cases. It will create more elegant proofs, and it will create lemmas that are easier to use in other proofs.</p>

#### [ Patrick Thomas (Dec 22 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152399842):
<p>How do you avoid the risk of misinterpreting the theorem? Isn't it good to make it as explicit as possible?</p>

#### [ Johan Commelin (Dec 22 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152400178):
<p>If you want you can use the "garbage-include" version to prove the explicit morally-mathematically-correct version. That shouldn't be hard.</p>

#### [ Mario Carneiro (Dec 22 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152400288):
<p>There is no risk of the theorem being wrong, since lean is checking that. More than likely, if you try to prove anything nontrivial using <code>n - m : nat</code> you will naturally end up needing <code>m &lt;= n</code> at some point, and so you add it to the theorem hypothesis and the garbage is excluded. In this particular case, you never needed this assumption, so it's true even in the "garbage case". You can add the assumption anyway if you want, or not.</p>

#### [ Patrick Thomas (Dec 22 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152401340):
<p>I guess it is primarily a matter of not being aware of what the axioms are or how type theory works. I am a little worried that I may run into other unexpected cases. Maybe there is no easy way to avoid that?</p>

#### [ Patrick Thomas (Dec 22 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152401644):
<p>This came from my attempt to prove that the Principle of Induction implies the Principle of Induction from a Starting Point and being able to leave out m &lt;= n in the consequent. This feels somewhat nontrivial?</p>

#### [ Mario Carneiro (Dec 22 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152402330):
<p>What is the real theorem you want to state? What you quoted doesn't look like the principle of induction from a starting point</p>

#### [ Patrick Thomas (Dec 22 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152403321):
<div class="codehilite"><pre><span></span><span class="c1">-- Principle of Induction</span>
<span class="n">def</span> <span class="n">ind_1</span> <span class="o">:=</span>
<span class="o">(</span> <span class="bp">∀</span> <span class="n">P</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">,</span>
    <span class="o">(</span> <span class="o">(</span> <span class="n">P</span> <span class="mi">0</span> <span class="bp">∧</span> <span class="o">(</span> <span class="bp">∀</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="o">(</span><span class="n">P</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">P</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">))</span> <span class="o">)</span> <span class="o">)</span> <span class="bp">→</span>
    <span class="o">(</span> <span class="bp">∀</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="n">P</span> <span class="n">n</span> <span class="o">)</span> <span class="o">)</span>
<span class="o">)</span>

<span class="c1">-- Principle of Induction from a Starting Point</span>
<span class="n">def</span> <span class="n">ind_2</span> <span class="o">:=</span>
<span class="o">(</span> <span class="bp">∀</span> <span class="n">Q</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">,</span>
    <span class="bp">∀</span> <span class="n">m</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="o">(</span> <span class="o">(</span> <span class="n">Q</span> <span class="n">m</span> <span class="bp">∧</span> <span class="o">(</span> <span class="bp">∀</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="o">(</span> <span class="o">(</span> <span class="n">n</span> <span class="bp">≥</span> <span class="n">m</span> <span class="o">)</span> <span class="bp">→</span> <span class="o">(</span> <span class="n">Q</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">Q</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="o">)</span> <span class="o">)</span> <span class="o">)</span> <span class="o">)</span> <span class="bp">→</span>
    <span class="o">(</span> <span class="bp">∀</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="o">(</span> <span class="o">(</span> <span class="n">n</span> <span class="bp">≥</span> <span class="n">m</span> <span class="o">)</span> <span class="bp">→</span> <span class="n">Q</span> <span class="n">n</span> <span class="o">)</span> <span class="o">)</span> <span class="o">)</span>
<span class="o">)</span>

<span class="c1">-- Principle of Induction -&gt; Principle of Induction from a Starting Point</span>
<span class="kn">example</span> <span class="o">:</span> <span class="n">ind_1</span> <span class="bp">→</span> <span class="n">ind_2</span> <span class="o">:=</span>
    <span class="k">assume</span> <span class="n">a1</span> <span class="o">:</span> <span class="n">ind_1</span><span class="o">,</span>
        <span class="k">assume</span> <span class="n">Q</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">,</span>
            <span class="k">assume</span> <span class="n">m</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span>
                <span class="k">assume</span> <span class="n">a2</span> <span class="o">:</span> <span class="o">(</span> <span class="n">Q</span> <span class="n">m</span> <span class="bp">∧</span> <span class="o">(</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="o">(</span> <span class="o">(</span> <span class="n">n</span> <span class="bp">≥</span> <span class="n">m</span> <span class="o">)</span> <span class="bp">→</span> <span class="o">(</span> <span class="n">Q</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">Q</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="o">)</span> <span class="o">)</span> <span class="o">)</span> <span class="o">),</span>
                <span class="k">have</span> <span class="n">s1</span> <span class="o">:</span> <span class="n">Q</span> <span class="n">m</span><span class="o">,</span> <span class="k">from</span> <span class="n">and</span><span class="bp">.</span><span class="n">left</span> <span class="n">a2</span><span class="o">,</span>
                <span class="k">have</span> <span class="n">s2</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="o">(</span> <span class="o">(</span> <span class="n">n</span> <span class="bp">≥</span> <span class="n">m</span> <span class="o">)</span> <span class="bp">→</span> <span class="o">(</span> <span class="n">Q</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">Q</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="o">)</span> <span class="o">),</span> <span class="k">from</span> <span class="n">and</span><span class="bp">.</span><span class="n">right</span> <span class="n">a2</span><span class="o">,</span>
                <span class="k">have</span> <span class="n">s3</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="o">(</span> <span class="n">Q</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="n">n</span><span class="o">)</span> <span class="bp">→</span> <span class="n">Q</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">))</span> <span class="o">),</span> <span class="k">from</span>
                    <span class="k">assume</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span>
                    <span class="k">have</span> <span class="n">s4</span> <span class="o">:</span> <span class="o">(</span> <span class="o">(</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="n">n</span><span class="o">)</span> <span class="bp">≥</span> <span class="n">m</span> <span class="o">)</span> <span class="bp">→</span> <span class="o">(</span> <span class="n">Q</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="n">n</span><span class="o">)</span> <span class="bp">→</span> <span class="n">Q</span> <span class="o">((</span><span class="n">m</span> <span class="bp">+</span> <span class="n">n</span><span class="o">)</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">))</span> <span class="o">),</span> <span class="k">from</span> <span class="n">s2</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="n">n</span><span class="o">),</span>
                    <span class="k">have</span> <span class="n">s5</span> <span class="o">:</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="n">n</span><span class="o">)</span> <span class="bp">≥</span> <span class="n">m</span><span class="o">,</span> <span class="k">from</span> <span class="n">sorry</span><span class="o">,</span>
                    <span class="k">have</span> <span class="n">s6</span> <span class="o">:</span> <span class="o">(</span> <span class="n">Q</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="n">n</span><span class="o">)</span> <span class="bp">→</span> <span class="n">Q</span> <span class="o">((</span><span class="n">m</span> <span class="bp">+</span> <span class="n">n</span><span class="o">)</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="o">),</span> <span class="k">from</span> <span class="n">s4</span> <span class="n">s5</span><span class="o">,</span>
                    <span class="k">show</span> <span class="o">(</span> <span class="n">Q</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="n">n</span><span class="o">)</span> <span class="bp">→</span> <span class="n">Q</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">))</span> <span class="o">),</span> <span class="k">from</span> <span class="n">s6</span><span class="o">,</span>
                <span class="k">let</span> <span class="n">P&#39;</span> <span class="o">:=</span> <span class="k">fun</span> <span class="n">n</span><span class="o">,</span> <span class="n">Q</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="n">n</span><span class="o">)</span> <span class="k">in</span>
                <span class="k">have</span> <span class="n">s7</span> <span class="o">:(</span> <span class="o">(</span> <span class="n">P&#39;</span> <span class="mi">0</span> <span class="bp">∧</span> <span class="o">(</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="o">(</span> <span class="n">P&#39;</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">P&#39;</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="o">)</span> <span class="o">)</span> <span class="o">)</span> <span class="bp">→</span> <span class="o">(</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="n">P&#39;</span> <span class="n">n</span> <span class="o">)</span> <span class="o">),</span> <span class="k">from</span> <span class="n">a1</span> <span class="n">P&#39;</span><span class="o">,</span>
                <span class="k">have</span> <span class="n">s8</span> <span class="o">:</span> <span class="n">P&#39;</span> <span class="mi">0</span><span class="o">,</span> <span class="k">from</span> <span class="n">s1</span><span class="o">,</span>
                <span class="k">have</span> <span class="n">s9</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="o">(</span> <span class="n">P&#39;</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">P&#39;</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="o">),</span> <span class="k">from</span> <span class="n">s3</span><span class="o">,</span>
                <span class="k">have</span> <span class="n">s10</span> <span class="o">:</span> <span class="n">P&#39;</span> <span class="mi">0</span> <span class="bp">∧</span> <span class="o">(</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="o">(</span> <span class="n">P&#39;</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">P&#39;</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="o">)</span> <span class="o">),</span> <span class="k">from</span> <span class="n">and</span><span class="bp">.</span><span class="n">intro</span> <span class="n">s8</span> <span class="n">s9</span><span class="o">,</span>
                <span class="k">have</span> <span class="n">s11</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="n">P&#39;</span> <span class="n">n</span><span class="o">,</span> <span class="k">from</span> <span class="n">s7</span> <span class="n">s10</span><span class="o">,</span>
                <span class="k">have</span> <span class="n">s12</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="n">Q</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="n">n</span><span class="o">),</span> <span class="k">from</span> <span class="n">s11</span><span class="o">,</span>
                    <span class="k">assume</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span>
                        <span class="k">assume</span> <span class="n">a3</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">≥</span> <span class="n">m</span><span class="o">,</span>
                        <span class="k">have</span> <span class="n">s14</span> <span class="o">:</span> <span class="n">Q</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="o">(</span><span class="n">n</span> <span class="bp">-</span> <span class="n">m</span><span class="o">)),</span> <span class="k">from</span> <span class="n">s12</span> <span class="o">(</span><span class="n">n</span> <span class="bp">-</span> <span class="n">m</span><span class="o">),</span> <span class="c1">-- did not expect to work</span>
                        <span class="k">show</span> <span class="n">Q</span> <span class="n">n</span><span class="o">,</span> <span class="k">from</span> <span class="n">sorry</span>
</pre></div>

#### [ Kevin Buzzard (Dec 22 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152403526):
<p>To write code on this forum enclose it in three backticks <code> ``` </code></p>

#### [ Kevin Buzzard (Dec 22 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152403577):
<p>Even better write <code> ```lean </code> for the first one and  it'll do syntax highlighting</p>

#### [ Mark Dickinson (Dec 22 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152403963):
<p>So if it helps at all, to resolve your last <code>sorry</code> you're going to need to show that <code>m + (n - m) = n</code>. And that will need the hypothesis that <code>n ≥ m</code>.</p>

#### [ Mario Carneiro (Dec 22 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152403968):
<blockquote>
<div class="codehilite"><pre><span></span><span class="k">have</span> <span class="n">s14</span> <span class="o">:</span> <span class="n">Q</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="o">(</span><span class="n">n</span> <span class="bp">-</span> <span class="n">m</span><span class="o">)),</span> <span class="k">from</span> <span class="n">s12</span> <span class="o">(</span><span class="n">n</span> <span class="bp">-</span> <span class="n">m</span><span class="o">),</span> <span class="c1">-- did not expect to work</span>
<span class="k">show</span> <span class="n">Q</span> <span class="n">n</span><span class="o">,</span> <span class="k">from</span> <span class="n">sorry</span>
</pre></div>


</blockquote>
<p>You may not have expected the first line to work, but I think you will be vindicated when you do the second line</p>

#### [ Patrick Thomas (Dec 22 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152404182):
<p>Why does <code>m + (n - m) = n</code> require <code>n &gt;= m</code>?</p>

#### [ Mark Dickinson (Dec 22 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152404225):
<p>You may also want to look at <code>nat.less_than_or_equal.rec</code> at some point. It probably doesn't help here, if this is a learning exercise, but it was an "aha" moment for me (as a Lean newcomer) to understand why the recursion principle for <code>nat.less_than_or_equal</code> is pretty much exactly induction from a starting point.</p>

#### [ Mario Carneiro (Dec 22 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152404226):
<p>because if <code>m &gt; n</code>, then <em>since <code>n - m</code> is a natural number and hence is <code>&gt;= 0</code></em>, we cannot possibly have <code>m + (something nonnegative) = n</code>.</p>

#### [ Mario Carneiro (Dec 22 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152404235):
<p>the fact that <code>n - m</code> is a natural number is purely a fact of its type, it is impossible for any term of that type to not be nonnegative</p>

#### [ Mario Carneiro (Dec 22 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152404278):
<p>If we want to have a function <code>sub : nat -&gt; nat -&gt; nat</code> (and we do), it must not behave like regular subtraction everywhere. We do the next best thing and make it 0 when it ought to be negative</p>

#### [ Mario Carneiro (Dec 22 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152404285):
<p>Not sure if it helps, but the natural number subtraction operation is called <a href="https://en.wikipedia.org/wiki/Monus" target="_blank" title="https://en.wikipedia.org/wiki/Monus">monus</a> in regular maths</p>

#### [ Patrick Thomas (Dec 22 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152405626):
<p>Is there an easy way to find the theorems for <code>(m + n) ≥ m</code> and <code>m + (n - m) = n</code>?</p>

#### [ Mario Carneiro (Dec 23 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152406036):
<p>They are all in <code>init.data.nat.lemmas</code> and <code>data.nat.basic</code>. You can browse those files, or try to guess the names like <code>nat.add_sub_...</code> in the autocompletion</p>

#### [ Mario Carneiro (Dec 23 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152406038):
<p>the first one is <code>nat.le_add_left</code></p>

#### [ Mark Dickinson (Dec 23 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152406173):
<p>... and the second is <code>nat.sub_add_cancel</code> (<code>∀ {n m : ℕ}, n ≥ m → n - m + m = n</code>'), modulo a use of commutativity of addition.</p>

#### [ Patrick Thomas (Dec 23 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152406223):
<p>Thank you.</p>

#### [ Mario Carneiro (Dec 23 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152406229):
<p>the commutated version should also be there</p>

#### [ Mark Dickinson (Dec 23 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152406232):
<p>Ah, looks like it's also exactly <code>nat.add_sub_cancel'</code>, from mathlib.</p>

#### [ Mark Dickinson (Dec 23 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152406293):
<p>... and <code>nat.add_sub_of_le</code> from the standard library</p>

#### [ Patrick Thomas (Dec 23 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20subtraction/near/152408358):
<p>Completed proof:</p>
<div class="codehilite"><pre><span></span><span class="kn">open</span> <span class="n">nat</span>


<span class="c1">-- Principle of Induction</span>
<span class="n">def</span> <span class="n">ind_1</span> <span class="o">:=</span>
<span class="bp">∀</span> <span class="n">P</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">,</span>
    <span class="n">P</span> <span class="mi">0</span> <span class="bp">∧</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="n">P</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">P</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">))</span> <span class="bp">→</span>
    <span class="bp">∀</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="n">P</span> <span class="n">n</span>


<span class="c1">-- Principle of Induction from a Starting Point</span>
<span class="n">def</span> <span class="n">ind_2</span> <span class="o">:=</span>
<span class="bp">∀</span> <span class="n">Q</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">,</span>
    <span class="bp">∀</span> <span class="n">m</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="o">(</span>
        <span class="o">(</span> <span class="n">Q</span> <span class="n">m</span> <span class="bp">∧</span> <span class="o">(</span> <span class="bp">∀</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="o">(</span><span class="n">n</span> <span class="bp">≥</span> <span class="n">m</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="n">Q</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">Q</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">))</span> <span class="o">)</span> <span class="o">)</span> <span class="bp">→</span>
        <span class="o">(</span> <span class="bp">∀</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="o">(</span><span class="n">n</span> <span class="bp">≥</span> <span class="n">m</span><span class="o">)</span> <span class="bp">→</span> <span class="n">Q</span> <span class="n">n</span> <span class="o">)</span>
    <span class="o">)</span>


<span class="c1">-- Principle of Induction -&gt; Principle of Induction from a Starting Point</span>
<span class="kn">example</span> <span class="o">:</span> <span class="n">ind_1</span> <span class="bp">→</span> <span class="n">ind_2</span> <span class="o">:=</span>
    <span class="k">assume</span> <span class="n">a1</span> <span class="o">:</span> <span class="n">ind_1</span><span class="o">,</span>
        <span class="k">assume</span> <span class="n">Q</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">,</span>
            <span class="k">assume</span> <span class="n">m</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span>
                <span class="k">assume</span> <span class="n">a2</span> <span class="o">:</span> <span class="o">(</span> <span class="n">Q</span> <span class="n">m</span> <span class="bp">∧</span> <span class="o">(</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="o">(</span> <span class="o">(</span> <span class="n">n</span> <span class="bp">≥</span> <span class="n">m</span> <span class="o">)</span> <span class="bp">→</span> <span class="o">(</span> <span class="n">Q</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">Q</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="o">)</span> <span class="o">)</span> <span class="o">)</span> <span class="o">),</span>
                <span class="k">have</span> <span class="n">s1</span> <span class="o">:</span> <span class="n">Q</span> <span class="n">m</span><span class="o">,</span> <span class="k">from</span> <span class="n">and</span><span class="bp">.</span><span class="n">left</span> <span class="n">a2</span><span class="o">,</span>
                <span class="k">have</span> <span class="n">s2</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="o">(</span> <span class="o">(</span> <span class="n">n</span> <span class="bp">≥</span> <span class="n">m</span> <span class="o">)</span> <span class="bp">→</span> <span class="o">(</span> <span class="n">Q</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">Q</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="o">)</span> <span class="o">),</span> <span class="k">from</span> <span class="n">and</span><span class="bp">.</span><span class="n">right</span> <span class="n">a2</span><span class="o">,</span>
                <span class="k">have</span> <span class="n">s3</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="o">(</span> <span class="n">Q</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="n">n</span><span class="o">)</span> <span class="bp">→</span> <span class="n">Q</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">))</span> <span class="o">),</span> <span class="k">from</span>
                    <span class="k">assume</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span>
                    <span class="k">have</span> <span class="n">s4</span> <span class="o">:</span> <span class="o">(</span> <span class="o">(</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="n">n</span><span class="o">)</span> <span class="bp">≥</span> <span class="n">m</span> <span class="o">)</span> <span class="bp">→</span> <span class="o">(</span> <span class="n">Q</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="n">n</span><span class="o">)</span> <span class="bp">→</span> <span class="n">Q</span> <span class="o">((</span><span class="n">m</span> <span class="bp">+</span> <span class="n">n</span><span class="o">)</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">))</span> <span class="o">),</span> <span class="k">from</span> <span class="n">s2</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="n">n</span><span class="o">),</span>
                    <span class="k">have</span> <span class="n">s5</span> <span class="o">:</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="n">n</span><span class="o">)</span> <span class="bp">≥</span> <span class="n">m</span><span class="o">,</span> <span class="k">from</span> <span class="n">le_add_right</span> <span class="n">m</span> <span class="n">n</span><span class="o">,</span>
                    <span class="k">have</span> <span class="n">s6</span> <span class="o">:</span> <span class="o">(</span> <span class="n">Q</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="n">n</span><span class="o">)</span> <span class="bp">→</span> <span class="n">Q</span> <span class="o">((</span><span class="n">m</span> <span class="bp">+</span> <span class="n">n</span><span class="o">)</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="o">),</span> <span class="k">from</span> <span class="n">s4</span> <span class="n">s5</span><span class="o">,</span>
                    <span class="k">show</span> <span class="o">(</span> <span class="n">Q</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="n">n</span><span class="o">)</span> <span class="bp">→</span> <span class="n">Q</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">))</span> <span class="o">),</span> <span class="k">from</span> <span class="n">s6</span><span class="o">,</span>
                <span class="k">let</span> <span class="n">P&#39;</span> <span class="o">:=</span> <span class="k">fun</span> <span class="n">n</span><span class="o">,</span> <span class="n">Q</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="n">n</span><span class="o">)</span> <span class="k">in</span>
                <span class="k">have</span> <span class="n">s7</span> <span class="o">:(</span> <span class="o">(</span> <span class="n">P&#39;</span> <span class="mi">0</span> <span class="bp">∧</span> <span class="o">(</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="o">(</span> <span class="n">P&#39;</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">P&#39;</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="o">)</span> <span class="o">)</span> <span class="o">)</span> <span class="bp">→</span> <span class="o">(</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="n">P&#39;</span> <span class="n">n</span> <span class="o">)</span> <span class="o">),</span> <span class="k">from</span> <span class="n">a1</span> <span class="n">P&#39;</span><span class="o">,</span>
                <span class="k">have</span> <span class="n">s8</span> <span class="o">:</span> <span class="n">P&#39;</span> <span class="mi">0</span><span class="o">,</span> <span class="k">from</span> <span class="n">s1</span><span class="o">,</span>
                <span class="k">have</span> <span class="n">s9</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="o">(</span> <span class="n">P&#39;</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">P&#39;</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="o">),</span> <span class="k">from</span> <span class="n">s3</span><span class="o">,</span>
                <span class="k">have</span> <span class="n">s10</span> <span class="o">:</span> <span class="n">P&#39;</span> <span class="mi">0</span> <span class="bp">∧</span> <span class="o">(</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="o">(</span> <span class="n">P&#39;</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">P&#39;</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="o">)</span> <span class="o">),</span> <span class="k">from</span> <span class="n">and</span><span class="bp">.</span><span class="n">intro</span> <span class="n">s8</span> <span class="n">s9</span><span class="o">,</span>
                <span class="k">have</span> <span class="n">s11</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="n">P&#39;</span> <span class="n">n</span><span class="o">,</span> <span class="k">from</span> <span class="n">s7</span> <span class="n">s10</span><span class="o">,</span>
                <span class="k">have</span> <span class="n">s12</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="n">Q</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="n">n</span><span class="o">),</span> <span class="k">from</span> <span class="n">s11</span><span class="o">,</span>
                    <span class="k">assume</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span>
                        <span class="k">assume</span> <span class="n">a3</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">≥</span> <span class="n">m</span><span class="o">,</span>
                        <span class="k">have</span> <span class="n">s13</span> <span class="o">:</span> <span class="n">Q</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="o">(</span><span class="n">n</span> <span class="bp">-</span> <span class="n">m</span><span class="o">)),</span> <span class="k">from</span> <span class="n">s12</span> <span class="o">(</span><span class="n">n</span> <span class="bp">-</span> <span class="n">m</span><span class="o">),</span>
                        <span class="k">have</span> <span class="n">s14</span> <span class="o">:</span> <span class="n">m</span> <span class="bp">+</span> <span class="o">(</span><span class="n">n</span> <span class="bp">-</span> <span class="n">m</span><span class="o">)</span> <span class="bp">=</span> <span class="n">n</span><span class="o">,</span> <span class="k">from</span> <span class="n">add_sub_of_le</span> <span class="n">a3</span><span class="o">,</span>
                        <span class="k">show</span> <span class="n">Q</span> <span class="n">n</span><span class="o">,</span> <span class="k">from</span> <span class="n">eq</span><span class="bp">.</span><span class="n">subst</span> <span class="n">s14</span> <span class="n">s13</span>
</pre></div>


{% endraw %}
