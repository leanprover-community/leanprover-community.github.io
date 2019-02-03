---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/98209convergentsequencesarebounded.html
---

## Stream: [maths](index.html)
### Topic: [convergent sequences are bounded](98209convergentsequencesarebounded.html)

---


{% raw %}
#### [ Kevin Buzzard (Jan 18 2019 at 19:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156388362):
<p>How do I prove that a convergent sequence is bounded in Lean, in a way which is comprehensible to undergraduates? Say a_n tends to L. Setting epsilon=1 I know that for n&gt;=N I have |a_n|&lt;=|L|+1 by the triangle inequality. Now I need to let B be the max of |l|+1 and |a_n| for n&lt;N (and then |a_n|&lt;=B for all n). Mathematicians would say this was "trivial" so ideally I'd like to use as much automation as possible.</p>

#### [ Kevin Buzzard (Jan 18 2019 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156388915):
<p>[I'll just write the boilerplate now]</p>

#### [ Kevin Buzzard (Jan 18 2019 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156389440):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>
<span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">linarith</span>

<span class="n">noncomputable</span> <span class="n">theory</span>
<span class="n">local</span> <span class="n">attribute</span> <span class="o">[</span><span class="kn">instance</span><span class="o">,</span> <span class="n">priority</span> <span class="mi">0</span><span class="o">]</span> <span class="n">classical</span><span class="bp">.</span><span class="n">prop_decidable</span>

<span class="n">local</span> <span class="kn">notation</span> <span class="bp">`|`</span> <span class="n">x</span> <span class="bp">`|`</span> <span class="o">:=</span> <span class="n">abs</span> <span class="n">x</span>

<span class="kn">definition</span> <span class="n">is_limit</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">l</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="bp">∀</span> <span class="n">ε</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">,</span> <span class="bp">∃</span> <span class="n">N</span><span class="o">,</span> <span class="bp">∀</span> <span class="n">n</span> <span class="bp">≥</span> <span class="n">N</span><span class="o">,</span> <span class="bp">|</span> <span class="n">a</span> <span class="n">n</span> <span class="bp">-</span> <span class="n">l</span> <span class="bp">|</span> <span class="bp">&lt;</span> <span class="n">ε</span>

<span class="kn">definition</span> <span class="n">is_bounded</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="bp">∃</span> <span class="n">B</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">,</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="bp">|</span><span class="n">a</span> <span class="n">n</span><span class="bp">|</span> <span class="bp">≤</span> <span class="n">B</span>

<span class="kn">theorem</span> <span class="n">convergent_implies_bounded</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">l</span><span class="o">,</span> <span class="n">is_limit</span> <span class="n">a</span> <span class="n">l</span><span class="o">)</span> <span class="bp">→</span> <span class="n">is_bounded</span> <span class="n">a</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>I am a bit scared that my proof looks intimidating.</p>
<p>I was just watching Patrick proving that all epis were split in the category of sets and I thought it was going to be horrible but he just used this "choose" tactic and it was wonderful. I'm now wondering whether I can pull off something equally slick looking with this.</p>

#### [ Andrew Ashworth (Jan 18 2019 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156389873):
<p>A slick proof would be interesting. I tried doing a bit of basic analysis in Lean a long time ago, my proofs took me forever to write.</p>

#### [ Andrew Ashworth (Jan 18 2019 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156389882):
<p>Just proving Cauchy sequences were bounded led me to:</p>

#### [ Andrew Ashworth (Jan 18 2019 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156389887):
<div class="codehilite"><pre><span></span>-- Lemma 5.1.15 (Cauchy sequences are bounded).
example : ∃ r, ∀ i, abv (f i) &lt; r :=
let ⟨i, h⟩ := cauchy f zero_lt_one in
let R := (finset.range (i+1)).sum (λ j, abv (f j)) in
have h₁ : ∀ j ≤ i, abv (f j) ≤ R, from
  λ j ij, show (λ j, abv (f j)) j ≤ R, from
  finset.single_le_sum
    (λ k hk, is_absolute_value.abv_nonneg abv (f k))
    (by rwa [finset.mem_range, nat.lt_succ_iff]),
exists.intro (R + 1) (λ j, or.elim (lt_or_le j i)
  (λ h₂,
    let h₃ := le_of_lt h₂ in
    lt_of_le_of_lt (h₁ j h₃) (lt_add_one R))
  (λ ij,
    let h₃ := lt_of_le_of_lt (is_absolute_value.abv_add abv _ _)
      (add_lt_add_of_le_of_lt (h₁ _ (le_refl i)) (h j ij)) in
    by rw [add_sub, add_comm] at h₃; simpa using h₃))
</pre></div>

#### [ Kevin Buzzard (Jan 18 2019 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156389989):
<p><code>finset.max</code> spits out a term of type <code>option alpha</code>. How come the one time I _want_ it to spit out zero (on the basis that forall x in X, x &lt;= finset.max X would still be true when X is empty) it uses the option trick? :-/</p>

#### [ Kevin Buzzard (Jan 18 2019 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156390063):
<p>Yeah, that code looks really intimidating. Obviously Lean code can become intimidating after a certain level, but I was hoping I had not got to that point yet, I'm trying to show the undergraduates how to use this thing.</p>

#### [ Kevin Buzzard (Jan 18 2019 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156390214):
<p>How close can I get to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>X</mi><mo>:</mo><mo>=</mo><mi>max</mi><mo>{</mo><mi mathvariant="normal">∣</mi><msub><mi>a</mi><mi>n</mi></msub><mi mathvariant="normal">∣</mi><mspace width="0.16667em"></mspace><mi mathvariant="normal">∣</mi><mspace width="0.16667em"></mspace><mi>n</mi><mo>≤</mo><mi>N</mi><mo>}</mo></mrow><annotation encoding="application/x-tex">X:=\max\{|a_n|\,|\,n\leq N\}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.07847em;">X</span><span class="mrel">:</span><span class="mrel">=</span><span class="mop">max</span><span class="mopen">{</span><span class="mord mathrm">∣</span><span class="mord"><span class="mord mathit">a</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.151392em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mord mathrm">∣</span><span class="mord mathrm"><span class="mspace thinspace"></span><span class="mord mathrm">∣</span></span><span class="mord mathit"><span class="mspace thinspace"></span><span class="mord mathit">n</span></span><span class="mrel">≤</span><span class="mord mathit" style="margin-right:0.10903em;">N</span><span class="mclose">}</span></span></span></span> plus a theorem saying <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>n</mi><mo>≤</mo><mi>N</mi><mspace width="0.277778em"></mspace><mo>⟹</mo><mspace width="0.277778em"></mspace><mi mathvariant="normal">∣</mi><msub><mi>a</mi><mi>n</mi></msub><mi mathvariant="normal">∣</mi><mo>≤</mo><mi>X</mi></mrow><annotation encoding="application/x-tex">n\leq N\implies |a_n|\leq X</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit">n</span><span class="mrel">≤</span><span class="mord mathit" style="margin-right:0.10903em;">N</span><span class="mrel"><span class="mspace thickspace"></span><span class="mrel">⟹</span></span><span class="mord mathrm"><span class="mspace thickspace"></span><span class="mord mathrm">∣</span></span><span class="mord"><span class="mord mathit">a</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.151392em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mord mathrm">∣</span><span class="mrel">≤</span><span class="mord mathit" style="margin-right:0.07847em;">X</span></span></span></span>?</p>

