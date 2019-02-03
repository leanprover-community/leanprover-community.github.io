---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/46824Usehaveonorhypothesis.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [Use "have" on "or" hypothesis](https://leanprover-community.github.io/archive/113489newmembers/46824Usehaveonorhypothesis.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Abhimanyu Pallavi Sudhir (Oct 06 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135318782):
<p>If we had a hypothesis "HX: ∀x : nat, x ^ 2 - 3 * x + 2 = 0" and wanted to prove "false", we could do so by writing "have H3 := HX 3," and then revert and do norm_num.</p>
<p>But "∀x : nat, x ^ 2 - 3 * x + 2 = 0" is just a way of writing "x = 0 ∨ x = 1 ∨ x = 2 ∨ ... → x ^ 2 - 3 * x + 2 = 0". If instead you had "x = 1 ∨ x = 2 ∨ x = 3 → x ^ 2 - 3 * x + 2 = 0", what is the equivalent of the "have" command?</p>

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135319310):
<p>This works:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span> <span class="bp">∨</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">2</span> <span class="bp">∨</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">3</span> <span class="bp">→</span> <span class="n">x</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">-</span> <span class="mi">3</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">+</span> <span class="mi">2</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">→</span> <span class="n">false</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">intros</span> <span class="n">hx</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">or</span><span class="bp">.</span><span class="n">elim</span> <span class="n">hx</span> <span class="o">(</span><span class="k">by</span> <span class="o">{</span> <span class="n">intro</span> <span class="n">h</span><span class="o">,</span> <span class="n">simp</span> <span class="o">[</span><span class="n">h</span><span class="o">]</span> <span class="n">at</span> <span class="n">H</span><span class="o">,</span> <span class="n">contradiction</span> <span class="o">})</span>
    <span class="o">(</span><span class="k">by</span> <span class="o">{</span> <span class="n">intro</span> <span class="n">h&#39;</span><span class="o">,</span>
      <span class="n">exact</span> <span class="n">or</span><span class="bp">.</span><span class="n">elim</span> <span class="n">h&#39;</span> <span class="o">(</span><span class="k">by</span> <span class="o">{</span> <span class="n">intro</span> <span class="n">h</span><span class="o">,</span> <span class="n">simp</span> <span class="o">[</span><span class="n">h</span><span class="o">]</span> <span class="n">at</span> <span class="n">H</span><span class="o">,</span> <span class="n">contradiction</span> <span class="o">})</span>
        <span class="o">(</span><span class="k">by</span> <span class="o">{</span> <span class="n">intro</span> <span class="n">h</span><span class="o">,</span> <span class="n">simp</span> <span class="o">[</span><span class="n">h</span><span class="o">]</span> <span class="n">at</span> <span class="n">H</span><span class="o">,</span> <span class="n">contradiction</span> <span class="o">})</span> <span class="o">})</span>
<span class="kn">end</span>
</pre></div>


<p>There's probably a cleaner way to do it involving pattern-matching / better use of tactics though.</p>

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135319743):
<p>Oh this is weird. If I import <code>tactic.norm_num</code>, the second <code>contradiction</code> above fails because after <code>simp [h] at H</code> we have <code>H : 2 = 0 ∧ 2 ^ 2 - 3 * 2 = 0</code> instead of <code>H : 2 + (2 ^ 2 - 3 * 2) = 0</code>. That's scary.</p>
<p>And the following gives me <code>no goals</code> by the end, but also a strange error under <code>example</code>:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">norm_num</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span> <span class="bp">∨</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">2</span> <span class="bp">∨</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">3</span> <span class="bp">→</span> <span class="n">x</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">-</span> <span class="mi">3</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">+</span> <span class="mi">2</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">→</span> <span class="n">false</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">intros</span> <span class="n">hx</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">or</span><span class="bp">.</span><span class="n">elim</span> <span class="n">hx</span> <span class="o">(</span><span class="k">by</span> <span class="o">{</span> <span class="n">revert</span> <span class="n">H</span><span class="o">,</span> <span class="n">norm_num</span> <span class="o">})</span>
    <span class="o">(</span><span class="k">by</span> <span class="o">{</span> <span class="n">intro</span> <span class="n">h&#39;</span><span class="o">,</span>
      <span class="n">exact</span> <span class="n">or</span><span class="bp">.</span><span class="n">elim</span> <span class="n">h&#39;</span> <span class="o">(</span><span class="k">by</span> <span class="o">{</span> <span class="n">revert</span> <span class="n">H</span><span class="o">,</span> <span class="n">norm_num</span> <span class="o">})</span>
        <span class="o">(</span><span class="k">by</span> <span class="o">{</span> <span class="n">revert</span> <span class="n">H</span><span class="o">,</span> <span class="n">norm_num</span> <span class="o">})</span> <span class="o">})</span>
