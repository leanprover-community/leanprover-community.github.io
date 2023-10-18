<div class="alert alert-info">
<p>
We are currently updating the Lean community website to describe working with Lean 4,
but most of the information you will find here today still describes Lean 3.
</p>
<p>
Pull requests updating this page for Lean 4 are very welcome.
There is a link at the bottom of this page.
</p>
<p>
Please visit <a href="https://leanprover.zulipchat.com">the leanprover zulip</a>
and ask for whatever help you need during this transitional period!
</p>
<p>
The website for Lean 3 has been <a href="https://leanprover-community.github.io/lean3/">archived</a>.
If you need to link to Lean 3 specific resources please link there.
</p>
</div>

# Maths in Lean: linear algebra

### Semimodules, Modules and Vector Spaces

#### [`algebra.module`](https://leanprover-community.github.io/mathlib_docs/algebra/module/basic.html)

This file defines the typeclass `module R M`, which gives an `R`-module structure on the type `M`.
An additive commutative monoid `M` is a module over the (semi)ring `R` if there is a scalar multiplication `•` (`has_scalar.smul`) that satisfies the expected distributivity axioms for `+` (in `M` and `R`) and `*` (in `R`).
To define a `module R M` instance, you first need instances for `semiring R` and `add_comm_monoid M`.
By splitting out these dependencies, we avoid instance loops and diamonds.

In general mathematical usage, a module over a semiring is also called a semimodule, and a module over a field is also called a vector space.
We do not have separate `semimodule` or `vector_space` typeclasses because those requirements are more easily expressed by changing the typeclass instances on `R` (and `M`).
In this document, we'll use "module" as the general term for "semimodule, module or vector space" and "ring" as the general term for "(commutative) semiring, ring or field".

