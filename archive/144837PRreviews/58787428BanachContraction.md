---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/58787428BanachContraction.html
---

## Stream: [PR reviews](https://leanprover-community.github.io/archive/144837PRreviews/index.html)
### Topic: [#428 Banach Contraction](https://leanprover-community.github.io/archive/144837PRreviews/58787428BanachContraction.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Dec 11 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/151452941):
<p>PR by <span class="user-mention" data-user-id="120559">@Rohan Mitta</span>.</p>

#### [ Rohan Mitta (Dec 13 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/151607136):
<p>I edited this PR based on feedback from Patrick, I think it's ready now but any other feedback would be appreciated!</p>

#### [ Patrick Massot (Dec 13 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/151618862):
<p>I think there is still overlap with existing stuff, eg <a href="https://github.com/leanprover/mathlib/blob/master/data/real/cau_seq_filter.lean#L164" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/data/real/cau_seq_filter.lean#L164">https://github.com/leanprover/mathlib/blob/master/data/real/cau_seq_filter.lean#L164</a></p>

#### [ Patrick Massot (Dec 13 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/151618877):
<p>And I'm sure you can extract lemmas from the Banach contraction proof</p>

#### [ Alistair Tucker (Dec 15 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/151834889):
<p>(deleted)</p>

#### [ Alistair Tucker (Dec 15 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/151834942):
<p>In fact I don't think I found a use for anything in cau_seq_filter.lean<br>
   (Edit : I see this was because I didn't go beyond the first half of metric_sequences.lean)</p>

#### [ Alistair Tucker (Dec 15 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/151835097):
<p>We've got <code>sequentially_complete.tendsto_div</code>used in metric_sequences.lean, in</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">lim_sequence_of_mem_closure</span> <span class="o">{</span><span class="n">Y</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">closure</span> <span class="n">Y</span><span class="o">)</span> <span class="o">:</span>
<span class="bp">∃</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">H1</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">f</span> <span class="n">n</span> <span class="err">∈</span> <span class="n">Y</span><span class="o">),</span> <span class="n">filter</span><span class="bp">.</span><span class="n">tendsto</span> <span class="n">f</span> <span class="n">at_top</span> <span class="o">(</span><span class="n">nhds</span> <span class="n">a</span><span class="o">)</span>
</pre></div>


<p>But nothing from metric_sequences.lean is actually used in banach_contraction.lean any more</p>

#### [ Alistair Tucker (Dec 17 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152036009):
<p>Isn't this basically constructive? It's a shame I that we have to mark as noncomputable the function to return the fixed point because the definition of completeness uses an exists.</p>

#### [ Patrick Massot (Dec 17 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152036085):
<p>It looks very non-computable to me</p>

#### [ Patrick Massot (Dec 17 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152036140):
<p>This is what we keep repeating to our students: compactness and completeness give you elements for free! Constructive maths don't give anything for free, they want you to suffer.</p>

#### [ Alistair Tucker (Dec 17 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152036161):
<p>Why is that? If I have a cauchy sequence of, say, reals then I have constructed a real</p>

#### [ Patrick Massot (Dec 17 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152036192):
<p>This is a very special case, because you constructed real like that</p>

#### [ Patrick Massot (Dec 17 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152036251):
<p>And it's breaking an abstraction barrier</p>

#### [ Patrick Massot (Dec 17 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152036288):
<p>We want to use this theorem for many complete spaces which are not constructed as completions</p>

#### [ Alistair Tucker (Dec 17 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152036327):
<p>OK. Can you give me an example?</p>

#### [ Patrick Massot (Dec 17 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152036342):
<p>Differentiable functions for instance</p>

#### [ Patrick Massot (Dec 17 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152036376):
<p>Say you want to prove Cauchy-Lipschitz theorem about existence and uniqueness of solutions to nice ordinary differential equations</p>

#### [ Alistair Tucker (Dec 17 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152044239):
<p>I think @Rohan Mitta will probably want to kill me because I put Mario off reviewing this <span class="emoji emoji-1f615" title="oh no">:oh_no:</span></p>

