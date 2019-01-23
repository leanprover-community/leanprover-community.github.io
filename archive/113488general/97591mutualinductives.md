---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/97591mutualinductives.html
---

## Stream: [general](index.html)
### Topic: [mutual inductives](97591mutualinductives.html)

---


{% raw %}
#### [ Chris Hughes (Nov 04 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mutual%20inductives/near/137132804):
What's the "canonical" proof that the Types A and B are empty. I proved it by reference to the auxiliary `A._mut_`. Is there a nicer way?
```lean
mutual inductive A, B
with A : Type
| mk : B → A
with B : Type
| mk : A → B
```

#### [ Kenny Lau (Nov 04 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mutual%20inductives/near/137132957):
```lean
mutual inductive A, B
with A : Type
| mk : B → A
with B : Type
| mk : A → B

def A.to_sort (l : Sort*) : A → l
| (A.mk (B.mk x)) := A.to_sort x
```

#### [ Chris Hughes (Nov 04 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mutual%20inductives/near/137132960):
Of course.

#### [ Chris Hughes (Nov 04 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mutual%20inductives/near/137133128):
Are there any recursors that look a bit like this?
```lean
def AB.reca : Π {Ca : A → Sort*} {Cb : B → Sort*} 
  (ha : Π a : A, Ca a → Cb (B.mk a))
  (hb : Π b : B, Cb b → Ca (A.mk b))
  (a : A), Ca a
```

#### [ Kenny Lau (Nov 04 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mutual%20inductives/near/137133175):
you can write one


{% endraw %}
