---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/88815simplicialcomplexesinlean.html
---

## Stream: [maths](index.html)
### Topic: [simplicial complexes in lean](88815simplicialcomplexesinlean.html)

---

#### [Johan Commelin (May 28 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127203178):
Now we have simplicial complexes!

#### [Johan Commelin (May 28 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127203179):
And also the singular complex

#### [Johan Commelin (May 28 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127203191):
With coefficients in arbitrary `\Z`-modules

#### [Johan Commelin (May 28 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127203237):
See https://github.com/jcommelin/mathlib/tree/simplicial

#### [Patrick Massot (May 28 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127203238):
A less magical solution:
```lean
lemma simplicial_identity₁ {X : simplicial_set} {n : ℕ} (i j : [n + 1]) (H : i ≤ j) :
(@δ X n) i ∘ δ j.succ = δ j ∘ δ i.raise :=
begin
  unfold δ,
  rw comp,
  rw comp,
  congr' 1, 
  exact simplex_category.simplicial_identity₁ _ _ H
end
```

#### [Johan Commelin (May 28 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127203241):
Aaah, so `congr'` is what I was waiting for...

#### [Johan Commelin (May 28 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127203244):
I have no idea what that does...

#### [Patrick Massot (May 28 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127203250):
Uses congruence exactly once

#### [Patrick Massot (May 28 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127203254):
congruence is something we wouldn't bother to state

#### [Johan Commelin (May 28 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127203256):
Alas, we don't have singular homology yet. Because there are no quotient groups... only quotient modules...

#### [Patrick Massot (May 28 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127203257):
x = y implies f(x) = f(y)

#### [Johan Commelin (May 28 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127203301):
And although we take coeffients in `\Z`-modules, we get a complex of `add_comm_group`s

#### [Johan Commelin (May 28 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127203311):
Because `finsupp` gives me `add_comm_group`, and because `is_linear_map` drove me crazy...

#### [Patrick Massot (May 28 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127203317):
Small tip: `i` and `j` should be implicit arguments because they can be inferred from `H`

#### [Johan Commelin (May 28 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127203320):
Ok, fair enough

#### [Patrick Massot (May 28 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127203321):
And this is what I did in my `simplex_category.simplicial_identity₁ _ _ H`

#### [Johan Commelin (May 28 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127203364):
So, now begins the ugly part...

#### [Johan Commelin (May 28 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127203365):
cleaning up the proof

#### [Patrick Massot (May 28 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127203429):
https://github.com/jcommelin/mathlib/blob/06469f0cd7c502ec64b31ba5e6211e937a00b0e1/algebraic_topology/simplicial_set.lean#L49 certainly looks like it could use some cleaning

#### [Johan Commelin (May 28 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127204820):
I cleaned up that line

#### [Johan Commelin (May 28 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127204821):
I also added some user comments to the definitions

#### [Johan Commelin (May 28 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127204822):
https://github.com/leanprover/mathlib/pull/144

#### [Patrick Massot (May 28 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127209260):
https://gist.github.com/PatrickMassot/ef4d356b2c42e469a94f392d61cf173b

#### [Patrick Massot (May 28 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127209274):
@**Johan Commelin**  I went through your file, with random local edits

#### [Patrick Massot (May 28 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127209277):
I stopped when I went below 150 lines

#### [Patrick Massot (May 28 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127209281):
I hope you can learn stuff from the diff

#### [Patrick Massot (May 28 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127209285):
But keep in mind these are only local edits

#### [Johan Commelin (May 28 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127209326):
Thanks! I'm looking at it!

#### [Patrick Massot (May 28 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127209332):
You certainly need some global thinking to get useful lemmas replacing parts of this gigantic proof

#### [Patrick Massot (May 28 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127209344):
and using `calc` would almost certainly make a more readable proof

#### [Patrick Massot (May 28 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127209719):
One last edit spotted because VScode showed me a large area without blue marking: after line 75 of my version `simpa using nat.succ_le_succ (mem_filter.mp hp).2` closes the goal

#### [Johan Commelin (May 28 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127213378):
So what is the best way to get some intuition for when to try the `finish` magic? Or should I just always try it?

#### [Kenny Lau (May 28 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127213387):
don't use it :P

