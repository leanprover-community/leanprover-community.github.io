---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/23851understandingprofileroutput.html
---

## [general](index.html)
### [understanding profiler output](23851understandingprofileroutput.html)

#### [Kevin Buzzard (May 11 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126403538):
So I am 2/3 of the way through a pretty big proof which I am currently reluctant to break up into smaller pieces.

#### [Kevin Buzzard (May 11 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126403551):
I might be pushing type class inference quite hard here, because it's a maths proof so everything is a group homomorphism and a ring homomorphism and I want Lean to infer everything.

#### [Kevin Buzzard (May 11 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126403554):
It has got to the point when, whenever I type something, I get the orange "thinking" bars for 5 seconds.

#### [Kevin Buzzard (May 11 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126403595):
I can live with this, but I wondered if there was an easy way to speed things up.

#### [Kevin Buzzard (May 11 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126403604):
[I have other alternatives, such as "plough on" or "break the proof up into two pieces", which will be painful]

#### [Kevin Buzzard (May 11 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126403613):
So I typed `set_option profiler true`

#### [Kevin Buzzard (May 11 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126403618):
and now I can see a bunch of information and I realise I don't really understand it.

#### [Kevin Buzzard (May 11 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126403655):
For example

#### [Kevin Buzzard (May 11 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126403671):
it starts

#### [Kevin Buzzard (May 11 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126403715):
```
elaboration: tactic execution took 4.96s
num. allocated objects:  5886
num. allocated closures: 6029
 4961ms   100.0%   _interaction._lambda_2
 4960ms   100.0%   tactic.istep
 4960ms   100.0%   scope_trace
 4959ms   100.0%   tactic.istep._lambda_1
 4959ms   100.0%   tactic.step
 3460ms    69.7%   tactic.to_expr
 1388ms    28.0%   tactic.interactive.have._lambda_1
 1055ms    21.3%   tactic.interactive.propagate_tags
 1007ms    20.3%   interaction_monad_orelse
```

#### [Kevin Buzzard (May 11 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126403719):
so I would be quite happy to get the wait time down to 1 second

#### [Kevin Buzzard (May 11 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126403727):
but I now see that the problem might be `tactic.to_expr` and `tactic.step` and this doesn't really help me at all in locating the problem

#### [Kevin Buzzard (May 11 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126403735):
I am envisaging that the problem might be "this simp is taking forever", which I could fix by looking at the proof simp finds and then typing it in directly

#### [Kevin Buzzard (May 11 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126403740):
or "this type class inference is taking forever", which again I feel like I might be able to help out with

#### [Kevin Buzzard (May 11 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126403742):
How do I diagnose the issue further?

#### [Mario Carneiro (May 11 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126403850):
The heavy hitters are the ones when the number of ms decreases significantly from the previous line

#### [Mario Carneiro (May 11 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126403852):
so `tactic.to_expr` and `tactic.interactive.have` here

#### [Mario Carneiro (May 11 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126403894):
Basically that means that elaboration is taking up all the time

#### [Kevin Buzzard (May 11 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126404455):
so how can I help?

#### [Kevin Buzzard (May 11 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126404456):
Can I see explicitly which lines of code are causing the problem?

#### [Kevin Buzzard (May 11 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126404498):
ooh I just got an achievement

#### [Kevin Buzzard (May 11 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126404499):
"type of sorry macro is not a sort"

#### [Kevin Buzzard (May 11 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126404500):
new error message

#### [Kevin Buzzard (May 11 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126404510):
heh

#### [Kevin Buzzard (May 11 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126404511):
it should have said "you put an extra bracket on that line you dimwit"

#### [Kevin Buzzard (May 11 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126404553):
OK so it might be the case that I can help the elaborator out. I have 500 lines of code. Where do I start?

#### [Kevin Buzzard (May 12 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126436589):
`elaboration of zariski.sheaf_of_types_on_standard_basis_for_finite_covers took 20.3s`

#### [Kevin Buzzard (May 12 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126436596):
finished :-)

#### [Kenny Lau (May 12 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126436650):
wonderful

#### [Kevin Buzzard (May 12 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126436661):
`set_option class.instance_max_depth 75`

#### [Kevin Buzzard (May 12 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126436665):
This is just for one lemma.#

#### [Kevin Buzzard (May 12 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126436666):
Obviously my code might be crappy

#### [Kevin Buzzard (May 12 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126436667):
Will this whole system really scale?

#### [Kevin Buzzard (May 12 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126436716):
max depth 72 is the min for which the code compiles

#### [Kevin Buzzard (May 12 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126436733):
It's the proof that an affine scheme satisfies the sheaf axiom for finite covers of basic opens by basic opens

#### [Kevin Buzzard (May 12 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126436738):
I've been putting it off for weeks, I knew it would be horrible, but I didn't know it would be this horrible.

#### [Andrew Ashworth (May 12 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126439771):
Big proofs are quite wobbly... there's no way you can split the lemma up into something shorter and less complicated?

