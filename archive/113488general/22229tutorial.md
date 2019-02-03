---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/22229tutorial.html
---

## Stream: [general](index.html)
### Topic: [tutorial](22229tutorial.html)

---


{% raw %}
#### [ Johan Commelin (Oct 04 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135155789):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> Would you mind pushing your demo to a new <code>tutorial</code> branch on community fork? Maybe as <code>docs/tutorial/demo.lean</code>.</p>

#### [ Johan Commelin (Oct 04 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135155799):
<p>After that we could attempt answering Neil's questions in that branch as well.</p>

#### [ Johan Commelin (Oct 04 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135155804):
<p>Q1 and Q2 have been done. They can easily be entered.</p>

#### [ Johan Commelin (Oct 04 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135155874):
<p>Q3 shouldn't be hard either. Q4 needs work. Q5 should be rather easy again.</p>

#### [ Johan Commelin (Oct 04 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135155893):
<p>The point is that we should write lots of comments in those files. So that people can actually learn a lot of Lean. Instead of learning only a tiny bit of maths (that they actually knew already).</p>

#### [ Patrick Massot (Oct 04 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135155894):
<p>Ok, I'll do that</p>

#### [ Bryan Gin-ge Chen (Oct 04 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135156024):
<p>If you're looking for help with this, I'd be happy to contribute. I think I should be able to do Q5.</p>

#### [ Johan Commelin (Oct 04 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135156040):
<p>Sure! Please contribute!</p>

#### [ Johan Commelin (Oct 04 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135156234):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> Do you have time to do this before the talks start? Otherwise I can start the branch... and you can dump your demo later (-;</p>

#### [ Patrick Massot (Oct 04 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135156333):
<p>depends on the RER train. I'm leaving my house, let's see when I'll arrive in Orsay</p>

#### [ Sean Leather (Oct 04 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135156338):
<p>I would recommend using a top-level <code>tutorial</code> directory instead of the subdirectory  under <code>docs</code>. First, it's more discoverable (easier to find). Second, I think many people expect <code>docs</code> to not be code, which could lead people to not look in there for code.</p>

#### [ Johan Commelin (Oct 04 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135156397):
<p>I'm fine with that. It depends on what the powers that be prefer (-; <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span></p>

#### [ Johannes Hölzl (Oct 04 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135156595):
<p>if we add tutorials, I would also prefer <code>tutorial</code> in the top level directory.</p>

#### [ Johannes Hölzl (Oct 04 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135156651):
<p>But we could also have a separate repository in <code>leanprover-community</code> then its easier to contribute</p>

#### [ Johan Commelin (Oct 04 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135156668):
<p>I think it is best to have this end up in mathlib. Because then we are forced to keep it working. Also: better discoverability</p>

#### [ Kevin Buzzard (Oct 04 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135161048):
<p>Stick it in the top level and it can be moved later</p>

#### [ Bryan Gin-ge Chen (Oct 05 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135240591):
<p>I've made some progress on Q5. Is someone (Patrick? Johan?) planning to make a branch in leanprover-community I can PR to?</p>

#### [ Johan Commelin (Oct 05 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135240650):
<p>Sorry, I have to do some other stuff now. Please go ahead and create the branch</p>

#### [ Patrick Massot (Oct 05 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135240799):
<p>I'll create the branch if you want</p>

#### [ Bryan Gin-ge Chen (Oct 05 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135240813):
<p>Sure, that'd be great.</p>

#### [ Patrick Massot (Oct 05 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135240831):
<p><a href="https://github.com/leanprover-community/mathlib/tree/tutorials" target="_blank" title="https://github.com/leanprover-community/mathlib/tree/tutorials">https://github.com/leanprover-community/mathlib/tree/tutorials</a></p>

#### [ Patrick Massot (Oct 05 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135240896):
<p>wait</p>

#### [ Patrick Massot (Oct 05 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135240898):
<p>I messed up</p>

#### [ Patrick Massot (Oct 05 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135240985):
<p>now it's ok</p>

#### [ Patrick Massot (Oct 05 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135241326):
<p>Ok, I've pushed my demo file: <a href="https://github.com/leanprover-community/mathlib/commit/bf36dd1e66d373c53666ca4579649f767955ed42" target="_blank" title="https://github.com/leanprover-community/mathlib/commit/bf36dd1e66d373c53666ca4579649f767955ed42">https://github.com/leanprover-community/mathlib/commit/bf36dd1e66d373c53666ca4579649f767955ed42</a></p>

#### [ Bryan Gin-ge Chen (Oct 05 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135241958):
<p>OK, I've PR'd my file for review <a href="https://github.com/leanprover-community/mathlib/pull/6" target="_blank" title="https://github.com/leanprover-community/mathlib/pull/6">here</a>.</p>

#### [ Johan Commelin (Oct 05 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135242037):
<p>You don't have write access to the community fork?</p>

#### [ Bryan Gin-ge Chen (Oct 05 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135242038):
<p>Oh, I guess not.</p>

#### [ Johan Commelin (Oct 05 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135242098):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> <span class="user-mention" data-user-id="110026">@Simon Hudon</span> can one of you fix this?</p>

#### [ Simon Hudon (Oct 05 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135242854):
<p>Done</p>

#### [ Simon Hudon (Oct 05 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135242861):
<p>And now, I'm off. Good day!</p>

#### [ Johan Commelin (Oct 05 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135242909):
<p>Sleep tight!</p>

#### [ Simon Hudon (Oct 05 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135242942):
<p>Thanks :) <span class="emoji emoji-1f4a4" title="zzz">:zzz:</span></p>

#### [ Bryan Gin-ge Chen (Oct 05 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135254193):
<p>Thanks Simon!</p>

#### [ Bryan Gin-ge Chen (Oct 05 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135254614):
<p>I've gone ahead and merged my PR. Here are two specific questions, and I would appreciate any other comments as well:</p>
<p>1) I'm not sure how to finish <a href="https://github.com/leanprover-community/mathlib/blob/tutorials/tutorials/partitions.lean#L96" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/tutorials/tutorials/partitions.lean#L96">this proof</a>.</p>
<p>2) The forward and backward directions in the <code>iff.intro</code> <a href="https://github.com/leanprover-community/mathlib/blob/4752d91c7e0781e275e6a14edafcbf1a73b8c8ae/tutorials/partitions.lean#L134" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/4752d91c7e0781e275e6a14edafcbf1a73b8c8ae/tutorials/partitions.lean#L134">here</a> are identical except that the roles of <code> s₁</code> and <code>s₂</code> are swapped. Is there a cleaner way to do this? I thought about using <code>wlog</code> but I couldn't figure out how to use it in this case.</p>

#### [ Kevin Buzzard (Oct 05 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135259968):
<blockquote>
<p>1) I'm not sure how to finish <a href="https://github.com/leanprover-community/mathlib/blob/tutorials/tutorials/partitions.lean#L96" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/tutorials/tutorials/partitions.lean#L96">this proof</a>.</p>
</blockquote>
<p>Oh I love these questions. Mathematicians don't even give them a second thought. You have two finite types with the same cardinality and and you want to conclude that some operation on the type which only depends on the cardinality (e.g. the cardinality of the number of partitions) is the same for each. This is stupidly hard to do in Lean and it's coming up more and more. The general problem is that if you have two types which are equivalent (i.e. you are given inverse bijections between the types and proofs that the maps are inverse to each other on both sides) then a mathematician instantly identifies the types, and any reasonable theorem or definition constructed with one has an obvious counterpart for the other. Now someone will explain that yeah in theory this can all be done with <code>traversable</code> or <code>transportable</code> or something, but I can't do this because I don't really understand what needs to be done. We've just missed <span class="user-mention" data-user-id="110026">@Simon Hudon</span> but he knows something about this sort of question. My guess is that you need to prove that if the cards are the same then there's an <code>equiv</code> (which might well be there), and then you want to prove that if <code>X equiv Y</code> then <code>partitions X equiv partitions Y</code> (which looks trivial but might involve some actual work) and then you want to prove that partitions X equiv partitions Y then the cards are the same, which might well be there.</p>

#### [ Simon Hudon (Oct 05 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135260449):
<p>Thanks for cueing me in <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span>! That is indeed a nice question!</p>

#### [ Bryan Gin-ge Chen (Oct 05 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135260515):
<blockquote>
<p>if the cards are the same then there's an equiv (which might well be there), </p>
</blockquote>
<p>Yeah, I was attempting to use <code>fintype.equiv_fin</code>for that but it gives me an equiv wrapped up in <code>trunc</code>... so I gave up and decided to ask for help.</p>

#### [ Kevin Buzzard (Oct 05 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135261258):
<p>The example I ran into in around Feb/Mar time was that I had a complex of abelian groups <code>A -&gt; B -&gt; C</code> and an isomorphic (in the obvious sense) complex <code>A' -&gt; B' -&gt; C'</code> and wanted to deduce that these two complexes had isomorphic cohomology -- in fact I had several questions of this nature. I wanted the isomorphism to be explictly built for me by a tactic but in the end I don't think this ever happened.</p>

#### [ Kevin Buzzard (Oct 05 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135261330):
<p>People ground out proofs very quickly -- "this is an isomorphism and this is an isomorphism so this map between kernels is an isomorphism, and now this map between images is an isomorphism, and..." but they really had to build them</p>

#### [ Kevin Buzzard (Oct 05 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135261383):
<p>But I want proof by a tactic called <code>mathematical_intuition</code> or <code>transport_de_structure</code> or something</p>

#### [ Kevin Buzzard (Oct 05 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135261600):
<p>and my understanding was that making a tactic would somehow involve having to go through a bunch of Lean theorems or definitions applying to abelian groups, and tagging them with an attribute which is a claim that this function some of whose inputs or outputs are abelian groups "naturally" descends to a function whose inputs and outputs are equivalence classes of abelian groups, where the equivalence is given by group isomorphism.</p>

#### [ Kevin Buzzard (Oct 05 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135261654):
<p>And I think the idea was that some of the attribute-tagging could be done automatically.</p>

#### [ Simon Hudon (Oct 05 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135261659):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I did build some isomorphisms with a tactic but I got some push back because transport was seem as redundant with transfer and I didn't take it any further</p>

#### [ Kevin Buzzard (Oct 05 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135261668):
<p><code>transfer</code>, that's it.</p>

#### [ Kevin Buzzard (Oct 05 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135261673):
<p>Thanks Simon.</p>

#### [ Simon Hudon (Oct 05 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135261691):
<p><span class="emoji emoji-1f44d" title="+1">:+1:</span></p>

#### [ Simon Hudon (Oct 05 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135261724):
<p><span class="user-mention" data-user-id="123965">@Bryan Gin-ge Chen</span> <code>trunc</code> should not deter you. You can unwrap it when you're proving a proposition.</p>

#### [ Simon Hudon (Oct 05 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135261750):
<p>It just states that the object exists in a non constructive way</p>

#### [ Kevin Buzzard (Oct 05 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135261789):
<p>This is an important tactic for mathematicians and it isn't there. Bryan's question is a great example of an EIMHIL questions (easy in maths, hard in Lean). The exciting thing about this community is that several times in the past I have explicitly flagged things which were easy in maths but hard in Lean, and other members of the community like Simon, Mario and Johannes sometimes step up and make them easy in Lean. The <code>ring</code> tactic is a great example of this.</p>

#### [ Simon Hudon (Oct 05 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135261791):
<p>Look at <code>trunc.induction_on</code></p>

#### [ Kevin Buzzard (Oct 05 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135261831):
<p>Simon, do you know if is there a relatively easy way to patch up the sorry completely?</p>

#### [ Simon Hudon (Oct 05 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135261837):
<p>:D Glad to be helpful. I think Lean won't be as easy as math (!) but there certainly are a lot of low hanging fruits to make it a lot easier to use.</p>

#### [ Kevin Buzzard (Oct 05 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135261924):
<p><span class="user-mention" data-user-id="110865">@Jeremy Avigad</span> I would be really interested to hear your opinion on what a mathematician <em>means</em> when they say that two objects are "canonically isomorphic".</p>

#### [ Kevin Buzzard (Oct 05 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135261940):
<p>This is notion which is somehow still missing in my Lean experience.</p>

#### [ Kevin Buzzard (Oct 05 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135261980):
<p>I contributed to some mathoverflow chat about this once</p>

#### [ Kevin Buzzard (Oct 05 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135262053):
<p><a href="https://mathoverflow.net/questions/19644/what-is-the-definition-of-canonical/19663#19663" target="_blank" title="https://mathoverflow.net/questions/19644/what-is-the-definition-of-canonical/19663#19663">https://mathoverflow.net/questions/19644/what-is-the-definition-of-canonical/19663#19663</a></p>

#### [ Simon Hudon (Oct 05 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135262059):
<blockquote>
<p>Simon, do you know if is there a relatively easy way to patch up the sorry completely?</p>
</blockquote>
<p>I'll look into it</p>

#### [ Kevin Buzzard (Oct 05 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135262100):
<p>Oh I just wondered whether you knew immediately that this would be a relatively straightforward sorry to remove. Like when Patrick asks silly questions about subs on nats not working properly and I know I can prove every one because I just know how they work better than he does in some funny way.</p>

#### [ Kevin Buzzard (Oct 05 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135262150):
<p>I think he can do them too, but they just annoy him too much :-)</p>

#### [ Bryan Gin-ge Chen (Oct 05 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135262174):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> Ah, thanks! Up to now I've been getting away with just applying lemmas and not really thinking much about how things are actually set up using inductive types and such, but now I should probably turn my brain on.</p>

#### [ Kevin Buzzard (Oct 05 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135262176):
<p>but I have no idea whether Bryan's sorry is easy to fill in or not. In some sense Neil Strickland is exhibiting a problem with doing mathematics in Lean here.</p>

#### [ Kevin Buzzard (Oct 05 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135262251):
<p>And it's a problem I stumbled upon when doing schemes and so no doubt is looming when the perfectoid project gets really moving again</p>

