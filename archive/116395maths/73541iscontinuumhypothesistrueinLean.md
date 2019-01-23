---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/73541iscontinuumhypothesistrueinLean.html
---

## Stream: [maths](index.html)
### Topic: [is continuum hypothesis true in Lean?](73541iscontinuumhypothesistrueinLean.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 11 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20continuum%20hypothesis%20true%20in%20Lean%3F/near/126419454):
Is the continuum hypothesis true in Lean’s model of ZFC?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (May 11 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20continuum%20hypothesis%20true%20in%20Lean%3F/near/126420089):
I believe that in the set-theoretic model of Lean, the inner model of ZFC is isomorphic to $$V_\kappa$$ where $$\kappa$$ is an inaccessible cardinal in the "outer" model of ZFC.  So CH should be independent as usual.  You can probably prove the independence in Lean using the typical Cohen forcing.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 11 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20continuum%20hypothesis%20true%20in%20Lean%3F/near/126420102):
it’s a model, it can’t be independent

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (May 11 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20continuum%20hypothesis%20true%20in%20Lean%3F/near/126420172):
Oh yes, what you can (directly) prove inside Lean is of course only that CH is independent of ZFC...  However CH is still independent of Lean.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 11 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20continuum%20hypothesis%20true%20in%20Lean%3F/near/126432647):
@**Gabriel Ebner** I mean, we do have a model of ZFC, where "CH" is one specific sentence that can either be true or false

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 11 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20continuum%20hypothesis%20true%20in%20Lean%3F/near/126432655):
so I wonder if it is true or false in that specific model of ZFC

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 11 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20continuum%20hypothesis%20true%20in%20Lean%3F/near/126432659):
@**Mario Carneiro** maybe you have some idea

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (May 11 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20continuum%20hypothesis%20true%20in%20Lean%3F/near/126432932):
We have a model of ZFC inside a model of Lean inside a model of ZFC (+ some large cardinals); and CH is true in the inner ZFC model iff CH is true in the outer ZFC model.  Since we can choose CH or ¬CH for the outer ZFC model, Set⊧CH should be independent of Lean.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 11 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20continuum%20hypothesis%20true%20in%20Lean%3F/near/126432950):
why is CH true in the inner model iff CH is true in the outer model?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 11 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20continuum%20hypothesis%20true%20in%20Lean%3F/near/126432955):
I have a hard time believing your claim, since a model has a valuation making statements either true or false, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 11 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20continuum%20hypothesis%20true%20in%20Lean%3F/near/126432961):
things can't be independent in a model

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 11 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20continuum%20hypothesis%20true%20in%20Lean%3F/near/126432968):
if a sentence phi is independent of a theory, then phi is true in some models of the theory and false in others

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 11 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20continuum%20hypothesis%20true%20in%20Lean%3F/near/126432975):
that's what i'm taught

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (May 11 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20continuum%20hypothesis%20true%20in%20Lean%3F/near/126433136):
```quote
why is CH true in the inner model iff CH is true in the outer model?
```
I haven't worked out the details, but I think `Set.{u}` should be isomorphic to $$V_\kappa$$ for the inaccessible cardinal $$\kappa$$ that we use as the interpretation for `Type u` (maybe off by one or two universe levels).  Then `Set.{u}` has the same cardinals and real numbers as the outer ZFC model.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 11 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20continuum%20hypothesis%20true%20in%20Lean%3F/near/126433143):
Indeed, CH is either true or false in the model. It is true in the model if it is true in the metatheory, and false in the model if it is false in the metatheory.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 11 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20continuum%20hypothesis%20true%20in%20Lean%3F/near/126433150):
hmm...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 11 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20continuum%20hypothesis%20true%20in%20Lean%3F/near/126433212):
I refuse to believe it..

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 11 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20continuum%20hypothesis%20true%20in%20Lean%3F/near/126433336):
This is assuming we use the interpretation in which `t : Type n` means `t` is an element of the universe $$U_n$$ (for some chosen universes $$U_0 \subset U_1 \subset \cdots$$), and `a \to b` means the set of all maps from the set of `a` to the set of `b`, etc.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 11 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20continuum%20hypothesis%20true%20in%20Lean%3F/near/126433398):
can this actually be proved? i.e. if we assume CH outside, can we prove CH inside, and if we assume ¬CH outside, can we prove ¬CH inside?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 11 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20continuum%20hypothesis%20true%20in%20Lean%3F/near/126433402):
or is this one of those things that would take 1000 lines?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (May 11 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20continuum%20hypothesis%20true%20in%20Lean%3F/near/126433429):
```quote
can this actually be proved? i.e. if we assume CH outside, can we prove CH inside, and if we assume ¬CH outside, can we prove ¬CH inside?
```
Neither CH nor ¬CH follows from the axioms of Lean.  It is just that CH or ¬CH can be true in different models of Lean.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 11 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20continuum%20hypothesis%20true%20in%20Lean%3F/near/126433435):
assume, meaning have it as a variable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 11 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20continuum%20hypothesis%20true%20in%20Lean%3F/near/126433483):
Assuming CH outside isn't going to help you construct any proofs, presumably.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 11 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20continuum%20hypothesis%20true%20in%20Lean%3F/near/126433488):
but you said that if CH is true outside then CH is true inside

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 11 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20continuum%20hypothesis%20true%20in%20Lean%3F/near/126433492):
I mean, proofs inside the system. It will be true inside the model.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (May 11 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20continuum%20hypothesis%20true%20in%20Lean%3F/near/126433592):
Whether a proposition is provable in Lean is a $$\Sigma^0_1$$-statement, and hence it does not really matter what metatheory you have.  The Lean-provable statements are the same whether you work in ZFC, Lean, Coq, PA, or even weaker systems of arithmetic.  (Well, assuming consistency.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 11 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20continuum%20hypothesis%20true%20in%20Lean%3F/near/126433689):
interesting

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (May 11 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20continuum%20hypothesis%20true%20in%20Lean%3F/near/126433984):
Essentially, this just means that all these formal systems agree on whether programs terminate on given inputs.  (The Lean-provable statements are a computably enumerable set.)  In order to represent program execution, you only need a bit of natural numbers.  So pretty much every system that has natural numbers and can evaluate addition, multiplication, and comparison for concrete numbers knows exactly what theorems Lean can prove.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 12 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20continuum%20hypothesis%20true%20in%20Lean%3F/near/126440848):
In lean, you can only "assume CH inside". So if you assume it the proof is trivial by reference to the assumption. In order to "assume CH outside" you would have to do a proof at the meta level, in the outer ZFC system. In this case you would be able to prove a statement like "if CH is true (i.e. true outside), then lean |= CH is true". You will also be able to prove that (lean |- CH) is false (without any CH assumptions), because if lean |- CH then ZFC |- CH, and then you can refer to Godel and Cohen to show that is impossible.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 12 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/is%20continuum%20hypothesis%20true%20in%20Lean%3F/near/126440920):
(actually if lean |- X then ZFC+inaccessibles |- X, but it is known that large cardinals don't affect the independence of CH.)

