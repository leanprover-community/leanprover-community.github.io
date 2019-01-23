---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/60703CSstuff.html
---

## Stream: [general](index.html)
### Topic: [CS stuff](60703CSstuff.html)

---


{% raw %}
#### [ Simon Hudon (Aug 30 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133077454):
I wrote a package for serialization in Lean. Is this something people would like to have in `mathlib` or the nursery?

#### [ Patrick Massot (Aug 30 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133083162):
It serializes from what to what?

#### [ Simon Hudon (Aug 30 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133083394):
If you have a data structure that you want to write to the disk or to a network you can create a `serial` instance (which can be derived) to convert from and to a series of bytes.

#### [ Simon Hudon (Aug 30 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133083434):
So the short answer is, it serializes (and deserializes) from your data structure to a series of bytes (and back)

#### [ Simon Hudon (Aug 30 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133083496):
I haven't built any support for XML or JSON but that can be future work.

#### [ Simon Hudon (Aug 30 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133083648):
(and `serial` includes a proof of correctness of the serialization process)

#### [ Simon Hudon (Aug 30 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133084768):
Added benefit: if you insist on writing your own serializer, you get to use my `there_and_back_again` function in the proof of correctness. :D

#### [ Andrew Ashworth (Aug 31 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133101706):
Hmm, I would vote for serialization being in its own package.

#### [ Simon Hudon (Aug 31 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133101756):
Interesting. Is it because of the possibility of having multiple alternative to that library or is it too CS for mathlib?

#### [ Andrew Ashworth (Aug 31 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133101758):
I think the advantage of mathlib here is that it's a maintained, curated package that lots of people know about... and since there is no well known programming stdlib, that would be one reason to stick it in there

#### [ Andrew Ashworth (Aug 31 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133101766):
but i think instead that just means we should go for a cslib instead

#### [ Andrew Ashworth (Aug 31 2018 at 06:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133101832):
i'm not sure most people doing math will need exotic data structures, network comms, parsing libraries, graph algorithms, etc

#### [ Johan Commelin (Aug 31 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133101847):
graph algorithms :check_mark:

#### [ Johan Commelin (Aug 31 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133101860):
The rest, we'll need for automation...

#### [ Simon Hudon (Aug 31 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133101865):
That makes sense. There is a weird dependency that I can see between math and CS in formal proofs. Logic, sets and natural numbers are the most fundamental but then good programming tools are useful for writing tactics that more advanced mathematical proofs use.

#### [ Simon Hudon (Aug 31 2018 at 06:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133101912):
I can see parsing libraries and graph algorithms as potentially useful for more advanced proof automation

#### [ Johan Commelin (Aug 31 2018 at 06:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133101922):
I view graph algorithms as part of combinatorics, and hence part of maths... maybe I'm weird.

#### [ Simon Hudon (Aug 31 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102017):
I think graphs are relevant both in discrete math and in computer science. For the structure of Lean libraries, even more important is what it uses and what uses it

#### [ Simon Hudon (Aug 31 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102034):
I could actually see mathlib becoming three libraries: logic + discrete math, programming and tactics, advanced math

#### [ Andrew Ashworth (Aug 31 2018 at 06:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102152):
i think for more practical minded users a more useful split would further divide advanced math into linear algebra, fourier analysis, prob/stats, and then everything else. of course this would be a day far far in the future

#### [ Johan Commelin (Aug 31 2018 at 06:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102213):
I think Simon's first two suggestions might be too interdependent, not?

#### [ Simon Hudon (Aug 31 2018 at 06:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102214):
I can see the sense in doing that. I also like having a lot of it under one roof so that they can be curated together.

#### [ Simon Hudon (Aug 31 2018 at 06:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102269):
I lost track ... which ones are those?

#### [ Johan Commelin (Aug 31 2018 at 06:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102270):
discrete math will want to use tactics

#### [ Johan Commelin (Aug 31 2018 at 06:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102280):
and tactics need discrete math and logic

#### [ Johan Commelin (Aug 31 2018 at 06:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102282):
etc

#### [ Johan Commelin (Aug 31 2018 at 06:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102324):
In that sense, I think I don't care about a huge monolith

#### [ Johan Commelin (Aug 31 2018 at 06:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102333):
The alternative is that everything goes into its own tiny little package, npm style

#### [ Simon Hudon (Aug 31 2018 at 06:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102334):
That's true. I think some basic tactics need to be intertwined with logic + discrete math.

#### [ Johan Commelin (Aug 31 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102340):
And some advanced ones!

#### [ Johan Commelin (Aug 31 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102344):
We were talking about `rewrite_search` and using `A*` for it.

