---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/01468Programverification.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Program verification](https://leanprover-community.github.io/archive/113488general/01468Programverification.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ William Whistler (Jan 12 2019 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Program%20verification/near/154986620):
<p>The stub for the program verification chapter in "Programming in Lean" says "Give some natural examples, for example, proving properties of functions of lists, sorting routines, properties of the extended gcd. Discuss two styles: separating functions and properties, and combining them, using subtypes."</p>
<p>Are any of these examples implemented, even though the chapter is incomplete? Alternatively, are there any other particularly nice examples of such proofs that someone could point me at?</p>

#### [ Mario Carneiro (Jan 12 2019 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Program%20verification/near/154986679):
<p><code>list.merge_sort</code> is a verified sorting algorithm</p>

#### [ Mario Carneiro (Jan 12 2019 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Program%20verification/near/154986682):
<p><code>list.reverse_reverse</code> is a classic example of proving a property of a program</p>

#### [ Mario Carneiro (Jan 12 2019 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Program%20verification/near/154986720):
<p>they are pretty much all implemented</p>

#### [ William Whistler (Jan 12 2019 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Program%20verification/near/154986732):
<p>Thanks for the pointers!</p>

#### [ Mario Carneiro (Jan 12 2019 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Program%20verification/near/154986745):
<p>Most of the mathlib examples use the "separate function and properties" style</p>

#### [ Mario Carneiro (Jan 12 2019 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Program%20verification/near/154986794):
<p>Minchao Wu presented a pretty good example of the "dependent types" proof approach at lean together this week</p>


{% endraw %}
