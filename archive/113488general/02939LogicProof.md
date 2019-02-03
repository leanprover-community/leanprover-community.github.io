---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/02939LogicProof.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Logic & Proof](https://leanprover-community.github.io/archive/113488general/02939LogicProof.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kaushik Chakraborty (Jun 07 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/127707574):
<p>Hi, I am going through the online course Logic and Proof. I am stuck in the exercises. Is this the right place to ask such questions?</p>

#### [ Chris Hughes (Jun 07 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/127707694):
<p>Yes</p>

#### [ Kaushik Chakraborty (Jun 07 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/127708058):
<p>Thanks. So I'm stuck progressing with the last prob. of <a href="https://leanprover.github.io/logic_and_proof/propositional_logic_in_lean.html#exercises" target="_blank" title="https://leanprover.github.io/logic_and_proof/propositional_logic_in_lean.html#exercises">Chapter 4's exercises</a> i.e. prove <code>¬ (A ↔ ¬ A)</code></p>

#### [ Kaushik Chakraborty (Jun 07 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/127708189):
<p>I am thinking of following the rules mentioned in the book till now and start with the assumption that <code>(A ↔ ¬ A)</code>is true and then progress to show <code>false</code> so that I can prove the negation. But I can't figure out a way forward</p>

#### [ Kenny Lau (Jun 07 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/127708218):
<p>hint: prove <code>¬ A</code> from your assumption</p>

#### [ Chris Hughes (Jun 07 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/127708555):
<p>This actually came up in M1F, and I was annoyed with myself for assuming excluded middle.</p>

#### [ Kenny Lau (Jun 07 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/127708566):
<p>not constructive enough, eh :P</p>

#### [ Kaushik Chakraborty (Jun 07 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/127708801):
<p>am failing to get how can I get <code>¬ A</code> with just assuming <code>A ↔ ¬ A</code>. I can get it if I also assume <code>A</code> and apply left elimination to the iff to get <code>¬ A</code>. Is my understanding correct ?</p>

#### [ Kenny Lau (Jun 07 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/127708812):
<p>no, you need to assume <code>A</code> and prove <code>false</code></p>

#### [ Kenny Lau (Jun 07 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/127708823):
<p>ok, which you get via deducing <code>¬ A</code></p>

#### [ Chris Hughes (Jun 07 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/127708944):
<p>Try <code>have h : ¬ A</code></p>

#### [ Kaushik Chakraborty (Jun 07 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/127708955):
<p>I am trying to do something like that but I am getting a type mismatch error coz of the additional assumption. <br>
Could you please look at this <a href="https://leanprover.github.io/live/3.4.1/#code=variables%20A%20:%20Prop%0A%0Aexample%20:%20¬%20(A%20↔%20¬%20A)%20:=%0Aassume%20h,%0Aassume%20a%20:%20A,%0Ahave%20h1%20:%20¬%20A,%20from%20h.mp%20a,%0Ashow%20false,%20from%20h1%20a" target="_blank" title="https://leanprover.github.io/live/3.4.1/#code=variables%20A%20:%20Prop%0A%0Aexample%20:%20¬%20(A%20↔%20¬%20A)%20:=%0Aassume%20h,%0Aassume%20a%20:%20A,%0Ahave%20h1%20:%20¬%20A,%20from%20h.mp%20a,%0Ashow%20false,%20from%20h1%20a">LEAN code</a></p>

#### [ Chris Hughes (Jun 07 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/127709050):
<p>You can only do <code>assume a : A</code> if your goal is <code>A → something</code></p>

#### [ Chris Hughes (Jun 07 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/127709059):
<p>Have you used <code>have</code> before?</p>

#### [ Kenny Lau (Jun 07 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/127709121):
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="n">A</span> <span class="o">:</span> <span class="kt">Prop</span>

<span class="kn">example</span> <span class="o">:</span> <span class="bp">¬</span> <span class="o">(</span><span class="n">A</span> <span class="bp">↔</span> <span class="bp">¬</span> <span class="n">A</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">assume</span> <span class="n">h</span><span class="o">,</span>
<span class="k">have</span> <span class="n">h1</span> <span class="o">:</span> <span class="bp">¬</span> <span class="n">A</span><span class="o">,</span> <span class="k">from</span> <span class="bp">_</span><span class="o">,</span>
<span class="k">show</span> <span class="n">false</span><span class="o">,</span> <span class="k">from</span> <span class="bp">_</span>
</pre></div>

#### [ Kenny Lau (Jun 07 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/127709126):
<p>so your code should look like this</p>

#### [ Kaushik Chakraborty (Jun 07 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/127709348):
<p>yeah that's what I am trying but could not think of any intro/elim rule to apply to get <code>¬ A</code> from <code>h</code></p>

#### [ Moses Schönfinkel (Jun 07 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/127709518):
<p>The biggest hint here was the innocuous sentence "...and I was annoyed with myself for assuming excluded middle" :). You can't conjure <code>not A</code> from thin air, but you <em>can</em> conjure something almost as good.</p>

#### [ Kaushik Chakraborty (Jun 07 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/127709738):
<p>Ok I think I got it</p>
<div class="codehilite"><pre><span></span>variables A : Prop

example : ¬ (A ↔ ¬ A) :=
assume h,
have h1 : ¬ A, from
    assume a : A,
    show false, from (h.mp a) a,
show false, from h1 (h.mpr h1)
</pre></div>

#### [ Kaushik Chakraborty (Jun 07 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/127709838):
<p>thanks a lot for the guidance</p>

#### [ Kaushik Chakraborty (Jul 19 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/129916601):
<p>Hello again. I want to do the exercise 17.1 of the course on proving the equivalence of <em>principle of complete induction</em> to <em>principle of least element</em> in Lean. So in that regard does the following setup make sense? I still need to do the actual proof. </p>
<div class="codehilite"><pre><span></span><span class="kn">variable</span> <span class="n">P</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span>

<span class="kn">example</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">m</span><span class="o">,</span> <span class="n">m</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="bp">∧</span> <span class="n">P</span><span class="o">(</span><span class="n">m</span><span class="o">)</span> <span class="bp">→</span>  <span class="n">P</span><span class="o">(</span><span class="n">n</span><span class="o">))</span> <span class="bp">→</span> <span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">P</span><span class="o">(</span><span class="n">x</span><span class="o">)</span> <span class="bp">↔</span>
                <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="n">P</span><span class="o">(</span><span class="n">n</span><span class="o">)</span> <span class="bp">∧</span> <span class="bp">∃</span> <span class="n">m</span> <span class="n">x</span><span class="o">,</span> <span class="n">m</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="bp">∧</span> <span class="bp">¬</span> <span class="o">(</span><span class="n">x</span> <span class="bp">&lt;</span> <span class="n">m</span><span class="o">)</span> <span class="bp">→</span> <span class="n">P</span><span class="o">(</span><span class="n">m</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">sorry</span>
</pre></div>

#### [ Mario Carneiro (Jul 19 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/129917107):
<p>the parentheses seem to be off in a few places</p>

#### [ Mario Carneiro (Jul 19 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/129917793):
<p>I think this is correct with minimal parentheses:</p>
<div class="codehilite"><pre><span></span><span class="kn">variable</span> <span class="n">P</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span>

<span class="kn">example</span> <span class="o">:</span> <span class="o">((</span><span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">m</span><span class="o">,</span> <span class="n">m</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">P</span> <span class="n">m</span><span class="o">)</span> <span class="bp">→</span> <span class="n">P</span> <span class="n">n</span><span class="o">)</span> <span class="bp">→</span> <span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">P</span> <span class="n">x</span><span class="o">)</span> <span class="bp">↔</span>
            <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="n">P</span> <span class="n">n</span> <span class="bp">→</span> <span class="bp">∃</span> <span class="n">m</span><span class="o">,</span> <span class="n">P</span> <span class="n">m</span> <span class="bp">∧</span> <span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="n">m</span> <span class="bp">→</span> <span class="bp">¬</span> <span class="n">P</span> <span class="n">x</span> <span class="o">:=</span>
<span class="n">sorry</span>
</pre></div>

#### [ Mario Carneiro (Jul 19 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/129917947):
<p>the statement of the principle of least element you gave looks really weird and is probably incorrect - I've changed the statement a bit</p>

#### [ Mario Carneiro (Jul 19 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/129917995):
<p>I expect it to say something like "if P(n) for some n, then there exists an m such that P(m), and ¬ P(x) for all smaller x"</p>

#### [ Johan Commelin (Jul 19 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/129918082):
<p>The current statement reads to me as "I can prove <code>P</code> by induction iff the principle of least element holds for <code>P</code>"</p>

#### [ Mario Carneiro (Jul 19 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/129918311):
<p>My point is that the right hand side doesn't look like the PLE to me</p>

#### [ Johan Commelin (Jul 19 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/129918399):
<p>Oooh, you are completely right. The right hand side should start with <code>\exists</code>. As stated it is trivial: take <code>m = 0</code>.</p>

#### [ Mario Carneiro (Jul 19 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/129918405):
<p>Also, I don't think this will actually work (unless you prove both sides individually), since the traditional reduction of induction to PLE and vice versa involves negating P</p>

#### [ Mario Carneiro (Jul 19 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/129918425):
<p>this can be rectified by quantifying P individually on each side:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">P</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">,</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">m</span><span class="o">,</span> <span class="n">m</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">P</span> <span class="n">m</span><span class="o">)</span> <span class="bp">→</span> <span class="n">P</span> <span class="n">n</span><span class="o">)</span> <span class="bp">→</span> <span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">P</span> <span class="n">x</span><span class="o">)</span> <span class="bp">↔</span>
           <span class="bp">∀</span> <span class="o">(</span><span class="n">P</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="n">n</span><span class="o">,</span> <span class="n">P</span> <span class="n">n</span> <span class="bp">→</span> <span class="bp">∃</span> <span class="n">m</span><span class="o">,</span> <span class="n">P</span> <span class="n">m</span> <span class="bp">∧</span> <span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="n">m</span> <span class="bp">→</span> <span class="bp">¬</span> <span class="n">P</span> <span class="n">x</span> <span class="o">:=</span>
<span class="n">sorry</span>
</pre></div>

#### [ Kaushik Chakraborty (Jul 19 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/129918491):
<p>Ok. I got the formalization of PLE. Thanks</p>

#### [ Kaushik Chakraborty (Jul 19 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/129918612):
<p>although in your formalization of PLE, there is no relation between <code>n</code> and <code>m</code>. Shouldn't we mention that <code>m &lt; n</code> ?</p>

#### [ Mario Carneiro (Jul 19 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/129918986):
<p>There is no need, in the same way that there is no relation between n and x in the statement of induction</p>

#### [ Mario Carneiro (Jul 19 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/129919018):
<p>You can prove, given the conclusion, that <code>m &lt;= n</code>, but it is possible that <code>m = n</code> if <code>n</code> is already the minimal witness</p>

#### [ Mario Carneiro (Jul 19 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/129919095):
<p>another way to bracket it is <code>∀ (P : ℕ → Prop), (∃ n, P n) → ∃ m, P m ∧ ∀ x, x &lt; m → ¬ P x</code></p>

#### [ Kaushik Chakraborty (Jul 19 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/129919210):
<p>Ok got it.</p>

#### [ Kaushik Chakraborty (Jul 23 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130138371):
<p>I'm stuck at this simple proof. how do I go from <code>n * n &lt; m * m</code> to <code>n ^ 2 &lt; m ^2</code></p>
<div class="codehilite"><pre><span></span>open nat
variables n m : ℕ

example : 0 &lt; n ∧ n &lt; m → n ^ 2 &lt; m ^ 2 :=
assume h,
have n * n &lt; n * m, from mul_lt_mul_of_pos_left h.right h.left,
have n * m &lt; m * m, from mul_lt_mul_of_pos_right h.right (lt_trans h.left h.right),
have n * n &lt; m * m, from lt_trans ‹ n * n &lt; n * m › ‹ n * m &lt; m * m ›,
sorry
</pre></div>

#### [ Kenny Lau (Jul 23 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130138666):
<div class="codehilite"><pre><span></span><span class="kn">open</span> <span class="n">nat</span>
<span class="kn">variables</span> <span class="n">n</span> <span class="n">m</span> <span class="o">:</span> <span class="bp">ℕ</span>

<span class="kn">example</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="bp">∧</span> <span class="n">n</span> <span class="bp">&lt;</span> <span class="n">m</span> <span class="bp">→</span> <span class="n">n</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">&lt;</span> <span class="n">m</span> <span class="err">^</span> <span class="mi">2</span> <span class="o">:=</span>
<span class="k">assume</span> <span class="n">h</span><span class="o">,</span>
<span class="k">calc</span>  <span class="n">n</span> <span class="err">^</span> <span class="mi">2</span>
    <span class="bp">=</span> <span class="n">nat</span><span class="bp">.</span><span class="n">pow</span> <span class="n">n</span> <span class="mi">2</span> <span class="o">:</span> <span class="k">by</span> <span class="n">dsimp</span> <span class="o">[(</span><span class="err">^</span><span class="o">)]</span><span class="bp">;</span> <span class="n">refl</span>
<span class="bp">...</span> <span class="bp">=</span> <span class="mi">1</span> <span class="bp">*</span> <span class="o">(</span><span class="n">n</span> <span class="bp">*</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span> <span class="n">nat</span><span class="bp">.</span><span class="n">mul_assoc</span> <span class="mi">1</span> <span class="n">n</span> <span class="n">n</span>
<span class="bp">...</span> <span class="bp">=</span> <span class="n">n</span> <span class="bp">*</span> <span class="n">n</span> <span class="o">:</span> <span class="n">nat</span><span class="bp">.</span><span class="n">one_mul</span> <span class="bp">_</span>
<span class="bp">...</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="bp">*</span> <span class="n">m</span> <span class="o">:</span> <span class="n">mul_lt_mul_of_pos_left</span> <span class="n">h</span><span class="bp">.</span><span class="n">right</span> <span class="n">h</span><span class="bp">.</span><span class="n">left</span>
<span class="bp">...</span> <span class="bp">&lt;</span> <span class="n">m</span> <span class="bp">*</span> <span class="n">m</span> <span class="o">:</span> <span class="n">mul_lt_mul_of_pos_right</span> <span class="n">h</span><span class="bp">.</span><span class="n">right</span> <span class="o">(</span><span class="n">lt_trans</span> <span class="n">h</span><span class="bp">.</span><span class="n">left</span> <span class="n">h</span><span class="bp">.</span><span class="n">right</span><span class="o">)</span>
<span class="bp">...</span> <span class="bp">=</span> <span class="n">m</span> <span class="err">^</span> <span class="mi">2</span> <span class="o">:</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[(</span><span class="err">^</span><span class="o">),</span> <span class="n">nat</span><span class="bp">.</span><span class="n">pow</span><span class="o">]</span>
</pre></div>

#### [ Kenny Lau (Jul 23 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130138680):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> why can't I replace <code>by dsimp [(^)]; refl</code> with <code>rfl</code>?</p>

#### [ Chris Hughes (Jul 23 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130138725):
<p>Definitional equality is not transitive.</p>

#### [ Kenny Lau (Jul 23 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130138729):
<p>but then why does this work?</p>

#### [ Kenny Lau (Jul 23 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130138731):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="n">n</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">=</span> <span class="n">nat</span><span class="bp">.</span><span class="n">pow</span> <span class="n">n</span> <span class="mi">2</span> <span class="o">:=</span> <span class="n">rfl</span>
</pre></div>

#### [ Kenny Lau (Jul 23 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130138738):
<p>Definitional equality is not consistent either?</p>

#### [ Kaushik Chakraborty (Jul 23 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130138817):
<p>thanks <span class="user-mention" data-user-id="110064">@Kenny Lau</span> . I still don't understand tactics. Maybe the theorem proving in lean course will help. Logic and Proof course have few mentions of tactics.</p>

#### [ Johan Commelin (Jul 23 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130139007):
<p>Kaushik, to answer your original question, there is <code>pow_two</code> which you can use to rewrite between <code>n * n</code> and <code>n^2</code>.</p>

#### [ Kenny Lau (Jul 23 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130139020):
<p>it's not available without further import though</p>

#### [ Johan Commelin (Jul 23 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130139360):
<p>Right, you need to import <code>algebra.group_power</code>, I think.</p>

#### [ Kaushik Chakraborty (Jul 23 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130140974):
<p>thanks <span class="user-mention" data-user-id="112680">@Johan Commelin</span>. but am still not sure how to use <code>pow_two</code> in my proof. I think I have to use <code>rewrite</code> tactic but not sure how. Here is how I've changed my earlier proof</p>
<div class="codehilite"><pre><span></span>import algebra.group_power
open nat
variables n m : ℕ

example : 0 &lt; n ∧ n &lt; m → n ^ 2 &lt; m ^ 2 :=
assume h,
have n * n &lt; n * m, from mul_lt_mul_of_pos_left h.right h.left,
have n ^ 2 &lt; n * m, by sorry,
have n * m &lt; m * m, from mul_lt_mul_of_pos_right h.right (lt_trans h.left h.right),
have n * m &lt; m ^ 2, by sorry,
lt_trans ‹ n ^ 2 &lt; n * m ›  ‹ n * m &lt; m ^ 2 ›
</pre></div>

#### [ Johan Commelin (Jul 23 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130141157):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">n</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">=</span> <span class="n">n</span> <span class="bp">*</span> <span class="n">n</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">rewrite</span> <span class="n">pow_two</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Jul 23 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130141225):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">n</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">=</span> <span class="n">n</span> <span class="bp">*</span> <span class="n">n</span> <span class="o">:=</span> <span class="n">pow_two</span> <span class="n">n</span>
</pre></div>

#### [ Kaushik Chakraborty (Jul 23 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130141616):
<p>yeah I got the function usage part but how do I use <code>pow_two</code> when I've the <code>lt</code> relation i.e. replace sorry in <code>have n ^ 2 &lt;  n * m, by sorry</code> when I've established <code>n * n &lt; n * m</code>. Or I'm approaching it wrong ?</p>

#### [ Kevin Buzzard (Jul 23 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130168976):
<p>You should be able to do this with <code>rw</code></p>

#### [ Kevin Buzzard (Jul 23 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130169439):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">group_power</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">*</span> <span class="n">n</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="bp">*</span> <span class="n">m</span><span class="o">)</span> <span class="o">:</span> <span class="n">n</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="bp">*</span> <span class="n">m</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">have</span> <span class="n">H</span> <span class="o">:</span> <span class="n">n</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">=</span> <span class="n">n</span> <span class="bp">*</span> <span class="n">n</span> <span class="o">:=</span> <span class="n">pow_two</span> <span class="n">n</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">h</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Jul 23 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130169462):
<p>You should also be able to do it with <code>eq.subst</code> but I can never ever ever for the life of me get it to work.</p>

#### [ Kenny Lau (Jul 23 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130169478):
<p><code>\t</code></p>

#### [ Kevin Buzzard (Jul 23 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130169502):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">group_power</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">*</span> <span class="n">n</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="bp">*</span> <span class="n">m</span><span class="o">)</span> <span class="o">:</span> <span class="n">n</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="bp">*</span> <span class="n">m</span> <span class="o">:=</span> <span class="o">(</span><span class="n">pow_two</span> <span class="n">n</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span> <span class="bp">▸</span> <span class="n">h</span>
</pre></div>


<p>[doesn't work]</p>

#### [ Kevin Buzzard (Jul 23 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130169525):
<p>Can you fix it Kenny?</p>

#### [ Kenny Lau (Jul 23 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130169559):
<p>I think you would like <code>by convert h</code></p>

#### [ Kenny Lau (Jul 23 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130169633):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">group_power</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">*</span> <span class="n">n</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="bp">*</span> <span class="n">m</span><span class="o">)</span> <span class="o">:</span> <span class="n">n</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="bp">*</span> <span class="n">m</span> <span class="o">:=</span>
<span class="k">have</span> <span class="n">H</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">*</span> <span class="n">n</span> <span class="bp">=</span> <span class="n">n</span> <span class="err">^</span> <span class="mi">2</span><span class="o">,</span> <span class="k">from</span> <span class="n">eq</span><span class="bp">.</span><span class="n">symm</span> <span class="err">$</span> <span class="n">pow_two</span> <span class="n">n</span><span class="o">,</span>
<span class="n">H</span> <span class="bp">▸</span> <span class="n">h</span>
</pre></div>

#### [ Kenny Lau (Jul 23 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130169668):
<p>I'm not sure why your original version doesn't work</p>

#### [ Kenny Lau (Jul 23 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130169677):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">group_power</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">*</span> <span class="n">n</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="bp">*</span> <span class="n">m</span><span class="o">)</span> <span class="o">:</span> <span class="n">n</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="bp">*</span> <span class="n">m</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">convert</span> <span class="n">h</span><span class="bp">;</span> <span class="k">from</span> <span class="n">pow_two</span> <span class="n">n</span>
</pre></div>

#### [ Kevin Buzzard (Jul 23 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130169688):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">*</span> <span class="n">n</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="bp">*</span> <span class="n">m</span><span class="o">)</span> <span class="o">:</span> <span class="n">n</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="bp">*</span> <span class="n">m</span> <span class="o">:=</span>
<span class="o">((((</span><span class="n">pow_two</span> <span class="n">n</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">*</span> <span class="n">n</span> <span class="bp">=</span> <span class="n">n</span> <span class="err">^</span> <span class="mi">2</span><span class="o">)</span> <span class="bp">▸</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">*</span> <span class="n">n</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="bp">*</span> <span class="n">m</span><span class="o">))</span> <span class="o">:</span> <span class="n">n</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="bp">*</span> <span class="n">m</span><span class="o">)</span>
</pre></div>

#### [ Kenny Lau (Jul 23 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130169727):
<p>:o</p>

#### [ Kevin Buzzard (Jul 23 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130169729):
<div class="codehilite"><pre><span></span>invalid &#39;eq.subst&#39; application, elaborator has special support for this kind of application (it is handled as an &quot;eliminator&quot;), but expected type must not contain metavariables
  n ^ 2 &lt; n * m
</pre></div>

#### [ Kevin Buzzard (Jul 23 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130169733):
<p>I see no metavariables!</p>

#### [ Kenny Lau (Jul 23 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130169743):
<p>yeah I'm puzzled too</p>

#### [ Chris Hughes (Jul 23 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130169747):
<p><code>example (m n : ℤ) (h : n * n &lt; n * m) : n ^ (2 : ℕ) &lt; n * m := (pow_two n).symm ▸ h</code></p>

#### [ Kenny Lau (Jul 23 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130169752):
<p>...</p>

#### [ Chris Hughes (Jul 23 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130169753):
<p>works</p>

#### [ Kevin Buzzard (Jul 23 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130169755):
<p>...</p>

#### [ Kevin Buzzard (Jul 23 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130169775):
<p>The well-known metavariable <code>2</code></p>

#### [ Kevin Buzzard (Jul 23 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130169932):
<div class="codehilite"><pre><span></span>invalid &#39;eq.subst&#39; application, elaborator has special support for this kind of application (it is handled as an &quot;eliminator&quot;), but expected type must not contain metavariables
  @has_lt.lt.{0} int int.has_lt
    (@has_pow.pow.{0 ?l_1} int ?m_2 ?m_3 n (@bit0.{?l_1} ?m_2 ?m_4 (@has_one.one.{?l_1} ?m_2 ?m_5)))
    (@has_mul.mul.{0} int int.has_mul n m)
</pre></div>

#### [ Kevin Buzzard (Jul 23 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130169934):
<p>Indeed there was a metavariable</p>

#### [ Chris Hughes (Jul 23 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130169942):
<p>This works <code>lemma thing (m n : ℤ) (h : n * n &lt; n * m) : n ^ 2 &lt; n * m := (pow_two n).symm ▸ h</code></p>

#### [ Kenny Lau (Jul 23 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130169949):
<p>?????????????????</p>

#### [ Chris Hughes (Jul 23 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130169960):
<p>not this though <code>def thing (m n : ℤ) (h : n * n &lt; n * m) : n ^ 2 &lt; n * m := (pow_two n).symm ▸ h</code></p>

#### [ Kevin Buzzard (Jul 23 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130170018):
<p>I think this is a bug in <code>pow_two</code> -- the inbuilt <code>2</code> is a nat</p>

#### [ Kevin Buzzard (Jul 23 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130170049):
<p>Clearly pow_two should be a definition not a theorem</p>

#### [ Kevin Buzzard (Jul 23 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130170055):
<p>Or am I barking up the wrong tree ;-)</p>

#### [ Kenny Lau (Jul 23 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130170117):
<p>I agree. Split the definition into more cases for easier definitional equality.</p>

#### [ Chris Hughes (Jul 23 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130170126):
<p>I don't think it has anything to do with <code>pow_two</code></p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">two_add_three</span> <span class="o">:</span> <span class="mi">2</span> <span class="bp">+</span> <span class="mi">3</span> <span class="bp">=</span> <span class="mi">5</span> <span class="o">:=</span> <span class="n">add_comm</span> <span class="mi">0</span> <span class="mi">5</span> <span class="bp">▸</span> <span class="n">rfl</span> <span class="c1">-- works</span>

<span class="kn">example</span> <span class="o">:</span> <span class="mi">2</span> <span class="bp">+</span> <span class="mi">3</span> <span class="bp">=</span> <span class="mi">5</span> <span class="o">:=</span> <span class="n">add_comm</span> <span class="mi">0</span> <span class="mi">5</span> <span class="bp">▸</span> <span class="n">rfl</span> <span class="c1">-- doesn&#39;t work</span>
</pre></div>

#### [ Kevin Buzzard (Jul 23 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130171125):
<p><code>example : (2 : ℕ) + 3 = 5 := add_comm 0 5 ▸ rfl -- works</code></p>

#### [ Kevin Buzzard (Jul 23 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130171160):
<p>So the bit where it says "Ok I can't figure out the type of this <code>2</code> thing, let's let it be <code>nat</code> just so we can get on" is not occurring in the <code>example</code>s</p>

#### [ Kevin Buzzard (Jul 23 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130171165):
<p>Maybe <code>pow_two</code> should have been an example. Wait...</p>

#### [ Mario Carneiro (Jul 24 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130180460):
<p>The reason that <code>example</code> and <code>def</code> fail while <code>theorem</code> succeeds is due to the separation of statement and proof done with <code>theorem</code></p>

#### [ Mario Carneiro (Jul 24 2018 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130180493):
<p>Remember how I mentioned a long time ago that <code>nat</code> is the default type for numerals but it occurs very late in the elaboration? It's basically the last resort if there is a numeral of indeterminate type</p>

#### [ Mario Carneiro (Jul 24 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130180615):
<p>In regard to this example, what happens is that since <code>def</code>/<code>example</code> allows the statement and proof to be elaborated together, it checks the proof to see if that will give a hint what is alpha in <code>(2:alpha) + 3 = 5</code>. But that means that when it hits the <code>eq.subst</code> it will still have a lingering metavariable. In the <code>theorem</code> case, there is no information to be had, since the proof doesn't contribute to elaborating the statement, so it goes with the default <code>nat</code> type for numerals. Then when it elaborates the proof, there are no metavariables</p>

#### [ Kaushik Chakraborty (Jul 25 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130244645):
<p>For this code in the LEAN live in-browser IDE</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">group_power</span>
<span class="kn">theorem</span> <span class="n">thing</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">*</span> <span class="n">n</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="bp">*</span> <span class="n">m</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">n</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="bp">*</span> <span class="n">m</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="n">pow_two</span> <span class="n">n</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span> <span class="bp">▸</span> <span class="n">h</span>
</pre></div>


<p>am getting following error</p>
<div class="codehilite"><pre><span></span><span class="s2">&quot;eliminator&quot;</span> <span class="n">elaborator</span> <span class="n">type</span> <span class="n">mismatch</span><span class="o">,</span> <span class="n">term</span>
  <span class="n">h</span>
<span class="n">has</span> <span class="n">type</span>
  <span class="n">n</span> <span class="bp">*</span> <span class="n">n</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="bp">*</span> <span class="n">m</span>
<span class="n">but</span> <span class="n">is</span> <span class="n">expected</span> <span class="n">to</span> <span class="k">have</span> <span class="n">type</span>
  <span class="n">n</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="bp">*</span> <span class="n">m</span>
<span class="n">Additional</span> <span class="n">information</span><span class="o">:</span>
<span class="bp">/</span><span class="n">test</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="mi">2</span><span class="o">:</span><span class="mi">82</span><span class="o">:</span> <span class="kn">context</span><span class="o">:</span> <span class="n">the</span> <span class="n">inferred</span> <span class="n">motive</span> <span class="n">for</span> <span class="n">the</span> <span class="n">eliminator</span><span class="bp">-</span><span class="n">like</span> <span class="n">application</span> <span class="n">is</span>
  <span class="bp">λ</span> <span class="o">(</span><span class="bp">_</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">n</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="bp">*</span> <span class="n">m</span>
</pre></div>

#### [ Kevin Buzzard (Jul 25 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130244817):
<p>Join the <code>▸</code>-haters club!</p>

#### [ Kevin Buzzard (Jul 25 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130244863):
<p>Sometimes the issue is that higher-order unification is undecidable, sometimes I've just made a silly mistake.</p>

#### [ Chris Hughes (Jul 25 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130244921):
<p>The mistake here is that <code>pow_two</code> is a theorem about <code>monoid.pow</code> and not <code>nat.pow</code></p>

#### [ Kevin Buzzard (Jul 25 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130244927):
<p>yes, I just realised that when trying to solve without the triangle</p>

#### [ Kevin Buzzard (Jul 25 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130244928):
<div class="codehilite"><pre><span></span>invalid type ascription, term has type
  @has_lt.lt nat nat.has_lt (@has_pow.pow nat nat (@monoid.has_pow nat nat.monoid) n 2)
    (@has_mul.mul nat nat.has_mul n m)
but is expected to have type
  @has_lt.lt nat nat.has_lt (@has_pow.pow nat nat nat.has_pow n 2) (@has_mul.mul nat nat.has_mul n m)
</pre></div>

#### [ Kevin Buzzard (Jul 25 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130245103):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">nat</span><span class="bp">.</span><span class="n">pow_two</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">=</span> <span class="n">a</span> <span class="bp">*</span> <span class="n">a</span> <span class="o">:=</span> <span class="k">show</span> <span class="o">(</span><span class="mi">1</span> <span class="bp">*</span> <span class="n">a</span><span class="o">)</span> <span class="bp">*</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">a</span> <span class="bp">*</span> <span class="n">a</span><span class="o">,</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">one_mul</span>

<span class="kn">theorem</span> <span class="n">thing</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">*</span> <span class="n">n</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="bp">*</span> <span class="n">m</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">n</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="bp">*</span> <span class="n">m</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">pow_two</span> <span class="n">n</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span> <span class="bp">▸</span> <span class="n">h</span>
</pre></div>

#### [ Kaushik Chakraborty (Jul 25 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130246833):
<p>thanks <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span>  this worked. however, I have some doubts about the <code>nat.pow_two</code> theorem. In your proof, you showed a different equality than what is in the sig. of the theorem. Is Lean somehow guessing the fact that <code>(1 * a) * a = a ^ 2</code>. Or how is the rewrite tactics working here?</p>

#### [ Nicholas Scheel (Jul 25 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130247804):
<p>that’s obtained by unfolding the definition of <code>pow</code>, which basically is that <code>n^a = (((1*n)*n)*...)*n</code> (with <code>a</code> <code>n</code>s of course)</p>

#### [ Kaushik Chakraborty (Jul 25 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130261244):
<p>got it. thanks, <span class="user-mention" data-user-id="111651">@Nicholas Scheel</span></p>

#### [ Kevin Buzzard (Jul 25 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/130263722):
<p>Yes, there are two kinds of equality in Lean. There's "equal by definition" and "equal because of a theorem". <code>a^2=1*a*a</code> is true by definition of <code>^</code> (you can discover this sort of thing by continually unfolding everything -- switch off notation and just get unfolding in tactic mode and see where you go) but <code>1*a=a</code> is true because of a theorem. Things that are equal by definition you can just use interchangeably (I used <code>show</code> to change the goal to a goal which Lean thinks is the same goal by definition), but then I used a rewrite to apply the theorem.</p>

#### [ Kaushik Chakraborty (Aug 09 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/131140816):
<p>I am trying to attempt a Lean proof of quotient-remainder theorem shown <a href="https://leanprover.github.io/logic_and_proof/elementary_number_theory.html#the-quotient-remainder-theorem" target="_blank" title="https://leanprover.github.io/logic_and_proof/elementary_number_theory.html#the-quotient-remainder-theorem">here</a> and, as usual, clueless on the approach. I've tried to chalk out a rough skeleton of the proof based on my understandings from an earlier chapter on doing induction in Lean &amp; some exploration of Lean's types and functions. Does it make sense?</p>
<div class="codehilite"><pre><span></span>open int
open nat

 -- quotient / remainder theorem
theorem qt (n m q r : ℤ) : m &gt; 0 → n = m * q + r ∧ (0 ≤ r ∧ r &lt; m) :=
assume h,
show (n = m * q + r) ∧ (0 ≤ r ∧ r &lt; m), from
  int.rec_on n
  (assume k,
  show (of_nat k = m * q + r) ∧ ( 0 ≤ r ∧ r &lt; m ), from
    nat.rec_on k
      (show (of_nat 0 = m * q + r) ∧ (0 ≤ r ∧ r &lt; m), from sorry)
      (assume k ih,
        show of_nat (succ k) = m * q + r ∧ (0 ≤ r ∧ r &lt; m), from sorry)
  )
  (assume k,
    have h11 : -of_nat (k + 1) = m * q + r, from sorry,
    have h22 : 0 ≤ r ∧ r &lt; m, from sorry,
    ⟨ h11 , h22 ⟩)
</pre></div>

#### [ Chris Hughes (Aug 09 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/131141198):
<p>The theorem isn't true. This says for all n m q r, ... Whereas you want <code>forall m n, exists q r,...</code></p>

#### [ Chris Hughes (Aug 09 2018 at 02:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/131141265):
<p>the proof of this theorem in the lean library is a combination of <code>int.mod_add_div</code>, <code>int.mod_lt</code>  and <code>int.mod_nonneg</code>.</p>

#### [ Kaushik Chakraborty (Aug 09 2018 at 07:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/131151108):
<p>Oh, thanks for clarifying. Does this theorem statement make sense?</p>
<div class="codehilite"><pre><span></span>theorem qt : ∀ n m : ℤ, m &gt; 0 → ∃ q r : ℤ, (n = m * q + r) ∧ (0 ≤ r ∧ r &lt; m) :=
sorry
</pre></div>

#### [ Kaushik Chakraborty (Aug 09 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/131155084):
<p>I tried to solve the above statement with the functions you mentioned but I could not figure out how to come up with the existential terms <code>q</code> &amp; <code>r</code> from <code>n</code> and  <code>m</code> and hence the proof does not type check. I must be formulating the theorem statement wrong or missing some approach in the proof.</p>
<div class="codehilite"><pre><span></span>theorem qt : ∀ n m : ℤ, m &gt; 0 → ∃ q r : ℤ, n = m * q + r ∧ (0 ≤ r ∧ r &lt; m) :=
assume n m h,

assume q r,
assume h2 : q = n / m,
assume h1 : r = n % m,

have HH:  n = m * q + r, from calc
  n = n % m + m * (n / m) : by rw [int.mod_add_div]
  ... = r + m * (n / m) : by rw h1
  ... = r + (m * q) : by rw h2
  ... = (m * q) + r : by rw add_comm,

have HH1: 0 ≤ r, from calc
  0 ≤ n % m : int.mod_nonneg n (ne_of_gt h)
  ... ≤ r : by rw h1,

have HH2: r &lt; m, from calc
  r = n % m : by rw h1
  ... &lt; abs m : int.mod_lt n (ne_of_gt h)
  ... = m : abs_of_pos h,

exists.intro q (exists.intro r (and.intro HH  (and.intro HH1 HH2) ))
</pre></div>

#### [ Mario Carneiro (Aug 09 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/131155253):
<p>This is an incorrect use of the <code>assume</code> keyword. <code>assume</code> is used <em>only</em> for proving a forall or pi or implication, and it introduces a variable with the type specified in the domain. To prove an existential, you use <code>exists.intro</code> and provide the witness you want</p>

#### [ Mario Carneiro (Aug 09 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/131155369):
<p>So after <code>assume n m h,</code> you should write <code>exists.intro (n / m) $ exists.intro (n % m) $</code> instead of <code>assume q r, assume h2 : q = n / m, assume h1 : r = n % m,</code></p>

#### [ Mario Carneiro (Aug 09 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/131155379):
<p>(The dollar signs are to save on having to close parentheses at the end of the proof)</p>

#### [ Mario Carneiro (Aug 09 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/131155394):
<p>After that, <code>q</code> and <code>r</code> will no longer be present in the statement, so you won't need to rewrite with <code>h1</code> anymore</p>

#### [ Kaushik Chakraborty (Aug 09 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Logic%20%26%20Proof/near/131157187):
<p>I knew what was wrong with that <em>assume</em> but your tip on the <code>exists.intro</code> was helpful. Here's my updated proof which type checks</p>
<div class="codehilite"><pre><span></span>theorem qt : ∀ n m : ℤ, m &gt; 0 → ∃ q r : ℤ, n = m * q + r ∧ (0 ≤ r ∧ r &lt; m) :=
assume n m h,

exists.intro (n / m) $ exists.intro (n % m) $

  have HH:  n = m * (n / m)  + (n % m), from calc
    n = n % m + m * (n / m) : by rw [int.mod_add_div]
    ... = m * (n / m) + (n % m) : by rw add_comm,

  have HH1: 0 ≤ (n % m), from int.mod_nonneg n (ne_of_gt h),

  have HH2: (n % m) &lt; m, from calc
    (n % m) &lt; abs m : int.mod_lt n (ne_of_gt h)
    ... = m : abs_of_pos h,

  ⟨ HH , ⟨ HH1 , HH2 ⟩ ⟩
</pre></div>


{% endraw %}
