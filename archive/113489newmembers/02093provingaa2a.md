---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/02093provingaa2a.html
---

## Stream: [new members](index.html)
### Topic: [proving a + a = 2* a](02093provingaa2a.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Atze van der Ploeg (Jan 11 2019 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20a%20%2B%20a%20%3D%202%2A%20a/near/154909221):
I'm trying to prove the shocking lemma ∀ n : ℕ, n + n = 2*n , how do i tell lean to unfold the definition of *?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 11 2019 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20a%20%2B%20a%20%3D%202%2A%20a/near/154909512):
you don't; you just tell Lean what you want it to unfold to

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 11 2019 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20a%20%2B%20a%20%3D%202%2A%20a/near/154909517):
There's a lemma `nat.mul_succ`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Jan 11 2019 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20a%20%2B%20a%20%3D%202%2A%20a/near/154909526):
You can use `simp only [(*)]`. This will unfold the notation, then you'll have to deal with the definition `nat.mul`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 11 2019 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20a%20%2B%20a%20%3D%202%2A%20a/near/154909570):
Sorry, `nat.succ_mul`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Jan 11 2019 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20a%20%2B%20a%20%3D%202%2A%20a/near/154909583):
You can unfold that with the same method, or `unfold nat.mul`, but since it's defined by recursion on `n`, you'll have to use induction first.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 11 2019 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20a%20%2B%20a%20%3D%202%2A%20a/near/154909621):
You can't actually unfold multiplication in this scenario, since it's defined by recursion on the second argument.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 11 2019 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20a%20%2B%20a%20%3D%202%2A%20a/near/154909625):
well I imagined he would do induction on `n`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Atze van der Ploeg (Jan 11 2019 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20a%20%2B%20a%20%3D%202%2A%20a/near/154912689):
Thanks, nat.succ_mul works fine, or using mul_comm but this requires me to know that nat.mul is defined by recursively on the second argument.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 11 2019 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20a%20%2B%20a%20%3D%202%2A%20a/near/154913474):
You can just use the 'ring' tactic if you don't care about what the low level proof looks like

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mark Dickinson (Jan 11 2019 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20a%20%2B%20a%20%3D%202%2A%20a/near/154936758):
There's also `two_mul` in the standard library:
```lean
two_mul : ∀ {α : Type u_1} [_inst_1 : semiring α] (n : α), 2 * n = n + n
```


{% endraw %}
