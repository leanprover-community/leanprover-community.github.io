---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/43082538opposites.html
---

## [PR reviews](index.html)
### [#538 opposites](43082538opposites.html)

#### [Kenny Lau (Dec 20 2018 at 03:28)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152229118):
maybe someone can write a tactic!

#### [Kevin Buzzard (Dec 20 2018 at 08:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152238513):
Do we have modules over a non-commutative ring? If so you could do left modules over R = right modules over $$R^{op}$$.

#### [Kevin Buzzard (Dec 20 2018 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152238562):
I agree that what you did should all be automated somehow. This is just the sort of thing that as a lecturer I would skip over -- I would let the students automate it.

#### [Kenny Lau (Dec 20 2018 at 08:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152238632):
do we have right modules?

#### [Kevin Buzzard (Dec 20 2018 at 08:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152238648):
Oh well if we don't that would be great because you can just define them as left modules over the opposite ring :P

#### [Kenny Lau (Dec 20 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152238695):
great!

#### [Mario Carneiro (Dec 20 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152238699):
Note that by kenny's definition `R^op = R` for any ring

#### [Kenny Lau (Dec 20 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152238702):
what?

#### [Mario Carneiro (Dec 20 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152238706):
you commuted the addition, which is commutative in a ring

#### [Kenny Lau (Dec 20 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152238709):
but multiplication?

#### [Mario Carneiro (Dec 20 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152238724):
did you commute both? that's confusing

#### [Kenny Lau (Dec 20 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152238725):
yes, I commuted both

#### [Kenny Lau (Dec 20 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152238727):
since addition doesn't matter anyway

#### [Kenny Lau (Dec 20 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152238730):
@**Kevin Buzzard** what's an argument against commuting both?

#### [Mario Carneiro (Dec 20 2018 at 08:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152238787):
it might still matter for defeq which way you have it

#### [Mario Carneiro (Dec 20 2018 at 08:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152238800):
like I asked on the PR, what do you want to use this for?

#### [Mario Carneiro (Dec 20 2018 at 08:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152238809):
I thought that everything is commutative in Kevin's world

#### [Kenny Lau (Dec 20 2018 at 08:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152238859):
not really

#### [Kenny Lau (Dec 20 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152238870):
as long as he cares about group representation

#### [Kenny Lau (Dec 20 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152238955):
End(A,A) = A^op

#### [Kenny Lau (Dec 20 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152239077):
@**Johan Commelin** what do you think?

#### [Johan Commelin (Dec 20 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152239244):
Ehm, we definitely care about non-commutative rings. It's just that we call them that: *non-commutative rings*, instead of *rings*.

#### [Johan Commelin (Dec 20 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152239251):
Whether commuting the addition is a good idea, I don't know. Mathematically it doesn't matter, and I guess it might make some things a bit easier to prove?

#### [Mario Carneiro (Dec 20 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152239312):
> End(A,A) = A^op

what does that mean exactly? Since A^op ~= A why isn't it just End(A,A) = A?

#### [Johan Commelin (Dec 20 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152239481):
`End(_,_)` looks a bit funny anyway :rolling_on_the_floor_laughing:

#### [Kenny Lau (Dec 20 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152239555):
@**Mario Carneiro** oops I meant End(A), I don't know what's wrong with me

#### [Johan Commelin (Dec 20 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152239560):
Well, maybe you're human? :grinning:

#### [Kenny Lau (Dec 20 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152239562):
I don't think A^op and A are isomorphic in general?

#### [Johan Commelin (Dec 20 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152239569):
Definitely not.

#### [Reid Barton (Dec 20 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152239573):
Not that I can visualize a concrete situation where the choice matters, but it feels wrong to me to reverse the order of addition in the opposite ring

#### [Kenny Lau (Dec 20 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152239576):
G^op and G are in fact isomorphic

#### [Kenny Lau (Dec 20 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152239581):
for a group G

#### [Kenny Lau (Dec 20 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152239583):
I think this still works for division rings

#### [Johan Commelin (Dec 20 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152239585):
Sure, for groups it's fine.