#### [ Kevin Buzzard (Oct 05 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135262278):
<p>We will need to be replacing complete topological rings with canonically isomorphic complete topological rings left right and centre.</p>

#### [ Kevin Buzzard (Oct 05 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135262354):
<p>where by canonically isomorphic I mean an explicit <code>equiv</code> of morphisms in the appropriate category.</p>

#### [ Simon Hudon (Oct 05 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135262623):
<p><span class="user-mention" data-user-id="123965">@Bryan Gin-ge Chen</span> It's a common experience I find. E. W. Dijkstra had a nice way to put it: just let the symbols do the work.</p>

#### [ Simon Hudon (Oct 05 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135262725):
<p>It's taking me a little bit to boot up my brain but I have my coffee now so I should be able to understand a bit more. But Kevin had the right idea I think: you need a congruence lemma for <code>partition</code> with regards to <code>equiv</code></p>

#### [ Simon Hudon (Oct 05 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135262743):
<p>For the rest, let's see where the symbols take us</p>

#### [ Kevin Buzzard (Oct 05 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135264259):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> is that sorry above easy to fill in?</p>

#### [ Bryan Gin-ge Chen (Oct 05 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135264261):
<p>OK, I think I have a rough idea of what to look at now.  It's rather hard to figure out how to use something new, e.g. <code>equiv</code> when there isn't a chapter of TPiL to fall back on. It doesn't help that core lean has <code>has_equiv</code> which is apparently just unrelated notation. At least mathlib itself provides plenty of example code to learn from. Anyways, hopefully these tutorials will help future users...</p>

#### [ Kevin Buzzard (Oct 05 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135264271):
<p><a href="https://github.com/leanprover-community/mathlib/blob/tutorials/tutorials/partitions.lean#L96" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/tutorials/tutorials/partitions.lean#L96">https://github.com/leanprover-community/mathlib/blob/tutorials/tutorials/partitions.lean#L96</a></p>

#### [ Simon Hudon (Oct 05 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135264295):
<p>I'm almost done proving:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">card_eq_of_equiv</span> <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">t</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">β</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">s</span><span class="bp">.</span><span class="n">to_set</span> <span class="err">≃</span> <span class="n">t</span><span class="bp">.</span><span class="n">to_set</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">s</span><span class="bp">.</span><span class="n">card</span> <span class="bp">=</span> <span class="n">t</span><span class="bp">.</span><span class="n">card</span> <span class="o">:=</span>  <span class="bp">...</span>
</pre></div>


<p>if you want to wait a moment</p>

#### [ Kevin Buzzard (Oct 05 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135264308):
<p><code>equiv X Y</code> is the best kind of bijection between two types <code>X</code> and <code>Y</code>.</p>

#### [ Kevin Buzzard (Oct 05 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135264376):
<p>It's an explicit map from <code>X</code> to <code>Y</code> and an explicit inverse.</p>

#### [ Kevin Buzzard (Oct 05 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135264419):
<p>Just saying "there's a map and it's a bijection" is slightly less information in Lean, because they need the computer science version of the axiom of choice (getting data from proofs of existence), so <code>equiv</code> is the important one to focus on.</p>

#### [ Bryan Gin-ge Chen (Oct 05 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135264426):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> Cool! I'm still digesting other code so you'll probably finish before I even get close to attempting my own version.</p>

#### [ Kevin Buzzard (Oct 05 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135264431):
<p>The problem is that <code>equiv</code> is what mathematicians would think of as a canonical bijection between two sets.</p>

#### [ Kevin Buzzard (Oct 05 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135264494):
<p>There are other equivs too -- group isomorphisms, topological space isomorphism etc.</p>

#### [ Kevin Buzzard (Oct 05 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135264510):
<p>And then there is a whole bunch of stuff defined on types or groups or whatever, which descends to the equivalence classes under these various equivalence relations.</p>

#### [ Kevin Buzzard (Oct 05 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135264591):
<p>And for mathematicians these are all "proof by obvious", so it's clear there's a tactic brewing. But we don't have that tactic yet.</p>

#### [ Kevin Buzzard (Oct 05 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135264690):
<p>And without it, replacing a topological monoid with a canonically isomorphic topological monoid in a complex of topological monoids and then proving that the cohomology of the complex "hasn't changed" (when Lean actually can see that it _has_ changed in some sense) is going to be hard work I think.</p>

#### [ Bryan Gin-ge Chen (Oct 05 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135264916):
<p>It's certainly eye-opening (in a good way, probably). I remember having vaguely similar feelings about all the calculus I thought I knew when I took analysis.</p>

#### [ Simon Hudon (Oct 05 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135266320):
<p><span class="user-mention" data-user-id="123965">@Bryan Gin-ge Chen</span> The short answer to your question is: yes it's feasible. You need congruence of <code>partitions</code> with regards to <code>equiv</code> and congruence of <code>card</code> with regards to congruence as well. I'm completing the proof now if you want it. It you want to do it yourself, you can use these three hints:</p>
<p>1. prove congruence of partitions<br>
2. prove congruence of card<br>
3. use trunc.induction_on</p>

#### [ Bryan Gin-ge Chen (Oct 05 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135266793):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> Great, thanks so much! Feel free to push your proofs into the tutorials branch if you'd like. I'll try to study them and add tutorial-style documentation later on.</p>

#### [ Kevin Buzzard (Oct 05 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135266877):
<blockquote>
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> Great, thanks so much! Feel free to push your proofs into the tutorials branch if you'd like. I'll try to study them and add tutorial-style documentation later on.</p>
</blockquote>
<p>This should not be being documented. This should be being hidden by tactics, no?</p>

#### [ Kevin Buzzard (Oct 05 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135266939):
<p>"We now do a big song and dance to replace an object with a canonically isomorphic object". I'm sure the mathematicians would be fascinated :-)</p>

#### [ Kevin Buzzard (Oct 05 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135266952):
<p>I think there's something missing here.</p>

#### [ Kevin Buzzard (Oct 05 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135266989):
<p>It's rw for data somehow</p>

#### [ Kevin Buzzard (Oct 05 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135267068):
<p>We want a rw that eats equivs, not equalities and iffs, and works for data in situations where we only care about the answer up to canonical isomorphism.</p>

#### [ Simon Hudon (Oct 05 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135267175):
<p>That would be nice. It involves proving congruence about a ton of functions though. The nice thing about <code>=</code> is that every function preserves it.</p>

#### [ Simon Hudon (Oct 05 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135267222):
<p>Such a tactic as you're describing is doable. We only need to decide how high it needs to be on the priority list</p>

#### [ Kevin Buzzard (Oct 05 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135267239):
<p>I think we've had this discussion before. Wasn't there some hope that by proving some lemmas about the basic constructors in Lean one could then go on and get a machine to generate all the congruence lemmas automatically?</p>

#### [ Kevin Buzzard (Oct 05 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135267426):
<p>Can the <code>transfer</code> tactic be turned into this mega-rw tactic? Very often in mathematics people only care about the answer up to isomorphism or perhaps a well-defined notion of canonical isomorphism (maybe it's part of the story that the object is unique up to unique isomorphism, for example).</p>

#### [ Kevin Buzzard (Oct 05 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135267545):
<p>we want to be able to rewrite isomorphic perfectoid spaces. Is Lean up to that?</p>

#### [ Simon Hudon (Oct 05 2018 at 19:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135267731):
<p>I remember building group isomorphism from their underlying type isomorphism but I don't remember the rest of the discussion that you're referring to.</p>

#### [ Simon Hudon (Oct 05 2018 at 19:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135267823):
<p>But in my libraries, I have some code to construct an isomorphism from an arbitrary type to sums and pairs. With Jeremy, we're talking about adding support for reasoning about W-types which should complete the picture to building isomorphism to canonical type representations</p>

#### [ Simon Hudon (Oct 05 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135267946):
<p>Maybe that's what you're looking for?</p>

#### [ Kevin Buzzard (Oct 05 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135268845):
<p>I'm looking for magic</p>

#### [ Kevin Buzzard (Oct 05 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135268851):
<p><code>example (X Y : Type) (f : Type → Type) (h : equiv X Y) : equiv (f X) (f Y) := by rw h</code></p>

#### [ Kevin Buzzard (Oct 05 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135268880):
<p>Mario sometimes tells me that this isn't always true, but I'm not sure I've ever seen a mathematical example of it going wrong.</p>

#### [ Kevin Buzzard (Oct 05 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135268942):
<p>Here <code>equiv</code> could mean an <code>equiv</code> of structures, and then f is somehow known to preserve all the structure.</p>

#### [ Kevin Buzzard (Oct 05 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135268989):
<p>Is that magic Simon?</p>

#### [ Kevin Buzzard (Oct 05 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135269044):
<p>This time round I have a far more mature understanding of what I think is missing.</p>

#### [ Simon Hudon (Oct 05 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135269222):
<p>What we probably need is a type class to tell us that <code>f</code> preserves <code>equiv</code>. Then <code>iso_rw h</code> (a tactic we want to build) would know how to build the proof. As it is, <code>rw</code> builds its proofs using <code>congr_arg</code> and <code>congr_fun</code> which needs no assumptions about <code>f</code>. We need basically the same tools for <code>equiv</code>.</p>

#### [ Kevin Buzzard (Oct 05 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135269351):
<p>It would be interesting to find out when this is going to bite the perfectoid project and how badly it will bite it. With schemes it bit us when we were doing structure sheaves. Here we only have structure presheaves but who knows.</p>

#### [ Kevin Buzzard (Oct 05 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135269402):
<p>In the schemes project I ended up writing some really weird code.</p>

#### [ Kevin Buzzard (Oct 05 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135269745):
<p><a href="https://github.com/kbuzzard/lean-stacks-project/blob/53bea440dc519a1f6d023cbecc2dfe270499bbbf/src/tag01HR.lean#L210" target="_blank" title="https://github.com/kbuzzard/lean-stacks-project/blob/53bea440dc519a1f6d023cbecc2dfe270499bbbf/src/tag01HR.lean#L210">https://github.com/kbuzzard/lean-stacks-project/blob/53bea440dc519a1f6d023cbecc2dfe270499bbbf/src/tag01HR.lean#L210</a></p>

#### [ Kevin Buzzard (Oct 05 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135269818):
<p>Over 350 (admittedly very inelegant and much commented) lines of code, to prove something which de Jong dismisses with one throwaway comment.</p>

#### [ Kevin Buzzard (Oct 05 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135269955):
<p>"Thus we may apply Algebra, Lemma 10.23.1 to the module <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>M</mi><mi>f</mi></msub></mrow><annotation encoding="application/x-tex">M_f</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.969438em;vertical-align:-0.286108em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.10903em;">M</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3361079999999999em;"><span style="top:-2.5500000000000003em;margin-left:-0.10903em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight" style="margin-right:0.10764em;">f</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.286108em;"></span></span></span></span></span></span></span></span> over <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>R</mi><mi>f</mi></msub></mrow><annotation encoding="application/x-tex">R_f</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.969438em;vertical-align:-0.286108em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.3361079999999999em;"><span style="top:-2.5500000000000003em;margin-left:-0.00773em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight" style="margin-right:0.10764em;">f</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.286108em;"></span></span></span></span></span></span></span></span> and the elements <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>g</mi><mn>1</mn></msub><mo separator="true">,</mo><mo>…</mo><mo separator="true">,</mo><msub><mi>g</mi><mi>n</mi></msub></mrow><annotation encoding="application/x-tex">g_1,\ldots,g_n</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.625em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.03588em;">g</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:-0.03588em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">1</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span><span class="mpunct">,</span><span class="minner">…</span><span class="mpunct">,</span><span class="mord"><span class="mord mathit" style="margin-right:0.03588em;">g</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.151392em;"><span style="top:-2.5500000000000003em;margin-left:-0.03588em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span>." Note that Chris had already proved the lemma. The issue was applying it.</p>

#### [ Kevin Buzzard (Oct 05 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135270021):
<p>because <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi><mo>[</mo><mn>1</mn><mi mathvariant="normal">/</mi><mi>f</mi><mo>]</mo><mo>[</mo><mn>1</mn><mi mathvariant="normal">/</mi><mi>g</mi><mo>]</mo></mrow><annotation encoding="application/x-tex">R[1/f][1/g]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mopen">[</span><span class="mord mathrm">1</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mclose">]</span><span class="mopen">[</span><span class="mord mathrm">1</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.03588em;">g</span><span class="mclose">]</span></span></span></span> was only canonically isomorphic to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi><mo>[</mo><mn>1</mn><mi mathvariant="normal">/</mi><mi>f</mi><mi>g</mi><mo>]</mo></mrow><annotation encoding="application/x-tex">R[1/fg]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mopen">[</span><span class="mord mathrm">1</span><span class="mord mathrm">/</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mord mathit" style="margin-right:0.03588em;">g</span><span class="mclose">]</span></span></span></span></p>

#### [ Scott Morrison (Oct 05 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135284021):
<blockquote>
<p>"We now do a big song and dance to replace an object with a canonically isomorphic object". I'm sure the mathematicians would be fascinated :-)</p>
</blockquote>
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span>, have you seen <span class="user-mention" data-user-id="130272">@David Michael Roberts</span> attempt to summarise the latest disagreement between Mochizuki and Scholze? &lt;<a href="https://thehighergeometer.files.wordpress.com/2018/09/mochizuki_final1.pdf" target="_blank" title="https://thehighergeometer.files.wordpress.com/2018/09/mochizuki_final1.pdf">https://thehighergeometer.files.wordpress.com/2018/09/mochizuki_final1.pdf</a>&gt;. It's very much about whether such replacements were valid or not.</p>

#### [ Kevin Buzzard (Oct 06 2018 at 02:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135291222):
<p>Wow I had not seen that. Thanks.</p>

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135298733):
<p>Is there an easy proof of this (is it secretly in mathlib)? I did this the hard way with <code>ext</code> and lots of digging back and forth through exists statements:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">embedding_of_finset</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="err">↪</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span> <span class="err">↪</span> <span class="n">finset</span> <span class="n">β</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">S</span><span class="o">,</span> <span class="n">S</span><span class="bp">.</span><span class="n">map</span> <span class="n">f</span><span class="o">,</span> <span class="k">by</span> <span class="o">{</span>
  <span class="n">unfold</span> <span class="n">function</span><span class="bp">.</span><span class="n">injective</span><span class="o">,</span>
  <span class="n">intros</span> <span class="n">a₁</span> <span class="n">a₂</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">finset</span><span class="bp">.</span><span class="n">ext</span><span class="o">]</span> <span class="n">at</span> <span class="n">h</span> <span class="err">⊢</span><span class="o">,</span>
  <span class="n">intro</span> <span class="n">x</span><span class="o">,</span>
  <span class="n">split</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">intro</span> <span class="n">H</span><span class="o">,</span>
    <span class="k">have</span> <span class="n">hex</span> <span class="o">:=</span> <span class="o">(</span><span class="n">h</span> <span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">))</span><span class="bp">.</span><span class="n">mp</span> <span class="o">(</span><span class="n">exists</span><span class="bp">.</span><span class="n">intro</span> <span class="n">x</span> <span class="bp">⟨</span><span class="n">H</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span><span class="o">),</span>
    <span class="n">exact</span> <span class="n">exists</span><span class="bp">.</span><span class="n">elim</span> <span class="n">hex</span> <span class="o">(</span><span class="k">by</span> <span class="o">{</span> <span class="n">intros</span> <span class="n">y</span> <span class="n">hy</span><span class="o">,</span>
      <span class="k">have</span> <span class="o">:</span> <span class="n">y</span> <span class="bp">=</span> <span class="n">x</span> <span class="o">:=</span> <span class="n">f</span><span class="bp">.</span><span class="mi">2</span> <span class="n">hy</span><span class="bp">.</span><span class="mi">2</span><span class="o">,</span>
      <span class="n">exact</span> <span class="n">this</span> <span class="bp">▸</span> <span class="n">hy</span><span class="bp">.</span><span class="mi">1</span> <span class="o">})</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">intro</span> <span class="n">H</span><span class="o">,</span>
    <span class="k">have</span> <span class="n">hex</span> <span class="o">:=</span> <span class="o">(</span><span class="n">h</span> <span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">))</span><span class="bp">.</span><span class="n">mpr</span> <span class="o">(</span><span class="n">exists</span><span class="bp">.</span><span class="n">intro</span> <span class="n">x</span> <span class="bp">⟨</span><span class="n">H</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span><span class="o">),</span>
    <span class="n">exact</span> <span class="n">exists</span><span class="bp">.</span><span class="n">elim</span> <span class="n">hex</span> <span class="o">(</span><span class="k">by</span> <span class="o">{</span> <span class="n">intros</span> <span class="n">y</span> <span class="n">hy</span><span class="o">,</span>
      <span class="k">have</span> <span class="o">:</span> <span class="n">y</span> <span class="bp">=</span> <span class="n">x</span> <span class="o">:=</span> <span class="n">f</span><span class="bp">.</span><span class="mi">2</span> <span class="n">hy</span><span class="bp">.</span><span class="mi">2</span><span class="o">,</span>
      <span class="n">exact</span> <span class="n">this</span> <span class="bp">▸</span> <span class="n">hy</span><span class="bp">.</span><span class="mi">1</span> <span class="o">})</span> <span class="o">}</span> <span class="o">}</span><span class="bp">⟩</span>
</pre></div>

#### [ Johan Commelin (Oct 06 2018 at 07:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135299119):
<blockquote>
<blockquote>
<p>"We now do a big song and dance to replace an object with a canonically isomorphic object". I'm sure the mathematicians would be fascinated :-)</p>
</blockquote>
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span>, have you seen <span class="user-mention" data-user-id="130272">@David Michael Roberts</span> attempt to summarise the latest disagreement between Mochizuki and Scholze? &lt;<a href="https://thehighergeometer.files.wordpress.com/2018/09/mochizuki_final1.pdf" target="_blank" title="https://thehighergeometer.files.wordpress.com/2018/09/mochizuki_final1.pdf">https://thehighergeometer.files.wordpress.com/2018/09/mochizuki_final1.pdf</a>&gt;. It's very much about whether such replacements were valid or not.</p>
</blockquote>
<p><span class="user-mention" data-user-id="130272">@David Michael Roberts</span> Thanks for writing these!</p>

#### [ Mario Carneiro (Oct 06 2018 at 07:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135299259):
<p>oops... I was too focused on the image properties and forgot about the fact that the function is injective</p>

#### [ Simon Hudon (Oct 06 2018 at 07:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135299510):
<p>I pushed something like that to <code>tutorial</code> and called it <code>map'</code></p>

#### [ Simon Hudon (Oct 06 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135299600):
<p>Also, I finished the proof of <code>card_partitions_eq_card_partitions_fin</code> in the partition tutorial. It needed much more work than I thought</p>

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135299601):
<p>Ah, perfect! I was so engrossed in my attempt that I missed your commit.</p>

#### [ Simon Hudon (Oct 06 2018 at 07:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135299610):
<p>The big changes that I made was using <code>finset.sup</code> in the formulation of partition instead of using <code>multiset</code>s which required a few lemmas in <code>finset</code></p>

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 07:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135300028):
<p>Very nice! Using <code>sup</code> is much cleaner than the hack I was using with multiset.</p>
<p><a href="https://gist.github.com/bryangingechen/4ba169f7db65711a07643cf213039049#file-partitions-lean-L282" target="_blank" title="https://gist.github.com/bryangingechen/4ba169f7db65711a07643cf213039049#file-partitions-lean-L282">Here's what I had</a>. Now that I've looked at what you did, I see there's still a ton of stuff needed to fill in the sorry at line 292. In particular I hadn't even started on something like <code>partitions_congr</code> yet and that was definitely also necessary.</p>

