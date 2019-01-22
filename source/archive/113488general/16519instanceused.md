---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/16519instanceused.html
---

## [general](index.html)
### [instance used](16519instanceused.html)

#### [petercommand (Nov 18 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance%20used/near/147922878):
is there some way to show which instance (of a class) is actually used in a definition? If I use ```set_option trace.class_instances true```, it lists lots of possible instances, but I only want the actual instance used

#### [Mario Carneiro (Nov 18 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance%20used/near/147922929):
I sometimes grep the output to remove lines immediately followed with `failed defeq`

#### [Mario Carneiro (Nov 18 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance%20used/near/147922937):
but of course you can always just look at the term

#### [petercommand (Nov 18 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance%20used/near/147922940):
just look at the term?

#### [petercommand (Nov 18 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance%20used/near/147922941):
yeah, I can grep the output

#### [Mario Carneiro (Nov 18 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance%20used/near/147922984):
Just trigger the instance search manually. For example:
```lean
set_option pp.implicit true
#check (by apply_instance : preorder int)
-- @partial_order.to_preorder ℤ
--   (@ordered_comm_group.to_partial_order ℤ
--      (@ordered_ring.to_ordered_comm_group ℤ
--         (@linear_ordered_ring.to_ordered_ring ℤ
--            (@linear_ordered_comm_ring.to_linear_ordered_ring ℤ
--               (@decidable_linear_ordered_comm_ring.to_linear_ordered_comm_ring ℤ
--                  int.decidable_linear_ordered_comm_ring))))) :
--   preorder ℤ
```

#### [petercommand (Nov 18 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance%20used/near/147922996):
Ah..that works great! Thanks!

#### [Kenny Lau (Nov 18 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance%20used/near/147923628):
alternatively:
```lean
set_option pp.implicit true
#check (infer_instance : preorder int)
/-
@infer_instance (preorder ℤ)
  (@partial_order.to_preorder ℤ
     (@ordered_comm_group.to_partial_order ℤ
        (@ordered_ring.to_ordered_comm_group ℤ
           (@linear_ordered_ring.to_ordered_ring ℤ
              (@linear_ordered_comm_ring.to_linear_ordered_ring ℤ
                 (@decidable_linear_ordered_comm_ring.to_linear_ordered_comm_ring ℤ
                    int.decidable_linear_ordered_comm_ring)))))) :
  preorder ℤ
-/
```

