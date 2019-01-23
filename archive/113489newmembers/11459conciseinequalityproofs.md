---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/11459conciseinequalityproofs.html
---

## Stream: [new members](index.html)
### Topic: [concise inequality proofs](11459conciseinequalityproofs.html)

---

#### [Scott Olson (Sep 27 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/concise%20inequality%20proofs/near/134732046):
How do you approach simple proofs with inequalities like this, concisely? I can always find a way, but it seems like there must be shorter ways.

```
n : ℕ,
h : 1 + n ≤ 1
⊢ n = 0
```

#### [Andrew Ashworth (Sep 27 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/concise%20inequality%20proofs/near/134732212):
the most concise way is probably to blast it away with a tactic - there are several out there

#### [Scott Olson (Sep 27 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/concise%20inequality%20proofs/near/134732996):
What are some tactics that might be able to solve this?

#### [Johannes Hölzl (Sep 27 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/concise%20inequality%20proofs/near/134733028):
`linarith` could work. I think it got some support for natural numbers.

#### [Scott Olson (Sep 27 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/concise%20inequality%20proofs/near/134733118):
You're right, `linarith` handles it

