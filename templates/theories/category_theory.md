# Maths in Lean: category theory

The `Category` typeclass is defined in [`Mathlib.CategoryTheory.Category.Basic`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Category/Basic.html).
It depends on the type of the objects, so for example we might write `Category (Type u)` if we're talking about a category whose objects are types (in universe `u`).

Functors (which are a structure, not a typeclass) are defined in [`Mathlib.CategoryTheory.Functor.Basic`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Functor/Basic.html),
along with identity functors and functor composition.

Natural transformations, and their compositions, are defined in [`Mathlib.CategoryTheory.NatTrans`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/NatTrans.html).

The category of functors and natural transformations between fixed categories `C` and `D`
is defined in [`Mathlib.CategoryTheory.Functor.Category`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Functor/Category.html).

Cartesian products of categories, functors, and natural transformations appear in
[`Mathlib.CategoryTheory.Products.Basic`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Products/Basic.html).

The category of types, and the hom pairing functor, are defined in [`Mathlib.CategoryTheory.Types`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/CategoryTheory/Types.html).

## Notation

### Categories

We use the `⟶` (`\hom`) arrow to denote sets of morphisms, as in `X ⟶ Y`.
This leaves the actual category implicit; it is inferred from the type of `X` and `Y` by typeclass inference.

We use `𝟙` (`\b1`) to denote identity morphisms, as in `𝟙 X`.

We use `≫` (`\gg`) to denote composition of morphisms, as in `f ≫ g`, which means "`f` followed by `g`".
You may prefer write composition in the usual convention, using `⊚` (`\oo` or `\circledcirc`), as in `f ⊚ g` which means "`g` followed by `f`". To do so you'll need to add this notation locally, via

```lean
local notation f ` ⊚ `:80 g:80 := category.comp g f
```

### Isomorphisms

We use `≅` for isomorphisms.

### Functors

We use `⥤` (`\func`) to denote functors, as in `C ⥤ D` for the type of functors from `C` to `D`.

We use `F.obj X` to denote the action of a functor on an object.
We use `F.map f` to denote the action of a functor on a morphism`.

Functor composition can be written as `F ⋙ G`.

### Natural transformations

We use `τ.app X` for the components of a natural transformation.

Otherwise, we mostly use the notation for morphisms in any category:

We use `F ⟶ G` (`\hom` or `-->`) to denote the type of natural transformations, between functors
`F` and `G`.
We use `F ≅ G` (`\iso`) to denote the type of natural isomorphisms.

For vertical composition of natural transformations we just use `≫`. For horizontal composition,
use `hcomp`.
