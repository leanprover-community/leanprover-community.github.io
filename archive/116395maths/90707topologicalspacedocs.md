---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/90707topologicalspacedocs.html
---

## [maths](index.html)
### [topological space docs](90707topologicalspacedocs.html)

#### [Kevin Buzzard (Apr 14 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088079):
Ok so after a ropey start (see my heq thread earlier) I made it through the `topological_space.lean` file today and wrote some docs on it: https://github.com/kbuzzard/mathlib/blob/docs-topspaces/docs/theories/topological_spaces.md . I needed to read this file for my work on schemes -- in particular I had to finally understand what a filter was and what they had to do with topological spaces.

#### [Patrick Massot (Apr 14 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088666):
You are a bit unfair with filters. You should at least explain that they allow to cover uniformly the cases of sequences and maps from topological spaces. And then slightly more exotic stuff like one-sided limits at some real. That's why Bourbaki invented them.

#### [Patrick Massot (Apr 14 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088713):
They also allow to mimic using sequential continuity and compactness for non-metric spaces

#### [Mario Carneiro (Apr 14 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088714):
One way to motivate them is to consider the ~16 variations on L'hopital's theorem that arise with lots of permutations of limits to different places in the domain and codomain

#### [Kevin Buzzard (Apr 14 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088753):
I was just grumpy about them because they have actively stopped me doing what should be trivial stuff for a couple of days, because I didn't know what \Glb meant

#### [Kevin Buzzard (Apr 14 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088760):
when I actually ploughed through the file and a lot of the imports, and set pp.all on occasionally etc etc and finally got to the bottom of things and discovered that F <= G iff G subseteq F

#### [Kevin Buzzard (Apr 14 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088761):
then it all began to make sense

#### [Patrick Massot (Apr 14 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088762):
This is what this definition if compactness is about: a space is compact if every sequence has a converging subsequence,made true for all spaces

#### [Mario Carneiro (Apr 14 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088763):
The description of topological basis is also a bit grumpy; the point as I mentioned before is to say "a topological basis is a collection of sets satisfying these two axioms" and then fold in the connection to generating a topology

#### [Kevin Buzzard (Apr 14 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088764):
I'm sure it's a very cute way to think about things

#### [Kevin Buzzard (Apr 14 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088803):
yeah, I had to get up early this morning, I've been in a grumpy mood all day :-)

#### [Patrick Massot (Apr 14 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088807):
I'm defending filters here but zulip and gitter can testify I went through the same frustrations

#### [Mario Carneiro (Apr 14 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088814):
In fact I think the "filters are a complete lattice" angle should probably be emphasized more, since it underlies many of the filter-theoretic definitions

#### [Mario Carneiro (Apr 14 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088857):
A filter which is not bottom is called a proper filter fyi

#### [Kevin Buzzard (Apr 14 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088858):
Mario, the reason I don't buy your explanation is that there is a standard definition of a basis of a topological space, which we all learn, and which is on Wikipedia, and which is not what is implemented, so all your protestations that it's a better way of doing it are cancelled out by the fact that every mathematician will be confused by the way it's done. I have flagged the relevant lemma which saves us.

#### [Mario Carneiro (Apr 14 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088863):
but it is that definition...

#### [Patrick Massot (Apr 14 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088864):
I think Mario had the right idea when I faced that:we keep filters but add lemmas translating to usual stuff in usual situations

#### [Kevin Buzzard (Apr 14 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088865):
[explanation of why bases are done like that]

#### [Kevin Buzzard (Apr 14 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088866):
Yes, I explictly flag the lemmas saying "oh look, compactness looks insane, here's the lemma you need"

#### [Kevin Buzzard (Apr 14 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088867):
"bases look insane, here's the lemma you need"

#### [Kevin Buzzard (Apr 14 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088868):
That's the philosophy of the docs

