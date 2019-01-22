---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/80390somethingisweird.html
---

## [new members](index.html)
### [`some`thing is weird](80390somethingisweird.html)

#### [Abhimanyu Pallavi Sudhir (Nov 21 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%60some%60thing%20is%20weird/near/148117675):
I've been looking at the `classical.lean` file, and `p_implies_uv` strikes me as a very odd theorem. You have a proposition `p`, and you have two propositions, `u` which is `some` proposition such that it is true or `p` is true, and `v` which is `some` proposition such that it is false or `p` is true.  

But now you have `p_implies_uv`, which proves, apparently, that if `p` is true, `u = v`. I have no idea how this can be true. `u` and `v` can be `true` and `false`, for example -- having `p` be true does nothing to change this fact.

What's wrong with this? I'm guessing there's something wrong with my understanding of how `some` works.

#### [Abhimanyu Pallavi Sudhir (Nov 21 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%60some%60thing%20is%20weird/near/148118042):
I'm reading the proof on [wikipedia](https://en.wikipedia.org/wiki/Diaconescu%27s_theorem) -- and I can understand the set theoretic version.

#### [Abhimanyu Pallavi Sudhir (Nov 21 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%60some%60thing%20is%20weird/near/148118122):
Or well, I can understand their version -- since U and V are sets in their version, all this means is that if P is true then `u` and `v` have the same range of possible values (`true`, `false`).

#### [Jeremy Avigad (Nov 21 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%60some%60thing%20is%20weird/near/148118128):
The proof is described in detail here: https://leanprover.github.io/theorem_proving_in_lean/axioms_and_computation.html#the-law-of-the-excluded-middle. You are right that it is a weird proof, a clever trick rather than something deep.

`some` works as follows: given `h : ∃ x : α, p x`, `some h` returns an `x` satisfying `p`.

#### [Abhimanyu Pallavi Sudhir (Nov 21 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%60some%60thing%20is%20weird/near/148118190):
Yeah, I get that -- but if it just returns _an_ `x` satisfying `p`, does it really make sense to say two the two `some`s are equal?

#### [Abhimanyu Pallavi Sudhir (Nov 21 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%60some%60thing%20is%20weird/near/148118194):
Oh wait, `some h = some h`.

#### [Abhimanyu Pallavi Sudhir (Nov 21 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%60some%60thing%20is%20weird/near/148118199):
That's all that's going on.

#### [Abhimanyu Pallavi Sudhir (Nov 21 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%60some%60thing%20is%20weird/near/148118268):
It doesn't mean that anything in `h` is equal to anything else in `h`, it just means a generic element in `h` is equal to a generic element in `h`.

#### [Abhimanyu Pallavi Sudhir (Nov 21 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%60some%60thing%20is%20weird/near/148118274):
I see. Very weird, but I think I understand.

#### [Jeremy Avigad (Nov 21 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%60some%60thing%20is%20weird/near/148118750):
Yes, `some` choose a particular though unspecified element with the given property. If `h₀ : ∃ x, odd x`, `some h₀` returns an odd number. If `h₁ : ∃ x, prime x`, `some h₁` returns a prime number. We can ask whether `some h₀ = some h₁`. In this case, Lean's axioms don't allow us to prove or refute this statement. But as you note, sometimes we can prove things about `some`. For example, if `h₂ : ∃ x, even x ∧ prime x`, we can prove `some h₂ = 2`, because `some h₂` has to be both even and prime. For another example, we can prove `even (some h₀ + 1)`, because we know `some h₀` is odd.

#### [Abhimanyu Pallavi Sudhir (Nov 21 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%60some%60thing%20is%20weird/near/148125215):
```quote
Yes, `some` choose a particular though unspecified element with the given property. If `h₀ : ∃ x, odd x`, `some h₀` returns an odd number. If `h₁ : ∃ x, prime x`, `some h₁` returns a prime number. We can ask whether `some h₀ = some h₁`. In this case, Lean's axioms don't allow us to prove or refute this statement. But as you note, sometimes we can prove things about `some`. For example, if `h₂ : ∃ x, even x ∧ prime x`, we can prove `some h₂ = 2`, because `some h₂` has to be both even and prime. For another example, we can prove `even (some h₀ + 1)`, because we know `some h₀` is odd.
```
 Those make sense. What wasn't making sense to me -- and is used in the Diaconescu proof -- is the fact that `some h = some h`, i.e.

```lean
lemma h : ∃ n : ℕ, n = 1 ∨ n = 2 := ⟨1, or.inl rfl⟩

noncomputable def h1 := classical.some h
noncomputable def h2 := classical.some h

theorem something : h1 = h2 := rfl
```
Which is weird, because in my mind, `h1` and `h2` can still be either 1 or 2 -- all we know about them is that they satisfy "it's either 1 or 2", and not all things that are "either 1 or 2" are equal. 

But I guess choice allows Lean to just have some concept of  "a general `some`" so that saying `h1 = h2` is really just extensionality on `some`.

#### [Johannes Hölzl (Nov 21 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%60some%60thing%20is%20weird/near/148135819):
this is completely unrelated to `some`, it is just reflexivity of `=` in Lean (internally `h1` and `h2` are unfolded). It is not possible to have a `some` operator where this doesn't hold. With some tricks it is possible to hide this fact. By marking `h1` and/or `h2` as `@[irreducible]`. Then at least one cannot prove it `by refl` anymore (but it is still true in the logic)

#### [Kevin Buzzard (Nov 21 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/%60some%60thing%20is%20weird/near/148136060):
A function always produces the same output when presented with the same input.