<span class="kn">end</span>
<span class="c">/-</span><span class="cm"> type mismatch at application</span>
<span class="cm">  eq.trans (nat.pow_eq_pow x 2) (norm_num.pow_bit0_helper x x 1 (pow_one x))</span>
<span class="cm">term</span>
<span class="cm">  norm_num.pow_bit0_helper x x 1 (pow_one x)</span>
<span class="cm">has type</span>
<span class="cm">  @eq nat (@has_pow.pow nat nat (@monoid.has_pow nat nat.monoid) x 2)</span>
<span class="cm">    (@has_mul.mul nat (@semigroup.to_has_mul nat (@monoid.to_semigroup nat nat.monoid)) x x)</span>
<span class="cm">but is expected to have type</span>
<span class="cm">  @eq nat (@has_pow.pow nat nat nat.has_pow x 2)</span>
<span class="cm">    (@has_mul.mul nat (@semigroup.to_has_mul nat (@monoid.to_semigroup nat nat.monoid)) x x) -/</span>
</pre></div>

#### [ Abhimanyu Pallavi Sudhir (Oct 06 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135319963):
<blockquote>
<p>This works:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span> <span class="bp">∨</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">2</span> <span class="bp">∨</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">3</span> <span class="bp">→</span> <span class="n">x</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">-</span> <span class="mi">3</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">+</span> <span class="mi">2</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">→</span> <span class="n">false</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">intros</span> <span class="n">hx</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">or</span><span class="bp">.</span><span class="n">elim</span> <span class="n">hx</span> <span class="o">(</span><span class="k">by</span> <span class="o">{</span> <span class="n">intro</span> <span class="n">h</span><span class="o">,</span> <span class="n">simp</span> <span class="o">[</span><span class="n">h</span><span class="o">]</span> <span class="n">at</span> <span class="n">H</span><span class="o">,</span> <span class="n">contradiction</span> <span class="o">})</span>
    <span class="o">(</span><span class="k">by</span> <span class="o">{</span> <span class="n">intro</span> <span class="n">h&#39;</span><span class="o">,</span>
      <span class="n">exact</span> <span class="n">or</span><span class="bp">.</span><span class="n">elim</span> <span class="n">h&#39;</span> <span class="o">(</span><span class="k">by</span> <span class="o">{</span> <span class="n">intro</span> <span class="n">h</span><span class="o">,</span> <span class="n">simp</span> <span class="o">[</span><span class="n">h</span><span class="o">]</span> <span class="n">at</span> <span class="n">H</span><span class="o">,</span> <span class="n">contradiction</span> <span class="o">})</span>
        <span class="o">(</span><span class="k">by</span> <span class="o">{</span> <span class="n">intro</span> <span class="n">h</span><span class="o">,</span> <span class="n">simp</span> <span class="o">[</span><span class="n">h</span><span class="o">]</span> <span class="n">at</span> <span class="n">H</span><span class="o">,</span> <span class="n">contradiction</span> <span class="o">})</span> <span class="o">})</span>
