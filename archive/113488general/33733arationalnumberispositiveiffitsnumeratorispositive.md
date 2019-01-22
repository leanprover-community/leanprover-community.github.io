---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/33733arationalnumberispositiveiffitsnumeratorispositive.html
---

## [general](index.html)
### [a rational number is positive iff its numerator is positive](33733arationalnumberispositiveiffitsnumeratorispositive.html)

#### [Kenny Lau (Apr 30 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125905999):
do we have that?

#### [Johan Commelin (Apr 30 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906320):
So $$\frac{-1}{-1}$$ is not a positive rational number?

#### [Kenny Lau (Apr 30 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906332):
in `rat` the denominator is always positive

#### [Johan Commelin (Apr 30 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906393):
So $$\frac{1}{-2}$$ is not a rational number...

#### [Kenny Lau (Apr 30 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906398):
denominator

#### [Johan Commelin (Apr 30 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906409):
I find this disturbing...

#### [Kenny Lau (Apr 30 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906582):
```lean
theorem rat.num_pos_of_pos (r : rat) (H : r > 0) : (r.num : ℚ) > 0 :=
calc  (r.num : ℚ)
    = r.num / (r.denom:ℤ) * r.denom : eq.symm $ div_mul_cancel _ $ ne_of_gt $ nat.cast_pos.2 r.pos
... = r * r.denom : by rw [← rat.mk_eq_div, ← rat.num_denom r]
... > 0 : mul_pos H $ nat.cast_pos.2 r.pos
```

#### [Kenny Lau (Apr 30 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906590):
it's hard to prove anything about the rational numbers when I don't have enough lemmas...

#### [Johan Commelin (Apr 30 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906724):
Are you building an interface for \Q ?

#### [Kenny Lau (Apr 30 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906727):
I'm using Q

#### [Kenny Lau (Apr 30 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906734):
and I'm finding everything hard to prove

#### [Johan Commelin (Apr 30 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906760):
Ok, then we need an interface... because end-users shouldn't use r.num and r.denom, in my opinion.

#### [Kenny Lau (Apr 30 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906768):
well don't rationals have denominators...

#### [Johan Commelin (Apr 30 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906824):
Not really well-defined... I think

#### [Kenny Lau (Apr 30 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906831):
they are

#### [Johan Commelin (Apr 30 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906833):
Of course you can make choices

#### [Kenny Lau (Apr 30 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906836):
no choices required

#### [Johan Commelin (Apr 30 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906842):
Well, not *morally* well-defined

#### [Kenny Lau (Apr 30 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906854):
in Lean a rational number consists of a numerator in Z, denominator in N, proof that the denominator is positive, and proof that they are coprime

#### [Kenny Lau (Apr 30 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906861):
and I find that to be morally well-defined also

#### [Kenny Lau (Apr 30 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906869):
every rational number has a simplified form

#### [Johan Commelin (Apr 30 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906931):
Yes, but that should be hidden away as much as possible

#### [Johan Commelin (Apr 30 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906940):
I think

#### [Kenny Lau (Apr 30 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906952):
I need its denominator to prove that every rational number is smaller than some power of 2

#### [Kenny Lau (Apr 30 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906956):
in particular, 1/2^r.denom < r

#### [Johan Commelin (Apr 30 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906988):
Well, part of the interface could say that for every rational number `r` there exists an integer `n` with `r < n`

#### [Johan Commelin (Apr 30 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906995):
Or something like that.

#### [Kenny Lau (Apr 30 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907033):
aha that's existing

#### [Kenny Lau (Apr 30 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907041):
but I don't like it :P

#### [Reid Barton (Apr 30 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907056):
there's even a class for that

#### [Kenny Lau (Apr 30 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907215):
```lean
theorem lt_two_pow (n : nat) : n < 2 ^ n :=
nat.rec_on n dec_trivial $ λ n ih,
calc  n + 1
    < 2^n + 1   : nat.add_lt_add_right ih 1
... ≤ 2^n + 2^n : nat.add_le_add_left (nat.pow_le_pow_of_le_right dec_trivial $ nat.zero_le n) (2^n)
... = 2^n * 2   : eq.symm $ mul_two (2^n)
... = 2^(n+1)   : eq.symm $ nat.pow_succ 2 n

theorem rat.coe_pow (m n : nat) : (m : ℚ) ^ n = (m^n : ℕ) :=
nat.rec_on n rfl $ λ n ih, by simp [pow_succ', ih, nat.pow_succ]

theorem rat.num_pos_of_pos (r : rat) (H : r > 0) : r.num > 0 :=
int.cast_lt.1 $
calc  (r.num : ℚ)
    = r.num / (r.denom:ℤ) * r.denom : eq.symm $ div_mul_cancel _ $ ne_of_gt $ nat.cast_pos.2 r.pos
... = r * r.denom : by rw [← rat.mk_eq_div, ← rat.num_denom r]
... > 0 : mul_pos H $ nat.cast_pos.2 r.pos

theorem rat.one_le_num_of_pos (r : rat) (H : r > 0) : 1 ≤ (r.num : ℚ) :=
have H1 : ((0+1:ℤ):ℚ) = (1:ℚ), from rfl,
H1 ▸ int.cast_le.2 $ int.add_one_le_of_lt $ rat.num_pos_of_pos r H

theorem rat.lt (r : ℚ) (H : r > 0) : (1 / 2^r.denom : ℚ) < r :=
calc  (1 / 2^r.denom : ℚ)
    < 1 / r.denom : one_div_lt_one_div_of_lt (nat.cast_pos.2 r.pos)
  (trans_rel_left _ (nat.cast_lt.2 $ lt_two_pow _) (rat.coe_pow 2 _).symm)
... ≤ r.num / r.denom : div_le_div_of_le_of_pos (rat.one_le_num_of_pos r H) (nat.cast_pos.2 r.pos)
... = r.num / (r.denom:ℤ) : rfl
... = r : by rw [← rat.mk_eq_div, ← rat.num_denom r]
```

