# Maths in lean : linear algebra

### semimodules, modules and vector spaces ###

#### algebra.module ####

This file defines the typeclass `semimodule R M`, which gives an `R`-semimodule structure on the type `M`, and similarly `module R M` and `vector_space R M`.
An additive commutative monoid `M` is a semimodule over the semiring `R` if there is a scalar multiplication `•` (`has_scalar.smul`) that satisfies the expected distributivity axioms for `+` (in `M` and `R`) and `*` (in `R`).
A module (typeclass `module`) is a semimodule that additionally requires that `R` is a ring and `M` is a group.
A vector space (typeclass `vector_space`) is a module that additionally requires that `R` is a field.
All vector spaces are also modules, and all modules are also semimodules.

Typical examples are that `m → ℕ` is an `ℕ`-semimodule, `m → ℤ` is a `ℤ`-module and `m → ℚ` is a `ℚ`-vector space
(outside of type theory, these are known as `ℕ^m`, `ℤ^m` and `ℚ^m` respectively).
These instances are defined in `algebra.pi_instances`.
A (semi)ring is a (semi)module over itself, with `•` defined as `*` (`smul_eq_mul`).

The file `linear_algebra.basis` defines linear independence and bases for modules.

The file `linear_algebra.dimension` defines the dimension of a vector space as the minimum cardinality of a basis.
Tre rank of a linear map is defined as the dimension of its image.
Most definitions in this file are non-computable.

### matrices ###

#### data.matrix.basic ###
The type `matrix m n α` contains rectangular, `m` by `n` arrays of elements of the type `α`.
It is an alias for the type `m → n → α`, under the assumptions `[fintype m] [fintype n]` stating that `m` and `n` have finitely many elements.
A matrix type can be indexed over arbitrary `fintype`s.
For example, the adjacency matrix of a graph could be indexed over the nodes in that graph.
If you want to specify the dimensions of a matrix as natural numbers `m n : ℕ`, you can use `fin m` and `fin n` as index types.

A matrix is constructed by giving the map from indices to entries: `(λ (i : m) (j : n), (_ : α)) : matrix m n α`.
For matrices indexed by natural numbers, you can also use the notation defined in `data.matrix.notation`: `![![a, b, c], ![b, c, d]] : matrix (fin 2) (fin 3) α`.
To get an entry of the matrix `M : matrix m n α` at row `i : m` and column `j : n`,
you can apply `M` to the indices: `M i j : α`.
Lemmas about the entries of a matrix typically end in `_val`: `add_val M N i j : (M + N) i j = M i j + N i j`.

Matrix multiplication and transpose have notation that is made available by the command `open_locale matrix`.

When working with matrices, a *vector* means a function `m → α` for an arbitrary `fintype` `m`.
These have a module (or vector space) structure defined in `algebra.pi_instances`
consisting of pointwise addition and multiplication.
The distinction between row and column vectors is only made by the choice of function.
For example, `mul_vec M v` multiplies a matrix with a column vector `v : m → α` and `vec_mul v M` multiplies a row vector `v : m → α` with a matrix.

Permutation matrices are defined in `data.matrix.pequiv`.

The determinant of a matrix is defined in `linear_algebra.determinant`.

The adjugate and for nonsingular matrices, the inverse is defined in `linear_algebra.nonsingular_inverse`.

The type `special_linear_group m R` is the group of `m` by `m` matrices with determinant `1`,
and is defined in `linear_algebra.special_linear_group`.

### linear maps and equivalences ###

#### linear_algebra.basic ####

The type `M →[R]ₗ M₂`, or `linear_map R M M₂`, represents `R`-linear maps from the `R`-module `M` to `M₂`.
These are defined by their action on elements of `M`.
The type `M ≃[R]ₗ M₂`, or `linear_equiv R M M₂`, is the type of invertible `R`-linear maps from `M` to `M₂`.

The equivalence between matrices and linear maps is formalised in `linear_algebra.matrix`.
`linear_equiv_matrix'` shows that `matrix.mul_vec` is a linear equivalence between `matrix m n R` and `(n → R) →[R]ₗ (m → R)`.
The difference between matrices and linear maps is that matrices are in their essence an array of entries
(which incidentally allows actions such as `matrix.mul_vec`),
while linear maps are in their essence an action on vectors
(which incidentally can be represented by a matrix if we have a finite basis).
If you want to do computations, a matrix is a better choice.
If you want to do proofs without computations, a linear map is a better choice.

The type `general_linear_group R M` is the group of invertible `R`-linear maps from `M` to itself.
`general_linear_equiv R M` is the equivalence between `general_linear_group` and `M ≃[R]ₗ M`.
`special_linear_group.to_GL` is the embedding from the special linear group (of matrices) to the general linear group (of linear maps).

The file `linear_algebra.matrix` connects matrices with linear maps.
`linear_equiv_matrix'` shows that `matrix.mul_vec` is a linear equivalence between `matrix m n R` and `(n → R) →[R]ₗ (m → R)`.
In addition, `linear_equiv_matrix` takes a basis `ι` for `M₁` and `κ` for `M₂`
and gives the equivalence between `R`-linear maps between `M₁` and `M₂` and `matrix ι κ R`.
If you have an explicit basis for your maps, this equivalence allows you to do calculations such as getting the determinant.

The dual space, consisting of linear maps `M →[R]ₗ R`, is defined in `linear_algebra.dual`.

### bilinear, sesquilinear and quadratic forms ###

#### linear_algebra.bilinear_form ####

For an `R`-module `M`, the type `bilin_form R M` is the type of maps `M → M → R` that are linear in both arguments.
The equivalence between `bilin_form R M` and maps `M →ₗ[R] M →ₗ[R] R` that are linear in both arguments is called `bilin_linear_map_equiv`.
A matrix `M` corresponds to a bilinear form that maps vectors `v` and `w` to `row v ⬝ M ⬝ col w`.
The equivalence between `bilin_form R (n → R)` and `matrix n n R` is called `bilin_form_equiv_matrix`.

#### linear_algebra.sesquilinear_form ####

For an `R`-module `M`, the type `sesq_form R M` is the type of maps `M → M → R` that are linear in the first argument and antilinear in the second.
Antilinearity for `f : sesq M R` means there is an `I : R → R` such that `f x (a • y) = I a * f x y`, `I (x + y) = I x + I y` and `I (x * y) = I y * I x`.

#### linear_algebra.quadratic_form ####

For an `R`-module `M`, the type `quadratic_form R M` is the type of maps `f : M → R` such that `f (a • x) = a * a * f x` and `λ x y, f (x + y) - f x - f y` is a bilinear map.

Up to a factor `2`, the theory of quadratic and bilinear forms is equivalent.
`bilin_form.to_quadratic_form f` is the quadratic form given by `λ x, f x x`.
`quadratic_form.associated f` is the bilinear form given by `λ x y, ⅟2 * (f (x + y) - f x - f y)` (if there is a multiplicative inverse of `2`).
`quadratic_form.to_matrix` and `matrix.to_quadratic_form` are the maps between quadratic forms and matrices.
