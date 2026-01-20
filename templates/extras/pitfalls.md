# Common Lean Pitfalls

This document lists some common mistakes that Lean users frequently make, as well as unintuitive features of Lean that can lead to errors.

If you find a mistake in this document or would like something added, please write about it on Zulip or open an issue or pull request on the [repository for this website](https://github.com/leanprover-community/leanprover-community.github.io).

## Table of contents
- [Automatic implicit parameters](#automatic-implicit-parameters)
- [Forgetting the Mathlib cache](#forgetting-the-mathlib-cache)
- [Using `have` for data](#using-have-for-data)
- [Rewriting under binders](#rewriting-under-binders)
- [Trusting tactics to unfold definitions](#trusting-tactics-to-unfold-definitions)
- [Using `b > a` instead of `a < b`](#using-b-gt-a-instead-of-a-lt-b)
- [Confusing `Prop` and `Bool`](#confusing-prop-and-bool)
- [Not checking for distinctness](#not-checking-for-distinctness)
- [Not accounting for 0](#not-accounting-for-0)
- [Division by 0](#division-by-0)
- [Integer division](#integer-division)
- [Natural number subtraction](#natural-number-subtraction)
- [Other partial functions](#other-partial-functions)
- [Wrapping arithmetic in `Fin`](#wrapping-arithmetic-in-fin)
- [Real power](#real-power)
- [Distance in `Fin n → ℝ`](#distance-in-fin-n--%E2%84%9D)
- [Accidental double `iInf` or `iSup`](#accidental-double-iinf-or-isup)
- [Trying to extract data from proofs of propositions](#trying-to-extract-data-from-proofs-of-propositions)
- [Working with equality of types](#working-with-equality-of-types)
- [Parameters for instances that already exist](#parameters-for-instances-that-already-exist)
- [Using `Set`s as types](#using-sets-as-types)
- [Sort _](#sort-_)
- [Trying to prove properties about Float](#trying-to-prove-properties-about-float)
- [`native_decide`](#native_decide)
- [Panic does not abort](#panic-does-not-abort)
- [Lean 3 code](#lean-3-code)
- [Non-terminal simp](#non-terminal-simp)
- [Ignoring warnings](#ignoring-warnings)
- [Ambiguous unicode characters](#ambiguous-unicode-characters)
- [Default values in structure fields](#default-values-in-structure-fields)

## Automatic implicit parameters

By default, Lean's [automatic implicit parameters](https://lean-lang.org/doc/reference/latest///Definitions/Headers-and-Signatures/#automatic-implicit-parameters) feature (`autoImplicit` for short) causes unbound variables to be converted to implicit parameters. For example, when this feature is enabled,
```lean
theorem my_theorem : a + 1 = 1 + a := by omega
```
is short for
```lean
theorem my_theorem {a : Nat} : a + 1 = 1 + a := by omega
```

This feature can make your code more concise, but it also means that any typo in a theorem statement could make the theorem statement wrong.
For example, the following statement
```lean
theorem my_theorem (n : Nat) (h : 1 ≤ n) : 0 < m := sorry
```
is false because `m` is an automatic implicit parameter.
The automatic implicit feature makes it hard to see that `m` was typed when `n` should have been typed instead.
In newer Lean versions, you should be able to see an inline `{m}` appear in your text editor next to `my_theorem`, which indicates that `m` is acting as an automatic implicit parameter; it is worth watching for these annotations because they can help you find unintentional uses of `autoImplicit`.

Issues can also manifest in hard to predict ways.
For example, if you haven't yet imported `Mathlib.Data.Nat.Notation`, then in
```lean
theorem my_theorem : ∃ (a b : ℕ), a ≠ b := sorry
```
`ℕ` is actually an automatic implicit variable and can be any type, so this statement is actually false:
```lean
example : False := Exists.elim (my_theorem (ℕ := False)) (fun f _ ↦ f)
```

Automatic implicit parameters are enabled globally by default, but they are disabled if you are working on Mathlib.
If you are new to Lean, I recommend that you disable them and use the `variable`
command instead.
This can be done either by adding
```lean
set_option autoImplicit false
```
at the top of every Lean file right after the `import` statements, or by disabling it globally in your `lakefile.toml` or `lakefile.lean`.

## Forgetting the Mathlib cache

If you are working on `Mathlib` or a project depending on `Mathlib`, opening a file that depends on `Mathlib` or running `lake build` in the terminal may take upwards of an hour to complete the first time it is run.
When Lean files are compiled for the first time, Lean caches the results of the compilation in `.olean` files so that subsequent runs are faster.

Running `lake exe cache get` in the terminal or [invoking "Project: Fetch Mathlib Build Cache" in VSCode](https://github.com/leanprover/vscode-lean4/blob/master/vscode-lean4/manual/manual.md#project-actions) downloads `.olean` files for `Mathlib` from a central server, which prevents you from having to compile them yourself and can save over an hour of compute time.
(You might want to try `lake exe cache get!` if `lake exe cache get` does not work.)
If you find that your project is taking an unusually long amount of time to compile or start in VSCode, it could be because you forgot to run this command.

Note that the decompressed compiled version of Mathlib is over 5 GB large, so make sure you have enough storage space and are connected to a suitable network (and not e.g. a phone hotspot with monthly limits) before downloading the cache.

## Using `have` for data

Sometimes it can be convenient to introduce a new variable to represent a more complicated expression in a proof.
For example, suppose you have a complicated predicate `MyPredicate` and would like to set `x := 37 * n + 42 * m + 76` inside a proof.
If you do this with `have` and then prove `h : MyPredicate x`, you will notice that there's no way to use `h` to close the goal.
```lean
example (n m : Nat) : MyPredicate (37 * n + 42 * m + 76) := by
  have x : Nat := 37 * n + 42 * m + 76
  have h : MyPredicate x := ...
  /- Tactic state is now:
  n m x : Nat
  h : MyPredicate x
  ⊢ MyPredicate (37 * n + 42 * m + 76)
  Now what? -/
```
Additionally, you might be unable to prove `MyPredicate x` if your proof depends on what the value of `x` is.

The problem here is that when you use `have` to create a new variable in a proof, Lean forgets what value you assigned to `have`.
So, after executing `have x : Nat := 37 * n + 42 * m + 76`, the proposition
`x = 37 * n + 42 * m + 76` is now unprovable.

The solution is to use `let` instead of `have` whenever you are introducing a
new variable that is not a proof.
Notice how in the following tactic state, `x` has a value attached to it.
```lean
example (n m : Nat) : MyPredicate (37 * n + 42 * m + 76) := by
  let x : Nat := 37 * n + 42 * m + 76
  have h : MyPredicate x := ...
  /- Tactic state is now:
  n m : Nat
  x : Nat := 37 * n + 42 * m + 76
  h : MyPredicate x
  ⊢ MyPredicate (37 * n + 42 * m + 76)
  -/
```
This means that for the rest of the proof, `x` is definitionally equal to
`37 * n + 42 * m + 76`.
Thus, the type of `h` is definitionally equal to the goal, so we can finish
the proof with `exact h` without having to do any sort of manual conversion.
If you do want access to a proof of `x = 37 * n + 42 * m + 76`, you can get
one with `have hx : x = 37 * n + 42 * m + 76 := rfl`, where `rfl` is a valid
proof of this fact because of the definitional equality.

You may also be interested in the `set` tactic, which is like `let` but
also automatically replaces instances of the expression in the proof state.

## Rewriting under binders

It would be reasonable to expect `rw` to change `0 + i ^ 2` to `i ^ 2` in the following, but unfortunately `rw` fails:
```lean
import Mathlib.Algebra.BigOperators.Group.Finset.Defs

example (s : Finset Nat) : ∑ i ∈ s, (0 + i ^ 2) = ∑ i ∈ s, i ^ 2 := by
  rw [Nat.zero_add]
  /-
  tactic 'rewrite' failed, did not find instance of the pattern in the target expression
    0 + ?n
  s : Finset ℕ
  ⊢ ∑ i ∈ s, (0 + i ^ 2) = ∑ i ∈ s, i ^ 2
  -/
```
This is because `∑ i ∈ s, (0 + i ^ 2)` is shorthand for `Finset.sum s (fun i ↦ 0 + i ^ 2)`, and `rw` sometimes fails to rewrite inside `fun` expressions because it cannot rewrite subexpressions like `0 + i ^ 2` that contain bound variables.

In this case, you can use `simp_rw [Nat.zero_add]` to perform the rewrite, but in some cases you might have to make a precise rewrite using [conversion mode](https://leanprover.github.io/theorem_proving_in_lean4/The-Conversion-Tactic-Mode/):
```lean
example (s : Finset Nat) : ∑ i ∈ s, (0 + i ^ 2) = ∑ i ∈ s, i ^ 2 := by
  conv =>
    lhs
    congr
    · rfl
    · intro i
      rw [Nat.zero_add]
```

## Trusting tactics to unfold definitions

A common mistake in Lean is trying to use tactics like `rw` and `simp` in the hopes that they will "see through" `def`s and `let` statements.
For example, in the following, you might hope that the `rw` would realize that `x` is just shorthand for `0 + n` and rewrite it to `n`, but this doesn't happen:
```lean
theorem mythm (n : Nat) : True := by
  let x := 0 + n
  have : x = n := by
    rw [Nat.zero_add]
    /-
    tactic 'rewrite' failed, did not find instance of the pattern in the target expression
      0 + ?n
    n : Nat
    x : Nat := 0 + n
    ⊢ x = n
    -/
```
Similarly `simp` will also fail here with the error message "simp made no progress".

The solution here is to first `unfold x` or use `change 0 + n = n` before calling `rw [Nat.zero_add]` or `simp`.
You could also use `simp [x]` instead of `simp`.
Finally, if `x` were a `def` instead of a `let`, you could do `rw [x]`, which is equivalent to `rw [show x = 0 + n from rfl]`.
Note that it is important you use `let` and not `have` for `x`; see the section above on using `have` for data.

That being said, it's worth understanding why this is even a problem in the first place.
Recall that there are three main types of equality in Lean: propositional equality, definitional equality, and synctactic equality.
Propositional equality is the normal notion of equality in traditional mathematics, and the proposition `a = b` in Lean refers to propositional equality.
In constrast, definitional and syntactic equality are not things you can prove or disprove; two expressions are either definitionally equal or they aren't, and they are either syntactically equal or they aren't.

A rough way of thinking about this is that two terms are syntactically equal if they are written the same way in Lean, and two terms are definitionally equal if calling `#reduce` on both of them would result in the same expression.
For example, when `n` is an unknown natural number:
- `n + 0` is both syntactically, definitionally, and propositionally equal to `n + 0`.
- `n + 0` is definitionally and propositionally equal to `n` but not syntactically equal. This is because `Nat.add` is defined by recursion on the second argument, so Lean can reduce `n + 0` to `n` even if it doesn't know what `n` is.
- `0 + n` is propositionally equal to `n` but not definitionally or syntactically equal. This is because Lean doesn't know how to reduce `0 + n` when `n` is unknown, so this statement has to be proven by induction.

For more information, please see https://b-mehta.github.io/formalising-mathematics-notes/Part_1/equality.html

Unfortunately, the line between syntactic and definitional equality is often blurred in Lean.
The important thing to remember is that some tactics, such as `exact`, work up to definitional equality, but others such as `rw` and `simp` work up to syntactic equality.
Even though Lean's core typechecker only cares about definitional equality, tactics are free to use the extra information about the syntax of terms to help them operate.

## Using `b > a` instead of `a < b`

Most of the time, `a < b` and `b > a` are definitionally equal in Lean.
But in light of the above discussion about not trusting tactics to unfold definitions, even if two terms are definitionally equal they still might not be interchangable in all circumstances.
For example, this rewrite fails because the right hand side of `Nat.mod_eq_iff_lt` is `m < n`, not `n > m`:
```lean
example {n m : Nat} (h₁ : m % n = m) (h₂ : n ≠ 0) : n > m := by
  rw [←Nat.mod_eq_iff_lt h₂]
```

In Mathlib, `a < b` is preferred over `b > a`.
In fact, `>` hardly even appears at all in Mathlib.
This means that if you want to avoid having to use `gt_iff_lt` all the time, you should prefer `a < b` to `b > a` everywhere in your code.
Similarly, you should prefer `a ≤ b` to `b ≥ a`.
Outside of expressions like `∀ ε > 0, ∃ δ > 0, _` where the `>` is joined with the `∀` or `∃`, it is often best to not use `>` or `≥` at all.

## Confusing `Prop` and `Bool`

The types `Prop` and `Bool` both capture the notion of something being true or false,
but they behave very differently in Lean.
`Prop` is the universe of *propositions*, which are mathematical statements that have a truth value,
while `Bool` is the type of *booleans*; it consists of exactly two elements, `true` and `false`.
Note that `True` and `False` are *propositions*, while `true` and `false` are *booleans*.

Using booleans where propositions are expected or vice versa can lead to some counterintuitive errors. Additionally, because booleans can be implicitly coerced into propositions, the issues that arise might not be immediately apparent.
For example, `a = b` is a proposition, while `a == b` is a boolean (see the `BEq` typeclass), and mixing them up can lead to issues.
It is worth making sure you have a good grasp on the difference between `Prop` and `Bool`.

In Lean, `Prop` and `Bool` are both types, but `Prop` is also a universe while `Bool` is just a regular type containing two elements.
This means that if `p : Prop` and `q : Bool`, then `h : p` might be valid but `h : q` is never valid.
On the other hand, you can use terms of type `Bool` in `match` statements, but you cannot `match` on terms of type `Prop` (the equivalent operation on `Prop` would be the `by_cases hp : p` tactic or the "dependent" if-then-else statement `if hp : p then ... else ...`).
`Bool` is used sparingly in mathematics, but it is used much more often when `Lean` is used as a programming language.

Intuitively, a proposition is a mathematical statement that might be either be proven or disproven.
If `p` is a proposition, it might make sense to say `h : p`, which means that `h` is a proof of `p`.
On the other hand, if `q` is a boolean, then `q` is literally equal to either `true` or `false`; it doesn't make sense to "prove" `q`, because `q` is a value, not a statement.

If you have a boolean `q`, you can convert it to a proposition by writing `q = true`.
Conversely, if `p` is a proposition and if Lean can synthesize an instance of `Decidable p`, then you can convert `p` to a boolean by writing `decide p`.
(Here, the term `decide` should not be confused with the tactic `decide`.)
Since the axiom `Classical.choice` can be used to produce a `Decidable p` instance for any proposition `p`, any proposition can be converted to a boolean, and thus `Prop` and `Bool` are *classically equivalent*.

Despite this, it still makes sense to maintain a distinction between `Prop` and `Bool`.
In mathlib, `Prop` and `Bool` may be assigned different instances for typeclasses; for example, `Prop` is given the Sierpiński space (with `{True}` open) as its topology while `Bool` is given the discrete topology.

## Not checking for distinctness

Consider the following statement of the pigeonhole principle, which states that if $f : A \to B$ is a function betwen finite sets and $|A| > |B|$, then there exists two distinct elements in $A$ which $f$ maps to the same element of $B$:
```lean
import Mathlib.Data.Fintype.Card

variable {A B : Type*} [Fintype A] [Fintype B]

theorem pigeonhole_principle (f : A → B) (h : Fintype.card B < Fintype.card A) : ∃ (x y : A), f x = f y := by
  let a : A := Classical.choice <| Fintype.card_pos_iff.mp (by omega)
  exact ⟨a, a, rfl⟩
```
If you look at the proof, you will notice that it is way too simple.
Notice that the statement of the theorem forgets to require that `x` and `y` be distinct, so all we have to do is to show that there exists some element `a : α` and then we have `f(a) = f(a)` by definition.
This is not a Lean specific issue, but it is more likely to lead to problems down the line in Lean than in informal math.

## Not accounting for 0

Consider the following statement of Fermat's Last Theorem:
```lean
theorem flt (a b c n : Nat) (h : 3 ≤ n) : a ^ n + b ^ n ≠ c ^ n := sorry
```
Unfortunately, this statement is false:
```lean
example : False := flt 0 0 0 3 le_rfl rfl
```

Remember that in Lean, `0 : ℕ`, and that you should account for this case in your theorem statements.
(This is also a case where using Mathlib definitions would have helped:
Mathlib already has a definition `FermatLastTheorem` for the statement of Fermat's Last Theorem, which is much less likely to contain errors.)

## Division by 0

In Lean, `n / 0 = 0`. This is different from other programming languages, where division by zero usually results in an exception.

This means that a statement like
```lean
import Mathlib.Data.Real.Basic

theorem my_theorem : ∃! (x : ℝ), x / (1 + x) = 0 := sorry
```
is actually false, because the equation `x / (1 + x) = 0` has two solutions over the reals in Lean:
```lean
example : False := by
  suffices h : (0 : ℝ) = -1 by aesop
  apply my_theorem.unique <;> simp
```

Division behaves this way because Lean is a pure functional language, so all functions must be total—functions cannot throw exceptions.
In Lean, the preferred way of working with a partial function $f : A \rightharpoonup B$ is to instead define a function $g : A \to B$ such that $g(x) = f(x)$ whenever $x \in \text{dom}(f)$.
The values of $g$ on $A \setminus \text{dom}(f)$ are arbitrary and are usually chosen to be whatever gives the nicest algebraic properties (these values are often known as "junk values").

It is possible to instead define division like
```lean
def div (a b : ℝ) (h : b ≠ 0) : ℝ := ...
```
but in practice, providing a proof that the demoninator is nonzero every time we want to divide two numbers gets tedious very quickly.
In contrast, *theorems* involving division usually have a hypothesis stating that the denominator is nonzero.
It is recommended to add hypotheses making sure your denominator is nonzero to your own theorems, unless you have carefully thought through the case where the denominator is zero.
For more information, please see [this Xena project blog post](https://xenaproject.wordpress.com/2020/07/05/division-by-zero-in-type-theory-a-faq/).

## Integer division

When dividing two `Int`s or `Nat`s in Lean, the result is always rounded down (this is slightly different behavior from most languages, which round towards zero).
This is so that using division does not cause the type of the number being worked with to change.
For example, the following statement is false:
```lean
import Mathlib.Algebra.Field.Rat
import Mathlib.Algebra.Order.Ring.Rat

def thm₁ (n : ℤ) (h : 2 < n) : (1 / n) < (1 / 2) := by
  /-
  ===================
  Found a counter-example!
  n := 3
  guard: 2 < 3
  issue: 0 < 0 does not hold
  (0 shrinks)
  -------------------
  -/
  plausible
```

But at the same time, you might not want to rely on this behavior. For instance, this theorem is actually true:
```lean
def thm₂ (n : ℚ) (h : 2 < n) : (1 / n) < (1 / 2) := by
  simp [inv_strictAnti₀ rfl h]
```
In this example, the left hand side of the `<` is a rational number, so Lean interprets the right hand side as a rational number so integer division no longer applies.
This is similar to what happens in the following:
```lean
#eval (1 / 2) + 0 -- 0
#eval (1 / 2) + (0 : ℚ) -- (1 : Rat)/2
```

This may surprise you if you're used to languages like Java where `(1 / 2) + 0.0` evaluates to `0.0` because in Java type information outside parentheses usually does not affect what happens inside the parentheses.

In general, it is hard to determine the presence or absence of integer division.
It is also possible that Lean's behavior with respect in the most recent example might change in the future.

If this concerns you, you may want to consider adding `set_option pp.numericTypes true` near the top of your file, so that numeric literals are annotated with their corresponding
type (e.g. `ℕ`, `ℤ`, `ℚ`, `ℝ`, `ℂ`) when they are displayed in the infoview.

## Natural number subtraction

Subtraction of natural numbers truncates at `0` because we want the return type of natural subtraction to be `Nat`. That is, we have
```lean
#eval 5 - 3 -- 2
#eval 5 - 7 -- 0
#eval 10 - 100 + 100 -- 100
#eval 5 - 13 + 11 + 0 -- 11
```
As explained above in the integer division section, type annotations can affect which operations are performed:
```lean
#eval 10 - 100 + (100 : Int) -- 10
#eval 5 - 13 + 11 + (-0) -- 3
```

Trucating subtraction is also known as [monus](https://en.wikipedia.org/wiki/Monus).

One place where natural number subtraction might arise is if you have a predicate `P : Nat → Prop` and want to show that `P n` holds for all `n ≥ 1`.
If you try to prove
```lean
theorem mythm {n : Nat} (hn : 1 ≤ n) : P n := ...
```
you might find that the proof of `mythm` requires you to frequently refer to `n - 1`.
Even though no truncation occurs here, this statement may still be tedious to prove because automation often does not work well with natural number subtraction.
In many cases, it makes sense to instead prove
```lean
theorem mythm (n : Nat) : P (n + 1) := ...
```
because this completely avoids natural number subtraction.
More generally, you can often rephrase a statement that involves natural number subtraction to one that doesn't.
Additionally, in a lot of cases, the latter phrasing of `mythm` is easier to use than the former phrasing.

## Other partial functions

You should also be aware that many other functions in Mathlib use junk values.
For example,
- `deriv f s x = 0` if `f` is not differentiable at `x` within `s`.
Similarly, the Fréchet derivative `fderiv` returns the 0 linear map when
`f` is not differentiable at the given point.
You might need to add `HasDerivAt` or `HasFDerivAt` to your theorems' hypotheses.
- The "topological sum" `tsum f`, also denoted `∑' i, f i`, computes the sum of a series, or returns 0 if the sum does not converge.
Consider adding `Summable f` hypotheses to theorems that involve `∑' i, f i`.
  - Note that because `tsum` does not assume an order structure on the domain, only unconditionally converging series are considered `Summable`.
  Intuitively, a series is unconditionally convergent if it doesn't matter which order you take the sum.
  For example, the alternating harmonic series is *not* `Summable` because it is only conditionally convergent.
  (By the [Riemann series theorem](https://en.wikipedia.org/wiki/Riemann_series_theorem), a real valued series is *unconditionally convergent* if
  and only if it is *absolutely convergent*.
  In general, unconditional convergence is weaker than absolute convergence: If $(e_n)_{n \in \mathbb{N}}$ is an orthonormal basis of an countably-infinite dimensional Hilbert Space, then $\sum (e_n)/n$ converges unconditionally, but not absolutely.)
- `tprod f` (denoted `∏' i, f i`) is similar to `tsum`, but the junk value is `1` instead of `0`.
- `Nat.sqrt x` takes the floor of $\sqrt{x}$.
- `Real.sqrt x` is `0` for negative inputs.
- `Real.log x` actually means $\log_e |x|$ when $x \ne 0$ and is $0$ when $x = 0$.
This gives nicer algebraic properties than setting it to be $0$ for all negative $x$.
- `Real.sSup` and `Real.iSup` are 0 if the set is empty or not bounded above, and likewise `Real.sInf`, and `Real.iInf` are 0 if the set is empty or not bounded below.
This interacts nicely with `Real.sqrt`: it means that $\sqrt{x} = \sup \{y \mid y^2 < x\}$ for all $x \in \mathbb{R}$, since when $x \le 0$ both sides are $0$.

## Wrapping arithmetic in `Fin`

Arithmetic in `Fin` wraps around if it overflows or underflows:
```lean
#eval (7 : Fin 10) + 6 -- 3
#eval (7 : Fin 10) * 6 -- 2
#eval (2 : Fin 10) - 8 -- 4
```
This applies to literals as well:
```lean
#eval (15 : Fin 10) -- 5
#eval (10 : Fin 10) -- 0
```
Note that even though `Fin n` uses the same notion of addition, subtraction, and multiplication as `ZMod n` for positive `n`, they are not exactly the same because `Fin n` is ordered while `ZMod n` is unordered and `Fin n` uses truncating integer division while `ZMod n` uses the "mathematically correct" notion of division on $\mathbb{Z}/n\mathbb{Z}$ whenever $n$ is prime.
Also `Fin 0` is empty while `ZMod 0 = Int` (this is so that `ZMod n` is always a ring of characteristic `n`, because empty types cannot be rings).

One reason that `Fin` uses wrapping arithmetic instead of something like saturating arithmetic is that it is used to represent native fixed-width integer types like `UInt32`, and the operations on `Fin` need to agree with the overflow and underflow of machine-native arithmetic.

## Real power

`Real.rpow x y` is defined somewhat arbitrarily for negative `x`.
In particular, it is defined as the real part of the complex exponentiation function, which is itself somewhat arbitrary as it depends on the complex logarithm.
This gives the function nice analytic properties, but it also means that taking roots of negative numbers can be unintuitive.
For example, the value of `(-125 : ℝ) ^ (1/3 : ℝ)` is $5\cos(\pi/3)$, and not $-5$ like you might have expected.

## Distance in `Fin n → ℝ`

In many cases, `Fin n → ℝ` is the recommended way to represent $\mathbb{R}^n$ in Lean.
Vectors of this type can be written using the `![x,y,z,...]` notation.
But note that in Lean, if $(S_i)_{i \in I}$ is a finite family of (pseudo)metric spaces, then $\prod_{i \in I}S_i$ uses the $L^\infty$ metric:
$$
\text{dist}(\textbf{x},\textbf{y}) = \sup\left\{ \text{dist}(x_i,y_i) \mid i \in I\right\}
$$
and `Fin n → ℝ` is a special case of this.

This means that the distance between $(1,0)$ and $(0,1)$ is actually $1$:
```lean
import Mathlib.Analysis.InnerProductSpace.PiL2

example : dist ![(1 : ℝ),0] ![0,1] = 1 := by
  rw [dist_pi_eq_iff (by positivity)]
  constructor
  · use 0
    simp
  · intro b
    fin_cases b <;> simp
```

To instead use the standard Euclidean metric (also called the $L^2$ metric), you must use `EuclideanSpace ℝ (Fin n)`, which is an abbreviation for `WithLp 2 (Fin n → ℝ)`. Vectors of this type can be written using the `!₂[x,y,z,...]` notation.
```lean
example : dist !₂[(1 : ℝ),0] !₂[0,1] = √2 := by
  norm_num [EuclideanSpace.dist_eq]
```

One consequence of this is that `Fin n → ℝ` is not registered as an inner product space,because the norm corresponding to the inner product would disagree with the existing $L^\infty$ norm.
If you need $\mathbb{R}^n$ as an inner product space, use `EuclideanSpace ℝ (Fin n)`.

## Accidental double `iInf` or `iSup`

You might expect `⨅ x > 2, (x : ℝ) ^ 2` to be equal to `4`, because the image of `(2,∞)` under `fun x : ℝ ↦ x ^ 2` is `(4,∞)`. But in Lean, this expression actual equals `0`:

```lean
import Mathlib.Data.Real.Archimedean
import Mathlib.Order.ConditionallyCompleteLattice.Indexed

-- The infimum of x^2 on (2,∞) is ... 0?
example : ⨅ x > 2, (x : ℝ) ^ 2 = 0 := by
  set f := fun x : ℝ ↦ ⨅ (h : x > 2), x ^ 2
  have hf₁ (x : ℝ) : f x = if _ : x > 2 then x ^ 2 else sInf ∅ := ciInf_eq_ite
  have hf₂ : f 0 = 0 := by simp [hf₁]
  have hf₃ (x : ℝ) : 0 ≤ f x := by
    rw [hf₁]
    split_ifs <;> simp [sq_nonneg]
  apply le_antisymm
  · rw [←hf₂]
    refine ciInf_le ?_ 0
    rw [bddBelow_iff_exists_le 0]
    use 0
    simp [hf₃]
  · simp [le_ciInf, hf₃]
```

The reason for this is that `⨅ x > 2, (x : ℝ) ^ 2` is shorthand for `⨅ (x : ℝ) (h : x > 2), x ^ 2`, which is shorthand for `⨅ (x : ℝ), ⨅ (h : x > 2), x ^ 2`.
Note that:
- When `x > 2`, `⨅ (h : x > 2), x ^ 2` means `⨅ (h : True), x ^ 2` which equals `x ^ 2`.
- When `x ≤ 2`, `⨅ (h : x > 2), x ^ 2` means `⨅ (h : False), x ^ 2` which equals
`sInf (∅ : Set ℝ)`.
In traditional math, $\inf \varnothing$ over the reals is usually undefined or defined to equal $+\infty$. But in Lean, `sInf (∅ : Set ℝ) = 0` (see the partial functions section above for an explanation).

So, in summary, `⨅ x > 2, (x : ℝ) ^ 2` equals `⨅ (x : ℝ), f x` where
$$
f(x) = \begin{cases} x^2 &\text{ for } x > 2 \\ 0 &\text{ for } x \le 2 \end{cases}
$$
and the infimum of this function is `0`.

A similar situation arises for sets. `⨅ x ∈ s, f x` is shorthand for `⨅ x, ⨅ (_ : x ∈ s), f x` and might not be the same as `⨅ x : ↑s, f ↑x` (where the index type is `s` coerced to a type).
Additionally, everything in this section applies as much to `iSup` as it does to `iInf`.

`⨅` and `⨆` behave this way for consistency with other binders such as `∀` and `∃`:
`∀ x ∈ s, p x` is shorthand for `∀ x, ∀ h : x ∈ s, p x` and `∃ x ∈ s, p x` is shorthand for `∃ x, ∃ h : x ∈ s, p x`.
However, there have been discussions about possibly changing this behavior in the future: see [this discussion on Zulip](https://leanprover.zulipchat.com/#narrow/channel/287929-mathlib4/topic/sup.20and.20inf.20over.20sets/with/472565284).

## Trying to extract data from proofs of propositions

Given a proof `h : ∃ n : Nat, p n`, you may wish to extract the particular `n` for which `p n`
holds.
Or given a term `q : Nonempty Nat` you may wish to obtain the particular `Nat` used to construct `q`.
In each of these cases, it is possible to extract an *arbitrary* `n : Nat` from `h` or `q`, but obtaining the *particular* `n` used in `h` or `p`'s construction is impossible.

To understand why, first recall that Lean has a single universe hierarchy `Sort 0`, `Sort 1`, `Sort 2`, `Sort 3`, ...,
and that `Prop` is shorthand for `Sort 0`, `Type` is shorthand for `Sort 1`, `Type 1` is shorthand for `Sort 2`, etc.
The distinction between `Prop` and `Type u` exists because `Prop` has some special behavior which sometimes requires us to treat it distinctly from the rest of the universes.
The two most important special properties of `Prop` are *impredicativity* and *proof irrelevance*.
In this section, I will mainly discuss the consequences of proof irrelevance.

In essence, proof irrelevance states that every proposition has at most one proof; that is, any two proofs of the same proposition are equal.
Another way to state this is that every proposition is a *subsingleton*—a type with zero or one elements.
The way proof irrelevance is implemented in Lean is that if `P : Prop` and `p : P` and `q : P`, then `p` and `q` are defintionally equal, so `rfl : p = q`.
This is a built-in rule in Lean's type theory, and should not be confused with `propext`, which is an axiom that states that if `P Q : Prop` and `P ↔ Q`, then `P = Q`.

To see why this rule is necessary, recall that an element of the subtype `{x : X // p x}` is of the form `{ val := x, property := h }` where `x` is an element of `X` and `h` is a proof that `p x`. If we defined
```lean
def x : {n : Nat // 4 < n} := { val := 8, property := Nat.lt_of_sub_eq_succ rfl }
def y : {n : Nat // 4 < n} := { val := 8, property := by omega }
```
then `x` and `y` have the same value, but have different proofs.
We would like `x` and `y` to be equal despite their different proofs, and it would be very convenient if they were even definitionally equal, and it is proof irrelevance that makes this possible:
```lean
example : x = y := rfl
```

Because of proof irrelevance, when a proof `h : ∃ n : Nat, p n` is constructed, it "forgets" which `n` was used to prove it.
If there were some function `f : (∃ n : Nat, p n) → Nat` which extracted the natural number used in `h`'s construction, then we could make two different proofs `h₁ h₂ : ∃ n : Nat, p n` for which `f h₁ ≠ f h₂` but `h₁ = h₂` holds by proof irrelevance.
This would be a contradiction, so no such `f` exists.

More generally, when you define an inductive type `T` that lives in `Prop`, the return type of `T.rec` is only allowed to live in `Prop`.
Practically speaking, this means that while the function
```lean
def swap {P Q : Prop} (h : P ∨ Q) : Q ∨ P :=
  match h with
  | Or.inl hp => Or.inr hp
  | Or.inr hq => Or.inl hq
```
is allowed because the return type of the match expression lives in `Prop`, the function
```lean
def bad {P Q : Prop} (h : P ∨ Q) : Nat :=
  match h with
  | Or.inl hp => 1
  | Or.inr hq => 2
```
is not allowed, because the return type of the match expression lives in `Type`.
Note that some inductive propositions, known as *syntactic subsingletons*, are exempt from this limitation via a process known as *subsingleton elimination*.

If you must extract data from a proposition, there are a couple of things you can do:
- If you are extracting data in the middle of the proof of a proposition (as opposed to a `def` in `Type` or higher), then tactics like `cases` and `obtain` will work like normal. You can also apply eliminators like `Exists.elim` and `Nonempty.elim`, which only let you eliminate to propositions.
- If you just need to extract an *arbitrary* `α` out of a proof `h : Nonempty α`, you can use the axiom `Classical.choice` to do so. Note that no properties can be proven about the output of `Classical.choice` aside from the fact that it lives in `α`. For example, if you use `Classical.choice` on a proof `h : Nonempty Nat` to produce an element `n : Nat`, then statements like `n = 37` are neither provable nor disprovable in Lean.
Additionally, if you write code whose behavior depends on the value of `n`, then you will be forced to mark such code as `noncomputable`.
- If you instead have an element `h : ∃ n : Nat, p n`. then you can use `Classical.choose` to get an element `n : Nat` and `Classical.choose_spec` to get a proof of `p n`.
`Classical.choose` and `Classical.choose_spec` are defined internally by using `Classical.choice` to produce an element of `{n : Nat // p n}`, so the same stipulation about computability applies.
- If you need to depend on the *particular* value used in the proof of `∃ n : Nat, p n`, you should probably avoid the `Exists` type entirely and exhibit an element of `{n : Nat // p n}` instead.
`∃ n : Nat, p n` and `{n : Nat // p n}` both consist of a `n : Nat` and a proof that `p n`; their only different is which universe the type lives in.
- If you are working over `Nat`, and you have a `h : ∃ n : Nat, p n` where `p` is a `DecidablePred`, then you can use `Nat.find` and `Nat.find_spec` similar to `Classical.choose` and `Classical.choose_spec`.
`Nat.find` is computable, although it may not be particularly efficent since evaluating `Nat.find h` will check every natural number in order starting at 0 until it finds the smallest one satisfying `p`.

## Working with equality of types

Equality of types is poorly behaved in Lean's type theory.
If `A` and `B` are distinct inductive types or structures in `Type u`, and if `A` and `B` have the same cardinality, then the statement `A = B` is neither provable nor disprovable in Lean.
For example, `Int = Nat` is neither provable nor disprovable.
For more information, please read Jason Rute's and Andrej Bauer's answers to this question: https://proofassistants.stackexchange.com/q/4046

Roughly speaking, the only time that you can prove two types are equal is if
they were defined from the same irreducible types. For example, `Fin n = Fin m` is provable when `n = m`, but `Fin 2 = Bool` is not provable.
The only time that you can prove that two types are *not* equal is if they have different cardinalities. So, `Fin 3 ≠ Bool` is provable, but `Fin 2 ≠ Bool` is not provable.
The exception is `Prop`, where the axiom `propext` can be thought of as saying that two `Prop`s are equal if they have the same cardinality.

If you *are* able to prove that `A = B`, then you can use `cast` to convert an element of `A` to an element of `B`.
But reliance upon `cast` often causes problems down the line and can lead to the poorly behaved `HEq`.
Usually, instead of working with equality of types, it is much better to work with a suitable type of isomorphisms (or `Equiv` if you are not working with any sort of algebraic or topological structure).
Alternatively, if you are working with equality of `Subtype`s of `α`, you might want to instead work with elements of `Set α`.
Equality in `Set α` is well-behaved.

## Parameters for instances that already exist

A common mistake is introducing `variable`s or parameters for instances that already exist.
For instance, in the following theorem statement, note that the `[Ring ℤ]` is unnecessary because `ℤ` already has a `Ring` instance available.
```lean
import Mathlib.Algebra.Equiv.TransferInstance
import Mathlib.Algebra.Field.ZMod
import Mathlib.Algebra.Polynomial.Cardinal

theorem my_theorem [Ring ℤ] : CharZero ℤ := sorry
```

In fact as stated, this statement says that *every* ring on $\mathbb{Z}$ has characteristic 0, which is false because there exist countably infinite rings (e.g. $(\mathbb{Z}/2\mathbb{Z})[X]$) with nonzero characteristic.
The following proof is by Bhavik Mehta:
```lean
open Cardinal in
theorem bad : False := by
  have e1 : #(Polynomial (ZMod 2)) = ℵ₀ := by simpa using (Cardinal.nat_lt_aleph0 2).le
  have e2 : #ℤ = ℵ₀ := by simp
  obtain ⟨e⟩ := Cardinal.eq.1 (e2.trans e1.symm)
  let i : Ring ℤ := e.ring
  cases @Nat.cast_injective _ _ my_theorem 2 0 rfl
```

One symptom of this is that you might encounter expressions which look identical in the infoview but are not actually equal, resulting in tactics like `rfl`, `apply`, and `rw` failing with cryptic messages.
For example, the tactic state below shows that the goal is to prove `dist 0 1 = dist 0 1` and you have to click three levels deep into the `dist` function on the right to find out that it is using the wrong instance.
```lean
import Mathlib.Topology.MetricSpace.Basic

example [inst : MetricSpace ℝ] : dist (0 : ℝ) 1 = inst.dist (0 : ℝ) 1 := by
  /-
  Tactic state:
  1 goal
  inst : MetricSpace ℝ
  ⊢ dist 0 1 = dist 0 1
  -/
  sorry
```
In this particular case, trying `rfl` will give you the error message
```
tactic 'rfl' failed, the left-hand side
  @dist ℝ (@PseudoMetricSpace.toDist ℝ Real.pseudoMetricSpace) 0 1
is not definitionally equal to the right-hand side
  @dist ℝ (@PseudoMetricSpace.toDist ℝ MetricSpace.toPseudoMetricSpace) 0 1
inst : MetricSpace ℝ
⊢ dist 0 1 = dist 0 1
```
from which you can conclude that the type classes do not match. When tactics such as `congr` or `convert` generate subgoals, it is often worth running `rfl` on those goals to see if they were caused by mismatching typeclass instances.

In actual code, you probably would not write `inst.dist` by accident, but in more complicated examples the bad instances can manifest in hard to detect ways.

Thank you to Edward van de Meent for suggesting that I include this topic and finding a misleading statement, and to Bhavik Mehta to working out the details of the proof that the first example was `False`.

## Using `Set`s as types

In Lean, `Set X` is defined as `X → Prop`, so sets are predicates, not types. However, there is an implicit coercion from `Set X` to `Type u`, so if you have parameters `(X : Type) (s : Set X) (a : s)`, the `(a : s)` really means `(a : {x : X // x ∈ s})`.
Here, `{x : X // x ∈ s}` is notation for `Subtype (fun x ↦ x ∈ s)`.

That is, `a` is really a pair `⟨x, hx⟩` where `x : X` and `hx` is a proof that `x ∈ s`.
So, `a` is not actually an element of `X`, but you might not realize this because there is another implicit coercion from `{x : X // x ∈ s}` to `X` which makes `a` behave like an element of `X` in some, but not all, circumstances.

This can lead to various issues. For example,
```lean
import Mathlib.Data.Set.Basic

example (s : Set ℕ) (n : s) : 0 + n = n := by
  sorry
```
fails to compile because Lean does not know what `0 + n` means, since technically `n` is not a natural number.
You have to write `(n : ℕ)` to make the addition succeed.

Additionally, if you try proving this by induction on `n`, you may find that your tactics do not do what you expect.
```lean
import Mathlib.Data.Set.Basic
import Mathlib.Tactic

example (s : Set ℕ) (n : s) : 0 + (n : ℕ) = n := by
  /- Tactic state before:
  s : Set ℕ
  n : ↑s
  ⊢ 0 + ↑n = ↑n
  -/
  induction' n with d hd
  /- Tactic state after:
  s : Set ℕ
  d : ℕ
  hd : d ∈ s
  ⊢ 0 + ↑⟨d, hd⟩ = ↑⟨d, hd⟩
  -/
```
Here, the tactic did not perform induction on `n` as a natural number; instead, it deconstructed the two components of the `Subtype`.
If you had instead tried to use the unprimed `induction` tactic, you would have gotten an "invalid alternative name 'zero', expected 'mk'" error message.

Note the presence of the `↑` in the tactic states. This represents a coercion, and it is one clue that the type of `n` might not be what you think it is.

Because of these problems and others, if you have `(s : Set X)` as a parameter and you want to assume that `a` is an element of `s`, it is often better to add two parameters `(a : X) (ha : a ∈ S)` than to write `(a : s)`.
Similarly, if you want `t` to be a subset of `s`, you should declare `(t : Set X) (h : t ⊆ s)` rather than `(t : Set s)`.
Using this coercion from `Set`s to types should usually be reserved for cases where you need to pass in a `Set` to another function that requires a type as input.

Mathlib's algebra library has been designed with this in mind. For example,
`Subgroup` is defined like
```lean
structure Subgroup (M : Type*) [Group M] where
  carrier : Set M
  mul_mem {a b} : a ∈ carrier → b ∈ carrier → a * b ∈ carrier
  one_mem : (1 : M) ∈ carrier
  inv_mem {x} : x ∈ carrier → x⁻¹ ∈ carrier
```
This is so that if you have a `H : Subgroup G`, then you can work with elements of `H` by declaring `x : G` and `hx : x ∈ H` instead of having to write `x : H` and deal with `x` not actually having type `G`.

## Sort _

Writing `Sort _` and `Type _` causes Lean to fill in the universe level parameter automatically.
Sometimes, this results in Lean specializing the universe level more than you might have anticipated.
For example, in
```lean
import Mathlib.Data.Countable.Defs

example (α : Sort _) (x y : α) (_ : Countable α := inferInstance) : x = y := by
  rfl
```
the `inferInstance` default argument finds `Prop.countable`, which causes `Sort _` to be restricted to `Prop`.
So, `α : Prop`, which means that `x : α` and `y : α` are definitionally equal due to proof irrelevance.

In older Lean versions, this behavior was even more likely to trigger, because code after the `:=` could affect what `Sort _` was.
For example, the following code compiles in Lean 4.8.0:
```lean
example {α : Sort _} (x y : α) : x = y := by
  have := α ∧ α -- Force α to have type Prop
  rfl
```

Because of this behavior, it is recommended to either use `Sort*` or `Type*` (which are stricter versions of `Sort _` and `Type _` that force Lean to generate a new universe parameter each time they are used) or to specify the universe parameter explicitly.

## Trying to prove properties about Float

By default, entering a number like `5.42` creates a term of type `Float` rather than `Rat` or `Real`.
It is very difficult to prove properties about `Float`.
This is because within the mathematical portion of Lean, `Float` is defined as an opaque type and `Float = Unit` is consistent with Lean's core type theory (as long as `native_decide` is not used).
But computationally, `Float` follows the IEEE 754 *binary64* format, which is like `double` in C or `f64` in Rust.
(See `Float32` for 32-bit floating point numbers.)
This means that to prove anything meaningful about `Float`, you have to use `native_decide`, which is a risky tactic (see the section in this document on `native_decide`).

Additionally, because of the behavior of floating point numbers, `0.1 + 0.2 == 0.3` evaluates to `false`.
(See <https://0.30000000000000004.com/> for an explanation.)

So, if you are not interested in using Lean as a programming language or otherwise want to prove complicated properties about the numbers you work with, you should avoid `Float` and use another numeric type such as `Rat` or `Real`.

## `native_decide`

`native_decide`, also written as `decide +native`, is similar to the `decide` tactic except it uses `#eval` to run the decision procedure instead of reducing it in the kernel.
This has the potential to be much faster than `decide`, and it is the only way to prove properties about `Float` and some other opaque types, but it is risky because it trusts the Lean compiler, which is much more complicated and likely to contain a bug than the Lean kernel.

In particular, using `native_decide` makes your theorem depend on the `Lean.ofReduceBool` axiom, which states that the Lean compiler is trustworthy.
You can check whether a proof relies on this axiom by using `#print axioms`.
In addition to trusting the compiler, `Lean.ofReduceBool` also trusts all `@[extern]` and `@[implemented_by]` annotations as well as other extensions to the compiler.
Since there are hundreds of these annotations in Lean core, at the present moment `native_decide` is almost certainly capable of proving `False`.
It will also trust your `@[extern]` and `@[implemented_by]` annotations without keeping track of them:
```lean
def m := 37

@[implemented_by m]
def n := 22

#reduce n -- 22
#eval n -- 37

theorem bad : False := by
  have : n = 22 := by decide
  have : n = 37 := by native_decide
  contradiction

#print axioms bad -- 'bad' depends on axioms: [Lean.ofReduceBool]
```

Code contributed to Mathlib is not allowed to use `native_decide`.

## Panic does not abort

If you are using Lean as a programming language, note that the `panic!` macro does not trigger a crash by default; instead, it just just prints an error message and lets the code keep running.
This applies to functions like `Option.get!` as well. `panic` behaves this way because it is a safe function, and it is formally equivalent to `default`.

This can be dangerous if you are using panic to guard potentially dangerous `IO` operations or prevent data corruption.
You may want to consider setting the environment variable `LEAN_ABORT_ON_PANIC` to `1`, although this might not be sufficient for user facing applications where environment variables are hard to control.

## Lean 3 code

Lots of Lean 3 code can be found on the internet, and LLMs frequently generate Lean 3 code instead of Lean 4 code.
If you are reading old Lean code or using an LLM, and you see details such as
- Names of types, like `nat` and `rat` starting with a lowercase letter
- Lowercase imports like `import data.real.basic` that don't start with a library
name (the Lean 4 equivalent is `import Mathlib.Data.Real.Basic`).
- Usage of `begin` and `end` to surround tactic mode instead of `by`
- Plural commands like `variables` and `universes` when introducing 2 or more variables or universes
- The `rw` tactic without square brackets
- The `refl` tactic (which is spelled `rfl` in Lean 4)

then the code you are reading is probably Lean 3 code (or, if you are using an LLM, it could be an incoherent mix of Lean 3 and Lean 4).
Lean 3 and Lean 4 are very different languages, so Lean 3 code will not work in Lean 4.

## Non-terminal simp

This is not something you need to be concerned about when writing proofs for the first time, but if you are trying to tidy up a proof, perhaps so that it can be added to a library like mathlib, then note that using `simp` in the middle of a tactic block is considered bad practice.
In the following
```lean
example : ... := by
  ...
  simp
  rw [...]
  exact h
```
the usage of `simp` is considered *non-terminal*.

Non-terminal `simp`s create maintainability issues.
In general, `simp` will become more powerful over time as more lemmas are added to mathlib, and that means that the goal state after `simp` can change when code in other parts of the library changes, potentially breaking any tactics that come after `simp`, such as the `rw` in this example.
In the less common cases where lemmas are removed from mathlib, both terminal `simp`s and non-terminal `simp`s can break, but it is usually much easier to fix a terminal `simp` call.

To avoid non-terminal `simp`s, you can use a simp variant like `simpa` or `simp_rw` to combine `simp` with the tactics that come after it, or you can "squeeze" your simp calls by using `simp?`.
Note that it is fine for `simp` to appear in the middle of a proof as long as it fully closes a goal.
For example, even though the `simp` in
```lean
  induction n with
  | zero =>
    simp
  | succ d hd =>
    ...
```
is in the middle of the proof, it is not considered a non-terminal simp because it fully closes a goal.

For more information, see [these notes about non-terminal simps](simp.html#non-terminal-simps).

## Ignoring warnings

Pay close attention to warnings in your Lean files.
An unused variables warning in a completed theorem could mean that not all hypotheses were used, which usually indicates that the theorem statement was wrong.
Similarly, a warning that a declaration uses sorry when you did not type `sorry` yourself could indicate that a tactic failed and closed the proof with a synthetic sorry silently.

If you are certain that a warning does not apply, you can disable it with an appropriate usage of `set_option`.
This is better programming practice than ignoring the warnings and leaving others (or your future self!) to guess which warnings are expected and which you should be concerned about.

Note that the `#lint` command (defined in `Batteries`) can detect some common issues,
such as syntactic tautologies.
It will only check parts of the file above the `#lint` command, so it should
be run at the end of the file.

## Ambiguous unicode characters

Lean makes extensive use of non-ASCII unicode characters, but a side effect of this is that many characters look similar but have very different functionality in Lean.
If you are using VSCode with the Lean 4 extension, you can hover over unfamiliar characters to see instructions on how to type them.

Some characters that are often confused include:

Character | Unicode Name | How to type | Usage in Lean
--- | --- | --- | ---
`\|` | Vertical Line (U+007C) | ASCII character | Set builder notation; Pattern matching, Absolute value
`∣` | Divides (U+2223) | `\\|`, `\dvd`, `\mid`, `\shortmid` | Divisibility
`Π` | Greek Capital Letter Pi (U+03A0) | `\p`, `\P`, `\Pi` | Dependent function type: `Π x : α, β x` is another way to write `(x : α) → β x`
`∏` | N-Ary Product (U+220F) | `\prod` | Indexed products: see `BigOperators.bigprod`
`⊓` | Square Cap (U+2293) | `\inf`, `\meet`, `\glb`, `\sqcap` | Infimum of two elements: `a ⊓ b` means `min a b`. See the `Min` typeclass, which is used even when the order is not linear
`⨅` | N-Ary Square Intersection Operator (U+2A05) | `\infi`, `\Glb`, `\Inf`, `\Meet`, `\Sqcap`, `\bigglb`, `\biginf`, `\bigmeet`, `\bigsqcap` | Indexed infimum operation, requires the `InfSet` typeclass.
`Σ` | Greek Capital Letter Sigma (U+03A3) | `\S` `\GS`, `\Sigma` | The `Sigma` (aka dependent pair/dependent sum) type
`∑` | N-Ary Summation (U+2211) | `\sum` | Indexed summations: see `BigOperators.bigsum`
`×` | Multiplication Sign (U+00D7) | `\x`, `\times`, `\multiplication` | Cartesian product of types
`x` | Latin Small Letter X (U+0078) | ASCII character | No special function
`X` | Latin Capital Letter X (U+0058) | ASCII character | Normally no special function; when the `Polynomial` namespace is open, represents the polynomial variable/indeterminant
`*` | Asterisk (U+002A) | ASCII character | Multiplication
`∨` | Logical Or (U+2228) | `\v`, `\or`, `\vee` | The Or symbol: `a ∨ b` means `Or a b`
`\/` | | ASCII characters | ASCII alternative for the Or symbol `∨`
`v` | Latin Small Letter V (U+0076) | ASCII character | No special function
`·` | Middle Dot (U+00B7) | `\.`, `\centerdot` | Indenting and focusing on subgoals in tactic mode; Anonymous function syntax like `(· + 2)`, which is short for `fun x ↦ x + 2`
`•` | Bullet (U+2022) | `\smul`, `\bub`, `\bu` | scalar multiplication or left action (see the `HSMul` and `SMul` typeclasses)
`⬝` | Black Very Small Square (U+2B1D) | `\cdot`, `\dot`, `\tr`, `\con` | used only in `u ⬝ᵥ w = dotProduct u w` (enter `ᵥ` with `\_v`)
`→` | Rightwards Arrow (U+2192) | `\r`, `\imp`, `\->`, `\to`, `\r-`, `\rightarrow` | Function type `A → B`
`->` | | ASCII characters | ASCII alternative to `→` for function types
`↦` | Rightwards Arrow From Bar (U+21A6) | `\mapsto`, `\\|->`, `\r-\|` | Used in Lambda binders like `fun x : Nat ↦ x + 2`
`=>` | | ASCII characters | Pattern matching; ASCII alternative to `↦`
`⟶` | Long Rightwards Arrow (U+27F6) | `\hom`, `\-->`, `\longrightarrow`, `\r--` | `a ⟶ b` is the type of morphisms from `a` to `b` in a category or quiver: see `Quiver.Hom`.
`↪` | Rightwards Arrow With Hook (U+21AA) | `\hookrightarrow` | `α ↪ β` is the type of injective functions from `α` to `β`: see `Function.Embedding`
`=` | Equals Sign (U+003D) | ASCII character | Equality between objects: see `Eq`
`==` | | ASCII characters | Boolean equality: see `BEq`. Boolean equality is type-dependent, but if a `LawfulBEq` instance exists, `BEq` agrees with `Eq`.
`≃` | Asymptotically Equal To (U+2243) | `\equiv`, `\~-`, `\simeq` | Bijections: `α ≃ β = Equiv α β` is the type of functions from `α → β` equipped with a two-sided inverse; `≃o`, `≃r`, etc. instead refer to specific types of isomorphisms.
`≅` | Approximately Equal To (U+2245) | `\iso`, `\~=`, `\cong` | Isomorphisms in a category; when `open scoped Congruent` is active, refers instead to `Congruent`.
`≈` | Almost Equal To (U+2248) | `\~~`, `\approx`, `\thickapprox` | Type-dependent equivalence notation: see `HasEquiv`. Usually refers to a typeclass inferred `Setoid` instance
`~` | Tilde (U+007E) | ASCII character | Permutation equivalence relation for `List`s, `Array`s, and `Vector`s; some special meaning for other types
`≡` | Identical To (U+2261) | `\==` | `a ≡ b [MOD n]` means `Nat.ModEq n a b` and `a ≡ b [ZMOD n]` means `Int.ModEq n a b`. Some special meaning for other types

## Default values in structure fields

Users often assume that the use of `:=` in structure fields means "this field is defined
to have this value". But this is not the case! Instead, this is the way to supply default
values of structure fields. In particular, these values can be overridden.

```
structure foo : Type where
  n : Nat := 37 -- I want n to always be 37...

def X : foo where
  n := 42 -- ...but that's not the way to do it

#eval X.n -- 42

def Y : foo where -- only if `n` is not supplied does the default value kick in.

#eval Y.n -- 37
```

If you really want to have something like this, try the following instead:

```
structure foo : Type where

def foo.n : Nat := 37

def X : foo where

#eval X.n -- 37
```
