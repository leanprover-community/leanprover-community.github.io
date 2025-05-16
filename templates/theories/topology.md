# Maths in Lean: Topological, uniform and metric spaces

The `TopologicalSpace` typeclass is defined in mathlib,
in `Mathlib.Topology.Defs.Basic`. There a lot of
lines of code in `topology`,covering the basics of topological spaces, continuous functions,
topological groups and rings, and infinite sums. These docs
are just concerned with the contents of the `Mathlib.Topology`
folder.

### The basic typeclass

The `TopologicalSpace` typeclass is an inductive type, defined
as a structure on a type `α` in the obvious way: there is an `IsOpen`
predicate, telling us when `U : Set α` is open, and then the axioms
for a topology (pedantic note: the axiom that the empty set is open
is omitted, as it follows from the fact that a union of open sets
is open, applied to the empty union!).

Note that there are two ways of formalizing the axiom that an arbitrary
union of open sets is open: one could either ask that given a set
of open sets, their union is open, or one could ask that given
a function from some index set `I` to the set of open sets, the union
of the values of the function is open. Mathlib goes for the first
one, so the axiom is

```lean
isOpen_sUnion : ∀ (s : Set (set α)), (∀ t ∈ s, IsOpen t) → IsOpen (⋃₀ s)
```

and then the index set version is a lemma:

```lean
lemma isOpen_biUnion {f : ι → Set α} {s : Set ι} (h : ∀ i ∈ s, IsOpen (f i)) : IsOpen (⋃ i ∈ s, f i)
```

Note the naming conventions, standard across mathlib, that `sUnion`
is a union over sets and `biUnion` is a union over
the image of a function on an indexing set. The capital U's are
to indicate a union of arbitrary size, as opposed to `union`, which
indicates a union of two sets:

```lean
lemma IsOpen.union (h₁ : is_open s₁) (h₂ : is_open s₂) : is_open (s₁ ∪ s₂)
```

The predicate `IsClosed`, and functions `interior`, `closure`, and
`frontier` (closure minus interior,
sometimes called boundary in mathematics) are defined, and basic
properties about them are proved. For example

```lean
import Mathlib.Topology.Basic


open TopologicalSpace
variable {X : Type} [TopologicalSpace X] {U V C D Y Z : Set X}

example : IsClosed C → IsClosed D → IsClosed (C ∪ D) := IsClosed.union

example : IsOpen Cᶜ ↔ IsClosed C := isOpen_compl_iff

example : IsOpen U → IsClosed C → IsOpen (U \ C) := IsOpen.sdiff

example : interior Y = Y ↔ IsOpen Y := interior_eq_iff_isOpen

example : Y ⊆ Z → interior Y ⊆ interior Z := interior_mono

example : IsOpen Y ↔ ∀ x ∈ Y, ∃ U ⊆ Y, IsOpen U ∧ x ∈ U := isOpen_iff_forall_mem_open

example : closure Y = Y ↔ IsClosed Y := closure_eq_iff_isClosed

example : closure Y = (interior Yᶜ)ᶜ := closure_eq_compl_interior_compl
```

### Filters

In mathlib, unlike the typical approach in a mathematics textbook, extensive
use is made of filters as a tool in the theory of topological spaces. Let
us briefly review the notion of a filter in mathematics. A filter on a set
`X` is a non-empty collection `F` of subsets of `X` satisfying the following
two axioms:

1) if `U ∈ F` and `U ⊆ V`, then `V ∈ F`; and
2) if `U, V ∈ F` then there exists `W ∈ F` with `W ⊆ U ∩ V`.

Informally, one can think of `F` as the set of "big" subsets of `X`. For example, if `X` is a set and `F` is the set of subsets `Y` of `X` such that `X \ Y` is finite, then `F` is a filter. This is called the _cofinite filter_ on `X`.

Note that if `F` is a filter that contains the empty set, then it contains all subsets of `X` by the first axiom. This filter is sometimes called "bottom" (we will see why a little later on). Some references demand that the empty set is not allowed to be in a filter -- Lean does not have this restriction. A filter not containing the empty set is sometimes called a "proper filter".

If `X` is a topological space, and `x ∈ X`, then the _neighborhood filter_ `𝓝 x` of `x` is the set of subsets `Y` of `X` such that `x` is in the interior of `Y`. One checks easily that this is a filter (technical point: to see that this is actually the definition of `𝓝 x` in mathlib, it helps to know that the set of all filters on a type is a complete lattice, partially ordered using `F ≤ G` iff `G ⊆ F`, so the definition, which involves an inf, is actually a union; also, the definition I give is not literally the definition in mathlib, but `lemma mem_nhds_iff` says that their definition is the one here. Note also that this is why the filter with the most sets is called bottom!).