#### [Kenny Lau (Dec 20 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152239590):
so H and H^op are isomorphic

#### [Johan Commelin (Dec 20 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152239633):
That's coincidence.

#### [Johan Commelin (Dec 20 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152239636):
Because H has order 2 in the Brauer group.

#### [Johan Commelin (Dec 20 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152239640):
In general division rings arent isom to their opposite.

#### [Kenny Lau (Dec 20 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152239664):
oh right never mind sorry

#### [Reid Barton (Dec 20 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152239676):
Also, I wonder if these opposites will run into the same kind of issues we had/have in category theory, where it's too easy to get confused between an object of a category and an object of the opposite category

#### [Kenny Lau (Dec 20 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152239679):
that's exactly why I put `irreducible`!

#### [Reid Barton (Dec 20 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152239729):
Oh whoops, my mind was numbed by the endless identical instances and I missed that line

#### [Johan Commelin (Dec 20 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152239745):
@**Mario Carneiro** What do you think of the `irreducible` thing? It seems like a good idea to me? (But then, I might not know all the consequences...)

#### [Kenny Lau (Dec 20 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152239793):
> I don't like the use of irreducible here. What is the application of this file? additive and multiplicative are useful in contexts where you just assert that a theorem has a type involving addition instead of multiplication, and the kernel figures out the defeq; irreducible will block that kind of move. Also you aren't being specific about whether the addition or multiplication is being commuted here.

(by Mario)

#### [Mario Carneiro (Dec 20 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152239934):
For example, suppose I want to prove add_comm from mul_comm. The `multiplicative` trick relies on the fact that `add A x y = add A y x` is definitionally equal to `mul (multiplicative A) x y = mul (multiplicative A) y x`. With irreducible in there I have to insert lots of ops and unops and the kernel can't do it on its own

#### [Mario Carneiro (Dec 20 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152240032):
By the way re: isom to opposite, I was thinking of the map x |-> x, and using antihoms where appropriate

#### [Kenny Lau (Dec 20 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152240043):
and I think using that defintional equality is not very safe

#### [Mario Carneiro (Dec 20 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152240049):
it's not, it has to be used in carefully controlled circumstances

#### [Mario Carneiro (Dec 20 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152240100):
its use is more or less restricted to one liner proofs where you reinterpret a multiplicative theorem as additive

#### [Johan Commelin (Dec 20 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152240111):
Right, but here we will want to talk about `op R`, which is a completely different ring.

#### [Johan Commelin (Dec 20 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152240116):
I think it is fitting to make it irreducible.

#### [Kenny Lau (Dec 20 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152240121):
```quote
its use is more or less restricted to one liner proofs where you reinterpret a multiplicative theorem as additive
```
 and it's open to abuse / misuse

#### [Mario Carneiro (Dec 20 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152240126):
if you want it to be a different ring, then you should use a structure

#### [Kenny Lau (Dec 20 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152240192):
really?

#### [Kenny Lau (Dec 20 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152240203):
well isn't the effect the same

#### [Reid Barton (Dec 20 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152240312):
It's not exactly the same, as `op (unop x)` will not be defeq to `x`.
(... `newtype`?)

#### [Kenny Lau (Dec 20 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152240326):
then I think the current definition is better :P

#### [Kenny Lau (Dec 20 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152240382):
and this is consistent with my support of auxiliary types

#### [Kenny Lau (Dec 20 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152240387):
I think `additive` and `multiplicative` should be irreducible as well

#### [Johan Commelin (Dec 20 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152240399):
```quote
I think `additive` and `multiplicative` should be irreducible as well
```
 I still hope that one day we will have a system where they don't exist.

#### [Mario Carneiro (Dec 20 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152240461):
If you are giving a newtype API for opposite, then I would rather have no defeqs at all

#### [Mario Carneiro (Dec 20 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152240464):
`op (unop x) = x` is a theorem

#### [Mario Carneiro (Dec 20 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152240470):
as well as `unop (op x) = x`

#### [Kenny Lau (Dec 20 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152240482):
what is newtype?

