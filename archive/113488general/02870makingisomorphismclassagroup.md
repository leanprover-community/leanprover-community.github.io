---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/02870makingisomorphismclassagroup.html
---

## Stream: [general](index.html)
### Topic: [making isomorphism class a group](02870makingisomorphismclassagroup.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124464358):
Let's say I have a bunch of groups, and I use `quotient` to make isomorphism classes. Is there a constructive way to make the isomorphism classes inherit the structure of a group?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124464513):
I don't know but I'd like to find out. Let's say our groups are specified as:

```
variables {I : Type} (G : I -> Type) [Π i, group (G i)]
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124464561):
Are we also given the isomorphisms between those groups or to you want to construct them somehow?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124464564):
I have already constructed the quotient

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124464567):
Can you show it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124464607):
```
import data.set.basic group_theory.subgroup

universe u

namespace group

variables {α : Type u} [group α] (S : set α)

inductive generate : set α
| basic : ∀ x ∈ S, generate x
| one : generate 1
| mul_inv : ∀ x y, generate x → generate y → generate (x * y⁻¹)

namespace generate

def is_subgroup : is_subgroup (generate S) :=
{ one_mem := generate.one S,
  mul_inv_mem := λ x y hx hy, generate.mul_inv x hx y hy }

end generate

variables {β : Type u} [group β]
variables α β

class isomorphism extends α ≃ β :=
( is_group_hom : is_group_hom to_fun )

namespace isomorphism

variables {γ : Type u} [group γ]
variables {β γ}

@[refl] protected def refl : isomorphism α α :=
{ is_group_hom := λ x y, rfl
  .. equiv.refl α }

variables {α β γ}

@[symm] protected def symm (e : isomorphism α β) : isomorphism β α :=
{ is_group_hom := λ x y, calc
          e.inv_fun (x * y)
        = e.inv_fun (e.to_fun (e.inv_fun x) * e.to_fun (e.inv_fun y)) : by rw [e.right_inv, e.right_inv]
    ... = e.inv_fun (e.to_fun (e.inv_fun x * e.inv_fun y)) : by rw e.is_group_hom
    ... = e.inv_fun x * e.inv_fun y : by rw e.left_inv,
  .. equiv.symm e.to_equiv }

@[trans] protected def trans (e₁ : isomorphism α β) (e₂ : isomorphism β γ) : isomorphism α γ :=
{ is_group_hom := λ x y, by unfold equiv.trans; dsimp; rw [e₁.is_group_hom, e₂.is_group_hom],
  .. equiv.trans e₁.to_equiv e₂.to_equiv }

end isomorphism

end group

variable (S : Type u)

namespace free_group

structure to_be_named (G : Type u) [group G] :=
( gen : set G )
( gen_gen : group.generate gen = set.univ )
( func : gen → S )
( inj : function.injective func )

def to_be_named.quotient_rel : setoid Σ G [H : group G], @to_be_named S G H :=
⟨λ G H, nonempty $ @group.isomorphism G.1 G.2.1 H.1 H.2.1,
 λ G, ⟨@group.isomorphism.refl G.1 G.2.1⟩,
 λ G H ⟨e⟩, ⟨@group.isomorphism.symm G.1 G.2.1 H.1 H.2.1 e⟩,
 λ G H K ⟨e₁⟩ ⟨e₂⟩, ⟨@group.isomorphism.trans G.1 G.2.1 H.1 H.2.1 K.1 K.2.1 e₁ e₂⟩⟩

def something : Type (u+1) :=
quotient (to_be_named.quotient_rel S)

noncomputable def rep : something S → Σ G [H : group G], @to_be_named S G H :=
λ G, classical.some (@quotient.exists_rep _ (to_be_named.quotient_rel S) G)

#check λ G, classical.some (@quotient.exists_rep _ (to_be_named.quotient_rel S) G)

