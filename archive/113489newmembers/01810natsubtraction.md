---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/01810natsubtraction.html
---

## [new members](index.html)
### [nat subtraction](01810natsubtraction.html)

#### [Patrick Thomas (Dec 22 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152392979):
I am a bit confused by the results of the following:

constants m n : ℕ
#check m - n
#eval 5 - 6

The check reports a natural number. The eval returns 0.

example (Q : ℕ → Prop) (m : ℕ) : (∀ n : ℕ, Q n) → ( ∀ n : ℕ, Q (n - m) ) :=
    assume a1 : ∀ n : ℕ, Q n,
        assume n : ℕ,
        show Q (n - m), from a1 (n - m)

I did not expect that the substitution in the last line would be allowed, since n - m might not be a natural number.

#### [Johan Commelin (Dec 22 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152393031):
`n - m` is always a natural number. It is zero when you expect it to be negative.

#### [Kevin Buzzard (Dec 22 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152393174):
`-` is defined on `nat` for convenience, it's not the mathematical `-`. If you want to allow negative numbers, use `int`.

#### [Patrick Thomas (Dec 22 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152393219):
Is there a way to override that? It does not seem like the proof I posted should be valid. I would like it to require that m <= n.

#### [Kevin Buzzard (Dec 22 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152393233):
I don't know what you mean by "override". You can't change the definition of `nat.sub` but you could define a new function if you like and I guess you could even redefine the notation `-` on `nat` to mean your new function. What do you actually want?

#### [Kevin Buzzard (Dec 22 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152393290):
Remember that every function has to have a well-defined source and target type. `nat.sub` takes two nats and returns a nat.

#### [Patrick Thomas (Dec 22 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152393347):
I guess I am just uncomfortable that the proof I posted is valid. It seems that it should require m <= n.

#### [Kevin Buzzard (Dec 22 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152393353):
Your example is about a function called `nat.sub`

#### [Kevin Buzzard (Dec 22 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152393355):
because you used the notation `-` on naturals and that's what it expands to

#### [Kevin Buzzard (Dec 22 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152393394):
Whether or not you're uncomfortable, Lean is just doing what you told it to do. You still haven't made clear to me what you expect to happen.

#### [Kevin Buzzard (Dec 22 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152393410):
You can change definitions or change notation or define new functions, you can make Lean behave the way you want it to behave, but your example as it stands is behaving normally because computer scientists had reasons for defining nat.sub the way they did.

#### [Kevin Buzzard (Dec 22 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152393424):
Your example is *not* about usual mathematician's subtraction.

#### [Patrick Thomas (Dec 22 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152393472):
Is there an existing function I could use to make it the usual mathematician's subtraction?

#### [Kevin Buzzard (Dec 22 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152393475):
`int.sub`

#### [Kevin Buzzard (Dec 22 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152393488):
This takes two ints and returns the int that you think it should return.

#### [Patrick Thomas (Dec 22 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152393546):
I see. Thank you.

#### [Kevin Buzzard (Dec 22 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152393591):
But note that a nat is not an int -- there is a function from nat to int which to a mathematician is "the obvious inclusion". In computer science nat and int are two different types and there's a map from nat to int which you have to somehow invoke, which makes things a little more complicated than a mathematician would feel that they should be.

#### [Kevin Buzzard (Dec 22 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152393599):
NB notation for `int.sub` is just `-` again -- you just have to remember to feed ints to it and not nats. The notation `-` just figures out which `blah.sub` it should expand to depending on what you feed it.

#### [Kevin Buzzard (Dec 22 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152393602):
```lean
#eval (5 - 6) -- 0
#eval ((5 : ℤ) - 6) -- -1
```

#### [Kevin Buzzard (Dec 22 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152393647):
`(5 : ℤ)` means "I mean the integer 5". The default 5 is the natural number 5.

#### [Patrick Thomas (Dec 22 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152393752):
So in the example I posted I should introduce the assumption m <= n and use it to show that 'int.sub_nat_nat n m' is a natural number, then use 'a1 (int.sub_nat_nat n m)'?

#### [Johan Commelin (Dec 22 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152393948):
It's not so easy. Your function will return an `int`, which is never a `nat`.

