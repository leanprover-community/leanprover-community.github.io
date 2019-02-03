---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/23851understandingprofileroutput.html
---

## Stream: [general](index.html)
### Topic: [understanding profiler output](23851understandingprofileroutput.html)

---


{% raw %}
#### [ Kevin Buzzard (May 11 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126403538):
<p>So I am 2/3 of the way through a pretty big proof which I am currently reluctant to break up into smaller pieces.</p>

#### [ Kevin Buzzard (May 11 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126403551):
<p>I might be pushing type class inference quite hard here, because it's a maths proof so everything is a group homomorphism and a ring homomorphism and I want Lean to infer everything.</p>

#### [ Kevin Buzzard (May 11 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126403554):
<p>It has got to the point when, whenever I type something, I get the orange "thinking" bars for 5 seconds.</p>

#### [ Kevin Buzzard (May 11 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126403595):
<p>I can live with this, but I wondered if there was an easy way to speed things up.</p>

#### [ Kevin Buzzard (May 11 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126403604):
<p>[I have other alternatives, such as "plough on" or "break the proof up into two pieces", which will be painful]</p>

#### [ Kevin Buzzard (May 11 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126403613):
<p>So I typed <code>set_option profiler true</code></p>

#### [ Kevin Buzzard (May 11 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126403618):
<p>and now I can see a bunch of information and I realise I don't really understand it.</p>

#### [ Kevin Buzzard (May 11 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126403655):
<p>For example</p>

#### [ Kevin Buzzard (May 11 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126403671):
<p>it starts</p>

#### [ Kevin Buzzard (May 11 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126403715):
<div class="codehilite"><pre><span></span>elaboration: tactic execution took 4.96s
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
</pre></div>

#### [ Kevin Buzzard (May 11 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126403719):
<p>so I would be quite happy to get the wait time down to 1 second</p>

#### [ Kevin Buzzard (May 11 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126403727):
<p>but I now see that the problem might be <code>tactic.to_expr</code> and <code>tactic.step</code> and this doesn't really help me at all in locating the problem</p>

#### [ Kevin Buzzard (May 11 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126403735):
<p>I am envisaging that the problem might be "this simp is taking forever", which I could fix by looking at the proof simp finds and then typing it in directly</p>

#### [ Kevin Buzzard (May 11 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126403740):
<p>or "this type class inference is taking forever", which again I feel like I might be able to help out with</p>

#### [ Kevin Buzzard (May 11 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126403742):
<p>How do I diagnose the issue further?</p>

#### [ Mario Carneiro (May 11 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126403850):
<p>The heavy hitters are the ones when the number of ms decreases significantly from the previous line</p>

#### [ Mario Carneiro (May 11 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126403852):
<p>so <code>tactic.to_expr</code> and <code>tactic.interactive.have</code> here</p>

#### [ Mario Carneiro (May 11 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126403894):
<p>Basically that means that elaboration is taking up all the time</p>

#### [ Kevin Buzzard (May 11 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126404455):
<p>so how can I help?</p>

#### [ Kevin Buzzard (May 11 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126404456):
<p>Can I see explicitly which lines of code are causing the problem?</p>

#### [ Kevin Buzzard (May 11 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126404498):
<p>ooh I just got an achievement</p>

#### [ Kevin Buzzard (May 11 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126404499):
<p>"type of sorry macro is not a sort"</p>

#### [ Kevin Buzzard (May 11 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126404500):
<p>new error message</p>

#### [ Kevin Buzzard (May 11 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126404510):
<p>heh</p>

#### [ Kevin Buzzard (May 11 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126404511):
<p>it should have said "you put an extra bracket on that line you dimwit"</p>

#### [ Kevin Buzzard (May 11 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126404553):
<p>OK so it might be the case that I can help the elaborator out. I have 500 lines of code. Where do I start?</p>

