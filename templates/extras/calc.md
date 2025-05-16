# How to use calc

`calc` is an environment -- so a "mode" like tactic mode, term mode and
[conv mode](conv.html). Documentation and basic examples for how to use
it are in Theorem Proving In Lean, in
[section 4](https://lean-lang.org/theorem_proving_in_lean4/quantifiers_and_equality.html#calculational-proofs).

Basic example usage:

```lean
example (a b c : ℕ) (H1 : a = b + 1) (H2 : b = c) : a = c + 1 :=
calc a = b + 1 := H1
     _ = c + 1 := by rw [H2]
```

`calc` is also available in tactic mode. You can leave `?_`s to create a
new goal:
```lean
example (a b c : ℕ) (H1 : a = b + 1) (H2 : b = c) : a = c + 1 := by
  calc
    a = b + 1 := ?_
    _ = c + 1 := ?_
  · exact H1
  · rw [H2]
```
In fact, `calc A = B := H ...` in tactic mode functions exactly like a
call to `refine (calc A = B := H ...)`.

## Getting effective feedback while using calc

To get helpful error messages, keep the calc structure even before the
proof is complete. Use `_` as in the example above or `sorry` to stand
for missing justifications. `sorry` will suppress error messages
entirely, while `_` will generate a guiding error message.

If the structure of calc is incorrect (e.g., missing `:=` or the
justification after it), you may see error messages that are obscure
and/or red squiggles that end up under a random `_`. To avoid these,
you might first populate a skeleton proof such as:

```lean
example (A B C D : ℝ ) : A = D :=
calc A = B := sorry
     _ = C := _
     _ = D := sorry
```

and then fill in the `sorry` and `_` gradually.


```lean
example (A B C D : ℝ ) : A = D := by
     calc A = B := sorry
          _ = C := ?_
          _ = D := sorry
     sorry
```

There is also a Calc widget that makes this easier here is a [video](https://youtu.be/8MFGhOWeCNE?t=1834) demonstrating it.

## Using operators other than equality

Many of the basic examples in TPIL use equality for most or all of
the operators, but actually `calc` will work with any relation for which
we have created an instance of `Trans`

```lean
def r : ℕ → ℕ → Prop := sorry
variable (a b c: ℕ)
def r_trans {a b c} (h₁ : r a b) (h₂ : r b c) : r a c := sorry

instance : Trans r r r where
  trans := r_trans

infix:50 "***" => r

example (a b c : ℕ) (H1 : a *** b) (H2 : b *** c) : a *** c :=
calc a *** b := H1
     _ *** c := H2
```

## Using more than one operator

This is possible, for example:

```lean
theorem T2 (a b c d : ℕ)
  (h1 : a = b) (h2 : b ≤ c) (h3 : c + 1 < d) : a < d := 
  calc
    a = b     := h1
    _ < b + 1 := Nat.lt_succ_self b
    _ ≤ c + 1 := Nat.succ_le_succ h2
    _ < d     := h3

 ```

What is actually going on here? The proofs themselves are not a mystery,
for example `Nat.succ_le_succ h2` is a proof of `b + 1  ≤ c + 1`. The
clever part is that lean can put all of these together to correctly
deduce that if `U = V < W ≤ X < Y` then `U < Y`. Note the following subtlety:
given `U op1 V` and `V op2 W` Lean
has to conclude `U op3 W` for some operator, which might be `op1`
or `op2` (or even, as we shall see, a new operator). How is Lean
doing this? The easiest case is when one of `op1` and `op2`
is `=`. Lean knows

```lean
#check trans_rel_right -- {α : Sort u} {a b c : α} (r : α → α → Prop) (h₁ : a = b) (h₂ : r b c) : r a c
#check trans_rel_left -- {α : Sort u} {a b c : α} (r : α → α → Prop) (h₁ : r a b) (h₂ : b = c) : r a c
```

and uses them if one of the operators is an equality operator. If however neither
operator is the equality operator, Lean looks through the instances of
`Trans` and applies these instead.

## Using user-defined operators

It is as simple as creating the relevant `Trans` instances. For example

```lean
def r : ℕ → ℕ → Prop := sorry
def s : ℕ → ℕ → Prop := sorry
def t : ℕ → ℕ → Prop := sorry

theorem rst_trans {a b c : ℕ} : r a b → s b c → t a c := sorry
infix:50 "****" => r
infix:50 "^^^^" => s
infix:50 "%%%%" => t

instance : Trans r s t  where
  trans := rst_trans

example (a b c : ℕ) (H1 : a **** b) (H2 : b ^^^^ c) : a %%%% c :=
calc a **** b := H1
     _ ^^^^ c := H2
```

This example shows us that the third operator `op3` can be different to both `op1` and `op2`.
