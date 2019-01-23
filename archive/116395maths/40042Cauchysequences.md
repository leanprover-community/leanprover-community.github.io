---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/40042Cauchysequences.html
---

## Stream: [maths](index.html)
### Topic: [Cauchy sequences](40042Cauchysequences.html)

---

#### [Sebastien Gouezel (Oct 20 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy%20sequences/near/136173276):
If I understand correctly, for now, in mathlib, there are Cauchy filters, and a notion named `cau_seq` but defined on rings and with respect to some absolute value, but not the classical notion of Cauchy sequence in metric spaces (which is simply `cauchy (at_top.map u)` where `u` is a sequence from ℕ to some metric or even uniform space). And neither is the fact that a metric space is complete iff every Cauchy sequence converges, right?

Would it make sense to use `cau_seq_abv` for the slightly exotic `cau_seq` above, and to use `cau_seq` for the usual notion? I fear there would be some duplication with the current `cau_seq`, but I do not see how it could be avoided without a big refactoring.

#### [Kenny Lau (Oct 20 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy%20sequences/near/136173321):
I don't think that's right. We do have everything you say.

#### [Reid Barton (Oct 20 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy%20sequences/near/136173379):
I think there was some question here about how to prove that a metric space in which every Cauchy sequence converges is complete

#### [Sebastien Gouezel (Oct 20 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy%20sequences/near/136173387):
```quote
I don't think that's right. We do have everything you say.
```
Great! Can you point me to the definition of metric Cauchy sequences?

#### [Mario Carneiro (Oct 20 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy%20sequences/near/136173403):
we have Cauchy filters

#### [Reid Barton (Oct 20 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy%20sequences/near/136173407):
See https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/Sequences.20in.20topological.2Fmetric.20spaces/near/133882373

#### [Mario Carneiro (Oct 20 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy%20sequences/near/136173412):
I don't think there is much point in focusing on sequences once we go to that generality, except as a "oh by the way"

#### [Kenny Lau (Oct 20 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy%20sequences/near/136173414):
oh right, I confused it with Cauchy filter.

#### [Kenny Lau (Oct 20 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy%20sequences/near/136173457):
what's wrong with `cauchy (at_top.map u)`?

#### [Sebastien Gouezel (Oct 20 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy%20sequences/near/136173527):
When you prove completeness of a metric space, you really want to restrict to sequences. For instance, the completeness of `L^p` is proved by taking a converging series, arguing about the almost sure convergence, and then deducing convergence in `L^p` using some monotone convergence theorem. This is a subtle proof, and it really goes through sequences, not filters :)

#### [Sebastien Gouezel (Oct 20 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy%20sequences/near/136173561):
And the notion you want to use is the epsilon-delta one, by the way.

#### [Reid Barton (Oct 20 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy%20sequences/near/136173700):
As I mentioned in the linked conversation, `cauchy_of_metric` should give you the epsilon-N definition if you apply it to `at_top` I think

#### [Reid Barton (Oct 20 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy%20sequences/near/136173710):
Any fact like "in order to check P for all X you only need to check it for X of a special form Y" is a good fact which we should have. I think we don't have this for checking completeness of metric spaces in terms of sequences, and we should.

#### [Sebastien Gouezel (Oct 21 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy%20sequences/near/136225391):
It is already there in disguise, in `data.real.cau_seq_filter`, but formulated only in normed fields. See #PR435 for an adaptation to all metric spaces.

#### [Mario Carneiro (Oct 22 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy%20sequences/near/136233400):
I think you don't need metric spaces for cauchy sequences

#### [Mario Carneiro (Oct 22 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy%20sequences/near/136233404):
first countable uniform spaces should be enough

#### [Mario Carneiro (Oct 22 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy%20sequences/near/136233409):
I think facts of the form "sequences are as good as filters" are what first countability is all about

#### [Mario Carneiro (Oct 22 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy%20sequences/near/136233469):
But I'm also not convinced by your monotone convergence example. There are quite a lot of theorems in metric space theory that are stated on sequences just because that's the tool you have, even though they would be easier expressed with filters

#### [Sebastien Gouezel (Oct 22 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy%20sequences/near/136251760):
First countable is only talking about neighborhoods of points that exist in the space. If you imagine a first countable complete uniform space, except for a point `x` that can not be reached by countable sequences, and you remove this point, then the new space will still be first countable, all Cauchy sequences will converge, and still it will not be complete. The good condition would rather be that the uniformity is countably generated, but we have no type class for this, and I do not see real life examples where it would be useful to have this generalization.

