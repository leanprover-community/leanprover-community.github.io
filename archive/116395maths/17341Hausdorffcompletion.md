---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/17341Hausdorffcompletion.html
---

## [maths](index.html)
### [Hausdorff completion](17341Hausdorffcompletion.html)

#### [Patrick Massot (Jul 11 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff completion/near/129461026):
@**Johannes Hölzl** around https://github.com/leanprover/mathlib/blob/master/analysis/topology/uniform_space.lean#L1102, is there any reason why you didn't push to the Hausdorff completion? Is the idea that users should easily combine stuff in this section with the https://github.com/leanprover/mathlib/blob/master/analysis/topology/uniform_space.lean#L928 section? Or did you intend to continue this?

#### [Johannes Hölzl (Jul 11 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff completion/near/129462922):
The idea was to be compositional. So I wanted to split the separation quotient from the Cauchy construction. I'm not exactly sure what Hausdorff completion is, but I guess you can use the composition `hausdorff_completion α := quotient (separation_setoid (Cauchy α))`. Or do I miss something?

#### [Patrick Massot (Jul 11 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff completion/near/129463129):
Yes, this is what I had in mind.

#### [Patrick Massot (Jul 11 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff completion/near/129463135):
Or maybe compose in the opposite order, I would need to think whether it's the same

#### [Patrick Massot (Jul 11 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff completion/near/129463277):
Bourbaki does it a bit differently. They consider the space of *minimal* Cauchy filters.. It seems this is always Hausdorff

#### [Patrick Massot (Jul 11 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff completion/near/129464037):
I found some text claiming that your definition of `hausdorff_completion α` gives the same result as the minimal Cauchy filter definition. Anyway, the real test is to try to prove the universal property for this definition (every uniformly continuous map from `α` into a complete Hausdorff space factors through the, not necessarily injective, "inclusion" of `α` in `hausdorff_completion α`)

#### [Johannes Hölzl (Jul 11 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff completion/near/129480597):
I didn't choose to use minimal Cauchy filters, as I thought the splitting into (all) Cauchy filters and quotient makes the formalization easier. And the separation quotient will be used anyway. The universal property is proved for each dense embedding from a closed set on a complete space (see section `uniform_extension`)

#### [Patrick Massot (Jul 11 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff completion/near/129481701):
I understand. I have a stub at  https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean  that I'll try to complete. I think I understand what's already in mathlib and what remains to be done. Then next step would be to unsorry the end of https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/topological_structures.lean

#### [Johannes Hölzl (Jul 11 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff completion/near/129495769):
All this was already done for the real numbers, if you want I can look it up in the mathlib history

#### [Patrick Massot (Jul 11 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff completion/near/129495855):
Any help is welcome

#### [Patrick Massot (Jul 11 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff completion/near/129495862):
But there is no separation issue in the real case

#### [Patrick Massot (Jul 11 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff completion/near/129496013):
By the way, is https://github.com/leanprover/mathlib/blob/master/analysis/topology/uniform_space.lean#L18 still true?

#### [Johannes Hölzl (Jul 11 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff completion/near/129496855):
No, its not true anymore.
As far as I remember, there is a separation issue for the real case: I used the separation/Cauchy construction: https://github.com/leanprover/mathlib/blob/7fd7ea8c323c5f622bda6bc8de6dd352cc2732a8/analysis/real.lean#L384

#### [Patrick Massot (Jul 11 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff completion/near/129497515):
Thanks. This will probably be very useful when I'll move to completions of groups and rings. But I don't see anything that looks like the universal property of Hausdorff  completions

#### [Patrick Massot (Jul 11 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff completion/near/129497598):
I'm really curious to know why the separation quotient was necessary. I have no intuition about filters, but to me rationals numbers seems separated enough.

#### [Johannes Hölzl (Jul 11 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff completion/near/129498685):
But the _Cauchy filters over the rationals_ are not separated. In this regard is no difference between Cauchy sequences and filters. One also needs to put a quotient over the Cauchy sequences when constructing the reals via Cauchy sequences.

#### [Patrick Massot (Jul 11 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff completion/near/129499261):
Indeed

#### [Patrick Massot (Jul 15 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff completion/near/129696906):
Now I know what I meant. The fundamental difference is that the map `of_rat  ℚ → ℝ` is injective. Then you proved it's a uniform embedding, and used lemmas about uniform embeddings everywhere. This is no longer true in my context.

#### [Johannes Hölzl (Jul 15 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff completion/near/129699781):
So instead of injective your function respects the separability relation?

#### [Patrick Massot (Jul 15 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff completion/near/129700245):
It's uniformly continuous, hence respects the separability relation (this is the first lemma in the other uniformity thread).

#### [Patrick Massot (Jul 15 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff completion/near/129700297):
Anyway, I now have the universal mapping property for Hausdorff completion: https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L40-L41  It also uses Chris' proof at https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/quotient.lean

#### [Johan Commelin (Oct 15 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff completion/near/135846674):
```quote
Uniform spaces have Hausdorff completions https://github.com/leanprover/mathlib/blob/80d688e3ae2a721ab61f4cd000ea3e336158b04f/analysis/topology/completion.lean#L535. More precisely, there is a completion functor which is left-adjoint to the inclusion of complete Hausdorff spaces into all uniform spaces. (Quoted from [here](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/subject/What's.20new.20in.20Lean.20maths.3F/near/135846567).)
```
@**Patrick Massot** When you say "functor" and "left-adjoint" are you actually using category-theoretical machinery? Or do you mean that all the ingredients are there, and that what's left is that we just need to write the abstract nonsense boilerplate?

#### [Patrick Massot (Oct 15 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff completion/near/135846789):
Adjunctions are not yet in mathlib, so I mean all the ingredients are there

#### [Patrick Massot (Oct 15 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hausdorff completion/near/135846966):
There is a map from a uniform space to its completion: https://github.com/leanprover/mathlib/blob/80d688e3ae2a721ab61f4cd000ea3e336158b04f/analysis/topology/topological_groups.lean#L27 (it's called `coe` because it is setup as a coercion in Lean sense). Maps into a completed Hausdorff space factor through the completion: https://github.com/leanprover/mathlib/blob/80d688e3ae2a721ab61f4cd000ea3e336158b04f/analysis/topology/completion.lean#L651 This is used to build the action of the completion functor on arrows: https://github.com/leanprover/mathlib/blob/80d688e3ae2a721ab61f4cd000ea3e336158b04f/analysis/topology/completion.lean#L670 this is functorial https://github.com/leanprover/mathlib/blob/80d688e3ae2a721ab61f4cd000ea3e336158b04f/analysis/topology/completion.lean#L700 etc. etc. (I'm skipping a lot. I think everything is there)

