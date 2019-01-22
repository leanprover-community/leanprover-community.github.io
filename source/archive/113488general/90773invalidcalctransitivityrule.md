---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/90773invalidcalctransitivityrule.html
---

## [general](index.html)
### [invalid 'calc': transitivity rule](90773invalidcalctransitivityrule.html)

#### [Kenny Lau (Apr 16 2018 at 03:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130147):
> invalid 'calc' expression, transitivity rule is not defined for current step

#### [Kenny Lau (Apr 16 2018 at 03:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130156):
I am using `≃` in `calc` as in [here](https://github.com/leanprover/mathlib/blob/master/group_theory/coset.lean#L146)

#### [Kenny Lau (Apr 16 2018 at 03:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130157):
why does it give me this error?

#### [Kenny Lau (Apr 16 2018 at 03:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130159):
mathlib:
```
lemma group_equiv_left_cosets_times_subgroup {s : set α} (hs : is_subgroup s) :
  nonempty (α ≃ (left_cosets s × s)) :=
⟨calc α ≃ (@set.univ α) :
    (equiv.set.univ α).symm
  ... ≃ (⋃t∈left_cosets s, t) :
    by rw [←hs.Union_left_cosets_eq_univ]; simp
  ... ≃ (Σt:left_cosets s, t) :
    equiv.set.bUnion_eq_sigma_of_disjoint hs.pairwise_left_cosets_disjoint
  ... ≃ (Σt:left_cosets s, s) :
    equiv.sigma_congr_right $ λ⟨t, ht⟩, classical.choice $ hs.left_cosets_equiv_subgroup ht
  ... ≃ (left_cosets s × s) :
    equiv.sigma_equiv_prod _ _⟩

#### [Kenny Lau (Apr 16 2018 at 03:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130160):
why can mathlib use it but gives me error when I use it

#### [Kenny Lau (Apr 16 2018 at 04:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130403):
oh my god

#### [Kenny Lau (Apr 16 2018 at 04:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130414):
it is a totally unrelated error caused by `≃` having higher priority than `×`

#### [Mario Carneiro (Apr 16 2018 at 04:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130459):
the priority of ≃ is a bit dumb, I know

#### [Mario Carneiro (Apr 16 2018 at 04:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130468):
but it's hard to be both equality like and also lower than most type operators

#### [Kenny Lau (Apr 16 2018 at 04:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130475):
```
theorem orbit_stab : nonempty ((orbit G X x × stab G X x) ≃ G) :=
nonempty.elim (orbit_equiv_stab_cosets G X x) $ λ F1,
nonempty.elim (is_subgroup.group_equiv_left_cosets_times_subgroup $ stab.is_subgroup G X x) $ λ F2,
nonempty.intro $
(equiv.prod_congr F1 (equiv.refl $ stab G X x)).trans
F2.symm

#### [Kenny Lau (Apr 16 2018 at 04:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130477):
orbit-stabilizer theorem done :D

#### [Mario Carneiro (Apr 16 2018 at 04:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130517):
does it have to be `nonempty`? Can't you give the equiv itself?

#### [Kenny Lau (Apr 16 2018 at 04:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130520):
ask `group_equiv_left_cosets_times_subgroup`

#### [Kenny Lau (Apr 16 2018 at 04:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130522):
https://github.com/leanprover/mathlib/blob/master/group_theory/coset.lean#L146

#### [Kenny Lau (Apr 16 2018 at 04:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130524):
hey `group_equiv_left_cosets_times_subgroup`, why are you nonempty?

#### [Mario Carneiro (Apr 16 2018 at 04:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130533):
probably because of the choice in the middle

#### [Mario Carneiro (Apr 16 2018 at 04:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130572):
you can't constructively pick an element from each coset

#### [Kenny Lau (Apr 16 2018 at 04:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130574):
I see

#### [Mario Carneiro (Apr 16 2018 at 04:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130576):
does that generalize to your theorem?

#### [Kenny Lau (Apr 16 2018 at 04:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130577):
well I used that theorem so it has to be nonempty

#### [Mario Carneiro (Apr 16 2018 at 04:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130630):
Maybe your application is constructive though

#### [Kenny Lau (Apr 16 2018 at 04:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130675):
well then it is `noncomputable def` at most?

#### [Kenny Lau (Apr 16 2018 at 04:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130677):
don't quite see the difference between that and just `nonempty`

#### [Mario Carneiro (Apr 16 2018 at 04:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130678):
I think `orbit_equiv_stab_cosets` gives you a way to select an element from each coset

#### [Mario Carneiro (Apr 16 2018 at 04:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130679):
I think it is computable

#### [Kenny Lau (Apr 16 2018 at 04:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130683):
that one isn't computable either

#### [Kenny Lau (Apr 16 2018 at 04:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130687):
there's no computable inverse

#### [Kenny Lau (Apr 16 2018 at 04:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130688):
I am not using quotient

#### [Mario Carneiro (Apr 16 2018 at 04:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130692):
Maybe the problem is that you have to deal with cosets then

#### [Kenny Lau (Apr 16 2018 at 04:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130733):
well maybe https://github.com/leanprover/mathlib/blob/master/group_theory/coset.lean could use quotients instead of sets

#### [Kenny Lau (Apr 16 2018 at 04:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130734):
then our lives will be easier

#### [Kenny Lau (Apr 16 2018 at 04:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130735):
they even have the equivalence relation set up

#### [Mario Carneiro (Apr 16 2018 at 04:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130838):
I think you are right...

#### [Kevin Buzzard (Apr 16 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125137593):
You need the axiom of choice to pick coset representatives, i.e. if G is a group (even an abelian group) and H is a subgroup then you need the axiom of choice to choose a subset S of G containing precisely one element of each coset. One perhaps rather convoluted way of seeing this is that if G is the reals and H the rationals then if you can choose S then you can build a non-measurable subset of the reals; however there is a model of ZF (no C) in which every set is measurable.

#### [Kevin Buzzard (Apr 16 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125137646):
Apply this to the action of G on the cosets of H and you see that an explicit bijection would give you S, you look at the image of (orbit x {1})

#### [Kenny Lau (Apr 16 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125137657):
what is this a response to?

#### [Mario Carneiro (Apr 16 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125137746):
I think he is arguing that the orbit stabilizer theorem is also necessarily nonconstructive (in the infinite case)

#### [Kevin Buzzard (Apr 16 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125137752):
```quote
does it have to be `nonempty`? Can't you give the equiv itself?
```

#### [Kenny Lau (Apr 16 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125137754):
it's nonconstructive, but can't we use noncomputable def instead of nonempty

#### [Kevin Buzzard (Apr 16 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125137850):
I'm not sure I understand the question yet. I think that out of everyone in this conversation I'm the least well placed to answer it anyway. I just wanted to tell you (Kenny) the argument I came up with yesterday which convinced me that some form of nonconstructive maths was provably needed to choose coset reps.

#### [Kenny Lau (Apr 16 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125137898):
we three all agree with that

#### [Mario Carneiro (Apr 16 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125138168):
You can always extract an equiv from a nonempty equiv using `choice`, which makes it a noncomputable def. Doing this before or after makes little difference

#### [Kevin Buzzard (Apr 16 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125138181):
```quote
we three all agree with that
```
yes, but I gave a proof ;-)