#### [ David Michael Roberts (Oct 06 2018 at 07:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135300233):
<blockquote>
<blockquote>
<blockquote>
<p>"We now do a big song and dance to replace an object with a canonically isomorphic object". I'm sure the mathematicians would be fascinated :-)</p>
</blockquote>
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span>, have you seen <span class="user-mention" data-user-id="130272">@David Michael Roberts</span> attempt to summarise the latest disagreement between Mochizuki and Scholze? &lt;<a href="https://thehighergeometer.files.wordpress.com/2018/09/mochizuki_final1.pdf" target="_blank" title="https://thehighergeometer.files.wordpress.com/2018/09/mochizuki_final1.pdf">https://thehighergeometer.files.wordpress.com/2018/09/mochizuki_final1.pdf</a>&gt;. It's very much about whether such replacements were valid or not.</p>
</blockquote>
<p><span class="user-mention" data-user-id="130272">@David Michael Roberts</span> Thanks for writing these!</p>
</blockquote>
<p>You're welcome!</p>

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135300977):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> Just a heads-up, I'm rebuilding tutorial and I think your changes to <code>ext</code> have broken the proofs of various things in category_theory and holor.</p>

#### [ Simon Hudon (Oct 06 2018 at 08:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135300987):
<p>Sorry about that. You can revert them for now.</p>

#### [ Simon Hudon (Oct 06 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135301074):
<p>For the last <code>sorry</code>, do you need the lattice to be different from the lattice on finite sets?</p>

#### [ Simon Hudon (Oct 06 2018 at 08:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135301119):
<p>Ok, I see your definition of subset. I'll pick it up tomorrow if you haven't managed to solve it</p>

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 08:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135301126):
<p>Yeah, I was thinking of implementing as a bonus <a href="https://en.wikipedia.org/wiki/Partition_of_a_set#Refinement_of_partitions" target="_blank" title="https://en.wikipedia.org/wiki/Partition_of_a_set#Refinement_of_partitions">the lattice structure described here</a>.</p>

#### [ Simon Hudon (Oct 06 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135301169):
<p>Ah! I see! You can somehow decrease a partition by taking one of its parts and splitting it, right?</p>

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135301174):
<p>Exactly.</p>

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135301305):
<p>I think I could muddle my way through that eventually, though you're definitely welcome to work on it if you want to. I'd also appreciate comments on the other proofs / tutorial text that I've added if you've had a chance to look at them.</p>

#### [ Mario Carneiro (Oct 06 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135301647):
<p>If you use equivalence relations instead of partitions, this follows from the fact that equivalence relations have a Moore structure (they are closed under arbitrary intersection), so they have a complete lattice structure</p>

#### [ Johan Commelin (Oct 06 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135301756):
<p><span class="user-mention" data-user-id="123965">@Bryan Gin-ge Chen</span> <a href="https://github.com/leanprover-community/mathlib/blob/tutorials/tutorials/partitions.lean#L109" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/tutorials/tutorials/partitions.lean#L109">https://github.com/leanprover-community/mathlib/blob/tutorials/tutorials/partitions.lean#L109</a> Couldn't you just compare the <code>multiset.join</code> to the <code>multiset</code> that underlies our <code>finset</code>?</p>

#### [ Johan Commelin (Oct 06 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135301989):
<p><span class="user-mention" data-user-id="123965">@Bryan Gin-ge Chen</span> Consider adding an example to <a href="https://github.com/leanprover-community/mathlib/blob/tutorials/tutorials/partitions.lean#L193" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/tutorials/tutorials/partitions.lean#L193">https://github.com/leanprover-community/mathlib/blob/tutorials/tutorials/partitions.lean#L193</a> where the issue is multiplicity &gt; 1.</p>

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135302186):
<blockquote>
<p><span class="user-mention" data-user-id="123965">@Bryan Gin-ge Chen</span> <a href="https://github.com/leanprover-community/mathlib/blob/tutorials/tutorials/partitions.lean#L109" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/tutorials/tutorials/partitions.lean#L109">https://github.com/leanprover-community/mathlib/blob/tutorials/tutorials/partitions.lean#L109</a> Couldn't you just compare the <code>multiset.join</code> to the <code>multiset</code> that underlies our <code>finset</code>?</p>
</blockquote>
<p>Thanks for pointing this out. In fact, Simon has created a better solution for this using <code>sup</code> which is used in <code>partition_of_disjoint_union</code> right below. I'll edit...</p>
<p>I've added this example:</p>
<div class="codehilite"><pre><span></span><span class="bp">#</span><span class="kn">eval</span> <span class="o">(</span><span class="n">is_partition</span> <span class="o">({{</span><span class="mi">0</span><span class="o">},</span> <span class="o">{</span><span class="mi">1</span><span class="o">},</span> <span class="o">{</span><span class="mi">1</span><span class="o">,</span><span class="mi">3</span><span class="o">}}</span> <span class="o">:</span> <span class="n">finset</span> <span class="o">(</span><span class="n">finset</span> <span class="o">(</span><span class="n">fin</span> <span class="mi">4</span><span class="o">)))</span> <span class="o">:</span> <span class="n">bool</span><span class="o">)</span> <span class="c1">-- ff</span>
</pre></div>

#### [ Mario Carneiro (Oct 06 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135302235):
<p>I think this file could stand to be generalized quite a bit. I would want to see partitions defined as equivalence relations, forget the finiteness constraint, and forget the finset representatives</p>

#### [ Mario Carneiro (Oct 06 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135302244):
<p>Then, given this, you can define the Bell numbers by a recurrence (so they compute fast), and prove that the number of partitions on a finite set is a bell number</p>

#### [ Mario Carneiro (Oct 06 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135302257):
<p>At the same time, you can define an efficiently computable finset representation of a partition by recursion rather than filtering the universe</p>

#### [ Mario Carneiro (Oct 06 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135302304):
<p>this both proves the recursion scheme for calculating its size, and also gives an efficiently computable partition function on finset</p>

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135302314):
<p>That sounds cool. Is there a good place to read about this approach?</p>

#### [ Mario Carneiro (Oct 06 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135302320):
<p>not particularly... basically finsets are bad for proving stuff when you don't need finiteness explicitly</p>

#### [ Mario Carneiro (Oct 06 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135302360):
<p>you should use sets instead</p>

#### [ Mario Carneiro (Oct 06 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135302363):
<p>especially since "partition" generalizes so nicely to the infinite case</p>

#### [ Mario Carneiro (Oct 06 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135302371):
<p>If you need more details about some part about that let me know</p>

#### [ Mario Carneiro (Oct 06 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135302418):
<p>It would be nice to have the <a href="https://en.wikipedia.org/wiki/Bell_triangle" target="_blank" title="https://en.wikipedia.org/wiki/Bell_triangle">Bell triangle</a> used for calculating and defining the bell numbers</p>

#### [ Johan Commelin (Oct 06 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135302637):
<p>I guess Lean automatically memoizes computations? If I define <code>A n k = A (n-1) k + A n (k - 1)</code>, and I ask it to compute <code>A 10 5</code>, does that lead to combinatorial explosion? Or will it efficiently remember the terms it computed?</p>

#### [ Johan Commelin (Oct 06 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135302638):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> Do you know this?</p>

#### [ Mario Carneiro (Oct 06 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135302991):
<p>Just for fun:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">bell_aux₁</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="bp">×</span> <span class="n">list</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="bp">×</span> <span class="n">list</span> <span class="bp">ℕ</span>
<span class="bp">|</span> <span class="n">n</span> <span class="o">(</span><span class="n">r</span><span class="o">,</span> <span class="n">l</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="n">r</span><span class="o">,</span> <span class="n">n</span> <span class="bp">::</span> <span class="n">l</span><span class="o">)</span>

