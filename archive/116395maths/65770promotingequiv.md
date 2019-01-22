---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/65770promotingequiv.html
---

## [maths](index.html)
### [promoting equiv](65770promotingequiv.html)

#### [Kevin Buzzard (Apr 10 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124877520):
In mathematics, people constantly invoke the idea that an object is "defined up to unique isomorphism".

#### [Kevin Buzzard (Apr 10 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124877560):
I have seen this really full in the face in my work on schemes

#### [Kevin Buzzard (Apr 10 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124877565):
I am defining a certain gadget in algebraic geometry called "the structure sheaf on an affine scheme"

#### [Kevin Buzzard (Apr 10 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124877586):
and in the mathematics literature it typically goes like this: "the open set is of the form $$D(f)$$ (f is an element of a ring) and define the structure sheaf on this set to be $$R[1/f]$$" (this is just some ring)

#### [Kevin Buzzard (Apr 10 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124877624):
and the catch is that the open set can be of the form $$D(g)$$ for other elements $$g$$ of the ring

#### [Kevin Buzzard (Apr 10 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124877627):
but $$R[1/f]$$ and $$R[1/g]$$ are isomorphic

#### [Kevin Buzzard (Apr 10 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124877637):
and moreover there is a unique isomorphism between $$R[1/f]$$ and $$R[1/g]$$ which has some properties, and this is the isomorphism which mathematicians use to hide behind the issue that they have not actually defined the structure sheaf on this open set.

#### [Kevin Buzzard (Apr 10 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124877682):
Now if this isomorphism were an equality, then `eq.rec` would be really helpful

#### [Kevin Buzzard (Apr 10 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124877691):
because I would be able to promote a claim involving $$R[1/f]$$ to a claim involving any $$R[1/g]$$

#### [Kevin Buzzard (Apr 10 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124877697):
But it's not an equality -- $$R[1/f]$$ and $$R[1/g]$$ are most definitely different types

#### [Gabriel Ebner (Apr 10 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124877700):
You can make it into an equality, by taking a quotient on the ring extensions.  Not sure this makes it any simpler, though.

#### [Kevin Buzzard (Apr 10 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124877755):
However there is a special map $$R[1/f]\to R[1/g]$$

#### [Kevin Buzzard (Apr 10 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124877760):
which I can produce

#### [Kevin Buzzard (Apr 10 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124877764):
with an inverse

#### [Kevin Buzzard (Apr 10 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124877771):
and I think what I want is a recursor which enables me to effortlessly change between these rings

#### [Kevin Buzzard (Apr 10 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124877779):
and just push through all the theorems I want

#### [Kevin Buzzard (Apr 10 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124877780):
from theorems about $$R[1/f]$$

#### [Gabriel Ebner (Apr 10 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124877781):
Hmm, do you care about elements of $$R[1/f]$$?

#### [Kevin Buzzard (Apr 10 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124877782):
to theorems about any choice of $$R[1/g]$$.

#### [Kevin Buzzard (Apr 10 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124877786):
I do care about elements of $$R[1/f]$$

#### [Kevin Buzzard (Apr 10 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124877823):
however

#### [Kevin Buzzard (Apr 10 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124877826):
because I am doing maths and not type theory

#### [Kevin Buzzard (Apr 10 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124877827):
there is some sort of implicit understanding

#### [Kevin Buzzard (Apr 10 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124877831):
that any theorem I prove will only depend on my object up to "canonical isomorphism"

#### [Kevin Buzzard (Apr 10 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124877834):
and the map $$R[1/f]\to R[1/g]$$ is a canonical isomorphism

#### [Kevin Buzzard (Apr 10 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124877840):
The word "canonical" does not have a general definition, but in any given case one can supply one

#### [Kevin Buzzard (Apr 10 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124877844):
for example in this case I can supply some technical maths definition of the form "the unique map with some property"

#### [Kevin Buzzard (Apr 10 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124877891):
But I do have maps between products of such rings and want to make claims about sets of elements which go to certain other sets of elements

#### [Kevin Buzzard (Apr 10 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124877897):
And whilst I have not yet embarked upon writing what will be the last proof that I will need for proving that an affine scheme is a scheme

#### [Kevin Buzzard (Apr 10 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124877898):
I have planned the proof

#### [Kevin Buzzard (Apr 10 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124877908):
and I know that at some point I will have to replace $$R[1/f]$$ with $$R[1/g]$$ and instantly I will be hit with 10 proof obligations

