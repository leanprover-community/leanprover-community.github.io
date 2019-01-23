---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/67390quadraticreciprocitygraph.html
---

## Stream: [general](index.html)
### Topic: [quadratic reciprocity graph](67390quadraticreciprocitygraph.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134058821):
Chris just sent me a text file of all the theorems used in his proof of quadratic reciprocity

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134058869):
[quadratic_reciprocity.txt](/user_uploads/3121/V5O2ze1stMrqhYQNQydKuqvL/quadratic_reciprocity.txt)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134058872):
Maybe @**Chris Hughes**  can explain what this file represents while I spend 5 minutes doing emacs hackery on it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134058882):
but in 10 minutes' time we're going to have this in GePhi

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 16 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134058932):
who is gephi?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 16 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134058935):
Chris I'd very interested to know why you duplicate this meta-effort. If you don't like what I wrote in https://github.com/leanprover-community/leancrawler you can improve it, or propose a brand new stuff.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 16 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134058938):
https://gephi.org/

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 16 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134058947):
It's a `list (name × list name)`. Each element of the list is a `declaration` used in the proof and the list of depth one dependencies.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 16 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134058949):
The same graph visualization format my crawler natively writes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 16 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134058952):
I duplicated it to learn how to write `meta` mainly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 16 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134058959):
Your meta code may be better than mine, you could contribute it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 16 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134059000):
Learning meta stuff was also one of my main motivations

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134059007):
I've got it working

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 16 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134059012):
It does slightly different things from yours

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134059013):
[quadratic_reciprocity.csv](/user_uploads/3121/N1FVZyB30X5bFl3Tw6A1_EDy/quadratic_reciprocity.csv)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134059022):
I've never used gephi before in my life but it's very intuitive. The hard work is done.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134059064):
open GePhi, click on "open graph file", select that csv file

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134059073):
make sure "separator" is set to semicolon, "import as" is set to "Adjacency List" and "Charset" apparently should be UTF-16LE (blame chris for this)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134059118):
then Window -> Graph and you have a graph of the proof of quadratic reciprocity in Lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134059121):
and 10 gigs less of free ram

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134059189):
In the "statistics" section you can do a bunch of tests and compute things, and those run fine, it's just the visualisation stuff that really hammers the CPU

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134059211):
Diameter is 24, which I guess means that that's the longest chain of dependencies (25 definitions I guess)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134059251):
[chaos.png](/user_uploads/3121/hZZB39E4kv_LHQ8xY8yys-dY/chaos.png)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134059253):
It's still trying to see the wood from the trees

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 16 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134059321):
Did you use the Force 2 layout?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 16 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134059361):
You need to push the scale parameter

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 16 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134059379):
Most of the very high valence vertices seem to be the usual suspects (eq, eq.rec...)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 16 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134059413):
has_mem and friends, has_zero...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134059662):
oh -- force 2 uses all the threads!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134059663):
Oh that's much better

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 16 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134065462):
[QR.png](/user_uploads/3121/ZIxA3pfZ9pcVlAK1Wd8IaGot/QR.png)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134065843):
That's a proof of quadratic reciprocity!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 16 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134065896):
You can spend hours fiddling with all the options on that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134066752):
[qr2.png](/user_uploads/3121/8Wzwd0qZKOxY52vR2VrHTRh_/qr2.png)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134066793):
yeah. Yours is nice and arty :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 16 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134066801):
lol I guess it doesn't lend itself well to word cloud format

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134066865):
[QR3.png](/user_uploads/3121/AjrtdEkiMh0ZVvx2aZkHKhp3/QR3.png) You can see the words a bit better if you zoom in

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 16 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134066906):
I notice that all the biggest things are typeclass instances

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134066909):
`Nice to see polynomial.integral_domain._proof_12` there.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 16 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134066913):
what am I looking at?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134066914):
Node size is based on "betweenness centrality"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134066915):
and font size is proportional to node size

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 16 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134066956):
I'm afraid I can't guess what that means

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Sep 16 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134066965):
There's apparently a whole [wikipedia page  on it](https://en.wikipedia.org/wiki/Betweenness_centrality).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134066977):
[degree.png](/user_uploads/3121/RnxBANmJ2Yoxrv_VVQ-ck_ac/degree.png) size now proportional to degree of node

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134067075):
OK last one, with size proportional to out-degree -- completely different. [QR4.png](/user_uploads/3121/WBULe2a2A5SozefrvDmtCRc0/QR4.png) Thanks so much to @**Patrick Massot** for pointing me to GePhi. It's really easy to use. Patrick's scripts even create a graph in GePhi format -- Chris sent me a list of edges and I had to do some emacs hackery to turn it into an appropriate format.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Sep 16 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134067187):
I know very little about quadratic reciprocity and this proof, but for those who do, in your opinion, what should be the biggest nodes in terms of "mathematical importance", i.e. the "key steps"?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 16 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134067500):
The key steps are polynomials of degree n over an integral domain have at most n roots, Lagrange's theorem in group theory, cyclicness of units of finite field, the fact that integers mod p are a field. After that it's more or less just annoying manipulations of products that have no relevance outside of this proof.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 16 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134067616):
> it's really easy to use