structure funny_structure : Type (u+1) :=
( G : something S )
( func : S → (rep S G).1 )
( im_gen : @group.generate _ (rep S G).2.1 (func '' set.univ) = set.univ )

def some_product : Type (u+1) :=
Π A : funny_structure S, (rep S A.G).1

noncomputable instance some_product.group : group (some_product S) :=
{ mul := λ f g x, @has_mul.mul _ (@semigroup.to_has_mul _ (@monoid.to_semigroup _ (@group.to_monoid _ (rep S (x.G)).2.1))) (f x) (g x),
  mul_assoc := λ f g h, funext $ λ x, by apply mul_assoc,
  one := λ x, @has_one.one _ (@monoid.to_has_one _ (@group.to_monoid _ (rep S (x.G)).2.1)),
  one_mul := λ f, funext $ λ x, by apply one_mul,
  mul_one := λ f, funext $ λ x, by apply mul_one,
  inv := λ f x, @has_inv.inv _ (@group.to_has_inv _ (rep S (x.G)).2.1) (f x),
  mul_left_inv := λ f, funext $ λ x, by apply mul_left_inv }

def aux_func : S → some_product S :=
λ x A, A.func x

end free_group

def free_group : Type (u+1) :=
group.generate (free_group.aux_func S '' set.univ)

instance free_group.group : group (free_group S) :=
is_subgroup.group group.generate.is_subgroup

