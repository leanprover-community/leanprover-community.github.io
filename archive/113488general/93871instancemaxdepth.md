---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/93871instancemaxdepth.html
---

## [general](index.html)
### [instance_max_depth](93871instancemaxdepth.html)

#### [Sebastien Gouezel (Nov 10 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance_max_depth/near/147440040):
I am really proud of me :) Just encountered the famous message `maximum class-instance resolution depth has been reached`. And indeed it worked by increasing it to 38. I can't really figure out why, however, since this looks like a trivial instance to me:
```lean
set_option class.instance_max_depth 38
instance foo [metric_space α] [compact_space α] [metric_space β] [compact_space β]: 
  compact_space ((α ⊕ β) × (α ⊕ β)) := by apply_instance
```
I have already registered the instances that the product and disjoint union of compact spaces are compact spaces.

#### [Sebastien Gouezel (Nov 10 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance_max_depth/near/147440126):
Even better: if I replace the metric spaces with topological spaces, I have to increase the depth even more, but in the end there is a failure, with the message
```lean
kernel failed to type check declaration 'foo' this is usually due to a buggy tactic or a bug in the builtin elaborator
elaborated type:
  ∀ (α : Type u) (β : Type v) [_inst_1 : metric_space α] [_inst_2 : compact_space α] [_inst_3 : inhabited α]
  [_inst_4 : metric_space β] [_inst_5 : compact_space β] [_inst_6 : inhabited β] [_inst_7 : topological_space α]
  [_inst_8 : compact_space α] [_inst_9 : topological_space β] [_inst_10 : compact_space β],
    compact_space ((α ⊕ β) × (α ⊕ β))
elaborated value:
  λ (α : Type u) (β : Type v) [_inst_1 : metric_space α] [_inst_2 : compact_space α] [_inst_3 : inhabited α]
  [_inst_4 : metric_space β] [_inst_5 : compact_space β] [_inst_6 : inhabited β] [_inst_7 : topological_space α]
  [_inst_8 : compact_space α] [_inst_9 : topological_space β] [_inst_10 : compact_space β], prod.compact_space
nested exception message:
type mismatch at application
  @prod.compact_space (α ⊕ β) (α ⊕ β)
    (@uniform_space.to_topological_space (α ⊕ β)
       (@glouglou.sum.uniform_space α β (@metric_space.to_uniform_space' α _inst_1)
          (@metric_space.to_uniform_space' β _inst_4)
          (@metric_space.to_uniform_space' α _inst_1)
          (@metric_space.to_uniform_space' β _inst_4)))
    (@uniform_space.to_topological_space (α ⊕ β)
       (@glouglou.sum.uniform_space α β (@metric_space.to_uniform_space' α _inst_1)
          (@metric_space.to_uniform_space' β _inst_4)
          (@metric_space.to_uniform_space' α _inst_1)
          (@metric_space.to_uniform_space' β _inst_4)))
    (@sum.compact_space α β _inst_7 _inst_9 _inst_8 _inst_10)
term
  @sum.compact_space α β _inst_7 _inst_9 _inst_8 _inst_10
has type
  @compact_space (α ⊕ β) (@sum.topological_space α β _inst_7 _inst_9)
but is expected to have type
  @compact_space (α ⊕ β)
    (@uniform_space.to_topological_space (α ⊕ β)
       (@glouglou.sum.uniform_space α β (@metric_space.to_uniform_space' α _inst_1)
          (@metric_space.to_uniform_space' β _inst_4)
          (@metric_space.to_uniform_space' α _inst_1)
          (@metric_space.to_uniform_space' β _inst_4)))
```

#### [Kenny Lau (Nov 10 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance_max_depth/near/147440192):
I had something like 100 in the tensor product

#### [Kevin Buzzard (Nov 10 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance_max_depth/near/147442624):
yeah, thirty eight shmirty eight. I've seen over 100 too. 

What I would really like to know is *why*. I had this vague idea that somehow short cutting type class inference by defining some intermediate instances explicitly was a way to perhaps solve this (indeed I had sort-of suspected that stuff like [this](https://github.com/leanprover/mathlib/blob/891dfbbebba8a0269072460785172c294935af22/data/real/basic.lean#L26) was to stop that sort of thing from happening) but you have what looks like a fairly MWE...wait though, I can't reproduce. What do you have that I don't?

```lean
import analysis.metric_space

variables (α β : Type)

set_option class.instance_max_depth 38
instance foo [metric_space α] [compact_space α] [metric_space β] [compact_space β] :
compact_space ((α ⊕ β) × (α ⊕ β)) :=
by apply_instance -- tactic.mk_instance failed to generate instance 
```

#### [Kevin Buzzard (Nov 10 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance_max_depth/near/147442679):
https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/maximum.20class-instance.20resolution.20depth.20has.20been.20reached/near/125643888 ;-)

#### [Sebastien Gouezel (Nov 11 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/instance_max_depth/near/147469609):
This is not a MWE as the facts that a sum and a product of compact spaces are compact is not in mathlib (yet). I tried to cook up a MWE with just these instances, but then the instance_max_depth is not reached when I deal with the above example of `(α ⊕ β) × (α ⊕ β)` . I guess the problem comes from more clutter in my files...

