---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/01491Namingquestion.html
---

## Stream: [general](index.html)
### Topic: [Naming question](01491Namingquestion.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20question/near/124463575):
```quote
@**Simon Hudon** do you have any suggestions?
```
Not yet. I'm still trying to see what it is

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 31 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20question/near/124463576):
i asked earlier and was told just proving the central limit theorem was a massive 6000 line development in isabelle

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20question/near/124463617):
https://www3.nd.edu/~andyp/notes/CategoricalFree.pdf

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20question/near/124463618):
@**Simon Hudon** it's a brand new way of constructing free groups

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20question/near/124463620):
Can you call it `free_group` then?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20question/near/124463621):
it isn't the free group

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 31 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20question/near/124463626):
now suppose I want to formalize the statement of the curse of dimensionality, i.e. if you have a bunch of variables in R^n that are iid, most points in the sphere are located near the surface. that would be months of work, hah

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Mar 31 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20question/near/124463629):
and it would probably take me twice as long since I'm not named Mario :)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 31 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Naming%20question/near/124463783):
@**Kenny Lau**  The boring answer might be `free_group_aux`. But a nicer name might express what it does for `free_group`

