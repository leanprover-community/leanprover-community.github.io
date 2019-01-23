---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/71476structureturnedintoclass.html
---

## Stream: [general](index.html)
### Topic: [structure turned into class](71476structureturnedintoclass.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 08 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20turned%20into%20class/near/124809321):
In `topological_space.lean`, I see:
```lean
structure topological_space (α : Type u) :=
(is_open : set α → Prop)
(is_open_univ : is_open univ)
(is_open_inter : ∀s t, is_open s → is_open t → is_open (s ∩ t))
(is_open_sUnion : ∀s, (∀t∈s, is_open t) → is_open (⋃₀ s))

attribute [class] topological_space
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 08 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20turned%20into%20class/near/124809361):
Why not directly replacing `structure` with `class`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 08 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20turned%20into%20class/near/124809362):
What would be the difference?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 08 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20turned%20into%20class/near/124809726):
Currently the operations `topological_space.is_open` has an **explicit** `topological_space` argument, when using `class` this would be a **instance** argument. So when working with multiple topologies on the same type the current way is a little bit simpler as one can just write `t.is_open s`, instead of `@is_open _ t s`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 08 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20turned%20into%20class/near/124809769):
Thanks. What does this last line do then?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 08 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20turned%20into%20class/near/124809778):
we still want to use `topological_space` as a type class, for this we need to add this attribute. Later we add `is_open` etc as names in the root namespace with the corresponding **instance** arguments.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 08 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20turned%20into%20class/near/124809868):
I sort of see. Do you have an example of a lemma involving two topological structures on the same type? I guess in this case you don't use square brackets arguments?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 08 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20turned%20into%20class/near/124810140):
I should be more precise, it is not about structures on the same type, but a way to refer explicitly to the structure and not be force to only refer to it  over the type. For example see: https://github.com/leanprover/mathlib/blob/master/analysis/topology/topological_space.lean#L712 and following.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 08 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20turned%20into%20class/near/124810253):
You mean the same definition with `class topological_space` would not give you a type `topological_space α`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 08 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20turned%20into%20class/near/124810355):
But I can still do

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 08 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20turned%20into%20class/near/124810395):
```lean
class toto (α : Type)

instance {α : Type }: group (toto α) := sorry
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 08 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20turned%20into%20class/near/124810397):
So I don't understand what you mean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 08 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20turned%20into%20class/near/124810407):
In my search for minimal example I noticed a class doesn't need to have any field :stuck_out_tongue_winking_eye:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Apr 08 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20turned%20into%20class/near/124811318):
No, `class topological_space` is nearly the same as `structure topological_space`. The main difference is the attribute added to `topological_space` and the binder information on the generated projections, i.e. that `is_open` has a explicit argument or that it has a type class instance argument.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20turned%20into%20class/near/124812952):
```lean
structure foo (α : Type) := 
(bar : α → Prop)

attribute [class] foo

class foo' (α : Type) :=
(bar' : α → Prop)

example (α : Type) [foo α] (a : α) : foo.bar a := sorry -- this doesn't work

example (α : Type) [foo' α] (a : α) : foo'.bar' a := sorry -- this works 

example (α : Type) [H : foo α] (a : α) : H.bar a := sorry -- this works

example (α : Type) [H' : foo' α] (a : α) : H'.bar' a := sorry -- this doesn't work
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20turned%20into%20class/near/124812957):
Projections work differently.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20turned%20into%20class/near/124812998):
I am not saying I understand why we want topological space to be this way, but I think this is what Johannes is saying.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/structure%20turned%20into%20class/near/124813133):
Johannes' link is to a construction partially ordering all topologies on a fixed type, so he likes `foo` better here because `H.bar` works nicely if we have `H1, H2...`


{% endraw %}
