# Maths in Lean: linear algebra

### Semimodules, Modules and Vector Spaces

#### [`Mathlib.Algebra.Module.Defs`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Module/Defs.html)

This file defines the typeclass `Module R M`, which gives an `R`-module structure on the type `M`.
An additive commutative monoid `M` is a module over the (semi)ring `R` if there is a scalar multiplication `•` (`SMul`) that satisfies the expected distributivity axioms for `+` (in `M` and `R`) and `*` (in `R`).
To define a `Module R M` instance, you first need instances for `Semiring R` and `AddCommMonoid M`.
By splitting out these dependencies, we avoid instance loops and diamonds.

In general mathematical usage, a module over a semiring is also called a semimodule, and a module over a field is also called a vector space.
We do not have separate `Semimodule` or `VectorSpace` typeclasses because those requirements are more easily expressed by changing the typeclass instances on `R` (and `M`).
In this document, we'll use "module" as the general term for "semimodule, module or vector space" and "ring" as the general term for "(commutative) semiring, ring or field".

Let `m` be an arbitrary type, e.g. `Fin n`, then the typical examples are:
`m → ℕ` is an `ℕ`-semimodule, `m → ℤ` is a `ℤ`-module and `m → ℚ` is a `ℚ`-vector space
(outside of type theory, these are known as `ℕ^m`, `ℤ^m` and `ℚ^m` respectively).
A ring is a module over itself, with `•` defined as `*` (this equality is stated by the `simp` lemma [`smul_eq_mul`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Group/Action/Defs.html#smul_eq_mul)).
Each additive monoid has a canonical `ℕ`-module structure given by `n • x = x + x + ... + x` (`n` times), and each additive group has a canonical `ℤ`-module structure defined similarly; these also apply for (semi)rings.

The file [`Mathlib.LinearAlgebra.LinearIndependent`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/LinearIndependent.html) defines linear independence for an indexed family in a module.
To express that a set `s : Set M` is linear independent, we view it as a family indexed by itself, written as `LinearIndependent R ((↑)  : s → M)`.

The file [`Mathlib.LinearAlgebra.Basis`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Basis.html) defines bases for modules.

The file [`Mathlib.LinearAlgebra.Dimension.Basic`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Dimension/Basic.html) defines the `rank` of a module as a cardinal.
We also use `rank` for the dimension of a vector space, since the dimension is always equal to the rank.
The `rank` of a linear map is defined as the dimension of its image.
Most definitions in this file are non-computable.

The file [`Mathlib.LinearAlgebra.Dimension.Finrank`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Dimension/Finrank.html) defines the `finrank` of a module as a natural number.
By convention, the `finrank` is equal to 0 if the rank is infinite.

### Matrices

#### [`Mathlib.Data.Matrix.Basic`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Matrix/Basic.html)

The type `Matrix m n α` contains rectangular, `m` by `n` arrays of elements of the type `α`.
It is an alias for the type `m → n → α`. A matrix type can be indexed over arbitrary types.
For example, the adjacency matrix of a graph could be indexed over the nodes in that graph.
If you want to specify the dimensions of a matrix as natural numbers `m n : ℕ`, you can use `Fin m` and `Fin n` as index types.

A matrix is constructed by giving the map from indices to entries: `(fun (i : m) (j : n) ↦ (_ : α)) : Matrix m n α`.
However, it is not advisable to construct matrices using terms of the form `fun i j ↦ _` or even `(fun i j ↦ _ : Matrix m n α)`,
as these are not recognized by Lean as having the right type. Instead, `Matrix.of` should be used.
For matrices indexed by natural numbers, you can also use the notation defined in [`Mathlib.Data.Matrix.Notation`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Data/Matrix/Notation.html): `![![a, b, c], ![b, c, d]] : Matrix (Fin 2) (Fin 3) α`.
To get an entry of the matrix `M : Matrix m n α` at row `i : m` and column `j : n`,
you can apply `M` to the indices: `M i j : α`.
Lemmas about the entries of a matrix typically end in `_apply`: `Matrix.add_apply M N i j : (M + N) i j = M i j + N i j`.

Matrix multiplication and transpose have notation that is made available by the command `open scoped Matrix`.
Multiplication of matrices is denoted using `*` as usual. The infix operator `⬝ᵥ` stands for `Matrix.dotProduct`,
and a postfix operator `ᵀ` stands for `Matrix.transpose`.

When working with matrices, a *vector* means a function `m → α` for an arbitrary `Fintype` `m`.
These have a module (or vector space) structure defined in [`algebra.module.pi`](https://leanprover-community.github.io/mathlib_docs/algebra/module/pi.html)
consisting of pointwise addition and multiplication.
The distinction between row and column vectors is only made by the choice of function.
For example, `Matrix.mulVec M v` (denoted `M *ᵥ v`) multiplies a matrix with a column vector `v : m → α` and `Matrix.Vecmul v M`
(denoted `v ᵥ* M`) multiplies a row vector `v : m → α` with a matrix.
If you use `mulVec` and `Vecmul` a lot, you might want to consider using a linear map instead (see below).

Permutation matrices are defined in [`Mathlib.LinearAlgebra.Matrix.Permutation`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/Permutation.html).

The determinant of a matrix is defined in [`Mathlib.LinearAlgebra.Matrix.Determinant.Basic`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/Determinant/Basic.html).

The adjugate and for nonsingular matrices, the inverse are defined in [`Mathlib.LinearAlgebra.Matrix.Adjugate`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/Adjugate.html) and [`Mathlib.LinearAlgebra.Matrix.NonsingularInverse`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/NonsingularInverse.html).

The type `Matrix.SpecialLinearGroup m R` is the group of `m` by `m` matrices with determinant `1`,
and is defined in [`Mathlib.LinearAlgebra.Matrix.SpecialLinearGroup`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/SpecialLinearGroup.html).

### Linear Maps and Equivalences

#### [`Mathlib.Algebra.Module.LinearMap.Defs`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Module/LinearMap/Defs.html)

The type `M →[R]ₗ M₂`, or `LinearMap R M M₂`, represents `R`-linear maps from the `R`-module `M` to the `R`-module `M₂`.
These are defined by their action on elements of `M`.
The type `M ≃[R]ₗ M₂`, or `LinearEquiv R M M₂`, is the type of invertible `R`-linear maps from `M` to `M₂`.

The equivalence between matrices and linear maps is formalized in [`Matrix.toLin`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/ToLin.html#Matrix.toLin).
[`Matrix.toLin'`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/ToLin.html#Matrix.toLin') shows that `Matrix.mulVec` is a linear equivalence between `Matrix m n R` and `(n → R) →[R]ₗ (m → R)`.
In addition, [`LinearMap.toMatrix`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/ToLin.html#LinearMap.toMatrix) takes a basis `ι` for `M₁` and `κ` for `M₂`
and gives the equivalence between `R`-linear maps between `M₁` and `M₂` and `Matrix ι κ R`.
If you have an explicit basis for your maps, this equivalence allows you to do calculations such as getting the determinant.

The difference between matrices and linear maps is that matrices are in their essence an array of entries
(which incidentally allows actions such as `Matrix.mulVec`),
while linear maps are in their essence an action on vectors
(which incidentally can be represented by a matrix if we have a finite basis).
If you want to do computations, a matrix is a better choice.
If you want to do proofs without computations, a linear map is a better choice.

The type [`Matrix.GeneralLinearGroup R M`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/GeneralLinearGroup/Defs.html#Matrix.GeneralLinearGroup) is the group of invertible `R`-linear maps from `M` to itself.
`LinearMap.GeneralLinearGroup.generalLinearEquiv R M` is the equivalence between `GeneralLinearGroup ` and `M ≃[R]ₗ M`.
`Matrix.SpecialLinearGroup.toGL` is the embedding from the special linear group (of matrices) to the general linear group (of linear maps).

The dual space, consisting of linear maps `M →[R]ₗ R`, is defined in [`Mathlib.LinearAlgebra.Dual`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Dual.html).

### Bilinear, Sesquilinear and Quadratic Forms

#### [`Mathlib.LinearAlgebra.BilinearMap`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/BilinearMap.html)

For an `R`-module `M`, the type `LinearMap.BilinForm R M` is the type of maps `M → M → R` that are linear in both arguments.
The equivalence between `LinearMap.BilinForm R M` and maps `M →ₗ[R] M →ₗ[R] R` that are linear in both arguments is called `bilin_linear_map_equiv`.
A matrix `M` corresponds to a bilinear form that maps vectors `v` and `w` to `row v ⬝ M ⬝ col w`.
The equivalence between `BilinForm R (n → R)` and `Matrix n n R` is called [`BilinForm.toMatrix`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/Matrix/BilinearForm.html#BilinForm.toMatrix).

#### [`Mathlib.LinearAlgebra.SesquilinearForm`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/SesquilinearForm.html)

For an `R`-module `M` and `I : R →+* R`, the type `M →ₗ M →ₛₗ[I] R` is the type of maps `M → M → R` that are linear in the first argument
and that in the second argument are `I`-[semilinear](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Algebra/Module/LinearMap/Defs.html#LinearMap).
Semilinearity of `f` with respect to a ring homomorphism `I` means the following equation hold: `f x (a • y) = I a * f x y`.

#### [`Mathlib.LinearAlgebra.QuadraticForm.Basic`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/QuadraticForm/Basic.html)

For an `R`-module `M`, the type `QuadraticForm R M` is the type of maps `f : M → R` such that `f (a • x) = a * a * f x` and `fun x y ↦ f (x + y) - f x - f y` is a bilinear map.

Up to a factor `2`, the theory of quadratic and bilinear forms is equivalent.
[`LinearMap.BilinMap.toQuadraticMap f`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/QuadraticForm/Basic.html#LinearMap.BilinMap.toQuadraticMap) is the quadratic form given by `fun x ↦ f x x`.
[`QuadraticMap.associatedHom f`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/QuadraticForm/Basic.html#QuadraticMap.associatedHom) is the bilinear form given by `fun x y ↦ ⅟2 * (f (x + y) - f x - f y)` (if there is a multiplicative inverse of `2`).
[`QuadraticMap.toMatrix'`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/QuadraticForm/Basic.html#QuadraticMap.toMatrix') and [`Matrix.toQuadraticMap'`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/QuadraticForm/Basic.html#Matrix.toQuadraticMap') are the maps between quadratic forms and matrices.