Unfortunately it's not quite true. It's really easy to have fun with, like you and I did. But the purpose of this software is to actually get information from the graph, either visually or in tables. And this is much harder.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068463):
I think that Gauss knew all of the facts that Chris quoted when he formulated the law, but it took him years to find the proof. Perhaps because in some sense the proof isn't conceptual -- or at least the proofs Gauss found weren't. Now we can deduce it from more general reciprocity laws which do have conceptual proofs, but to formalise those proofs we need some basic algebraic number theory first (factorisation of ideals into prime ideals in the integers of a number field).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 16 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068468):
https://github.com/leanprover/mathlib/issues/40

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 16 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068516):
[screenshot_232944.png](/user_uploads/3121/vZjqKnNises6zhwJQRTU1Rte/screenshot_232944.png)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068517):
We could do that in 10 minutes flat Kenny if you were interested

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 16 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068520):
This is probably a more readable graph

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068526):
However we wouldn't be able to prove anything about them, it would just be a PR stunt

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 16 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068533):
do what in 10 minutes?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068535):
Is the middle dot `eq`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 16 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068536):
It's limited to mathlib (not core), all declarations used in quadratic reciprocity (big dot in the center) but not recursors or other auto-generated stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068575):
Oh

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068577):
Is the middle dot QR then?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 16 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068578):
Yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 16 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068581):
[qr.gephi](/user_uploads/3121/UWID5NbYAEpuHVIMWfhm0fTg/qr.gephi)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068584):
Define adeles in 10 minutes. Adeles of K are adeles of Q tensor K.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 16 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068588):
aha

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068592):
Adeles of Q are just restricted product of p-adics

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068593):
And the reals

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 16 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068594):
and R

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 16 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068595):
Blue is definition, orange is theorem, green is instance

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068636):
Can you label some of the nodes?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 16 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068637):
Kevin, please download the gephi file. I claim it contains relevant stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 16 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068646):
Not noise

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068690):
@**Bryan Gin-ge Chen** quadratic reciprocity does not follow easily from these standard facts that Chris quoted. The hard part is putting everything together in a subtle way. I wonder how long a computer would take to prove it just given the standard facts. I suspect a long time. As Chris said, you end up doing some delicate counting with some intermediate lemmas that you never use again for anything else

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068793):
The conceptual proof uses the fact that if $$p\equiv1$$ mod 4, then $$\mathbb{Q}(p^{1/2})\subseteq\mathbb{Q}(\zeta_p)$$ where $$\zeta_p=e^{2\pi i/p}$$

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 16 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068801):
and then doing a lot of non-trivial stuff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 16 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068802):
Even better: a version removing any declaration whose name contains "coe" or "cast" (which is noise from a mathematical point of view) [qr.gephi](/user_uploads/3121/WiWuTI0G5fM74Vd8TIbSO6FY/qr.gephi)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068803):
The factorization of a prime number $$q$$ in $$\mathbb{Q}(p^{1/2})$$ is governed by whether $$p$$ is a square mod $$q$$

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 16 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068804):
[screenshot_234141.png](/user_uploads/3121/MzakNFD8LM3qNGgIlSgA6br0/screenshot_234141.png)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068844):
but the factorization in $$\mathbb{Q}(\zeta_p)$$ is determined by the behaviour of $$q$$ mod $$p$$ and there's the link.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 16 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068855):
In this last version you can actually browse the graph and see what's there

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068856):
This proof historically came much later though. It then goes on to become Artin reciprocity in the early 1900s, which then gets generalised to Langlands reciprocity, a statement sufficiently vague that nobody knows what it is.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068857):
But we know it when we see it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068897):
We just can't state it precisely.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068900):
Patrick is it easy to say what the definitions and instances are?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 16 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068912):
one should ask

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 16 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068913):
Do you want lists of definitions, or do you want to know which color is what?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 16 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068914):
is Chris's proof a proof?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068916):
Not of Langlands reciprocity, but probably of quadratic reciprocity.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 16 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068957):
should proofs give us some understanding about *why* it is true?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068958):
I was wondering what the names of the small list of things that weren't theorems were. I can look tomorrow. I'm just off to bed.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068959):
```quote
should proofs give us some understanding about *why* it is true?
```
That's so 1900s.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068961):
If it happens, it's a bonus. If it doesn't, rotten luck.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 16 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068963):
Kevin, in gephi, if you go to tab probably called "data lab" (guessing from my French speaking version), you can sort by type of node

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134068964):
It's like asking if food which is good for you should taste nice.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 16 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134069014):
But of course I can also ask the python shell. Definitions are:
```
['finset.univ',
 'fintype.fintype_prod_right',
 'nat.modeq',
 'multiset',
 'nat.prime',
 'zmodp',
 'fintype.fintype_prod_left',
 'zmod',
 'fintype.card',
 'zmodp.legendre_sym',
 'fintype.of_equiv',
 'multiset.card',
 'multiset.map',
 'set_fintype',
 'order_of',
 'nat.decidable_prime_1']
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 16 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134069024):
instances:
```
['zmodp.comm_ring',
 'list.perm.setoid',
 'zmod.has_neg',
 'zmod.add_comm_semigroup',
 'zmod.has_zero',
 'zmodp.decidable_eq',
 'fintype.decidable_exists_fintype',
 'zmodp.discrete_field',
 'zmod.has_one',
 'zmodp.fintype',
 'fin.fintype',
 'fintype.decidable_forall_fintype',
 'decidable_gpowers',
 'zmod.comm_ring',
 'fintype.subsingleton',
 'prod.fintype',
 'nat.decidable',
 'zmod.fintype']
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 16 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134069071):
and I should also go to bed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 16 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134069230):
there's something wrong with me if Patrick consistently goes to bed earlier than me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134069272):
I am not sure that Gauss's proofs of quadratic reciprocity gave us any understanding of why the theorem is true. The arguments are sufficiently elementary to be easily checkable by a third year undergraduate but at the end of the day it's a big motivationless computation of eg the number of dots in a rectangle counted in a weird way

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134069273):
What insight does that give us?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 16 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134069275):
I can confirm the part about third year undergraduate

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 16 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134069278):
I was in the very course

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 16 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134069285):
You went to Toby's lectures?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 16 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134069287):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 17 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134069345):
And the student was right :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 17 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134069346):
I got some of the summer students to formalise his example sheet questions and after a few hours one of them came up to me and told me that the first part of the first question was false :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 17 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134069347):
Which proof did he give? The Hardy and Wright one?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 17 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134069387):
the rectangle one

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 17 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134087595):
```quote
there's something wrong with me if Patrick consistently goes to bed earlier than me
```
It's called "you are not a parent and don't have a job" -- I'm not sure that this qualifies as something wrong with you, it just means you're young.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 17 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134087882):
But back to the point I've been thinking more about quadratic reciprocity. What insight does that stupid rectangle proof give you? It's of the form "divide the rectangle up into about 6 regions, prove some boring lemmas about the number of points in each region, add everything up, deduce quadratic reciprocity". I am not at all sure that it gives you any insight into why the theorem is true at all. Chris gave an excellent summary of the proof -- "invoke some standard lemmas and then do a completely unmotivated computation about an apparently unrelated rectangle, and it happens to drop out". Kenny -- you probably followed Toby's proof -- can you then give me a succinct one-line summary as to why an odd prime p is a square mod 13 if and only if 13 is a square mod p? That assertion on the face of it looks like the ramblings of a madman -- those statements clearly have nothing to do with each other. The proof is entirely non-constructive as well (of course -- actually computing the square root of 13 mod p is computationally hard if p is huge, whereas computing a square root of p mod 13 is trivial). Is the rectangle proof really a proof? I read it and read it, and I still have no idea "why" the theorem is true.

