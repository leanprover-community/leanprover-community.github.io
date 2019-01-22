---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/66636complexformsuniformspace.html
---

## [maths](index.html)
### [complex forms uniform space](66636complexformsuniformspace.html)

#### [Kenny Lau (Oct 05 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135222007):
```lean
import analysis.real analysis.complex

theorem complex.conj_sub (z w : ℂ) : complex.conj (z - w) = complex.conj z - complex.conj w :=
complex.conj_add _ _

theorem complex.uniform_continuous_conj : uniform_continuous complex.conj :=
uniform_continuous_of_metric.2 $ λ ε hε, ⟨ε, hε,
λ z w hzw, show complex.abs _ < ε, by rwa [← complex.conj_sub, complex.abs_conj]⟩

theorem complex.uniform_continuous_re : uniform_continuous complex.re :=
uniform_continuous_of_metric.2 $ λ ε hε, ⟨ε, hε, λ z w hzw,
calc  dist z.re w.re
    ≤ complex.abs (z-w) : complex.abs_re_le_abs (z-w)
... < ε : hzw⟩

theorem complex.uniform_continuous_im : uniform_continuous complex.im :=
uniform_continuous_of_metric.2 $ λ ε hε, ⟨ε, hε, λ z w hzw,
calc  dist z.im w.im
    ≤ complex.abs (z-w) : complex.abs_im_le_abs (z-w)
... < ε : hzw⟩

example (f : filter ℂ) (hf : cauchy f) : ∃ x, f ≤ nhds x :=
let ⟨xr, hxr⟩ := complete_space.complete
  (cauchy_map complex.uniform_continuous_re hf) in
let ⟨xi, hxi⟩ := complete_space.complete
  (cauchy_map complex.uniform_continuous_im hf) in
⟨⟨xr, xi⟩, sorry⟩

/-
state:
f : filter ℂ,
hf : cauchy f,
xr : ℝ,
hxr : filter.map complex.re f ≤ nhds xr,
xi : ℝ,
hxi : filter.map complex.im f ≤ nhds xi
⊢ f ≤ nhds {re := xr, im := xi}
-/
```
half-completed proof

#### [Kenny Lau (Oct 05 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135222089):
@**Andreas Swerdlow**

#### [Kenny Lau (Oct 05 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135222945):
```lean
import analysis.real analysis.complex

theorem complex.conj_sub (z w : ℂ) : complex.conj (z - w) = complex.conj z - complex.conj w :=
complex.conj_add _ _

theorem complex.uniform_continuous_conj : uniform_continuous complex.conj :=
uniform_continuous_of_metric.2 $ λ ε hε, ⟨ε, hε,
λ z w hzw, show complex.abs _ < ε, by rwa [← complex.conj_sub, complex.abs_conj]⟩

theorem complex.uniform_continuous_re : uniform_continuous complex.re :=
uniform_continuous_of_metric.2 $ λ ε hε, ⟨ε, hε, λ z w hzw,
calc  dist z.re w.re
    ≤ complex.abs (z-w) : complex.abs_re_le_abs (z-w)
... < ε : hzw⟩

theorem complex.uniform_continuous_im : uniform_continuous complex.im :=
uniform_continuous_of_metric.2 $ λ ε hε, ⟨ε, hε, λ z w hzw,
calc  dist z.im w.im
    ≤ complex.abs (z-w) : complex.abs_im_le_abs (z-w)
... < ε : hzw⟩

theorem complex.uniform_continuous_of_real : uniform_continuous complex.of_real :=
uniform_continuous_of_metric.2 $ λ ε hε, ⟨ε, hε, λ z w hzw,
calc  dist (complex.of_real z) (complex.of_real w)
    = dist z w : complex.abs_of_real _
... < ε : hzw⟩

example (f : filter ℂ) (hf : cauchy f) : ∃ x, f ≤ nhds x :=
let ⟨xr, hxr⟩ := complete_space.complete
  (cauchy_map complex.uniform_continuous_re hf) in
let ⟨xi, hxi⟩ := complete_space.complete
  (cauchy_map complex.uniform_continuous_im hf) in
have hxr2 : filter.tendsto (complex.of_real ∘ complex.re) f (nhds (complex.of_real xr)),
  from filter.tendsto.comp hxr (continuous.tendsto
    (uniform_continuous.continuous complex.uniform_continuous_of_real) xr),
have hxi2 : filter.tendsto (complex.of_real ∘ complex.im) f (nhds (complex.of_real xi)),
  from filter.tendsto.comp hxi (continuous.tendsto
    (uniform_continuous.continuous complex.uniform_continuous_of_real) xi),
have filter.tendsto (λ z:ℂ, (z.re + z.im * complex.I:ℂ)) f (nhds _),
  from tendsto_add hxr2 (tendsto_mul hxi2 (@tendsto_const_nhds _ _ _ complex.I _)),
⟨(xr+xi*complex.I), by rw [funext complex.re_add_im] at this; rw [← (filter.map_id : _ = f)]; exact this⟩
```