#### [Patrick Massot (Apr 16 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125138750):
It's a complete mystery to me: why mathlib doesn't use a quotient to talk about quotient of a group by a (non-normal) subgroup?

#### [Kenny Lau (Apr 16 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125138755):
well "mathlib" isn't a person

#### [Kenny Lau (Apr 16 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125138760):
and the person you seek is @**Scott Morrison**

#### [Kenny Lau (Apr 16 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125138764):
and this thing is just here 5 days ago

#### [Patrick Massot (Apr 16 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125138770):
I'm sure it's older

#### [Patrick Massot (Apr 16 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125138773):
When Johannes proved Lagrange

#### [Kenny Lau (Apr 16 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125138816):
nvm what i said is bs

#### [Kenny Lau (Apr 16 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125138819):
right, @**Johannes Hölzl** proved it in March 6

#### [Johannes Hölzl (Apr 16 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125138964):
The answer is simple: I didn't think about quotients of a group to prove Lagrange. I just wanted to show a property about the orbit of a group.

#### [Patrick Massot (Apr 16 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125139451):
But the orbit of a point  is canonically the quotient of the group by the stabilizer of the point

#### [Kenny Lau (Apr 16 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125139455):
cardinalities don't interact well with quotients

#### [Patrick Massot (Apr 16 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125139460):
(deleted)