#### [Mario Carneiro (Apr 14 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088907):
https://en.wikipedia.org/wiki/Base_(topology)
> A base is a collection B of subsets of X satisfying these two properties:
> 1. The base elements cover X.
> 2. Let B1, B2 be base elements and let I be their intersection. Then for each x in I, there is a base element B3 containing x and contained in I.

#### [Kevin Buzzard (Apr 14 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088908):
Now I can use topological spaces in Lean, and this morning I couldn't.

#### [Kevin Buzzard (Apr 14 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088910):
Right.

#### [Kevin Buzzard (Apr 14 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088911):
Whereas you have generate_open

#### [Kevin Buzzard (Apr 14 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088913):
it's the generate_open that makes it unusable

#### [Patrick Massot (Apr 14 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088914):
I'm sure you could also explain why filters are useful

#### [Mario Carneiro (Apr 14 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088915):
Any topological basis is a basis for the topology it generates

#### [Kevin Buzzard (Apr 14 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088916):
the lemma you proved and I flagged makes the definition usable

#### [Mario Carneiro (Apr 14 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088918):
you can always satisfy that clause with refl

#### [Kevin Buzzard (Apr 14 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088927):
My point is simply that if you want to prove that (a,b) x (c,d) is a basis of open sets for the standard topology on R^2, you cannot possibly do that from the definition

#### [Kevin Buzzard (Apr 14 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088928):
but it's easy from the lemma

#### [Mario Carneiro (Apr 14 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088930):
Yes you can

#### [Kevin Buzzard (Apr 14 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088932):
_you_ can

#### [Kevin Buzzard (Apr 14 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088934):
a mathematician can't

#### [Kevin Buzzard (Apr 14 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088977):
becuase they have no clue how to use generate_open

#### [Mario Carneiro (Apr 14 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088978):
Those are two different goals though

#### [Mario Carneiro (Apr 14 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088980):
you are trying to prove that some basis is a basis for something else, rather than just proving it's a basis

#### [Patrick Massot (Apr 14 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088981):
My wife says I must stop participating but please be nice :smiley:

#### [Kevin Buzzard (Apr 14 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088988):
In maths, the proof goes "insert argument to prove that if x is in an open set U in R^2 then ther's some (a,b) x (c,d) in U containing x and now we're done

#### [Kevin Buzzard (Apr 14 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088990):
in Lean the proof from the definition of basis goes "that, and then we have to prove something about generate_open"

#### [Kevin Buzzard (Apr 14 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088991):
except now we don't because of the lemma

#### [Mario Carneiro (Apr 14 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088992):
You have a preconceived topology in that example

#### [Kevin Buzzard (Apr 14 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088993):
yes, the one the mathematicans use :-)

#### [Mario Carneiro (Apr 14 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088994):
I'm talking about proving that some collection of sets is a basis full stop

#### [Kevin Buzzard (Apr 14 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088995):
I know

#### [Kevin Buzzard (Apr 14 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089033):
but that's a silly notion

#### [Mario Carneiro (Apr 14 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089037):
That's the one wikipedia discusses

#### [Kevin Buzzard (Apr 14 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089038):
there's no generate_open there

#### [Kevin Buzzard (Apr 14 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089039):
it's the generate_open which makes the definition a complete pain to work with

#### [Kevin Buzzard (Apr 14 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089040):
and it's the lemma that saves us

#### [Kevin Buzzard (Apr 14 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089041):
so I highlight the lemma

#### [Kevin Buzzard (Apr 14 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089046):
that's all

#### [Kevin Buzzard (Apr 14 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089047):
the lemmas are all there

#### [Mario Carneiro (Apr 14 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089048):
The generate_open is dischargable by refl, like I said

#### [Kevin Buzzard (Apr 14 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089049):
I'm saying the definitions are silly, but that's OK because the lemmas are there

#### [Kevin Buzzard (Apr 14 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089050):
yeah but I don't really know what that means

#### [Kevin Buzzard (Apr 14 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089089):
and I know what the lemma means

#### [Mario Carneiro (Apr 14 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089091):
If S satisfies axioms 1 and 2, then it is a basis for (generate_open S)

