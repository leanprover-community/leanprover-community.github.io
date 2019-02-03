---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/90707topologicalspacedocs.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [topological space docs](https://leanprover-community.github.io/archive/116395maths/90707topologicalspacedocs.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Apr 14 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088079):
<p>Ok so after a ropey start (see my heq thread earlier) I made it through the <code>topological_space.lean</code> file today and wrote some docs on it: <a href="https://github.com/kbuzzard/mathlib/blob/docs-topspaces/docs/theories/topological_spaces.md" target="_blank" title="https://github.com/kbuzzard/mathlib/blob/docs-topspaces/docs/theories/topological_spaces.md">https://github.com/kbuzzard/mathlib/blob/docs-topspaces/docs/theories/topological_spaces.md</a> . I needed to read this file for my work on schemes -- in particular I had to finally understand what a filter was and what they had to do with topological spaces.</p>

#### [ Patrick Massot (Apr 14 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088666):
<p>You are a bit unfair with filters. You should at least explain that they allow to cover uniformly the cases of sequences and maps from topological spaces. And then slightly more exotic stuff like one-sided limits at some real. That's why Bourbaki invented them.</p>

#### [ Patrick Massot (Apr 14 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088713):
<p>They also allow to mimic using sequential continuity and compactness for non-metric spaces</p>

#### [ Mario Carneiro (Apr 14 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088714):
<p>One way to motivate them is to consider the ~16 variations on L'hopital's theorem that arise with lots of permutations of limits to different places in the domain and codomain</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088753):
<p>I was just grumpy about them because they have actively stopped me doing what should be trivial stuff for a couple of days, because I didn't know what \Glb meant</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088760):
<p>when I actually ploughed through the file and a lot of the imports, and set pp.all on occasionally etc etc and finally got to the bottom of things and discovered that F &lt;= G iff G subseteq F</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088761):
<p>then it all began to make sense</p>

#### [ Patrick Massot (Apr 14 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088762):
<p>This is what this definition if compactness is about: a space is compact if every sequence has a converging subsequence,made true for all spaces</p>

#### [ Mario Carneiro (Apr 14 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088763):
<p>The description of topological basis is also a bit grumpy; the point as I mentioned before is to say "a topological basis is a collection of sets satisfying these two axioms" and then fold in the connection to generating a topology</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088764):
<p>I'm sure it's a very cute way to think about things</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088803):
<p>yeah, I had to get up early this morning, I've been in a grumpy mood all day :-)</p>

#### [ Patrick Massot (Apr 14 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088807):
<p>I'm defending filters here but zulip and gitter can testify I went through the same frustrations</p>

#### [ Mario Carneiro (Apr 14 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088814):
<p>In fact I think the "filters are a complete lattice" angle should probably be emphasized more, since it underlies many of the filter-theoretic definitions</p>

#### [ Mario Carneiro (Apr 14 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088857):
<p>A filter which is not bottom is called a proper filter fyi</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088858):
<p>Mario, the reason I don't buy your explanation is that there is a standard definition of a basis of a topological space, which we all learn, and which is on Wikipedia, and which is not what is implemented, so all your protestations that it's a better way of doing it are cancelled out by the fact that every mathematician will be confused by the way it's done. I have flagged the relevant lemma which saves us.</p>

#### [ Mario Carneiro (Apr 14 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088863):
<p>but it is that definition...</p>

#### [ Patrick Massot (Apr 14 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088864):
<p>I think Mario had the right idea when I faced that:we keep filters but add lemmas translating to usual stuff in usual situations</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088865):
<p>[explanation of why bases are done like that]</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088866):
<p>Yes, I explictly flag the lemmas saying "oh look, compactness looks insane, here's the lemma you need"</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088867):
<p>"bases look insane, here's the lemma you need"</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088868):
<p>That's the philosophy of the docs</p>

#### [ Mario Carneiro (Apr 14 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088907):
<p><a href="https://en.wikipedia.org/wiki/Base_(topology)" target="_blank" title="https://en.wikipedia.org/wiki/Base_(topology)">https://en.wikipedia.org/wiki/Base_(topology)</a></p>
<blockquote>
<p>A base is a collection B of subsets of X satisfying these two properties:<br>
1. The base elements cover X.<br>
2. Let B1, B2 be base elements and let I be their intersection. Then for each x in I, there is a base element B3 containing x and contained in I.</p>
</blockquote>

