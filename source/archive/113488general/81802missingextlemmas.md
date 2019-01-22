---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/81802missingextlemmas.html
---

## [general](index.html)
### [missing ext lemmas?](81802missingextlemmas.html)

#### [Johan Commelin (Oct 03 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135088491):
How many of the following should be marked with `@[extensionality]`?
```lean
data/buffer/basic.lean:lemma ext : ∀ {b₁ b₂ : buffer α}, to_list b₁ = to_list b₂ → b₁ = b₂
data/equiv/basic.lean:lemma ext (f g : equiv α β) (H : ∀ x, f x = g x) : f = g :=
data/finsupp.lean:lemma ext : ∀{f g : α →₀ β}, (∀a, f a = g a) → f = g
data/list/basic.lean:lemma foldl_ext (f g : α → β → α) (a : α)
data/list/basic.lean:lemma foldr_ext (f g : α → β → β) (b : β)
data/prod.lean:lemma ext {α β} {p q : α × β} : p.1 = q.1 → p.2 = q.2 → p = q :=
data/subtype.lean:lemma subtype.ext {a1 a2 : {x // β x}} : a1 = a2 ↔ a1.val = a2.val :=
data/subtype.lean:lemma subtype.coe_ext {a1 a2 : {x // β x}} : a1 = a2 ↔ (a1 : α) = a2 :=
logic/function.lean:lemma hfunext {α α': Sort u} {β : α → Sort v} {β' : α' → Sort v} {f : Πa, β a} {f' : Πa, β' a}
order/filter.lean:protected lemma ext : (∀ s, s ∈ f.sets ↔ s ∈ g.sets) → f = g :=
category/applicative.lean:theorem applicative.ext {F} : ∀ {A1 : applicative F} {A2 : applicative F}
category/functor.lean:theorem functor.ext {F} : ∀ {F1 : functor F} {F2 : functor F}
data/analysis/topology.lean:theorem ext [T : topological_space α] {σ : Type*} {F : ctop α σ}
data/complex/basic.lean:theorem ext : ∀ {z w : ℂ}, z.re = w.re → z.im = w.im → z = w
data/finset.lean:theorem ext {s₁ s₂ : finset α} : s₁ = s₂ ↔ ∀ a, a ∈ s₁ ↔ a ∈ s₂ :=
data/list/basic.lean:theorem ext : ∀ {l₁ l₂ : list α}, (∀n, nth l₁ n = nth l₂ n) → l₁ = l₂
data/list/perm.lean:theorem perm_ext {l₁ l₂ : list α} (d₁ : nodup l₁) (d₂ : nodup l₂) : l₁ ~ l₂ ↔ ∀a, a ∈ l₁ ↔ a ∈ l₂ :=
data/multiset.lean:theorem ext {s t : multiset α} : s = t ↔ ∀ a, count a s = count a t :=
data/multiset.lean:theorem nodup_ext {s t : multiset α} : nodup s → nodup t → (s = t ↔ ∀ a, a ∈ s ↔ a ∈ t) :=
data/multiset.lean:theorem erase_dup_ext {s t : multiset α} : erase_dup s = erase_dup t ↔ ∀ a, a ∈ s ↔ a ∈ t :=
data/option.lean:theorem ext : ∀ {o₁ o₂ : option α}, (∀ a, a ∈ o₁ ↔ a ∈ o₂) → o₁ = o₂
data/real/cau_seq.lean:theorem ext {f g : cau_seq β abv} (h : ∀ i, f i = g i) : f = g :=
data/semiquot.lean:theorem ext {q₁ q₂ : semiquot α} : q₁ = q₂ ↔ ∀ a, a ∈ q₁ ↔ a ∈ q₂ :=
data/seq/wseq.lean:theorem equiv.ext {s t : wseq α} (h : ∀ n, nth s n ~ nth t n) : s ~ t :=
data/set/basic.lean:theorem set_coe.ext {s : set α} {a b : s} : (↑a : α) = ↑b → a = b :=
data/set/basic.lean:theorem ext {a b : set α} (h : ∀ x, x ∈ a ↔ x ∈ b) : a = b :=
group_theory/free_abelian_group.lean:protected theorem ext (g h : free_abelian_group α → β)
linear_algebra/linear_map_module.lean:theorem ext (h : ∀ x, A x = B x) : A = B := subtype.eq $ funext h
linear_algebra/tensor_product.lean:theorem to_module.ext {g h : M ⊗ N → P}
number_theory/dioph.lean:  theorem ext {S S' : set (α → ℕ)} (d : dioph S) (H : ∀v, S v ↔ S' v) : dioph S' :=
number_theory/pell.lean:  theorem ext : ∀ {z w : ℤ√d}, z = w ↔ z.re = w.re ∧ z.im = w.im
order/basic.lean:theorem preorder.ext {α} {A B : preorder α}
order/basic.lean:theorem partial_order.ext {α} {A B : partial_order α}
order/basic.lean:theorem linear_order.ext {α} {A B : linear_order α}
order/bounded_lattice.lean:theorem order_top.ext {α} {A B : order_top α}
order/bounded_lattice.lean:theorem order_bot.ext {α} {A B : order_bot α}
order/bounded_lattice.lean:theorem bounded_lattice.ext {α} {A B : bounded_lattice α}
order/lattice.lean:theorem semilattice_sup.ext {α} {A B : semilattice_sup α}
order/lattice.lean:theorem semilattice_inf.ext {α} {A B : semilattice_inf α}
order/lattice.lean:theorem lattice.ext {α} {A B : lattice α}
set_theory/zfc.lean:theorem equiv.ext : Π (x y : pSet), equiv x y ↔ (x ⊆ y ∧ y ⊆ x)
set_theory/zfc.lean:theorem mem.ext : Π {x y : pSet.{u}}, (∀w:pSet.{u}, w ∈ x ↔ w ∈ y) → equiv x y
set_theory/zfc.lean:theorem ext {x y : Set.{u}} : (∀z:Set.{u}, z ∈ x ↔ z ∈ y) → x = y :=
```

