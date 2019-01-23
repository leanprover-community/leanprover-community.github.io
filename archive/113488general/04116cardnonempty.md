---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/04116cardnonempty.html
---

## Stream: [general](index.html)
### Topic: [card_nonempty](04116cardnonempty.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 08 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/card_nonempty/near/133577651):
Is there some easy way to tackle this goal:
```lean
n : Type u,
_inst_1 : fintype n,
h : nonempty n
⊢ 0 < fintype.card n
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 08 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/card_nonempty/near/133577761):
```lean
import data.fintype

universe u
variables (n : Type u) [fintype n]
example (h : nonempty n) : 0 < fintype.card n :=
begin
  by_contra H,
  rw [not_lt, nat.le_zero_iff, fintype.card_eq_zero_iff] at H,
  exact h.rec_on H
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 08 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/card_nonempty/near/133577817):
I guess this could be a simp lemma in mathlib?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 08 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/card_nonempty/near/133577822):
Ooh, and thanks!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 08 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/card_nonempty/near/133577926):
```lean
import set_theory.cardinal

universe u
variables (n : Type u)
example (h : nonempty n) : 0 < cardinal.mk n :=
by rwa [cardinal.pos_iff_ne_zero, cardinal.ne_zero_iff_nonempty]
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 08 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/card_nonempty/near/133577929):
I think Mario likes cardinal.mk more than fintype.card

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 08 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/card_nonempty/near/133578072):
It is in mathlib. `fintype.card_pos_iff` I believe.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 08 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/card_nonempty/near/133578180):
Aaah, thanks! (Sorry, Kenny)

