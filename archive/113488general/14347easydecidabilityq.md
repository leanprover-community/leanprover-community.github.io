---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/14347easydecidabilityq.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [easy decidability q](https://leanprover-community.github.io/archive/113488general/14347easydecidabilityq.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Jul 11 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129492071):
<p>Is this provable:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">multiset</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">C</span> <span class="o">:</span> <span class="n">multiset</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">decidable</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="n">a</span> <span class="bp">≥</span> <span class="mi">4</span> <span class="bp">∧</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">C</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>and if so, is there a cheap proof? I tried doing it by hand and ended up with a horrible heq goal :-/</p>

#### [ Kenny Lau (Jul 11 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129492098):
<p>yes it is provable</p>

#### [ Kenny Lau (Jul 11 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129492116):
<p>might want to destruct <code>C</code></p>

#### [ Simon Hudon (Jul 11 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129492249):
<p>Isn't membership in multisets decidable? You combine that fact with decidability of existentials on finite ranges</p>

#### [ Kevin Buzzard (Jul 11 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129492333):
<p>If I use lists I end up with</p>
<div class="codehilite"><pre><span></span>C1 C2 : list ℕ,
Crel : setoid.r C1 C2
⊢ eq.rec
      (list.rec (is_false _)
         (λ (n : ℕ) (L : list ℕ),
            decidable.rec
              (λ (D : ¬∃ (a : ℕ), a ≥ 4 ∧ a ∈ ↑L),
                 dite (3 &lt; n) (λ (h : 3 &lt; n), is_true _) (λ (h : ¬3 &lt; n), is_false _))
              (λ (D : ∃ (a : ℕ), a ≥ 4 ∧ a ∈ ↑L), is_true _))
         C1)
      _ =
    list.rec (is_false _)
      (λ (n : ℕ) (L : list ℕ),
         decidable.rec
           (λ (D : ¬∃ (a : ℕ), a ≥ 4 ∧ a ∈ ↑L),
              dite (3 &lt; n) (λ (h : 3 &lt; n), is_true _) (λ (h : ¬3 &lt; n), is_false _))
           (λ (D : ∃ (a : ℕ), a ≥ 4 ∧ a ∈ ↑L), is_true _))
      C2
</pre></div>

#### [ Kevin Buzzard (Jul 11 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129492409):
<p>If I use <code>multiset.rec</code> I end up with</p>
<div class="codehilite"><pre><span></span>a a&#39; : ℕ,
m : multiset ℕ,
b : decidable (∃ (a : ℕ), a ≥ 4 ∧ a ∈ m)
⊢ decidable.rec
      (λ (H : ¬∃ (a : ℕ), a ≥ 4 ∧ a ∈ a&#39; :: m),
         dite (3 &lt; a) (λ (h : 3 &lt; a), is_true _) (λ (h : ¬3 &lt; a), is_false _))
      (λ (H : ∃ (a : ℕ), a ≥ 4 ∧ a ∈ a&#39; :: m), is_true _)
      (decidable.rec
         (λ (H : ¬∃ (a : ℕ), a ≥ 4 ∧ a ∈ m),
            dite (3 &lt; a&#39;) (λ (h : 3 &lt; a&#39;), is_true _) (λ (h : ¬3 &lt; a&#39;), is_false _))
         (λ (H : ∃ (a : ℕ), a ≥ 4 ∧ a ∈ m), is_true _)
         b) ==
    decidable.rec
      (λ (H : ¬∃ (a_1 : ℕ), a_1 ≥ 4 ∧ a_1 ∈ a :: m),
         dite (3 &lt; a&#39;) (λ (h : 3 &lt; a&#39;), is_true _) (λ (h : ¬3 &lt; a&#39;), is_false _))
      (λ (H : ∃ (a_1 : ℕ), a_1 ≥ 4 ∧ a_1 ∈ a :: m), is_true _)
      (decidable.rec
         (λ (H : ¬∃ (a : ℕ), a ≥ 4 ∧ a ∈ m),
            dite (3 &lt; a) (λ (h : 3 &lt; a), is_true _) (λ (h : ¬3 &lt; a), is_false _))
         (λ (H : ∃ (a : ℕ), a ≥ 4 ∧ a ∈ m), is_true _)
         b)
</pre></div>

#### [ Kevin Buzzard (Jul 11 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129492413):
<p>I assume I'm doing something wrong.</p>

#### [ Kenny Lau (Jul 11 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129492442):
<p>I think there might be some lemmas that one could use</p>

#### [ Kenny Lau (Jul 11 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129492448):
<p>bounded existential</p>

#### [ Kevin Buzzard (Jul 11 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129492681):
<blockquote>
<p>Isn't membership in multisets decidable? You combine that fact with decidability of existentials on finite ranges</p>
</blockquote>
<p><code>example (D : multiset ℕ) (d : ℕ) : decidable (d ∈ D) := by apply_instance </code> works</p>

#### [ Kenny Lau (Jul 11 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129492691):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> shouldn't you be watching the world cup?</p>

#### [ Kevin Buzzard (Jul 11 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129492692):
<p>Oh, has it started?</p>

#### [ Kenny Lau (Jul 11 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129492694):
<p>:o</p>

#### [ Kenny Lau (Jul 11 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129492696):
<p>it's already 67 minutes</p>

#### [ Simon Hudon (Jul 11 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129492939):
<p>You can try this:</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">P</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">C</span> <span class="o">:</span> <span class="n">multiset</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">decidable</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">C</span><span class="o">,</span> <span class="n">P</span> <span class="n">a</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">sorry</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">C</span> <span class="o">:</span> <span class="n">multiset</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">decidable</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="n">a</span> <span class="bp">≥</span> <span class="mi">4</span> <span class="bp">∧</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">C</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">suffices</span> <span class="n">this</span> <span class="o">:</span> <span class="n">decidable</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">C</span><span class="o">,</span> <span class="n">a</span> <span class="bp">≥</span> <span class="mi">4</span><span class="o">),</span>
<span class="k">by</span> <span class="o">{</span> <span class="n">resetI</span><span class="o">,</span> <span class="n">apply</span> <span class="bp">@</span><span class="n">decidable_of_iff</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">this</span><span class="o">,</span> <span class="n">apply</span> <span class="n">exists_congr</span><span class="o">,</span> <span class="n">intro</span><span class="o">,</span> <span class="n">tauto</span> <span class="o">},</span>
<span class="k">by</span> <span class="o">{</span> <span class="n">apply_instance</span> <span class="o">}</span>
</pre></div>

#### [ Kenny Lau (Jul 11 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129492951):
<p>well you want P to be decidable</p>

#### [ Simon Hudon (Jul 11 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129493047):
<p>Yes, that's right</p>

#### [ Kevin Buzzard (Jul 11 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129493435):
<p>I don't understand how to use this code. If I comment out the instance then there's an error in the final <code>apply_instance</code> but if I look at what needs to be proved at that point it seems to be <code>decidable (∃ (a : ℕ) (H : a ∈ C), a ≥ 4)</code> which is exactly my question I think?</p>

#### [ Simon Hudon (Jul 11 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129494162):
<p>Ok, one second I'm filling in that instance</p>

#### [ Chris Hughes (Jul 11 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129494757):
<p>Add this before Simon'd code</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">decidable_exists_multiset</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">multiset</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">[</span><span class="n">decidable_pred</span> <span class="n">p</span><span class="o">]</span> <span class="o">:</span>
  <span class="n">decidable</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">s</span><span class="o">,</span> <span class="n">p</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">s</span>
<span class="n">list</span><span class="bp">.</span><span class="n">decidable_exists_mem</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span> <span class="n">h</span><span class="o">,</span> <span class="n">subsingleton</span><span class="bp">.</span><span class="n">elim</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span>
</pre></div>

#### [ Simon Hudon (Jul 11 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129494794):
<p>Nice! that's better than what I have</p>

#### [ Simon Hudon (Jul 11 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129494850):
<p>It would be worth pushing to mathlib I think along with a <code>finset</code> counterpart and decidable universals for both</p>

#### [ Chris Hughes (Jul 11 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129494880):
<p>Will do.</p>

#### [ Simon Hudon (Jul 11 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129494979):
<p>Thanks!</p>

#### [ Kevin Buzzard (Jul 11 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129500464):
<p>Thanks to both of you! I cannot believe how much trouble Ellen's dots and boxes project is causing me :-)</p>

#### [ Simon Hudon (Jul 11 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129500565):
<p>What's that project?</p>

#### [ Kevin Buzzard (Jul 11 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20decidability%20q/near/129500822):
<p>She's formalizing some of the theory of dots and boxes</p>


{% endraw %}
