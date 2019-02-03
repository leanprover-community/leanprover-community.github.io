---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/96855definingapredicate.html
---

## Stream: [new members](index.html)
### Topic: [defining a predicate](96855definingapredicate.html)

---


{% raw %}
#### [ Patrick Thomas (Nov 26 2018 at 05:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20predicate/near/148346494):
<p>Hi,</p>
<p>I do not have a lot of experience using computer theorem provers, and I have just started trying to learn Lean. As practice I am attempting to formalize and prove that the Principle of Induction implies the Principle of Induction from a Starting Point. So far I have:</p>
<div class="codehilite"><pre><span></span>open nat

-- Principle of Induction -&gt; Principle of Induction from a Starting Point
example : ( forall P : nat -&gt; Prop, ( ( P 0 /\ ( forall n, ( P n -&gt; P (n + 1) ) ) ) -&gt; ( forall n, P n ) ) ) -&gt; ( forall Q : nat -&gt; Prop, forall m, ( ( Q m /\ ( forall n, ( ( n &gt;= m ) -&gt; ( Q n -&gt; Q (n + 1) ) ) ) ) -&gt; ( forall n, ( ( n &gt;= m ) -&gt; Q n ) ) ) ) :=
    assume a1 : forall P : nat -&gt; Prop, ( ( P 0 /\ ( forall n, ( P n -&gt; P (n + 1) ) ) ) -&gt; ( forall n, P n ) ),
        assume Q : nat -&gt; Prop,
            assume m : nat,
                assume a2 : ( Q m /\ ( forall n, ( ( n &gt;= m ) -&gt; ( Q n -&gt; Q (n + 1) ) ) ) ),
                have s1 : Q m, from and.left a2,
                have s2 : forall n, ( ( n &gt;= m ) -&gt; ( Q n -&gt; Q (n + 1) ) ), from and.right a2,
                have s3 : forall n, ( Q (n + m) -&gt; Q ((n + m) + 1) ), from
                    assume n : nat,
                    have s4 : ( ( (n + m) &gt;= m ) -&gt; ( Q (n + m) -&gt; Q ((n + m) + 1) ) ), from s2 (n + m),
                    have s5 : (n + m) &gt;= m, from sorry,
                    show ( Q (n + m) -&gt; Q ((n + m) + 1) ), from s4 s5,

                -- define P&#39; n to hold if and only if Q (m + n) holds
                -- then P&#39; 0 holds by s1, and forall n, ( P&#39; n -&gt; P&#39; (n + 1) ) holds by s3
                -- then forall n, P&#39; n holds by a1
                -- then Q (m + n) holds for all n
                -- then Q holds for all n &gt;= m
</pre></div>


<p>I am currently trying to define a predicate P' n : nat -&gt; Prop that holds if and only if the predicate Q holds for m + n. Is there any chance that someone could show me how this can be done?</p>
<p>Thank you very much for your time,<br>
Patrick</p>

#### [ Johan Commelin (Nov 26 2018 at 06:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20predicate/near/148347104):
<p>Hi <span class="user-mention" data-user-id="139442">@Patrick Thomas</span> Welcome to Lean (and Zulip).</p>

#### [ Johan Commelin (Nov 26 2018 at 06:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20predicate/near/148347120):
<p>This is certainly possible.</p>

#### [ Johan Commelin (Nov 26 2018 at 06:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20predicate/near/148347174):
<p>By the way (depending on taste) you can make your code a bit more readable by using unicode.<br>
For example, you can type <code>\and</code> or <code>\to</code> to get nice symbols for <code>/\</code> and <code>-&gt;</code>.</p>

#### [ Patrick Thomas (Nov 26 2018 at 06:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20predicate/near/148347184):
<p>Thank you.</p>

#### [ Johan Commelin (Nov 26 2018 at 06:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20predicate/near/148347204):
<p>Are you using mathlib?</p>

#### [ Johan Commelin (Nov 26 2018 at 06:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20predicate/near/148347211):
<p>Because there must be some lemma in <code>data/nat/basic.lean</code> that will tell you that <code>(n - m) + m = n</code> if <code>n ≥ m</code>.</p>

#### [ Patrick Thomas (Nov 26 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20predicate/near/148347271):
<p>No. I just read about it a couple of minutes ago actually.</p>

#### [ Johan Commelin (Nov 26 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20predicate/near/148347275):
<p>Aah, it will be very helpful. There's tons of useful little facts in there.</p>

#### [ Johan Commelin (Nov 26 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20predicate/near/148347279):
<p>Do you have a CS or a maths background, or both?</p>