#### [Johan Commelin (Dec 22 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152393957):
You could however use a function that turns an `int` into a `nat`. But it will give you garbage for negative integers.

#### [Johan Commelin (Dec 22 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152393968):
Alternatively, you can continue using natural numbers. And you can prove that it gives the "correct" result when `m <= n`. (Such proofs already exist in mathlib.)

#### [Johan Commelin (Dec 22 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152394015):
And then you just live with the fact that you also proved something else, something garbage. But who cares.

#### [Kevin Buzzard (Dec 22 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152395321):
```quote
and use it to show that `int.sub_nat_nat n m` is a natural number
```
You have a misconception about what is going on. The integer 4 is *not* a natural number, it is a non-negative integer. It is a term of type int, and because in type theory every term has at most one type, the integer 4 is not a natural number; indeed in type theory it does not even make sense to ask whether the integer 4 and the natural number 4 are equal -- terms of different types cannot be equal.

#### [Kevin Buzzard (Dec 22 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152395333):
On the other hand there is a map from the natural numbers to the integers, and a map (the absolute value function) from the integers to the naturals, so you can move between them -- but the moving has to be done.

#### [Kevin Buzzard (Dec 22 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152395375):
In particular, `a1 x` will never work if `a1` is expecting a natural and `x` is an integer, even if `x` is non-negative.

#### [Patrick Thomas (Dec 22 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152397122):
So there is a function that takes a positive integer and returns a natural number?

#### [Johan Commelin (Dec 22 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152397163):
No, same reason as above.

#### [Kevin Buzzard (Dec 22 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152397166):
`int.nat_abs` takes an arbitrary integer and returns a natural number.

#### [Kevin Buzzard (Dec 22 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152397175):
and if you feed it a non-negative integer, it will return the corresponding natural number.

#### [Kevin Buzzard (Dec 22 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152397230):
Type theory likes total functions, and this is a bit weird for mathematicians. For example the square root function just goes from the reals to the reals -- if you feed it a non-negative real then it returns its non-negative square root, and if you feed it a negative real then it just returns some junk, maybe 0, maybe the square root of the absolute value -- as a mathematician I don't care what it returns because I never apply this function unless the input is non-negative. It's just a different way of looking at things. Took me a while to get used to.

#### [Patrick Thomas (Dec 22 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152398558):
Would this be a better approach then:
example (Q : ℤ → Prop) (m : ℤ) (m ≥ 0) : (∀ n : ℤ, (n ≥ 0) → Q n) → ( ∀ n : ℤ, (n ≥ m) → Q (n - m) ) := ...

#### [Johan Commelin (Dec 22 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152398876):
The better approach is to accept the fact that your theorem might have some garbage edge cases. It will create more elegant proofs, and it will create lemmas that are easier to use in other proofs.

#### [Patrick Thomas (Dec 22 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152399842):
How do you avoid the risk of misinterpreting the theorem? Isn't it good to make it as explicit as possible?

#### [Johan Commelin (Dec 22 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152400178):
If you want you can use the "garbage-include" version to prove the explicit morally-mathematically-correct version. That shouldn't be hard.

#### [Mario Carneiro (Dec 22 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152400288):
There is no risk of the theorem being wrong, since lean is checking that. More than likely, if you try to prove anything nontrivial using `n - m : nat` you will naturally end up needing `m <= n` at some point, and so you add it to the theorem hypothesis and the garbage is excluded. In this particular case, you never needed this assumption, so it's true even in the "garbage case". You can add the assumption anyway if you want, or not.

#### [Patrick Thomas (Dec 22 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152401340):
I guess it is primarily a matter of not being aware of what the axioms are or how type theory works. I am a little worried that I may run into other unexpected cases. Maybe there is no easy way to avoid that?

#### [Patrick Thomas (Dec 22 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152401644):
This came from my attempt to prove that the Principle of Induction implies the Principle of Induction from a Starting Point and being able to leave out m <= n in the consequent. This feels somewhat nontrivial?

#### [Mario Carneiro (Dec 22 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152402330):
What is the real theorem you want to state? What you quoted doesn't look like the principle of induction from a starting point

