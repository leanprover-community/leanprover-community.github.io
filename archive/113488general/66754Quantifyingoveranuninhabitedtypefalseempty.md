---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/66754Quantifyingoveranuninhabitedtypefalseempty.html
---

## Stream: [general](index.html)
### Topic: [Quantifying over an uninhabited type (false/ empty)](66754Quantifyingoveranuninhabitedtypefalseempty.html)

---


{% raw %}
#### [ Adam Kurkiewicz (Mar 22 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Quantifying%20over%20an%20uninhabited%20type%20%28false/%20empty%29/near/124058931):
<p>I'm wondering whether this is something I should be able to prove (I think I should). It came up when I was trying to show that two definitions of primality are equivalent.</p>
<p>Let's say that we have a property, which quantifies over an empty, uninhabited type:</p>
<div class="codehilite"><pre><span></span>def  impossible_property : Prop  :=
∀ (Pfalse : false), 1  =  1
</pre></div>


<p>Is it true that <code>¬ impossible_property</code>, i.e. how, if at all, can I finish this proof:</p>
<div class="codehilite"><pre><span></span>def  cant_happen : ¬ impossible_property :=
λ Pimp : impossible_property,
sorry
</pre></div>

#### [ Johannes Hölzl (Mar 22 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Quantifying%20over%20an%20uninhabited%20type%20%28false/%20empty%29/near/124059054):
<p>Its the opposite: <code>impossible_property</code> is always inhabited, it can be easily proved using <code>false.elim</code>.</p>

#### [ Adam Kurkiewicz (Mar 22 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Quantifying%20over%20an%20uninhabited%20type%20%28false/%20empty%29/near/124059575):
<p>Cheers, indeed:</p>
<div class="codehilite"><pre><span></span>def  impossible_property : Prop  :=
∀ (Pfalse : false), 1  =  1
def  can_happen_ : impossible_property :=
λ (Pfalse: false),
false.elim Pfalse
</pre></div>

#### [ Moses Schönfinkel (Mar 22 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Quantifying%20over%20an%20uninhabited%20type%20%28false/%20empty%29/near/124059651):
<p>This is better shown with a "ridiculous" example. </p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">exfalso_quod_libet</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">false</span><span class="o">)</span> <span class="o">:</span> <span class="mi">4</span> <span class="bp">=</span> <span class="mi">2</span> <span class="o">:=</span> <span class="n">false</span><span class="bp">.</span><span class="n">elim</span> <span class="n">h</span>
</pre></div>

#### [ Adam Kurkiewicz (Mar 22 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Quantifying%20over%20an%20uninhabited%20type%20%28false/%20empty%29/near/124060858):
<p>Thanks Moses,</p>
<p>this is indeed a better example. I'm afraid though that my confusion goes deeper than the initial question.</p>
<p>I've been trying to show that two definitions of primality are equivalent:</p>
<div class="codehilite"><pre><span></span>def  is_divisible: nat → nat →  Prop  :=
λ n m : nat, ∃ k : nat, m * k = n

def  is_prime1: nat →  Prop  :=
λ p, ∀ (m : nat) (Pmdp : is_divisible p m), ((m =  1) ∨ (m = p)) ∧ (p ≠  1)

def  is_prime2: nat →  Prop  :=
λ p, ∀ (k : nat) (b1 : k &lt; p) (b2 : 1  &lt; k), (¬ is_divisible p k)
</pre></div>


<p>Using your example I was able to show that 1 is prime according to the second definition <code>is_prime2</code>:</p>
<div class="codehilite"><pre><span></span>def  one_is_prime2 : is_prime2 1  :=
λ (k : nat) (x : k &lt;  1) (y : 1  &lt; k),
have a : 1  &lt;  1, from lt.trans y x,
have one_ne_one : 1  ≠  1, from (ne_of_lt a),
false.elim (one_ne_one (eq.refl 1))
</pre></div>


<p>This clearly makes <code>is_prime_2</code> a bad definition of primality, but I really can't see what went wrong.</p>

#### [ Mario Carneiro (Mar 22 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Quantifying%20over%20an%20uninhabited%20type%20%28false/%20empty%29/near/124061502):
<p>You should look at the definition of <code>prime</code> and equivalent variations in mathlib <code>data.nat.prime</code></p>

#### [ Mario Carneiro (Mar 22 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Quantifying%20over%20an%20uninhabited%20type%20%28false/%20empty%29/near/124061507):
<p>Most definitions of <code>prime</code> have to explicitly exclude 1</p>

#### [ Mario Carneiro (Mar 22 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Quantifying%20over%20an%20uninhabited%20type%20%28false/%20empty%29/near/124061570):
<p>It is true that there are no 1&lt;k&lt;1 such that 1 | k, meaning that 1 is spuriously identified as prime using <code>is_prime2</code>.</p>

#### [ Mario Carneiro (Mar 22 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Quantifying%20over%20an%20uninhabited%20type%20%28false/%20empty%29/near/124061651):
<p>By the way you probably want <code>p \ne 1</code> in<code>is_prime1</code> to come before the forall, otherwise it only applies when there exists an m such that p|m (which is true, but still it's a bit subtle)</p>

#### [ Mario Carneiro (Mar 22 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Quantifying%20over%20an%20uninhabited%20type%20%28false/%20empty%29/near/124061716):
<p>forall has low binding power, meaning that it extends until it hits a close parenthesis</p>

#### [ Adam Kurkiewicz (Mar 22 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Quantifying%20over%20an%20uninhabited%20type%20%28false/%20empty%29/near/124063178):
<p>Thanks, this makes sense. </p>
<p>The problem extends to <code>is_prime2 0</code>, since <code>k &lt; 0 → false</code> and we end up with the same problems. Definition of primality in mathlib excludes  these cases, just as you pointed out, before the quantifier:  <code>def  prime (p : ℕ) := p ≥  2  ∧  ∀ m ∣ p, m =  1  ∨ m = p</code></p>


{% endraw %}
