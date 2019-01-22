---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/94921teachinguseofquotientsinLean.html
---

## [maths](index.html)
### [teaching use of quotients in Lean](94921teachinguseofquotientsinLean.html)

#### [Kevin Buzzard (Aug 09 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131184986):
I once found it hard to use quotients in Lean. I typically wanted to use quotients to define mathematical objects (like quotient rings) and the example (unordered pairs) in TPIL was a bit CSish for me. The first time I needed them was for localisation of rings and Kenny wrote everything for me. But I needed them more and more, and eventually I had to learn how they worked. I wrote code for the integers mod n, but at the time I didn't understand the type class inference system very well either, and the code was not great. @**Luca Gerolla** needs to work with quotients for his work on the fundamental group and it occurred to me that I should revisit the work and tidy it up. One problem with integers mod n which I think could confuse beginners was a problem discussed here once, namely that it's hard to use type classes to put the equivalence relation of being congruent mod n onto Z, because that's one equivalence relation per n, and type class inference would rather there just be one equivalence relation on a type. The fix suggested to me at the time was to use a new version of Z for each integer, but having mulled this over for a while I decided that it added another layer of complexity which was unsuitable for the beginner. So I decided to choose everyone (except Johan)'s favourite integer 37, and just construct the integers mod 37 instead.

I jump from tactic mode proofs to half-tactic half-term to full term mode proofs, depending on whether I'm trying to demonstrate something for the first time or just get things done. This code is supposed to be readable by learners who know a bit about Lean and are interested in decyphering all the `quotient.induction_on\2` stuff and want to see a relatively simple example. The code is here:

https://github.com/kbuzzard/xena/blob/master/xenalib/m1f/zmod37.lean

#### [Patrick Massot (Aug 09 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131185870):
Why do you define a setoid instance instead of having a def?

#### [Mario Carneiro (Aug 09 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186089):
I'm not seeing why 37 is better than n

#### [Kevin Buzzard (Aug 09 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186102):
I want to give the same answer to both questions -- so I can use type class inference

