---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/63156DependentlyTypedFoldsforNestedDataTypes.html
---

## Stream: [general](index.html)
### Topic: [Dependently Typed Folds for Nested Data Types](63156DependentlyTypedFoldsforNestedDataTypes.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jul 05 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20Typed%20Folds%20for%20Nested%20Data%20Types/near/129137513):
@**Sebastian Ullrich** [wrote](https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/cases/near/126323093):

```quote
With nested and mutual inductives moving into the kernel, there shouldn't be any need for an abstraction layer. Well, it's still not clear how nested inductives would be represented.
```

Would this paper help?

[Dependently Typed Folds for Nested Data Types](https://arxiv.org/abs/1806.05230):

```quote
We present an approach to develop folds for nested data types using dependent types. We call such folds dependently typed folds, they have the following properties. (1) Dependently typed folds are defined by well-founded recursion and they can be defined in a total dependently typed language. (2) Dependently typed folds do not depend on maps, map functions and many terminating functions can be defined using dependently typed folds. (3) The induction principles for nested data types follow from the definitions of dependently typed folds and the programs defined by dependently typed folds can be formally verified. (4) Dependently typed folds exist for any nested data types and they can be specialized to the traditional higher-order folds. Using various of examples, we show how to program and reason about dependently typed folds. We also show how to obtain dependently typed folds in general and how to specialize them to the corresponding higher-order folds.
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jul 05 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20Typed%20Folds%20for%20Nested%20Data%20Types/near/129145511):
@**Sean Leather** This seems to be about a different kind of nested types. Note that `Bush` cannot even be defined in Lean 3 because of universe constraints.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jul 05 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20Typed%20Folds%20for%20Nested%20Data%20Types/near/129145627):
What are the nested inductives that you're referring to?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jul 05 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20Typed%20Folds%20for%20Nested%20Data%20Types/near/129145672):
And conversely, the type `Term` from the first case study is just a regular inductive type according to Lean. I didn't compare the induction principles, though.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jul 05 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20Typed%20Folds%20for%20Nested%20Data%20Types/near/129145876):
@**Sean Leather**  Any inductive type that is passed to another inductive type in its own definition, as in https://github.com/leanprover/lean/wiki/Inductive-datatypes#encoding-datatypes-that-contain-recursive-occurrences-nested-in-existing-datatypes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jul 05 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20Typed%20Folds%20for%20Nested%20Data%20Types/near/129146139):
Ok, right. That's the "simple" version of nested data types.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 03:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20Typed%20Folds%20for%20Nested%20Data%20Types/near/129175542):
> Note that Bush cannot even be defined in Lean 3 because of universe constraints.

Actually this is an instance of non-uniform parameters, which I have figured out how to simulate in lean without any kernel extensions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jul 06 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20Typed%20Folds%20for%20Nested%20Data%20Types/near/129183673):
```quote
Actually this is an instance of non-uniform parameters, which I have figured out how to simulate in lean without any kernel extensions
```

@**Mario Carneiro** Please do share. Can you define a `Bush` type from constants?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20Typed%20Folds%20for%20Nested%20Data%20Types/near/129183675):
what do you mean from constants?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jul 06 2018 at 07:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20Typed%20Folds%20for%20Nested%20Data%20Types/near/129183799):
I mean the sort of constants generated by the equation compiler.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jul 06 2018 at 07:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20Typed%20Folds%20for%20Nested%20Data%20Types/near/129183844):
Err, maybe I'm using the wrong terminology. What do you call the process of taking an `inductive` to its constants?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 08:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20Typed%20Folds%20for%20Nested%20Data%20Types/near/129184389):
the constructors?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 08:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20Typed%20Folds%20for%20Nested%20Data%20Types/near/129184456):
To be precise, I can define a type `Bush` together with constructors of the stated types, the natural recursion principle, and a computation rule (as a provable equality, not definitional) while circumventing any universe inconsistencies

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jul 06 2018 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20Typed%20Folds%20for%20Nested%20Data%20Types/near/129184572):
```quote
To be precise, I can define a type `Bush` together with constructors of the stated types, the natural recursion principle, and a computation rule (as a provable equality, not definitional) while circumventing any universe inconsistencies
```
Yes, that's what I'd like to see.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20Typed%20Folds%20for%20Nested%20Data%20Types/near/129189453):
I think I will just give a rough sketch:
```lean
inductive {u} bushn (α : Type u) : nat → Type u
| zero : α → bushn 0
| nil {n} : bushn (n+1)
| cons {n} : bushn n → bushn (n+2) → bushn (n+1)

def bush (α : Type*) := bushn α 1

def bushn.equiv (α : Type*) : ∀ n : ℕ, bushn α n ≃ (bush^[n] α) := sorry

def bush.nil (α : Type*) : bush α := bushn.nil α
def bush.cons {α : Type*} (a : α) (b : bush (bush α)) : bush α :=
bushn.cons (bushn.zero a) ((bushn.equiv α 2).symm b)

def {u l} bush.rec {C : ∀ {α : Type u}, bush α → Sort l}
  (C0 : ∀ α, C (bush.nil α))
  (C1 : ∀ α a b, C b → C (@bush.cons α a b))
  (α b) : @C α b := sorry

def bush.rec_nil {C} (C0 C1 α) :
  @bush.rec @C C0 C1 α (bush.nil α) = C0 α := sorry

def bush.rec_cons {C} (C0 C1 α a b) :
  @bush.rec @C C0 C1 α (bush.cons a b) =
  C1 α a b (@bush.rec @C C0 C1 (bush α) b) := sorry
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jul 06 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20Typed%20Folds%20for%20Nested%20Data%20Types/near/129190374):
At a glance, that looks similar to what's in the article I linked.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20Typed%20Folds%20for%20Nested%20Data%20Types/near/129190460):
Is it? I thought they assume that `bush` makes sense as an inductive without further justification, since Agda accepts it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jul 06 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20Typed%20Folds%20for%20Nested%20Data%20Types/near/129190525):
Copy-paste:
```agda
data BushN : Nat -> Set -> Set where
  Base : {a : Set} -> a -> BushN Z a
  NilBN : {a : Set} -> {n : Nat} -> BushN (S n) a
  ConsBN : {a : Set} -> {n : Nat} -> BushN n a -> BushN (S (S n)) a -> BushN (S n) a
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 06 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently%20Typed%20Folds%20for%20Nested%20Data%20Types/near/129190559):
Oh, I missed that

