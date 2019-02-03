---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/90773invalidcalctransitivityrule.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [invalid 'calc': transitivity rule](https://leanprover-community.github.io/archive/113488general/90773invalidcalctransitivityrule.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Apr 16 2018 at 03:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130147):
<blockquote>
<p>invalid 'calc' expression, transitivity rule is not defined for current step</p>
</blockquote>

#### [ Kenny Lau (Apr 16 2018 at 03:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130156):
<p>I am using <code>≃</code> in <code>calc</code> as in <a href="https://github.com/leanprover/mathlib/blob/master/group_theory/coset.lean#L146" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/group_theory/coset.lean#L146">here</a></p>

#### [ Kenny Lau (Apr 16 2018 at 03:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130157):
<p>why does it give me this error?</p>

#### [ Kenny Lau (Apr 16 2018 at 03:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130159):
<p>mathlib:</p>
<div class="codehilite"><pre><span></span>lemma group_equiv_left_cosets_times_subgroup {s : set α} (hs : is_subgroup s) :
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
</pre></div>

#### [ Kenny Lau (Apr 16 2018 at 03:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130160):
<p>why can mathlib use it but gives me error when I use it</p>

#### [ Kenny Lau (Apr 16 2018 at 04:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130403):
<p>oh my god</p>

#### [ Kenny Lau (Apr 16 2018 at 04:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130414):
<p>it is a totally unrelated error caused by <code>≃</code> having higher priority than <code>×</code></p>

#### [ Mario Carneiro (Apr 16 2018 at 04:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130459):
<p>the priority of ≃ is a bit dumb, I know</p>

#### [ Mario Carneiro (Apr 16 2018 at 04:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130468):
<p>but it's hard to be both equality like and also lower than most type operators</p>

#### [ Kenny Lau (Apr 16 2018 at 04:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130475):
<div class="codehilite"><pre><span></span>theorem orbit_stab : nonempty ((orbit G X x × stab G X x) ≃ G) :=
nonempty.elim (orbit_equiv_stab_cosets G X x) $ λ F1,
nonempty.elim (is_subgroup.group_equiv_left_cosets_times_subgroup $ stab.is_subgroup G X x) $ λ F2,
nonempty.intro $
(equiv.prod_congr F1 (equiv.refl $ stab G X x)).trans
F2.symm
</pre></div>

#### [ Kenny Lau (Apr 16 2018 at 04:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130477):
<p>orbit-stabilizer theorem done :D</p>

#### [ Mario Carneiro (Apr 16 2018 at 04:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130517):
<p>does it have to be <code>nonempty</code>? Can't you give the equiv itself?</p>

#### [ Kenny Lau (Apr 16 2018 at 04:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130520):
<p>ask <code>group_equiv_left_cosets_times_subgroup</code></p>

#### [ Kenny Lau (Apr 16 2018 at 04:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130522):
<p><a href="https://github.com/leanprover/mathlib/blob/master/group_theory/coset.lean#L146" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/group_theory/coset.lean#L146">https://github.com/leanprover/mathlib/blob/master/group_theory/coset.lean#L146</a></p>

#### [ Kenny Lau (Apr 16 2018 at 04:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130524):
<p>hey <code>group_equiv_left_cosets_times_subgroup</code>, why are you nonempty?</p>

#### [ Mario Carneiro (Apr 16 2018 at 04:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130533):
<p>probably because of the choice in the middle</p>

#### [ Mario Carneiro (Apr 16 2018 at 04:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130572):
<p>you can't constructively pick an element from each coset</p>

#### [ Kenny Lau (Apr 16 2018 at 04:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130574):
<p>I see</p>

#### [ Mario Carneiro (Apr 16 2018 at 04:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130576):
<p>does that generalize to your theorem?</p>

#### [ Kenny Lau (Apr 16 2018 at 04:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130577):
<p>well I used that theorem so it has to be nonempty</p>

#### [ Mario Carneiro (Apr 16 2018 at 04:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130630):
<p>Maybe your application is constructive though</p>

#### [ Kenny Lau (Apr 16 2018 at 04:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130675):
<p>well then it is <code>noncomputable def</code> at most?</p>

#### [ Kenny Lau (Apr 16 2018 at 04:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130677):
<p>don't quite see the difference between that and just <code>nonempty</code></p>

#### [ Mario Carneiro (Apr 16 2018 at 04:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130678):
<p>I think <code>orbit_equiv_stab_cosets</code> gives you a way to select an element from each coset</p>

#### [ Mario Carneiro (Apr 16 2018 at 04:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130679):
<p>I think it is computable</p>

#### [ Kenny Lau (Apr 16 2018 at 04:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130683):
<p>that one isn't computable either</p>

#### [ Kenny Lau (Apr 16 2018 at 04:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130687):
<p>there's no computable inverse</p>

#### [ Kenny Lau (Apr 16 2018 at 04:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130688):
<p>I am not using quotient</p>

#### [ Mario Carneiro (Apr 16 2018 at 04:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130692):
<p>Maybe the problem is that you have to deal with cosets then</p>

#### [ Kenny Lau (Apr 16 2018 at 04:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130733):
<p>well maybe <a href="https://github.com/leanprover/mathlib/blob/master/group_theory/coset.lean" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/group_theory/coset.lean">https://github.com/leanprover/mathlib/blob/master/group_theory/coset.lean</a> could use quotients instead of sets</p>

#### [ Kenny Lau (Apr 16 2018 at 04:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130734):
<p>then our lives will be easier</p>

#### [ Kenny Lau (Apr 16 2018 at 04:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130735):
<p>they even have the equivalence relation set up</p>

#### [ Mario Carneiro (Apr 16 2018 at 04:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130838):
<p>I think you are right...</p>

#### [ Kevin Buzzard (Apr 16 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125137593):
<p>You need the axiom of choice to pick coset representatives, i.e. if G is a group (even an abelian group) and H is a subgroup then you need the axiom of choice to choose a subset S of G containing precisely one element of each coset. One perhaps rather convoluted way of seeing this is that if G is the reals and H the rationals then if you can choose S then you can build a non-measurable subset of the reals; however there is a model of ZF (no C) in which every set is measurable.</p>

#### [ Kevin Buzzard (Apr 16 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125137646):
<p>Apply this to the action of G on the cosets of H and you see that an explicit bijection would give you S, you look at the image of (orbit x {1})</p>

#### [ Kenny Lau (Apr 16 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125137657):
<p>what is this a response to?</p>

#### [ Mario Carneiro (Apr 16 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125137746):
<p>I think he is arguing that the orbit stabilizer theorem is also necessarily nonconstructive (in the infinite case)</p>

#### [ Kevin Buzzard (Apr 16 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125137752):
<blockquote>
<p>does it have to be <code>nonempty</code>? Can't you give the equiv itself?</p>
</blockquote>

#### [ Kenny Lau (Apr 16 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125137754):
<p>it's nonconstructive, but can't we use noncomputable def instead of nonempty</p>

#### [ Kevin Buzzard (Apr 16 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125137850):
<p>I'm not sure I understand the question yet. I think that out of everyone in this conversation I'm the least well placed to answer it anyway. I just wanted to tell you (Kenny) the argument I came up with yesterday which convinced me that some form of nonconstructive maths was provably needed to choose coset reps.</p>

#### [ Kenny Lau (Apr 16 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125137898):
<p>we three all agree with that</p>

#### [ Mario Carneiro (Apr 16 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125138168):
<p>You can always extract an equiv from a nonempty equiv using <code>choice</code>, which makes it a noncomputable def. Doing this before or after makes little difference</p>

#### [ Kevin Buzzard (Apr 16 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125138181):
<blockquote>
<p>we three all agree with that</p>
</blockquote>
<p>yes, but I gave a proof ;-)</p>

