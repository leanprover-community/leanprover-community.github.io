---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/34371GaussLemmaandEisensteinsCriterion.html
---

## Stream: [maths](index.html)
### Topic: [Gauss Lemma and Eisenstein's Criterion](34371GaussLemmaandEisensteinsCriterion.html)

---


{% raw %}
#### [ Aditya Agarwal (Nov 13 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Gauss%20Lemma%20and%20Eisenstein%27s%20Criterion/near/147559555):
Is anyone working on Gauss Lemma and Eisenstein's Criterion or are they present in mathlib?

#### [ Kenny Lau (Nov 13 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Gauss%20Lemma%20and%20Eisenstein%27s%20Criterion/near/147559562):
@**Chris Hughes** What do you think

#### [ Kevin Buzzard (Nov 13 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Gauss%20Lemma%20and%20Eisenstein%27s%20Criterion/near/147559732):
I believe general UFDs are in mathlib nowadays, so anyone who implements them should probably do it in this generality.

#### [ Kevin Buzzard (Nov 13 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Gauss%20Lemma%20and%20Eisenstein%27s%20Criterion/near/147559809):
although I guess Rob Lewis proved all the stuff about valuations for the integers when defining the p-adic numbers, and it might even be the case that the basic theory of valuations for a general UFD is not done (athough it might be a fairly simple port from Rob's work on Z)

#### [ Johan Commelin (Nov 13 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Gauss%20Lemma%20and%20Eisenstein%27s%20Criterion/near/147576659):
@**Aditya Agarwal** Cool, I'm currently writing exercise sheets for 2nd year students who have to practice with Gauss Lemma and Eisenstein. It would be awesome if that lands in mathlib!

#### [ Kevin Buzzard (Nov 13 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Gauss%20Lemma%20and%20Eisenstein%27s%20Criterion/near/147576816):
https://github.com/leanprover/mathlib/blob/master/data/padics/padic_norm.lean The first 370 or so lines of that file are the basics of the p-adic valuation on the integers and rationals. That should all be ported to a general UFD really, if one is to do this properly. One needs it in the proofs of such things as R a UFD -> R[X] a UFD.


{% endraw %}
