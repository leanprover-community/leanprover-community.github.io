---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/99121natinequalities.html
---

## Stream: [new members](index.html)
### Topic: [nat inequalities](99121natinequalities.html)

---


{% raw %}
#### [ Scott Olson (Sep 25 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20inequalities/near/134592941):
<p>What is the most efficient way to solve situations like this? I get a bit lost in all the details of lt, le, negations, and symmetries...</p>
<div class="codehilite"><pre><span></span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span>
<span class="n">is_lt</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="mi">2</span><span class="o">,</span>
<span class="n">h_zero</span> <span class="o">:</span> <span class="bp">¬</span><span class="n">x</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">,</span>
<span class="n">h_one</span> <span class="o">:</span> <span class="bp">¬</span><span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span>
<span class="err">⊢</span> <span class="n">false</span>
</pre></div>

#### [ Kevin Buzzard (Sep 25 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20inequalities/near/134593248):
<p>I am really bad at questions like this still, and I've been playing with Lean for a year. People come up with all sorts of tricks using tactics like <code>cc</code> or <code>finish</code> or a clever application of <code>dec_trivial</code> or whatever, which I never seem to spot.</p>

#### [ Reid Barton (Sep 25 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20inequalities/near/134593402):
<p>Depending on how you obtained the hypotheses <code>h_zero</code> and <code>h_one</code>, it might have been more efficient to use <code>cases</code> on <code>x</code> earlier</p>

#### [ Scott Olson (Sep 25 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20inequalities/near/134593796):
<p>I'm interested in the nat inequalites problem in general, but this came up while trying to match exhaustively on a <code>fin 2</code>. (It's a contrived example, I suppose, but I also run into <code>fin</code> troubles fairly often.)</p>
<p>The trouble there is I'm not sure how to make the pattern compiler understand I don't need any cases beyond 0 and 1, and if I do fill in the catch-all case, I wouldn't automatically even have <code>x != 0</code> and <code>x != 1</code> with which to prove this.</p>

#### [ Scott Olson (Sep 25 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20inequalities/near/134594159):
<p>Ohhh, I think I finally understood the useful way to match on them. If I use a <code>⟨n+2, is_lt⟩</code> pattern, I get the <code>is_lt : n + 2 &lt; 2</code> contradiction.</p>

#### [ Reid Barton (Sep 25 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20inequalities/near/134594218):
<p>Yes exactly</p>

#### [ Reid Barton (Sep 25 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20inequalities/near/134594230):
<p>Now you need to prove that's false, probably something like (made up names) <code>not_lt_of_ge (le_add_self _ _)</code></p>

#### [ Reid Barton (Sep 25 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20inequalities/near/134594252):
<p>and then combine that with <code>absurd is_lt ...</code></p>

#### [ Reid Barton (Sep 25 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20inequalities/near/134594422):
<p>For your original question you could do <code>cases</code> on <code>x</code>, handle the first case with <code>h_zero</code>, then <code>cases</code> again and handle the first case with <code>h_one</code>, then you'd be at proving <code>n + 2 &lt; 2 -&gt; false</code> again. But those two <code>cases</code> steps are just repeating some case analysis that you've already done, it sounds like (that's why you have <code>h_zero</code> and <code>h_one</code> in the first place).</p>

#### [ Scott Olson (Sep 25 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20inequalities/near/134594432):
<p>Yep, that makes sense. At that point I would just be going the long way around to do the same thing.</p>

#### [ Chris Hughes (Sep 25 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20inequalities/near/134594920):
<p><code>example : ∀ x : ℕ, x &lt; 2 → x ≠ 0 → x ≠ 1 → false := dec_trivial</code></p>

#### [ Reid Barton (Sep 25 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20inequalities/near/134595075):
<p>Aha! sneaky...</p>

#### [ Reid Barton (Sep 25 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20inequalities/near/134595259):
<p>So I guess <code>revert x, exact dec_trivial</code> should work for the original question. That's a good trick, changing the goal to something with a bounded quantifier</p>

#### [ Scott Olson (Sep 25 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20inequalities/near/134595295):
<p>Interesting, I was having trouble making that work in context, didn't realize I needed <code>revert x</code></p>

#### [ Scott Olson (Sep 25 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20inequalities/near/134595371):
<p>Does that work because <code>\all n &lt; k, p n</code> has a <code>decidable</code> instance or something tricky like that?</p>

#### [ Scott Olson (Sep 25 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20inequalities/near/134595456):
<p>Heh, yeah, I see instances like <code>decidable (∀ (n_1 : ℕ) (h : n_1 &lt; n), P n_1 h)</code></p>

#### [ Reid Barton (Sep 25 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20inequalities/near/134595469):
<p>Yes exactly</p>

#### [ Scott Olson (Sep 25 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20inequalities/near/134595513):
<p>Which is from mathlib, actually, so good thing I finally started using mathlib today...</p>

#### [ Scott Olson (Sep 25 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20inequalities/near/134596870):
<p>Thanks for all the help. For the record, this is the exercise I gave myself, and it looks pretty minimal now:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">fin2_equiv_bool</span> <span class="o">:</span> <span class="n">fin</span> <span class="mi">2</span> <span class="err">≃</span> <span class="n">bool</span> <span class="o">:=</span> <span class="o">{</span>
    <span class="n">to_fun</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">,</span>

    <span class="n">inv_fun</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">b</span><span class="o">,</span> <span class="n">cond</span> <span class="n">b</span> <span class="mi">1</span> <span class="mi">0</span><span class="o">,</span>

    <span class="n">left_inv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span>
        <span class="k">match</span> <span class="n">x</span> <span class="k">with</span>
        <span class="bp">|</span> <span class="bp">⟨</span><span class="mi">0</span><span class="o">,</span> <span class="bp">_⟩</span> <span class="o">:=</span> <span class="n">rfl</span>
        <span class="bp">|</span> <span class="bp">⟨</span><span class="mi">1</span><span class="o">,</span> <span class="bp">_⟩</span> <span class="o">:=</span> <span class="n">rfl</span>
        <span class="bp">|</span> <span class="bp">⟨</span><span class="n">n</span><span class="bp">+</span><span class="mi">2</span><span class="o">,</span> <span class="n">is_lt</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">absurd</span> <span class="n">is_lt</span> <span class="o">(</span><span class="n">not_lt_of_le</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">le_add_left</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">))</span>
        <span class="kn">end</span><span class="o">,</span>

    <span class="n">right_inv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">b</span><span class="o">,</span> <span class="k">by</span> <span class="n">cases</span> <span class="n">b</span><span class="bp">;</span> <span class="n">refl</span><span class="o">,</span>
<span class="o">}</span>
</pre></div>