<span class="kn">end</span>
</pre></div>


<p>There's probably a cleaner way to do it involving pattern-matching / better use of tactics though.</p>
</blockquote>
<p>Wait a minute -- that's not the correct goal, though. The order of associativity is wrong.</p>

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135320003):
<p>Oops, you're right! Let me take another look.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 06 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135320004):
<p>I'm actually confused as to how you managed to prove that statement at all -- it's not true that for <em>any</em> x, x^2 - 3x + 2 = 0 is false.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 06 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135320065):
<p>(deleted)</p>

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135320281):
<p>It's true that the goal <code>(x = 1 ∨ x = 2 ∨ x = 3 → x ^ 2 - 3 * x + 2 = 0) → false</code> can't be proved (I just spent an embarrassingly long time attempting it nonetheless), but as you say, that's quite different from the one I proved above, which is <code>x = 1 ∨ x = 2 ∨ x = 3 → (x ^ 2 - 3 * x + 2 = 0 → false)</code>.</p>

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135320384):
<p>Anyways, returning to your original question, my instinct when I want to use hypotheses of the form <code>H : h1 ∨ h2</code> is to immediately start writing <code>exact or.elim H (by {}) (by {})</code> and then start filling in the curly braces. I'd be curious if more experienced members have better advice.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 06 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135320389):
<p>You must've made a typo -- the two statements you've written are identical.</p>

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135320414):
<p>Yes, sorry about that. I've fixed it above.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 06 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135320483):
<p>That can't be right -- (P → Q) → false just means that P → Q is false, which is exactly right, since indeed Q is not always true when P is true. (...I'm letting P: x = 1 ∨ x = 2 ∨ x = 3 and Q : x ^ 2 - 3 * x + 2 = 0)</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 06 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135320532):
<p>On the other hand P → (Q → false) (which you proved, although I have no clue how it worked) can't be right, since that implies Q is <em>always</em> false when P is true. But this isn't right, since you can have x = 1 or x = 2, for which P is true and Q is true.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 06 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135320554):
<p>I must be confused on something basic here, as Lean couldn't possibly accept a proof of a false statement.</p>

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135320611):
<p>I think we should be careful with the quantifiers here. There's a (x : nat) before the statement, which is \forall x in front of everything.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 06 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135320669):
<p>But how does that make a difference?</p>

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135320781):
<p>You're right. That doesn't. I think I'm getting confused now too. :) Give me a minute.</p>

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135321000):
<p>haha, OK. I see the issue. Remember that subtraction over the nats won't do what you expect, in particular n - m when n &lt; m gives you zero!</p>

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135321004):
<p>That explains the second part. Let me now put together a proof of the first part.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 06 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135321011):
<p>(deleted)</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 06 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135321061):
<p>Ah, ok, I see. Changing nat to int does break things.</p>

#### [ Kevin Buzzard (Oct 06 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135322325):
<p>It's still true that <code>3 ^ 2 - 3 * 3 + 2 = 0</code> is false in <code>nat</code>, even though subtraction is not the mathematics subtraction on nat.</p>

#### [ Chris Hughes (Oct 06 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135322374):
<p>(deleted)</p>

#### [ Kevin Buzzard (Oct 06 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135322375):
<p>I guess you should be proving <code>example : ¬ (∀ x, x = 1 ∨ x = 2 ∨ x = 3 → x ^ 2 - 3 * x + 2 = 0) := sorry</code></p>

