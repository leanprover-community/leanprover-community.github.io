---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/94368FeedbackHeineBorelinprogress.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [Feedback (Heine Borel in progress)](https://leanprover-community.github.io/archive/113489newmembers/94368FeedbackHeineBorelinprogress.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Guillermo Barajas Ayuso (Sep 16 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134030478):
<p>Hi, I have uploaded some code in the link  <a href="https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/Topology/Heine-Borel%20(incomplete)" target="_blank" title="https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/Topology/Heine-Borel%20(incomplete)">https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/Topology/Heine-Borel%20(incomplete)</a> , I'll leave it here in case you want to give me some feedback. Thank you for your time! :-)</p>

#### [ Kevin Buzzard (Sep 16 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134045098):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">for_all_not_all</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">P</span> <span class="n">Q</span> <span class="n">R</span><span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">):</span>
<span class="o">(</span><span class="bp">∀</span> <span class="n">x</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">R</span> <span class="n">x</span><span class="o">),</span> <span class="bp">¬</span> <span class="o">(</span><span class="n">P</span> <span class="n">x</span> <span class="bp">∧</span> <span class="n">Q</span> <span class="n">x</span><span class="o">))</span> <span class="bp">↔</span>  <span class="bp">∀</span> <span class="n">x</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">R</span> <span class="n">x</span><span class="o">),</span> <span class="n">P</span> <span class="n">x</span> <span class="bp">→</span> <span class="bp">¬</span> <span class="n">Q</span> <span class="n">x</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">Hnand</span> <span class="n">x</span> <span class="n">Hx</span><span class="o">,</span> <span class="n">not_and</span><span class="bp">.</span><span class="n">mp</span> <span class="err">$</span> <span class="n">Hnand</span> <span class="n">x</span> <span class="n">Hx</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">Hton</span> <span class="n">x</span> <span class="n">Hx</span><span class="o">,</span> <span class="n">not_and</span><span class="bp">.</span><span class="n">mpr</span> <span class="err">$</span> <span class="n">Hton</span> <span class="n">x</span> <span class="n">Hx</span><span class="bp">⟩</span>
</pre></div>


<p>Mathlib would prefer that kind of style to your tactic proof. I always suspect that such results are either in mathlib already or easily deducible. Looking at the proof I feel like it's one of those ones which could be shortened with some magic use of function.comp like in <a href="https://xenaproject.wordpress.com/2018/05/19/function-composition/" target="_blank" title="https://xenaproject.wordpress.com/2018/05/19/function-composition/">https://xenaproject.wordpress.com/2018/05/19/function-composition/</a> . </p>
<p>Oh wait -- </p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">for_all_not_all</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">P</span> <span class="n">Q</span> <span class="n">R</span><span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">):</span>
<span class="o">(</span><span class="bp">∀</span> <span class="n">x</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">R</span> <span class="n">x</span><span class="o">),</span> <span class="bp">¬</span> <span class="o">(</span><span class="n">P</span> <span class="n">x</span> <span class="bp">∧</span> <span class="n">Q</span> <span class="n">x</span><span class="o">))</span> <span class="bp">↔</span>  <span class="bp">∀</span> <span class="n">x</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">R</span> <span class="n">x</span><span class="o">),</span> <span class="n">P</span> <span class="n">x</span> <span class="bp">→</span> <span class="bp">¬</span> <span class="n">Q</span> <span class="n">x</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">not_and</span><span class="o">]</span>
</pre></div>


<div class="codehilite"><pre><span></span>
</pre></div>

#### [ Kevin Buzzard (Sep 16 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134045185):
<p>The simp proof -- the proof takes 50% longer to process but the parser takes far less time parsing :-) End result is that both versions run in about the same time.</p>

#### [ Kevin Buzzard (Sep 16 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134045233):
<p>I have an error at line 431 by the way, and there are 6 sorrys. Do you need help filling them in?</p>