<span class="n">def</span> <span class="n">bell_triangle</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">list</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="bp">×</span> <span class="n">list</span> <span class="bp">ℕ</span>
<span class="bp">|</span> <span class="n">n</span> <span class="o">[]</span> <span class="o">:=</span> <span class="o">(</span><span class="n">n</span><span class="o">,</span> <span class="o">[])</span>
<span class="bp">|</span> <span class="n">n</span> <span class="o">(</span><span class="n">m</span> <span class="bp">::</span> <span class="n">l</span><span class="o">)</span> <span class="o">:=</span> <span class="k">let</span> <span class="n">n&#39;</span> <span class="o">:=</span> <span class="n">n</span> <span class="bp">+</span> <span class="n">m</span> <span class="k">in</span> <span class="n">bell_aux₁</span> <span class="n">n&#39;</span> <span class="o">(</span><span class="n">bell_triangle</span> <span class="n">n&#39;</span> <span class="n">l</span><span class="o">)</span>

<span class="n">def</span> <span class="n">bell_aux</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="bp">×</span> <span class="n">list</span> <span class="bp">ℕ</span>
<span class="bp">|</span> <span class="mi">0</span>     <span class="o">:=</span> <span class="o">(</span><span class="mi">1</span><span class="o">,</span> <span class="o">[])</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">k</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="k">let</span> <span class="o">(</span><span class="n">n</span><span class="o">,</span> <span class="n">l</span><span class="o">)</span> <span class="o">:=</span> <span class="n">bell_aux</span> <span class="n">k</span> <span class="k">in</span> <span class="n">bell_aux₁</span> <span class="n">n</span> <span class="o">(</span><span class="n">bell_triangle</span> <span class="n">n</span> <span class="n">l</span><span class="o">)</span>

<span class="n">def</span> <span class="n">bell</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="o">(</span><span class="n">bell_aux</span> <span class="n">n</span><span class="o">)</span><span class="bp">.</span><span class="mi">1</span>

<span class="bp">#</span><span class="kn">eval</span> <span class="n">list</span><span class="bp">.</span><span class="n">map</span> <span class="n">bell</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">range</span> <span class="mi">20</span><span class="o">)</span>
</pre></div>

#### [ Mario Carneiro (Oct 06 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135303001):
<p>lean does not memoize things unless you tell it to. This is one of the major shortcomings of lean 3</p>

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135303250):
<p>Is the efficient partition function on finset that you had in mind one based on the "Combinatorial Interpretation" in the Bell triangle wiki page?</p>

#### [ Johan Commelin (Oct 06 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135303251):
<p>Do we have a <code>memoize</code> monad that automagically does that for you?</p>

#### [ Mario Carneiro (Oct 06 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135303295):
<p>I PR'd one to core back in the day, rejected</p>

#### [ Mario Carneiro (Oct 06 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135303301):
<p>To do it in pure lean requires explicit maintenance of the accumulator data, in this case the <code>list nat</code> that forms the lines of the triangle as we progress</p>

#### [ Johan Commelin (Oct 06 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135303345):
<p>Right, but a pure Lean version might already be nice.</p>

#### [ Mario Carneiro (Oct 06 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135303346):
<p><span class="user-mention" data-user-id="123965">@Bryan Gin-ge Chen</span> Yes. That description of how to count partitions is exactly what you need to write a partition generating algorithm that obviously has length B_n</p>

#### [ Mario Carneiro (Oct 06 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135303357):
<p>Lean can't figure out your accumulator data for you, at least not effectively</p>

#### [ Mario Carneiro (Oct 06 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135303361):
<p>For example it's not completely obvious that you can calculate fibonacci numbers with a two number sliding window</p>

#### [ Johan Commelin (Oct 06 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135303406):
<p>I was thinking about a naive cache that would just remember all Fibonacci numbers. Don't bother about two number sliding windows. Or am I missing something?</p>

#### [ Mario Carneiro (Oct 06 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135303459):
<p>Well, yes that can be done, indeed that's how lean used to work</p>

#### [ Mario Carneiro (Oct 06 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135303498):
<p>Leo decided that this causes unpredictable performance characteristics (since it depends on how the equation compiler compiles your code)</p>

#### [ Mario Carneiro (Oct 06 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135303500):
<p>so now it just follows what you tell it, and if you use a bad algorithm then it's your fault</p>

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135318182):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> I've just pushed a commit that moves the more general lemmas you wrote in <code>partitions</code> to more appropriate places in <code>data.finset</code>, <code>data.fintype</code> and <code>data.equiv.basic</code>. Also, one of the <code>tactic.tfae</code> tests still fails, even after I reverted the <code>tactic.ext</code> change.</p>
<p>For now I think I'll leave the tutorial partitions file alone and see if I can make some progress working on Mario's idea in another file. If that turns out well that we can then decide whether we want to completely replace what we've done or perhaps include both approaches.</p>

#### [ Simon Hudon (Oct 07 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135327337):
<p>The <code>tfae</code> problem is separate. Maybe we should just remove it from master while I fix it</p>

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 03:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135333218):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I'm stuck on something dumb:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">set</span><span class="bp">.</span><span class="n">lattice</span>

<span class="kn">open</span> <span class="n">function</span>

<span class="kn">variable</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span>

<span class="c">/-</span><span class="cm"> We define a partition as a family of sets associated to an equivalence relation on a set -/</span>

<span class="kn">structure</span> <span class="n">partition</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">blocks</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">set</span> <span class="n">α</span><span class="o">))</span>
<span class="o">(</span><span class="n">empty_not_mem_blocks</span> <span class="o">:</span> <span class="n">blocks</span><span class="o">)</span>
<span class="o">(</span><span class="n">blocks_partition</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span><span class="o">,</span> <span class="bp">∃</span> <span class="n">b</span><span class="o">,</span> <span class="n">b</span> <span class="err">∈</span> <span class="n">blocks</span> <span class="bp">∧</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">b</span> <span class="bp">∧</span> <span class="bp">∀</span> <span class="n">b&#39;</span> <span class="err">∈</span> <span class="n">blocks</span><span class="o">,</span> <span class="n">b</span> <span class="bp">≠</span> <span class="n">b&#39;</span> <span class="bp">→</span> <span class="n">a</span> <span class="err">∉</span> <span class="n">b&#39;</span><span class="o">)</span>

<span class="n">def</span> <span class="n">coe_of_setoid</span> <span class="o">[</span><span class="n">setoid</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span> <span class="n">partition</span> <span class="n">α</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">blocks</span> <span class="o">:=</span> <span class="o">{</span><span class="n">t</span> <span class="bp">|</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">s₁</span> <span class="n">s₂</span><span class="o">),</span> <span class="n">s₁</span> <span class="err">∈</span> <span class="n">t</span> <span class="bp">→</span> <span class="n">s₂</span> <span class="err">∈</span> <span class="n">t</span> <span class="bp">→</span> <span class="n">s₁</span> <span class="bp">≈</span> <span class="n">s₂</span> <span class="o">},</span>
  <span class="n">empty_not_mem_blocks</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">blocks_partition</span> <span class="o">:=</span> <span class="n">sorry</span> <span class="o">}</span>
</pre></div>


<p>I can't seem to prove that the empty set isn't contained in <code>blocks</code>. I also tried <code>blocks :=  {t | ∃ a, s ∈ t → a ≈ s}</code> without success.</p>

#### [ Mario Carneiro (Oct 07 2018 at 03:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135333262):
<p><code>blocks := {t | ∃ a, {b | a ≈ b} = t}</code></p>

#### [ Mario Carneiro (Oct 07 2018 at 03:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135333265):
<p>You can also write this as the range of a function</p>

#### [ Mario Carneiro (Oct 07 2018 at 03:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135333318):
<blockquote>
<p><code>blocks :=  {t | ∃ a, s ∈ t → a ≈ s}</code></p>
</blockquote>
<p>This gives the set of subsets of some equivalence class</p>
<blockquote>
<p><code>blocks := {t | ∀ (s₁ s₂), s₁ ∈ t → s₂ ∈ t → s₁ ≈ s₂ }</code></p>
</blockquote>
<p>This gives the set of unions of equivalence classes</p>

#### [ Mario Carneiro (Oct 07 2018 at 03:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135333360):
<blockquote>
<p><code>(empty_not_mem_blocks : blocks)</code></p>
</blockquote>
<p>The type on this isn't quite right...</p>

#### [ Mario Carneiro (Oct 07 2018 at 03:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135333367):
<p>But I don't think you should think much about this definition of partition. As far as possible you should just use equivalence relations</p>

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 03:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135333410):
<p>Ah, thanks! I need to be more careful...</p>
<p>I do have <code>(empty_not_mem_blocks : ∅ ∉ blocks)</code>. I think I accidentally deleted it when I was  writing my previous message.</p>

#### [ Mario Carneiro (Oct 07 2018 at 03:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135333420):
<p>I would hope to be able to use <code>quot</code> to talk about equivalence classes, rather than sets</p>

#### [ Mario Carneiro (Oct 07 2018 at 03:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135333422):
<p>but that doesn't fit in this definition of partition</p>

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 03:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135333519):
<p>OK, so I should just try to define poset / lattice instances on <code>setoid α</code>.</p>

#### [ Mario Carneiro (Oct 07 2018 at 03:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135333682):
<p>yes, that should work</p>

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 04:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135335317):
<p>This works:</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">:</span> <span class="n">has_subset</span> <span class="o">(</span><span class="n">setoid</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">r₁</span> <span class="n">r₂</span><span class="o">,</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="k">let</span> <span class="n">r1</span> <span class="o">:=</span> <span class="n">r₁</span><span class="bp">.</span><span class="n">r</span> <span class="k">in</span> <span class="k">let</span> <span class="n">r2</span> <span class="o">:=</span> <span class="n">r₂</span><span class="bp">.</span><span class="n">r</span> <span class="k">in</span> <span class="o">{</span><span class="n">b</span> <span class="bp">|</span> <span class="n">r1</span> <span class="n">a</span> <span class="n">b</span><span class="o">}</span> <span class="err">⊆</span> <span class="o">{</span><span class="n">b</span> <span class="bp">|</span> <span class="n">r2</span> <span class="n">a</span> <span class="n">b</span><span class="o">}</span><span class="bp">⟩</span>
</pre></div>


<p>This fails:</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">a22</span> <span class="o">:</span> <span class="n">has_subset</span> <span class="o">(</span><span class="n">setoid</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">r₁</span> <span class="n">r₂</span><span class="o">,</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="o">{</span><span class="n">b</span> <span class="bp">|</span> <span class="n">r₁</span><span class="bp">.</span><span class="n">r</span> <span class="n">a</span> <span class="n">b</span><span class="o">}</span> <span class="err">⊆</span> <span class="o">{</span><span class="n">b</span> <span class="bp">|</span> <span class="n">r₂</span><span class="bp">.</span><span class="n">r</span> <span class="n">a</span> <span class="n">b</span><span class="o">}</span><span class="bp">⟩</span>
<span class="c">/-</span><span class="cm"> invalid field notation, function &#39;setoid.r&#39; does not have explicit argument with type (setoid ...) -/</span>
</pre></div>


<p>Anyone know why?</p>

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 05:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135336689):
<p>Usually the <code>simp</code> proves these equalities between structures, but not this time:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">setoid_eq_iff_r_eq</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">r₁</span> <span class="n">r₂</span> <span class="o">:</span> <span class="n">setoid</span> <span class="n">α</span><span class="o">},</span> <span class="n">r₁</span> <span class="bp">=</span> <span class="n">r₂</span> <span class="bp">↔</span> <span class="n">r₁</span><span class="bp">.</span><span class="n">r</span> <span class="bp">=</span> <span class="n">r₂</span><span class="bp">.</span><span class="n">r</span>
<span class="bp">|</span> <span class="bp">⟨</span><span class="n">r1</span><span class="o">,</span> <span class="n">e1</span><span class="bp">⟩</span> <span class="bp">⟨</span><span class="n">r2</span><span class="o">,</span> <span class="n">e2</span><span class="bp">⟩</span>
<span class="o">:=</span> <span class="k">begin</span>
  <span class="n">simp</span><span class="o">,</span>
  <span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>


<p>What's the right way to do this? I don't know how to project out what I want from the equality <code>r₁ = r₂</code> between setoid structures.</p>

#### [ Simon Hudon (Oct 07 2018 at 06:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135337108):
<p>You can use <code>cases</code> on <code>r1</code>, <code>r2</code>, split the equivalence and use <code>cases</code> on the equality assumption in both cases.</p>

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 06:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135337309):
<p>Thanks. Did you mean something like this?</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">eq_iff_r_eq</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">r₁</span> <span class="n">r₂</span> <span class="o">:</span> <span class="n">setoid</span> <span class="n">α</span><span class="o">},</span> <span class="n">r₁</span> <span class="bp">=</span> <span class="n">r₂</span> <span class="bp">↔</span> <span class="n">r₁</span><span class="bp">.</span><span class="n">r</span> <span class="bp">=</span> <span class="n">r₂</span><span class="bp">.</span><span class="n">r</span>
<span class="bp">|</span> <span class="bp">⟨</span><span class="n">r1</span><span class="o">,</span> <span class="n">e1</span><span class="bp">⟩</span> <span class="bp">⟨</span><span class="n">r2</span><span class="o">,</span> <span class="n">e2</span><span class="bp">⟩</span>
<span class="o">:=</span> <span class="k">begin</span>
  <span class="n">intros</span><span class="o">,</span>
  <span class="n">split</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">intro</span> <span class="n">h</span><span class="o">,</span>
    <span class="n">cases</span> <span class="n">h</span><span class="o">,</span> <span class="o">},</span>
  <span class="o">{</span>  <span class="o">}</span>
<span class="kn">end</span>
</pre></div>


<p>I'm getting a rather unhelpful error: <code>cases tactic failed, unexpected failure when introducing auxiliary equatilies</code>.</p>

#### [ Simon Hudon (Oct 07 2018 at 06:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135337320):
<p>That's odd. Try <code>injection h</code>, maybe that'll work</p>

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135337464):
<p>Yep, that worked. I don't know how to use <code>cases</code> in the second case though, since now the equality between structures is now in the goal.</p>

