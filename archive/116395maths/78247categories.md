---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/78247categories.html
---

## Stream: [maths](index.html)
### Topic: [categories](78247categories.html)

---


{% raw %}
#### [ Reid Barton (Sep 05 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133380177):
This new functor arrow doesn't seem to have an abbreviation in emacs.
'to input: type "C-x 8 RET 2964" or "C-x 8 RET RIGHTWARDS HARPOON WITH BARB UP ABOVE RIGHTWARDS HARPOON WITH BARB DOWN"'

#### [ Reid Barton (Sep 05 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133403401):
Scott, I see in the latest version of limits, `is_limit` and so on have become classes. I'm not sure how workable that will be because there are so many different ways to obtain new (co)limits from old ones. Right now I'm proving that restriction along a cofinal functor preserves colimit cones, but also consider that a left adjoint preserves colimits, and pushout squares glue together, and the other stuff I proved in my colimit_lemmas.lean file. I think this is too much to ask of the class system, and I worry that making the `is_*` types classes will make it more difficult to apply all these facts about (co)limits.

#### [ Reid Barton (Sep 05 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133404897):
We still don't have `is_singleton` do we?
```lean
variables (C : Type u) [𝒞 : category.{u v} C]
include 𝒞

def is_connected : Type u := is_singleton (quot (λ (a b : C), nonempty (a ⟶ b)))
```

#### [ Reid Barton (Sep 05 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133404913):
Lean taught me that this is the True Definition.

#### [ Kenny Lau (Sep 05 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133404989):
so the empty graph isn't connected?

#### [ Reid Barton (Sep 05 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133405066):
You missed a discussion on this topic in Orsay.

#### [ Reid Barton (Sep 05 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133405067):
https://ncatlab.org/nlab/show/connected+category

#### [ Johannes Hölzl (Sep 05 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133405186):
Shouldn't `is_singleton` be a `Prop`?

#### [ Reid Barton (Sep 05 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133405317):
That is an interesting question. If I make it constructive, then I can prove the result about cofinal functors preserving colimits constructively as well. It's actually a bit subtle--you need to get your hands on an inhabitant of C, but if you define connectedness in terms of the existence of zigzags, then you don't need the zigzags constructively, because they are only used to prove equalities.

#### [ Reid Barton (Sep 05 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133405369):
Currently, I simply have `def is_singleton (α : Type*) := α ≃ unit`.
This plus the above definition gives the correct amount of constructiveness.

#### [ Reid Barton (Sep 05 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133405456):
`is_colimit` is not a Prop (it is a subsingleton though), because it includes the data of how to construct the map given by the universal property. In order to build that map in my setting, I need to know that certain categories are connected in the above constructive sense.

#### [ Reid Barton (Sep 05 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133405470):
I'm still not sure whether these distinctions between Prop and subsingletons are worth making in the context of category theory.

#### [ Reid Barton (Sep 05 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133405561):
For context, I proved basically the implication 1 => 3 at https://ncatlab.org/nlab/show/final+functor#properties.

#### [ Reid Barton (Sep 05 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133405580):
There it is stated as "a map ... is an isomorphism", which is also a proposition classically which has constructive content.

#### [ Reid Barton (Sep 05 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133405669):
It's kind of fun to see how all these constructive aspects relate to one another, but I'm not sure how useful it is and there are some associated minor annoyances.

#### [ Reid Barton (Sep 05 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133405675):
So: I don't know. :)

#### [ Reid Barton (Sep 06 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133405841):
Probably either the name or the definition is wrong though.

#### [ Kevin Buzzard (Sep 06 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133405857):
yeah, that's definitely path-connected ;-)

#### [ Reid Barton (Sep 06 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133407262):
Haha :) The distinction doesn't exist to a homotopy theorist.
I remember being very confused when I couldn't prove that an arbitrary product of discrete topological spaces is discrete. Then I realized it was only true up to weak homotopy equivalence...

#### [ Scott Morrison (Sep 06 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133418582):
I think it's relatively painless to turn `is_limit` and friends back into structures (not classes). I guess what I desired was that the fact that `is_limit c` is a subsingleton should imply that it's okay that there are different ways to construct it. But I understand that Lean is not actually that clever, and we will run into problems where two typeclass instances look different, even though a `subsingleton` instance is available.