#### [Johan Commelin (Oct 03 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135088502):
Is it worth going through this list. Or have people done that before, and decided that this should not get the `extensionality` attribute?

#### [Kenny Lau (Oct 03 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135089015):
thanks for bringing this up

#### [Patrick Massot (Oct 03 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135089062):
I think it's worth going through the list

#### [Simon Hudon (Oct 03 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135089070):
I, for one, have not done it and I was working on the basis of "let's add them when we need them" after I added the most obvious ones.

#### [Johan Commelin (Oct 03 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135089396):
Can someone give an entry on the list that should *not* be tagged with the `extensionality` attribute? If I understand the reason, then I might be able to go through the list myself.

#### [Simon Hudon (Oct 03 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135089575):
`set_theory/zfc.lean:theorem equiv.ext`

#### [Scott Morrison (Oct 03 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135089902):
You missed `yoneda.ext` :-). (Perhaps because it's a `def`?)  Anyway, it probably shouldn't have `@[extensionality]`.

#### [Simon Hudon (Oct 03 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135089964):
Also, I wouldn't tag `semilattice_sup.ext_sup`

#### [Johan Commelin (Oct 03 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135090054):
Can you explain why?

#### [Johan Commelin (Oct 03 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135090064):
@**Scott Morrison|110087** Indeed, I only looked for lemmas and theorems

#### [Simon Hudon (Oct 03 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135090608):
It's a comparison of class instances rather than the objects themselves. It seems like it could produce surprising results

#### [Johan Commelin (Oct 03 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135090806):
Ok, I see. @**Johannes Hölzl** Does it make sense to create an `extensionality` PR that adds about 40 `extensionality` attributes?

#### [Johannes Hölzl (Oct 03 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135090874):
Do we have 40 types? Are sensible? Also be careful that they don't overlap.

#### [Johan Commelin (Oct 03 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135090907):
See the list I posted above.

#### [Johan Commelin (Oct 03 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135090923):
Simon mentioned a couple that shouldn't be tagged, but I think a lot of them could reasonably be tagged.

#### [Simon Hudon (Oct 03 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135091116):
Some of them are equivalences while `ext` uses implications. When I encounter such lemma, I rename them `ext_iff` so that I can add a `ext` lemma as an implication

#### [Johannes Hölzl (Oct 03 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135097606):
also before you add the extensionality lemmas we should change the semantics of `ext`. Instead of applying all possible extensionality lemmas it should only work along the names given by the user, or accept `*` to apply all.

#### [Johan Commelin (Oct 03 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135097698):
Hmm, ok. Do you mean you want people to write `ext set` or `ext subtype` etc...?

#### [Simon Hudon (Oct 03 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135097745):
Right now, `ext` detects the type of the arguments (e.g. set) and only tries relevant extensionality lemmas

#### [Simon Hudon (Oct 03 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135097758):
It used to be that functional extensionality might be selected for the equality of two sets. It's no longer the case.

#### [Patrick Massot (Oct 03 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135097764):
Johannes, that would be very sad

#### [Patrick Massot (Oct 03 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135097769):
I like to type `ext` and Lean figures out what I mean

#### [Johannes Hölzl (Oct 03 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135097780):
and I hate it to add an attribute and half of mathlib breaks

#### [Mario Carneiro (Oct 03 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135097781):
Johannes this was implemented recently, like simon says

#### [Johannes Hölzl (Oct 03 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135097790):
okay, thats good!

#### [Mario Carneiro (Oct 03 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135097800):
You don't need to say `ext set`, it looks at the type of the objects in the equality in the goal

#### [Simon Hudon (Oct 03 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135097851):
It's also tolerant on the kind of relation you can prove but I think sticking close to `=` is a good idea.

#### [Mario Carneiro (Oct 03 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135097866):
But this also means that you essentially want one extensionality lemma for each type, so no multiples, and no equalities over generic types

#### [Johan Commelin (Oct 03 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135097868):
Right, but `functor.ext` seems like a good exception

#### [Mario Carneiro (Oct 03 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135097939):
If there are multiple candidates for extensionality, e.g. `roption.ext` vs `roption.ext'` then you have to think about which one is better general-purpose and pick one

#### [Simon Hudon (Oct 03 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135097970):
@**Johan Commelin** I'm tempted to agree with you but technically, there's no reason why `functor.ext` wouldn't work as an extensionality lemma

#### [Johan Commelin (Oct 03 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135097992):
@**Simon Hudon** I meant that it is an exception to sticking to `=`

#### [Mario Carneiro (Oct 03 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135097994):
Also keep in mind that `ext` will apply all extensionality lemmas it can all the way down so you don't want loopable hypotheses

#### [Simon Hudon (Oct 03 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135098052):
@**Mario Carneiro** You can also give the most general one a lower priority

#### [Johan Commelin (Oct 03 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135098057):
Or we want `ext` to take an optional `small_nat` argument like `congr`

#### [Johan Commelin (Oct 03 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135098062):
Or `congr'`, whatever

#### [Simon Hudon (Oct 03 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135098066):
It already does: `ext : 3`

#### [Mario Carneiro (Oct 03 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135098081):
AFAIK competing extensionality lemmas always apply in the same generality, they just have different hypotheses, so giving priority wouldn't help

#### [Simon Hudon (Oct 03 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135098082):
But I think Mario is right. There has to be a sense that something decreases as we keep applying `ext`, for instance the complexity of the objects being compared

#### [Simon Hudon (Oct 03 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135098144):
@**Mario Carneiro** I don't understand what you mean by "in the same generality"

#### [Mario Carneiro (Oct 03 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135098185):
Most theorems that could qualify as `@[extensionality]` have a conclusion `(a : T) = b`, so if this is the goal then all extensionalities for T will apply

#### [Mario Carneiro (Oct 03 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135098270):
With other kinds of theorems there might be a difference in generality like if one theorem only has say `F a = G b` in the conclusion, but with extensionality lemmas it's always `a = b` where `a` and `b` match anything in the type

#### [Simon Hudon (Oct 03 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135098278):
You could see one lemma being `(a : set α) = b` and another be `(a : set (list α)) = b`. The first one is the most general one although both would be attempted

#### [Mario Carneiro (Oct 03 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135098339):
I suppose that is a possibility, but so far I don't think we have any such "composite extensionality lemmas"

#### [Mario Carneiro (Oct 03 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135098348):
it's always a constant or type constructor applied to variables

#### [Mario Carneiro (Oct 03 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135098445):
Looking at the list, I see `free_abelian_group.ext` and `to_module.ext` have composite types, and `dioph` has something that isn't an extensionality at all

#### [Mario Carneiro (Oct 03 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135098492):
I don't think `free_abelian_group.ext` qualifies as an extensionality, this is some kind of yoneda thing

#### [Patrick Massot (Oct 03 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135133090):
what about `topological_space_eq`?

#### [Patrick Massot (Oct 03 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/missing%20ext%20lemmas%3F/near/135133135):
yes