#### [Kevin Buzzard (Apr 10 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124877913):
all of which will be of the form "you need to check that the composite of this canonical map with this canonical map is this canonical map"

#### [Kevin Buzzard (Apr 10 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124877914):
I know how to prove all of these things

#### [Kevin Buzzard (Apr 10 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124877954):
but I was idly wondering whether I could set up the infrastructure more cleverly

#### [Kevin Buzzard (Apr 10 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124877958):
because I have just been reading about UniMath

#### [Kevin Buzzard (Apr 10 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124877959):
and I see that equality is not a Prop there

#### [Kevin Buzzard (Apr 10 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124877967):
and indeed equality is much more strongly related to equiv than in DTT

#### [Kevin Buzzard (Apr 10 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124877970):
which made me think that maybe I was missing a trick here.

#### [Kevin Buzzard (Apr 10 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878015):
I think that perhaps the way forward here is to actually write the proof

#### [Kevin Buzzard (Apr 10 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878016):
and when the explosion of obligations occurs

#### [Kevin Buzzard (Apr 10 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878019):
to really think about the simp lemmas I need to kill all of them

#### [Kevin Buzzard (Apr 10 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878020):
(or maybe they won't be valid lemmas for simp)

#### [Kevin Buzzard (Apr 10 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878024):
and then to ask again.

#### [Andrew Ashworth (Apr 10 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878029):
is `transfer` as written for the integers at all helpful? here's the paper from isabelle (https://www21.in.tum.de/~kuncar/documents/huffman-kuncar-cpp2013.pdf)

#### [Johannes Hölzl (Apr 10 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878033):
`transfer` is not only for integers

#### [Andrew Ashworth (Apr 10 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878036):
of course, i only meant in lean that's where you'll find it used

#### [Kevin Buzzard (Apr 10 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878085):
At first glance, this looks like it might be the sort of thing I need

#### [Johannes Hölzl (Apr 10 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878097):
there are still many things are missing. I never continued to work on it, I think with all the subtypes and quotient types we have now it may worth a try

#### [Kevin Buzzard (Apr 10 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878101):
Here is a toy example of the kind of thing I might need

#### [Kevin Buzzard (Apr 10 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878164):
It is ridiculous to continually write $$R[1/f]$$, I may as well write `X f` where `f : R` ($$R$$ is a ring but may as well be a type) and `X : Π (f : R), Type`

#### [Kevin Buzzard (Apr 10 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878215):
There is an equivalence relation on `R`, and if `f` and `g` are equivalent then, in my language, `X f` and `X g` are canonically isomorphic.

#### [Kevin Buzzard (Apr 10 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878225):
This means in practice that if `f` and `g` are equivalent then there is a map `Y f g : X f -> X g`

#### [Kevin Buzzard (Apr 10 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878226):
satisfying `Y f f = id`

#### [Kevin Buzzard (Apr 10 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878261):
and `Y f g` composed with `Y g h` equals `Y f h`

#### [Kevin Buzzard (Apr 10 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878275):
Now I might have maps `X f₁ -> X f₂` and `X f₂ -> X f₃` and a theorem saying that the image of the first map is precisely the preimage of `0` of the second map

#### [Kevin Buzzard (Apr 10 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878277):
(X f is a ring and Y f g sends 0 to 0)

#### [Kevin Buzzard (Apr 10 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878321):
and now I want to know _immediately_ that if `f_1` is equivalent to `g_1` etc

#### [Kevin Buzzard (Apr 10 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878322):
then the image of `X g_1 -> X g_2` equals the preimage of 0 in `X g_2 -> X g_3`

#### [Kevin Buzzard (Apr 10 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878337):
The proof in Lean is a diagram chase

#### [Kevin Buzzard (Apr 10 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878339):
but I have a gazillion of such diagram chases

#### [Kevin Buzzard (Apr 10 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878341):
I want the proof to be a tactic or something

#### [Kevin Buzzard (Apr 10 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878378):
I want the proof to follow from some foundational properties which I do not need to invoke explicitly.

#### [Kevin Buzzard (Apr 10 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878390):
That's what going on in my head as a mathematician

#### [Kevin Buzzard (Apr 10 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878391):
I don't want to have to invoke lemmas from the mathlib set files

#### [Kevin Buzzard (Apr 10 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878395):
I want to say that this is all obvious

#### [Patrick Massot (Apr 10 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878397):
What about using the limit ring?

#### [Kevin Buzzard (Apr 10 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878402):
Yes, the projective limit. I have considered this

#### [Kevin Buzzard (Apr 10 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878405):
But do you think that this is what mathematicians do?

#### [Kevin Buzzard (Apr 10 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878406):
I am not so sure

#### [Patrick Massot (Apr 10 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878409):
This is what they do when then get cornered

#### [Kevin Buzzard (Apr 10 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878410):
I have seen Lean do impressive things

#### [Patrick Massot (Apr 10 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878412):
But not otherwise

#### [Kevin Buzzard (Apr 10 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878413):
automatically

#### [Kevin Buzzard (Apr 10 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878457):
I have seen quite complex goals being solved by refl because I set stuff up right

#### [Kevin Buzzard (Apr 10 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878459):
but this will not be refl because `X f` is not _equal_ to `X g`

#### [Kevin Buzzard (Apr 10 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878471):
Can you see my point Patrick? If `X f_i` were _equal_ to `X g_i` then this [image = kenel] would be refl

#### [Kevin Buzzard (Apr 10 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878484):
and they're not equal, but they're sufficiently equal that everything that I will be doing with them would yield to some analogue of refl

#### [Kevin Buzzard (Apr 10 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878534):
I think that's my point. I have seen the power of `rfl` and I want it more generally

#### [Kevin Buzzard (Apr 10 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878547):
and I don't see why I can't have something like it here

#### [Kevin Buzzard (Apr 10 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878550):
because I must be only using some specific collection of ideas which are invariant under canonical isomorphism

#### [Kevin Buzzard (Apr 10 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878594):
and I would love to just be able to write down these ideas in this specific case and then just get everything for free

#### [Patrick Massot (Apr 10 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878613):
Of course we all want magic for free

#### [Patrick Massot (Apr 10 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878619):
But `rfl` magic is very special. It's meta-theoretic magic

#### [Kevin Buzzard (Apr 10 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878664):
eq.refl is just some constructor

#### [Patrick Massot (Apr 10 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878671):
Definitional (or judgemental) equality is not inside type theory

#### [Scott Morrison (Apr 10 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878681):
(I suspect Kevin wants univalence here, but having read the HoTT book doesn't seem to qualify me to speak coherent sentences about univalence in practice...)

#### [Patrick Massot (Apr 10 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878689):
`eq.refl` is something else

#### [Patrick Massot (Apr 10 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878740):
You could try to write a proof and then see if some tactic could help. But the mathematical way to solve this problems seems to be using the projective limit

#### [Kevin Buzzard (Apr 10 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878742):
It doesn't solve the problem

#### [Patrick Massot (Apr 10 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878743):
The fact that we don't need it in the real world is the power of sloppy maths discussion

#### [Kevin Buzzard (Apr 10 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878744):
does it?

#### [Kevin Buzzard (Apr 10 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878748):
It just moves the work I think

#### [Kevin Buzzard (Apr 10 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878752):
I prove that some image equals some kernel

#### [Kevin Buzzard (Apr 10 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878754):
wait

#### [Kevin Buzzard (Apr 10 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878757):
the theorem I have is that the image equals the kernel in the $$R[1/f]$$ world

#### [Kevin Buzzard (Apr 10 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878800):
I then have to promote this theorem to the projective limit world

#### [Kevin Buzzard (Apr 10 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878801):
so I get some canonical object which depends only on the equivalence class of `f` and is canonically isomorphic to $$R[1/f]$$

#### [Kevin Buzzard (Apr 10 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878806):
`X f`

#### [Kevin Buzzard (Apr 10 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878819):
and now I still have to prove that the image equals the kernel in the projective limit world

#### [Kevin Buzzard (Apr 10 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878875):
the only difference being that before `X g` depended on `g`, known to be in the same equivalence class of `f`, whereas now I have some new object `X-univ [[f]]` which depends only on the equivalence class of `f`

#### [Patrick Massot (Apr 10 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878878):
You need to do the full proof in the limit world

#### [Patrick Massot (Apr 10 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878880):
I guess

#### [Kevin Buzzard (Apr 10 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878881):
that can't happen

#### [Kevin Buzzard (Apr 10 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878885):
the proof only works

#### [Kevin Buzzard (Apr 10 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878888):
in the world where I have one f

#### [Kevin Buzzard (Apr 10 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878889):
because the proof depends on f

#### [Kevin Buzzard (Apr 10 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878890):
The maps don't

#### [Kevin Buzzard (Apr 10 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878891):
but the proof does

#### [Kevin Buzzard (Apr 10 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878892):
the proof of exactness

#### [Patrick Massot (Apr 10 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878894):
What are you proving exactly?

#### [Kevin Buzzard (Apr 10 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878896):
I want to go from this:

#### [Kevin Buzzard (Apr 10 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878938):
https://stacks.math.columbia.edu/tag/00EJ

#### [Kevin Buzzard (Apr 10 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878949):
to the statement that the sheaf axiom holds for finite covers of Spec(R) by basic open sets of the form D(f_i)

#### [Kevin Buzzard (Apr 10 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878957):
and the proof is "those two statements say the same thing"

#### [Kevin Buzzard (Apr 10 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124878976):
just like Chris' lemma the other day which he found hard to prove, which was that sum from 1 to n of f(i) equalled sum from 1 to n of f(i) formalised in a different way

#### [Kevin Buzzard (Apr 10 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124879020):
But the problem is that if $$U$$ is an open set which equals $$D(f)$$ for some $$f$$

#### [Kevin Buzzard (Apr 10 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124879024):
then it is almost certainly equal to $$D(g)$$ for lots of other $$g$$

#### [Kevin Buzzard (Apr 10 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124879033):
and I am not allowed to define the global sections on $$D(f)$$ to be $$R[1/f]$$

#### [Kevin Buzzard (Apr 10 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124879035):
because this involves choosing $$f$$.

#### [Kevin Buzzard (Apr 10 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124879080):
So like you say I can do some projective limit construction over all $$g$$ with $$D(f)=D(g)$$

#### [Kevin Buzzard (Apr 10 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124879084):
[the equivalence relation on $$R$$ is that `f` and `g` are equivalent iff $$D(f)=D(g)$$]

#### [Kevin Buzzard (Apr 10 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124879091):
or I could also do some construction involving inverting all $$g$$ which are non-vanishing on $$U$$

#### [Kevin Buzzard (Apr 10 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124879096):
and either way I get a new ring which is not definitionally equal to $$R[1/f]$$

#### [Kevin Buzzard (Apr 10 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124879099):
but which is uniquely isomorphic to it as $$R$$-algebra

#### [Kevin Buzzard (Apr 10 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124879102):
and now I have to push the diagram chase over

#### [Kevin Buzzard (Apr 10 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124879103):
It's just a little thing

#### [Kevin Buzzard (Apr 10 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124879145):
but I feel like it's some variant of `rfl`

#### [Kevin Buzzard (Apr 10 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124879147):
"you're only chasing around images and kernels of maps, so everything is fine if you replace your rings with isomorphic rings"

#### [Patrick Massot (Apr 10 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124880478):
```quote
"you're only chasing around images and kernels of maps, so everything is fine if you replace your rings with isomorphic rings"
```
I though about this, and I think you are cheating a bit here. You still need the maps in your exact sequence to commute with your canonical isomorphisms. I think you can only hope for automation if you have a really fancy categorical way of defining both your canonical isomorphisms *and* the maps entering the exact sequence. Otherwise you can still define standard open subsets as equivalence classes of $$f$$, the associated system of rings $$R[1/f]$$, and the sheaf on such an open subsets as the limit of this system. And you can have many lemmas about diagrams of rings (or modules), their limits and how to build exact sequences of limits out of exact sequences and commutation relations. Actually this should probably all be provided by @**Scott Morrison**'s category theory lib.

#### [Scott Morrison (Apr 10 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124880767):
(getting there...)

#### [Kevin Buzzard (Apr 10 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124880888):
My maps are also "canonical" in the sense that they are "built from" the unique R-algebra maps between these rings.

#### [Kevin Buzzard (Apr 10 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124880941):
By which I mean the map $$R[1/f]\to R[1/fg]$$ is the unique $$R$$-algebra map, and then everything is put together just from such maps in such a way as to not break anything.

#### [Kevin Buzzard (Apr 10 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/124880951):
Maybe this is going towards telling me exactly which lemmas I need to prove.

#### [Kevin Buzzard (Apr 27 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/125763232):
Two weeks later and I have all the infrastructure I need to prove that all my diagrams commute painlessly

#### [Kevin Buzzard (Apr 27 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/125763237):
In particular, Patrick said "I though about this, and I think you are cheating a bit here. You still need the maps in your exact sequence to commute with your canonical isomorphisms.", and he's right, and I now have this

#### [Kevin Buzzard (Apr 27 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/125763243):
so now I start the painful task of taking some exact sequence, replacing every term with an isomorphic term, and then proving that it's still exact

#### [Kevin Buzzard (Apr 27 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/promoting equiv/near/125763283):
not painful because it's hard, but painful because it's obvious :-)

