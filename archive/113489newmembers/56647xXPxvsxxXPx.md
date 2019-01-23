---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/56647xXPxvsxxXPx.html
---

## Stream: [new members](index.html)
### Topic: [∃ x ∈ X, P x vs. ∃ x, x ∈  X ∧ P x](56647xXPxvsxxXPx.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Sep 22 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%E2%88%83%20x%20%E2%88%88%20X%2C%20P%20x%20vs.%20%E2%88%83%20x%2C%20x%20%E2%88%88%20%20X%20%E2%88%A7%20P%20x/near/134438550):
Up to now I've been using `∃ x ∈ X, P x` in theorem statements (or also e.g. `∃ X ⊆  Y, Q X`) (where X : finset a and a has decidable_eq) without really thinking about it. First of all, they look like what I'm used to, and second of all, I've been able to get things to work with them up to now. In lean, they translate to `∃ x, ∃ (h : x ∈ X), P x` and `∃ X, ∃ (H : X ⊆ Y), Q X`, and I've just been mindlessly using extra layers of `exists.elim` / `exists.intro` to deal with the `h`'s and `H`'s in proofs.

Recently I've been defining new functions from these existence theorems using `encodable.choose` and then defining other functions using `encodable.choose_spec`to prove things about them. While contemplating the prospect of unwrapping these extra "exists" again, I've come to the realization that maybe it's just much cleaner to use `∃ x, x ∈ X ∧ P x` everywhere instead. This turns out to break decidability, but I think I've managed to get that sorted by adding an extra instance.

Anyways, I just wanted to see whether my conclusion (avoid `∃ x ∈ X, P x` in favor of `∃ x, x ∈ X ∧ P x`) makes sense and whether there are other related pitfalls I should be wary of.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 22 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%E2%88%83%20x%20%E2%88%88%20X%2C%20P%20x%20vs.%20%E2%88%83%20x%2C%20x%20%E2%88%88%20%20X%20%E2%88%A7%20P%20x/near/134439149):
(deleted)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 22 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%E2%88%83%20x%20%E2%88%88%20X%2C%20P%20x%20vs.%20%E2%88%83%20x%2C%20x%20%E2%88%88%20%20X%20%E2%88%A7%20P%20x/near/134439203):
`∃ x ∈ X, P x` is a pretty well-established idiom. I'm not that familiar with `encodable` but I think I would be more inclined to make whatever worked with `x ∈ X ∧ P x` also work with the nested exists. After all, `∃ h : P, Q` (with `Q` not mentioning `h`) is isomorphic to `P ∧ Q` anyways.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Sep 22 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%E2%88%83%20x%20%E2%88%88%20X%2C%20P%20x%20vs.%20%E2%88%83%20x%2C%20x%20%E2%88%88%20%20X%20%E2%88%A7%20P%20x/near/134440789):
It is indeed possible to make things work both ways, but I'm still thinking the second way is will be easier in the long run. Here's a toy example showing the flavor of how I've been using `encodable.choose_spec`:
```lean
import data.finset data.equiv.encodable

variables {α : Type*} [decidable_eq α] {E F G : finset α} [encodable α]

open finset encodable

-- implicit nested exists
theorem foo (h : F ∩ G ≠ ∅) : ∃ e ∈ F, e ∈ G :=
exists.elim (exists_mem_of_ne_empty h) $
  λ a ha, ⟨a, (mem_inter.mp ha).1, (mem_inter.mp ha).2⟩

def foo_e (h : F ∩ G ≠ ∅) : α :=
choose $ foo h

-- have to unwrap the extra exists in foo here and elsewhere
def foo_e_spec (h : F ∩ G ≠ ∅) : foo_e h ∈ F ∧ foo_e h ∈ G :=
exists.elim (choose_spec $ foo h) (λ a ha, ⟨a, ha⟩)

-- only one exists
theorem bar (h : F ∩ G ≠ ∅) : ∃ e, e ∈ F ∧ e ∈ G :=
exists.elim (exists_mem_of_ne_empty h) $
  λ a ha, ⟨a, mem_inter.mp ha⟩

def bar_e (h : F ∩ G ≠ ∅) : α :=
choose $ bar h

def bar_e_spec (h : F ∩ G ≠ ∅) : bar_e h ∈ F ∧ bar_e h ∈ G :=
choose_spec $ bar h
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 22 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%E2%88%83%20x%20%E2%88%88%20X%2C%20P%20x%20vs.%20%E2%88%83%20x%2C%20x%20%E2%88%88%20%20X%20%E2%88%A7%20P%20x/near/134442413):
Be sure to read the discussion in https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/undead about nested exist

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Sep 22 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%E2%88%83%20x%20%E2%88%88%20X%2C%20P%20x%20vs.%20%E2%88%83%20x%2C%20x%20%E2%88%88%20%20X%20%E2%88%A7%20P%20x/near/134442546):
Yeah, I think I tried to use `∃! x∈ X` once and immediately ran into the issue described there.

