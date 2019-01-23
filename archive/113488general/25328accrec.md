---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/25328accrec.html
---

## Stream: [general](index.html)
### Topic: [acc.rec](25328accrec.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Mar 19 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/acc.rec/near/123928942):
I've been trying to prove things using acc.rec, and I'm finding it difficult to deal with. Of these three lemmas, only the first compiled. Definitional equality doesn't always seem to work. I'm particularly surprised that the third lemma doesn't reduce, given that the two terms differ only by a proof with the same type.
```lean
lemma acc.rec_1 {α : Sort u} {r : α → α → Prop} {C : α → Sort v}
(f : Π x, (∀ y, r y x → acc r y) → (Π y, r y x → C y) → C x) {a : α}
(b : α) (h : ∀ y, r y b → acc r y) : 
@acc.rec α r C f b (acc.intro b h) = 
f b h (λ y hyb, @acc.rec α r C f y (h y hyb)) := rfl

lemma acc.rec_2 {α : Sort u} {r : α → α → Prop} {C : α → Sort v}
(f : Π x, (∀ y, r y x → acc r y) → (Π y, r y x → C y) → C x) {a : α}
(b : α) (h : ∀ y, r y b → acc r y) (h₁ : acc r b) : 
@acc.rec α r C f b h₁ = 
f b h (λ y hyb, @acc.rec α r C f y (h y hyb)) := rfl

lemma acc.rec_3 {α : Sort u} {r : α → α → Prop} {C : α → Sort v}
(f : Π x, (∀ y, r y x → acc r y) → (Π y, r y x → C y) → C x) {a : α}
(b : α) (h : ∀ y, r y b → acc r y) (h₁ : acc r b) : 
@acc.rec α r C f b h₁ = 
@acc.rec α r C f b (acc.intro b h) := rfl
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 19 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/acc.rec/near/123929213):
heh, I was just discussing how acc.rec is the root of all evil...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Mar 19 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/acc.rec/near/123929240):
`(show acc.intro b h = h₁, from rfl) ▸ rfl` works for the second two proofs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 19 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/acc.rec/near/123929323):
suffice it to say, yes this happens. Probably `congr rfl rfl` will also work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Mar 19 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/acc.rec/near/123929578):
Might be worth putting this in docs, since it is very weird behaviour.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 19 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/acc.rec/near/123936259):
See end of section 3.7 in the reference manual: https://leanprover.github.io/reference/expressions.html#computation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 19 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/acc.rec/near/123936268):
There is a problem with definitional equality, in that there is provably no algorithm which checks to see that two things are definitionally equal!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 19 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/acc.rec/near/123936316):
Lean's algorithm is an algorithm :-) so it can't be doing definitional equality correctly.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 19 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/acc.rec/near/123936399):
See Mario's Masters thesis https://github.com/digama0/lean-type-theory/releases/download/v0.1/main.pdf for some more info -- section 3.1.


{% endraw %}
