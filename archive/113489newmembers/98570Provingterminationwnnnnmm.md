---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/98570Provingterminationwnnnnmm.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [Proving termination w/ (n' < n \/ (n' = n /\ m' < m))](https://leanprover-community.github.io/archive/113489newmembers/98570Provingterminationwnnnnmm.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ cbailey (Jan 10 2019 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20termination%20w/%20%28n%27%20%3C%20n%20%5C/%20%28n%27%20%3D%20n%20/%5C%20m%27%20%3C%20m%29%29/near/154824198):
<p>Is there any way to convince Lean that a function  f (n : nat, m : nat) -&gt; T, where each recursive call satisfies ( n' &lt; n \/ ( n' = n /\ m' &lt; m ) ) is indeed terminating without explicitly adding a third parameter to represent (n + m) or gas?<br>
Thank you!</p>

#### [ Kenny Lau (Jan 10 2019 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20termination%20w/%20%28n%27%20%3C%20n%20%5C/%20%28n%27%20%3D%20n%20/%5C%20m%27%20%3C%20m%29%29/near/154824668):
<p>1. give us an example 2. custom well-founded tactic</p>

#### [ Jeremy Avigad (Jan 10 2019 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20termination%20w/%20%28n%27%20%3C%20n%20%5C/%20%28n%27%20%3D%20n%20/%5C%20m%27%20%3C%20m%29%29/near/154824899):
<p>You can do arbitrary well-founded recursion in Lean, though it doesn't always work as smoothly as one would like. </p>
<p><a href="https://leanprover.github.io/theorem_proving_in_lean/induction_and_recursion.html#well-founded-recursion-and-induction" target="_blank" title="https://leanprover.github.io/theorem_proving_in_lean/induction_and_recursion.html#well-founded-recursion-and-induction">https://leanprover.github.io/theorem_proving_in_lean/induction_and_recursion.html#well-founded-recursion-and-induction</a></p>
<p>In your case, I think the equation compiler (the system that compiles your function specification down to a function expressed in terms of the foundational primitives) will guess that you want to use lexicographic order, and with luck you'll be able to convince it that the recursive call is decreasing (as described in TPIL).</p>
<p>Generally speaking, though, life will be easier if you can find a structural recursion that will do the job.</p>

#### [ Kevin Buzzard (Jan 10 2019 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20termination%20w/%20%28n%27%20%3C%20n%20%5C/%20%28n%27%20%3D%20n%20/%5C%20m%27%20%3C%20m%29%29/near/154826761):
<p><a href="https://github.com/leanprover/mathlib/blob/master/docs/extras/well_founded_recursion.md" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/docs/extras/well_founded_recursion.md">https://github.com/leanprover/mathlib/blob/master/docs/extras/well_founded_recursion.md</a></p>

#### [ cbailey (Jan 10 2019 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20termination%20w/%20%28n%27%20%3C%20n%20%5C/%20%28n%27%20%3D%20n%20/%5C%20m%27%20%3C%20m%29%29/near/154827110):
<p>Thank you for the links <span class="user-mention" data-user-id="110865">@Jeremy Avigad</span>  and <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> ,  this looks like exactly what I need.</p>
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span>  I'm just using Euclid's algorithm. I'll try and put together a tactic with the reading material you guys referenced</p>
<p>Thanks!</p>

#### [ Wojciech Nawrocki (Jan 13 2019 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20termination%20w/%20%28n%27%20%3C%20n%20%5C/%20%28n%27%20%3D%20n%20/%5C%20m%27%20%3C%20m%29%29/near/155045083):
<p>I found that definining the entire recursive function as an equation-compiler-expression and then ignoring some of the match variables in cases where they don't matter works best, e.g.:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">rec_fn</span><span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="n">b</span> <span class="n">f</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">f</span> <span class="n">b</span>
<span class="bp">|</span> <span class="n">a</span> <span class="n">b</span> <span class="n">f</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="n">rec_fn</span> <span class="n">a</span> <span class="o">(</span><span class="n">b</span><span class="bp">+</span><span class="n">a</span><span class="o">)</span> <span class="n">f</span> <span class="n">n</span>
</pre></div>


<p>but then I end up having to type things like (real example):</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">applyTypeSub</span><span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="err">Γ</span> <span class="err">Γ&#39;</span> <span class="n">T</span><span class="o">},</span> <span class="n">SubFn</span> <span class="err">Γ</span> <span class="err">Γ&#39;</span> <span class="bp">→</span> <span class="n">Term</span> <span class="err">Γ</span> <span class="n">T</span> <span class="bp">→</span> <span class="n">Term</span> <span class="err">Γ&#39;</span> <span class="n">T</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">s</span> <span class="o">(</span><span class="n">Var</span> <span class="n">v</span><span class="o">)</span> <span class="o">:=</span> <span class="n">s</span> <span class="bp">_</span> <span class="n">v</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="n">Nat</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span> <span class="n">Nat</span> <span class="n">n</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="n">Bool</span> <span class="n">b</span><span class="o">)</span> <span class="o">:=</span> <span class="n">Bool</span> <span class="n">b</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">s</span> <span class="o">(</span><span class="n">Abs</span> <span class="n">e</span><span class="o">)</span> <span class="o">:=</span> <span class="n">Abs</span> <span class="o">(</span><span class="n">applyTypeSub</span> <span class="o">(</span><span class="n">STmL</span> <span class="n">s</span><span class="o">)</span> <span class="n">e</span><span class="o">)</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">s</span> <span class="o">(</span><span class="n">App</span> <span class="n">fn</span> <span class="n">arg</span><span class="o">)</span> <span class="o">:=</span> <span class="n">App</span> <span class="o">(</span><span class="n">applyTypeSub</span> <span class="n">s</span> <span class="n">fn</span><span class="o">)</span> <span class="o">(</span><span class="n">applyTypeSub</span> <span class="n">s</span> <span class="n">arg</span><span class="o">)</span>
</pre></div>


<p>in order to make all the variables unify correctly.</p>


{% endraw %}
