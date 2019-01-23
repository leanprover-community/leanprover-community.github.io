---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/99007Floatingpoint.html
---

## Stream: [general](index.html)
### Topic: [Floating point](99007Floatingpoint.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ben Sherman (May 21 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Floating%20point/near/126891715):
Does Lean have any support for floating point? Just for computation, not necessarily reasoning?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 21 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Floating%20point/near/126892277):
there's a preliminary floating point implementation in mathlib, but as i'm sure you know, there's way less to reason about with that vs the rational numbers

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 21 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Floating%20point/near/126892298):
you'll want to ask @**Mario Carneiro** more about that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ben Sherman (May 21 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Floating%20point/near/126892439):
Oh, neat: https://github.com/leanprover/mathlib/blob/master/data/fp/basic.lean
Thanks for pointing that out to me!
Unfortunately, I was looking for something that just reduced to underlying floating point computation, so I'd have things like `log` there. Maybe I can somehow use the FFI?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 21 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Floating%20point/near/126892589):
uh, there's an FFI? the API in `lean/src/api` is for external C++ programs to call

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 21 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Floating%20point/near/126892613):
unfortunately in this case if you really need floats in a theorem prover Coq is the best bet for now...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ben Sherman (May 21 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Floating%20point/near/126893399):
Well, actually, in Coq, I'd just write the program on reals and then extract the code to floating point

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 21 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Floating%20point/near/126893511):
I'm hoping Lean 4 really improves in that regard. I can't use Lean for a lot of math-type things because it doesn't have a fast float/rational

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 21 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Floating%20point/near/126893576):
even if proving correctness with IEEE floats is a gigantic pain, handwaving and going from real to float is good enough, as you said

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 21 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Floating%20point/near/126893640):
but one of the bigger goals for the next version of Lean is better support for program extraction and a C++ FFI (I think), so I'm optimistic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 22 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Floating%20point/near/126898716):
This is a compilation issue. Lean would need native support for floating point numbers. I think this is coming with the Lean 4 compiler.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 22 2018 at 02:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Floating%20point/near/126900085):
By the way there's nothing in principle stopping us from having `log` available on floats, in fact once the rounding is done right pretty much all the functions have the same definition in terms of their real counterparts - apply function, round, special behavior at inf and nan.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 22 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Floating%20point/near/126900134):
(Although I recall hearing that some IEEE functions are impossible to round correctly, i.e. the spec requires solving an undecidable problem.)

