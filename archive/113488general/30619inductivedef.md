---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/30619inductivedef.html
---

## Stream: [general](index.html)
### Topic: [inductive def](30619inductivedef.html)

---


{% raw %}
#### [ Patrick Massot (Dec 01 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductive%20def/near/150691842):
I very rarely use inductive def so I'm a bit confused by:
```lean
-- Works ok
def find : ℕ → list ℕ → bool
| a []     := ff
| a (h::t) := if (a = h) then tt else find a t

-- Lean complains: type mismatch at application  find' a, term  a has type  ℕ but is expected to have type   list ℕ
def find' (a : ℕ) : list ℕ → bool 
| []     := ff
| (h::t) := if (a = h) then tt else find' a t
```
Is there a way to get something like my second attempt to work?

#### [ Gabriel Ebner (Dec 01 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductive%20def/near/150691886):
`find' t` (without the `a`)

#### [ Gabriel Ebner (Dec 01 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductive%20def/near/150692066):
(The parameters before the colon---`a` in this case---are assumed to be constant in the recursive calls, so you don't have to repeat them.)

#### [ Kevin Buzzard (Dec 01 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductive%20def/near/150692420):
That used to confuse me so much. 

```lean
inductive eq {α : Sort u} (a : α) : α → Prop
| refl : eq a
```

I was like "...yeah, but what is `a` equal to??". It's equal to the `a` before the colon.

#### [ Patrick Massot (Dec 01 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductive%20def/near/150692857):
Thanks!


{% endraw %}