For the completeness of `L^p`, let me insist that this is really something which is proved by sequences (contrary to many statements in metric spaces that could be proved more easily with filters, I completely agree with you about that). With more details, the proof goes as follows. Take a Cauchy sequences `u n`. Extract a subsequence `v n` such that the distance from `v n`to `v(n+1)` is at most `2^{-n}`. Form the series `V = \sum \abs(v_{n+1} - v_n)`. Check that it has finite integral. In particular, it is almost everywhere finite. Then the series `v = \sum (v_{n+1} - v_n)` is also defined almost everywhere. Moreover, by dominated convergence (using the dominating function `V`), `v n` tends to `v` in `L^p`. Finally, our original Cauchy sequence `u n` has a converging subsequence, hence it converges.

#### [Mario Carneiro (Oct 22 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy%20sequences/near/136252243):
It looks to me like the original cauchy sequence serves no purpose here

#### [Mario Carneiro (Oct 22 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy%20sequences/near/136252246):
because you have to refine it by a subsequence anyway

#### [Mario Carneiro (Oct 22 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy%20sequences/near/136252250):
you may as well have taken a sequence out of a filter

#### [Sebastien Gouezel (Oct 22 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy%20sequences/near/136252401):
This is true, but taking a subsequence out of a sequence is much easier than taking a sequence out of a filter.

#### [Mario Carneiro (Oct 22 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy%20sequences/near/136252466):
is it?

#### [Mario Carneiro (Oct 22 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy%20sequences/near/136252505):
the constraints are the same

#### [Mario Carneiro (Oct 22 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy%20sequences/near/136252549):
at least, it's not obvious to me that there is much difference

#### [Sebastien Gouezel (Oct 22 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy%20sequences/near/136252683):
Well, the proof of completeness from sequential completeness is not really trivial: the version written by Robert Lewis takes roughly 150 lines. And the main point is to extract a sequence from a filter. Extracting a subsequence from a Cauchy sequence should take 5 lines, at most 10. But maybe this simply shows that Robert was not perfectly efficient in its filter use (and I certainly would not have been more efficient), I can not say for sure. What I can say for sure is that, the day a mathematician who is not completely familiar with the filters library wants to prove the completeness of some Sobolev or Hardy space, say, he will be extremely happy to have the sequential criterion!

#### [Mario Carneiro (Oct 22 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy%20sequences/near/136252738):
I don't mean to say that we should not have sequences

#### [Mario Carneiro (Oct 22 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy%20sequences/near/136252742):
but the language to talk about them is there

#### [Mario Carneiro (Oct 22 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy%20sequences/near/136252752):
if you want to formalize a proof using sequences, the lemmas should be there to help you do so

#### [Mario Carneiro (Oct 22 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy%20sequences/near/136252774):
but they may also be avoidable, and I think there will often be a proof length gain in doing so

#### [Mario Carneiro (Oct 22 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy%20sequences/near/136252789):
The equivalence may very well be nontrivial, but that's a one time cost

#### [Mario Carneiro (Oct 22 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy%20sequences/near/136252842):
What 150 line proof are you talking about?

#### [Sebastien Gouezel (Oct 22 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy%20sequences/near/136252938):
The one in `data.real.cau_seq_filter` that my pull request #PR435 refactors. By the way, I have edited my branch to remove the leftover statements, and answered your comment on this PR, but nothing shows up on the PR page. Is github more or less down?

#### [Mario Carneiro (Oct 22 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy%20sequences/near/136253090):
I was having some issues with GH a few hours ago, status says the DB is undergoing some "repairs"

#### [Mario Carneiro (Oct 22 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy%20sequences/near/136253140):
I think the proof can be simplified a bit, but I will work from your version rather than Rob's if you've already refactored it

#### [Mario Carneiro (Oct 22 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy%20sequences/near/136253194):
in particular I notice `cauchy_of_metric` is never used, which would simplify things

#### [Mario Carneiro (Oct 22 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy%20sequences/near/136253220):
(at least in `cauchy_of_filter_cauchy` and converse)

#### [Sebastien Gouezel (Oct 22 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy%20sequences/near/136253355):
In my PR, I have in `metric_space.lean` a statement `cauchy_seq_metric` expressing Cauchy sequences purely in metric terms, and using `cauchy_of_metric`, so `cauchy_of_filter_cauchy`and converse  should become essentially trivial.

#### [Mario Carneiro (Oct 22 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy%20sequences/near/136253371):
what is this `topo_metric` thing?

#### [Mario Carneiro (Oct 22 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy%20sequences/near/136253438):
also `cauchy_seq_metric` should have a trivial proof if you prove the behavior of the at_top quantifier

#### [Sebastien Gouezel (Oct 22 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy%20sequences/near/136253554):
`topo_metric` means I consider maps from a topological space to a metric space. What would be a better name? `topo_to_metric` is bad as it seems to imply that we are converting a topology to a metric...

#### [Sebastien Gouezel (Oct 22 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Cauchy%20sequences/near/136253561):
I have to go. Feel free to change anything you like!

