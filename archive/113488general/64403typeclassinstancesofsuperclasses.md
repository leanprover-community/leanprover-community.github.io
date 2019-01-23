---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/64403typeclassinstancesofsuperclasses.html
---

## Stream: [general](index.html)
### Topic: [type class instances of superclasses](64403typeclassinstancesofsuperclasses.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 21 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20instances%20of%20superclasses/near/128414454):
Given roughly the following combination of classes and instances:

```lean
class A (a : Type) := ...
class B (a : Type) extends B := ...
def T : Type := ...
instance : B T := ...
```

do you also automatically get:

```lean
instance : A T := ...
```

such that the latter instance is the appropriate component of the former instance?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 21 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20instances%20of%20superclasses/near/128414483):
Depends on what you mean by "automatically get"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 21 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20instances%20of%20superclasses/near/128414546):
typeclass inference should find it, but no additional def is made

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 21 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20instances%20of%20superclasses/near/128414547):
Let's assume I don't have a specific meaning and would welcome a precise definition of the phrase. :wink:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 21 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20instances%20of%20superclasses/near/128414628):
```quote
typeclass inference should find it, but no additional def is made
```
So, if `class A` included a def `aaa : a -> bool` and you used `aaa` on `t : T`, this would use the implementation in `instance : B T`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 21 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20instances%20of%20superclasses/near/128414686):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 21 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20instances%20of%20superclasses/near/128414708):
Interesting. But I would not be able to explicitly reference any definition of type `A T`: this is what you mean by “no additional def is made”?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 21 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20instances%20of%20superclasses/near/128414759):
typeclass inference would insert a term of the type `BtoA BT` rather than making an `AT` def and using that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 21 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20instances%20of%20superclasses/near/128414845):
Okay. Does that `BtoA` have a name that you can `#print`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 21 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20instances%20of%20superclasses/near/128414928):
`B.to_A` I believe

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 21 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20instances%20of%20superclasses/near/128415195):
I just noticed that `lattice` is defined in the `namespace lattice`, resulting in `lattice.lattice` as the qualified name.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 21 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20instances%20of%20superclasses/near/128415218):
```lean
#print instances lattice.lattice
```

```lean
finset.lattice.lattice : Π {α : Type u_1} [_inst_1 : decidable_eq α], lattice.lattice (finset α)
multiset.lattice.lattice : Π {α : Type u_1} [_inst_1 : decidable_eq α], lattice.lattice (multiset α)
with_zero.lattice.lattice : Π {α : Type u} [_inst_1 : lattice.lattice α], lattice.lattice (with_zero α)
with_top.lattice : Π {α : Type u} [_inst_1 : lattice.lattice α], lattice.lattice (with_top α)
with_bot.lattice : Π {α : Type u} [_inst_1 : lattice.lattice α], lattice.lattice (with_bot α)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 21 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20instances%20of%20superclasses/near/128415225):
Lots of `lattice.lattice`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 21 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20instances%20of%20superclasses/near/128415328):
Ah, here are the conversions for `lattice` to `semilattice_inf` and `semilattice_sup`:

```lean
#print prefix lattice.lattice
```

```lean
...
lattice.lattice.to_semilattice_inf : Π (α : Type u) [s : lattice.lattice α], lattice.semilattice_inf α
lattice.lattice.to_semilattice_sup : Π (α : Type u) [s : lattice.lattice α], lattice.semilattice_sup α
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 21 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20instances%20of%20superclasses/near/128415413):
Thanks, Mario!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 21 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20instances%20of%20superclasses/near/128415592):
I suppose the goal of this feature is to reduce the number of instances one writes. However, it does make it more difficult to determine if `T` is an instance of `A`.

```lean
#print instances lattice.semilattice_inf
```

```lean
lattice.semilattice_inf_bot.to_semilattice_inf : Π (α : Type u) [s : lattice.semilattice_inf_bot α], lattice.semilattice_inf α
lattice.semilattice_inf_top.to_semilattice_inf : Π (α : Type u) [s : lattice.semilattice_inf_top α], lattice.semilattice_inf α
lattice.lattice.to_semilattice_inf : Π (α : Type u) [s : lattice.lattice α], lattice.semilattice_inf α
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 21 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20instances%20of%20superclasses/near/128416353):
one trick for testing instance problems and getting the result is `#check (by apply_instance : T A)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 21 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20instances%20of%20superclasses/near/128416816):
That works only if `A` is exactly the type of the instance. For example: `#check (by apply_instance : lattice.semilattice_inf (finset ℕ))` but not `#check (by apply_instance : lattice.semilattice_inf (finset α))`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 21 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20instances%20of%20superclasses/near/128416961):
Also, that's a tool for diagnosing an issue. It doesn't help discovering all the instances, which I have found to be useful in Haskell (and would find useful in Lean).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 21 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20instances%20of%20superclasses/near/128430586):
Do you know about `#print instances`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 22 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20instances%20of%20superclasses/near/128458664):
@**Simon Hudon** Did you see my uses of it above? :wink:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 22 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20instances%20of%20superclasses/near/128476919):
oops! Sorry!

