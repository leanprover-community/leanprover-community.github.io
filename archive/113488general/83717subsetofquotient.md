---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/83717subsetofquotient.html
---

## Stream: [general](index.html)
### Topic: [subset of quotient](83717subsetofquotient.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134956599):
For the perfectoid project we often need to work with subsets of quotient types. A mathematician would write
```lean
def foobar := {x : QuotType | formula x}
```
and afterwards bother with the proof obligation of showing that it is well-defined. Can we mimic this in Lean?
I imagine that this subset notation would call the appropriate `lift` lemma, and generate a proof obligation that we can prove after the subset notation. Something like
```lean
def foobar := {x : QuotType | formula x} (by proof_of_soundness)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134956665):
Maybe we could have `{ .. | .. } is_well_defined ..` be some fancy notation for this type of things?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 01 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134956774):
Do you mean `{[[x]] : QuotType | formula x}`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134956817):
Does that work?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Oct 01 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134956818):
Looks like the image of `quotient.mk` of some set.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Oct 01 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134956832):
`quotient.mk '' {x | formula x}`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 01 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134956838):
there are two ways of forming subquotient

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 01 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134956842):
and a theorem that they are the same

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 01 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134956843):
(in maths, not in Lean)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134956847):
Right, I see where this is going...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134956850):
In particular, they aren't defeq

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 01 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134956970):
few things are

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134956992):
So Chris gives a workaround, but proving that his thing is the same as what I want is non-trivial.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Oct 01 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134957502):
But it's non trivial because there's mathematical content right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134957509):
Right, you have to prove that `formula` is constant on equivalence classes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Oct 01 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134957645):
The harder `lift` definition is probably the best one to use.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134957658):
Yes, so I don't mind proving something hard, but I would like to keep a readable definition. Hence this question.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134958313):
To keep the definition readable, make the well definedness part a lemma that you prove immediately before

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959001):
@**Mario Carneiro** That is certainly an option, but
(1) the definition still won't be able to use subset notation;
(2) it is not what mathematicians are used to. We always define something, and afterwards fill in the proof obligation of showing that the definition is well-defined.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959021):
I think that it matches mathematical practice in that you aren't licensed to use the definition until you have proven the well definedness condition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959030):
in lean if you can say it you can use it, so you have to be intercepted right at the definition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959080):
I'm a little confused about what exactly you want to write though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959096):
I completely agree.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959144):
So my suggestion was to *syntactically* prove the well-definedness after the definition. But in fact it is just part of the definition.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959148):
Most importantly, I would like the definition to be *very* readable.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959149):
Isn't that what `quot.lift` already does?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959155):
Yes. But then my subset notation goes out of the window.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959176):
Can you be more specific?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959189):
Any mathematician who first looks at Lean, and wants to look up the definition of `Spv` in the perfectoid project will not understand anything if he/she sees a `quot.lift`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959229):
That is completely foreign.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959232):
And the stuff that follows it is barely recognisable.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959244):
On the other hand
```lean
def foobar := {x : QuotType | formula x} is_well_defined (by proof_of_soundness)
```
is very readable.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959255):
But my Lean-fu is not sufficient to turn that into valid Lean.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959266):
Currently in the perfectoid project we are stacking 5 subquotients on top of each other.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959302):
And it becomes really horrible.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959324):
(Well, *currently* there is no `quot`, but that isn't tenable either. So we need the `quot`, and we'dd like it to be readable.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 01 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959443):
I am confused about why your def is not valid lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 01 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959455):
I wrote what I thought you were trying to say but you have not adopted my change

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959507):
Sorry, which change are you talking about?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 01 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959509):
I mean, I wrote what I thought was invalid lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 01 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959513):
I put the equiv class notation in

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959525):
Right. So now I tried using Chris's suggestion.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959533):
But then you can define `Spa`, and you get stuck when you want to define the opens.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959614):
To paraphrase Mario:
```quote
But I *do not* want to be thinking about `quot.lift` and `subtype.val` when I am writing a proof
the mindset is completely different, it is a distraction
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959617):
Is your `foobar` stuff about `Spa`? If so can you show what it looks like in situ

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 01 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959618):
All I am saying is that you keep saying that something is invalid lean and it looks fine to me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Oct 01 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959634):
But the definitional equality of `quotient.lift` is really handy. Just give a docstring. Aiming to make your code usable by someone who doesn't know what `quotient.lift` is is probably impossible.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 01 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959650):
And I wrote something which was invalid lean and asked if it was what you meant and all you did was asked me if my invalid lean was valid

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 01 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959708):
So we're clearly at cross purposes. My question is what is invalid about your lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 01 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959722):
Are we talking about `def foobar := {x : QuotType | formula x} is_well_defined (by proof_of_soundness)`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959728):
In the case of `Spa`, I don't think you should try to get defeq just right, because `Spa` itself is not quite a quotient in the way we want it to be anyway

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 01 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959729):
It seems pretty invalid to me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 01 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959735):
I don't have access to lean right now so I'll just shut up and stop adding to the noise

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959782):
@**Kevin Buzzard** Sorry, I finally understand. I think `{[[x]] : QuotType | formula x}` doesn't leave any room for the proof obligation that `formula x` only depends on `[[x]]`. That proof has to go somewhere. Mathematicians also do that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959783):
That's a perfectly valid definition, which means the image of such and such

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959806):
why not `{q : QuotType | formula q}`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959814):
and define `formula q` using a lift

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959816):
```lean
definition Spa (A : Huber_pair) := quotient.mk '' {v : Valuation A | v.is_continuous ∧ ∀ r, r ∈ A⁺ → v r ≤ 1}
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959855):
This is what I have now.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959863):
is `is_continuous` constant on equivalence classes?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959866):
And
```lean
variables (R : Type u₁) [comm_ring R] [decidable_eq R]