#### [Patrick Massot (May 28 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127213438):
Reading the doc is a good start

#### [Johan Commelin (May 28 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127213549):
Oooh, and thanks a lot for shaving of 80 lines!

#### [Patrick Massot (May 28 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127213663):
Again, you can certainly shave much more, but I hope you can still learn something from this diff

#### [Kevin Buzzard (May 28 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127222299):
Johan I have had my mind on other things today and have only just noticed this -- well done! Want to try perfectoid spaces now? :-)

#### [Johan Commelin (May 29 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127237060):
@**Kevin Buzzard** Well, I'm not so sure what the best way forward is. (1) I need to do some paper writing on non-formal maths. (2) I would love to formalise something cool (like perfectoid spaces), but I will need a lot of help. (3) There is still a lot of scaffolding missing. `module.lean` needs some love, I would like to do finitely generated groups/modules/algebras/fields. Then we can do number fields, rings of integers. Define etale morphisms of schemes. Galois theory... the list goes on and on.

#### [Johan Commelin (May 29 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127237062):
So, concerning (3). Your plan is to train an army of students  to do this for us.

#### [Kevin Buzzard (May 29 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127241755):
Yes, I also do not know what the best way forward is. Here are some things that need doing.

#### [Kevin Buzzard (May 29 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127241788):
1) I should look at your code and review it

#### [Kevin Buzzard (May 29 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127241793):
2) Someone should look at my schemes code and review it

#### [Kevin Buzzard (May 29 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127241798):
3) A group of people should define a perfectoid space before 1st August

#### [Kevin Buzzard (May 29 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127241800):
I am unclear about how important it is to put those things in an appropriate order

#### [Johan Commelin (May 29 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127241826):
```quote
2) Someone should look at my schemes code and review it
```
I could try to be that someone. But I guess that doesn't help. I can't give much feedback on the Lean... and I'm quite sure that the maths is fine (-; After all, Lean thinks its fine. So I definitely want to review it. But I guess the only one gaining something from that is myself.

#### [Johan Commelin (May 29 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127241875):
1) is not very important. That can wait.

#### [Johan Commelin (May 29 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127241902):
Sounds like Assia wants to look at your scheme code as well.

#### [Johan Commelin (May 29 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127242065):
Ok, Kevin, I've attended a seminar on perfectoid spaces. And I have seen some talks on them (including one by you). Do you think the complexity of the definition is much beyond that of schemes? To me it seems like you need to prove some stuff on power-bounded elements and such, and otherwise you just run the "sheaf of rings on a space" machinery, with a different model of affines.

#### [Johan Commelin (May 29 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127242071):
But of course that is hopelessly naive. Both math-wise and lean-wise, I guess.

#### [Kevin Buzzard (May 29 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127242099):
No, I think defining a perfectoid space will be easy

#### [Kevin Buzzard (May 29 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127242102):
that's why I'm so keen to do it

#### [Kevin Buzzard (May 29 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127242104):
I can see no obstruction

#### [Kevin Buzzard (May 29 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127242110):
and if we find an obstruction

#### [Kevin Buzzard (May 29 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127242145):
then we learn more about whether Lean is an appropriate place to do interesting mathematics

#### [Kevin Buzzard (May 29 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127242148):
but if we find an obstruction

#### [Kevin Buzzard (May 29 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127242153):
I am optimistic the CS guys will fix it

#### [Kevin Buzzard (May 29 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127242155):
because look at my horrible pre_semi_sheaf question

#### [Kevin Buzzard (May 29 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127242156):
those goals looked awful

#### [Kevin Buzzard (May 29 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127242157):
and they fixed it

#### [Johan Commelin (May 29 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127242177):
Ok... do you want to do it in a separate project? Or in a feature branch of mathlib?

#### [Johan Commelin (May 29 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127242302):
```quote
because look at my horrible pre_semi_sheaf question
those goals looked awful
and they fixed it
```
Yes, that was fantastic.

#### [Sean Leather (May 29 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127242305):
```quote
Ok... do you want to do it in a separate project? Or in a feature branch of mathlib?
```
I recommend not starting from a fork of mathlib. Your compile times will generally be faster. You can always add it to mathlib later.

