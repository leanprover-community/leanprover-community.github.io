---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/55375additivegrouphoms.html
---

## Stream: [maths](index.html)
### Topic: [additive group homs](55375additivegrouphoms.html)

---


{% raw %}
#### [ Johan Commelin (May 23 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/126990085):
<p>This has come up before. I need additive group homs. I can duplicate Patrick's work on group homs, but I also saw <code>@[to_additive finsupp.sum_map_range_index]</code> in <code>data/finsupp.lean</code>. Can someone explain to me how that magic works? Would it be enough to sprinkle some <code>@[to_additive ...]</code>'s into <code>algebra/group.lean</code> to have everything work?</p>

#### [ Kevin Buzzard (May 23 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/126990781):
<p>There are additive group homs in the scheme stuff</p>

#### [ Kevin Buzzard (May 23 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/126990782):
<p>Kenny wrote them</p>

#### [ Kevin Buzzard (May 23 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/126990787):
<p>you could cut and paste for some basic stuff</p>

#### [ Kevin Buzzard (May 23 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/126990789):
<p>if you just want a solution</p>

#### [ Johan Commelin (May 23 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/126990833):
<p>Sure, but I'm also interested in the long-term approach</p>

#### [ Kevin Buzzard (May 23 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/126990842):
<p>lines 47 onwards at <a href="https://github.com/kbuzzard/lean-stacks-project/blob/master/src/canonical_isomorphism_nonsense.lean" target="_blank" title="https://github.com/kbuzzard/lean-stacks-project/blob/master/src/canonical_isomorphism_nonsense.lean">https://github.com/kbuzzard/lean-stacks-project/blob/master/src/canonical_isomorphism_nonsense.lean</a></p>

#### [ Kevin Buzzard (May 23 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/126990862):
<p>already there is a little magic going on</p>

#### [ Andrew Ashworth (May 23 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/126991426):
<p>the long term approach would be to learn a bit about tactics and understand how to_additive works, which is for automatically moving theorems from multiplicative groups to additive groups... unfortunately, learning tactics in Lean is a bit of a chore right now since Programming in Lean is unfinished</p>

#### [ Andrew Ashworth (May 23 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/126991559):
<p>well, actually, now that I'm looking at <code>algebra/group.lean</code>, you don't need to know much about tactics to understand what's going on there</p>

#### [ Johan Commelin (May 23 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/126991753):
<p>But then... I know next to nothing...</p>

#### [ Andrew Ashworth (May 23 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/126992374):
<p>hmm, have you worked through TPIL by chance?</p>

#### [ Andrew Ashworth (May 23 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/126992434):
<p>The first eleven chapters of Software Foundations is in Coq, but also quite good</p>

#### [ Andrew Ashworth (May 23 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/126992443):
<p>I am the kind of person who learns by grabbing a textbook and doing the exercises...</p>

#### [ Johan Commelin (May 23 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/126992799):
<p>Yes, maybe I should do that as well... but trying to define singular homology seems like a lot more fun...</p>

#### [ Johan Commelin (May 23 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/126992815):
<p>I am the kind of person who learns by cargo cult hacking</p>

#### [ Andrew Ashworth (May 23 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/126993051):
<p>this is also valid, but unfortunately if you get stuck there is no solutions manual available to unstuck you, whereas such a thing exists for Software Foundations... the solutions manual known as Mario is asleep right now</p>

#### [ Johannes Hölzl (May 23 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/126993084):
<p>the magic of <code>to_additive</code> is a search and replace of all <code>to_additive</code> constants in the definition of the constant. Afterwards the additive, multiplicative constant pair is added to the <code>to_additive</code> database. By using <code>attribute [to_additive a_c] m_c</code> you add a new relation. The requirement is that the additive constants are an exact mirror of the multiplicative ones.</p>

#### [ Johan Commelin (May 23 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/126993161):
<p>So, if I understand you correctly, it shouldn't be too complicated to sprinkle <code>@to_additive</code> in <code>algebra/group.lean</code>. Is that right?</p>

