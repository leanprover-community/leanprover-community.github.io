---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/23272mustliveinsameuniverse.html
---

## Stream: [general](index.html)
### Topic: [must live in same universe](23272mustliveinsameuniverse.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jul 17 2018 at 05:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/must%20live%20in%20same%20universe/near/129790411):
Any insight into this error?
```lean
inductive value
| object : rbmap string value → value
/-
nested inductive type compiled to invalid inductive type
nested exception message:
nested inductive type compiled to invalid inductive type
nested exception message:
nested inductive type compiled to invalid inductive type
nested exception message:
nested occurrence 'rbnode.well_formed.{0} _nest_3_3.prod.json.value (fun (a : _nest_3_3.prod.json.value) (b : _nest_3_3.prod.json.value), (has_lt.lt.{0} string string.has_lt (prod.fst.{0 0} string _nest_3_3.json.value a) (prod.fst.{0 0} string _nest_3_3.json.value b)))' lives in universe '0' but must live in the same universe as the inductive types being declared, which is '1'
-/
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jul 17 2018 at 05:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/must%20live%20in%20same%20universe/near/129790488):
I think it's because `rbtree` is defined as a subtype, and so contains a field which is a Prop, but I don't know what I should do about it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 17 2018 at 05:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/must%20live%20in%20same%20universe/near/129790726):
You can only use inductive types this way. `rbnode` is inductive so you may be able to write your definition as:

```lean
inductive value
| object : forall (t : rbnode /- something in terms of value -/), t.well_formed lt -> value
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 17 2018 at 05:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/must%20live%20in%20same%20universe/near/129790735):
Then you can write a function that puts the `rbmap` back together.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 17 2018 at 05:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/must%20live%20in%20same%20universe/near/129790740):
You can define it if you use `meta inductive`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jul 17 2018 at 05:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/must%20live%20in%20same%20universe/near/129790781):
Oh nice, `meta` is good enough for me (for now anyways)


{% endraw %}