#### [ Kevin Buzzard (Oct 06 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135322383):
<p>The way to think about it is that if something is directly before the colon, you can move it to the right but you then have to add a universal quantifier. I agree that these things are confusing!</p>

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135323812):
<p>Consider the following:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span> <span class="bp">∨</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">2</span> <span class="bp">∨</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">3</span> <span class="bp">→</span> <span class="n">x</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">-</span> <span class="mi">3</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">+</span> <span class="mi">2</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span> <span class="bp">∨</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">2</span> <span class="bp">∨</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">3</span> <span class="bp">→</span> <span class="n">x</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">-</span> <span class="mi">3</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">+</span> <span class="mi">2</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span> <span class="bp">→</span> <span class="n">false</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>As Kevin says, the stuff to the left of the colon corresponds to a forall quantifier. One thing to keep in mind is that with the forall quantifiers there, these expressions are closely related to certain Prop-valued functions (predicates) over the nats. The first predicate (λ x, x = 1 ∨ x = 2 ∨ x = 3 → x ^ 2 - 3 * x + 2 = 0) happens to be false for every nat, so we have finally:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span> <span class="bp">∨</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">2</span> <span class="bp">∨</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">3</span> <span class="bp">→</span> <span class="n">x</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">-</span> <span class="mi">3</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">+</span> <span class="mi">2</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span> <span class="bp">→</span> <span class="n">false</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">intro</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">replace</span> <span class="n">h</span> <span class="o">:=</span> <span class="n">h</span> <span class="mi">1</span> <span class="o">(</span><span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="n">rfl</span><span class="o">),</span>
  <span class="n">contradiction</span>
<span class="kn">end</span>
</pre></div>


<p>The predicate corresponding to the second one (λ x, (x = 1 ∨ x = 2 ∨ x = 3 → x ^ 2 - 3 * x + 2 = 0) → false) is sometimes true and sometimes false. In particular it's true when x=1, x=2, x=3 but false everywhere else. The Prop version of this (∀x, (x = 1 ∨ x = 2 ∨ x = 3 → x ^ 2 - 3 * x + 2 = 0) → false) then should be false, so </p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="o">(</span><span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span> <span class="bp">∨</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">2</span> <span class="bp">∨</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">3</span> <span class="bp">→</span> <span class="n">x</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">-</span> <span class="mi">3</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">+</span> <span class="mi">2</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span> <span class="bp">→</span> <span class="n">false</span><span class="o">)</span> <span class="bp">→</span> <span class="n">false</span><span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">intro</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">replace</span> <span class="n">H</span> <span class="o">:=</span> <span class="n">H</span> <span class="mi">0</span><span class="o">,</span>
  <span class="n">simp</span> <span class="n">at</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">H</span> <span class="o">(</span><span class="k">by</span> <span class="o">{</span> <span class="n">intro</span> <span class="n">h</span><span class="o">,</span> <span class="n">exact</span> <span class="n">or</span><span class="bp">.</span><span class="n">elim</span> <span class="n">h</span> <span class="o">(</span><span class="k">by</span> <span class="n">contradiction</span><span class="o">)</span> <span class="o">(</span><span class="k">by</span> <span class="n">contradiction</span><span class="o">)</span> <span class="o">})</span>
<span class="kn">end</span>
</pre></div>

#### [ Abhimanyu Pallavi Sudhir (Oct 06 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135324682):
<p>Thanks -- that makes sense. And although the notation you gave (<code>replace h := h 1 (or.inl rfl),</code>) doesn't seem to be working, I guess just adding the forall x allows one to use the <code>have</code> command normally, i.e. as <code>have h3 := h 3,</code></p>

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135324850):
<p>Sorry for all the edits! Thinking about this definitely cleared up a lot of confusion on my end. Hopefully it's all right now.</p>
<p><code>replace</code> only works in tactic mode, so if you're using term mode, you'll have to do what you did with <code>have</code>.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 06 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325128):
<p>Tactic mode just means enclosed by <code>begin</code> and <code>end</code>, right? <code>replace</code> doesn't seem to be working for me in tactic mode either. I'm using the web editor, does that affect things?</p>

#### [ Kenny Lau (Oct 06 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325137):
<p>you need to <code>import tactic.interactive</code></p>

