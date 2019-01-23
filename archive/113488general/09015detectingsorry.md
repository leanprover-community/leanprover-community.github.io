---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/09015detectingsorry.html
---

## Stream: [general](index.html)
### Topic: [detecting sorry](09015detectingsorry.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 02 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20sorry/near/123177763):
I am assuming that the following should be easy, or at least possible.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 02 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20sorry/near/123177765):
I have a "definition" of an affine scheme in Lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 02 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20sorry/near/123177766):
but it's not yet complete because it relies on a definition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 02 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20sorry/near/123177768):
which uses another definition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 02 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20sorry/near/123177810):
which uses another definition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 02 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20sorry/near/123177811):
which uses sorry

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 02 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20sorry/near/123177812):
`leanpkg build` will tell you about this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 02 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20sorry/near/123177814):
I was expecting to be able to spot this in VS Code (or emacs)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 02 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20sorry/near/123177821):
but `#print affine_scheme` and `#check affine_scheme` don't seem to mention this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Mar 02 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20sorry/near/123177962):
`#print axioms affine_scheme` should do the trick

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 02 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20sorry/near/123177968):
Aah yes, thanks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 02 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20sorry/near/123177969):
I knew there was a way.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 02 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20sorry/near/123177972):
I used the powerful `sorry` axiom.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 02 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20sorry/near/123178001):
I wonder why they didn't make this part of ZFC.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 02 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20sorry/near/123178022):
<close topic>

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Mar 02 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20sorry/near/123178029):
IIRC it's a very well known large cardinal axiom.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20sorry/near/123321180):
Oh wait there's still something I don't understand

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20sorry/near/123321186):
```
definition foo : ℕ → ℕ := sorry 

structure bar :=
(baz : ℕ → ℕ)
(H : baz = foo)

#print axioms bar 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20sorry/near/123321193):
Claims no axioms

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20sorry/near/123321247):
What I am hoping to find is either a method for detecting when my definition is finished

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20sorry/near/123321248):
or a proof that this can't be done

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 05 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20sorry/near/123321253):
but in my mind bar is not yet finished because it relies on unfinished foo

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 06 2018 at 03:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/detecting%20sorry/near/123330439):
```
#print axioms bar.mk
```
seems to work


{% endraw %}
