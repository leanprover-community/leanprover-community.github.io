---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/22601calciff.html
---

## Stream: [general](index.html)
### Topic: [calc iff](22601calciff.html)

---

#### [Patrick Massot (Dec 20 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20iff/near/152244122):
Is there anything we can do to get something like
```lean
example (p q r s : Prop) (h : p ↔ q) (h' : q → r) (h'' : r ↔ s) : p → s :=
λ hp, (calc p ↔ q : h
... → r : h'
... ↔ s : h'') hp
```
to work?

#### [Patrick Massot (Dec 20 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20iff/near/152244233):
I'm trying to please Johannes who doesn't like
```lean
example (p q r s : Prop) (h : p ↔ q) (h' : q → r) (h'' : r ↔ s) : p → s :=
begin
  rw h,
  rwa h'' at h',
end
```
which I admit is less transparent...

#### [Johan Commelin (Dec 20 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20iff/near/152244390):
If only `Prop` were a category... then you could write
```lean
example (p q r s : Prop) (h : p ↔ q) (h' : q → r) (h'' : r ↔ s) : p → s :=
h.mp ≫ h' ≫ h''.mp
```

#### [Patrick Massot (Dec 20 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20iff/near/152244479):
Maybe I should say that the actual proof would rather look like
```lean
example (p q r s : Prop) (h : ...) (h' : ...) (h'' : ...) : p → s :=
λ hp, (calc p ↔ q : by rw h
... → r : by h'
... ↔ s : by rw h'') hp
```

#### [Mario Carneiro (Dec 20 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20iff/near/152245121):
unfortunately no. Here's the best we can do:
```lean
abbreviation imp (p q : Prop) := p → q
infixr `→→`:25 := imp
@[trans] theorem imp_of_iff_of_imp {p q r : Prop}
  (h₁ : p ↔ q) (h₂ : q →→ r) : p →→ r := h₂ ∘ h₁.1

@[trans] theorem iff_of_imp_of_imp {p q r : Prop}
  (h₁ : p →→ q) (h₂ : q ↔ r) : p →→ r := h₂.1 ∘ h₁

example (p q r s : Prop) (h : p ↔ q) (h' : q → r) (h'' : r ↔ s) : p → s :=
λ hp, (calc p ↔ q : h
... →→ r : h'
... ↔ s : h'') hp
```

#### [Mario Carneiro (Dec 20 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20iff/near/152245150):
If you replace `→→` with `→` the trans lemmas are rejected

#### [Mario Carneiro (Dec 20 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20iff/near/152245167):
because `→` is a bit magic for a binary operator

#### [Patrick Massot (Dec 20 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20iff/near/152245218):
This magic obstruction is what I suspected when I tried to define those trans lemmas

#### [Patrick Massot (Dec 20 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20iff/near/152245238):
Here is the best I could do in order to rewrite my continuity proof so that it looks like what I see on paper:
```lean
lemma uniform_continuous.continuous [uniform_space β] {f : α → β}
  (hf : uniform_continuous f) : continuous f :=
let ff := (λ p : α×α, (f p.1, f p.2)) in
continuous_iff_tendsto.mpr $ λ a,
have key : prod.mk (f a) ∘ f = ff ∘ prod.mk a, by ext x ; simp,
have map ff uniformity ≤ uniformity, from hf,
have uniformity ≤ comap ff uniformity, from map_le_iff_le_comap.1 this,
have comap (prod.mk a) (@uniformity α _) ≤ (comap (prod.mk a) (comap ff uniformity)), from comap_mono this,
have nhds a ≤ comap (ff ∘ prod.mk a) uniformity, by rwa [comap_comap_comp, ←nhds_eq_comap_uniformity] at this,
have nhds a ≤ comap (prod.mk (f a) ∘ f) uniformity, by rwa key at this,
have nhds a ≤ comap f (comap (prod.mk (f a)) uniformity), by rwa ←comap_comap_comp at this,
have nhds a ≤ comap f (nhds (f a)), by rwa ←nhds_eq_comap_uniformity at this,
tendsto_iff_comap.2 this
```

#### [Patrick Massot (Dec 20 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20iff/near/152245338):
How do you like that style?

#### [Kenny Lau (Dec 20 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20iff/near/152245645):
too long

#### [Patrick Massot (Dec 20 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20iff/near/152245876):
Variation:
```lean
lemma uniform_continuous.continuous [uniform_space β] {f : α → β}
  (hf : uniform_continuous f) : continuous f :=
let ff := (λ p : α×α, (f p.1, f p.2)) in
continuous_iff_tendsto.mpr $ λ a,
have key : prod.mk (f a) ∘ f = ff ∘ prod.mk a, by ext x ; simp,
have map ff uniformity ≤ uniformity, from hf,
have uniformity ≤ comap ff uniformity, from map_le_iff_le_comap.1 this,
have comap (prod.mk a) (@uniformity α _) ≤ (comap (prod.mk a) (comap ff uniformity)), from comap_mono this,
let this := calc
nhds a ≤ comap (ff ∘ prod.mk a) uniformity : by rwa [comap_comap_comp, ←nhds_eq_comap_uniformity] at this
   ... ≤ comap (prod.mk (f a) ∘ f) uniformity : by simp[key, le_refl]
   ... ≤ comap f (comap (prod.mk (f a)) uniformity) : by rw ←comap_comap_comp ; exact le_refl _
   ... ≤ comap f (nhds (f a)) : by rw ←nhds_eq_comap_uniformity ; exact le_refl _  in
tendsto_iff_comap.2 this
```

#### [Patrick Massot (Dec 20 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20iff/near/152245892):
It's really a pain that `le_refl` isn't inserted automatically

#### [Kenny Lau (Dec 20 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20iff/near/152245999):
what's wrong with the current proof?

#### [Sebastien Gouezel (Dec 20 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20iff/near/152246297):
I have added `le_refl` to the simp set in my mathlib. I will probably PR it one day, together with a lot of other stuff (but cut into atomic pieces, if this is the way we should do PRs), once (or if?) my two topology PRs are merged.

#### [Patrick Massot (Dec 20 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20iff/near/152246363):
Kenny, the current proof is inelegant. Remember that only Lean thinks proofs are irrelevant

#### [Kenny Lau (Dec 20 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20iff/near/152246384):
eh, I also think they're irrelevant

#### [Johan Commelin (Dec 20 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20iff/near/152246517):
@**Kevin Buzzard** You've created little monsters :scream:. Clearly they need to be brought up in the ways of the old masters, who value the esthetics of a good proof, and whose proofs illuminate and inspire understanding.

#### [Kevin Buzzard (Dec 20 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20iff/near/152247283):
Kids these days

#### [Scott Morrison (Dec 20 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20iff/near/152247312):
... uphill both ways.

#### [Johan Commelin (Dec 20 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20iff/near/152248786):
```quote
I will probably PR it one day, ... once (or if?) my two topology PRs are merged.
```
 O.o... that doesn't sound good.

#### [Kenny Lau (Dec 20 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20iff/near/152248926):
looks like he will PR it after Lean 4 has been released

#### [Sebastien Gouezel (Dec 20 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20iff/near/152249007):
It's just that all my constructions build on these two PRs, so there is no way I can PR anything before those two are merged. But this does not prevent me of working steadily on my own branch, I have almost proved now that the Gromov-Hausdorff distance is a distance, which involves a lot of material (several thousands of line, I would say :)

#### [Mario Carneiro (Dec 20 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calc%20iff/near/152249801):
yeah okay. I've been putting it off because it's a big PR and I had to check it out and fiddle with stuff, but I will work on that now

