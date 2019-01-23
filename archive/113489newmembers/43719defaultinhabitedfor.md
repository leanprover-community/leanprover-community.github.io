---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/43719defaultinhabitedfor.html
---

## Stream: [new members](index.html)
### Topic: [default / inhabited for ℚ, ℝ, ℂ](43719defaultinhabitedfor.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Aug 13 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/default%20/%20inhabited%20for%20%E2%84%9A%2C%20%E2%84%9D%2C%20%E2%84%82/near/132070075):
I'm going through [TPIL's chapter on typeclasses](https://leanprover.github.io/theorem_proving_in_lean/type_classes.html#type-classes-and-instances) and while messing around tried the following:
```lean
import data.complex.basic
#reduce default ℚ -- no type class instance of inhabited ℚ
#reduce default ℝ -- timeout
#reduce default ℂ -- timeout
```
`#check` succeeds on the last two.

Questions: Is the lack of something like 
```lean
instance : inhabited ℚ := ⟨0⟩
``` 
in data.rat just an oversight or was this intentional? Why do the other two lines time out?

Meta-question: am I right that this doesn't really matter; i.e. `default` is unlikely to be used in an "actual" proof?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 13 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/default%20/%20inhabited%20for%20%E2%84%9A%2C%20%E2%84%9D%2C%20%E2%84%82/near/132070230):
I suspect that `#reduce` fails on the last two because the reals and complexes are in general a pain to compute with -- they don't have decidable equality and they might well not even have an algorithm for printing out a real number. What would you expect  sqrt(2) to look like in Lean? Is it supposed to print out all the digits? :-)

I would imagine that Q not being inhabited, if true, is an oversight.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Aug 13 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/default%20/%20inhabited%20for%20%E2%84%9A%2C%20%E2%84%9D%2C%20%E2%84%82/near/132070343):
They time out because a real number is built from a Cauchy sequence, and making a Cauchy sequence requires a proof that the sequence is Cauchy. When you #reduce a real, it will try to unfold this proof to axioms, and this will be huge.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Aug 13 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/default%20/%20inhabited%20for%20%E2%84%9A%2C%20%E2%84%9D%2C%20%E2%84%82/near/132070420):
Thanks, that makes sense! Out of curiosity, what would be the right way to get Lean to spit out the default elements for ℝ and ℂ then?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Aug 13 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/default%20/%20inhabited%20for%20%E2%84%9A%2C%20%E2%84%9D%2C%20%E2%84%82/near/132070513):
The best way to check what they are is to look at the definition of the inhabited instance. Reals don't have decidable equality, so given a real, lean cannot tell if it equals zero or not.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 13 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/default%20/%20inhabited%20for%20%E2%84%9A%2C%20%E2%84%9D%2C%20%E2%84%82/near/132070886):
```lean
import data.real.basic 

definition d : inhabited ℝ := by apply_instance

#print d

/-

def d : inhabited ℝ :=
real.inhabited

-/

#check real.inhabited -- inhabited ℝ

-- Now right-click on real.inhabited and select "peek definition"
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 13 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/default%20/%20inhabited%20for%20%E2%84%9A%2C%20%E2%84%9D%2C%20%E2%84%82/near/132071991):
I only mention this because I know of no other way of figuring out the real number which was used other than by looking at the source. I don't know how to look at the definition of d directly, as it were.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Aug 13 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/default%20/%20inhabited%20for%20%E2%84%9A%2C%20%E2%84%9D%2C%20%E2%84%82/near/132072791):
Ah, OK, so in general, `instance : typeclass something` can be accessed with `something.typeclass`. I must have read this somewhere...

Knowing that I can just `#print real.inhabited` and read off `{default := 0}.`

As an aside, it seems that `rat` is missing a bunch of other stuff too, like `rat.ring`, `rat.add_group`, `rat.field`, etc. although they're all an easy `by apply_instance` away.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 13 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/default%20/%20inhabited%20for%20%E2%84%9A%2C%20%E2%84%9D%2C%20%E2%84%82/near/132072805):
waitwaitwait. If `by apply_instance` works, it's there.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 13 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/default%20/%20inhabited%20for%20%E2%84%9A%2C%20%E2%84%9D%2C%20%E2%84%82/near/132072874):
A lot of these instances might be being inferred automatically. For example, Lean knows that any `field` is automatically a `comm_ring`, a `ring`, an `add_monoid` etc etc.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Aug 13 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/default%20/%20inhabited%20for%20%E2%84%9A%2C%20%E2%84%9D%2C%20%E2%84%82/near/132072906):
```quote
waitwaitwait. If `by apply_instance` works, it's there.
```
Maybe I used the wrong words, but I was referring to the following behavior:
```lean
#check rat.comm_ring -- unknown identifier
instance : comm_ring rat := by apply_instance
#check rat.comm_ring -- Lean is happy
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Aug 13 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/default%20/%20inhabited%20for%20%E2%84%9A%2C%20%E2%84%9D%2C%20%E2%84%82/near/132072965):
Another way of discovering the name is
 ```lean
