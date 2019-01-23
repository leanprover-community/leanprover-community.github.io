---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/67981quotients.html
---

## Stream: [general](index.html)
### Topic: [quotients](67981quotients.html)

---


{% raw %}
#### [ Patrick Massot (Jul 15 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129697433):
I still don't know much about quotients in Lean. I have the goal `{x : completion α × completion α | (g x.1, g x.2) ∈ r} ∈ uniformity.sets`. And `completion α` is the quotient of something, and `g` is induced by `h` defined before quotienting. So I'd like to rewrite the left hand side as the image under `lam y, (quotient.mk y.1,  quotient.mk y.2)` of the obvious set where  `(g x.1, g x.2)` becomes `(h y.1, h y.2)`. How can I do that? Should I do that?

#### [ Chris Hughes (Jul 15 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129698784):
I proved it, but it's not pretty. I think there's a demand for more advanced versions of cases which can deal with quotients, bound variables, and things like turning `f : α → β × β` to `f₁ f₂ : α → β`.

```lean
import data.set.basic
variables {α : Type*} {β : Type*} [s : setoid α] (g : quotient s → β) (r : set (β × β))

example (h : α → β) (Hh : h = g ∘ quotient.mk) : 
  {x : quotient s × quotient s | (g x.1, g x.2) ∈ r} = 
  (λ a : α × α, (⟦a.1⟧, ⟦a.2⟧)) '' ((λ a : α × α, (h a.1, h a.2)) ⁻¹' r) := 
  Hh.symm ▸ 
  set.ext (λ ⟨a₁, a₂⟩, ⟨quotient.induction_on₂ a₁ a₂ 
    (λ a₁ a₂ h, ⟨(a₁, a₂), h, rfl⟩), 
    λ ⟨⟨b₁, b₂⟩, h₁, h₂⟩, show (g a₁, g a₂) ∈ r, from
    have h₃ : ⟦b₁⟧ = a₁ ∧ ⟦b₂⟧ = a₂ := prod.ext_iff.1 h₂, 
     h₃.1 ▸ h₃.2 ▸ h₁⟩)
```

#### [ Mario Carneiro (Jul 15 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129698842):
`induction` for quotients is a feature I want in lean 4

#### [ Chris Hughes (Jul 15 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129698851):
There's no reason why it can't be done in lean 3 is there?

#### [ Mario Carneiro (Jul 15 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129698890):
I'm not sure how replicable `induction` is

#### [ Chris Hughes (Jul 15 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129698894):
Is it C++?

#### [ Mario Carneiro (Jul 15 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129698895):
mostly

#### [ Chris Hughes (Jul 15 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129698897):
Isn't it just basically `revert, refine quotient.induction_on _ _, intros`