Why are we interested in these filters? Well, given a map `f` from `ℕ` to a topological space `X`, one can check that the resulting sequence `f 0`, `f 1`, `f 2`... tends to `x ∈ X` if and only if the pre-image of any element in the filter `𝓝 x` is in the cofinite filter on `ℕ` -- this is just another way of saying that given any open set `U` containing `x`, there exists `N` such that for all `n ≥ N`, `f n ∈ U`. So filters provide a way of thinking about limits.

As an example, below are three limits formulated in Lean.
The example uses the filters `atTop` and `atBot` that represent "tends to `∞`" and "tends to `-∞`" in a type equipped with an order.

```lean
open Filter Topology

-- The limit of `2 * x` as `x` tends to `3` is `6`
example : Tendsto (fun x : ℝ ↦ 2 * x) (𝓝 3) (𝓝 6) := sorry
-- The limit of `1 / x` as `x` tends to `∞` is `0`
example : Tendsto (fun x : ℝ ↦ 1 / x) atTop (𝓝 0) := sorry
-- The limit of `x ^ 2` as `x` tends to `-∞` is `∞`
example : Tendsto (fun x : ℝ ↦ x ^ 2) atBot atTop := sorry
```

The _principal filter_ `Filter.principal Y` attached to a subset `Y` of a set `X` is the collection of all subsets of `X` that contain `Y`. So it's not difficult to convince yourself that the following results should be true:

```lean
variable (X : Type) [TopologicalSpace X] (Y : Set X)

example : interior Y = {x | 𝓝 x ≤ Filter.principal Y} := interior_eq_nhds

example : IsOpen Y ↔ ∀ y ∈ Y, Y ∈ (𝓝 y).sets := isOpen_iff_eventually
```

### Compactness with filters

As a consequence of the filter-centric approach, some definitions in mathlib
look rather strange to a mathematician who is not used to this approach.
We have already seen a definition using filters
for what it means for a sequence to tend to a limit. The definition
of compactness is also written in filter-theoretic terms:

```lean
/-- A set `s` is compact if for every nontrivial filter `f` that contains `s`,
    there exists `a ∈ s` such that every set of `f` meets every neighborhood of `a`. -/
def IsCompact (s : Set X) :=
  ∀ ⦃f⦄ [NeBot f], f ≤ 𝓟 s → ∃ x ∈ s, ClusterPt x f
```

Translated, this says that a subset `Y` of a topological space `X` is compact if for every proper filter `F` on `X`, if `Y` is an element of `F` then there's an element `y` of `Y` such that the smallest filter containing both F and the neighborhood filter of `y` is not the filter of all subsets of `X` either. This should be thought of as being the correct general analogue of the Bolzano-Weierstrass theorem, that in a compact subspace of `ℝ^n`, any sequence has a convergent subsequence.

One might ask why this definition of compactness has been chosen, rather than the standard one about open covers having finite subcovers. The reasons for this are in some sense computer-scientific rather than mathematical -- the issue should not be what definition is ultimately chosen (indeed the developers should feel free to choose whatever definition they like as long as it is logically equivalent to the usual one, and they might have reasons related to non-mathematical points such as running times), the issue should be how to prove that the inbuilt definition is equivalent to the one you want to use in practice. And fortunately, we have

```lean
example : IsCompact Y ↔ ∀ {ι : Type} (U : ι → Set X),
      (∀ i, IsOpen (U i)) → (Y ⊆ ⋃ i, U i) → ∃ t : Finset ι, Y ⊆ ⋃ i ∈ t, U i :=
    isCompact_iff_finite_subcover
```

so the Lean definition is equivalent to the standard one.

### Hausdorff spaces

In Lean they chose the terminology `T2Space` to mean Hausdorff (perhaps because it is shorter!).

```lean
class T2Space (X : Type u) [TopologicalSpace X] : Prop where
  /-- Every two points in a Hausdorff space admit disjoint open neighbourhoods. -/
  t2 : Pairwise fun x y => ∃ u v : Set X, IsOpen u ∧ IsOpen v ∧ x ∈ u ∧ y ∈ v ∧ Disjoint u v
```