#### [ Kevin Buzzard (Oct 06 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325174):
<p>Yes, tactic mode is anything with in a <code>begin/.../end</code> or <code>by {...}</code>.</p>

#### [ Kevin Buzzard (Oct 06 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325183):
<p>Aah, <code>replace</code> is a mathlib tactic?</p>

#### [ Kevin Buzzard (Oct 06 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325192):
<p>If you have <code>norm_num</code> imported then these basic tactic imports will come too I guess.</p>

#### [ Patrick Massot (Oct 06 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325199):
<p>Congratulations to both of you: you went through a very important Lean initiatory ritual, where the initiate becomes utterly confused, loses all confidence in his or her most elementary mathematical skills. You met ℕ substraction!</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 06 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325204):
<blockquote>
<p>you need to <code>import tactic.interactive</code></p>
</blockquote>
<p>Oh, thanks, works.</p>

#### [ Kevin Buzzard (Oct 06 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325208):
<p><span class="user-mention" data-user-id="130500">@Abhimanyu Pallavi Sudhir</span> the lean web editor is horrible! Are you using Lean on a computer you own, or a computer at Imperial?</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 06 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325261):
<blockquote>
<p><span class="user-mention" data-user-id="130500">@Abhimanyu Pallavi Sudhir</span> the lean web editor is horrible! Are you using Lean on a computer you own, or a computer at Imperial?</p>
</blockquote>
<p>My own computer. It (the web editor) seems to be okay for basic proofs, though.</p>

#### [ Kevin Buzzard (Oct 06 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325271):
<p>What OS?</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 06 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325275):
<p>Windows.</p>

#### [ Kevin Buzzard (Oct 06 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325281):
<p>Patrick -- that logic stuff is super-confusing, and broken <code>-</code> makes things worse :-)</p>

#### [ Kenny Lau (Oct 06 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325335):
<blockquote>
<p>Windows.</p>
</blockquote>
<p>install a linux VM</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 06 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325337):
<p>I do have a Linux VM (Ubuntu, if that still counts). It's just really slow.</p>

#### [ Kevin Buzzard (Oct 06 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325338):
<p>Win10 or 7?</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 06 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325339):
<p>Win 10.</p>

#### [ Kevin Buzzard (Oct 06 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325341):
<p>OK I have a cheap way of installing Lean on your PC</p>

#### [ Kenny Lau (Oct 06 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325346):
<blockquote>
<p>I do have a Linux VM. It's just really slow.</p>
</blockquote>
<p>it was a joke</p>

#### [ Kevin Buzzard (Oct 06 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325357):
<p>For Sage they used to recommend that peolpe on Windows just ran it in a Linux VM</p>

#### [ Kevin Buzzard (Oct 06 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325364):
<p>(deleted)</p>

#### [ Kevin Buzzard (Oct 06 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325366):
<p>wait that won't work for you</p>

#### [ Chris Hughes (Oct 06 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325368):
<p>Scott's new method should work, provided there are no spaces in your username.</p>

#### [ Kevin Buzzard (Oct 06 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325413):
<p><a href="https://xenaproject.wordpress.com/getting-lean-and-mathlib-running-in-the-mlc/" target="_blank" title="https://xenaproject.wordpress.com/getting-lean-and-mathlib-running-in-the-mlc/">https://xenaproject.wordpress.com/getting-lean-and-mathlib-running-in-the-mlc/</a></p>

#### [ Kevin Buzzard (Oct 06 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325415):
<p>That way is super-cheap and needs no git or command line.</p>

#### [ Kevin Buzzard (Oct 06 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325419):
<p>However Scott's method is much better, because it will enable you to upgrade properly.</p>

#### [ Kenny Lau (Oct 06 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325428):
<p><a href="https://gist.github.com/kckennylau/611cc453c67df074ad492b4939ddd356" target="_blank" title="https://gist.github.com/kckennylau/611cc453c67df074ad492b4939ddd356">https://gist.github.com/kckennylau/611cc453c67df074ad492b4939ddd356</a></p>

