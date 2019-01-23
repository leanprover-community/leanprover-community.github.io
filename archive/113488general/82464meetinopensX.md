---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/82464meetinopensX.html
---

## Stream: [general](index.html)
### Topic: [meet in opens X](82464meetinopensX.html)

---


{% raw %}
#### [ Johan Commelin (Nov 10 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meet%20in%20opens%20X/near/147442296):
If I have `U V : opens X`, then `(U ⊓ V).val` is not defeq to `U.val ∩ V.val`. Can this be fixed while still using the galois insertion to define the lattice structure on `opens X`?

#### [ Johan Commelin (Nov 12 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meet%20in%20opens%20X/near/147524558):
A related thing that I'm worried about: the opposite category of the category associated with a preorder is not going to be defeq to the category associated with the dual order.

#### [ Johannes Hölzl (Nov 12 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meet%20in%20opens%20X/near/147525462):
`(U ⊓ V).val := U.val ∩ V.val` should be possible. And I think also that `op ∘ order2cat = order2cat ∘ dual` could be `rfl`. On both sides we construct a category using the constructor, which looks at the Hom-set fully expanded (so no funext is needed). So both sides should reduce to something like `λα [ord], ⟨α, λa b, a ≥ b, ...⟩` (plus/minus some things).

Be aware that this is different to `op (op C) = C` where `C` doesn't reduce further

#### [ Johan Commelin (Nov 12 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meet%20in%20opens%20X/near/147525508):
Ok, that's reassuring. Thanks!
So how should we make `(U ⊓ V).val := U.val ∩ V.val` happen?

#### [ Johannes Hölzl (Nov 12 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meet%20in%20opens%20X/near/147526957):
wait, you mean the other way round, right?
```lean
lemma test (u v : opens α) : (u ⊔ v).val = u.val ∪ v.val := rfl
```
works

#### [ Johannes Hölzl (Nov 12 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meet%20in%20opens%20X/near/147527006):
Ah I see. We need to use `complete_lattice.copy`

#### [ Johannes Hölzl (Nov 12 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meet%20in%20opens%20X/near/147527078):
there we can override the lattice operations with equal ones

#### [ Johan Commelin (Nov 12 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meet%20in%20opens%20X/near/147527609):
I have no experience with this...

#### [ Johan Commelin (Nov 17 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meet%20in%20opens%20X/near/147882867):
What is going on here? https://github.com/leanprover/mathlib/blob/master/order/filter.lean#L314
Locally there are two instances of complete lattice. Why does that not create trouble?
Also, once the complete lattice structure is copied, how can the Galois connection still work?

#### [ Reid Barton (Nov 17 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meet%20in%20opens%20X/near/147885913):
"Locally" here is only up to the end of the section (line 341), and there's nothing else in the section.

#### [ Reid Barton (Nov 17 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meet%20in%20opens%20X/near/147886091):
And by definition the new instance agrees with the existing `preorder`, `has_top`, `has_inf` instances

#### [ Johan Commelin (Dec 04 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meet%20in%20opens%20X/near/150871778):
@**Johannes Hölzl** Does this look like what you had in mind?
```lean
instance : complete_lattice (opens α) :=
complete_lattice.copy
(@order_dual.lattice.complete_lattice _
  (@galois_insertion.lift_complete_lattice
    (order_dual (set α)) (order_dual (opens α)) _ interior (subtype.val : opens α → set α) _ gi))
/- le  -/ (λ U V, U.1 ⊆ V.1) rfl
/- top -/ ⟨set.univ, _root_.is_open_univ⟩ (subtype.ext.mpr interior_univ.symm)
/- bot -/ ⟨∅, is_open_empty⟩ rfl
/- sup -/ (λ U V, ⟨U.1 ∪ V.1, _root_.is_open_union U.2 V.2⟩) rfl
/- inf -/ (λ U V, ⟨U.1 ∩ V.1, _root_.is_open_inter U.2 V.2⟩)
begin
  funext,
  apply subtype.ext.mpr,
  symmetry,
  apply interior_eq_of_open,
  exact (_root_.is_open_inter U.2 V.2),
end
/- Sup -/ (λ Us, ⟨⋃₀ (subtype.val '' Us), _root_.is_open_sUnion $ λ U hU,
by { rcases hU with ⟨⟨V, hV⟩, h, h'⟩, dsimp at h', subst h', exact hV}⟩)
begin
  funext,
  apply subtype.ext.mpr,
  simp [Sup_range],
  refl,
end
/- Inf -/ _ rfl
```

#### [ Johan Commelin (Dec 04 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meet%20in%20opens%20X/near/150872320):
I guess this also needs a bunch of simp-lemmas to be useful?
Of the form `opens_sup_val : (U \cap V).val = U.val \cap V.val := rfl`.

#### [ Johan Commelin (Dec 04 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meet%20in%20opens%20X/near/150872680):
The only thing I'm not so sure about is the `Sup` case of the "copy". It isn't `rfl` to what comes out of the galois insertion, but it also isn't very far of. Should I just use what comes out of the galois insertion, or is what I provide here the more useful thing. Feedback appreciated.

#### [ Johannes Hölzl (Dec 04 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meet%20in%20opens%20X/near/150877968):
Yes, that's what I had in mind. If `Sup` doesn't make sense, then you don't need to change it. Just `_` for `Sup` and `rfl` for the equality proof.

#### [ Johan Commelin (Dec 05 2018 at 05:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meet%20in%20opens%20X/near/150901943):
`Sup` is meaningful, and it gives you the "correct" answer modulo `Sup_range`. So now the question becomes whether I should make that simplification step here, or leave it to the user.
The one that is meaningless is `Inf`: it is the interior of an arbitrary intersection of opens.

#### [ Johan Commelin (Dec 05 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/meet%20in%20opens%20X/near/150903641):
#511


{% endraw %}