#### [ Johan Commelin (Aug 31 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102346):
But maybe it should roll its own A*

#### [ Simon Hudon (Aug 31 2018 at 06:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102396):
I think we're going to see that a lot that some specialized mathematics / CS will need to roll its own automation.

#### [ Simon Hudon (Aug 31 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102407):
```quote
But maybe it should roll its own A*
```
I would rather not: one benefit of using a A* package is that optimizations can be added and studied and the automation can benefit from it.

#### [ Mario Carneiro (Aug 31 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102448):
Do I need to show you the slide in my mathlib talk where I talk about the CS and math goals of mathlib? Or the part where it used to be called stdlib until leo changed the name to differentiate it from corelib?

#### [ Mario Carneiro (Aug 31 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102458):
mathlib is absolutely a place for cs stuff

#### [ Mario Carneiro (Aug 31 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102463):
it's only sparse on cs stuff now because there are a bunch of mathematicians on the project

#### [ Johan Commelin (Aug 31 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102466):
Hahaha

#### [ Simon Hudon (Aug 31 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102468):
I wouldn't want to argue with you but I would love to see your slides ...

#### [ Johan Commelin (Aug 31 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102510):
So... who's going to formalise TAOCP?

#### [ Simon Hudon (Aug 31 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102513):
*whistles and looks elsewhere*

#### [ Mario Carneiro (Aug 31 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102514):
https://goo.gl/DifCWB

#### [ Johan Commelin (Aug 31 2018 at 06:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102515):
Lol, I just realised that the Bourbaki of CS is just 1 person...

#### [ Simon Hudon (Aug 31 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102694):
I can see a lot of CS going into mathlib but I wonder if networking and the like fits in as it may not support the math

#### [ Andrew Ashworth (Aug 31 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102696):
Knuth is kind of a big deal like that...

#### [ Andrew Ashworth (Aug 31 2018 at 06:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102707):
Nobody knows if he'll finish all of his planned volumes of TAOCP

#### [ Johan Commelin (Aug 31 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102753):
```quote
but I wonder if networking and the like fits in as it may not support the math
```
Of course it will! We will have Lean instances talking with each other, trying to prove things together!

#### [ Simon Hudon (Aug 31 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102775):
I'm sold!

#### [ Mario Carneiro (Aug 31 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102776):
certainly IO stuff is useful for proof work

#### [ Mario Carneiro (Aug 31 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102791):
i.e. connecting to mathematica or sage or Z3

#### [ Simon Hudon (Aug 31 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102822):
```quote
Nobody knows if he'll finish all of his planned volumes of TAOCP
```
I'm getting less hopeful about than than I am of seeing an end to A Song of Ice and Fire

#### [ Johan Commelin (Aug 31 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102823):
Basically, as long as you don't start formalising enumerative biology, everything goes into mathlib...

#### [ Simon Hudon (Aug 31 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102830):
Even there, I guess if I can formalize the brain of a mathematician ...

#### [ Mario Carneiro (Aug 31 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102885):
also I consider theoretical computer science math and on topic, even if some others here don't :P

#### [ Simon Hudon (Aug 31 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133104388):
Actually, I agree with this sentiment. I sense you mean it in the sense that it's a set of worthwhile mathematical problems but I also feel like it's not really relevant to computer science unless you're doing research in theoretical computer science.

#### [ Simon Hudon (Aug 31 2018 at 07:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133104403):
But back to the "let's put everything into mathlib" idea. I think one limiting factor might be the number of maintainers of mathlib.

#### [ Johan Commelin (Aug 31 2018 at 07:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133104510):
But that's not a problem yet. I think we can deal with that as soon as it becomes a real problem.

#### [ Simon Hudon (Aug 31 2018 at 07:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133104556):
I sense it becoming a problem already but maybe it's just that I don't have a good PR workflow. Maybe the nursery will improve that

#### [ Mario Carneiro (Aug 31 2018 at 07:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133104568):
fewer maintainers just means a longer wait for your PR to be merged, it's not a structural problem

#### [ Mario Carneiro (Aug 31 2018 at 07:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133104610):
but also I expect that there will be more maintainers available if/when lean gets really big

#### [ Simon Hudon (Aug 31 2018 at 07:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133104677):
What I'm having a hard time with is planning the evolution of projects while considering that features will eventually be merged into mathlib.

#### [ Mario Carneiro (Aug 31 2018 at 07:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133104722):
perhaps the perfectoid project is a model?

#### [ Simon Hudon (Aug 31 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133104783):
For example, with monotonicity is a tactic I use in temporal logic and in separation logic. Making changes to respond to reviews and making changes in the version that I use sometimes get difficult to reconcile. More so before `traversable` got merged.