#### [ Kenny Lau (Oct 06 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325430):
<p>this is the one that I use</p>

#### [ Kenny Lau (Oct 06 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325433):
<p>but they don't really recommend this</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 06 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135325546):
<p>Oh ok. I'll try the cheap way for now -- I'll just re-install the updated versions manually.</p>

#### [ Kevin Buzzard (Oct 07 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135327522):
<blockquote>
<p>this is the one that I use</p>
</blockquote>
<p>Kenny, that involves compiling Lean. What's the point of doing that now? Lean has been stable for ages, you can just take the binary.</p>

#### [ Kenny Lau (Oct 07 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135327573):
<p>I see</p>

#### [ Kevin Buzzard (Oct 07 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135329837):
<p><span class="user-mention" data-user-id="130500">@Abhimanyu Pallavi Sudhir</span> the way dependent type theory works is that it prefers  functions to be defined everywhere and just give junk values at places mathematicians would not normally evaluate them, and it also wants things like <code>-</code> to go from <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>X</mi><mo>×</mo><mi>X</mi></mrow><annotation encoding="application/x-tex">X\times X</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.76666em;vertical-align:-0.08333em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.07847em;">X</span><span class="mbin">×</span><span class="mord mathit" style="margin-right:0.07847em;">X</span></span></span></span> to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>X</mi></mrow><annotation encoding="application/x-tex">X</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.07847em;">X</span></span></span></span>, for varying <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>X</mi></mrow><annotation encoding="application/x-tex">X</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.07847em;">X</span></span></span></span> (see around 300 lines in in <code>core.lean</code> in the core lean library -- <code>class has_sub      (α : Type u) := (sub : α → α → α)</code> and <code>class has_div      (α : Type u) := (div : α → α → α)</code> ). This means that subtraction on <code>nat</code> has to take two nats and give back a <code>nat</code> (hence <code>2 - 3 = 0</code>) and division on, say, the reals, has to take two reals and give back a real, hence <code>1 / 0 = 0</code>. This isn't a logical problem -- they have just artificially extended these functions to places where mathematicians would not normally use them; I think of <code>-</code> and <code>/</code> as being "computer science versions" of these operators, and in the statements of theorems I care about, if either of them are used then I have to do a little check to make sure that the results imply what I want them to say. Of course it doens't matter in the proofs -- you would not object if a mathematician defined a new function <code>f(x,y)</code> to be <code>x/y</code> if <code>y</code> was non-zero but <code>0</code> if <code>y</code> was zero and then used <code>f</code> in proofs; that's all that's happening here. Subtraction is particularly horrible because at least division gives the same weird answer in all cases; the behaviour of subtraction actually changes if you move from <code>nat</code> (where it's weird) to <code>int</code> (where it's normal).</p>

#### [ Andrew Ashworth (Oct 07 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135330196):
<p><span class="emoji emoji-1f600" title="grinning">:grinning:</span> Could be worse. With computers, <code>((0 : uint32_t) - 1) = 4294967295</code>.</p>

#### [ Kevin Buzzard (Oct 07 2018 at 01:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135330204):
<p>so Lean's convention is actually closer in this case ;-)</p>

#### [ Scott Olson (Oct 07 2018 at 05:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135335803):
<p>I'd argue it's quite natural to define versions of functions like <code>nat.sub</code> or division that restrict their domain (either by type or dependent hypothesis argument) rather than returning "junk" values, but it depends on the use case. For example, it's quite nice that <code>nat.sub</code> <em>precisely</em> matches the structure of <code>list.drop</code>, so you can prove things like <code>list.drop n (list.repeat a m) = list.repeat a (m - n)</code>.</p>
<p>But you could look at Idris for example where the total division function has type <code>Nat -&gt; (y : Nat) -&gt; Not (y = Z) -&gt; Nat</code>, or look at <code>List.head : (l : List a) -&gt; {auto ok : NonEmpty l} -&gt; a</code> as opposed to Lean's <code>list.head : Π {α} [inhabited α], list α → α</code>.</p>
<p>On the other hand, both Lean and Idris have a <code>head' : list α → option α</code> alternative which is the preferred API in non-dependent modern programming languages, since you can chain convenient methods on the resulting <code>option</code> to deal with the error case in different ways.</p>

