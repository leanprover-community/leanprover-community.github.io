---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/95179exprswithlocalconstant.html
---

## Stream: [general](index.html)
### Topic: [expr's with local constant](95179exprswithlocalconstant.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 02 2019 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154192394):
What's the best way of getting something a bit like this to work?
```lean
meta example {α : Type} [group α] : expr := `(1 : α) 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 02 2019 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154193433):
I guess it would it be better for `α` to be an expression representing a type, instead of a type?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 02 2019 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154193848):
Do you really want an `expr` or would a `tactic expr` be good enough?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Jan 02 2019 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154193945):
That's generally the right move, yes. There are ways to make something like this work with alpha being a type using `reflected` instances. Along the lines of 
```lean
meta def my_def (α : Type) [h : group α] [h2 : reflected h] [h3 : reflected α] : expr := `(@has_one.one.{0} %%h3 %%h2)
```
But that's weird. What application do you have in mind?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 02 2019 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154193947):
`tactic expr` is good enough.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 02 2019 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154194059):
`tactic.to_expr ```((1 : α))` should work then

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Jan 02 2019 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154194062):
For `tactic expr` and taking alpha as an `expr`, it's easy.
```lean
meta def my_def' (α : expr) : tactic expr :=
tactic.to_expr ``(1 : %%α)
```
If the check for a group instance is important, it's easy to add.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 02 2019 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154194098):
It's difficult to be more precise without more context

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 02 2019 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154194913):
The context is, and I think I might be going about this the wrong way, is that I have a function that computes the conjugacy classes of a finite group as a `finset (finset G)`. It's too slow for the kernel, but fast enough for the VM. I want to compute this in the VM, and then verify it does indeed return the conjugacy classes in the kernel. Do I have to go via `expr` for this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 02 2019 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154195434):
how do you intend to verify the result?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 02 2019 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154195453):
Some decidable instance.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 02 2019 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154195475):
Though I'm not at all sure this is a good approach.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 02 2019 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154195541):
no, I mean what's the method you use to check that the result is correct, which is not the same as just calculating the classes?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 02 2019 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154195557):
how does that decidable instance work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 02 2019 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154195567):
is it fast enough?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 02 2019 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154195595):
I haven't written it yet. It probably won't be that much faster than computing it from scratch.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 02 2019 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154195663):
I'm trying to prove A5 is simple by the way, and there's a proof that says look at the cardinalities of the conjugacy classes.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 02 2019 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154195684):
so you only need the cardinalities, not the classes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 02 2019 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154195695):
Yeah.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 02 2019 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154195722):
But I guess it's hard to verify the cardinalities without verifying the elements.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 02 2019 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154195789):
what are you looking for in the cardinalities? Do you really need to calculate all of them or can you use a symmetry argument for the rest?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 02 2019 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154195899):
I like to think of these kinds of problems as if I am a human mathematician who doesn't want to do too much calculation; theorem provers generally prefer those kinds of proofs, as opposed to the blasty proofs that make them sweat

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 02 2019 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154195929):
The cardinalities are `{1, 12, 12, 15, 20}`. I was hoping to do a blasty proof that meant I didn't have to think.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 02 2019 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154195966):
The non blasty proofs pretty much involve looking at cycle shapes, which is quite a lot of work.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 02 2019 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154196031):
isn't there some thing about 3-transpositions generating A5 that helps?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 02 2019 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154196170):
The version of that I've seen involves casing on the cycle type, and proving that whatever the cycle type of a non trivial element, there is a 3-cycle.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 02 2019 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154196301):
You can still split the difference between the blasty stuff and some smarts. For example, you can calculate the order of a subgroup with only a few well chosen elements and non-elements, depending on the group

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 02 2019 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154196439):
So I have to prove [Screenshot-2019-01-02-at-19.44.58.png](/user_uploads/3121/gRIVgvyOkROAJNzRRcZ6Bt96/Screenshot-2019-01-02-at-19.44.58.png)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 02 2019 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154196501):
and what is A5 for you?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 02 2019 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154196525):
```lean
def alternating (α : Type*) [decidable_eq α] [fintype α] : Type* :=
is_group_hom.ker (sign : perm α → units ℤ)
```
with`fin 5` instead of alpha

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 02 2019 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154196889):
I guess you can consider the orders of different elements in sigma

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 02 2019 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154196997):
They can't all be 1. If all are 1 or 2 it is (a b)(c d), if there is one with 3 it is (a b c); and if there is one with 5 it is (a b c d e). You have to argue that 4 is not possible, and (a b c) (d e) is not possible

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 02 2019 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154197163):
I think it is important to have some way to talk about cycles for this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 02 2019 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154197262):
Actually the first step is calculating partitions of 5

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 02 2019 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154197322):
for a given partition you can say if it is even or odd and thus get the list 3+1+1, 2+2+1, 5 for possible cycle decompositions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 02 2019 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154197423):
(I guess a partition is even if the sum of all the elements of the list decreased by 1 is even, so 3+1+1 sums to 2 so is included, while 3+2 sums to 3 and is excluded)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 02 2019 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154198375):
Here's one approach to verify the conjugacy classes. For the proof it suffices to prove that every conjugacy class I produce is a subset of a conjugacy class, it doesn't have to be equal. So it suffices to prove conjugacy of one element of each class with every other element, which I can do much more efficiently by  intelligently finding the element, instead of searching. This is getting rather complicated now though.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 02 2019 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154198562):
In meta land, can I not just turn any object of any type into an `expr` really easily?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 02 2019 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154198577):
what's the `expr` for the real number pi?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 02 2019 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154198871):
```lean
meta def pi_expr : expr := `(real.pi)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 02 2019 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154198944):
but you only have the object now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 02 2019 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154198949):
you don't know how it was created

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 02 2019 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154198961):
Point is there is uncountably many real numbers yet only countably many `expr`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 02 2019 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154198968):
you can't possibly surject `real -> expr`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 02 2019 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154198976):
Yeah, but it's meta, so who cares.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 02 2019 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154198988):
I won't be able to input those undefinable reals into my function.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 02 2019 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154199141):
There are abstract proofs that A_n is simple for all n>=5 but for just A_5 I always tell people to go for the counting proof. Can Lean really not count to 60?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 02 2019 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154199174):
What's the counting proof. The one I mentioned?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 02 2019 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154199257):
Naively computing conjugacy classes is quadratic time I think. Plus there's lots of little inefficiencies in the algorithm that I've written.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 02 2019 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154199328):
Naively computing conjugacy classes might be quadratic time, but 60^2 is still a lot less than a million.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 02 2019 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154199457):
But more than the kernel can handle apparently. You've got to erase duplicates as well, which increases the time quite a bit, so it's worse than quadratic I think.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 02 2019 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154199465):
I know something about abstract algorithms, and I know something about maths, but I have no idea how Lean implements abstract algorithms, or stores data types, so I am bewildered as to why all this is even an issue. I am pretty sure that I can write code which does this in gap and terminates very quickly.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 02 2019 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154199484):
My VM version takes 246ms. But the kernel is unbelievably slow.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 02 2019 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154199492):
From the point of view of abstract algorithms, stuff like erasing dupes can just be done with hash tables or whatever.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 02 2019 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154199502):
Maybe I am imagining what the VM does, not what the kernel does. I still don't really know the difference.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 02 2019 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154199503):
yeah but when you use hash tables in say PARI/GP you don't need to prove that it works

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 02 2019 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154199507):
right.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 02 2019 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154199561):
but here the hash is just the list of where [1,2,3,4,5] go and proving that two lists are equal or not is not hard.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 02 2019 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154199606):
maybe we can store lemmas like 4 != 5 :P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 02 2019 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154199621):
I don't think there's any caching in Lean...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 02 2019 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/expr%27s%20with%20local%20constant/near/154199887):
Imagine how bad it would be if I'd filtered all the functions to prove `fintype_perm` like some people suggested.

