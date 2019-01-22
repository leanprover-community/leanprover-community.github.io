---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/74503commringclosure.html
---

## [maths](index.html)
### [comm_ring.closure](74503commringclosure.html)

#### [Patrick Massot (Oct 09 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135495590):
@**Kenny Lau** Do you secretely have `comm_ring.closure` with a `subring` instance somewhere in your repositories?

#### [Kenny Lau (Oct 09 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135495611):
I don't think so.

#### [Patrick Massot (Oct 09 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135495859):
Too bad. Do you want to sprint through it?

#### [Kenny Lau (Oct 09 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135495873):
sure

#### [Patrick Massot (Oct 09 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135495989):
I began with
```lean
import ring_theory.subring

namespace group
variables {α : Type*} [group α]
theorem exists_list_of_mem_closure {s : set α} {a : α} (h : a ∈ closure s) :
  (∃l:list α, (∀x∈l, x ∈ s ∨ x⁻¹ ∈ s) ∧ l.prod = a) :=
begin
  induction h,
  case in_closure.basic : a ha { existsi ([a]), simp [ha] },
  case in_closure.one { existsi ([]), simp },
  case in_closure.mul : a b _ _ ha hb {
    rcases ha with ⟨la, ha, eqa⟩,
    rcases hb with ⟨lb, hb, eqb⟩,
    existsi (la ++ lb),
    simp [eqa.symm, eqb.symm, or_imp_distrib],
    exact assume a, ⟨ha a, hb a⟩
  },
  case in_closure.inv : a a_in_clo hlist {
    rcases hlist with ⟨la, ha, eqa⟩,
    existsi (la.reverse.map (λ x, x⁻¹)),
    split,
    { intros x x_in,
      rw list.mem_map at x_in,
      rcases x_in with ⟨b, b_in, hb⟩,
      rw list.mem_reverse at b_in,
      specialize ha b b_in,
      have hb' : b = x⁻¹, by rw ←hb ; simp,
      rw [hb, hb'] at ha,
      cc },
    { rw [←eqa, inv_prod la] } }
end
end group

namespace add_group
variables {α : Type*} [add_group α]

theorem exists_list_of_mem_closure {s : set α} {a : α} (h : a ∈ closure s) :
  (∃l:list α, (∀x∈l, x ∈ s ∨ -x ∈ s) ∧ l.sum = a) :=
sorry
end add_group

namespace comm_ring
variables {R : Type*} [comm_ring R]

def closure (s : set R) := add_group.closure (monoid.closure s)

instance {s : set R} : is_subring (closure s) :=
begin
  dunfold closure,
  exact
    { zero_mem := is_add_submonoid.zero_mem _,
      add_mem := λ a b ha hb, is_add_submonoid.add_mem ha hb,
      neg_mem := λ a h, is_add_subgroup.neg_mem h,
      one_mem := add_group.mem_closure (is_submonoid.one_mem _),
      mul_mem := begin
        intros a b a_in b_in,
        rcases add_group.exists_list_of_mem_closure a_in with ⟨la, hla, sum_a⟩,
        rcases add_group.exists_list_of_mem_closure b_in with ⟨lb, hlb, sum_b⟩,
        rw [←sum_a, ←sum_b],
        sorry,
      end }
end

end comm_ring
```

#### [Patrick Massot (Oct 09 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135496035):
But I lost courage because of https://leanprover.zulipchat.com/#narrow/stream/116395-maths/subject/to_additive.20multiplicative/near/135470227 and sum manipulations

#### [Patrick Massot (Oct 09 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135496067):
The trouble is that the big_operator stuff in mathlib is all about sums over finset, not lists

#### [Patrick Massot (Oct 09 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135496121):
(here I mean the trouble with the final sorry, the `to_additive` stuff is simply total mystery)