#### [Patrick Thomas (Dec 22 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152403321):
```lean
-- Principle of Induction
def ind_1 :=
( ∀ P : ℕ → Prop,
    ( ( P 0 ∧ ( ∀ n : ℕ, (P n → P (n + 1)) ) ) → 
    ( ∀ n : ℕ, P n ) )
)

-- Principle of Induction from a Starting Point
def ind_2 :=
( ∀ Q : ℕ → Prop,
    ∀ m : ℕ, ( ( Q m ∧ ( ∀ n : ℕ, ( ( n ≥ m ) → ( Q n → Q (n + 1) ) ) ) ) → 
    ( ∀ n : ℕ, ( ( n ≥ m ) → Q n ) ) )
)

-- Principle of Induction -> Principle of Induction from a Starting Point
example : ind_1 → ind_2 :=
	assume a1 : ind_1,
		assume Q : ℕ → Prop,
			assume m : ℕ,
				assume a2 : ( Q m ∧ ( ∀ n, ( ( n ≥ m ) → ( Q n → Q (n + 1) ) ) ) ),
				have s1 : Q m, from and.left a2,
				have s2 : ∀ n, ( ( n ≥ m ) → ( Q n → Q (n + 1) ) ), from and.right a2,
				have s3 : ∀ n, ( Q (m + n) → Q (m + (n + 1)) ), from
					assume n : ℕ,
					have s4 : ( ( (m + n) ≥ m ) → ( Q (m + n) → Q ((m + n) + 1)) ), from s2 (m + n),
					have s5 : (m + n) ≥ m, from sorry,
					have s6 : ( Q (m + n) → Q ((m + n) + 1) ), from s4 s5,
                    show ( Q (m + n) → Q (m + (n + 1)) ), from s6,
                let P' := fun n, Q (m + n) in
                have s7 :( ( P' 0 ∧ ( ∀ n, ( P' n → P' (n + 1) ) ) ) → ( ∀ n, P' n ) ), from a1 P',
                have s8 : P' 0, from s1,
                have s9 : ∀ n, ( P' n → P' (n + 1) ), from s3,
                have s10 : P' 0 ∧ ( ∀ n, ( P' n → P' (n + 1) ) ), from and.intro s8 s9,
                have s11 : ∀ n, P' n, from s7 s10,
                have s12 : ∀ n, Q (m + n), from s11,
                    assume n : ℕ,
                        assume a3 : n ≥ m,
                        have s14 : Q (m + (n - m)), from s12 (n - m), -- did not expect to work
                        show Q n, from sorry
```

#### [Kevin Buzzard (Dec 22 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152403526):
To write code on this forum enclose it in three backticks ` ``` `

#### [Kevin Buzzard (Dec 22 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152403577):
Even better write ` ```lean ` for the first one and  it'll do syntax highlighting

#### [Mark Dickinson (Dec 22 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152403963):
So if it helps at all, to resolve your last `sorry` you're going to need to show that `m + (n - m) = n`. And that will need the hypothesis that `n ≥ m`.

#### [Mario Carneiro (Dec 22 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152403968):
```quote
```lean
have s14 : Q (m + (n - m)), from s12 (n - m), -- did not expect to work
show Q n, from sorry
```
```
You may not have expected the first line to work, but I think you will be vindicated when you do the second line

#### [Patrick Thomas (Dec 22 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152404182):
Why does ```m + (n - m) = n``` require ```n >= m```?

#### [Mark Dickinson (Dec 22 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152404225):
You may also want to look at `nat.less_than_or_equal.rec` at some point. It probably doesn't help here, if this is a learning exercise, but it was an "aha" moment for me (as a Lean newcomer) to understand why the recursion principle for `nat.less_than_or_equal` is pretty much exactly induction from a starting point.

#### [Mario Carneiro (Dec 22 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152404226):
because if `m > n`, then *since `n - m` is a natural number and hence is `>= 0`*, we cannot possibly have `m + (something nonnegative) = n`.

#### [Mario Carneiro (Dec 22 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152404235):
the fact that `n - m` is a natural number is purely a fact of its type, it is impossible for any term of that type to not be nonnegative