#### [Kevin Buzzard (Apr 14 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089092):
and a generic mathematician will come along

#### [Kevin Buzzard (Apr 14 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089093):
with a proof of the two things in wikipedia

#### [Kevin Buzzard (Apr 14 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089094):
and will want to prove that they have a basis

#### [Kevin Buzzard (Apr 14 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089095):
and so they can use the lemma

#### [Mario Carneiro (Apr 14 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089101):
okay I get it you think the notion is useless

#### [Kevin Buzzard (Apr 14 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089103):
right

#### [Kevin Buzzard (Apr 14 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089105):
but I'm not saying it shouldn't be there

#### [Kevin Buzzard (Apr 14 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089106):
I'm just explaining why I had to write the docs

#### [Mario Carneiro (Apr 14 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089107):
but the docs are

#### [Kevin Buzzard (Apr 14 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089109):
and why they came out grumpy :-)

#### [Kevin Buzzard (Apr 14 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089110):
that is an absurd definition of compact as well.

#### [Kevin Buzzard (Apr 14 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089156):
It should be a theorem not a definition.

#### [Kevin Buzzard (Apr 14 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089160):
But again it doesn't matter

#### [Kevin Buzzard (Apr 14 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089161):
anyway, I am not grumpy any more :-)

#### [Mario Carneiro (Apr 14 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089162):
I'm not sure how much I want to defend this... I think Johannes thought the filter stuff would make everything neat and concise

#### [Kevin Buzzard (Apr 14 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089167):
it doesn't matter

#### [Kevin Buzzard (Apr 14 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089170):
I'm just taking a contrary position for a laugh really

#### [Kevin Buzzard (Apr 14 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089171):
I'm really happy now

#### [Kevin Buzzard (Apr 14 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089172):
I can work topological spaces

#### [Mario Carneiro (Apr 14 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089173):
I personally have a preference for standard point-set definitions

#### [Kevin Buzzard (Apr 14 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089174):
and I'm hoping that other people with the same background as me (i.e. basically two courses in topology and that's it) can do the same

#### [Mario Carneiro (Apr 14 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089214):
but there are enough lemmas around to get rid of any filter claims you come across

#### [Kevin Buzzard (Apr 14 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089215):
yeah, that's why Hausdorff is called t2 probably ;-)

#### [Mario Carneiro (Apr 14 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089217):
t2 is shorter :)

#### [Kevin Buzzard (Apr 14 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089219):
I'm really happy with the lemmas. I was preparing a list of lemmas which you should have proved

#### [Kevin Buzzard (Apr 14 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089220):
and it came out empty in the end

#### [Kevin Buzzard (Apr 14 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089223):
Occasionally it would have size 1 or 2

#### [Kevin Buzzard (Apr 14 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089226):
and then I'd find them :-)

#### [Kevin Buzzard (Apr 14 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089232):
Props to @**Johannes Hölzl** too.

#### [Mario Carneiro (Apr 14 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089233):
yeah he gets the credit for most of this work

#### [Kevin Buzzard (Apr 14 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089234):
It's a really nice complete library

#### [Kevin Buzzard (Apr 14 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089236):
even though some definitions are theorems and some theorems are definitions ;-)

#### [Kevin Buzzard (Apr 14 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089276):
I guess you guys can barely tell the difference

#### [Kevin Buzzard (Apr 14 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089278):
you probably think I'm talking about unfolding or something

#### [Mario Carneiro (Apr 14 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089280):
it will teach you to forget about definitions and worry more about interfaces

#### [Kevin Buzzard (Apr 14 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089281):
OK, enough CS baiting. Thank you for your library!

#### [Kevin Buzzard (Apr 14 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089282):
I need to learn what this word interface means

#### [Mario Carneiro (Apr 14 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089289):
does API mean something to you?

#### [Kevin Buzzard (Apr 14 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089337):
not really

#### [Kevin Buzzard (Apr 14 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089340):
this is some way of talking to the theorems