#### [Kenny Lau (Oct 09 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135497365):
```lean
import ring_theory.subring

universe u

@[elab_as_eliminator]
theorem add_monoid.in_closure.rec_on {α : Type u} [add_monoid α] {s : set α} {C : α → Prop}
  {a : α} (H : a ∈ add_monoid.closure s)
  (H1 : ∀ {a : α}, a ∈ s → C a) (H2 : C 0)
  (H3 : ∀ {a b : α}, a ∈ add_monoid.closure s → b ∈ add_monoid.closure s → C a → C b → C (a + b)) :
  C a :=
monoid.in_closure.rec_on H (λ _, H1) H2 (λ _ _, H3)

@[elab_as_eliminator]
theorem add_group.in_closure.rec_on {α : Type u} [add_group α] {s : set α} {C : α → Prop}
  {a : α} (H : a ∈ add_group.closure s)
  (H1 : ∀ {a : α}, a ∈ s → C a) (H2 : C 0) (H3 : ∀ {a : α}, a ∈ add_group.closure s → C a → C (-a))
  (H4 : ∀ {a b : α}, a ∈ add_group.closure s → b ∈ add_group.closure s → C a → C b → C (a + b)) :
  C a :=
group.in_closure.rec_on H (λ _, H1) H2 (λ _, H3) (λ _ _, H4)

namespace comm_ring
variables {R : Type u} [comm_ring R]

def closure (s : set R) := add_group.closure (monoid.closure s)

local attribute [reducible] closure

instance {s : set R} : is_subring (closure s) :=
{ zero_mem := is_add_submonoid.zero_mem _,
  add_mem := λ a b ha hb, is_add_submonoid.add_mem ha hb,
  neg_mem := λ a h, is_add_subgroup.neg_mem h,
  one_mem := add_group.mem_closure (is_submonoid.one_mem _),
  mul_mem := λ a b ha hb, add_group.in_closure.rec_on hb
    (λ b hb, add_group.in_closure.rec_on ha
      (λ a ha, add_group.subset_closure (is_submonoid.mul_mem ha hb))
      ((zero_mul b).symm ▸ is_add_submonoid.zero_mem _)
      (λ a ha hab, (neg_mul_eq_neg_mul a b) ▸ is_add_subgroup.neg_mem hab)
      (λ a c ha hc hab hcb, (add_mul a c b).symm ▸ is_add_submonoid.add_mem hab hcb))
    ((mul_zero a).symm ▸ is_add_submonoid.zero_mem _)
    (λ b hb hab, (neg_mul_eq_mul_neg a b) ▸ is_add_subgroup.neg_mem hab)
    (λ b c hb hc hab hac, (mul_add a b c).symm ▸ is_add_submonoid.add_mem hab hac) }

end comm_ring
```

#### [Kenny Lau (Oct 09 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135497371):
@**Patrick Massot**

#### [Patrick Massot (Oct 09 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135497490):
Thanks!

#### [Patrick Massot (Oct 09 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135497506):
Could we still get the list statements analogue to what is already in mathlib for monoids?

#### [Patrick Massot (Oct 09 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135497537):
Is the reducible attribute purely intended to save a couple of `dunfold` in the instance building?

#### [Kenny Lau (Oct 09 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135497735):
```quote
Is the reducible attribute purely intended to save a couple of `dunfold` in the instance building?
```
yes

#### [Patrick Massot (Oct 09 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135497881):
Why do you get `monoid.in_closure.rec_on` for free when defining `monoid.in_closure` but need to write `add_monoid.in_closure.rec_on`?

#### [Patrick Massot (Oct 09 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135497906):
Is it because of the multiplicative to additive magic?

#### [Patrick Massot (Oct 09 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135497918):
which is not magic enough?

#### [Kenny Lau (Oct 09 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135498021):
because `add_monoid.closure` is not defined using `to_additive`

#### [Patrick Massot (Oct 09 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135498278):
And why isn't it defined using `to_additive`?

#### [Patrick Massot (Oct 09 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135498343):
The definition is really weird. At some point earlier Lean was completely confused and asked me to prove stuff involving 1 in an additive context

#### [Patrick Massot (Oct 09 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135498464):
I would have never thought of proving that instance using these nested inductions. The real world proof manipulating sums is so easy, it seems beyond masochistic to write your proof.

#### [Kenny Lau (Oct 09 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135498625):
```lean
theorem exists_list_of_mem_closure {s : set α} {a : α} (h : a ∈ closure s) :
  (∃l:list α, (∀x∈l, x ∈ s ∨ -x ∈ s) ∧ l.sum = a) :=
group.exists_list_of_mem_closure h
```

#### [Patrick Massot (Oct 09 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135498664):
this is even more confusing

#### [Patrick Massot (Oct 09 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135498756):
I thought you would be using your custom recursor

#### [Kenny Lau (Oct 09 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135498770):
me too

#### [Kenny Lau (Oct 09 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135498777):
and halfway I realized