#### [ Kevin Buzzard (May 12 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126436589):
<p><code>elaboration of zariski.sheaf_of_types_on_standard_basis_for_finite_covers took 20.3s</code></p>

#### [ Kevin Buzzard (May 12 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126436596):
<p>finished :-)</p>

#### [ Kenny Lau (May 12 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126436650):
<p>wonderful</p>

#### [ Kevin Buzzard (May 12 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126436661):
<p><code>set_option class.instance_max_depth 75</code></p>

#### [ Kevin Buzzard (May 12 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126436665):
<p>This is just for one lemma.#</p>

#### [ Kevin Buzzard (May 12 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126436666):
<p>Obviously my code might be crappy</p>

#### [ Kevin Buzzard (May 12 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126436667):
<p>Will this whole system really scale?</p>

#### [ Kevin Buzzard (May 12 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126436716):
<p>max depth 72 is the min for which the code compiles</p>

#### [ Kevin Buzzard (May 12 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126436733):
<p>It's the proof that an affine scheme satisfies the sheaf axiom for finite covers of basic opens by basic opens</p>

#### [ Kevin Buzzard (May 12 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126436738):
<p>I've been putting it off for weeks, I knew it would be horrible, but I didn't know it would be this horrible.</p>

#### [ Andrew Ashworth (May 12 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126439771):
<p>Big proofs are quite wobbly... there's no way you can split the lemma up into something shorter and less complicated?</p>

#### [ Kevin Buzzard (May 12 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126440349):
<p>Not really. I could break it into some smaller pieces, but the problem is that the pieces other than the "main" piece would have really really complicated statements. Even the statement of the result whose hypotheses are so painful to check involves 13 groups / group homomorphisms which are inferred by type class inference, and the actual groups and homomorphisms involved are very elaborate, coming from some technical ring theory which I built up within the proof. Taking this stuff out into another lemma would involve making some very convoluted definitions and very long statements. On the other hand this is a snapshot of what "deep" mathematics looks like -- when one moves away from stuff like finite groups it does get complicated. Formalising graduate level real analysis (standard results in Hardy and Sobolev spaces) will I imagine be much worse.</p>

#### [ Mario Carneiro (May 12 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126440571):
<p>If you yearn for the day of explicit <code>is_group_hom</code> assumptions, why don't you make the type <code>group_hom A B</code> of all functions that are group homs between groups A and B? That will make the typeclass problem trivial</p>

#### [ Mario Carneiro (May 12 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126440582):
<p>It's not clear to me that this is the real issue, but it might help</p>

#### [ Mario Carneiro (May 12 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126440640):
<p>I am not convinced that the problems you are discovering are unavoidable, but I haven't had much time to look at your formalization in depth</p>

#### [ Johan Commelin (May 12 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126448591):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> Wow! Congratulations! That must have been a major road block.</p>

#### [ Johan Commelin (May 12 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126448638):
<p>Can someone explain to me what the pros and cons are of having a type <code>group_hom A B</code> like Mario suggested?</p>

#### [ Kevin Buzzard (May 12 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126455761):
<p>I personally don't understand the subtleties between the different possibilities for doing this - you could have a definition, or a structure, or a class. If you have a class then you want type class inference to do the donkeywork for you -- you seem to be making a commitment of the form "it should be easy to work out when something is a group hom so we'll make a machine do it for you". Unfortunately as I found out in my scheme work, life is not always so easy: I had a situation with a map f of (finite) types J -&gt; I, groups G i and H j, and group homs c j from G (f j) to H j, and then wanted to define a map from Pi_i G i to Pi_j H j sending (g i) to the element which was c j (g (f j)) at j, and I thought I would be clogging up the type class inference system to write some explicit instance which was supposed to spot this, so I proved it by hand and then had to feed it into the type class inference system manually -- as I'm sure you'll agree Johan, a mathematician would note that this was obviously a group homomorphism -- "none of the G i or H j know anything about each other so they can't interfere with each other" -- and move on.</p>

