---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/77049typeclass.html
---

## Stream: [general](index.html)
### Topic: [typeclass](77049typeclass.html)

---


{% raw %}
#### [ Kenny Lau (Mar 15 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123761005):
why does this have no problem:
```
class add_comm_monoid (α : Type u) extends add_monoid α, add_comm_semigroup α

class add_group (α : Type u) extends add_monoid α, has_neg α :=
(add_left_neg : ∀ a : α, -a + a = 0)

class add_comm_group (α : Type u) extends add_group α, add_comm_monoid α
```
but this gives me an error?
```
class has_upair extends has_zmem α :=
(upair : α → α → α)
(zmem_upair_iff_eq_or_eq : ∀ x y z, z ∈ upair x y ↔ z = x ∨ z = y)

class has_sUnion extends has_zmem α :=
(sUnion : α → α)
(zmem_sUnion_iff_zmem_zmem : ∀ x z, z ∈ sUnion x ↔ ∃ t, z ∈ t ∧ t ∈ x)

class has_sUnion_upair extends has_sUnion α, has_upair α
```

#### [ Kenny Lau (Mar 15 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123761012):
error:
```
invalid 'structure' header, field 'to_has_zmem' from 'zfc.has_upair' has already been declared
```

#### [ Simon Hudon (Mar 15 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123761063):
Why isn't `α` a parameter of `has_upair` and `has_sUnion`?

#### [ Kenny Lau (Mar 15 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123761069):
oh it's a variable I declared before

#### [ Kenny Lau (Mar 15 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123761073):
(sorry for not providing MWE)

#### [ Simon Hudon (Mar 15 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123761280):
Ah! I see! This is what is called diamond-shaped inheritance scheme. It causes you to inherit `to_has_zmem` multiple times which causes it to clash with itself.

#### [ Simon Hudon (Mar 15 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123761299):
(C++ programmers also know that as "diamond of death")

#### [ Simon Hudon (Mar 15 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123761350):
They have been carefully exorcised from the basic libraries

#### [ Simon Hudon (Mar 15 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123761435):
Is there a way to not make `has_upair` inherit `has_zmem`?

#### [ Simon Hudon (Mar 15 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123761461):
You could change:

```
class has_upair extends has_zmem α :=
```

into

```
class has_upair [has_zmem α] :=
```

#### [ Kenny Lau (Mar 15 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123761472):
then why does the first one work?

#### [ Simon Hudon (Mar 15 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123761601):
Good question. I wonder if that's because `add_comm_monoid` doesn't have fields. You can basically inline it in the `extends` clause of `add_comm_group`

#### [ Simon Hudon (Mar 15 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123761784):
If that's the case, you maybe could take advantage of it by splitting `has_upair` in two:

```
class has_upair_1 [has_zmem α] :=
(upair : α → α → α)
(zmem_upair_iff_eq_or_eq : ∀ x y z, z ∈ upair x y ↔ z = x ∨ z = y)

class has_upair_2 extends has_zmem α,  has_upair  α
```

I'm not sure if that would work but it might be worth a try

#### [ Kenny Lau (Mar 15 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123761803):
```
class has_sUnion_upair extends has_zmem α :=
(upair : α → α → α)
(zmem_upair_iff_eq_or_eq : ∀ x y z, z ∈ upair x y ↔ z = x ∨ z = y)
(sUnion : α → α)
(zmem_sUnion_iff_zmem_zmem : ∀ x z, z ∈ sUnion x ↔ ∃ t, z ∈ t ∧ t ∈ x)

instance has_sUnion_upair.to_has_sUnion [s : has_sUnion_upair α] : has_sUnion α :=
{ ..s }

instance has_sUnion_upair.to_has_upair [s : has_sUnion_upair α] : has_upair α :=
{ ..s }
```

#### [ Kenny Lau (Mar 15 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123761807):
this is what i did

#### [ Simon Hudon (Mar 15 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123761870):
The part I don't like about your solution is that I believe it forces you to duplicate the statement of your laws.

#### [ Kenny Lau (Mar 15 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123761979):
the part I don't like about your solution is that I would have to have `has_zmem` as my hypothesis each time

#### [ Simon Hudon (Mar 15 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123762005):
No. If you use `has_upair_2`, it comes with `has_zmem`

#### [ Kenny Lau (Mar 15 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123762095):
oh...

#### [ Kenny Lau (Mar 15 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123762102):
so your solution is basically like "distrib"

#### [ Kenny Lau (Mar 15 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123762106):
create a useless class that only has distributivity

#### [ Simon Hudon (Mar 15 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123762194):
You could say that

#### [ Simon Hudon (Mar 15 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123762295):
Actually, useless is not accurate: try commenting it out to see if it's useful

#### [ Kenny Lau (Mar 15 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123762354):
I mean `distrib` is useless in the sense that no mathematician cares about it

#### [ Simon Hudon (Mar 15 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123762436):
I think it's still useful. It might not be an interesting structure but for some theorems, you may only care about distributivity without a whole semiring

#### [ Simon Hudon (Mar 15 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123762495):
The same theorem or tactics could then be applicable whether you have a semiring or a distributive lattice

#### [ Simon Hudon (Mar 15 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123762702):
In the case of my solution, the `has_upair_1` is more of a coding trick, you're right. I think it happens rarely enough that it's an ugliness we can live with. I would prefer if diamond shaped inheritance was supported properly but it has been ruled out for performance reason

#### [ Mario Carneiro (Mar 15 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123768060):
@**Kenny Lau** The original code works because it is using the old structure command to merge the fields together. People seem to be scared of anything marked "old" though, so if you want to recover this behavior with the new structure command, rather than creating a useless typeclass, you should extend `has_upair` and restate the axioms of `has_sUnion`, then construct a parent instance for `has_sUnion` (or vice versa).

#### [ Kenny Lau (Mar 15 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123769395):
so if I use old structure, everything will work?

#### [ Mario Carneiro (Mar 15 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123769435):
for some value of "everything"

#### [ Kevin Buzzard (Mar 15 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123770735):
I guess whether or not it will work in Lean 4 is another matter...

#### [ Kevin Buzzard (Mar 15 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123770925):
I guess the other thing is that presumably there was a reason the structure command was changed. Hmm, they might only be performance-related though.

#### [ Simon Hudon (Mar 15 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123771129):
I think they are. Leo considered the price to be too high despite C++ and Eiffel offering the feature with reasonable performances

#### [ Andrew Ashworth (Mar 15 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123771153):
eh, most large software projects have moved away from large inheritance trees

#### [ Simon Hudon (Mar 15 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123771236):
Have they? For performance reasons? I seem to remember it being a bottomless well of bugs in C++ because the design is kind of dumb. As far as I know, the feature is still in use in Eiffel code bases

#### [ Andrew Ashworth (Mar 15 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123771293):
not for performance, but because most people do inheritance wrong. this is the feeling i get from the places i've worked at with large code-bases

#### [ Andrew Ashworth (Mar 15 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123771351):
if you asked most people what the liskov substitution principle was they'd cross their eyes and wonder what you'd had for breakfast

#### [ Andrew Ashworth (Mar 15 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123771426):
well, that's a bit unfair, LSP is a bit jargon-ny, but the point is, it's easy to shoot yourself in the foot with misuse of inheritance

#### [ Simon Hudon (Mar 16 2018 at 00:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/typeclass/near/123772124):
I think that's one reason Eiffel got inheritance right. Have you ever used it?


{% endraw %}