#### [ Simon Hudon (Oct 07 2018 at 06:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135337504):
<p>you can do <code>subst h</code></p>

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 06:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135337558):
<p><code>intro h, subst h</code> gives this error:</p>
<div class="codehilite"><pre><span></span><span class="n">subst</span> <span class="n">tactic</span> <span class="n">failed</span><span class="o">,</span> <span class="kn">hypothesis</span> <span class="err">&#39;</span><span class="n">h&#39;</span> <span class="n">is</span> <span class="n">not</span> <span class="n">of</span> <span class="n">the</span> <span class="n">form</span> <span class="o">(</span><span class="n">x</span> <span class="bp">=</span> <span class="n">t</span><span class="o">)</span> <span class="n">or</span> <span class="o">(</span><span class="n">t</span> <span class="bp">=</span> <span class="n">x</span><span class="o">)</span>
<span class="n">state</span><span class="o">:</span>
<span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">,</span>
<span class="n">eq_iff_r_eq</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">r₁</span> <span class="n">r₂</span> <span class="o">:</span> <span class="n">setoid</span> <span class="n">α</span><span class="o">},</span> <span class="n">r₁</span> <span class="bp">=</span> <span class="n">r₂</span> <span class="bp">↔</span> <span class="bp">@</span><span class="n">r</span> <span class="n">α</span> <span class="n">r₁</span> <span class="bp">=</span> <span class="bp">@</span><span class="n">r</span> <span class="n">α</span> <span class="n">r₂</span><span class="o">,</span>
<span class="n">r1</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">,</span>
<span class="n">e1</span> <span class="o">:</span> <span class="bp">@</span><span class="n">equivalence</span> <span class="n">α</span> <span class="n">r1</span><span class="o">,</span>
<span class="n">r2</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">,</span>
<span class="n">e2</span> <span class="o">:</span> <span class="bp">@</span><span class="n">equivalence</span> <span class="n">α</span> <span class="n">r2</span><span class="o">,</span>
<span class="n">h</span> <span class="o">:</span> <span class="bp">@</span><span class="n">r</span> <span class="n">α</span> <span class="o">(</span><span class="bp">@</span><span class="n">mk</span> <span class="n">α</span> <span class="n">r1</span> <span class="n">e1</span><span class="o">)</span> <span class="bp">=</span> <span class="bp">@</span><span class="n">r</span> <span class="n">α</span> <span class="o">(</span><span class="bp">@</span><span class="n">mk</span> <span class="n">α</span> <span class="n">r2</span> <span class="n">e2</span><span class="o">)</span>
<span class="err">⊢</span> <span class="bp">@</span><span class="n">mk</span> <span class="n">α</span> <span class="n">r1</span> <span class="n">e1</span> <span class="bp">=</span> <span class="bp">@</span><span class="n">mk</span> <span class="n">α</span> <span class="n">r2</span> <span class="n">e2</span>
</pre></div>

#### [ Simon Hudon (Oct 07 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135337605):
<p>What if you do <code>dsimp at h</code> first?</p>

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135337610):
<p>Ah, perfect! Thanks so much!</p>

#### [ Simon Hudon (Oct 07 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135337663):
<p><span class="emoji emoji-1f44d" title="+1">:+1:</span></p>

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135340678):
<p><a href="https://github.com/leanprover-community/mathlib/blob/tutorials/order/partitions.lean" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/tutorials/order/partitions.lean">Here's</a> the WIP complete lattice instance on setoids. I've completed the poset stuff and inf, top, bot but not much else, so a lot of the theorems are just broken skeletons from e.g. data.set.basic.</p>
<p>Is there a clean way of defining the sup / union / join operation? This boils down to something like two elements a z are equivalent in the transitive closure of r1 and r2 if there exists a finite chain of equivalences r1 a b, r2 b c, r1 c d, ... , r_ y z.</p>

#### [ Simon Hudon (Oct 07 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135340789):
<p>Aren't the relations in the setoid equivalences? They should be already transitive, symmetric and reflexive. sup and inf of <code>f : a -&gt; b -&gt; b -&gt; Prop</code> should be <code>λ x y, ∃ i, f i x y</code> and <code>λ x y, ∀ i, f i x y</code> respectively</p>

#### [ Mario Carneiro (Oct 07 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135340915):
<p>Note that <code>eqv_gen</code> will allow you to take the "span" of an arbitrary relation, so you can just union up a bunch of things and take the span for the supremum</p>

#### [ Simon Hudon (Oct 07 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135341333):
<p>What's the span of a relation?</p>

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135341672):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> I'm not sure I understand. I guess your <code>f</code> is a family of equivalence relations indexed by <code>a</code>? I think your inf agrees with <a href="https://github.com/leanprover-community/mathlib/blob/tutorials/order/partitions.lean#L87" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/tutorials/order/partitions.lean#L87">what I have</a>, but I don't think your sup is the correct one. Consider the following two equivalence relations r1 and r2 on the nats, the equivalence classes of r1 are {0,1}, {2,3}, {4,5}, ... and the equivalence classes of r2 are {0}, {1,2}, {3,4}, {5,6}, ....  The sup of r1 and r2 has only one equivalence class equal to nat, so in particular 0 is equivalent to 1000, but you need a very long chain of r1 and r2 relations to witness it.</p>

#### [ Mario Carneiro (Oct 07 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135341680):
<p><code>eqv_gen</code> is the equivalence closure of a relation, this is what Bryan wants</p>

#### [ Mario Carneiro (Oct 07 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135341740):
<p>Because equivalence relations are closed under arbitrary intersection, you can construct a generic "span" function that gets the smallest equivalence relation including some specified relation, and <code>eqv_gen</code> is this</p>

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135341836):
<p>Thanks Mario! <code>eqv_gen</code> looks promising. It will probably take me some time to figure out how to use it though.</p>

#### [ Mario Carneiro (Oct 07 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135341919):
<p>In your case I think you want to take the <code>eqv_gen</code> of Simon's relation <code>λ x y, ∃ i, f i x y</code></p>

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135342114):
<p>OK great, I think I'm starting to get it. I think I would have never found this definition on my own.</p>

#### [ Mario Carneiro (Oct 07 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135342177):
<p>Note that it's not required to use that definition, and indeed there is a more "abstract nonsense" definition that makes the proof obligations easier. Define the intersection of an arbitrary indexed family of equivalence relations using Simon's definition; it is straightforward to show this is an equivalence relation. From this, you can define every other element of the complete lattice structure, the inf, the sup, the Sup, the top and bot</p>

#### [ Simon Hudon (Oct 07 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135342226):
<p>Do you use "abstract nonsense" interchangeably with category theory?</p>

#### [ Mario Carneiro (Oct 07 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135342301):
<p>in this case it's lattice theory</p>

#### [ Mario Carneiro (Oct 07 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135342337):
<p>but I guess posets are categories, so sure</p>

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135342344):
<p>So I see that the intersection works, but how do I get the union from it? Would I have to define it using the finite chains of relations manually?</p>

#### [ Simon Hudon (Oct 07 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135342950):
<p>I haven't looked at that function too closely but I think you could take the union as I defined it and take its transitive, symmetric, reflexive closure</p>

#### [ Simon Hudon (Oct 07 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135342951):
<p>Does that make sense?</p>

#### [ Kevin Buzzard (Oct 07 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135342999):
<blockquote>
<p>Do you use "abstract nonsense" interchangeably with category theory?</p>
</blockquote>
<p>This is the most common usage of the phrase "abstract nonsense" when you see it in the mathematical literature, but the category theory in question can range from a simple diagram chase to the adjoint functor theorem and possibly beyond.</p>

#### [ Mario Carneiro (Oct 07 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135343827):
<p>You don't need to take any reflexive symmetric closures with the approach I suggested</p>

#### [ Mario Carneiro (Oct 07 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135343837):
<p>Given an intersection construction, you can define the supremum as the intersection of all equivalence classes containing the inputs</p>

#### [ Patrick Massot (Oct 07 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135343843):
<p>(deleted)</p>

#### [ Simon Hudon (Oct 07 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135343905):
<p>But what about the union?</p>

#### [ Mario Carneiro (Oct 07 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135343945):
<p>that is the union</p>

#### [ Mario Carneiro (Oct 07 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135343949):
<p>i.e. <code>a \sqcup b = Inf {s | a &lt;= s /\ b &lt;= s}</code></p>

#### [ Mario Carneiro (Oct 07 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135343955):
<p>similarly for arbitrary union</p>

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135343958):
<blockquote>
<p>Given an intersection construction, you can define the supremum as the intersection of all equivalence classes containing the inputs</p>
</blockquote>
<p>Typo here? Should the supremum be defined in terms of the union of [...]</p>

#### [ Mario Carneiro (Oct 07 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135343962):
<p>no</p>

#### [ Mario Carneiro (Oct 07 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135343971):
<p>Think of it as an approximation of the union "from above"</p>

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135344018):
<p>Ah, OK.</p>

#### [ Mario Carneiro (Oct 07 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135344019):
<p>the union is the LEAST upper bound, so you can just take the infimum of upper bounds</p>

#### [ Kenny Lau (Oct 07 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135344079):
<p>are there any <code>sorry</code> that I can fill?</p>

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135344146):
<p>Feel free to consider any broken proof in my files as a sorry. I'm not actively working on it at the moment.</p>

#### [ Kenny Lau (Oct 07 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135344231):
<p>do I need to compile for 1 hour to find out which proof is broken?</p>

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135344301):
<p>Ah, OK. Well <code>inter_subset_right</code>, <code>inter_subset_left</code>, <code>subset_inter</code> are broken but the statements should be right. You can just delete their proofs and fill them in. Let me see if there are others.</p>

#### [ Kenny Lau (Oct 07 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135344303):
<p>again, I need to compile for 1 hour to build this branch</p>

#### [ Kenny Lau (Oct 07 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135344306):
<p>so I don't really know what I can do</p>

#### [ Kenny Lau (Oct 07 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135344308):
<p>how do other people work on this branch?</p>

#### [ Kenny Lau (Oct 07 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135344350):
<p>how does <span class="user-mention" data-user-id="110026">@Simon Hudon</span> work on this branch?</p>

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135344402):
<p>I guess we've all got faster computers? It takes my computer about 10 minutes to compile mathlib.</p>

#### [ Kenny Lau (Oct 07 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135344423):
<p>do you have 24 threads?</p>

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135344477):
<p>The Activity monitor says lean is using 14 right now. I just started another build after switching branches. Let's see how long it takes.</p>

#### [ Kenny Lau (Oct 07 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135344480):
<p>can't you see how many threads you have?</p>

#### [ Kenny Lau (Oct 07 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135344635):
<p><a href="/user_uploads/3121/8KeKjpR28C3y92LYg_XEHFbR/2018-10-07.png" target="_blank" title="2018-10-07.png">2018-10-07.png</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/8KeKjpR28C3y92LYg_XEHFbR/2018-10-07.png" target="_blank" title="2018-10-07.png"><img src="/user_uploads/3121/8KeKjpR28C3y92LYg_XEHFbR/2018-10-07.png"></a></div>

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135344636):
<p>Do you mean threads across all processes? It's something like 1800 threads and 360 processes. I'm on a 6 core macbook pro.</p>

#### [ Kenny Lau (Oct 07 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135344642):
<p>I have 2 cores and 4 threads</p>

#### [ Kenny Lau (Oct 07 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135344643):
<p>I'm on a windows surface</p>

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135344780):
<p>That's really amazing. I'm sure the surface has its advantages. </p>
<p>Oh yeah, you can now bind a key to toggle the infoview live updating in the VS code extension, in case you want to pause the tactic state while lean is busy. It's <code>lean.infoview.toggleUpdating</code> in the keyboard shortcuts.</p>

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135344793):
<p>This branch seems to be all kinds of screwed up. There's something wrong in <code>data.finset</code> that I have to look at.</p>

#### [ Kenny Lau (Oct 07 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135344845):
<blockquote>
<p>That's really amazing. I'm sure the surface has its advantages. </p>
</blockquote>
<p>I guess it isn't designed to build lean</p>

#### [ Mario Carneiro (Oct 07 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135345229):
<p>Yes, an ultrabook is not intended for heavy workstation programming</p>

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135345608):
<p>tutorial should now build properly. <code>order.partitions</code> is also filled out with sorries, so it should be more clear what's missing.</p>

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135359879):
<p><a href="https://github.com/leanprover-community/mathlib/blob/tutorials/order/partitions.lean#L68" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/tutorials/order/partitions.lean#L68">Here's my definition for union using <code>eqv_gen</code></a> (is this right?).  Now this is what I need to show <code>union_subset</code> (forgive any typos introduced by my manual prettifying...):</p>
<div class="codehilite"><pre><span></span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">,</span>
<span class="n">r₁</span> <span class="n">r₂</span> <span class="n">r₃</span> <span class="o">:</span> <span class="n">setoid</span> <span class="n">α</span><span class="o">,</span>
<span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span>
<span class="n">r1</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span> <span class="o">:=</span>
  <span class="bp">@</span><span class="n">eqv_gen</span> <span class="n">α</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">s₁</span> <span class="n">s₂</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="bp">@</span><span class="n">r</span> <span class="n">α</span> <span class="n">r₁</span> <span class="n">s₁</span> <span class="n">s₂</span> <span class="bp">∨</span> <span class="bp">@</span><span class="n">r</span> <span class="n">α</span> <span class="n">r₂</span> <span class="n">s₁</span> <span class="n">s₂</span><span class="o">),</span>
<span class="n">r2</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">r</span> <span class="n">α</span> <span class="n">r₃</span><span class="o">,</span>
<span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span>
<span class="n">a_1</span> <span class="o">:</span> <span class="n">r1</span> <span class="n">a</span> <span class="n">x</span><span class="o">,</span>
<span class="n">h23</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="bp">@</span><span class="n">r</span> <span class="n">α</span> <span class="n">r₂</span> <span class="n">a</span> <span class="n">y</span> <span class="bp">→</span> <span class="n">r2</span> <span class="n">a</span> <span class="n">y</span><span class="o">,</span>
<span class="n">h13</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="bp">@</span><span class="n">r</span> <span class="n">α</span> <span class="n">r₁</span> <span class="n">a</span> <span class="n">y</span> <span class="bp">→</span> <span class="n">r2</span> <span class="n">a</span> <span class="n">y</span>
<span class="err">⊢</span> <span class="n">r2</span> <span class="n">a</span> <span class="n">x</span>
</pre></div>


