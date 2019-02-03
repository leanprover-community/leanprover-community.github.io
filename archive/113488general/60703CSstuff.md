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
<p>I wrote a package for serialization in Lean. Is this something people would like to have in <code>mathlib</code> or the nursery?</p>

#### [ Patrick Massot (Aug 30 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133083162):
<p>It serializes from what to what?</p>

#### [ Simon Hudon (Aug 30 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133083394):
<p>If you have a data structure that you want to write to the disk or to a network you can create a <code>serial</code> instance (which can be derived) to convert from and to a series of bytes.</p>

#### [ Simon Hudon (Aug 30 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133083434):
<p>So the short answer is, it serializes (and deserializes) from your data structure to a series of bytes (and back)</p>

#### [ Simon Hudon (Aug 30 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133083496):
<p>I haven't built any support for XML or JSON but that can be future work.</p>

#### [ Simon Hudon (Aug 30 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133083648):
<p>(and <code>serial</code> includes a proof of correctness of the serialization process)</p>

#### [ Simon Hudon (Aug 30 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133084768):
<p>Added benefit: if you insist on writing your own serializer, you get to use my <code>there_and_back_again</code> function in the proof of correctness. :D</p>

#### [ Andrew Ashworth (Aug 31 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133101706):
<p>Hmm, I would vote for serialization being in its own package.</p>

#### [ Simon Hudon (Aug 31 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133101756):
<p>Interesting. Is it because of the possibility of having multiple alternative to that library or is it too CS for mathlib?</p>

#### [ Andrew Ashworth (Aug 31 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133101758):
<p>I think the advantage of mathlib here is that it's a maintained, curated package that lots of people know about... and since there is no well known programming stdlib, that would be one reason to stick it in there</p>

#### [ Andrew Ashworth (Aug 31 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133101766):
<p>but i think instead that just means we should go for a cslib instead</p>

#### [ Andrew Ashworth (Aug 31 2018 at 06:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133101832):
<p>i'm not sure most people doing math will need exotic data structures, network comms, parsing libraries, graph algorithms, etc</p>

#### [ Johan Commelin (Aug 31 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133101847):
<p>graph algorithms <span class="emoji emoji-2714" title="check mark">:check_mark:</span></p>

#### [ Johan Commelin (Aug 31 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133101860):
<p>The rest, we'll need for automation...</p>

#### [ Simon Hudon (Aug 31 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133101865):
<p>That makes sense. There is a weird dependency that I can see between math and CS in formal proofs. Logic, sets and natural numbers are the most fundamental but then good programming tools are useful for writing tactics that more advanced mathematical proofs use.</p>

#### [ Simon Hudon (Aug 31 2018 at 06:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133101912):
<p>I can see parsing libraries and graph algorithms as potentially useful for more advanced proof automation</p>

#### [ Johan Commelin (Aug 31 2018 at 06:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133101922):
<p>I view graph algorithms as part of combinatorics, and hence part of maths... maybe I'm weird.</p>

#### [ Simon Hudon (Aug 31 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102017):
<p>I think graphs are relevant both in discrete math and in computer science. For the structure of Lean libraries, even more important is what it uses and what uses it</p>

#### [ Simon Hudon (Aug 31 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102034):
<p>I could actually see mathlib becoming three libraries: logic + discrete math, programming and tactics, advanced math</p>

#### [ Andrew Ashworth (Aug 31 2018 at 06:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102152):
<p>i think for more practical minded users a more useful split would further divide advanced math into linear algebra, fourier analysis, prob/stats, and then everything else. of course this would be a day far far in the future</p>

#### [ Johan Commelin (Aug 31 2018 at 06:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102213):
<p>I think Simon's first two suggestions might be too interdependent, not?</p>

#### [ Simon Hudon (Aug 31 2018 at 06:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102214):
<p>I can see the sense in doing that. I also like having a lot of it under one roof so that they can be curated together.</p>

