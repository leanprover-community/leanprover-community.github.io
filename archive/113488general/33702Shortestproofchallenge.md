---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/33702Shortestproofchallenge.html
---

## Stream: [general](index.html)
### Topic: [Shortest proof challenge](33702Shortestproofchallenge.html)

---


{% raw %}
#### [ Chris Hughes (Apr 05 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Shortest%20proof%20challenge/near/124686991):
`example (a b : ℕ) : a ≠ b →  0  < a + b `

#### [ Kevin Buzzard (Apr 05 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Shortest%20proof%20challenge/near/124688057):
`nat.rec (nat.pos_of_ne_zero) (λ n H I, nat.zero_lt_succ _) b` (or smaller if I'm allowed to open nat)

#### [ Kevin Buzzard (Apr 05 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Shortest%20proof%20challenge/near/124688064):
These games are slightly artificial because a lot depends on whether the things you want are already in lean.

#### [ Kevin Buzzard (Apr 05 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Shortest%20proof%20challenge/near/124688115):
`nat.rec (nat.pos_of_ne_zero) (λ_ H I, nat.zero_lt_succ _) b` cheating a character away

#### [ Chris Hughes (Apr 05 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Shortest%20proof%20challenge/near/124689279):
Thanks. I need this one as well 
```lean
lemma  nat.div_mul_le (a : ℕ) {b : ℕ} (hb : 0  < b) : a / b * b ≤ a
```

#### [ Kevin Buzzard (Apr 05 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Shortest%20proof%20challenge/near/124690034):
I think induction on `b` might fare less well this time.

#### [ Kenny Lau (Apr 06 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Shortest%20proof%20challenge/near/124694848):
```quote
`nat.rec (nat.pos_of_ne_zero) (λ_ H I, nat.zero_lt_succ _) b` cheating a character away
```
you don't need parentheses to enclose something without space


{% endraw %}
