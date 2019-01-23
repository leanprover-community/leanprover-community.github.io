---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/30861bundledbases.html
---

## Stream: [maths](index.html)
### Topic: [bundled bases](30861bundledbases.html)

---


{% raw %}
#### [ Johan Commelin (Oct 17 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/135955551):
I pushed the results of yesterdays painful efforts to https://github.com/leanprover-community/mathlib/blob/open_set/category_theory/examples/topological_spaces.lean. This wouldn't have been possible without the great help of @**Johannes Hölzl** 
I guess that some of the proofs need to be minimised. I obfuscated them as much as possible, and don't see how to squeeze out more. If someone wants to take a look, please go ahead.
The motivation for these changes is that we want to be able to talk about "sheaves on a basis".

#### [ Mario Carneiro (Oct 17 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/135990528):
I think `open_set` should be unbundled in the topology argument

#### [ Johan Commelin (Oct 17 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/135991087):
@**Mario Carneiro**  What do you mean with that?

#### [ Johan Commelin (Oct 17 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/135991108):
You want an unbundled version in `analysis/topology/blah.lean`?

#### [ Johan Commelin (Oct 17 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/135991165):
I think we also want the bundled version. But maybe I should first prove things with it, to show that it is useful.

#### [ Mario Carneiro (Oct 17 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/135994508):
I mean that for a fixed topological space, `@open_set X top_X` is a category

#### [ Mario Carneiro (Oct 17 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/135994589):
On top of that there is an `open_set` *functor*  from `Top` to `Type`, but that needs its own definition anyway

#### [ Mario Carneiro (Oct 17 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/135994650):
er, I think I mean lattice not category, I see you haven't given it a category structure

#### [ Mario Carneiro (Oct 17 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/135994706):
so in that case it could indeed move to `analysis/topology`. I would suggest the name `opens` for this lattice

#### [ Johan Commelin (Oct 17 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/135994710):
It is... every preorder is a category (in mathlib)

#### [ Mario Carneiro (Oct 17 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/135994724):
right, but you haven't made any explicit reference to categories in the definition

#### [ Johan Commelin (Oct 17 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/135994811):
Hmmm... I don't follow exactly. Do you want to change the definition of `open_set`? Or do you want to define `opens` and if so, what should it be?

#### [ Johan Commelin (Oct 17 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/135994954):
Also, should we change the definition of `open_set X` to `open_set X := X.str`? That is equivalent, and might simplify a lot of the stuff that follows...

#### [ Mario Carneiro (Oct 17 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/135997479):
`def opens (X : Type*) [topological_space X] : Type* := {s // is_open s}`

#### [ Mario Carneiro (Oct 17 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/135997602):
I don't understand the idea behind the `X.str` definition. The point is that `open_set X` is a type, not a structure

#### [ Mario Carneiro (Oct 17 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/135997659):
my proposal is `opens` as above, and `category.opens : Top ⥤ Cat` (or some other prefix?) has that as its object part

#### [ Mario Carneiro (Oct 17 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/135997756):
although maybe we need more functors than just that because it's properly a 2-functor

#### [ Johan Commelin (Oct 18 2018 at 05:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136018803):
@**Mario Carneiro** So `open_set` should go asway, and be replaced by `opens`?
What is wrong with:
```lean
def opens (X : Type*) [t : topological_space X] : Type* := subtype t.is_open
```
That is what I meant with the `X.str` definition.

#### [ Mario Carneiro (Oct 18 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136018818):
That doesn't typecheck?

#### [ Johan Commelin (Oct 18 2018 at 06:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136018953):
Ok, fair enough. I meant `subtype t.is_open`. I fixed this above.

#### [ Mario Carneiro (Oct 18 2018 at 06:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136018996):
that's the same as I wrote modulo eta expansion

#### [ Johan Commelin (Oct 18 2018 at 06:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136018999):
Right. So it doesn't matter.

#### [ Mario Carneiro (Oct 18 2018 at 06:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136019003):
well, you are also using a different `is_open`

#### [ Johan Commelin (Oct 18 2018 at 06:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136019018):
Aah, and maybe mine is more painful?

#### [ Mario Carneiro (Oct 18 2018 at 06:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136019025):
there are fewer lemmas about it

#### [ Johan Commelin (Oct 18 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136023764):
@**Mario Carneiro** Do you mean you would like to see something like this in `analysis/topology/topological_space.lean`?
```lean
section opens
variable (α)

def opens := {s : set α // _root_.is_open s}

variables {α}

instance : has_coe (opens α) (set α) := { coe := λ U, U.val }

instance : has_subset (opens α) :=
{ subset := λ U V, U.val ⊆ V.val }

instance : has_mem α (opens α) :=
{ mem := λ a U, a ∈ U.val }

@[extensionality] lemma ext {U V : opens α} (h : U.val = V.val) : U = V :=
by cases U; cases V; congr; exact h

instance topological_space.opens.partial_order : partial_order (opens α) := by refine { le := (⊆), .. } ; tidy

end opens
```
Note that I am using `tidy` in the last line. I don't know if this is too early in the mathlib-tree?

#### [ Johan Commelin (Oct 18 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136023792):
If this is the direction you had in mind, I can continue moving stuff from the category folder into this file; and then PR it.

#### [ Mario Carneiro (Oct 18 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136023793):
We have functions for transfering a partial order

#### [ Mario Carneiro (Oct 18 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136023837):
`partial_order.lift`

#### [ Mario Carneiro (Oct 18 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136023849):
I hope you aren't so attached to using blasty tactics that you are reproving theorems that we already have

#### [ Mario Carneiro (Oct 18 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136023856):
in fact, `subtype.partial_order` is just what you need

#### [ Mario Carneiro (Oct 18 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136023905):
`ext` is `subtype.eq`

#### [ Johan Commelin (Oct 18 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136023910):
Ok, that's fine with me. But about the general direction? Is this what you want?

#### [ Mario Carneiro (Oct 18 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136023918):
yes

#### [ Johan Commelin (Oct 18 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136023966):
But `subtype.ext` is not an ext-lemma

#### [ Johan Commelin (Oct 18 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136023971):
Should I phrase mine as an ext-lemma, or as an iff?

#### [ Mario Carneiro (Oct 18 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136024115):
I'm not saying you shouldn't state it, but it is a proof by reference to subtype.eq

#### [ Johan Commelin (Oct 18 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136024117):
Right. But which version should I state? Or both?

#### [ Mario Carneiro (Oct 18 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136024159):
`extensionality` requires the one-directional form

#### [ Mario Carneiro (Oct 18 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136024162):
I don't know if it would be better to use set extensionality as well though

#### [ Mario Carneiro (Oct 18 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136024168):
so it says `forall a, a \in U \lr a \in V`

#### [ Johan Commelin (Oct 18 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136024230):
`ext` can chain those together. So I think I'll only do the first step.

#### [ Johan Commelin (Oct 18 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136025567):
Done. See #427.

#### [ Scott Morrison (Oct 18 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136047222):
```quote
But `subtype.ext` is not an ext-lemma
```
I've been wondering about this one --- can we make `attribute [extensionality] subtype.eq`?

#### [ Mario Carneiro (Oct 18 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136047463):
ext can chain them, but you will get `x \in U.val` instead of `x \in U`


{% endraw %}
