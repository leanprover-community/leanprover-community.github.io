---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/76686measuretheory.html
---

## Stream: [general](index.html)
### Topic: [measure theory](76686measuretheory.html)

---


{% raw %}
#### [ Mario Carneiro (Jul 19 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129954535):
Hey, this is just an ad for the rather large commit I just put out. It doesn't add too much new stuff, instead it is doing what I do best, proving the same things other people did but better. :) It's focused primarily on the measure theory development, with the hope that I can bring down some of the compile times in that area. But there are some more substantive changes:

* `outer_measure.trim` is the truncation of an outer measure to a measurable space
* `measure_space` was renamed to `measure`. There is a good sense of what a measure space could be, and this wasn't it.
* `measure` and `outer_measure` now have coe_fn instances so you don't need to refer to the underlying `measure_of` function.
* `measure` extends `outer_measure`, so in particular it contains a field that is the outer measure projection, rather than containing a function only defined on measurable sets and recovering the outer measure by extension. In order to ensure we don't add extra measures, we require that a measure is `trimmed` in the sense above.
* `is_complete` asserts that a measure is complete (every null set is measurable)
* `is_null_measurable` is the property of differing from a measurable set by a null set. It is proven that this is a sigma algebra, and a measure extends unchanged to this larger algebra; this is the completion of the measure.
* `lebesgue` has mostly the same theorems but the proofs are rather different. In particular the proof that intervals are measured correctly uses compactness instead of the least upper bound property.
* Some more interval theorems were added; `Icc` is the closed interval

#### [ Kevin Buzzard (Jul 19 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129954606):
Mario do you know about Haar measure? There's a canonical measure on any locally compact Hausdorff topological group (for example the real numbers).

#### [ Kevin Buzzard (Jul 19 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129954650):
The proof is "do the same as for the real numbers, but with an arbitrary locally compact Hausdorff topological group".

#### [ Kevin Buzzard (Jul 19 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129954654):
although some details are a lot more fiddly if I'm honest...

#### [ Mario Carneiro (Jul 19 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129954682):
I have heard of it, but I've never done anything with it besides getting uncomfortable about "unique up to a multiplicative constant"

#### [ Patrick Massot (Jul 19 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129954740):
Lebesgue is also only determined up to a multiplicative constant on a finite dimensional real vector space

#### [ Kevin Buzzard (Jul 19 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129954753):
Well, who said [0,1] should have measure 1...

#### [ Mario Carneiro (Jul 19 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129954762):
Oh, I forgot to mention I added scalar multiplication of measures; they are unfortunately not a module since the base "ring" is `ennreal`

#### [ Patrick Massot (Jul 19 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129954773):
If you talk about [0,1] then you've already chosen a basis of your 1-dimensional vector space

#### [ Kevin Buzzard (Jul 19 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129954778):
yes, my comment was supposed to be before yours :-)

#### [ Patrick Massot (Jul 19 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129954790):
Too bad we miss an opportunity to enjoy module type class hell

#### [ Kevin Buzzard (Jul 19 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129954845):
If CS people are happy to divide by 0, why can't they multiply by infinity?

#### [ Kevin Buzzard (Jul 19 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129954851):
Just make it 0 :-)

#### [ Mario Carneiro (Jul 19 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129954869):
actually `ennreal` is surprisingly nice as an ordered semiring

#### [ Mario Carneiro (Jul 19 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129954880):
the fact that it is a complete lattice really helps

#### [ Patrick Massot (Jul 19 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129954881):
That's the trouble: if I understand correctly Mario *is* happy to multiply by infinity

#### [ Mario Carneiro (Jul 19 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129954981):
>  a basis of your 1-dimensional vector space

It's not a vector space

#### [ Patrick Massot (Jul 19 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129954991):
affine space I should say

#### [ Mario Carneiro (Jul 19 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129955000):
is there a notion of semi-vector space in the literature?

#### [ Mario Carneiro (Jul 19 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129955007):
there are no negatives

#### [ Kevin Buzzard (Jul 19 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129955061):
I am amazed that this is not already in Lean

#### [ Patrick Massot (Jul 19 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129955062):
You know we already don't want to talk about semirings

#### [ Kevin Buzzard (Jul 19 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129955070):
I guess a monoid is just a semi-module over N

#### [ Mario Carneiro (Jul 19 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129955085):
I find of am as well. We have semi everything else, but modules pick right up at rings

#### [ Kevin Buzzard (Jul 19 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129955126):
actually maybe that's a commutative monoid

#### [ Mario Carneiro (Jul 19 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129955195):
A nat-semi-module is a commutative monoid

#### [ Mario Carneiro (Jul 19 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129955215):
but if the scalar field is something else then it's different

#### [ Patrick Massot (Jul 19 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129957474):
I'm curious about all this integration stuff in mathlib. I never tried to use it or even looked at it. Can we do crazy things like proving the integral of `id` on `[1, 2]` is `3/2`?

#### [ Sean Leather (Jul 20 2018 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129979482):
```quote
Hey, this is just an ad for the rather large commit I just put out. It doesn't add too much new stuff, instead it is doing what I do best, proving the same things other people did but better. :)
```

Thanks for that, @**Mario Carneiro**!

#### [ Mario Carneiro (Jul 20 2018 at 08:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129979507):
you were the one who mentioned the issue with `meaure'_union`, right? I may have gone a bit overboard. :)

#### [ Sean Leather (Jul 20 2018 at 08:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129979565):
```quote
you were the one who mentioned the issue with `meaure'_union`, right? 
```

Indeed, I was.

```quote
I may have gone a bit overboard. :)
```

No problem! As long as you think it improved things.

#### [ Kevin Buzzard (Jul 20 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129981327):
Actually I have a problem too -- Fermat's Last Theorem can't currently be proved by `finish` -- can you fix it for me Mario?

#### [ Johan Commelin (Jul 20 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129981388):
Kevin, the proof is `by ᛗᛃᛟᛚᚾᛁᚱ`

#### [ Sean Leather (Jul 20 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129981390):
This is the `Mario` variation of the `ᛗᛃᛟᛚᚾᛁᚱ` tactic.

#### [ Johan Commelin (Jul 20 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129981468):
Speaking of hammers... I would like the decomposition theorem for mixed Hodge modules.

#### [ Kevin Buzzard (Jul 20 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129981485):
Yeah well I would like perfectoid spaces but I spent an hour last night writing the universal property of quotient groups :-/

#### [ Kenny Lau (Jul 20 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129981494):
should have told me to write it lol

#### [ Kevin Buzzard (Jul 20 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129981498):
Can you do algebraically closed fields Kenny? Chris' polynomials in one variable got accepted

#### [ Kevin Buzzard (Jul 20 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129981499):
Things are happening :-)

#### [ Kenny Lau (Jul 20 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129981561):
have you proved that k[X] is UFD?

#### [ Kevin Buzzard (Jul 20 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129981569):
https://github.com/kbuzzard/lean-perfectoid-spaces/blob/master/src/for_mathlib/quotient_group.lean

#### [ Kevin Buzzard (Jul 20 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129981574):
Do we even have a definition of UFD? It's pretty ugly

#### [ Kenny Lau (Jul 20 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129981578):
also I think we need "a in L/K: a is integral over K iff K(a) is finite"

#### [ Kenny Lau (Jul 20 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129981588):
```quote
Do we even have a definition of UFD? It's pretty ugly
```
A is UFD iff (A\{0})/A* is a free monoid :)

#### [ Kevin Buzzard (Jul 20 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129981590):
Blair is doing fdvs. Why not ask her if you can help?

#### [ Kevin Buzzard (Jul 20 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129981636):
We need more UG maths!

#### [ Johan Commelin (Jul 20 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129981648):
So we need more UG's, so that we can prove things `by UG`. You do have access to two hammers!

#### [ Kenny Lau (Jul 20 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129981650):
let's say we've built L such that every polynomial in K[X] splits over L. How then do you show that L contains an algebraically closed field?

#### [ Kenny Lau (Jul 20 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129981660):
I think we should prove that K[X] is ED, that might help

#### [ Johan Commelin (Jul 20 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129981699):
That was almost there, right?

#### [ Kenny Lau (Jul 20 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129981706):
how should we prove "L is algebraically closed iff every finite extension of L is L"? that would involve building splitting fields

#### [ Johan Commelin (Jul 20 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129981707):
Except that the definition of ED wasn't optimal, so Chris had to work with degree + 1, or change the definition

#### [ Johan Commelin (Jul 20 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129981728):
I guess you want to do separable closure at the same time

#### [ Kenny Lau (Jul 20 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129981783):
my point is, there's a long way to go before we build algebraic closure

#### [ Johannes Hölzl (Jul 20 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129985250):
@**Patrick Massot** there is no integral in mathlibs measure theory, yet.

#### [ Johannes Hölzl (Jul 20 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129985369):
```quote
Oh, I forgot to mention I added scalar multiplication of measures; they are unfortunately not a module since the base "ring" is `ennreal`
```
Yeah, semimodules would be nice to have. But up to now I didn't find any literature on them.

#### [ Patrick Massot (Jul 20 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129985492):
Oh, I didn't even imagine that. I was concerned about the fact that we don't have derivative and that could be a problem when wanting to compute integrals.

#### [ Johannes Hölzl (Jul 20 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129985626):
Well, the basic theory of integrals in measure theory doesn't need derivatives. It starts with integration over the Lebesgue measure. But there is some theory to be developed up to this point.

#### [ Patrick Massot (Jul 20 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129985681):
Sure, that's why I though we could have integrals but no mean of computing one

#### [ Patrick Massot (Jul 20 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129985691):
But let's have normed spaces first :wink:

#### [ Kevin Buzzard (Jul 20 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129985812):
```quote
```quote
Oh, I forgot to mention I added scalar multiplication of measures; they are unfortunately not a module since the base "ring" is `ennreal`
```
Yeah, semimodules would be nice to have. But up to now I didn't find any literature on them.
```
Maybe that's because most mathematicians think they're about as useless as `distrib`s? Having said that, the existence of distribs proves that computer scientists have very different opinions to mathematicians as to what is "nice to have". What would mathlib want semimodules for? Is this something to do with compile times or something?

#### [ Kevin Buzzard (Jul 20 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129985886):
A related story : @**Chris Hughes** decided to do group actions yesterday, and his first question was "wait -- there's no mention of the inverse in the definition?". "No", I replied. "Oh dear, then we'll have to make it monoid actions if we want to get it into mathlib..."

#### [ Johannes Hölzl (Jul 20 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/129985954):
`semimodules` would help to abstract some basic proofs and syntax. we can abstract the scalar multiplication over `measure`, `outer_measure`, measurable functions into `ennreal`, integrable functions into `ennreal`, etc...

#### [ Mario Carneiro (Jul 20 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/130014392):
>  there is no integral in mathlibs measure theory, yet.

FYI I started working on that yesterday

#### [ Kenny Lau (Jul 20 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/130014435):
nice

#### [ Patrick Massot (Jul 20 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/130014452):
Does it mean you'll do derivatives as well?

#### [ Mario Carneiro (Jul 20 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/130014469):
no, like Johannes said, those two are completely unrelated except for a certain fundamental theorem

#### [ Mario Carneiro (Jul 20 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/130014474):
obviously the fundamental theorem can't be stated until we have both parts

#### [ Patrick Massot (Jul 20 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/130014517):
There are indeed completely unrelated except for their fundamental relation

#### [ Patrick Massot (Jul 20 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/130014530):
Anyway, it's already great to work on integrals

#### [ Mario Carneiro (Jul 20 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/130014532):
I don't even think they operate on the same kinds of spaces. There are spaces with integrals but no derivatives and vice versa

#### [ Patrick Massot (Jul 20 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/130014540):
sure

#### [ Mario Carneiro (Jul 20 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/130014561):
so it's not like they are really different sides of the same coin, as in you could use either one to define the other

#### [ Mario Carneiro (Jul 20 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/130014627):
but I guess people care about R -> R and it's true there

#### [ Patrick Massot (Jul 20 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/130014634):
it's an important special case, especially for teaching purposes

#### [ Mario Carneiro (Jul 20 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/130014658):
especially when it gives people the weird impression that these things are fundamentally related

#### [ Mario Carneiro (Jul 20 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/130014672):
they are related, but not fundamentally

#### [ Mario Carneiro (Jul 20 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/130014717):
in the foundational sense

#### [ Patrick Massot (Jul 20 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/130014722):
Since you seem to be in an analytical mood, what about returning to the oldest open mathlib PR?

#### [ Mario Carneiro (Jul 20 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/130014765):
Well, measure theory isn't quite analysis

#### [ Mario Carneiro (Jul 20 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/130014769):
Let's put it next on the list

#### [ Mario Carneiro (Jul 20 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/130014820):
that will set us up for derivatives

#### [ Kenny Lau (Oct 14 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/135776602):
```quote
>  there is no integral in mathlibs measure theory, yet.

FYI I started working on that yesterday
```
how is it now?

#### [ Mario Carneiro (Oct 14 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/135776650):
Johannes has taken over on that development

#### [ Mario Carneiro (Oct 14 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/135776653):
I think it might be merged now? I heard some talk about it but I haven't checked

#### [ Patrick Massot (Oct 14 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/135776655):
https://leanprover.zulipchat.com/#narrow/stream/116395-maths/subject/How.20much.20of.20analysis.20is.20formalised.3F/near/135735421

#### [ Kenny Lau (Oct 14 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/measure%20theory/near/135776663):
ok


{% endraw %}
