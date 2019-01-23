---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/43440bestdefinitionofcongruentmod37.html
---

## Stream: [general](index.html)
### Topic: [best definition of "congruent mod 37"](43440bestdefinitionofcongruentmod37.html)

---

#### [Kevin Buzzard (Aug 25 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132741889):
```lean

definition r1 (a b : ℤ) := ∃ k : ℤ, a - b = 37 * k
definition r2 (a b : ℤ) := ∃ k : ℤ, a - b = k * 37
definition r3 (a b : ℤ) := ∃ k : ℤ, 37 * k = a - b
definition r4 (a b : ℤ) := ∃ k : ℤ, k * 37 = b - a
-- I'm open to more suggestions

definition r1.symm (a b : ℤ) (H : r1 a b) : r1 b a :=
begin
  cases H with k Hk,
  existsi -k,
  simp [Hk], -- b + -a = -(37 * k)
  sorry
end

definition r2.symm (a b : ℤ) (H : r2 a b) : r2 b a :=
begin
  cases H with k Hk,
  existsi -k,
  simp [Hk], -- b + -a = -(k * 37)
  sorry
end

definition r3.symm (a b : ℤ) (H : r3 a b) : r3 b a :=
begin
  cases H with k Hk,
  existsi -k,
  simp [Hk] -- success!
end

definition r4.symm (a b : ℤ) (H : r4 a b) : r4 b a :=
begin
  cases H with k Hk,
  existsi -k,
  simp [Hk] -- success!
end
```

If you'd asked me in advance which relations would be easiest to work with I realise I would have no idea. But it seems `r3` and `r4` are better than `r1` and `r2`. Why is this?

#### [Kenny Lau (Aug 25 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132741991):
```lean
import data.int.modeq

def r5 (a b : ℤ) := a ≡ b [ZMOD 37]

theorem r5.symm (a b : ℤ) (H : r5 a b) : r5 b a :=
int.modeq.symm H
```

#### [Johan Commelin (Aug 25 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132741992):
Of course you could also try
`definition r6 (a b : ℤ) := ∃ k : ℤ, a = b + 37 * k`
I have no idea if it is easy to work with...

#### [Patrick Massot (Aug 25 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742000):
You could insert `eq.symm` in your simp

#### [Kevin Buzzard (Aug 25 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742152):
My "objection" to Kenny's approach is that my question is really about how one writes the interface, not the fact that it's there already.

#### [Kevin Buzzard (Aug 25 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742206):
My objection to Patrick's is that sure I could work a bit harder and get stuff to work, but why do I have to do this for some and not others? Is it the case that `r3` and `r4` are actually *better* in some way?

#### [Patrick Massot (Aug 25 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742216):
I think r6 is better

#### [Patrick Massot (Aug 25 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742255):
because you can use `rw Hk, ring`

#### [Kevin Buzzard (Aug 25 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742258):
`simp` works for `r6` too

#### [Kevin Buzzard (Aug 25 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742264):
One problem with r1 -- r4 is that you can't use rw with any of them

#### [Chris Hughes (Aug 25 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742265):
Johan's definition generalizes to a semiring :-)

#### [Kevin Buzzard (Aug 25 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742268):
I don't think symmetry is true for a semiring :-)

#### [Patrick Massot (Aug 25 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742275):
Kevin, do you see what you've done to your students?

#### [Kevin Buzzard (Aug 25 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742311):
only one of them!

#### [Patrick Massot (Aug 25 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742324):
Oh yeah, the other one became a constructivist...

#### [Kevin Buzzard (Aug 25 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742327):
:-)

#### [Kevin Buzzard (Aug 25 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742334):
maybe I need to rethink this entire thing

#### [Patrick Massot (Aug 25 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742387):
I think r3-r6 are better than r1 and r2 because it allows to write the same thing as in real world: `cases H with k Hk,  existsi -k,  finish`

#### [Kevin Buzzard (Aug 25 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742450):
But isn't this answer just like mine -- "try all ways, see which ones work, decide those must be the best ways"

#### [Kevin Buzzard (Aug 25 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742451):
I was interested in knowing which was the best way before I started

#### [Kevin Buzzard (Aug 25 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742453):
I don't see how to figure it out a priori

#### [Patrick Massot (Aug 25 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742492):
I think that we could have anticipated that Johan's version would be easier to rewrite

#### [Kevin Buzzard (Aug 25 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742625):
yes; I didn't instinctively mention that possibility because it looked so asymmetric

#### [Kevin Buzzard (Aug 25 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742627):
which is counter to my intuition, but which seems to play a big role here

#### [Kevin Buzzard (Aug 25 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742632):
Mathematicians even _say_ "a and b are congruent mod 37" and there's an implicit symmetry implied when we say "and", but when you have to prove symmetry the first thing you have to do is to break it I guess

#### [Kevin Buzzard (Aug 25 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742634):
and Johan's breaks it the most

#### [Patrick Massot (Aug 25 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742637):
The point is that `x = ...` can't fail to rewrite `x`

#### [Patrick Massot (Aug 25 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742670):
whatever you do to `x` in your expression

#### [Kenny Lau (Aug 25 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132746777):
```quote
My "objection" to Kenny's approach is that my question is really about how one writes the interface, not the fact that it's there already.
```
my objection to your objection is that my answer prompts one to look at the definition in mathlib:
```lean
def modeq (n a b : ℤ) := a % n = b % n

notation a ` ≡ `:50 b ` [ZMOD `:50 n `]`:0 := modeq n a b

namespace modeq
variables {n m a b c d : ℤ}

@[refl] protected theorem refl (a : ℤ) : a ≡ a [ZMOD n] := @rfl _ _

@[symm] protected theorem symm : a ≡ b [ZMOD n] → b ≡ a [ZMOD n] := eq.symm

@[trans] protected theorem trans : a ≡ b [ZMOD n] → b ≡ c [ZMOD n] → a ≡ c [ZMOD n] := eq.trans
```

#### [Kevin Buzzard (Aug 25 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132746937):
Yes but my actual question is: "I am defining some new relation on some new type completely unrelated to the integers, and I want to prove it's an equivalence relation. I've just realised that mathematically equivalent definitions of the relation will behave differently in Lean, so I need some pointers about how to formulate my relation so that I can use it efficiently".

#### [Kenny Lau (Aug 25 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132746951):
my objection is that you don't just have some random types

#### [Kenny Lau (Aug 25 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132746954):
if it's a group like the integers are, then you should just use quotient groups

