---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/01468Programverification.html
---

## Stream: [general](index.html)
### Topic: [Program verification](01468Programverification.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) William Whistler (Jan 12 2019 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Program%20verification/near/154986620):
The stub for the program verification chapter in "Programming in Lean" says "Give some natural examples, for example, proving properties of functions of lists, sorting routines, properties of the extended gcd. Discuss two styles: separating functions and properties, and combining them, using subtypes."

Are any of these examples implemented, even though the chapter is incomplete? Alternatively, are there any other particularly nice examples of such proofs that someone could point me at?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 12 2019 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Program%20verification/near/154986679):
`list.merge_sort` is a verified sorting algorithm

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 12 2019 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Program%20verification/near/154986682):
`list.reverse_reverse` is a classic example of proving a property of a program

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 12 2019 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Program%20verification/near/154986720):
they are pretty much all implemented

#### [![Click to go to Zulip](../../assets/img/zulip2.png) William Whistler (Jan 12 2019 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Program%20verification/near/154986732):
Thanks for the pointers!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 12 2019 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Program%20verification/near/154986745):
Most of the mathlib examples use the "separate function and properties" style

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 12 2019 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Program%20verification/near/154986794):
Minchao Wu presented a pretty good example of the "dependent types" proof approach at lean together this week


{% endraw %}
