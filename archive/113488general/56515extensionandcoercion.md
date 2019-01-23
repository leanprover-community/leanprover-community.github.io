---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/56515extensionandcoercion.html
---

## Stream: [general](index.html)
### Topic: [extension and coercion](56515extensionandcoercion.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 13 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extension%20and%20coercion/near/123660814):
A long time ago, I wrote:
```lean
structure homeo (α β) [topological_space α] [topological_space β] extends equiv α β :=
(fun_con : continuous to_fun)
(inv_con : continuous inv_fun)

instance : has_coe_to_fun (homeo α β) := ⟨_, λ f, f.to_fun⟩
```
But now it seems I have trouble, probably because a homeo f and f.to_equiv don't have defeq coercion to function. I'm especially interested in direct images of subsets under homeomorphisms. For instance, I'd like to prove `(f : homeo X X) (s : set X) : f '' closure s = closure (f '' s)`, using `image_closure_subset_closure_image` from mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 13 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extension%20and%20coercion/near/123660819):
How should I setup this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Mar 13 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extension%20and%20coercion/near/123661281):
this works for me
```lean
example (h : homeo α β) : (h : α → β) = h.to_equiv := rfl
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 13 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extension%20and%20coercion/near/123661897):
hum. Maybe the problem is something else. Do you manage to prove my closure lemma using this coercion? In principle this a trivial lemma once you have `image_closure_subset_closure_image` (to be applied to both f and its inverse)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Mar 13 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extension%20and%20coercion/near/123662202):
My solution looks like this now: 

```lean
import analysis.topology.continuity data.equiv
open set
variables {α : Type*} {β : Type*} [topological_space α] [topological_space β]
structure homeo (α β) [topological_space α] [topological_space β] extends equiv α β :=
(fun_con : continuous to_fun)
(inv_con : continuous inv_fun)
instance : has_coe_to_fun (homeo α β) := ⟨_, λ f, f.to_fun⟩
lemma homeo_coe_to_equiv_coe (h : homeo α β) : (h : α → β) = h.to_equiv := rfl
lemma equiv.image_eq_preimage {α β} (e : α ≃ β) (s : set α) : e '' s = e.symm ⁻¹' s := ext $ assume x, mem_image_iff_of_inverse e.left_inv e.right_inv

example (f : homeo α α) (s : set α) : f '' closure s = closure (f '' s) :=
subset.antisymm
  (image_closure_subset_closure_image f.fun_con)
  begin
    rw [homeo_coe_to_equiv_coe, f.to_equiv.image_eq_preimage (closure s), ← image_subset_iff],
    refine subset.trans (image_closure_subset_closure_image f.inv_con) _,
    simp [(image_comp _ _ _).symm, f.to_equiv.inverse_apply_apply],
    show closure (id '' s) ⊆ closure s, by rw [image_id]; exact subset.refl _
  end
```

One problem is that `rw` and the simplifier can now see through the coercion. So when you want to apply `equiv` lemmas you need to apply `homeo_coe_to_equiv_coe` first. Another solution is to make a `calc` proof, which might be a little bit nicer and one has the opportunity to state the goal in the required form.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 13 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extension%20and%20coercion/near/123662495):
Thanks you very much. I feared needing to invoke something like ` homeo_coe_to_equiv_coe` but it doesn't seem so bad in the end, especially if a calc proof works (I'll try).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 13 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extension%20and%20coercion/near/123662522):
I see this is also a good opportunity for my poor man tactic (as Kevin would put it):
```lean
meta def by_double_inclusion : tactic unit := do
`[apply set.subset.antisymm_iff.2, split]
```
Obviously it's a bit ridiculous but the main point is readablity

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Mar 13 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extension%20and%20coercion/near/123662958):
If you add some infrastructure for `homeo` it gets also nicer:
```lean
import analysis.topology.continuity data.equiv
open set

variables {α : Type*} {β : Type*} [topological_space α] [topological_space β]

structure homeo (α β) [topological_space α] [topological_space β] extends equiv α β :=
(fun_con : continuous to_fun)
(inv_con : continuous inv_fun)

instance : has_coe_to_fun (homeo α β) := ⟨_, λ f, f.to_fun⟩

def homeo.id (α) [topological_space α] : homeo α α :=
{ fun_con := continuous_id, inv_con := continuous_id, .. equiv.refl α }

lemma home.id_apply : (homeo.id α : α → α) = id := rfl

def homeo.symm (h : homeo α β) : homeo β α :=
{ fun_con := h.inv_con, inv_con := h.fun_con, .. h.to_equiv.symm }

lemma homeo.symm_comp (h : homeo α β) : (h.symm) ∘ h = homeo.id α :=
funext h.left_inv

lemma homeo_coe_to_equiv_coe (h : homeo α β) : (h : α → β) = h.to_equiv := rfl

lemma equiv.image_eq_preimage {α β} (e : α ≃ β) (s : set α) : e '' s = e.symm ⁻¹' s :=
ext $ assume x, mem_image_iff_of_inverse e.left_inv e.right_inv

lemma equiv.subset_image {α β} (e : α ≃ β) (s : set α) (t : set β) : t ⊆ e '' s ↔ e.symm '' t ⊆ s :=
by rw [image_subset_iff, e.image_eq_preimage]

example (f : homeo α β) (s : set α) : f '' closure s = closure (f '' s) :=
subset.antisymm
  (image_closure_subset_closure_image f.fun_con)
  ((f.to_equiv.subset_image _ _).2 $
    calc f.symm '' closure (f '' s) ⊆ closure (f.symm '' (f '' s)) :
        image_closure_subset_closure_image f.inv_con
      ... = closure s :
        by rw [← image_comp, f.symm_comp, home.id_apply, image_id])
```

I don't see the value in `by_double_inclusion`. You could just use `apply subset.antisymm`. I would prefer if people wrote term style proofs.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 14 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/extension%20and%20coercion/near/123695171):
Thank you very much @**Johannes Hölzl** I'm sorry my Lean time is very fragmented those days, so I suddenly stopped answering. I already had some infrastructure but it is only partially compatible with what you wrote. I'll need time to make the whole story consistent, including probably some more lemmas assuming only injectivity or surjectivity.


{% endraw %}
