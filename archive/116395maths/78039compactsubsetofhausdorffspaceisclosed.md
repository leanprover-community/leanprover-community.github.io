---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/78039compactsubsetofhausdorffspaceisclosed.html
---

## Stream: [maths](index.html)
### Topic: [compact subset of hausdorff space is closed](78039compactsubsetofhausdorffspaceisclosed.html)

---

#### [Edward Ayers (Aug 14 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132127153):
Hi everyone. I would really appreciate any comments on how to improve this proof. Also, is this result in the library?
```lean
import .topological_space
open set filter lattice

universes u v
variables {α : Type u} [ topological_space α]

def inclusion (s : set α) : s -> α := λ a, a
def subspace_top (s : set α) := topological_space.induced (inclusion s)

lemma not_bot_left (f g : filter α) (H1 : f ⊓ g ≠ ⊥) : f ≠ ⊥ := begin
    apply neq_bot_of_le_neq_bot,
    apply H1,
    exact inf_le_left
end

lemma compact_subset_of_t2space_is_closed 
    [t2_space α] (Y : set α) (sc : compact Y) : (is_closed Y) := begin
    cases is_closed_iff_nhds, clear mp,
    apply mpr, clear mpr, intros, rename a y,
    let f := (nhds y ⊓ principal Y),
    have H3 : (∃ a (H : a ∈ Y), f ⊓ nhds a ≠ ⊥), from sc f a_1 inf_le_right,
    apply exists.elim H3,
    intros, apply exists.elim a_2, intros,
    have H5 : nhds a ⊓ nhds y ≠ ⊥,
        rewrite inf_assoc at a_4, -- if I do inf_assoc first it fails?!
        rewrite inf_comm at a_4,
        rewrite inf_assoc at a_4,
        rewrite inf_comm at a_4,
        apply not_bot_left, assumption,
    have H4:  a = y, from eq_of_nhds_neq_bot H5,
    rewrite H4 at a_3,
    assumption
    end
```

#### [Edward Ayers (Aug 14 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132129134):
Version 2:
```lean
lemma compact_subset_of_t2space_is_closed_2
    [t2_space α] (Y : set α) (sc : compact Y) : (is_closed Y) := 
    iff.elim_right is_closed_iff_nhds (λ y H1,
        let f := (nhds y ⊓ principal Y) in
        exists.elim (sc f H1 inf_le_right) (λ a H2, exists.elim H2 
        (
            assume H3 H4,
            suffices y = a, from by rw this; assumption,
            suffices nhds y ⊓ nhds a ⊓ principal Y ≠ ⊥, from eq_of_nhds_neq_bot $ not_bot_left _ _ this,
            by cc
        )
    )
)
```

#### [Edward Ayers (Aug 14 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132133848):
Found it in library: `closed_of_compact`

#### [Edward Ayers (Aug 14 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132133886):
Although I proved it with filters

#### [Kevin Buzzard (Aug 14 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132134882):
First line of proof could be `is_closed_iff_nhds.2 (λ y H1,` (`iff` is a structure and you can access its elements with `.1`, `.2`). There's a mathlib style guide and you're not conforming to it (I don't think they like the one-bracket-on-a-line thing, and I know they like 2 spaces indent rather than 4).  `by rw this; assumption,` could be `by rwa this` (`rwa` = `rw ; assumption`, similarly `simpa`).

#### [Kevin Buzzard (Aug 14 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132134906):
but it's certainly a darn sight better than I could have done :-)

#### [Patrick Massot (Aug 14 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132134941):
`simpa` is more than `simp ... ; assumption`, see https://github.com/leanprover/mathlib/blob/master/docs/tactics.md#simpa

#### [Kevin Buzzard (Aug 14 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132135482):
Instead of `λ a H2, exists.elim H2 ...` I wonder if you could have done `λ a ⟨H,H2⟩,` and then you can maybe avoid the `exists.elim`

#### [Patrick Massot (Aug 14 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132135502):
Everybody dreams that could be possible, but no.

#### [Kevin Buzzard (Aug 14 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132135570):
```lean
(λ a ⟨H3,H4⟩,
        (
            suffices y = a, from by rwa this,
```
;-)

#### [Patrick Massot (Aug 14 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132135580):
Latest discussion is probably https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eta.20for.20structures

#### [Kevin Buzzard (Aug 14 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132135586):
I got lucky because he assumes `H3` and `H4`

#### [Edward Ayers (Aug 14 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132135629):
```quote
There's a mathlib style guide 
```
I should read that.

#### [Patrick Massot (Aug 14 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132135806):
Kevin, I don't understand what you wrote? Do you have something that compiles?

#### [Kevin Buzzard (Aug 14 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132135863):
```lean
lemma compact_subset_of_t2space_is_closed_2
  [t2_space α] (Y : set α) (sc : compact Y) : (is_closed Y) :=
is_closed_iff_nhds.2 (λ y H1,
  let f := (nhds y ⊓ principal Y) in
  exists.elim (sc f H1 inf_le_right) (λ a ⟨_,_⟩,
    ( suffices y = a, from by rwa this,
      suffices nhds y ⊓ nhds a ⊓ principal Y ≠ ⊥, from eq_of_nhds_neq_bot $ not_bot_left _ _ this,
      by cc)))
```

My attempt to conform to mathlib style guide but I'm not sure I am -- I don't normally do term mode

#### [Kevin Buzzard (Aug 14 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132135967):
https://github.com/leanprover/mathlib/blob/master/docs/style.md

#### [Patrick Massot (Aug 14 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132135972):
`from by` is redundant

#### [Patrick Massot (Aug 14 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132135979):
`by` is enough

#### [Patrick Massot (Aug 14 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132135997):
how is it possible that `λ a ⟨_,_⟩,`? Someone lied to me!

#### [Kevin Buzzard (Aug 14 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132136008):
There's a problem with that idiom

#### [Mario Carneiro (Aug 14 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132136024):
use `$` to drop the parentheses and indents

#### [Kevin Buzzard (Aug 14 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132136027):
It doesn't unfold *at all* well

#### [Mario Carneiro (Aug 14 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132136044):
it unfolds exactly as well as `exists.elim`

#### [Kevin Buzzard (Aug 14 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132136071):
https://github.com/leanprover/mathlib/blob/master/docs/naming.md explains why this lemma is called `closed_of_compact`

#### [Kevin Buzzard (Aug 14 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132136230):
I should also say that I don't know if any of my suggested changes are _better_, I'm just observing that they exist :-)

#### [Mario Carneiro (Aug 14 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132136347):
there is worth in separating stylistic improvements from proof improvements

#### [Mario Carneiro (Aug 14 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132136428):
space after comma ` ⟨_, _⟩,`

#### [Mario Carneiro (Aug 14 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132136501):
you can use `let` match in place of `exists.elim`

#### [Edward Ayers (Aug 14 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132137333):
```lean
lemma compact_subset_of_t2space_is_closed_2
  [t2_space α] (Y : set α) (sc : compact Y) : is_closed Y := 
is_closed_iff_nhds.2 $ assume y h₁,
  let ⟨a, h₂, h₃⟩ := sc (nhds y ⊓ principal Y) h₁ inf_le_right in
  suffices y = a, by rwa this,
  suffices nhds y ⊓ nhds a ⊓ principal Y ≠ ⊥, 
    from eq_of_nhds_neq_bot $ not_bot_left _ _ this,
  by cc
```

#### [Mario Carneiro (Aug 14 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132137444):
I think you got everything

#### [Edward Ayers (Aug 14 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132137466):
Fabulous thanks so much for your help everyone.

#### [Mario Carneiro (Aug 14 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132137479):
oh, the name needs work

#### [Mario Carneiro (Aug 14 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132137536):
then again `closed_of_compact` is already taken, I hear

#### [Edward Ayers (Aug 14 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132137637):
Yes I found it in `continuity.lean`.

#### [Edward Ayers (Aug 14 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132137712):
My big problem with proving this was not knowing what lemmas were available. I would use vscodes find window with regex to find candidate lemmas. Are there any search tools in Lean?

#### [Patrick Massot (Aug 14 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132137720):
tactic.find in mathlib

#### [Patrick Massot (Aug 14 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132137729):
https://github.com/leanprover/mathlib/blob/master/docs/tactics.md

#### [Patrick Massot (Aug 14 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132137739):
Reading mathlib doc would probably be a good idea

#### [Patrick Massot (Aug 14 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132137748):
That find tactic is from Sebastian btw

#### [Patrick Massot (Aug 15 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132142686):
Let me try something more constructive than OS recommendations. Since you like term mode, why isn't the first lemma:
`lemma not_bot_left (f g : filter α) (H1 : f ⊓ g ≠ ⊥) : f ≠ ⊥ := neq_bot_of_le_neq_bot H1 inf_le_left`

#### [Patrick Massot (Aug 15 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/compact%20subset%20of%20hausdorff%20space%20is%20closed/near/132142828):
and mathlib name would probably be closer to `neq_bot_of_inf_neq_bot_left`

