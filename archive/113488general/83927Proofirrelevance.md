---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/83927Proofirrelevance.html
---

## Stream: [general](index.html)
### Topic: [Proof irrelevance](83927Proofirrelevance.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Dec 13 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20irrelevance/near/151624464):
Does anyone know whether https://hal.inria.fr/hal-01859964 is something Lean should care about? It's a paper about "Definitional Proof-Irrelevance without K" which explicitly mentions Lean's type theory.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Dec 13 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20irrelevance/near/151721652):
Their typesetting ate the → symbols. :sad: Maybe I'm missing something, but the results are not very exciting to me.  In summary, they add a universe `sProp u` of squashed types, whose elements are then made definitionally equal.  They don't have any good ideas for the problems with `acc` that make type-checking undecidable in Lean.  They just disallow subsingleton elimination completely, so you can't even cast along equations...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 13 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20irrelevance/near/151722715):
only some of them... the Agda code also has some missing → symbols, but also some visible ones

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Dec 13 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20irrelevance/near/151722732):
(By exciting I mean exciting for math/programming in Lean.  The idea of using squash types with definitional equality could be nice in HoTT (I guess we could even squash in Lean by going into `Prop`).)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 13 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20irrelevance/near/151722733):
also the lambdas

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 13 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20irrelevance/near/151722777):
what is the intuition behind these squash types?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 13 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20irrelevance/near/151722793):
are they like HoTT propositions or lean propositions?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Dec 13 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20irrelevance/near/151722889):
They're essentially just ~~quotients with the universal relation~~ + definitional equality.  The rules are on page 10.  Edit: no they're even less---you can't eliminate into Type at all from squash types.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 13 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof%20irrelevance/near/151724356):
I think the moral of the story is that everything you can do with sType is already possible in lean, this paper just describes how


{% endraw %}
