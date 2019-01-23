---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/25068quadraticreciprocity.html
---

## Stream: [maths](index.html)
### Topic: [quadratic reciprocity](25068quadraticreciprocity.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 01 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125919765):
@**Chris Hughes** Did you prove Fermat's Little Theorem https://en.wikipedia.org/wiki/Fermat%27s_little_theorem in Lean? I am interested in proving Euler's Criterion https://en.wikipedia.org/wiki/Euler%27s_criterion and Gauss' Lemma https://en.wikipedia.org/wiki/Gauss%27s_lemma_(number_theory) in Lean, with a view to proving when -1 and +-2 are squares mod p (this is related to quadratic reciprocity).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 01 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125919774):
Is anything like that there already? Do we know the integers mod p are a field?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 01 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125919786):
What are good mathlib files to look at?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 01 2018 at 01:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125920424):
Oh I have it in Xena in M1F ;-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 01 2018 at 01:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125920427):
That's handy :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 01 2018 at 03:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125924429):
Are the finite rings Z/nZ in Lean? I thought a bit about how to define them and decided that constructing the quotient of Z by the equivalence relation of being congruent mod n would be a really painless way to do it because all the lemmas would probably already be there. I found many of them all for nat in `modeq` but to avoid kerfuffle with `neg` I thought that Z would be better. How much of this stuff is already done?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 01 2018 at 04:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125925147):
There is `data.int.modeq` now, too

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 01 2018 at 05:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125926213):
Oh perfect! Many thanks.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (May 01 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125932072):
I did get started on defining integers mod n. My effort is here. Some of the proofs are unfinished https://github.com/dorhinj/lean/blob/master/Zmod.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (May 01 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125932130):
I thought it would probably be better to define this stuff in a general ring / euclidean domain, not just integers, especially after I ran into a load of trouble converting xgcd from nats into ints.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (May 01 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125933136):
You mean that you want to define "ring mod ideal" in general? Or just "ring mod n"?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 01 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125933272):
```quote
You mean that you want to define "ring mod ideal" in general? Or just "ring mod n"?
```
ring mod n doesn't make much sense in general, I think

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 01 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125933274):
Sure it does, (n) is an ideal

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 01 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125933275):
but not a special one

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 01 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125933281):
n is as special as other elements in the ring

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 01 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125933324):
I've been thinking about how to unify this idea with my idea for Z/nZ as fin n with better operations. I think the best option is just to keep the developments separate (ish), with a provable isomorphism Z/nZ -> Z mod (n) where (n) is the ideal generated by n

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (May 01 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125933327):
Didn't you do it in a general ring Kenny?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 01 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125933328):
indeed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (May 01 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125933333):
Why not PR it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 01 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125933334):
reasons

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 01 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125933335):
For similar reasons to `rat`, I would not want Z/nZ to be a quotient when doing computations. This would make stuff like `a^k : Z/nZ` far too expensive

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 01 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125933336):
(it will just be an interface of `linear_algebra.quotient_module` and `ring_theory.ideal`)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 01 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125933375):
It's not completely trivial, you have to take a ring as a module over itself and then quotient by the ideal construed as a submodule

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 01 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125933380):
and then convert back to a ring

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 01 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125933381):
right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 01 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125933383):
The theorems are probably easy specializations of existing theorems, but I think the specialization is worthwhile

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 01 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125933422):
so are you saying I should build the interface?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 01 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125933423):
right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 01 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125933424):
make it so users don't have to think about modules for ring theory

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 01 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125933426):
:)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 01 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125950166):
```quote
n is as special as other elements in the ring
```
n is one of the elements you can guarantee is there in every ring, so it's special in some sense.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 01 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quadratic%20reciprocity/near/125950172):
ah, you're on about the universal ring business again


{% endraw %}