#### [Kevin Buzzard (Aug 09 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186108):
I wanted access to the \[[ notation etc

#### [Mario Carneiro (Aug 09 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186114):
make a notation for that

#### [Kevin Buzzard (Aug 09 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186129):
I didn't want to make it harder. I wanted to show Luca how to do it

#### [Kevin Buzzard (Aug 09 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186132):
That's the actual answer.

#### [Kevin Buzzard (Aug 09 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186147):
I want *him* to use type class inference

#### [Mario Carneiro (Aug 09 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186235):
I think `setoid` is one of the more poorly thought out typeclasses

#### [Chris Hughes (Aug 09 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186259):
Are we still going to be stuck with those things in lean4?

#### [Mario Carneiro (Aug 09 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186284):
no idea

#### [Mario Carneiro (Aug 09 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186302):
I think it should be called `has_equiv` and be tied to the `\approx` notation, but the `\[[` notation should be inferred by unification

#### [Kenny Lau (Aug 09 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186335):
in lean4 we wouldn't have to worry about + and * being different things right

#### [Mario Carneiro (Aug 09 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186342):
that's a bit vague

#### [Chris Hughes (Aug 09 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186375):
I think the idea is that we won't have both `add_group` and `group`

#### [Mario Carneiro (Aug 09 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186403):
we won't have either

#### [Kevin Buzzard (Aug 09 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186410):
```quote
I think `setoid` is one of the more poorly thought out typeclasses
```
Sure, but I am teaching Lean 3.4.1 so I went with it.

#### [Mario Carneiro (Aug 09 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186413):
presumably that's moving to mathlib

#### [Kevin Buzzard (Aug 09 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186424):
we could have `heartsuit_group`

#### [Kevin Buzzard (Aug 09 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186431):
the possibilities are endless

#### [Mario Carneiro (Aug 09 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186432):
my point is that it's not a great example if you are teaching typeclasses

#### [Kevin Buzzard (Aug 09 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186593):
I'm not teaching typeclasses, I'm teaching Luca how to work with the quotient of the paths from x to x by the is_homotopic relation which he's shown is an equivalence relation. He now has to define a group structure on the quotient, and I looked at his code, and he defined the group law by using `quotient.out` to choose two random lifts, composed the paths, and went back down again. He was not using type class inference either, so it was `@quotient.out [insert proof of equiv reln here]` I needed to show him how to do it properly. I agree that the file doesn't do everything, but hopefully it does what it needs to do.

#### [Kevin Buzzard (Aug 09 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186610):
It is also the file I wished I had when I was trying to figure out how to use quotients for the first time.

#### [Mario Carneiro (Aug 09 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186629):
maybe it should be

#### [Mario Carneiro (Aug 09 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186646):
rather than showing people Z/37Z, show them the fundamental group

#### [Mario Carneiro (Aug 09 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186686):
it's surely more interesting for students with more mathematical sophistication

#### [Mario Carneiro (Aug 09 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186824):
then prove the fundamental group of the circle is Z and PR it :D

#### [Kevin Buzzard (Aug 09 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186893):
```quote
then prove the fundamental group of the circle is Z and PR it :D
```
You mean do an _example_???

#### [Kevin Buzzard (Aug 09 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186908):
Oh, is this just a way of proving that the definition is correct?

#### [Kevin Buzzard (Aug 09 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186946):
The proof of pi_1(S^1)=Z I know involves constructing going via a triangulation and using some simplicial approximation theorem stuff

#### [Kevin Buzzard (Aug 09 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186973):
it would not surprise me if there were a cute proof though

#### [Mario Carneiro (Aug 09 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186997):
that is not what I expected

#### [Mario Carneiro (Aug 09 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187011):
the proof I know uses covering maps and winding numbers

#### [Johan Commelin (Aug 09 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187038):
`S^1 = real/int`, and `real` is contractible. So `int` is the fundamental group.

#### [Johan Commelin (Aug 09 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187047):
Now, how do we explain that to Lean?

#### [Mario Carneiro (Aug 09 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187054):
wait what

#### [Mario Carneiro (Aug 09 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187098):
how does that last step work?

#### [Johan Commelin (Aug 09 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187132):
I guess you need to know that `S^1` is a *nice* space...

#### [Mario Carneiro (Aug 09 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187146):
I believe the first line, that's not hard to prove

#### [Johan Commelin (Aug 09 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187147):
Where *nice* means locally compact and t2, or something similar.

#### [Mario Carneiro (Aug 09 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187170):
and you should get niceness that way

#### [Johan Commelin (Aug 09 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187189):
And then you know that S^1 has a universal covering space, and you get a group structure on the fibre, which is exactly pi_1

#### [Mario Carneiro (Aug 09 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187203):
are you still elucidating your one line proof?

#### [Johan Commelin (Aug 09 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187215):
Yes... I'm sorry.

#### [Mario Carneiro (Aug 09 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187223):
I'm trying to figure out how R is contractible plays into this

#### [Johan Commelin (Aug 09 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187235):
Well, that is supposed to convince you that R is the universal covering space...

#### [Johan Commelin (Aug 09 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187327):
We could prove a general lemma of the form `simply_connected X` implies `pi_1(X/G) = G`

#### [Mario Carneiro (Aug 09 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187337):
oh so that's true in generality?

#### [Johan Commelin (Aug 09 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187345):
If `X` is nice.

#### [Johan Commelin (Aug 09 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187350):
Maybe even in general.

#### [Mario Carneiro (Aug 09 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187354):
G is discrete?

#### [Mario Carneiro (Aug 09 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187413):
i.e. pi_1(X/X) is not X

#### [Johan Commelin (Aug 09 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187429):
True.

#### [Mario Carneiro (Aug 09 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187451):
to make X a covering map you need it to be locally like a quotient by a discrete space

#### [Johan Commelin (Aug 09 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187456):
So there are some conditions. G needs to be discrete (topologically) and act freely on X, and the action must be continuous.

#### [Johan Commelin (Aug 09 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187468):
So `G` is a discrete subgroup of `Aut_Top(X)`.

#### [Mario Carneiro (Aug 09 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187536):
which kind of quotient are we talking about here?

#### [Johan Commelin (Aug 09 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187537):
But I haven't formalised this... so I don't know what I'm talking about.

#### [Johan Commelin (Aug 09 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187557):
X/G as a set, with quotient topology, I think.

#### [Mario Carneiro (Aug 09 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187558):
If X is a topological group and G a discrete subgroup you get the other conditions

#### [Mario Carneiro (Aug 09 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187627):
R/Z as a set is garbage, that just identifies the points of Z in R making it a bouquet of circles

#### [Johan Commelin (Aug 09 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187650):
Aah, sorry. I meant as group action of sets.

#### [Kevin Buzzard (Aug 09 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187660):
this is the quotient of a group acting on a nice top space

#### [Kevin Buzzard (Aug 09 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187664):
so the quotient space is the set of orbits

#### [Kevin Buzzard (Aug 09 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187676):
An example is the quotient of a group by a subgroup

#### [Kevin Buzzard (Aug 09 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187749):
but if $$\Gamma$$ is a subgroup of $$SL(2,\mathbb{Z})$$ with no torsion (e.g. the elements congruent to the identity modulo $$N$$ for any $$N>=3$$) then $$\Gamma$$ acts on the upper half plane (which is nice and contractible) discretely, and the quotient is a non-compact Riemann surface with fundamental group $$\Gamma$$.

#### [Johan Commelin (Aug 09 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187808):
What would the definition of `S^1` be in Lean?

#### [Kevin Buzzard (Aug 09 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187823):
You could certainly define it to be the closed subspace of R^2

#### [Johan Commelin (Aug 09 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187837):
Right, that is maybe a more reasonable definition.

#### [Mario Carneiro (Aug 09 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187839):
that's my thought as well, it's true to the literature and also generalizes to using circles as... circles

#### [Kevin Buzzard (Aug 09 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187840):
and IF WE EVER MANAGED TO GET THE EXPONENTIAL FUNCTION INTO MATHLIB then you could even prove it was R mod Z :-)

#### [Johan Commelin (Aug 09 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187841):
And then identify it with the unit circle in C

#### [Johan Commelin (Aug 09 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187845):
Right.

#### [Kevin Buzzard (Aug 09 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187911):
https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Trivial.20things.20about.20convergent.20power.20series

#### [Johan Commelin (Aug 09 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187915):
Maybe exp should move to the community fork. Who knows if that would move it forward...

#### [Mario Carneiro (Aug 09 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187918):
pff, use rational trig and you don't need exp

#### [Kevin Buzzard (Aug 09 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187926):
:-)

