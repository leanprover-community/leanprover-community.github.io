---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/03626request.html
---

## [general](index.html)
### [request](03626request.html)

#### [Scott Morrison (Oct 01 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/request/near/134968732):
Hi @**Johannes Hölzl**, @**Mario Carneiro**, I'm hoping one of you can have a look at <https://github.com/leanprover/mathlib/pull/382> for me. (It's a replacement for https://github.com/leanprover/mathlib/pull/324, which has been up for a few weeks; I cleaned up the history and left the previous discussion at the old PR.)

I need to build further on this PR in order to build one more tactic before I can continue migrating my category theory library (limits and colimits), but I'd like to be sure this first PR is okay.

#### [Scott Morrison (Oct 01 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/request/near/134968782):
This PR just extends the syntax of `solve_by_elim`, allowing the user at add or remove additional lemmas or hypotheses from the set of lemmas that are applied.

