---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/16607Showingautomaticallyobtainedtypeclassinstances.html
---

## Stream: [general](index.html)
### Topic: [Showing automatically obtained typeclass instances](16607Showingautomaticallyobtainedtypeclassinstances.html)

---


{% raw %}
#### [ Seul Baek (May 29 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Showing%20automatically%20obtained%20typeclass%20instances/near/127225600):
Is it possible to show which instance Lean is using when it successfully performs a typeclass inference? 

For instance, I know from the fact that I can use `neg_le_neg` with integers that Lean has silently performed a typeclass inference and found an instance of type `ordered_comm_group int`. But I don't know exactly *which* instance Lean has found. Is there a way to display this information, similar to how I can jump to definitions using f12?

#### [ Kenny Lau (May 29 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Showing%20automatically%20obtained%20typeclass%20instances/near/127225655):
you can print the proof of your theorem

#### [ Kenny Lau (May 29 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Showing%20automatically%20obtained%20typeclass%20instances/near/127225656):
using `#print`

#### [ Kenny Lau (May 29 2018 at 01:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Showing%20automatically%20obtained%20typeclass%20instances/near/127225695):
and you can `set pp.implicit true` (there may be a better option) to see the implicit arguments, including the proof of the typeclass inference

#### [ Scott Morrison (May 29 2018 at 01:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Showing%20automatically%20obtained%20typeclass%20instances/near/127225696):
`set_option trace.class_instances true`

#### [ Kenny Lau (May 29 2018 at 01:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Showing%20automatically%20obtained%20typeclass%20instances/near/127225699):
well that displays too much information

#### [ Seul Baek (May 29 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Showing%20automatically%20obtained%20typeclass%20instances/near/127225853):
Thanks!

#### [ Mario Carneiro (May 29 2018 at 03:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Showing%20automatically%20obtained%20typeclass%20instances/near/127228102):
you can also test instance problems with
```
theorem T : ordered_comm_group int := by apply_instance
#print T
```

#### [ Kenny Lau (May 29 2018 at 03:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Showing%20automatically%20obtained%20typeclass%20instances/near/127228104):
`#check (by apply_instance : ordered_comm_group int)`

#### [ Kenny Lau (May 29 2018 at 03:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Showing%20automatically%20obtained%20typeclass%20instances/near/127228105):
do I win?

#### [ Mario Carneiro (May 29 2018 at 03:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Showing%20automatically%20obtained%20typeclass%20instances/near/127228146):
clever


{% endraw %}
