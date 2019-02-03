---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/17341Hausdorffcompletion.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [Hausdorff completion](https://leanprover-community.github.io/archive/116395maths/17341Hausdorffcompletion.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Jul 11 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff%20completion/near/129461026):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> around <a href="https://github.com/leanprover/mathlib/blob/master/analysis/topology/uniform_space.lean#L1102" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/analysis/topology/uniform_space.lean#L1102">https://github.com/leanprover/mathlib/blob/master/analysis/topology/uniform_space.lean#L1102</a>, is there any reason why you didn't push to the Hausdorff completion? Is the idea that users should easily combine stuff in this section with the <a href="https://github.com/leanprover/mathlib/blob/master/analysis/topology/uniform_space.lean#L928" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/analysis/topology/uniform_space.lean#L928">https://github.com/leanprover/mathlib/blob/master/analysis/topology/uniform_space.lean#L928</a> section? Or did you intend to continue this?</p>

#### [ Johannes Hölzl (Jul 11 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff%20completion/near/129462922):
<p>The idea was to be compositional. So I wanted to split the separation quotient from the Cauchy construction. I'm not exactly sure what Hausdorff completion is, but I guess you can use the composition <code>hausdorff_completion α := quotient (separation_setoid (Cauchy α))</code>. Or do I miss something?</p>

#### [ Patrick Massot (Jul 11 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff%20completion/near/129463129):
<p>Yes, this is what I had in mind.</p>

#### [ Patrick Massot (Jul 11 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff%20completion/near/129463135):
<p>Or maybe compose in the opposite order, I would need to think whether it's the same</p>

#### [ Patrick Massot (Jul 11 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff%20completion/near/129463277):
<p>Bourbaki does it a bit differently. They consider the space of <em>minimal</em> Cauchy filters.. It seems this is always Hausdorff</p>

#### [ Patrick Massot (Jul 11 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff%20completion/near/129464037):
<p>I found some text claiming that your definition of <code>hausdorff_completion α</code> gives the same result as the minimal Cauchy filter definition. Anyway, the real test is to try to prove the universal property for this definition (every uniformly continuous map from <code>α</code> into a complete Hausdorff space factors through the, not necessarily injective, "inclusion" of <code>α</code> in <code>hausdorff_completion α</code>)</p>

#### [ Johannes Hölzl (Jul 11 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff%20completion/near/129480597):
<p>I didn't choose to use minimal Cauchy filters, as I thought the splitting into (all) Cauchy filters and quotient makes the formalization easier. And the separation quotient will be used anyway. The universal property is proved for each dense embedding from a closed set on a complete space (see section <code>uniform_extension</code>)</p>

#### [ Patrick Massot (Jul 11 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff%20completion/near/129481701):
<p>I understand. I have a stub at  <a href="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean" target="_blank" title="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean">https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean</a>  that I'll try to complete. I think I understand what's already in mathlib and what remains to be done. Then next step would be to unsorry the end of <a href="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/topological_structures.lean" target="_blank" title="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/topological_structures.lean">https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/topological_structures.lean</a></p>

#### [ Johannes Hölzl (Jul 11 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff%20completion/near/129495769):
<p>All this was already done for the real numbers, if you want I can look it up in the mathlib history</p>

#### [ Patrick Massot (Jul 11 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff%20completion/near/129495855):
<p>Any help is welcome</p>

#### [ Patrick Massot (Jul 11 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff%20completion/near/129495862):
<p>But there is no separation issue in the real case</p>

#### [ Patrick Massot (Jul 11 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff%20completion/near/129496013):
<p>By the way, is <a href="https://github.com/leanprover/mathlib/blob/master/analysis/topology/uniform_space.lean#L18" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/analysis/topology/uniform_space.lean#L18">https://github.com/leanprover/mathlib/blob/master/analysis/topology/uniform_space.lean#L18</a> still true?</p>

#### [ Johannes Hölzl (Jul 11 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff%20completion/near/129496855):
<p>No, its not true anymore.<br>
As far as I remember, there is a separation issue for the real case: I used the separation/Cauchy construction: <a href="https://github.com/leanprover/mathlib/blob/7fd7ea8c323c5f622bda6bc8de6dd352cc2732a8/analysis/real.lean#L384" target="_blank" title="https://github.com/leanprover/mathlib/blob/7fd7ea8c323c5f622bda6bc8de6dd352cc2732a8/analysis/real.lean#L384">https://github.com/leanprover/mathlib/blob/7fd7ea8c323c5f622bda6bc8de6dd352cc2732a8/analysis/real.lean#L384</a></p>

#### [ Patrick Massot (Jul 11 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff%20completion/near/129497515):
<p>Thanks. This will probably be very useful when I'll move to completions of groups and rings. But I don't see anything that looks like the universal property of Hausdorff  completions</p>

#### [ Patrick Massot (Jul 11 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff%20completion/near/129497598):
<p>I'm really curious to know why the separation quotient was necessary. I have no intuition about filters, but to me rationals numbers seems separated enough.</p>

#### [ Johannes Hölzl (Jul 11 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff%20completion/near/129498685):
<p>But the _Cauchy filters over the rationals_ are not separated. In this regard is no difference between Cauchy sequences and filters. One also needs to put a quotient over the Cauchy sequences when constructing the reals via Cauchy sequences.</p>

#### [ Patrick Massot (Jul 11 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff%20completion/near/129499261):
<p>Indeed</p>

#### [ Patrick Massot (Jul 15 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff%20completion/near/129696906):
<p>Now I know what I meant. The fundamental difference is that the map <code>of_rat  ℚ → ℝ</code> is injective. Then you proved it's a uniform embedding, and used lemmas about uniform embeddings everywhere. This is no longer true in my context.</p>

#### [ Johannes Hölzl (Jul 15 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff%20completion/near/129699781):
<p>So instead of injective your function respects the separability relation?</p>

#### [ Patrick Massot (Jul 15 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff%20completion/near/129700245):
<p>It's uniformly continuous, hence respects the separability relation (this is the first lemma in the other uniformity thread).</p>

#### [ Patrick Massot (Jul 15 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff%20completion/near/129700297):
<p>Anyway, I now have the universal mapping property for Hausdorff completion: <a href="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L40-L41" target="_blank" title="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L40-L41">https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L40-L41</a>  It also uses Chris' proof at <a href="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/quotient.lean" target="_blank" title="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/quotient.lean">https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/quotient.lean</a></p>

#### [ Johan Commelin (Oct 15 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff%20completion/near/135846674):
<blockquote>
<p>Uniform spaces have Hausdorff completions <a href="https://github.com/leanprover/mathlib/blob/80d688e3ae2a721ab61f4cd000ea3e336158b04f/analysis/topology/completion.lean#L535" target="_blank" title="https://github.com/leanprover/mathlib/blob/80d688e3ae2a721ab61f4cd000ea3e336158b04f/analysis/topology/completion.lean#L535">https://github.com/leanprover/mathlib/blob/80d688e3ae2a721ab61f4cd000ea3e336158b04f/analysis/topology/completion.lean#L535</a>. More precisely, there is a completion functor which is left-adjoint to the inclusion of complete Hausdorff spaces into all uniform spaces. (Quoted from <a href="#narrow/stream/116395-maths/subject/What's.20new.20in.20Lean.20maths.3F/near/135846567" title="#narrow/stream/116395-maths/subject/What's.20new.20in.20Lean.20maths.3F/near/135846567">here</a>.)</p>
</blockquote>
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> When you say "functor" and "left-adjoint" are you actually using category-theoretical machinery? Or do you mean that all the ingredients are there, and that what's left is that we just need to write the abstract nonsense boilerplate?</p>

#### [ Patrick Massot (Oct 15 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff%20completion/near/135846789):
<p>Adjunctions are not yet in mathlib, so I mean all the ingredients are there</p>

#### [ Patrick Massot (Oct 15 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff%20completion/near/135846966):
<p>There is a map from a uniform space to its completion: <a href="https://github.com/leanprover/mathlib/blob/80d688e3ae2a721ab61f4cd000ea3e336158b04f/analysis/topology/topological_groups.lean#L27" target="_blank" title="https://github.com/leanprover/mathlib/blob/80d688e3ae2a721ab61f4cd000ea3e336158b04f/analysis/topology/topological_groups.lean#L27">https://github.com/leanprover/mathlib/blob/80d688e3ae2a721ab61f4cd000ea3e336158b04f/analysis/topology/topological_groups.lean#L27</a> (it's called <code>coe</code> because it is setup as a coercion in Lean sense). Maps into a completed Hausdorff space factor through the completion: <a href="https://github.com/leanprover/mathlib/blob/80d688e3ae2a721ab61f4cd000ea3e336158b04f/analysis/topology/completion.lean#L651" target="_blank" title="https://github.com/leanprover/mathlib/blob/80d688e3ae2a721ab61f4cd000ea3e336158b04f/analysis/topology/completion.lean#L651">https://github.com/leanprover/mathlib/blob/80d688e3ae2a721ab61f4cd000ea3e336158b04f/analysis/topology/completion.lean#L651</a> This is used to build the action of the completion functor on arrows: <a href="https://github.com/leanprover/mathlib/blob/80d688e3ae2a721ab61f4cd000ea3e336158b04f/analysis/topology/completion.lean#L670" target="_blank" title="https://github.com/leanprover/mathlib/blob/80d688e3ae2a721ab61f4cd000ea3e336158b04f/analysis/topology/completion.lean#L670">https://github.com/leanprover/mathlib/blob/80d688e3ae2a721ab61f4cd000ea3e336158b04f/analysis/topology/completion.lean#L670</a> this is functorial <a href="https://github.com/leanprover/mathlib/blob/80d688e3ae2a721ab61f4cd000ea3e336158b04f/analysis/topology/completion.lean#L700" target="_blank" title="https://github.com/leanprover/mathlib/blob/80d688e3ae2a721ab61f4cd000ea3e336158b04f/analysis/topology/completion.lean#L700">https://github.com/leanprover/mathlib/blob/80d688e3ae2a721ab61f4cd000ea3e336158b04f/analysis/topology/completion.lean#L700</a> etc. etc. (I'm skipping a lot. I think everything is there)</p>


{% endraw %}