Of course Hausdorffness is what we need to ensure that limits are unique, but because limits are defined using filters this statements ends up reading as follows:

```lean
lemma tendsto_nhds_unique [T2Space X] {f : β → X} {l : Filter β} {x y : X}
  [l.NeBot] (hx : Tendsto f l (𝓝 x)) (hb : Tendsto f l (𝓝 y)) : x = y
```

Note that actually this statement is more general than the classical statement that if a sequence tends to two limits in a Hausdorff space then the limits are the same, because it applies to any non-trivial filter on any set rather than just the cofinite filter on the natural numbers.

### Bases for topologies.

If `X` is a _set_, and `S` is a collection of subsets of `X`, then one can
consider the topology "generated by" `S`, which (as is typical in these
situations) can be defined in two ways: firstly as the intersection
of all the topologies on `X` containing `S` (where we are here identifying
a topology with the underlying collection of open sets), or more constructively
as the sets "generated by" `S` using the axioms of a topological space.
Unsurprisingly, it is this latter definition which is used in Lean, as the
open sets are naturally an inductive type; the open sets are called
`generate_open S` and the topology is `generate_from S`.

The definition of a basis for a topology in mathlib includes an axiom
that the topology is generated from the basis in the sense above, which may make
it hard to prove for an end user that a given set satisfies the definition
directly. However again we have a theorem which reduces us to checking
the two usual axioms for a basis:

```lean
example (B : Set (Set X)) (h_open : ∀ V ∈ B, IsOpen V)
  (h_nhds : ∀ (x : X) (U : Set X), x ∈ U → IsOpen U → ∃ V ∈ B, x ∈ V ∧ V ⊆ U) :
IsTopologicalBasis B :=
isTopologicalBasis_of_isOpen_of_nhds h_open h_nhds
```

### Other things

There are other things involving filters, there are separable, first-countable
and second-countable spaces, product spaces, subspace and quotient
topologies (and more generally pull-back and push-forward of a topology)
and things like t1 and t3 spaces.

## File organization

The following "core" modules form a linear chain of imports. A theorem involving concepts defined in several of these files should be found in the last such file in this ordering.

* `Mathlib.Topology.Basic`
  Topological spaces. Open and closed subsets, interior, closure and frontier (boundary). Neighborhood filters. Limit of a filter. Locally finite families. Continuity and continuity at a point.
* `Mathlib.Topology.Order.Basic`
  The complete lattice structure on topologies on a fixed set. Induced and coinduced topologies.
* `maps`
  Open and closed maps. "Inducing" maps. Embeddings, open embeddings and closed embeddings. Quotient maps.
* `Mathlib.Topology.Constructions`
  Building new topological spaces from old ones: products, sums, subspaces and quotients.
* `Mathlib.Topology.Separation`
  Separation axioms T₀ through T₄, also known as Kolmogorov, Tychonoff or Fréchet, Hausdorff, regular, and normal spaces respectively.

Some of the remaining directories and files, in no particular order:

* `Mathlib.Topology.Algebra`
  Topological spaces with compatible algebraic or ordered structure.
* `Mathlib.Topology.Category`
  The categories of topological spaces, uniform spaces, etc.
* `Mathlib.Topology.Instances`
  Specific topological spaces such as the real numbers and the complex numbers.
* `Mathlib.Topology.MetricSpace`
  The theory of metric spaces; but some notions one might expect to find here are instead generalized to uniform spaces.
* `Mathlib.Topology.Sheaves`
  Presheaves on a topological space.
* `Mathlib.Topology.UniformSpace`
  The theory of uniform spaces, including notions such as completeness, uniform continuity and totally bounded sets.
* `Mathlib.Topology.Bases`
  Bases for filters and topological spaces. Separable, first countable and second countable spaces.
* `Mathlib.Topology.CompactOpen`
  The compact-open topology on the space of continuous maps between two topological spaces.
* `Mathlib.Topology.ContinuousOn`
  Neighborhoods within a subset. Continuity on a subset, and continuity within a subset at a point.
* `Mathlib.Topology.DenseEmbedding`
  Embeddings and other functions with dense image.
* `Mathlib.Topology.Homeomorph`
  Homeomorphisms between topological spaces.
* `Mathlib.Topology.List`
  Topologies on lists and vectors.
* `Mathlib.Topology.Sequences`
  Sequential closure and sequential spaces. Sequentially continuous functions.
* `Mathlib.Topology.StoneCech`
  The Stone-Čech compactification of a topological space.