#### [Kevin Buzzard (Apr 14 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089341):
or something

#### [Kevin Buzzard (Apr 14 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089378):
Are my docs some sort of attempt to make an API for mathematicians trying to use topological spaces in Lean?

#### [Mario Carneiro (Apr 14 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089382):
it's the idea that you encapsulate the underlying definition, somehow make it inaccessible, and then only use theorems that express properties of it

#### [Kevin Buzzard (Apr 14 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089384):
encapsulate is another mystery

#### [Kevin Buzzard (Apr 14 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089385):
these are all very CS words

#### [Kevin Buzzard (Apr 14 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089391):
I understand that a mathematician will come along with a proof that every cover has a finite subcover and will want to deduce that their space is compact

#### [Kevin Buzzard (Apr 14 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089392):
so I point them to the lemma which says this

#### [Kevin Buzzard (Apr 14 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089393):
[and make some snarky remark probably about how the definition is something else]

#### [Mario Carneiro (Apr 14 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089394):
Category theory does this a lot, for example: A product of two objects is some object with a universal property, so that you can only use the universal property to prove stuff rather than unfolding whatever the product is "actually" defined to be in a particular category

#### [Kevin Buzzard (Apr 14 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089396):
universal properties I understand

#### [Kevin Buzzard (Apr 15 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089439):
but I don't understand why this is an argument for giving an unrecognisable definition of compact

#### [Mario Carneiro (Apr 15 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089442):
A biconditional is also a "universal property", in a sense

#### [Kevin Buzzard (Apr 15 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089443):
biconditional is a theorem of the form X iff Y?

#### [Mario Carneiro (Apr 15 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089444):
it tells you everything you ever need to know about the definition, without actually telling you what the definition is

#### [Kevin Buzzard (Apr 15 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089445):
I see

#### [Kevin Buzzard (Apr 15 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089448):
but you really need to know where the theorem is

#### [Mario Carneiro (Apr 15 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089449):
yes, that's the public part

#### [Mario Carneiro (Apr 15 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089457):
the definition is the private part

#### [Kevin Buzzard (Apr 15 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089459):
Maybe I saw this in java once

#### [Kevin Buzzard (Apr 15 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089460):
your variables are private

#### [Kevin Buzzard (Apr 15 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089462):
and you make some functions which lets the user change them

#### [Kevin Buzzard (Apr 15 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089463):
or read them

#### [Kevin Buzzard (Apr 15 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089464):
without actually letting them fiddle with them directly

#### [Kevin Buzzard (Apr 15 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089465):
sorry, methods

#### [Kevin Buzzard (Apr 15 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089502):
but I didn't realise this had anything to do with topological spaces at the time

#### [Mario Carneiro (Apr 15 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089505):
{% raw %}
One reasonably basic example of a gnarly construction is the Kuratowski pair (a,b) = {{a}, {a, b}}{% endraw %}

#### [Kevin Buzzard (Apr 15 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089506):
eew

#### [Kevin Buzzard (Apr 15 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089507):
eew

#### [Kevin Buzzard (Apr 15 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089509):
I see

#### [Kevin Buzzard (Apr 15 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089510):
that's a great example

#### [Kevin Buzzard (Apr 15 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089516):
we just need (a,b) = (c,d) iff a=c and b=d

#### [Mario Carneiro (Apr 15 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089517):
exactly

#### [Kevin Buzzard (Apr 15 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089518):
so we point the user to where that is proved

#### [Kevin Buzzard (Apr 15 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089519):
and they can't see the disgusting truth behind it all

#### [Mario Carneiro (Apr 15 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089559):
{% raw %}
and later, we might want to change the definition for some reason to, say, {{0,a}, {1, b}} and that's okay as long as we can still prove the defining property, since no user depended on the specific construction{% endraw %}

#### [Kevin Buzzard (Apr 15 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089560):
but the compactness thing is different. We go for Kuratowski because all the choices are horrible and this one is the least horrible

