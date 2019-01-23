---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/11367matchindefs.html
---

## Stream: [general](index.html)
### Topic: [match in defs](11367matchindefs.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 02 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20in%20defs/near/124532070):
Out of the following two definitions, I find the first much easier to use.
```lean
private  def  mul_aux : α × S → α × S → loc α S :=
λ x y, ⟦⟨x.1  * y.1, x.2.1  * y.2.1, is_submonoid.mul_mem x.2.2 y.2.2⟩⟧

private def mul_aux : α × S → α × S → loc α S :=
λ ⟨r₁, s₁, hs₁⟩ ⟨r₂, s₂, hs₂⟩, ⟦⟨r₁ * r₂, s₁ * s₂, is_submonoid.mul_mem hs₁ hs₂⟩⟧
```

The first one unfolds much more easily if I give it arguments either of the form `x y` but also works okay with `⟨r₁, s₁, hs₁⟩ ⟨r₂, s₂, hs₂⟩` as arguments. What are the advantages/disadvantages of each approach?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 02 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20in%20defs/near/124540129):
Let me make the comment that in the past, when I have used pointy brackets and lambdas when writing a definition, I've found it much more difficult to prove things by rfl because high powered stuff is going on behind the scenes.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 02 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20in%20defs/near/124544887):
Essentially, I think it's because` λ ⟨r₁, s₁, hs₁⟩ ` uses prod.rec and subtype.rec, or the various derived lemmas like `subtype.cases_on` and these don't reduce to anything unless you give them something of the form `subtype.mk _ _` The first def will unfold when the arguments are not of the form `subtype.mk _ _`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 02 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20in%20defs/near/124545185):
don't use any pointy brackets or tactics in a definition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 03 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20in%20defs/near/124552407):
Any reason not to want this?

```
private def mul_aux : α × S → α × S → loc α S
| ⟨r₁, s₁, hs₁⟩ ⟨r₂, s₂, hs₂⟩ := ⟦⟨r₁ * r₂, s₁ * s₂, is_submonoid.mul_mem hs₁ hs₂⟩⟧ 
```

It only unfolds with explicit tuples, unlike the first alternative. In the second alternative, it will unfold to a useless auxiliary definition.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 03 2018 at 02:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20in%20defs/near/124552424):
it's private

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 03 2018 at 02:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20in%20defs/near/124552442):
Why is that relevant?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 03 2018 at 02:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20in%20defs/near/124552499):
it isn't

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 03 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20in%20defs/near/124552550):
Why was that your response to my question then?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 03 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20in%20defs/near/124552626):
it wasn't

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 03 2018 at 02:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20in%20defs/near/124552651):
it's relevant because I'm not going to unfold that definition except in the definition of multiplication

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 03 2018 at 02:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20in%20defs/near/124552691):
and I only need to use its properties, not its definition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 03 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20in%20defs/near/124552703):
Are you saying that the whole conversation is pointless?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 03 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20in%20defs/near/124552745):
he's asking about one of my definitions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 03 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20in%20defs/near/124552746):
I don't know why he's doing that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 03 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20in%20defs/near/124552749):
ok

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 03 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20in%20defs/near/124552750):
```quote
Are you saying that the whole conversation is pointless?
```
• <-- there you go, a point

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 03 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20in%20defs/near/124552879):
Sorry that, was the wrong place to write that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 03 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/match%20in%20defs/near/124552882):
sorry


{% endraw %}
