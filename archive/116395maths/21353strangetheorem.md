---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/21353strangetheorem.html
---

## Stream: [maths](index.html)
### Topic: [strange theorem](21353strangetheorem.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 07:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/strange%20theorem/near/125808366):
```lean
α : Type u,
A B : set α,
t : set (set α),

ht1 : t ⊆ {A},
ht2 : set.finite t,
ht3 : ⋂₀ t ⊆ B
⊢ A ⊆ B
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 07:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/strange%20theorem/near/125808368):
claim: you can't prove it without using ht2

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 07:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/strange%20theorem/near/125808416):
I mean, constructively, of course

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 28 2018 at 07:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/strange%20theorem/near/125808417):
I was going to say, I'm pretty sure *I* can prove it, since I can use LEM :simple_smile:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 07:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/strange%20theorem/near/125808418):
:D


{% endraw %}