#### [ Simon Hudon (Aug 31 2018 at 06:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102269):
<p>I lost track ... which ones are those?</p>

#### [ Johan Commelin (Aug 31 2018 at 06:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102270):
<p>discrete math will want to use tactics</p>

#### [ Johan Commelin (Aug 31 2018 at 06:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102280):
<p>and tactics need discrete math and logic</p>

#### [ Johan Commelin (Aug 31 2018 at 06:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102282):
<p>etc</p>

#### [ Johan Commelin (Aug 31 2018 at 06:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102324):
<p>In that sense, I think I don't care about a huge monolith</p>

#### [ Johan Commelin (Aug 31 2018 at 06:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102333):
<p>The alternative is that everything goes into its own tiny little package, npm style</p>

#### [ Simon Hudon (Aug 31 2018 at 06:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102334):
<p>That's true. I think some basic tactics need to be intertwined with logic + discrete math.</p>

#### [ Johan Commelin (Aug 31 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102340):
<p>And some advanced ones!</p>

#### [ Johan Commelin (Aug 31 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102344):
<p>We were talking about <code>rewrite_search</code> and using <code>A*</code> for it.</p>

#### [ Johan Commelin (Aug 31 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102346):
<p>But maybe it should roll its own A*</p>

#### [ Simon Hudon (Aug 31 2018 at 06:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102396):
<p>I think we're going to see that a lot that some specialized mathematics / CS will need to roll its own automation.</p>

#### [ Simon Hudon (Aug 31 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102407):
<blockquote>
<p>But maybe it should roll its own A*</p>
</blockquote>
<p>I would rather not: one benefit of using a A* package is that optimizations can be added and studied and the automation can benefit from it.</p>

#### [ Mario Carneiro (Aug 31 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102448):
<p>Do I need to show you the slide in my mathlib talk where I talk about the CS and math goals of mathlib? Or the part where it used to be called stdlib until leo changed the name to differentiate it from corelib?</p>

#### [ Mario Carneiro (Aug 31 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102458):
<p>mathlib is absolutely a place for cs stuff</p>

#### [ Mario Carneiro (Aug 31 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102463):
<p>it's only sparse on cs stuff now because there are a bunch of mathematicians on the project</p>

#### [ Johan Commelin (Aug 31 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102466):
<p>Hahaha</p>

#### [ Simon Hudon (Aug 31 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102468):
<p>I wouldn't want to argue with you but I would love to see your slides ...</p>

#### [ Johan Commelin (Aug 31 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102510):
<p>So... who's going to formalise TAOCP?</p>

#### [ Simon Hudon (Aug 31 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102513):
<p><em>whistles and looks elsewhere</em></p>

#### [ Mario Carneiro (Aug 31 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102514):
<p><a href="https://goo.gl/DifCWB" target="_blank" title="https://goo.gl/DifCWB">https://goo.gl/DifCWB</a></p>

#### [ Johan Commelin (Aug 31 2018 at 06:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102515):
<p>Lol, I just realised that the Bourbaki of CS is just 1 person...</p>

#### [ Simon Hudon (Aug 31 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102694):
<p>I can see a lot of CS going into mathlib but I wonder if networking and the like fits in as it may not support the math</p>

#### [ Andrew Ashworth (Aug 31 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102696):
<p>Knuth is kind of a big deal like that...</p>

#### [ Andrew Ashworth (Aug 31 2018 at 06:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102707):
<p>Nobody knows if he'll finish all of his planned volumes of TAOCP</p>

#### [ Johan Commelin (Aug 31 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102753):
<blockquote>
<p>but I wonder if networking and the like fits in as it may not support the math</p>
</blockquote>
<p>Of course it will! We will have Lean instances talking with each other, trying to prove things together!</p>

#### [ Simon Hudon (Aug 31 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102775):
<p>I'm sold!</p>

