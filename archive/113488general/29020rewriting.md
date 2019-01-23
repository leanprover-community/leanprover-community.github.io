---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/29020rewriting.html
---

## Stream: [general](index.html)
### Topic: [rewriting](29020rewriting.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Pablo Le Hénaff (Jun 08 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting/near/127773629):
Hey again,
I'm stuck with this rewriting issue, I don't understand why it won't match :'(

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Pablo Le Hénaff (Jun 08 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting/near/127773672):
```lean
set_option pp.all true
example {V : Type} (s : finset V) [decidable_eq V] (x y : V) (h : x ≠ y) :
  finset.filter (λ a : V, a = x ∧ a = y) s = finset.filter (λa, false) s :=
begin
  have : ∀a : V, a = x ∧ a = y ↔ false := sorry,
  rw [this]
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 08 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting/near/127773904):
use `simp` instead. `rw` does not rewrite bound variables. You need congruence lemmas for that and `simp` can access them.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 08 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting/near/127792061):
How come `simp` can handle rewriting the type of the `decidable_pred` instance?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 08 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting/near/127792184):
rewriting `decidable` is tricky because of how dependent those types are

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 08 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting/near/127792303):
Sorry, I misread. You're asking why it can?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 08 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewriting/near/127793688):
Yes. I always have this problem with fintype.


{% endraw %}
