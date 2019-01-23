---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/40432easysubsetsubtypelemma.html
---

## Stream: [general](index.html)
### Topic: [easy subset/subtype lemma](40432easysubsetsubtypelemma.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 16 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20subset/subtype%20lemma/near/129752088):
I've reduced my goal to

```lean
example (X : Type) (U A B : set X) : U ∩ A = U ∩ B ↔ {u : U | u.val ∈ A} = {u : U | u.val ∈ B} := sorry 
```

Is there a one-liner for this? As it happens I only need the <- direction but it somehow all looks easy.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 16 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20subset/subtype%20lemma/near/129752297):
can you try `by ext; dsimp; tauto`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 16 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20subset/subtype%20lemma/near/129752338):
Sorry, no that won't work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 16 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20subset/subtype%20lemma/near/129752413):
there should be a lemma `{x : A | x \in B} = A \cap B`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 16 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20subset/subtype%20lemma/near/129752438):
wait, that's not type correct

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 16 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20subset/subtype%20lemma/near/129752451):
hence Kevin's `.val`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 16 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20subset/subtype%20lemma/near/129752573):
Second attempt: `dsimp [set_eq_def]; apply forall_congr; tauto`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 16 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20subset/subtype%20lemma/near/129752609):
I think `and.congr_right` needs a biconditional version

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 16 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20subset/subtype%20lemma/near/129753490):
```lean
lemma and.congr_right_iff {a b c : Prop} : (a ∧ b ↔ a ∧ c) ↔ (a → (b ↔ c)) :=
⟨λ h ha, by simp [ha] at h; exact h, and_congr_right⟩

example (X : Type) (U A B : set X) :
  U ∩ A = U ∩ B ↔ {u : U | u.val ∈ A} = {u : U | u.val ∈ B} :=
by simp [set.set_eq_def, and.congr_right_iff]
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 16 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20subset/subtype%20lemma/near/129754062):
Thanks Mario.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 16 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20subset/subtype%20lemma/near/129754286):
@**Luca Gerolla** is doing homotopy theory in Lean and this was all that was left for proving that a function on [0,1] is continuous iff its restriction to [0,1/2] and [1/2,1] is.


{% endraw %}
