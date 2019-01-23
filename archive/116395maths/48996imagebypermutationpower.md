---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/48996imagebypermutationpower.html
---

## Stream: [maths](index.html)
### Topic: [image by permutation power](48996imagebypermutationpower.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 17 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125188730):
```lean
variables (α : Type) (g : perm α) (i : ℕ) (U : set α)
#check g '' U         -- set α
#check g^i             -- perm α
#check g^i '' U     -- maximum class-instance resolution depth has been reached
```
I tried adding various type annotations and parentheses, getting a variety of error messages but no luck

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 17 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125188792):
Trying `(g^i) '' U` is probably a better start

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 17 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125188794):
But then g is coerced to function too early

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 17 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125188808):
Is this related to the recent changes to powers?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125188854):
did you try `((g^i:perm α):set α) '' U`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125188856):
but g^i isn't a set

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 17 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125188901):
He means `(g^i : perm α) '' U : set α`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 17 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125188902):
That works indeed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125188905):
huh. You're right, that's nonsense, but lean is okay with it for some reason

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 17 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125188915):
Of course I tried `(g^i : perm α) '' U`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 17 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125188960):
But didn't think of giving `: set α` at the end

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125188966):
This is weird. Apparently the second type ascription isn't checked at all, the only important thing is that it's a function type so `coe_fn` is inserted

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125188968):
```
#check ((g^i:perm α):_ → unit) '' U --ok
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 17 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125188969):
At least I can continue. But I'd be interested in a shorter way

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 17 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125188972):
wow

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 17 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125188973):
strange

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 17 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189026):
`#check (↑(g^i : perm α)) '' U ` also works

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 17 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189033):
`#check ↑(g^i) '' U` also!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189037):
`#check ⇑(g^i) '' U`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 17 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189102):
Do you understand what happens?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 17 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189157):
Actually I think it's not so far from stuff we already saw (but without me understanding enough to handle new instances of the problem)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189199):
The explicit coercion gives no information to the expected type on the inside, so `g^i : _` is inferred to `g^i : perm A` (usually it goes the other way around), so `⇑(g^i)` gets the coe_fn instance for `perm A` which is `A -> A`, and it's simple from then on

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 17 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189254):
And what happens when it does not work?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 17 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189263):
I mean when we don't help Lean at all

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189364):
Without a literal arrow, it first assumes the types match up. So `(g^i) '' U : _` infers `set ?B` where `g^i : A -> ?B` (using `U : set A`). By the type of `^` we get `g : A -> ?B` and `i : ?C` which solves to `i : nat` and a coercion is inserted for `g` so `⇑g : A -> A`. Finally, it tries to find `has_pow (A -> A) nat` and no such instance exists.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 17 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189513):
Thanks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 17 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189574):
Would it make any sense to try to define a coercion from `perm X` to `set X -> set X` and hope Lean would use that if I write `g U` or `g^i U`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189585):
The original instance resolution overflow is due to `g^i '' U` which by precedence quirks means `g ^ (i '' U)`; it gets caught in a loop looking for `has_coe_to_fun nat` for some reason

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 17 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189597):
Yes, I understood that bit

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189642):
No, `coe_fn` only takes one argument, the domain, unlike `coe` which has domain and target

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 17 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189652):
Not sure why `''` has higher precedence than `^` though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189653):
so you can only coerce to one kind of function for a given object

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 17 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189661):
What about using the general `has_coe`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189671):
it's way too underdetermined, I think

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 17 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189676):
That's what I feared

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189678):
Any function can be treated as a set function by applying `image`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189681):
it's basically just a functor

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189684):
and there are loads of those

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 17 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189686):
I heard functor

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 17 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189728):
Even without the perm layer, this `f '' U` notation is definitely the part of my file that looks further away from usual mathematical notation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189741):
I know at least one math book which uses double open quotes as an infix operator for image

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 17 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189744):
really?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189754):
Takeuti-Zaring Axiomatic Set Theory :P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 17 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189760):
I guess it makes sense to have some kind of specific notation for beginners

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 17 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189762):
I see

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 17 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189764):
that kind of books

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189766):
I think it's more about unambiguous notation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189767):
it's not a beginners book

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 17 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189808):
It seems to be a set theory book

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 17 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189814):
of course if you pretend to be serious when you say everything is a set then you need contortions everywhere

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Apr 17 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125189821):
Or if you pretend to be serious when you say everything you write is well typed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192260):
This is all (both Patrick's coercion issue and the weird '' notation) part of one underlying problem.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192262):
Mathematicians have developed a really good system for overloading notation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192274):
Patrick is exactly right about '' -- I've never seen it used to mean image so it doesn't surprise me that he hasn't, and it also doesn't surprise me that the only place Mario has is some set theory book (as opposed to what Patrick and I would call mathematics)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192283):
In maths the notation for the image of U under f : X -> Y is of course just f(U)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192284):
but I am well aware that life is not so easy in Lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192329):
What the current fix seems to be is this exotic type class system plus clever coercions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192331):
I must be frank

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192332):
I am not sure that it scales

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192335):
I have seen problems with diamonds

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192337):
I have seen problems with the wrong coercion being chosen

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192343):
so my instinct is to

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192345):
(a) give up type classes to a large extent

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192346):
and (b) to give up on mathematician's overloading

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192353):
With my schemes repo I've not made any attempt to do anything clever like this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192355):
If F is a sheaf then F is not the function on open sets, it's some other thing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192358):
and I have F.whatever_i_called_it for the function

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192399):
It looks a bit messier

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192402):
but I am coming round to the idea that it is not the end of the world to actually begin distinguishing between these things

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192413):
In particular if I were writing the code Patrick is writing I simply would not attempt to identify the permutation, the bijection and the function

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192416):
they would all be different notation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192420):
and I would not moan about ''

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192422):
because f(U) doesn't really make sense

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192424):
The reason for me is a practical one

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192425):
I just want to write code that works

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192465):
so I don't want to get bogged down with all the issues Patrick is running into just to make it look more like mathematics

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 17 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192471):
@**Kevin Buzzard** I think you should be sure that you're distinguishing between coercion issues and type class issues. I'm not sure they're the same.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192477):
You're right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192481):
but in some sense they are both solved by filling in the answers myself

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192482):
and in all cases I know the answers

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192483):
the issue is that they are both issues

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192484):
and I don't want to be dealing with issues

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192485):
and filling in the answers myself resolves them

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192524):
I am very happy with how `{ H : blah}` works

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192531):
because if I have `{U : set X} (OU : is_open U)` then Lean is going to be able to guess what U is

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192540):
but I am becoming more and more suspicious of user-added coercions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192542):
I cannot see a viable way of stopping different users creating loops

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192543):
What if person X and person Y are both interested in widgets and foos

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192545):
but one of them is more widgety

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192556):
and one more fooey

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192594):
so one has some coercion from widgets to foos

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192599):
and the other a coercion from foos to widgets

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192601):
and all of a sudden we have two pieces of incompatible code

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192613):
user-added type class inference I guess I'm talking about here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192619):
but I am also avoiding has_coe_to_fun

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192663):
and this more cautious approach solved a lot of problems for me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 17 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192665):
I agree with what you're saying in a purely practical sense. However, I think it stems in general from Lean using elaboration (esp. but not solely via coercions and type-class instance resolution) to guess what you mean. It gets it right most of the time, but it's those few times that it doesn't that wind up frustrating you.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192677):
I think that what happened was that in these cases where it didn't work I first got completely stuck

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192678):
and then I learnt how to unravel things in some cases

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192679):
and then I got used to the unravelling

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 17 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125192680):
and then I figured unravelling wasn't so bad

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 17 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125193991):
I'm not convinced unraveling everything will scale

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 17 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125194000):
And, up to now, I've always been able to solve those kind of issue (well, Mario has always been able...)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 17 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125194004):
And I'm very happy to see how it looks like now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 17 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20by%20permutation%20power/near/125194058):
Ok, it's summer here and I have a lot of maths to read. I'll be trying the IHES garden as a working place, without bringing a computer. See you. :sunglasses:

