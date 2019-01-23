---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/83465setisacompletelattice.html
---

## Stream: [general](index.html)
### Topic: [set is a complete lattice](83465setisacompletelattice.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 13 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set%20is%20a%20complete%20lattice/near/125037337):
mathlib proof:
```
instance lattice_set : complete_lattice (set α) :=
{ lattice.complete_lattice .
  le           := (⊆),
  le_refl      := subset.refl,
  le_trans     := assume a b c, subset.trans,
  le_antisymm  := assume a b, subset.antisymm,

  lt           := λ x y, x ⊆ y ∧ ¬ y ⊆ x,
  lt_iff_le_not_le := λ x y, iff.refl _,

  sup          := (∪),
  le_sup_left  := subset_union_left,
  le_sup_right := subset_union_right,
  sup_le       := assume a b c, union_subset,

  inf          := (∩),
  inf_le_left  := inter_subset_left,
  inf_le_right := inter_subset_right,
  le_inf       := assume a b c, subset_inter,

  top          := {a | true },
  le_top       := assume s a h, trivial,

  bot          := ∅,
  bot_le       := assume s a, false.elim,

  Sup          := λs, {a | ∃ t ∈ s, a ∈ t },
  le_Sup       := assume s t t_in a a_in, ⟨t, ⟨t_in, a_in⟩⟩,
  Sup_le       := assume s t h a ⟨t', ⟨t'_in, a_in⟩⟩, h t' t'_in a_in,

  Inf          := λs, {a | ∀ t ∈ s, a ∈ t },
  le_Inf       := assume s t h a a_in t' t'_in, h t' t'_in a_in,
  Inf_le       := assume s t t_in a h, h _ t_in }
```
my proof:
```
instance lattice_set : complete_lattice (set α) :=
lattice.complete_lattice_fun
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 13 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set%20is%20a%20complete%20lattice/near/125037338):
I win

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Apr 13 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set%20is%20a%20complete%20lattice/near/125037562):
I guess `Sup` and `Inf` are defined differently now?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 13 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set%20is%20a%20complete%20lattice/near/125037602):
really?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Apr 13 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set%20is%20a%20complete%20lattice/near/125037907):
They should be equal.   However I don't think they are definitionally equal.  `Sup s a = (∃ b ∈ set.image (λ f, f a) s, b) = (∃ b, (∃ c, s c ∧ s c a = b) → b)` which is different

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 13 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set%20is%20a%20complete%20lattice/near/125037929):
well one could prove that they are equal

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 13 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set%20is%20a%20complete%20lattice/near/125037930):
simp lemma

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Apr 13 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set%20is%20a%20complete%20lattice/near/125037988):
This still doesn't give you definitional reduction.  If you want to prove `a ∈ Sup s`, you'll now always need to `simp` first.  There are quite a few places where we accept some additional complexity in order to guarantee good definitional reduction, the `lt` in preorder is another place.  We can define `lt` in terms of `le`, but we want it to reduce differently for natural numbers.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 13 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set%20is%20a%20complete%20lattice/near/125037998):
I see

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 13 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set%20is%20a%20complete%20lattice/near/125038503):
Yes, for nat, `a<b` is _defined_ to be `succ a <= b` and if you know this you can write some neat obfuscated code :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 13 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set%20is%20a%20complete%20lattice/near/125038512):
such as?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 13 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set%20is%20a%20complete%20lattice/near/125038557):
I believe I used this to do some golf question here a week or two ago. Either a question of Chris or of Nima.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 13 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set%20is%20a%20complete%20lattice/near/125038813):
It just means that you never have to use the lemma `succ_le_of_lt`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 13 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set%20is%20a%20complete%20lattice/near/125039063):
you can `match` or use the equation compiler to do case analysis and inductionon `<`, with the definition following the default setup this would be not possible.

