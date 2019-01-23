---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/25792zeroideal.html
---

## Stream: [maths](index.html)
### Topic: [zero ideal](25792zeroideal.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 17 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ideal/near/152032669):
I lost the zero ideal during the module refactor. Does anyone know where it ended up?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 17 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ideal/near/152032688):
I guess it is now `⊥`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 17 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ideal/near/152032759):
Thanks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 17 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ideal/near/152032784):
I'm a very slow learner. I was looking for something named zero

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 17 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ideal/near/152032827):
lol

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 17 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ideal/near/152032844):
"I lost something" -- what is it? "I lost the zero ideal"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 17 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ideal/near/152032859):
```quote
I'm a very slow learner. I was looking for something named zero
```
 That would be too easy.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 17 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ideal/near/152032888):
Who would think that zero is a more natural thing than the bottom of a lattice nowadays?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 17 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ideal/near/152033162):
`ideal.mul_mem_left : ∀ {α : Type u_1} [_inst_1 : comm_ring α] (I : ideal α) {a b : α}, b ∈ I → a * b ∈ I` What happened to binder types here?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 17 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ideal/near/152033212):
what binder types?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 17 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ideal/near/152033393):
Why not
```lean
lemma ideal.mul_mem_left' {α : Type*} [comm_ring α] {I : ideal α} (a : α) {b : α} (h : b ∈ I) : a * b ∈ I :=
ideal.mul_mem_left _ h
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 17 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ideal/near/152033413):
Like, I want `a` and `b ∈ I` to be explicit, and everything else implicit

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 17 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ideal/near/152033432):
because we want to write `I.mul_mem_left _ _`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 17 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ideal/near/152033567):
And how does it guess who is `a`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 17 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ideal/near/152033607):
from the type

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 17 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ideal/near/152033761):
hmm


{% endraw %}
