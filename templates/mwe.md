# Minimal working examples

## tl;dr

When posting code on Zulip, please include all `import`s, `open`s, `universe`s, and `variable`s, so others can simply just copy-paste what you post, and see the same issue that you are seeing.

The best way to ensure you have done this is to copy-paste the code snipped you are proposing to post into an empty Lean file, or into the [lean web editor](https://live.lean-lang.org/), and check it compiles.

## Examples

### Bad example:

```lean
#check (univ : Set X)
```

### Good example:

```lean
import Mathlib

universe u

variable (X : Type u)

open Set

#check (univ : Set X)
```

### Bad example:

```text
Goal state:
/-
a b : blah,
h : a.fst < b.fst,
h2 : a.fst < b.snd
⊢ false
-/
```

### Good example:

```lean
def blah : Type := Nat × Nat

example (a b : blah) (h : a.fst < b.fst) (h2 : a.fst < b.snd) : False := by
  /-
  a b : blah,
  h : a.fst < b.fst,
  h2 : a.fst < b.snd
  ⊢ False
  -/
  done
```

Tip: If you are using [mathlib](https://github.com/leanprover-community/mathlib4) (e.g. with `import Mathlib`), there's a tactic called [`extract_goal`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Tactic/ExtractGoal.html) that can help you format the current goal as a stand-alone example. You can remove extraneous variables and hypotheses from the output of `extract_goal` to further minimize your example.

Note you still need to include the corresponding `import`s and `open`s and `universe`s and `variable`s as mentioned above.

## Formal Definition

A **minimal working example** is a code snippet that can be copied-and-pasted into an empty Lean file and still have the same features (working) and that does not include unnecessary details (minimal).

[Here](https://stackoverflow.com/help/minimal-reproducible-example) is the StackOverflow guide to making MWEs.

Please make sure that your code snippet has:

- correct imports; and
- all the relevant definitions / theorems.

It is fine for your example to throw compiler errors or warnings. In particular, it is fine for your code to contain the keyword `sorry` (and indeed, replacing irrelevant proofs with `sorry` is a good way of minimizing your example). The point of MWE is that your code should *throw the same errors in a blank file as it does for you*, that way people can help you with exactly the error you are confused about.

## How do I know if my code is a MWE?

You should *test* this by copy-pasting your code snippet into a new Lean file, or the [lean web editor](https://live.lean-lang.org/), and seeing if you get the expected behavior. This is exactly what people who try to help you will do!

## What if I'm asking about games like the [Natural Number Game](https://adam.math.hhu.de/#/g/hhu-adam/NNG4)?

If your example comes from the Natural Number Game or any such browser-based Lean demo, then you can add a link to the webpage instead of finding the correct imports. So for example it would be much more useful to say "I am on [this level](https://adam.math.hhu.de/#/g/leanprover-community/nng4/world/Addition/level/2) of the Natural Number Game and my proof script is _blah_", rather than "I am on Addition World Level 2 of the Natural Number Game and my proof script is _blah_".

If you post a code snippet on Zulip, please make sure it is surrounded in triple backticks.

````text
```
def myNat : Nat := 5
```
````

## Tips for minimizing code
- A simple `import Mathlib` is a perfectly fine import in a MWE.
- For the purposes of making a MWE, you can replace all proofs of `theorem`s and `lemma`s (outside of the one you're working on) with `sorry`. Lean will give you extra warnings, but these are harmless.

- Remove all declarations (`def`s, `theorem`s, `lemma`s, `example`s, etc.) that are irrelevant to the issue you're seeing. In general, if you can comment out some code without throwing errors, then it can be removed.

- After deleting some code, you can then delete all the declarations that were only referenced there. By repeating this process a few times, you may be able to shorten a long file to just a few lines.
- Finally, you can add a comment into the code like `-- HERE`, `-- TODO`, `-- ERROR: yada yada`, or similar to guide the attention to a certain part in your MWE.

---

## Bug reports and feature requests for Lean

*This section is aimed at experienced users filing bug reports or feature requests for Lean itself. If you are a beginner asking questions on Zulip, the advice above is sufficient—you don't need to worry about this section.*

When reporting unexpected behavior in Lean (whether a bug or a feature request), it helps to make your example as precise and reproducible as possible. Two techniques are especially valuable: `#guard_msgs` and the `lean-minimizer` project.

### Using `#guard_msgs` to capture expected output

The `#guard_msgs` command lets you embed the expected compiler output directly in your code. This makes your example unambiguous: anyone running it will immediately see whether they can reproduce the issue.

#### Basic usage

The expected output goes in a **doc comment before** `#guard_msgs`, and must match exactly:

```lean
/-- info: Nat.add : Nat → Nat → Nat -/
#guard_msgs in
#check Nat.add
```

If the output doesn't match, `#guard_msgs` will show you a diff:

```lean
-- This fails because #check Nat.mul produces different output
/-- info: Nat.add : Nat → Nat → Nat -/
#guard_msgs in
#check Nat.mul
```

`#guard_msgs` provides a code action which will add or update the doc comment if it doesn't match the output. (In particular, it is not necessary to manually copy and paste the text when setting it up!)

#### Documenting errors

```lean
/--
error: Application type mismatch: The argument
  true
has type
  Bool
but is expected to have type
  Nat
in the application
  Nat.succ true
---
info: sorry.succ : Nat
-/
#guard_msgs in
#check Nat.succ true
```

#### Using `drop` to ignore message categories

Use `drop info` or `drop warning` to ignore entire categories of messages:

```lean
#guard_msgs (drop info) in
#check Nat.add
```

#### Using `substring` for partial matching

When you only care about part of the output, use `#guard_msgs (substring := true)`. The doc comment just needs to contain text that appears somewhere in the actual output:

```lean
/-- Nat.add -/
#guard_msgs (substring := true) in
#check Nat.add
```

This is particularly useful for:
- **Timeout errors**: Match the key part without the variable heartbeat count
- **Long error messages**: Focus on the key part you want to demonstrate
- **Version-sensitive output**: Match only the stable portion

#### Documenting timeouts

Combine `set_option maxHeartbeats` with `#guard_msgs (substring := true)`:

```lean
set_option maxHeartbeats 1 in
/-- maximum number of heartbeats (1) has been reached -/
#guard_msgs (substring := true) in
example : True := by trivial
```


#### Stabilizing metavariable names with `pp.mvars`

Error messages often include metavariable names like `?m.47` which change between runs. Use `set_option pp.mvars false` to replace them with stable `?_` placeholders:

```lean
set_option pp.mvars false in
/--
error: Type mismatch
  rfl
has type
  ?_ = ?_
but is expected to have type
  1 + 1 = 3
-/
#guard_msgs in
example : 1 + 1 = 3 := rfl
```


### Mathlib-free minimizations

For bug reports to the Lean repository, examples that don't depend on Mathlib are much more actionable. A Mathlib-free example:

- Makes it easier to bisect which Lean commit introduced a regression
- Removes the possibility that the bug is in Mathlib rather than Lean
- Is faster to compile when developers are iterating on a fix

Of course, producing a Mathlib-free example can be tedious. [**lean-minimizer**](https://github.com/kim-em/lean-minimizer) can help automate this. It works by repeatedly trying to remove or simplify parts of your code—including inlining and removing imports—while preserving the error you're trying to demonstrate. The process can take a while, but the result is often a tiny, self-contained example that makes the bug obvious.

For Mathlib-dependent code, [**mathlib-minimizer**](https://github.com/kim-em/mathlib-minimizer) is a convenience project that bundles lean-minimizer with Mathlib as a dependency, so you can run the minimizer without setting up the dependencies yourself.