#### [Kevin Buzzard (Apr 15 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089561):
I see

#### [Kevin Buzzard (Apr 15 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089563):
it's not completely different

#### [Kevin Buzzard (Apr 15 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089574):
you are reserving the right to invent some even more weird thing that is better than filters

#### [Kevin Buzzard (Apr 15 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089576):
and then change the definition of compactness

#### [Kevin Buzzard (Apr 15 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089577):
because it compiles better on a quantum computer or whatever

#### [Mario Carneiro (Apr 15 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089579):
or even just the point-set definition

#### [Kevin Buzzard (Apr 15 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089616):
I see. In fact you could just play that trump card and that would shut me up

#### [Kevin Buzzard (Apr 15 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089620):
you should just say "Kevin, you don't understand, the definition we have here works better if your machine has 8 cores"

#### [Kevin Buzzard (Apr 15 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089622):
and I would have no response

#### [Mario Carneiro (Apr 15 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089623):
the real point is that *it shouldn't matter* what the actual definition is, and if it does you're doing it wrong

#### [Kevin Buzzard (Apr 15 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089626):
This is different to mathematics

#### [Kevin Buzzard (Apr 15 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089630):
If you wrote a maths book with some weird definitions of things

#### [Kevin Buzzard (Apr 15 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089634):
and then proved theorems which said that they were the same as everyone else's definition

#### [Mario Carneiro (Apr 15 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089635):
there's also the pedagogical angle, but that's a different issue

#### [Kevin Buzzard (Apr 15 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089639):
people would be confused as to why you were doing it

#### [Mario Carneiro (Apr 15 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089641):
I don't think that exact thing is unheard of though

#### [Kevin Buzzard (Apr 15 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089642):
and you can't answer "this definition works better if you have 8 brains"

#### [Mario Carneiro (Apr 15 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089684):
your new definition might be suitable to a particular sort of generalization, for example

#### [Kevin Buzzard (Apr 15 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089685):
As you are probably aware, I am extremely interested in the pedagogical angle

#### [Kevin Buzzard (Apr 15 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089688):
and have very little understanding of stuff like run time analysis and other CS-related matters

#### [Mario Carneiro (Apr 15 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089689):
in the pedagogical view, you might redefine the same thing several times depending on the current teaching goals

#### [Mario Carneiro (Apr 15 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089695):
the new definition may not even be the same as earlier ones, although it is usually a generalization or provably equivalent

#### [Kevin Buzzard (Apr 15 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089742):
So ultimately I should not care about your definitions, my main aim is to make sure that the interfaces are there.

#### [Mario Carneiro (Apr 15 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089743):
exactly

#### [Kevin Buzzard (Apr 15 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089744):
OK maybe tomorrow I will degrump it a bit :-)

#### [Kevin Buzzard (Apr 15 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089745):
but now I have to make a birthday present

#### [Mario Carneiro (Apr 15 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089750):
lol it's my birthday so I'll just pretend that's for me ;)

#### [Kevin Buzzard (Apr 15 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089752):
ha ha it's for my son's GF

#### [Kevin Buzzard (Apr 15 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089753):
happy birthday

#### [Kevin Buzzard (Apr 15 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089795):
I'm not entirely sure you'd want a plastic T anyway

#### [Mario Carneiro (Apr 15 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089802):
good mathlib docs are a good present :)

#### [Kevin Buzzard (Apr 15 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125091717):
OK well seeing as it's your birthday I de-grumped the docs a bit.

#### [Kevin Buzzard (Apr 15 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125091718):
even though it's strictly speaking not even your birthday any more where I'm sitting

#### [Kevin Buzzard (Apr 15 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125091723):
I'm now about to get onto the job I meant to do today, which was to prove that Spec(R) is compact using some argument involving bases :-)

#### [Kevin Buzzard (Apr 15 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125091724):
now I understand the interface better :-)

#### [Kevin Buzzard (Apr 15 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125091725):
Thanks as ever, by the way.