#### [ Kevin Buzzard (Apr 14 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088908):
<p>Now I can use topological spaces in Lean, and this morning I couldn't.</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088910):
<p>Right.</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088911):
<p>Whereas you have generate_open</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088913):
<p>it's the generate_open that makes it unusable</p>

#### [ Patrick Massot (Apr 14 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088914):
<p>I'm sure you could also explain why filters are useful</p>

#### [ Mario Carneiro (Apr 14 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088915):
<p>Any topological basis is a basis for the topology it generates</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088916):
<p>the lemma you proved and I flagged makes the definition usable</p>

#### [ Mario Carneiro (Apr 14 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088918):
<p>you can always satisfy that clause with refl</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088927):
<p>My point is simply that if you want to prove that (a,b) x (c,d) is a basis of open sets for the standard topology on R^2, you cannot possibly do that from the definition</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088928):
<p>but it's easy from the lemma</p>

#### [ Mario Carneiro (Apr 14 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088930):
<p>Yes you can</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088932):
<p>_you_ can</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088934):
<p>a mathematician can't</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088977):
<p>becuase they have no clue how to use generate_open</p>

#### [ Mario Carneiro (Apr 14 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088978):
<p>Those are two different goals though</p>

#### [ Mario Carneiro (Apr 14 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088980):
<p>you are trying to prove that some basis is a basis for something else, rather than just proving it's a basis</p>

#### [ Patrick Massot (Apr 14 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088981):
<p>My wife says I must stop participating but please be nice <span class="emoji emoji-1f603" title="smiley">:smiley:</span></p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088988):
<p>In maths, the proof goes "insert argument to prove that if x is in an open set U in R^2 then ther's some (a,b) x (c,d) in U containing x and now we're done</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088990):
<p>in Lean the proof from the definition of basis goes "that, and then we have to prove something about generate_open"</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088991):
<p>except now we don't because of the lemma</p>

#### [ Mario Carneiro (Apr 14 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088992):
<p>You have a preconceived topology in that example</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088993):
<p>yes, the one the mathematicans use :-)</p>

#### [ Mario Carneiro (Apr 14 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088994):
<p>I'm talking about proving that some collection of sets is a basis full stop</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125088995):
<p>I know</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089033):
<p>but that's a silly notion</p>

#### [ Mario Carneiro (Apr 14 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089037):
<p>That's the one wikipedia discusses</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089038):
<p>there's no generate_open there</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089039):
<p>it's the generate_open which makes the definition a complete pain to work with</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089040):
<p>and it's the lemma that saves us</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089041):
<p>so I highlight the lemma</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089046):
<p>that's all</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089047):
<p>the lemmas are all there</p>

#### [ Mario Carneiro (Apr 14 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089048):
<p>The generate_open is dischargable by refl, like I said</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089049):
<p>I'm saying the definitions are silly, but that's OK because the lemmas are there</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089050):
<p>yeah but I don't really know what that means</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089089):
<p>and I know what the lemma means</p>

#### [ Mario Carneiro (Apr 14 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089091):
<p>If S satisfies axioms 1 and 2, then it is a basis for (generate_open S)</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089092):
<p>and a generic mathematician will come along</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089093):
<p>with a proof of the two things in wikipedia</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089094):
<p>and will want to prove that they have a basis</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089095):
<p>and so they can use the lemma</p>

#### [ Mario Carneiro (Apr 14 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089101):
<p>okay I get it you think the notion is useless</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089103):
<p>right</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089105):
<p>but I'm not saying it shouldn't be there</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089106):
<p>I'm just explaining why I had to write the docs</p>

#### [ Mario Carneiro (Apr 14 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089107):
<p>but the docs are</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089109):
<p>and why they came out grumpy :-)</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089110):
<p>that is an absurd definition of compact as well.</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089156):
<p>It should be a theorem not a definition.</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089160):
<p>But again it doesn't matter</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089161):
<p>anyway, I am not grumpy any more :-)</p>

