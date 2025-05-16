# The conversion tactic mode

Inside a tactic block, one can use the keyword `conv` to enter conversion
mode. This mode allows to travel inside assumptions and goals, even
inside `fun` binders in them, to apply rewriting or simplifying steps.

This is similar to the conversion tacticals (tactic combinators) found in
other theorem provers like HOL4, HOL Light or Isabelle.

## Basic navigation and rewriting

As a first example, let us prove
`example (a b c : ℕ) : a * (b * c) = a * (c * b)` (examples in this file
are somewhat artificial since the `ring` tactic from
`Tactic.Ring` could finish them immediately). The naive first attempt is
to enter tactic mode and try `rw [mul_comm]`. But this transforms the goal
into `b * c * a = a * (c * b)`, after commuting the very first
multiplication appearing in the term. There are several ways to fix this
issue, and one way is to use a more precise tool : the
conversion mode.  The following code block shows the current target after
each line. Note that the target is prefixed by `|` where normal mode
shows a goal prefixed by `⊢` (these targets are still called "goals"
though).

```lean
example (a b c : ℕ) : a * (b * c) = a * (c * b) := by
  conv =>           -- | a * (b * c) = a * (c * b)
    lhs             -- | a * (b * c)
    congr           -- | a and | b * c
    · skip          -- | a
    · rw [mul_comm] -- | c * b
```

The above snippet show three navigation commands:
* `lhs` navigates to the left hand side of a relation (here
  equality), there is also a `rhs` navigating to the right hand side.
* `congr` creates as many targets as there are arguments to the current
  head function (here the head function is multiplication)
* `skip` goes to the next target

Once arrived at the relevant target, we can use `rw` as in normal mode.
Note that Lean tries to solves the current goal if it became `x = x` (in
the strict syntactical sense, definitional equality is not enough: one
needs to conclude by `rfl` or `trivial` in this case).

For your information, we can write "conv => lhs .." to "conv_lhs => ..":

```lean
example (a b c : ℕ) : a * (b * c) = a * (c * b) := by
  conv_lhs =>
    congr
    · skip
    · rw [mul_comm]
```

The second main reason to use conversion mode is to rewrite under
binders. Suppose we want to prove `example (fun x : ℕ ↦ 0 + x) = (fun x ↦ x)`.
The naive first attempt is to enter tactic mode and try `rw [zero_add]`.
But this fails with a frustrating
```text
tactic 'rewrite' failed, did not find instance of the pattern in the target expression
  0 + ?a
⊢ (fun x ↦ 0 + x) = fun x ↦ x
```

The solution is:
```lean
example : (fun x : ℕ ↦ 0 + x) = (fun x ↦ x) := by
  conv_lhs =>     -- | fun x ↦ 0 + x
    ext x         -- | 0 + x
    rw [zero_add] -- | x
```
where `ext` is the navigation command entering inside the `fun` binder.
Note that this example is somewhat artificial, one could also do:
```lean
example : (fun x : ℕ ↦ 0 + x) = (fun x ↦ x) := by
  funext x; rw [zero_add]
```

All this is also available to rewrite an hypothesis `H` from the local context
using `conv at H`.

## Pattern matching

Navigation using the above commands can be tedious. One can shortcut it
using pattern matching as follows:

```lean
example (a b c : ℕ) : a * (b * c) = a * (c * b) := by
  conv in (b * c) => -- | b * c
    rw [mul_comm]    -- | c * b
```

We can write this proof in one line:

```lean
example (a b c : ℕ) : a * (b * c) = a * (c * b) := by
  conv in (b * c) => rw [mul_comm]
```

Of course wild-cards are allowed:

```lean
example (a b c : ℕ) : a * (b * c) = a * (c * b) := by
  conv in (_ * c) => rw [mul_comm]
```

In all those cases, only the first match is affected.
A more sophisticated version of pattern matching is available inside
conversion mode using the `for` command. The following performs rewriting
only for the second and third occurrences of `b * c`:

```lean
example (a b c : ℕ) : (b * c) * (b * c) * (b * c) = (b * c) * (c * b) * (c * b) := by
  conv in (occs := 2 3) (b * c) =>
    · rw [mul_comm]
    · rw [mul_comm]
```

We can write this proof in one line with "all_goals":

```lean
example (a b c : ℕ) : (b * c) * (b * c) * (b * c) = (b * c) * (c * b) * (c * b) := by
  conv in (occs := 2 3) (b * c) => all_goals rw [mul_comm]
```

## Other tactics inside conversion mode

Besides rewriting using `rw`, one can use `simp`, `dsimp`, `change` and `whnf`.
`change` is a useful tool -- it allows changing a term to something
definitionally equal, rather like the `show` command in tactic mode.
The `whnf` command means "reduces to weak head normal form" and will eventually
be explained in [Metaprogramming in Lean 4](https://leanprover-community.github.io/lean4-metaprogramming-book/main/04_metam.html#weak-head-normalisation) section 4.

Extensions to `conv` provided by mathlib, such as `ring` and `norm_num`, can be
found using `#help conv` command in [`Mathlib.Tactic.HelpCmd`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Tactic/HelpCmd.html).
