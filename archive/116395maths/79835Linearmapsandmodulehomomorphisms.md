---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/79835Linearmapsandmodulehomomorphisms.html
---

## Stream: [maths](index.html)
### Topic: [Linear maps and module homomorphisms](79835Linearmapsandmodulehomomorphisms.html)

---


{% raw %}
#### [ Johan Commelin (May 08 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Linear%20maps%20and%20module%20homomorphisms/near/126260883):
In `algebra/module.lean` on line 78 there is `structure is_linear_map`. I have two questions:
(1) Why is this not a class?
(2) Would it make sense to call this `is_module_hom`? (For me that would be the 'expected' name.)

#### [ Kevin Buzzard (May 08 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Linear%20maps%20and%20module%20homomorphisms/near/126261114):
maps between algebraic structures are a relatively new thing in Lean and I guess people are still trying to decide whether they should be classes or not. `is_group_hom`was a `definition` a few weeks ago and is now a `class`.

#### [ Johan Commelin (May 08 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Linear%20maps%20and%20module%20homomorphisms/near/126261184):
Ok, that's good to know. To make another comment on terminology: I think it is funny that we write `[group G]` and `[is_group_hom f]`. I would expect `is_group` or `group_hom` for either of those.

#### [ Johan Commelin (May 08 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Linear%20maps%20and%20module%20homomorphisms/near/126261186):
But I guess this is also due to the organic growth...

#### [ Johan Commelin (May 08 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Linear%20maps%20and%20module%20homomorphisms/near/126261195):
Are proposals to "normalise" such conventions welcome? Or is this already in some pipeline?

#### [ Johan Commelin (May 08 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Linear%20maps%20and%20module%20homomorphisms/near/126261204):
On the other hand, I realise now that there is a real difference between homs and groups

#### [ Johan Commelin (May 08 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Linear%20maps%20and%20module%20homomorphisms/near/126261247):
A group gives you extra data, being a group_hom is merely a property

#### [ Johan Commelin (May 08 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Linear%20maps%20and%20module%20homomorphisms/near/126261252):
This is maybe reflected in the terminology


{% endraw %}