#### [ Johan Commelin (May 25 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127063451):
<p>Ok, so here is something that I am a bit worried about: in mathematics the notion of an "additive" group is really just notation (though pretty useful!). In Lean we have "groups" and "additive groups" and now we have <code>is_group_hom</code> and <code>is_add_group_hom</code>. But we also need mixed homomorphisms (from a multiplicative group to an additive group, and vice versa). For example, exp and log are such mixed homomorphisms. So all of a sudden, we have 4 notions of group homomorphisms. And now we want to compose these guys. So we need 8 composition lemmas. And I proved the 5 lemma some time ago: it has 10 groups in its statements. But any of those can be an "additive" group (and this occurs in nature!). Does that mean we need 1024 statements of the Five Lemma?</p>

#### [ Mario Carneiro (May 25 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064340):
<p>Use <code>multiplicative</code> to do these kind of things</p>

#### [ Johan Commelin (May 25 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064381):
<p>But, doesn't that mean we should use <code>multiplicative</code> all the time?</p>

#### [ Mario Carneiro (May 25 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064392):
<p>The additive / multiplicative group thing has a long history, and we are still debating the best way to do it</p>

#### [ Johan Commelin (May 25 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064404):
<p>Ok, I see. I can understand that it might be delicate to pick the correct approach</p>

#### [ Mario Carneiro (May 25 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064456):
<p><code>multiplicative</code> is useful for post hoc fitting a multiplicative theorem in an additive or mixed-additive use case</p>

#### [ Johan Commelin (May 25 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064464):
<p>I feel like I would rather just remove <code>add_group</code> entirely. But I don't see through all the ramifications</p>

#### [ Mario Carneiro (May 25 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064467):
<p><code>to_additive</code> is useful for preparing theorems up front <em>with new names</em> and statements</p>

#### [ Mario Carneiro (May 25 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064508):
<p>It's very confusing to apply <code>mul_one</code> when you want to simplify <code>x + 0 = x</code></p>

#### [ Johan Commelin (May 25 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064513):
<p>Yes, but I think that that <code>to_additive</code> magic will replace <em>all</em> occurences of mul with add</p>

#### [ Mario Carneiro (May 25 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064515):
<p>yes, that's the idea</p>

#### [ Johan Commelin (May 25 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064516):
<p>Or can you also use it to create mixed statements?</p>

#### [ Mario Carneiro (May 25 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064522):
<p>it's not very smart, it usually fails on mixed statements</p>

#### [ Mario Carneiro (May 25 2018 at 06:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064551):
<p>like <code>gpow</code>, which has an interplay between the additive semiring N and the group in question</p>

#### [ Mario Carneiro (May 25 2018 at 06:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064565):
<p>those translations had to be done manually, and in that case usually <code>multiplicative</code> is easier</p>

#### [ Johan Commelin (May 25 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064577):
<p>So, if we didn't have all the "multiplicative" connotations with our groups... but just <code>op_neu</code> instead of <code>mul_one</code>. Would that be helpful?</p>

#### [ Mario Carneiro (May 25 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064621):
<p>Jeremy likes this idea. I think it's the worst of both worlds</p>

#### [ Johan Commelin (May 25 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064630):
<p>If you could somehow have some magic that infers whether you use <code>*</code> or <code>+</code> notation, I feel like it would give a very nice fusion.</p>

#### [ Mario Carneiro (May 25 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064633):
<p>(Jeremy Avigad has been testing out a bunch of solutions in this space the past few months)</p>

#### [ Johan Commelin (May 25 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064635):
<p>But why do you think it is worse?</p>

#### [ Mario Carneiro (May 25 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064638):
<p>It's less mnemonic than either add_zero or mul_one</p>

#### [ Mario Carneiro (May 25 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064679):
<p>some of that magic goes beyond what lean will currently do on its own</p>

#### [ Johan Commelin (May 25 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064681):
<p>Yes, but having a lot of <code>gsmul</code> sprinkled through your goal is also not very helpful</p>

#### [ Mario Carneiro (May 25 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064683):
<p>but then it gets into extending lean, which gets messy</p>

