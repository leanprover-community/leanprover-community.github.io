---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/54951valuations.html
---

## Stream: [maths](index.html)
### Topic: [valuations](54951valuations.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127105553):
Both the Fibonacci Squares project and the Adic Space project need valuations on rings -- one in rather more generality than the other. But let's start at the beginning. Does Lean have p-adic valuations on Z? In other words, is the function $$v_p(\cdot)$$ on the non-zero integers (or even rationals) sending $$p^nN$$ (with $$N$$ coprime to the prime $$p$$) to $$n$$? The key theorems are $$v_p(ab)=v_p(a)+v_p(b)$$ and $$v_p(a+b)\geq\min\{v_p(a),v_p(b)\}$$ (where $$v_p(0)$$ is usually taken to be $$+\infty$$).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127105607):
Perfectoid space valuations would take values in a certain kind of totally ordered monoid

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127105620):
(and are of a slightly different nature -- they are really norms not valuations, so the total function $$M \mapsto p^{-v_p(M)}$$ with target the non-negative reals would be an example).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 26 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127106671):
I have approximately this lying around somewhere

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 26 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127106845):
https://gist.github.com/rwbarton/599327954b01b2e840894189981172ea

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 26 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127106894):
I guess `ord_add` is missing, but it should be easy to prove from the other stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127107157):
line 91 should now be

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127107159):
`         ...   = p * (p^r * k)   : by unfold pow nat.pow; ac_refl,`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127107162):
[adding pow, probably because of some relatively recent change with `^`]

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127107276):
Thanks so much! This is exactly what I wanted!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127107285):
What a great little community we are getting here!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127107301):
I'm just going to dump it in a subdirectory in my project called `Reid_Barton`. Is that OK?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127107340):
Is there a better way of doing things?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 26 2018 at 01:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127107625):
Sure, no problem.
The better way is probably to try to PR things into mathlib, but that's more effort.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127107925):
`example : has_le (ℕ+) := by apply_instance -- fails`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127107937):
Noticed this along the way. You've not proved the valuation of a + b but you've proved everything but. I've never worked with `\N+` before.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127107991):
Is there a good reason for not having le on `\N+`? I am making a little collection of random short mathlib proposals. I understand how mathlib works much better after my schemes exercise.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 26 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127108119):
I doubt there is any good reason. `pnat` isn't used that much, it seems. I remember finding it a little more annoying to use than I would have liked

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 26 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127108122):
Particularly as there are coercions in both directions between `nat` and `pnat`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127108166):
Is `ord_pow` broken?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127108167):
Or did I break it myself?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 26 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127108177):
It's quite possibly broken because it is about 2.5 months old

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127108178):
do computer scientists really need a _coercion_ from `nat` to `pnat`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127108180):
I just can't even guess what it would be

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127108183):
"any one of a couple of random examples"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 02:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127108278):
`lemma ord_pow {k : ℕ} {a : ℕ+} : ord p (a^k) = k * ord p a := ord_ppow`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 02:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127108279):
:-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 02:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127108281):
I think some coercion magic happened?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 02:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127109528):
Is there a type Nat union {infinity}? I mean, it's option Nat but I want the obvious le, add and min functions (and don't want to write them if they're already there). The reason I ask is to extend p-adic valuation to zero, and I think I do have to add infinity, because the standard CS answer of just defining it to be 37 or whatever and ploughing on regardless doesn't seem to work here, because then things like min are wrong.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 26 2018 at 02:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127109552):
it's called the ordinal omega+1 :D

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 03:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127109604):
:D

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 03:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127109613):
Things which I want to be there, are more and more often beginning to be there :D

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127109668):
Anyone fancy univariate polynomials over a field (division algorithm, degree function with the usual problems at 0, gcd, unique factorization?)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127109673):
I'm seeing that pop up more and more. Lean has multivariate polynomials but I think these deserve to be a special class rather than constantly carrying around the type "unit" for your list of variables.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127109730):
@**Nicholas Scheel** do you want to try this? I'm going to show your work on Z[alpha] to the British Maths Olympiad squad tomorrow! See what they make of it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127109786):
Some stuff is there by a student of Johannes in his mason-stother directory but I don't think it's all there. And didn't someone do some Euclidean Algorithm stuff recently? Some student of Scott maybe? That might help I guess.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127109793):
We need univariate polynomials for the Fibonacci project, as you know.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127109800):
Or maybe Kenny or Chris will do it now their exams are over.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 03:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127109843):
A fair amount of this stuff should be tidied up and put in mathlib, so it's all in one place.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 26 2018 at 03:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127109967):
hah, won't you soon have your own army of undergraduates working for you over the summer?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 03:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127109993):
Over 20 undergrads now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 03:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127109997):
They start 2nd July

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 03:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127109998):
It's going to be a crazy summer!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 03:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127110000):
2 months!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 03:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127110674):
I am so rubbish at coe

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 03:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127110679):
```lean
@[simp] lemma pgcd_coe_something (a b : ℕ) : pgcd a b = gcd a b := begin
unfold pgcd,
--rw pnat.coe_nat_coe a, -- I am so rubbish at coe
sorry
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 03:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127110681):
This is Reid's pgcd from his gist from earlier

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 04:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127111216):
```quote
https://gist.github.com/rwbarton/599327954b01b2e840894189981172ea
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 26 2018 at 04:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127111362):
> Is there a type Nat union {infinity}?

