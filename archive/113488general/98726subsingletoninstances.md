---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/98726subsingletoninstances.html
---

## [general](index.html)
### [subsingleton instances](98726subsingletoninstances.html)

#### [Chris Hughes (Mar 03 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton instances/near/123231023):
I'm struggling with the following proof
```lean
α : Type u_1,
s : set α,
_inst_1 : fintype ↥s,
h : s = ∅
⊢ card ↥s = 0
```
the trouble is that rw h` does not work because it has to rewrite the fintype instance at the same time. I'm having trouble in general with lean not recognizing two terms as equal because the fintype instances are different. Is there a nice way of dealing with this. I can use congr to prove that two terms with different fintype instances are equal, but this seems quite messy.

#### [Gabriel Ebner (Mar 03 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton instances/near/123231503):
Does `simp [h]` work by chance?

#### [Chris Hughes (Mar 03 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton instances/near/123232077):
no

#### [Kevin Buzzard (Mar 03 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton instances/near/123234939):
```  
import data.fintype
universe u


example (α : Type u) (s : set α) [fintype s] (h : s = ∅) : fintype.card ↥s = 0 := begin
rw ←fintype.card_empty,
rw fintype.card_eq,
rw h,
show nonempty ({x : α // false} ≃ empty),
refine ⟨_⟩,
refine ⟨_,_,_,_⟩,
exact λ x, false.elim x.property,
intro x,cases x,
intro x,exact false.elim x.property,
intro x,cases x,
end 

```

#### [Kevin Buzzard (Mar 03 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton instances/near/123234993):
kind of a comical proof because I never used these types before, so most of it is me experimenting with what is there. Obviously this can be shortened a lot.

#### [Chris Hughes (Mar 03 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton instances/near/123235101):
`rw ← set.empty_card; congr; assumption` is also a slightly shorter proof, but I was hoping there was an easy way.

#### [Patrick Massot (Mar 03 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton instances/near/123235357):
Are students allowed to be that insolent in England?

#### [Gabriel Ebner (Mar 03 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton instances/near/123235716):
I think this is a more idiomatic solution:
```lean
import data.fintype
universe u

@[simp] lemma fintype.card_emptyset (α : Type u) [fintype.{u} (∅ : set α)] :
    fintype.card (∅ : set α) = 0 :=
begin
simp [fintype.card], apply finset.ext.mpr, intros, cases a, cases a_property
end

local attribute [-simp] set.set_coe_eq_subtype -- bad simp lemma

example (α : Type u) (s : set α) [fintype s] (h : s = ∅) :
    fintype.card ↥s = 0 :=
by simp [h]
```

#### [Chris Hughes (Mar 03 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton instances/near/123237242):
the lemma `fintype.card_emptyset` already exists, it's called `set.empty_card` in data/set/finite. However it doesn't require a fintype instance as an argument, because it uses a different proof that the empty set is finite.

#### [Gabriel Ebner (Mar 03 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton instances/near/123237868):
That's the core of the misunderstanding: `fintype` is not a proof, it is data.  So you need to write all lemmas with generic `fintype` arguments, otherwise they won't match.  We have a very similar problem with decidability instances actually.

#### [Gabriel Ebner (Mar 03 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton instances/near/123237912):
One solution is to use E-matching in the SMT mode.  This would transparently ignore the different subsingleton instances.  However the SMT mode is abandoned and does not have a clear future.

#### [Gabriel Ebner (Mar 03 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton instances/near/123238082):
I'm not sure if I see a good and general solution.  The same issue applies not just to simp, but pretty much all tactics and also term-mode proof construction.  A somewhat clean approach that works in all those cases would be to post-process the types of lemmas, and generalize non-dependent subsingleton subterms.  Maybe we could do this automatically with more powerful user attributes, or user commands once the new parser lands.

#### [Kevin Buzzard (Mar 03 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton instances/near/123239544):
```quote
Are students allowed to be that insolent in England?
```
Ha ha :-) Chris knows a lot more about these finite types than I do. He's been doing stuff with finite groups -- I've never used them at all. Chris -- why not PR some stuff to xena? Or just email it me if you can't be bothered? I'd be interested to see what you've been doing.

#### [Chris Hughes (Mar 03 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton instances/near/123240179):
Just made a PR to xena. It's quite an incomplete file with a few sorries, but there's lagrange in there, which is good.

#### [Patrick Massot (Mar 04 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton instances/near/123256948):
What's the point of proving Lagrange without developing group actions? If you want to do more group theory you won't be able to bypass them much longer.

#### [Patrick Massot (Mar 04 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton instances/near/123256953):
@**Scott Morrison** what happened to your student who was doing group theory?

#### [Patrick Massot (Mar 04 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton instances/near/123256993):
@**Chris Hughes** what happened to your analysis PRs?

#### [Kevin Buzzard (Mar 04 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton instances/near/123261173):
```quote
What's the point of proving Lagrange without developing group actions? If you want to do more group theory you won't be able to bypass them much longer.
```
There's a danger here that you can argue that there's no point doing anything because someone did something more general. Chris is a first year undergraduate who just learnt Lagrange's theorem and we don't teach group actions until the 3rd year, so his view of the subject is very different to yours. I completely appreciate your point of view but the answer is that Chris is using Lean to teach himself the material that he's going to be examined on in the summer.

#### [Chris Hughes (Mar 04 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton instances/near/123261269):
@**Patrick Massot** I'm waiting for a PR on Cauchy Sequence limits to be merged, and then I'll merge some more stuff. There was a bit of discussion about the best way to implement the exponential function, about whether to do it using Johannes definition of a limit, or Mario's simpler definition of a limit. I'm not going to work on making it mathlib ready until that discussion is resolved.

The answer to your other question was pretty much the same as @**Kevin Buzzard** 's answer. I've no idea if my group theory stuff is useful, given that I've formalised most of what I know, it's unlikely I'll have defined things in the most useful manner.

#### [Patrick Massot (Mar 04 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton instances/near/123268844):
I agree that aiming for the greatest generality is not a good idea. My point is that, if you continue finite group theory, then you will encounter group actions really soon (for instance if you go for Sylow).

#### [Patrick Massot (Mar 04 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton instances/near/123268852):
Maybe I'm confused about what you know because Kevin teaches the concept of rigorous proofs, schemes, and perfectoid spaces in the same year.

#### [Kevin Buzzard (Mar 04 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton instances/near/123268901):
I teach several different courses/classes I guess

#### [Patrick Massot (Mar 04 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton instances/near/123268913):
No, you teach schemes to Kenny and you mentioned teaching perfectoid spaces to first years on March 11th or something

#### [Kevin Buzzard (Mar 04 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton instances/near/123268915):
That's right but these are different things

#### [Kevin Buzzard (Mar 04 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton instances/near/123268916):
There's my normal course for 220 first years

#### [Kevin Buzzard (Mar 04 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton instances/near/123268917):
there is xena

#### [Kevin Buzzard (Mar 04 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton instances/near/123268919):
there is an undergraduate conference

#### [Kevin Buzzard (Mar 04 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton instances/near/123268958):
I am also teaching a graduate course

#### [Kevin Buzzard (Mar 04 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton instances/near/123268966):
oh golly

#### [Kevin Buzzard (Mar 04 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton instances/near/123268967):
he pushed them to mine

#### [Patrick Massot (Mar 04 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton instances/near/123269006):
yes

#### [Kevin Buzzard (Mar 04 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton instances/near/123269009):
OK I merged.

#### [Kevin Buzzard (Mar 04 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton instances/near/123269010):
Should I just push to mathlib?

#### [Patrick Massot (Mar 04 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton instances/near/123269067):
Nah

#### [Patrick Massot (Mar 04 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton instances/near/123269072):
You should do something to my pending review

#### [Patrick Massot (Mar 04 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton instances/near/123269079):
Otherwise Chris cannot see it

#### [Kevin Buzzard (Mar 04 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton instances/near/123269135):
I can't figure out how to do that

#### [Patrick Massot (Mar 04 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton instances/near/123269140):
Hum, maybe the fact that you merged is not helping here

#### [Patrick Massot (Mar 04 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton instances/near/123269189):
Or maybe it's my fault

#### [Patrick Massot (Mar 04 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton instances/near/123269192):
yes it was

#### [Patrick Massot (Mar 04 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton instances/near/123269198):
I forgot to hit some button to submit my review

#### [Patrick Massot (Mar 04 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton instances/near/123269199):
It should be visible now

#### [Patrick Massot (Mar 04 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton instances/near/123269200):
@**Chris Hughes** could you have a look at https://github.com/kbuzzard/mathlib/pull/1/ ?

#### [Kevin Buzzard (Mar 04 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton instances/near/123269241):
OK I can now see it

#### [Scott Morrison (Mar 04 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subsingleton instances/near/123271415):
@**Patrick Massot** they are getting a PR ready. We met on Friday to discuss, and I'm now travelling all this week (actually doing some maths...), so I'm not sure when it will happen.

I think his plan is to send an initial PR covering subgroups, normal subgroups, centers, and kernels, and then a second PR with quotient groups and the first isomorphism theorem.