def free_group.from_S : S → free_group S :=
λ x, ⟨free_group.aux_func S x, group.generate.basic _ ⟨x, trivial, rfl⟩⟩

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124464610):
this is WIP so there are errors on the bottom, ignore those

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124464612):
the quotient is appropriately named `something`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124464943):
So you'd like to remove `noncomputable` from your `group` instance?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124465033):
right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 31 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124465035):
You had to prove that the composite of group homs is a group hom?? That's not there already?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124465038):
you'll be surprised

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124465249):
Instead of `classical.some` and `quotient.exists_rep` in `rep`, can you try and use `quotient.lift`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124465250):
to where?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124465316):
Not sure yet

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124465376):
You're basically taking the value of a quotient type and sticking it in a sigma type. Because the sigma type is in `Type u` depending on which representative you extract, you will be able to tell members of the quotient sets apart.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124465422):
There are two possibilities I can see to stay constructive: instead of using a sigma type, use an existential quantification (not sure if that's workable with the group) or extract something other than the element of one of the group. A representative value that will be the same for every element of a given equivalence class

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124465475):
Or maybe Mario's `trunc` contraption can make the sigma type into something that isn't data

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124467440):
@**Simon Hudon** do we even need the quotient?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124467543):
I think you're right, you don't need it, at least not there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124467547):
I think the reason the author introduced it is because of some foundational issues with ZFC

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124467552):
the paper is here for reference https://www3.nd.edu/~andyp/notes/CategoricalFree.pdf

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469143):
@**Kevin Buzzard** this can be viewed in two ways

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469144):
you will view it as "another reason why ZFC is stupid"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469192):
I will view it as "another reason why Lean is stupid"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 01 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469193):
I'm wondering if you even need the sigma type

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469228):
I did it without any quotient

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469233):
and without injectivity

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469234):
the only reason why the paper introduced those is to justify it in ZFC

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 01 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469235):
And sigma type?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469236):
well the sigma type has UMP as pi type right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469237):
that means, (Sigma x1 x2) -> x3 is the same as x1 -> x2 -> x3

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469240):
since they're there, the sigma doesn't need to be there anymore

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469243):
am I speaking English

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469244):
that thing there with that sigma is no longer used

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469245):
I can't English

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 01 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469246):
What's UMP?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469247):
universal mapping property

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469273):
or in CS language, "destructor" / "eliminator"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 01 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469290):
Ah I see

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 01 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469291):
So why is it that not needing a quotient type makes Lean stupid?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469296):
well if I need to explain I would have to bring another concept from math philosophy into here :P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469297):
called predicativity

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 01 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469336):
Cool, I'm all ears

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469337):
inductive types are predicative

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469338):
they're philosophically well-founded

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469339):
bigger things are built on top of smaller things

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469348):
like "canonical", this word can't be properly defined, but a common criterion is whether the quantifiers quantify over the object to be constructed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469349):
e.g. in ZFC, omega is constructed to be the intersection of every inductive set

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469388):
instead of building it from below, omega is constructed from above, which makes it philosophically not well-founded, and we call that impredicative

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469389):
in ZFC, omega := {x | x in A for every inductive A}

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469390):
but the "for every" quantifier there, quantifiers over omega itself

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469399):
now, the free group construction in the paper is equally impredicative

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469400):
in the sense that it takes the product of every possible group and then find the subgroup generated by the image of S

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469440):
but that product would have to already include that group to be constructed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469442):
ZFC is an impredicative theory

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469443):
but that's unavoidable, because we want a strong foundation theory to do maths

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469449):
the common construction of free group is predicative

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469450):
because it builds on smaller things, i.e. individual words

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469494):
in ZFC, i.e. in the paper, the author constructed the free product by considering every group generated by a set that injects into S

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469495):
there's still a limitation on the size

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469497):
in Lean, i.e. in my file, I don't even need to care about the size, since Lean allows it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469498):
https://github.com/kckennylau/Lean/blob/master/free_group.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 01 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469550):
Why is that a problem?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469551):
it's not very well-founded is it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 01 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469644):
Isn't the "big things built from smaller things" idea supported by the hierarchy of universes?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469683):
well but one universe is already big enough

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469696):
philosophy aside, this construction is quite funny

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469737):
what do you think of my file? is it mathematically correct? should I PR it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469743):
I wonder why this construction isn't more well-known

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 01 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469796):
I don't think I can make a judgement about your construction. Mario and Kevin probably should be the ones to comment

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469797):
ok

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 01 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469798):
Or Johannes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 01 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124469800):
It looks like a cool construction :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470041):
@**Simon Hudon** https://github.com/kckennylau/Lean/commit/c6eac863b23d58d40deaab62489f6069f860407e#diff-fdee7d198ee1f7316cba5649313e084a

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470042):
rip universe limitation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470043):
now it can be in any universe

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 01 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470084):
Yeah, that's universe polymorphism for you ;-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470096):
I wonder if `free_group.{u v} S` and `free_group.{u w} S` are different

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470183):
@**Simon Hudon** this is such a convenient construction

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470185):
basically constructing an object from its UMP

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470187):
I can probably construct the abelianization this way also

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 01 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470229):
That looks like the free objects I've worked with before. I remember being blown away by how cool they are :D

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470232):
you've seen this construction before?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 01 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470238):
I've seen it in free monads mostly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470283):
do you have any idea how I can fix the file to remove the need for manual typeclassing?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470285):
group to monoid, monoid to semigroup, semigroup to has_mul...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 01 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470335):
What happens when you replace it with an underscore?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470337):
can't synthesize that thing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 01 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470383):
Right but what instances are in your context?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470384):
the thing is that the instances aren't declared to the left of the colon

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470385):
rather, they're introduced as variables

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470392):
because of how I defined ambient

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 01 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470433):
Right, so you can write:

```lean
λ x y G HG f, by resetI ; exact @has_mul.mul _ _ ... 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470434):
I thought definitions shouldn't have any tactics

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470435):
because they're difficult to destruct

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 01 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470476):
This tactic won't create a complicated term. But it's also useful to just try it and see if it works. Otherwise, you can also use a separate `def`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470479):
hmm...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470578):
free functors on steroids

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 02:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470859):
https://github.com/kckennylau/Lean/blob/master/abelianization.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 02:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124470860):
comes with commutators for free!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 01 2018 at 03:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124472206):
I'm familiar with this construction, which is sometimes used as an application of category theory: use the adjoint functor theorem to construct free groups. When you unwind the category theory it's exactly this construction: taking a suitable quotient over all groups

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 01 2018 at 03:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124472250):
The universe issues that arise in ZFC also arise in lean, because they are valid concerns and can cause inconsistency if they are not attended to. In lean this expresses as a bumping up of the universe level of the constructed free group

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 01 2018 at 03:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124472296):
To prove that the universe doesn't need to increase, you need a size limitation which amounts to doing the standard (internal) free group construction anyway. This is why I'm not a big fan of this approach - it's just shuffling proof obligations around

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 01 2018 at 03:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124472356):
When you write the UMP predicatively, it ends up weaker than people want (and use), because the free group you've constructed lives in `max u (v+1)` but is only universal wrt groups in `Type v`, which is strictly lower. In particular, the free group UMP doesn't apply to itself, which we want to be true for it to really be a free group. Otherwise it's only an approximation - if you try proving equivalence to the standard internal definition you will get stuck

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 01 2018 at 03:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124473230):
Re: making the isomorphism class a group, it is impossible to do this computably for some reasonable definitions of the problem. Suppose we want to take a quotient of all groups (in some universe) with respect to isomorphism. First of all, note that a quotient is with respect to a relation, meaning a Prop, meaning data about the isomorphism itself will be lost. We can define such a quotient, let's call it `Q`. Now each element `q : Q` somehow "represents" a group unique up to isomorphism, but I claim that there is no computable function `rep : Q -> Group` such that `G ~= rep (mk G)` for all groups `G`.

Now one way to define such a function is by applying choice as you've done to just pick one of the groups in the class, but maybe you thought there might be a way of using all the groups at once to form a new group which is isomorphic to each of the groups in the equivalence class. Supposing this is possible, and supposing also that you computably have the isomorphism `f G : G ~= rep (mk G)`, i.e. that's not just an existence statement, then you have `choice` for group isomorphisms, since if `nonempty (G ~= H)` then `mk G = mk H` and hence you can construct `G ~= rep (mk G) = rep (mk H) ~= H`.

To turn this into at least unique choice, we can construct a group `H` which is isomorphic to `G = C_2` iff `α` is nonempty. For example, `H := Σ g : G, g ≠ 0 → trunc α` will do the trick. Then given an isomorphism `f : G ~= H`, we have `f 1 : psum (trunc α) (1 = 0)` from which we obtain an element of `trunc α`. This is not as strong as full choice, but it is known unprovable in lean.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476618):
@**Mario Carneiro** so what should I do? I'm confused, you keep saying it's unprovable but you're giving an algorithm

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 01 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476658):
I'm showing that if you could construct it you could prove something that is known unprovable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 01 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476659):
thus it's not computable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476664):
ok, then what should I do?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 01 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476675):
Live with the fact that going from an isomorphism class to a specific group is nonconstructive?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476715):
oh well, but I didn't use isomorphism class in the end

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 01 2018 at 06:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476721):
maybe you can phrase it independently of the choice then?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 06:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476722):
phrase what?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 01 2018 at 06:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476723):
your theorem, whatever it is

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 06:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476724):
that free group exists?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 01 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476762):
I'm not sure what you are trying to do now...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476765):
I realized that using isomorphism class is because of some stupid limitation of ZFC

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 01 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476766):
it's a limitation of lean too, I say

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476767):
I just stopped using it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476768):
and then I constructed the free group and proved its property

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 01 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476769):
did you though?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 01 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476770):
watch your universe levels

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 01 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476777):
I'm claiming you didn't construct the real free group

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476778):
I'm starting to suspect so

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 01 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476818):
Have you ever heard of system F encodings or church encodings?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476824):
I've heard of church encodings, if you're referring to the numbers

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 01 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476865):
I'm talking about the types. Something like this:
```
def unit := ∀ X : Type, X → X
def nat := ∀ X : Type, X → (X → X) → X
def prod (α β) := ∀ X : Type, (α → β → X) → X
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 06:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476870):
oh

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 06:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476871):
I get it, go on

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 01 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476912):
This sort of thing works great in system F, where there is only one impredicative data type `Type`, because then `unit : Type` etc and this has the expected universal property

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 01 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476915):
But in lean, it's not as strong as you want because the elimination property only goes to `Type 0` in this case while the constructed type lives in `Type 1`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 01 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476923):
Note that real eliminators such as are generated by `inductive` eliminate to `Sort u` where `u` is independent of the universes involved in the definition of the inductive type itself

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 01 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476924):
This allows creation of type families over the inductive type in very large universes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476963):
fair enough

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 01 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476968):
There is a curious property about these weak eliminators, though: *If* there exists a real type with the right eliminator, then you can prove that the weak type and the strong type are isomorphic, so the weak type inherits the strong eliminator

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476969):
hence what you mean by moving proof obligations around

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 01 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476970):
That means that your free group construction is correct if there is a free group

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124476971):
and here am I thinking that it's a brand new construction that nobody knows :P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 01 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124477010):
The size limitation thing is really important but manifests in weird ways in ZFC and lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 01 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124477057):
I think it's also related to the "B" in BNF, bounded natural functors used in isabelle for generating arbitrary (co)inductive types

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 01 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124477060):
which literally have an axiom on limitation of size, to prevent universe issues

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124477066):
🅱ounded 🅱atural 🅱unctors

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 01 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124477111):
now I need to make a "bounded natural blunders" joke

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124477264):
I'm thoroughly confused now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124493878):
Well that's really annoying. I thought that type theory was getting around these silly ZFC universe problems

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124493882):
but it's just moving them to Lean universe problems

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124493885):
same thought here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124493886):
Why do you care about isomorphic groups?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124493887):
Why not just work with all groups?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124493888):
right, I worked with all groups at the end

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124493889):
I was following the paper, which used isomorphic groups

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124493891):
my conjecture is that the author used isomorphism classes to make it justified in ZFC

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124493928):
Similarly you don't need to work with "generated by a subset of S"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124493931):
which i take to be a really shitty thing to do

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124493932):
That just seemed to be a red herring

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124493933):
right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124493934):
I didn't use that in my construction

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124493935):
but then it still depends on the universe

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124493936):
since you're quantifying over every group anyway

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124493984):
that's the thing with impredicative constructions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124493986):
you can send the other elements of $$S$$ to the identity

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124493987):
Oh I broke zulip

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124493988):
I can't edit $S$ into $$S$$

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494040):
you see, in ZFC this is the way you would do it:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494042):
firstly you consider only the isomorphism classes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494043):
Bingo, I had to reload the page.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494044):
and you only consider the groups generated by a subset of S

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494045):
because in some sense you can build it from S

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494082):
I don't see where the subset comes in

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494085):
but I do see where the isomorphism classes come in

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494087):
well

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494088):
they are both limitations on the size of the set

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494094):
after these two restrictions, you can justify the existence of the set by building it from a large enough set that you still build from S

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494096):
I don't see where they're needed in the ZFC proof.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494098):
if you don't limit the size of the generator, your set is still too big

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494099):
I want my generator to have size S

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494100):
exactly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494140):
ah

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494141):
hmm

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494142):
that's what you meant

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494143):
I suppose it's ok then

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494144):
So in ZFC I start with S and then I choose some cardinal kappa such that in V_kappa there is a copy of every group generated by S

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494151):
Lean is better because in Lean I don't think you even need that S generates G

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494154):
But as Mario points out, your answer is in the wrong universe.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 01 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494204):
I think you do need that S generates G if you don't want to run into universe problems

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494300):
In ZFC you do, but I don't see where you need it in Lean.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494347):
You just put a group structure on the product of G over all pairs (G,f:S -> G)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494353):
and give this a map from S

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494354):
and then take the intersection over all the subgroups containing the image of S

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 01 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/making%20isomorphism%20class%20a%20group/near/124494362):
This should definitely be in #**maths**

