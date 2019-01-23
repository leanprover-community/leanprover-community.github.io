---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/24577idleequivquestion.html
---

## Stream: [general](index.html)
### Topic: [idle equiv question](24577idleequivquestion.html)

---

#### [Kevin Buzzard (Apr 28 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20equiv%20question/near/125831713):
```lean
universes u v
def αu (X Y : Type u) := X → Y 
def αv {X : Type u} {Y : Type v} := X → Y
def αuv {X Y : Type v} := X → Y 
```

#### [Kevin Buzzard (Apr 28 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20equiv%20question/near/125831714):
Which of those types are related by equiv?

#### [Kevin Buzzard (Apr 28 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20equiv%20question/near/125831756):
equiv is my new toy

#### [Kevin Buzzard (Apr 28 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20equiv%20question/near/125831759):
and I realise I don't understand universes

#### [Chris Hughes (Apr 28 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20equiv%20question/near/125831764):
none of them? equiv has nothing to do with universes.

#### [Gabriel Ebner (Apr 29 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20equiv%20question/near/125846281):
All of them?  Given `X` and `Y`, all of `αu X Y`, `@αv X Y`, and `@αuv X Y` are definitionally equal (and hence equiv).  You cannot even state that `αu ≃ @αuv` (as they are not types).

#### [Gabriel Ebner (Apr 29 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20equiv%20question/near/125846329):
Since you're worried about universes, let me annotate the first example with universes:  Given `X : Type u` and `Y : Type u`, all of `αu.{u} X Y`, `@αv.{u u} X Y`, and `@αuv.{u} X Y` are definitionally equal (and hence equiv).  The only potential way to even write down this statement is by using the same universe variable for both `X` and `Y`.

#### [Gabriel Ebner (Apr 29 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20equiv%20question/near/125846414):
(deleted)

#### [Gabriel Ebner (Apr 29 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20equiv%20question/near/125846600):
Maybe it's useful to think about the interpretation of `equiv` in the set-theoretic model: there, two sets are `equiv` iff they have the same cardinality.  And `Type u` is the `u`-th inaccessible cardinal.  So you're asking when two function spaces are equinumerous.

#### [Kevin Buzzard (Apr 29 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20equiv%20question/near/125852120):
The question that remains, which is not particularly well-defined, is whether it is somehow possible using `ulift` to have `{X : Type u}` and `{Y : Type v}` and (maybe using ulift here) making some kind of`alphau X Y` which is equiv to `alphauv X Y`

#### [Mario Carneiro (Apr 29 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20equiv%20question/near/125852168):
sure, `U -> V` is equiv to `ulift U -> V` or `U -> ulift V`

#### [Mario Carneiro (Apr 29 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20equiv%20question/near/125852179):
(not sure why you are writing it with the funny notation, but that's just the arrow type)

