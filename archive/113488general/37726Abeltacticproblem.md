---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/37726Abeltacticproblem.html
---

## Stream: [general](index.html)
### Topic: [Abel tactic problem](37726Abeltacticproblem.html)

---

#### [Neil Strickland (Jan 16 2019 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Abel%20tactic%20problem/near/155242485):
I tried the following:
```lean

lemma L1 (M : Type*) [comm_semiring M] (s t u v : M) :
 s * u * (t * v) = s * t * (u * v) := by ring.

lemma L2 (M : Type*) [comm_monoid M] (s t u v : M) :
 s * u * (t * v) = s * t * (u * v) := by abel

```

`L1` works but `L2` gives `abel failed to simplify`.  Is this a bug or am I misunderstanding something?

#### [Chris Hughes (Jan 16 2019 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Abel%20tactic%20problem/near/155242603):
Glancing over the code for abel, it appears it only works with addition.

#### [Neil Strickland (Jan 16 2019 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Abel%20tactic%20problem/near/155243065):
OK, you seem to be right.  It would be good if the tactic docstring mentioned that.  Do you understand the story about the `to_additive` attribute?  It would be  nice if we could automagically make `abel` work with both additive and multiplicative monoids, but I have no idea how to go about that.

#### [Kevin Buzzard (Jan 16 2019 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Abel%20tactic%20problem/near/155245482):
The story is that typeclasses were invented to be a cool way to deal with notation in Haskell, Lean has taken them to extremes, and now we discover that what looked like a cool definition of a group turns out to be bound to a notation for the group law. No reasonable solution to this has yet been found, or at least, to my knowledge, has been coded in Lean. The `to_additive` thing is just a hack which attempts to switch `has_mul.mul` to `has_add.add`, with limited success (the definition of "success" would be "nobody has to ever worry about this issue ever again and it all happens automatically whenever we want it to", which is apparently an unattainable dream). A structure equipped with a `has_mul.mul` instance is canonically isomorphic to a structure equipped with a `has_add.add` instance, however as you surely know by now, the CS guys cannot seem to write a tactic which seamlessly moves from one to the other -- or at least they have not done this yet. So currently we are stuck with `group` and `add_group`, and all the resulting noise. One of the problems is, I think, that mathematicians tend to hide behind this "canonically isomorphic" phrase without ever really saying what they mean by it, and another problem, I think, is that apparently dealing with this issue in full generality is very hard in dependent type theory for some reason. I mentioned this to several people last week and they all replied "switch to HOTT!" which is an extremely unhelpful response in my opinion. I would rather be told more about why DTT struggles here.

Could there be a `has_binary_operation` typeclass, not attached to any notation by default, which could somehow be used as a partial fix for all this? Then I think we're back to isomorphic structures and Lean's inability to easily pass theorems and definitions between them.

