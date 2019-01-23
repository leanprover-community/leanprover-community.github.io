---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/81043LargestSquareintheFibonacciSequence.html
---

## Stream: [maths](index.html)
### Topic: [Largest Square in the Fibonacci Sequence](81043LargestSquareintheFibonacciSequence.html)

---

#### [Kevin Buzzard (May 23 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126977998):
Did you know that 144 is the largest square in the Fibonacci sequence?

#### [Kevin Buzzard (May 23 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126977999):
The proof is elementary but delicate

#### [Kevin Buzzard (May 23 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126978039):
I give talks about this to bright schoolchildren occasionally

#### [Kevin Buzzard (May 23 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126978044):
http://wwwf.imperial.ac.uk/~buzzard/2017nt2.pdf

#### [Kevin Buzzard (May 23 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126978047):
There is a sketch of the idea

#### [Kevin Buzzard (May 23 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126978048):
I'm giving one such talk on Saturday

#### [Kevin Buzzard (May 23 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126978050):
to the British IMO team

#### [Kevin Buzzard (May 23 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126978053):
and in fact I am giving two talks to these people on Saturday

#### [Kevin Buzzard (May 23 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126978055):
one on this

#### [Kevin Buzzard (May 23 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126978056):
and one on...whatever I like

#### [Kevin Buzzard (May 23 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126978066):
So I have made the crazy decision to try and give my second talk on a Lean proof of this fact

#### [Kevin Buzzard (May 23 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126978070):
The only problem is that today is Wednesday

#### [Kevin Buzzard (May 23 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126978075):
which means that it's only three days to Saturday

#### [Kevin Buzzard (May 23 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126978087):
So I did this

#### [Kevin Buzzard (May 23 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126978088):
https://github.com/kbuzzard/lean-squares-in-fibonacci/issues/1

#### [Kevin Buzzard (May 23 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126978092):
and I will start this evening

#### [Kevin Buzzard (May 23 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126978094):
but if anyone wants to help

#### [Kevin Buzzard (May 23 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126978137):
then I would happily let them join in

#### [Kevin Buzzard (May 23 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126978138):
give them push access, whatever

#### [Kevin Buzzard (May 23 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126978141):
The link to the issues makes it clear what I think the problems are

#### [Kevin Buzzard (May 23 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126978148):
(1) We either cheat and assume some UG-level facts about primes

#### [Kevin Buzzard (May 23 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126978152):
(when -2 is a square mod p)

#### [Kevin Buzzard (May 23 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126978154):
or we prove it

#### [Kevin Buzzard (May 23 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126978157):
which will involve proving that a poly of degree n over a field has at most n roots

#### [Kevin Buzzard (May 23 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126978164):
and that Z/pZ is a field

#### [Kevin Buzzard (May 23 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126978171):
(2) we either use the real numbers or build our own Z[(1+sqrt(5))/2]

#### [Kevin Buzzard (May 23 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126978177):
(3) a bunch of relatively simple arithmetic

#### [Kevin Buzzard (May 23 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126978180):
but a fair amount of it, from a Lean point of view

#### [Kevin Buzzard (May 23 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126978220):
I attained my schemes goal

#### [Kevin Buzzard (May 23 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126978224):
so I want to spend a few days goofing around with this one

#### [Kevin Buzzard (May 23 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126978225):
it's very easy arithmetic

#### [Kevin Buzzard (May 23 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126978228):
and maybe I will do it all myself

#### [Kevin Buzzard (May 23 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126978233):
but if anyone wants to help

#### [Kevin Buzzard (May 23 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126978238):
this would be greatly appreciated :-)

#### [Kevin Buzzard (May 23 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126978259):
@**Johannes Hölzl** and @**Chris Hughes** I might have to steal your work (with attribution of course).

#### [Kevin Buzzard (May 23 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126978323):
Johannes -- who do I credit if I take your polynomial stuff from mason-stothers? [or mason-stother as you seem to have called it]? Is it you or JWageM?

#### [Kevin Buzzard (May 23 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126978336):
I firmly believe I could do this entire thing in 3 days

#### [Kevin Buzzard (May 23 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126978338):
it's a bit unfortunate about the marking I still have to do though :-/

#### [Kevin Buzzard (May 23 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126978382):
Chris and Kenny will have finished their exams by Friday afternoon UK time so this would be a perfect all-night binge for them to do afterwards.

#### [Kevin Buzzard (May 23 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126978384):
;-)

#### [Kevin Buzzard (May 23 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126978394):
OK now back to marking

#### [Johannes Hölzl (May 23 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126978481):
Mason-stother's polynomials are from us both, most parts were done by Jens, some by me. Its okay to only credit Jens.

#### [Nicholas Scheel (May 23 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126980169):
Hi! How can I help best? Maybe start building Z[(1+sqrt(5))/2] ? I have a little experience with field extensions from abstract algebra this past semester ...

#### [Nicholas Scheel (May 23 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126980265):
that’s really just Z[sqrt(5)] right? field operations will get you (1+-sqrt(5))/2 from that

#### [Patrick Massot (May 23 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126980273):
He wants a ring, not a field

#### [Patrick Massot (May 23 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126980283):
And that's what this notation denotes

#### [Kevin Buzzard (May 23 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126980547):
Right -- there is Q(sqrt(5)) = Q(alpha) [alpha := (1+sqrt(5))/2] and there is Z[sqrt(5)] which is strictly smaller than Z[alpha] [it has index 2]

#### [Kevin Buzzard (May 23 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126980642):
The only reason I suggested the ring not the field was (1) rings have fewer axioms than fields and (2) my instinct was to construct the smallest object which was mathematically reasonable [so no semirings or distribs, thank you] and which contained enough to formalise the statement "u_m = (alpha^m - beta^m) / sqrt (5)"...oh crap

#### [Kevin Buzzard (May 23 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126980651):
maybe a field is fine :-)

#### [Kevin Buzzard (May 23 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126980667):
One could prove sqrt(5) * u_m = alpha^m - beta^m

#### [Kevin Buzzard (May 23 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126980710):
and then mumble about integral domains

#### [Kevin Buzzard (May 23 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126980735):
OK so @**Nicholas Scheel** if you want to take a look at how the complex numbers were built from the real numbers in mathlib (in some file called complex.lean probably) then you could just copy this and build Q(sqrt(5)) from Q by adjoining a square root of 5

#### [Kevin Buzzard (May 23 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126980754):
The only difficulty will be in proving that if a+b*sqrt(5) is non-zero then a^2-5b^2 is non-zero, which you need for division

#### [Kevin Buzzard (May 23 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126980762):
For the complexes the argument is that everything is positive, that doesn't work here

#### [Kevin Buzzard (May 23 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126980764):
you need that 5 isn't the square of a rational

#### [Kevin Buzzard (May 23 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126980770):
but modulo that, there's your Q(sqrt(5))

#### [Kevin Buzzard (May 23 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126980786):
at some point one would need this anyway, to prove Z[alpha] is an integral domain, so there's no getting away from it

#### [Chris Hughes (May 23 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126981799):
I've done some stuff on integers mod n which I'll send you when I get home.

#### [Nicholas Scheel (May 23 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126982536):
Ah okay, I see ... I think I'll try to build Z[alpha], doesn't look like we'll need division

#### [Chris Hughes (May 23 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126985180):
@**Kevin Buzzard** Very messy, but the most basic stuff about integers mod n is there. https://github.com/dorhinj/leanstuff/blob/master/Zmod1.lean

#### [Chris Hughes (May 23 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126985212):
@**Nicholas Scheel** I also made a bit of a start on univariate polys, although I haven't done much more than copy Johannes stuff on multivariate polys.

#### [Chris Hughes (May 23 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126985259):
I think Sean's finset.max would be a more appropriate definition of degree than `sup`

#### [Nicholas Scheel (May 23 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126985360):
okay I have a commutative ring instance for Z[alpha]!

#### [Johannes Hölzl (May 23 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126985419):
with `sup` you don't need to use `iget`. `max` is the better name but I think `sup` has the better behaviour.

#### [Patrick Massot (May 23 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126989627):
Thanks, but I don't know how to use `sup`

#### [Kenny Lau (May 23 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126990758):
@**Kevin Buzzard** have you pushed?

#### [Kevin Buzzard (May 23 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126990917):
pushed what?

#### [Kenny Lau (May 23 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126990921):
fibonacci

#### [Kevin Buzzard (May 23 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126990927):
Chris -- Johannes and his student wrote some univariate poly stuff in their mason-stother repo

#### [Kevin Buzzard (May 23 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126991057):
What Fibonacci is there for me to push?

#### [Kevin Buzzard (May 23 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126991060):
I have epsilon

#### [Kevin Buzzard (May 23 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126991062):
I proved `luc (m + 3) = 2 * fib (m + 3) + fib m`

#### [Kevin Buzzard (May 23 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126991064):
I will push some stuff

#### [Chris Hughes (May 23 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126991211):
They didn't do the theorem you need I don't think.

#### [Kevin Buzzard (May 23 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126991755):
I pushed some stuff

#### [Kevin Buzzard (May 23 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126991798):
I proved 2/3 of point 4

#### [Kevin Buzzard (May 23 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126993768):
Is `gcd (a + n * b) b = gcd a b` in lean or mathlib somewhere? (everything a nat)]

#### [Patrick Massot (May 23 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126993776):
If everything is a nat, this is almost certainly wrong in some edge case

#### [Kenny Lau (May 23 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126993922):
there isn't, since gcd is well-defined for 0 in the real world

#### [Patrick Massot (May 23 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126994021):
I knew it: edge case

#### [Kenny Lau (May 23 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126994031):
```lean
#check nat.gcd_rec -- nat.gcd m n = nat.gcd (n % m) m
open nat
example (a n b : ℕ) : gcd (a + n * b) b = gcd a b :=
by rw [gcd_comm, gcd_rec, add_mul_mod_self_right, ← gcd_rec, gcd_comm]
```

#### [Kenny Lau (May 23 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126994032):
there is no edge case!

#### [Patrick Massot (May 23 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126994097):
This is an edge case to the general statement that every general statement about  nat is wrong

#### [Kevin Buzzard (May 23 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126994501):
of course one could argue that gcd 0 0 = 0 is already wrong

#### [Kevin Buzzard (May 23 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126994507):
given that 7 divides both 0 and 0

#### [Patrick Massot (May 23 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126994600):
To be honest, that one has nothing to do with nat. It's also a problem in integers

#### [Kevin Buzzard (May 23 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126994670):
You know that $$\frac{\zeta(1-k)}{2} + \Sigma_{n\geq1}\sigma_{k-1}(n)q^n$$ is a modular form, right?

#### [Kevin Buzzard (May 23 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126994695):
Here $$\sigma_{k-1}(n)$$ denotes the sum of the $$k-1$$ st powers of the positive divisors of $$n$$.

#### [Kevin Buzzard (May 23 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126994718):
but if you set $$n=0$$ in the sum you get the sum of the $$k-1$$ st powers of the positive divisors of $$0$$

#### [Kevin Buzzard (May 23 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126994777):
so that's $$1^{k-1} + 2 ^{k-1} + 3^{k-1} + \cdots$$

#### [Kevin Buzzard (May 23 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126994781):
which is $$\zeta(1-k)$$ by...erm...definition...or something

#### [Kevin Buzzard (May 23 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126994808):
but the sum is only over half of the integers

#### [Kevin Buzzard (May 23 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126994813):
so you should only take the term at zero half as seriously

#### [Kevin Buzzard (May 23 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126994819):
which gives you $$\zeta(1-k)/2$$

#### [Kevin Buzzard (May 23 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126994823):
and that's how I remember it

#### [Patrick Massot (May 23 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126994876):
And we are surprised formalizing maths is hard...

#### [Nicholas Scheel (May 23 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126995026):
@**Kevin Buzzard** Should I make a fork, or may I have commit access?

#### [Kenny Lau (May 23 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126995041):
do I have commit access?

#### [Kevin Buzzard (May 23 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126995177):
what is the most sensible idea?

#### [Kevin Buzzard (May 23 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126995196):
nobody has commit access except me

#### [Kevin Buzzard (May 23 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126995201):
but I am happy to give it to anybody

#### [Kevin Buzzard (May 23 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126995212):
unless someone has a good reason why I shouldn't do this

#### [Kevin Buzzard (May 23 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126995218):
I need to know your github usernames I guess

#### [Kenny Lau (May 23 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126995291):
I'll kindly delete your alpha and beta :P (after proving points 4 and 6)

#### [Patrick Massot (May 23 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126995295):
If I were you I would fear seeing constructive stuff invading my repo

#### [Kevin Buzzard (May 23 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126995412):
OK Kenny and Nicholas you should have push access

#### [Kenny Lau (May 23 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126995415):
thanks

#### [Kenny Lau (May 23 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126995424):
```quote
If I were you I would fear seeing constructive stuff invading my repo
```
much fear of the unknown :P

#### [Kevin Buzzard (May 23 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126995425):
but lemme push some stuff

#### [Patrick Massot (May 23 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126995427):
Constructive madness on the way...

#### [Kevin Buzzard (May 23 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126995432):
I need a job done

#### [Patrick Massot (May 23 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126995455):
Selling your mathematician soul...

#### [Kevin Buzzard (May 23 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126995551):
OK I am pushed

#### [Kenny Lau (May 23 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126995598):
waitttt where did the Z alpha come from

#### [Kenny Lau (May 23 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126995613):
oh Nicholas built it...

#### [Kenny Lau (May 23 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126995631):
@**Nicholas Scheel** do you think we'll really need it?

#### [Nicholas Scheel (May 23 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126995633):
oops sorry, did I step on your push?

#### [Kenny Lau (May 23 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126995668):
no

#### [Kenny Lau (May 23 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126995683):
I'm just doubting whether we need sqrt(5) at all

#### [Kevin Buzzard (May 23 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126995698):
Here's the reason I think we might need sqrt(5)

#### [Nicholas Scheel (May 23 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126995703):
I think this might help along the way ;) :
```
lemma αβsum : α + β = 1 := rfl
lemma αβprod : α * β = -1 := rfl
```

#### [Kevin Buzzard (May 23 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126995711):
that looks really good

#### [Kevin Buzzard (May 23 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126995719):
it's a little bit better than my method

#### [Kenny Lau (May 23 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126995738):
so, constructivism wins?

#### [Kevin Buzzard (May 23 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126995747):
To prove something like `luc (m + 3) = 2 * fib (m + 3) + fib m` you can just do it by induction

#### [Kevin Buzzard (May 23 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126995765):
but to prove `luc (4 * n) = (luc (2 * n) ^ 2) - 2`

#### [Kevin Buzzard (May 23 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126995813):
the only method I know is to prove the general sqrt (5) formula

#### [Kenny Lau (May 23 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126995817):
you just need the right lemmas

#### [Kevin Buzzard (May 23 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126995822):
maybe some theorem of logic says you don't need square roots of 5

#### [Kenny Lau (May 23 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126995826):
like the one I proved that day

#### [Kenny Lau (May 23 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126995832):
```lean
variables (m n : ℕ)

local attribute [elab_as_eliminator] nat.strong_induction_on

theorem to_be_named : fib (m + n + 1) =
  fib m * fib n + fib (m + 1) * fib (n + 1) :=
nat.strong_induction_on n $ λ n, nat.cases_on n (λ _, by simp [fib]) $ λ n,
nat.cases_on n (λ _, by simp [fib]) $ λ n ih,
have H1 : _ := ih n (nat.lt_trans (nat.lt_succ_self n) (nat.lt_succ_self (n+1))),
have H2 : fib (m + n + 2) = _ + _ * (fib n + fib (n+1)) := ih (n+1) (nat.lt_succ_self (n+1)),
calc  fib (m + n + 1) + fib (m + n + 2)
    = fib m * (fib n + fib (n+1)) + fib (m+1) * (fib (n+1) + (fib n + fib (n+1))) :
  by rw [H1, H2, mul_add, mul_add, mul_add, mul_add]; ac_refl
```

#### [Kevin Buzzard (May 23 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126995834):
but then you will end up defining some auxiliary function on Z x Z

#### [Kevin Buzzard (May 23 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126995843):
Let me just read through the proof

#### [Kevin Buzzard (May 23 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126995867):
Of course one might also argue that using sqrt(5) is a _natural_ thing to do

#### [Kevin Buzzard (May 23 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126995872):
which might make it a good thing to do

#### [Kenny Lau (May 23 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126995929):
I should add "building the algebraic numbers" to my want-to-do-but-god-knows-when list

#### [Kevin Buzzard (May 23 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126995944):
Of course you could also take the ring Q[x] and quotient out by the ideal (x^2-5) right? ;-)

#### [Kevin Buzzard (May 23 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126995972):
I will write comments about the proof in the issue

#### [Patrick Massot (May 23 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126996089):
From an arithmetic point of view it makes much more sense than defining square root on nonnegative reals

#### [Mario Carneiro (May 23 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126996291):
Hey, it might be too late for this remark but I built the ring Z[\sqrt n] in `pell.lean`. Not directly applicable, but it might be useful

#### [Mario Carneiro (May 23 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126996458):
> of course one could argue that gcd 0 0 = 0 is already wrong
> given that 7 divides both 0 and 0

I think there are good reasons to believe that gcd 0 0 = 0 is *right* over both nat and int, and in traditional math, if you think about the integers in that calculation as representing their principal ideals. (gcd m n) = (m, n)

#### [Mario Carneiro (May 23 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126996521):
so here "greatest" actually means greatest in the divisor order, putting 0 at the top not the bottom

#### [Kenny Lau (May 23 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126996708):
@**Kevin Buzzard** 7 divides both 0 and 0, and 7 divides gcd(0,0) = 0, consistent with the UMP of GCD

#### [Kenny Lau (May 23 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126997108):
@**Kevin Buzzard** can I push?

#### [Kevin Buzzard (May 23 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126997123):
sure go ahead and push

#### [Kevin Buzzard (May 23 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126997133):
I wrote a more detailed sketch of how to flesh out the argument in the issue

#### [Kenny Lau (May 23 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126997191):
are you sure I have write access?

#### [Kevin Buzzard (May 23 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126997208):
I need to go and steer my children towards their beds now. Thanks for the help all of you. Mario and Kenny, I see the advantages of the "zero bigger than everything" approach here! Of course it's just the ideal-theoretic way of thinking about it -- gcd(x,y) = ideal generated by x and y, and if it's principal then let's choose a canonical generator if we can.

#### [Kevin Buzzard (May 23 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126997214):
Kenny I think I invited you. Did you check your email or did I fail?

#### [Kenny Lau (May 23 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126997225):
oh, I need to accept the invitation

#### [Kevin Buzzard (May 23 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126997228):
https://github.com/kbuzzard/lean-squares-in-fibonacci/issues/1

#### [Kevin Buzzard (May 23 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126997235):
Note the last part -- point 12 is slightly delicate, it needs the following consequence of uniqueness of prime factorization: if gcd(x,y)=1 and x*y is a square then x and y are both squares (here x,y>0).

#### [Kevin Buzzard (May 23 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126997316):
and for that you need: n square iff v_p(n) even for all primes p (v_p(n) = largest power of p dividing n) and gcd(x,y)=1 iff min(v_p(x),v_p(y))=0 for all primes p

#### [Mario Carneiro (May 23 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126997456):
pretty sure that exact theorem is in my formalization

#### [Mario Carneiro (May 23 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126997502):
and you don't need UFD for it

#### [Kevin Buzzard (May 23 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126997557):
well you do need something

#### [Kevin Buzzard (May 23 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126997562):
because it's not true in a general ring

#### [Kevin Buzzard (May 23 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126997571):
well I suppose it depends on what you mean by gcd in a general ring

#### [Mario Carneiro (May 23 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126997580):
you need nat.gcd facts and some induction

#### [Mario Carneiro (May 23 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126997644):
I'm not saying it doesn't depend in a reverse mathematics way on UFD, but you don't need all that complexity for the proof

#### [Kevin Buzzard (May 23 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126997647):
a bit like the proof of UFD ;-)

#### [Kevin Buzzard (May 23 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126997654):
[I mean, you need nat.gcd facts and some induction for that too]

#### [Kevin Buzzard (May 23 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126997670):
For a general comm ring there are two natural defs of gcd, one more general than the other

#### [Kevin Buzzard (May 23 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126997701):
and the weaker version of coprime doesn't cut it

#### [Kevin Buzzard (May 23 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126997705):
oh there are also issues with units

#### [Kevin Buzzard (May 23 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126997713):
-4 and -9 are coprime and their product is a square etc etc

#### [Kevin Buzzard (May 23 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126997756):
so there are issues in general

#### [Kevin Buzzard (May 23 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126997767):
but I take your point that you are saying you don't have to go through v_p(x)

#### [Mario Carneiro (May 23 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126997771):
right

#### [Mario Carneiro (May 23 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126997780):
it's a nice way to conceptualize it, but it's technically complicated and not worth it for most problems IMO

#### [Mario Carneiro (May 23 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126997837):
whenever you need a fact that would come from primality of the p in v_p(n), just use the coprime assumption instead, it's just as well for the purpose of the proof

#### [Kenny Lau (May 23 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126998319):
@**Mario Carneiro** what's the fastest way to know that `n=1` or `n=2` given `n` divides 2?

#### [Mario Carneiro (May 23 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126998321):
n | 2 implies n <= 2

#### [Chris Hughes (May 23 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126998325):
2 is prime

#### [Mario Carneiro (May 23 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126998326):
alternatively, 2 is prime

#### [Kenny Lau (May 23 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126998329):
oh lol

#### [Kenny Lau (May 23 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/126998680):
Point 4 done!

#### [Nicholas Scheel (May 24 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127001593):
I want to prove this but I don't know how? `lemma Fib.is_fib (n : ℤ) : Fib (n+2) = Fib n + Fib (n + 1)` :P

#### [Nicholas Scheel (May 24 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127001606):
```  cases n, refl,
  induction n using nat.case_strong_induction_on with n ih, refl,
  cases n, refl,
  cases n, refl,
  have ih0 := ih n (nat.le_succ_of_le (nat.le_succ _)),
  have ih1 : Fib (-[1+n+1] + 2) = Fib -[1+n+1] + Fib -[1+n] :=
    ih (n+1) (nat.le_succ _),
  have ih2 : Fib -[1+n] = Fib -[1+n+2] + Fib -[1+n+1] :=
    ih (n+2) (le_refl _),
  ```

#### [Kenny Lau (May 24 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127001612):
write x^(n+2) as x^n x^2?

#### [Kenny Lau (May 24 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127001619):
you might find `int.induction_on` useful

#### [Kenny Lau (May 24 2018 at 04:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127009320):
Point 6 done except the last claim

#### [Kevin Buzzard (May 24 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017268):
OK this is great.

#### [Kevin Buzzard (May 24 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017269):
Looking at what has been already done

#### [Kevin Buzzard (May 24 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017270):
I already easily have enough material to fill the session.

#### [Kevin Buzzard (May 24 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017271):
So actually the time pressure is over.

#### [Kevin Buzzard (May 24 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017311):
These kids are smart kids (my audience of 8)

#### [Kevin Buzzard (May 24 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017312):
but the Lean session will last 90 minutes

#### [Kevin Buzzard (May 24 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017317):
and even talking about how to construct Z[alpha] and computing Fibonacci numbers mod n throws up so much stuff

#### [Kevin Buzzard (May 24 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017322):
that my talk is already written.

#### [Kevin Buzzard (May 24 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017325):
However I am definitely still interested in finishing the job :-)

#### [Kevin Buzzard (May 24 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017326):
Here's a question.

#### [Kevin Buzzard (May 24 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017363):
Oh -- before I start -- thanks to Kenny and Nicholas for their contributions!

#### [Kevin Buzzard (May 24 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017369):
I'm still mired in marking and preparing these talks for Sat was beginning to become a worry.

#### [Kevin Buzzard (May 24 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017374):
The question is how to express the following assertion in Lean

#### [Kevin Buzzard (May 24 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017377):
We need to compute the Fibonacci sequence mod 16

#### [Kevin Buzzard (May 24 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017422):
The theorem is that mod 16 it goes like this:

#### [Kevin Buzzard (May 24 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017424):
`[0, 1, 1, 2, 3, 5, 8, 13, 5, 2, 7, 9, 0, 9, 9, 2, 11, 13, 8, 5, 13, 2, 15, 1]`

#### [Kevin Buzzard (May 24 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017427):
And the proof is "trivial by induction"

#### [Kevin Buzzard (May 24 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017433):
(because each term in that list is the sum of the previous two terms mod 16, and at the end we have 15 + 1 = 0 and 1 + 0 = 1 so we wrap back)

#### [Kevin Buzzard (May 24 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017472):
The question is how one can prove this in Lean in a way which actually looks reasonable

#### [Kevin Buzzard (May 24 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017478):
This is not a question about how to do anything mod n, this is a specific question about mod 16 (there's an analogous one for mod 3 but I chose the most awkward one).

#### [Kevin Buzzard (May 24 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017480):
One issue is what to do the induction on.

#### [Kevin Buzzard (May 24 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017486):
You could do strong induction on m

#### [Kevin Buzzard (May 24 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017488):
or you could write m = 24 * n + t with 0 <= t < 24 and do induction on n

#### [Kevin Buzzard (May 24 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017527):
What I am (not really that) concerned about is that with either approach you end up writing essentially the same code block 24 or so times

#### [Kevin Buzzard (May 24 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017581):
In the direct strong induction argument you case on n mod 24 and I don't really know how to do that

#### [Kevin Buzzard (May 24 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017584):
hmm

#### [Kevin Buzzard (May 24 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017586):
maybe it's OK

#### [Kevin Buzzard (May 24 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017597):
if t < 22 it's some lemma of the form `(a+b)%m = (a%m+b%m)%m` -- is that in Lean/mathlib?

#### [Kevin Buzzard (May 24 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017599):
and in the induction case you end up with a statement of the form `a0 and a1 and ... and a23`

#### [Kevin Buzzard (May 24 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017602):
you would never write such a statement in python or whatever, you would somehow wrap everything up in a list

#### [Kevin Buzzard (May 24 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017603):
Hmm

#### [Kevin Buzzard (May 24 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017644):
I think my question is that I am seeing two competing methods for proving this and they book look a bit "trivial in maths but a bit ugly to write in Lean" at the minute. Anyone have any suggestions?

#### [Chris Hughes (May 24 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017725):
```quote
if t < 14 it's some lemma of the form `(a+b)%m = (a%m+b%m)%m` -- is that in Lean/mathlib?
```
int.modeq.modeq_add should help, since this is defeq to `a + b \== a%m + b % m` Although I forgot `modeq_mod` i.e. , so you'll have to prove that.
Why not just prove it as a lemma about integers mod n, and not naturals.

#### [Kevin Buzzard (May 24 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017789):
The problem with working with integers mod n is that if you want the _input_ to fib to be an integer mod n (n would be 24 here) then you have to prove that your definition is well-defined.

#### [Kevin Buzzard (May 24 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017793):
and that's basically the same question, or another way of writing it, as far as I can see. Am I missing your point?

#### [Kevin Buzzard (May 24 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017798):
Oh -- or are you just talking about the (a+b)%m lemma?

#### [Chris Hughes (May 24 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017835):
The definition is just `quot.mk \circ fib`

#### [Kevin Buzzard (May 24 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017843):
Chris I'm talking about the input not the output

#### [Chris Hughes (May 24 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017845):
I'm talking about the mod 16 lemma

#### [Kevin Buzzard (May 24 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017847):
I can get fib : N -> N / 16 fine

#### [Kevin Buzzard (May 24 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017849):
But fib : (N / 24) -> N / 16 is less fine

#### [Kevin Buzzard (May 24 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017851):
what am I saying

#### [Kevin Buzzard (May 24 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017852):
what has happened to me

#### [Kevin Buzzard (May 24 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017853):
(Z  / 24)

#### [Chris Hughes (May 24 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017856):
Just do nat \r mod 16

#### [Kevin Buzzard (May 24 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017861):
what the hell is N mod 24

#### [Kevin Buzzard (May 24 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017865):
I understand how to build fib : N -> Z / 16

#### [Kevin Buzzard (May 24 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017867):
The issue is proving that fib (n + 24) = fib n

#### [Kevin Buzzard (May 24 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017879):
The only proof I know of that statement is

#### [Kevin Buzzard (May 24 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017911):
"consider n mod 24"

#### [Kevin Buzzard (May 24 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017914):
Oh

#### [Kevin Buzzard (May 24 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017918):
I realised I made a mistake above

#### [Kevin Buzzard (May 24 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017923):
I am going to edit a bunch of 16s and change them to 24s

#### [Kevin Buzzard (May 24 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017924):
input mod 24, output mod 16

#### [Kevin Buzzard (May 24 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017982):
OK fixed

#### [Kevin Buzzard (May 24 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017984):
So the issue is proving a = b mod 24 implies fib a = fib b mod 16

#### [Kevin Buzzard (May 24 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017986):
hmm

#### [Kevin Buzzard (May 24 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017987):
this is an idea

#### [Kevin Buzzard (May 24 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017993):
one can prove fib (n + 24) = fib n mod 16

#### [Kevin Buzzard (May 24 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017995):
by induction on n

#### [Kevin Buzzard (May 24 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017996):
and one has to hope that Lean has the firepower to compute fib 24

#### [Kevin Buzzard (May 24 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017998):
to get the induction started

#### [Kevin Buzzard (May 24 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127017999):
OK so

#### [Kevin Buzzard (May 24 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127018000):
actually

#### [Kevin Buzzard (May 24 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127018041):
one can define fibmod16

#### [Kevin Buzzard (May 24 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127018044):
I see

#### [Kevin Buzzard (May 24 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127018046):
fibmod16 : N -> Z/16

#### [Kevin Buzzard (May 24 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127018051):
then prove that forall n, fibmod16 (n + 24) = fibmod16 n by induction on n

#### [Kevin Buzzard (May 24 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127018052):
and now no firepower needed

#### [Kevin Buzzard (May 24 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127018055):
and now prove fib mod 16 is fibmod16 by induction on n

#### [Kevin Buzzard (May 24 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127018058):
and you're done!

#### [Kevin Buzzard (May 24 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127018063):
This is great!

#### [Kevin Buzzard (May 24 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127018064):
Thanks Chris!

#### [Kevin Buzzard (May 24 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127018068):
I could even make that discussion into 90 minutes, given that none of the kids will have seen Lean before

#### [Chris Hughes (May 24 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127018109):
induction, bases case `rfl`, next case unfold 24 times, and hope things simplify

#### [Kevin Buzzard (May 24 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127018162):
Yeah I think you've cracked it. Thanks Chris.

#### [Kevin Buzzard (May 24 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127018165):
Now get back to stats revision ;-)

#### [Kenny Lau (May 24 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127019961):
The correct way is to use the theorem I proved that day :P

#### [Kevin Buzzard (May 24 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020007):
Kenny

#### [Kevin Buzzard (May 24 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020008):
your comments are sometimes obscure

#### [Kevin Buzzard (May 24 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020010):
but "the theorem I proved that day" will take some beating

#### [Kevin Buzzard (May 24 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020011):
`(a%m+b%m)%m=(a+b)%m` is horrible

#### [Kenny Lau (May 24 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020012):
```lean
theorem to_be_named : fib (m + n + 1) =
  fib m * fib n + fib (m + 1) * fib (n + 1) :=
nat.strong_induction_on n $ λ n, nat.cases_on n (λ _, by simp [fib]) $ λ n,
nat.cases_on n (λ _, by simp [fib]) $ λ n ih,
have H1 : _ := ih n (nat.lt_trans (nat.lt_succ_self n) (nat.lt_succ_self (n+1))),
have H2 : fib (m + n + 2) = _ + _ * (fib n + fib (n+1)) := ih (n+1) (nat.lt_succ_self (n+1)),
calc  fib (m + n + 1) + fib (m + n + 2)
    = fib m * (fib n + fib (n+1)) + fib (m+1) * (fib (n+1) + (fib n + fib (n+1))) :
  by rw [H1, H2, mul_add, mul_add, mul_add, mul_add]; ac_refl
```

#### [Kenny Lau (May 24 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020013):
it's how it's done in proofwiki

#### [Kenny Lau (May 24 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020014):
this lemma, plus the fact that fib 16 and fib 17 are coprime

#### [Kevin Buzzard (May 24 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020019):
OK so I will now home in on the other part of your sentence

#### [Kevin Buzzard (May 24 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020020):
"The correct way"

#### [Kenny Lau (May 24 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020023):
it's more general

#### [Kenny Lau (May 24 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020025):
you can prove that fib m | fib n iff m | n

#### [Kevin Buzzard (May 24 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020027):
Oh so you're just talking about the correct way to do something random

#### [Kevin Buzzard (May 24 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020066):
I was rather hoping you were talking about the thing I was interested in :-)

#### [Kenny Lau (May 24 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020069):
m = 16?

#### [Kevin Buzzard (May 24 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020070):
Oh yeah!

#### [Kevin Buzzard (May 24 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020071):
Let's talk about that!

#### [Kenny Lau (May 24 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020072):
that's a special case lol

#### [Chris Hughes (May 24 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020073):
```quote
this lemma, plus the fact that fib 16 and fib 17 are coprime
```
Is this easy to prove, or are the numbers too big for lean to handle?

#### [Kevin Buzzard (May 24 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020075):
fib n is coprime to fib (n+1)

#### [Kenny Lau (May 24 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020076):
```quote
```quote
this lemma, plus the fact that fib 16 and fib 17 are coprime
```
Is this easy to prove, or are the numbers too big for lean to handle?
```
kevin already proved it

#### [Kevin Buzzard (May 24 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020079):
by Euclid's algorithm

#### [Kevin Buzzard (May 24 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020093):
I can't face `(a%m+a%m)%m=(a+b)%m`

#### [Kevin Buzzard (May 24 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020095):
I am going to work with Z/n

#### [Kevin Buzzard (May 24 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020096):
Where is this in Lean?

#### [Kevin Buzzard (May 24 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020097):
I currently have

#### [Kevin Buzzard (May 24 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020120):
```lean
definition fib_mod (m : ℕ) : ℕ → ℕ 
| 0 := 0 % m
| 1 := 1 % m
| (n + 2) := ( (fib_mod n) + (fib_mod (n + 1)) ) % m
```

#### [Kevin Buzzard (May 24 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020145):
but I am going to go for a map from N to whatever Z/nZ is called

#### [Kevin Buzzard (May 24 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020146):
as long as it's an abelian group

#### [Chris Hughes (May 24 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020151):
https://github.com/dorhinj/leanstuff/blob/master/Zmod1.lean I did it.

#### [Kevin Buzzard (May 24 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020155):
oh so it's not in Lean?

#### [Chris Hughes (May 24 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020157):
No.

#### [Kevin Buzzard (May 24 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020159):
I mean mathlib

#### [Kevin Buzzard (May 24 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020163):
OK

#### [Kevin Buzzard (May 24 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020164):
I will steal it

#### [Kevin Buzzard (May 24 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020166):
you only did Z mod 1?

#### [Chris Hughes (May 24 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020209):
The 1 is to distinguish it from another construction I did.

#### [Kevin Buzzard (May 24 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020212):
Oh OK :-)

#### [Kevin Buzzard (May 24 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020214):
That's a relief

#### [Kevin Buzzard (May 24 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020215):
I was hoping for Zmod16

#### [Kevin Buzzard (May 24 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020223):
wow

#### [Kevin Buzzard (May 24 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020224):
https://github.com/dorhinj/leanstuff

#### [Kevin Buzzard (May 24 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020226):
you have been pretty productive in the last 16 hours

#### [Kevin Buzzard (May 24 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020229):
about 50 lean files commited

#### [Kenny Lau (May 24 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020230):
lol

#### [Kevin Buzzard (May 24 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020270):
it's Chrislib

#### [Kevin Buzzard (May 24 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020275):
I like the look of kbuzzard.lean

#### [Kevin Buzzard (May 24 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020277):
Is that one of my theorems?

#### [Kevin Buzzard (May 24 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020279):
something about modular forms maybe?

#### [Kevin Buzzard (May 24 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020282):
Actually, hopefully, one of my theorems really _will_ be in Lean soon

#### [Kevin Buzzard (May 24 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020286):
Ellen is going to formalize my dots and boxes paper

#### [Kevin Buzzard (May 24 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020520):
If Z mod n isn't in mathlib and requires a bunch of Chris' local imports it might be easier to just go for `def nat.mod_add (a b m : ℕ) : (a % m + b % m) % m = (a + b) % m := sorry`

#### [Kevin Buzzard (May 24 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020524):
I am not enough of an expert in how to use `%` to see how to prove this

#### [Kevin Buzzard (May 24 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020525):
and it doesn't appear to be there already

#### [Kevin Buzzard (May 24 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020532):
KB <- professional number theorist who is not an expert in mod

#### [Kevin Buzzard (May 24 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020535):
:-/

#### [Kevin Buzzard (May 24 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020583):
I added the sorried assertion to https://github.com/kbuzzard/lean-squares-in-fibonacci/blob/master/src/definitions.lean

#### [Chris Hughes (May 24 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020647):
```lean
@[simp] lemma nat.mod_mod (n m : ℕ) : n % m % m = n % m := 
nat.cases_on m (by simp) (λ m, mod_eq_of_lt (mod_lt _ (succ_pos _)))

def nat.mod_add (a b m : ℕ) : (a % m + b % m) % m = (a + b) % m :=
nat.modeq.modeq_add (nat.mod_mod _ _) (nat.mod_mod _ _)
```

#### [Patrick Massot (May 24 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020695):
This is becoming slightly creepy

#### [Patrick Massot (May 24 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020697):
Kevin, what have you created?

#### [Kenny Lau (May 24 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020775):
```lean
import definitions

theorem fib_add (m n : ℕ) : fib (m + n + 1) =
  fib m * fib n + fib (m + 1) * fib (n + 1) :=
nat.rec_on_two n (by unfold fib; rw [mul_zero, zero_add, mul_one]; refl)
  (by unfold fib; rw [zero_add, mul_one, mul_one]; refl) $ λ n ih1 ih2,
calc  fib (m + n + 1) + fib (m + nat.succ n + 1)
    = fib m * (fib n + fib (n+1)) + fib (m+1) * (fib (n+1) + (fib n + fib (n+1))) :
  by rw [ih1, ih2, fib, mul_add, mul_add, mul_add, mul_add, nat.succ_eq_add_one]; ac_refl

attribute [refl] dvd_refl
attribute [trans] dvd_trans

theorem fib_dvd_mul (m n : ℕ) : fib m ∣ fib (m * n) :=
nat.cases_on m (by rw [zero_mul]; refl) $ λ m,
nat.rec_on n (dvd_zero _) $ λ n ih,
show fib (nat.succ m) ∣ fib (nat.succ m * n + m + 1),
by rw [fib_add]; apply dvd_add;
[apply dvd_mul_of_dvd_left ih, apply dvd_mul_left]
```

#### [Kenny Lau (May 24 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020776):
done

#### [Kenny Lau (May 24 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020778):
I don't need the fact that fib m and fib m+1 are coprime

#### [Kenny Lau (May 24 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020816):
I would need it to prove the converse though

#### [Kevin Buzzard (May 24 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020843):
```quote
Kevin, what have you created?
```
This is the new normal. Professors who can't prove things about mod so they ask the undergraduates

#### [Kevin Buzzard (May 24 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020886):
I really want that by December there are a bunch of undergraduates at my university asking their tutors questions which the tutors can't answer

#### [Kevin Buzzard (May 24 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020888):
or showing them code which the tutors can't understand

#### [Kevin Buzzard (May 24 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020892):
or saying "I typed up your problem sheet into Lean and you made an off by one error"

#### [Kenny Lau (May 24 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020894):
pushed

#### [Kevin Buzzard (May 24 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020895):
Thanks Kenny

#### [Kevin Buzzard (May 24 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020903):
I need a recursor for %

#### [Kevin Buzzard (May 24 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020913):
If I have a function F from nat to X

#### [Kevin Buzzard (May 24 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020915):
and a proof that F (n +  24) = F n

#### [Kevin Buzzard (May 24 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020917):
then I want a theorem that F n = F (n % 24)

#### [Kevin Buzzard (May 24 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020919):
Is that a recursor?

#### [Kevin Buzzard (May 24 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020920):
It's what I want, at any rate

#### [Kenny Lau (May 24 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020961):
ok a minute

#### [Kevin Buzzard (May 24 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020962):
what I don't want

#### [Kevin Buzzard (May 24 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020963):
is what I have to do

#### [Kevin Buzzard (May 24 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020964):
which is marking 150 scripts about sup S

#### [Kevin Buzzard (May 24 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020965):
I think I need to go offline for 7 hours

#### [Kevin Buzzard (May 24 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020966):
I will push too

#### [Kevin Buzzard (May 24 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020986):
Before I go

#### [Kevin Buzzard (May 24 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020987):
just let me make one thing clear to Kenny and Chris

#### [Kevin Buzzard (May 24 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127020988):
Last night I was a bit worried about all this

#### [Kevin Buzzard (May 24 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127021000):
because I still have 10 hours of marking and I wanted to give a good talk on Sat

#### [Kevin Buzzard (May 24 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127021035):
but now I know I have enough material to give a good talk

#### [Kevin Buzzard (May 24 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127021039):
so feel free to stop thinking about this and worry about your stats exam

#### [Kevin Buzzard (May 24 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127021042):
and come back to it on Friday

#### [Kevin Buzzard (May 24 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127021046):
I will be at Xena tonight by the way, from 6pm

#### [Kevin Buzzard (May 24 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127021053):
Thanks to all of you, as ever

#### [Kenny Lau (May 24 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127021167):
```lean
lemma nat.mod_rec (m n : ℕ) {C : ℕ → Sort*}
  (H : ∀ n, C n = C (n+m)) :
  C n = C (n%m) :=
have H1 : ∀ q r, C (r + m * q) = C r,
  from λ q, nat.rec_on q (λ r, by rw [mul_zero]; refl) $ λ n ih r,
    by rw [mul_succ, ← add_assoc, ← H, ih],
by conv in (C n) { rw [← mod_add_div n m, H1] }
```

#### [Kenny Lau (May 24 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127024645):
```lean
theorem fib_gcd (m : ℕ) : ∀ n, nat.gcd (fib m) (fib n) = fib (nat.gcd m n) :=
[thing that works]
```

#### [Kenny Lau (May 24 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127024647):
pushed

#### [Kenny Lau (May 24 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127025051):
pushed

#### [Kenny Lau (May 24 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127025052):
i'm going to eat and then revise statistics until tonight

#### [Kevin Buzzard (May 26 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127122627):
What is the prettiest way to prove that there's a positive real number alpha with the property that `alpha ^ 2 = alpha + 1`?

#### [Kenny Lau (May 26 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127122630):
not to.

#### [Kenny Lau (May 26 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127122632):
(why can't we just use the Zalpha)

#### [Kevin Buzzard (May 26 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127122664):
I would be really interested in an answer to this question before 2000 BST and ideally earlier

#### [Kevin Buzzard (May 26 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127122672):
Kenny I am giving a talk to a bunch of schoolkids

#### [Kevin Buzzard (May 26 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127122674):
I am going to give two talks

#### [Mario Carneiro (May 26 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127122675):
square root, or FTA

#### [Kevin Buzzard (May 26 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127122676):
In the first talk I will ask them to prove to me that alpha exists and I'll see what they come up with.

#### [Kevin Buzzard (May 26 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127122677):
In the second talk I will show them how Lean does it

#### [Kevin Buzzard (May 26 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127122678):
But I want it to look really sexy

#### [Mario Carneiro (May 26 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127122683):
IVT works too

#### [Kevin Buzzard (May 26 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127122687):
I want to define a real number alpha as $$(1+5^{(1/2)})/2$$ or something that looks as close to that as possible

#### [Mario Carneiro (May 26 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127122689):
then use sqrt thm

#### [Kevin Buzzard (May 26 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127122730):
I would like a square root symbol ideally. Is there one of them?

#### [Kevin Buzzard (May 26 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127122731):
Oh I saw one in Pell maybe?

#### [Mario Carneiro (May 26 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127122732):
I thought we did this a few months ago

#### [Kevin Buzzard (May 26 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127122733):
I know how to solve it

#### [Kevin Buzzard (May 26 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127122734):
I just want to make it look maximally sexy

#### [Kevin Buzzard (May 26 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127122735):
I want to write a human-readable proof

#### [Mario Carneiro (May 26 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127122741):
I think it is `\surd`

#### [Mario Carneiro (May 26 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127122742):
it is in pell

#### [Kevin Buzzard (May 26 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127122781):
i.e. something where you show the exact proof to a smart schoolkid and whilst they don't know any of the precise syntax they can still kind of see that it's a proof that if alpha is (1+sqrt(5))/2 then alpha^2=alpha+1.

#### [Kevin Buzzard (May 26 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127122784):
I'll see what I can come up with

#### [Kevin Buzzard (May 26 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127122836):
I fear becoming mired in div_muls and mul_adds when expanding everything out

#### [Mario Carneiro (May 26 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127122842):
complete the square

#### [Mario Carneiro (May 26 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127122843):
using ring

#### [Kevin Buzzard (May 26 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128227):
`theorem root_5_squared : (sqrt 5) ^ 2 = 5 := by norm_num -- fails`

#### [Kevin Buzzard (May 26 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128228):
Why can't it be easy

#### [Kevin Buzzard (May 26 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128229):
`theorem root_5_squared : (sqrt 5) ^ 2 = 5 := by simp [(sqrt_prop 5).2] -- fails`

#### [Kevin Buzzard (May 26 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128230):
I am so bad at reals

#### [Kevin Buzzard (May 26 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128231):
`#check sqrt_prop -- ∀ (x : ℝ), 0 ≤ sqrt x ∧ sqrt x * sqrt x = max 0 x`

#### [Mario Carneiro (May 26 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128284):
you want `sqr_sqrt`

#### [Mario Carneiro (May 26 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128287):
it's already a simp lemma, so you just have to supply a proof of `0 <= 5`

#### [Kevin Buzzard (May 26 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128291):
why do I need to supply a proof of that?

#### [Kevin Buzzard (May 26 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128293):
It's clear it will yield to norm_num right?

#### [Kevin Buzzard (May 26 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128298):
Can I somehow add norm_num to simp?

#### [Mario Carneiro (May 26 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128301):
sure, but norm_num and simp don't talk back and forth like that

#### [Kevin Buzzard (May 26 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128304):
I am still a million miles away from writing a clear readable statement and proof that if alpha = (1+sqrt(5))/2 then alpha^2=alpha+1

#### [Kevin Buzzard (May 26 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128305):
I will keep trying

#### [Mario Carneiro (May 26 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128314):
norm_num doesn't know about square roots, and simp doesn't use norm_num as a discharger

#### [Mario Carneiro (May 26 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128351):
you could try `simp {discharger := norm_num}`, not sure if that works

#### [Kevin Buzzard (May 26 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128356):
completely unrelated -- why do I have `imported file '/home/buzzard/lean-projects/lean-squares-in-fibonacci/_target/deps/mathlib/data/set/lattice.lean' uses sorry` and several other mathlib errors? This looks really unprofessional :-/ Can you tell me a quick fix?

#### [Mario Carneiro (May 26 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128357):
still, I think `simp (dec_trivial : 0 <= 5)` is easy enough

#### [Kevin Buzzard (May 26 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128362):
That's enough? It goes from nats to reals?

#### [Mario Carneiro (May 26 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128368):
Oh wait no, le on real is not computable

#### [Mario Carneiro (May 26 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128371):
you need to use norm_num

#### [Mario Carneiro (May 26 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128372):
`simp [(by norm_num : 0 <= 5)]`

#### [Kevin Buzzard (May 26 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128412):
I don't understand what you are saying

#### [Kevin Buzzard (May 26 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128413):
I don't understand this stuff well enough

#### [Kevin Buzzard (May 26 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128414):
`theorem root_5_squared : (sqrt 5) ^ 2 = 5 := by simp [sqr_sqrt,(dec_trivial : 0 <= 5)]-- fails`

#### [Kevin Buzzard (May 26 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128416):
I am not even sure that's valid syntax

#### [Mario Carneiro (May 26 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128418):
it should be...

#### [Mario Carneiro (May 26 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128424):
the full proof is just `sqr_sqrt (by norm_num : 0 <= 5)`

#### [Kevin Buzzard (May 26 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128472):
```lean

theorem zero_le_5 : (0 : ℝ) ≤ 5 := by norm_num

theorem root_5_squared : (sqrt 5) ^ 2 = 5 := by simp [sqr_sqrt,zero_le_5]
```

#### [Kevin Buzzard (May 26 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128473):
First molehill conquered

#### [Mario Carneiro (May 26 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128475):
Oh, you might need to write `simp [(by norm_num : (0:R) <= 5)]`

#### [Kevin Buzzard (May 26 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128477):
Where?

#### [Mario Carneiro (May 26 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128478):
as a proof of the theorem

#### [Mario Carneiro (May 26 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128485):
that proves zero_le_5 inline, and uses it as a simp lemma in the main proof

#### [Kevin Buzzard (May 26 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128534):
It's really annoying to use Lean like this. Why do I have all these errors in mathlib?

#### [Kevin Buzzard (May 26 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128535):
```
imported file '/home/buzzard/lean-projects/lean-squares-in-fibonacci/_target/deps/mathlib/order/complete_lattice.lean' uses sorry
real_alpha.lean:1:0: warning

imported file '/home/buzzard/lean-projects/lean-squares-in-fibonacci/_target/deps/mathlib/order/bounded_lattice.lean' uses sorry
real_alpha.lean:1:0: warning

imported file '/home/buzzard/lean-projects/lean-squares-in-fibonacci/_target/deps/mathlib/data/finset.lean' uses sorry
real_alpha.lean:1:0: warning

imported file '/home/buzzard/lean-projects/lean-squares-in-fibonacci/_target/deps/mathlib/order/boolean_algebra.lean' uses sorry
real_alpha.lean:1:0: warning

imported file '/home/buzzard/lean-projects/lean-squares-in-fibonacci/_target/deps/mathlib/data/equiv.lean' uses sorry
real_alpha.lean:1:0: warning

imported file '/home/buzzard/lean-projects/lean-squares-in-fibonacci/_target/deps/mathlib/data/set/lattice.lean' uses sorry

```

#### [Kevin Buzzard (May 26 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128536):
What have I done wrong?

#### [Mario Carneiro (May 26 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128537):
maybe those files use sorry

#### [Kevin Buzzard (May 26 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128540):
I thought I was all up to date

#### [Kevin Buzzard (May 26 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128543):
They're all your files

#### [Mario Carneiro (May 26 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128546):
Look for an actual error

#### [Mario Carneiro (May 26 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128588):
Usually lean will have some error in a theorem, and then since the theorem failed it uses sorry instead, and then every other file that imports that file complains about the sorry so you get hundreds of sorry warnings

#### [Kevin Buzzard (May 26 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128593):
```
complete_lattice.lean:119:36: error

ambiguous overload, possible interpretations
  ⊥
  ⊥
Additional information:
/home/buzzard/lean-projects/lean-squares-in-fibonacci/_target/deps/mathlib/order/complete_lattice.lean:119:36: context: switched to basic overload resolution where arguments are elaborated without any information about the expected type because it failed to disambiguate overload using the expected type
  ?m_1
the following overloaded terms were applicable
  ⊥
  ⊥

#### [Kevin Buzzard (May 26 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128601):
Looks like much of a muchness to me

#### [Kevin Buzzard (May 26 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128609):
```
don't know how to synthesize placeholder
context:
α : Type u,
_inst_1 : lattice.complete_lattice.{u} α
⊢ Type ?l_1
complete_lattice.lean:120:36: error

ambiguous overload, possible interpretations
  @lattice.has_bot.bot.{?l_1} ?m_2 ?m_3
  @lattice.has_bot.bot.{?l_4} ?m_5 ?m_6
Additional information:
/home/buzzard/lean-projects/lean-squares-in-fibonacci/_target/deps/mathlib/order/complete_lattice.lean:120:36: context: switched to basic overload resolution where arguments are elaborated without any information about the expected type because it failed to disambiguate overload using the expected type
  ?m_1
the following overloaded terms were applicable
  @lattice.has_bot.bot.{?l_2} ?m_3 ?m_4
  @lattice.has_bot.bot.{?l_5} ?m_6 ?m_7
```

#### [Kevin Buzzard (May 26 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128647):
with pp_all on

#### [Mario Carneiro (May 26 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128651):
what about `#print ⊥`?

#### [Kevin Buzzard (May 26 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128657):
```
`⊥`:1024 :=
  | lattice.has_bot.bot _
  | lattice.has_bot.bot _
```

#### [Mario Carneiro (May 26 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128661):
some file somewhere has declared ⊥ as a global notation

#### [Kevin Buzzard (May 26 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128662):
Thanks

#### [Mario Carneiro (May 26 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128664):
I recently moved the location of the declaration of ⊥

#### [Mario Carneiro (May 26 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128704):
it's possible you have an old version of one of the files and so are getting a double declaration

#### [Kevin Buzzard (May 26 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128707):
Thanks

#### [Kevin Buzzard (May 26 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128708):
I can't see any of these symbols or bot in my file

#### [Mario Carneiro (May 26 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128712):
check lattice.lean

#### [Kevin Buzzard (May 26 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128720):
```
:~/lean-projects/lean-squares-in-fibonacci/_target/deps/mathlib$ git branch
* (HEAD detached at 6811f13)
  master
```

#### [Kevin Buzzard (May 26 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128721):
I don't know what detached head means

#### [Mario Carneiro (May 26 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128722):
or just search for ``notation `⊥` ``

#### [Kevin Buzzard (May 26 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128723):
Should I switch to master?

#### [Mario Carneiro (May 26 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128725):
it means you have a commit checked out, not a branch

#### [Mario Carneiro (May 26 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128771):
what does `git status` give?

#### [Kevin Buzzard (May 26 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128773):
That sounds right

#### [Kevin Buzzard (May 26 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128774):
shall I checkout a branch?

#### [Kevin Buzzard (May 26 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128775):
I did everything with leanpkg as far as I know

#### [Mario Carneiro (May 26 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128786):
leanpkg usually checks out commits, which is why it is like that

#### [Kevin Buzzard (May 26 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128790):
```
$ git status
HEAD detached at 6811f13
nothing to commit, working directory clean
```

#### [Kevin Buzzard (May 26 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128793):
Instead of trying to debug

#### [Kevin Buzzard (May 26 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128795):
can you just tell me how to install the latest mathlib and get it all working?

#### [Mario Carneiro (May 26 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128845):
You appear to have it already, from that status message

#### [Kevin Buzzard (May 26 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128848):
Is there just a brutal fix so I have a working version of mathlib? Should I just delete _target and run leanpkg something?

#### [Kevin Buzzard (May 26 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128852):
Or check out some other commit or branch?

#### [Kevin Buzzard (May 26 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128860):
I just want to get this fixed quickly, I am giving a talk in an hour

#### [Mario Carneiro (May 26 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128861):
yes probably, but I'm not a leanpkg expert

#### [Kevin Buzzard (May 26 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128865):
and then another one at 8 where I want to show Lean off

#### [Kevin Buzzard (May 26 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128866):
and all its erros

#### [Kevin Buzzard (May 26 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128867):
errors

#### [Mario Carneiro (May 26 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128870):
maybe back up the directory first, but sure just remove _target and do the usual leanpkg incantations

#### [Mario Carneiro (May 26 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128910):
that folder only has cached stuff so it should be fine

#### [Kevin Buzzard (May 26 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128914):
I'm on a train :-/

#### [Mario Carneiro (May 26 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128921):
try removing .olean files

#### [Mario Carneiro (May 26 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128922):
and rebuild

#### [Kevin Buzzard (May 26 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128924):
i did that already

#### [Mario Carneiro (May 26 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128928):
did you search for notation bot like I said?

#### [Kevin Buzzard (May 26 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128964):
git is working

#### [Kevin Buzzard (May 26 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128966):
really good

#### [Kevin Buzzard (May 26 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128974):
patchy 3g phone and hotspot

#### [Mario Carneiro (May 26 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128975):
this line
```
notation `⊥` := has_bot.bot _
```
should appear exactly once in mathlib, in bounded_lattice.lean

#### [Kevin Buzzard (May 26 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128978):
I got bored trying to work out why it was broken

#### [Kevin Buzzard (May 26 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128983):
I am under time pressure

#### [Mario Carneiro (May 26 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128984):
I'm hoping that the location of the second hit will hint at why you have old files

#### [Kevin Buzzard (May 26 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127128986):
had

#### [Mario Carneiro (May 26 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129032):
that's why I'm giving suggestions that are fast to check

#### [Kevin Buzzard (May 26 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129094):
```quote
you could try `simp {discharger := norm_num}`, not sure if that works
```
I can't get it to work

#### [Chris Hughes (May 26 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129100):
How about this for a readable proof?
```lean
example : (((1 : ℝ) + √5) / 2) ^ 2 = ((1 : ℝ) + √5 ) / 2 + 1 := 
have h : (0 : ℝ) ≤ 5 := by norm_num,
begin
  rw [pow_two, div_mul_div, mul_add, mul_one, add_mul, one_mul, ← pow_two, sqr_sqrt h],
  ring,
end
```

#### [Kevin Buzzard (May 26 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129103):
```lean
import analysis.real tactic.norm_num tactic.ring

namespace real 
noncomputable theory 

def α := (real.sqrt 5 + 1) / 2
def β := 1 - α 

theorem root_5_squared : (sqrt 5) ^ 2 = 5 := by simp [sqr_sqrt,(by norm_num : (0:ℝ) <= 5)]

lemma αβsum : α + β = 1 := begin
  unfold β,
  unfold α,
  norm_num, -- ;-)
end 

lemma αβprod : α * β = -1 := begin
  unfold β,
  unfold α,
  rw [mul_sub,mul_one,add_div,mul_add,add_mul,add_mul], -- meh 
  simp [root_5_squared],
  norm_num, -- unknown exception while type-checking theorem 
end
```

#### [Kevin Buzzard (May 26 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129106):
I got an achievement -- "unknown exception while type-checking theorem"

#### [Kevin Buzzard (May 26 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129150):
Why isn't this easy

#### [Kevin Buzzard (May 26 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129151):
simp wants facts from norm_num but I don't know what facts

#### [Kevin Buzzard (May 26 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129153):
goal after simp is

#### [Kevin Buzzard (May 26 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129154):
```lean
⊢ 2⁻¹ +
      (sqrt 5 / 2 +
         (-(2⁻¹ * 2⁻¹) + (-(2⁻¹ * (sqrt 5 / 2)) + (-(sqrt 5 / 2 * 2⁻¹) + -(sqrt 5 / 2 * (sqrt 5 / 2)))))) =
    -1
```

#### [Kevin Buzzard (May 26 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129155):
I must have taken a wrong turn

#### [Kevin Buzzard (May 26 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129162):
I am not a competent driver when it comes to the reals

#### [Mario Carneiro (May 26 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129164):
simp on its own will not know how to finish the job

#### [Mario Carneiro (May 26 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129165):
you need `ring` for all that

#### [Kevin Buzzard (May 26 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129166):
All I want to do is prove that if alpha is (1+sqrt(5))/2 then alpha^2=alpha+1

#### [Kevin Buzzard (May 26 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129204):
in R

#### [Kevin Buzzard (May 26 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129208):
because if that's not easy

#### [Kevin Buzzard (May 26 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129209):
then what kind of an R have you got here

#### [Kevin Buzzard (May 26 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129211):
a computer scientist's one but not a mathematican's one

#### [Kevin Buzzard (May 26 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129219):
I completely understand the other approach

#### [Kevin Buzzard (May 26 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129222):
but for pedagogical reasons I would like to see this happening in R

#### [Kevin Buzzard (May 26 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129224):
I can always fall back on Nicholas' construction

#### [Kevin Buzzard (May 26 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129226):
which indeed I will ultimately fall back on

#### [Kevin Buzzard (May 26 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129266):
but my goal was not to explain how incredibly difficult it was to even the most trivial things

#### [Mario Carneiro (May 26 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129267):
I get it

#### [Mario Carneiro (May 26 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129269):
1 sec

#### [Kevin Buzzard (May 26 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129270):
Sorry to moan

#### [Kevin Buzzard (May 26 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129271):
I am giving an important talk

#### [Kevin Buzzard (May 26 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129275):
and I want it to be _really good_

#### [Mario Carneiro (May 26 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129280):
I believe it can be done with a short tactic invoke

#### [Kevin Buzzard (May 26 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129281):
so I want to make a really professional job of it

#### [Mario Carneiro (May 26 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129285):
I think you can use `ring` to get it down to an expression involving `(sqrt 5)^2`, and then use `simp` and `norm_num` to finish

#### [Kevin Buzzard (May 26 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129351):
Removed target and re-installed everything and I'm back up to speed :-)

#### [Kevin Buzzard (May 26 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129352):
one further step towards professional

#### [Kevin Buzzard (May 26 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129353):
No more errors

#### [Kevin Buzzard (May 26 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129390):
aargh that's a lie

#### [Kevin Buzzard (May 26 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129400):
I will sort this out later -- I've got until 8pm

#### [Mario Carneiro (May 26 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129403):
what time is it now?

#### [Kenny Lau (May 26 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129404):
```quote
I will sort this out later -- I've got until 8pm
```
what do you need to sort out?

#### [Kevin Buzzard (May 26 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129448):
I have loads of errors in mathlib

#### [Kevin Buzzard (May 26 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129450):
I've tried everything

#### [Kevin Buzzard (May 26 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129451):
I might reboot my computer

#### [Kevin Buzzard (May 26 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129452):
and recompile all .olean files

#### [Kenny Lau (May 26 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129453):
are you trying to prove anything?

#### [Kevin Buzzard (May 26 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129454):
but that's all I can think of

#### [Kevin Buzzard (May 26 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129457):
I'm tyring to prove that two real numbers are equal

#### [Kevin Buzzard (May 26 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129460):
I'll push

#### [Kevin Buzzard (May 26 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129502):
https://github.com/kbuzzard/lean-squares-in-fibonacci/blob/master/src/real_alpha.lean

#### [Kevin Buzzard (May 26 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129504):
But I want it to look sexy

#### [Mario Carneiro (May 26 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129512):
you could import `data.real.basic` instead

#### [Mario Carneiro (May 26 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129776):
```
import data.real.basic tactic.norm_num tactic.ring

open real 
noncomputable theory 

prefix `√`:90 := sqrt

def α := (√5 + 1) / 2
def β := 1 - α 

theorem root_5_squared : √5 ^ 2 = 5 :=
by simp {discharger := `[norm_num]}

lemma αβsum : α + β = 1 := begin
  unfold α β,
  ring
end 

lemma αβprod : α * β = -1 := begin
  unfold α β,
  ring,
  simp {discharger := `[norm_num]},
  ring
end
```

#### [Kenny Lau (May 26 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129779):
what

#### [Kenny Lau (May 26 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129879):
```lean
import data.real.basic tactic.norm_num

noncomputable theory 

prefix `√`:90 := real.sqrt

def α := (1 + √5) / 2
def β := 1 - α 

theorem root_5_squared : √5 * √5 = 5 :=
real.mul_self_sqrt $ show (0:ℝ) ≤ 5, by norm_num

lemma αβsum : α + β = 1 :=
show α + (1 - α) = 1,
from add_sub_cancel'_right α 1

lemma αβprod : α * β = -1 :=
calc  α * β
    = ((1 + √5) / 2) * (1 - (1 + √5) / 2) : rfl
... = ((1 + √5) / 2) * ((1 + 1) / 2 - (1 + √5) / 2) : by rw add_self_div_two
... = ((1 + √5) / 2) * (((1 + 1) - (1 + √5)) / 2) : by rw div_sub_div_same
... = ((1 + √5) / 2) * ((1 - √5) / 2) : by rw add_sub_add_left_eq_sub
... = ((1 + √5) * (1 - √5)) / (2 * 2) : by rw div_mul_div
... = (1 * 1 - √5 * √5) / (2 * 2) : by rw mul_self_sub_mul_self_eq
... = (1 * 1 - 5) / (2 * 2) : by rw root_5_squared
... = -1 : by norm_num
```

#### [Kenny Lau (May 26 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129880):
@**Kevin Buzzard** do you like direct proofs?

#### [Mario Carneiro (May 26 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129922):
You could also half-cheat and write a plausible-looking sequence of equalities all proven by `ring`

#### [Kenny Lau (May 26 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129927):
but that defeats the purpose of the presentation

#### [Kevin Buzzard (May 26 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129928):
This is somehow awful

#### [Mario Carneiro (May 26 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129929):
it makes it look nice and readable

#### [Kevin Buzzard (May 26 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129930):
but it's much better than nothing

#### [Kevin Buzzard (May 26 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129932):
But I don't want it to be readable

#### [Kevin Buzzard (May 26 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129933):
I want it to be trivial

#### [Kenny Lau (May 26 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129934):
what

#### [Kevin Buzzard (May 26 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129935):
An obscure one-liner?

#### [Mario Carneiro (May 26 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129936):
you didn't like my ring solution?

#### [Kenny Lau (May 26 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129937):
I thought you're teaching rigour

#### [Kenny Lau (May 26 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129942):
if you asked me in m1f to prove that alpha * beta = -1, that is exactly what I would write down

#### [Kenny Lau (May 26 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129944):
minus the `by rw ...` things

#### [Kevin Buzzard (May 26 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129945):
I don't understand -- what ring solution?

#### [Kenny Lau (May 26 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129947):
https://leanprover.zulipchat.com/#narrow/stream/116395-maths/subject/Largest.20Square.20in.20the.20Fibonacci.20Sequence/near/127129776

#### [Kenny Lau (May 26 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127129951):
:D

#### [Kenny Lau (May 26 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127130004):
I can't delete my own messages...

#### [Kevin Buzzard (May 26 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127130016):
I want as many solutions as I can

#### [Kevin Buzzard (May 26 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127130024):
And we vote for the most beautiful

#### [Kenny Lau (May 26 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127130026):
beauty is in the eye of the beholder

#### [Kenny Lau (May 26 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127130027):
in this case, you

#### [Kenny Lau (May 26 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127130032):
it's you who is/are presenting

#### [Mario Carneiro (May 26 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127130082):
semi-explicit, only one `ring`
```
lemma αβprod : α * β = -1 := begin
  unfold α β,
  ring,
  rw sqr_sqrt; norm_num
end
```

#### [Kenny Lau (May 26 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127130090):
I still don't know what @**Kevin Buzzard** wants

#### [Kenny Lau (May 26 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127130092):
what is the goal of this?

#### [Reid Barton (May 26 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127130208):
or an intermediate one, still using calc
```lean
lemma αβsum : α + β = 1 := by dsimp [β]; ring

lemma αβprod : α * β = -1 :=
calc  α * β
    = ((1 + √5) / 2) * (1 - (1 + √5) / 2) : rfl
... = (1 * 1 - √5^2) / (2 * 2) : by ring
... = -1 : by rw real.sqr_sqrt; norm_num
```

#### [Mario Carneiro (May 26 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127130231):
I guess you could write the middle line as `(1 - √5^2) / 4` for extra clean

#### [Kenny Lau (May 26 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127130235):
low-tech one-liners:

#### [Kenny Lau (May 26 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127130237):
```lean
import data.real.basic tactic.norm_num

noncomputable theory 

prefix `√`:90 := real.sqrt

def α := (1 + √5) / 2
def β := (1 - √5) / 2

theorem root_5_squared : √5 * √5 = 5 :=
real.mul_self_sqrt $ show (0:ℝ) ≤ 5, by norm_num

lemma αβsum : α + β = 1 :=
by rw [α, β, ← add_div]; simp

lemma αβprod : α * β = -1 :=
by rw [α, β, div_mul_div, ← mul_self_sub_mul_self_eq, root_5_squared]; norm_num
```

#### [Kenny Lau (May 26 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127130280):
(is changing the definition allowed?)

#### [Mario Carneiro (May 26 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127130356):
```
lemma αβprod : α * β = -1 :=
calc ((√5 + 1) / 2) * (1 - (√5 + 1) / 2)
    = (1 - √5^2) / 4 : by ring
... = -1 : by rw sqr_sqrt; norm_num
```

#### [Kenny Lau (May 26 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127130362):
not very different from the one above...

#### [Mario Carneiro (May 26 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127130365):
it's based on reid's

#### [Kenny Lau (May 26 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127130416):
```lean
import data.real.basic tactic.norm_num

noncomputable theory 

prefix `√`:90 := real.sqrt

def α := (1 + √5) / 2
def β := (1 - √5) / 2

lemma sqrt_5_mul_self : √5 * √5 = 5 :=
real.mul_self_sqrt $ show (0:ℝ) ≤ 5, by norm_num

lemma αβsum : α + β = 1 :=
by simp [α, β, add_div, neg_div, -one_div_eq_inv]

lemma αβprod : α * β = -1 :=
by simp [α, β, div_mul_div, add_mul, mul_add, sqrt_5_mul_self]; norm_num
```

#### [Reid Barton (May 26 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127130417):
And I just took Kenny's long calc and deleted all the intermediate steps that could be handled by `ring`.

#### [Reid Barton (May 26 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127130427):
I like calc here because the fact `α * β = -1` is actually not immediately obvious to a human, and you'd write out about the same number of intermediate steps to explain the calculation to a human.

#### [Kenny Lau (May 26 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127130428):
still avoiding ring as usual :P

#### [Kenny Lau (May 26 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127130429):
I like my new definition

#### [Kenny Lau (May 26 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127130466):
who likes my new definition

#### [Mario Carneiro (May 26 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127130472):
I think your definition is nicer if you are going to define both alpha and beta

#### [Mario Carneiro (May 26 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127130485):
In a human proof I would probably have an additional step in the middle with all four terms and cross out the cross terms

#### [Kenny Lau (May 26 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127130527):
that's what I did with the `add_mul` and `mul_add`

#### [Kenny Lau (May 26 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127130532):
```lean
import data.real.basic tactic.norm_num

noncomputable theory 

prefix `√`:90 := real.sqrt

def α := (1 + √5) / 2
def β := (1 - √5) / 2

lemma sqrt_5_mul_self : √5 * √5 = 5 :=
real.mul_self_sqrt $ show (0:ℝ) ≤ 5, by norm_num1

lemma αβsum : α + β = 1 :=
by simp [α, β, add_div, neg_div, -one_div_eq_inv]

lemma αβprod : α * β = -1 :=
by simp [α, β, div_mul_div, add_mul, mul_add, sqrt_5_mul_self]; norm_num1
```

#### [Kenny Lau (May 26 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127130535):
low-tech :P

#### [Mario Carneiro (May 26 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127130536):
A long `rw` proof is hard to read though

#### [Mario Carneiro (May 26 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127130537):
unless you step through it

#### [Kenny Lau (May 26 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127130542):
I thought @**Kevin Buzzard** wants a one-liner

#### [Mario Carneiro (May 26 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127130543):
and you can't even do that for a simp proof

#### [Mario Carneiro (May 26 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127130544):
I think we have that already

#### [Mario Carneiro (May 26 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127130552):
```
lemma αβprod : α * β = -1 :=
by unfold α β; ring; simp {discharger := `[norm_num]}; ring
```

#### [Mario Carneiro (May 26 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127130655):
ooh, with this modification to `norm_num`:
```
meta def norm_num (loc : parse location) : tactic unit :=
let t := orelse' (norm_num1 loc) $
  simp_core {} (norm_num1 (interactive.loc.ns [none])) ff [] [] loc in
t >> repeat t
```
you can get away with just `by unfold α β; ring; norm_num`

#### [Kevin Buzzard (May 26 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127130933):
I just want to explain to kids who don't know any better, what maths is

#### [Kenny Lau (May 26 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127130973):
then why wouldn't you write down every step

#### [Kevin Buzzard (May 26 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127130974):
All of this stuff is great

#### [Kevin Buzzard (May 26 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127130982):
Because what is a step when you are 16 years old?

#### [Kevin Buzzard (May 26 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127130986):
You have never thought about steps

#### [Kevin Buzzard (May 26 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127130992):
You just answer the question

#### [Mario Carneiro (May 26 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127130993):
I presume that will be part of the talk

#### [Mario Carneiro (May 26 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127130997):
at least, the idea that math is built on axioms and rules

#### [Mario Carneiro (May 26 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127131002):
and you have to use those rules to prove things

#### [Mario Carneiro (May 26 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127131004):
the sense of "step" is not far from this

#### [Kevin Buzzard (May 26 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127131186):
Yes exactly

#### [Kevin Buzzard (May 26 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127131190):
I will be here at 8pm UK time (i.e. now + 3h50m) asking more stupid questions about real numbers

#### [Nicholas Scheel (May 26 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127133670):
`lemma α_sqr : α^2 = α + 1 := rfl` in ℤα ;)

#### [Kenny Lau (May 26 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127133673):
but he doesn't want to use Zalpha in the presentation lol

#### [Nicholas Scheel (May 26 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127133714):
btw I proved point 3, should I leave it in Zalpha or move it to a `point3.lean`?

#### [Kenny Lau (May 26 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127133717):
move it to `point3.lean`

#### [Nicholas Scheel (May 26 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127133772):
done!

#### [Nicholas Scheel (May 26 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127133829):
I tried and failed to prove that it is an integral domain, got any tips?

#### [Kenny Lau (May 26 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127133837):
where are you stuck in?

#### [Nicholas Scheel (May 26 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127133987):
it’s something like
`a * c + b * d = 0 AND a * d + b * c + b * d = 0 IMPLIES THAT (a, b) = 0 OR (c, d) = 0`

#### [Nicholas Scheel (May 26 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127134063):
I understand that it’s equivalent to the fact that α is not an integer, and equivalent to the fact that 1 and α are linearly independent, but I don’t see how to do that from the definition of multiplication

#### [Johan Commelin (May 26 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127134505):
Well, you could define an embedding of Zalpha into R.

#### [Johan Commelin (May 26 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127134510):
I think we now have about a dozen proofs of why that works :wink:

#### [Kenny Lau (May 26 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127134511):
proving that it is injective needs work also

#### [Johan Commelin (May 26 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127134556):
That is the linear independence of 1 and alpha

#### [Nicholas Scheel (May 26 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127134666):
sure, why not ;D

#### [Kenny Lau (May 26 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127134669):
oh right you need to prove that sqrt(5) is irrational

#### [Kevin Buzzard (May 26 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127140546):
Yeah, that's the analogue of showing that if $$z=x+iy$$ is a complex number which isn't zero, then you can divide by $$z$$, by multiplying by $$\overline{z}$$ and then dividing by the non-zero real $$z\overline{z}$$.

#### [Kevin Buzzard (May 26 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127140598):
In this instance it boils down to proving that the product of $$a+b\surd{5}$$ and its Galois conjugate $$a-b\surd{5}$$ is non-zero if at least one of $$a$$ and $$b$$ is non-zero

#### [Kevin Buzzard (May 26 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127140600):
`\surd`for square roots in maths mode, not `\sqrt`

#### [Kevin Buzzard (May 26 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127140601):
So as Kenny says it's precisely the irrationality of $$\surd 5$$, or, more precisely, it's the statement that no rational number squared is $$5$$ (rather than any statement about real numbers not being rational)

#### [Kevin Buzzard (May 26 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127140603):
So one way to do it is to prove that if $$a+b\surd 5$$ is non-zero then the rational $$a^2-5b^2$$ is non-zero and then use that a non-zero rational has an inverse.

#### [Kevin Buzzard (May 26 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127140700):
I've just been telling some kids about Lean. Some of them got into it. We were doing induction on nat and on or and on false and stuff

#### [Kevin Buzzard (May 26 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127140709):
I did some Fibonacci stuff

#### [Kevin Buzzard (May 26 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127140710):
and some logic stuff

#### [Kevin Buzzard (May 26 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127140711):
and we looked at why induction was a theorem in Lean

#### [Nicholas Scheel (May 26 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127141063):
```quote
Well, you could define an embedding of Zalpha into R.
```
Thanks @**Johan Commelin** I think that worked ;) https://github.com/kbuzzard/lean-squares-in-fibonacci/blob/master/src/Zalpha_real.lean
again, ugly code, but it typechecks

#### [Nicholas Scheel (May 26 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127141257):
and thanks @**Chris Hughes** for the alpha squared proof, such a time saver! :D

#### [Kenny Lau (May 27 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127142885):
hmm, I wonder if we can shorten it

#### [Kenny Lau (May 27 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127143270):
@**Nicholas Scheel** do you mind if I edit your files?

#### [Nicholas Scheel (May 27 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127143309):
go for it!

#### [Nicholas Scheel (May 27 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127143311):
I think I’m done for now, have to spend time on other things now

#### [Nicholas Scheel (May 27 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127143313):
but I’m curious: what is norm_num? I haven’t found much documentation for it

#### [Kevin Buzzard (May 27 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127143424):
It proves identities between explicit real numbers

#### [Kevin Buzzard (May 27 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127143425):
And inequalities etc

#### [Nicholas Scheel (May 27 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127143472):
cool 🙂

#### [Kenny Lau (May 27 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127143761):
```lean
theorem α_fib (n : ℕ) : α^(n+1) = ⟨Fib n, Fib (n+1)⟩ :=
begin
  induction n with n ih, { refl },
  change α*α^(n + 1) = ⟨Fib (n+1), Fib (n+2)⟩,
  rw ih, apply ext; simp [-add_comm],
  exact int.coe_nat_inj'.2 rfl
end
```

#### [Kenny Lau (May 27 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127143762):
I golfed off a lot of lines from here

#### [Nicholas Scheel (May 27 2018 at 01:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127143810):
that’s great 😃

#### [Kenny Lau (May 27 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127143872):
```lean
theorem α_fib (n : ℕ) : α^(n+1) = ⟨Fib n, Fib (n+1)⟩ :=
begin
  induction n with n ih, { refl },
  change α*α^(n + 1) = ⟨Fib (n+1), Fib (n+2)⟩,
  rw ih, apply ext; simp [-add_comm, Fib.is_fib]
end
```

#### [Nicholas Scheel (May 27 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127143928):
🤯 `change` sounds amazing, funny that I hadn’t run across it before

#### [Kenny Lau (May 27 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127143935):
do you realize that the `show` in tactic mode is different from the `show` in term mode

#### [Kenny Lau (May 27 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127143939):
and then `change` is a generalization of that, that allows you to change the hypotheses as well

#### [Nicholas Scheel (May 27 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127144089):
I haven’t used show in term mode, what’s the difference?

#### [Kenny Lau (May 27 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127144135):
well there's not a huge difference

#### [Reid Barton (May 27 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127144332):
I haven't used `show` in tactic mode!

#### [Nicholas Scheel (May 27 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127144344):
that moment when computer programs understand analogies better than we expect 😉

#### [Kenny Lau (May 27 2018 at 03:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127147117):
@**Nicholas Scheel** I hope you don't mind

#### [Kenny Lau (May 27 2018 at 03:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127147159):
https://github.com/kbuzzard/lean-squares-in-fibonacci/commit/7ba981070187c25d322b0e8de14021ec7214ddb9#diff-44f4839567c6f9e6617b4e04801b926a

#### [Kenny Lau (May 27 2018 at 03:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127147257):
TODO: incorporate [this](https://github.com/leanprover/mathlib/blob/master/number_theory/pell.lean#L421)

#### [Nicholas Scheel (May 27 2018 at 03:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127147478):
not at all, that’s cool! thanks!

#### [Kenny Lau (May 27 2018 at 04:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127147926):
https://github.com/kbuzzard/lean-squares-in-fibonacci/commit/9106996916442e8f17239323d5a6cbe3e236efd3#diff-44f4839567c6f9e6617b4e04801b926a

#### [Kenny Lau (May 27 2018 at 04:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127147927):
done

#### [Chris Hughes (May 27 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127162054):
I'm working on polys. I've just done the remainder theorem.

#### [Kevin Buzzard (May 27 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127162168):
Polys in 1 variable need to go in mathlib so perhaps keep this in mind

#### [Kevin Buzzard (May 27 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127162208):
When I write code now, I realise that sometimes it's code for me and sometimes it's stuff I think should be in mathlib

#### [Kevin Buzzard (May 27 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127162209):
And I've started separating the two

#### [Kevin Buzzard (May 27 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127162356):
I think this is an interesting consequence of proving "random" things like 144 being the largest square in the Fibonacci sequence.

#### [Kevin Buzzard (May 27 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127162399):
I am pretty sure (am I right @**Mario Carneiro** ?) that mathlib has no interest in keeping and maintaining a proof of the curiosity that 144 is the largest square in the Fibonacci sequence.

#### [Kevin Buzzard (May 27 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127162401):
However

#### [Kevin Buzzard (May 27 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127162403):
When a mathematician looks at the proof, they expect to have to work in some areas

#### [Kevin Buzzard (May 27 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127162408):
but conversely they expect some "standard tools" to be there

#### [Kevin Buzzard (May 27 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127162413):
and this can be used to guide development of mathlib

#### [Kevin Buzzard (May 27 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127162414):
For example, at some point someone is going to need quadratic reciprocity

#### [Kevin Buzzard (May 27 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127162453):
and we will end up developing some of the tools needed to prove QR in this 144 proof

#### [Kevin Buzzard (May 27 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127162454):
and I think there's a strong argument for QR going into mathlib as it's one of the jewels in the crown of mathematics

#### [Kevin Buzzard (May 27 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127162456):
[as well as being a special case of Langlands Reciprocity ;-) ]

#### [Kevin Buzzard (May 27 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127162464):
In the 144 proof we don't need full QR

#### [Kevin Buzzard (May 27 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127162465):
but we need Gauss' Lemma and Euler's Criterion

#### [Kevin Buzzard (May 27 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127162502):
so we're starting along the road to QR with these.

#### [Kenny Lau (May 27 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127162963):
```lean
instance : decidable_linear_ordered_comm_ring ℤα :=
```

#### [Kenny Lau (May 27 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127162964):
https://github.com/kbuzzard/lean-squares-in-fibonacci/blob/master/src/Zalpha_Zsqrt5.lean#L38

#### [Kenny Lau (May 27 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127162966):
@**Nicholas Scheel** @**Kevin Buzzard** I find embedding into `ℤ√5` a better idea than embedding into the reals

#### [Kevin Buzzard (May 27 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127163332):
Mario's $$\mathbb{Z}[\surd{5}]$$?

#### [Kevin Buzzard (May 27 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127163335):
(why doesn't sqrt work in LaTeX?)

#### [Kevin Buzzard (May 27 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127163337):
He proved it was an ID?

#### [Kenny Lau (May 27 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127163378):
```quote
He proved it was an ID?
```
yes

#### [Kenny Lau (May 27 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127163382):
(althought I didn't use that)

#### [Kenny Lau (May 27 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127163386):
(I used norm to prove that Zalpha is ID)

#### [Kevin Buzzard (May 27 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127163387):
So how do you deduce ID from norm? You need that if norm is 0 then term is 0, right?

#### [Kenny Lau (May 27 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127163388):
yes

#### [Kenny Lau (May 27 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127163425):
which is tantamount to proving that sqrt5 is irrational

#### [Kevin Buzzard (May 27 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127163429):
and so you need to prove irrationality#

#### [Kevin Buzzard (May 27 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127163430):
right

#### [Kenny Lau (May 27 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127163431):
on hindsight I should have used the embedding

#### [Kenny Lau (May 27 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127163433):
but I still want to have the norm

#### [Kevin Buzzard (May 27 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127163434):
I was suggesting that Mario might have done that already

#### [Kenny Lau (May 27 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127163435):
the norm is useful

#### [Kevin Buzzard (May 27 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127163436):
Sure

#### [Kenny Lau (May 27 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127163438):
sure

#### [Kevin Buzzard (May 27 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127163439):
And your norm commutes with Mario's

#### [Kevin Buzzard (May 27 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127163445):
so you could have deduced your norm result from Mario's

#### [Kevin Buzzard (May 27 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127163447):
and this would have saved you the trouble of proving irrationality of sqrt(5)

#### [Kenny Lau (May 27 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127163448):
you see, in my embedding, I multiply the "real value" by 2

#### [Kenny Lau (May 27 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127163449):
because alpha is not an element of Z[sqrt5]

#### [Kenny Lau (May 27 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127163450):
```quote
and this would have saved you the trouble of proving irrationality of sqrt(5)
```
I know

#### [Kenny Lau (May 27 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127163488):
I'll do it when I finish lunch

#### [Kevin Buzzard (May 27 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127163491):
but I guess it's nice to check it every now and then

#### [Nicholas Scheel (May 27 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127163597):
that’s cool! I’ll have to see how Zsqrt is decidable, I just avoided it because it’s irrational xD

#### [Nicholas Scheel (May 27 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127163646):
oh duh: `def sq_le (a c b d : ℕ) : Prop := c*a*a ≤ d*b*b`

#### [Kenny Lau (May 27 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127168247):
done

#### [Kenny Lau (May 27 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127168250):
now the long proof that 5 is irrational is gone

#### [Kenny Lau (May 27 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127168635):
```lean
theorem char_eq (z : ℤα) (H : z * z - z - 1 = 0) : z = α ∨ z = β :=
have H1 : (z - α) * (z - β) = 0,
  by rw [← H, α, β]; ring,
(eq_zero_or_eq_zero_of_mul_eq_zero H1).cases_on
  (or.inl ∘ eq_of_sub_eq_zero)
  (or.inr ∘ eq_of_sub_eq_zero)
```

#### [Kenny Lau (May 27 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127168638):
completely pointless theorem

#### [Kenny Lau (May 27 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127168639):
Gal(Zalpha/Z) = C2

#### [Mario Carneiro (May 27 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127168646):
I guess `z * z - z - 1 = (z - α) * (z - β)` is also a way to prove alpha*beta = -1

#### [Kenny Lau (May 27 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127168649):
sure

#### [Kenny Lau (May 27 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127169687):
```lean
theorem gal (f : ℤα → ℤα) [is_ring_hom f] : f = id ∨ f = conj :=
```

#### [Kenny Lau (May 27 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127169688):
lol I did it

#### [Kevin Buzzard (May 27 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127170066):
nice!

#### [Kevin Buzzard (May 27 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127170068):
Did you develop any tools for proving polys of degree n have at most n roots?

#### [Kenny Lau (May 27 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127171159):
```lean
local notation `α` := Zalpha.units.α

#eval α^(-3:ℤ) -- -3 +   2α
#eval α^(-2:ℤ) --  2 +  -1α
#eval α^(-1:ℤ) -- -1 +   1α
#eval α^( 0:ℤ) --  1 +   0α
#eval α^( 1:ℤ) --  0 +   1α
#eval α^( 2:ℤ) --  1 +   1α
#eval α^( 3:ℤ) --  1 +   2α
#eval α^(12:ℤ) -- 89 + 144α
```

#### [Kenny Lau (May 27 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127171160):
look at what I did

#### [Kenny Lau (May 27 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127171161):
```quote
Did you develop any tools for proving polys of degree n have at most n roots?
```
I thought Chris is doing that

#### [Kenny Lau (May 27 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127173701):
Theorem (reverse mathematics): you need to use induction to prove that L(n) = F(n) + F(n-3).
Proof: [link](http://www.wolframalpha.com/input/?i=%28%28%CE%B1%5Ex%2B%CE%B2%5Ex%29-%28%28%CE%B1%5Ex-%CE%B2%5Ex%29%2B%28%CE%B1%5E%28x-3%29-%CE%B2%5E%28x-3%29%29%29%2Fsqrt%285%29%29+where+%CE%B1%3D%281%2Bsqrt%285%29%29%2F2%2C%CE%B2%3D%281-sqrt%285%29%29%2F2).

#### [Kenny Lau (May 27 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127173791):
and if you define L(n) := F(n) + F(n-3), you would have to use induction to prove other things later

#### [Mario Carneiro (May 27 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127174670):
how are those defined?

#### [Mario Carneiro (May 27 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127174808):
From that plot it looks like it's not even true

#### [Mario Carneiro (May 27 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127174857):
L(3) = 4, F(3)+F(0) = 2

#### [Kenny Lau (May 27 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127176377):
@**Mario Carneiro** I'm an idiot. L(n) = 2F(n) + F(n-3).

#### [Kenny Lau (May 27 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127176378):
what am i doing

#### [Kenny Lau (May 27 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127176388):
@**Kevin Buzzard** @**Nicholas Scheel** should we actually call it Zphi instead of Zalpha?

#### [Kenny Lau (May 27 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127176389):
Wikipedia calls its little brother psi

#### [Mario Carneiro (May 27 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127177700):
that one is true for the continuous extension too

#### [Mario Carneiro (May 27 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127177702):
I call the little brother phi bar

#### [Mario Carneiro (May 27 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127177703):
because it's the conjugate of phi

#### [Nicholas Scheel (May 28 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127178931):
they’re alpha equivalent so I don’t care ;) feel free to rename it

#### [Kenny Lau (May 28 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127178994):
@**Kevin Buzzard** what do you think?

#### [Kenny Lau (May 28 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127182144):
patchily converted everything to Zalpha

#### [Kevin Buzzard (May 28 2018 at 05:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127186344):
I don't care about names

#### [Kevin Buzzard (May 28 2018 at 05:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127186347):
I call things lemma 3.1

#### [Kevin Buzzard (May 28 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Largest%20Square%20in%20the%20Fibonacci%20Sequence/near/127186351):
What do I know about names

