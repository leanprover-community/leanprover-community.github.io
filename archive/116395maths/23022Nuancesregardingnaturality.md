---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/23022Nuancesregardingnaturality.html
---

## Stream: [maths](index.html)
### Topic: [Nuances regarding naturality](23022Nuancesregardingnaturality.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 05 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances%20regarding%20naturality/near/135266364):
https://mathoverflow.net/questions/244131/nuances-regarding-naturality?noredirect=1&lq=1

Does Lean have a good answer to this question? My understanding is that the OP is trying to define data which involves an uncomputable choice of some other data (and it's a theorem that such a choice can always be made in at least one way) and then a proof that the data we care about is independent of this uncomputable choice.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 05 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances%20regarding%20naturality/near/135266773):
Is the function that sends a vector space to the cardinal corresponding to its dimension any "better" in any way than the function that sends a vector space to a basis which was chosen using the axiom of choice?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 05 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances%20regarding%20naturality/near/135271784):
Perhaps I'm missing something, but the dimension function is defined using the "choose-a-basis" function, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 05 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances%20regarding%20naturality/near/135271867):
I ran into this when I was working on the rank function for matroids (which is a generalization of dimension for f.d. vector spaces); even with unique existence, you still have to apply some form of choice to define the actual nat.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 05 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances%20regarding%20naturality/near/135272437):
Yes. The question is whether the added nuance of the proof that the output is independent of the choice can be expressed in Lean. A mathematician might argue that they hadn't "seriously" used choice, or something. I was wondering if there was anything in this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Oct 05 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances%20regarding%20naturality/near/135272490):
It could still be done computably, using `trunc`, instead of` exists`, and `quot.lift` instead of choice.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 05 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances%20regarding%20naturality/near/135272523):
The dimension function can be defined using only "unique choice" `nonempty a -> (\all x y : a, x = y) -> a`. This is just as noncomputable as full choice but philosophically less problematic (at least to me) because the type of the "unique choice" constant is a subsingleton.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 05 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances%20regarding%20naturality/near/135272533):
Another formulation is `nonempty a -> trunc a`, yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 05 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances%20regarding%20naturality/near/135272596):
At the time I ended up throwing in an `encodable` instance. I'll have to look into `trunc` now that I know a little more about it though.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 05 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances%20regarding%20naturality/near/135272696):
The "pick a basis" function is different because its value depends on the interpretation of the `choice` constant

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 05 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances%20regarding%20naturality/near/135273811):
What's `nonempty a -> trunc a`? I see `nonempty_of_trunc` in mathlib but not the other way around. Is this because in lean's foundations there's no unique choice? To define the dimension function in lean, am I right that you could only do it by returning the cardinality of "pick a basis"? Well-definedness would be proven and used separately I suppose.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 05 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances%20regarding%20naturality/near/135273995):
`choice`, then `trunc.mk`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 05 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances%20regarding%20naturality/near/135274205):
Lean's core library only has the axiom `choice`, and derives all the other classical principles from it. So in this setup you can't make fine distinctions between things like using choice and only using unique choice. However, you could imagine adding unique choice (and LEM) as separate axioms.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 05 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances%20regarding%20naturality/near/135274280):
You could also add the "axiom of choice" (which is a Prop) as a separate axiom.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 05 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances%20regarding%20naturality/near/135274327):
Then you could define the dimension function using only the "axiom of choice" (to prove `nonempty (basis V)`) and "unique choice" (to extract the dimension)--in order to do this you *have* to prove that every basis has the same cardinality

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 05 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances%20regarding%20naturality/near/135274384):
Both of these axioms are subsingletons, so you can conclude that the dimension of a vector space doesn't depend on the interpretation of `choice` or on any other "arbitrary choices".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 05 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances%20regarding%20naturality/near/135274415):
You cannot define the "pick a basis" function this way

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 05 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances%20regarding%20naturality/near/135274693):
is it possible to define `trunc (basis V)` computably?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 05 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances%20regarding%20naturality/near/135274730):
How are you given `V`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 05 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances%20regarding%20naturality/near/135274795):
```
k : Type u
V : Type v
_inst_1 : field k
_inst_2 : vector_space k V
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Oct 05 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances%20regarding%20naturality/near/135274888):
@**Kenny Lau** providing a truncated basis could be part of the definition of finite dimensional vector space.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Oct 05 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances%20regarding%20naturality/near/135274976):
For the infinite case you can't do it, but who cares when cardinals don't have decidable equality.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 05 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Nuances%20regarding%20naturality/near/135274977):
so essentially I'm asking for a term of the type `\Pi (k : Type u) (V : Type v) [field k] [vector_space k V], trunc (basis k V)`

