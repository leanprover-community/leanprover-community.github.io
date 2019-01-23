---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/54516simpattr.html
---

## Stream: [general](index.html)
### Topic: [simp_attr](54516simpattr.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 11 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_attr/near/133724617):
I think `simp_attr` is a great idea that will help us speed up many proofs and that we should use this extensively. What do you think?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 11 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_attr/near/133724629):
if we tag a bunch of lemmas with a certain attribute, then we can avoid having `simp` to try every `simp` lemmas, but only the lemmas with a certain attribute

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 11 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_attr/near/133724696):
so maybe you have a bunch of simp lemmas associated with perfectoid spaces, then you can tag them all with an attribute `[perfectoid]`, and then if you say `simp only with perfectoid` then `simp` will only try those lemmas

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 11 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_attr/near/133724704):
@**Mario Carneiro** @**Johannes Hölzl**  is this understanding correct?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 11 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_attr/near/133725007):
Yes, this is what the `simp_attr` attribute is for. I'm just not sure what a good way of splitting the simp set is. Also I'm not sure where the simplifier loses a lot of time. One problem might acutally building up the simpset, which get more expensive when do not use the standard simp set, but add our own! The simp lemmas are indexed by their head symbol. The simplifier looks at the current position and has a fast way to select all possible rewrite rules for the current head symbol. So the simplifer does not necessarily get slower with a lot of simp lemmas.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 11 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_attr/near/133725023):
@**Kevin Buzzard** I think you would like this. A long time ago you talked to a student about speeding up simp

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 11 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_attr/near/133725058):
@**Johannes Hölzl** from my experience, a single `simp` application can take 2000 ms, while a `simp only` will only take 300 ms

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 11 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_attr/near/133725085):
but `simp only` will get long, so if we have a set set of simp rules for a particular purpose, then we can make it shorter while still preserving the speed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 11 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_attr/near/133725141):
You don't know where the simplifier loses its time. It might very well be that it checks a lot of simp lemmas, but it might also be that it is the construction of the simp set itself.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 11 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_attr/near/133725167):
what do you mean that building the simpset will get more expensive when [we] do not use the standard simp set?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 11 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_attr/near/133725297):
My guess is: adding a couple of rules to the standard simp set is a fast operation, copying and adding a couple of new entries to a hash table should be a fast operation. But merging multiple simp sets (i.e. hash tables) with a lot of clashing head symbols could be expensive in itself.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Sep 11 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_attr/near/133725321):
```quote
from my experience, a single `simp` application can take 2000 ms, while a `simp only` will only take 300 ms
```

I've seen the same thing. Consequently, I've occasionally considered looking through mathlib and replacing easy `simp`s with `simp only` to speed up the build.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 11 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_attr/near/133725325):
I should say that this is just a guess. I only roughly know how the simplifier manages its simp set.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 11 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_attr/near/133725412):
I would be very careful with the 2000ms number. In my experience this is only the case if the simp set is not cached. So if you work interactively you often run into this case. If you run the theory in batch mode it is usually cashed from the previous tactic calls.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 11 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_attr/near/133725435):
I remember some instances where Lean told me that the simplifier needed 1s or 2s to build its simp set, but it didn't show up in the batch run.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Sep 11 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_attr/near/133725441):
I don't work interactively. I only run `lean --make`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Sep 11 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_attr/near/133725500):
I should say that I was referring to the relative time difference, not the specific times that Kenny found.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 11 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_attr/near/133725503):
It could also be that the lemmas we could easily exclude by switching to a specialized simp set are ones which simp can immediately or cheaply reject based on the types not matching anyways.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 11 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_attr/near/133725525):
so if we have a specialized simp set, the things inside can't be immediately or cheaply rejected?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 11 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_attr/near/133726751):
Well it may turn out that way--if you're trying to prove a statement in topology then excluding lemmas about rings from the simp set may not save very much time

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 11 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_attr/near/133726758):
I'm not sure.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 11 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp_attr/near/133727033):
It could depend on how you form the smaller simp sets.