#### [ Chris Hughes (Jul 15 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129698941):
```lean
meta def qindunction (p : parse texpr) (n : parse types.using_ident) : tactic unit :=
do e ← to_expr p,
revert_kdependencies e,
refine ``(quotient.induction_on %%e _),
intro n,
`[intros]
```

#### [ Kevin Buzzard (Jul 15 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129698945):
Here's a really dumb question about quotients. It seems to me that instead of using the quotient type one could just use an inductive type: the quotient of `X` by `r` could be `{x : set X // I am an equivalence class}` and the facts about quotients that don't come for free in type theory could be added as axioms about this subtype. Why is it not done this way?

#### [ Kevin Buzzard (Jul 15 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129698949):
Then quotients would be easier to think about

#### [ Mario Carneiro (Jul 15 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129698951):
Sure, you can do that

#### [ Chris Hughes (Jul 15 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129698953):
Computablity perhaps?

#### [ Mario Carneiro (Jul 15 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129698954):
some facts need the axiom of choice

#### [ Mario Carneiro (Jul 15 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129698955):
and it's not data when you do that

#### [ Chris Hughes (Jul 15 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129698961):
It's very nice to have the definitional reduction of `quotient.lift`

#### [ Mario Carneiro (Jul 15 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129698962):
You can't get that with any construction

#### [ Mario Carneiro (Jul 15 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699003):
and that adds real power - `funext` is *proven using quotients*

#### [ Patrick Massot (Jul 15 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699004):
Thank you very much Chris!

#### [ Patrick Massot (Jul 15 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699006):
I hope I'll be able to use that.

#### [ Mario Carneiro (Jul 15 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699009):
In fact, I highly recommend reading the proof of `funext`. It's quite the mind bender

#### [ Patrick Massot (Jul 15 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699018):
This is explained in TPIL

#### [ Mario Carneiro (Jul 15 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699021):
It's really not obvious why you can't use set-quotients to do the same proof

#### [ Kevin Buzzard (Jul 15 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699022):
oh my goodness Chris is posting meta code. How things move on! Two weeks ago he was asking me what a monad was.

#### [ Patrick Massot (Jul 15 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699068):
Kevin, I don't understand why you'd want this set-theoretic construction. I actually spend quite a lot of time explaining to my students that this construction is a lie. What matter about quotients are the axioms enforced in Lean.

#### [ Patrick Massot (Jul 15 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699086):
To me the set theoretic quotient is the same level of lie as the Kuratowski pair definition

#### [ Mario Carneiro (Jul 15 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699088):
But an obvious question with that is why quotients and not other things?

#### [ Kevin Buzzard (Jul 15 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699127):
Oh that's an interesting comment Patrick. The truth of the matter was that I was watching a school play with one of my kids in, which turned out to be over three hours long, and so I spent most of the last 90 minutes thinking about other ways of doing quotients in my head in the dark

#### [ Patrick Massot (Jul 15 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699144):
Mario, I'm not sure what is "that" in your latest message

#### [ Mario Carneiro (Jul 15 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699157):
Why do quotients get an axiomatic definition but, say, real numbers don't?

#### [ Mario Carneiro (Jul 15 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699207):
is there a sense in which lean's type formers are "complete" with quotients but not without?

#### [ Patrick Massot (Jul 15 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699212):
I think most people in France teach the set-theoretic quotient and never explicitly say it's a lie. Students are expected to magically understand what really matters

#### [ Kevin Buzzard (Jul 15 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699213):
```quote
In fact, I highly recommend reading the proof of `funext`. It's quite the mind bender
```
Funnily enough I tried this only recently, when I realised that I was going to have to learn how to use quotients. 

I have been writing about "the three basic kinds of types", trying to explain them to mathematicians. All this came from my trying to figure out why there were three basic kinds of types at all -- inductive types and pi types sure, and now quotients -- why can't we just do them with inductive types? In some sense Patrick's comments are quite a good answer to this -- I am now thinking that the construction I've known all my working life is just a hack.

#### [ Mario Carneiro (Jul 15 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699224):
That's actually a good question - why are quotients not an inductive type?

#### [ Patrick Massot (Jul 15 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699225):
and I think almost no university seriously teaches the construction of real numbers

#### [ Kevin Buzzard (Jul 15 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699267):
Quotients as sets of sets is the ZFC construction of the object which has the right universal property.

#### [ Mario Carneiro (Jul 15 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699268):
HoTT has an interesting answer to this: they are a "higher inductive type"

#### [ Mario Carneiro (Jul 15 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699270):
The point is that in type theory, set-quotients do not have the right universal property

#### [ Kevin Buzzard (Jul 15 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699274):
?

#### [ Mario Carneiro (Jul 15 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699278):
They lack the computation rule

#### [ Kevin Buzzard (Jul 15 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699280):
which one is that?

#### [ Mario Carneiro (Jul 15 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699281):
`lift f (mk a) = f a`

#### [ Chris Hughes (Jul 15 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699321):
It is true, but not `rfl`

#### [ Kevin Buzzard (Jul 15 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699323):
"lack" :-)

#### [ Mario Carneiro (Jul 15 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699325):
because in type theory *definitional equality matters*

