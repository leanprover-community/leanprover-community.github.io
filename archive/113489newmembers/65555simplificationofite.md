---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/65555simplificationofite.html
---

## [new members](index.html)
### [simplification of ite](65555simplificationofite.html)

#### [Ken Roe (Aug 11 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/simplification of ite/near/131967259):
How do I complete the following theorem:
```lean
theorem th : ∀ (a:ℕ) (b:ℕ), a ≠ b → (if a=b then 5 else 3)=3 :=
begin
    intros, ...
end
```

#### [Simon Hudon (Aug 11 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/simplification of ite/near/131967372):
`simp *`

#### [Chris Hughes (Aug 11 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/simplification of ite/near/131967501):
Also `rw if_neg h` if `h` is your proof of `a \ne b`

#### [Simon Hudon (Aug 11 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/simplification of ite/near/131967526):
For @**Chris Hughes** 's solution, you might make it clearer as `introv h, rw if_neg h`. As a habit, you should avoid referring to auto generated variable names.

#### [Patrick Massot (Aug 11 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/simplification of ite/near/131967584):
why `introv` instead of `intro` or `intros`?

#### [Patrick Massot (Aug 11 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/simplification of ite/near/131967631):
I would have done `intros a b h`

#### [Simon Hudon (Aug 11 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/simplification of ite/near/131967640):
Because the two natural numbers already have a name and we can just keep them. The assumption however is anonymous in the statement and you should rely on the name given under the hood. Additionally, we don't refer to `a` and `b` in the proof so renaming them is not very useful.

#### [Patrick Massot (Aug 11 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/simplification of ite/near/131967645):
I didn't know that tactic!

#### [Simon Hudon (Aug 11 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/simplification of ite/near/131967693):
Pretty neat eh? :)

#### [Patrick Massot (Aug 11 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/simplification of ite/near/131967704):
what does the v stand for?

#### [Simon Hudon (Aug 11 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/simplification of ite/near/131967708):
Btw @**Ken Roe**, feel free to migrate your questioning to the `general` stream of Zulip. `new members` is more for introductions I believe.