#### [Kevin Buzzard (Aug 09 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187935):
Who needs to be complex when you can just be rational.

#### [Mario Carneiro (Aug 09 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187976):
that's actually a good idea Johan

#### [Kevin Buzzard (Aug 09 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188024):
Or you could just come to the xena project, we use it freely over there :-)

#### [Kevin Buzzard (Aug 09 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188035):
warning: not all code compiles

#### [Mario Carneiro (Aug 09 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188043):
which is why it is a good community fork project

#### [Mario Carneiro (Aug 09 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188061):
you are already using it but the PR needs more work

#### [Mario Carneiro (Aug 09 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188077):
or at least I need to spend more time on it

#### [Kevin Buzzard (Aug 09 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188135):
I don't even know which PR it is any more. Is it in the binomial theorem one or the limits one?

#### [Kevin Buzzard (Aug 09 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188145):
I can't find it in either

#### [Mario Carneiro (Aug 09 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188153):
surely it's not in the binomial theorem

#### [Johan Commelin (Aug 09 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188155):
I think anyone can pull that branch into the community fork, right? (After we found it)

#### [Mario Carneiro (Aug 09 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188163):
yes

#### [Kevin Buzzard (Aug 09 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188178):
I think he needed the binomial theorem to prove exp(x+y)=exp(x)exp(y)

#### [Mario Carneiro (Aug 09 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188188):
I suppose you do

#### [Kevin Buzzard (Aug 09 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188262):
By the way, another random PR we use a lot at Imperial is Chris' zmod work. But I hear you didn't like pos_nat and I believe Chris is now re-doing everything with pnat and prime

#### [Kevin Buzzard (Aug 09 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188285):
I can't find exp. Did he close it?

#### [Kevin Buzzard (Aug 09 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188293):
No wonder it didn't get accepted :-)

#### [Johan Commelin (Aug 09 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188299):
@**Chris Hughes** We need you (-;

#### [Kevin Buzzard (Aug 09 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188322):
he's too busy helping all the other Imperial UGs while I'm on holiday :-)

#### [Mario Carneiro (Aug 09 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188323):
https://github.com/leanprover/mathlib/pull/43

#### [Johan Commelin (Aug 09 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188395):
branch is no longer there.

#### [Johan Commelin (Aug 09 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188398):
So we will need to get the stuff out of Xena.

#### [Kevin Buzzard (Aug 09 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188401):
so it looks like the ball's in Chris' court.

#### [Mario Carneiro (Aug 09 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188402):
no wait it's https://github.com/leanprover/mathlib/pull/41

#### [Mario Carneiro (Aug 09 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188414):
it says it is a PR from `unknown repository`

#### [Kevin Buzzard (Aug 09 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188466):
I'd be quite happy if he were to concentrate on zmod at the minute, we've all found this very helpful. There's a bunch of people doing number theory and group theory, some of whom use it.

#### [Johan Commelin (Aug 09 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188467):
Which means that the repo was deleted from github, I think

#### [Chris Hughes (Aug 09 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188476):
I think I deleted my fork of mathlib at some point when I was frustratedly trying to learn how to use git.

#### [Kevin Buzzard (Aug 09 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188485):
They don't teach mathematicians git :-(

#### [Johan Commelin (Aug 09 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188497):
Chapter 0 in your book is about git, right?

#### [Mario Carneiro (Aug 09 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188499):
I think those files should all be dumped in the community fork, and we can come back to it at some point

#### [Kevin Buzzard (Aug 09 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188500):
I'm not competent to write it

#### [Johan Commelin (Aug 09 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188509):
You could have a foreword by someone else... Mario for example

#### [Mario Carneiro (Aug 09 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188563):
Step 1: git-scm.com, step 2: profit

#### [Andrew Ashworth (Aug 09 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131191018):
Install sourcetree while you're at it

#### [Andrew Ashworth (Aug 09 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131191048):
Nobody has time to remember all the magic git invocations, so a gui wrapper really helps

#### [Patrick Massot (Aug 09 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131197153):
I used to believe that. So I advised computer afraid colleagues to use source tree and, after many rescuing operations, I realized command line is much simpler. Because you don't have to know about all commands and options that are not written in your git cheat sheet.

