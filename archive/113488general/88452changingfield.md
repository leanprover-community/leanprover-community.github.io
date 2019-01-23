---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/88452changingfield.html
---

## Stream: [general](index.html)
### Topic: [changing `field`](88452changingfield.html)

---

#### [Mario Carneiro (Sep 03 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133230210):
Before we get too involved in field theory, I would like to propose a change to `division_ring` and `field`. The problem is that these are defined in core, meaning that we would have to more or less completely ignore all the core definitions based on fields (which isn't much) and add primes or something to avoid name collision.

The change is simply to add `div_zero` and decidable equality as an axiom to both of them. This will make `field` the same as `discrete_field`, so we could just use that, but I think it is not worth the effort to explain to people that they should always use `discrete_field` instead of `field`, and there are already several examples of people thinking that `field` is the more useful one.

#### [Kevin Buzzard (Sep 03 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133231143):
Mathematicians are not taught "discrete" fields so would probably gravitate to fields naturally given the choice. Isn't there something mentioned about this in one of the doc strings?

#### [François G. Dorais (Sep 05 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133381566):
Would that imply hiding the current field definition? The distinction is useful for actual computation with real numbers, so there should be a way to go back to the not necessarily discrete case when necessary.

#### [Johannes Hölzl (Sep 05 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133383028):
I don't think we should actually compute with the reals. If you want to compute with transcendental functions etc,  one needs to implement interval arithmetic or similar. This would be some kind of decision procedure.

#### [François G. Dorais (Sep 05 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133384484):
I'm puzzled by "we" but just to clarify: hiding the current field and having only discrete fields means that I can't use mathlib at all for many of the things I want to do. Currently, I can still use parts of mathlib that don't rely on decidable equality.

#### [Reid Barton (Sep 05 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133384705):
What's something you want to do with `field` that you can't do with `discrete_field`?
I don't understand how you can get anything out of a real number (other than another real number).

#### [Reid Barton (Sep 05 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133384899):
At least, not with the real numbers as implemented in mathlib.

#### [Chris Hughes (Sep 05 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133386146):
I think he might be worried because reals aren't really a discrete field. But that doesn't matter because you just cheat and use `classical.dec_eq` to make the instance.

#### [Reid Barton (Sep 05 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133386420):
I expect François has some specific things in mind, but maybe I misunderstood the meaning of "computation" or "do". I guess proving theorems in constructive real analysis is in some sense a computation, but I don't understand how you can actually run such a computation in Lean and get any useful data out.

#### [Reid Barton (Sep 05 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133386546):
Anyways I don't think you can shadow the existing `field`, except maybe with notation, which sounds super confusing.

#### [Reid Barton (Sep 05 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133386607):
So is the suggestion basically to rename/copy `discrete_field` to `field'`?

#### [Johannes Hölzl (Sep 05 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133386664):
With *we* I meant users of mathlib's reals.

#### [Johannes Hölzl (Sep 05 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133386836):
Proofs in mathlib shouldn't expect that any equalities on the reals hold by **definitional equality**, i.e. something like `(1 + 1 : real) = 2` is only by accident provable using `rfl`. To prove such a statement one would use `norm_num` or similar.

#### [Johannes Hölzl (Sep 05 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133387017):
I also think that we currently are forced to use `discrete_field`. I think we need to wait until Lean 4 comes out to make such a change.

#### [Mario Carneiro (Sep 05 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133392499):
To be clear, I am on board with not assuming decidable equality when it is not necessary, but there are essentially no examples of instances of `division_ring` and `field` that don't have decidable equality. The reason is that `has_inv` is a *total function*, which already excludes all the interesting intuitionistic examples of fields like the computable reals

#### [Mario Carneiro (Sep 05 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133392527):
Basically, `field` is a worst-of-both-worlds halfway house between decidable fields and nondecidable fields

#### [Kenny Lau (Sep 05 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133392910):
did the constructivist type theorists never think of this problem?

#### [Mario Carneiro (Sep 05 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133394241):
The constructivists didn't write `field`, leo did. A constructivist would be opposed to totalizing `inv`

#### [Chris Hughes (Sep 05 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133394523):
What's the point in intuitionist reals? Is there a decidable predicate on reals other than true and false?

#### [Kenny Lau (Sep 05 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133394807):
no, because every function is continuous, and {true, false} is discrete

#### [Kenny Lau (Sep 05 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133394863):
but there are a lot of decidable predicates on the computable reals / algebraic reals

#### [Mario Carneiro (Sep 05 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133395209):
Careful there; there are decidable predicates on real algebraic numbers but not on computable real numbers (by Rice's theorem)

#### [Kenny Lau (Sep 05 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133395279):
is "I am an algebraic number" decidable over the computable real numbers?

#### [Kevin Buzzard (Sep 05 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133395290):
Is pi algebraic?

#### [Kevin Buzzard (Sep 05 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133395296):
That is pretty hard to decide

#### [Kevin Buzzard (Sep 05 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133395302):
but pi is computable

#### [Kenny Lau (Sep 05 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133395312):
oh, if they were, then we would already know if e+pi is algebraic

#### [Kevin Buzzard (Sep 05 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133395315):
well, maybe nobody decided yet

#### [Johan Commelin (Sep 05 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133395328):
I decide that it is not.

#### [Kevin Buzzard (Sep 05 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133395334):
We don't know if every group scheme of order 4 is killed by 4, but there's an algorithm for finding out.

#### [Kevin Buzzard (Sep 05 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133395415):
It turns into the question "is this completely explicit element of a polynomial ring in about 30 variables over the integers in this completely explicit ideal" and I think one can use Groebner basis techniques to figure it out.

#### [Chris Hughes (Sep 05 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133395900):
What's an explicit ideal?

#### [Kevin Buzzard (Sep 05 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133396254):
it's "here are about 100 explicit polynomials in the variables X1,X2,...,X30, and it's the ideal generated by them"

#### [Kevin Buzzard (Sep 05 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133396265):
The last time I asked, the computation was out of reach on a modern machine.

#### [Simon Hudon (Sep 05 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133396352):
```quote
is "I am an algebraic number" decidable over the computable real numbers?
```
Probably not. Rice's theorem which Mario refers to can be paraphrased as "if your predicate over computations is interesting then it's undecidable"

#### [Leonardo de Moura (Sep 05 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133396718):
@**Mario Carneiro** I did not develop `field`. It was developed by @**Rob Lewis**  for Lean 2. I only maintained it and made modifications to make sure it worked with Lean 3. One good news is that the whole algebraic hierarchy has already been deleted from Lean 4.

#### [Leonardo de Moura (Sep 05 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133396870):
@**Johan Commelin** I have no idea whether the "four leaf clover" is a positive or negative reaction :)

#### [Kenny Lau (Sep 05 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133396886):
```quote
/me proposes :four_leaf_clover: as the default emoji for marking dreams and wishes that will be trivially realizable when Lean 4 emerges :stuck_out_tongue_wink:
```
[Johan Commelin, 03/09/2018 08:07:17 (UTC)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/source.20code.20browser/near/133246918)

#### [Johan Commelin (Sep 05 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133396945):
@**Leonardo de Moura** No worries. It's meant to be positive. Kudos for all the work you are doing!

#### [Kevin Buzzard (Sep 05 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133396948):
Moving the algebraic hierarchy out of core lean seems to be something everyone is excited about.

#### [Leonardo de Moura (Sep 05 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133396988):
@**Kenny Lau** Ok, but this one is not in the dream/wish category since it was already deleted several weeks ago. Well, Lean 4 itself may still be a distant dream.

#### [Patrick Massot (Sep 05 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133396999):
Leo, you shouldn't worry about us. We are very happy to use Lean 3, and I'm sure Lean 4 will be even better. Please, do what you think you have to do, at the pace you think is good

#### [Leonardo de Moura (Sep 05 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133397092):
@**Patrick Massot** I see. If this is the "happy mode", I wonder how you are going to react when you are not happy ;)