#### [ Simon Hudon (Aug 31 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133104785):
How do they do it?

#### [ Johan Commelin (Aug 31 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133105189):
```quote
For example, with monotonicity is a tactic I use in temporal logic and in separation logic. Making changes to respond to reviews and making changes in the version that I use sometimes get difficult to reconcile. More so before `traversable` got merged.
```
I suppose @**Scott Morrison** could also provide valuable insight in how he managed all his category libs, and got them mathlib-ready and keeps the synced, etc...

#### [ Reid Barton (Aug 31 2018 at 08:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133105737):
BTW, I have a really simple output-only json library (only on my non-working laptop)

#### [ Simon Hudon (Aug 31 2018 at 08:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133105740):
That's a non-constructive proof of existence

#### [ Simon Hudon (Aug 31 2018 at 08:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133105747):
Does it prove anything?

#### [ Simon Hudon (Aug 31 2018 at 08:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133105797):
@**Johan Commelin** Thanks! I'll talk to him about it

#### [ Reid Barton (Aug 31 2018 at 08:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133105805):
I guess it proves that string is inhabited

#### [ Reid Barton (Aug 31 2018 at 08:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133105863):
Hopefully I will be able to use my laptop again when I get home in about a week. On the other hand the library only took an hour or two to write and probably looks very much like what you would expect so you may not even want to wait for it.

#### [ Simon Hudon (Aug 31 2018 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133105974):
Actually, the hardest problem I had to solve was proving the serializers and deserializers are each other's inverse in a compositional way. In the end, I got to have a lot of fun with free monads.

#### [ Reid Barton (Aug 31 2018 at 08:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133106039):
Oh yeah, decoding json seemed quite a lot more annoying and I didn't need it.

#### [ Simon Hudon (Aug 31 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133106110):
Darn! I think the same machinery might be usable though. The only thing missing would be an embedding from JSON syntax trees to your favorite data structure

#### [ Scott Morrison (Sep 01 2018 at 04:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133159304):
@**Simon Hudon**, @**Johan Commelin**, regarding coping with merging bits-and-pieces of larger repositories into mathlib: Yes, it's hard work. :-)

#### [ Scott Morrison (Sep 01 2018 at 04:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133159352):
On the positive side, having to rewrite things over and over again to adapt to changes suggested by others has made them better...

#### [ Scott Morrison (Sep 01 2018 at 04:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133159358):
But I'm generally in agreement that pretty much everything short of enumerative biology should be heading into mathlib.

#### [ Simon Hudon (Sep 01 2018 at 04:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133159472):
Thanks :) 

How do you minimize the number of competing versions of the same package when you use that package in a project and you try to move some of the features around?

#### [ Scott Morrison (Sep 01 2018 at 04:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133159532):
I don't want to describe Mario and Johannes, as the maintainers of mathlib, as "bottlenecks", but in the long run we need to make sure that their time is not wasted (i.e. they have enough time to do the other things they need to do!), and this means working out how make reviewing and cleaning up PRs a more distributed process.

#### [ Scott Morrison (Sep 01 2018 at 04:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133159540):
I've started making my later repositories depend on my pull requests.

#### [ Simon Hudon (Sep 01 2018 at 04:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133159548):
With the nursery, that might be a cleaner solution

#### [ Scott Morrison (Sep 01 2018 at 04:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133159600):
e.g. if I split of a chunk of a project and make a PR to mathlib for it, I just update the leanpkg.toml file for that repository temporarily point to the branch corresponding to that PR on leanprover-community.

#### [ Scott Morrison (Sep 01 2018 at 04:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133159611):
This is not super safe, as branches on leanprover-community are somewhat ephemeral things. (And in particular, Mario and Johannes may well delete them after merging, and if they squash commits in some way the commit SHA you're pointing to could completely vanish.)

#### [ Scott Morrison (Sep 01 2018 at 04:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133159614):
At times last week I had a "scott-supremum" branch on leanprover-community, which was just a merge of several active PRs, so I could point my repo at that.

#### [ Simon Hudon (Sep 01 2018 at 04:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133159863):
I think you're right that we should try to distribute more of the maintenance burden. I've started pitching in for reviewing PRs but there ought to be more we can do. I sense with leanprover-community there are more opportunity we're not tapping into yet.

#### [ Simon Hudon (Sep 01 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133189901):
I just pushed my serialization stuff to the nursery. I'd love to know if people find it useful or if there are ways I can improve it. I'd like it to find its way to mathlib at some point too so if @**Mario Carneiro** and @**Johannes Hölzl** have advice, I think I'll try editing the nursery version before I create a PR.


{% endraw %}
