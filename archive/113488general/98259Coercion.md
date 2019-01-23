---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/98259Coercion.html
---

## Stream: [general](index.html)
### Topic: [Coercion](98259Coercion.html)

---


{% raw %}
#### [ Ned Summers (Jul 23 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coercion/near/130142384):
For context, in Scott Morrison's category theory code he introduces isomorphism as the structure:
```
structure Isomorphism {C : Type u} [category.{u v} C] (X Y : C) :=
  (morphism : X ⟶ Y)
  (inverse : Y ⟶ X)
  (witness_1 : morphism ≫ inverse = 𝟙 X . obviously)
  (witness_2 : inverse ≫ morphism = 𝟙 Y . obviously)
```
This seems like a perfectly fine way of doing this. Later in the document he uses

```
instance Isomorphism_coercion_to_morphism : has_coe (Isomorphism.{u v} X Y) (X ⟶ Y) :=
{ coe := Isomorphism.morphism }
```

I can't seem to figure out what a coercion actually is, or what it's use is. It seems like it might be useful. I'm currently trying to state and prove a theorem where a morphism is shown to be an isomorphism and this looks like a promising way of moving from isomorphic objects to isomorphisms. Help much appreciated.

#### [ Patrick Massot (Jul 23 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coercion/near/130143610):
https://leanprover.github.io/theorem_proving_in_lean/type_classes.html#coercions-using-type-classes

#### [ Ned Summers (Jul 23 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coercion/near/130144000):
Thanks

#### [ Kevin Buzzard (Jul 23 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coercion/near/130170341):
A coercion is just a way of moving from one type to another by applying a function which you don't want to continually mention, you just want Lean to do it automatically. See that the coercion is defined using `instance` not `definition`? That means "define it, and let the type class inference system use it". The type class inference system will then apply it whenever necessary.

#### [ Chris Hughes (Jul 23 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coercion/near/130170444):
Shouldn't that be a `has_coe_to_fun` not a `has_coe`?

#### [ Mario Carneiro (Jul 24 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coercion/near/130180701):
No, because the target isn't a function type (that arrow is not a regular arrow)

#### [ Anthony Bordg (Oct 05 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coercion/near/135248099):
Hi,
in the current library is there already a coercion to see a field as a comm_semiring ? 
One can combine `field.to_comm_ring ` with `comm_ring.to_comm_semiring`, but maybe there is a more direct way.
Thanks

#### [ Johan Commelin (Oct 05 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coercion/near/135248182):
The typeclass system should do that for you. Usually you don't need to touch it.

#### [ Johan Commelin (Oct 05 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coercion/near/135248235):
If you really need it:
```lean
instance {K : Type*} [field K] : comm_semiring K := by apply_instance
```

#### [ Johan Commelin (Oct 05 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coercion/near/135248242):
You can usually also insert the `by apply_instance` into your proofs if you need it.

#### [ Anthony Bordg (Oct 05 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coercion/near/135248929):
```quote
The typeclass system should do that for you. Usually you don't need to touch it.
```
The typeclass system doesn't help here, but the code you gave me with "instance" works fine.
Thank you @**Johan Commelin**

#### [ Kevin Buzzard (Oct 05 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coercion/near/135259239):
This instance code is exactly using the type class inference system to construct the term which you asked for. But usually the type class inference system can be trusted to handle this question completely, and users don't have to construct this term at all. Why did you want this coercion?

#### [ Anthony Bordg (Oct 05 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coercion/near/135265433):
```quote
This instance code is exactly using the type class inference system to construct the term which you asked for. But usually the type class inference system can be trusted to handle this question completely, and users don't have to construct this term at all. Why did you want this coercion?
```
@**Kevin Buzzard**  I want to use `polynomial.eval` with a field (the default argument is a commutative semiring).

#### [ Johan Commelin (Oct 05 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coercion/near/135265444):
That should work out of the box

#### [ Kevin Buzzard (Oct 05 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coercion/near/135265490):
Are these typeclasses not just all resolved using type class inference?

#### [ Kevin Buzzard (Oct 05 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coercion/near/135265684):
```lean
import data.polynomial
definition KX (K : Type) [field K] := polynomial K
```
It just works when you do it this way @**Anthony Bordg**

#### [ Kevin Buzzard (Oct 05 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coercion/near/135265787):
```lean
import data.polynomial

definition KX (K : Type) [field K] := polynomial K

open polynomial

variables {K : Type} [field K] [decidable_eq K]

lemma eval_works (k : K) : eval k X = k := by simp
```


{% endraw %}