#### [ Mario Carneiro (May 25 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064691):
<p>What do you mean?</p>

#### [ Johan Commelin (May 25 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064696):
<p>Well, I was playing around with <code>multiplicative</code> a bit. And I think it gave me those <code>gsmul</code>'s</p>

#### [ Johan Commelin (May 25 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064735):
<p>But maybe I just used it wrong</p>

#### [ Johan Commelin (May 25 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064768):
<p>I think I will just wait to see what you and Jeremy work out.</p>

#### [ Mario Carneiro (May 25 2018 at 06:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064811):
<p>What are you trying to do exactly?</p>

#### [ Johan Commelin (May 25 2018 at 06:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064812):
<p>If I understand you correctly, you say that a class <code>is_add_group_hom</code> is fine. But we shouldn't have classes for mixed homomorphisms. If one of those pops up, just turn it into an <code>is_group_hom</code>with <code>multiplicative</code>. Is that correct?</p>

#### [ Mario Carneiro (May 25 2018 at 06:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064852):
<p>yes</p>

#### [ Johan Commelin (May 25 2018 at 06:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064853):
<p>Because if we also have classes for the mixed homomorphisms, then you do need 8 composition rules. And I feel like you run head first into some cambrian explosion.</p>

#### [ Mario Carneiro (May 25 2018 at 06:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064855):
<p>we don't</p>

#### [ Johan Commelin (May 25 2018 at 06:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064865):
<p>So, shouldn't I just get rid of <code>is_add_group_hom</code> as well? And just use <code>multiplicative</code> immediately?</p>

#### [ Mario Carneiro (May 25 2018 at 07:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064914):
<p>I should hope there isn't too much theory on <code>is_add_group_hom</code></p>

#### [ Mario Carneiro (May 25 2018 at 07:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064917):
<p>seeing as it can usually be rephrased in terms of <code>is_group_hom</code></p>

#### [ Johan Commelin (May 25 2018 at 07:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064929):
<p>But still, I don't see why you draw the line there...</p>

#### [ Mario Carneiro (May 25 2018 at 07:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064933):
<p>two is manageable, 2^n isn't?</p>

#### [ Johan Commelin (May 25 2018 at 07:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064969):
<p>Anyway, what I am trying to do, is to prove that the boundary operator on the simplicial complex satisfies <code>d \circ d = 0</code></p>

#### [ Johan Commelin (May 25 2018 at 07:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064975):
<p>Yes, but one is even more manageable... (-;</p>

#### [ Mario Carneiro (May 25 2018 at 07:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064979):
<p>so use <code>is_group_hom</code> and call it a day</p>

#### [ Johan Commelin (May 25 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064980):
<p>And this complex consists of an additive group for each <code>n : nat</code>. And an additive hom between succesive groups.</p>

#### [ Mario Carneiro (May 25 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064989):
<p>what makes them additive?</p>

#### [ Johan Commelin (May 25 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064991):
<p>Those groups are all <code>finsupp (X n) int</code></p>

#### [ Johan Commelin (May 25 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127064992):
<p>where <code>X n</code> is a Type; depending on <code>n</code> (duh)</p>

#### [ Mario Carneiro (May 25 2018 at 07:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127065036):
<p>okay, so where is the mixed group hom?</p>

#### [ Johan Commelin (May 25 2018 at 07:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127065048):
<p>And the homomorphisms between them are somehow a bit involved... You take an alternating sum of (n+1) maps from <code>X (n+1)</code> to <code>X n</code>, and those induce maps between those additive groups.</p>

#### [ Johan Commelin (May 25 2018 at 07:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127065051):
<p>Aah, there is no mixed group hom in this picture yet.</p>

#### [ Johan Commelin (May 25 2018 at 07:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127065052):
<p>But I was thinking about other stuff in maths, where they do pop up.</p>

#### [ Johan Commelin (May 25 2018 at 07:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127065055):
<p>In all sorts of exponential sequences</p>

#### [ Mario Carneiro (May 25 2018 at 07:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127065098):
<p>So you can use <code>is_group_hom</code> + <code>multiplicative</code> to define <code>is_add_group_hom</code>, and then most of the theorems will defeq carry over (although they may need to be restated)</p>

#### [ Johan Commelin (May 25 2018 at 07:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127065121):
<p>Ok, but I think I will try to just use <code>multiplicative</code> directly.</p>

#### [ Johan Commelin (May 25 2018 at 07:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127065163):
<p>So instead of proving <code>is_add_group_hom d</code> I prove <code>@is_group_hom (multiplicate _) (multiplicative _) d</code></p>

#### [ Johan Commelin (May 25 2018 at 07:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127065164):
<p>Or something like that.</p>

#### [ Mario Carneiro (May 25 2018 at 07:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127065222):
<p>they should be the same, but yes unfold if necessary</p>

#### [ Johan Commelin (May 25 2018 at 07:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127065227):
<p>Ok, thanks for this discussion! I learned something (-;</p>

#### [ Johan Commelin (May 25 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127065234):
<p>Ooh, and if I locally make every instance of <code>add_group</code> into an instance of <code>group</code>, I think I run into the same trouble with ugly notation and names, right?</p>

#### [ Mario Carneiro (May 25 2018 at 07:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127065235):
<p>Oh don't do that</p>

#### [ Mario Carneiro (May 25 2018 at 07:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127065275):
<p>that's a recipe for disaster because the notations get all mixed up</p>

#### [ Johan Commelin (May 25 2018 at 07:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127065277):
<p>ok</p>

#### [ Mario Carneiro (May 25 2018 at 07:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127065281):
<p>next you know it you write <code>1 + 1 : nat</code> and get <code>0</code> :/</p>

#### [ Johan Commelin (May 25 2018 at 07:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127065286):
<p>got it</p>

#### [ Johan Commelin (May 25 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067503):
<p>Ok, so here is another ignorant question:<br>
The reason we have infix notation <code>*</code> for every <code>group</code> is because they are instances of <code>has_mul</code>, right?</p>

#### [ Johan Commelin (May 25 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067516):
<p>So what if we made abstract groups, with <code>op</code> and <code>neu</code> etc...</p>

#### [ Johan Commelin (May 25 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067520):
<p>And we don't have infix notation for those</p>

#### [ Johan Commelin (May 25 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067526):
<p>And then we have concrete groups (like the units in <code>rat</code>, or <code>int</code>) and we make those instances of <code>has_mul</code> resp. <code>has_add</code></p>

#### [ Johan Commelin (May 25 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067527):
<p>Then we still have our beloved infix notation.</p>

#### [ Johan Commelin (May 25 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067568):
<p>And then we can have some <code>to_multiplicate</code> resp. <code>to_additive</code> magic, that will turn <code>op_neu</code> into <code>mul_one</code> resp. <code>add_zero</code></p>

#### [ Johan Commelin (May 25 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067569):
<p>So the proofs remain readable and intuitive</p>

#### [ Johan Commelin (May 25 2018 at 08:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067616):
<p>If you want to prove something about an abstract group, and you would like to use infix <code>*</code> notation, then inside the proof you can make the group into an instance of <code>has_mul</code> (I hope) and voila, you have your <code>*</code>. But the statement that you proved is all of a sudden also valid in the context of additive notation.</p>

#### [ Johan Commelin (May 25 2018 at 08:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067619):
<p>Does this idea make any sense at all?</p>

#### [ Mario Carneiro (May 25 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067625):
<p>If you use <code>has_mul</code> then it gets involved in the statements of the theorems you prove, so there is some unfolding to apply it in a given context</p>

#### [ Johan Commelin (May 25 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067629):
<p>Well, I hope to keep it out of the statements.</p>

#### [ Mario Carneiro (May 25 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067631):
<p>then you can't use notation with abstract group theory</p>

#### [ Mario Carneiro (May 25 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067669):
<p>which is a thing people want</p>

#### [ Johan Commelin (May 25 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067672):
<p>So you would have some statement <code>theorem {G : Type} [group G] : blabla := begin ... end</code></p>

#### [ Johan Commelin (May 25 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067677):
<p>and between the <code>begin</code> and <code>end</code> you do some sort of <code>have_instance : has_mul G := { mul := op }</code></p>

#### [ Johan Commelin (May 25 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067683):
<p>and then you can use multiplicative notation in the rest of the proof.</p>

#### [ Johan Commelin (May 25 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067685):
<p>But it does not affect the statement</p>

#### [ Mario Carneiro (May 25 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067690):
<p>so <code>blabla</code> there has no notation?</p>

#### [ Johan Commelin (May 25 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067733):
<p>Yes, that is correct</p>

#### [ Johan Commelin (May 25 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067734):
<p>Unless we can somehow sugar that in... but I guess then we run into trouble again (which was your point)</p>

#### [ Mario Carneiro (May 25 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067735):
<p>right</p>

#### [ Mario Carneiro (May 25 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067742):
<p>Also, without <code>mul</code> constants in that statement <code>simp</code>  gets lost in higher order unification</p>

#### [ Johan Commelin (May 25 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067743):
<p>I think there is quite a lot of interesting <code>blabla</code> that does not have very much notation</p>

#### [ Mario Carneiro (May 25 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067745):
<p>for example if you have the theorem <code>op x id = x</code> where <code>op</code> and <code>id</code> are variables, <code>simp</code> can't use it</p>

#### [ Mario Carneiro (May 25 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067748):
<p>but if the theorem is <code>x + 0 = x</code> then it can</p>

#### [ Johan Commelin (May 25 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067788):
<p>You could wrap the statement with <code>local notation x' \bullet 'y := op x y</code></p>

#### [ Johan Commelin (May 25 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067789):
<p>If you really want infix notation in the statement</p>

#### [ Mario Carneiro (May 25 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067790):
<p>that doesn't solve the problem I just mentioned though</p>

#### [ Johan Commelin (May 25 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067797):
<p>Hmmm, so why can't <code>simp</code> use the former? (Newbie alert!)</p>

#### [ Mario Carneiro (May 25 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067800):
<p>the expression <code>?M1 x ?M2</code> matches almost anything</p>

#### [ Mario Carneiro (May 25 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067835):
<p>because you can have some lambda term for <code>?M1</code></p>

#### [ Mario Carneiro (May 25 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067842):
<p>unification up to beta reduction is called higher order unification and it's undecidable</p>

#### [ Mario Carneiro (May 25 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067843):
<p>and lean only does a very limited subset of it</p>

#### [ Johan Commelin (May 25 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067849):
<p>Ok, so then we don't have <code>simp</code> for abstract groups.</p>

#### [ Mario Carneiro (May 25 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067850):
<p>sad face</p>

#### [ Johan Commelin (May 25 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067851):
<p>But as soon as you are in a multiplicate of additive setting, you have it back</p>

#### [ Mario Carneiro (May 25 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067854):
<p>then I always want to be in a multiplicative or additive setting</p>

#### [ Johan Commelin (May 25 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067855):
<p>and if inside the proof you do the <code>have instance</code> thing that I suggested above, then you also have it back (I hope)</p>

#### [ Johan Commelin (May 25 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067895):
<p>So (I hope, once again) inside proofs you can always assume that you are inside the multiplicative setting</p>

#### [ Johan Commelin (May 25 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067898):
<p>even if you prove something for an abstract group</p>

#### [ Mario Carneiro (May 25 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067908):
<p>no, you still have that <code>simp</code> can only <em>use</em> groups with notation regardless of whether the goal uses notation</p>

#### [ Johan Commelin (May 25 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067918):
<p>Yes, but you will <em>have</em> a group with notation. Because the first thing you prove inside your proof is that you have notation. And then you continue with the actual proof.</p>

#### [ Johan Commelin (May 25 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067957):
<p>I really hope something like that is possible</p>

#### [ Mario Carneiro (May 25 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067959):
<p>I mean, if you have a theorem whose statement is neutral but whose proof uses notation, it can't be used with simp</p>

#### [ Johan Commelin (May 25 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067961):
<p>Hmmz, that is very sad</p>

#### [ Mario Carneiro (May 25 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067962):
<p>because only the statement matters for simp</p>

#### [ Johan Commelin (May 25 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067971):
<p>But you can change the statement inside the proof, right? By some <code>apply to_multiplicative</code>, or something</p>

#### [ Mario Carneiro (May 25 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127067975):
<p>So I just use multiplicative notation for "generic" group theory, and use <code>multiplicative</code> for transferring to additive</p>

#### [ Mario Carneiro (May 25 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068019):
<p>I don't see any reason to avoid some kind of primacy between the notations</p>

#### [ Johan Commelin (May 25 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068020):
<p>Ok, maybe I just need to get used to that (-;</p>

#### [ Johan Commelin (May 25 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068042):
<p>But let me try to understand Lean better: if I have a "generic" statement, and I start my proof with <code>apply multiplicative</code>. Would I be able to use <code>simp</code> after that?</p>

#### [ Mario Carneiro (May 25 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068094):
<p><code>simp</code> can be used on any statement, but it can only use simp lemmas that are stated with notation</p>

#### [ Mario Carneiro (May 25 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068133):
<p>I guess if you want to use <code>simp</code> on a generic statement you will need to change your goal to one that uses notation for the lemmas to match though</p>

#### [ Johan Commelin (May 25 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068143):
<p>Right, and I think a tactic could do that change for me</p>

#### [ Mario Carneiro (May 25 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068145):
<p>yes</p>

#### [ Mario Carneiro (May 25 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068152):
<p>no such tactic exists, but it could be done</p>

#### [ Johan Commelin (May 25 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068154):
<p>Great. Then I prefer that approach to group theory. But I respect your choice.</p>

#### [ Johan Commelin (May 25 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068160):
<p>It would solve all the <code>group_hom</code> hassle</p>

#### [ Johan Commelin (May 25 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068161):
<p>I think in the end, the code would be shorter, less duplication, and less <code>multiplicative</code> for end users.</p>

#### [ Mario Carneiro (May 25 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068162):
<p>but it would still have the problem of not being registerable with simp, as a lemma on its own right</p>

#### [ Johan Commelin (May 25 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068202):
<p>True, but I believe that the bulk of generic group theory is not simp lemmas</p>

#### [ Johan Commelin (May 25 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068205):
<p>So we would need to state a couple of simp lemmas for groups with notation.</p>

#### [ Johan Commelin (May 25 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068212):
<p>We don't want the five lemma to be a simp lemma, right?</p>

#### [ Mario Carneiro (May 25 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068214):
<p>more complicated theorems, proving existence of things or what not, can often be opened up to defeq anyway so it doesn't matter</p>

#### [ Johan Commelin (May 25 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068216):
<p>But I wouldn't mind if end users could use it, without figuring out to which of the 10 groups they first need to apply <code>multiplicative</code></p>

#### [ Mario Carneiro (May 25 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068266):
<p>Why don't you just state a version where everything is group, and another where everything is add_group, and let users deal with it themselves if they have mixed groups</p>

#### [ Johan Commelin (May 25 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068274):
<p>Because I really think that means I won't have many users...</p>

#### [ Johan Commelin (May 25 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068287):
<p>The conversion between <code>group</code> and <code>add_group</code> should be completely transparent</p>

#### [ Johan Commelin (May 25 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068299):
<p>Otherwise we won't convert much mathematicians to formalisation</p>

#### [ Mario Carneiro (May 25 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068346):
<p>Not completely transparent, if it's too transparent then <code>*</code> and <code>+</code> become the same and that's bad</p>

#### [ Mario Carneiro (May 25 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068348):
<p>it's really not an easy problem</p>

#### [ Mario Carneiro (May 25 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068356):
<p>I think <code>multiplicative</code> strikes the right balance, you have to explicitly state what you want but otherwise lean does the proof for free</p>

#### [ Johan Commelin (May 25 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068370):
<p>Hmmm, would still like to have groups without notation</p>

#### [ Mario Carneiro (May 25 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068371):
<p>why?</p>

#### [ Mario Carneiro (May 25 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068397):
<p>it's not easier to read</p>

#### [ Mario Carneiro (May 25 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068412):
<p>it's not easier to use</p>

#### [ Mario Carneiro (May 25 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068415):
<p>the names are less obvious</p>

#### [ Johan Commelin (May 25 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068416):
<p>For the generic theorems. Because those can be applied transparently to both settings</p>

#### [ Mario Carneiro (May 25 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068418):
<p>I see no advantages</p>

#### [ Mario Carneiro (May 25 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068425):
<p>it can't be applied transparently though</p>

#### [ Johan Commelin (May 25 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068426):
<p>I think they are just as easy to use (or easier, in the mixed setting).</p>

#### [ Mario Carneiro (May 25 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068433):
<p>it is as easy to apply a neutral theorem to an additive setting as it is to apply a multiplicative theorem in an additive setting</p>

#### [ Johan Commelin (May 25 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068434):
<p>If every <code>add_group</code> is an instance of <code>generic_group</code>, and I prove the five lemma for generic groups, then I can just apply it to additive groups, right?</p>

#### [ Johan Commelin (May 25 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068435):
<p>Without any <code>multiplicative</code> stuff</p>

#### [ Johan Commelin (May 25 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068479):
<p>You see, when I have my mathematician hat on I never think about whether my group is additive or multiplicative. I just use it. And I just use theorems. And it works.</p>

#### [ Mario Carneiro (May 25 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068491):
<p>I never had to deal with this in metamath either</p>

#### [ Johan Commelin (May 25 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068492):
<p>So I don't want end users to have to figure out themselves where they need to use <code>multiplicative</code> to make some generic theorem work</p>

#### [ Kenny Lau (May 25 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068493):
<blockquote>
<p>You see, when I have my mathematician hat on I never think about whether my group is additive or multiplicative. I just use it. And I just use theorems. And it works.</p>
</blockquote>
<p>hear hear</p>

#### [ Mario Carneiro (May 25 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068496):
<p>it was all local notation</p>

#### [ Kenny Lau (May 25 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068497):
<p>we do have an algebra hierarchy that mario doesn't use though</p>

#### [ Kenny Lau (May 25 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068498):
<p>in that hierarchy this problem is avoided, I think</p>

#### [ Mario Carneiro (May 25 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068537):
<p>Leo has his own ideas about generic groups. Like I said, this issue has a long history</p>

#### [ Mario Carneiro (May 25 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068539):
<p>The core lean impl is unfinished though, maybe lean 4 will have something workable</p>

#### [ Mario Carneiro (May 25 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068588):
<p>Honestly I have had more conversations on this topic than I would like, and things have not changed as a result</p>

#### [ Mario Carneiro (May 25 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068601):
<p>I just want to prove theorems and use what's there</p>

#### [ Johan Commelin (May 25 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068613):
<p>Ok. Got that.</p>

#### [ Johan Commelin (May 25 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068617):
<p>I really don't want to start any fights of course. I really love what you have done so far.</p>

#### [ Mario Carneiro (May 25 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068660):
<p>I don't mean to be short with you, but everyone has an idea and every solution has pros and cons</p>

#### [ Mario Carneiro (May 25 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068669):
<p>I would suggest not entering the ring unless you have a large amount of testing to support your claims</p>

#### [ Johan Commelin (May 25 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127068765):
<p>Yeah, that's good advice.</p>

#### [ Kevin Buzzard (May 26 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127104639):
<blockquote>
<p>I don't see any reason to avoid some kind of primacy between the notations</p>
</blockquote>
<p>This is a concept alien to mathematicians, that's why Johan is talking about it. But, like division by zero, it's just something we have to learn.</p>

#### [ Kevin Buzzard (May 26 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/127104713):
<p>They have different customs here.</p>

#### [ Patrick Massot (Jul 10 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/additive%20group%20homs/near/129399170):
<p>Did we get anywhere with this additive group homs thread? <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> what is the definition you recommend in the end?</p>


{% endraw %}
