---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/74626statementofthefivelemma.html
---

## Stream: [general](index.html)
### Topic: [statement of the five lemma](74626statementofthefivelemma.html)

---


{% raw %}
#### [ Johan Commelin (Apr 24 2018 at 08:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125606612):
I just wrote a statement of the five lemma: https://gist.github.com/jcommelin/d097eb8f2587d34e5c337450bca543db

#### [ Johan Commelin (Apr 24 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125606625):
It seems extremely verbose to me. (And no, removing line breaks is not the solution :wink: ...)

#### [ Johan Commelin (Apr 24 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125606670):
If we ignore the facts that I am (i) not using lowercase greek for types, (ii) write types and conditions in the wrong order, and (iii) write lots of linebreaks; are there ways to improve this statement?

#### [ Reid Barton (Apr 24 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125606677):
Not nearly as verbose as the proof, I'm sure :simple_smile:

#### [ Reid Barton (Apr 24 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125606729):
One thing you could do is package up the underlying set function and `is_group_hom` instance of each map into a single type

#### [ Johan Commelin (Apr 24 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125606737):
I would love to just say: "Hey Lean, all these types are groups, and by the way, all my functions are homomorphisms"

#### [ Kenny Lau (Apr 24 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125606923):
sancta mater dei

#### [ Kenny Lau (Apr 24 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125606929):
you formalized five lemma

#### [ Kenny Lau (Apr 24 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125606933):
@**Kevin Buzzard** this is dank

#### [ Johan Commelin (Apr 24 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125606936):
no I did not

#### [ Johan Commelin (Apr 24 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125606938):
Only the statement

#### [ Kenny Lau (Apr 24 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125606942):
that’s what i mean

#### [ Johan Commelin (Apr 24 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125606945):
Which is not so hard to formalise, right?

#### [ Kenny Lau (Apr 24 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125606946):
formalize [sth] = formalize the statement of sth

#### [ Kenny Lau (Apr 24 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125606953):
well I never got my hands dirty

#### [ Johan Commelin (Apr 24 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125606965):
It's just a lot of repetitive strain injury inducing introductory blabla typing

#### [ Johan Commelin (Apr 24 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125606967):
I'm scared of the proof atm

#### [ Johan Commelin (Apr 24 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125606972):
But I hope that `cc` will do a lot of diagram chasing for me

#### [ Johan Commelin (Apr 24 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125607023):
Currently my proof starts with `split, apply is_group_hom.inj_of_trivial_ker n`. And then I'm stuck, because I don't know how to prove that two subsets are equal...

#### [ Johan Commelin (Apr 24 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125607026):
I really need a lot of handholding with Lean :confounded:

#### [ Johan Commelin (Apr 24 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125607236):
How do you split the goal `subset_1 = subset_2` into proving `x \in subset_1 \to x \in subset_2` and its converse?

#### [ Reid Barton (Apr 24 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125607243):
You can apply `set.ext`

#### [ Reid Barton (Apr 24 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125607246):
(I was just about to write something longer, but you said just what it does.)

#### [ Johan Commelin (Apr 24 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125607252):
Thanks, that helps. Now I get an `\iff`. How do I split it into two implications?

#### [ Johan Commelin (Apr 24 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125607258):
(And more meta: what is the best way to discover the answer to these questions without spamming Zulip?)

#### [ Johannes Hölzl (Apr 24 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125607355):
Either you use `iff.intro` or the anonymous constructor written as `\< ... ,  ... \>` where the VS Code plugin replaces the `\<` and `\>` .

#### [ Johan Commelin (Apr 24 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125607358):
Ok, cool

#### [ Johan Commelin (Apr 24 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125607360):
thanks!