#### [Kevin Buzzard (Sep 05 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133397166):
We will work with whatever you come up with.

#### [Kevin Buzzard (Sep 05 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133397170):
When it's ready.

#### [Kevin Buzzard (Sep 05 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133397200):
and it will almost certainly be better, so we will almost certainly be happy.

#### [Patrick Massot (Sep 05 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133397204):
I hosted a Lean user meeting in my math department two weeks ago, with Kevin, Johan, Johannes, Mario, Scott, Reid, Chris and Rob. I can tell you everybody seemed very very happy.

#### [Simon Hudon (Sep 05 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133397244):
It doesn't look unhappy to me. Sure there's the occasional whining but I think a lot of it can be attributed to a bunch of mathematician who didn't expect they would need to understand functional programming.

#### [Patrick Massot (Sep 05 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133397452):
About the specific question of the algebraic hierarchy, it will probably be more convenient to have it outside of the core library but, as far as I know, the current state did not block anything in our experimentations. And the number of mathematicians trying to learn Lean seems to increase much faster than for other proof assistants, if I understand correctly what I heard from https://www.dagstuhl.de/en/program/calendar/semhp/?semnr=18341

#### [François G. Dorais (Sep 06 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133409655):
@**Mario Carneiro** You're right about `has_div` (and a few other `has_*` signatures are wrong too) but I thought I would be the only one to care about this and it wouldn't get fixed until Lean 4 anyway...
In any case, my main goal is to avoid spending an awful lot of time proving trivial things about fields. If all the theorems are about discrete fields then I can't use them in much of my work and I have to re-do them on my own, perhaps by copy/paste most of the time but I might lose the clever tactics and have do do everything over again the painful way...
@**Reid Barton** Yes, you're right about the confusion. One of the main reasons why Lean is useful for me is that (avoiding non-computational axioms) everything I can do in lean is computable. It's not about writing a program to "do" things, it's reasoning about computational processes...