#### [Johan Commelin (May 29 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127242353):
Ok, I developed simplicial sets in a feature branch. And I was quite happy.

#### [Johan Commelin (May 29 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127242365):
The positive side is that it is very easy to make small improvements to mathlib when you need them.

#### [Johan Commelin (May 29 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127242369):
For example, I made small changes to `fin` and later added `nnreal`, and I got those merged before my current PR.

#### [Sean Leather (May 29 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127242416):
I've done both, and I was happier not starting from mathlib. :smile:

#### [Sean Leather (May 29 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127242432):
I just add files to the same directory as mathlib that I intend to place them. It's just as easy.

#### [Kevin Buzzard (May 29 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127264180):
Oh that's a nice idea

#### [Kevin Buzzard (May 29 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127264181):
I was just mulling over this sort of thing myself.

#### [Scott Morrison (May 30 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127279311):
I think an advantage of working in a feature branch of mathlib is that it keeps at the front of your mind that it's important that new work is eventually merged into mathlib.

#### [Scott Morrison (May 30 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127279353):
(Otherwise, the work is lost. Of course, indirect consequences of the work, such as inspiring people to think about interactive theorem proving through talks, may survive.)

#### [Scott Morrison (May 30 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127279366):
Not that I am doing this myself. But as soon as I have satisfactory resolution of handling universes in category theory (getting there?), next up should be a PR. :-)

#### [Kevin Buzzard (May 30 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127279720):
Johan Commelin suggests that I wait for you before defining more sheaves of things

#### [Kevin Buzzard (May 30 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127279722):
and perfectoid spaces have sheaves of topological rings...

#### [Johan Commelin (May 30 2018 at 05:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127286907):
But Johan Commelin is a layman, who doesn't know anything about proper writing of structures and interfaces. I guess he thinks you just use some abstract category theory imported from Scott's library, and then definitions become 1-liners. But he forgets that you will still need a lot of interface writing. And this interface writing may or may not become more complicated with the overhead of the category lib. Johan has no clue whether this is a good idea or not.

#### [Scott Morrison (May 30 2018 at 05:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127287077):
I'm really sorry about being slow. I am feeling lame about not finishing real papers recently, and trying to get some non-Lean work done. Given the perfectoid spaces project is not immediately planning on contributing to mathlib (tsk) perhaps I could give you a relatively stable version of my category theory library to use as a dependency, and once (I mustn't say "if") I get it PR'd into mathlib it should be relatively easy to replumb.

