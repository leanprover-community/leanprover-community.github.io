---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/12961subtypeinstance.html
---

## Stream: [general](index.html)
### Topic: [subtype_instance](12961subtypeinstance.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 15 2018 at 06:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtype_instance/near/135805972):
I'm having trouble using `subtype_instance`.

With a state of 
```
R S : examples.CommRing,
f g : R ⟶ S,
h : is_subring {r : ↥R | ⇑f r = ⇑g r}
⊢ comm_ring ↥{r : ↥R | ⇑f r = ⇑g r}
```
running `subtype_instance` reports:
```
assumption tactic failed
state:
R S : examples.CommRing,
f g : R ⟶ S,
h : is_subring {r : ↥R | ⇑f r = ⇑g r}
⊢ set ?m_1
```
Is this expected? I appreciate I may be asking too much from `subtype_instance` there.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 15 2018 at 06:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtype_instance/near/135806058):
isn't this a theorem?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 15 2018 at 06:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtype_instance/near/135806102):
A subring of a comm_ring yields a comm_ring

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 09 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtype_instance/near/147337331):
Hi @**Simon Hudon**, did you write `subtype_instance`? I think I need some help with it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 09 2018 at 00:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtype_instance/near/147337936):
Sorry, problem solved.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Nov 09 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/subtype_instance/near/147374270):
Oh! I just saw that! What was the issue?


{% endraw %}
