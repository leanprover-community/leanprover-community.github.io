---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/82902easyfinitesetquestion.html
---

## [general](index.html)
### [easy finite set question](82902easyfinitesetquestion.html)

#### [Kevin Buzzard (Apr 15 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20finite%20set%20question/near/125096226):
```lean
import data.set
example (X Y : Type) (C : set X) (HC : set.finite C) (f : C → Y) : set.finite (set.range f) := sorry
```

#### [Kevin Buzzard (Apr 15 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20finite%20set%20question/near/125096272):
I see `fintype_range`, an instance proving that the range of a function with fintype domain is a fintype, but I have never worked with finite sets/types before. Should I be switching to and fro between finite sets and fintypes? Should I be letting type class inference and/or automation do the work for me? This stuff looks pretty easy in maths so hopefully isn't too painless here.

#### [Kenny Lau (Apr 15 2018 at 04:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20finite%20set%20question/near/125096454):
```
import data.set

local attribute [instance] classical.prop_decidable

example (X Y : Type) (C : set X) (HC : set.finite C) (f : C → Y) : set.finite (set.range f) :=
HC.rec $ λ HF, nonempty.intro $ @set.fintype_range _ _ _ f HF

#### [Kenny Lau (Apr 15 2018 at 04:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20finite%20set%20question/near/125096493):
```
import data.set

local attribute [instance] classical.prop_decidable

example (X Y : Type) (C : set X) (HC : set.finite C) (f : C → Y) : set.finite (set.range f) :=
let ⟨HF⟩ := HC in ⟨@set.fintype_range _ _ _ f HF⟩

#### [Kenny Lau (Apr 15 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20finite%20set%20question/near/125096591):
```
import data.set

local attribute [instance] classical.prop_decidable

example (X Y : Type) (C : set X) (f : C → Y) : set.finite C → set.finite (set.range f)
| ⟨HF⟩ := ⟨@set.fintype_range _ _ _ f HF⟩

#### [Kevin Buzzard (Apr 15 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20finite%20set%20question/near/125096597):
Thanks Kenny. I have spent all evening reducing the statement that Spec(R) is compact to the case of covers by a basis ;-)

#### [Kenny Lau (Apr 15 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20finite%20set%20question/near/125096598):
nice