#### [ Mario Carneiro (Apr 14 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089162):
<p>I'm not sure how much I want to defend this... I think Johannes thought the filter stuff would make everything neat and concise</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089167):
<p>it doesn't matter</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089170):
<p>I'm just taking a contrary position for a laugh really</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089171):
<p>I'm really happy now</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089172):
<p>I can work topological spaces</p>

#### [ Mario Carneiro (Apr 14 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089173):
<p>I personally have a preference for standard point-set definitions</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089174):
<p>and I'm hoping that other people with the same background as me (i.e. basically two courses in topology and that's it) can do the same</p>

#### [ Mario Carneiro (Apr 14 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089214):
<p>but there are enough lemmas around to get rid of any filter claims you come across</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089215):
<p>yeah, that's why Hausdorff is called t2 probably ;-)</p>

#### [ Mario Carneiro (Apr 14 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089217):
<p>t2 is shorter :)</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089219):
<p>I'm really happy with the lemmas. I was preparing a list of lemmas which you should have proved</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089220):
<p>and it came out empty in the end</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089223):
<p>Occasionally it would have size 1 or 2</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089226):
<p>and then I'd find them :-)</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089232):
<p>Props to <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> too.</p>

#### [ Mario Carneiro (Apr 14 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089233):
<p>yeah he gets the credit for most of this work</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089234):
<p>It's a really nice complete library</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089236):
<p>even though some definitions are theorems and some theorems are definitions ;-)</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089276):
<p>I guess you guys can barely tell the difference</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089278):
<p>you probably think I'm talking about unfolding or something</p>

#### [ Mario Carneiro (Apr 14 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089280):
<p>it will teach you to forget about definitions and worry more about interfaces</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089281):
<p>OK, enough CS baiting. Thank you for your library!</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089282):
<p>I need to learn what this word interface means</p>

#### [ Mario Carneiro (Apr 14 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089289):
<p>does API mean something to you?</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089337):
<p>not really</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089340):
<p>this is some way of talking to the theorems</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089341):
<p>or something</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089378):
<p>Are my docs some sort of attempt to make an API for mathematicians trying to use topological spaces in Lean?</p>

#### [ Mario Carneiro (Apr 14 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089382):
<p>it's the idea that you encapsulate the underlying definition, somehow make it inaccessible, and then only use theorems that express properties of it</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089384):
<p>encapsulate is another mystery</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089385):
<p>these are all very CS words</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089391):
<p>I understand that a mathematician will come along with a proof that every cover has a finite subcover and will want to deduce that their space is compact</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089392):
<p>so I point them to the lemma which says this</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089393):
<p>[and make some snarky remark probably about how the definition is something else]</p>

#### [ Mario Carneiro (Apr 14 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089394):
<p>Category theory does this a lot, for example: A product of two objects is some object with a universal property, so that you can only use the universal property to prove stuff rather than unfolding whatever the product is "actually" defined to be in a particular category</p>

#### [ Kevin Buzzard (Apr 14 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089396):
<p>universal properties I understand</p>

#### [ Kevin Buzzard (Apr 15 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089439):
<p>but I don't understand why this is an argument for giving an unrecognisable definition of compact</p>

#### [ Mario Carneiro (Apr 15 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089442):
<p>A biconditional is also a "universal property", in a sense</p>

#### [ Kevin Buzzard (Apr 15 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089443):
<p>biconditional is a theorem of the form X iff Y?</p>

#### [ Mario Carneiro (Apr 15 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089444):
<p>it tells you everything you ever need to know about the definition, without actually telling you what the definition is</p>

#### [ Kevin Buzzard (Apr 15 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089445):
<p>I see</p>

#### [ Kevin Buzzard (Apr 15 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089448):
<p>but you really need to know where the theorem is</p>

#### [ Mario Carneiro (Apr 15 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089449):
<p>yes, that's the public part</p>

#### [ Mario Carneiro (Apr 15 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089457):
<p>the definition is the private part</p>

#### [ Kevin Buzzard (Apr 15 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089459):
<p>Maybe I saw this in java once</p>

