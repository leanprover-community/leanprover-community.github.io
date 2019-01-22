---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/64871pnatandequationcompiler.html
---

## [general](index.html)
### [pnat and equation compiler?](64871pnatandequationcompiler.html)

#### [Kevin Buzzard (Nov 16 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pnat%20and%20equation%20compiler%3F/near/147850385):
Can I somehow make the equation compiler work on pnat as well as it works on nat? Something like

```lean
def f : ℕ+ → ℕ+
| 1 := 37
| (n + 1) := 2 * f n 
```

How does the equation compiler work? It is presumably bound to the inbuilt constructors? Would this basically just entail writing a new pnat with `one` and `succ` and then defining stuff like `*` on the new structure?

#### [Kenny Lau (Nov 16 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pnat%20and%20equation%20compiler%3F/near/147850569):
is it possible to build a custom equation compiler?

#### [Mario Carneiro (Nov 16 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pnat%20and%20equation%20compiler%3F/near/147850900):
right. Lean 3 doesn't have the necessary customizability for this

#### [Mario Carneiro (Nov 16 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pnat%20and%20equation%20compiler%3F/near/147850924):
Although we could write our own equation compiler if we write our own version of `def`