<p>Here's a very informal argument: <code>a_1</code> tells us that there's some finite chain of r₁  and r₂ equivalences between a and x, and and we then repeatedly apply h13 and h23 to each of the links of that chain to win. How do I do this?</p>

#### [ Kevin Buzzard (Oct 07 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135365476):
<p>I have only half-been paying attention to this thread (and indeed Zulip) but I have a little time before bed. You're trying to prove that if r,s,t are three equivalence relations on a set, and both s and t are subsets of r, then the equivalence relation generated by s and t is a subset of r, right? Do you have that if x is a random relation contained in an equivalence relation r then the equivalence relation generated by x is also contained in r? It's trivial from this, right?</p>

#### [ Kevin Buzzard (Oct 07 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135365488):
<p>I'm asking if we have the universal property of "equivalence relation generated by".</p>

#### [ Kenny Lau (Oct 07 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135365545):
<p>you mean <code>rec_on</code></p>

#### [ Kevin Buzzard (Oct 07 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135365546):
<p>This would be trivial if you knew that the equivalence relation generated by an arbitrary relation was equal to the intersection of all the equivalence relations containing this relation. Sorry I'm late to the party; there's a lot of other noise in this thread too.</p>

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135365653):
<p>I think I can do what I want with <a href="https://github.com/leanprover/mathlib/blob/57194fa57e76721a517d6969ee88a6007f0722b3/logic/relation.lean#L367" target="_blank" title="https://github.com/leanprover/mathlib/blob/57194fa57e76721a517d6969ee88a6007f0722b3/logic/relation.lean#L367"><code>relation.eqv_gen_mono</code></a>. That might be the same thing that you're saying.</p>

#### [ Kevin Buzzard (Oct 07 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135365655):
<p>Kenny you're right</p>

#### [ Kevin Buzzard (Oct 07 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135365667):
<p>Is the question "how do I fill in the sorry here: <a href="https://github.com/leanprover-community/mathlib/blob/1030f5324363a9213cf4b68f834fad0d124b8a13/order/partitions.lean#L110" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/1030f5324363a9213cf4b68f834fad0d124b8a13/order/partitions.lean#L110">https://github.com/leanprover-community/mathlib/blob/1030f5324363a9213cf4b68f834fad0d124b8a13/order/partitions.lean#L110</a> "?</p>

#### [ Kevin Buzzard (Oct 07 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135365716):
<p>If so, I am suggesting that you first prove that for an arbitrary relation x and an equiv reln r, x is a subset of r iff the equiv reln generated by x is a subset of r</p>

#### [ Kevin Buzzard (Oct 07 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135365717):
<p>and then the union thing is a triviality</p>

#### [ Kevin Buzzard (Oct 07 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135365728):
<p>and Kenny is suggesting that that the universal property of the relation is just the recursor</p>

#### [ Kevin Buzzard (Oct 07 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135365730):
<p>so this should be hopefully straightforward.</p>

#### [ Kevin Buzzard (Oct 07 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135365733):
<p>Do you want me to try or am I answering the wrong question <span class="user-mention" data-user-id="123965">@Bryan Gin-ge Chen</span> ?</p>

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135365828):
<p>Yes, that was the question. I think I've solved it just now though:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">union_subset</span> <span class="o">{</span><span class="n">r₁</span> <span class="n">r₂</span> <span class="n">r₃</span> <span class="o">:</span> <span class="n">setoid</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">h13</span> <span class="o">:</span> <span class="n">r₁</span> <span class="err">⊆</span> <span class="n">r₃</span><span class="o">)</span> <span class="o">(</span><span class="n">h23</span> <span class="o">:</span> <span class="n">r₂</span> <span class="err">⊆</span> <span class="n">r₃</span><span class="o">)</span> <span class="o">:</span> <span class="n">r₁</span> <span class="err">∪</span> <span class="n">r₂</span> <span class="err">⊆</span> <span class="n">r₃</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">subset_def</span><span class="o">]</span> <span class="n">at</span> <span class="n">h13</span> <span class="n">h23</span> <span class="err">⊢</span><span class="o">,</span>
  <span class="n">simp</span> <span class="n">only</span> <span class="o">[</span><span class="n">set</span><span class="bp">.</span><span class="n">subset_def</span><span class="o">,</span> <span class="n">set</span><span class="bp">.</span><span class="n">mem_set_of_eq</span><span class="o">]</span> <span class="n">at</span> <span class="n">h13</span> <span class="n">h23</span> <span class="err">⊢</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">union_def</span><span class="o">,</span> <span class="n">rel_union</span><span class="o">],</span>
  <span class="n">intros</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">hor</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="n">x</span><span class="o">,</span> <span class="bp">@</span><span class="n">r</span> <span class="n">α</span> <span class="n">r₁</span> <span class="n">a</span> <span class="n">x</span> <span class="bp">∨</span> <span class="bp">@</span><span class="n">r</span> <span class="n">α</span> <span class="n">r₂</span> <span class="n">a</span> <span class="n">x</span> <span class="bp">→</span> <span class="bp">@</span><span class="n">r</span> <span class="n">α</span> <span class="n">r₃</span> <span class="n">a</span> <span class="n">x</span> <span class="o">:=</span> <span class="k">by</span> <span class="o">{</span> <span class="n">intros</span> <span class="n">a</span> <span class="n">x</span> <span class="n">h</span><span class="o">,</span>
    <span class="n">exact</span> <span class="n">or</span><span class="bp">.</span><span class="n">elim</span> <span class="n">h</span> <span class="o">(</span><span class="n">h13</span> <span class="n">a</span> <span class="n">x</span><span class="o">)</span> <span class="o">(</span><span class="n">h23</span> <span class="n">a</span> <span class="n">x</span><span class="o">)</span> <span class="o">},</span>
  <span class="k">have</span> <span class="n">H</span> <span class="o">:=</span> <span class="n">relation</span><span class="bp">.</span><span class="n">eqv_gen_mono</span> <span class="n">hor</span> <span class="n">a_1</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">h</span> <span class="o">:=</span> <span class="o">(</span><span class="bp">@</span><span class="n">relation</span><span class="bp">.</span><span class="n">eqv_gen_iff_of_equivalence</span> <span class="bp">_</span> <span class="n">r₃</span><span class="bp">.</span><span class="n">r</span> <span class="n">a</span> <span class="n">x</span> <span class="n">r₃</span><span class="bp">.</span><span class="mi">2</span><span class="o">)</span><span class="bp">.</span><span class="n">mp</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">h</span> <span class="n">H</span>
<span class="kn">end</span>
</pre></div>

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135365891):
<p>I think <code>relation.eqv_gen_mono</code> is this property you are describing. And it does appear to me to be proved in the way you guys are suggesting. Thanks for the explanation though, without it, I was probably just going to go on not really understanding what was happening under the hood here!</p>

#### [ Kevin Buzzard (Oct 07 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366475):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> why did this come out so horrible:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">sub_of_gen_sub</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">setoid</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="n">x</span> <span class="n">a</span> <span class="n">b</span> <span class="bp">→</span> <span class="bp">@</span><span class="n">setoid</span><span class="bp">.</span><span class="n">r</span> <span class="bp">_</span> <span class="n">s</span> <span class="n">a</span> <span class="n">b</span><span class="o">)</span> <span class="o">:</span>
<span class="bp">∀</span> <span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="o">(</span><span class="n">eqv_gen</span> <span class="n">x</span><span class="o">)</span> <span class="n">a</span> <span class="n">b</span> <span class="bp">→</span> <span class="bp">@</span><span class="n">setoid</span><span class="bp">.</span><span class="n">r</span> <span class="bp">_</span> <span class="n">s</span> <span class="n">a</span> <span class="n">b</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span> <span class="n">H2</span><span class="o">,</span> <span class="n">eqv_gen</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">H2</span> <span class="n">H</span>
  <span class="o">(</span><span class="bp">@</span><span class="n">setoid</span><span class="bp">.</span><span class="n">iseqv</span> <span class="n">α</span> <span class="n">s</span><span class="o">)</span><span class="bp">.</span><span class="mi">1</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span> <span class="bp">_</span> <span class="n">H3</span><span class="o">,</span> <span class="o">(</span><span class="bp">@</span><span class="n">setoid</span><span class="bp">.</span><span class="n">iseqv</span> <span class="n">α</span> <span class="n">s</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span><span class="bp">.</span><span class="mi">1</span> <span class="n">H3</span><span class="o">)</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span> <span class="n">z</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">H4</span> <span class="n">H5</span><span class="o">,(</span><span class="bp">@</span><span class="n">setoid</span><span class="bp">.</span><span class="n">iseqv</span> <span class="n">α</span> <span class="n">s</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span><span class="bp">.</span><span class="mi">2</span> <span class="n">H4</span> <span class="n">H5</span><span class="o">)</span>
</pre></div>

#### [ Kevin Buzzard (Oct 07 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366478):
<p>Oh it's because I should be using a typeclass</p>

#### [ Kenny Lau (Oct 07 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366479):
<p>what do you mean by terrible?</p>

#### [ Kenny Lau (Oct 07 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366480):
<p>oh</p>

#### [ Kevin Buzzard (Oct 07 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366518):
<p>I didn't use typeclasses because I could see I'd have two equiv relns on alpha</p>

#### [ Kenny Lau (Oct 07 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366530):
<p>well it's a lemma</p>

#### [ Kenny Lau (Oct 07 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366531):
<p>the typeclass is local</p>

#### [ Kenny Lau (Oct 07 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366578):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">sub_of_gen_sub</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">[</span><span class="n">setoid</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="n">x</span> <span class="n">a</span> <span class="n">b</span> <span class="bp">→</span> <span class="n">a</span> <span class="bp">≈</span> <span class="n">b</span><span class="o">)</span> <span class="o">:</span>
<span class="bp">∀</span> <span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="o">(</span><span class="n">eqv_gen</span> <span class="n">x</span><span class="o">)</span> <span class="n">a</span> <span class="n">b</span> <span class="bp">→</span> <span class="n">a</span> <span class="bp">≈</span> <span class="n">b</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span> <span class="n">H2</span><span class="o">,</span> <span class="n">eqv_gen</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">H2</span> <span class="n">H</span>
  <span class="n">setoid</span><span class="bp">.</span><span class="n">refl</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">setoid</span><span class="bp">.</span><span class="n">symm</span><span class="o">)</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">setoid</span><span class="bp">.</span><span class="n">trans</span><span class="o">)</span>
</pre></div>

#### [ Kevin Buzzard (Oct 07 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366588):
<p><span class="user-mention" data-user-id="123965">@Bryan Gin-ge Chen</span> it's not mono, this is a slightly longer way around isn't it? Mono says if x sub y then the equiv reln gen by x is a subset of the equiv reln generated by y. To get the universal property from that you also need that the equiv reln generated by an equiv reln is itself, which is another lemma</p>

#### [ Kenny Lau (Oct 07 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366590):
<p>inb4 <em>galois insertion</em></p>

#### [ Kevin Buzzard (Oct 07 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366594):
<p>rofl</p>

#### [ Kevin Buzzard (Oct 07 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366599):
<p>I can quite believe it.</p>

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366600):
<p>Right, you can see I had to use <code>relation.eqv_gen_iff_of_equivalence</code>.</p>

#### [ Kevin Buzzard (Oct 07 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366601):
<p>although it might be a coinsertion</p>

#### [ Kevin Buzzard (Oct 07 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366602):
<p>With <code>sub_of_gen_sub</code> (which is a relatively straightforward consequence of the recursor) the proof is simpler.</p>

#### [ Kevin Buzzard (Oct 07 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366644):
<p>The lemma reduces you to checking that if X and Y are subsets of Z then so is X union Y, which will be in the library</p>

#### [ Kenny Lau (Oct 07 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366692):
<p>I don't really understand</p>

#### [ Kevin Buzzard (Oct 07 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366694):
<p>It wouldn't surprise me if <code>sub_of_gen_sub</code> is already in the library, perhaps under a better name.</p>

#### [ Kenny Lau (Oct 07 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366695):
<p>this is just the preimage of the canonical embedding from the set of equivalence relations on A to P(A x A)</p>

#### [ Kevin Buzzard (Oct 07 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366698):
<p>yes</p>

#### [ Kevin Buzzard (Oct 07 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366704):
<p>Bryan is using subset notation in exactly this way</p>

#### [ Kenny Lau (Oct 07 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366705):
<p>but he's not proving things this way</p>

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366706):
<p>I did a search for <code>eqv_gen</code> in mathlib and it only showed up in <code>logic.relation</code> and Kenny's free group file.</p>

#### [ Kevin Buzzard (Oct 07 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366750):
<p>Kenny I'm sure both Bryan and I would be interested if you were to blow his code out of the water using a more high-powered way of thinking about this question.</p>

#### [ Kenny Lau (Oct 07 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366765):
<p>blow his code out of the water?</p>

#### [ Kevin Buzzard (Oct 07 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366766):
<p>Bryan, do you know what a Galois insertion is?</p>

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366782):
<p>I'm about to have dinner, so I'll push what I have. Feel free to make arbitrary changes if you're willing to deal with the compile times.</p>
<p>I was just about to ask whether I ought to know about Galois (co)insertions...</p>

#### [ Kevin Buzzard (Oct 07 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366814):
<p>So the idea is that the construction sending a random relation to an equivalence relation is an adjoint to the forgetful functor sending an equivalence relation to the underlying relation</p>

#### [ Kenny Lau (Oct 07 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366817):
<blockquote>
<p>Kenny I'm sure both Bryan and I would be interested if you were to blow his code out of the water using a more high-powered way of thinking about this question.</p>
</blockquote>
<p>I still don't know what the question is</p>

