# Library Style Guidelines

In addition to the [naming conventions](naming.html),
files in the Lean library generally adhere to the following guidelines
and conventions. Having a uniform style makes it easier to browse the
library and read the contents, but these are meant to be guidelines
rather than rigid rules.

### Variable conventions

- `u`, `v`, `w`, ... for universes
- `α`, `β`, `γ`, ... for generic types
- `a`, `b`, `c`, ... for propositions
- `x`, `y`, `z`, ... for elements of a generic type
- `h`, `h₁`, ...     for assumptions
- `p`, `q`, `r`, ... for predicates and relations
- `s`, `t`, ...      for lists
- `s`, `t`, ...      for sets
- `m`, `n`, `k`, ... for natural numbers
- `i`, `j`, `k`, ... for integers

Types with a mathematical content are expressed with the usual
mathematical notation, often with an upper case letter
(`G` for a group, `R` for a ring, `K` or `𝕜` for a field, `E` for a vector space, ...).
This convention is not followed in older files, where greek letters are used
for all types. Pull requests renaming type variables in these files are welcome.

### Line length

Lines should not be longer than 100 characters. This makes files
easier to read, especially on a small screen or in a small window.
If you are editing with VS Code, there is a visual marker which
will indicate a 100 character limit.

### Header and imports

The file header should contain copyright information, a list of all
the authors who have made significant contributions to the file, and
a description of the contents. Do all `import`s right after the header,
without a line break, on separate lines.

```lean
/-
Copyright (c) 2024 Joe Cool. All rights reserved.
Released under Apache 2.0 license as described in the file LICENSE.
Authors: Joe Cool
-/
import Mathlib.Data.Nat.Basic
import Mathlib.Algebra.Group.Defs
```

(Tip: If you're editing mathlib in VS Code, you can write `copy`
and then press <kbd>TAB</kbd> to generate a skeleton of the copyright header.)