#### [Mario Carneiro (Dec 22 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152404278):
If we want to have a function `sub : nat -> nat -> nat` (and we do), it must not behave like regular subtraction everywhere. We do the next best thing and make it 0 when it ought to be negative

#### [Mario Carneiro (Dec 22 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152404285):
Not sure if it helps, but the natural number subtraction operation is called [monus](https://en.wikipedia.org/wiki/Monus) in regular maths

#### [Patrick Thomas (Dec 22 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152405626):
Is there an easy way to find the theorems for ```(m + n) ≥ m``` and ```m + (n - m) = n```?

#### [Mario Carneiro (Dec 23 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152406036):
They are all in `init.data.nat.lemmas` and `data.nat.basic`. You can browse those files, or try to guess the names like `nat.add_sub_...` in the autocompletion

#### [Mario Carneiro (Dec 23 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152406038):
the first one is `nat.le_add_left`

#### [Mark Dickinson (Dec 23 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152406173):
... and the second is `nat.sub_add_cancel` (`∀ {n m : ℕ}, n ≥ m → n - m + m = n`'), modulo a use of commutativity of addition.

#### [Patrick Thomas (Dec 23 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152406223):
Thank you.

#### [Mario Carneiro (Dec 23 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152406229):
the commutated version should also be there

#### [Mark Dickinson (Dec 23 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152406232):
Ah, looks like it's also exactly `nat.add_sub_cancel'`, from mathlib.

#### [Mark Dickinson (Dec 23 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152406293):
... and `nat.add_sub_of_le` from the standard library

#### [Patrick Thomas (Dec 23 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/nat subtraction/near/152408358):
Completed proof:

```lean
open nat


-- Principle of Induction
def ind_1 :=
∀ P : ℕ → Prop,
	P 0 ∧ (∀ n : ℕ, P n → P (n + 1)) → 
	∀ n : ℕ, P n


-- Principle of Induction from a Starting Point
def ind_2 :=
∀ Q : ℕ → Prop,
	∀ m : ℕ, (
		( Q m ∧ ( ∀ n : ℕ, (n ≥ m) → (Q n → Q (n + 1)) ) ) → 
		( ∀ n : ℕ, (n ≥ m) → Q n )
	)


-- Principle of Induction -> Principle of Induction from a Starting Point
example : ind_1 → ind_2 :=
	assume a1 : ind_1,
		assume Q : ℕ → Prop,
			assume m : ℕ,
				assume a2 : ( Q m ∧ ( ∀ n, ( ( n ≥ m ) → ( Q n → Q (n + 1) ) ) ) ),
				have s1 : Q m, from and.left a2,
				have s2 : ∀ n, ( ( n ≥ m ) → ( Q n → Q (n + 1) ) ), from and.right a2,
				have s3 : ∀ n, ( Q (m + n) → Q (m + (n + 1)) ), from
					assume n : ℕ,
					have s4 : ( ( (m + n) ≥ m ) → ( Q (m + n) → Q ((m + n) + 1)) ), from s2 (m + n),
					have s5 : (m + n) ≥ m, from le_add_right m n,
					have s6 : ( Q (m + n) → Q ((m + n) + 1) ), from s4 s5,
					show ( Q (m + n) → Q (m + (n + 1)) ), from s6,
				let P' := fun n, Q (m + n) in
				have s7 :( ( P' 0 ∧ ( ∀ n, ( P' n → P' (n + 1) ) ) ) → ( ∀ n, P' n ) ), from a1 P',
				have s8 : P' 0, from s1,
				have s9 : ∀ n, ( P' n → P' (n + 1) ), from s3,
				have s10 : P' 0 ∧ ( ∀ n, ( P' n → P' (n + 1) ) ), from and.intro s8 s9,
				have s11 : ∀ n, P' n, from s7 s10,
				have s12 : ∀ n, Q (m + n), from s11,
					assume n : ℕ,
						assume a3 : n ≥ m,
						have s13 : Q (m + (n - m)), from s12 (n - m),
						have s14 : m + (n - m) = n, from add_sub_of_le a3,
						show Q n, from eq.subst s14 s13
```