#### [ Kevin Buzzard (Sep 16 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134046514):
<p>Re the argument on line 431: there is already <code>nat.lt_pow_self</code>. </p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">le_pow</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">≤</span> <span class="o">(</span><span class="mi">2</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="err">^</span> <span class="n">n</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">show</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">≤</span> <span class="o">((</span><span class="mi">2</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="err">^</span> <span class="n">n</span><span class="o">,</span>
  <span class="n">rw</span> <span class="err">←</span><span class="n">nat</span><span class="bp">.</span><span class="n">cast_pow</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cast_le</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">le_of_lt</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">lt_pow_self</span> <span class="o">(</span><span class="n">dec_trivial</span><span class="o">)</span> <span class="n">n</span><span class="o">),</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Sep 16 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134046673):
<p><code>notation ⟦a,b] := closed_interval a b </code></p>
<p>This is a hilarious idea. Does it work? Re-using notation which is already used is a dangerous game, but given that as far as I know in Lean every use of <code>]</code> in notation comes with an <code>[</code> too, so avoiding the <code>[</code> in this case gives you better leeway.</p>

#### [ Kevin Buzzard (Sep 16 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134048119):
<p><code>theorem le_ε_to_le (Hle_ε : ∀ ε &gt; 0, a ≤ b + ε) : a ≤ b := sorry</code> These things are really annoying if they're not there already. <span class="user-mention" data-user-id="110064">@Kenny Lau</span> how is one supposed to prove stuff like this?</p>

#### [ Kevin Buzzard (Sep 16 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134048714):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">le_ε_to_le</span> <span class="o">(</span><span class="n">Hle_ε</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">ε</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">,</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">b</span> <span class="bp">+</span> <span class="n">ε</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">b</span> <span class="o">:=</span>
<span class="n">le_of_not_gt</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">H</span><span class="o">,</span> <span class="k">begin</span>
  <span class="k">have</span> <span class="n">H2</span> <span class="o">:=</span> <span class="n">Hle_ε</span> <span class="o">((</span><span class="n">a</span> <span class="bp">-</span> <span class="n">b</span><span class="o">)</span> <span class="bp">/</span> <span class="mi">2</span><span class="o">)</span> <span class="bp">_</span><span class="o">,</span>
    <span class="n">revert</span> <span class="n">H2</span><span class="o">,</span> <span class="c1">-- because it makes the rewriting easier</span>
    <span class="n">rw</span> <span class="o">[</span><span class="err">←</span><span class="o">(</span><span class="n">mul_le_mul_right</span> <span class="o">(</span><span class="k">show</span> <span class="o">(</span><span class="mi">2</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">,</span> <span class="k">by</span> <span class="n">norm_num</span><span class="o">)),</span><span class="n">add_mul</span><span class="o">,</span>
    <span class="n">div_mul_cancel</span> <span class="bp">_</span> <span class="o">(</span><span class="k">show</span> <span class="o">(</span><span class="mi">2</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">≠</span> <span class="mi">0</span><span class="o">,</span> <span class="k">by</span> <span class="n">norm_num</span><span class="o">),</span>
   <span class="o">(</span><span class="k">show</span> <span class="n">b</span> <span class="bp">*</span> <span class="mi">2</span> <span class="bp">+</span> <span class="o">(</span><span class="n">a</span> <span class="bp">-</span> <span class="n">b</span><span class="o">)</span> <span class="bp">=</span> <span class="n">a</span> <span class="bp">+</span> <span class="n">b</span><span class="o">,</span> <span class="k">by</span> <span class="n">ring</span><span class="o">),</span>
    <span class="n">mul_two</span><span class="o">,</span><span class="n">add_le_add_iff_left</span><span class="o">],</span>
    <span class="n">exact</span> <span class="n">not_le_of_gt</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">div_pos</span> <span class="bp">_</span> <span class="o">(</span><span class="k">show</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">&lt;</span> <span class="mi">2</span><span class="o">,</span> <span class="k">by</span> <span class="n">norm_num</span><span class="o">),</span>
  <span class="n">exact</span> <span class="n">sub_pos_of_lt</span> <span class="n">H</span>
<span class="kn">end</span>
</pre></div>


<p>This time last year there was no <code>norm_num</code> and no <code>ring</code> -- imagine how hard it was doing M1F example sheets!</p>

#### [ Kenny Lau (Sep 16 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134048768):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">le_ε_to_le</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">linear_ordered_field</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span>
  <span class="o">(</span><span class="n">Hle_ε</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">ε</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">,</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">b</span> <span class="bp">+</span> <span class="n">ε</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">b</span> <span class="o">:=</span>
<span class="n">le_of_not_lt</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">H</span><span class="o">,</span> <span class="n">not_lt_of_le</span> <span class="o">(</span><span class="n">Hle_ε</span> <span class="o">((</span><span class="n">a</span><span class="bp">-</span><span class="n">b</span><span class="o">)</span><span class="bp">/</span><span class="mi">2</span><span class="o">)</span> <span class="o">(</span><span class="n">half_pos</span> <span class="err">$</span> <span class="n">sub_pos_of_lt</span> <span class="n">H</span><span class="o">))</span> <span class="err">$</span>
<span class="k">calc</span>  <span class="n">b</span><span class="bp">+</span><span class="o">(</span><span class="n">a</span><span class="bp">-</span><span class="n">b</span><span class="o">)</span><span class="bp">/</span><span class="mi">2</span>
    <span class="bp">&lt;</span> <span class="n">b</span><span class="bp">+</span><span class="o">(</span><span class="n">a</span><span class="bp">-</span><span class="n">b</span><span class="o">)</span> <span class="o">:</span> <span class="n">add_lt_add_left</span> <span class="o">(</span><span class="n">half_lt_self</span> <span class="o">(</span><span class="n">sub_pos_of_lt</span> <span class="n">H</span><span class="o">))</span> <span class="bp">_</span>
<span class="bp">...</span> <span class="bp">=</span> <span class="n">a</span> <span class="o">:</span> <span class="n">add_sub_cancel&#39;_right</span> <span class="n">b</span> <span class="n">a</span>
</pre></div>

#### [ Kevin Buzzard (Sep 16 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134048808):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">between_shorter</span> <span class="o">(</span><span class="n">H1</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">≤</span> <span class="n">c</span><span class="o">)</span> <span class="o">(</span><span class="n">H2</span> <span class="o">:</span> <span class="n">c</span> <span class="bp">≤</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">H3</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">≤</span> <span class="n">d</span><span class="o">)</span> <span class="o">(</span><span class="n">H4</span> <span class="o">:</span> <span class="n">d</span> <span class="bp">≤</span> <span class="n">a</span><span class="o">)</span> <span class="o">:</span>
<span class="n">abs</span> <span class="o">(</span><span class="n">c</span> <span class="bp">-</span> <span class="n">d</span><span class="o">)</span> <span class="bp">≤</span> <span class="n">abs</span> <span class="o">(</span><span class="n">a</span> <span class="bp">-</span> <span class="n">b</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">rw</span> <span class="n">abs_of_nonneg</span> <span class="o">(</span><span class="n">sub_nonneg_of_le</span> <span class="err">$</span> <span class="n">le_trans</span> <span class="n">H1</span> <span class="n">H2</span><span class="o">),</span>
  <span class="n">rw</span> <span class="n">abs_le</span><span class="o">,</span> <span class="n">split</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">neg_sub</span><span class="o">,</span>
    <span class="n">exact</span> <span class="bp">_</span><span class="n">root_</span><span class="bp">.</span><span class="n">sub_le_sub</span> <span class="n">H1</span> <span class="n">H4</span><span class="o">,</span>
    <span class="n">exact</span> <span class="bp">_</span><span class="n">root_</span><span class="bp">.</span><span class="n">sub_le_sub</span> <span class="n">H2</span> <span class="n">H3</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p>This one wasn't too bad -- proof felt natural.</p>

#### [ Kenny Lau (Sep 16 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134049053):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">between_shorter</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">decidable_linear_ordered_comm_group</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="n">d</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span>
  <span class="o">(</span><span class="n">H1</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">≤</span> <span class="n">c</span><span class="o">)</span> <span class="o">(</span><span class="n">H2</span> <span class="o">:</span> <span class="n">c</span> <span class="bp">≤</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">H3</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">≤</span> <span class="n">d</span><span class="o">)</span> <span class="o">(</span><span class="n">H4</span> <span class="o">:</span> <span class="n">d</span> <span class="bp">≤</span> <span class="n">a</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">abs</span> <span class="o">(</span><span class="n">c</span> <span class="bp">-</span> <span class="n">d</span><span class="o">)</span> <span class="bp">≤</span> <span class="n">abs</span> <span class="o">(</span><span class="n">a</span> <span class="bp">-</span> <span class="n">b</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">calc</span>  <span class="n">abs</span> <span class="o">(</span><span class="n">c</span> <span class="bp">-</span> <span class="n">d</span><span class="o">)</span>
    <span class="bp">≤</span> <span class="n">a</span> <span class="bp">-</span> <span class="n">b</span> <span class="o">:</span> <span class="n">abs_sub_le_iff</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">⟨</span><span class="n">sub_le_sub</span> <span class="n">H2</span> <span class="n">H3</span><span class="o">,</span> <span class="n">sub_le_sub</span> <span class="n">H4</span> <span class="n">H1</span><span class="bp">⟩</span>
<span class="bp">...</span> <span class="bp">=</span> <span class="n">abs</span> <span class="o">(</span><span class="n">a</span> <span class="bp">-</span> <span class="n">b</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">abs_of_nonneg</span> <span class="err">$</span> <span class="n">sub_nonneg_of_le</span> <span class="err">$</span> <span class="n">le_trans</span> <span class="n">H1</span> <span class="n">H2</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span>
</pre></div>

#### [ Kevin Buzzard (Sep 16 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134049054):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">half_le_self</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">≤</span> <span class="n">a</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">/</span> <span class="mi">2</span> <span class="bp">≤</span> <span class="n">a</span> <span class="o">:=</span> <span class="k">begin</span>
  <span class="n">rw</span> <span class="n">div_le_iff</span> <span class="o">(</span><span class="k">show</span> <span class="o">(</span><span class="mi">2</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">,</span> <span class="k">by</span> <span class="n">norm_num</span><span class="o">),</span>
  <span class="n">rw</span> <span class="n">mul_two</span><span class="o">,</span>
  <span class="n">rwa</span> <span class="n">le_add_iff_nonneg_left</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Sep 16 2018 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134049259):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">half_le_self</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">linear_ordered_field</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span>
  <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">≤</span> <span class="n">a</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">/</span> <span class="mi">2</span> <span class="bp">≤</span> <span class="n">a</span> <span class="o">:=</span>
<span class="n">div_le_of_le_mul</span> <span class="n">two_pos</span> <span class="err">$</span> <span class="o">(</span><span class="n">two_mul</span> <span class="n">a</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span> <span class="bp">▸</span> <span class="n">le_add_of_nonneg_left</span> <span class="n">H</span>
</pre></div>

#### [ Kevin Buzzard (Sep 16 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134049371):
<p>Should there be training or exercises or something for people who need stuff like this?</p>

#### [ Rob Lewis (Sep 16 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134050573):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">linarith</span>

<span class="kn">lemma</span> <span class="n">half_le_self</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">linear_ordered_field</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span>
  <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">≤</span> <span class="n">a</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">/</span> <span class="mi">2</span> <span class="bp">≤</span> <span class="n">a</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">linarith</span>

<span class="kn">theorem</span> <span class="n">between_shorter</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">decidable_linear_ordered_comm_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="n">d</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span>
  <span class="o">(</span><span class="n">H1</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">≤</span> <span class="n">c</span><span class="o">)</span> <span class="o">(</span><span class="n">H2</span> <span class="o">:</span> <span class="n">c</span> <span class="bp">≤</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">H3</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">≤</span> <span class="n">d</span><span class="o">)</span> <span class="o">(</span><span class="n">H4</span> <span class="o">:</span> <span class="n">d</span> <span class="bp">≤</span> <span class="n">a</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">abs</span> <span class="o">(</span><span class="n">c</span> <span class="bp">-</span> <span class="n">d</span><span class="o">)</span> <span class="bp">≤</span> <span class="n">abs</span> <span class="o">(</span><span class="n">a</span> <span class="bp">-</span> <span class="n">b</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">unfold</span> <span class="n">abs</span> <span class="n">max</span><span class="bp">;</span> <span class="n">split_ifs</span><span class="bp">;</span> <span class="n">linarith</span>
</pre></div>

#### [ Kevin Buzzard (Sep 16 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134050865):
<p>...or maybe even a tactic!</p>

#### [ Scott Morrison (Sep 16 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134050868):
<p>Next we make a wrapper for linarith that unfolds stuff that is secretly arithmetic. :-)</p>

#### [ Kevin Buzzard (Sep 16 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134051134):
<blockquote>
<div class="codehilite"><pre><span></span>    <span class="bp">&lt;</span> <span class="n">b</span><span class="bp">+</span><span class="o">(</span><span class="n">a</span><span class="bp">-</span><span class="n">b</span><span class="o">)</span> <span class="o">:</span> <span class="o">[</span><span class="n">blah</span><span class="o">]</span>
<span class="bp">...</span> <span class="bp">=</span> <span class="n">a</span> <span class="o">:</span> <span class="n">add_sub_cancel&#39;_right</span> <span class="n">b</span> <span class="n">a</span>
</pre></div>


</blockquote>
<p>Kenny -- you misspelt "by ring". </p>
<p>Why should mathematican end users have to know that the triviality <code>b + (a - b) = a</code> is called <code>add_sub_cancel'_right</code>? Surely we should just be able to write something which generates this proof for us, and then internally replaces what we wrote with this add_sub_cancel' nonsense?  I'm assuming that using <code>ring</code> to do this is not recommended because it might take about 10 times as long. It's all well and good people writing clever tactics which solve all goals of this nature, but then we end up in this situation where people are encouraged not to use them and instead get an encyclopedic knowledge of all this <code>add_sub_cancel'_right</code> nonsense, or learn how to look it up. I guess what I'm asking for is a tactic which does <code>by ring</code> but only takes a long time the first time -- like Scott's <code>tidy</code> trick. Can this be done in other cases somehow?</p>

#### [ Kevin Buzzard (Sep 16 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134051186):
<p><span class="user-mention" data-user-id="120690">@Guillermo Barajas Ayuso</span> -- <code>linarith</code> is a brand new tactic which Rob wrote. You might find it useful in other situations.</p>

#### [ Kenny Lau (Sep 16 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134051860):
<p><span class="user-mention" data-user-id="110596">@Rob Lewis</span> re <code>between_shorter</code>, my version works for objects without multiplication</p>

#### [ Rob Lewis (Sep 16 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134051971):
<blockquote>
<p>Can this be done in other cases somehow?</p>
</blockquote>
<p>It can in principle. But things like <code>ring</code> often don't try to produce short or pretty output, because it's way harder to write something that does that and works generally. And the output will probably still look messy on anything more complicated than that basic example.</p>

#### [ Rob Lewis (Sep 16 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134052060):
<p>I wouldn't expect <code>ring</code> to be unreasonably slow for examples like that, either.</p>

#### [ Scott Morrison (Sep 16 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134052895):
<p>Hi <span class="user-mention" data-user-id="110596">@Rob Lewis</span>, in the interest in making <code>linarith</code> even easier to use, what would you think of having it automatically try <code>exfalso</code> if the goal doesn't look like linear arithmetic?</p>

#### [ Scott Morrison (Sep 16 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134052931):
<p>It's of course possible to achieve this by: <code>linarith &lt;|&gt; (exfalso &gt;&gt; linarith)</code>, but I worry that this is inefficient.</p>

#### [ Scott Morrison (Sep 16 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134052956):
<p>(Actually maybe it isn't --- if the goal is something else, linarith I guess fails before doing any work already...)</p>

#### [ Rob Lewis (Sep 16 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134053111):
<p>That's completely reasonable. I actually thought it did that already, but apparently I added a check for a <code>false</code> goal.</p>

#### [ Rob Lewis (Sep 16 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134053146):
<p>If there are no inequality hypotheses, it'll fail immediately. If there are hypotheses it can work with, it will try, but failure is a lot quicker than success.</p>

#### [ Rob Lewis (Sep 16 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134053210):
<p>I'll add a config option for trying to prove arbitrary goals by <code>exfalso</code>.</p>

#### [ Keeley Hoek (Sep 16 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134054291):
<p>This sort of follows-up what Kevin was saying before: it seems to me that it'd be really great if Lean had a facility for tactics to opt-in to cache what they did on invocation, not just in the interactive lean session (memoizing there), but statically in a file in the repository.</p>

#### [ Keeley Hoek (Sep 16 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134054292):
<p>The (my?) dream is that mathlib (or just mathematics) could be filled with tactic proofs which call shiny-new maybe-expensive tactics which do all of your dirty-work for you in one line (e.g <code>by super_ring</code>), without any detrimental performance impact; if you change the first line of a file, the expensive tactic proofs in the file below instantly recompile; and if you change the statement of a lemma the cached proof will just silently fail to typecheck and the tactic proof will be re-run. mathlib can be distributed with these cache-files, or they could just be built the first time mathlib is built, and everyone is happy.</p>

#### [ Keeley Hoek (Sep 16 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134054295):
<p>Instead it seems like in many places people have to steer clear of the "big guns", or at least only use them to get a term/tactic-mode proof which they will replace them with. To me, this seems just like a manual way of doing the same sort of static caching, but the tools which helped generate your easy proof (e.g. <code>ring</code> → <code>add_sub_cancel'_right</code>) are lost forever (and don't auto-fix your proof when you e.g. tinker with your lemma).</p>

#### [ Patrick Massot (Sep 16 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134058680):
<blockquote>
<blockquote>
<div class="codehilite"><pre><span></span>    <span class="bp">&lt;</span> <span class="n">b</span><span class="bp">+</span><span class="o">(</span><span class="n">a</span><span class="bp">-</span><span class="n">b</span><span class="o">)</span> <span class="o">:</span> <span class="o">[</span><span class="n">blah</span><span class="o">]</span>
<span class="bp">...</span> <span class="bp">=</span> <span class="n">a</span> <span class="o">:</span> <span class="n">add_sub_cancel&#39;_right</span> <span class="n">b</span> <span class="n">a</span>
</pre></div>


</blockquote>
<p>Kenny -- you misspelt "by ring". </p>
</blockquote>
<p>Or "by abel"</p>

#### [ Kevin Buzzard (Sep 17 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134104742):
<p>Or even <code>by simp</code>. Grr. What is the point of this <code>abel</code> tactic? I still haven't found an example which <code>simp</code> can't do.</p>

#### [ Patrick Massot (Sep 17 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Feedback%20%28Heine%20Borel%20in%20progress%29/near/134106299):
<p>Hopefully <code>abel</code> is a step towards the <code>module</code> tactic which should be more useful</p>


{% endraw %}