#### [ Mario Carneiro (Aug 31 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102776):
<p>certainly IO stuff is useful for proof work</p>

#### [ Mario Carneiro (Aug 31 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102791):
<p>i.e. connecting to mathematica or sage or Z3</p>

#### [ Simon Hudon (Aug 31 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102822):
<blockquote>
<p>Nobody knows if he'll finish all of his planned volumes of TAOCP</p>
</blockquote>
<p>I'm getting less hopeful about than than I am of seeing an end to A Song of Ice and Fire</p>

#### [ Johan Commelin (Aug 31 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102823):
<p>Basically, as long as you don't start formalising enumerative biology, everything goes into mathlib...</p>

#### [ Simon Hudon (Aug 31 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102830):
<p>Even there, I guess if I can formalize the brain of a mathematician ...</p>

#### [ Mario Carneiro (Aug 31 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133102885):
<p>also I consider theoretical computer science math and on topic, even if some others here don't :P</p>

#### [ Simon Hudon (Aug 31 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133104388):
<p>Actually, I agree with this sentiment. I sense you mean it in the sense that it's a set of worthwhile mathematical problems but I also feel like it's not really relevant to computer science unless you're doing research in theoretical computer science.</p>

#### [ Simon Hudon (Aug 31 2018 at 07:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133104403):
<p>But back to the "let's put everything into mathlib" idea. I think one limiting factor might be the number of maintainers of mathlib.</p>

#### [ Johan Commelin (Aug 31 2018 at 07:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133104510):
<p>But that's not a problem yet. I think we can deal with that as soon as it becomes a real problem.</p>

#### [ Simon Hudon (Aug 31 2018 at 07:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133104556):
<p>I sense it becoming a problem already but maybe it's just that I don't have a good PR workflow. Maybe the nursery will improve that</p>

#### [ Mario Carneiro (Aug 31 2018 at 07:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133104568):
<p>fewer maintainers just means a longer wait for your PR to be merged, it's not a structural problem</p>

#### [ Mario Carneiro (Aug 31 2018 at 07:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133104610):
<p>but also I expect that there will be more maintainers available if/when lean gets really big</p>

#### [ Simon Hudon (Aug 31 2018 at 07:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133104677):
<p>What I'm having a hard time with is planning the evolution of projects while considering that features will eventually be merged into mathlib.</p>

#### [ Mario Carneiro (Aug 31 2018 at 07:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133104722):
<p>perhaps the perfectoid project is a model?</p>

#### [ Simon Hudon (Aug 31 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133104783):
<p>For example, with monotonicity is a tactic I use in temporal logic and in separation logic. Making changes to respond to reviews and making changes in the version that I use sometimes get difficult to reconcile. More so before <code>traversable</code> got merged.</p>

#### [ Simon Hudon (Aug 31 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133104785):
<p>How do they do it?</p>

#### [ Johan Commelin (Aug 31 2018 at 07:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133105189):
<blockquote>
<p>For example, with monotonicity is a tactic I use in temporal logic and in separation logic. Making changes to respond to reviews and making changes in the version that I use sometimes get difficult to reconcile. More so before <code>traversable</code> got merged.</p>
</blockquote>
<p>I suppose <span class="user-mention" data-user-id="110524">@Scott Morrison</span> could also provide valuable insight in how he managed all his category libs, and got them mathlib-ready and keeps the synced, etc...</p>

#### [ Reid Barton (Aug 31 2018 at 08:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133105737):
<p>BTW, I have a really simple output-only json library (only on my non-working laptop)</p>

#### [ Simon Hudon (Aug 31 2018 at 08:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133105740):
<p>That's a non-constructive proof of existence</p>

#### [ Simon Hudon (Aug 31 2018 at 08:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133105747):
<p>Does it prove anything?</p>

#### [ Simon Hudon (Aug 31 2018 at 08:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133105797):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> Thanks! I'll talk to him about it</p>