#### [Mario Carneiro (Apr 15 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125091768):
I forget if the contrapositive form of the compactness definition is there: a collection of closed sets with the finite intersection property has nonempty intersection

#### [Kevin Buzzard (Apr 15 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125091778):
I didn't see it

#### [Kevin Buzzard (Apr 15 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125091783):
and I almost mentioned it as a theorem which should be there

#### [Kevin Buzzard (Apr 15 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125091819):
but then I decided I'd never used it in my life :-)

#### [Kevin Buzzard (Apr 15 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125091830):
I almost mentioned it the other day when Simon was asking whether the same was true for an arbitrary set

#### [Mario Carneiro (Apr 15 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125091840):
I guess it is somewhat similar to the filter definition

#### [Kevin Buzzard (Apr 15 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125091933):
Hmm, I've just realised that I want that a mathlib-basis is a Wikipedia-basis

#### [Mario Carneiro (Apr 15 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125091939):
that's just the first two parts of the definition

#### [Kevin Buzzard (Apr 15 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125091985):
oh sorry I don't mean that

#### [Mario Carneiro (Apr 15 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125091990):
If `h1` and `h2` are proofs of the two axioms, then `<h1, h2, rfl>` is a proof it's a mathlib-basis

#### [Mario Carneiro (Apr 15 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125091994):
that's what I've been saying

#### [Kevin Buzzard (Apr 15 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125091999):
`is_topological_basis_of_open_of_nhds`

#### [Kevin Buzzard (Apr 15 2018 at 01:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092001):
I mean the converse of that

#### [Kevin Buzzard (Apr 15 2018 at 01:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092038):
Yes, sorry, I understand now

#### [Kevin Buzzard (Apr 15 2018 at 01:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092043):
I was talking nonsense at some points earlier

#### [Kevin Buzzard (Apr 15 2018 at 01:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092047):
when I said "wikipedia definition"

#### [Kevin Buzzard (Apr 15 2018 at 01:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092049):
I sometimes meant "hypotheses in `is_topological_basis_of_open_of_nhds`"

#### [Kevin Buzzard (Apr 15 2018 at 01:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092050):
:-/

#### [Mario Carneiro (Apr 15 2018 at 01:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092061):
`mem_nhds_of_is_topological_basis` is the easiest way to get converses of that stuff

#### [Kevin Buzzard (Apr 15 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092062):
https://topospaces.subwiki.org/wiki/Basis_for_a_topological_space

#### [Mario Carneiro (Apr 15 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092106):
but there should be a theorem saying that a basis element is open

#### [Kevin Buzzard (Apr 15 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092108):
there's a website (which I've never heard of) giving that as the definition.

#### [Kevin Buzzard (Apr 15 2018 at 01:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092111):
This is evidence that I am very fluid with what my definition is :-/

#### [Kevin Buzzard (Apr 15 2018 at 01:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092119):
mem_nhds means I might have to get my hands dirty with neighbourhoods maybe :-/

#### [Mario Carneiro (Apr 15 2018 at 01:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092124):
which statement are you going for specifically?

#### [Kevin Buzzard (Apr 15 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092176):
if B is a basis then I want that for all U open and for all x in U, there's V in B with x in V in U

#### [Kevin Buzzard (Apr 15 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092179):
because as we all know

#### [Kevin Buzzard (Apr 15 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092223):
50% of the time I will swear blind that this is the definition of a basis in Wikipedia

#### [Kevin Buzzard (Apr 15 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092228):
and I don't want to do induction on generate_open

#### [Kevin Buzzard (Apr 15 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092229):
I want this to be there on a plate

#### [Kevin Buzzard (Apr 15 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092231):
Kenny proved it

#### [Kevin Buzzard (Apr 15 2018 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092233):
in a file called temp.lean :-)

#### [Kevin Buzzard (Apr 15 2018 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092238):
but I was trying to avoid importing this file

#### [Kevin Buzzard (Apr 15 2018 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092239):
because its name looked a bit ominous

