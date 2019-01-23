---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/13525calculationswitheq.html
---

## Stream: [general](index.html)
### Topic: [calculations with eq](13525calculationswitheq.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 22 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calculations%20with%20eq/near/128483780):
Is this provable?
```lean
lemma eq_mpr_val {α : Type} {p q : α → Prop} (e : subtype p = subtype q)
  (x : subtype q) : (eq.mpr e x).val = x.val :=
sorry
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 22 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calculations%20with%20eq/near/128483850):
(`subtype` here is just an example of a type which has a field whose type doesn't depend on the type indices being changed by `e`.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 22 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calculations%20with%20eq/near/128483937):
Or if I find myself needing to prove this sort of thing, do I need to back up and make sure that instead of this `eq.mpr e x`, I have an expression that recurses on a proof of `p = q`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 22 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calculations%20with%20eq/near/128484399):
Yeah, I don't see an alternative. `eq.mpr` is going to be difficult to get rid of. I tried various things with generalize and congr but to no avail

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 22 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calculations%20with%20eq/near/128493634):
I think it's probably not provable. I don't see a reason why `@subtype.val α p == @subtype.val α q` without `p = q`. I think in lean two types of the same size are indistinguishable, so if `p ≠ q`, but `subtype p = subtype q`, there's no contradiction, provided they're the same size, but there's no canonical isomorphism or way of identifying `@subtype.val α p` with `@subtype.val α q`. Mario will know.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jun 22 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calculations%20with%20eq/near/128493734):
I couldn't actually prove a contradiction from assuming `subtype p = subtype q`, where `p ≠ q` and your lemma though.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 23 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/calculations%20with%20eq/near/128504956):
These sorts of things are independent in lean. Injectivity of inductive type constructors is either independent or false in every case I'm aware of.

