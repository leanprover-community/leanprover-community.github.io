# How to use congr()

`congr()` is a term elaborator using *congruence* to build proofs of equality, `HEq` and `Iff`.
The prototypical congruence lemma is called [`congr`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=congr#doc),
stating that two expressions are equal (here, two function applications) when the components are equal (here, the functions and their arguments).
```lean
theorem congr {f₁ f₂ : α → β} {a₁ a₂ : α} (h₁ : f₁ = f₂) (h₂ : a₁ = a₂) : f₁ a₁ = f₂ a₂
```
Congruence lemmas allow us to chain together equality proofs into a large proof.
Instead of composing proofs manually using `congr` and its specializations [`congrFun`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=congrFun#doc) and [`congrArg`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=congrArg#doc),
the `congr()` elaborator does this for you with less syntactical noise.

Basic example usage:

```lean
import Mathlib.Tactic.TermCongr

example (a b : Nat) (h : a = b) : 4 * (37 + a) = 4 * (37 + b) :=
  congr(4 * (37 + $h))
```

Here, most parts of the expression given to `congr()` appear on both sides of the equality, except where we write `$h`.
The syntax `$h` means `congr()` inserts `a`, the left hand side of `h`, on the left hand side of the resulting equality, and `b`, the right hand side of `h`, on the right hand side.
`$h` is an example of an [antiquotation](https://lean-lang.org/doc/reference/latest/Notations-and-Macros/Macros/#quasiquotation).
Later in this document we will cover the full syntax of quotations and antiquotations used by `congr()`.

`congr()` supports `Eq`, `Iff` and `HEq` and can convert between them as needed:

```lean
example (a b : Nat) (h : a = b) : 4 * (37 + a) = 0 ↔ 4 * (37 + b) = 0 :=
  congr(4 * (37 + $h) = 0)

example (p q : Prop) [Decidable p] [Decidable q] (h : p ↔ q) :
    (if p then 1 else 0) = if q then 1 else 0 :=
  congr(if $h then 1 else 0)

example (a b : Nat) (h : a = b) [NeZero a] [NeZero b] : (37 : Fin a) ≍ (37 : Fin b) :=
  congr((37 : Fin $h))
```

## Syntax

Like other elaborators and macros, the parentheses are always attached to `congr()` without a space in between.
`congr(...)` means something different from `congr (...)`: the first is the term elaborator we are discussing, while the second is the [`congr`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=congr#doc) lemma from the library applied to the arguent `(...)`.

Inside the parentheses goes a [*quasiquoted*](https://lean-lang.org/doc/reference/latest/Notations-and-Macros/Macros/#quasiquotation) expression.
In addition to the syntax of a typical expression, you can insert *antiquotations* which allow the content to vary.
There are two kinds of antiquotations:

* `$ident`, like `$h` in the examples above, to refer to a single variable.
* `$(term)`, where a whole expression can be inserted in the place of the term.

Whenever `congr()` encounters an antiquotation, it treats the contents of the antiquotation as an expression.
As long as the expression can be elaborated in the context, it can be as complicated as you want:

```lean
example (a b : Nat) (h : a = b) : 4 * (37 + a) = 4 * (37 + b) :=
  congr(4 * (37 + $h))

example (a b : Nat) (h : a = b) : 4 * (37 + a) = 4 * (37 + b) :=
  congr(4 * (37 + $(h)))

example (a b : Nat) (h : a = b) : 4 * (37 + a) = 4 * (37 + b) :=
  congr(4 * (37 + $(h.symm.symm)))

example (a b : Nat) (h : a = b) : 4 * (37 + a) = 4 * (37 + b) :=
  congr($(by rfl) * ($(by grind) + $(by simp [h])))
```

The expression inside an antiquotation can refer to local variables, which is useful if your proofs are not fully applied:
```lean
example (f g : Nat → Nat) (h : ∀ i, f i = g i) (a : Nat) : f a = g a :=
  congr($(h a))

-- Make sure to apply the proof inside the antiquotation brackets.
-- The example below fails, because `h` is expected to be an equality of functions.
example (f g : Nat → Nat) (h : ∀ i, f i = g i) (a : Nat) : f a = g a :=
  congr($h a) -- Error: function expected.

-- The local variables can be bound inside the `congr` expression:
example (f g : Nat → Nat) (h : ∀ i, f i = g i) : (fun a => f a) = (fun a => g a) :=
  congr(fun a => $(h a))

-- Since `fun a => f a` is equal to `f`, this is a tricky proof of function extensionality:
example (f g : Nat → Nat) (h : ∀ i, f i = g i) : f = g :=
  congr(fun a => $(h a))
```

## Proofs

Depending on the expected type, `congr()` will produce an `Eq`, `HEq` or `Iff`.
For simplicity, we will assume in this section that `congr()` produces equalities.
We call the term `t` inside `congr(t)` the *pattern* and the type of `congr(t)` the *result*.
If the pattern contains no antiquotations, `congr(t)` is equivalent to `rfl : t = t`.
For any antiquotations, the left hand side of the result will contain the left hand side of the antiquotation's type,
and the right hand side of the result will contain the right hand side of the antiquotation's type.

`congr()` processes the pattern twice: once as left hand side, once as right hand side.
The quoted expression is elaborated as normal until `congr()` encounters an antiquotation:
these antiquotations are first elaborated without an expected type,
in order to determine the left- and right hand side.
If this elaboration results in a type with holes, then those are postponed to be solved later by unification with the goal.

In other words, `congr()` uses the expected type to fill in holes in the pattern:

```lean
example (a b : Nat) (h : a = b) : 1 + a = 1 + b := by
  have : 1 + _ = _ := congr(_ + $h)
  exact this
```

This means antiquotations can be postponed as required, such as calling the `assumption` tactic only at the end:
```lean
example (a b : Nat) (h : a = b) : 4 * (37 + a) = 4 * (37 + b) :=
  congr(4 * (37 + $(by assumption)))
```

But if the expected type is missing and the antiquotation still needs to be filled in, then it is run with metavariables, and it can make the wrong guess:
```lean
example (a b c : Nat) (h : a = b) (h2 : b = c) : 1 + a = 1 + b := by
  have : 1 + _ = _ := congr(_ + $(by assumption -- Goal: `?m.55 = ?m.56`, filled with `h2 : b = c`))
  exact this -- Error: `this` has type `1 + b = 1 + c`
```

When the pattern has been elaborated twice, it is unified against the expected type,
to fill in most remaining holes.
Finally the left hand side and right hand side are matched against each other,
inserting congruence lemmas or the proofs inside the antiquotations as appropriate.
`congr()` has special support for `Subsingleton` and propositional extensionality,
allowing it to handle functions depending on subsingleton classes like `Decidable` and `Fintype`.

Depending on the context, `congr()` has the ability to convert between proofs of `Eq`, `HEq`, or `Iff`.
By default, `congr()` will produce a proof of `Eq`. It uses `HEq` or `Iff` if the expected type suggests this:
```lean
example (p q : Prop) [Decidable p] [Decidable q] (h : p ↔ q) : (if p then 1 else 0) = (if q then 1 else 0) := by
  have := congr($h)
  -- No expected type given above, so `this : p = q`.
  exact congr(if $this then 1 else 0)

example (p q : Prop) [Decidable p] [Decidable q] (h : p ↔ q) : (if p then 1 else 0) = (if q then 1 else 0) := by
  have : _ ↔ _ := congr($h)
  -- `Iff` expected above, so `this : p ↔ q`.
  exact congr(if $this then 1 else 0)
```

`congr()` has the ability to move inside binders. If your equality is not fully applied, make sure to use the right syntax for applying it inside the binder:

```lean
example (f g : Nat → Nat) (s t : Finset Nat) (hfg : ∀ i, f i = g i) (hst : s = t) :
    ∑ i ∈ s, f i = ∑ i ∈ t, g i :=
  congr(∑ i ∈ $hst, $(hfg i))

-- Equivalent to:
example (f g : Nat → Nat) (s t : Finset Nat) (hfg : f = g) (hst : s = t) :
    ∑ i ∈ s, f i = ∑ i ∈ t, g i :=
  congr(∑ i ∈ $hst, $hfg i)
```

## Related functionality

There are many tools like `congr()` for constructing proofs involving equalities.

* The [`congr`](https://leanprover-community.github.io/mathlib4_docs/tactics.html#Lean.Parser.Tactic.congr) and [`congr!`](https://leanprover-community.github.io/mathlib4_docs/tactics.html#Congr!.congr!) tactics use congruence rules to prove equalities. Where the `congr()` elaborator starts with proofs for each small part of the expression and uses congruence rules to assemble them into one proof for the whole expression, the `congr` and `congr!` tactics break apart an equality goal for the whole expression using congruence rules into smaller parts. `congr!` is more powerful than `congr()` since it has access to custom congruence lemmas.
* The triangle `▸` is a macro for rewriting inside the type of an expression. If `h : a = b` and the goal is `4 * (37 + a) = 4 * (37 + b)`, then the hole in `h ▸ _` has expected type `4 * (37 + a) = 4 * (37 + a)`. So `h ▸ rfl` would close this goal, just like `congr(4 * (37 + $h))` would. Unlike `congr()`, the triangle works outside-in: if we write `have := h ▸ rfl` without an expected type, we would end up with a hypothesis `this : a = b`.
* Rewriting tactics like `rw` and `simp` can use hypotheses like `h : a = b` to prove a goal like `4 * (37 + a) = 4 * (37 + b)`, by rewriting both sides of the equality to be identical and closing the goal with `rfl`. Unlike `congr()`, these tactics work outside-in: if the goal type is missing, they fail. `simp` is more powerful than `congr()` since it uses a more powerful congruence lemma generator.

## Limitations

`congr()` cannot handle all possible expressions: it can only compose the exact equalities you pass in.
The following example succeeds because `(37 : Fin a)` can be turned into `(37 : Fin b)` by rewriting using `h : a = b` everywhere:

```lean
example (a b : Nat) (h : a = b) [NeZero a] [NeZero b] : (37 : Fin a) ≍ (37 : Fin b) :=
  congr((37 : Fin $h))
```

On the other hand, the following example fails because `(37 + _ : Fin a)` cannot turn into `(37 + _ : Fin b)` by rewriting using `h : x ≍ y`.

```lean
example (a b : Nat) [NeZero a] [NeZero b] (x : Fin a) (y : Fin b) (h : x ≍ y) :
    37 + x ≍ 37 + y :=
  congr(37 + $h) -- Error: could not generate congruence between `a` and `b`.
```

We'd need to construct the proof of `a = b` ourselves and insert it into the expression in the right place to make `congr()` work:

```lean
example (a b : Nat) [NeZero a] [NeZero b] (x : Fin a) (y : Fin b) (h : x ≍ y) :
    37 + x ≍ 37 + y :=
  have hab : a = b := Fin.equiv_iff_eq.mp ⟨type_eq_of_heq h ▸ Equiv.refl _⟩
  congr(Add.add (α := Fin $hab) 37 $h)
```

## Bugs

Rarely, internal metadata or reducible wrappers leak out of the generated term, being exposed in the unification process.
These are not visible to the user, but some tactics might have their pattern matching configured too strictly and trip on them.
If you notice a tactic failing to apply after using `congr()`, please report the issue on the Lean community Zulip chat.