#### [Kevin Buzzard (Apr 15 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092284):
I can do this myself

#### [Kevin Buzzard (Apr 15 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092285):
The lemmas I need are all there

#### [Kevin Buzzard (Apr 15 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092287):
I just need to glue them

#### [Kevin Buzzard (Apr 15 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092292):
This morning I didn't know what nhds a was

#### [Kevin Buzzard (Apr 15 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092293):
I have to remember that I'm not scared of it any more

#### [Mario Carneiro (Apr 15 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092339):
I can add these to the file:
```
lemma is_open_of_is_topological_basis {s : set α} {b : set (set α)}
  (hb : is_topological_basis b) (hs : s ∈ b) : _root_.is_open s :=
is_open_iff_mem_nhds.2 $ λ a as,
(mem_nhds_of_is_topological_basis hb).2 ⟨s, hs, as, subset.refl _⟩

lemma mem_subset_basis_of_mem_open {b : set (set α)}
  (hb : is_topological_basis b) {a:α} (u : set α) (au : a ∈ u)
  (ou : _root_.is_open u) : ∃v ∈ b, a ∈ v ∧ v ⊆ u :=
(mem_nhds_of_is_topological_basis hb).1 $ mem_nhds_sets ou au
```

#### [Kevin Buzzard (Apr 15 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092348):
It's the easy way of `is_open_iff_mem_nhds` I need and then I'm done :-)

#### [Kevin Buzzard (Apr 15 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092388):
yeah, what you said

#### [Kevin Buzzard (Apr 15 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092390):
I'd vote for them definitely.

#### [Kevin Buzzard (Apr 15 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092391):
Then I can eschew temp.lean completely

#### [Mario Carneiro (Apr 15 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092393):
I like `mem_nhds_of_is_topological_basis` because it generalizes well to all sorts of bounded quantification over open sets that comes up in topology, like continuity or compactness that can be stated with basis sets

#### [Kevin Buzzard (Apr 15 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092398):
I didn't like it until today because of the obscure definition of nhds

#### [Kevin Buzzard (Apr 15 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092449):
but again there was a lemma -- in this case `mem_nhds_sets_iff` -- which made this clear

#### [Kevin Buzzard (Apr 15 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092510):
or even `nhds_sets`, which I mention in the docs

#### [Kevin Buzzard (Apr 15 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092516):
I see. I'm mentioning all the results that a mathematician needs for the interface.

#### [Kevin Buzzard (Apr 15 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092887):
eew, `exists v \in B` -- I have to run classical.some twice to get that v is in B

#### [Mario Carneiro (Apr 15 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092927):
You can use `exists.fst` for the `v \in B` hypothesis

#### [Kevin Buzzard (Apr 15 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092928):
That means `exists v in B, P` (B a set) unravels to `exists v in X, exists H : v in B, ...`

#### [Kevin Buzzard (Apr 15 2018 at 02:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092935):
Why not unravel to `exists v in X, v in B and ...`

#### [Mario Carneiro (Apr 15 2018 at 02:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092936):
You can also use `exists v : B, P` to pack them both into one

#### [Kevin Buzzard (Apr 15 2018 at 02:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092937):
yeah but you wrote v in B not me ;-)

#### [Mario Carneiro (Apr 15 2018 at 02:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092938):
because that same translation works for a wide variety of binders

#### [Kevin Buzzard (Apr 15 2018 at 02:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092975):
I don't know what a binder is

#### [Mario Carneiro (Apr 15 2018 at 02:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092981):
A thing that introduces a bound variable

#### [Mario Carneiro (Apr 15 2018 at 02:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092982):
like exists or forall or lambda

#### [Kevin Buzzard (Apr 15 2018 at 02:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092983):
somehow I thought that there were only about three of these

#### [Mario Carneiro (Apr 15 2018 at 02:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092984):
or Glb or Lub

#### [Kevin Buzzard (Apr 15 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092991):
but you're saying "exists v \in B" is somehow another one