#### [ Kevin Buzzard (Apr 15 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089460):
<p>your variables are private</p>

#### [ Kevin Buzzard (Apr 15 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089462):
<p>and you make some functions which lets the user change them</p>

#### [ Kevin Buzzard (Apr 15 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089463):
<p>or read them</p>

#### [ Kevin Buzzard (Apr 15 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089464):
<p>without actually letting them fiddle with them directly</p>

#### [ Kevin Buzzard (Apr 15 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089465):
<p>sorry, methods</p>

#### [ Kevin Buzzard (Apr 15 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089502):
<p>but I didn't realise this had anything to do with topological spaces at the time</p>

#### [ Mario Carneiro (Apr 15 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089505):
<p>One reasonably basic example of a gnarly construction is the Kuratowski pair (a,b) = {{a}, {a, b}}</p>

#### [ Kevin Buzzard (Apr 15 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089506):
<p>eew</p>

#### [ Kevin Buzzard (Apr 15 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089507):
<p>eew</p>

#### [ Kevin Buzzard (Apr 15 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089509):
<p>I see</p>

#### [ Kevin Buzzard (Apr 15 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089510):
<p>that's a great example</p>

#### [ Kevin Buzzard (Apr 15 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089516):
<p>we just need (a,b) = (c,d) iff a=c and b=d</p>

#### [ Mario Carneiro (Apr 15 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089517):
<p>exactly</p>

#### [ Kevin Buzzard (Apr 15 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089518):
<p>so we point the user to where that is proved</p>

#### [ Kevin Buzzard (Apr 15 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089519):
<p>and they can't see the disgusting truth behind it all</p>

#### [ Mario Carneiro (Apr 15 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089559):
<p>and later, we might want to change the definition for some reason to, say, {{0,a}, {1, b}} and that's okay as long as we can still prove the defining property, since no user depended on the specific construction</p>

#### [ Kevin Buzzard (Apr 15 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089560):
<p>but the compactness thing is different. We go for Kuratowski because all the choices are horrible and this one is the least horrible</p>

#### [ Kevin Buzzard (Apr 15 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089561):
<p>I see</p>

#### [ Kevin Buzzard (Apr 15 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089563):
<p>it's not completely different</p>

#### [ Kevin Buzzard (Apr 15 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089574):
<p>you are reserving the right to invent some even more weird thing that is better than filters</p>

#### [ Kevin Buzzard (Apr 15 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089576):
<p>and then change the definition of compactness</p>

#### [ Kevin Buzzard (Apr 15 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089577):
<p>because it compiles better on a quantum computer or whatever</p>

#### [ Mario Carneiro (Apr 15 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089579):
<p>or even just the point-set definition</p>

#### [ Kevin Buzzard (Apr 15 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089616):
<p>I see. In fact you could just play that trump card and that would shut me up</p>

#### [ Kevin Buzzard (Apr 15 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089620):
<p>you should just say "Kevin, you don't understand, the definition we have here works better if your machine has 8 cores"</p>

#### [ Kevin Buzzard (Apr 15 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089622):
<p>and I would have no response</p>

#### [ Mario Carneiro (Apr 15 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089623):
<p>the real point is that <em>it shouldn't matter</em> what the actual definition is, and if it does you're doing it wrong</p>

#### [ Kevin Buzzard (Apr 15 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089626):
<p>This is different to mathematics</p>

#### [ Kevin Buzzard (Apr 15 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089630):
<p>If you wrote a maths book with some weird definitions of things</p>

#### [ Kevin Buzzard (Apr 15 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089634):
<p>and then proved theorems which said that they were the same as everyone else's definition</p>

#### [ Mario Carneiro (Apr 15 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089635):
<p>there's also the pedagogical angle, but that's a different issue</p>

#### [ Kevin Buzzard (Apr 15 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089639):
<p>people would be confused as to why you were doing it</p>

#### [ Mario Carneiro (Apr 15 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089641):
<p>I don't think that exact thing is unheard of though</p>

#### [ Kevin Buzzard (Apr 15 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089642):
<p>and you can't answer "this definition works better if you have 8 brains"</p>

