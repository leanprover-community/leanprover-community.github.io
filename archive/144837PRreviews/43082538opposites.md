---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/43082538opposites.html
---

## Stream: [PR reviews](index.html)
### Topic: [#538 opposites](43082538opposites.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 20 2018 at 03:28)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152229118):
maybe someone can write a tactic!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 20 2018 at 08:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152238513):
Do we have modules over a non-commutative ring? If so you could do left modules over R = right modules over $$R^{op}$$.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 20 2018 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152238562):
I agree that what you did should all be automated somehow. This is just the sort of thing that as a lecturer I would skip over -- I would let the students automate it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 20 2018 at 08:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152238632):
do we have right modules?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 20 2018 at 08:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152238648):
Oh well if we don't that would be great because you can just define them as left modules over the opposite ring :P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 20 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152238695):
great!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 20 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152238699):
Note that by kenny's definition `R^op = R` for any ring

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 20 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152238702):
what?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 20 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152238706):
you commuted the addition, which is commutative in a ring

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 20 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152238709):
but multiplication?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 20 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152238724):
did you commute both? that's confusing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 20 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152238725):
yes, I commuted both

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 20 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152238727):
since addition doesn't matter anyway

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 20 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152238730):
@**Kevin Buzzard** what's an argument against commuting both?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 20 2018 at 08:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152238787):
it might still matter for defeq which way you have it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 20 2018 at 08:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152238800):
like I asked on the PR, what do you want to use this for?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 20 2018 at 08:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152238809):
I thought that everything is commutative in Kevin's world

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 20 2018 at 08:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152238859):
not really

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 20 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152238870):
as long as he cares about group representation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 20 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152238955):
End(A,A) = A^op

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 20 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239077):
@**Johan Commelin** what do you think?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 20 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239244):
Ehm, we definitely care about non-commutative rings. It's just that we call them that: *non-commutative rings*, instead of *rings*.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 20 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239251):
Whether commuting the addition is a good idea, I don't know. Mathematically it doesn't matter, and I guess it might make some things a bit easier to prove?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 20 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239312):
> End(A,A) = A^op

what does that mean exactly? Since A^op ~= A why isn't it just End(A,A) = A?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 20 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239481):
`End(_,_)` looks a bit funny anyway :rolling_on_the_floor_laughing:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 20 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239555):
@**Mario Carneiro** oops I meant End(A), I don't know what's wrong with me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 20 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239560):
Well, maybe you're human? :grinning:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 20 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239562):
I don't think A^op and A are isomorphic in general?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 20 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239569):
Definitely not.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 20 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239573):
Not that I can visualize a concrete situation where the choice matters, but it feels wrong to me to reverse the order of addition in the opposite ring

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 20 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239576):
G^op and G are in fact isomorphic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 20 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239581):
for a group G

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 20 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239583):
I think this still works for division rings

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 20 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239585):
Sure, for groups it's fine.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 20 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239590):
so H and H^op are isomorphic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 20 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239633):
That's coincidence.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 20 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239636):
Because H has order 2 in the Brauer group.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 20 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239640):
In general division rings arent isom to their opposite.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 20 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239664):
oh right never mind sorry

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 20 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239676):
Also, I wonder if these opposites will run into the same kind of issues we had/have in category theory, where it's too easy to get confused between an object of a category and an object of the opposite category

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 20 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239679):
that's exactly why I put `irreducible`!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 20 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239729):
Oh whoops, my mind was numbed by the endless identical instances and I missed that line

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 20 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239745):
@**Mario Carneiro** What do you think of the `irreducible` thing? It seems like a good idea to me? (But then, I might not know all the consequences...)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 20 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239793):
> I don't like the use of irreducible here. What is the application of this file? additive and multiplicative are useful in contexts where you just assert that a theorem has a type involving addition instead of multiplication, and the kernel figures out the defeq; irreducible will block that kind of move. Also you aren't being specific about whether the addition or multiplication is being commuted here.

(by Mario)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 20 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152239934):
For example, suppose I want to prove add_comm from mul_comm. The `multiplicative` trick relies on the fact that `add A x y = add A y x` is definitionally equal to `mul (multiplicative A) x y = mul (multiplicative A) y x`. With irreducible in there I have to insert lots of ops and unops and the kernel can't do it on its own

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 20 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240032):
By the way re: isom to opposite, I was thinking of the map x |-> x, and using antihoms where appropriate

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 20 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240043):
and I think using that defintional equality is not very safe

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 20 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240049):
it's not, it has to be used in carefully controlled circumstances

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 20 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240100):
its use is more or less restricted to one liner proofs where you reinterpret a multiplicative theorem as additive

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 20 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240111):
Right, but here we will want to talk about `op R`, which is a completely different ring.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 20 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240116):
I think it is fitting to make it irreducible.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 20 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240121):
```quote
its use is more or less restricted to one liner proofs where you reinterpret a multiplicative theorem as additive
```
 and it's open to abuse / misuse

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 20 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240126):
if you want it to be a different ring, then you should use a structure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 20 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240192):
really?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 20 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240203):
well isn't the effect the same

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 20 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240312):
It's not exactly the same, as `op (unop x)` will not be defeq to `x`.
(... `newtype`?)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 20 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240326):
then I think the current definition is better :P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 20 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240382):
and this is consistent with my support of auxiliary types

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 20 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240387):
I think `additive` and `multiplicative` should be irreducible as well

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 20 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240399):
```quote
I think `additive` and `multiplicative` should be irreducible as well
```
 I still hope that one day we will have a system where they don't exist.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 20 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240461):
