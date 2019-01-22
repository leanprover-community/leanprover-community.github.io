---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/51637typeclassinferenceaftercolon.html
---

## [general](index.html)
### [type class inference after colon](51637typeclassinferenceaftercolon.html)

#### [Kevin Buzzard (Mar 11 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20after%20colon/near/123577754):
In `example (α : Type) [comm_ring α] : ∀ x y z : α, x*(y+z)=x*y+x*z := mul_add`, type class inference enables us to use `mul_add`. Is it possible to move the colon to the left of the alpha though? Not that  I need to, it's just an idle question. If I try `example : ∀ (α : Type) [comm_ring α], ∀ x y z : α, x*(y+z)=x*y+x*z := mul_add` then Lean complains about not being able to find `has_add alpha` etc.

#### [Kevin Buzzard (Mar 11 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20after%20colon/near/123577804):
A related question: is there ever a difference between `[comm_ring alpha]` and `[H : comm_ring alpha]` in terms of the type class inference system? Or between `[comm_ring alpha]` and `[_inst_1 : comm_ring alpha]`?

#### [Kevin Buzzard (Mar 11 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20after%20colon/near/123578051):
And another type class subtlety. With

```
structure foo (α : Type) :=
(bar : α)
(baz : α → α)

#check @foo.bar
#check @foo.baz 
```

both `foo.bar` and `foo.baz` are `Π {α : Type},...`. But if I change the structure to a class, `foo.bar` (but not `foo.baz`) magically changes to `Π (α : Type)...` (no longer implicit). It didn't have to be that way, right? That is presumably some design decision?

#### [Mario Carneiro (Mar 11 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20after%20colon/near/123579280):
The first issue is #1920. You have to write `example : ∀ (α : Type) [comm_ring α], ∀ x y z : α, by exactI x*(y+z)=x*y+x*z` if you want to use any typeclass args right of the colon

#### [Kevin Buzzard (Mar 11 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20after%20colon/near/123579286):
Aah -- this is exactly the change that caused you so much trouble!

#### [Mario Carneiro (Mar 11 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20after%20colon/near/123579327):
The second issue is just the usual analysis of when to make arguments implicit. It's a design decision, of course, but it is reasonably predictable and well motivated

