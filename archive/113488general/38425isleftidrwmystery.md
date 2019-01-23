---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/38425isleftidrwmystery.html
---

## Stream: [general](index.html)
### Topic: [is_left_id rw mystery](38425isleftidrwmystery.html)

---


{% raw %}
#### [ Patrick Massot (Apr 23 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_left_id%20rw%20mystery/near/125570810):
```lean
example (R : Type) (op nil a) [is_left_id R op nil] : op nil a = a := by rw is_left_id.left_id
```
errors with:
```lean
rewrite tactic failed, did not find instance of the pattern in the target expression
  ?m_1 ?m_2 ?m_3
state:
R : Type,
op : R → R → R,
nil : out_param.{1} R,
a : R,
_inst_2 : is_left_id.{0} R op nil
⊢ @eq.{1} R (op nil a) a
```

#### [ Patrick Massot (Apr 23 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_left_id%20rw%20mystery/near/125570848):
I know I could use `is_left_id.left_id _ _` in place of the rw

#### [ Patrick Massot (Apr 23 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_left_id%20rw%20mystery/near/125570853):
But in my real use case I want to rewrite

#### [ Patrick Massot (Apr 23 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_left_id%20rw%20mystery/near/125570855):
(or simp would be even better)

#### [ Kenny Lau (Apr 23 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_left_id%20rw%20mystery/near/125570941):
```lean
example (R : Type) (op nil a) [is_left_id R op nil] : op nil a = a := by rw is_left_id.left_id op a
```

#### [ Patrick Massot (Apr 23 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_left_id%20rw%20mystery/near/125571019):
interesting

#### [ Patrick Massot (Apr 23 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_left_id%20rw%20mystery/near/125571036):
doesn't explain why unification fails though

#### [ Kenny Lau (Apr 23 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_left_id%20rw%20mystery/near/125571042):
probably because that is a higher-order unification

#### [ Kenny Lau (Apr 23 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_left_id%20rw%20mystery/near/125571047):
https://en.wikipedia.org/wiki/Unification_(computer_science)#Higher-order_unification

#### [ Kenny Lau (Apr 23 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_left_id%20rw%20mystery/near/125571048):
it is undecidable

#### [ Patrick Massot (Apr 23 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_left_id%20rw%20mystery/near/125571051):
Oh I think you're right

#### [ Patrick Massot (Apr 23 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_left_id%20rw%20mystery/near/125571140):
@**Mario Carneiro** is this part of why you don't believe in the new algebraic hierarchy? Or is it possible to recover a working simp lemma here?

#### [ Mario Carneiro (Apr 23 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_left_id%20rw%20mystery/near/125575939):
Yes, this is the main problem with the new alg hierarchy. To be fair to Leo, he's been aware of this problem since the start, and the `algebra` attribute is part of a plan to fix it, but it requires more lean support than it currently gets. It should be a part of lean 4

#### [ Patrick Massot (Apr 23 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/is_left_id%20rw%20mystery/near/125576476):
Ok, it makes sense. Do you agree that the new hierarchy seems more suitable if we want a big_op library that is really operator centric as in mathcomp?


{% endraw %}