structure Valuation (R : Type u₁) [comm_ring R] :=
(Γ   : Type u₁)
(grp : linear_ordered_comm_group Γ)
(val : @valuation R _ Γ grp)

namespace Valuation

instance : has_coe_to_fun (Valuation R) :=
{ F := λ v, R → with_zero v.Γ, coe := λ v, v.val.val }

instance linear_ordered_value_group {v : Valuation R} : linear_ordered_comm_group v.Γ := v.grp

end Valuation

instance Spv.setoid : setoid (Valuation R) :=
{ r := λ v₁ v₂, ∀ r s, v₁ r ≤ v₁ s ↔ v₂ r ≤ v₂ s,
  iseqv := begin
    split,
    { intros v r s, refl },
    split,
    { intros v₁ v₂ h r s, symmetry, exact h r s },
    { intros v₁ v₂ v₃ h₁ h₂ r s,
      exact iff.trans (h₁ r s) (h₂ r s) }
  end }

definition Spv := quotient (Spv.setoid R)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959871):
@**Mario Carneiro** Yes it is, but the proof is sorried.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 01 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959879):
```quote
is `is_continuous` constant on equivalence classes?
```
yes, although I was waiting for module refactoring to prove it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959891):
Yep, that will need quite some module-juggling.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959900):
And a bit of `tfae`-icing :lol:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 01 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959913):
It is mostly rings but I was using module refactoring as an excuse to put it off

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959944):
what happened to the relations?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959946):
Which relations?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959958):
Aah, lol, they are gone

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959961):
They are in the setoid

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959967):
So there are no longer relations on `R`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959982):
The reason for that definition was because the quotient doesn't work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959989):
So how can you define `lift` and friends using the relations?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134959992):
it's not universe polymorphic enough, and your definition lives in a higher universe

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960044):
That's what the whole thing about generating valuations is for

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960045):
To me `quot` is a bunch of `C++` magic that somehow works. But I don't know how to provide my own `lift` without at some point resorting to `quot.lift`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960048):
You do it the old fashioned way

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960050):
with sets

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960059):
Sorry, I don't follow.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960068):
Given a relation on `R`. How do you get a valuation?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 01 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960073):
```quote
For the perfectoid project we often need to work with subsets of quotient types. A mathematician would write
```lean
def foobar := {x : QuotType | formula x}
```
and afterwards bother with the proof obligation of showing that it is well-defined. Can we mimic this in Lean?
```

```lean
variables (QuotType : Type) (formula : QuotType → Prop)
definition X := {x : QuotType | formula x} 
```

