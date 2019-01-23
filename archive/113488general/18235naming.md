---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/18235naming.html
---

## Stream: [general](index.html)
### Topic: [naming](18235naming.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 09 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming/near/133613270):
So I have a bunch of standard math terminology which contains a variable (a regular cardinal $$\kappa$$) in the middle of the term. For example:
* A set is $$\kappa$$-small if its cardinality is less than $$\kappa$$.
* A category is $$\kappa$$-small if its set of morphisms is $$\kappa$$-small.
* A category $$I$$ is $$\kappa$$-filtered if any functor from a $$\kappa$$-small category to I admits a cocone.
* An object $$A$$ of a category is $$\kappa$$-compact (or $$\kappa$$-presentable) if $$\mathrm{Hom}(A, -)$$ preserves colimits whose index categories are $$\kappa$$-filtered.
* A category is locally $$\kappa$$-presentable if... well you get the idea.

I'm not sure what good Lean names for these predicates would be. Currently I have `is_kappa_small`, `kappa_filtered` etc., but that's not very satisfying because the `kappa` part of the name doesn't really refer to anything--these things all take `κ` as an explicit argument. Furthermore the `κ` will vary in some cases, for example, in a locally $$\kappa$$-presentable category, any $$\mu$$-compact object is a $$\mu$$-small $$\kappa$$-filtered colimit of $$\kappa$$-compact objects.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 09 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming/near/133613343):
To make matters worse, if you remove the "$$\kappa$$-" part of the terminology, then they become new terms with meanings which relate to the original ones in different ways. A filtered category is one which is $$\aleph_0$$-filtered, but in other places we insert "finitely" in place of $$\aleph_0$$, and "locally presentable" means locally $$\kappa$$-presentable for some $$\kappa$$.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 09 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming/near/133613436):
Things I thought about: something like `filtered_wrt κ` or `filtered_rel κ` for $$\kappa$$-filtered, but it's not really standard terminology.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 09 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming/near/133613472):
There's probably some more familiar examples as well, like being a $$p$$-group.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 09 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming/near/133613548):
How would you want to write that $$G$$ is a $$q$$-group, or a 2-group?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Sep 09 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming/near/133613887):
We currently have `zmodp` (contrast `zmod`) and `padic_*`, but the use of $$p$$ may be a special case as far as naming goes.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 09 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming/near/133614434):
I guess the names with `kappa` (or maybe `κ`) in the middle aren't so bad.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 09 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming/near/133614776):
I'm also tempted by
```lean
notation κ `-filtered`:max := kappa_filtered κ
```
but I don't know whether that is mathlib-approved

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 09 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/naming/near/133620266):
We also have that kind of problem in symplectic topology. We things called J-holomorphic curves, or ξ-convex surfaces, even when we don't specify an almost complex structure J or a contact structure ξ