#### [ Johannes Hölzl (Apr 24 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125607363):
Alternatively: use `subset.antisymm` then you have it in the right form (the subset relation is defintional equal to forall x `subset_1 implies subset2`

#### [ Johan Commelin (Apr 24 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125607504):
What are the advantages of `subset.antisymm` over the other method?

#### [ Kenny Lau (Apr 24 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125607506):
@**Johan Commelin** use split

#### [ Kenny Lau (Apr 24 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125607543):
to break down an iff

#### [ Reid Barton (Apr 24 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125607552):
In this specific case, I imagine there's probably a lemma that says that it suffices to show that `f x = 0 \to x = 0`

#### [ Johan Commelin (Apr 24 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125607684):
Yeah, I've got the trivial part now. If `x \in trivial subgroup \to x \in ker`

#### [ Johan Commelin (Apr 24 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125607720):
that's paraphrasing

#### [ Johan Commelin (Apr 24 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125607928):
Can I easily rewrite the hypothesis `(com₁ : m ∘ f = r ∘ l)` into `com₁' : \fo x, (m (f x) = r (l x))` ?

#### [ Sean Leather (Apr 24 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125607939):
Here's [my attempt](https://gist.github.com/jcommelin/d097eb8f2587d34e5c337450bca543db#gistcomment-2568165) to syntactically follow the lemma.

#### [ Sean Leather (Apr 24 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125607997):
It probably won't help you prove anything, of course. :simple_smile:

#### [ Kenny Lau (Apr 24 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608015):
I mean, shouldn’t one prove the weak four lemmas first?

#### [ Johan Commelin (Apr 24 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608057):
One could, of course... but they are basically the two subgoals after the first split

#### [ Johan Commelin (Apr 24 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608062):
There is a good reason to do that though... because then you only have to prove one of them

#### [ Johan Commelin (Apr 24 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608063):
the other follows by duality

#### [ Johan Commelin (Apr 24 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608077):
Still, the proof is a very straightforward diagram chase... so I hope I can convince Lean that it is easy as well

#### [ Johan Commelin (Apr 24 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608120):
I want to tell lean "For every group_hom \phi that you can see, do this... `have := is_group_hom.one \phi`"

#### [ Johan Commelin (Apr 24 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608121):
And things like that

#### [ Johan Commelin (Apr 24 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608129):
And one it has figured out all these basic things, then `cc` might actually deduce the result

#### [ Johan Commelin (Apr 24 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608176):
But then `cc` needs to know how to deal with `\circ`, hence my previous question about rewriting `com\1`

#### [ Johan Commelin (Apr 24 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608213):
@**Sean Leather** Thanks for the refactoring. It is more readable now (except that I most I would give the arrows names like f_1, g_1 and f_2, g_2 etc...)

#### [ Johan Commelin (Apr 24 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608215):
But it is still a bit verbose, right?

#### [ Reid Barton (Apr 24 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608216):
I added a comment with an "artistic" layout

#### [ Reid Barton (Apr 24 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608218):
(warning: long lines)

#### [ Johan Commelin (Apr 24 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608263):
Ha! I like that one

#### [ Johan Commelin (Apr 24 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608269):
It really explains the diagram. Cool!

#### [ Johan Commelin (Apr 24 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608285):
It would be great of you could tell lean `[is_group_hom f g h i j k l]`

#### [ Johan Commelin (Apr 24 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608332):
something like that, and it just understands that all of them are group homs

#### [ Sean Leather (Apr 24 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608358):
```quote
It would be great of you could tell lean `[is_group_hom f g h i j k l]`
```
Something like that would be useful in your case, but you wouldn't want to remove the ability to use multiple-parameter type classes, which it looks like `is_group_hom` is there.

#### [ Johan Commelin (Apr 24 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608362):
Hmmz, I see

#### [ Johan Commelin (Apr 24 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608415):
Also: `↪` and `↠` for injective respectively surjective functions

#### [ Johan Commelin (Apr 24 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608421):
But I guess that might be a bit hard

#### [ Johan Commelin (Apr 24 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608431):
So `{f: A ↪ B}` means `{f: A → B} [function.injective f]`

#### [ Sean Leather (Apr 24 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608550):
At the very least, you can `open function` to avoid having to prepend `function.`. :simple_smile:

#### [ Johan Commelin (Apr 24 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608553):
Aaah, ok. TIL :)

#### [ Johan Commelin (Apr 24 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125608559):
Hmmz TIL is confusing in this context. I meant "Today I Learned"

#### [ Kevin Buzzard (Apr 24 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609111):
```quote
(And more meta: what is the best way to discover the answer to these questions without spamming Zulip?)
```
Spam Zulip. I was in just this situation last September and spamming Zulip was by far the most efficient method. Mario often answered very quickly, and several others too. Now there are more people who can help, and the sooner you're up to speed the sooner you can help others. It's really important that mathematicians learn how to use this software as quickly as possible.

#### [ Kevin Buzzard (Apr 24 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609118):
PS I hope you're going to implement the abstract abelian category proof rather than all the diagram-chasing ;-)

#### [ Kevin Buzzard (Apr 24 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609134):
[not serious]

#### [ Kevin Buzzard (Apr 24 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609181):
although, in this crazy, world, who's to say that the abstract universal property proof won't be easier!