Regarding the list of authors: use `Authors` even when there is only a single author.
Don't end the line with a period, and use commas (`, `) to separate all author names
(so don't use `and` between the penultimate and ultimate author.)
We don't have strict rules on what contributions qualify for inclusion there.
The general idea is that the people listed there should be the ones we would
reach out to if we had questions about the design or development of the Lean code.

### Module docstrings

After the copyright header and the imports,
please add a module docstring (delimited with `/-!` and `-/`) containing

- a title of the file,
- a summary of the contents (the main definitions and theorems, proof techniques, etc…)
- notation that has been used in the file (if any)
- references to the literature (if any)

In total, the module docstring should look something like this:
```markdown
/-!
# Foos and bars

In this file we introduce `foo` and `bar`,
two main concepts in the theory of xyzzyology.

## Main results

- `exists_foo`: the main existence theorem of `foo`s.
- `bar_of_foo`: a construction of a `bar`, given a `foo`.
- `bar_eq`    : the main classification theorem of `bar`s.

## Notation

 - `|_|` : The barrification operator, see `bar_of_foo`.

## References

See [Thales600BC] for the original account on Xyzzyology.
-/
```

New bibliography entries should be added to `docs/references.bib`.

See our [documentation requirements](doc.html) for more suggestions and examples.

### Structuring definitions and theorems

All declarations (e.g., `def`, `lemma`, `theorem`, `class`, `structure`, `inductive`, `instance`, etc.)
and commands (e.g., `variable`, `open`, `section`, `namespace`, `notation`, etc.) are considered
top-level and these words should appear flush-left in the document. In particular, opening a
namespace or section does not result in indenting the contents of that namespace or section.
(Note: within VS Code, hovering over any declaration such as `def Foo ...` will show the fully
qualified name, like `MyNamespace Foo` if `Foo` is declared while the namespace `MyNamespace` is open.)

These guidelines hold for declarations starting with `def`, `lemma` and `theorem`.
For "theorem statement", also read "type of a definition" and for "proof" also read
"definition body".

Use spaces on both sides of ":", ":=" or infix operators. Put them before a line break
rather than at the beginning of the next line.

In what follows, "indent" without an explicit indication of the amount means
"indent by 2 additional spaces".

After stating the theorem, we indent the lines in the subsequent proof by 2 spaces.
```lean
open Nat
theorem nat_case {P : Nat → Prop} (n : Nat) (H1 : P 0) (H2 : ∀ m, P (succ m)) : P n :=
  Nat.recOn n H1 (fun m IH ↦ H2 m)
```

If the theorem statement requires multiple lines, indent the subsequent lines by 4 spaces.
The proof is still indented only 2 spaces (*not* 6 = 4 + 2).
When providing a proof in tactic mode, the `by` is placed on the line *prior* to the
first tactic; however, `by` should not be placed on a line by itself.
In practice this means you will often see `:= by` at the end of a theorem statement.
```lean
import Mathlib.Data.Nat.Basic

theorem le_induction {P : Nat → Prop} {m}
    (h0 : P m) (h1 : ∀ n, m ≤ n → P n → P (n + 1)) :
    ∀ n, m ≤ n → P n := by
  apply Nat.le.rec
  · exact h0
  · exact h1 _

def decreasingInduction {P : ℕ → Sort*} (h : ∀ n, P (n + 1) → P n) {m n : ℕ} (mn : m ≤ n)
    (hP : P n) : P m :=
  Nat.leRecOn mn (fun {k} ih hsk => ih <| h k hsk) (fun h => h) hP
```

When a proof term takes multiple arguments, it is sometimes clearer, and often
necessary, to put some of the arguments on subsequent lines. In that case,
indent each argument. This rule, i.e., indent an additional two spaces, applies
more generally whenever a term spans multiple lines.
```lean
open Nat
axiom zero_or_succ (n : Nat) : n = zero ∨ n = succ (pred n)
theorem nat_discriminate {B : Prop} {n : Nat} (H1: n = 0 → B) (H2 : ∀ m, n = succ m → B) : B :=
  Or.elim (zero_or_succ n)
    (fun H3 : n = zero ↦ H1 H3)
    (fun H3 : n = succ (pred n) ↦ H2 (pred n) H3)
```
Don't orphan parentheses; keep them with their arguments.

Here is a longer example.
```lean
import Mathlib.Init.Data.List.Lemmas

open List
variable {T : Type}

theorem mem_split {x : T} {l : List T} : x ∈ l → ∃ s t : List T, l = s ++ (x :: t) :=
  List.recOn l
    (fun H : x ∈ [] ↦ False.elim ((mem_nil_iff _).mp H))
    (fun y l ↦
      fun IH : x ∈ l → ∃ s t : List T, l = s ++ (x :: t) ↦
      fun H : x ∈ y :: l ↦
      Or.elim (eq_or_mem_of_mem_cons H)
        (fun H1 : x = y ↦
          Exists.intro [] (Exists.intro l (by rw [H1]; rfl)))
        (fun H1 : x ∈ l ↦
          let ⟨s, (H2 : ∃ t : List T, l = s ++ (x :: t))⟩ := IH H1
          let ⟨t, (H3 : l = s ++ (x :: t))⟩ := H2
          have H4 : y  ::  l = (y :: s) ++ (x :: t) := by rw [H3]; rfl
          Exists.intro (y :: s) (Exists.intro t H4)))
```

A short declaration can be written on a single line:
```lean
open Nat
theorem succ_pos : ∀ n : Nat, 0 < succ n := zero_lt_succ

def square (x : Nat) : Nat := x * x
```

A `have` can be put on a single line when the justification is short.
```lean
example (n k : Nat) (h : n < k) : ... :=
  have h1 : n ≠ k := ne_of_lt h
  ...
```
When the justification is too long, you should put it on the next line,
indented by an additional two spaces.
```lean
example (n k : Nat) (h : n < k) : ... :=
  have h1 : n ≠ k :=
    ne_of_lt h
  ...
```
When the justification of the `have` uses tactic mode, the `by` should
be placed on the same line, regardless of whether the justification
spans multiple lines.
```lean
example (n k : Nat) (h : n < k) : ... :=
  have h1 : n ≠ k := by apply ne_of_lt; exact h
  ...

example (n k : Nat) (h : n < k) : ... :=
  have h1 : n ≠ k := by
    apply ne_of_lt
    exact h
  ...
```

When the arguments themselves are long enough to require line breaks, use
an additional indent for every line after the first, as in the following
example:
```lean
import Mathlib.Data.Nat.Basic

theorem Nat.add_right_inj {n m k : Nat} : n + m = n + k → m = k :=
  Nat.recOn n
    (fun H : 0 + m = 0 + k ↦ calc
      m = 0 + m := Eq.symm (zero_add m)
      _ = 0 + k := H
      _ = k     := zero_add _)
    (fun (n : Nat) (IH : n + m = n + k → m = k) (H : succ n + m = succ n + k) ↦
      have H2 : succ (n + m) = succ (n + k) := calc
        succ (n + m) = succ n + m   := Eq.symm (succ_add n m)
        _            = succ n + k   := H
        _            = succ (n + k) := succ_add n k
      have H3 : n + m = n + k := succ.inj H2
      IH H3)
```

In a class or structure definition, fields are indented 2 spaces, and moreover
each field should have a docstring, as in:

```lean
structure PrincipalSeg {α β : Type*} (r : α → α → Prop) (s : β → β → Prop) extends r ↪r s where
  /-- The supremum of the principal segment -/
  top : β
  /-- The image of the order embedding is the set of elements `b` such that `s b top` -/
  down' : ∀ b, s b top ↔ ∃ a, toRelEmbedding a = b

class Module (R : Type u) (M : Type v) [Semiring R] [AddCommMonoid M] extends
    DistribMulAction R M where
  /-- Scalar multiplication distributes over addition from the right. -/
  protected add_smul : ∀ (r s : R) (x : M), (r + s) • x = r • x + s • x
  /-- Scalar multiplication by zero gives zero. -/
  protected zero_smul : ∀ x : M, (0 : R) • x = 0
```

When using a constructor taking several arguments in a definition,
arguments line up, as in:

```lean
theorem Ordinal.sub_eq_zero_iff_le {a b : Ordinal} : a - b = 0 ↔ a ≤ b :=
  ⟨fun h => by simpa only [h, add_zero] using le_add_sub a b,
   fun h => by rwa [← Ordinal.le_zero, sub_le, add_zero]⟩
```

### Instances

When providing terms of structures or instances of classes, the `where`
syntax should be used to avoid the need for enclosing braces, as in:

```lean
instance instOrderBot : OrderBot ℕ where
  bot := 0
  bot_le := Nat.zero_le
```

If there is already an instance `instBot`, then one can write

```lean
instance instOrderBot : OrderBot ℕ where
  __ := instBot
  bot_le := Nat.zero_le
```

### Hypotheses Left of Colon

Generally, having arguments to the left of the colon is preferred
over having arguments in universal quantifiers or implications,
if the proof starts by introducing these variables. For instance:

```lean
example (n : ℝ) (h : 1 < n) : 0 < n := by linarith
```

is preferred over

```lean
example (n : ℝ) : 1 < n → 0 < n := fun h ↦ by linarith
```

and

```lean
example (n : ℕ) : 0 ≤ n := dec_trivial __Nat.zero_le n
```

is preferred over

```lean
example : ∀ (n : ℕ), 0 ≤ n := Nat.zero_le
```

### Binders

Use a space after binders:
```lean
example : ∀ α : Type, ∀ x : α, ∃ y, y = x :=
  fun (α : Type) (x : α) ↦ Exists.intro x rfl
```

### Anonymous functions

Lean has several nice syntax options for declaring anonymous functions. For very simple
functions, one can use the centered dot as the function argument, as in `(· ^ 2)` to
represent the squaring function. However, sometimes it is necessary to refer to the
arguments by name (e.g., if they appear in multiple places in the function body). The
Lean default for this is `fun x => x * x`, but the `↦` arrow (inserted with `\mapsto`)
is also valid. In mathlib the pretty printer displays `↦`, and we slightly prefer this
in the source as well.  The lambda notation `λ x ↦ x * x`, while syntactically valid,
is disallowed in mathlib in favor of the `fun` keyword.

### Calculations

There is some flexibility in how you write calculational proofs, although there are some
rules enforced by the syntax requirements of `calc` itself. However, there are some general
guidelines.

As with `by`, the `calc` keyword should be placed on the line *prior* to the start of the
calculation, with the calculation indented. Whichever relations are involved (e.g.,
`=` or `≤`) should be aligned from one line to the next. The underscores `_` used as
placeholders for terms indicating the continuation of the calculation should be left-justified.

As for the justifications, it is not necessary to align the `:=` symbols, but it can be
nice if the expressions are short enough. The terms on either side of the first relation can either
go on one line or separate lines, which may be decided by the size of the expressions.

An example of adequate style which can more easily accommodate longer expressions is:

```lean
import Init.Data.List.Basic

open List

theorem reverse_reverse : ∀ (l : List α), reverse (reverse l) = l
  | []       => rfl
  | (a :: l) => calc
      reverse (reverse (a :: l))
        = reverse (reverse l ++ [a]) := by rw [reverse_cons]
      _ = reverse [a] ++ reverse (reverse l) := reverse_append _ _
      _ = reverse [a] ++ l := by rw [reverse_reverse l]
      _ = a :: l := rfl
```

However, because the expressions and proofs are relatively short, the following style
might be preferable in this situation.

```lean
import Init.Data.List.Basic

open List

theorem reverse_reverse : ∀ (l : List α), reverse (reverse l) = l
  | []       => rfl
  | (a :: l) => calc
      reverse (reverse (a :: l)) = reverse (reverse l ++ [a])         := by rw [reverse_cons]
      _                          = reverse [a] ++ reverse (reverse l) := reverse_append _ _
      _                          = reverse [a] ++ l                   := by rw [reverse_reverse l]
      _                          = a :: l                             := rfl
```

### Tactic mode

As we have already mentioned, when opening a tactic block,
`by` is placed at the end of the line
*preceding* the start of the tactic block, but not on its own line.
Everything within the tactic block is indented, as in:

```lean
theorem continuous_uncurry_of_discreteTopology [DiscreteTopology α] {f : α → β → γ}
    (hf : ∀ a, Continuous (f a)) : Continuous (uncurry f) := by
  apply continuous_iff_continuousAt.2
  rintro ⟨a, x⟩
  change map _ _ ≤ _
  rw [nhds_prod_eq, nhds_discrete, Filter.map_pure_prod]
  exact (hf a).continuousAt
```

One can mix term mode and tactic mode, as in:
```lean
theorem Units.isUnit_units_mul {M : Type*} [Monoid M] (u : Mˣ) (a : M) :
    IsUnit (↑u * a) ↔ IsUnit a :=
  Iff.intro
    (fun ⟨v, hv⟩ => by
      have : IsUnit (↑u⁻¹ * (↑u * a)) := by exists u⁻¹ * v; rw [← hv, Units.val_mul]
      rwa [← mul_assoc, Units.inv_mul, one_mul] at this)
    u.isUnit.mul
```

When new goals arise as side conditions or steps, they are indented and preceded by
a focusing dot `·` (inserted as `\.`); the dot is not indented.
```lean
import Mathlib.Algebra.Group.Basic

theorem exists_npow_eq_one_of_zpow_eq_one' [Group G] {n : ℤ} (hn : n ≠ 0) {x : G} (h : x ^ n = 1) :
    ∃ n : ℕ, 0 < n ∧ x ^ n = 1 := by
  cases n
  · simp only [Int.ofNat_eq_coe] at h
    rw [zpow_ofNat] at h
    refine ⟨_, Nat.pos_of_ne_zero fun n0 ↦ hn ?_, h⟩
    rw [n0]
    rfl
  · rw [zpow_negSucc, inv_eq_one] at h
    refine ⟨_ + 1, Nat.succ_pos _, h⟩
```

Certain tactics, such as `refine`, can create *named* subgoals which
can be proven in whichever order is desired using `case`. This feature
is also useful in aiding readability. However, it is not required to
use this instead of the focusing dot (`·`).

```lean
example {p q : Prop} (h₁ : p → q) (h₂ : q → p) : p ↔ q := by
  refine ⟨?imp, ?converse⟩
  case converse => exact h₂
  case imp => exact h₁
```

Often `t0 <;> t1` is used to execute `t0` and then `t1` on all new goals.
Either write the tactics in one line, or indent the following tactic.

```lean
  cases x <;>
    simp [a, b, c, d]
```

For single line tactic proofs (or short tactic proofs embedded in a term),
it is acceptable to use `by tac1; tac2; tac3` with semicolons instead of
a new line with indentation.

In general, you should put a single tactic invocation per line, unless you are
closing a goal with a proof that fits entirely on a single line. Short sequences of
tactics that correspond to a single mathematical idea can also be put on a single line,
separated by semicolons as in `cases bla; clear h` or `induction n; simp` or
`rw [foo]; simp_rw [bar]`, but even in these scenarios, newlines are preferred.

```lean
example : ... := by
  by_cases h : x = 0
  · rw [h]; exact hzero ha
  · rw [h]
    have h' : ... := H ha
    simp_rw [h', hb]
    ...
```

Very short goals can be closed right away using `swap` or `pick_goal` if needed, to avoid
additional indentation in the rest of the proof.

```lean
example : ... := by
  rw [h]
  swap; exact h'
  ...
```

We generally use a blank line to separate theorems and definitions,
but this can be omitted, for example, to group together a number of
short definitions, or to group together a definition and notation.

### Whitespace and delimiters

Lean is whitespace-sensitive, and in general we opt for a style which avoids
delimiting code. For instance, when writing tactics, it is possible to write
them as `tac1; tac2; tac3`, separated by `;`, in order to override the default
whitespace sensitivity. However, as mentioned above, we generally try to avoid
this except in a few special cases.

Similarly, sometimes parentheses can be avoided by judicious use of the `<|`
operator (or its cousin `|>`). Note: while `$` is a synonym for `<|`, its
use in mathlib is disallowed in favor of `<|` for consistency as well as
because of the symmetry with `|>`. These operators have the effect of
parenthesizing everything to the right of `<|` (note that `(` is curved the
same direction as `<`) or to the left of `|>` (and `)` curves the same way
as `>`).

A common example of the usage of `|>` occurs with dot notation when the term
preceding the `.` is a function applied to some arguments. For instance,
`((foo a).bar b).baz` can be rewritten as `foo a |>.bar b |>.baz`

A common example of the usage of `<|` is when the user provides a term which
is a function applied to multiple arguments whose last argument is a proof in
tactic mode, especially one that spans multiple lines. In that case, it is
natural to use `<| by ...` instead of `(by ...)`, as in:

```lean
import Mathlib.Tactic

example {x y : ℝ} (hxy : x ≤ y) (h : ∀ ε > 0, y - ε ≤ x) : x = y :=
  le_antisymm hxy <| le_of_forall_pos_le_add <| by
    intro ε hε
    have := h ε hε
    linarith
```

When using the tactics `rw` or `simp` there should be a space after the left arrow  `←`.
For instance `rw [← add_comm a b]` or `simp [← and_or_left]`.
(There should also be a space between the tactic name and its arguments, as in `rw [h]`.)
This rule applies the `do` notation as well: `do return (← f) + (← g)`

### Normal forms

Some statements are equivalent. For instance, there are several equivalent
ways to require that a subset `s` of a type is nonempty. For another example, given
`a : α`, the corresponding element of `Option α` can be equivalently written
as `Some a` or `(a : Option α)`. In general, we try to settle
on one standard form, called the normal form, and use it both in statements and
conclusions of theorems. In the above examples, this would be `s.Nonempty` (which
gives access to dot notation) and `(a : Option α)`. Often, simp lemmas will be
registered to convert the other equivalent forms to the normal form.

There is a special case to this rule. In types with a bottom element, it is equivalent
to require `hlt : ⊥ < x` or `hne : x ≠ ⊥`, and it is not clear which one would
be better as a normal form since both have their pros and cons. An analogous situation
occurs with `hlt : x < ⊤` and `hne : x ≠ ⊤` in types with a top element. Since it is very
easy to convert from `hlt` to `hne` (by using `hlt.ne` or `hlt.ne'` depending
on the direction we want) while the other conversion is more lengthy, we use `hne` in
*assumptions* of theorems (as this is the easier assumption to check), and `hlt` in
*conclusions* of theorems (as this is the more powerful result to use).
A common usage of this rule is with naturals, where `⊥ = 0`.

## Comments

Use module doc delimiters `/-! -/` to provide section headers and
separators since these get incorporated into the auto-generated docs,
and use `/- -/` for more technical comments (e.g. TODOs and
implementation notes) or for comments in proofs.
Use `--` for short or in-line comments.

Documentation strings for declarations are delimited with `/-- -/`.

See our [documentation requirements](doc.html) for more suggestions
and examples.