#### [Kevin Buzzard (May 12 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126440349):
Not really. I could break it into some smaller pieces, but the problem is that the pieces other than the "main" piece would have really really complicated statements. Even the statement of the result whose hypotheses are so painful to check involves 13 groups / group homomorphisms which are inferred by type class inference, and the actual groups and homomorphisms involved are very elaborate, coming from some technical ring theory which I built up within the proof. Taking this stuff out into another lemma would involve making some very convoluted definitions and very long statements. On the other hand this is a snapshot of what "deep" mathematics looks like -- when one moves away from stuff like finite groups it does get complicated. Formalising graduate level real analysis (standard results in Hardy and Sobolev spaces) will I imagine be much worse.

#### [Mario Carneiro (May 12 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126440571):
If you yearn for the day of explicit `is_group_hom` assumptions, why don't you make the type `group_hom A B` of all functions that are group homs between groups A and B? That will make the typeclass problem trivial

#### [Mario Carneiro (May 12 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126440582):
It's not clear to me that this is the real issue, but it might help

#### [Mario Carneiro (May 12 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126440640):
I am not convinced that the problems you are discovering are unavoidable, but I haven't had much time to look at your formalization in depth

#### [Johan Commelin (May 12 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126448591):
@**Kevin Buzzard** Wow! Congratulations! That must have been a major road block.

#### [Johan Commelin (May 12 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126448638):
Can someone explain to me what the pros and cons are of having a type `group_hom A B` like Mario suggested?

#### [Kevin Buzzard (May 12 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126455761):
I personally don't understand the subtleties between the different possibilities for doing this - you could have a definition, or a structure, or a class. If you have a class then you want type class inference to do the donkeywork for you -- you seem to be making a commitment of the form "it should be easy to work out when something is a group hom so we'll make a machine do it for you". Unfortunately as I found out in my scheme work, life is not always so easy: I had a situation with a map f of (finite) types J -> I, groups G i and H j, and group homs c j from G (f j) to H j, and then wanted to define a map from Pi_i G i to Pi_j H j sending (g i) to the element which was c j (g (f j)) at j, and I thought I would be clogging up the type class inference system to write some explicit instance which was supposed to spot this, so I proved it by hand and then had to feed it into the type class inference system manually -- as I'm sure you'll agree Johan, a mathematician would note that this was obviously a group homomorphism -- "none of the G i or H j know anything about each other so they can't interfere with each other" -- and move on.

#### [Patrick Massot (May 12 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126464249):
I think this scheme theory effort could be important for the future of maths in Lean. I can't wait to see how Mario or Johannes will clean it

#### [Patrick Massot (May 12 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126464252):
I don't believe this monster proof cannot be cut in pieces

#### [Patrick Massot (May 12 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126464255):
The issue is to figure out what is the right infrastructure

#### [Patrick Massot (May 12 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126464262):
It's not about stating a lemma for each quarter of the proof (which would indeed give very technical statements)

#### [Patrick Massot (May 12 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126464264):
It's like my problem with the chain rule, compared to the new Coq proof

#### [Patrick Massot (May 12 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126464307):
In this case part of the infrastructure is a clever way of handling little o notations

#### [Patrick Massot (May 12 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126464354):
I think figuring out the infrastructure is really a core skill for non-trivial math formalization, and it's certainly normal that we don't get it right on our first try (especially for people with no CS background)

#### [Kevin Buzzard (May 12 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126467149):
I just did this scheme thing for fun. I have no idea whether they're interested in it for mathlib. I know that various bits should go in there, like the universal property of localization etc, but I don't know if they want all this sheaf stuff. My impression is that Mario is not that interested in definitions, he would rather have lemmas. I'm of a very different opinion but I was not going to be pushing for schemes to go into mathlib because of this. Mario was like "yeah but what the theorem?" when we talked about it and I was just going "it's schemes, there is no theorem, there are 1000 theorems but the fundamental thing is the definition". Well we'll have a theorem soon, but I'm not sure he'll be interested in it. I must say that this experience has made me deeply skeptical about stuff like https://blog.deepsense.ai/machine-learning-application-in-automated-reasoning/

#### [Johan Commelin (May 12 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126468000):
Yes... there is something of a gap to bridge (-; You don't get there with just a bit of NLP.

#### [Johan Commelin (May 12 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126468003):
Nevertheless, I sincerely hope that throwing some AI into the mix, the computer can take some of the tedious bits of work out of our hands...

#### [Johan Commelin (May 12 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126468011):
And basically this is what we try to do with some tactics...

#### [Johan Commelin (May 12 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126468012):
But one could imagine a rigged up version.

#### [Kevin Buzzard (May 12 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126468709):
Having spent several days wrestling with a 500 line proof which was of the form "this is completely trivial", it is now a joy to be back writing short proofs of non-trivial statements -- "continuous image of compact is compact", "we already proved a lemma saying what the image of Spec(f) was in this case", "compact iff every open cover has a finite subcover" etc etc -- I feel like I'm making rapid progress in every line now.

#### [Patrick Massot (May 13 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126508258):
I really really think you should try to get schemes in mathlib

#### [Patrick Massot (May 13 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126508261):
Otherwise we'll never know whether Lean can handle it without type class depth 100

#### [Patrick Massot (May 13 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126508301):
And I also think like https://blog.deepsense.ai/machine-learning-application-in-automated-reasoning/ looks like crackpot science

#### [Patrick Massot (May 13 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding profiler output/near/126508309):
Clearly writing this paper without first trying to translate the scheme definition by hand is either stupid or fraud

