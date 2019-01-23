---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/95636checkgivinganunexpectederror.html
---

## Stream: [general](index.html)
### Topic: [#check giving an unexpected error](95636checkgivinganunexpectederror.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) M. Andrew Moshier (Apr 27 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23check%20giving%20an%20unexpected%20error/near/125761013):
This example illustrates behavior I am not able to explain. #check gives expected answers for sub-expressions, but not for `G.arr A B` unless I explicitly decorate `G.arr` with its type. But the example shows that #check already correctly inferred the type.

Any ideas why?

```
class {u} graph (α : Type u) := 
    (arr : α  → α  → Sort u)

variable α : Type 1
variables A B : α
variable G : graph α 


#check G         -- G : graph α 
#check G.arr     -- graph.arr : α → α → Type
#check A         -- A : α
#check G.arr A B -- error "invalid field notation, 
                 -- function 'graph.arr' does not have explicit argument 
                 -- with type (graph ...)"
#check (G.arr : α → α → Type) A B
                 -- G.arr A B : Type   (as expected)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 27 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23check%20giving%20an%20unexpected%20error/near/125761057):
what does `#check @graph.arr` give?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 27 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23check%20giving%20an%20unexpected%20error/near/125761061):
```lean
graph.arr : Π {α : Type u_1} [c : graph α], α → α → Sort u_1
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 27 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23check%20giving%20an%20unexpected%20error/near/125761062):
the `graph` is not the **first explicit argument** of `graph.arr`, so projection fails

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 27 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23check%20giving%20an%20unexpected%20error/near/125761070):
If you make it a `structure`, then you can use projections, as it becomes:
```lean
graph.arr : Π {α : Type u_1}, graph α → α → α → Sort u_1
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) M. Andrew Moshier (Apr 27 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23check%20giving%20an%20unexpected%20error/near/125761080):
` Π {α : Type u_1} [c : graph α], α → α → Sort u_1`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 27 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23check%20giving%20an%20unexpected%20error/near/125761161):
alternative solution:
```lean
class {u} graph (α : Type u) :=
    (arr : α  → α  → Sort u)

def graph.arr_proj {α} (G : graph α) : α → α → Sort _ :=
@graph.arr α G

variable α : Type 1
variables A B : α
variable G : graph α

#check G.arr_proj A B
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) M. Andrew Moshier (Apr 27 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23check%20giving%20an%20unexpected%20error/near/125761175):
I think my problem is I don't quite understand how `[...]` arguments are dealt with. My intuition is that `G.arr` ought to resolve correctly to the right type. I see why your soln works, but not why mine does not. Anyway, thanks.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 27 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23check%20giving%20an%20unexpected%20error/near/125761220):
I already told you

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 27 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23check%20giving%20an%20unexpected%20error/near/125761222):
```quote
the `graph` is not the **first explicit argument** of `graph.arr`, so projection fails
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 27 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23check%20giving%20an%20unexpected%20error/near/125761223):
Alternative solution, don't mention `G` at all
```
class {u} graph (α : Type u) :=
    (arr : α  → α  → Sort u)

variable α : Type 1
variables A B : α
variable G : graph α
include G

#check graph.arr A B
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 27 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23check%20giving%20an%20unexpected%20error/near/125761231):
when you use typeclass arguments (by marking `graph` as `class`), the idea is that you don't mention the variables of those types at all, they are inferred from context

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 27 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23check%20giving%20an%20unexpected%20error/near/125761239):
you win

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 27 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23check%20giving%20an%20unexpected%20error/near/125761243):
Actually the usual way to write `G` there is `variable [graph α]` and skip the `include` line

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 27 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23check%20giving%20an%20unexpected%20error/near/125761291):
right, you don't give names to instances of class

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 27 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23check%20giving%20an%20unexpected%20error/near/125761293):
confer how partial orders are defined

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 27 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23check%20giving%20an%20unexpected%20error/near/125761294):
and used

#### [![Click to go to Zulip](../../assets/img/zulip2.png) M. Andrew Moshier (Apr 27 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23check%20giving%20an%20unexpected%20error/near/125761349):
Thanks both.


{% endraw %}