#### [ Kevin Buzzard (Apr 24 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609187):
I find myself in a similar situation right now, as it happens.

#### [ Kevin Buzzard (Apr 24 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609191):
I would like to prove R[1/f][1/g] = R[1/fg] (unique isomorphism of R-algebras)

#### [ Kevin Buzzard (Apr 24 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609202):
and I have set up all these universal properties and I know I can deduce it from those, and it will be really nice to do

#### [ Kevin Buzzard (Apr 24 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609215):
but I suspect that if I were to ask Kenny he would just write down a proof with lots of quotient.mk's in which just did everything directly.

#### [ Kevin Buzzard (Apr 24 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609269):
i.e. we have an interface (i.e. a bunch of universal properties) which will enable me to prove my result, but now I realise that someone who knows the underlying implementation can just prove the result directly anyway.

#### [ Kevin Buzzard (Apr 24 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609271):
It might be the same here; you can deduce the 5 lemma from the axioms of an ab cat

#### [ Kevin Buzzard (Apr 24 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609272):
or from the diagram chase

#### [ Kevin Buzzard (Apr 24 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609277):
and the proofs will be very different

#### [ Johan Commelin (Apr 24 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609403):
Yes, I see. I think it should be possible to have a diagram_chase tactic

#### [ Johan Commelin (Apr 24 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609416):
And my gut feeling is that `cc` is almost it. But you need to spam the context with a lot of information about group homomorphisms and kernels etc...

#### [ Kevin Buzzard (Apr 24 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609488):
`diagram_chase` tactic: I wonder if that's possible!

#### [ Kevin Buzzard (Apr 24 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609491):
As far as I know these CS people don't really do this kind of maths

#### [ Kevin Buzzard (Apr 24 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609530):
so you might find that this is actually a possibility once you formalise what you want

#### [ Patrick Massot (Apr 24 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609541):
That would be sooo nice

#### [ Kevin Buzzard (Apr 24 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609542):
When drawing that snake map from ker(map3) to coker(map1) I always feel I'm making the unique move each time

#### [ Patrick Massot (Apr 24 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609545):
Is the new parser going to accept `tikz-cd` input?

#### [ Sean Leather (Apr 24 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609546):
```quote
As far as I know these CS people don't really do this kind of maths
```
:astonished: Diagrams are pretty core to PLT.

#### [ Patrick Massot (Apr 24 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609547):
PLT?

#### [ Kevin Buzzard (Apr 24 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609548):
diagram-chasing in abelian groups is perhaps a bit different

#### [ Sean Leather (Apr 24 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609549):
Programming language theory.

#### [ Patrick Massot (Apr 24 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609550):
thks

#### [ Sean Leather (Apr 24 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609591):
```quote
diagram-chasing in abelian groups is perhaps a bit different
```
Okay. I'm not familiar with it, so that may be.

#### [ Kevin Buzzard (Apr 24 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609593):
Is the theory of abelian categories "complete" in some way?

