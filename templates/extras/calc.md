# How to use calc

`calc` is an environment -- so a "mode" like tactic mode, term mode and
[conv mode](conv.html). Documentation and basic examples for how to use 
it are in Theorem Proving In Lean, in
[section 4.3](https://leanprover.github.io/theorem_proving_in_lean/quantifiers_and_equality.html#calculational-proofs).

Basic example usage:

```lean
example (a b c : ℕ) (H1 : a = b + 1) (H2 : b = c) : a = c + 1 :=
calc a = b + 1 : H1
...    = c + 1 : by rw H2
```

`calc` is also available in tactic mode. You can leave `_`s to create a 
new goal:
```lean
example (a b c : ℕ) (H1 : a = b + 1) (H2 : b = c) : a = c + 1 :=
begin
  calc a = b + 1 : H1
  ...    = c + 1 : _,
  { rw H2 }
end
```
In fact, `calc A = B : H ...` in tactic mode functions exactly like a 
call to `refine (calc A = B : H ...)`.

## Getting effective feedback while using calc

To get helpful error messages, keep the calc structure even before the 
proof is complete. Use `_` as in the example above or `sorry` to stand 
for missing justifications. `sorry` will supress error messages 
entirely, while `_` will generate a guiding error message. 

If the structure of calc is incorrect (e.g., missing `:` or the 
justification after it), you may see error messages that are obscure 
and/or red squiggles that end up under a random `...`. To avoid these, 
you might first populate a skeleton proof such as:

```lean
example (A B C D : ℝ ) : A = D :=
calc A = B : sorry
...    = C : _
...    = D : sorry
```

and then fill in the `sorry` and `_` gradually.

In tactic mode calc should be terminated with a comma:
```lean
have H : A = D,
{ calc A = B : sorry
  ...    = C : sorry
  ...    = D : _, 
  sorry },
```
and the `_` can be left in as they generate a subgoal to be resolved 
after calc (here by the last `sorry`).

(Idle thought: could one write a VS Code snippet to write this skeleton?)

## Using operators other than equality

Many of the basic examples in TPIL use equality for most or all of
the operators, but actually `calc` will work with any relation for which
the corresponding transitivity statement is tagged `[trans]`:

```lean
definition r : ℕ → ℕ → Prop := sorry
@[trans] theorem r_trans (a b c : ℕ) : r a b → r b c → r a c := sorry
infix `***`: 50 := r

example (a b c : ℕ) (H1 : a *** b) (H2 : b *** c) : a *** c :=
calc a *** b : H1
...    *** c : H2
```

## Using more than one operator

This is possible; TPIL has the following example:

```lean
theorem T2 (a b c d : ℕ)
  (h1 : a = b) (h2 : b ≤ c) (h3 : c + 1 < d) : a < d :=
calc
  a     = b     : h1
    ... < b + 1 : nat.lt_succ_self b
    ... ≤ c + 1 : nat.succ_le_succ h2
    ... < d     : h3
 ```

What is actually going on here? The proofs themselves are not a mystery,
for example `nat.succ_le_succ h2` is a proof of `b + 1  ≤ c + 1`. The
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
doing this? The easiest case is when one of `op1` and `op2`
is `=`. Lean knows

```lean
#check @trans_rel_right -- ∀ {α : Sort u_1} {a b c : α} (r : α → α → Prop), a = b → r b c → r a c
#check @trans_rel_left -- ∀ {α : Sort u_1} {a b c : α} (r : α → α → Prop), r a b → b = c → r a c
```

and (Kevin believes) uses them if one of the operators is an equality operator. If however neither
operator is the equality operator, Lean looks through the theorems in its database which are tagged
`[trans]` and applies these instead. For example Lean has the following definitions:

```
@[trans] lemma lt_of_lt_of_le [preorder α] : ∀ {a b c : α}, a < b → b ≤ c → a < c
@[trans] lemma lt_trans [preorder α] : ∀ {a b c : α}, a < b → b < c → a < c
```

and it is easily seen that these lemmas can be used to justify the example in the manual.

## Using user-defined operators

It is as simple as tagging the relevant results with `trans`. For example

```lean
definition r : ℕ → ℕ → Prop := sorry
definition s : ℕ → ℕ → Prop := sorry
definition t : ℕ → ℕ → Prop := sorry
@[trans] theorem rst_trans (a b c : ℕ) : r a b → s b c → t a c := sorry
infix `***`: 50 := r
infix `&&&` : 50 := s
infix `%%%` : 50 := t

example (a b c : ℕ) (H1 : a *** b) (H2 : b &&& c) : a %%% c :=
calc a *** b : H1
...    &&& c : H2
```

This example shows us that the third operator `op3` can be different to both `op1` and `op2`.
