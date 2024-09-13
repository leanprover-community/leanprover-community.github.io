# Pull Request Review Guide

This guide provides a detailed look at how to conduct PR reviews for mathlib. You may
wonder whether this guide applies to you, and the answer is "yes!"

While the mathlib maintainers are the only users with authority to *merge* pull requests,
everyone is welcome, and even encouraged, to *review* pull requests. (Note: there is in 
fact another category of people, mathlib *reviewers*, who have shown that they can provide
valuable PR reviews; approving reviews from these users with `maintainer merge` are more
quickly merged by maintainers).

A history of helpful reviews is a key criterion for membership on either the mathlib
reviewer or mathlib maintainer teams.

This guide starts with general [guidelines](#guidelines-for-review) for conducting reviews,
a high-level [overview](#what-to-consider-when-reviewing) of what reviewers should be
considering and then focuses on a few practical [examples](#examples).

While this guide is rather long, it is not required to comprehend everything before
starting to review. Partial reviews are themselves helpful, and you can learn about the
various considerations in a piecemeal fashion as you progress in your understanding
of Lean and mathlib.

## Guidelines for review

### Respect and encouragment

As with all interactions in the mathlib community, be sure to adhere to the
[Code of Conduct](https://www.contributor-covenant.org/version/2/0/code_of_conduct/).
In short, be respectful. However, when reviewing please be
sure to also be *encouraging*. The majority of contributors have only made
a handful of pull requests, and this may even be their first! As such it is
important to avoid comments like "This result is useless, we already have a
version of it." Instead you could be more gentle and say, for example, "Thanks
for proving this, but I think we already have a lemma to this effect. It is
`my_generic_lemma`. Please try to use that instead." Try to find the
good in what they have done, even while pointing out room for improvement.

### Humility

None of us, including the mathlib maintainers, is perfect or has a monopoly
on best practices. As such, reviewers should always leave room for someone
to suggest a better approach. In addition, it's important to recognize that
*you may be wrong*, and to allow for this possibility. Of course, perfect is
the enemy of the good, so it is not necessary to wait indefinitely for 
better approaches or new ideas.

## What to consider when reviewing

Reviewing is essentially about looking at code and asking yourself questions.
The foundational issues, organized approximately from easiest to hardest, are:
style, documentation, location, improvements and library integration.

Note that new reviewers are certainly capable of commenting on the first two
or three issues, whereas answering questions of library integration generally
requires several months of developing familiarity with mathlib and contributing
toward the reviewing process.

Here are some explicit questions you can ask yourself as a reviewer.
This is just an outline; in later sections we investigate each question
in more detail with examples.

- [does it adhere to style?](#style)
    + [code formatting](style.html)
    + [naming conventions](naming.html)
    + is the [PR title and description](commit.html) appropriately informative?
- [is there useful documentation?](#documentation)
    + do the definitions have sufficiently informative docstrings?
    + are there cross references to related declarations?
    + do complicated proofs have a sketch in comments interspersed throughout?
    + do important theorems have docstrings?
    + are there warnings to the user when code should only be used in certain ways?
    + is it formalizing something from the literature?
- [location, location, location](#location)
    + are the declarations in the appropriate files?
      [`#find_home`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Util/Imports.html#«command#find_home_») can be useful here.
    + do the results already exist? possibly in a more general form with a different name? 
      The `apply?` or `exact?` tactics can help answer this sometimes.
    + are new `import`s introduced, and if so, do they import too much material for this file?
    + should some of the results be placed into a new file to minimize import requirements?
    + should a file be split into multiple pieces because its getting too long (e.g., > 1000 lines),
      or touches on too many different topics?
- [are there obvious improvements that can be made?](#improvements)
    + can pieces be split into supporting lemmas or definitions (especially for long proofs)?
    + can different / better tactics be used to improve readability (e.g., using `gcongr`
      instead of `mul_le_mul_of_nonneg_left`)?
      Note: code golfing is okay as long as it *doesn't sacrifice readability*, although golfing
      trivial results is generally okay.
    + does a different proof structure greatly simplify the argument?
    + are the definitions introduced the best way to formalize the concept (very difficult!)?
- [does it advance or improve the library?](#library-integration)
    + does it provide a sensible API?
    + is it general enough to support known future needs?
    + does it fit the design and collective vision of mathlib?
- more specific considerations
    + do declarations use `α β : Type*` instead of `α β : Type _` to refer to arbitrary universe levels?
      (Note: this is a performance issue because using `Type _` introduces unification problems that
      need solving.)
    + are lemmas tagged `@[simp]`, `@[ext]`, et cetera where they should be? or shouldn't be?
    + do new definitions come with lemmas about them (perhaps even just those generated by `@[simps]`)
    + do any newly declared instances create diamonds? non-defeq or non-propeq?

## Examples

The remainder of this guide is devoted to considering both contrived and real-world
examples of the review process. We attempt to provide examples for each of the following
questions above. Parties involved in the real-world examples have been consulted for
permission for inclusion in this style guide.

Not every question has a corresponding example, but we attempt to provide at least a 
discussion about what should be considered in each case.

### Style

#### Code formatting

```lean
-- do NOT write code in this style!
theorem mul_assoc_assoc {α : Type*} [Semigroup α] (a b c d : α)
: a*b*c*d=a*(b*(c*d)) :=
by
rw [mul_assoc,
    mul_assoc]
```

The code above violates several formatting guidelines: there are no
spaces around binary operations, the line starts with a `:` instead of 
ending it on the previous line, `by` should be moved to the previous line
instead of by itself (a style linter should catch this anyway in CI),
and the `rw` tactic is unnecessarily split across multiple lines.

The author of the PR in this situation, by virtue of violating so many
style guidelines, is probably a new contributor and is unfamiliar with,
or doesn't recall, the style guide. An appropriate review comment would 
be something like:

````markdown
In case you're unaware, please familiarize yourself with the mathlib
[style guide](https://leanprover-community.github.io/contribute/style.html).
You need spaces around `*`, `:` at the end of the line and the `rw` to 
be on the same line.
```suggestion
theorem mul_assoc_assoc {α : Type*} [Semigroup α] (a b c d : α) :
    a * b * c * d = a * (b * (c * d)) := by
  rw [mul_assoc, mul_assoc]
```
````

#### Naming conventions

```lean
theorem inv_is_unit_times_self_eq_1 {M : Type*} [Monoid M] {a : M} (h : IsUnit a) :
    ↑(IsUnit.unit h)⁻¹ * a = 1 := sorry
```

The above lemma is taken directly from the library, can you guess its actual name?
It is `IsUnit.inv_val_mul`. An appropriate review to suggest a new name might look
something like:

````markdown
In order to accord with the 
[naming conventions](https://leanprover-community.github.io/contribute/naming.html)
for mathlib, I suggest renaming this to: `IsUnit.inv_val_mul`. Note that:

- we use `mul` instead of `times`, and `one` instead of `1`
- the lemma is sufficiently clear without the reference to `1`
- If we are referencing an `IsUnit` hypothesis, we would use `isUnit`, not `is_unit`
- However, since we have an `IsUnit` hypothesis, putting it in the `IsUnit.` 
  namespace allows for use with dot notation.
- we should reference the coercion that appears here, which is `Subtype.val`, hence
  the `val` in the suggested name.
````

This provides the PR author with a link to the naming conventions in case they
haven't yet seen it, but also points out the specific issues so that they don't
have to read through the entire guide again. This is probably helpful also if 
they have only made one error in the naming convention.

Note: not all declarations have exactly one suitable name, there may be a few, 
each with their own advantages and disadvantages.

#### Is the PR title and description appropriately informative?

Consider the following PR title and description:

```markdown
Title: feat(Analysis/SpecificLimits)
Description: Where should we put these lemmas?
```

This has two issues: the title doesn't provide any information about the changes
and the description includes a discussion question, as opposed to information 
about the changes. A reasonable review comment might be something like:

```markdown
Please update the PR title and description to be more informative about what 
you have added or changed as these will be permanently included in the git
history when this is merged. Questions or topics for discussion are allowed
in the PR description, but should be placed after the `---`, as then they
will be treated as comments and not included in the git history.
```

Of course, you could provide suggestions, or even update the PR title and 
description yourself, but you may want to point it out, especially if the 
PR author is a relatively new contributor.

### Documentation

#### Do the definitions have sufficiently informative docstrings?

The `docBlame` linter should ensure that users add docstrings to all their
definitions. However, just because a docstring *exists* doesn't necessarily
mean it's *useful* and *accurate*. Reviewers should do their best to make sure
the provided docstring accurately describes the `def` in an easily intelligible
way.

#### Do important theorems have docstrings?

The following example makes reference to the review in
[#5580](https://github.com/leanprover-community/mathlib4/pull/5580/files).
In that PR, the following theorem was added:

```lean
protected theorem _root_.WithSeminorms.equicontinuous_TFAE {κ : Type*}
    {q : SeminormFamily 𝕜₂ F ι'} [UniformSpace E] [UniformAddGroup E] [u : UniformSpace F]
    [hu : UniformAddGroup F] (hq : WithSeminorms q) [ContinuousSMul 𝕜 E]
    (f : κ → E →ₛₗ[σ₁₂] F) : TFAE
    [ EquicontinuousAt ((↑) ∘ f) 0,
      Equicontinuous ((↑) ∘ f),
      UniformEquicontinuous ((↑) ∘ f),
      ∀ i, ∃ p : Seminorm 𝕜 E, Continuous p ∧ ∀ k, (q i).comp (f k) ≤ p,
      ∀ i, BddAbove (range fun k ↦ (q i).comp (f k)) ∧ Continuous (⨆ k, (q i).comp (f k)) ] :=
  sorry
```

This theorem is useful, but also a bit long and takes time to parse (for humans).
As such, it should probably have a docstring, which lead to the
[following comment](https://github.com/leanprover-community/mathlib4/pull/5580/files#r1286511394)

```markdown
Can you please add a docstring explaining the statement of the theorem, as well as a cross reference to
`NormedSpace.equicontinuous_TFAE`?
```

The PR author then updated the theorem with the following informative docstring, and here we can
see tremendous added value:

```lean
/-- Let `E` and `F` be two topological vector spaces over a `NontriviallyNormedField`, and assume
that the topology of `F` is generated by some family of seminorms `q`. For a family `f` of linear
maps from `E` to `F`, the following are equivalent:
* `f` is equicontinuous at `0`.
* `f` is equicontinuous.
* `f` is uniformly equicontinuous.
* For each `q i`, the family of seminorms `k ↦ (q i) ∘ (f k)` is bounded by some continuous
  seminorm `p` on `E`.
* For each `q i`, the seminorm `⊔ k, (q i) ∘ (f k)` is well-defined and continuous.
In particular, if you can determine all continuous seminorms on `E`, that gives you a complete
characterization of equicontinuity for linear maps from `E` to `F`. For example `E` and `F` are
both normed spaces, you get `NormedSpace.equicontinuous_TFAE`. -/
```

#### Are there cross references to related declarations?

See the previous example, where a cross reference was requested for a related declaration.

#### Do complicated proofs have a sketch in comments interspersed throughout?

In this example, we just show an existing example of how interspersed comments can 
significantly add to the value of a proof in Lean. This is copied directly from the 
source for [Gromov_Hausdorff.GH_space.topological_space.second_countable_topology](https://leanprover-community.github.io/mathlib_docs/topology/metric_space/gromov_hausdorff.html#Gromov_Hausdorff.GH_space.topological_space.second_countable_topology).

Whenever a complicated proof isn't documented like this, please encourage the PR
author to do so. You can point them to this code. Another suitable and less complicated
example can be found in the source for
[banach_steinhaus](https://leanprover-community.github.io/mathlib_docs/analysis/normed_space/banach_steinhaus.html#banach_steinhaus).

```
/-- The Gromov-Hausdorff space is second countable. -/
instance : second_countable_topology GH_space :=
begin
  refine second_countable_of_countable_discretization (λ δ δpos, _),
  let ε := (2/5) * δ,
  have εpos : 0 < ε := mul_pos (by norm_num) δpos,
  have : ∀ p:GH_space, ∃ s : set p.rep, s.finite ∧ (univ ⊆ (⋃x∈s, ball x ε)) :=
    λ p, by simpa only [subset_univ, exists_true_left]
      using finite_cover_balls_of_compact is_compact_univ εpos,
  -- for each `p`, `s p` is a finite `ε`-dense subset of `p` (or rather the metric space
  -- `p.rep` representing `p`)
  choose s hs using this,
  have : ∀ p:GH_space, ∀ t:set p.rep, t.finite → ∃ n:ℕ, ∃ e:equiv t (fin n), true,
  { assume p t ht,
    letI : fintype t := finite.fintype ht,
    exact ⟨fintype.card t, fintype.equiv_fin t, trivial⟩ },
  choose N e hne using this,
  -- cardinality of the nice finite subset `s p` of `p.rep`, called `N p`
  let N := λ p:GH_space, N p (s p) (hs p).1,
  -- equiv from `s p`, a nice finite subset of `p.rep`, to `fin (N p)`, called `E p`
  let E := λ p:GH_space, e p (s p) (hs p).1,
  -- A function `F` associating to `p : GH_space` the data of all distances between points
  -- in the `ε`-dense set `s p`.
  let F : GH_space → Σn:ℕ, (fin n → fin n → ℤ) :=
    λp, ⟨N p, λa b, ⌊ε⁻¹ * dist ((E p).symm a) ((E p).symm b)⌋⟩,
  refine ⟨Σ n, fin n → fin n → ℤ, by apply_instance, F, λp q hpq, _⟩,
  /- As the target space of F is countable, it suffices to show that two points
  `p` and `q` with `F p = F q` are at distance `≤ δ`.
  For this, we construct a map `Φ` from `s p ⊆ p.rep` (representing `p`)
  to `q.rep` (representing `q`) which is almost an isometry on `s p`, and
  with image `s q`. For this, we compose the identification of `s p` with `fin (N p)`
  and the inverse of the identification of `s q` with `fin (N q)`. Together with
  the fact that `N p = N q`, this constructs `Ψ` between `s p` and `s q`, and then
  composing with the canonical inclusion we get `Φ`. -/
  have Npq : N p = N q := (sigma.mk.inj_iff.1 hpq).1,
  let Ψ : s p → s q := λ x, (E q).symm (fin.cast Npq ((E p) x)),
  let Φ : s p → q.rep := λ x, Ψ x,
  -- Use the almost isometry `Φ` to show that `p.rep` and `q.rep`
  -- are within controlled Gromov-Hausdorff distance.
  have main : GH_dist p.rep q.rep ≤ ε + ε/2 + ε,
  { refine GH_dist_le_of_approx_subsets Φ  _ _ _,
    show ∀ x : p.rep, ∃ (y : p.rep) (H : y ∈ s p), dist x y ≤ ε,
    { -- by construction, `s p` is `ε`-dense
      assume x,
      have : x ∈ ⋃y∈(s p), ball y ε := (hs p).2 (mem_univ _),
      rcases mem_Union₂.1 this with ⟨y, ys, hy⟩,
      exact ⟨y, ys, le_of_lt hy⟩ },
    show ∀ x : q.rep, ∃ (z : s p), dist x (Φ z) ≤ ε,
    { -- by construction, `s q` is `ε`-dense, and it is the range of `Φ`
      assume x,
      have : x ∈ ⋃y∈(s q), ball y ε := (hs q).2 (mem_univ _),
      rcases mem_Union₂.1 this with ⟨y, ys, hy⟩,
      let i : ℕ := E q ⟨y, ys⟩,
      let hi := ((E q) ⟨y, ys⟩).is_lt,
      have ihi_eq : (⟨i, hi⟩ : fin (N q)) = (E q) ⟨y, ys⟩, by rw [fin.ext_iff, fin.coe_mk],
      have hiq : i < N q := hi,
      have hip : i < N p, { rwa Npq.symm at hiq },
      let z := (E p).symm ⟨i, hip⟩,
      use z,
      have C1 : (E p) z = ⟨i, hip⟩ := (E p).apply_symm_apply ⟨i, hip⟩,
      have C2 : fin.cast Npq ⟨i, hip⟩ = ⟨i, hi⟩ := rfl,
      have C3 : (E q).symm ⟨i, hi⟩ = ⟨y, ys⟩,
      { rw ihi_eq, exact (E q).symm_apply_apply ⟨y, ys⟩ },
      have : Φ z = y,
      { simp only [Φ, Ψ], rw [C1, C2, C3], refl },
      rw this,
      exact le_of_lt hy },
    show ∀ x y : s p, |dist x y - dist (Φ x) (Φ y)| ≤ ε,
    { /- the distance between `x` and `y` is encoded in `F p`, and the distance between
      `Φ x` and `Φ y` (two points of `s q`) is encoded in `F q`, all this up to `ε`.
      As `F p = F q`, the distances are almost equal. -/
      assume x y,
      have : dist (Φ x) (Φ y) = dist (Ψ x) (Ψ y) := rfl,
      rw this,
      -- introduce `i`, that codes both `x` and `Φ x` in `fin (N p) = fin (N q)`
      let i : ℕ := E p x,
      have hip : i < N p := ((E p) x).2,
      have hiq : i < N q, by rwa Npq at hip,
      have i' : i = ((E q) (Ψ x)), by { simp only [equiv.apply_symm_apply, fin.coe_cast] },
      -- introduce `j`, that codes both `y` and `Φ y` in `fin (N p) = fin (N q)`
      let j : ℕ := E p y,
      have hjp : j < N p := ((E p) y).2,
      have hjq : j < N q, by rwa Npq at hjp,
      have j' : j = ((E q) (Ψ y)).1,
      { simp only [equiv.apply_symm_apply, fin.val_eq_coe, fin.coe_cast] },
      -- Express `dist x y` in terms of `F p`
      have : (F p).2 ((E p) x) ((E p) y) = floor (ε⁻¹ * dist x y),
        by simp only [F, (E p).symm_apply_apply],
      have Ap : (F p).2 ⟨i, hip⟩ ⟨j, hjp⟩ = floor (ε⁻¹ * dist x y),
        by { rw ← this, congr; apply fin.ext_iff.2; refl },
      -- Express `dist (Φ x) (Φ y)` in terms of `F q`
      have : (F q).2 ((E q) (Ψ x)) ((E q) (Ψ y)) = floor (ε⁻¹ * dist (Ψ x) (Ψ y)),
        by simp only [F, (E q).symm_apply_apply],
      have Aq : (F q).2 ⟨i, hiq⟩ ⟨j, hjq⟩ = floor (ε⁻¹ * dist (Ψ x) (Ψ y)),
        by { rw ← this, congr; apply fin.ext_iff.2; [exact i', exact j'] },
      -- use the equality between `F p` and `F q` to deduce that the distances have equal
      -- integer parts
      have : (F p).2 ⟨i, hip⟩ ⟨j, hjp⟩ = (F q).2 ⟨i, hiq⟩ ⟨j, hjq⟩,
      { -- we want to `subst hpq` where `hpq : F p = F q`, except that `subst` only works
        -- with a constant, so replace `F q` (and everything that depends on it) by a constant `f`
        -- then `subst`
        revert hiq hjq,
        change N q with (F q).1,
        generalize_hyp : F q = f at hpq ⊢,
        subst hpq,
        intros,
        refl },
      rw [Ap, Aq] at this,
      -- deduce that the distances coincide up to `ε`, by a straightforward computation
      -- that should be automated
      have I := calc
        |ε⁻¹| * |dist x y - dist (Ψ x) (Ψ y)| =
          |ε⁻¹ * (dist x y - dist (Ψ x) (Ψ y))| : (abs_mul _ _).symm
        ... = |(ε⁻¹ * dist x y) - (ε⁻¹ * dist (Ψ x) (Ψ y))| : by { congr, ring }
        ... ≤ 1 : le_of_lt (abs_sub_lt_one_of_floor_eq_floor this),
      calc
        |dist x y - dist (Ψ x) (Ψ y)| = (ε * ε⁻¹) * |dist x y - dist (Ψ x) (Ψ y)| :
          by rw [mul_inv_cancel (ne_of_gt εpos), one_mul]
        ... = ε * (|ε⁻¹| * |dist x y - dist (Ψ x) (Ψ y)|) :
          by rw [abs_of_nonneg (le_of_lt (inv_pos.2 εpos)), mul_assoc]
        ... ≤ ε * 1 : mul_le_mul_of_nonneg_left I (le_of_lt εpos)
        ... = ε : mul_one _ } },
  calc dist p q = GH_dist p.rep (q.rep) : dist_GH_dist p q
    ... ≤ ε + ε/2 + ε : main
    ... = δ : by { simp only [ε], ring }
end
```

#### Are there warnings to the user when code should only be used in certain ways?

Some declarations are only intended for use within a particular file, perhaps because they are auxiliary.
Others can be used anywhere, but should be use sparingly, and only when the preferred method is
unavailable or downside of using it is irrelevant.

##### Use in a particular file

An example of the former is:
[PiLp.iSup_edist_ne_top_aux](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/NormedSpace/PiLp.html#PiLp.iSup_edist_ne_top_aux)
which contains the following docstring.

```lean
/-- An auxiliary lemma used twice in the proof of `PiLp.pseudoMetricAux` below. Not intended for use outside this file. -/
```

This lemma signals to the reader both with its name (contains `aux`) and its docstring that it is not intended for
general purpose use. The reason for this is that the declaration immediately preceding it,
[PiLp.pseudoEmetricAux](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/NormedSpace/PiLp.html#PiLp.pseudoEmetricAux),
is an instance which is only activated temporarily to build the proper pseudo extended metric structure.
Its docstring also makes this clear:

```lean
/-- Endowing the space `PiLp p β` with the `L^p` pseudoemetric structure. This definition is not
satisfactory, as it does not register the fact that the topology and the uniform structure coincide
with the product one. Therefore, we do not register it as an instance. Using this as a temporary
pseudoemetric space instance, we will show that the uniform structure is equal (but not defeq) to
the product one, and then register an instance in which we replace the uniform structure by the
product one using this pseudoemetric space and `PseudoEMetricSpace.replaceUniformity`. -/
```

##### Conditions for use

An example of the latter is:
[completeLatticeOfSup](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Order/CompleteLattice.html#completeLatticeOfSup),
which contains the following docstring.

````lean
/-- Create a `CompleteLattice` from a `PartialOrder` and `SupSet`
that returns the least upper bound of a set. Usually this constructor provides
poor definitional equalities.  If other fields are known explicitly, they should be
provided; for example, if `inf` is known explicitly, construct the `CompleteLattice`
instance as
```
instance : CompleteLattice my_T :=
  { inf := better_inf,
    le_inf := ...,
    inf_le_right := ...,
    inf_le_left := ...
    -- don't care to fix sup, sInf, bot, top
    ..completeLatticeOfSup my_T _ }
```
-/
````

In this case, a `CompleteLattice` is constructed, but the data-carrying `sup`, `sInf`,
`bot` and `top` fields are defined in terms of `sSup`, and will therefore be 
inconvenient to prove things about when access to the definition is required. This 
docstring therefore serves as an important warning to the user that this constructor
should be used sparingly, and these data-carrying fields should be provided if they
are known explicitly.
    
#### Is it formalizing something from the literature?

Some objects in mathlib exist only to serve formalization (e.g., `AddMonoidWithOne`),
but most ideas formalized come directly from the mathematical literature. In such
cases, especially when the contributor is mimicking an existing published proof on 
paper, they should be encouraged to add an entry to the `references.bib` file and
cite it in the module documentation and / or the docstring of the relevant theorem.

In addition, having mathematics in mathlib that is connected to the literature is
an extra sanity check that what is being added is relevant, and that hopefully
someone will care about it and use it later. Incorporating mathematics into mathlib
places a burden to maintain what was added, and there's no reason to take on that 
burden if it won't ever be used.

### Location

#### Are the declarations in the appropriate files?

Consider the following example from [#5742](github.com/leanprover-community/mathlib4/pull/5742)
where the PR author was placing a norm structure on the `Unitization`. The author was
creating a new file `Analysis.NormedSpace.Unitization` and at a certain point declared the
instance:

```lean
instance Unitization.instNontrivial {𝕜 A} [Nontrivial 𝕜] [Nonempty A] :
    Nontrivial (Unitization 𝕜 A) :=
  nontrivial_prod_left
```

Notice that this instance has nothing to do with norms, and so it likely belongs in an
earlier file. A reviewer could use the `#find_home Unitization.instNontrivial` to determine
that the natural place to put this declaration is `Algebra.Algebra.Unitization`. A helpful
reviewer could comment:

```markdown
It seems like this instance doesn't have anything to do with the norm structure on the 
`Unitization`. Perhaps you could place this instance in `Algebra.Algebra.Unitization` instead.
```

#### Do the results already exist? possibly in a more general form with a different name? 

Mathlib is by now quite a large library, and it's difficult for anyone, especially new
users, to be familiar with all the different corners and exactly which results are 
available. This is exacerbated by the fact that we aspire for generality, and eschew
code duplication; this leads to the canonical questions by new users: "is mathlib really
missing vector spaces and group homomorphisms?", and its answer: "no, these are `Module`
and `MonoidHom`, respectively."

As a result, it is not uncommon for new contributors (or even experienced ones!) to 
create a PR for a result that already exists, sometimes verbatim, and other times in
greater generality.

The `apply?` and `exact?` tactics can help answer this sometimes. If you suspect a 
result already exists, just copy it to a new file with `import Mathlib` and try `exact?`.

#### Are new `import`s introduced? Do they import too much?

Maintaining the organization of the mathlib import hierarchy is an important task, 
but it can easily get out of hand without careful review. Generally, the problem occurs
in the following manner.

A contributor thinks: "I would like to add `my_theorem` and it's all about `Z`, so I'll
add it to `X.Y.Z`." Upon trying to add the theorem there, the contributor realizes: "oh,
I don't have access to `helper_lemma`, I need to `import A.B.C`." During review, the 
reviewer is focused on other things, and the PR is merged with this import change.
This is the story of how, at one time, `Analysis.NormedSpace.Star.Basic` imported 
`Analysis.NormedSpace.OperatorNorm`! This occurred in
[#16964](https://github.com/leanprover-community/mathlib/pull/16964)
and then had to be fixed in [#18194](https://github.com/leanprover-community/mathlib/pull/18194).

As another example, in [#6239](https://github.com/leanprover-community/mathlib4/pull/6239),
the contributor had added the import `Data.IsROrC.Basic` to
`LinearAlgebra.Matrix.DotProduct`. This is probably a hard thing for a new 
contributor to recognize, because it sometimes requires decent familiarity with the
way the library is organized.

Of course, reviewers should do their best to catch the most egregious examples
(e.g., importing `Analysis` files into `Algebra` files is generally rather suspect),
but asking the question is always warranted. It can often mean that the results belong
elsewhere, the file should be split along a natural boundary, or the new results should
go in a new a file.

#### Should a file be split into multiple pieces?

There are essentially three reasons to split a file:

1. It is simply too long to be nice to use.
   A good rule of thumb here is that it exceeds 1000 lines.
2. The file is sectioned into multiple pieces that are only loosely related.
3. To avoid import creep from the introduction of new results that are closely
   related to existing ones.

Let's say some results, about 500 lines worth, are added to an existing file which 
already contains 700 lines, and suppose further that the new material is closely 
related to some of the existing material in the file. A reviewer should be on the 
lookout for a natural boundaries where the file can be split into coherent pieces.

### Improvements

#### Splitting into supporting lemmas or definitions (especially for long proofs)?

Long standalone proofs are frequently an indication that there is a worthwhile
refactor lurking close at hand. Often new contributors are unaware of existing
lemmas in the library, or may not know how to split their theorem into more 
manageable chunks. In these cases, the reviewer has a few options including:
rolling up their sleeves and refactoring the result into multiple lemmas 
themselves in the form of a `suggestion` on GitHub; looking for a potential
refactor and mentioning it, as in "you might consider splitting out the 
argument on lines xx into its own lemma, which will simplify the proof"; or 
simply asking, "this proof seems rather long and unwieldy, have you considered
at all how it might be split into more manageable pieces?"; or even, "this 
proof seems like it might be easier if you make use of theorem X."

#### Different tactics to improve readability

A good example where using better tactics, or golfing, can *improve* readability
can be found in this suggestion from [#6140](https://github.com/leanprover-community/mathlib4/pull/6140/files/d2506ba26543b630722124dbf030339f43f6590a#r1287284988).
In this case, the original subsequence of tactics in the proof was:

```lean
  have h₀ : log b = log (- -b) := by simp
  rw [h₀, log_neg_eq_log]
  have hb' : 0 < -b := by linarith
  have h₁ : log (-b) < 0 := by rw [log_neg_iff hb']; linarith
  refine tendsto_exp_atBot.comp ?_
  rw [tendsto_const_mul_atBot_of_neg h₁]
  show atTop ≤ atTop
  rfl
```

and the suggestion was to golf it to:

```lean
  refine tendsto_exp_atBot.comp <| (tendsto_const_mul_atBot_of_neg ?_).mpr tendsto_id
  rw [←log_neg_eq_log, log_neg_iff (by linarith)]
  linarith
```

from the golfed version, we can easily see that this is essentially just composing some
library lemmas about `Filter.Tendsto`, along with a single hypothesis to one of these
theorems which is proven with some basic rewriting and calls to `linarith`.

An example where using a better tactic can improve readability can be found in the 
entire diff of [#4702](https://github.com/leanprover-community/mathlib4/pull/4702/files),
which golfed lemmas throughout the library using the new `gcongr` tactic.  We'll
highlight one particularly nice example for reference. The original code was:

```lean
  _ ≤ ε / 2 * ‖∑ i in range n, g i‖ + ε / 2 * ∑ i in range n, g i := by
    rw [← mul_sum]
    exact add_le_add hn (mul_le_mul_of_nonneg_left le_rfl (half_pos εpos).le)
```

which was improved using `gcongr` to:

```lean
  _ ≤ ε / 2 * ‖∑ i in range n, g i‖ + ε / 2 * ∑ i in range n, g i := by rw [← mul_sum]; gcongr
```

Or, from the same PR, this example which used `positivity` to go from:

```lean
  · have ha' := mul_le_mul_of_nonneg_left ha (inv_pos.2 hab).le
    rwa [MulZeroClass.mul_zero, ← div_eq_inv_mul] at ha'
  · have hb' := mul_le_mul_of_nonneg_left hb (inv_pos.2 hab).le
    rwa [MulZeroClass.mul_zero, ← div_eq_inv_mul] at hb'
```

to:

```lean
  · positivity
  · positivity
```

#### Does a different proof structure greatly simplify the argument?

A great example of this occurred in the review for
[#5602](https://github.com/leanprover-community/mathlib4/pull/5602/files/ea99653c047046bae3a109ee980314eec0bb9e81#r1282044795)
In this case, the PR author proved:

```lean
variable {R S A : Type*} [CommSemiring R] [Semiring A] [Algebra R A] [SetLike S A]
  [hSA : NonUnitalSubsemiringClass S A] [hSRA : SMulMemClass S R A] (s : S)

-- `NonUnitalSubalgebra.unitization s : Unitization R s →ₐ[R] Algebra.adjoin R (s : Set A)`
theorem NonUnitalSubalgebra.unitization_surjective :
    Function.Surjective (NonUnitalSubalgebra.unitization s) := by
  apply Algebra.adjoin_induction'
  · refine' fun x hx => ⟨(0, ⟨x, hx⟩), Subtype.ext _⟩
    simp only [NonUnitalSubalgebra.unitization_apply_coe, Subtype.coe_mk]
    change (algebraMap R { x // x ∈ Algebra.adjoin R (s : Set A) } 0 : A) + x = x
    rw [map_zero, Subsemiring.coe_zero, zero_add]
  · exact fun r => ⟨algebraMap R (Unitization R s) r, AlgHom.commutes _ r⟩
  · rintro _ _ ⟨x, rfl⟩ ⟨y, rfl⟩
    exact ⟨x + y, map_add _ _ _⟩
  · rintro _ _ ⟨x, rfl⟩ ⟨y, rfl⟩
    exact ⟨x * y, map_mul _ _ _⟩
```

The reviewer commented:

```markdown
I see why it's not immediate (you'd have to get back to the full codomain),
but is there really no good way of using `Algebra.adjoin_le` here?
```

which resulted in the vastly improved three-line proof:

```lean
theorem NonUnitalSubalgebra.unitization_surjective :
    Function.Surjective (NonUnitalSubalgebra.unitization s) := by
  have : Algebra.adjoin R s ≤ ((Algebra.adjoin R (s : Set A)).val.comp (unitization s)).range :=
    Algebra.adjoin_le fun a ha ↦ ⟨(⟨a, ha⟩ : s), by simp⟩
  fun x ↦ match this x.property with | ⟨y, hy⟩ => ⟨y, Subtype.ext hy⟩
```

In this case, appealing to the lemma `Algebra.adjoin_le` was a tremendous
simplification over using `Algebra.adjoin_induction'`.

#### Are the definitions introduced the best way to formalize the concept (very difficult!)?

This is incredibly hard to describe in general, but perhaps the simplest
rule of thumb that can be given is this: the more definitions avoid 
dependent types, the better.

As an example, consider the definition of [Vector](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Vector.html#Vector).
Many introductory expositions of dependent type theory define `Vector`
as an inductive type and give it as the canonical example of a dependent
type. While the dependent typing is unavoidable, mathlib's definition 
instead opts for a simple subtype of `List`, and the dependence on `ℕ`
appears only in `List.length` equality proposition. This has the 
advantage that we can easily pass out of the dependent type world by
coercing to `List` and then life is much easier. In fact, most operations
on `Vector` are precisely the corresponding operation on `List` combined
with an equality proof on the lengths.

### Library integration

Many of the questions here are a bit nebulous and generally require a large amount of
familiarity with the structure of mathlib, or at least significant prior expertise
in formalization. Don't be discouraged if you find it difficult to address these
questions when reviewing.

#### Does it provide a sensible API?

- Are attributes added appropriately (e.g., `@[simp]`, `@[ext]`, `@[gcongr]`, `@[aesop]`, etc.)?
- Are rewrite lemmas provided to avoid the need to pass through equalities definitionally all the time?
- Does a new type provide convenient constructors in common use cases?

#### Is it general enough to support known future needs?

This requires knowing what some of the future needs may be! Being active on Zulip
can help make a reviewer aware of these needs. However, one may use a proxy for this question, 
namely, "is there a more general version of this result in the literature which invokes pre-existing
concepts in mathlib?" If there is, perhaps the existing PR should be generalized.

#### Does it fit the design and collective vision of mathlib?

Again, this is a vague question and requires knowing what the design and collective vision are!
However, as some practical examples:

- If a user is adding a new kind of morphism (not in the category theory library), they should 
  more likely than not be defining a bundled morphism type, and probably an associated morphism
  class using the `FunLike` API.
- Similarly, if a contributor is adding a new subobject, they should probably be using bundled
  subobjects and making use of the `SetLike` API. For reference, see the [relevant section 
  in Mathematics in Lean](https://leanprover-community.github.io/mathematics_in_lean/C07_Hierarchies.html#sub-objects).
- Follow the advice of any existing library note.