#### [ Alistair Tucker (Dec 17 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152044258):
<p>I panicked</p>

#### [ Mario Carneiro (Dec 17 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152045032):
<p>if you want some more tips: the style of tactic indentation isn't quite standard, there are some funny names like <code>Banach's_fixed_point</code> and generally nonconforming names (they should be more or less strictly based on reading the symbols), <code>fixed_point_of_iteration_limit'</code> and <code>fixed_point_of_iteration_limit</code> are the same, the main theorem is far too long (I think it can be shorter, and this should also be lemma'd if not)</p>

#### [ Patrick Massot (Dec 17 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152045161):
<p>I wrote that last remark many times, so I guess they'll need more help there. But I really want to finish completions (before the end of July 2018...)</p>

#### [ Alistair Tucker (Dec 17 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152045274):
<p>We do have a much shorter one here <a href="https://github.com/agjftucker/mathlib/blob/Banach/analysis/topology/banach_contraction.lean#L253" target="_blank" title="https://github.com/agjftucker/mathlib/blob/Banach/analysis/topology/banach_contraction.lean#L253">https://github.com/agjftucker/mathlib/blob/Banach/analysis/topology/banach_contraction.lean#L253</a></p>

#### [ Patrick Massot (Dec 17 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152045404):
<p>That's much better!</p>

#### [ Patrick Massot (Dec 17 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152045488):
<p>What's the difference with the next statement?</p>

#### [ Patrick Massot (Dec 17 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152045558):
<p>Why can't you get rid of <code>0 ≤ K →</code>?</p>

#### [ Alistair Tucker (Dec 17 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152045561):
<p>The statement is much the same but the method is different</p>

#### [ Alistair Tucker (Dec 17 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152045676):
<p>I think because otherwise you need inhabiteds ?</p>

#### [ Alistair Tucker (Dec 17 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152045720):
<p>In fact you need at least two distinct points</p>

#### [ Mario Carneiro (Dec 17 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152045730):
<p>the space is already inhabited</p>

#### [ Mario Carneiro (Dec 17 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152045736):
<p>why two points?</p>

#### [ Patrick Massot (Dec 17 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152045796):
<p>Oh I see</p>

#### [ Patrick Massot (Dec 17 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152045799):
<p>crazy computers...</p>

#### [ Alistair Tucker (Dec 17 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152045811):
<p>To prove that K &gt;=0 I think you need two</p>

#### [ Mario Carneiro (Dec 17 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152045947):
<p>yeah, but if the space has only one point then it's a fixed point :P</p>

#### [ Patrick Massot (Dec 17 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152045958):
<p>Yeah!</p>

#### [ Patrick Massot (Dec 17 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152045970):
<p>Let's begin with this very natural case disjunction!</p>

#### [ Mario Carneiro (Dec 17 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152045977):
<p>lol</p>

#### [ Mario Carneiro (Dec 17 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152045995):
<p>I would suggest putting <code>K &gt;= 0</code> in the definition of lipschitz</p>

#### [ Alistair Tucker (Dec 17 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152046020):
<p>OK I can change that in the main theorem :) But I might still need some <code>0 \leq K</code> in the preceding lemmas</p>

#### [ Sebastien Gouezel (Dec 17 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152054653):
<blockquote>
<p>I would suggest putting <code>K &gt;= 0</code> in the definition of lipschitz</p>
</blockquote>
<p>Yes, definitely -- I played a lot with this in Isabelle, and it turned out to be much more manageable once I enforced <code>K &gt;= 0</code>.</p>

#### [ Alistair Tucker (Dec 17 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152054798):
<p>will do. Thanks</p>

#### [ Kevin Buzzard (Dec 17 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23428%20Banach%20Contraction/near/152056937):
<blockquote>
<p>Let's begin with this very natural case disjunction!</p>
</blockquote>
<p>That's pretty much how the proof I was taught as an undergraduate began!</p>


{% endraw %}
