---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/87225finiteness.html
---

## Stream: [general](index.html)
### Topic: [finiteness](87225finiteness.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Apr 04 2018 at 08:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finiteness/near/124610398):
Do mathlib have something that behaves like:
````
class  Finite (α : Type u) :=
  (cardinality : nat)
  (bijection : trunc (equiv α (fin cardinality)))
````

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Apr 04 2018 at 08:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finiteness/near/124610440):
Is this gross for some reason, and should be avoided?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 04 2018 at 08:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finiteness/near/124610449):
It is in my category theory repo (the category “set”)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 04 2018 at 08:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finiteness/near/124610450):
and it’s called fintype

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Apr 04 2018 at 08:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finiteness/near/124610479):
It can't be called fintype, because mathlib already has a fintype which is slightly different (but equivalent, of course).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Apr 04 2018 at 08:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finiteness/near/124610492):
I guess I'm asking if there is a strong reason to (bite the bullet and learn how to use multisets and) use mathlib's fintype, or if it's okay to use something like this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 04 2018 at 08:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finiteness/near/124610554):
oops i meant the category is called set and uses fintype

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 04 2018 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finiteness/near/124610595):
but I guess I didn’t notice that you used trunc

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 04 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finiteness/near/124610881):
That's `fintype`. If you want to use such an interface to it, prove it and use it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Apr 04 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finiteness/near/124610925):
Okay, I  guess that's a good point. In the meantime I'm discovering `fintype` is pretty easy to use anyway.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Apr 04 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finiteness/near/124611257):
What is the lemma that says `fintype` gives `decidable_eq`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 04 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finiteness/near/124611576):
I don't think it's true. So your formulation is a bit stronger, since it equips the set with a function to `fin`; in mathlib's `fintype`, this function is `index_of`, but it requires a separate proof of `decidable_eq`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 04 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finiteness/near/124611584):
your `Finite` should be equivalent to the conjunction of `fintype` and `decidable_eq`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Apr 04 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finiteness/near/124611585):
ah, okay.


{% endraw %}
