---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/07977existselimintacticmode.html
---

## [new members](index.html)
### [exists.elim in tactic mode?](07977existselimintacticmode.html)

#### [Abhimanyu Pallavi Sudhir (Oct 11 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/exists.elim%20in%20tactic%20mode%3F/near/135602582):
Hi -- I've been trying to prove a certain relation is symmetric -- is there a way to use "exists.elim" in tactic mode? It always gives me errors.

#### [Johan Commelin (Oct 11 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/exists.elim%20in%20tactic%20mode%3F/near/135602627):
Is that `existsi`?

#### [Edward Ayers (Oct 11 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/exists.elim%20in%20tactic%20mode%3F/near/135602711):
`cases h with x p` will take an existential hypothesis and hit it with `exists.elim`

#### [Johan Commelin (Oct 11 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/exists.elim%20in%20tactic%20mode%3F/near/135602728):
Aah, in that case, you might also be interested in `rcases`. It is `cases` on steroids.

#### [Edward Ayers (Oct 11 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/exists.elim%20in%20tactic%20mode%3F/near/135602865):
```lean
example (P : α → Prop) (Q : Prop) (h₁ : ∃ x, P(x)) (h₂ : ∀ x, P(x) → Q) : Q :=
begin
    cases h₁ with x h₃, -- you can also omit the `with` and it will name them `h₁_w` and `h₁_h`
    apply h₂ _ h₃
end
```

#### [Abhimanyu Pallavi Sudhir (Oct 11 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/exists.elim%20in%20tactic%20mode%3F/near/135602884):
Ok, that seems to work, thanks. It's quite natural to uses cases on ∃, certainly.

#### [Abhimanyu Pallavi Sudhir (Oct 11 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/exists.elim%20in%20tactic%20mode%3F/near/135603772):
(deleted)

#### [Abhimanyu Pallavi Sudhir (Oct 11 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/exists.elim%20in%20tactic%20mode%3F/near/135603852):
(deleted)

#### [Abhimanyu Pallavi Sudhir (Oct 11 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/exists.elim%20in%20tactic%20mode%3F/near/135603888):
(deleted)

#### [Bryan Gin-ge Chen (Oct 11 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/exists.elim%20in%20tactic%20mode%3F/near/135610299):
I've been writing `exact exists.elim h (by { intro x hx, ... })`, but maybe that's considered less elegant.

#### [Kenny Lau (Oct 11 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/exists.elim%20in%20tactic%20mode%3F/near/135610649):
yes, that is considered less elegant

#### [Kevin Buzzard (Oct 11 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/exists.elim%20in%20tactic%20mode%3F/near/135616278):
Elegance was never my strong point when it came to Lean code.

#### [Kevin Buzzard (Oct 11 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/exists.elim%20in%20tactic%20mode%3F/near/135616293):
Lucky I might now have an MSc student who will elegantify my code :D