#### [Mario Carneiro (Apr 15 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092992):
or indexed intersection

#### [Kevin Buzzard (Apr 15 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125093034):
I see.

#### [Mario Carneiro (Apr 15 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125093035):
No, I'm saying that *every* binder has the translation `Q a R b, p a => Q a, Q (_ : a R b), p a` where `Q` is any binder

#### [Mario Carneiro (Apr 15 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125093037):
and `R` is any infix operator

#### [Kevin Buzzard (Apr 15 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125093038):
`unknown identifier 'exists.fst'`

#### [Mario Carneiro (Apr 15 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125093039):
should be in `logic.basic`

#### [Mario Carneiro (Apr 15 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125093044):
It's `Exists.fst` so you can use projections

#### [Kevin Buzzard (Apr 15 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125093083):
capital E, got it

#### [Kevin Buzzard (Apr 15 2018 at 02:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125093090):
you use Q again

#### [Patrick Massot (Apr 15 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125106157):
```quote
OK well seeing as it's your birthday I de-grumped the docs a bit.
```
I think it still misses the main point of using filters: you have limits at a point and limits when a real variable or a natural number goes to infinity gathered in a single definition. For instance uniqueness of limit that you mention in your doc is proved for all three (and more) situations at once. This has nothing to do with "non-mathematical points such as running times".

#### [Kevin Buzzard (Apr 15 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125107091):
I just don't know anything about how filters are used in practice so am in no position to be able to write those parts of the docs properly. I've never had to use them before and I don't really care about explaining them for this reason; I just wanted to get down the things I needed to know myself.

#### [Johannes Hölzl (Apr 15 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125116397):
@**Kevin Buzzard**  just added your documentation, I guess we can add more comments on filters later.
I think one problem why there is not a lot of knowledge about filters (or nets) in math, is that it is obvious and usually something you don't need to think about. But we are in a formal system, so we are either forced to generalize over limits (using filters or nets) or we produce a lot of duplication (as Mario and Patrick mentioned). We can avoid them and define things like `compact` using open covers etc. But some proofs get much more concise using the fact that you can use the complete lattice (and even category theory) properties properties of filters. Currently it is not always intuitive to work with filters, but maybe with more automation and better syntax notations and support from the parser it may get better.
In the end they are a powerful abstraction, and as most abstractions it takes some time to learn it.

#### [Kevin Buzzard (Apr 15 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125116956):
Yeah, Mario convinced me not to worry about what was a definition and what was a theorem, as long as the theorems were all there.

#### [Sebastien Gouezel (Apr 15 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125120174):
There is a very expressive way to use filters, with the word eventually.
```def eventually {α : Type} (P : α → Prop) (f : filter α) := {x | P x} ∈ f.sets```
Then if you want to say that, eventually, some function u defined on nat is nonnegative, you write
```eventually (λn, 0 ≤ u n) at_top```
If you want to say the same thing around a point x, say (which corresponds to a filter `at x`), you just write it as
```eventually (λy, 0 ≤ f y) (at x)```
In this way, you can also write readable definitions of limits, or essentially whatever involves filters. This is the only way I use filters in Isabelle, and I was essentially never stuck.

#### [Patrick Massot (Apr 15 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125122549):
@**Johannes Hölzl** what do you think about adding (and using) this definition?

#### [Johannes Hölzl (Apr 16 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125137370):
I'm fine with adding this definition, especially with a corresponding quantifier notation (and also its dual the `frequently` quantifier). I'm just not sure if we should abandon the `f.sets` notation or keep both.

#### [Mario Carneiro (Apr 16 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125137483):
I want to refactor the filter stuff so that `.sets` is superfluous, i.e. `s \in f` means `s \in f.sets`. I guess we can support `eventually` if it's a `reducible` definition, but I don't like the idea of duplicating everything for this purpose

#### [Johannes Hölzl (Apr 16 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125138117):
Setting up a `has_mem` for filter is surely a good idea.