Let `m` be an arbitrary type, e.g. `fin n`, then the typical examples are:
`m → ℕ` is an `ℕ`-semimodule, `m → ℤ` is a `ℤ`-module and `m → ℚ` is a `ℚ`-vector space
(outside of type theory, these are known as `ℕ^m`, `ℤ^m` and `ℚ^m` respectively).
A ring is a module over itself, with `•` defined as `*` (this equality is stated by the `simp` lemma [`smul_eq_mul`](https://leanprover-community.github.io/mathlib_docs/group_theory/group_action/defs.html#smul_eq_mul)).
Each additive monoid has a canonical `ℕ`-module structure given by `n • x = x + x + ... + x` (`n` times), and each additive group has a canonical `ℤ`-module structure defined similarly; these also apply for (semi)rings.

The file [`linear_algebra.linear_independent`](https://leanprover-community.github.io/mathlib_docs/linear_algebra/linear_independent.html) defines linear independence for an indexed family in a module.
To express that a set `s : set M` is linear independent, we view it as a family indexed by itself, written as `linear_independent R (coe : s → M)`.

The file [`linear_algebra.basis`](https://leanprover-community.github.io/mathlib_docs/linear_algebra/basis.html) defines bases for modules.

The file [`linear_algebra.dimension`](https://leanprover-community.github.io/mathlib_docs/linear_algebra/dimension.html) defines the `rank` of a module as a cardinal.
We also use `rank` for the dimension of a vector space, since the dimension is always equal to the rank.
(In fact, `rank` is currently only defined for vector spaces, as the cardinality of a basis. A definition of rank for all modules still needs to be done.)
The `rank` of a linear map is defined as the dimension of its image.
Most definitions in this file are non-computable.

The file [`linear_algebra.finite_dimensional`](https://leanprover-community.github.io/mathlib_docs/linear_algebra/finite_dimensional.html) defines the `finrank` of a module as a natural number.
By convention, the `finrank` is equal to 0 if the rank is infinite.

### Matrices

#### [`data.matrix.basic`](https://leanprover-community.github.io/mathlib_docs/data/matrix/basic.html)

The type `matrix m n α` contains rectangular, `m` by `n` arrays of elements of the type `α`.
It is an alias for the type `m → n → α`, under the assumptions `[fintype m] [fintype n]` stating that `m` and `n` have finitely many elements.
A matrix type can be indexed over arbitrary `fintype`s.
For example, the adjacency matrix of a graph could be indexed over the nodes in that graph.
If you want to specify the dimensions of a matrix as natural numbers `m n : ℕ`, you can use `fin m` and `fin n` as index types.

A matrix is constructed by giving the map from indices to entries: `(λ (i : m) (j : n), (_ : α)) : matrix m n α`.
For matrices indexed by natural numbers, you can also use the notation defined in [`data.matrix.notation`](https://leanprover-community.github.io/mathlib_docs/data/matrix/notation.html): `![![a, b, c], ![b, c, d]] : matrix (fin 2) (fin 3) α`.
To get an entry of the matrix `M : matrix m n α` at row `i : m` and column `j : n`,
you can apply `M` to the indices: `M i j : α`.
Lemmas about the entries of a matrix typically end in `_val`: `add_val M N i j : (M + N) i j = M i j + N i j`.

Matrix multiplication and transpose have notation that is made available by the command `open_locale matrix`.
The infix operator `⬝` stands for `matrix.mul`,
and a postfix operator `ᵀ` stands for `matrix.transpose`.

When working with matrices, a *vector* means a function `m → α` for an arbitrary `fintype` `m`.
These have a module (or vector space) structure defined in [`algebra.module.pi`](https://leanprover-community.github.io/mathlib_docs/algebra/module/pi.html)
consisting of pointwise addition and multiplication.
The distinction between row and column vectors is only made by the choice of function.
For example, `mul_vec M v` multiplies a matrix with a column vector `v : m → α` and `vec_mul v M` multiplies a row vector `v : m → α` with a matrix.
If you use `mul_vec` and `vec_mul` a lot, you might want to consider using a linear map instead (see below).

Permutation matrices are defined in [`data.matrix.pequiv`](https://leanprover-community.github.io/mathlib_docs/data/matrix/pequiv.html).

The determinant of a matrix is defined in [`linear_algebra.determinant`](https://leanprover-community.github.io/mathlib_docs/linear_algebra/determinant.html).

The adjugate and for nonsingular matrices, the inverse is defined in [`linear_algebra.matrix.nonsingular_inverse`](https://leanprover-community.github.io/mathlib_docs/linear_algebra/matrix/nonsingular_inverse.html).

The type `special_linear_group m R` is the group of `m` by `m` matrices with determinant `1`,
and is defined in [`linear_algebra.special_linear_group`](https://leanprover-community.github.io/mathlib_docs/linear_algebra/special_linear_group.html).

### Linear Maps and Equivalences

#### [`algebra.module.linear_map`](https://leanprover-community.github.io/mathlib_docs/algebra/module/linear_map.html)

The type `M →[R]ₗ M₂`, or `linear_map R M M₂`, represents `R`-linear maps from the `R`-module `M` to the `R`-module `M₂`.
These are defined by their action on elements of `M`.
The type `M ≃[R]ₗ M₂`, or `linear_equiv R M M₂`, is the type of invertible `R`-linear maps from `M` to `M₂`.

The equivalence between matrices and linear maps is formalised in [`linear_algebra.matrix.to_lin`](https://leanprover-community.github.io/mathlib_docs/linear_algebra/matrix/to_lin.html).
[`to_lin`](https://leanprover-community.github.io/mathlib_docs/linear_algebra/matrix/to_lin.html#matrix.to_lin) shows that `matrix.mul_vec` is a linear equivalence between `matrix m n R` and `(n → R) →[R]ₗ (m → R)`.
In addition, `linear_map.to_matrix` takes a basis `ι` for `M₁` and `κ` for `M₂`
and gives the equivalence between `R`-linear maps between `M₁` and `M₂` and `matrix ι κ R`.
If you have an explicit basis for your maps, this equivalence allows you to do calculations such as getting the determinant.

The difference between matrices and linear maps is that matrices are in their essence an array of entries
(which incidentally allows actions such as `matrix.mul_vec`),
while linear maps are in their essence an action on vectors
(which incidentally can be represented by a matrix if we have a finite basis).
If you want to do computations, a matrix is a better choice.
If you want to do proofs without computations, a linear map is a better choice.

The type [`general_linear_group R M`](https://leanprover-community.github.io/mathlib_docs/linear_algebra/basic.html#linear_map.general_linear_group) is the group of invertible `R`-linear maps from `M` to itself.
`general_linear_equiv R M` is the equivalence between `general_linear_group` and `M ≃[R]ₗ M`.
`special_linear_group.to_GL` is the embedding from the special linear group (of matrices) to the general linear group (of linear maps).

The dual space, consisting of linear maps `M →[R]ₗ R`, is defined in [`linear_algebra.dual`](https://leanprover-community.github.io/mathlib_docs/linear_algebra/dual.html).

### Bilinear, Sesquilinear and Quadratic Forms

#### [`linear_algebra.bilinear_form`](https://leanprover-community.github.io/mathlib_docs/linear_algebra/bilinear_form.html)

For an `R`-module `M`, the type `bilin_form R M` is the type of maps `M → M → R` that are linear in both arguments.
The equivalence between `bilin_form R M` and maps `M →ₗ[R] M →ₗ[R] R` that are linear in both arguments is called `bilin_linear_map_equiv`.
A matrix `M` corresponds to a bilinear form that maps vectors `v` and `w` to `row v ⬝ M ⬝ col w`.
The equivalence between `bilin_form R (n → R)` and `matrix n n R` is called [`bilin_form_equiv_matrix`](https://leanprover-community.github.io/mathlib_docs/linear_algebra/bilinear_form.html#bilin_form_equiv_matrix).

#### [`linear_algebra.sesquilinear_form`](https://leanprover-community.github.io/mathlib_docs/linear_algebra/sesquilinear_form.html)

For an `R`-module `M` and `I : R →+* R`, the type `M →ₗ M →ₛₗ[I] R` is the type of maps `M → M → R` that are linear in the first argument
and that in the second argument are `I`-[semilinear](https://leanprover-community.github.io/mathlib_docs/algebra/module/linear_map.html#linear_map).
Semilinearity of `f` with respect to a ring homomorphism `I` means the following equation hold: `f x (a • y) = I a * f x y`.

#### [`linear_algebra.quadratic_form`](https://leanprover-community.github.io/mathlib_docs/linear_algebra/quadratic_form/basic.html)

For an `R`-module `M`, the type `quadratic_form R M` is the type of maps `f : M → R` such that `f (a • x) = a * a * f x` and `λ x y, f (x + y) - f x - f y` is a bilinear map.

Up to a factor `2`, the theory of quadratic and bilinear forms is equivalent.
[`bilin_form.to_quadratic_form f`](https://leanprover-community.github.io/mathlib_docs/linear_algebra/quadratic_form/basic.html#bilin_form.to_quadratic_form) is the quadratic form given by `λ x, f x x`.
[`quadratic_form.associated f`](https://leanprover-community.github.io/mathlib_docs/linear_algebra/quadratic_form.html#quadratic_form.associated) is the bilinear form given by `λ x y, ⅟2 * (f (x + y) - f x - f y)` (if there is a multiplicative inverse of `2`).
[`quadratic_form.to_matrix`](https://leanprover-community.github.io/mathlib_docs/linear_algebra/quadratic_form.html#quadratic_form.to_matrix) and [`matrix.to_quadratic_form`](https://leanprover-community.github.io/mathlib_docs/linear_algebra/quadratic_form.html#matrix.to_quadratic_form) are the maps between quadratic forms and matrices.