#### [Kenny Lau (Oct 05 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135222946):
complete proof

#### [Andreas Swerdlow (Oct 05 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135224448):
Wow thank you!

#### [Andreas Swerdlow (Oct 05 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135224468):
@**Joseph Corneli** look what Kenny did

#### [Kenny Lau (Oct 05 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135224585):
I should probably extract a lemma

#### [Mario Carneiro (Oct 05 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135224597):
that proof looks like a good advertisement for bundling continuous functions

#### [Mario Carneiro (Oct 05 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135224662):
For a while I was thinking that maybe we want to work with continuous functions as a predicate, but compositional proofs of continuity really suck from a readability standpoint

#### [Kenny Lau (Oct 05 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135224685):
another thing to refactor :P

#### [Kenny Lau (Oct 05 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135225113):
```lean
import analysis.real analysis.complex

theorem complex.conj_sub (z w : ℂ) : complex.conj (z - w) = complex.conj z - complex.conj w :=
complex.conj_add _ _

theorem complex.uniform_continuous_conj : uniform_continuous complex.conj :=
uniform_continuous_of_metric.2 $ λ ε hε, ⟨ε, hε,
λ z w hzw, show complex.abs _ < ε, by rwa [← complex.conj_sub, complex.abs_conj]⟩

theorem complex.uniform_continuous_re : uniform_continuous complex.re :=
uniform_continuous_of_metric.2 $ λ ε hε, ⟨ε, hε, λ z w hzw,
calc  dist z.re w.re
    ≤ complex.abs (z-w) : complex.abs_re_le_abs (z-w)
... < ε : hzw⟩

theorem complex.uniform_continuous_im : uniform_continuous complex.im :=
uniform_continuous_of_metric.2 $ λ ε hε, ⟨ε, hε, λ z w hzw,
calc  dist z.im w.im
    ≤ complex.abs (z-w) : complex.abs_im_le_abs (z-w)
... < ε : hzw⟩

theorem complex.uniform_continuous_of_real : uniform_continuous complex.of_real :=
uniform_continuous_of_metric.2 $ λ ε hε, ⟨ε, hε, λ z w hzw,
calc  dist (complex.of_real z) (complex.of_real w)
    = dist z w : complex.abs_of_real _
... < ε : hzw⟩

theorem complex.continuous_conj : continuous complex.conj :=
uniform_continuous.continuous complex.uniform_continuous_conj

theorem complex.continuous_re : continuous complex.re :=
uniform_continuous.continuous complex.uniform_continuous_re

theorem complex.continuous_im : continuous complex.im :=
uniform_continuous.continuous complex.uniform_continuous_im

theorem complex.continuous_of_real : continuous complex.of_real :=
uniform_continuous.continuous complex.uniform_continuous_of_real

theorem complex.filter_le_iff (f : filter ℂ) (z : ℂ) :
  f ≤ nhds z ↔ filter.tendsto complex.re f (nhds z.re) ∧ filter.tendsto complex.im f (nhds z.im) :=
⟨λ h, ⟨le_trans (filter.map_mono h)
    (continuous.tendsto complex.continuous_re z),
  le_trans (filter.map_mono h)
    (continuous.tendsto complex.continuous_im z)⟩,
λ ⟨hr, hi⟩,
have hr2 : filter.tendsto (λ z:ℂ, (z.re:ℂ)) f (nhds z.re),
  from filter.tendsto.comp hr (continuous.tendsto
    (complex.continuous_of_real) z.re),
have hi2 : filter.tendsto (λ z:ℂ, (z.im:ℂ)) f (nhds z.im),
  from filter.tendsto.comp hi (continuous.tendsto
    (complex.continuous_of_real) z.im),
have _ := tendsto_add hr2 (tendsto_mul hi2 (@tendsto_const_nhds _ _ _ complex.I _)),
by rw [funext complex.re_add_im, complex.re_add_im] at this; rw [← (filter.map_id : _ = f)]; exact this⟩

example (f : filter ℂ) (hf : cauchy f) : ∃ x, f ≤ nhds x :=
let ⟨xr, hxr⟩ := complete_space.complete
  (cauchy_map complex.uniform_continuous_re hf) in
let ⟨xi, hxi⟩ := complete_space.complete
  (cauchy_map complex.uniform_continuous_im hf) in
⟨⟨xr,xi⟩, (complex.filter_le_iff _ _).2 ⟨hxr, hxi⟩⟩
```

