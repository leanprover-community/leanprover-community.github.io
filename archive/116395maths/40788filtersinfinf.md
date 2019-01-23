---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/40788filtersinfinf.html
---

## Stream: [maths](index.html)
### Topic: [filters inf inf](40788filtersinfinf.html)

---

#### [Patrick Massot (Jun 16 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128166284):
@**Johannes Hölzl** I have difficulties setting up my uniform space structure on topological groups. Basically the trouble is the definition involves dependent nested infimum. I tried to mimick the metric space case where you wrote:
```lean
uniformity := (⨅ ε>0, principal {p:α×α | dist p.1 p.2 < ε}),
```
(nested inf is somewhat hidden but still there). Question 1: would it be a good idea to rather use the subtype of positive real number as the indexing set?

#### [Patrick Massot (Jun 16 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128166325):
So, in the context of a topological add group R, I wrote, with obvious notations:
```lean
uniformity  := ⨅ U ∈ nhd_zero R, principal {p : R×R | p.2 - p.1 ∈ U}
```

#### [Patrick Massot (Jun 16 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128166331):
But again this is somewhat inconvenient to use.

#### [Patrick Massot (Jun 16 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128166332):
I have the following lemma, which is a restatement of something already there:

#### [Patrick Massot (Jun 16 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128166335):
```lean
lemma filter.mem_sets_of_mem_infi {α : Type*} {ι : Sort*} {f : ι → filter α} {A : set α} 
  (h : directed (≤) f) (ne : nonempty ι) : A ∈ (⨅ i,f i).sets → ∃ i, A ∈ (f i).sets := 
begin
  intro H,  
  finish [infi_sets_eq]
end
```

#### [Patrick Massot (Jun 16 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128166375):
but already I'd like to deduced `ne` from existence of `A`

#### [Patrick Massot (Jun 16 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128166385):
And then I need a version for dependent nested inf that, I think, would be something like:
```lean
lemma filter.mem_sets_of_mem_infi' {α : Type*} {ι : Sort*} {P : ι → Prop} {f : Π i, P i → filter α} {A : set α} 
  (H : A ∈ (⨅ i, ⨅ h : P i, f i h).sets) : ∃ i, ∃ h : P i, A ∈ (f i h).sets := 
```
but with some directedness assumption somewhere

#### [Patrick Massot (Jun 16 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128166424):
Any help would be appreciated

#### [Chris Hughes (Jun 16 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128168185):
I tried to prove it, but then realised it wasn't true.
```lean
import data.analysis.filter
open set list filter lattice

lemma filter.mem_sets_of_mem_infi' {α : Type*} {ι : Sort*} {P : ι → Prop} {f : Π i, P i → filter α} {A : set α}
  (H : A ∈ (⨅ i, ⨅ h : P i, f i h).sets) : ∃ i, ∃ h : P i, A ∈ (f i h).sets := sorry

lemma proof_of_false : false :=
let ⟨x, hx⟩ := @filter.mem_sets_of_mem_infi' ℕ empty empty.elim (λ i, i.elim) set.univ (by simp) in
x.elim
```

#### [Chris Hughes (Jun 16 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128168190):
Not sure how helpful that is.

#### [Chris Hughes (Jun 16 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128168559):
Probably need `A ≠ univ`, because `univ` is in every filter, but you might as well just have `nonempty ι`, which is implied by `A ≠ univ`,

#### [Reid Barton (Jun 16 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128168701):
```quote
but already I'd like to deduced `ne` from existence of `A`
```
You should be deducing `ne` from the fact that `f` is directed, but I guess mathlib's definition leaves out that condition, oops.

#### [Reid Barton (Jun 16 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128169091):
Apparently not assuming that a directed set is nonempty is a Bourbaki thing.

#### [Reid Barton (Jun 16 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128169188):
@**Patrick Massot** There is
```lean
lemma infi_sets_eq' {f : β → filter α} {s : set β} (h : directed_on (λx y, f x ≤ f y) s) (ne : ∃i, i ∈ s) :
  (⨅ i∈s, f i).sets = (⋃ i ∈ s, (f i).sets)
```

#### [Johannes Hölzl (Jun 16 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128172055):
Hm, I think you don't need the infimum at all, it should be possible to use `vmap` and `nhds_zero`:
`uniformity := vmap (fun p, p.1 - p.2) (nhds_zero R)`

#### [Patrick Massot (Jun 16 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128178252):
Oh. That's a completely different start

#### [Patrick Massot (Jun 16 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128178253):
But maybe it's more natural

