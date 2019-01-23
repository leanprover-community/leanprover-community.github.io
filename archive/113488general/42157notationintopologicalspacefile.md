---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/42157notationintopologicalspacefile.html
---

## Stream: [general](index.html)
### Topic: [notation in topological space file](42157notationintopologicalspacefile.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 12 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20in%20topological%20space%20file/near/123620935):
In `analysis/topology/topological_space.lean` we have s and t being used for more than one thing. Even in the definition of a topological space we have
```
(is_open_inter  : ∀s t, is_open s → is_open t → is_open (s ∩ t))
(is_open_sUnion : ∀s, (∀t∈s, is_open t) → is_open (⋃₀ s))
```
Here s is an open set on one line, and a set of open sets on the next. Is this sort of thing regarded as OK? We're doing Xena tonight (it's usually Thursdays but I'm busy this Thurs) and a 2nd year undergraduate who has just learnt what a topological space is, is trying to read this mathlib file and this sort of notational trickery is not helping. Would @**Mario Carneiro** be interested in a PR which only contained changes of the form
```
(is_open_inter  : ∀s₁ s₂, is_open s₁ → is_open s₂ → is_open (s₁ ∩ s₂))
(is_open_sUnion : ∀I, (∀s∈I, is_open s) → is_open (⋃₀ I))
```
? For me, that is more readable, but might not conform to some sort of mathlib style (I'm not sure about this). Later on in `is_open_sUnion` we have a `t` in the statement and a different `t` in the proof. Of course none of this is logically wrong, but it does strike me as a strange design decision in some sense. Maybe mathematicians don't label their theorems as well as computer scientists might want them to, but I think they label their objects in a more consistent manner than this (e.g it would be considered bad writing to have s representing more than one thing, particularly two different types in consecutive sentences -- although of course I've seen it happen!)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 12 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20in%20topological%20space%20file/near/123621019):
I often use capital letters for higher order sets. So `is_open_sUnion` would become `∀S, (∀s∈S, is_open s) → is_open (⋃₀ S)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 12 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20in%20topological%20space%20file/near/123621034):
I believe there is a similar convention of changing font registers in standard math

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 12 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20in%20topological%20space%20file/near/123621093):
I usually reserve `I` or `ι` for the index set of a type/set family, say if I was discussing the indexed union instead of the set union


{% endraw %}
