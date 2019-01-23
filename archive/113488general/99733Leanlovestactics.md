---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/99733Leanlovestactics.html
---

## Stream: [general](index.html)
### Topic: [Lean loves tactics](99733Leanlovestactics.html)

---


{% raw %}
#### [ Patrick Massot (Jun 26 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20loves%20tactics/near/128672482):
Why?
```clean

structure foo (X : Type) :=
(domain : set X)
(map : domain → X)


class bar (X : Type) :=
(foos : set (foo X))
(prop : ∀ f ∈ foos, by exact (set.range f.map = univ))

class bar' (X : Type) :=
(foos : set (foo X))
(prop : ∀ f ∈ foos, set.range f.map = univ) -- invalid field notation, type is not of the form (C ...) where C is a constant  f has type  ?m_1
```

#### [ Simon Hudon (Jun 26 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20loves%20tactics/near/128672828):
I think that's because the type of `f` is not fully elaborated by the time `f.map` is parsed. If you wrote:

```lean
(prop : ∀ f : foo _, f ∈ foos -> set.range f.map = univ)
```

I think that should work

#### [ Patrick Massot (Jun 26 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20loves%20tactics/near/128672972):
I guessed the issue comes from elaboration but couldn't see the fix

#### [ Patrick Massot (Jun 26 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20loves%20tactics/near/128672977):
This fix indeed works

#### [ Patrick Massot (Jun 26 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20loves%20tactics/near/128673023):
In the mean time I also realize that defining an auxiliary function from `foo X` to `Prop` also works

#### [ Patrick Massot (Jun 26 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20loves%20tactics/near/128673026):
Thanks

#### [ Simon Hudon (Jun 26 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20loves%20tactics/near/128673104):
Also `has_mem` has two type parameters so the type of `∈` is not enough to impose a type on `f` until type class resolution

#### [ Simon Hudon (Jun 26 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20loves%20tactics/near/128673109):
:+1:

#### [ Patrick Massot (Jun 26 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20loves%20tactics/near/128673162):
hum

#### [ Simon Hudon (Jun 26 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20loves%20tactics/near/128673304):
Can I clarify something?

#### [ Patrick Massot (Jun 26 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20loves%20tactics/near/128673320):
I think I sort of see

#### [ Chris Hughes (Jun 26 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20loves%20tactics/near/128673587):
Does elaboration always happen before type class resolution?

#### [ Simon Hudon (Jun 26 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20loves%20tactics/near/128673704):
I'm unsure whether elaboration is completed before type class resolution begins but most of it is done before type class resolution


{% endraw %}
