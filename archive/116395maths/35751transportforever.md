---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/35751transportforever.html
---

## Stream: [maths](index.html)
### Topic: [transport forever](35751transportforever.html)

---


{% raw %}
#### [ Patrick Massot (Oct 10 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135547994):
<p>Today I tried to setup transport of structure along equiv, since <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> wanted to see (part of) what we would like to be automated. It can be seen at <a href="https://gist.github.com/PatrickMassot/9c5246efe8d1fd4f26c21cbf2ac99ff8" target="_blank" title="https://gist.github.com/PatrickMassot/9c5246efe8d1fd4f26c21cbf2ac99ff8">https://gist.github.com/PatrickMassot/9c5246efe8d1fd4f26c21cbf2ac99ff8</a> First I'd like to know if the beginning looks reasonnable. The answer is almost certainly not since I'm stuck when I try to go to rings at the bottom. This file is autonomous, it should fail reliably with any recentish version of mathlib.</p>

#### [ Patrick Massot (Oct 10 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135548014):
<p>Of course this is needed for the ring completions project, which is needed for the perfectoid project</p>

#### [ Patrick Massot (Oct 10 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135548345):
<p>I should say why this is only part of what Kevin always asks for. Here we start with some structure on a type and want to transport it along a given equiv, so that the equiv becomes an isomorphism in the relevant category. The next step is to assume we have an isomorphism in a category and transport various statements (like Kevin's exact sequences).</p>

#### [ Patrick Massot (Oct 10 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135548838):
<p>Let me recall the context of the ring completion project. We start with a topological ring <code>α</code>. We get a topological ring structure on <code>separation_quotient α</code> in <a href="https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L279" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L279">https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L279</a>. We get a topological ring structure on the completion of a separated topological ring at <a href="https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L1205" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L1205">https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L1205</a> (oops, this is only a <code>comm_ring</code> instance, but the topological axioms should be easy). And  we have <a href="https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L747" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L747">https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L747</a> : <code>completion (separation_quotient α) ≃ completion α</code> along which we want to transport the topological ring structure.</p>

#### [ Johan Commelin (Oct 10 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135556061):
<p>Nice start <span class="user-mention" data-user-id="110031">@Patrick Massot</span>! It's also a bit sad that it is breaking down for rings.</p>

#### [ Patrick Massot (Oct 10 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135561185):
<p>Don't loose hope Johan, Mario will save us.</p>

#### [ Mario Carneiro (Oct 10 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135561760):
<p>As you point out, there are two slightly different senses of "transport of structure" being used here. One, which seemed to be Kevin's main point, is a theorem such as "if R ~= S are isomorphic rings and R is artinian then S is artinian", and this has a possibility of being addressed by <code>transfer</code>. The other has the form "Given an equiv A ~= B of sets, and a ring structure on A, there is an induced ring structure on B" which is what you seem to be demonstrating in the gist.</p>

#### [ Patrick Massot (Oct 10 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135561778):
<p>yes</p>

#### [ Patrick Massot (Oct 10 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135561836):
<p>In my use case I first want to transport the structure over an equiv and then transport properties</p>

#### [ Mario Carneiro (Oct 10 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135561849):
<p>One reason I wouldn't want to just jump in with that kind of tactic is that most of those theorems generalize to a weaker structure than equiv</p>

#### [ Patrick Massot (Oct 10 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135561854):
<p>And my equiv is actually a uniform space equiv so completeness would be transported for instance</p>

#### [ Mario Carneiro (Oct 10 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135561875):
<p>For example you might just have an injection into a subring of a ring</p>

#### [ Mario Carneiro (Oct 10 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135561899):
<p>or it might not even be an injection but there is a coherence property</p>

#### [ Patrick Massot (Oct 10 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135561902):
<p>Maybe it's too early for a tactic here. As you wrote, we first need to see a couple of handcrafted examples in order to understand what we want</p>

#### [ Patrick Massot (Oct 10 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135561982):
<p>Do you think the ring thing can be done with that starting point? I'm not sure whether I should try to have local instances, or maybe use <code>haveI</code> in the constructions...</p>

#### [ Mario Carneiro (Oct 10 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562025):
<p>I also have no applications of your kind of transport of structure</p>

#### [ Patrick Massot (Oct 10 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562043):
<p>what?</p>

#### [ Mario Carneiro (Oct 10 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562090):
<p>the "A is a ring so B is a ring" kind</p>

#### [ Patrick Massot (Oct 10 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562094):
<p>I wrote very precisely what immediate application I have</p>

#### [ Patrick Massot (Oct 10 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562106):
<p>In this thread, right before Johan's message</p>

#### [ Mario Carneiro (Oct 10 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562141):
<p>the problem is that just transporting the whole structure won't work</p>

#### [ Mario Carneiro (Oct 10 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562155):
<p>you will end up with yet another copy of the uniform structure</p>

#### [ Patrick Massot (Oct 10 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562236):
<p>A uniform structure <em>and</em> a compatible ring structure, and a universal property, that's exactly what I want</p>

#### [ Mario Carneiro (Oct 10 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562282):
<p>So what is the setting exactly for this theorem? <code>completion (separation_quotient α) ≃ completion α</code></p>

#### [ Patrick Massot (Oct 10 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562344):
<p><a href="https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L747" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L747">https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L747</a></p>

#### [ Patrick Massot (Oct 10 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562349):
<p>any uniform space structure on any type</p>

#### [ Mario Carneiro (Oct 10 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562378):
<p>so where are the rings coming from</p>

#### [ Patrick Massot (Oct 10 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562459):
<p>I don't know what to write that is not copy-pasting my message before Johan's message</p>

#### [ Johan Commelin (Oct 10 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562511):
<blockquote>
<p>Let me recall the context of the ring completion project. We start with a topological ring <code>α</code>. We get a topological ring structure on <code>separation_quotient α</code> in <a href="https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L279" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L279">https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L279</a>. We get a topological ring structure on the completion of a separated topological ring at <a href="https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L1205" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L1205">https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L1205</a> (oops, this is only a <code>comm_ring</code> instance, but the topological axioms should be easy). And  we have <a href="https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L747" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L747">https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L747</a> : <code>completion (separation_quotient α) ≃ completion α</code> along which we want to transport the topological ring structure.</p>
</blockquote>
<p>Voila. I did it.</p>

#### [ Mario Carneiro (Oct 10 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562576):
<p>explain the last sentence. Which side has the ring, and why doesn't the other side have one?</p>

#### [ Patrick Massot (Oct 10 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562604):
<p>Left hand side has the ring</p>

#### [ Patrick Massot (Oct 10 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562615):
<p>Because <code>separation_quotient α</code> is separated</p>

#### [ Patrick Massot (Oct 10 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562634):
<p>This is the content of the second sentence</p>

#### [ Mario Carneiro (Oct 10 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562813):
<p>I don't get it. Is this <code>completion (separation_quotient α) ≃ completion α</code> in fact (in math) a uniform ring isomorphism?</p>

#### [ Mario Carneiro (Oct 10 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562826):
<p>If so, why isn't <code>completion α</code> already separated?</p>

#### [ Patrick Massot (Oct 10 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562828):
<p>A posteriori yes</p>

#### [ Patrick Massot (Oct 10 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562856):
<p><code>completion α</code> is separated, but <code>α</code> isn't</p>

#### [ Mario Carneiro (Oct 10 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135562875):
<p>what goes wrong in the <code>ring (completion α)</code> instance if you drop the <code>separated α</code> property?</p>

#### [ Patrick Massot (Oct 10 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563061):
<p>The map <code>coe : α -&gt; completion α</code> is no longer injective</p>

#### [ Mario Carneiro (Oct 10 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563201):
<p>does injectivity get used somewhere?</p>

#### [ Patrick Massot (Oct 10 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563225):
<p>It is currently used in the proof everywhere, but maybe there is another proof. Johannes wrote that proof.</p>

#### [ Patrick Massot (Oct 10 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563266):
<p>So I didn't think hard about it</p>

#### [ Mario Carneiro (Oct 10 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563276):
<p>but again a posteriori it seems like it is actually injective</p>

#### [ Mario Carneiro (Oct 10 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563283):
<p>or else you wouldn't have that equiv</p>

#### [ Patrick Massot (Oct 10 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563284):
<p>No</p>

#### [ Patrick Massot (Oct 10 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563289):
<p>it's not injective</p>

#### [ Patrick Massot (Oct 10 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563305):
<p><code>coe : α -&gt; completion α</code> is injective if and only if <code>α</code> is separated</p>

#### [ Patrick Massot (Oct 10 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563316):
<p><code>separation_quotient α -&gt; completion (separation_quotient α)</code> is injective</p>

#### [ Mario Carneiro (Oct 10 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563320):
<p>ah, ok</p>

#### [ Patrick Massot (Oct 10 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563321):
<p>because <code>separation_quotient α</code> is separated</p>

#### [ Mario Carneiro (Oct 10 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563370):
<p>Do the definitions of <code>has_one</code> and <code>has_mul</code> at least work without <code>separated</code>?</p>

#### [ Patrick Massot (Oct 10 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563397):
<p>Probably</p>

#### [ Patrick Massot (Oct 10 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563402):
<p>maybe not actually</p>

#### [ Patrick Massot (Oct 10 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563424):
<p>sorry</p>

#### [ Patrick Massot (Oct 10 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563463):
<p>You can define mul</p>

#### [ Patrick Massot (Oct 10 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563466):
<p>the issue is continuity</p>

#### [ Mario Carneiro (Oct 10 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563544):
<p>I'm checking this branch out, 1 sec</p>

#### [ Mario Carneiro (Oct 10 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563584):
<p>anyway, my intuition is that you don't want to use transfer of structure like this. You should already be able to define the structure a priori, and you want to show that the equivalence respects the structure that is already there</p>

#### [ Patrick Massot (Oct 10 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563659):
<p>In need to transport something along this equiv though</p>

#### [ Mario Carneiro (Oct 10 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563662):
<p>In particular, if we did transfer of structure your way, we would end up with two ring structures on <code>completion (separation_quotient A)</code></p>

#### [ Patrick Massot (Oct 10 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563689):
<p>I'm ready to trow away any ring structure which is not compatible with the uniform structure</p>

#### [ Mario Carneiro (Oct 10 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563749):
<p>I would guess the two ring structures are equal, but as we know that's not good enough for lean</p>

#### [ Patrick Massot (Oct 10 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135563873):
<p>maths on a computer are so complicated...</p>

#### [ Mario Carneiro (Oct 10 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565503):
<p>Oh, this is evil: <a href="https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L263-L273" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L263-L273">https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L263-L273</a></p>

#### [ Mario Carneiro (Oct 10 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565530):
<p>I'm starting to see why you get heq goals</p>

#### [ Patrick Massot (Oct 10 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565593):
<p><a href="#narrow/stream/113488-general/subject/heq.20hell.20again/near/135479776" title="#narrow/stream/113488-general/subject/heq.20hell.20again/near/135479776">https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/heq.20hell.20again/near/135479776</a></p>

#### [ Patrick Massot (Oct 10 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565596):
<p>I already confessed</p>

#### [ Patrick Massot (Oct 10 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565687):
<p>And I blame Danish thefts</p>

#### [ Mario Carneiro (Oct 10 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565707):
<p>I think we need to be less constructive with our quotient constructions</p>

#### [ Mario Carneiro (Oct 10 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565730):
<p>the quotient ring construction for example should apply to any quotient map, not just the canonical one</p>

#### [ Chris Hughes (Oct 10 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565737):
<p>What's evil about it?</p>

#### [ Patrick Massot (Oct 10 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565743):
<p>constructive is evil</p>

#### [ Mario Carneiro (Oct 10 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565745):
<p>Type equality is evil</p>

#### [ Patrick Massot (Oct 10 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565830):
<p>Actually I tried to redeem with the next lemma</p>

#### [ Mario Carneiro (Oct 10 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565858):
<p><code>eq_mpr_heq</code>?</p>

#### [ Patrick Massot (Oct 10 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565859):
<p>or previous lemma</p>

#### [ Mario Carneiro (Oct 10 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565876):
<p>the instance?</p>

#### [ Patrick Massot (Oct 10 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565889):
<p>I have one lemma saying the quotients are equal but the other one says the setoids are equal</p>

#### [ Chris Hughes (Oct 10 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565899):
<blockquote>
<p>the quotient ring construction for example should apply to any quotient map, not just the canonical one</p>
</blockquote>
<p>Do you mean so it would be easy to prove things about quotient rings that aren't constructed using <code>quotient</code>, like <code>zmod</code>, or <code>complex</code> using theorems about quotient rings?</p>

#### [ Patrick Massot (Oct 10 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565949):
<p>I mean <a href="https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L255-L261" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L255-L261">https://github.com/leanprover-community/mathlib/blob/completions/analysis/topology/completion.lean#L255-L261</a></p>

#### [ Mario Carneiro (Oct 10 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565965):
<p>right</p>

#### [ Mario Carneiro (Oct 10 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135565991):
<p>as long as it acts like a quotient you should have quotient ring construction, quotient topology, etc</p>

#### [ Patrick Massot (Oct 10 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135566883):
<blockquote>
<p>as long as it acts like a quotient you should have quotient ring construction, quotient topology, etc</p>
</blockquote>
<p>Is this something I'm meant to understand and convert into action, or was this you thinking aloud?</p>

#### [ Mario Carneiro (Oct 10 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135566901):
<p>I don't really expect you to do anything on that front, it's mostly the fault of <code>quotient_ring</code> and such</p>

#### [ Mario Carneiro (Oct 10 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135566962):
<p>in the short term you might try to avoid casting between types but still unfold the fact that it is a quotient</p>

#### [ Patrick Massot (Oct 10 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135566972):
<p>This quotient ring stuff seems tricky to get right. I was already refactored once</p>

#### [ Mario Carneiro (Oct 10 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135566984):
<p>indeed it's been refactored again</p>

#### [ Mario Carneiro (Oct 10 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135566993):
<p>(module refactor touched this too)</p>

#### [ Patrick Massot (Oct 10 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135567002):
<p>I hope this completion stuff will help you get the refactor right</p>

#### [ Patrick Massot (Oct 10 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135567198):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> this conversation suggests that the perfectoid project is waiting for module refactor also on the ring completion side</p>

#### [ Patrick Massot (Oct 10 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135567217):
<p>unless we find a way to finish that ring completion thing using evil lemmas and fake transport of structure</p>

#### [ Kevin Buzzard (Oct 10 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135567220):
<p>One thing that really spurs me on with this whole thing is that as we try to do a different kind of mathematics to the kind that is typically done in a theorem prover, we run into issues which computer scientists seem to be able to solve. I am constantly feeling like both sides somehow benefit.</p>

#### [ Kevin Buzzard (Oct 10 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135567284):
<p>I did this once (cutting corners) with schemes, and now look at that project.</p>

#### [ Kevin Buzzard (Oct 10 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135567295):
<p>I say we do it right this time, however long it takes.</p>

#### [ Patrick Massot (Oct 10 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135567303):
<p>Yes, this is exactly what I was thinking</p>

#### [ Kevin Buzzard (Oct 10 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135567311):
<p>I'm not that busy in January...</p>

#### [ Patrick Massot (Oct 10 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135567348):
<p>Yeah, too bad we have orthogonal teaching schedules this year</p>

#### [ Patrick Massot (Oct 10 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/135567464):
<p>Mario, could we still have <code>congr'</code> trying to discharge goals using <code>proof_irrel</code> and <code>proof_irrel_heq</code> in order to cover my evil actions?</p>

#### [ Patrick Massot (Oct 19 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/136137596):
<p>About transport of structure, Assia pointed out to me <a href="https://hal.inria.fr/hal-01559073" target="_blank" title="https://hal.inria.fr/hal-01559073">https://hal.inria.fr/hal-01559073</a> It seems it's actually relevant, despite the univalent stuff</p>

#### [ Patrick Massot (Oct 19 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/136137628):
<p>I notice that it helps publishing CS papers to promise stuff for free. It seems most papers titles in this area contain this promise.</p>

#### [ Andrew Ashworth (Oct 19 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/136138635):
<p>Everybody loves free things! This is a good paper, I linked it previously in the "hott for newbies" thread, and Mario made a few comments.</p>

#### [ Rudi Grinberg (Oct 20 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/136146880):
<p>Where is this thread? The search is failing me.</p>

#### [ Bryan Gin-ge Chen (Oct 20 2018 at 02:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/136146954):
<p>It's <a href="#narrow/stream/113488-general/subject/what.20is.20wrong.20with.20HoTT/near/135265404" title="#narrow/stream/113488-general/subject/what.20is.20wrong.20with.20HoTT/near/135265404">here</a>.</p>

#### [ Bryan Gin-ge Chen (Oct 20 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/136147013):
<p>As a side note, I've found that by default, searching Zulip doesn't turn up results from before I joined the server. However, it does if I additionally include "stream:general" or "stream:maths", etc.</p>

#### [ Patrick Massot (Oct 20 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transport%20forever/near/136162441):
<blockquote>
<p>Everybody loves free things! This is a good paper, I linked it previously in the "hott for newbies" thread, and Mario made a few comments.</p>
</blockquote>
<p>Thanks! I was sure it had been mentioned, I even told <span class="user-mention" data-user-id="110172">@Assia Mahboubi</span> but I couldn't find it.</p>


{% endraw %}