#### [ Kevin Buzzard (Jan 18 2019 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156390280):
<p>I would like to avoid list.map list.range etc etc if possible.</p>

#### [ Mario Carneiro (Jan 18 2019 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156390309):
<p>you could use the real supremum of the set, that's pretty direct although you have less library assistance</p>

#### [ Kevin Buzzard (Jan 18 2019 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156390329):
<p>I now realise that I want to take the sup in the set of non-negative reals, which exists even for the empty set. Do we have this trick in Lean?</p>

#### [ Kevin Buzzard (Jan 18 2019 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156390350):
<p>eew but then I'd have to redefine <code>|x|</code> to take values in nnreal</p>

#### [ Mario Carneiro (Jan 18 2019 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156390416):
<p>just put 0 in the supremum</p>

#### [ Kevin Buzzard (Jan 18 2019 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156390427):
<p>Can I even make the set in a way that looks close to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>{</mo><mi mathvariant="normal">∣</mi><msub><mi>a</mi><mi>n</mi></msub><mi mathvariant="normal">∣</mi><mspace width="0.16667em"></mspace><mi mathvariant="normal">∣</mi><mspace width="0.16667em"></mspace><mi>n</mi><mo>≤</mo><mi>N</mi><mo>}</mo></mrow><annotation encoding="application/x-tex">\{|a_n|\,|\,n\leq N\}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mopen">{</span><span class="mord mathrm">∣</span><span class="mord"><span class="mord mathit">a</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.151392em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mord mathrm">∣</span><span class="mord mathrm"><span class="mspace thinspace"></span><span class="mord mathrm">∣</span></span><span class="mord mathit"><span class="mspace thinspace"></span><span class="mord mathit">n</span></span><span class="mrel">≤</span><span class="mord mathit" style="margin-right:0.10903em;">N</span><span class="mclose">}</span></span></span></span>?</p>

