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

# Maths in Lean: category theory

The `category` typeclass is defined in [category_theory/category/basic.lean](https://leanprover-community.github.io/mathlib_docs/category_theory/category/basic.html).
It depends on the type of the objects, so for example we might write `category (Type u)` if we're talking about a category whose objects are types (in universe `u`).

Functors (which are a structure, not a typeclass) are defined in [category_theory/functor/basic.lean](https://leanprover-community.github.io/mathlib_docs/category_theory/functor/basic.html),
along with identity functors and functor composition.

Natural transformations, and their compositions, are defined in [category_theory/natural_transformation.lean](https://leanprover-community.github.io/mathlib_docs/category_theory/natural_transformation.html).

The category of functors and natural transformations between fixed categories `C` and `D`
is defined in [category_theory/functor/category.lean](https://leanprover-community.github.io/mathlib_docs/category_theory/functor/category.html).

Cartesian products of categories, functors, and natural transformations appear in
[category_theory/products/basic.lean](https://leanprover-community.github.io/mathlib_docs/category_theory/products/basic.html). (Product in the sense of limits will appear elsewhere soon!)

The category of types, and the hom pairing functor, are defined in [category_theory/types.lean](https://leanprover-community.github.io/mathlib_docs/category_theory/types.html).

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
(Unfortunately `⇒` is reserved in [`logic.relator`](https://github.com/leanprover-community/mathlib/blob/master/src/logic/relator.lean), so we can't use that here.)

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
