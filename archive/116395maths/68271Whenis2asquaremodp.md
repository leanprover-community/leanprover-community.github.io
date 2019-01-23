---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/68271Whenis2asquaremodp.html
---

## Stream: [maths](index.html)
### Topic: [When is -2 a square mod p?](68271Whenis2asquaremodp.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125797166):
Is there a proof in Lean that if `p` is a prime congruent to `5` or `7` mod `8` then `-2` is not a square mod p?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125797169):
This result drops out rather nicely from the Gauss' lemma approach

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125797173):
One counts the number of multiples of -2, mod p, which are negative

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125797178):
and it's rather easy to do

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125797183):
That's the simplest proof I know.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125797188):
I don't know of an elementary trick (in contrast to -1 and -3 which can be done by hand using roots of unity)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125797241):
https://en.wikipedia.org/wiki/Gauss%27s_lemma_(number_theory)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125797248):
Uses Euler's criterion

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125797261):
which uses that the Sylow 2-subgroup of $$(Z/pZ)^*$$ is cyclic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125797266):
which follows from `x^2-1=(x+1)(x-1)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125797325):
Assuming Gauss' lemma, then you look at the sequence $$-2,-4,-6,...-(p-1)$$

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125797340):
and mod `p` this set is the same as `1,3,5,...,p-2` (reverse the order)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125797346):
and Gauss' Lemma says that the number of elements of this sequence which are $$>p/2$$

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125797390):
is `odd` if `-2` is a non-square and even otherwise

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 05:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805619):
[2018-04-28.png](/user_uploads/3121/ek7lPaRVtdjGMhhBY2BebHzC/2018-04-28.png)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 05:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805622):
From the lecture notes of number theory (M345P14)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 05:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805623):
@**Kevin Buzzard**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 05:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805634):
That's 2

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 05:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805635):
we need -2

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 05:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805636):
oh well

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 05:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805638):
the symbol is multiplicative :P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 05:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805686):
proof by euler criterion, I hope

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 05:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805688):
that's slightly deeper than you want

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 05:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805689):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 05:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805692):
which is elementary enough?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 05:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805693):
You can generalise the link you sent me to deal with the -2 case

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 05:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805694):
I see

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 05:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805695):
and in fact the -2 case comes out slightly nicer than the +2 case

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 05:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805703):
so we consider (-2)^q q! instead?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 05:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805705):
and then after rearranging it turns out to be q!?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805857):
I can't guess what you mean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805863):
There's something called Gauss' Lemma

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805864):
and it follows from that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805865):
I think we should prove quadratic reciprocity :P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 05:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805905):
that would be call

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 05:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805906):
cool

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 05:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805908):
See if Mario already did it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 05:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805909):
I don't think it's done

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 06:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805968):
I reckon I'll need 1000 lines to do it lol

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 06:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805973):
Do it after exams and write your M1R project on it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 06:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805976):
heh...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805987):
are you sure I should use QR as project... seems quite well known

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125806517):
It would not be the first time that a 1st year undergraduate had done a project on something which some of the professors think is "quite well-known".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125806521):
On the other hand if you want to be top

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125806524):
then you have to do something hard and do it well

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125806525):
You could do affine schemes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 28 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125806527):
That would be impressive

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 28 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125806528):
lol


{% endraw %}