#### [ Mario Carneiro (Jan 18 2019 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156390448):
<p>not without using range</p>

#### [ Kevin Buzzard (Jan 18 2019 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156390457):
<p>I feel like my choice of notation might be about to bite me as well :-)</p>

#### [ Kevin Buzzard (Jan 18 2019 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156390467):
<p>Can I avoid using map?</p>

#### [ Kevin Buzzard (Jan 18 2019 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156390474):
<p>In python I can do quite fancy set comprehensions</p>

#### [ Kevin Buzzard (Jan 18 2019 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156390486):
<p>I've just realised that I don't even know if I can do them in Lean</p>

#### [ Mario Carneiro (Jan 18 2019 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156390529):
<p>lol, Simon will show you how to do fancy set comprehensions using do notation</p>

#### [ Andrew Ashworth (Jan 18 2019 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156390546):
<p>Are these lemmas actually trivial? Iirc, when I was following along these textbook proofs, each one required at least a paragraph of explanation</p>

#### [ Mario Carneiro (Jan 18 2019 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156390568):
<p>I agree actually, I've never seen this be a 0 line proof</p>

#### [ Kevin Buzzard (Jan 18 2019 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156390634):
<p>The fact that <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi mathvariant="normal">∣</mi><msub><mi>a</mi><mi>n</mi></msub><mi mathvariant="normal">∣</mi><mo>≤</mo><msub><mi>B</mi><mn>1</mn></msub></mrow><annotation encoding="application/x-tex">|a_n|\leq B_1</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathrm">∣</span><span class="mord"><span class="mord mathit">a</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.151392em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mord mathrm">∣</span><span class="mrel">≤</span><span class="mord"><span class="mord mathit" style="margin-right:0.05017em;">B</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:-0.05017em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span> for <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>n</mi><mo>≥</mo><mi>N</mi></mrow><annotation encoding="application/x-tex">n\geq N</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.8193em;vertical-align:-0.13597em;"></span><span class="base"><span class="mord mathit">n</span><span class="mrel">≥</span><span class="mord mathit" style="margin-right:0.10903em;">N</span></span></span></span> implies that <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>a</mi><mi>n</mi></msub></mrow><annotation encoding="application/x-tex">a_n</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.58056em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit">a</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.151392em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span> is bounded would be presented in a maths class like this: "let <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>B</mi><mn>2</mn></msub></mrow><annotation encoding="application/x-tex">B_2</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.83333em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.05017em;">B</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:-0.05017em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span> be the max of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi mathvariant="normal">∣</mi><msub><mi>a</mi><mi>n</mi></msub><mi mathvariant="normal">∣</mi></mrow><annotation encoding="application/x-tex">|a_n|</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathrm">∣</span><span class="mord"><span class="mord mathit">a</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.151392em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mord mathrm">∣</span></span></span></span> for <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>n</mi><mo>&lt;</mo><mi>N</mi></mrow><annotation encoding="application/x-tex">n&lt;N</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.72243em;vertical-align:-0.0391em;"></span><span class="base"><span class="mord mathit">n</span><span class="mrel">&lt;</span><span class="mord mathit" style="margin-right:0.10903em;">N</span></span></span></span>, then clearly <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>B</mi><mo>=</mo><mi>max</mi><mo>{</mo><msub><mi>B</mi><mn>1</mn></msub><mo separator="true">,</mo><msub><mi>B</mi><mn>2</mn></msub><mo>}</mo></mrow><annotation encoding="application/x-tex">B=\max\{B_1,B_2\}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.05017em;">B</span><span class="mrel">=</span><span class="mop">max</span><span class="mopen">{</span><span class="mord"><span class="mord mathit" style="margin-right:0.05017em;">B</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:-0.05017em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mpunct">,</span><span class="mord"><span class="mord mathit" style="margin-right:0.05017em;">B</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:-0.05017em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mclose">}</span></span></span></span> works"</p>