#### [Patrick Massot (Oct 09 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135498839):
Do you understand what's going on with this way of turning multiplicative stuff into additive one?

#### [Kenny Lau (Oct 09 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135498846):
somewhat.

#### [Patrick Massot (Oct 09 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135500038):
What about the `exists_lists_of_mem_closure` in the ring case?

#### [Patrick Massot (Oct 09 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135500057):
something like
```lean
theorem exists_list_of_mem_closure {s : set R} {a : R} (h : a ∈ closure s) :
  (∃ L : list (list R), (∀ l ∈ L, ∀ x ∈ l, x ∈ s ∨ -x ∈ s) ∧ (list.map list.prod L).sum = a) 
```

#### [Patrick Massot (Oct 09 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135500098):
I guess I would try to use the previous theorems but you'll run crazy inductions...

#### [Kenny Lau (Oct 09 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135500174):
why do we need `list (list R)`?

#### [Kenny Lau (Oct 09 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135500189):
ah I see

#### [Kenny Lau (Oct 09 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135500217):
maybe we should prove the recursor for comm_ring.closure first

#### [Patrick Massot (Oct 09 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135500248):
of course the maths proof is not at all by induction

#### [Patrick Massot (Oct 09 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135500297):
but in Lean it would probably be easier by induction

#### [Kenny Lau (Oct 09 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135500313):
oh how do you prove it in maths?

#### [Patrick Massot (Oct 09 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135500454):
The maths proof starts with `  rcases add_group.exists_list_of_mem_closure h with ⟨L1, hL1, L1sum⟩,`

#### [Patrick Massot (Oct 09 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135500482):
Then you need to apply `monoid.exists_list_of_mem_closure` everywhere you see monoid.closure in hL1

#### [Patrick Massot (Oct 09 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135500500):
of course it's already beyond my Lean fu, because of the binder

#### [Patrick Massot (Oct 09 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135500566):
and this get you get your list of lists

#### [Patrick Massot (Oct 09 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135500573):
except for the substractions

#### [Patrick Massot (Oct 09 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135500579):
I guess my statement is wrong

#### [Patrick Massot (Oct 09 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135500610):
no, it's ok

#### [Reid Barton (Oct 09 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135500677):
I think it is wrong, because of -1. `s` could even be empty.

#### [Patrick Massot (Oct 09 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135500702):
edge cases...

#### [Patrick Massot (Oct 09 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135500707):
who cares about those?

#### [Patrick Massot (Oct 09 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135500809):
I clearly need to sleep though. I'm sure the `Kenny` tactic can fix the statement while writing the proof

#### [Kenny Lau (Oct 09 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135500845):
of what?

#### [Patrick Massot (Oct 09 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/135501115):
`ring.exists_list_of_mem_closure`

