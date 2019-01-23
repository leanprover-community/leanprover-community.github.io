---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/01184libaryinitalgebragroup.html
---

## Stream: [general](index.html)
### Topic: [libary/init/algebra/group](01184libaryinitalgebragroup.html)

---


{% raw %}
#### [ Kenny Lau (Apr 22 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125509188):
L165:
```lean
/- αdditive "sister" structures.
```
alpha-dditive??

#### [ Kenny Lau (Apr 22 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125509229):
is that an easter egg

#### [ Mario Carneiro (Apr 22 2018 at 01:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125509785):
I tried to PR that almost a year ago and of course it was rejected

#### [ Kenny Lau (Apr 22 2018 at 01:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125509787):
lol

#### [ Kenny Lau (Apr 22 2018 at 01:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125509788):
what was the reason

#### [ Mario Carneiro (Apr 22 2018 at 01:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125509835):
Leo doesn't want to hear about tiny changes

#### [ Kevin Buzzard (Apr 22 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125509877):
that one must be hard to review or something

#### [ Patrick Massot (Apr 22 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125509879):
That one was provocation

#### [ Mario Carneiro (Apr 22 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125509880):
It's not an easter egg, it's a bad find-replace job when we moved from using `A B C` to `α β γ` for types

#### [ Kevin Buzzard (Apr 22 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125509881):
it's a pretty spectacular bad find-replace job!

#### [ Patrick Massot (Apr 22 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125509887):
We'll need to be much more careful when we'll to the `s/α/G/g` in all group theory files

#### [ Kevin Buzzard (Apr 22 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125509888):
Did they change every A to an alpha and then change 100 alpha's back to A's?

#### [ Kevin Buzzard (Apr 22 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125509927):
put it in the pile for the one time patch

#### [ Mario Carneiro (Apr 22 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125509930):
an easter egg would be replacing `A` with a capital alpha

#### [ Patrick Massot (Apr 22 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125509980):
`variables (Α : Type) (A : Type)`

#### [ Patrick Massot (Apr 22 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125509981):
Yeah!

#### [ Patrick Massot (Apr 22 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125509983):
Lean doesn't complain

#### [ Mario Carneiro (Apr 22 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125509984):
no, that's shadowing

#### [ Mario Carneiro (Apr 22 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125509986):
but universe shadowing is disallowed for some reason...

#### [ Patrick Massot (Apr 22 2018 at 01:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125509991):
No, I the first one wasn't a capital alpha Lean would complain

#### [ Mario Carneiro (Apr 22 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125510030):
I stand corrected

#### [ Patrick Massot (Apr 22 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125510031):
Anyway, I should be sleeping

#### [ Patrick Massot (Apr 22 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125510041):
See you!

#### [ Kenny Lau (Apr 22 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/libary/init/algebra/group/near/125510125):
I just woke up


{% endraw %}
