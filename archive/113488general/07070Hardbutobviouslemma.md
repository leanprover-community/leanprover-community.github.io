---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/07070Hardbutobviouslemma.html
---

## Stream: [general](index.html)
### Topic: [Hard but obvious lemma](07070Hardbutobviouslemma.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 23 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hard%20but%20obvious%20lemma/near/128498549):
How to prove this? I don't need it, I'm just curious.
```lean
example {α β : Sort u} {γ : α → Sort v} {δ : β → Sort v} {f : Π a, γ a} {g : Π b, δ b}
  {a : α} {b : β} (hfg : f == g) (hab : a == b) : f a == g b :=
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 23 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hard%20but%20obvious%20lemma/near/128498682):
I think there’s a meta theorem that says it can’t be proved in DTT

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 23 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hard%20but%20obvious%20lemma/near/128498686):
@**Mario Carneiro**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 23 2018 at 01:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hard%20but%20obvious%20lemma/near/128498834):
In that case, same question for
```lean
example {α β : Sort u} {γ δ : Sort v} {f : α → γ} {g : β → δ}
  {a : α} {b : β} (hfg : f == g) (hab : a == b) : f a == g b
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 23 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hard%20but%20obvious%20lemma/near/128499127):
I think you would need an equality `α = β` and `γ = δ`  for this to be provable. Then, you can deduce `f = g`. I saw the theorem in a talk by Cody Roux. If I remember correctly, when you want to prove `f x₀ .. xᵢ = g y₀ .. yᵢ`, from `x₀ == y₀` .. `xᵢ == yᵢ`, you need `f = g` for the statement to be provable.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 23 2018 at 04:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hard%20but%20obvious%20lemma/near/128505009):
Leo has a whole paper on how he works around the unprovability of this theorem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 23 2018 at 04:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hard%20but%20obvious%20lemma/near/128505013):
(co-authored with Cody IIRC)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 23 2018 at 04:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hard%20but%20obvious%20lemma/near/128505054):
Although I think the actual unprovability is only folklore, I don't know an explicit proof although there is probably a way to modify the set model to get it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 23 2018 at 04:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hard%20but%20obvious%20lemma/near/128505074):
He basically generates all the relevant theorems right? I think that's what `congr` does for `heq` goals

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 23 2018 at 04:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Hard%20but%20obvious%20lemma/near/128505091):
yes, he's implemented a tactic meta-theorem for the version you stated