#### [Kenny Lau (Apr 30 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907217):
yay done

#### [Johan Commelin (Apr 30 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907246):
I just don't like the fact that if some computation spits out two integers, `a` and `b`, with `b \ne 0`, and I want to consider the rational number `a/b`, then Lean decides it *also* wants to put them in lowest terms.

#### [Johan Commelin (Apr 30 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907251):
That might be an immense computation

#### [Johan Commelin (Apr 30 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907264):
Or can it formally divide away the gcd, without actually calculating it?

#### [Kevin Buzzard (Apr 30 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907336):
Johan you should take a look at `data/rat.lean` in mathlib

#### [Kevin Buzzard (Apr 30 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907337):
I found that file not too intimidating

#### [Johan Commelin (Apr 30 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907343):
Will do

#### [Kevin Buzzard (Apr 30 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907393):
I would tell my students "of course a rational number is an equivalence class"

#### [Kevin Buzzard (Apr 30 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907398):
(because it's Z localised away from 0)

#### [Kevin Buzzard (Apr 30 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907401):
but in Lean working with equivalence classes is sometimes hard work

#### [Kevin Buzzard (Apr 30 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907406):
so if they can get away with it, they work with an inductive type

#### [Kevin Buzzard (Apr 30 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907482):
So they go with this structure of a numerator n in Z, a denominator d in N, a proof that d > 0 and a proof that n and d are coprime!

#### [Reid Barton (Apr 30 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907488):
If you don't reduce to lowest terms, then `1/2 + 1/2 + 1/2 + ... + 1/2` becomes an unwieldy computation

#### [Kevin Buzzard (Apr 30 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907492):
At this point you can't even make 6/8

#### [Kevin Buzzard (Apr 30 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907495):
but it's OK, they're only a few lines in

#### [Kevin Buzzard (Apr 30 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907501):
and then they go on to make other constructors

#### [Kevin Buzzard (Apr 30 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907513):
because they implemented Euclid already

#### [Kevin Buzzard (Apr 30 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907535):
so you finally get a definition of `mk`

#### [Kevin Buzzard (Apr 30 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907576):
on line 61

#### [Kevin Buzzard (Apr 30 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907581):
and they define `/` to be mk

#### [Johan Commelin (Apr 30 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907592):
Well, Lean can decide to reduce to lowest terms when I force it to actually compute something. But if I want to define $$\frac{\pi(10^9)-1}{\pi(10^9+1)-1}$$ where $$\pi(n)$$ is the $$n$$-th prime, that should be possible, right?

#### [Kevin Buzzard (Apr 30 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907598):
inductive structures with lots of things which are quite easy to carry around are very popular round here

#### [Johan Commelin (Apr 30 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907606):
It shouldn't actually start computing those primes.

#### [Kevin Buzzard (Apr 30 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907624):
If you want to actually work something complicated out then you should not be using Lean at this point

#### [Johan Commelin (Apr 30 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907626):
Also, I *would* want to have a proof that `d = 0`, *all the time*

#### [Reid Barton (Apr 30 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907630):
If you believe it won't start computing the primes, then why would it need to do the conversion to lowest terms?

#### [Johan Commelin (Apr 30 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907634):
But there they choose to just put `n/0 = 0`

#### [Kevin Buzzard (Apr 30 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907681):
`n/0=0`.

#### [Kevin Buzzard (Apr 30 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907684):
Mathematicians can often get upset about that.

#### [Kevin Buzzard (Apr 30 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907696):
but the issue is just notation

#### [Kevin Buzzard (Apr 30 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907714):
Just imagine you went through all the Lean source code replacing the notation `/` with something that looked more like $$/^*$$

#### [Kevin Buzzard (Apr 30 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907754):
and the asterisk indicates a footnote:

#### [Kevin Buzzard (Apr 30 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907763):
"Note to mathematicians: this is not your divide. This is just notation for a different function which we invented because we find it more useful."

#### [Johan Commelin (Apr 30 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907766):
```quote
If you want to actually work something complicated out then you should not be using Lean at this point
```
Says the person who is formalising schemes... :rolling_on_the_floor_laughing:

#### [Kevin Buzzard (Apr 30 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907767):
because whenever a mathematician writes the symbol `/`

#### [Kevin Buzzard (Apr 30 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907780):
they are doing that thing that mathematicians love to do -- they are making a promise.

#### [Johan Commelin (Apr 30 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907785):
Lol

#### [Kevin Buzzard (Apr 30 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907790):
They are saying "I promise that the denominator is not zero."

#### [Johan Commelin (Apr 30 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907794):
Yeah, ok... I'll try to forget some of my home culture.

#### [Kevin Buzzard (Apr 30 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907796):
but if you really make them keep their promises

#### [Kevin Buzzard (Apr 30 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907807):
then that means that they have to supply a proof.

#### [Kevin Buzzard (Apr 30 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907861):
And that is your input which you as a mathematician enter into /

#### [Kevin Buzzard (Apr 30 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907873):
and that's exactly the data needed to work out /*

#### [Kevin Buzzard (Apr 30 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907875):
with a guarantee that it's equal to /

#### [Johan Commelin (Apr 30 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907877):
Fair enough

#### [Kevin Buzzard (Apr 30 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907879):
Mathematicans are full of promises.

#### [Kevin Buzzard (Apr 30 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907883):
A is a hypergeometric schemeoid

#### [Kevin Buzzard (Apr 30 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907896):
and B is a set that bijects with A

#### [Kevin Buzzard (Apr 30 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907902):
therefore B is a hypergeometric schemeoid.

#### [Kevin Buzzard (Apr 30 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907909):
That statement comes with a promise. I had not realised this until very recently.

#### [Kevin Buzzard (Apr 30 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907960):
The promise is: "I promise that the definition of a hypergeometric schemeoid structure on a set A does not involve actually looking at any of A's elements"

#### [Kevin Buzzard (Apr 30 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907965):
"it just involves things like structures of multiplication and addition on A

#### [Kevin Buzzard (Apr 30 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125908006):
You don't have to rely on A having an element containing an element containing the empty set in the definition -- but such a condition is a **completely valid thing to say in ZFC**.

#### [Johan Commelin (Apr 30 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125908047):
Yup...

#### [Kevin Buzzard (Apr 30 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125908052):
So when you make that transport of structure you are making a promise

#### [Kevin Buzzard (Apr 30 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125908063):
and mathematicians have kind of forgotten this, because it's just part of the culture.

#### [Johan Commelin (Apr 30 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125908072):
And lately we have more or less been working under that promise all the time... to never actually look at the elements of our sets.

#### [Johan Commelin (Apr 30 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125908088):
Our objects may have an element "3", but we don't actually care what that element "3" looks like. As long as it behaves like a "3"

#### [Kevin Buzzard (Apr 30 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125908089):
There are certain things we _can_ do to sets, but we choose not to do. If G is a group, I don't care about the underlying set, I just care about one special element of G with the _name_ "identity" -- I don't care which set it is -- and the inversion and multiplication.

#### [Chris Hughes (Apr 30 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125908159):
`pow_unbounded_of_gt_one` in `algebra.archimedean` sounds like what you want.

#### [Kevin Buzzard (Apr 30 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125908160):
And I would be really interested in formalising the notion of what we as mathematicians consider decent things to do to types. Exactly what can mathematicians do to mathematical objects?

#### [Johan Commelin (Apr 30 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125908210):
Agreed. (But we are stealing Kenny's thread...) Chris subtly reminded me of that (-;

#### [Mario Carneiro (May 01 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125921367):
> I just don't like the fact that if some computation spits out two integers, a and b, with b \ne 0, and I want to consider the rational number a/b, then Lean decides it also wants to put them in lowest terms. That might be an immense computation

The runtime for doing this is not much more than multiplication of rationals to begin with, so I think it's a reasonable cost given you are doing a division. As Reid says, the alternative is much worse, unnormalized rationals have exponentially worse runtime in some situations.

```quote
Well, Lean can decide to reduce to lowest terms when I force it to actually compute something. But if I want to define $$\frac{\pi(10^9)-1}{\pi(10^9+1)-1}$$ where $$\pi(n)$$ is the $$n$$-th prime, that should be possible, right?
```
If you say `def x : rat := pi bla bla...` then nothing is computed up front, but `x` is computed when you use it in a program which is `#eval`'d. In particular, Lean uses an eager evaluation semantics, so in fact `pi(10^9)` will be calculated *regardless* of whether rationals are defined as a quotient or as reduced fractions. (This isn't Haskell!) The only way to avoid the calculation at this stage is to have `/` be some sort of thunk-taking operation so as to defer evaluation of its arguments, but it is not at all obvious that these "lazy rats" are the intended usual use of rational numbers.

#### [Johan Commelin (May 01 2018 at 06:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125929510):
Ok, understood. Somehow laziness feels natural to me. But I don't have that much experience actually. If at some point I need it, then I'll bring it up again (-;

#### [Reid Barton (May 01 2018 at 07:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125929676):
The point I was (too obliquely) trying to make before is that if Lean were lazy, then it would presumably have no reason to do the GCD computation, either