#### [Mario Carneiro (Dec 20 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152240492):
it's a structure with one field

#### [Kenny Lau (Dec 20 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152240493):
```quote
If you are giving a newtype API for opposite, then I would rather have no defeqs at all
```
 don't we like defeqs?

#### [Mario Carneiro (Dec 20 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152240500):
recall the real irreducible discussion

#### [Mario Carneiro (Dec 20 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152240534):
defeq breaks abstractions

#### [Reid Barton (Dec 20 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152240544):
I was hoping for "newtype" to be defeq in both directions but still a new type

#### [Kenny Lau (Dec 20 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152240550):
it's a new type to the kernel

#### [Mario Carneiro (Dec 20 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152240551):
if lean had structure eta that would be possible

#### [Reid Barton (Dec 20 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152240561):
on the basis that Haskell semantic equality (considering bottom) ~ Lean definitional equality

#### [Kenny Lau (Dec 20 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152240565):
```quote
defeq breaks abstractions
```
 I don't understand

#### [Kenny Lau (Dec 20 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152240568):
and also why is `unop (op x) = x` being defeq ok

#### [Reid Barton (Dec 20 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152240594):
(BTW, *lots* of category theory stuff would be less awful with eta for structures)

#### [Mario Carneiro (Dec 20 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152241162):
it's called a newtype because it's underlying representation is the same

#### [Mario Carneiro (Dec 20 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152241163):
it's a "zero cost abstraction"

#### [Mario Carneiro (Dec 20 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152241305):
> on the basis that Haskell semantic equality (considering bottom) ~ Lean definitional equality

I don't think this is a good comparison; why isn't that ~ lean propositional equality?

#### [Reid Barton (Dec 20 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152241327):
I don't understand why, but it seems to be a useful heuristic in practice.

#### [Reid Barton (Dec 20 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152241333):
For example `fst (a, b) = a` is okay, but `(fst p, snd p) = p` is not.

#### [Reid Barton (Dec 20 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152241465):
The stuff about "lazy patterns" should fit in somehow, too. But I don't know how to make real sense out of any of this. For one thing, Haskell has a (partial) definedness ordering between things like `(fst p, snd p)` and `p`, but in Lean, the thing that would be more defined in Haskell is instead somehow "better", but I don't know why.

#### [Reid Barton (Dec 20 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152241485):
It's not like `\lam \<a, b\>, \<a, b\>` is "less defined" than `\lam p, p`

#### [Mario Carneiro (Dec 20 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152241532):
hm, you may be on to something here

#### [Reid Barton (Dec 20 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152241566):
I hope you can figure out what it is, because I find it puzzling!

#### [Mario Carneiro (Dec 20 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152241577):
It reminds me of the problem of understanding metamath semantics

#### [Mario Carneiro (Dec 20 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152241588):
Maybe another way to think of it is that every type is populated, in additional to the usual things, with "raw variables"

#### [Mario Carneiro (Dec 20 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152241593):
which are just terms that don't denote anything, like atoms

#### [Mario Carneiro (Dec 20 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152241633):
and those two lambdas behave differently on raw variables

#### [Reid Barton (Dec 20 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152241638):
Yes, this sounds promising

#### [Reid Barton (Dec 20 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152241655):
that gives an ordering too perhaps, by specializing variables to values (which might contain new variables inside)

#### [Mario Carneiro (Dec 20 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152241661):
exactly

#### [Mario Carneiro (Dec 20 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152241663):
that's how metamath semantics works

#### [Mario Carneiro (Dec 20 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/152241667):
it's all about the metavariables

#### [Kenny Lau (Jan 07 2019 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/154559706):
so what should we do? @**Johan Commelin** @**Mario Carneiro**

#### [Kenny Lau (Jan 08 2019 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/154631186):
I guess I have made opposite inductive

#### [Kenny Lau (Jan 12 2019 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/154975129):
Should we make `order_dual` in `order/basic.lean` also a structure / inductive?

#### [Kenny Lau (Jan 12 2019 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR reviews/topic/#538 opposites/near/154975174):
or maybe we should merge these two