#### [Johan Commelin (May 30 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127287092):
No worries. We all have other obligations as well (-;

#### [Johan Commelin (May 30 2018 at 05:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127287147):
The thing is: I really am a layman. I have no clue whether you lib will allow us to write shorter code. Or whether we still need to write lots of plumbing stuff. I just don't have enough experience with formalisations to have good intuition about this.

#### [Johan Commelin (May 30 2018 at 05:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127287164):
In maths you would say: "Look, Scott has written a book on category theory! Let's just refer to that, instead of writing a 50 page appendix ourselves. That will save us 50 pages!"

#### [Johan Commelin (May 30 2018 at 05:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127287166):
But it seems like it might not work that way in Lean.

#### [Patrick Massot (May 30 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/127293960):
```quote
 Of course, indirect consequences of the work, such as inspiring people to think about interactive theorem proving through talks, may survive.
```
Did you already gave talks about interactive theorem proving?

#### [Johan Commelin (Nov 22 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148191703):
I tried to update my `simplicial` branch today: https://github.com/leanprover-community/mathlib/blob/simplicial/algebraic_topology/simplicial_set.lean#L188 is the proof that `boundary (boundary x) = 0`.

#### [Johan Commelin (Nov 22 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148191759):
I do have some issues with `pmf.map f` where `f` is a function between two fintypes. This should be continuous for the subspace topology. And I had a working proof. But in the last months, the topology on `nnreal` has changed, using uniform spaces. Now my proof seems pretty broken.

#### [Johan Commelin (Nov 22 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148191764):
If any of the uniform spaces wizards want to help me out there, that would be cool.

#### [Johan Commelin (Nov 22 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148192272):
@**Reid Barton** I think that I would like to make use of all the machinery that you have developed in you homotopy repo. So I won't push this much further. At least now the files are somewhat up to date with mathlib again.

#### [Johan Commelin (Nov 22 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148193784):
@**Mario Carneiro** So now I have a proof that
```lean
lemma lboundary_lboundary : (lboundary R M X n).comp (lboundary R M X (n+1)) = 0 :=
ext $ λ x, boundary_boundary _ _ _ _
```
Is there now an easy way to take homology? What is the *correct* way to do that?

#### [Reid Barton (Nov 22 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148193785):
Which machinery did you have in mind?

#### [Johan Commelin (Nov 22 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148193787):
Aah, the stuff about cylinders etc

#### [Reid Barton (Nov 22 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148193788):
Can we do a version for simplicial modules now?

#### [Johan Commelin (Nov 22 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148193798):
I do not have a working functor `Top` to `simplicial_set` yet. It is a bit annoying.

#### [Johan Commelin (Nov 22 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148193800):
But the other pieces are now becoming quite nice.

#### [Johan Commelin (Nov 22 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148193859):
Also, I guess I should call them simplicial types? And the category should be `sType`?

#### [Reid Barton (Nov 22 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148193863):
That is--this argument also works to show that the (unnormalized) chain complex associated to any simplicial module is in fact a chain complex. The original simplicial module doesn't have to be free.

#### [Reid Barton (Nov 22 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148193867):
I don't know whether that will make the proof any easier

#### [Reid Barton (Nov 22 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148193881):
https://ncatlab.org/nlab/show/Moore+complex#ForSimplicialAbelianGroups

#### [Johan Commelin (Nov 22 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148193886):
Aaah, I don't know anything about this.

#### [Johan Commelin (Nov 22 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148193928):
Are you planning to PR parts of your project into mathlib in the near future?

#### [Reid Barton (Nov 22 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148193942):
Probably not the near future. It's more likely that I will do a "version 2.0" of some parts in the less near future.

#### [Johan Commelin (Nov 22 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148193944):
Aha

#### [Reid Barton (Nov 22 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148193947):
But, it depends on the part. Some stuff about Top could probably be PRed relatively soon without many changes

#### [Reid Barton (Nov 22 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148193954):
Let me see if I can read your proof

#### [Johan Commelin (Nov 22 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148193955):
It would be nice to have singular homology

#### [Reid Barton (Nov 22 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194000):
I wrote out a plan for it in a comment on one of your earlier PRs

#### [Reid Barton (Nov 22 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194014):
what's the story with the topological simplices functor?

#### [Reid Barton (Nov 22 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194017):
Delta -> Top

#### [Reid Barton (Nov 22 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194021):
Something broke with it?

#### [Johan Commelin (Nov 22 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194023):
https://github.com/leanprover/mathlib/pull/144#issuecomment-425715546

#### [Johan Commelin (Nov 22 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194028):
Yes, that's broken...

#### [Johan Commelin (Nov 22 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194081):
And I didn't see an obvious fix. The topology on `pmf [n]` is now no longer a subspace topology of a Pi-topology. But a subspace of some uniform thing.

#### [Johan Commelin (Nov 22 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194086):
And my uniform-fu is nil.

#### [Reid Barton (Nov 22 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194092):
Technically we can do all this right now I think, without even waiting for limits or adjunctions

#### [Johan Commelin (Nov 22 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194140):
Yes, apart from this stupid brokenness, all the other parts are mostly there.

#### [Johan Commelin (Nov 22 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194145):
I didn't abstract complexes yet.

#### [Johan Commelin (Nov 22 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194275):
Did you do complexes somewhere?

#### [Johan Commelin (Nov 22 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194277):
I know that we had some discussion here on zulip a long time ago.

#### [Reid Barton (Nov 22 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194280):
Not yet

#### [Johan Commelin (Nov 22 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194348):
@**Patrick Massot** Are you interested in exercising your mastery of uniform spaces again?

#### [Patrick Massot (Nov 22 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194403):
I can try

#### [Patrick Massot (Nov 22 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194411):
Did you already precisely described the problem? I didn't read carefully

#### [Patrick Massot (Nov 22 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194455):
Is there something I could clone?

#### [Johan Commelin (Nov 22 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194458):
Nope, there is a broken proof. It used to work, long ago. But then uniform spaces came along, and now it is broken.

#### [Johan Commelin (Nov 22 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194460):
`simplicial` branch on community mathlib

#### [Patrick Massot (Nov 22 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194462):
did you push everything relevant to that branch?

#### [Johan Commelin (Nov 22 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194471):
https://github.com/leanprover-community/mathlib/blob/simplicial/algebraic_topology/standard_topological_simplex.lean#L31

#### [Johan Commelin (Nov 22 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194473):
That might not be the exact statement that you want to prove...

#### [Johan Commelin (Nov 22 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194475):
You could generalise to any `f : X → Y` where `X` and `Y` are fintypes.

#### [Johan Commelin (Nov 22 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194512):
you get an induced map `pmf.map f`

#### [Johan Commelin (Nov 22 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194519):
And that should be continuous

#### [Johan Commelin (Nov 22 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148194530):
We will then apply this to monotone maps between `[n]` and `[m]`

#### [Patrick Massot (Nov 22 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148196152):
@**Johan Commelin** I investigate a bit. There isn't much uniform space here, only metric space. The seemingly missing lemma is:
```lean
lemma metric_pi_topology {α : Type*} {π : α → Type*} [fintype α] [∀ a, metric_space (π a)]: 
  (@metric_space_pi _ π _ _).to_uniform_space.to_topological_space = @Pi.topological_space _ π _ :=
sorry
```

#### [Patrick Massot (Nov 22 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148196155):
Which says the topology on a finite product of metric spaces is the product topology. It probably used to be rfl but isn't.

#### [Patrick Massot (Nov 22 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148196167):
After proving that lemma, typing:
```lean
variables {α : Type*} {β : Type*} [fintype α] [fintype β]

def pmf_top : topological_space (pmf α) := subtype.topological_space
local attribute [instance] pmf_top
lemma map.cont  (f : α → β) :
  continuous (pmf.map f) :=
begin
  apply continuous_subtype_mk,
  rw metric_pi_topology,
  apply continuous_pi,
  intro j,
  sorry
end
```
should put you back on track

#### [Patrick Massot (Nov 22 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148196212):
because then `theorem map.continuous (f : [m] → [n]) : continuous (map f) := map.cont f`

#### [Patrick Massot (Nov 22 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148196266):
It may be better to state a `continuous_metric_pi` with proof containing the `rw metric_pi_topology` which we'd rather keep hidden

#### [Patrick Massot (Nov 22 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148196287):
Clearly the definition `metric_space_pi` currently lacks proper API. @**Sebastien Gouezel** and @**Johannes Hölzl** do you have opinons about that (you don't need to read anything before this monologue)?

#### [Reid Barton (Nov 23 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148201901):
@**Johan Commelin** I pushed an "exercise" for you, in https://github.com/leanprover-community/mathlib/blob/simplicial/algebraic_topology/simplicial_module.lean

#### [Reid Barton (Nov 23 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148201905):
It should be a proper subset of your existing `boundary_boundary` proof, I hope.

#### [Johan Commelin (Nov 23 2018 at 06:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148209235):
@**Patrick Massot** Thanks a lot for investigating. I'll connect the pieces together now.

#### [Johan Commelin (Nov 23 2018 at 06:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148209238):
@**Reid Barton** Thanks! I'll take a look.

#### [Patrick Massot (Nov 23 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148214146):
Johan, are you working on this product topology vs product metric? Or do you need help?

#### [Johan Commelin (Nov 23 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148214147):
I just finished some bureaucracy. I'll look at it now

#### [Patrick Massot (Nov 23 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148214150):
It probably requires quite a bit of preparation if you want to do it right

#### [Patrick Massot (Nov 23 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148214190):
including figuring out what is already in mathlib

#### [Patrick Massot (Nov 23 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148214196):
stuff like the base of the product topology in terms of open subsets in the factors, maybe some congr lemma for topologies, balls in the product metric space is products of balls etc.

#### [Patrick Massot (Nov 23 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148214208):
maybe also things like projection on factors is an open map

#### [Johan Commelin (Nov 23 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148214276):
@**Patrick Massot** Why do your fintypes have such strange names? Did you give up on `X` and `Y`?

#### [Patrick Massot (Nov 23 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148214345):
I copied and pasted too much. The idea of using π in `{π : α → Type*} [fintype α] [∀ a, metric_space (π a)]` is also a nightmare, since there are Pi-type mixed with π map everywhere then

#### [Johan Commelin (Nov 23 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148215270):
@**Patrick Massot** Ok, my proof works again, modulo the lemma. It is a bit scary (in the sense of *unmathematical*) to do rewrites that don't change the pretty printed goal. But I guess it is fine.

#### [Patrick Massot (Nov 23 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148215286):
Which lemma? `metric_pi_topology`?

#### [Johan Commelin (Nov 23 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148215369):
Right, that one.

#### [Johan Commelin (Nov 23 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148215412):
I need to dive into mathlib to figure out how to prove that...

#### [Patrick Massot (Nov 23 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148215415):
Do you want me to try proving it?

#### [Patrick Massot (Nov 23 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148215426):
I'd rather have you work on sheaves or that localization API hole

#### [Johan Commelin (Nov 23 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148215517):
Yeah, I should stop again with this project. I needed to do something else than sheaves for a day. But now I should return.

#### [Johan Commelin (Nov 23 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148215526):
@**Reid Barton** How did Lean figure out that your definition of `boundary` is a linear map?! That's really slick!

#### [Johan Commelin (Nov 23 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148215533):
Kudos to @**Mario Carneiro**

#### [Johan Commelin (Nov 23 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148215581):
```lean
def simplicial_module := simplicial_object (RMod R)

section

variables {R} (X : simplicial_module R)

local notation ` [`n`] ` := simplex_category.from_nat n

def boundary (n : ℕ) : X.obj [n+1] ⟶ X.obj [n] :=
sum univ $ λ i : [n+1], gsmul ((-1 : ℤ)^i.val) (X.δ i)
```

#### [Mario Carneiro (Nov 23 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148215584):
I don't know what you are talking about but I'm happy to take credit

#### [Johan Commelin (Nov 23 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148215585):
That's so concise! You'dd almost call it normal math.

#### [Johan Commelin (Nov 23 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148215595):
`boundary` is a map between to modules. And there you have it.

#### [Johan Commelin (Nov 23 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148215603):
The only difference from regular math is pretty printing

#### [Johan Commelin (Nov 23 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148215665):
It's using the fact that `linear_map` is a group. It is really nice that this *Just Works™*

#### [Johan Commelin (Nov 23 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148215829):
@**Mario Carneiro** Did you also prove that composition of linear maps is bilinear?

#### [Mario Carneiro (Nov 23 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148215832):
yeah, that's `lcomp` or `llcomp`

#### [Johan Commelin (Nov 23 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148215833):
Otherwise that would be a natural step in @**Reid Barton**s challenge.

#### [Johan Commelin (Nov 23 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148215838):
Ok, cool.

#### [Mario Carneiro (Nov 23 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148215879):
llcomp is linear in all the ways

#### [Reid Barton (Nov 23 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148232028):
btw, ` : ℤ` isn't necessary there

#### [Reid Barton (Nov 23 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148232113):
And yes, I was pretty happy about how easy it was to write down this statement. Now let's see how the proof turns out :)

#### [Johan Commelin (Nov 23 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148233797):
Yes, I think that we need to change the definition of composition to `llcomp g f`. After that, there is `map_sum` for `linear_map`s. If that works, I think we are good to go. I'll try it when I'm home.

#### [Johan Commelin (Nov 23 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148236827):
@**Reid Barton** Sadly, this gives a failure
```lean
instance RMod_category : category (RMod R) :=
{ hom := λ M N, M →ₗ N,
  id := λ M, linear_map.id,
  comp := λ M N P f g, linear_map.llcomp M N P g f }
```
Once again, Lean can not find the ring over which `M` is a module...

#### [Reid Barton (Nov 23 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148236903):
I'm confused, why are you trying to use `llcomp`?

#### [Johan Commelin (Nov 23 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237005):
Because then I can pull `sum` through the linear map that is composition.

#### [Reid Barton (Nov 23 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237097):
I see. So in the level of generality that I picked (RMod for a not necessarily commutative ring), the homs are only abelian groups, not modules. Of course, this is still enough but we have to use this additivity somehow

#### [Johan Commelin (Nov 23 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237106):
Aah, yes, I changed `R` to `comm_ring`, but that is not the problem I think.

#### [Johan Commelin (Nov 23 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237115):
It is still maxing out on some typeclass search

#### [Reid Barton (Nov 23 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237119):
Well, there is no reason it should not work for `ring` as well, or any additive category even

#### [Johan Commelin (Nov 23 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237192):
Sure, but we don't have enriched categories etc

#### [Reid Barton (Nov 23 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237198):
what about just proving the equality element-wise?

#### [Reid Barton (Nov 23 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237205):
Well, in any case, `comp` cannot be `llcomp`, because it has the wrong type. Right?

#### [Johan Commelin (Nov 23 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237219):
`llcomp g f` should be an element of `linear_map M P`

#### [Reid Barton (Nov 23 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237276):
Or, sorry

#### [Johan Commelin (Nov 23 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237279):
because `llcomp` is cast to a function that eats `g`, etc...

#### [Reid Barton (Nov 23 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237284):
So how can `llcomp` help

#### [Johan Commelin (Nov 23 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237297):
`llcomp boundary` is a linear map

#### [Reid Barton (Nov 23 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237322):
is the idea to get an expression containing a coercion of `llcomp`, so that some lemma can see it's linear?

#### [Reid Barton (Nov 23 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237392):
This sounds kind of fragile to me

#### [Johan Commelin (Nov 23 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237410):
why?

#### [Reid Barton (Nov 23 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237429):
It just does?

#### [Reid Barton (Nov 23 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237431):
Easy to imagine the simplifier deciding to rewrite `llcomp f g` to `lcomp f g` or whatever

#### [Reid Barton (Nov 23 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237433):
and then you're stuck

#### [Johan Commelin (Nov 23 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237488):
That would be `lcomp g f` because of [see above]

#### [Johan Commelin (Nov 23 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237490):
Anyway, I'm sidetracking.

#### [Johan Commelin (Nov 23 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237499):
Ok, I'll just `change` to the `llcomp` expression inside my proof.

#### [Reid Barton (Nov 23 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237843):
What lemma are you using to pull the sum through the composition?

#### [Johan Commelin (Nov 23 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237918):
`algebra/module.lean:@[simp] lemma map_sum`

#### [Johan Commelin (Nov 23 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237921):
That was my plan, at least.

#### [Reid Barton (Nov 23 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237987):
I see

#### [Reid Barton (Nov 23 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148237989):
hmm

#### [Reid Barton (Nov 23 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148238375):
Maybe it's better to make lemmas like `sum_comp`/`comp_sum` phrased in terms of the category composition and then write the proof in terms of those

#### [Johan Commelin (Nov 23 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148243762):
```lean
set_option class.instance_max_depth 100
```
I found this at the top of the `tensor_product` file. That was why the `llcomp` stuff wasn't working (@**Reid Barton**)
Seems a bit fragile indeed...

#### [Johan Commelin (Nov 23 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148244765):
@**Reid Barton** I just pushed some stuff. I can indeed copy most of my previous proof. I need one more little simp-lemma near the end. But I now need to do some other stuff first...

#### [Johan Commelin (Nov 23 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148248147):
@**Reid Barton** Done.

#### [Reid Barton (Nov 23 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148248153):
I just did it too :)

#### [Johan Commelin (Nov 23 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148248159):
Ooh, sorry...

#### [Johan Commelin (Nov 23 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148248162):
Are our proofs homotopic?

#### [Johan Commelin (Nov 23 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148248163):
Oooh, wait... this isn't HoTT

#### [Reid Barton (Nov 23 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148248232):
They're pretty similar

#### [Reid Barton (Nov 23 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148248350):
I added a bunch of lemmas for bilinearity of composition (without proofs)
https://github.com/leanprover-community/mathlib/blob/simplicial2/category_theory/examples/modules.lean#L35

#### [Johan Commelin (Nov 23 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148248469):
Ok, now I should really get back to sheaves

#### [Johan Commelin (Nov 23 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simplicial%20complexes%20in%20lean/near/148248476):
But I'm a bit stuck there...

