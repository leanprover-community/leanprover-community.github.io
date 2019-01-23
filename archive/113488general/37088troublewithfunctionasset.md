---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/37088troublewithfunctionasset.html
---

## Stream: [general](index.html)
### Topic: [trouble with function as set](37088troublewithfunctionasset.html)

---

#### [Marcus Klaas (Dec 02 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150700590):
Hi! Is this a proper channel for asking (elementary) questions?

#### [Marcus Klaas (Dec 02 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150700592):
I'm stuck trying to prove the following trivial statement:
```lean
def func_as_set {α β} (f : α → β) : set (α × β) := { x | x.2 = f(x.1) }

example {α β} (a : α) (f : α → β) : (a, f a) ∈ func_as_set f := sorry
```

#### [Marcus Klaas (Dec 02 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150700597):
Refl and Simp tactics don't seem to work, unfortunately

#### [Chris Hughes (Dec 02 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150700700):
Did you try `rfl`?

#### [Marcus Klaas (Dec 02 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150700743):
I don't think so. I will do it now.

#### [Chris Hughes (Dec 02 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150700744):
`refl` works for any reflexive relation, and I guess the elaborator looks for a proof that `∈` is reflexive. `rfl` is only for equality.

#### [Marcus Klaas (Dec 02 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150700750):
omg that worked. Thanks for the elaboration too. Very useful to know!!

#### [Kevin Buzzard (Dec 02 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150701125):
PS
```quote
Hi! Is this a proper channel for asking (elementary) questions?
```
Here is fine, although most of the elementary questions get asked in #**new members** . There are no hard and fast rules though.

#### [Marcus Klaas (Dec 02 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150701289):
Cool, thanks

#### [Marcus Klaas (Dec 02 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150701337):
In that case, I have another trivial follow up ;-) How does one go from a hypothesis in this form
```lean
x ∈{ y | P y }
```
to
```lean
P x
```
?

#### [Kevin Buzzard (Dec 02 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150701352):
Again isn't that `rfl`?

#### [Chris Hughes (Dec 02 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150701400):
`rw set.mem_set_of_eq` also works. That lemma does not have a good name.

#### [Marcus Klaas (Dec 02 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150701402):
but you can't use that when it's a hypothesis, right?

#### [Chris Hughes (Dec 02 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150701405):
`rw _ at h`

#### [Marcus Klaas (Dec 02 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150701406):
right - trying now

#### [Kevin Buzzard (Dec 02 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150701407):
Are you in tactic mode or term mode?

#### [Chris Hughes (Dec 02 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150701409):
if `h` is your hypothesis.

#### [Marcus Klaas (Dec 02 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150701412):
tactic mode

#### [Kenny Lau (Dec 02 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150701420):
you can just change it

#### [Kenny Lau (Dec 02 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150701422):
or pretend that it's already in that form

#### [Kenny Lau (Dec 02 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150701424):
depending on what you're trying to do

#### [Kevin Buzzard (Dec 02 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150701425):
You could do `change P x at h` as well

#### [Marcus Klaas (Dec 02 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150701431):
oooh, that's useful
thanks folks!

#### [Kevin Buzzard (Dec 02 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150701435):
Because the two terms are definitionally equal you might not even need to change it

#### [Marcus Klaas (Dec 02 2018 at 00:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150701602):
@**Kevin Buzzard** my proposition is an equality in this case. i need it for a rewrite. doesnt seem to work without an explicit change

#### [Marcus Klaas (Dec 02 2018 at 00:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150701605):
with the change, it does! :-)

#### [Kevin Buzzard (Dec 02 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150701611):
Post some working code?

#### [Kevin Buzzard (Dec 02 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trouble%20with%20function%20as%20set/near/150701615):
But yes, `rw` needs things to be unravelled explicitly.