#### [ Mario Carneiro (Jan 18 2019 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156390649):
<p>I have written this exact proof in mathlib somewhere, maybe you can make something of it</p>

#### [ Kevin Buzzard (Jan 18 2019 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156390749):
<p>Undergraduate mathematicians can fill in the proofs that there are only finitely many <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>n</mi><mo>&lt;</mo><mi>N</mi></mrow><annotation encoding="application/x-tex">n&lt;N</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.72243em;vertical-align:-0.0391em;"></span><span class="base"><span class="mord mathit">n</span><span class="mrel">&lt;</span><span class="mord mathit" style="margin-right:0.10903em;">N</span></span></span></span>, that the max exists, and that <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi mathvariant="normal">∣</mi><msub><mi>a</mi><mi>n</mi></msub><mi mathvariant="normal">∣</mi><mo>≤</mo><mi>B</mi></mrow><annotation encoding="application/x-tex">|a_n|\leq B</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathrm">∣</span><span class="mord"><span class="mord mathit">a</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.151392em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mord mathrm">∣</span><span class="mrel">≤</span><span class="mord mathit" style="margin-right:0.05017em;">B</span></span></span></span> for all <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>n</mi></mrow><annotation encoding="application/x-tex">n</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">n</span></span></span></span>, and they would be deemed sufficiently trivial as to be not worth mentioning.</p>

#### [ Mario Carneiro (Jan 18 2019 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156390770):
<p><a href="https://github.com/leanprover/mathlib/blob/master/src/topology/metric_space/basic.lean#L531-L545" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/src/topology/metric_space/basic.lean#L531-L545">https://github.com/leanprover/mathlib/blob/master/src/topology/metric_space/basic.lean#L531-L545</a></p>

#### [ Kevin Buzzard (Jan 18 2019 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156390838):
<p>One reason it's hard for all this Lean stuff to catch up with normal maths is that normal maths goes at what Lean people would think of as breakneck speed, with all sorts of side goals never dealt with. They're dealt with using the <code>undergraduate</code> tactic.</p>

#### [ Mario Carneiro (Jan 18 2019 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156390860):
<p>It looks like I used <code>finset.range</code> and <code>finset.sup</code>, with <code>nndist</code> to stay in the nnreals</p>

#### [ Mario Carneiro (Jan 18 2019 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391073):
<p>I guess I would say that in lean we write things in a particular way to prove side goals by type correctness when possible</p>

#### [ Kevin Buzzard (Jan 18 2019 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391179):
<p>that's because you poor guys have to prove these goals :-) We just say they're obvious and hence not worth the time!</p>

#### [ Mario Carneiro (Jan 18 2019 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391196):
<p>when you say "the max of |a_n| for n&lt;N" there is a proof obligation that the set is bounded above, and has a max. When it's a finset this is obvious</p>

#### [ Kevin Buzzard (Jan 18 2019 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391238):
<p>You guys would probably point out that you need to prove it by induction or something :-)</p>

#### [ Mario Carneiro (Jan 18 2019 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391249):
<p>because if I said "the max of |a_n| for n&gt;N" it wouldn't be true</p>

