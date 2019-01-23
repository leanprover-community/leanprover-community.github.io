---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/26581puniteqpunit.html
---

## Stream: [general](index.html)
### Topic: [punit_eq_punit](26581puniteqpunit.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Apr 23 2018 at 05:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/punit_eq_punit/near/125550617):
This definition (from `library/init/data/punit.lean`) is less general than probably intended because `()` is (apparently) built-in notation for `unit.star` only, and so the full inferred type is actually `punit_eq_punit : ∀ (a : punit.{1}), @eq.{1} punit.{1} a unit.star`.
```lean
lemma punit_eq_punit (a : punit) : a = () :=
punit_eq a ()
```
Since this is in the core Lean library, is there any hope to change it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 23 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/punit_eq_punit/near/125558322):
```quote
Since this is in the core Lean library, is there any hope to change it?
```
Someone should really read that Zulip bot documentation. Programming a bot to detect this question and answer "no" is probably a nice exercise then.


{% endraw %}