If you are giving a newtype API for opposite, then I would rather have no defeqs at all

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 20 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240464):
`op (unop x) = x` is a theorem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 20 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240470):
as well as `unop (op x) = x`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 20 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240482):
what is newtype?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 20 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240492):
it's a structure with one field

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 20 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240493):
```quote
If you are giving a newtype API for opposite, then I would rather have no defeqs at all
```
 don't we like defeqs?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 20 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240500):
recall the real irreducible discussion

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 20 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240534):
defeq breaks abstractions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 20 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240544):
I was hoping for "newtype" to be defeq in both directions but still a new type

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 20 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240550):
it's a new type to the kernel

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 20 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240551):
if lean had structure eta that would be possible

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 20 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240561):
on the basis that Haskell semantic equality (considering bottom) ~ Lean definitional equality

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 20 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240565):
```quote
defeq breaks abstractions
```
 I don't understand

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 20 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240568):
and also why is `unop (op x) = x` being defeq ok

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 20 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152240594):
(BTW, *lots* of category theory stuff would be less awful with eta for structures)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 20 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152241162):
it's called a newtype because it's underlying representation is the same

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 20 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152241163):
it's a "zero cost abstraction"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 20 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152241305):
> on the basis that Haskell semantic equality (considering bottom) ~ Lean definitional equality