#### [ Kevin Buzzard (Jan 18 2019 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391262):
<p>We don't even notice that we're using induction. We're even using recursion to define the max, I should think.</p>

#### [ Mario Carneiro (Jan 18 2019 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391286):
<p>that's one way to do it</p>

#### [ Kevin Buzzard (Jan 18 2019 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391346):
<p>There was a question on my M1F example sheet of the form "(i) Prove [blah] by induction (ii) now prove that I'm wasting your time and prove it directly without using induction"</p>

#### [ Kevin Buzzard (Jan 18 2019 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391363):
<p>and when I came to formalise it I realised that there was no way in hell that it was going to be proved without using induction :-)</p>

#### [ Andrew Ashworth (Jan 18 2019 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391367):
<p>Actually, I did have to prove that every finite sequence was bounded using induction, this was from Tao's UG analysis book "Analysis 1"...</p>

#### [ Mario Carneiro (Jan 18 2019 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391368):
<p>If you prove this theorem by induction you can avoid any contact with finite suprema</p>

#### [ Kevin Buzzard (Jan 18 2019 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391372):
<p>The question even had <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mn>3</mn><mi>n</mi></msup></mrow><annotation encoding="application/x-tex">3^n</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.664392em;"></span><span class="strut bottom" style="height:0.664392em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathrm">3</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span></span></span></span></span></span></span></span> in</p>

#### [ Kevin Buzzard (Jan 18 2019 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391375):
<p>which you can't even really define without induction</p>

#### [ Mario Carneiro (Jan 18 2019 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391408):
<p>well, exp(n*log 3) is not inductive</p>

#### [ Kevin Buzzard (Jan 18 2019 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391426):
<p>heh, it's not nat-valued either :-)</p>

#### [ Mario Carneiro (Jan 18 2019 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391443):
<p>of course it is, when the input is a natural number so is the output</p>

#### [ Kevin Buzzard (Jan 18 2019 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391449):
<p>and I'd better check with Chris that he didn't use nat.rec anywhere in his definition of exp</p>

#### [ Kevin Buzzard (Jan 18 2019 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391507):
<blockquote>
<p>of course it is, when the input is a natural number so is the output</p>
</blockquote>
<p>No! The output is a real number in the image of some coercion map, right? That's what you guys think anyway!</p>

#### [ Mario Carneiro (Jan 18 2019 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391510):
<p>if you think it's not that's DTT lying to you</p>

#### [ Kevin Buzzard (Jan 18 2019 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391516):
<p>:-)</p>

#### [ Kevin Buzzard (Jan 18 2019 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391575):
<p>I'm going to have to spend some time thinking about this. I don't think these problems are unsolvable. Patrick proved that if f was surjective then it had a one-sided inverse using some simple <code>choose</code> tactic and it looked really good. Last year I proved this without that tactic to my UGs and it looked really horrible.</p>

#### [ Kevin Buzzard (Jan 18 2019 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391590):
<p>Sometimes it's just a case of hiding all the true horror behind some simple interface.</p>

#### [ Mario Carneiro (Jan 18 2019 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391645):
<p>like <code>finset.sup</code>?</p>

#### [ Mario Carneiro (Jan 18 2019 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391657):
<p>Maybe all you need are nice notations for it</p>

#### [ Kevin Buzzard (Jan 18 2019 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391670):
<p>finset.sup wants some semilattice_bot thing, and the reals aren't one of those</p>

#### [ Kevin Buzzard (Jan 18 2019 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391707):
<p><code>lattice.semilattice_sup_bot</code></p>

#### [ Johan Commelin (Jan 18 2019 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391720):
<p>Can't we have <code>real.nnabs</code>?</p>

#### [ Kevin Buzzard (Jan 18 2019 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391736):
<p>Yes. But of course that will cause problems somewhere else.</p>

#### [ Mario Carneiro (Jan 18 2019 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391745):
<p><code>finset.max</code> I think doesn't care, but it returns an option</p>

#### [ Kevin Buzzard (Jan 18 2019 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391758):
<p>How come finset.max returns an option but 1 / 0 doesn't?</p>

