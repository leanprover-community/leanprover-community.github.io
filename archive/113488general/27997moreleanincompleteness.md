---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/27997moreleanincompleteness.html
---

## Stream: [general](index.html)
### Topic: [more lean incompleteness](27997moreleanincompleteness.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 04 2018 at 07:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20lean%20incompleteness/near/124609074):
@**Gabriel Ebner** I found another place where I lie in the paper compared to lean's actual behavior:
```
universe u
inductive fooProp : Prop | mk : ℕ → fooProp --ok
inductive fooType : Type u | mk : ℕ → fooType --ok
inductive fooSort : Sort u | mk : ℕ → fooSort
-- universe level of type_of(arg #1) of 'foo.mk' is too big for the corresponding inductive datatype
```
I assumed the last definition should work, writing the universe constraint as `imax v u <= u` where `u` is the sort of the inductive type itself (here `u`) and `v` is the sort of the constructor argument (here `1`). Is this just because lean doesn't know how to prove `imax 1 u <= u`?

