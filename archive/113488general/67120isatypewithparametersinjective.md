---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/67120isatypewithparametersinjective.html
---

## Stream: [general](index.html)
### Topic: [is a type with parameters injective?](67120isatypewithparametersinjective.html)

---


{% raw %}
#### [ Scott Buckley (May 02 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20a%20type%20with%20parameters%20injective%3F/near/125994740):
forgive me for perhaps not using the correct terminology. what i want to know is similar to below:

```
lemma type_something_injectivity: ∀ {T1 T2:Type} {l1:list T1} {l2:list T2},
  l1 == l2 ->
  T1 = T2
:= begin
  ???
end
```

Is the above provable?

More specifically, I have some inductive type ```vexp: forall (T:Type 0), T -> Type 1```, and I want to know that ```vexp T1 v1 == vexp T2 v2 -> T1 = T2 and v1 == v2```

does this make sense?

#### [ Mario Carneiro (May 02 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20a%20type%20with%20parameters%20injective%3F/near/125998623):
Yes it makes sense to ask this question, and the answer is that it is usually independent in lean and sometimes provably false

#### [ Mario Carneiro (May 02 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20a%20type%20with%20parameters%20injective%3F/near/125998731):
```
import logic.function

inductive noninj (T : set Type) : Type
| mk : noninj

example : ¬ (∀ x y, noninj x = noninj y → x = y) :=
function.cantor_injective _
```

#### [ Scott Buckley (May 03 2018 at 03:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is%20a%20type%20with%20parameters%20injective%3F/near/126023472):
I thought that may be the case, however I couldn't understand why, but your example makes it clear. Thanks very much! :)


{% endraw %}
