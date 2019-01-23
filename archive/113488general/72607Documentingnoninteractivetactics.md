---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/72607Documentingnoninteractivetactics.html
---

## Stream: [general](index.html)
### Topic: [Documenting non-interactive tactics](72607Documentingnoninteractivetactics.html)

---

#### [Patrick Massot (Apr 24 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Documenting%20non-interactive%20tactics/near/125638696):
@**Mario Carneiro** what's the problem with documenting non-interactive tactics?

#### [Mario Carneiro (Apr 24 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Documenting%20non-interactive%20tactics/near/125638723):
I am not saying don't document it, I'm saying document it in the docstring

#### [Patrick Massot (Apr 24 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Documenting%20non-interactive%20tactics/near/125638738):
Yes I understand

#### [Patrick Massot (Apr 24 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Documenting%20non-interactive%20tactics/near/125638742):
my question is why only in the docstring?

#### [Mario Carneiro (Apr 24 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Documenting%20non-interactive%20tactics/near/125638824):
What is the purpose of general documentation? You want to make people aware that the tactic exists and how to use it. Local tactics need not have this kind of exposure, it is sufficient to have documentation for people who see it and want to know what it does or how it works

#### [Patrick Massot (Apr 24 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Documenting%20non-interactive%20tactics/near/125638896):
Ok, it's true in this case one can hope people interested in creating such instances will have a look at existing ones, see the tactic and follow the link

#### [Patrick Massot (Apr 24 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Documenting%20non-interactive%20tactics/near/125638922):
It's difficult for me but ok, I'll go and remove some doc :cry:

#### [Patrick Massot (Apr 24 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Documenting%20non-interactive%20tactics/near/125638932):
You can go back merging :wink:

#### [Patrick Massot (Apr 24 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Documenting%20non-interactive%20tactics/near/125639129):
Done

#### [Kevin Buzzard (Apr 25 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Documenting%20non-interactive%20tactics/near/125659565):
Patrick -- I have pre-docs at https://github.com/kbuzzard/mathlib/tree/WIP_docs/docs/WIPs , just in some branch of my mathlib fork, and you could do the same (and probably do).

#### [Kevin Buzzard (Apr 25 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Documenting%20non-interactive%20tactics/near/125659576):
When I'm done with affine schemes (and I know I'm always saying this but I am nearly done -- I currently find myself actually working on an interface for localization of rings) I was going to spend some time taking stock and working out what to do next, and I might well spend some time tidying stuff up.

