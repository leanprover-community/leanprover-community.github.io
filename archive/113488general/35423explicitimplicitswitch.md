---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/35423explicitimplicitswitch.html
---

## Stream: [general](index.html)
### Topic: [explicit/implicit switch](35423explicitimplicitswitch.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 09 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explicit/implicit%20switch/near/127814721):
We have a section where all definitions and lemmas start with either `(A : type) [class1 A] [class2 A] [class3 A] [class4 A]` or `{A : type} [class1 A] [class2 A] [class3 A] [class4 A]` ( only difference is `()` vs `{}` in first argument). Is there any way we could tell Lean which one we want for each def/lemma without having to copy the whole line or use a different variable name? Of course simply writing `(A : Type)` or `{A : Type}` at the beginning of a def doesn't work since it shadows the variable and loses the instance implicit stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jun 09 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explicit/implicit%20switch/near/127819085):
`variable {A}` changes the binder of an existing variable `A`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jun 09 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/explicit/implicit%20switch/near/127819892):
Thanks!


{% endraw %}