#### [ Mario Carneiro (Apr 15 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089684):
<p>your new definition might be suitable to a particular sort of generalization, for example</p>

#### [ Kevin Buzzard (Apr 15 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089685):
<p>As you are probably aware, I am extremely interested in the pedagogical angle</p>

#### [ Kevin Buzzard (Apr 15 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089688):
<p>and have very little understanding of stuff like run time analysis and other CS-related matters</p>

#### [ Mario Carneiro (Apr 15 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089689):
<p>in the pedagogical view, you might redefine the same thing several times depending on the current teaching goals</p>

#### [ Mario Carneiro (Apr 15 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089695):
<p>the new definition may not even be the same as earlier ones, although it is usually a generalization or provably equivalent</p>

#### [ Kevin Buzzard (Apr 15 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089742):
<p>So ultimately I should not care about your definitions, my main aim is to make sure that the interfaces are there.</p>

#### [ Mario Carneiro (Apr 15 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089743):
<p>exactly</p>

#### [ Kevin Buzzard (Apr 15 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089744):
<p>OK maybe tomorrow I will degrump it a bit :-)</p>

#### [ Kevin Buzzard (Apr 15 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089745):
<p>but now I have to make a birthday present</p>

#### [ Mario Carneiro (Apr 15 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089750):
<p>lol it's my birthday so I'll just pretend that's for me ;)</p>

#### [ Kevin Buzzard (Apr 15 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089752):
<p>ha ha it's for my son's GF</p>

#### [ Kevin Buzzard (Apr 15 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089753):
<p>happy birthday</p>

#### [ Kevin Buzzard (Apr 15 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089795):
<p>I'm not entirely sure you'd want a plastic T anyway</p>

#### [ Mario Carneiro (Apr 15 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125089802):
<p>good mathlib docs are a good present :)</p>

#### [ Kevin Buzzard (Apr 15 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125091717):
<p>OK well seeing as it's your birthday I de-grumped the docs a bit.</p>

#### [ Kevin Buzzard (Apr 15 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125091718):
<p>even though it's strictly speaking not even your birthday any more where I'm sitting</p>

#### [ Kevin Buzzard (Apr 15 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125091723):
<p>I'm now about to get onto the job I meant to do today, which was to prove that Spec(R) is compact using some argument involving bases :-)</p>

#### [ Kevin Buzzard (Apr 15 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125091724):
<p>now I understand the interface better :-)</p>

#### [ Kevin Buzzard (Apr 15 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125091725):
<p>Thanks as ever, by the way.</p>

#### [ Mario Carneiro (Apr 15 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125091768):
<p>I forget if the contrapositive form of the compactness definition is there: a collection of closed sets with the finite intersection property has nonempty intersection</p>

#### [ Kevin Buzzard (Apr 15 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125091778):
<p>I didn't see it</p>

#### [ Kevin Buzzard (Apr 15 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125091783):
<p>and I almost mentioned it as a theorem which should be there</p>

#### [ Kevin Buzzard (Apr 15 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125091819):
<p>but then I decided I'd never used it in my life :-)</p>

#### [ Kevin Buzzard (Apr 15 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125091830):
<p>I almost mentioned it the other day when Simon was asking whether the same was true for an arbitrary set</p>

#### [ Mario Carneiro (Apr 15 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125091840):
<p>I guess it is somewhat similar to the filter definition</p>

#### [ Kevin Buzzard (Apr 15 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125091933):
<p>Hmm, I've just realised that I want that a mathlib-basis is a Wikipedia-basis</p>

#### [ Mario Carneiro (Apr 15 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125091939):
<p>that's just the first two parts of the definition</p>

#### [ Kevin Buzzard (Apr 15 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125091985):
<p>oh sorry I don't mean that</p>

#### [ Mario Carneiro (Apr 15 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125091990):
<p>If <code>h1</code> and <code>h2</code> are proofs of the two axioms, then <code>&lt;h1, h2, rfl&gt;</code> is a proof it's a mathlib-basis</p>

#### [ Mario Carneiro (Apr 15 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125091994):
<p>that's what I've been saying</p>