#### [ Mario Carneiro (Jan 18 2019 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391828):
<p>because it's on a generic type, there is no zero element</p>

#### [ Kevin Buzzard (Jan 18 2019 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391829):
<p>Is there a variant which returns default alpha if there's no elements?</p>

#### [ Mario Carneiro (Jan 18 2019 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391835):
<p>but yes, you could do just that</p>

#### [ Mario Carneiro (Jan 18 2019 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391851):
<p>I think there was one written at some point, not sure where it's gone</p>

#### [ Kevin Buzzard (Jan 18 2019 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391860):
<p>Maybe I'll write a little library with variants of these things which work better for me.</p>

#### [ Kevin Buzzard (Jan 18 2019 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391867):
<p>This has been helpful, thanks.</p>

#### [ Mario Carneiro (Jan 18 2019 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156391873):
<p>you can define it as <code>(finset.max s).iget</code></p>

#### [ Kevin Buzzard (Jan 18 2019 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156392053):
<p>It looks intimidating. I think that for my current purposes I just want to write some of my own functions which I'll hide in an import.</p>

#### [ Mario Carneiro (Jan 18 2019 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156392294):
<p>that's what I mean you should do</p>

#### [ Kevin Buzzard (Jan 18 2019 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156392350):
<p>Oh I see. Of course. I have the weekend to do it, hopefully I will have it right by Tuesday.</p>

#### [ Kevin Buzzard (Jan 18 2019 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156394768):
<div class="codehilite"><pre><span></span><span class="n">local</span> <span class="kn">notation</span> <span class="bp">`</span><span class="o">[</span><span class="mi">0</span><span class="bp">..`</span> <span class="n">n</span> <span class="bp">`</span><span class="o">]</span><span class="bp">`</span> <span class="o">:=</span> <span class="n">finset</span><span class="bp">.</span><span class="n">range</span> <span class="n">n</span>

<span class="bp">#</span><span class="kn">check</span> <span class="o">[</span><span class="mi">0</span><span class="bp">..</span><span class="mi">3</span><span class="o">]</span> <span class="c1">-- finset ℕ</span>
</pre></div>


<p>I'm liking that.</p>

#### [ Johan Commelin (Jan 18 2019 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156394791):
<p>You need more backticks <span class="emoji emoji-1f603" title="smiley">:smiley:</span></p>

#### [ Patrick Massot (Jan 18 2019 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156395416):
<blockquote>
<p>I was just watching Patrick proving that all epis were split in the category of sets and I thought it was going to be horrible but he just used this "choose" tactic and it was wonderful. I'm now wondering whether I can pull off something equally slick looking with this.</p>
</blockquote>
<p>This tactic was written specifically for this talk</p>

#### [ Kevin Buzzard (Jan 18 2019 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156395499):
<p>I know Johan, but I was between tube stations when this became clear :-)</p>

#### [ Mario Carneiro (Jan 18 2019 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156395578):
<p>except that set is {0,1,2}</p>

#### [ Kevin Buzzard (Jan 18 2019 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156395581):
<p>Yes Patrick I remember you talking about it here. It seemed to work very well in practice.</p>

#### [ Kevin Buzzard (Jan 18 2019 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156395587):
<blockquote>
<p>except that set is {0,1,2}</p>
</blockquote>
<p><em>doh</em></p>

#### [ Patrick Massot (Jan 18 2019 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156395599):
<p>I mean I think it's useful to give talk and lectures where we want proofs to look nice. Because it pushes us to improve our tool</p>

#### [ Kevin Buzzard (Jan 18 2019 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156395618):
<div class="codehilite"><pre><span></span>local notation `[0..` n `]` := finset.range (n + 1)
</pre></div>

#### [ Mario Carneiro (Jan 18 2019 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156395711):
<p>yeah but now how are you going to denote {|a_n| : n &lt; N}?</p>

#### [ Patrick Massot (Jan 18 2019 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156395742):
<p>We need that new parser</p>

#### [ Mario Carneiro (Jan 18 2019 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/convergent%20sequences%20are%20bounded/near/156395766):
<p>omg we could have something incredible</p>


{% endraw %}
