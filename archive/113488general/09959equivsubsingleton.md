---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/09959equivsubsingleton.html
---

## Stream: [general](index.html)
### Topic: [equiv_subsingleton](09959equivsubsingleton.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 14 2019 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv_subsingleton/near/155086021):
I couldn't find this in mathlib. Is this considered useful enough to include?
```lean
lemma equiv_subsingleton {α β : Type*} [subsingleton α] [subsingleton β] (f : α → β) (g : β → α) :
α ≃ β :=
{ to_fun := f,
  inv_fun := g,
  left_inv := λ _, subsingleton.elim _ _,
  right_inv := λ _, subsingleton.elim _ _, }
```
If so, where should it go?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 14 2019 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv_subsingleton/near/155086282):
Only one of them needs to be a subsingleton.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 14 2019 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv_subsingleton/near/155087369):
I misread the statement

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 14 2019 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv_subsingleton/near/155119532):
@**Johan Commelin** it isn't a lemma

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 15 2019 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equiv_subsingleton/near/155147420):
Yes it is useful. Not sure about the name though, it should be in the `equiv` namespace. Perhaps `equiv.of_subsingleton`?


{% endraw %}
