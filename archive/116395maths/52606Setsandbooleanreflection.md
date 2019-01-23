---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/52606Setsandbooleanreflection.html
---

## Stream: [maths](index.html)
### Topic: [Sets and boolean reflection](52606Setsandbooleanreflection.html)

---


{% raw %}
#### [ Tobias Grosser (Sep 19 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Sets%20and%20boolean%20reflection/near/134259292):
ssreflect has a pattern `[pick x in A | P] == Some x` (See: http://ssr.msr-inria.inria.fr/doc/ssreflect-1.5/Ssreflect.fintype.html) which is used in a proof that I want to translate from COQ. @**Johannes Hölzl** already showed me how to model other parts of ssreflect in pure lean. I wonder if there is a canonical way to express this pattern in lean?

#### [ Mario Carneiro (Sep 19 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Sets%20and%20boolean%20reflection/near/134260318):
There is `classical.some`, although I'm surprised to say there is no option-returning version of this. I guess it hasn't been necessary

#### [ Mario Carneiro (Sep 19 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Sets%20and%20boolean%20reflection/near/134260409):
The usual way we write it is to do `if h : \exists x, p x then classical.some h else default _`

#### [ Mario Carneiro (Sep 19 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Sets%20and%20boolean%20reflection/near/134260430):
where the branches are usually some more complicated expressions

#### [ Tobias Grosser (Sep 19 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Sets%20and%20boolean%20reflection/near/134261730):
Thank you. Playing with it.

#### [ Tobias Grosser (Sep 19 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Sets%20and%20boolean%20reflection/near/134265194):
This seems to not be as easy as I thought:
```lean
set_option class.instance_max_depth 200
def Gaussian_elimination [ordered_ring α] [decidable_eq α]:
   Π (m n), matrix (fin m) (fin n) α  → α
| (x+1) (y+1) A :=
  let S := { x | ¬ ((function.uncurry (A)) x = 0)} in
  if h: ∃ el, el ∈ S
  then
    let el2 := classical.some h in
    let i := el2.fst in
    let j := el2.snd in
    (A i j)
  else
  (A 0 0)
| _ _ A := (0 : α)
```

#### [ Tobias Grosser (Sep 19 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Sets%20and%20boolean%20reflection/near/134265203):
This gives me an error ```maximum class-instance resolution depth has been reached (the limit can be increased by setting option 'class.instance_max_depth') (the class-instance resolution trace can be visualized by setting option 'trace.class_instances')```


{% endraw %}
