---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/56023Faileddtosynthesizetypeclassinstanceforsetdecidab.html
---

## [general](index.html)
### [Failedd to synthesize type class instance for set.decidab...](56023Faileddtosynthesizetypeclassinstanceforsetdecidab.html)

#### [AHan (Dec 14 2018 at 03:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Failedd%20to%20synthesize%20type%20class%20instance%20for%20set.decidab.../near/151749704):
In the following example,  I don't understand why lean failed to synthesize type class instance for `decidable (x ∈ s)` ?
What did I miss?

```lean
import data.set
universes u
variables {α : Type u} 

def f (x : α) (s : set α) : set α := if x ∈ s then {x} else ∅
```

#### [Bryan Gin-ge Chen (Dec 14 2018 at 04:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Failedd%20to%20synthesize%20type%20class%20instance%20for%20set.decidab.../near/151751109):
`if P then _ else _` requires `P` to be `decidable`, otherwise how will lean know which branch to take? [Here's the discussion in TPiL](https://leanprover.github.io/theorem_proving_in_lean/type_classes.html#decidable-propositions). One thing you could do is use 
```lean
open classical
local attribute [instance, priority 0] prop_decidable
```

#### [Mario Carneiro (Dec 14 2018 at 04:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Failedd%20to%20synthesize%20type%20class%20instance%20for%20set.decidab.../near/151751350):
Another way is to write the set without an if statement, i.e.
```lean
def f (x : α) (s : set α) : set α := {y | x ∈ s ∧ y = x}
```

#### [AHan (Dec 14 2018 at 08:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Failedd%20to%20synthesize%20type%20class%20instance%20for%20set.decidab.../near/151759037):
Thanks a lot! 
Both solutions are nice!!

#### [Kenny Lau (Dec 14 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Failedd%20to%20synthesize%20type%20class%20instance%20for%20set.decidab.../near/151761275):
but the latter is nicer