#### [ Kevin Buzzard (Jul 15 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699326):
Yes!

#### [ Kevin Buzzard (Jul 15 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699333):
I understand this much better than I did a few months ago. Perhaps this is obvious to CS people. I think it really needs to be spelt out to mathematicians.

#### [ Mario Carneiro (Jul 15 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699334):
HoTT is of course all about exploring the nontrivial structure of equality, where definitional equality is the equalest equal

#### [ Kevin Buzzard (Jul 15 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699372):
All equalities are equal, but some are more equal than others.

#### [ Patrick Massot (Jul 15 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699375):
Kevin, did you read the first chapter of the HoTT book?

#### [ Kevin Buzzard (Jul 15 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699376):
no

#### [ Patrick Massot (Jul 15 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699377):
You should

#### [ Mario Carneiro (Jul 15 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699380):
It's a really good intro to dependent type theory

#### [ Kevin Buzzard (Jul 15 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699381):
Thanks. I'm always looking for new things to read, even though reading is so 1990s

#### [ Kevin Buzzard (Jul 15 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699387):
My kids don't read anything.

#### [ Kevin Buzzard (Jul 15 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699390):
They just google

#### [ Mario Carneiro (Jul 15 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699393):
Also you will find some decent material on HITs there

#### [ Patrick Massot (Jul 15 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699394):
http://saunders.phil.cmu.edu/book/hott-online.pdf

#### [ Mario Carneiro (Jul 15 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699395):
HoTT has some much more exotic HITs than quotients

#### [ Mario Carneiro (Jul 15 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699437):
like "the circle" `S1`, which is "inductively generated" by `base : S1` and `loop : base = base`

#### [ Mario Carneiro (Jul 15 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699441):
In HoTT you can prove that `loop` is not `rfl`

#### [ Kevin Buzzard (Jul 15 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699448):
In HoTT can you define the notion of a finite set? Can you use the axiom of choice?

#### [ Mario Carneiro (Jul 15 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699451):
You can do pretty much everything in classical math

#### [ Mario Carneiro (Jul 15 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699504):
You have to state the axiom of choice carefully to be consistent with univalence (lean's `choice` is not consistent with univalence), but it is a reasonable interpretation of ZFC-esque axiom of choice

#### [ Mario Carneiro (Jul 15 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699511):
it's not provable though, it's an axiom

#### [ Mario Carneiro (Jul 15 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699552):
there are more details in the HoTT book for how the axiom of choice works

#### [ Mario Carneiro (Jul 15 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699553):
it uses the "propositional truncation" as a substitute for the `Prop` universe

#### [ Patrick Massot (Jul 15 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699558):
I was not referring to all this. I really mean Chapter one, about type theory, only slightly biased towards exotic stuff that will follow

#### [ Mario Carneiro (Jul 15 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699602):
Yes, of course that's more advanced material and more HoTT-y stuff

#### [ Kevin Buzzard (Jul 15 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699604):
I know you weren't Patrick, but I mentioned to my old university set theory teacher that I was now doing type theory and he asked me if it was HoTT and if so then could I define a finite set (because he'd heard that it was problematic)

#### [ Kevin Buzzard (Jul 15 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699605):
and I told him that it wasn't and that I had no idea about his question

#### [ Mario Carneiro (Jul 15 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699618):
If you are specifically interested in finite sets in HoTT, I've had a conversation with Floris on that exact topic (he's our resident expert)

#### [ Mario Carneiro (Jul 15 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699658):
Constructively, there are a few variations on what "finite" means

#### [ Mario Carneiro (Jul 15 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699660):
The simplest is something isomorphic to fin n

#### [ Mario Carneiro (Jul 15 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699665):
If we call that one "finite", then "subfinite" means a subset of a finite set

#### [ Kevin Buzzard (Jul 15 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699667):
and equality is undecidable...

#### [ Mario Carneiro (Jul 15 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699702):
and then there is an image of a finite set (I forget what this is called), and a subset of an image of a finite set

