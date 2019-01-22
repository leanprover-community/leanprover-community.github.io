---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/55185Proptobool.html
---

## [new members](index.html)
### [Prop to bool](55185Proptobool.html)

#### [Olli (Sep 11 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Prop to bool/near/133728628):
I'm sure this will be covered later in the book, but I was wondering if there is a quick explanation for why I can't turn this `prime` Prop into a bool?

```lean
namespace hidden

open classical
open decidable
local attribute [instance] prop_decidable

def divides (m n : ℕ) : Prop := ∃ k, m * k = n

instance : has_dvd ℕ := ⟨divides⟩

variables m n : ℕ

def prime (n : ℕ) : Prop := n ≥ 2 ∧ ∀ k, k ∣ n → k = 1 ∨ k = n 

#reduce prime 5
-- nat.less_than_or_equal 2 5 ∧ ∀ (k : ℕ), (∃ (k_1 : ℕ), nat.mul k k_1 = 5) → k = 1 ∨ k = 5

#eval to_bool $ prime 5
-- code generation failed, VM does not have code for 'classical.choice'

end hidden
```

#### [Kenny Lau (Sep 11 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Prop to bool/near/133729533):
if you remove `local attribute [instance] prop_decidable` then it should be fine

#### [Olli (Sep 11 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Prop to bool/near/133729720):
I get:

```
failed to synthesize type class instance for
m n : ℕ
⊢ decidable (prime 5)
```

#### [Chris Hughes (Sep 11 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Prop to bool/near/133729749):
You need `prime` to be a decidable proposition.

#### [Chris Hughes (Sep 11 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Prop to bool/near/133729757):
Lean doesn't know how to check whether 5 is prime.

#### [Kenny Lau (Sep 11 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Prop to bool/near/133729766):
oh, he defined prime by himself

#### [Kenny Lau (Sep 11 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Prop to bool/near/133729769):
I didn't notice

#### [Chris Hughes (Sep 11 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Prop to bool/near/133729814):
But it does know how to decide for the library definition of prime, so it should work for that.

#### [Olli (Sep 11 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Prop to bool/near/133729861):
I found a definition for `prime` in mathlib but nothing for it in the core library

#### [Chris Hughes (Sep 11 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Prop to bool/near/133729875):
There isn't one in core.

#### [Kevin Buzzard (Sep 11 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Prop to bool/near/133731851):
If you're going to roll your own `prime` then to do what you want to do you're also going to have to roll your own `prime.decidable` function giving an algorithm for testing primality. This is a good exercise; the way to do it is perhaps to search the source code for example of proofs of decidability, then figure out how to prove the key lemma (if n>=1 and k divides n then k<=n) and then write the algorithm. If you don't make it efficient then that's OK, you will have trouble working out if 617 is prime, but on the other hand at least the code will work (or it might give you a time-out the moment the numbers get too large to do on your fingers :-) )

#### [Olli (Sep 11 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Prop to bool/near/133732019):
yeah I think I should finish a few more chapters before attempting that

#### [Kevin Buzzard (Sep 11 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Prop to bool/near/133734843):
or use mathlib's `prime` :-)