As of this morning, there is a `with_top A` structure that adds an infinity element to any order. So `with_top nat` is just what you want.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 26 2018 at 04:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127111551):
wow what a coincidence lol

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 26 2018 at 04:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127111894):
> do computer scientists really need a _coercion_ from nat to pnat?

Hm, my original concern was that if you wanted to write 5 as a pnat you would need to write <5, dec_trivial> which is obviously cumbersome. But actually since pnat has `has_one` and `has_add` that's actually enough for `bit0` and `bit1` to work, meaning that `(5 : pnat)` works fine (being defined as `bit1 (bit0 1)` where the 1 and addition are interpreted in `pnat`). So maybe this isn't needed. I'll see what breaks if I remove it, I agree it's not great to have a non-identity looking coercion

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 26 2018 at 04:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127111903):
I was thinking of using `pnat` for the domain of `Z/nZ` btw, which will give it a better algebraic theory than `fin n`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 26 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127112038):
```quote
> Is there a type Nat union {infinity}?

As of this morning, there is a `with_top A` structure that adds an infinity element to any order. So `with_top nat` is just what you want.
```
Mario -- did you see Remark 1.5 of www2.math.uni-paderborn.de/fileadmin/Mathematik/People/wedhorn/Lehre/AdicSpaces.pdf (page 4)? There is a fundamental construction in adic spaces -- adding a "bottom" element zero to a a totally ordered group (e.g the group of positive reals) and creating a totally ordered monoid. Is this sort of thing easy to do now?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nicholas Scheel (May 26 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127112046):
@**Kevin Buzzard** I could spend an hour or two on it ... should I use multivariate polynomials, should I use finsupp, or just do a direct list encoding?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 26 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127112134):
Actually your comment got me thinking about this. There is a related construction, let's say `with_zero A`, which adds a unit to any additive semigroup; and if the zero and bottom coincide then you get a composite structure which works well on some kinds of ordered groups, I would imagine. Similarly you can make sense of addition with infinity, and that structure coheres with the order of `with_top`, so that you can add an infinity element to an ordered additive semigroup.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 26 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127112177):
This could be used to factor `ennreal` into `with_top nnreal`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 26 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127112184):
rip ennreal 2017-2018

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 26 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127112217):
born [Aug 30, 2017](https://github.com/leanprover/mathlib/commit/51042cde36e3ff513866c7ee6a1909650ba7396e#diff-47b6fc31ab3cbab9a5353881776d1008)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 26 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127112226):
It probably wouldn't go away as a definition, it has enough properties on its own that make it worthy of study, but it would simplify and generalize some theorems

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 26 2018 at 04:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127112232):
But to answer your question, currently `with_bot` and `with_top` only deal with the order structure, they don't have any monoid stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127163781):
```quote
> do computer scientists really need a _coercion_ from nat to pnat?

Hm, my original concern was that if you wanted to write 5 as a pnat you would need to write <5, dec_trivial> which is obviously cumbersome. But actually since pnat has `has_one` and `has_add` that's actually enough for `bit0` and `bit1` to work, meaning that `(5 : pnat)` works fine (being defined as `bit1 (bit0 1)` where the 1 and addition are interpreted in `pnat`). So maybe this isn't needed. I'll see what breaks if I remove it, I agree it's not great to have a non-identity looking coercion
```
Is it possible to keep the coercion but demand that the type class resolution system produces a proof of positivity before it is applied? I think that this would very much mirror the way a mathematician thought about the issue.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127163783):
You might find that if proofs of positivity are carried around

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127163787):
with instances like "a > 0 and b > 0 implies a + b > 0"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127163792):
then the coercions work fine.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127163793):
With the current system you just occasionally see these \u \u x things

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127163833):
and it's only at the point where you go to cancel them and they won't cancel that you realise you've made a mathematical slip

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127163838):
Can we make the coercion part of type class resolution better?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164025):
this isn't how coercions work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164032):
they are functions `A -> B`, nothing else is allowed in there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164033):
in particular, coercions cannot be partial

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164037):
except the coercion `Prop -> bool` which is magical

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164524):
CS 101 question alert :-/

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164526):
What's the theorem `\<a,h\>.val = a` called for subtypes?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164565):
rfl

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164567):
I was trying not to use rfl

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164570):
I was looking at the proof that \u \u a =a

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164578):
I just figured that I had a bunch of stuff about coercions that I needed to understand better before I said too much more about this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164581):
and then I ended up going down a rabbit hole watching the type class resolution system unfold :-/

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164582):
Actually I don't understand.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164583):
How do I rewrite \u \u a as a?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164586):
Wait

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164589):
I was asking for the name of the theorem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164590):
not the proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164634):
you haven't given me enough info to answer the question

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164638):
I'll formulate something precise.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164639):
lots of theorems look like \u \u a = a

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164641):
I need to know what is the type of a, and the type of \u a

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164650):
[pause whilst we discover if Kevin is talking nonsense]

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164817):
```lean
variables (α : Type) (p : α → Prop) 
theorem what_am_i_called (a : α) (h : p a) : (subtype.mk a h).val = a := rfl 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164818):
The question.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164862):
because I want to use you in a rewrite

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164864):
so I need to know your name

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164867):
the theorem doesn't have a name, it is done automatically by dsimp

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164876):
And there's you guys saying our naming conventions are bad

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164877):
same as how beta reduction isn't a named theorem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164879):
dsimp is what?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164881):
I used it a couple of times recently

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164882):
Kenny told me "just use dsimp" and I'm like "ooh my goal has gone from 1 page to 5 lines"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164920):
it's `simp` for definitional rewrites

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164924):
which way does it go?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164925):
What does it actually do?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164927):
If it sees my subtype.mk.val stuff it just says "ooh I'll remove that"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164929):
but does it ever add it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164932):
it does exactly the same sort of thing as simp

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164937):
oh great :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164940):
Another black box :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164944):
I see

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164945):
it cancels projections applied to structure mk

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164947):
What else does it do?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164948):
this is the structure iota rule

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164951):
What's a complete list of what it does?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164952):
Would I be able to understand the source code?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164955):
Kenny says that Lean does not do magic but this is still magic to me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164995):
dsimp has a config too

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127164997):
53 extra options?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165001):
that has a fairly complete list of the kinds of automatic reductions it does, beta, eta, zeta, iota etc

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165007):
and it also uses `@[simp]` lemmas that are also rfl lemmas

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165013):
as well as definition unfolding when you give it to the bracket list or use `!`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165014):
I would be really interested in watching a video or seeing an article about what dsimp and/or simp do. If I understood what they were doing I wouldn't still just be hopefully typing simp every now and then just to see if I can make the goal go away

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165046):
Haven't we had this conversation before?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165057):
I'm pretty sure you wrote that article

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165060):
I feel like there's still a whole bunch of things I don't fully understand with all this business

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165061):
I'll read my own docs and see if this enlightens me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 27 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165117):
The textbook "term rewriting and all that" is pretty good on this subject, if your uni library has it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nicholas Scheel (May 27 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165171):
simplification using definition equalities, I believe

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165225):
So my real question was "how do I do a definitional rewrite in tactic mode", and the answer is "don't use rw, use show"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165231):
`change with` is literally definitional rw

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165232):
```quote
The textbook "term rewriting and all that" is pretty good on this subject, if your uni library has it
```
Thanks Andrew. My university can get any book for me.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165274):
but `dsimp` is nice for just cleaning up some common patterns

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165275):
Equality is asymmetric for you people, isn't it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165278):
This is only just dawning on me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165281):
yes, with term rewrites direction really matters

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165282):
If you write a = b, and if one side was more complicated than the other

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165283):
you would put the more complicated side first

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165284):
Is this just some general principle?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165287):
yeah, simp simplifies

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165288):
it's not called complexify

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165330):
I had not realised that = was asymmetric

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165331):
in any way whatsoever

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165332):
I have a different definition of = to you

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165333):
= itself is symmetric

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165334):
symmetric in some theorem sense

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165336):
but you have to decide which goes first

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165340):
and we don't care

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165343):
but simp and dsimp takes the list of simp lemmas and use them as a rewrite graph

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165344):
and this is directed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165345):
Right, I've just been learning this from my own notes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165347):
Aah!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165349):
I've just realised what my question actually is.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165394):
My question is this: "I never ever tag anything with @[simp]. I make loads of structures. Can you give me some basic advice over which trivial lemmas I should be (a) proving and (b) tagging with simp?"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165403):
Unfortunately, the answer is "depends on the structure"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165406):
some axioms of a structure should be simp lemmas

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165407):
subtype

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165408):
like `zero_add`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165409):
A type and a proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165449):
I don't think subtype has any simp lemmas

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165451):
which is to say, there is nothing that sticks out as necessary

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165453):
oh, <a, h1> = <b, h2> <-> a = b should be a simp lemma

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165455):
What about presheaf of types on a topological space?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165459):
I made that structure once

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165461):
but actually I think simp might do that automatically anyway

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165462):
I'll find you a link

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165499):
simp will already do a few things by default on all structures, which more or less covers all the general recommendations

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165503):
https://github.com/kbuzzard/lean-stacks-project/blob/6617de7dd5f11af46f0c7e0d2223ee065d71b9f3/src/tag006E.lean#L4

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165511):
I am proud to say that I did actually write a simp lemma for that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165512):
My simp lemma says "crap, I made a poor design decision when designing that structure, but I can't be bothered to change it now"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165514):
that's just what I would have recommended

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165555):
except possibly for the dependent args

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165556):
You would recommend the change in the structure?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165558):
that doesn't matter so much

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165559):
Oh!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165562):
You don't care which definition I use if they're all equivalent?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165567):
I was going to bite the bullet one day and edit the definition of that structure. You're saying that's a crazy idea?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165568):
it affects the proof goals when defining structures with `{ stuff := ... }`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165569):
so it depends on how you usually prove such goals

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165570):
I was going to change "f = g circ h" with "forall x, g (h x) = f x"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165571):
if the first thing you do is always funext, then that's a hint

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165608):
Note the equality "f = g circ h"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165611):
the more complicated side on the right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165612):
is that also unwise?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165613):
actually here I recommend that ordering

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165615):
The thing about funext was that there were a few times when the fact that it was comp was really useful, it made some proofs really nice and short

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165616):
because the argument to f is getting simpler

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165617):
*boggle*

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165622):
I don't understand

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165623):
think of it as `f (comp a b) = f a o f b`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165670):
here simp will want to go left to right to make the argument to `f` as simple as possible

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165671):
It's `res U W x = res V W (res U V x)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165672):
that's what it is really

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165673):
You still want it that way round?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165680):
that's not a good simp lemma

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165681):
"restriction of a function on U down to V and then down to W equals restriction directly down to W"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165684):
Either way round?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165726):
Okay, I guess in this case since it's a proof arg it shouldn't be a metric of simplicity

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165727):
so in that case you want `res V W (res U V x) = res U W x`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165729):
This is the thing I don't understand. It takes two functions `res U V` and `res W V` and it returns one function. It's made it simpler. I don't understand what should be a simp lemma.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165735):
Aah so you do want to switch the order?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165736):
And then make a simp lemma?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165781):
```quote
Okay, I guess in this case since it's a proof arg it shouldn't be a metric of simplicity
```
I don't understand that either :-/

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165790):
You have this extra argument that has a big term in it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165795):
I've mentioned that proof args are bad for rewrites before

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165838):
Why?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165839):
proof args are fundamental statements about the situation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165850):
Are you saying that associativity of addition should not be a simp lemma?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165892):
associativity of addition is both a simp lemma and seems to have the more complicated side on the right.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165901):
None of it adds up to me. I am still nowhere near understanding what should be a simp lemma.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165904):
assoc is a special case

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165906):
*boggle*

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165908):
I'll add it to the docs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165909):
simp has special handling for comm/assoc operations

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165948):
which uses a convention which goes against the "simpler argument on the right" convention?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165950):
it would not normally be a good simp lemma, because it doesn't simplify the term

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165958):
`mul_one` is a simp lemma and it's a proof arg, if I've understood the last term correctly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165959):
But simp will notice if you give it a lemma that looks like associativity and apply special algorithms to do smart things with that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165971):
None of those have proof args

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165973):
*oh*

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127165976):
I'm talking about proofs as arguments to functions you want to rewrite

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166014):
so in this case that would be like proof arguments to `mul` or `one`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166015):
I thought you were talking about proofs as arguments used to create a structure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166021):
in your case I'm talking about `res` which has three proof args

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166027):
Would your opinion change if made them all work magically using type class resolution?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166028):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166066):
that's an interesting idea, I'd have to see how messy the arguments can get

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166073):
The reason I didn't use type class resolution for those things was that when I wrote that code I had no idea how typeclass resolution system worked

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166074):
so I just over-rode it and would always pass the proofs manually

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166082):
and then later on in the project I was forced to work with rings and ring homs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166083):
so I was forced to learn the system

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166086):
and we had that long thread with me moaning and learning about `letI`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166279):
Ok so coercions.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166280):
`theorem eew (Y : ℕ+) : ((Y : ℕ) : ℕ+) = Y := rfl -- fails`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166282):
That's not good, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166286):
Should that be a simp lemma?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166295):
`ℕ+` is one of my favourite sets in ZFC

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166296):
Why is it so hard to work with here?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166333):
Just because it's not a stupid semiring

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166339):
maybe it's a demisemiring

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166349):
that is a simp lemma, I think

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166350):
Aah here's a question.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166351):
Let's say we ripped out the definition of pnat

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166352):
`coe_nat_coe`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166390):
and replaced it with a straight inductive structure with one and succ

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166396):
Would that make *any* difference to *anything*

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166397):
not really

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166398):
or you just write the new interface

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166399):
and that's it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166400):
No issue with compile time or running time

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166401):
or simp not working as well

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166402):
anything not using the interface would be affected, of course

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166404):
Aah

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166410):
anything accessing the innards of the structure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166411):
i.e. if someone creates a pnat by writing <2, dec_trivial>

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166413):
instead of (2 : pnat)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166414):
then they should be punished?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166415):
How does that work?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166454):
"You only use official constructors"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166456):
"not inbuilt stuff"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166458):
Oh wait -- surely anyone writing a proof in term mode with pnat will have constructors like that everywhere

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166463):
because it's a super-cool way of being fancy in fancy term mode

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 27 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166464):
right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166465):
eew

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166466):
well, the thing is that I don't want to avoid structure constructors, because they are very nice

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166467):
So there *is* a question left

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166468):
you can't replicate that functionality with an interface

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166515):
unless the interface is to pass in a specially defined structure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166518):
like simp_config

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166519):
you've lost me now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166524):
but I do see that there is a huge argument for structure constructors and this presumably has some bearing on exactly which constructors you choose and maybe even in which order?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166527):
maybe order irrelevant

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166528):
but you never know

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166529):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166530):
order is relevant for anonymous constructors

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166572):
Here are my currrent thoughts on presheaf fyi:
```
structure order_presheaf (α : Type u) [preorder α] :=
(F : α → Type u)
(res : ∀ x {y}, x ≤ y → F y → F x)
(Hid : ∀ x h a, res x h a = a)
(Hcomp : ∀ x y z h₁ h₂ (a : F z),
  res x h₁ (res y h₂ a) = res x (le_trans h₁ h₂) a)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 27 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166574):
what is an `order_presheaf`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166577):
Would you want presheaves in mathlib?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166581):
oh eew

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166582):
what just happened there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166583):
with the open sets

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 27 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166584):
oh, they form a preorder under inclusion!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166586):
he thinks he's being clever

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166587):
but we need the etale site ;-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166588):
so he's still not general enough ;-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166627):
if you add enough axioms to the preorder you can capture exactly the open sets of some topology

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166628):
yeah, I was just remarking that at some point later on algebraic geometry needs the notion of sheaf on something more general than a topological space

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166630):
but this part of the definition only needs a preorder

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 27 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166636):
```quote
yeah, I was just remarking that at some point later on algebraic geometry needs the notion of sheaf on something more general than a topological space
```
what do you need?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166638):
sheaf on a site

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 27 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166639):
`[category \a]`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 27 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166640):
i.e. there may be more than one morphisms?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166641):
if you want a category then this is just `functor`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 27 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166643):
Right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166644):
but it has to satisfy the sheaf axiom

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166645):
point me to that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166677):
and you need more than a category to formalise that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 27 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166686):
@**Mario Carneiro**  so they may have two "proofs" of `x \le y` and they want the two things to be unequal

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 27 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166687):
well, so far we are only talking about presheaf I thought

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166688):
I am actually very fine with that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166690):
that's true but I am interested in more than presheaves here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166691):
that's the remaining problem with this definition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166694):
as I said, I don't like proof args

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 27 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166697):
well then great! They won't be proofs once you generalize to a category :simple_smile:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166702):
but you can't easily remove them from this... what's the structure of that argument otherwise?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166704):
https://stacks.math.columbia.edu/tag/00VH

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166705):
I guess `Hom x y`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166751):
That's a site

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 27 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166756):
Right, just a morphism in some category.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166765):
Did you see https://stacks.math.columbia.edu/tag/00VI

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166812):
Mario, I think this says "if a computer scientist tries to do this, they will have universe issues. But in all the cases that a mathematican cares about, these issues can be avoided and we can do everything in Type"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166822):
Presheaves are already rather large

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166824):
"This definition uses two universes u and v, but when we apply it I claim that we can get away with one universe"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166825):
How do you formalise that? ;-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166866):
It looks like sites have to be small though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166868):
but what's a (pre)sheaf on a site?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166873):
all I see is a bunch of covering stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166884):
Also relevant

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166885):
https://stacks.math.columbia.edu/tag/00ZF

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166936):
https://stacks.math.columbia.edu/tag/00VL

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166937):
sheaf!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166938):
Still no presheaf :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 27 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166940):
Scott is doing sites in the his category stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166942):
https://stacks.math.columbia.edu/tag/00V1

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166943):
and what is the site corresponding to a top space?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166944):
OK so presheaf on a category, sheaf on a site

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166945):
The site corresponding to a top space is this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166953):
The category has an object for each open set

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166960):
Homs from U to V are empty unless V sub U in which case there is one elment

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127166966):
Coverings: a set of morphisms U_i -> U covers U iff the union of the image of the U_i is U

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167004):
The sheaf axiom says this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167017):
"If U is an open set, and it is covered by opens U_i, then to give a continuous function on U is to give a continuous function f_i on each U_i such that f_i and f_j agree on U_i intersect U_j"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 27 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167025):
You can equivalently describe the category like this. The objects are topological spaces equipped with a map to X which is an open immersion. A morphism is a continuous map which is compatible with the structural maps to X.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167027):
They say "continuity can be checked locally"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167071):
isn't that just true?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167072):
Reid's changing of my category to an equivalent category was something which turned out to be really important

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167073):
like as a statement of topology

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167074):
It's precisely the statement that continuity is a local condition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167081):
So the *presheaf* of continuous functions on a topological space

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167082):
is actually a sheaf!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167083):
But the presheaf of constant functions is not a sheaf

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167085):
because if I have two disjoint open sets

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167091):
and define a function to be 1 on one of them but 2 on the other one

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167093):
it's locally constant

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167094):
but not constant

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167095):
ah okay, so locally constant functions is a sheaf

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167097):
right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167101):
it's the sheafification of the presheaf of constant functions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167102):
sheafification is an adjoint to the forgetful functor

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167157):
so how much does it matter that these are poset categories?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167158):
Exactly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167161):
it doesn't matter at all

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167163):
and in general they won't be

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167165):
is a poset category one where the hom sets have size <= 1?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167166):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167175):
so the etale site attached to a scheme does not have this property I guess

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167178):
maybe it would be better to do this with honest categories

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167180):
I think Scott said that quite a long time ago

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167223):
but I just wanted to get on

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167230):
Sheaves of sets on a site are a Mathematician's Topos Mario.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167233):
This is distinct to the CS topos

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167238):
like in the literal sense?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167239):
You have some more general notion I think

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167240):
Topos is used to mean two different things, I believe

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167242):
I like Grothendieck topoi

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167244):
you like elmentary topoi

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167246):
I am not sure I would say that...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167247):
https://stacks.math.columbia.edu/tag/00X9

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167289):
topoi is usually where I get off the bus

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167290):
It took me a while, in the pre-Wikipedia age, to understand that the two uses of the word were distinct

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167293):
I knew this guy as an UG who would go round saying "a topos is a category which is finitely complete, finitely cocomplete, has exponentiation and a subobject classifier"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167295):
and I had no idea what any of those things meant

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167301):
and then years later I found some topoi I was actually interested in

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167303):
that's about where I am

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 27 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167304):
*as* an UG :o

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167305):
and then it turned out they were a different kind of topos

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167307):
I learn and forget those things every year

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167313):
There was once some debate about whether Wiles/Taylor-Wiles used Grothendieck topoi in their proof of FLT

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167353):
and the answer turned out to be

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167354):
because that means large universes, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167358):
"well, mathematicians are always a bit vague about what exactly they are using, and there is no mention of set-theoretic difficulties, but Brian Conrad went away and checked every single cohomology group in the entire proof and verified that it was OK, everything happened within one universe"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167366):
Wiles most definitely used etale cohomology in his proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167368):
and I am almost certain that he cited some papers which at some point use flat cohomology

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167412):
and they probably cite some papers which at some point mention fpqc cohomology

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167423):
so we really needed an expert who could come along and say "I know exactly which parts of the theory of etale cohomlogy and other cohomology theories he used and can verify that all the stuff he uses can be formalised in ZFC"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167430):
before that debate died down

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167484):
Some people really care about universes. If Lean really cannot keep track of them then these people might be skeptical

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167502):
My current personal viewpoint on this is simply to accept the large cardinals. If they make maths easier and more fun to do then I'm in

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167503):
For the most part, if it lives in `Type` it can be constructed in ZFC

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167552):
Right, but any file which uses "universes u v" is open to question right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167553):
Or even "universe u" perhaps

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167557):
if it uses Type as well

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167559):
no, as long as at the end you build something in `Type`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167561):
Oh

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167563):
The part which makes this not quite true is impredicativity of Prop

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167566):
aie

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167570):
so you get a proof which lived in another universe

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167573):
but you can't get a proof in your own universe

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167575):
so you use propext

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167577):
cunning

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167578):
you can construct proofs of propositions in Prop in Type, which assert existence of large cardinals

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167580):
ha ha

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167582):
oh I hadn't realised that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167585):
Prop covers its tracks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167587):
that's what impredicativity does for you

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167632):
But still to *construct* the proof you need the extra universes, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 27 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167636):
is @**Kevin Buzzard** being impredicative?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167637):
you could talk about configurations in Type 63 and it wouldn't make the proof large

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167641):
I am just interested in exactly what can go wrong with regards to translating a DTT proof into ZFC

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167648):
right, there are large universes in the proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167651):
Because one day someone serious is going to ask me about this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 27 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167652):
DTT

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 27 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167653):
?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167654):
so that wouldn't translate

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167655):
However, this sort of sleight of hand is very rare

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167656):
And the problem is that the proof might not be mine

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167657):
The theorem could be formulated about Type in some library

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 27 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167658):
so they work in a system stronger than ZFC?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 27 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167660):
like how PA can't prove Goodstein?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167661):
and I never look at the proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167699):
Yes Kenny

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167704):
they work in ZFC + infinitely many inaccessible cardinals here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167707):
It's infinitely less likely to be consistent than ZFC

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167709):
which is weaker than Tarski Grothendieck set theory btw

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 27 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167710):
Grothendieck?!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167713):
which is what most category theorists use

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167718):
That is equivalent to ZFC + proper class of inaccessible cardinals

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167720):
here we only need omega many

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 27 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167723):
fascinating

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 27 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167725):
logic never fails to fascinate me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167726):
and for any particular proof you can say "this used 3 universes" or such

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167767):
it's impossible to use all the universes in a proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167768):
But I am specifically interested in the proofs which only use one universe

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167769):
For example does FLT definitely only use one universe?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167771):
well, actually you want zero universes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167772):
Oh yes I just want Type

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167773):
ZFC has zero universes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 27 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167776):
```quote
ZFC has zero universes
```
zero built-in universes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167781):
So currently the reference for "Wiles/TW proof of FLT is in ZFC" is "Email from Conrad"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167782):
It's a bit tricky to work with DTT with zero universes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167783):
Why?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167784):
Say I globally exchange all the type u for type

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167786):
how far do I get before the errors appear?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167831):
Start with core lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167834):
you have to be careful: `Gamma |- A : Type` is okay, but `Type` is not a type, in the sense `Gamma |- Type : Type 1` doesn't exist

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167836):
Yeah, I promise I will never ask Type its type.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167837):
ZFC people are used to making promises

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167838):
and they're usually quite good at keeping them

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167845):
This is the world I have lived in all my life

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167846):
and you are claiming to offer me more

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167847):
Also you can have things like `A : Type -> Type` in ZFC

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167848):
but I don't see anything of interest out there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167850):
but again you can't quantify over them

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167851):
Yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167852):
no

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167891):
oh wait

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167894):
I can quantify over them

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167895):
`A : (Type -> Type) -> Type` is starting to get weird

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167899):
`A : Type -> Type` is a proper class function

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167900):
I just have to write some footnote explaining about how it can all be done properly if you ask a set theorist

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167902):
because no object I consider in my paper has size greater than 2^2^2^2^aleph_0 so it's all OK

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167903):
who needs inaccessible cardinals

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167909):
I just something closed under a few iterations of the power set axiom and I'll be fine

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167910):
That's really hard to do formally

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167913):
There will be people out there who care about this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167916):
at least if you didn't literally do that in the proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167918):
Right, and who wants to do that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167919):
We just wanna have fun

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167961):
I don't see any reason why ZFC should stay as the prevalent model of mathematics

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167962):
What you want is a way to take a proof and shrink all the things in it to ZFC things

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167964):
but without a doubt it is the prevalent model of mathematics

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167965):
I don't

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167968):
but some people might

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167969):
and I have them in mind

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167973):
or 2^2^2^2^aleph_0 things

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167984):
and it's my job to figure out how to make sense of your request

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127167989):
There are theorems of the form "if you proved X using 3 universes then you could have done it in ZFC" I think

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168008):
I think someone might have told me that even though wiles *certainly* used AC in his proof, FLT was now known to be a theorem of ZF

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168036):
because one of these magic meta-theorem things

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168042):
yes, it's a pi01 statement so magic happens

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168485):
here's the sheaf axiom using the poset presheaf definition:
```
def gluing {α} [complete_lattice α] (F : order_presheaf α) 
  (X : α) {ι : Type*} (Y : ι → α) (Hcov : X = ⨆ i, Y i)
  (r : F.F X) :
  {a : Π i, F.F (Y i) | ∀ (i j : ι), 
    F.res (Y i ⊓ Y j) inf_le_left (a i) = 
    F.res (Y i ⊓ Y j) inf_le_right (a j) } :=
