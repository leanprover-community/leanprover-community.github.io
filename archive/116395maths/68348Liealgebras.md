---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/68348Liealgebras.html
---

## Stream: [maths](index.html)
### Topic: [Lie algebras](68348Liealgebras.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 13 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/127997275):
I am completely stuck on the sorried definition. Is this just to ambitious at the moment?
```lean
import algebra.module

class has_bracket (α : Type*) := (bracket : α → α → α)

local notation `[` a `,` b `]` := has_bracket.bracket a b

class lie_algebra (R : out_param $ Type*) (𝔤 : Type*) [out_param $ comm_ring R]
extends module R 𝔤, has_bracket 𝔤 :=
(left_linear  := ∀ y : 𝔤, is_linear_map (λ x : 𝔤, [x,y]))
(right_linear := ∀ x : 𝔤, is_linear_map (λ y : 𝔤, [x,y]))
(alternating  := ∀ x : 𝔤, [x,x] = 0)
(Jacobi_identity := ∀ x y z : 𝔤, [x,[y,z]] + [z,[x,y]] + [y,[z,x]] = 0)
(anti_comm    := ∀ x y : 𝔤, [x,y] = -([y,x]))

variables {R : Type*} [ri : comm_ring R]
variables {𝔤 : Type*} [la : lie_algebra R 𝔤]
include ri la

section from_ring

variables {S : Type*} [ring S]
variables {f : R → S}  [is_ring_hom f]

instance commutator_bracket : has_bracket S := ⟨λ x y, x*y - y*x⟩

definition ring.to_lie_algebra : lie_algebra R S := sorry
-- { sorry,
--   ..ring.to_module }

end from_ring
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 13 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/127997433):
```lean
definition ring.to_lie_algebra : lie_algebra R S := 
begin
constructor, -- fails
end 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 13 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/127997434):
I am a bit surprised about this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 13 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/127997547):
`{}` is more instructive

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 13 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/127997549):
It says it can't prove `module R S`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 13 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/127997556):
which is fair enough because you never mentioned `f`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 13 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/127997636):
and `ring.to_module` is only the statement that `R` is an `R`-module

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 13 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/127997692):
Right. Thanks a lot!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 13 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/127997693):
I think when I was in your position a few months ago, wrestling with the type class inference system (but in a much less complex situation) Sebastian just pointed out that I could over-ride everything.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 13 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/127997709):
so I would just go and make my own explicit instances of everything

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 13 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/127997714):
and this got me a bit further

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 13 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/127997734):
I guess `constructor` doesn't work because it didn't even get round to thinking about how to construct the extra fields, it just gets hung up with the fact that it can't even make the extension

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 13 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/127997822):
Ok, so I've got a proof of `module R S`. How do I feed it to the system?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 13 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/127997830):
Because `@lie_algebra` is not interested in such a proof...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 13 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/127997887):
Is the `extends module R _` giving me trouble? Does that `extends` imply that it wants do deduce the module structure by type class inference?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 13 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/127997963):
I used to ask this sort of question all the time. If you search for type class woes you'll find my thread where I asked about 10 questions of this nature.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 13 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/127998035):
Unfortunately I can't keep all the answers in my head and I still have not found the time to go through that thread and write down all the tips in a proper doc

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 13 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/127998455):
@**Kevin Buzzard** Misa stupid! In the definition of the class I shouldn't use `:=` but `:` for the axioms... it should be
```lean
class lie_algebra (R : out_param $ Type*) (𝔤 : Type*) [out_param $ comm_ring R]
extends module R 𝔤, has_bracket 𝔤 :=
(left_linear  : ∀ y : 𝔤, is_linear_map (λ x : 𝔤, [x,y]))
(right_linear : ∀ x : 𝔤, is_linear_map (λ y : 𝔤, [x,y]))
(alternating  : ∀ x : 𝔤, [x,x] = 0)
(Jacobi_identity : ∀ x y z : 𝔤, [x,[y,z]] + [z,[x,y]] + [y,[z,x]] = 0)
(anti_comm    : ∀ x y : 𝔤, [x,y] = -([y,x]))
```
That messed up everything. Now that I've fixed it, all of a sudden problems vanish!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 13 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/127999527):
Oh yeah. Sorry, I should have caught that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 13 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/128000028):
Yoohoo!
```lean
section from_ring

variables {S : Type*} [ring S]
variables {f : R → S}  [is_ring_hom f]
variable  {central : ∀ (r : R) (s : S), f(r) * s = s * f(r)}

instance commutator_bracket : has_bracket S := ⟨λ x y, x*y - y*x⟩

include central
definition ring.to_lie_algebra : lie_algebra R S :=
{ left_linear  := begin
    intro y,
    dsimp [commutator_bracket],
    constructor,
    { intros x₁ x₂,
      simp [left_distrib,right_distrib,mul_assoc] },
    { intros r x,
      show f r * x * y + -(y * (f r * x)) = f r * (x * y + -(y * x)),
      simp [left_distrib,right_distrib,mul_assoc,central] }
  end,
  right_linear := begin
    intro x,
    dsimp [commutator_bracket],
    constructor,
    { intros x₁ x₂,
      simp [left_distrib,right_distrib,mul_assoc] },
    { intros r y,
      show x * (f r * y) + -(f r * y * x) = f r * (x * y + -(y * x)),
      simp [left_distrib,right_distrib,mul_assoc,central] }
  end,
  alternating  := begin
    intro x,
    dsimp [commutator_bracket],
    simp
  end,
  Jacobi_identity := begin
    intros x y z,
    dsimp [commutator_bracket],
    simp [left_distrib,right_distrib,mul_assoc],
  end,
  anti_comm := begin
    intros x y,
    dsimp [commutator_bracket],
    simp
  end,
  ..restriction_of_scalars.restriction_of_scalars f S
}

end from_ring
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 13 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/128000036):
I like `simp`!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 13 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/128000082):
It's a pity I can't use `ring` because I'm not in a commutative setting...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 13 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/128000416):
```quote
It's a pity I can't use `ring` because I'm not in a commutative setting...
```
I can tell you how to write the non-commutative version :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 13 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/128000429):
Lol

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 13 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/128000435):
actually there would be an issue

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 13 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/128000446):
Yes, I wouldn't be surprised if commutativity is essential [also: lunch]

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 13 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/128000491):
There's even an issue with my baby ring tactic -- one needs to be able to put every polynomial into a "canonical form", so that two polynomials (e.g. x^2+1 and 0*x^3+x^2+1) are equal if and only if their canonical forms are equal.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 13 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/128000502):
Make your polynomials a subtype, with a proof that the leading coeff is not zero

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 13 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/128000509):
Like finsets.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 13 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/128000510):
In my baby ring tactic this isn't even present (yet). In the grown-up ring tactic Mario uses Gregoire-Mahboubi's strategy of writing everything in "horner form" because this is much more efficient for sparse polys

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 13 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/128000519):
but in the non-comm case you would have to figure out a canonical form I guess, at least if you wanted to maximise the chance that the tactic worked.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 13 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/128000560):
Chris -- this doesn't work for zero

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 13 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/128000566):
I was going to go for the following:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 13 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/128000571):
either an empty list, or a non-empty list with last element non-zero

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 13 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/128000588):
One would have to check non-zero-ness in the ground ring (which might be Z/2Z)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 13 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/128000589):
What's the last element function?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 13 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/128000593):
I've seen one before

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 13 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/128000595):
I've seen an n'th element function somewhere in list.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 13 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/128000596):
How does it habdle the empty list? If it's option you're okay.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 13 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/128000599):
unsurprisingly, there are all sorts of variants

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 13 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/128000646):
e.g. one which asks for a proof that n < length before giving you a non-option n'th element

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 13 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Lie%20algebras/near/128000696):
`list.head'` looks like the best one, depending on the order of your lists.