#### [ Kevin Buzzard (Oct 07 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366820):
<p><a href="https://github.com/leanprover-community/mathlib/blob/1030f5324363a9213cf4b68f834fad0d124b8a13/order/partitions.lean" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/1030f5324363a9213cf4b68f834fad0d124b8a13/order/partitions.lean">https://github.com/leanprover-community/mathlib/blob/1030f5324363a9213cf4b68f834fad0d124b8a13/order/partitions.lean</a></p>

#### [ Kevin Buzzard (Oct 07 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366822):
<p>Prove all the lemmas there but in a much better way</p>

#### [ Kevin Buzzard (Oct 07 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366825):
<p>That's the question</p>

#### [ Kevin Buzzard (Oct 07 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366826):
<p>I think</p>

#### [ Kevin Buzzard (Oct 07 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366884):
<p>But the point is that you have something else here too -- these aren't just a pair of adjoint functors, because these are on posets (ordered by inclusion) and not just categories.</p>

#### [ Kenny Lau (Oct 07 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366890):
<p>well give me an hour to compile the mathlib first...</p>

#### [ Kenny Lau (Oct 07 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366891):
<p>I've changed some of the files</p>

#### [ Kevin Buzzard (Oct 07 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366893):
<p>So there's a special name for this situation, called a Galois insertion.</p>

#### [ Kenny Lau (Oct 07 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366901):
<p>so every time I change some files I need to spend one hour compiling the files</p>

#### [ Kevin Buzzard (Oct 07 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366903):
<p>And there's a bunch of lemmas proved about Galois insertions which might make these sorts of arguments easier.</p>

#### [ Kenny Lau (Oct 07 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366910):
<p>and in this hour my CPU will be fully used</p>

#### [ Kenny Lau (Oct 07 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366914):
<p>and the computer will be mostly unusable</p>

#### [ Kevin Buzzard (Oct 07 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366917):
<p>Kenny if you are only working on one branch which isn't master</p>

#### [ Kevin Buzzard (Oct 07 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366920):
<p>then you should just commit the olean files to master :P</p>

#### [ Kevin Buzzard (Oct 07 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366924):
<p>then whenever you checkout master again, the olean files will reappear</p>

#### [ Patrick Massot (Oct 07 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366967):
<p>Kenny and Kevin, you should pay attention to what Simon is writing in the nextdoor thread</p>

#### [ Kevin Buzzard (Oct 07 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366974):
<p>Kenny should -- I can compile mathlib in 10 minutes and I never fiddle with it anyway ;-)</p>

#### [ Kevin Buzzard (Oct 07 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135366981):
<p>well...hardly ever</p>

#### [ Kenny Lau (Oct 07 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135367165):
<p>do all of you have like 30 cores?</p>

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135368008):
<blockquote>
<p>And there's a bunch of lemmas proved about Galois insertions which might make these sorts of arguments easier.</p>
</blockquote>
<p>Are these lemmas in mathlib? There doesn't seem to be anything named <code>galois*</code>.</p>

#### [ Kenny Lau (Oct 08 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135368009):
<p><code>galois.*</code>?</p>

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135368011):
<p>Oh oops, I was trying to search  the community fork.</p>

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135368163):
<p>I remember reading about Galois connections whenever I learned about covering spaces. I don't remember insertions and coinsertions but the lean file seems clear enough.</p>

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369030):
<p>OK, I see the point now! The smart way to do all of this is to just use <code>lift_complete_lattice</code> on the complete lattice instance on subsets. Presumably that's what Kenny is up to now that an hour has passed. :)</p>

#### [ Kenny Lau (Oct 08 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369082):
<p>oh well I proved this</p>

#### [ Kenny Lau (Oct 08 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369083):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">order</span><span class="bp">.</span><span class="n">complete_lattice</span> <span class="n">data</span><span class="bp">.</span><span class="n">fintype</span>

<span class="kn">open</span> <span class="n">lattice</span>

<span class="kn">instance</span> <span class="n">bounded_lattice</span><span class="bp">.</span><span class="n">of_fintype_inhabited_lattice</span>
  <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">inhabited</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">lattice</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span>
  <span class="n">bounded_lattice</span> <span class="n">α</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">top</span> <span class="o">:=</span> <span class="n">finset</span><span class="bp">.</span><span class="n">fold</span> <span class="o">(</span><span class="err">⊔</span><span class="o">)</span> <span class="o">(</span><span class="n">default</span> <span class="n">α</span><span class="o">)</span> <span class="n">id</span> <span class="n">finset</span><span class="bp">.</span><span class="n">univ</span><span class="o">,</span>
  <span class="n">le_top</span> <span class="o">:=</span> <span class="k">begin</span>
    <span class="n">suffices</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">finset</span><span class="bp">.</span><span class="n">univ</span><span class="o">,</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">finset</span><span class="bp">.</span><span class="n">fold</span> <span class="o">(</span><span class="err">⊔</span><span class="o">)</span> <span class="o">(</span><span class="n">default</span> <span class="n">α</span><span class="o">)</span> <span class="n">id</span> <span class="n">finset</span><span class="bp">.</span><span class="n">univ</span><span class="o">,</span>
      <span class="k">from</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">this</span> <span class="n">x</span> <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">mem_univ</span> <span class="n">x</span><span class="o">),</span>
    <span class="n">generalize</span> <span class="o">:</span> <span class="n">finset</span><span class="bp">.</span><span class="n">univ</span> <span class="bp">=</span> <span class="n">U</span><span class="o">,</span>
    <span class="n">cases</span> <span class="n">U</span> <span class="k">with</span> <span class="n">U</span> <span class="n">hu1</span><span class="o">,</span>
    <span class="n">induction</span> <span class="n">U</span> <span class="kn">using</span> <span class="n">quot</span><span class="bp">.</span><span class="n">ind</span> <span class="k">with</span> <span class="n">L</span><span class="o">,</span>
    <span class="n">induction</span> <span class="n">L</span> <span class="k">with</span> <span class="n">hd</span> <span class="n">tl</span> <span class="n">ih</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">exact</span> <span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">false</span><span class="bp">.</span><span class="n">elim</span> <span class="o">},</span>
    <span class="n">intros</span> <span class="n">x</span> <span class="n">hx</span><span class="o">,</span>
    <span class="n">rcases</span> <span class="n">hx</span> <span class="k">with</span> <span class="n">rfl</span> <span class="bp">|</span> <span class="n">hx</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">exact</span> <span class="n">le_sup_left</span> <span class="o">},</span>
    <span class="n">transitivity</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">exact</span> <span class="n">ih</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">nodup_of_nodup_cons</span> <span class="n">hu1</span><span class="o">)</span> <span class="n">x</span> <span class="n">hx</span> <span class="o">},</span>
    <span class="o">{</span> <span class="n">exact</span> <span class="n">le_sup_right</span> <span class="o">}</span>
  <span class="kn">end</span><span class="o">,</span>
  <span class="n">bot</span> <span class="o">:=</span> <span class="n">finset</span><span class="bp">.</span><span class="n">fold</span> <span class="o">(</span><span class="err">⊓</span><span class="o">)</span> <span class="o">(</span><span class="n">default</span> <span class="n">α</span><span class="o">)</span> <span class="n">id</span> <span class="n">finset</span><span class="bp">.</span><span class="n">univ</span><span class="o">,</span>
  <span class="n">bot_le</span> <span class="o">:=</span> <span class="k">begin</span>
    <span class="n">suffices</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">finset</span><span class="bp">.</span><span class="n">univ</span><span class="o">,</span> <span class="n">finset</span><span class="bp">.</span><span class="n">fold</span> <span class="o">(</span><span class="err">⊓</span><span class="o">)</span> <span class="o">(</span><span class="n">default</span> <span class="n">α</span><span class="o">)</span> <span class="n">id</span> <span class="n">finset</span><span class="bp">.</span><span class="n">univ</span> <span class="bp">≤</span> <span class="n">a</span><span class="o">,</span>
      <span class="k">from</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">this</span> <span class="n">x</span> <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">mem_univ</span> <span class="n">x</span><span class="o">),</span>
    <span class="n">generalize</span> <span class="o">:</span> <span class="n">finset</span><span class="bp">.</span><span class="n">univ</span> <span class="bp">=</span> <span class="n">U</span><span class="o">,</span>
    <span class="n">cases</span> <span class="n">U</span> <span class="k">with</span> <span class="n">U</span> <span class="n">hu1</span><span class="o">,</span>
    <span class="n">induction</span> <span class="n">U</span> <span class="kn">using</span> <span class="n">quot</span><span class="bp">.</span><span class="n">ind</span> <span class="k">with</span> <span class="n">L</span><span class="o">,</span>
    <span class="n">induction</span> <span class="n">L</span> <span class="k">with</span> <span class="n">hd</span> <span class="n">tl</span> <span class="n">ih</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">exact</span> <span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">false</span><span class="bp">.</span><span class="n">elim</span> <span class="o">},</span>
    <span class="n">intros</span> <span class="n">x</span> <span class="n">hx</span><span class="o">,</span>
    <span class="n">rcases</span> <span class="n">hx</span> <span class="k">with</span> <span class="n">rfl</span> <span class="bp">|</span> <span class="n">hx</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">exact</span> <span class="n">inf_le_left</span> <span class="o">},</span>
    <span class="n">transitivity</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">exact</span> <span class="n">inf_le_right</span> <span class="o">},</span>
    <span class="o">{</span> <span class="n">exact</span> <span class="n">ih</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">nodup_of_nodup_cons</span> <span class="n">hu1</span><span class="o">)</span> <span class="n">x</span> <span class="n">hx</span> <span class="o">}</span>
  <span class="kn">end</span><span class="o">,</span>
  <span class="bp">..</span> <span class="o">(</span><span class="n">infer_instance</span> <span class="o">:</span> <span class="n">lattice</span> <span class="n">α</span><span class="o">)</span> <span class="o">}</span>
</pre></div>

#### [ Kenny Lau (Oct 08 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369135):
<p>and realized that proving it is a complete lattice is impossible</p>

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369151):
<p>Oh are you working on <code>tutorial/partitions.lean</code> or <code>order/partitions.lean</code>?</p>

#### [ Kenny Lau (Oct 08 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369193):
<p>what is the difference?</p>

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369199):
<p><code>tutorial/partitions.lean</code> was my first try on finite sets. Mario told me I should do stuff with general sets and then specialize, so I made <code>order/partitions.lean</code>.</p>

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369238):
<p>Is the issue with finite partitions that <code>Sup</code> and <code>Inf</code> need to use <code>set</code>?</p>

#### [ Kenny Lau (Oct 08 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369296):
<p>I think we should have an instance of <code>\Pi [fintype \a], bounded_lattice (finset \a)</code></p>

#### [ Kenny Lau (Oct 08 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369504):
<blockquote>
<p>Is the issue with finite partitions that <code>Sup</code> and <code>Inf</code> need to use <code>set</code>?</p>
</blockquote>
<p>yes</p>

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 01:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369556):
<p>That's unfortunate. There should be a version of <code>complete_lattice</code> that works for finsets. Is that what your instance above does?</p>

#### [ Kenny Lau (Oct 08 2018 at 01:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369571):
<p>no, that's <code>bounded_lattice</code></p>

#### [ Kenny Lau (Oct 08 2018 at 01:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369573):
<p>I don't think you can prove <code>complete_lattice</code>.</p>

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369687):
<p>Partitions of finite sets have a complete lattice structure just as much as partitions of arbitrary sets do, so we should add <code>complete_lattice_finset</code>.</p>

#### [ Kenny Lau (Oct 08 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369731):
<p>I don't think so.</p>

#### [ Jeremy Avigad (Oct 08 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369738):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I am sorry to be slow to respond to your ping, but I have thought about it and I don't have any great insights here. I don't think the notion of a canonical isomorphism is a sharp concept, and your post gives as good a working definition as any. It would be nice to have automation the finds/constructs them for you.</p>

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369842):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> Why not?</p>

#### [ Kenny Lau (Oct 08 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369846):
<p>because given an arbitrary set of partitions I don't see how you can find its supremum.</p>

#### [ Kenny Lau (Oct 08 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369850):
<p>let's just say our set is A = {0,1}</p>

#### [ Kenny Lau (Oct 08 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369856):
<p>I give you a set S of partitions of A</p>

#### [ Kenny Lau (Oct 08 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369857):
<p>how do you find the supremum of S?</p>

#### [ Kenny Lau (Oct 08 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369902):
<p>let's say S is {{{0},{1}}} if Goldbach conjecture is true and and {} otherwise.</p>

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369979):
<p>OK, but for finite partitions I only care about finsets of partitions which can't be that gross, right?</p>

#### [ Kenny Lau (Oct 08 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135369992):
<p>but if you want to have a <code>complete_lattice</code> instance then you need to find the supremum for arbitrary sets</p>

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135370045):
<p>So you're saying that there's not even <code>complete_lattice</code> on <code>setoid</code>, as I was aiming to prove in <code>order/partitions.lean</code>...</p>

#### [ Kenny Lau (Oct 08 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135370047):
<p>you can always make a <code>noncomputable def</code> :)</p>

#### [ Kenny Lau (Oct 08 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135370048):
<p>(don't make it an instance!)</p>

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135370296):
<p>I think I'm starting to get it. Do you happen to know which part of the galois insertion between the partial order on equivalence relations and that on subsets of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>α</mi><mo>×</mo><mi>α</mi></mrow><annotation encoding="application/x-tex">\alpha \times \alpha</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.58333em;"></span><span class="strut bottom" style="height:0.66666em;vertical-align:-0.08333em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.0037em;">α</span><span class="mbin">×</span><span class="mord mathit" style="margin-right:0.0037em;">α</span></span></span></span> is noncomputable?</p>

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135370318):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> What do you think about having a <code>complete_lattice_finset</code>?</p>

#### [ Kenny Lau (Oct 08 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135370319):
<p>none of the parts</p>