#### [ Patrick Thomas (Nov 26 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20predicate/near/148347497):
<p>I did an undergraduate degree in CS and physics, and have a strong interest in math. I started studying mathematical logic about a year ago in an attempt to understand computer proof assistants.</p>

#### [ Johan Commelin (Nov 26 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20predicate/near/148347559):
<p>Ok, cool. There's a nice mix of CS and math in this community.</p>

#### [ Patrick Thomas (Nov 26 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20predicate/near/148348284):
<blockquote>
<p>Because there must be some lemma in <code>data/nat/basic.lean</code> that will tell you that <code>(n - m) + m = n</code> if <code>n ≥ m</code>.</p>
</blockquote>
<p>I'm sorry, I'm not certain how I would use this in the proof. Is this in relation to step s5?</p>

#### [ Johan Commelin (Nov 26 2018 at 07:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20predicate/near/148349209):
<p><span class="user-mention" data-user-id="139442">@Patrick Thomas</span> I would first state something like <code>let P' : Prop := foobar,</code><br>
and then <code>have quux : Q \iff P' := xyzzy,</code></p>

#### [ Johan Commelin (Nov 26 2018 at 07:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20predicate/near/148349216):
<p>In that latter proof you will need some lemma from mathlib, I guess.</p>

#### [ Mario Carneiro (Nov 26 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20predicate/near/148353577):
<p>To define something in a proof, you can use <code>let</code>. In this case <code>let P' := λ n, Q (m + n)</code> will do. Here is a short proof following mathlib style. This is probably too dense for a first cut but I'm sure someone around here can unpack this a bit.</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span>
  <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">P</span> <span class="o">:</span> <span class="n">nat</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">,</span> <span class="n">P</span> <span class="mi">0</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="n">P</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">P</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">))</span> <span class="bp">→</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="n">P</span> <span class="n">n</span><span class="o">)</span>
  <span class="o">(</span><span class="n">Q</span> <span class="o">:</span> <span class="n">nat</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">m</span><span class="o">)</span>
  <span class="o">(</span><span class="n">h₁</span> <span class="o">:</span> <span class="n">Q</span> <span class="n">m</span><span class="o">)</span> <span class="o">(</span><span class="n">h₂</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span> <span class="bp">≥</span> <span class="n">m</span><span class="o">,</span> <span class="n">Q</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">Q</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">))</span> <span class="o">(</span><span class="n">n</span><span class="o">)</span> <span class="o">(</span><span class="n">mn</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">≥</span> <span class="n">m</span><span class="o">)</span> <span class="o">:</span> <span class="n">Q</span> <span class="n">n</span> <span class="o">:=</span>
<span class="k">let</span> <span class="n">P&#39;</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">n</span><span class="o">,</span> <span class="n">Q</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="n">n</span><span class="o">)</span> <span class="k">in</span>
<span class="k">have</span> <span class="n">P&#39;</span> <span class="o">(</span><span class="n">n</span> <span class="bp">-</span> <span class="n">m</span><span class="o">),</span> <span class="k">from</span> <span class="n">H</span> <span class="n">P&#39;</span> <span class="n">h₁</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">n</span><span class="o">,</span> <span class="n">h₂</span> <span class="bp">_</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">le_add_right</span> <span class="n">m</span> <span class="n">n</span><span class="o">))</span> <span class="o">(</span><span class="n">n</span> <span class="bp">-</span> <span class="n">m</span><span class="o">),</span>
<span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">P&#39;</span><span class="o">]</span> <span class="n">at</span> <span class="n">this</span><span class="bp">;</span> <span class="n">rwa</span> <span class="n">nat</span><span class="bp">.</span><span class="n">add_sub_cancel&#39;</span> <span class="n">mn</span> <span class="n">at</span> <span class="n">this</span>
</pre></div>

#### [ Kevin Buzzard (Nov 26 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20predicate/near/148353667):
<p><code>simp [P'] at this</code> is using Lean's inbuilt simplifier to do a lot of dirty work involving equalities; <code>rwa</code> means "rewrite, then use an assumption". Both <code>simp</code> and <code>rw</code> are talked about in Theorem Proving in Lean, in the chapter on tactics: <a href="https://leanprover.github.io/theorem_proving_in_lean/tactics.html" target="_blank" title="https://leanprover.github.io/theorem_proving_in_lean/tactics.html">https://leanprover.github.io/theorem_proving_in_lean/tactics.html</a></p>

#### [ Patrick Thomas (Nov 28 2018 at 06:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20predicate/near/148691325):
<p>Thank you! This has helped.</p>


{% endraw %}
