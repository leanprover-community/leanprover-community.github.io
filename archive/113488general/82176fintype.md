---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/82176fintype.html
---

## Stream: [general](index.html)
### Topic: [fintype](82176fintype.html)

---


{% raw %}
#### [ Chris Hughes (Feb 27 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fintype/near/123059884):
What's the reason fintype isn't marked as Prop?

#### [ Simon Hudon (Feb 27 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fintype/near/123060084):
I think it can't be `Prop` because its accessor `elems` has a non-`Prop` type

#### [ Chris Hughes (Feb 27 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fintype/near/123060323):
Exists is a Prop, so presumably it's possible to define it in a way such that it is a Prop. I thought that since it's a subsingleton, it may as well be a Prop, but there's probably a good reason why not.

#### [ Simon Hudon (Feb 27 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fintype/near/123060387):
That's true. The difference is that `Exists` is defined using `inductive` not `structure`. Inductive doesn't come with accessors (in the case of `Exists`, the accessors could also be called the axiom of choice).

#### [ Simon Hudon (Feb 27 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fintype/near/123060434):
I think allowing `fintype` to be `Prop` would render every constructivist paranoid

#### [ Simon Hudon (Feb 27 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fintype/near/123060441):
(because merely declaring a structure could quietly add the axiom of choice into your development)

#### [ Kevin Buzzard (Feb 27 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fintype/near/123060454):
```quote
I think allowing `fintype` to be `Prop` would render every constructivist paranoid
```
I think they're already pretty paranoid if they're constructivists...

#### [ Simon Hudon (Feb 27 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fintype/near/123060505):
Should I say "paranoider"?

#### [ Chris Hughes (Feb 27 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fintype/near/123060543):
Mario mentioned that he wanted his proofs of `[fintype \a] \r [fintype \b] \r [fintype (\a \r \b)]` to be computable. Not sure why, especially since choice is everywhere in mathlib

#### [ Simon Hudon (Feb 27 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fintype/near/123060674):
Even when you assume the axiom of choice, constructive functions are great. They allow you to build programs without efforts

#### [ Kevin Buzzard (Feb 27 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fintype/near/123061184):
Try calculations with integers

#### [ Kevin Buzzard (Feb 27 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fintype/near/123061227):
What do you mean by "forever"?

#### [ Simon Hudon (Feb 27 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fintype/near/123061255):
wrong topic

#### [ Kevin Buzzard (Feb 27 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fintype/near/123061261):
damn topics

#### [ Mario Carneiro (Feb 28 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fintype/near/123067712):
`fintype` and `finite` exist exactly so that you can decide whether or not you want to work in Prop

#### [ Chris Hughes (Feb 28 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fintype/near/123067953):
Didn't know about finite. I'll have to look at it.


{% endraw %}