def foo : inhabited real := by apply_instance
#print foo
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 13 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/default%20/%20inhabited%20for%20%E2%84%9A%2C%20%E2%84%9D%2C%20%E2%84%82/near/132072972):
Bryan, this is not a bug, this is what the type class system is about

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Aug 13 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/default%20/%20inhabited%20for%20%E2%84%9A%2C%20%E2%84%9D%2C%20%E2%84%82/near/132072982):
You get cascading for free

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Aug 13 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/default%20/%20inhabited%20for%20%E2%84%9A%2C%20%E2%84%9D%2C%20%E2%84%82/near/132073073):
```quote
Bryan, this is not a bug, this is what the type class system is about
```
Right, I didn't intend to imply that there were any bugs other than in my understanding.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 13 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/default%20/%20inhabited%20for%20%E2%84%9A%2C%20%E2%84%9D%2C%20%E2%84%82/near/132073292):
https://github.com/leanprover/mathlib/pull/254

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 13 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/default%20/%20inhabited%20for%20%E2%84%9A%2C%20%E2%84%9D%2C%20%E2%84%82/near/132073578):
```lean
import data.rat

definition x : comm_ring ℚ := by apply_instance

#print x

/-

def x : comm_ring ℚ :=
field.to_comm_ring ℚ

-/
```

Lean knows that the rationals are a commutative ring, but the instance is not called `rat.comm_ring`, it's called something else. 

If `X` is an inductive type and there's something called `X.foo`, and if `a` has type `X`, then you can sometimes talk about `a.foo` on a good day. But that's not what's happening here. It's not `rat` that has type `comm_ring`, it's some other thing which has type `comm_ring rat`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Aug 13 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/default%20/%20inhabited%20for%20%E2%84%9A%2C%20%E2%84%9D%2C%20%E2%84%82/near/132073675):
```quote
Lean knows that the rationals are a commutative ring, but the instance is not called `rat.comm_ring`, it's called something else. 
```
I don't think it has a name, it's just inferred from `rat.discrete_linear_ordered_field` or something.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 13 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/default%20/%20inhabited%20for%20%E2%84%9A%2C%20%E2%84%9D%2C%20%E2%84%82/near/132073758):
I guess the term is `field.to_comm_ring ℚ` and there's no name for this term. On the other hand when `instance : foo bar  := blah ` is run, Lean has a go at naming the instance itself using some vaguely sane algorithm.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Aug 13 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/default%20/%20inhabited%20for%20%E2%84%9A%2C%20%E2%84%9D%2C%20%E2%84%82/near/132074255):
It looks like `field.to_comm_ring` itself is created automatically from `extends comm_ring` in the `class field` declaration.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 14 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/default%20/%20inhabited%20for%20%E2%84%9A%2C%20%E2%84%9D%2C%20%E2%84%82/near/132074504):
Yeah, that's a cool part of type class inference. The projectors get constructed automatically.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Aug 14 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/default%20/%20inhabited%20for%20%E2%84%9A%2C%20%E2%84%9D%2C%20%E2%84%82/near/132074849):
```lean
import data.rat

definition d : comm_monoid ℚ := by apply_instance

set_option pp.all true
#print d

/-

def d : comm_monoid.{0} rat :=
@linear_ordered_comm_ring.to_comm_monoid.{0} rat
  (@decidable_linear_ordered_comm_ring.to_linear_ordered_comm_ring.{0} rat
     (@discrete_linear_ordered_field.to_decidable_linear_ordered_comm_ring.{0} rat rat.discrete_linear_ordered_field))

-/
```

Type class inference is quite clever.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Aug 14 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/default%20/%20inhabited%20for%20%E2%84%9A%2C%20%E2%84%9D%2C%20%E2%84%82/near/132075092):
It looks much more persistent than clever when I put on `set_option trace.class_instances true` :wink:


{% endraw %}