#### [ Patrick Massot (May 12 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126464249):
<p>I think this scheme theory effort could be important for the future of maths in Lean. I can't wait to see how Mario or Johannes will clean it</p>

#### [ Patrick Massot (May 12 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126464252):
<p>I don't believe this monster proof cannot be cut in pieces</p>

#### [ Patrick Massot (May 12 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126464255):
<p>The issue is to figure out what is the right infrastructure</p>

#### [ Patrick Massot (May 12 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126464262):
<p>It's not about stating a lemma for each quarter of the proof (which would indeed give very technical statements)</p>

#### [ Patrick Massot (May 12 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126464264):
<p>It's like my problem with the chain rule, compared to the new Coq proof</p>

#### [ Patrick Massot (May 12 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126464307):
<p>In this case part of the infrastructure is a clever way of handling little o notations</p>

#### [ Patrick Massot (May 12 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126464354):
<p>I think figuring out the infrastructure is really a core skill for non-trivial math formalization, and it's certainly normal that we don't get it right on our first try (especially for people with no CS background)</p>

#### [ Kevin Buzzard (May 12 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126467149):
<p>I just did this scheme thing for fun. I have no idea whether they're interested in it for mathlib. I know that various bits should go in there, like the universal property of localization etc, but I don't know if they want all this sheaf stuff. My impression is that Mario is not that interested in definitions, he would rather have lemmas. I'm of a very different opinion but I was not going to be pushing for schemes to go into mathlib because of this. Mario was like "yeah but what the theorem?" when we talked about it and I was just going "it's schemes, there is no theorem, there are 1000 theorems but the fundamental thing is the definition". Well we'll have a theorem soon, but I'm not sure he'll be interested in it. I must say that this experience has made me deeply skeptical about stuff like <a href="https://blog.deepsense.ai/machine-learning-application-in-automated-reasoning/" target="_blank" title="https://blog.deepsense.ai/machine-learning-application-in-automated-reasoning/">https://blog.deepsense.ai/machine-learning-application-in-automated-reasoning/</a></p>

#### [ Johan Commelin (May 12 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126468000):
<p>Yes... there is something of a gap to bridge (-; You don't get there with just a bit of NLP.</p>

#### [ Johan Commelin (May 12 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126468003):
<p>Nevertheless, I sincerely hope that throwing some AI into the mix, the computer can take some of the tedious bits of work out of our hands...</p>

#### [ Johan Commelin (May 12 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126468011):
<p>And basically this is what we try to do with some tactics...</p>

#### [ Johan Commelin (May 12 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126468012):
<p>But one could imagine a rigged up version.</p>

#### [ Kevin Buzzard (May 12 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126468709):
<p>Having spent several days wrestling with a 500 line proof which was of the form "this is completely trivial", it is now a joy to be back writing short proofs of non-trivial statements -- "continuous image of compact is compact", "we already proved a lemma saying what the image of Spec(f) was in this case", "compact iff every open cover has a finite subcover" etc etc -- I feel like I'm making rapid progress in every line now.</p>

#### [ Patrick Massot (May 13 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126508258):
<p>I really really think you should try to get schemes in mathlib</p>

#### [ Patrick Massot (May 13 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126508261):
<p>Otherwise we'll never know whether Lean can handle it without type class depth 100</p>

#### [ Patrick Massot (May 13 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126508301):
<p>And I also think like <a href="https://blog.deepsense.ai/machine-learning-application-in-automated-reasoning/" target="_blank" title="https://blog.deepsense.ai/machine-learning-application-in-automated-reasoning/">https://blog.deepsense.ai/machine-learning-application-in-automated-reasoning/</a> looks like crackpot science</p>

#### [ Patrick Massot (May 13 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/understanding%20profiler%20output/near/126508309):
<p>Clearly writing this paper without first trying to translate the scheme definition by hand is either stupid or fraud</p>


{% endraw %}
