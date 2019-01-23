---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/96225422limitsinCommRing.html
---

## Stream: [PR reviews](index.html)
### Topic: [#422 limits in CommRing](96225422limitsinCommRing.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135796679):
@**Patrick Massot**, I've started a WIP branch to construct products and equalizers in CommRing.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135796726):
Products work just fine. Equalizers still has lots of sorries, mostly because I'm not willing to get my hands dirty and do things by brute force. All the remaining goals are just about manipulating `is_ring_hom`. I wish most of them were solved by `simp`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135796732):
There's also an instance where `by subtype_instance` doesn't do what I hoped it would do. Perhaps @**Simon Hudon** would like to look at this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135796738):
Typical examples of the remaining goals are:
```
R S : examples.CommRing,
f g : R ⟶ S
⊢ set.mem (add_monoid.zero ↥R) {r : ↥R | ⇑f r = ⇑g r}
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135796787):
(A subproblem here is to explain to me why this has `set.mem` instead of `\in`, and `add_monoid.zero ↥R` instead of `0`! I'm really confused by both.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135796790):
If anyone wants to hack on this branch, please feel free.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135796796):
I've just arrived at a conference I'm organising, and probably should stop working on lean for a while. :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 15 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135796810):
I was going to say "you should post more precise coordinates about where this branch is" and then I remembered that you can click on the link in the title of the thread :D

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 15 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135796847):
the weird unfolding is probably because you have a universe metavariable

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135796858):
The equalizers file is at https://github.com/leanprover/mathlib/pull/422/files#diff-cc1aad82649d34fb81afe5403e9bd67f.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 05:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805078):
I've just pushed an attempt at products in `Top`, that reduces it to two `sorry` statements, which don't mention any category theory.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805099):
If you pull the `limits-examples` branch of `https://github.com/leanprover-community/mathlib/`, you'll find `https://github.com/leanprover-community/mathlib/blob/limits-examples/category_theory/examples/topological_spaces/products.lean`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805150):
The two remaining goals are just
```
β : Type u,
f : β → Top,
b : β
⊢ continuous (λ (g : Π (b : β), ↥(f b)), g b)
```
(here `↥(f b)` just means the underlying type of the `Top`)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805155):
and
```
α : Type u,
β : α → Type v,
R : Π (a : α), topological_space (β a),
γ : Type w,
_inst_1 : topological_space γ,
f : Π (a : α), γ → β a,
Rh : ∀ (a : α), continuous (f a)
⊢ continuous (λ (x : γ) (b : α), f b x)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 05:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805170):
which I think needs no explaination, and is presumably meant to be proved by switching the arguments in `continuous_pi` (which I discovered only because I tried to name this lemma `continuous_pi`).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 05:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805232):
Duh, the second one is exactly `continuous_pi`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 15 2018 at 05:49)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805241):
I am not sure what we are looking for, but I think that statement looks much nicer than the one with the fans

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 15 2018 at 05:49)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805244):
it's much more obvious what we need to prove

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 05:51)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805327):
duh, and the first one is just continuous_apply

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 05:51)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805338):
I agree, Mario. The problem was really @**Patrick Massot** typing `tidy` a bit too soon. :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 05:52)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805378):
I just pushed [this](https://github.com/leanprover-community/mathlib/blob/limits-examples/category_theory/examples/topological_spaces/products.lean).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 15 2018 at 05:52)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805379):
I'm surprised case on the fans is not done by the auto_cases stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 05:53)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805387):
No, it's not. auto_cases is pretty timid

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 05:53)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805393):
if you're trying to construct a fan, tidy will use split and intro to get you most of the way there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 05:54)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805435):
(just in case anyone followed that link, I was a moment too fast, and you might want to reload it :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 15 2018 at 05:55)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805455):
what does it mean that `Top.pi_π` is `@[simp]`? (Also that name is a bit confusing...)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 05:56)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805498):
Tagging it with @[simp] like that somehow(?!) encourages Lean to unfold its definition more freely later.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 05:56)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805499):
I don't understand that mechanism at all.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 05:56)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805501):
But I've found that you can often avoid stating lots of `rfl` lemmas just by putting `@[simp]` on the construction itself.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 15 2018 at 05:56)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805502):
oh, that means it marks the equation lemmas as `@[simp]`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 05:56)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805505):
Sorry, voodoo-programming. :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 15 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805506):
because it's a `def`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805514):
Cool, okay, I'll say that's why, if asked in future. :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805517):
The first @[simp] was unnecessary, so I removed it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 05:58)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805558):
I agree the name is bad. But I uniformly use `π` and `iota` for the maps in cones and cocones

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 05:58)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805559):
and I think `pi` is the correct name when talking about product types

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805566):
so you end up with the name collision `pi_π` for the maps out of product types ... :-(

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 15 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805642):
why the `dsimp` in the first construction and `convert` in the second instead of directly applying the theorem?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805644):
@**Mario Carneiro**, if you have a chance, could you explain that "universe metavariable" comment from above?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805646):
I've fixed those; reload.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 06:02)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805691):
It's now the [`rings/equalizers.lean`](https://github.com/leanprover-community/mathlib/blob/limits-examples/category_theory/examples/rings/equalizers.lean) file that I'm really unhappy about...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 15 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805814):
It's a weird bug that Kenny discovered. Here's a MWE:
```lean
instance sg {α} : semigroup α := sorry
instance mm {α} : monoid α :=
{ one := sorry,
  one_mul := sorry,
  mul_one := _, -- ∀ (a : α), semigroup.mul a sorry = a
  ..sg }
```

```lean
instance sg {α} : semigroup α := sorry
instance mm {α : Type u} : monoid α :=
{ one := sorry,
  one_mul := sorry,
  mul_one := _, -- ∀ (a : α), a * 1 = a
  ..sg }
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805815):
If I could understand why `set.mem` and `add_monoid` have mysteriously appeared, I could ask Simon why `subtype_instance` doesn't work. :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805835):
That is weird!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 15 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805838):
the presence of universe metavariables in the type of the theorem causes lean to unfold all sorts of stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 06:08)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135805894):
indeed, changing `CommRing` to `CommRing.{v}` solves that problem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 15 2018 at 11:03)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135817239):
```quote
I agree, Mario. The problem was really Patrick Massot typing `tidy` a bit too soon. :-)
```
What happened is I copied the proof from Type and started to edit where things went wrong...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 15 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135817319):
Thanks for your explanations Scott. I think it's unavoidable that  notations needs to be learned in order to use the category theory goodies. But hopefully it will be much easier with more examples

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 15 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23422%20limits%20in%20CommRing/near/135817428):
```quote
There's also an instance where `by subtype_instance` doesn't do what I hoped it would do. Perhaps Simon Hudon would like to look at this?
```
This tactic is really specialized, it's meant to prove substuff is stuff, starting from the definition of substuff, assuming that definition obeys standard naming conventions. It never claimed to be able to prove any random subtype of some stuff is stuff.

