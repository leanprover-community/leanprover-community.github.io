# How to use calc

`calc` is an syntax -- so a "mode" like tactic mode, term mode and
[conv mode](conv.html). Documentation and basic examples for how to use
it are in Theorem Proving In Lean 4, in
[chapter 4](https://lean-lang.org/theorem_proving_in_lean4/quantifiers_and_equality.html#calculational-proofs).

Basic example usage:

```lean
example (a b c : ℕ) (H1 : a = b + 1) (H2 : b = c) : a = c + 1 :=
  calc
    a = b + 1 := H1
    _ = c + 1 := by rw [H2]
```

`calc` is also available in tactic mode. You can leave `?_`s to create a
new goal:
```lean
example (a b c : ℕ) (H1 : a = b + 1) (H2 : b = c) : a = c + 1 := by
  calc
    a = b + 1 := H1
    _ = c + 1 := ?_
  rw [H2]
```
In fact, `calc A = B := H ...` in tactic mode functions exactly like a
call to `refine (calc A = B := H ...)`.

## Getting effective feedback while using calc

To get helpful error messages, keep the calc structure even before the
proof is complete. Use `?_` as in the example above or `sorry` to stand
for missing justifications. `sorry` will suppress error messages
entirely, while `?_` will generate a guiding error message.

If the structure of calc is incorrect (e.g., missing `:=` or the
justification after it), you may see error messages that are obscure
and/or red squiggles that end up under a random `_`. To avoid these,
you might first populate a skeleton proof such as:

```lean
example (A B C D : ℕ) : A = D :=
  calc
    A = B := sorry
    _ = B := _
    _ = D := sorry
```

and then fill in the `sorry` and `?_` gradually.

In tactic mode calc should be terminated with outdenting:
```lean
  have H : A = D := by
    calc
      A = B := sorry
      _ = C := sorry
      _ = D := ?_
    sorry
```
and the `?_` can be left in as they generate a subgoal to be resolved
after calc (here by the last `sorry`).

(Idle thought: could one write a VS Code snippet to write this skeleton?)

## Using operators other than equality

Many of the basic examples in TPIL use equality for most or all of
the operators, but actually `calc` will work with any relation with
a `Trans` instance:

```lean
def r : ℕ → ℕ → Prop := sorry
instance : Trans r r r := sorry
infix:50 "***" => r

example (a b c : ℕ) (H1 : a *** b) (H2 : b *** c) : a *** c :=
  calc
    a *** b := H1
    _ *** c := H2
```

## Using more than one operator

This is possible; TPIL has the following example:

```lean
example (a b c d : ℕ) (h1 : a = b) (h2 : b ≤ c) (h3 : c + 1 < d) : a < d :=
  calc
    a = b     := h1
    _ < b + 1 := Nat.lt_succ_self b
    _ ≤ c + 1 := Nat.succ_le_succ h2
    _ < d     := h3
 ```

What is actually going on here? The proofs themselves are not a mystery,
for example `Nat.succ_le_succ h2` is a proof of `b + 1 ≤ c + 1`. The
clever part is that lean can put all of these together to correctly
deduce that if `U = V < W ≤ X < Y` then `U < Y`. The way this is done,
Kevin thinks (can someone verify this?) is that Lean continually tries
to amalgamate the first two operators in the list, until there
is only one left. In other words, Lean will attempt to reduce
the equations thus:

```
U = V < W ≤ X < Y
U < W ≤ X < Y
U < X < Y
U < Y
```

Note the following subtlety: given `U op1 V` and `V op2 W` Lean
has to conclude `U op3 W` for some operator, which might be `op1`
or `op2` (or even, as we shall see, a new operator). How is Lean
doing this? Lean looks through the theorems in `Trans` instances and
applies these instead. For example Lean has the following instances:

```
instance (r : α → γ → Sort u) : Trans Eq r r
instance (r : α → β → Sort u) : Trans r Eq r
instance : Trans (. < . : Nat → Nat → Prop) (. ≤ . : Nat → Nat → Prop) (. < . : Nat → Nat → Prop)
instance : Trans (. < . : Nat → Nat → Prop) (. < . : Nat → Nat → Prop) (. < . : Nat → Nat → Prop)
```

and it is easily seen that these instances can be used to justify the example in the manual.

## Using user-defined operators

It is as simple as declaring the relevant results as a `Trans` instance. For example

```lean
def r : ℕ → ℕ → Prop := sorry
def s : ℕ → ℕ → Prop := sorry
def t : ℕ → ℕ → Prop := sorry
instance : Trans r s t := sorry
infix:50 "***" => r
infix:50 "$$$" => s
infix:50 "%%%" => t

example (a b c : ℕ) (H1 : a *** b) (H2 : b $$$ c) : a %%% c :=
  calc
    a *** b := H1
    _ $$$ c := H2
```

This example shows us that the third operator `op3` can be different to both `op1` and `op2`.
