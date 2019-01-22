---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/88775Inverseimageinfinmisafinset.html
---

## [maths](index.html)
### [Inverse image in `fin m` is a `finset`](88775Inverseimageinfinmisafinset.html)

#### [Johan Commelin (May 16 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126647766):
The following code is (obviously) not typechecking. How do I make this work?
```lean
definition finvj {m n : ℕ} (f : fin m → fin n) (j : fin n) : finset (fin m) :=
begin
exact {i // f i = j}
end
```

#### [Kevin Buzzard (May 16 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648041):
Well, I guess `{i // f i = j}` has type `Type`

#### [Kevin Buzzard (May 16 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648075):
and you want something of type `finset (fin m)`

#### [Kevin Buzzard (May 16 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648124):
so I guess you'd better find a way of constructing something of type `finset (fin m)`

#### [Kevin Buzzard (May 16 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648132):
I don't know the first thing about finsets so I guess I start with `#print finset`

#### [Kevin Buzzard (May 16 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648144):
oh and that doesn't look too good

#### [Kevin Buzzard (May 16 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648158):
you seem to have to supply a multiset and a proof that this multiset has no duplicates

#### [Kevin Buzzard (May 16 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648215):
but fortunately finset is in mathlib so there will probably exist a good interface

#### [Kevin Buzzard (May 16 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648230):
which in this case will mean "other constructors"

#### [Kevin Buzzard (May 16 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648235):
so next I guess I'd have a look at `finset.lean`

#### [Kevin Buzzard (May 16 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648257):
or maybe I could look for other constructors by typing `finset.` in VS code and then hitting ctrl-space a while

#### [Kevin Buzzard (May 16 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648415):
oh -- `finset.filter` exists

#### [Chris Hughes (May 16 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648416):
`univ.filter (\la i, f i = j)`

I think you might need the finset  namespace open.

#### [Kevin Buzzard (May 16 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648422):
aah, here's a finset expert

#### [Johan Commelin (May 16 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648430):
Aah, cool.

#### [Kevin Buzzard (May 16 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648432):
but I was seconds ahead of him ;-)