#### [ Scott Morrison (Sep 06 2018 at 05:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133418641):
I do wonder if it could be a plausible addition to the typeclass mechanism: whenever we find that we using two instances that don't agree, first check for an instance of `subsingleton` before complaining about it.

#### [ Scott Morrison (Sep 06 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133431137):
So, @**Reid Barton**, I guess I don't really understand what the problem is with having `is_limit` being a typeclass. Certainly there is a problem with having too many instances (because we'll get colliding instances), but nothing particularly forces us to mark constructions as instances.

#### [ Scott Morrison (Sep 06 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133431150):
Having "really canonical" ones, like the one that `has_limits` provides, seems quite helpful.

#### [ Scott Morrison (Sep 06 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133431224):
As you point out, we'll certainly want to use non-instance instances of `is_limit` and friends, so I agree a good change could be to change it back to a `structure` and just add the `class` attribute afterwards, so the syntax is as usual for structures.

#### [ Scott Morrison (Sep 06 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133431231):
I'm also open to being convinced it just shouldn't be a class at all.

#### [ Reid Barton (Sep 06 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133431408):
I think the structure + attribute [class] option will probably address my concerns. I do see the use of instance lookup for common cases.

#### [ Reid Barton (Sep 06 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133431728):
The problem with just a class is that it's useful to handle these `is_limit` values manually, as you say, and maybe I am just bad at dealing with classes, but I find there's more friction there. For example maybe you have a cone which is only propositionally equal to one which you have a lemma about. Then it's easier to `convert` the lemma application and fix up the resulting subgoals.

#### [ Reid Barton (Sep 06 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133431818):
I tried making my `is_colimit_of_is_cofinal` into an instance and it did work in the simple use case later... provided I made `is_cofinal` an instance too. It's infectious!

#### [ Reid Barton (Sep 06 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133431838):
Made `is_cofinal` a class, I mean.

#### [ Johan Commelin (Sep 06 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133431861):
That's automation, man!

#### [ Reid Barton (Sep 06 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133432716):
> For example maybe you have a cone which is only propositionally equal to one which you have a lemma about.

I guess the point here is that being a limit cone is a property of a diagram, and diagrams have morphisms in them, and it's really common to have non-syntactic or even non-definitional equalities between morphisms (we call them commutative diagrams). Whereas for the class `group`, for instance, it's much less common to have non-syntactic equalities *between groups*.

#### [ Scott Morrison (Sep 06 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133433168):
Okay: for now I will try out having them as `structure` with `class` added after the fact. If that doesn't go well, complain and we can just go back to bare structures. I think you're making more use of limits than I am, so I'm happy to follow your direction.

#### [ Scott Morrison (Sep 06 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133433224):
Also on the topic of categories, I'd be curious @**Reid Barton** and @**Johan Commelin** if you have any thought about my concerns re: @**Johannes Hölzl**'s nice framework for building concrete categories from typeclasses.

#### [ Scott Morrison (Sep 06 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133433227):
https://github.com/leanprover/mathlib/pull/316#issuecomment-419039990

#### [ Scott Morrison (Sep 06 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133433231):
My main concern is that it boxes us in to using lots of sigma types and subtypes, where my instinct had been to define lots of custom structures. :-)

#### [ Johan Commelin (Sep 06 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133433281):
hmmm... ring_homs don't form an additive group... but never mind

#### [ Johan Commelin (Sep 06 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133433449):
@**Scott Morrison** One of the reasons I was asking about definitions by meta code yesterday was for this sort of thing. If we make `concrete_category` meta, then it could make all those bundled defintions for us, couldn't it?

#### [ Johan Commelin (Sep 06 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133433471):
But I'm still too much of an amateur to know what the pros and cons are of these approaches.

#### [ Johan Commelin (Sep 06 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133433482):
My gut feeling is that if Johannes writes something, I won't be able to improve it. (Maybe next year :smiley:)

#### [ Reid Barton (Sep 06 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133433564):
oh I hadn't seen those comments yet, thanks.

#### [ Reid Barton (Sep 06 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133434056):
I also had the same, vague concern about your point 1. I hadn't thought of your point 2, will have to think about that one some more.
I think the example you gave of homeomorphisms isn't that compelling, because you could also build (Top, homeos) as the category- (or groupoid-)of-isomorphisms-in the concrete-category Top. Maybe we can come up with a more interesting example?

#### [ Reid Barton (Sep 06 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133434715):
I commented about point 1 on the issue.

#### [ Kevin Buzzard (Sep 06 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133434982):
```quote
I guess what I desired was that the fact that `is_limit c` is a subsingleton should imply that it's okay that there are different ways to construct it. But I understand that Lean is not actually that clever, and we will run into problems where two typeclass instances look different, even though a `subsingleton` instance is available.
```
Chris Hughes had typeclass problems with `fintype` even though it's a subsingleton -- he would occasionally get two instances kicking around and then rewrites would start to fail. He even talked at some point about writing a tactic which might solve his problems, but somehow tactic-writing is not our fort\'e in London, nobody can do it yet, and he just ended up with too many questions which nobody could answer.

Even more interesting -- `is_linear_map` is a `Prop` but Johannes made it a structure not a class. I talked to him about this a bit in Orsay. My impression was that he couldn't see the point of adding it to the type class inference system, because the instance that you want to trigger -- composition of two linear maps is a linear map -- tends not to trigger, because in functional languages people compose functions by writing them next to each other rather than using `function.comp`. We now have a hybrid system where `is_group_hom` is a class and `is_linear_map` is not.

#### [ Scott Morrison (Sep 06 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133435098):
> hmmm... ring_homs don't form an additive group... but never mind

Ooops. :flushed: I'll remove the evidence of that one. :-) There are plenty of less-wrong examples, of course.

#### [ Scott Morrison (Sep 06 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133435184):
The question about `is_linear_map` being problematic, because people write their functions using lambdas, could be solved by educating everyone to not use lambdas when you're hoping to use typeclass inference, I guess. It's not totally unreasonable. :-)

#### [ Reid Barton (Sep 06 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133435273):
And here I have been wondering how hard it would be to get something like lambda syntax for functors...

#### [ Kevin Buzzard (Sep 06 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133435395):
I actually engaged with Scott's category theory library for the first time yesterday, thanks to @**Ned Summers** peppering me with questions, and I must say it was a bit scary having to do all the morphism composition using some morphism composition operator...

#### [ Reid Barton (Sep 06 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133435403):
I tried writing down just the expression "colim_{j in J} lim_{i in I} F(i, j)" and it turned into something ugly like `colimit ((curry.map F).comp lim)`

#### [ Reid Barton (Sep 06 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133435457):
Kevin, that's why most of my files contain the magic words ``local notation f ` ∘ `:80 g:80 := g ≫ f`` :)

#### [ Scott Morrison (Sep 06 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133435901):
@**Kevin Buzzard**, were you referring to having to write some composition operator, rather than a lambda, or to the fact that the composition operator is "backwards"?