#### [Patrick Massot (Jun 16 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128178255):
It means I need to learn a completely new set of lemmas

#### [Patrick Massot (Jun 16 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128179700):
It's worse than my original method

#### [Patrick Massot (Jun 16 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128179701):
I can't prove any single property

#### [Mario Carneiro (Jun 16 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128179709):
like what?

#### [Patrick Massot (Jun 16 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128180101):
like `principal id_rel ≤ vmap (λ (p : R × R), p.fst - p.snd) (nhds 0)`

#### [Patrick Massot (Jun 16 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128180103):
and `tendsto prod.swap (vmap (λ (p : R × R), p.fst - p.snd) (nhds 0)) (vmap (λ (p : R × R), p.fst - p.snd) (nhds 0))`

#### [Patrick Massot (Jun 16 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128180142):
`filter.lift' (vmap (λ (p : R × R), p.fst - p.snd) (nhds 0)) (λ (s : set (R × R)), comp_rel s s) ≤  vmap (λ (p : R × R), p.fst - p.snd) (nhds 0)`

#### [Mario Carneiro (Jun 16 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128180145):
I assume you know `nhds_zero = nhds 0`?

#### [Patrick Massot (Jun 16 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128180146):
and `∀ (s : set R),    topological_space.is_open _inst_2 s ↔  ∀ (x : R),   x ∈ s → {p : R × R | p.fst = x → p.snd ∈ s} ∈ (vmap (λ (p : R × R), p.fst - p.snd) (nhds 0)).sets`

#### [Patrick Massot (Jun 16 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128180152):
Johannes suggestion doesn't use `nhds_zero` (which I defined earlier by `def nhd_zero := (nhds (0 : R)).sets`)

#### [Mario Carneiro (Jun 16 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128180192):
What do you mean? I see `nhds_zero` in his post

#### [Patrick Massot (Jun 16 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128180195):
this is based on him incorrectly guessing my definition

#### [Mario Carneiro (Jun 16 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128180202):
For the first one, you have `tendsto_iff_vmap`

#### [Patrick Massot (Jun 16 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128180203):
he probably thought I had `def nhd_zero := nhds (0 : R)`

#### [Mario Carneiro (Jun 16 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128180204):
Well, `nhds_zero` has a special place in the theory of top groups

#### [Patrick Massot (Jun 16 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128180205):
Indeed the first thing I wrote is `rw tendsto_vmap_iff`

#### [Patrick Massot (Jun 16 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128180245):
I also tried `rw tendsto_iff_vmap,`

#### [Patrick Massot (Jun 16 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128180254):
but then I'm stuck

#### [Mario Carneiro (Jun 16 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128180256):
then use that `-` is continuous

#### [Mario Carneiro (Jun 16 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128180258):
`continuous.tendsto`

#### [Patrick Massot (Jun 16 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128180449):
I'd love to continue this discussion but I must leave at 6:30 tomorrow morning to get a plane to go to a conference in Cagliari

#### [Patrick Massot (Jun 16 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128180450):
so I should sleep

#### [Patrick Massot (Jun 16 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128180451):
thank you very much for these hints

#### [Johannes Hölzl (Jun 17 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128206302):
I guessed `nhds_zero` from your equation `uniformity  := ⨅ U ∈ nhd_zero R, principal {p : R×R | p.2 - p.1 ∈ U}`.
(by the way: why is it okay to call the support type of a group `R` but not alpha?)

There are two important rules to convert between `map` and `vmap`: `map_le_iff_le_vmap`, and `map_eq_vmap_of_inverse`.

To prove the first rule use the rule  `map_le_iff_le_vmap` to move the`-` to the left side, then using rewriting to end up with `principal {a | a = 0} = pure 0 <= nhds 0`.

The second rule (using prod.swap): use `map_le_iff_le_vmap`, and then `map_comp` the left side by `(fun x, - x) o (fun p, p.1 - p.2)` Then use `tendsto_vmap` (together with `tendsto_comp`).

And for the last one I guess we want to  use `vmap_eq_lift'` (which essentially proofs that your and my definition are the equal)

#### [Johannes Hölzl (Jun 17 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128214709):
https://gist.github.com/johoelzl/ca90562c46b49a1bbb1be36272ec3b1a
transitivity, i.e. the `uniform_space.comp` rule, is a little bit harder to show

#### [Johannes Hölzl (Jun 17 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128214772):
Would you suggest any changes to this? if not I will just add this to mathlib