#### [ Scott Olson (Oct 07 2018 at 05:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135336120):
<p>Though as <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> pointed out, the interface the operator typeclasses have in Lean would get in the way of doing anything like this for the normal subtraction or division syntax.</p>

#### [ Kevin Buzzard (Oct 07 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135342844):
<p>I've long been convinced that Lean's approach is the simplest -- but Abhi is a new student at Imperial and I'd not mentioned this stuff to the students yet, and for a mathematician the convention is quite disconcerting and unexpected. As I pointed out recently, mathematicians expect to divide the integer 1 by the integer 2 and get the rational <code>1/2</code> because that's what happens with all the standard maths packages. I recently mentioned a possible typeclass trick which might let us emulate that here but it would need a lot of testing until we got it right.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 07 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135345234):
<blockquote>
<p><span class="user-mention" data-user-id="130500">@Abhimanyu Pallavi Sudhir</span> the way dependent type theory works is that it prefers  functions to be defined everywhere and just give junk values at places mathematicians would not normally evaluate them... the behaviour of subtraction actually changes if you move from nat (where it's weird) to int (where it's normal).</p>
</blockquote>
<p>Yeah, I get that -- although I'm not sure why this is better than just defining an object called "undefined" (as javascript does it with 1/0, for instance).</p>

#### [ Kenny Lau (Oct 07 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135345376):
<p>then the codomain wouldn't be N anymore</p>

#### [ Kenny Lau (Oct 07 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135345377):
<p>I'm not sure if javascript functions care about whether its codomain includes <code>undefined</code></p>

#### [ Scott Olson (Oct 07 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135345429):
<p>In a typed setting, the equivalent of that approach is to return <code>option nat</code> as in one of my examples above. I've seen almost no one ever do this for division, though</p>

#### [ Mario Carneiro (Oct 07 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135345683):
<p>This is an option. I think there is actually a function <code>nat.psub</code> that implements this</p>

#### [ Mario Carneiro (Oct 07 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135345726):
<p>These sorts of functions often go by the name e.g. "safe division"</p>

#### [ Scott Olson (Oct 07 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135345872):
<p>I think part of the argument for just using a junk value is that proofs about division like <code>div_self : a ≠ 0 → a / a = 1</code> will need to include the precondition <code>a ≠ 0</code> regardless of which definition for division you choose, and so you might as well pick a simple one.</p>
<p>It would be more controversial to define nat/integer division the Lean way for general purpose programming, but even that has been done</p>

#### [ Kevin Buzzard (Oct 07 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135346494):
<p>The point simply seems to be that whilst there are several methods for "fixing the problem" (as mathematicians would interpret it), all the ones I've tried seem to result in the "problem being fixed", the functions now being more of a pain to use in practice, and then the dawning realisation that actually...was this ever really a problem? Or was it just a psychological issue? There is no foundational logical issue -- the computer scientists are just using  a different function from mathematician's division, and calling it the same name. Mathematicians just need to be aware that these are not the functions they're used to, that the function they're used to can easily be constructed, but do they really <em>need</em> the functions they're used to? I'm not convinced they do.</p>

#### [ Kevin Buzzard (Oct 07 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22have%22%20on%20%22or%22%20hypothesis/near/135346514):
<p>What they need instead is to be educated that the CS functions are different and to be aware of this.</p>


{% endraw %}