#### [Kenny Lau (Oct 26 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/136534435):
```lean
import ring_theory.subring

universe u

@[elab_as_eliminator]
theorem add_monoid.in_closure.rec_on {α : Type u} [add_monoid α] {s : set α} {C : α → Prop}
  {a : α} (H : a ∈ add_monoid.closure s)
  (H1 : ∀ {a : α}, a ∈ s → C a) (H2 : C 0)
  (H3 : ∀ {a b : α}, a ∈ add_monoid.closure s → b ∈ add_monoid.closure s → C a → C b → C (a + b)) :
  C a :=
monoid.in_closure.rec_on H (λ _, H1) H2 (λ _ _, H3)

@[elab_as_eliminator]
theorem add_group.in_closure.rec_on {α : Type u} [add_group α] {s : set α} {C : α → Prop}
  {a : α} (H : a ∈ add_group.closure s)
  (H1 : ∀ {a : α}, a ∈ s → C a) (H2 : C 0) (H3 : ∀ {a : α}, a ∈ add_group.closure s → C a → C (-a))
  (H4 : ∀ {a b : α}, a ∈ add_group.closure s → b ∈ add_group.closure s → C a → C b → C (a + b)) :
  C a :=
group.in_closure.rec_on H (λ _, H1) H2 (λ _, H3) (λ _ _, H4)

instance int.cast_hom {R : Type u} [comm_ring R] : is_ring_hom (int.cast : ℤ → R) :=
⟨int.cast_one, int.cast_mul, int.cast_add⟩

instance int.coe_hom {R : Type u} [comm_ring R] : is_ring_hom (coe : ℤ → R) :=
⟨int.cast_one, int.cast_mul, int.cast_add⟩

namespace comm_ring
variables {R : Type u} [comm_ring R]

def closure (s : set R) := add_group.closure (monoid.closure s)

local attribute [reducible] closure

theorem exists_list_of_mem_closure {s : set R} {a : R} (h : a ∈ closure s) :
  (∃ L : list (list R), (∀ l ∈ L, ∀ x ∈ l, x ∈ s ∨ -x ∈ s ∨ x = (-1:R)) ∧ (L.map list.prod).sum = a) :=
add_group.in_closure.rec_on h
  (λ x hx, match x, monoid.exists_list_of_mem_closure hx with
    | _, ⟨L, h1, rfl⟩ := ⟨[L], list.forall_mem_singleton.2 (λ r hr, or.inl (h1 r hr)), zero_add _⟩
    end)
  ⟨[], list.forall_mem_nil _, rfl⟩
  (λ b _ ih, match b, ih with
    | _, ⟨L1, h1, rfl⟩ := ⟨L1.map (list.cons (-1)),
      λ L2 h2, match L2, list.mem_map.1 h2 with
        | _, ⟨L3, h3, rfl⟩ := list.forall_mem_cons.2 ⟨or.inr $ or.inr rfl, h1 L3 h3⟩
        end,
      by simp only [list.map_map, (∘), list.prod_cons, neg_one_mul];
      exact list.rec_on L1 neg_zero.symm (λ hd tl ih,
        by rw [list.map_cons, list.sum_cons, ih, list.map_cons, list.sum_cons, neg_add])⟩
    end)
  (λ r1 r2 hr1 hr2 ih1 ih2, match r1, r2, ih1, ih2 with
    | _, _, ⟨L1, h1, rfl⟩, ⟨L2, h2, rfl⟩ := ⟨L1 ++ L2, list.forall_mem_append.2 ⟨h1, h2⟩,
      by rw [list.map_append, list.sum_append]⟩
    end)

instance {s : set R} : is_subring (closure s) :=
{ zero_mem := is_add_submonoid.zero_mem _,
  add_mem := λ a b ha hb, is_add_submonoid.add_mem ha hb,
  neg_mem := λ a h, is_add_subgroup.neg_mem h,
  one_mem := add_group.mem_closure (is_submonoid.one_mem _),
  mul_mem := λ a b ha hb, add_group.in_closure.rec_on hb
    (λ b hb, add_group.in_closure.rec_on ha
      (λ a ha, add_group.subset_closure (is_submonoid.mul_mem ha hb))
      ((zero_mul b).symm ▸ is_add_submonoid.zero_mem _)
      (λ a ha hab, (neg_mul_eq_neg_mul a b) ▸ is_add_subgroup.neg_mem hab)
      (λ a c ha hc hab hcb, (add_mul a c b).symm ▸ is_add_submonoid.add_mem hab hcb))
    ((mul_zero a).symm ▸ is_add_submonoid.zero_mem _)
    (λ b hb hab, (neg_mul_eq_mul_neg a b) ▸ is_add_subgroup.neg_mem hab)
    (λ b c hb hc hab hac, (mul_add a b c).symm ▸ is_add_submonoid.add_mem hab hac) }

end comm_ring
```

#### [Kenny Lau (Oct 26 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/136534452):
@**Patrick Massot** will you PR this?

#### [Patrick Massot (Oct 26 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/136534702):
I can do it if you don't want to do it

#### [Patrick Massot (Oct 26 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/136534707):
But it would make more sense if you do it yourself

#### [Patrick Massot (Oct 26 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/136534710):
otherwise git won't credit you

#### [Kenny Lau (Oct 26 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/136534715):
where should I put it?

#### [Patrick Massot (Oct 26 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/136534762):
Maybe in the subgroup and subring files?

#### [Kenny Lau (Oct 26 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/136534767):
maybe it'll just go to limbo like https://github.com/leanprover/mathlib/pull/425

#### [Patrick Massot (Oct 26 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/136534791):
This is much smaller scope

#### [Patrick Massot (Oct 26 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/136534800):
It should be an easy merge

#### [Kenny Lau (Oct 28 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/136646441):
https://github.com/leanprover/mathlib/pull/444

#### [Kenny Lau (Oct 28 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/comm_ring.closure/near/136646444):
done @**Patrick Massot**

