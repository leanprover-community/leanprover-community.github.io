---
author: 'Mathlib community'
category: 'month-in-mathlib'
date: 2021-08-31 08:56:51+00:00
description: ''
has_math: true
link: ''
slug: month-in-mathlib-aug-2021
tags: ''
title: This month in mathlib (Aug 2021)
type: text
---

# This month in mathlib (Aug 2021)

## Highlighted PRs

* [PR #8652](https://github.com/leanprover-community/mathlib/pull/8652) :: chore(*): update lean to 3.32.1

  The community fork of Lean made two new
  [releases](https://github.com/leanprover-community/lean/blob/master/doc/changes.md#3321c-12-august-2021)
  `3.32.0` and `3.32.1`.
  This is part of the preparations for porting mathlib to Lean 4.

* [PR #8281](https://github.com/leanprover-community/mathlib/pull/8281) :: feat(topology,geometry/manifold): continuous and smooth partition of unity

  See the [companion blogpost](continuous-partitions-of-unity/) for details.

* Radon-Nikodym and Lebesgue decomposition. The four PRs
  [PR #8645](https://github.com/leanprover-community/mathlib/pull/8645)
  [PR #8687](https://github.com/leanprover-community/mathlib/pull/8687)
  [PR #8763](https://github.com/leanprover-community/mathlib/pull/8763)
  [PR #8875](https://github.com/leanprover-community/mathlib/pull/8875)
  together contribute
  the Lebesgue decomposition for sigma-finite measures
  and the Radon-Nikodym theorem.

* [PR #7978](https://github.com/leanprover-community/mathlib/pull/7978) :: feat(measure_theory/interval_integral): strong version of FTC-2

  This PR signals the start of a serious attack on Stokes' theorem,
  which will unlock a general approach to complex analysis.

* [PR #8692](https://github.com/leanprover-community/mathlib/pull/8692) :: feat(field_theory): finite fields exist

  Most of this PR had been lying around for ages,
  but it was finally put together in mathlib.
  It shows the existence and uniqueness of finite fields.

* Among several PRs from the Dedekind project, the two most noteworthy are
  - [PR #8530](https://github.com/leanprover-community/mathlib/pull/8530) :: feat(ring_theory): ideals in a Dedekind domain have unique factorization
  - [PR #8626](https://github.com/leanprover-community/mathlib/pull/8626) :: feat(ring_theory): define the ideal class group

* [PR #8377](https://github.com/leanprover-community/mathlib/pull/8377) :: feat(analysis/complex/upper_half_plane): new file

  This PR defines the complex upper half plane, together with the $\mathrm{SL}_2$-action.
  Upcoming PRs will characterize the fundamental domain of the $\mathrm{SL}_2(\mathbb{Z})$-action.

## Other mathematical contributions

The following PRs are ordered by the date that they were merged into mathlib.

* [PR #8424](https://github.com/leanprover-community/mathlib/pull/8424) :: feat(analysis/complex): prove that complex functions are conformal if and only if the functions are holomorphic/antiholomorphic with nonvanishing differential
* [PR #4885](https://github.com/leanprover-community/mathlib/pull/4885) :: feat(category_theory/adjunction): general adjoint functor theorem
* [PR #8560](https://github.com/leanprover-community/mathlib/pull/8560) :: feat(matrix/kronecker): Add the Kronecker product
* [PR #8388](https://github.com/leanprover-community/mathlib/pull/8388) :: feat(measure_theory/decomposition/signed_hahn): signed version of the Hahn decomposition theorem
* [PR #8588](https://github.com/leanprover-community/mathlib/pull/8588) :: feat(linear_algebra): Smith normal form for submodules over a PID
* [PR #8266](https://github.com/leanprover-community/mathlib/pull/8266) :: feat(measure_theory/stieltjes_measure): Stieltjes measures associated to monotone functions
* [PR #8598](https://github.com/leanprover-community/mathlib/pull/8598) :: feat(topology/algebra/weak_dual_topology + analysis/normed_space/weak_dual_of_normed_space): add definition and first lemmas about weak-star topology
* [PR #8639](https://github.com/leanprover-community/mathlib/pull/8639) :: feat(measure): prove Haar measure = Lebesgue measure on R
* [PR #8558](https://github.com/leanprover-community/mathlib/pull/8558) :: feat(algebraic_geometry/EllipticCurve): add working definition of elliptic curve
* [PR #8538](https://github.com/leanprover-community/mathlib/pull/8538) :: feat(group_theory/nilpotent): add nilpotent groups
* [PR #8343](https://github.com/leanprover-community/mathlib/pull/8343) :: feat(linear_algebra/dimension): generalize inequalities and invariance of dimension to arbitrary rings
* [PR #8791](https://github.com/leanprover-community/mathlib/pull/8791) :: feat(measure_theory): volume of a (closed) L∞-ball
* [PR #8576](https://github.com/leanprover-community/mathlib/pull/8576) :: feat(analysis/normed_space/exponential): define exponential in a Banach algebra and prove basic results
