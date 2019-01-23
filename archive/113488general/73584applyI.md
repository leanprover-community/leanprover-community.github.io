---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/73584applyI.html
---

## Stream: [general](index.html)
### Topic: [applyI](73584applyI.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 07 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/applyI/near/133495991):
Is there a variant on apply or refine which turns `[...]` arguments which couldn't be solved into new goals?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 07 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/applyI/near/133496017):
What are `[...]` arguments?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 07 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/applyI/near/133496109):
Class arguments

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 07 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/applyI/near/133496113):
Or instances rather

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 07 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/applyI/near/133496114):
`apply_with` allows you to provide a `apply_cfg` structure. I think `{ instances := ff }`should add them to the goals.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 07 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/applyI/near/133496119):
Ooh

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 07 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/applyI/near/133496402):
Yes, it worked.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 07 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/applyI/near/133498215):
Does `convert` work? I'm a big convert to `convert`. It seems to allow me to write proofs forwards like a mathematician would. "This term is actually the answer; I'll now pick up the pieces".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 07 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/applyI/near/133498553):
Huh, it does!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 07 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/applyI/near/133498721):
That's really good to know--I already wrote a couple "backwards" proofs involving instances (which I think are really forwards, in the sense that you are building up new known statements from old ones, rather than breaking down the goal) and I was annoyed that I couldn't write them in the normal fashion.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 07 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/applyI/near/133498749):
How long has `convert` existed? I can't believe I didn't notice it wasn't there. I only found it was there about a week ago and now I kind of feel stupid that I hadn't realised that I wanted it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 07 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/applyI/near/133498793):
For example
```lean
begin
  letI : Π (A : K ↝ Type v), is_iso (colimit.pre A (F.comp G)) :=
  begin intro A, rw colimit.pre_comp, apply_instance, end,
  apply is_cofinal_of_induced_is_iso
end
```
is now
```lean
begin
  convert is_cofinal_of_induced_is_iso _,
  intro A, rw colimit.pre_comp, apply_instance
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 07 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/applyI/near/133498834):
https://leanprover.zulipchat.com/#narrow/stream/116395-maths/subject/ZFC.20equality/near/127216190
We need better documentation!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 07 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/applyI/near/133498835):
April
https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/apply.20with.20new.20equality.20goals/near/125558382

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 07 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/applyI/near/133502820):
Maybe it would still be good to have an `applyI` tactic which is just `apply` with `{ instances := ff }`, though.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 07 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/applyI/near/133503124):
maybe we should have 32768 names for our 15 boolean configurations of `simp`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 07 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/applyI/near/133503487):
Indeed I would love to read more examples of using convert.


{% endraw %}
