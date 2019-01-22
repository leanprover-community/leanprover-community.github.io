---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/31254equationhasnotbeenusedinthecompilation.html
---

## [general](index.html)
### [equation has not been used in the compilation](31254equationhasnotbeenusedinthecompilation.html)

#### [Sean Leather (Sep 15 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20has%20not%20been%20used%20in%20the%20compilation/near/134002534):
This is the first time I've seen the error below. What does it mean? What might be causing it?

```lean
error: equation compiler error, equation #2 has not been used in the compilation (possible solution: delete equation)
```

#### [Mario Carneiro (Sep 15 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20has%20not%20been%20used%20in%20the%20compilation/near/134002547):
you have a match branch that was not used

#### [Mario Carneiro (Sep 15 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20has%20not%20been%20used%20in%20the%20compilation/near/134002559):
```
def f : ℕ → ℕ
| n := n + 1
| 0 := 0
```

#### [Mario Carneiro (Sep 15 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20has%20not%20been%20used%20in%20the%20compilation/near/134002576):
It is often caused by a constant in your pattern actually being interpreted as a variable and thus being more generic than it is supposed to be

#### [Mario Carneiro (Sep 15 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20has%20not%20been%20used%20in%20the%20compilation/near/134002617):
```
def f : ℕ → ℕ
| zero := 1 -- zero is a variable since it should be nat.zero
| (n+1) := n -- not used
```