#### [ Reid Barton (Aug 31 2018 at 08:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133105805):
<p>I guess it proves that string is inhabited</p>

#### [ Reid Barton (Aug 31 2018 at 08:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133105863):
<p>Hopefully I will be able to use my laptop again when I get home in about a week. On the other hand the library only took an hour or two to write and probably looks very much like what you would expect so you may not even want to wait for it.</p>

#### [ Simon Hudon (Aug 31 2018 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133105974):
<p>Actually, the hardest problem I had to solve was proving the serializers and deserializers are each other's inverse in a compositional way. In the end, I got to have a lot of fun with free monads.</p>

#### [ Reid Barton (Aug 31 2018 at 08:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133106039):
<p>Oh yeah, decoding json seemed quite a lot more annoying and I didn't need it.</p>

#### [ Simon Hudon (Aug 31 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133106110):
<p>Darn! I think the same machinery might be usable though. The only thing missing would be an embedding from JSON syntax trees to your favorite data structure</p>

#### [ Scott Morrison (Sep 01 2018 at 04:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133159304):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span>, <span class="user-mention" data-user-id="112680">@Johan Commelin</span>, regarding coping with merging bits-and-pieces of larger repositories into mathlib: Yes, it's hard work. :-)</p>

#### [ Scott Morrison (Sep 01 2018 at 04:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133159352):
<p>On the positive side, having to rewrite things over and over again to adapt to changes suggested by others has made them better...</p>

#### [ Scott Morrison (Sep 01 2018 at 04:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133159358):
<p>But I'm generally in agreement that pretty much everything short of enumerative biology should be heading into mathlib.</p>

#### [ Simon Hudon (Sep 01 2018 at 04:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133159472):
<p>Thanks :) </p>
<p>How do you minimize the number of competing versions of the same package when you use that package in a project and you try to move some of the features around?</p>

#### [ Scott Morrison (Sep 01 2018 at 04:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133159532):
<p>I don't want to describe Mario and Johannes, as the maintainers of mathlib, as "bottlenecks", but in the long run we need to make sure that their time is not wasted (i.e. they have enough time to do the other things they need to do!), and this means working out how make reviewing and cleaning up PRs a more distributed process.</p>

#### [ Scott Morrison (Sep 01 2018 at 04:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133159540):
<p>I've started making my later repositories depend on my pull requests.</p>

#### [ Simon Hudon (Sep 01 2018 at 04:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133159548):
<p>With the nursery, that might be a cleaner solution</p>

#### [ Scott Morrison (Sep 01 2018 at 04:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133159600):
<p>e.g. if I split of a chunk of a project and make a PR to mathlib for it, I just update the leanpkg.toml file for that repository temporarily point to the branch corresponding to that PR on leanprover-community.</p>

#### [ Scott Morrison (Sep 01 2018 at 04:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133159611):
<p>This is not super safe, as branches on leanprover-community are somewhat ephemeral things. (And in particular, Mario and Johannes may well delete them after merging, and if they squash commits in some way the commit SHA you're pointing to could completely vanish.)</p>

#### [ Scott Morrison (Sep 01 2018 at 04:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133159614):
<p>At times last week I had a "scott-supremum" branch on leanprover-community, which was just a merge of several active PRs, so I could point my repo at that.</p>

#### [ Simon Hudon (Sep 01 2018 at 04:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133159863):
<p>I think you're right that we should try to distribute more of the maintenance burden. I've started pitching in for reviewing PRs but there ought to be more we can do. I sense with leanprover-community there are more opportunity we're not tapping into yet.</p>

#### [ Simon Hudon (Sep 01 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CS%20stuff/near/133189901):
<p>I just pushed my serialization stuff to the nursery. I'd love to know if people find it useful or if there are ways I can improve it. I'd like it to find its way to mathlib at some point too so if <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> and <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> have advice, I think I'll try editing the nursery version before I create a PR.</p>


{% endraw %}