#### [ Scott Morrison (Sep 06 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133435982):
(I've been thinking a lot recently about monoidal categories enriched in a braided category, and here it really matters that you write composition "correctly", because every time you move symbols past each other you have to keep track of a braiding.)

#### [ Kevin Buzzard (Sep 06 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133436152):
I can handle "backwards", it was the shock of having to do it at all.

#### [ Scott Morrison (Sep 06 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133436515):
@**Reid Barton**, unfortunately I'm having trouble with the `structure` + `attribute [class]` approach: I can't ever get it to infer the `is_limit` instances, making it pretty useless.

#### [ Scott Morrison (Sep 06 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133436520):
I guess I will go back to just structures.

#### [ Kevin Buzzard (Sep 06 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133437816):
If it's any help, I think this (`structure + attribute [class]`) is how topological spaces are set up.

#### [ Ned Summers (Sep 06 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133455791):
Hey guys,

I've got a situation where I have two objects of a category X and Y, and a theorem that says X = Y. Obviously there then is a f  : X ⟶ Y corresponding to the identity morphism on X (or the identity morphism on Y).  I was wondering if writing/using this has been dealt with so far in the mathlib category theory content?

 (this is in the context of lean asking for something of type Y ⟶ Y. I have one of type X ⟶ X in mind but lean is not happy if I give it that here (except using cast or eq.rec and these have already caused a lot of trouble). Kevin and I figured it might be easier to instead compose on either side of this choice these morphisms X ⟶ Y and Y ⟶ X corresponding to those identities. Any ideas about that also welcomed!)
Thanks!

#### [ Reid Barton (Sep 06 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133456083):
Yes, there is something for exactly this situation. See `eq_to_iso` in `category_theory.isomorphism`.

#### [ Reid Barton (Sep 06 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133456175):
And there are a couple simp lemmas there which are supposed to make proving things about composition with these morphisms easier than proving things about `eq.rec`.

#### [ Reid Barton (Sep 06 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133463164):
@**Scott Morrison**, do you have some conversions between `equiv` and `iso` in Set somewhere?

#### [ Scott Morrison (Sep 07 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133475856):
No, I don't have that conversion, but it should be added!

#### [ Scott Morrison (Sep 07 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133475863):
"equiv is iso to iso"? :-)

#### [ Kenny Lau (Sep 07 2018 at 03:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133483585):
@**Scott Morrison** Do we have Yoneda? :D

#### [ Scott Morrison (Sep 07 2018 at 03:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133483801):
Sure, it's in <https://github.com/semorrison/lean-category-theory/blob/master/src/category_theory/yoneda.lean>. It's slowly getting towards the head of the queue for PR'ing into mathlib...

#### [ Reid Barton (Sep 10 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133627435):
Mario, do you have an opinion on whether "the category C is connected" and "the functor F is cofinal" should be props or subsingletons?

#### [ Reid Barton (Sep 10 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133627486):
I have a version using subsingletons and it means you can prove cofinal functors preserve colimits constructively (e.g., produce an inverse to the induced map) which is kind of cool, but now I feel it's probably not worth the hassle

#### [ Mario Carneiro (Sep 10 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133627621):
https://ncatlab.org/nlab/show/final+functor
> A functor F:C→DF : C \to D is final (often called cofinal)

WHYY

#### [ Mario Carneiro (Sep 10 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133627622):
> Dually, a functor is initial (sometimes called co-cofinal)

wtf

#### [ Mario Carneiro (Sep 10 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133627628):
I think I'm co-confused

#### [ Mario Carneiro (Sep 10 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133627825):
To me, "connected" sounds like a Prop, I'm not sure how to state it naturally as a subsingleton without using `trunc`

#### [ Mario Carneiro (Sep 10 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133627838):
The definition of cofinal appears to use "nonempty and connected", which sounds like an "is_singleton" statement, which I can see usefully as a type. Is there a natural choice of inhabitant in this case?

#### [ Mario Carneiro (Sep 10 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133627882):
I think that being able to construct inverses to given maps is one of the more relevant uses of doing category theory constructively

#### [ Reid Barton (Sep 10 2018 at 04:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133633778):
Yeah the terminology is unfortunate. The "co-" is not the dualizing "co-", but the "together" one, like the categories have the same behavior as you go towards the "end". In practice people only care about (co)final functors and not the other side I think.

#### [ Reid Barton (Sep 10 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133633825):
> Is there a natural choice of inhabitant in this case?

There isn't automatically one in general but typically when you prove a functor is cofinal there will be an obvious way to choose an inhabitant.

#### [ Reid Barton (Sep 10 2018 at 04:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133633979):
Oh yes, by connected I mean to include nonempty. That's the only part which is data

#### [ Reid Barton (Sep 10 2018 at 04:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133634088):
The connected components are `quot (λ (a b : C), nonempty (a ⟶ b))` (for some reason I don't remember ever seeing this very simple and Lean-friendly definition), and then you need to say this type has exactly one inhabitant, which can be constructively or not.

#### [ Reid Barton (Sep 10 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133634200):
I guess I'll continue to try with the constructive definition if you don't have a strong opinion. The pros and cons of both approaches are pretty minor


{% endraw %}