Mimicked. That was what I was trying to say.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960081):
The relation is assumed to be the image of some valuation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960141):
Could you write down the definition of `lift` (with a `sorry`)?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960150):
I couldn't write down anything of which I was even sure that a proof existed.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960158):
Wasn't this already done in an earlier version?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960261):
No, only the claim that it should be done.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960265):
`mk` was done. That's not so hard.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960267):
But `lift` wasn't.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 01 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960269):
`mk` took me forever

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 01 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960279):
Wasn't this the one where I had to invoke the first isomorphism theorem between objects in different universes?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960288):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 01 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960294):
I thought I did most of the hard work for this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 01 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960301):
and that everything else was just noise modulo continuous being constant on equiv classes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960311):
Hmm, sorry. That wasn't nice to say. You indeed need all the minimal_valuation stuff.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960357):
But once that is there `mk` is not very hard.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 01 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960360):
I'm not offended, I am just aware that there are issues here I don't understand so am a bit scared of messing with stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960379):
```lean
definition Spv :=
-- quotient (Spv.setoid R)
{ineq : R → R → Prop // ∃ {Γ : Type u₁} [linear_ordered_comm_group Γ],
  by exactI ∃ (v : valuation R Γ), ∀ r s : R, v r ≤ v s ↔ ineq r s}
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960381):
Voila, the old definition.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960396):
I agree that the universe issue wasn't solved by what I did. (I'm really silly when it comes to universes.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960467):
@**Mario Carneiro** Do you think this would work?
```lean
definition lift {β : Type u₃} (f : Valuation R → β)
(H : ∀ v₁ v₂ : Valuation R, v₁ ≈ v₂ → f v₁ = f v₂) : Spv R → β := sorry
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960497):
can you post enough to make `Spv` compile? Stub out the definition of `valuation` and such

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960670):
mathlib doesn't have `linear_ordered_comm_group`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960675):
```lean
import valuations 
import analysis.topology.topological_space
import data.finsupp
import group_theory.quotient_group

universes u₁ u₂ u₃

namespace valuation

class is_valuation {R : Type u₁} [comm_ring R] {Γ : Type u₂} [linear_ordered_comm_group Γ]
  (v : R → with_zero Γ) : Prop :=
(map_zero : v 0 = 0)
(map_one  : v 1 = 1)
(map_mul  : ∀ x y, v (x * y) = v x * v y)
(map_add  : ∀ x y, v (x + y) ≤ v x ∨ v (x + y) ≤ v y)

end valuation

def valuation (R : Type u₁) [comm_ring R] (Γ : Type u₂) [linear_ordered_comm_group Γ] :=
{ v : R → with_zero Γ // valuation.is_valuation v }
variables (R : Type u₁) [comm_ring R] [decidable_eq R]

open valuation

structure Valuation (R : Type u₁) [comm_ring R] :=
(Γ   : Type u₁)
(grp : linear_ordered_comm_group Γ)
(val : @valuation R _ Γ grp)

namespace Valuation

instance : has_coe_to_fun (Valuation R) :=
{ F := λ v, R → with_zero v.Γ, coe := λ v, v.val.val }

instance linear_ordered_value_group {v : Valuation R} : linear_ordered_comm_group v.Γ := v.grp

end Valuation

instance Spv.setoid : setoid (Valuation R) :=
{ r := λ v₁ v₂, ∀ r s, v₁ r ≤ v₁ s ↔ v₂ r ≤ v₂ s,
  iseqv := begin
    split,
    { intros v r s, refl },
    split,
    { intros v₁ v₂ h r s, symmetry, exact h r s },
    { intros v₁ v₂ v₃ h₁ h₂ r s,
      exact iff.trans (h₁ r s) (h₂ r s) }
  end }

definition Spv :=
{ineq : R → R → Prop // ∃ {Γ : Type u₁} [linear_ordered_comm_group Γ],
  by exactI ∃ (v : valuation R Γ), ∀ r s : R, v r ≤ v s ↔ ineq r s}

namespace Spv

variables {R} {Γ : Type u₂} [linear_ordered_comm_group Γ]

definition mk (v : valuation R Γ) : Spv R :=
⟨λ r s, v r ≤ v s,
  ⟨(minimal_value_group v).Γ,
    ⟨minimal_value_group.linear_ordered_comm_group v,
      ⟨v.minimal_valuation, v.minimal_valuation_equiv⟩⟩⟩⟩

definition lift {β : Type u₃} (f : Valuation R → β) (H : ∀ v₁ v₂ : Valuation R, v₁ ≈ v₂ → f v₁ = f v₂) :
Spv R → β := quotient.lift f H
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960677):
Aah, too bad mathlib doesn't have that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960745):
mathlib has the decidable version

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960750):
(rather core has it)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960763):
is there a reason that doesn't work here?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 01 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960848):
```quote
I agree that the universe issue wasn't solved by what I did. (I'm really silly when it comes to universes.)
```
I don't know if there is a universe issue with your version. I find subtypes easier to use than quotient types but this might just be lack of practice. I am happy if you think a change will make it more readable but I don't want to run into universe issues. My understanding of the universe issues is that I should not let a valuation be an "equivalence class" of `v : R -> with_zero Gamma` where Gamma is allowed to vary over any type in any universe. I instead restricted to Gamma varying over things in the same universe as R and then I had to work to show that if I had a Gamma in another universe it was equivalent to Gamma in R's universe. I think that these issues (which I don't understand fully) are not the same as the one Johan is talking about, which is defining Spv not to be the ordering on R but to be the equiv class of valuations which give the ordering, so my guess is that these changes should be fine *as long as the equiv reln is defined on valuations taking values in things in R's universe*. I am not 100% sure that this is the point but that's my current understanding; I'm currently about to start travelling for 2 hours by the way.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960849):
@**Mario Carneiro** ~~Mathlib~~core has the additive version...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960919):
Unfortunately, you can't even take an equivalence class over all valuations with type in the same universe as R, because this is already too big

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960982):
I have
```lean
hv :
  ∃ {Γ : Type u₁} [_inst_3 : linear_ordered_comm_group Γ] (v_1 : valuation R Γ),
    ∀ (r s : R), ⇑v_1 r ≤ ⇑v_1 s ↔ v r s
