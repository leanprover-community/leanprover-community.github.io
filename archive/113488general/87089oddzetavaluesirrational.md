---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/87089oddzetavaluesirrational.html
---

## Stream: [general](index.html)
### Topic: [odd zeta values irrational](87089oddzetavaluesirrational.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 08 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/odd%20zeta%20values%20irrational/near/123436696):
https://arxiv.org/abs/1802.09410 just popped up on ArXiv today. Needs prime number theorem as input but proves something which people have been wondering about for centuries. First proof was about a decade ago and used a lot of machinery; this one only uses prime number theorem and some combinatorics (and a bunch of good ideas).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Assia Mahboubi (Mar 09 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/odd%20zeta%20values%20irrational/near/123484974):
Hi @**Kevin Buzzard**, I stumbled upon that one  too. It looks really cool. A few years ago we verified the irrationality of zeta(3) in Coq and I hope that someone will be able to verify this one as well now that it's known to be elementary enough. For what it's worth you need slightly less than the prime number theorem but a coarser, $$O(3^{n})$$, estimation of the asymptotic behaviour of lcm(1...n), which can be obtained by much more elementary means. Sprang's proof also uses Stirling's formula though (which should not be too difficult to get, much less so that the prime number theorem).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Mar 09 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/odd%20zeta%20values%20irrational/near/123507005):
How do you know this paper is serious? The first sentence "In this small note, we provide an elementary proof of the fact that infinitely many odd zeta values are irrational." reads very much like crackpot science. Do you know the author or understand the new ideas he uses?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 10 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/odd%20zeta%20values%20irrational/near/123514425):
I don't know for sure, but I know something about the area and the story seems plausible. Let me stress that I have not read the paper myself.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Assia Mahboubi (Mar 14 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/odd%20zeta%20values%20irrational/near/123697736):
Hi @**Patrick Massot** . The title of the paper is a pun based on the title of a very recent paper by Zudilin (who is one of the world experts on this question of irrationality of zeta at the odds): "One of the odd zeta values from zeta(5) to zeta(25) is irrational. By elementry means".

I do not know the author, nor have I finished reading the note, but his claim is that the ideas proposed by Zudilin in the latter paper can prove this infinity result, by the means of a rather natural generalization of Zudilin's innovations. Finally, the important word here is "elementary": the result was known already, and the proof is not constructive so we still do not know which explicit odd has an irrational value, except 3 and one among 5,7,9 and 11.


{% endraw %}