#### [ Mario Carneiro (Oct 08 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135371718):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> <code>Sup</code> and <code>Inf</code> are inherently noncomputable, just from their types: <code>set A -&gt; A</code></p>

#### [ Mario Carneiro (Oct 08 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135371721):
<p>This means that they take in no data and produce data</p>

#### [ Kenny Lau (Oct 08 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135371723):
<p>well <code>set (set A) -&gt; set A</code> is computable though</p>

#### [ Mario Carneiro (Oct 08 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135371731):
<p>pointlessly so</p>

#### [ Mario Carneiro (Oct 08 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135371734):
<p>you can computabilize any definition of that type</p>

#### [ Kenny Lau (Oct 08 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135371738):
<p>aha</p>

#### [ Kenny Lau (Oct 08 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135371739):
<p>thanks</p>

#### [ Johan Commelin (Oct 09 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135448580):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> Do you know if Neil got Lean working in the end?</p>

#### [ Johan Commelin (Oct 09 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135448584):
<p><span class="user-mention" data-user-id="130308">@Neil Strickland</span> Aah, you're on this Zulip. Can you confirm?</p>

#### [ Johan Commelin (Oct 09 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135448697):
<p>I'm looking at the first "challenge", namely: prove <code>2 + 2 = 4</code>. Your goal with this challenge is</p>
<blockquote>
<p>Key points: basic boilerplate at the top of the file, basic grammar of stating and proving, how to interact with the proof assistant.</p>
</blockquote>
<p>But in Lean you won't learn that from <code>2 + 2 = 4</code>. In idiomatic Lean, a file dedicated to that lemma would contain 1 line:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">two_add_two</span> <span class="o">:</span> <span class="mi">2</span> <span class="bp">+</span> <span class="mi">2</span> <span class="bp">=</span> <span class="mi">4</span> <span class="o">:=</span> <span class="n">rfl</span>
</pre></div>


<p>No imports, no boiler plate, no interactions, no nothing.</p>

#### [ Scott Morrison (Oct 09 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135448700):
<p>I'm not really sure what state we left him in. At Dagstuhl he definitely had a working copy on the laptop he had with him, but that might not still be the case.</p>

#### [ Johan Commelin (Oct 09 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135448712):
<p>I think the "Key points" deserve to be in a dedicated tutorial file. But I'm not sure if <code>2 + 2 = 4</code> is the right "goal" of that file.</p>

#### [ Scott Morrison (Oct 09 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135448758):
<p>Well -- even that file teaches you a few things: the lemma keyword, colon, colon-equals. You could also explain the red and green underlines, and the fact that the absence of these shows Lean approves. (Or ... is just not even running...)</p>

#### [ Tobias Grosser (Oct 09 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135450223):
<p>(deleted)</p>

#### [ Tobias Grosser (Oct 09 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135450243):
<blockquote>
<p>do all of you have like 30 cores?</p>
</blockquote>
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> , any reason you don't compile on a proper server?</p>

#### [ Tobias Grosser (Oct 09 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135450297):
<p>If you don't have one available, I suggest you get an account at the GCC compile farm: "<a href="https://cfarm.tetaneutral.net" target="_blank" title="https://cfarm.tetaneutral.net">https://cfarm.tetaneutral.net</a>"</p>

#### [ Tobias Grosser (Oct 09 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135450314):
<p>They give accounts to open source contributors and have some servers that are commonly not too busy</p>

#### [ Tobias Grosser (Oct 09 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135450320):
<p>gcc20   22, 443 Dual Xeon   x86_64  Intel(R) Xeon(R) CPU X5670 @ 2.93GHz    2 CPU<br>
12 cores 24 threads 24105 MB    825.0 GB    Debian 7.11 wheezy<br>
3.2.0-4-amd64   1090 days   INRIA Rocquencourt  France</p>

#### [ Tobias Grosser (Oct 09 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135450325):
<p>Is mostly idle today.</p>

#### [ Tobias Grosser (Oct 09 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135450381):
<p>If you can get lean compiled on powerpc hardware you can run on IBM Power8 with 160 CPUs</p>

#### [ Tobias Grosser (Oct 09 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135450385):
<p>It's also at 99% idle ATM.</p>

#### [ Mario Carneiro (Oct 09 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135450516):
<p>I've never heard of this option</p>

#### [ Mario Carneiro (Oct 09 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135450564):
<p>Maybe there is a possibility we can set up Jenkins on it as an alternative to Travis?</p>

#### [ Johan Commelin (Oct 09 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135450973):
<p>Here is what I just pushed for Challenge 1.<br>
<a href="https://github.com/leanprover-community/mathlib/blob/tutorials/tutorials/two_add_two.lean" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/tutorials/tutorials/two_add_two.lean">https://github.com/leanprover-community/mathlib/blob/tutorials/tutorials/two_add_two.lean</a></p>

#### [ Johan Commelin (Oct 09 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135451044):
<p>I didn't do any tactics yet. So that should be done in Challenge 2 "Infinitude of primes".</p>

#### [ Johan Commelin (Oct 09 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135451447):
<p><span class="user-mention" data-user-id="130308">@Neil Strickland</span> Would you mind adding a link to <a href="https://github.com/leanprover-community/mathlib/tree/tutorials/tutorials" target="_blank" title="https://github.com/leanprover-community/mathlib/tree/tutorials/tutorials">https://github.com/leanprover-community/mathlib/tree/tutorials/tutorials</a> in you post on MO? Or is it ok with you if we edit the post while writing tutorials on the 5 challenges that you suggested?</p>

#### [ Johan Commelin (Oct 09 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135451645):
<p>General question <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> <span class="user-mention" data-user-id="123965">@Bryan Gin-ge Chen</span> should we leave active <code>#eval</code> and <code>#print</code> statements in these tutorials? Or should they be commented out, so that they don't spam ordinary mathlib-builds. I suppose it is easy enough for the user to uncomment them.</p>

#### [ Mario Carneiro (Oct 09 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135451694):
<p>I'm not sure mathlib is the best place for them</p>

#### [ Johan Commelin (Oct 09 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135451700):
<p>them what?</p>

#### [ Mario Carneiro (Oct 09 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135451706):
<p>the tutorials</p>

#### [ Johan Commelin (Oct 09 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135451713):
<p>I think it is</p>

#### [ Mario Carneiro (Oct 09 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135451716):
<p>Especially if it is an interactive walkthrough</p>

#### [ Johan Commelin (Oct 09 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135451717):
<p>Because it forces us to make sure they compile</p>

#### [ Mario Carneiro (Oct 09 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135451773):
<p>I don't know, I mean TPIL has code snippets and they only break occasionally, and it is reported and fixed</p>

#### [ Mario Carneiro (Oct 09 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135451785):
<p>It's not like they are going to be based on really complicated things</p>

#### [ Johan Commelin (Oct 09 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135451801):
<blockquote>
<p>It's not like they are going to be based on really complicated things</p>
</blockquote>
<p>One of the challenges is on nilpotent ideals... it would break helplessly by your module refactor.</p>

#### [ Mario Carneiro (Oct 09 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135451848):
<p>They could just as easily be in a separate project. Even better, if a user downloads the tutorial project depending on mathlib then they are already in the right place to do work of their own</p>

#### [ Kenny Lau (Oct 09 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135451861):
<blockquote>
<p>One of the challenges is on nilpotent ideals... it would break helplessly by your module refactor.</p>
</blockquote>
<p>what do you mean?</p>

#### [ Mario Carneiro (Oct 09 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135451871):
<p>I'm not saying they never change, but they won't change often</p>

#### [ Johan Commelin (Oct 09 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135451884):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> <a href="https://mathoverflow.net/a/311159/21815" target="_blank" title="https://mathoverflow.net/a/311159/21815">https://mathoverflow.net/a/311159/21815</a></p>

#### [ Kenny Lau (Oct 09 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135451939):
<p>yes?</p>

#### [ Johan Commelin (Oct 09 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135451954):
<p>That's homework for us (-;</p>

#### [ Scott Morrison (Oct 09 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135454675):
<p>I'd be pretty happy to see tutorials embedded in mathlib for now. Anything to avoid useful stuff bit-rotting away. :-)</p>

#### [ Sean Leather (Oct 09 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135455291):
<p>I agree that tutorials should go into in mathlib. I think that, as long as the plan is to keep mathlib monolithic (which seems to be working out for the most part), it should include tutorials. A reasonable alternative is to build a tutorial repository during mathlib's CI test phase.</p>

#### [ Mario Carneiro (Oct 09 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135455714):
<p>I still think it is a good idea to have a "scratch" repo that newbies can get to have a working setup in vscode with mathlib already hooked in, since this is the recommended use</p>

#### [ Johan Commelin (Oct 09 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135455740):
<p>What do you mean with "recommended use"?</p>

#### [ Mario Carneiro (Oct 09 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135455751):
<p>I mean this is the way third parties use mathlib</p>

#### [ Mario Carneiro (Oct 09 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135455802):
<p>you have a project, and this project imports mathlib</p>

#### [ Mario Carneiro (Oct 09 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135455809):
<p>this is the format vscode is expecting</p>

#### [ Mario Carneiro (Oct 09 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135455831):
<p>You can have mathlib as a global install and work with loose files, but I think this approach is less robust</p>

#### [ Johan Commelin (Oct 09 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135455852):
<p>Right, but I'm more thinking about mathematicians that want to contribute to mathlib</p>

#### [ Mario Carneiro (Oct 09 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135455859):
<p>contributing to mathlib is another thing altogether</p>

#### [ Johan Commelin (Oct 09 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135455901):
<p>So they will end up hacking on the community fork asap</p>

#### [ Mario Carneiro (Oct 09 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135455909):
<p>sure, in that case they are working on mathlib itself so there is already a project</p>

#### [ Mario Carneiro (Oct 09 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135455916):
<p>I mean for new leaners, like the kids in Kevin's classes</p>

#### [ Johan Commelin (Oct 09 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135455917):
<p>Right, and they get to know that project by looking in <code>tutorials/</code></p>

#### [ Scott Morrison (Oct 09 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135455933):
<p>A scratch project is a good idea.</p>

#### [ Johan Commelin (Oct 09 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135455938):
<p>I see. Well, I was more thinking about people like Neil.</p>

#### [ Mario Carneiro (Oct 09 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135455947):
<p>I don't think Neil was ready to be a contributor</p>

#### [ Scott Morrison (Oct 09 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135455951):
<p>Just the bare minimum setup, with perhaps a file that reminds them where to go for more help.</p>

#### [ Mario Carneiro (Oct 09 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135455966):
<p>I assume people start out with projects on their own for a while, and then move to contribution if they are so inclined</p>

#### [ Johan Commelin (Oct 09 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135455967):
<p><a href="https://github.com/leanprover-community/hello-world" target="_blank" title="https://github.com/leanprover-community/hello-world">https://github.com/leanprover-community/hello-world</a></p>

#### [ Scott Morrison (Oct 09 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135456022):
<p>And as Lean/mathlib improves, we actually hope a larger and larger fraction of the community are _not_ hacking on mathlib!</p>

#### [ Johan Commelin (Oct 09 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135456026):
<p>Why?</p>

#### [ Johan Commelin (Oct 09 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135456031):
<p>I thought we wanted to be a massive monolith</p>

#### [ Scott Morrison (Oct 09 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135456033):
<p>(because they're actually doing maths, rather than filling in all the gaps before they can actually get started)</p>

#### [ Sean Leather (Oct 09 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135456040):
<p>There's ambiguity in the word “tutorial.” I was thinking of something more like a walkthrough of various features of mathlib. But a scratch/hello-world repository would also be useful.</p>

#### [ Johan Commelin (Oct 09 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135456045):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> But why not do maths inside mathlib?</p>

#### [ Scott Morrison (Oct 09 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135456047):
<p>If I'm going to formalise a bunch of the boring-but-technical lemmas in my research paper, they don't belong in mathlib.</p>

#### [ Mario Carneiro (Oct 09 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135456049):
<p><span class="user-mention" data-user-id="110045">@Sean Leather</span>  I guess Kevin's mathlib docs pages already do that?</p>

#### [ Scott Morrison (Oct 09 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135456127):
<p>or because they're working out the lemmas for their research project. They don't belong in mathlib because they've got no idea if they're the right lemmas yet. But this is all dreaming. For the next couple of decades, I agree, all in mathlib. :-)</p>

#### [ Sean Leather (Oct 09 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135456195):
<blockquote>
<p>I guess Kevin's mathlib docs pages already do that?</p>
</blockquote>
<p>Not in the sense that you can see examples in Lean of what is provable and how with mathlib.</p>

#### [ Sean Leather (Oct 09 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135456299):
<p>Perhaps I'm off-topic here with my own definition of tutorial — I'm not sure — but I was thinking of something that demonstrated usage of mathlib with proofs and words, not <em>just</em> words.</p>

#### [ Johan Commelin (Oct 09 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135457779):
<p><span class="user-mention" data-user-id="110045">@Sean Leather</span> I think we can have both</p>

#### [ Sean Leather (Oct 09 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135457873):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> Yep, we probably should.</p>

#### [ Kevin Buzzard (Oct 09 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tutorial/near/135482607):
<p>The Xena.zip file which I was going to use with my 1st years this year (until ICT delivered something much better) -- that was precisely what Mario was describing above. The way this seems to work is that once a year I am allowed to update what the Imperial College undergraduates see by default when they open up VS Code. This year they see a project with one file <code>test.lean</code> containing <code>import data.int.basic theorem 2+2=4:=rfl</code> and then all the lean and olean files for mathlib and lean (with mathlib as a dependency). This is what I would now call "the bare minimum for mathematicians who are interested". But it sounds like the community might be able to make a much better variant of this, which we could just generally advertise on GH. I think it's worth stressing that win10 users have no git and no command line, and I've met plenty of people who just want to get going. We make a better repo, and we replace Xena.zip with this repo and I document it on the installation page and people will be happier.</p>


{% endraw %}
