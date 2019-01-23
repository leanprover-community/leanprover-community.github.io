---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/34767Suggestionsformathscomputingprojects.html
---

## Stream: [maths](index.html)
### Topic: [Suggestions for maths/computing projects](34767Suggestionsformathscomputingprojects.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 29 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134880233):
In the UK the system is that the undergraduates come into university having chosen their major and can only do classes offered by the corresponding department(s). The third year undergraduates doing a joint maths/computing degree hence know quite a bit of maths and CS. I have been asked to suggest possible projects for these students. No other pure mathematicians ever get involved. If anyone has any suggestions for projects they they think might be appropriate then I would be very interested to hear them.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 29 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134880247):
I think 4th years can also take them so MSc level is ok

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 29 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134880308):
I will suggest a homological algebra project and a project to make `math.rat`, a class for rational numbers which behaves like a number theorist thinks -- eg you can talk about a math.rat being prime or induct on it if it's known to be a nat etc

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 29 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134880349):
I'll suggest a number field / Galois theory project maybe

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 29 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134880351):
I'm not sure why you need another type, like I mentioned before

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 29 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134880360):
But if there's anything mathsy that anyone wants done then let me know quick

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 29 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134880363):
just define the typeclasses `is_nat_prime`, `is_nat`, `is_rat` on any nice type

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 29 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134880399):
Mario are you ok with a typeclass `is_nat q` on rat in mathlib?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 29 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134880406):
I think it should be generic in the type

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 29 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134880409):
I thought you had reservations about the `Prime` typeclass

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 29 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134880410):
On nat

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 29 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134880413):
it says `\ex n, nat.cast n = x`, in whatever generality that statement makes sense

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 29 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134880419):
Is it ok if it's data?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 29 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134880421):
sure

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 29 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134880463):
the name `is_nat` is a bit misleading in that case, but I don't have a better suggestion

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 29 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134880464):
at least it's a subsingleton (in char 0)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 29 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134880466):
is_of_nat?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 29 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134880475):
math.nat?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 29 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134880523):
I don't think I want to ever use `math` as a namespace

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 29 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134880526):
if you do that it's like "wait, what were we doing before?"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 29 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134880527):
`the_real_nat`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 29 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134880534):
what about `natural`, `integral` etc?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 29 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134880547):
like "x is a natural element of A"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 29 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134882048):
How big a project are we talking about? Have you checked https://github.com/leanprover-community/mathlib/wiki/Potential-projects for ideas?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 29 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134882089):
One item I'd like to see that hasn't made it onto that list is covering space theory

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 29 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134882161):
I actually went to some effort to do covering space theory in metamath a while back. The big theorem was existence and uniqueness of lifts; it was hard to find an appropriately general statement so it might be of use

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 29 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134882219):
But we need simply connected and path connected spaces first

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 29 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134882222):
also connectedness

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 29 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134882469):
On an unrelated note,
```quote
just define the typeclasses `is_nat_prime`, `is_nat`, `is_rat` on any nice type
```
some lemmas like `@[simp] lemma pos_of_is_nat_prime (p : rat) [is_nat_prime p] : p > 0` would make this padic norm stuff go a lot more smoothly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 29 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134882927):
though maybe this doesn't really require the class--I'm still unclear on how exactly simp tries to satisfy side conditions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Sep 29 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134882928):
Even just an `is_prime` class on `nat` would clean up the padic file a lot. Mario and I discussed this briefly in the first padics PR. I was planning to experiment with it soon.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 29 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134882983):
I am considering just marking `prime` itself as a class, without changing the theorems

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 29 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134883042):
One of my students wrote 1000 lines of Lean code on connectedness

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 29 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134883045):
and never really bothered to mention this to anyone

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 29 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134883051):
https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/Topology/Material/connected_spaces.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Sep 29 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134883114):
@**Mario Carneiro** That would certainly work. I wonder if we'd eventually end up duplicating the statements of the theorems with versions that take instance arguments though.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 29 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134883181):
```quote
How big a project are we talking about? Have you checked https://github.com/leanprover-community/mathlib/wiki/Potential-projects for ideas?
```
Maybe a term, maybe a year, and no I didn't check that -- thanks!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Sep 29 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134883196):
@**Kevin Buzzard** We've had a few CS undergrads come to us looking for BS thesis projects and put together a short list for them. If you have students looking for projects more aligned toward programming/tactics than formalizing, we can share.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 29 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134883282):
By the way, that connectedness file finishes with a big TFAE proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 29 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134884436):
@**Kevin Buzzard** How about quadratic forms over Q? Maybe that is too big. But Hasse-Minkowski would be really cool. And we have QR now...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 29 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134884476):
And p-adics, and Hensels lemma... so I think a lot of prerequisites are in place.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 29 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134885324):
What about doing more elementary stuff?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Tobias Grosser (Sep 30 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Suggestions%20for%20maths/computing%20projects/near/134926064):
I am very interested in having functionality similar to: http://ssr.msr-inria.inria.fr/doc/mathcomp-1.5/MathComp.mxalgebra.html


{% endraw %}