```
in my local context. Somehow `cases hv` complains that it can only eliminate into `Prop`. :cry:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960984):
The best you can do is take an equivalence class over all valuations in some "small" collection of representatives

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960986):
Use `classical.cases_on`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134960987):
```quote
Unfortunately, you can't even take an equivalence class over all valuations with type in the same universe as R, because this is already too big
```
Like I just experienced (-;

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134961003):
I'm still struggling to get your file to compile, but that's what I was going to do

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134961011):
just use `classical.cases_on` three times and apply the function

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134961053):
You won't even need the well definedness assumption, it's just for show

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134961068):
Let me try

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134961089):
How do I "use" `classical.cases_on` with `hv`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134961133):
`refine classical.cases_on hv (\lam Gamma h', _)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134961136):
I see

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134961138):
Good old refine

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134961139):
You might be able to use a custom recursor with `induction` but I find `refine` the most straightforward

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134961152):
```
type mismatch at application
  classical.cases_on hv
term
  hv
has type
  ∃ {Γ : Type u₁} [_inst_3 : linear_ordered_comm_group Γ] (v_1 : valuation R Γ),
    ∀ (r s : R), ⇑v_1 r ≤ ⇑v_1 s ↔ v r s : Prop
but is expected to have type
  Prop : Type
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134961156):
Also... lunch time

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134961157):
See you later

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134961159):
lol

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134961210):
sorry, I think it's called `classical.rec_on`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134961215):
it's a bad name

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 01 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134961221):
it should be more like `exists.rec_on_classical`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134963338):
```lean
noncomputable definition lift {β : Type u₃} (f : Valuation R → β) (H : ∀ v₁ v₂ : Valuation R, v₁ ≈ v₂ → f v₁ = f v₂) :
Spv R → β :=
begin
intro v,
cases v with v hv,
refine classical.rec_on hv (λ Γ hv', _),
refine classical.rec_on hv' (λ inst hv'', _),
refine classical.rec_on hv'' (λ v h, _),
exact f {Γ := Γ, grp := inst, val := v}
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134963350):
That kind of worked. But I didn't use `H`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 01 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134964015):
Mario announced that you wouldn't need H

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134964138):
So, is this some sort of "cheating" definition?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134964152):
I guess we should leave `H` in place, because otherwise `lift` can be abused.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 01 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134964277):
You will need `H` to prove that `lift f H (mk v) = f v`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134964394):
Good point. Let me prove such things now.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 01 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134964400):
It seems this is a very convenient way to setup things: define stuff without precondition, and prove they have the expected properties under the appropriate conditions. An extreme example is https://github.com/leanprover-community/mathlib/blob/b3b50ce67c8b73442372c5141e8836c64ea13826/analysis/topology/completion.lean#L442-L446

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134965116):
Now I'm stuck on the following goal:
```lean
⊢ classical.rec_on _
      (λ (Γ : Type u₁)
       (hv' :
         ∃ [_inst_3 : linear_ordered_comm_group Γ] (v_1 : valuation R Γ),
           ∀ (r s : R), ⇑v_1 r ≤ ⇑v_1 s ↔ ⇑(v.val) r ≤ ⇑(v.val) s),
         classical.rec_on hv'
           (λ (inst : linear_ordered_comm_group Γ)
            (hv'' : ∃ (v_1 : valuation R Γ), ∀ (r s : R), ⇑v_1 r ≤ ⇑v_1 s ↔ ⇑(v.val) r ≤ ⇑(v.val) s),
              classical.rec_on hv''
                (λ (v_1 : valuation R Γ) (h : ∀ (r s : R), ⇑v_1 r ≤ ⇑v_1 s ↔ ⇑(v.val) r ≤ ⇑(v.val) s),
                   f {Γ := Γ, grp := inst, val := v_1}))) =
    f v
```
The maths is clear, but I have no idea how to work with this `classical.rec_on`. How do I fight those?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134965842):
Ok, so I can turn it into the rather unhelpful:
```lean
lemma lift_mk {β : Type u₃} {f : Valuation R → β} {H : ∀ v₁ v₂ : Valuation R, v₁ ≈ v₂ → f v₁ = f v₂} (v : Valuation R) :
lift f H (mk v) = f v :=
begin
  refine H _ _ _,
  -- ⊢ {Γ := classical.some _, grp := classical.some _, val := classical.some _} ≈ v
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134965907):
As you can see in the code, there is this bit saying `(hv'' : ∃ (v_1 : valuation R Γ), ∀ (r s : R), ⇑v_1 r ≤ ⇑v_1 s ↔ ⇑(v.val) r ≤ ⇑(v.val) s),`. I need to extract that, and use it to close my goal.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134966633):
Ok, from browsing code I think that I should use `some_spec` or `some_spec2`. Can anyone confirm that this is reasonable? (I have yet to figure out how I should use them...)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134967775):
This is what I have now:
```lean
lemma lift_mk {β : Type u₃} {f : Valuation R → β} {H : ∀ v₁ v₂ : Valuation R, v₁ ≈ v₂ → f v₁ = f v₂} (v : Valuation R) :
lift f H (mk v) = f v :=
begin
  let ineq := mk v,
  have foo := classical.some_spec (ineq.2),
  refine H _ _ _,
  intros r s,
