---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/04281matrices.html
---

## Stream: [general](index.html)
### Topic: [matrices](04281matrices.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Apr 08 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matrices/near/124777985):
any of the coq experts out there know what the most complete linalg / tensor package is out there for theorem provers? I'd like to look into what's out there for computing with complex matrices. quaternions would be cool too

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Apr 08 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matrices/near/124778185):
the top referenced paper is this: http://www.math.ias.edu/~amortberg/papers/coqeal.pdf

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Yulia Zaplatina (Jul 13 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matrices/near/129593334):
I am slightly stuck on the definition of a GL group,  has anyone defined matrices yet?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 13 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matrices/near/129593382):
@**Kevin Buzzard** your year 2 student?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matrices/near/129593530):
@**Ellen Arlt** wrote some very basic code for matrices -- defining not much more than addition and multiplication, but it might be enough to define GL. @**Blair Shi** @**Blair Shi** I should tell you about this too. I think that both of you might be thinking about linear algebra and more specifically finite-dimensional vector spaces. 

Oh -- I found Ellen's code! https://github.com/kbuzzard/xena/blob/master/student_contributions/Ellen_Arlt_matrix_rings.lean . She proves that square matrices form a ring. @**Kenny Lau** presumably there is "units of a ring" somewhere?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 13 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matrices/near/129593729):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 13 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matrices/near/129593730):
`units \a`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 13 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matrices/near/129593732):
works for fake rings also

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Yulia Zaplatina (Jul 13 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matrices/near/129593733):
@**Kevin Buzzard**  Thank you!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Yulia Zaplatina (Jul 13 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matrices/near/129593868):
Could we add @**Ellen Arlt** 's code to mathlib so we don't have to define matrices every time?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Blair Shi (Jul 13 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matrices/near/129594650):
Wow, I think this might be useful for my vector space. Thank you for telling me about this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matrices/near/129598579):
I think it would be easier to just put it into our UROP repo. It's time to start a xenalib!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 13 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matrices/near/129602034):
@**Kevin Buzzard** @**Ellen Arlt** I suggest you remove the `ring` constraint in:

```lean
definition matrix (R: Type) (n m : nat)[ring R] :=  fin n →( fin m → R ) 
```

It makes it less useable in new and creative ways and it doesn't add any value: the ring assumption is really useful only for the operations and lemmas.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matrices/near/129604111):
I'm busy today doing admin but I dumped ellen's code and Sean's comments on it here https://github.com/ImperialCollegeLondon/xena-UROP-2018/tree/master/src/xenalib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jul 13 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matrices/near/129604201):
@**Yulia Zaplatina** if you pull the xena-UROP-2018 repo and open the folder in VS Code then you should be able to type stuff like `import xenalib/Ellen_Arlt_matrix_rings` and get her definitions. Someone should merge Sean's edits as well but I need to go and throw eggs at Trump


{% endraw %}