#### [ Kevin Buzzard (Jul 15 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699707):
If I assume AC and propext then all these are the same, right?

#### [ Patrick Massot (Jul 15 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699708):
Forget about HoTT Kevin, it's all constructive

#### [ Patrick Massot (Jul 15 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699713):
We have maths to do instead

#### [ Mario Carneiro (Jul 15 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699717):
With LEM, you know that the subset is decidable so subfinite and finite are the same

#### [ Mario Carneiro (Jul 15 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699753):
for images, I guess you can get a section out using AC so that becomes the same as finite too

#### [ Mario Carneiro (Jul 15 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699764):
I don't think you need propext for anything

#### [ Mario Carneiro (Jul 15 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699765):
Actually unique choice might be enough for the section thing, since it's a finite choice

#### [ Mario Carneiro (Jul 15 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699782):
Oh yeah, there's another gradation: "isomorphic to fin n" or "merely isomorphic to fin n"

#### [ Mario Carneiro (Jul 15 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699822):
where "merely" is a HoTT adjective meaning "in Prop" basically

#### [ Mario Carneiro (Jul 15 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129699825):
that's like the difference between "fintype" and "finite" in lean

#### [ Kevin Buzzard (Jul 15 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129700080):
```quote
You can do pretty much everything in classical math
```


```quote
Forget about HoTT Kevin, it's all constructive
```

?

#### [ Mario Carneiro (Jul 15 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129700138):
It's very constructivity-aware, even if there are some classical axioms that are admissible

#### [ Mario Carneiro (Jul 15 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129700141):
Lean's choice axiom is much more heavy handed

#### [ Mario Carneiro (Jul 15 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129700150):
It's comparable to the status of equality reflection as a type theory axiom

#### [ Mario Carneiro (Jul 15 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129700190):
lean doesn't have it, and as a result you have to do all these casts and things

#### [ Mario Carneiro (Jul 15 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129700193):
if you have equality reflection then it is much more like working in ZFC, where typing is just a provable property like any other

#### [ Mario Carneiro (Jul 15 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129700242):
So even though you can do everything in ZFC in lean, stuff that really doesn't respect types gets messy in lean

#### [ Mario Carneiro (Jul 15 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129700243):
(I don't know how helpful this is as an analogy)

#### [ Reid Barton (Jul 15 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/129701773):
For inducting on quotients, isn't there `induction _ using quot.ind`?

#### [ Johan Commelin (Sep 26 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/134662694):
Currently there is `quotient_module.quotient` and `quotient_ring.quotient`. They are both defined in terms of `_root_.quotient`. To me it would make sense to define a `quotient_ring` as a `quotient_module` and then add the extra algebraic structure.

#### [ Johan Commelin (Sep 26 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/134662711):
Is there a reason why this is not a good idea?

#### [ Patrick Massot (Sep 26 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/134665140):
Mario is working on module quotient: https://www.twitch.tv/videos/314424360

#### [ Patrick Massot (Sep 26 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/134665214):
It's exactly how I imagined Mario doing Lean before meeting him in Orsay

#### [ Patrick Massot (Sep 26 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/134665218):
No, wait!

#### [ Patrick Massot (Sep 26 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/134665227):
It seems that first thing was actually a trailer for the Venom movie

#### [ Patrick Massot (Sep 26 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/134665228):
Now I can see emacs

#### [ Johan Commelin (Sep 26 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/134665632):
Too bad I'm on a train... I don't think they want me to stream twitch over the train wifi

#### [ Kevin Buzzard (Sep 26 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/134665660):
The Dutch have free WiFi on every train in the country and then just moan about how slow it is ;-)

#### [ Johan Commelin (Sep 26 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/134665783):
I'm in Germany now. But yes, there is pretty good wifi coverage on the high speed trains in NL, DE, and FR

#### [ Johan Commelin (Sep 26 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotients/near/134665798):
I don't have experience with other countries


{% endraw %}