end
-- R : Type u₁,
-- _inst_1 : comm_ring R,
-- _inst_2 : decidable_eq R,
-- β : Type u₃,
-- f : Valuation R → β,
-- H : ∀ (v₁ v₂ : Valuation R), v₁ ≈ v₂ → f v₁ = f v₂,
-- v : Valuation R,
-- ineq : Spv R := mk v,
-- foo : ∀ (r s : R), ⇑(classical.some _) r ≤ ⇑(classical.some _) s ↔ ineq.val r s,
-- r s : R
-- ⊢ ⇑(classical.some _) r ≤ ⇑(classical.some _) s ↔ ⇑v r ≤ ⇑v s
```
Looks deceptively close, but I can't finish it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Oct 01 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134967787):
Yes, if you want to proof something about `classical.some`. What you usually do is to define a the constant using `classical.some` and then proof when a corresponding value exists, then the constant has the properties.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Oct 01 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134967800):
what is the type of `_` in `classical.some _`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134967891):
Hooray!
```lean
lemma lift_mk {β : Type u₃} {f : Valuation R → β} {H : ∀ v₁ v₂ : Valuation R, v₁ ≈ v₂ → f v₁ = f v₂} (v : Valuation R) :
lift f H (mk v) = f v :=
begin
  let ineq := mk v,
  have spec := classical.some_spec (mk v).property,
  refine H _ _ _,
  intros r s,
  dsimp [mk] at spec,
  exact spec r s
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 01 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134967896):
Somehow I managed to convince Lean!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Oct 01 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134967899):
I agree `some_spec` is awkward, but for what it's worth, it is mentioned in TPIL. When I first saw the example provided in 11.6 I didn't have any idea how it worked.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Oct 01 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subset%20of%20quotient/near/134967939):
```lean
open classical function
local attribute [instance] prop_decidable

noncomputable definition linv {α β : Type} [h : inhabited α]
  (f : α → β) : β → α :=
λ b : β, if ex : (∃ a : α, f a = b) then some ex else arbitrary α

theorem linv_comp_self {α β : Type} {f : α → β}
    [inhabited α] (inj : injective f) :
  linv f ∘ f = id :=
funext (assume a,
  have ex  : ∃ a₁ : α, f a₁ = f a, from exists.intro a rfl,
  have   feq : f (some ex) = f a, from some_spec ex,
  calc linv f (f a) = some ex :  dif_pos ex
             ...    = a       :  inj feq)
```


{% endraw %}