#### [ Scott Olson (Sep 25 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20inequalities/near/134596887):
<p>Although now that we mentioned dec_trivial, it occurs to me I noticed <code>\all x : fin n, p x</code> is decidable...</p>

#### [ Kenny Lau (Sep 25 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20inequalities/near/134596982):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">equiv</span><span class="bp">.</span><span class="n">basic</span> <span class="n">data</span><span class="bp">.</span><span class="n">fin</span>

<span class="n">def</span> <span class="n">fin2_equiv_bool</span> <span class="o">:</span> <span class="n">fin</span> <span class="mi">2</span> <span class="err">≃</span> <span class="n">bool</span> <span class="o">:=</span> <span class="o">{</span>
    <span class="n">to_fun</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">,</span>
    <span class="n">inv_fun</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">b</span><span class="o">,</span> <span class="n">cond</span> <span class="n">b</span> <span class="mi">1</span> <span class="mi">0</span><span class="o">,</span>
    <span class="n">left_inv</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">unfold</span> <span class="n">function</span><span class="bp">.</span><span class="n">left_inverse</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">dec_trivial</span><span class="o">,</span>
    <span class="n">right_inv</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">unfold</span> <span class="n">function</span><span class="bp">.</span><span class="n">right_inverse</span> <span class="n">function</span><span class="bp">.</span><span class="n">left_inverse</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">dec_trivial</span><span class="o">,</span>
<span class="o">}</span>
</pre></div>

#### [ Scott Olson (Sep 25 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20inequalities/near/134597033):
<p>Thanks! The <code>unfold</code> is the only step I was missing in my attempt</p>

#### [ Kenny Lau (Sep 25 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20inequalities/near/134597181):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">equiv</span><span class="bp">.</span><span class="n">basic</span> <span class="n">data</span><span class="bp">.</span><span class="n">fin</span>

<span class="n">def</span> <span class="n">fin2_equiv_bool</span> <span class="o">:</span> <span class="n">fin</span> <span class="mi">2</span> <span class="err">≃</span> <span class="n">bool</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">to_fun</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">,</span>
  <span class="n">inv_fun</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">b</span><span class="o">,</span> <span class="n">cond</span> <span class="n">b</span> <span class="mi">1</span> <span class="mi">0</span><span class="o">,</span>
  <span class="n">left_inv</span> <span class="o">:=</span> <span class="k">show</span> <span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="bp">_</span> <span class="bp">=</span> <span class="n">x</span><span class="o">,</span> <span class="k">from</span> <span class="n">dec_trivial</span><span class="o">,</span>
  <span class="n">right_inv</span> <span class="o">:=</span> <span class="k">show</span> <span class="bp">∀</span> <span class="n">b</span><span class="o">,</span> <span class="bp">_</span> <span class="bp">=</span> <span class="n">b</span><span class="o">,</span> <span class="k">from</span> <span class="n">dec_trivial</span> <span class="o">}</span>
</pre></div>

#### [ Scott Olson (Sep 25 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20inequalities/near/134597623):
<p>It seems like the last part of these is failing for me because there's no instance of decidable for <code>\all b : bool, p b</code></p>

#### [ Kenny Lau (Sep 25 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20inequalities/near/134597665):
<p>did you follow the imports?</p>

#### [ Scott Olson (Sep 25 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20inequalities/near/134597733):
<p><code>data.equiv.basic</code> doesn't exist for me, I just have <code>data.equiv</code> in mathlib</p>

#### [ Scott Olson (Sep 25 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20inequalities/near/134597737):
<p>I do have <code>data.fin</code></p>

#### [ Scott Olson (Sep 25 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20inequalities/near/134597764):
<p>I'll double-check my mathlib dependency... I just added it with <code>leanpkg add leanprover/mathlib</code> earlier today</p>

#### [ Scott Olson (Sep 25 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20inequalities/near/134597839):
<p>I see, i think it gave me the branch named lean-3.4.1 instead of master</p>

#### [ Simon Hudon (Sep 25 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/nat%20inequalities/near/134619039):
<p>Does <code>linarith</code> work for your kind of inequality?</p>


{% endraw %}