#### [Mario Carneiro (Sep 06 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133409737):
> If all the theorems are about discrete fields then I can't use them in much of my work and I have to re-do them on my own, perhaps by copy/paste most of the time but I might lose the clever tactics and have do do everything over again the painful way...

What are you doing that needs non-discrete fields? Note that the name "discrete field" is a misnomer if you are any kind of regular mathematician, it has nothing to do with topology

#### [Mario Carneiro (Sep 06 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133409849):
We've more or less made the decision to not care about constructive math for its own sake in core lean and mathlib. Either your field is actually decidable (i.e. `rat`), in which case there is no problem, or it is not decidable (i.e. `real`) but in this case you are working classically anyway so everything is decidable.

#### [François G. Dorais (Sep 06 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133409952):
@**Mario Carneiro** I agree (and don't really care) about the name. The issue is that decidable equality is a rare luxury in my kind of work. (Admittedly, we're a small crowd, but I care about Lean and how it's useful to me...)

#### [Mario Carneiro (Sep 06 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133409977):
I'm asking what your kind of work is, that makes decidable equality a rarity

#### [Mario Carneiro (Sep 06 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133409988):
I also care about lean being useful to you, but I don't know what you need

#### [François G. Dorais (Sep 06 2018 at 01:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133410606):
I don't need anything specific. I'm happy as things are but the future is where things will be... In Lean 4, as far as I understand, there won't be any algebraic structures (except really basic stuff). So I'll inevitably have to deal with mathlib (or equivalent?) for that kind of basic stuff. If mathlib suddenly decides that all fields have decidable equality then I'll have to stop using it because that's simply not true for my applications. Though my applications are specialized, this is just common sense.

#### [François G. Dorais (Sep 06 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133411365):
To answer your first question, I work in computability theory and reverse mathematics most of the time these days. Both of these areas use classical logic in the meta sense, but the bottom line is that equality of real numbers is not computable...

#### [Mario Carneiro (Sep 06 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133411854):
I think that it is better to encode such facts directly, with a notion of computation, rather than trying to work in a weak logic with the hope that the proven theorems correspond to computable facts at a higher meta level

#### [Mario Carneiro (Sep 06 2018 at 02:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133411933):
I think that there is definitely a place for computable reals in mathlib, but I don't think they are an adequate replacement for the real reals

#### [Mario Carneiro (Sep 06 2018 at 02:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133412066):
There are additional design considerations that go into it (e.g. efficiency, precision requests, etc), and certain operations (like total division) don't make sense, or at least don't have the same signature that lean wants to give them. At the same time I don't want these considerations to affect regular mathematics, where we just want to write `1 / 2` and not worry about the details, so it simply won't be a `field` or `field'` or whatever, it will be some special thing like `computable_field`

#### [Mario Carneiro (Sep 06 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133412245):
To be perfectly honest, I don't think lean is a very good place to do reverse mathematics, unless you do a deep embedding. "no axioms" lean is already way stronger than ZFC

#### [Simon Hudon (Sep 06 2018 at 02:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133412358):
@**Mario Carneiro**  Didn't you write your proof of soundness relative to ZFC?

#### [Simon Hudon (Sep 06 2018 at 02:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133412364):
How does that work if Lean is stronger than ZFC?

#### [Mario Carneiro (Sep 06 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133412392):
ZFC + omega inaccessibles. I haven't fully checked but I believe that "no axioms" lean also has this consistency strength (I proved it relative to lean plus the big 3 axioms)

#### [Simon Hudon (Sep 06 2018 at 02:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/changing%20%60field%60/near/133412620):
the three big ones: choice, quot.ind and prop.ext?