#### [Kenny Lau (Oct 05 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135225115):
@**Andreas Swerdlow**

#### [Mario Carneiro (Oct 05 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135225373):
I think there should be another way to say this in terms of the product topology

#### [Mario Carneiro (Oct 05 2018 at 02:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135225386):
That is, this should follow from the fact that C is homeomorphic to R x R with `re` and `im` as the projections

#### [Kenny Lau (Oct 05 2018 at 02:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135225448):
is this a fact yet? and will that be easier to use?

#### [Mario Carneiro (Oct 05 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135225459):
that remains to be seen

#### [Mario Carneiro (Oct 05 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135225466):
I don't think we have homeos yet (@**Patrick Massot** ? @**Johannes Hölzl** ?)

#### [Mario Carneiro (Oct 05 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135225526):
But I think you can prove `filter_le_iff` pretty easily if you do it on a product space with fst and snd

#### [Mario Carneiro (Oct 05 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135225593):
And in any case what you really need is just plain continuity of the relevant functions and I think you already have that

#### [Kenny Lau (Oct 05 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135225605):
I see

#### [Mario Carneiro (Oct 05 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135225695):
wait, does C have the metric topology or the product topology by definition?

#### [Kenny Lau (Oct 05 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135238089):
metric

#### [Patrick Massot (Oct 05 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135238108):
Those are meant to be defeq

#### [Kenny Lau (Oct 05 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135238160):
C isn't even defined to be a product

#### [Patrick Massot (Oct 05 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135238183):
I meant that product topology and metric topology on a product of metric spaces are defeq, I don't really know how C is constructed in Lean

#### [Mario Carneiro (Oct 05 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135238252):
It is possible to state this theorem using `(co)map` on topologies. You want to say that the topology on C is induced by the map `\lam z, (z.re, z.im)`, or coinduced by `\lam p, p.1 + I p.2`

#### [Kenny Lau (Oct 05 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135238944):
```quote
I meant that product topology and metric topology on a product of metric spaces are defeq, I don't really know how C is constructed in Lean
```
are they?

#### [Kenny Lau (Oct 05 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135238945):
isn't it a theorem?

#### [Kenny Lau (Oct 05 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135238948):
that involves drawing a cirlce inside a square inside a circle inside a square?

#### [Johan Commelin (Oct 05 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135238959):
```quote
that involves drawing a cirlce inside a square inside a circle inside a square?
```
Can Lean do that?

#### [Patrick Massot (Oct 05 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135238974):
there is no circle in Lean. The product metric is defined as the max metric

#### [Kenny Lau (Oct 05 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135239022):
oh well then it isn't defeq to the metric in C then

#### [Kenny Lau (Oct 05 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135239023):
the metric in C is the circle metric

#### [Mario Carneiro (Oct 05 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135239046):
the balls in C are circles because it uses the metric topology

#### [Johan Commelin (Oct 05 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135239110):
Right, but not the product metric...

#### [Mario Carneiro (Oct 05 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135239123):
if we wanted, we could define the topology on C as the product topology (or rather a mapping thereof), and then the typeclass would force us to prove this theorem

#### [Mario Carneiro (Oct 05 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135239177):
but given that C has no pre-existing topology on it, it seems okay to just use the metric topology as the definition; but this means that we don't get any help with the homeo proof

#### [Kenny Lau (Oct 05 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135239231):
I mean, my filter lemma *is* the homeomorphism

#### [Patrick Massot (Oct 05 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135239236):
```quote
I don't think we have homeos yet (Patrick Massot** ? Johannes Hölzl ?)
```
This is not in mathlib, mostly because I don't know whether it should use the category theory stuff or be as in https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/homeos.lean

#### [Mario Carneiro (Oct 05 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135239319):
no categories in the definition

#### [Mario Carneiro (Oct 05 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135239323):
it should be 100% topology

#### [Patrick Massot (Oct 05 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135239329):
do you want me to PR that file then?

#### [Mario Carneiro (Oct 05 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135239379):
I don't see why not... I will leave the merging to Johannes though since he's been involved more

#### [Kenny Lau (Oct 05 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135239463):
I really think the circle metric is the right one

#### [Kenny Lau (Oct 05 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135239471):
hmm, never mind

#### [Mario Carneiro (Oct 05 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135239608):
The circle *metric* is certainly the right one, but I wonder if the *topology* should be defined using something like `comap re \sqcap comap im`

#### [Mario Carneiro (Oct 05 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/complex forms uniform space/near/135239681):
which will make your filter theorem essentially by definition, and the bulk of that proof will be transferred to the construction of the metric_space instance

