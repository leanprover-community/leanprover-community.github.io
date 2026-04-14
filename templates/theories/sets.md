# Maths in Lean: Sets and set-like objects

### Lists

#### `Mathlib.Data.List.Basic`

`List α` is the type of lists of elements of type `α`. Lists are finite and ordered, and can contain duplicates. Lists can only contain elements of the same type. Lists are constructed using the cons function, which appends an element of `α` to the top of a list. Lists are discussed in more detail in TPIL, chapter 7.5

`[1, 1, 2, 4] ≠ [1, 2, 1, 4]`

`[1, 2, 1, 4] ≠ [1, 2, 4]`

### Multisets

#### `Mathlib.Data.Multiset.Basic`

`Multiset α` is the type of multisets of elements of type `α`. Multisets are finite and can contain duplicates, but are not ordered. They are defined as the quotient of lists over the `Perm` equivalence relation. Multisets can only contain elements of the same type.

`{1, 1, 2, 4} = {1, 2, 1, 4}`

`{1, 1, 2, 4} ≠ {1, 2, 4}`

### Finsets

#### `Mathlib.Data.Finset.Basic`

`Finset α` is the type of unordered lists of distinct elements of type α. A finset is constructed from a multiset and a proof that the multiset contains no duplicates. Finsets are finite. Finsets can only contain elements of the same type.

`{1, 1, 2, 4} = {1, 2, 1, 4}`

`{1, 1, 2, 4} = {1, 2, 4}`

### Sets and subtypes

#### `Mathlib.Data.Set.Basic`

`Set α`. A set is defined as a predicate, i.e. a function `α → Prop`. The notation used is `{n : ℕ | 4 ≤ n}` for the set of naturals greater than or equal to 4. Sets can be infinite, and can only contain elements of the same type.

A subtype is similar to a set in that it is defined by a predicate. The notation used is `{n : ℕ // 4 ≤ n}` for the type of naturals greater than or equal to 4. However, a subtype is a type rather than a set, and the elements the aforementioned subtype do not have type `ℕ`, they have type `{n : ℕ // 4 ≤ n}`. This means that addition is not defined on this type, and equality between naturals and this type is also undefined. However it is possible to coerce an element of this subtype back into a natural, in the same way that a natural can be coerced into an integer, and then addition and equality behave as normal (see TPIL, chapter 6.7 for more on coercions). To construct an element of a subtype of α, you need an element of α and a proof that it satisfies the predicate, `4` and ``le_refl 4`` in the example below.

```lean
def x : {n : ℕ // 4 ≤ n} := ⟨4, le_refl 4⟩
example : (x : ℕ) + 6 = 10 := rfl
```

Any set can be used where a type is expected, in which case the set will be coerced into the corresponding subtype.

```lean
def S : Set ℕ := {n : ℕ | 4 ≤ n}
example : ∀ n : S, 4 ≤ (n : ℕ) := fun ⟨n, hn⟩ ↦ hn
```

It is useful to use a subtype rather than a set when you need to define functions on subtypes, or when using the cardinal of a subtype.

### Finite types

#### `Mathlib.Data.Fintype.Basic`

`Fintype α` means that a type α is finite. It is constructed from a finset containing all elements of a type.

```lean
class Fintype (α : Type*) where
  /-- The `Finset` containing all elements of a `Fintype` -/
  elems : Finset α
  /-- A proof that `elems` contains every element of the type -/
  complete : ∀ x : α, x ∈ elems
```

`Fintype α` is not a proposition, because it contains data, however it is a subsingleton, meaning that any two elements of type `Fintype α` are equal.

`Finset.univ` is the finset containing all elements of a type, given a `Fintype α` instance.

### Finite sets

#### `Mathlib.Data.Set.Finite`

The definition of a finite set, distinct from a finset is that corresponding type is in bijection with `Fin n` for some `n : ℕ`.
This means when the set is coerced into a subtype, the type `Fintype s` is nonempty.
Using `Classical.choose`, you can produce an object of type `Fintype s` from a proof of `Finite s`. There is a function `Set.Finite.toFinset` which produces a finset from a finite set.

### Cardinals

There are three functions `Finset.card`, `Fintype.card` and `Multiset.card`, which refer to the sizes of finsets, finite types and multisets. For finite cardinals of sets, `Fintype.card` can be used, given a proof that the set is finite.

```lean
example : ∀ n : ℕ, Fintype.card (Fin n) = n := Fintype.card_fin
example : ∀ n : ℕ, Finset.card (Finset.range n) = n := Finset.card_range
```

Here, `Fin n` is the type of naturals less than n, and `Finset.range n` is the finset of naturals less than `n`.

`Mathlib.SetTheory.Cardinal.Basic` contains theory on infinite cardinals.