I don't think this is a good comparison; why isn't that ~ lean propositional equality?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 20 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152241327):
I don't understand why, but it seems to be a useful heuristic in practice.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 20 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152241333):
For example `fst (a, b) = a` is okay, but `(fst p, snd p) = p` is not.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 20 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152241465):
The stuff about "lazy patterns" should fit in somehow, too. But I don't know how to make real sense out of any of this. For one thing, Haskell has a (partial) definedness ordering between things like `(fst p, snd p)` and `p`, but in Lean, the thing that would be more defined in Haskell is instead somehow "better", but I don't know why.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 20 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152241485):
It's not like `\lam \<a, b\>, \<a, b\>` is "less defined" than `\lam p, p`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 20 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152241532):
hm, you may be on to something here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 20 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152241566):
I hope you can figure out what it is, because I find it puzzling!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 20 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152241577):
It reminds me of the problem of understanding metamath semantics

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 20 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152241588):
Maybe another way to think of it is that every type is populated, in additional to the usual things, with "raw variables"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 20 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152241593):
which are just terms that don't denote anything, like atoms

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 20 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152241633):
and those two lambdas behave differently on raw variables

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 20 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152241638):
Yes, this sounds promising

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Dec 20 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152241655):
that gives an ordering too perhaps, by specializing variables to values (which might contain new variables inside)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 20 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152241661):
exactly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 20 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152241663):
that's how metamath semantics works

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 20 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/152241667):
it's all about the metavariables

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 07 2019 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/154559706):
so what should we do? @**Johan Commelin** @**Mario Carneiro**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 08 2019 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/154631186):
I guess I have made opposite inductive

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 12 2019 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/154975129):
Should we make `order_dual` in `order/basic.lean` also a structure / inductive?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 12 2019 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/154975174):
or maybe we should merge these two

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 22 2019 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156643371):
@**Johannes Hölzl** what do you think about merging those two?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 22 2019 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156643518):
Which two?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Jan 22 2019 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156643551):
I guess Kenny meant "merge this too"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Jan 22 2019 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156643596):
I would prefer `opposite` to be like `order_dual`, just a definition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 22 2019 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156643616):
I think he continues from the previous message in this thread

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 22 2019 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156643678):
From January 12th

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 22 2019 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156643731):
Ah

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Jan 22 2019 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156643736):
ah

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 22 2019 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156643776):
oh, sorry, I meant merging opposite and order_dual

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Jan 22 2019 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156643870):
Hm, or we need `multiplicative_opp` and `additive_opp`...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 22 2019 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156643898):
I suppose you could have an ordered group and want to reverse the multiplication but not the order, or vice versa

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Jan 22 2019 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156643913):
Yep

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 22 2019 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156643940):
then what should I do?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 22 2019 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156644221):
@**Johannes Hölzl** I don't see why we need multiplicative_opp and additive_opp; the only structure with both addition and multiplication are children of `semiring` in which addition is commutative anyway, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Jan 22 2019 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156644378):
I don't know. I don't do a lot of non-commutative algebra.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Jan 22 2019 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156644453):
I wouldn't merge it, for the problem Reid mentioned. I think we should restrict `opposite` to `*` currently, and see what the actual applications are.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 22 2019 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156644457):
there's a heavy lack of consensus on this thread... everyone seems to want different things

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 22 2019 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156644497):
I also have the sense which I can't explain clearly that `opposite` should be just for multiplication and not addition.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 22 2019 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156644622):
I agree that `opposite` should not flip both. If necessary we can have `add_opposite`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 22 2019 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156644718):
ok, but what about merging opposite and order_dual?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 22 2019 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156644744):
and what about irreducible def vs. just def vs. newtype?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 22 2019 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156644854):
I've just been trying out different options for opposite categories and my impression there is that an irreducible def is the best option, though you could probably make do with other options for algebra because there isn't as heavy use of dependent types there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 22 2019 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156644857):
these all seem like different things

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 22 2019 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156644876):
you may want to invert the order without commuting the multiplication, or the addition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 22 2019 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156644888):
they are independent axes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 22 2019 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156644900):
so they should be different constructions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 22 2019 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156644989):
I'm sure there will be various diamond issues like how `opposite (order_dual A) != order_dual (opposite A)`... I don't have a unified suggestion here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 22 2019 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156645129):
remind me why newtypes are bad @**Reid Barton** . refl is overrated

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 22 2019 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156645153):
you should be using simp lemmas anyway in category theory

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 22 2019 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156645265):
It's really hard to deal with nondefinitional equalities between objects in category theory though.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 22 2019 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156645445):
If you define the objects of C^op to be an inductive type/structure, then eventually you have to deal with the fact that a general object of C^op is not definitionally of the form `op` of something

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 22 2019 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156645580):
isn't that by cases on the objects?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 22 2019 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156645637):
Or you can state your theorem to only apply to objects of the form `op X`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 22 2019 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156645671):
you can't really though, because you need to provide a natural transformation between two functors C^op -> Type or something

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 22 2019 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156645732):
You could define it using cases on the object but putting that in a definition feels like a bad idea

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 22 2019 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156645771):
I need to run but later I can prepare a version with irreducible and a version with an inductive type to compare

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 22 2019 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156645789):
In that case you can just use the `unop` function; the cases happens in the equality proof part

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 22 2019 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156645860):
Well, this hasn't happened yet but potentially you could need to build something by composing a function ... -> X with a function op (unop X) -> ...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 22 2019 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156646207):
I guess the categorical formulation of what's going on is that `op : C => C^op` is a contravariant functor, and `unop` is its essential inverse

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 22 2019 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156646226):
so the roundtrip is an iso

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 22 2019 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156646280):
but in category theory (at least the way I learnt it), C^op is the category with the same objects as C but `Mor[C^op](X,Y) := Mor[C](Y,X)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 22 2019 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156646408):
I mean in category theoretic language, not using material properties of the category

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 22 2019 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156646425):
"the objects of C^op are the objects of C" does not typecheck in category language

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 22 2019 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156646501):
I'm not sure how to define C^op using universal properties

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 22 2019 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156646575):
Just like any category language definition, it is defined up to a natural (2-)isomorphism

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 22 2019 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156646940):
@**Johannes Hölzl** what do you think? irreducible def or newtype?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Jan 22 2019 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156647057):
I prefer a (ir)reducible def. Or at least a `structure` with one field instead of a inductive

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 22 2019 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156647129):
I think the "newtype" option is a structure with one field

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 22 2019 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156647311):
so... irreducible def it is?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 22 2019 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156647491):
I think using a newtype is the "purist" approach, and it is workable if you are consistent about it. the (ir)reducible def approach has lower overhead, but lean will not check as much for you - the onus is on you to not misuse the defeqs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 22 2019 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156647738):
well but Reid has more experience on this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 22 2019 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156647816):
I'm just saying what the tradeoff is

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 23 2019 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156648359):
@**Mario Carneiro** are you happy with making it an irreducible def and then afterwards see if it brings any problems?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 23 2019 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156648373):
I would prefer to just make it a regular def for now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 23 2019 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156648425):
which is I think the current state of the PR

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 23 2019 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156648458):
well it's an inductive type currently

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 23 2019 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156648463):
the first version was an irreducible def

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jan 23 2019 at 00:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156649703):
Hmm... in the category theory opposites PR it is currently a (normal reducibility) definition. Perhaps Mario was talking about that one.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 23 2019 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156649757):
@**Scott Morrison|110087** what do you think then?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jan 23 2019 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156649849):
I think the semireducible def seems like a reasonable compromise. I wouldn't go all the way to the inductive type yet, unless we find that we're still finding confusing situations (because Lean is happily accepting things that "aren't quite right").

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jan 23 2019 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156649931):
Certainly making the def irreducible (using a newtype would have had the same benefit) revealed lots of places in the category_theory files where things "weren't quite right". So I appreciate the argument for keeping this level of protection permanently, and this is the argument for using a newtype.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 23 2019 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156650004):
semireducible is the default right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jan 23 2019 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156650024):
Yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 23 2019 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156650101):
done

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 23 2019 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156650107):
@**Johannes Hölzl** do you see any problem with this PR?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 23 2019 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23538%20opposites/near/156650116):
Actually I'm not in a hurry; I would rather #614 to be merged first