Looking at it now, that proof of quadratic reciprocity looks pretty much the same as the four colour theorem proof to me -- that proof goes something like: divide the problem up into around 2000 graphs, prove a lemma about each graph, put everything together. And yet people regard quadratic reciprocity as a brilliant thing and the 4 colour proof as something which gives no insight. Are we just being blinded by the fact that 6 is less than 2000?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Sep 17 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134087952):
```quote
Are we just being blinded by the fact that 6 is less than 2000?
```
Yes, we are!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 17 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134097189):
Wasn't there some "one-sentence" proof which showed an equation (maybe writing a prime 1 mod 4 as the sum of two squares?) has a solution by exhibiting an involution on some set of tuples of integers whose fixed points were solutions to the equations, and then exhibiting a second involution on the same set which obviously had a unique fixed point (or maybe an odd number of them)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 17 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134097214):
Yes. Here it is in lean https://github.com/dorhinj/leanstuff/blob/master/fermat_sum_two_squares.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 17 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134098431):
This is Zagier's "one line proof" that a prime which is 1 mod 4 is the sum of two squares. Since then a slightly simpler involution argument has been found: see https://www.sciencedirect.com/science/article/pii/S0012365X15004355 (possibly behind a firewall).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 17 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134098479):
Zagier's proof is here: https://www.jstor.org/stable/2323918?origin=crossref&seq=1#metadata_info_tab_contents

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 17 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134098763):
Yes this is the one I was thinking of. Nice!
I wonder how many of these verifications could be done automatically with a tool like Z3. Obviously it wouldn't be able to do the steps which use the fact that p is prime, but those cases could be handled manually and then fed in as additional hypotheses.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 17 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134099135):
I would be very interested in hearing people's opinion on to what extent this is possible.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 17 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134099150):
Any mathematics which is undergraduate level -- I am interested in what state of the art proof verification software can do.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 17 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134099230):
I guess I could try some of these

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 17 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134100248):
Here's what I did so far. I didn't put in the assumption that p is prime obviously, I just stated it must be at least 5 in case that was important.
```
(declare-const p Int)
(assert (> p 4))

(declare-datatypes () ((Triple (mk (x Int) (y Int) (z Int)))))

(define-fun S ((t Triple)) Bool
  (= (+ (* (x t) (x t)) (* 4 (y t) (z t))) p))
(define-fun f1 ((t Triple)) Triple
  (mk (x t) (z t) (y t)))
(define-fun f2 ((t Triple)) Triple
  (ite (< (+ (x t) (z t)) (y t))
       (mk (+ (x t) (* 2 (z t))) (z t) (- (y t) (x t) (z t)))
       (ite (< (* 2 (y t)) (x t))
	    (mk (- (x t) (* 2 (y t))) (+ (- (x t) (y t)) (z t)) (y t))
	    (mk (- (* 2 (y t)) (x t)) (y t) (+ (- (x t) (y t)) (z t))))))

(declare-const t Triple)
(assert (S t))

(push)
(assert (not (S (f1 t))))
(check-sat)				; unsat
(pop)

(push)
(assert (not (= t (f1 (f1 t)))))	; unsat
(check-sat)
(pop)

(push)
(assert (not (S (f2 t))))		; unsat
(check-sat)
(pop)

(push)
(assert (not (= t (f2 (f2 t)))))
(check-sat)				; sat

(declare-const t1 Triple)
(assert (= t1 (f2 t)))
(declare-const t2 Triple)
(assert (= t2 (f2 t1)))

(check-sat)				; sat
(get-model)				; p = 9, t = (3,1,0), t1 = (1,2,1), t2 = (3,2,0)
(pop)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 17 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134100272):
I learned that to prove f2 is an involution on S I need some further condition--looking at Chris's proof it's these checks that x, y, z have to be positive.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 17 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134100436):
Now I replaced the last section by
```
(push)
(assert (not (= t (f2 (f2 t)))))
(assert (> (x t) 0))
(assert (> (y t) 0))
(assert (> (z t) 0))
(check-sat)                             ; unsat
(pop)
```
so x y z positive is enough to prove it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 17 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134100519):
You only need that p is not square for x y z positive. Can you weaken the condition to that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 17 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134100590):
I didn't even say that p is prime or what it is mod 4 yet

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 17 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134100594):
Oh, I see.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 17 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134100598):
Hm...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 17 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134100625):
I'm not sure if I can encode "p is not square" in a helpful way

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 17 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134100756):
I tried `(assert (forall ((n Int)) (not (= p (* n n)))))`, but now Z3 seems to be running forever on the fourth check

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 17 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134100888):
Oh, I also missed part of the definition of S

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 17 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134100944):
okay, now it can actually do the fourth part with `(assert (forall ((n Int)) (not (= p (* n n)))))` and with the nonnegativity included in the definition of S

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 17 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134101038):
For f2 having a unique fixed point, it can prove (if I ask it to) that for a fixed point, we must have x = y

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 17 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134101232):
Here's the whole thing https://gist.github.com/rwbarton/440ef225da3c243c1c03028d5d32f87b

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 17 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134101304):
I guess maybe I can express not prime too, then

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 17 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134101319):
Or being prime, rather

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 17 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134101785):
Updated: https://gist.github.com/rwbarton/440ef225da3c243c1c03028d5d32f87b
If I tell it p is prime, it can check the first four facts and it can still prove that a fixed point of f2 must satisfy x = y but it can't deduce that x = y = 1. I guess it doesn't hit on the idea of using distributivity

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 17 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134102026):
I can't get `(set-option :produce-proofs true)` to do anything, not sure whether I am using it wrong or whether Z3 just doesn't want to produce proofs for the theory of integer arithmetic

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 17 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134102470):
oh you have to ask it for the proof explicitly as well

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 18 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134134218):
Kevin I would say that the partitions proof no longer has any steps which I would want out to Z3. At least not very large ones.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 18 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134134278):
I think I could explain it to someone at the board and there aren't really any mysterious computations happening.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 18 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quadratic%20reciprocity%20graph/near/134134314):
Whereas the Zagier proof has a couple ring computations to do plus various facts about linear inequalities to check

