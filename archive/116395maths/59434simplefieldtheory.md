---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/59434simplefieldtheory.html
---

## Stream: [maths](index.html)
### Topic: [simple field theory](59434simplefieldtheory.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Joey van Langen (Dec 04 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simple%20field%20theory/near/150851783):
I would like to work on some simple results about fields to contribute to the math library. Results that seem achievable are: field extensions and their degree, splitting fields, the existence and uniqueness of finite fields, maybe some galois theory. Is anyone working in this direction? If so, what has already been done?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 04 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simple%20field%20theory/near/150852014):
There is a branch `splitting_fields` on the community repo.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 04 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simple%20field%20theory/near/150852027):
Also: welcome!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 04 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simple%20field%20theory/near/150852057):
I think that branch has a definition of the splitting field, but not yet the proofs of the interesting properties.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 04 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simple%20field%20theory/near/150852105):
@**Kenny Lau** Defined the perfect closure of a field.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 04 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simple%20field%20theory/near/150852152):
See `field_theory/perfect_closure.lean`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 04 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simple%20field%20theory/near/150852231):
In general, Kenny and @**Chris Hughes** have been doing some stuff. So it would be good to check with them before you start big projects.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 04 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simple%20field%20theory/near/150852242):
I think Kenny has most of the definition of algebraic closure.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 04 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simple%20field%20theory/near/150852280):
Uniqueness of finite fields isn't there, as far as I know. Galois theory is completely missing. But I'dd love to see it there, so please work on it :smiley:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Joey van Langen (Dec 04 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simple%20field%20theory/near/150852444):
Thanks for all the information. Looking at the sources you mentioned now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 04 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simple%20field%20theory/near/150852528):
If you decide to work on splitting fields, it shouldn't be hard to give you access to the community repo, so that you can push your contributions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Dec 04 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simple%20field%20theory/near/150853364):
```quote
In general, Kenny and @**Chris Hughes** have been doing some stuff. So it would be good to check with them before you start big projects.
```
 I haven't done anything that hasn't been merged.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 04 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simple%20field%20theory/near/150853530):
Right, but it would also be a pity if people redid stuff that you did that isn't merged.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 04 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simple%20field%20theory/near/150853615):
I wrote a roadmap once

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 04 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simple%20field%20theory/near/150853674):
https://github.com/kckennylau/Lean/blob/master/algebraic-closure-roadmap.md
https://github.com/kckennylau/Lean/blob/master/Galois-theory-roadmap.md
https://github.com/semorrison/lean-category-theory/blob/master/schemes_roadmap.md

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 04 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simple%20field%20theory/near/150854972):
@**Kenny Lau** why not make your roadmaps into mathlib issues? They'd be easier to find.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Dec 04 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simple%20field%20theory/near/150869896):
My student @**Aditya Agarwal** has expressed some interest in doing some Galois theory over the summer. He's at a conference at the moment, so I'm not sure if he's started on anything yet.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 04 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simple%20field%20theory/near/150875160):
@**Scott Morrison|110087** you presumably mean Aussie summer i.e. right now?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Dec 12 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/simple%20field%20theory/near/151553124):
I've started work on splitting fields https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Splitting.20fields


{% endraw %}