#### [ Kevin Buzzard (Apr 15 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125091999):
<p><code>is_topological_basis_of_open_of_nhds</code></p>

#### [ Kevin Buzzard (Apr 15 2018 at 01:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092001):
<p>I mean the converse of that</p>

#### [ Kevin Buzzard (Apr 15 2018 at 01:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092038):
<p>Yes, sorry, I understand now</p>

#### [ Kevin Buzzard (Apr 15 2018 at 01:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092043):
<p>I was talking nonsense at some points earlier</p>

#### [ Kevin Buzzard (Apr 15 2018 at 01:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092047):
<p>when I said "wikipedia definition"</p>

#### [ Kevin Buzzard (Apr 15 2018 at 01:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092049):
<p>I sometimes meant "hypotheses in <code>is_topological_basis_of_open_of_nhds</code>"</p>

#### [ Kevin Buzzard (Apr 15 2018 at 01:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092050):
<p>:-/</p>

#### [ Mario Carneiro (Apr 15 2018 at 01:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092061):
<p><code>mem_nhds_of_is_topological_basis</code> is the easiest way to get converses of that stuff</p>

#### [ Kevin Buzzard (Apr 15 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092062):
<p><a href="https://topospaces.subwiki.org/wiki/Basis_for_a_topological_space" target="_blank" title="https://topospaces.subwiki.org/wiki/Basis_for_a_topological_space">https://topospaces.subwiki.org/wiki/Basis_for_a_topological_space</a></p>

#### [ Mario Carneiro (Apr 15 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092106):
<p>but there should be a theorem saying that a basis element is open</p>

#### [ Kevin Buzzard (Apr 15 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092108):
<p>there's a website (which I've never heard of) giving that as the definition.</p>

#### [ Kevin Buzzard (Apr 15 2018 at 01:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092111):
<p>This is evidence that I am very fluid with what my definition is :-/</p>

#### [ Kevin Buzzard (Apr 15 2018 at 01:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092119):
<p>mem_nhds means I might have to get my hands dirty with neighbourhoods maybe :-/</p>

#### [ Mario Carneiro (Apr 15 2018 at 01:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092124):
<p>which statement are you going for specifically?</p>

#### [ Kevin Buzzard (Apr 15 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092176):
<p>if B is a basis then I want that for all U open and for all x in U, there's V in B with x in V in U</p>

#### [ Kevin Buzzard (Apr 15 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092179):
<p>because as we all know</p>

#### [ Kevin Buzzard (Apr 15 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092223):
<p>50% of the time I will swear blind that this is the definition of a basis in Wikipedia</p>

#### [ Kevin Buzzard (Apr 15 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092228):
<p>and I don't want to do induction on generate_open</p>

#### [ Kevin Buzzard (Apr 15 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092229):
<p>I want this to be there on a plate</p>

#### [ Kevin Buzzard (Apr 15 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092231):
<p>Kenny proved it</p>

#### [ Kevin Buzzard (Apr 15 2018 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092233):
<p>in a file called temp.lean :-)</p>

#### [ Kevin Buzzard (Apr 15 2018 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092238):
<p>but I was trying to avoid importing this file</p>

#### [ Kevin Buzzard (Apr 15 2018 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092239):
<p>because its name looked a bit ominous</p>

#### [ Kevin Buzzard (Apr 15 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092284):
<p>I can do this myself</p>

#### [ Kevin Buzzard (Apr 15 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092285):
<p>The lemmas I need are all there</p>

#### [ Kevin Buzzard (Apr 15 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092287):
<p>I just need to glue them</p>

#### [ Kevin Buzzard (Apr 15 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092292):
<p>This morning I didn't know what nhds a was</p>

#### [ Kevin Buzzard (Apr 15 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092293):
<p>I have to remember that I'm not scared of it any more</p>

#### [ Mario Carneiro (Apr 15 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092339):
<p>I can add these to the file:</p>
<div class="codehilite"><pre><span></span>lemma is_open_of_is_topological_basis {s : set α} {b : set (set α)}
  (hb : is_topological_basis b) (hs : s ∈ b) : _root_.is_open s :=
is_open_iff_mem_nhds.2 $ λ a as,
(mem_nhds_of_is_topological_basis hb).2 ⟨s, hs, as, subset.refl _⟩

lemma mem_subset_basis_of_mem_open {b : set (set α)}
  (hb : is_topological_basis b) {a:α} (u : set α) (au : a ∈ u)
  (ou : _root_.is_open u) : ∃v ∈ b, a ∈ v ∧ v ⊆ u :=
(mem_nhds_of_is_topological_basis hb).1 $ mem_nhds_sets ou au
</pre></div>

#### [ Kevin Buzzard (Apr 15 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092348):
<p>It's the easy way of <code>is_open_iff_mem_nhds</code> I need and then I'm done :-)</p>

#### [ Kevin Buzzard (Apr 15 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092388):
<p>yeah, what you said</p>

#### [ Kevin Buzzard (Apr 15 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092390):
<p>I'd vote for them definitely.</p>

#### [ Kevin Buzzard (Apr 15 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092391):
<p>Then I can eschew temp.lean completely</p>

#### [ Mario Carneiro (Apr 15 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092393):
<p>I like <code>mem_nhds_of_is_topological_basis</code> because it generalizes well to all sorts of bounded quantification over open sets that comes up in topology, like continuity or compactness that can be stated with basis sets</p>

#### [ Kevin Buzzard (Apr 15 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092398):
<p>I didn't like it until today because of the obscure definition of nhds</p>

#### [ Kevin Buzzard (Apr 15 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092449):
<p>but again there was a lemma -- in this case <code>mem_nhds_sets_iff</code> -- which made this clear</p>

#### [ Kevin Buzzard (Apr 15 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092510):
<p>or even <code>nhds_sets</code>, which I mention in the docs</p>

#### [ Kevin Buzzard (Apr 15 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092516):
<p>I see. I'm mentioning all the results that a mathematician needs for the interface.</p>

#### [ Kevin Buzzard (Apr 15 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092887):
<p>eew, <code>exists v \in B</code> -- I have to run classical.some twice to get that v is in B</p>

#### [ Mario Carneiro (Apr 15 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092927):
<p>You can use <code>exists.fst</code> for the <code>v \in B</code> hypothesis</p>

#### [ Kevin Buzzard (Apr 15 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092928):
<p>That means <code>exists v in B, P</code> (B a set) unravels to <code>exists v in X, exists H : v in B, ...</code></p>

#### [ Kevin Buzzard (Apr 15 2018 at 02:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092935):
<p>Why not unravel to <code>exists v in X, v in B and ...</code></p>

#### [ Mario Carneiro (Apr 15 2018 at 02:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092936):
<p>You can also use <code>exists v : B, P</code> to pack them both into one</p>

#### [ Kevin Buzzard (Apr 15 2018 at 02:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092937):
<p>yeah but you wrote v in B not me ;-)</p>

#### [ Mario Carneiro (Apr 15 2018 at 02:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092938):
<p>because that same translation works for a wide variety of binders</p>

#### [ Kevin Buzzard (Apr 15 2018 at 02:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092975):
<p>I don't know what a binder is</p>

#### [ Mario Carneiro (Apr 15 2018 at 02:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092981):
<p>A thing that introduces a bound variable</p>

#### [ Mario Carneiro (Apr 15 2018 at 02:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092982):
<p>like exists or forall or lambda</p>

#### [ Kevin Buzzard (Apr 15 2018 at 02:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092983):
<p>somehow I thought that there were only about three of these</p>

#### [ Mario Carneiro (Apr 15 2018 at 02:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092984):
<p>or Glb or Lub</p>

#### [ Kevin Buzzard (Apr 15 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092991):
<p>but you're saying "exists v \in B" is somehow another one</p>

#### [ Mario Carneiro (Apr 15 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125092992):
<p>or indexed intersection</p>

#### [ Kevin Buzzard (Apr 15 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125093034):
<p>I see.</p>

#### [ Mario Carneiro (Apr 15 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125093035):
<p>No, I'm saying that <em>every</em> binder has the translation <code>Q a R b, p a =&gt; Q a, Q (_ : a R b), p a</code> where <code>Q</code> is any binder</p>

#### [ Mario Carneiro (Apr 15 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125093037):
<p>and <code>R</code> is any infix operator</p>

#### [ Kevin Buzzard (Apr 15 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125093038):
<p><code>unknown identifier 'exists.fst'</code></p>

#### [ Mario Carneiro (Apr 15 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125093039):
<p>should be in <code>logic.basic</code></p>

#### [ Mario Carneiro (Apr 15 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125093044):
<p>It's <code>Exists.fst</code> so you can use projections</p>

#### [ Kevin Buzzard (Apr 15 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125093083):
<p>capital E, got it</p>

#### [ Kevin Buzzard (Apr 15 2018 at 02:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125093090):
<p>you use Q again</p>

#### [ Patrick Massot (Apr 15 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125106157):
<blockquote>
<p>OK well seeing as it's your birthday I de-grumped the docs a bit.</p>
</blockquote>
<p>I think it still misses the main point of using filters: you have limits at a point and limits when a real variable or a natural number goes to infinity gathered in a single definition. For instance uniqueness of limit that you mention in your doc is proved for all three (and more) situations at once. This has nothing to do with "non-mathematical points such as running times".</p>

#### [ Kevin Buzzard (Apr 15 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125107091):
<p>I just don't know anything about how filters are used in practice so am in no position to be able to write those parts of the docs properly. I've never had to use them before and I don't really care about explaining them for this reason; I just wanted to get down the things I needed to know myself.</p>

#### [ Johannes Hölzl (Apr 15 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125116397):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span>  just added your documentation, I guess we can add more comments on filters later.<br>
I think one problem why there is not a lot of knowledge about filters (or nets) in math, is that it is obvious and usually something you don't need to think about. But we are in a formal system, so we are either forced to generalize over limits (using filters or nets) or we produce a lot of duplication (as Mario and Patrick mentioned). We can avoid them and define things like <code>compact</code> using open covers etc. But some proofs get much more concise using the fact that you can use the complete lattice (and even category theory) properties properties of filters. Currently it is not always intuitive to work with filters, but maybe with more automation and better syntax notations and support from the parser it may get better.<br>
In the end they are a powerful abstraction, and as most abstractions it takes some time to learn it.</p>

#### [ Kevin Buzzard (Apr 15 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125116956):
<p>Yeah, Mario convinced me not to worry about what was a definition and what was a theorem, as long as the theorems were all there.</p>

#### [ Sebastien Gouezel (Apr 15 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125120174):
<p>There is a very expressive way to use filters, with the word eventually.<br>
<code>def eventually {α : Type} (P : α → Prop) (f : filter α) := {x | P x} ∈ f.sets</code><br>
Then if you want to say that, eventually, some function u defined on nat is nonnegative, you write<br>
<code>eventually (λn, 0 ≤ u n) at_top</code><br>
If you want to say the same thing around a point x, say (which corresponds to a filter <code>at x</code>), you just write it as<br>
<code>eventually (λy, 0 ≤ f y) (at x)</code><br>
In this way, you can also write readable definitions of limits, or essentially whatever involves filters. This is the only way I use filters in Isabelle, and I was essentially never stuck.</p>

#### [ Patrick Massot (Apr 15 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125122549):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> what do you think about adding (and using) this definition?</p>

#### [ Johannes Hölzl (Apr 16 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125137370):
<p>I'm fine with adding this definition, especially with a corresponding quantifier notation (and also its dual the <code>frequently</code> quantifier). I'm just not sure if we should abandon the <code>f.sets</code> notation or keep both.</p>

#### [ Mario Carneiro (Apr 16 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125137483):
<p>I want to refactor the filter stuff so that <code>.sets</code> is superfluous, i.e. <code>s \in f</code> means <code>s \in f.sets</code>. I guess we can support <code>eventually</code> if it's a <code>reducible</code> definition, but I don't like the idea of duplicating everything for this purpose</p>

#### [ Johannes Hölzl (Apr 16 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20docs/near/125138117):
<p>Setting up a <code>has_mem</code> for filter is surely a good idea.</p>


{% endraw %}