#### [ Patrick Massot (Apr 16 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125138750):
<p>It's a complete mystery to me: why mathlib doesn't use a quotient to talk about quotient of a group by a (non-normal) subgroup?</p>

#### [ Kenny Lau (Apr 16 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125138755):
<p>well "mathlib" isn't a person</p>

#### [ Kenny Lau (Apr 16 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125138760):
<p>and the person you seek is <span class="user-mention" data-user-id="110524">@Scott Morrison</span></p>

#### [ Kenny Lau (Apr 16 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125138764):
<p>and this thing is just here 5 days ago</p>

#### [ Patrick Massot (Apr 16 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125138770):
<p>I'm sure it's older</p>

#### [ Patrick Massot (Apr 16 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125138773):
<p>When Johannes proved Lagrange</p>

#### [ Kenny Lau (Apr 16 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125138816):
<p>nvm what i said is bs</p>

#### [ Kenny Lau (Apr 16 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125138819):
<p>right, <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> proved it in March 6</p>

#### [ Johannes Hölzl (Apr 16 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125138964):
<p>The answer is simple: I didn't think about quotients of a group to prove Lagrange. I just wanted to show a property about the orbit of a group.</p>

#### [ Patrick Massot (Apr 16 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125139451):
<p>But the orbit of a point  is canonically the quotient of the group by the stabilizer of the point</p>

#### [ Kenny Lau (Apr 16 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125139455):
<p>cardinalities don't interact well with quotients</p>

#### [ Patrick Massot (Apr 16 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125139460):
<p>(deleted)</p>


{% endraw %}