#### [Johan Commelin (May 16 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648437):
Yeah, congrats (-;

#### [Johan Commelin (May 16 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648438):
I'll look at filter!

#### [Kevin Buzzard (May 16 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648456):
I was just showing you how I think about these things of course

#### [Kevin Buzzard (May 16 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648489):
but actually in retrospect I missed a trick

#### [Kevin Buzzard (May 16 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648503):
Instead of saying "I wonder what's there -- let's take a look at everything"

#### [Kevin Buzzard (May 16 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648510):
I should have said "let's assume everything is there -- what do I actually want?"

#### [Kevin Buzzard (May 16 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648523):
and what I want is (1) fin n is a finset and (2) a subset of a finset defined by a predicate being true is a finset

#### [Kevin Buzzard (May 16 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648532):
and I should by now know that (2) is called `filter`

#### [Johan Commelin (May 16 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648537):
And I learned that today (-;

#### [Johan Commelin (May 16 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648541):
I did not yet find out (1)...

#### [Johan Commelin (May 16 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648587):
Chris's answer isn't working flawlessly here

#### [Kevin Buzzard (May 16 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648591):
@**Chris Hughes** How does one prove fin n is a finset?

#### [Johan Commelin (May 16 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648600):
My search continues

#### [Kevin Buzzard (May 16 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648614):
it'll be there somewhere

#### [Kevin Buzzard (May 16 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648618):
hmm

#### [Kevin Buzzard (May 16 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648620):
it's somehow not strictly speaking meaningful

#### [Kevin Buzzard (May 16 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648635):
fin n is not a finset -- fin n and something of type finset are different things

#### [Chris Hughes (May 16 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648637):
fin n is not a finset. It is a fintype, and that should be automatically deduced as an instance

#### [Kevin Buzzard (May 16 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648639):
right

#### [Chris Hughes (May 16 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648646):
sometimes (univ : finset (fin n)) helps

#### [Kevin Buzzard (May 16 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648698):
Johan -- why do you want to use finset?

#### [Chris Hughes (May 16 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648699):
because otherwise it doesn't know the intended type. Also import data.fintype

#### [Kevin Buzzard (May 16 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648736):
"set" doesn't mean what mathematicians think it means

#### [Kevin Buzzard (May 16 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648742):
"set" in Lean means "subset of a set"

#### [Kevin Buzzard (May 16 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648749):
"subset of a given type"

#### [Kevin Buzzard (May 16 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648751):
rather than "arbitrary set of anything"

#### [Kevin Buzzard (May 16 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648797):
This took me a while to get my head around

#### [Kevin Buzzard (May 16 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648813):
"X : set N" doesn't mean "X is a proof that N is a set", it means "X is a subset of N". I sometimes read "set" as "subset_of".

#### [Kevin Buzzard (May 16 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648912):
Because fin n is a type, and you have a predicate on that type, the natural thing to make is either a subtype or a `set (fin m)`

#### [Johan Commelin (May 16 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648916):
Kevin, I want to use finset, because I want to sum a function over it.

#### [Johan Commelin (May 16 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648928):
And finset's have all sorts of stuff for that

#### [Kevin Buzzard (May 16 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648930):
My guess is that any type with a reasonable finiteness property will have sums

#### [Kevin Buzzard (May 16 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648934):
with all sorts of stuff

#### [Kevin Buzzard (May 16 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648945):
but on the other hand maybe finsets have the stuff you need

#### [Johan Commelin (May 16 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648965):
I couldn't find it for fin

#### [Kevin Buzzard (May 16 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126648968):
In which case I think Chris' answer sounds best. Why not do the dirty work with fintype (which presumably also has filter) and then turn it into a finset

#### [Kevin Buzzard (May 16 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126649037):
hmm I don't know what a fintype is either

#### [Kevin Buzzard (May 16 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126649039):
well, I just looked

#### [Kevin Buzzard (May 16 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126649042):
I know nothing about these finite gadgets

#### [Chris Hughes (May 16 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126649043):
It's only finsets that have sums.

#### [Kevin Buzzard (May 16 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126649089):
but there's a coercion from fintype to finset?

#### [Chris Hughes (May 16 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126649103):
There is a function from fintype to finset. It's not a coercion.

#### [Chris Hughes (May 16 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126649106):
It's called univ

#### [Kevin Buzzard (May 16 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126649109):
`example (m : ℕ) : fintype (fin m) := by apply_instance`

#### [Kevin Buzzard (May 16 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126649110):
that's a good start

#### [Kevin Buzzard (May 16 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126649123):
type class inference will tell you that (fin m) is a fintype

#### [Johan Commelin (May 16 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126649138):
Yes, it's working now

#### [Kevin Buzzard (May 16 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126649139):
OK great

#### [Johan Commelin (May 16 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126649143):
So now I can start mangling around with my sums

#### [Johan Commelin (May 16 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126649144):
(-;

#### [Kevin Buzzard (May 16 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126649185):
Now it's Patrick you want to talk to :-)

#### [Johan Commelin (May 16 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126649186):
But first I need to catch a train

#### [Johan Commelin (May 16 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126649187):
Yes, I am using big_ops

#### [Patrick Massot (May 16 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126649343):
Actually I currently focused on non-commutative operations. That's why I can't work with finite sets. I'm summing (or multiplying or composing or whatever) elements of (ordered!) lists

#### [Patrick Massot (May 16 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126649408):
That's why I can't use `algebra.big_operators`

#### [Chris Hughes (May 16 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Inverse image in `fin m` is a `finset`/near/126649647):
@**Johan Commelin** `algebra.big_operators` is probably better than Patrick's big operators in this case.