⟨λ i, F.res (Y i) (by rw Hcov; apply le_supr) r,
 λ i j, by simp [F.comp]⟩

def is_order_sheaf {α : Type u} [complete_lattice α]
  (F : order_presheaf α) : Prop :=
∀ (X : α) {ι : Type u} (Y : ι → α) (Hcov : X = ⨆ i, Y i),
function.bijective (gluing F X Y Hcov)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168542):
Did you look at what I did?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168543):
yes, it was based on your definition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168545):
ha ha hope I didn't make a mistake :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168585):
I think probably `bijective` makes more axioms than you really need here

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168586):
like it's probably already injective

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168592):
I would just state the actual condition you want, and prove it implies this function is bijective

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168644):
https://stacks.math.columbia.edu/tag/009I

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168648):
Actually I guess I just copied everything from the stacks project (and spotted a mistake or two along the way :-) )

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168688):
no, injective needs checking

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168689):
A presheaf is just a functor

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168690):
It takes an open set to a type

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168694):
I could easily replace its value on X with some gigantic type that maps to the old  value

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168700):
If you think of them as sheaves of functions then injectivity may well be obvious

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168702):
but this is a true pi type -- it takes an open set to a random type, not functions on U or anything

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168739):
and res is part of the data, not restriction of functions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168747):
So are you interested in putting this presheaf and sheaf stuff in mathlib?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168749):
I'm not bothered either way

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168750):
but it is compositional

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168753):
yes but that's an axiom

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168754):
one of the two axioms of functor

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168756):
Of course, I'm assuming it's a presheaf already

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168757):
gotcha

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168797):
I don't know whether I should bother tidying everything up

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168798):
I mean the condition of being a sheaf can be stated more directly given it's a presheaf

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168799):
right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168801):
but you still don't get injectivity for free

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168802):
because I can replace F X

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168805):
with with a random type Y that mapped to the old F X

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168806):
X the whole space

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168809):
and then it's still a presheaf

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168813):
but there's no reason Y -> old F X is injective

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 27 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127168814):
so I broke the sheaf property precisely by breaking injectivity

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (May 28 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/valuations/near/127191991):
@**Kevin Buzzard** Re: `@[simp]` and left-to-right rewriting, perhaps, by browsing through the `@[simp]` theorems in [this file](https://github.com/spl/tts/blob/32df31590e3f7a88eeea6d672981ac1de93c0af7/src/env/props.lean), you can get an idea of why they are structured the way they are.