#### [ Johan Commelin (Apr 24 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609595):
Yes, I was thinking about tikz-cd as well (-;

#### [ Kevin Buzzard (Apr 24 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609598):
i.e. "the five lemma is true, so there should be a proof which an algorithm can construct"?

#### [ Kevin Buzzard (Apr 24 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609608):
Just think, we could pester Mario to spend weeks developing such an algorithm, and then use it to prove the five lemma and then say "actually, the five lemma is pretty much the only thing we ever use"

#### [ Johan Commelin (Apr 24 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609609):
@**Patrick Massot** Did you see how @**Reid Barton** rewrote the statement? https://gist.github.com/jcommelin/d097eb8f2587d34e5c337450bca543db

#### [ Kevin Buzzard (Apr 24 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609610):
"but thanks anyway"

#### [ Johan Commelin (Apr 24 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609611):
Ouch

#### [ Johan Commelin (Apr 24 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609653):
And the snake lemma, and the rest of homological algebra

#### [ Kevin Buzzard (Apr 24 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609656):
That PR will be rejected because the groups aren't all called alpha

#### [ Johan Commelin (Apr 24 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609660):
Yeah, I will relabel everything to be alpha_1 alpha_2 etc...

#### [ Johan Commelin (Apr 24 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609661):
who needs betas

#### [ Kevin Buzzard (Apr 24 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609716):
I concur with Kenny's "dank" comment

#### [ Kevin Buzzard (Apr 24 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609717):
This is absolutely great

#### [ Patrick Massot (Apr 24 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609720):
No, you should keep groups G. Mario and Johannes will end up understanding.

#### [ Patrick Massot (Apr 24 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609721):
Don't release pressure on this important issue

#### [ Johan Commelin (Apr 24 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609724):
Sure

#### [ Johan Commelin (Apr 24 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609725):
Was just kidding

#### [ Johan Commelin (Apr 24 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125609736):
@**Kevin Buzzard** Well, thanks. I thought it was a good test case

#### [ Reid Barton (Apr 24 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125610505):
```quote
Is the theory of abelian categories "complete" in some way?
```
No, https://mathoverflow.net/a/12799

#### [ Reid Barton (Apr 24 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125610563):
Most similar theories will admit embeddings of the word problem like this, I think. But in diagrams where there are only finitely many ways to compose morphisms (basically, "without loops"), maybe there is hope.

#### [ Kevin Buzzard (Apr 24 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125611247):
Thanks @**Reid Barton** . I wondered if the abelian-ness of the situation saved our bacon but somehow this automorphism trick gets you back into a non-abelian situation

#### [ Johan Commelin (Apr 24 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612399):
I put an update in the comments of the gist: https://gist.github.com/jcommelin/d097eb8f2587d34e5c337450bca543db

#### [ Johan Commelin (Apr 24 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612404):
The first half of the proof is almost done

#### [ Johan Commelin (Apr 24 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612413):
There is one stupid `admit`

#### [ Johan Commelin (Apr 24 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612421):
And I don't get why `apply_assumption` fails, because 2 lines above, there is `f_1 w = y`

#### [ Kevin Buzzard (Apr 24 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612476):
Your definition of im is not great

#### [ Kevin Buzzard (Apr 24 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612486):
You defined `definition im (f : A → B) [is_group_hom f] := f '' (@set.univ A)`

#### [ Johan Commelin (Apr 24 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612488):
No, no longer

#### [ Johan Commelin (Apr 24 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612489):
See the update

#### [ Kevin Buzzard (Apr 24 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612490):
Oh OK

#### [ Johan Commelin (Apr 24 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612493):
It is now `set.range f`

#### [ Johan Commelin (Apr 24 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612498):
I dunno if that is better (-;

#### [ Kevin Buzzard (Apr 24 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612548):
That's definitely better

#### [ Kevin Buzzard (Apr 24 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612560):
The problem with the old one

#### [ Kevin Buzzard (Apr 24 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612564):
`definition im (f : A → B) [is_group_hom f] := f '' (@set.univ A)`

#### [ Kevin Buzzard (Apr 24 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612569):
was that you can write `#print notation ''` to find out what `''` expands to

#### [ Kevin Buzzard (Apr 24 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612577):
and see it expands to `set.image`

#### [ Kevin Buzzard (Apr 24 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612581):
and then `#print set.image` to find what that unfolds to

#### [ Johan Commelin (Apr 24 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612584):
I see...

#### [ Kevin Buzzard (Apr 24 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612586):
and you see it becomes `\ex a, a \in set.univ and f a = b`

#### [ Kevin Buzzard (Apr 24 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612625):
in particular we have some clause which is always true

#### [ Kevin Buzzard (Apr 24 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612626):
and in the way

#### [ Kevin Buzzard (Apr 24 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612628):
With your new definition we can do stuff like this:

#### [ Kevin Buzzard (Apr 24 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612632):
```lean
import group_theory.subgroup

open function is_group_hom

universes u

variables {A B : Type u} [group A] [group B]
definition im (f : A → B) := set.range f

example (G H K : Type u) [group G] [group H] [group K] (α : G → H) [is_group_hom α]
(β : H → K) [is_group_hom β] (Hexact : im α = ker β) (h : H) (Hker : β h = 1) :
∃ g, α g = h := 
begin
have Hker2 : h ∈ ker β := (mem_ker β).2 Hker,
rw ←Hexact at Hker2,
exact Hker2
end
```

#### [ Kevin Buzzard (Apr 24 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612635):
because after the rewrite, `Hker2` is definitionally equivalent to what you want

#### [ Kenny Lau (Apr 24 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612647):
I still think you should prove the weak four lemmas first

#### [ Johan Commelin (Apr 24 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612690):
@**Kenny Lau** I am almost done with the first one

#### [ Johan Commelin (Apr 24 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612693):
Just need to get rid of one stupid `admit`

#### [ Kevin Buzzard (Apr 24 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612818):
It's really hard to follow the argument without working hard

#### [ Kevin Buzzard (Apr 24 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612820):
what is the problem which you're admitting defeat on?

#### [ Kevin Buzzard (Apr 24 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612823):
I see you want to prove y in im f1

#### [ Kevin Buzzard (Apr 24 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612825):
and I see 100 assumptions

#### [ Johan Commelin (Apr 24 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612827):
Ok, so a minor change. I now have `local notation im := set.range`

#### [ Johan Commelin (Apr 24 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612830):
with backticks around `im`

#### [ Kevin Buzzard (Apr 24 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612838):
if you open set you can just use range

#### [ Kevin Buzzard (Apr 24 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612839):
but I think im is better

#### [ Kevin Buzzard (Apr 24 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612841):
what is your maths proof of the thing you;re admitting?

#### [ Johan Commelin (Apr 24 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612842):
So, I want to prove `y ∈ im f`

#### [ Johan Commelin (Apr 24 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612845):
and it should follow immediately from the two lines above it

#### [ Kevin Buzzard (Apr 24 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612888):
I see

#### [ Kevin Buzzard (Apr 24 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612889):
so name one of them and use rw?

#### [ Kevin Buzzard (Apr 24 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612894):
Although I am not an expert

#### [ Johan Commelin (Apr 24 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612895):
aha, I thought apply_assumption would just kill it off

#### [ Kevin Buzzard (Apr 24 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612899):
I am skeptical about not naming any assumptions

#### [ Kevin Buzzard (Apr 24 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612900):
I have never heard of apply_assumption

#### [ Kevin Buzzard (Apr 24 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612901):
What does it do?

#### [ Johan Commelin (Apr 24 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612915):
It is like `apply foo`, where `foo` is an assumption

#### [ Kevin Buzzard (Apr 24 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612950):
but you need 2 assumptions

#### [ Kevin Buzzard (Apr 24 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612955):
to deduce what you want

#### [ Johan Commelin (Apr 24 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612958):
yeah, that's true

#### [ Kevin Buzzard (Apr 24 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125612969):
I don't think it's the end of the world to start calling useful hypotheses H1 H2 H3...

#### [ Johan Commelin (Apr 24 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125613012):
But `rw` doesn't work either... I named one of the assumptions:
`have foo : f₁ w = y`

#### [ Johan Commelin (Apr 24 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125613017):
And then I try `rw foo`, but it doesn't work

#### [ Kevin Buzzard (Apr 24 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125613018):
rw \l foo

#### [ Johan Commelin (Apr 24 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125613022):
unknown identifier 'foo'

#### [ Kevin Buzzard (Apr 24 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125613036):
I think that you are not proving what you think you are proving

#### [ Kevin Buzzard (Apr 24 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125613081):
`have foo : f₁ w = y, apply_assumption,`

#### [ Kevin Buzzard (Apr 24 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125613083):
That's what you have now, right?

#### [ Johan Commelin (Apr 24 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125613085):
Yes

#### [ Kevin Buzzard (Apr 24 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125613091):
so put your cursor just after the comma after the y

#### [ Kevin Buzzard (Apr 24 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125613096):
and you see that the first goal is f1 w = y

#### [ Kevin Buzzard (Apr 24 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125613103):
and there are two goals

#### [ Johan Commelin (Apr 24 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125613104):
Yes

#### [ Kevin Buzzard (Apr 24 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125613106):
and now click after the comma after apply_assumption

#### [ Kevin Buzzard (Apr 24 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125613110):
and there are still 2 goals

#### [ Johan Commelin (Apr 24 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125613152):
aaah

#### [ Kevin Buzzard (Apr 24 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125613154):
so your "proof" didn't prove it

#### [ Kevin Buzzard (Apr 24 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125613164):
this is nothing to do with the naming of the assumption

#### [ Kevin Buzzard (Apr 24 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125613167):
it was just never added to the local context

#### [ Johan Commelin (Apr 24 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125613172):
ok, thanks!

#### [ Johan Commelin (Apr 24 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125613175):
let me try again

#### [ Kevin Buzzard (Apr 24 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125613178):
Because your context is gigantic

#### [ Kevin Buzzard (Apr 24 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125613180):
you should keep a close eye on the number of goals

#### [ Kevin Buzzard (Apr 24 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/statement%20of%20the%20five%20lemma/near/125613183):
which is displayed at the top of the output


{% endraw %}
