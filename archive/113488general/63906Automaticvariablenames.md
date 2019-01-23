---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/63906Automaticvariablenames.html
---

## Stream: [general](index.html)
### Topic: [Automatic variable names](63906Automaticvariablenames.html)

---

#### [Patrick Stevens (May 29 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatic%20variable%20names/near/127275253):
Another noob question, sorry. I haven't found an answer out there because everyone always proves this theorem using `simp`.

I've defined `myNat` in the obvious inductive way (`zero : myNat`, and `succ : myNat -> myNat`), and then defined `my_add` by cases as `| myNat.zero n := n` and `| (myNat.succ m) n := myNat.succ (my_add m n)`. To prove the theorem `addZero : (forall m : myNat, my_add m myNat.zero = m)` without using simp, I entered tactic mode and began with `assume m : myNat, induction m, refl` to take care of the base case. Now I have the goal to prove it for the successor case, and the Tactic State tells me that I have `m_a : myNat` and `m_ih : my_add m_a myNat.zero = m_a`. But when I try to reference these terms with `have (my_add (myNat.succ m_a) myNat.zero) = (myNat.succ (my_add m_a myNat.zero)), from sorry`, I get multiple syntax errors, one of which is "unknown identifier 'm_a'".

#### [Kenny Lau (May 29 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatic%20variable%20names/near/127275311):
post your code?

#### [Patrick Stevens (May 29 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatic%20variable%20names/near/127275314):
Have I got some syntax wrong, and if not, how do I reference variables that `induction` introduced?

#### [Andrew Ashworth (May 29 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatic%20variable%20names/near/127275316):
^ can you paste it in a formatted code block

#### [Patrick Stevens (May 29 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatic%20variable%20names/near/127275360):
Sorry - it really did come out pretty unreadable, hang on

#### [Patrick Stevens (May 29 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatic%20variable%20names/near/127275438):
```
inductive myNat : Type
| zero : myNat
| succ : myNat → myNat

axiom zeroIsNotASuccessor : (∀ n : myNat, ¬(myNat.succ n = myNat.zero))
axiom succPreservesInequality: (∀ n m : myNat, (¬(m = n)) → ¬(myNat.succ m = myNat.succ n))

definition my_add : myNat -> myNat -> myNat
| myNat.zero n := n
| (myNat.succ m) n := myNat.succ (my_add m n)

theorem addZero : (∀ m : myNat, my_add m myNat.zero = m) :=
begin
    assume m : myNat,
    induction m,
    refl,
    have (my_add (myNat.succ m_a) myNat.zero) = (myNat.succ (my_add m_a myNat.zero)), from
    begin
        sorry
    end
end
```

#### [Kenny Lau (May 29 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatic%20variable%20names/near/127275455):
`have :`

#### [Patrick Stevens (May 29 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatic%20variable%20names/near/127275520):
Ah, thanks - why was that colon not necessary in e.g.
```
example:p ∧ ¬q → ¬(p → q):=
begin
    intro h,
    assume hpq : p → q,
    cases h with hp hnq,
    have hq : q, from hpq hp,
    exact hnq hq
end
```

#### [Kenny Lau (May 29 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatic%20variable%20names/near/127275532):
it was

#### [Patrick Stevens (May 29 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatic%20variable%20names/near/127275533):
Oh, I get it - an anonymous member of the equality type

#### [Patrick Stevens (May 29 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatic%20variable%20names/near/127275536):
Sorry

#### [Kenny Lau (May 29 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatic%20variable%20names/near/127275541):
`have :` sets the name to `this`

#### [Kenny Lau (May 29 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatic%20variable%20names/near/127275542):
`have hq :` sets the names to `hq`

#### [Patrick Stevens (May 29 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatic%20variable%20names/near/127275590):
cheers

#### [Kevin Buzzard (May 30 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatic%20variable%20names/near/127277391):
I never know whether using `have :...` (and thus making a variable called `this`) is bad style.

#### [Kevin Buzzard (May 30 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Automatic%20variable%20names/near/127277444):
I tend to name all my have variables except for the ones I instantly use and throw away on the next line

