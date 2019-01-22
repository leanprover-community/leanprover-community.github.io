---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/39702euclideandomains.html
---

## [maths](index.html)
### [euclidean domains](39702euclideandomains.html)

#### [Johan Commelin (Jul 20 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean domains/near/129982059):
Currently, the definition of a Euclidean domain has the field
```lean
(val_remainder_lt : ∀ a {b}, b ≠ 0 → valuation (remainder a b) < valuation b)
```
I think it should read
```lean
(val_remainder_lt : ∀ a {b}, b ≠ 0 → (remainder a b = 0 ∨ valuation (remainder a b) < valuation b))
```
or something like that. What is best in these cases:
(i) the change as I suggest, or
(ii) move the claim `remainder a b = 0` to a condition, so `b \ne 0 \and remainder a b \ne 0 \to ...`

#### [Chris Hughes (Jul 20 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean domains/near/129982412):
My plan when I wrote polynomials, was that it should take a well founded relation instead of a valuation. `mod_lt` would be `r (remainder a b) b` and `val_me_mul_left` would be `not r (a * b) a` I think. `degree` now returns `with_bot nat` so it meets this definition.

#### [Chris Hughes (Jul 20 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean domains/near/129982687):
The trouble with your definition is it makes every proof and definition longer. For example gcd needs an extra `else if`.
```lean
def gcd : α → α → α
| a := λ b, if a0 : a = 0 then b 
 else if hba : remainder b a = 0 then a
 else
  have h:_ := or.resolve_left (val_mod_lt' b a0) hba,
  gcd (b%a) a
using_well_founded {rel_tac :=
  λ _ _, `[exact ⟨_, measure_wf valuation⟩]}
```

#### [Johan Commelin (Jul 20 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean domains/near/129983245):
On the other hand, it is the definition that every mathematician is used to...

#### [Johan Commelin (Jul 20 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean domains/near/129983258):
@**Chris Hughes** Do you think the `valuation` of an ED should also take values in `with_bot nat`? And then require that `valuation a = bot \iff a = 0`?

#### [Chris Hughes (Jul 20 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean domains/near/129983274):
That might be also be an idea, but without `valuation a = bot \iff a = 0`, because that will be annoying with integers.

#### [Chris Hughes (Jul 20 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean domains/near/129983330):
But even so, I think arbitrary well founded is better, because then people dealing with integers can use the relation `x.nat_abs < y.nat_abs` where the use of `with_bot` would just be annoying.

#### [Johan Commelin (Jul 20 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean domains/near/129987066):
So, what do you suggest as definition of ED?

#### [Johan Commelin (Jul 20 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean domains/near/129987081):
Then we can try to use that, and also prove that it is equivalent to the "usual" definition. And possibly build a 2nd constructor that mimics the "usual" one.

#### [Chris Hughes (Jul 20 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean domains/near/129992150):
I just made a PR with my suggested solution. https://github.com/leanprover/mathlib/pull/211

#### [Johan Commelin (Jul 20 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean domains/near/129992659):
Nice! I like your speed!

#### [Johan Commelin (Jul 20 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean domains/near/129996118):
Cool, you add an instance for `int`!

