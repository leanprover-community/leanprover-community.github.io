---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/45525tacticnoobie.html
---

## Stream: [general](index.html)
### Topic: [tactic noobie](45525tacticnoobie.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20noobie/near/133947182):
I'm taking a stab at the `tfae` tactic. This is what I have so far:
```lean
meta def tfae_have
  (p₁ : parse small_nat)
  (re : parse (((tk "→" <|> tk "->") *> return tt) <|> ((tk "↔" <|> tk "<->") *> return ff)))
  (p₂ : parse small_nat)
  (discharger : tactic unit :=
    (solve_by_elim <|> tauto <|> using_smt (smt_tactic.intros >> smt_tactic.solve_goals))) :
  tactic unit := do
    g <- get_goals,
```
Now I would like to loop over my goals, and check if any of them has the form `tfae [P, Q, ..., bla]`. How do I do that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 14 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20noobie/near/133947374):
maybe we can cocalc this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20noobie/near/133947386):
Sure!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20noobie/near/133947393):
Just in the big project?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 14 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20noobie/near/133947467):
Seems easiest

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 14 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20noobie/near/133947471):
I'm there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 14 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20noobie/near/133947610):
Maybe working on the main goal (`target`) is good enough. I'm looking at the split_ifs code and that is what it does

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 14 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20noobie/near/133947696):
I think this is going to need the tfae stuff to be defined already

