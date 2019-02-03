---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/78247categories.html
---

## Stream: [maths](index.html)
### Topic: [categories](78247categories.html)

---


{% raw %}
#### [ Reid Barton (Sep 05 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133380177):
<p>This new functor arrow doesn't seem to have an abbreviation in emacs.<br>
'to input: type "C-x 8 RET 2964" or "C-x 8 RET RIGHTWARDS HARPOON WITH BARB UP ABOVE RIGHTWARDS HARPOON WITH BARB DOWN"'</p>

#### [ Reid Barton (Sep 05 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133403401):
<p>Scott, I see in the latest version of limits, <code>is_limit</code> and so on have become classes. I'm not sure how workable that will be because there are so many different ways to obtain new (co)limits from old ones. Right now I'm proving that restriction along a cofinal functor preserves colimit cones, but also consider that a left adjoint preserves colimits, and pushout squares glue together, and the other stuff I proved in my colimit_lemmas.lean file. I think this is too much to ask of the class system, and I worry that making the <code>is_*</code> types classes will make it more difficult to apply all these facts about (co)limits.</p>

#### [ Reid Barton (Sep 05 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133404897):
<p>We still don't have <code>is_singleton</code> do we?</p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">(</span><span class="n">C</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="err">𝒞</span> <span class="o">:</span> <span class="n">category</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span> <span class="n">v</span><span class="o">}</span> <span class="n">C</span><span class="o">]</span>
<span class="n">include</span> <span class="err">𝒞</span>

<span class="n">def</span> <span class="n">is_connected</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="o">:=</span> <span class="n">is_singleton</span> <span class="o">(</span><span class="n">quot</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">C</span><span class="o">),</span> <span class="n">nonempty</span> <span class="o">(</span><span class="n">a</span> <span class="err">⟶</span> <span class="n">b</span><span class="o">)))</span>
</pre></div>

#### [ Reid Barton (Sep 05 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133404913):
<p>Lean taught me that this is the True Definition.</p>

#### [ Kenny Lau (Sep 05 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133404989):
<p>so the empty graph isn't connected?</p>

#### [ Reid Barton (Sep 05 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133405066):
<p>You missed a discussion on this topic in Orsay.</p>

#### [ Reid Barton (Sep 05 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133405067):
<p><a href="https://ncatlab.org/nlab/show/connected+category" target="_blank" title="https://ncatlab.org/nlab/show/connected+category">https://ncatlab.org/nlab/show/connected+category</a></p>

#### [ Johannes Hölzl (Sep 05 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133405186):
<p>Shouldn't <code>is_singleton</code> be a <code>Prop</code>?</p>

#### [ Reid Barton (Sep 05 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133405317):
<p>That is an interesting question. If I make it constructive, then I can prove the result about cofinal functors preserving colimits constructively as well. It's actually a bit subtle--you need to get your hands on an inhabitant of C, but if you define connectedness in terms of the existence of zigzags, then you don't need the zigzags constructively, because they are only used to prove equalities.</p>

#### [ Reid Barton (Sep 05 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133405369):
<p>Currently, I simply have <code>def is_singleton (α : Type*) := α ≃ unit</code>.<br>
This plus the above definition gives the correct amount of constructiveness.</p>

#### [ Reid Barton (Sep 05 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133405456):
<p><code>is_colimit</code> is not a Prop (it is a subsingleton though), because it includes the data of how to construct the map given by the universal property. In order to build that map in my setting, I need to know that certain categories are connected in the above constructive sense.</p>

#### [ Reid Barton (Sep 05 2018 at 23:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133405470):
<p>I'm still not sure whether these distinctions between Prop and subsingletons are worth making in the context of category theory.</p>

#### [ Reid Barton (Sep 05 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133405561):
<p>For context, I proved basically the implication 1 =&gt; 3 at <a href="https://ncatlab.org/nlab/show/final+functor#properties" target="_blank" title="https://ncatlab.org/nlab/show/final+functor#properties">https://ncatlab.org/nlab/show/final+functor#properties</a>.</p>

#### [ Reid Barton (Sep 05 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133405580):
<p>There it is stated as "a map ... is an isomorphism", which is also a proposition classically which has constructive content.</p>

#### [ Reid Barton (Sep 05 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133405669):
<p>It's kind of fun to see how all these constructive aspects relate to one another, but I'm not sure how useful it is and there are some associated minor annoyances.</p>

#### [ Reid Barton (Sep 05 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133405675):
<p>So: I don't know. :)</p>

#### [ Reid Barton (Sep 06 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133405841):
<p>Probably either the name or the definition is wrong though.</p>

#### [ Kevin Buzzard (Sep 06 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133405857):
<p>yeah, that's definitely path-connected ;-)</p>

#### [ Reid Barton (Sep 06 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133407262):
<p>Haha :) The distinction doesn't exist to a homotopy theorist.<br>
I remember being very confused when I couldn't prove that an arbitrary product of discrete topological spaces is discrete. Then I realized it was only true up to weak homotopy equivalence...</p>

#### [ Scott Morrison (Sep 06 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133418582):
<p>I think it's relatively painless to turn <code>is_limit</code> and friends back into structures (not classes). I guess what I desired was that the fact that <code>is_limit c</code> is a subsingleton should imply that it's okay that there are different ways to construct it. But I understand that Lean is not actually that clever, and we will run into problems where two typeclass instances look different, even though a <code>subsingleton</code> instance is available.</p>

#### [ Scott Morrison (Sep 06 2018 at 05:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133418641):
<p>I do wonder if it could be a plausible addition to the typeclass mechanism: whenever we find that we using two instances that don't agree, first check for an instance of <code>subsingleton</code> before complaining about it.</p>

#### [ Scott Morrison (Sep 06 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133431137):
<p>So, <span class="user-mention" data-user-id="110032">@Reid Barton</span>, I guess I don't really understand what the problem is with having <code>is_limit</code> being a typeclass. Certainly there is a problem with having too many instances (because we'll get colliding instances), but nothing particularly forces us to mark constructions as instances.</p>

#### [ Scott Morrison (Sep 06 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133431150):
<p>Having "really canonical" ones, like the one that <code>has_limits</code> provides, seems quite helpful.</p>

#### [ Scott Morrison (Sep 06 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133431224):
<p>As you point out, we'll certainly want to use non-instance instances of <code>is_limit</code> and friends, so I agree a good change could be to change it back to a <code>structure</code> and just add the <code>class</code> attribute afterwards, so the syntax is as usual for structures.</p>

#### [ Scott Morrison (Sep 06 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133431231):
<p>I'm also open to being convinced it just shouldn't be a class at all.</p>

#### [ Reid Barton (Sep 06 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133431408):
<p>I think the structure + attribute [class] option will probably address my concerns. I do see the use of instance lookup for common cases.</p>

#### [ Reid Barton (Sep 06 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133431728):
<p>The problem with just a class is that it's useful to handle these <code>is_limit</code> values manually, as you say, and maybe I am just bad at dealing with classes, but I find there's more friction there. For example maybe you have a cone which is only propositionally equal to one which you have a lemma about. Then it's easier to <code>convert</code> the lemma application and fix up the resulting subgoals.</p>

#### [ Reid Barton (Sep 06 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133431818):
<p>I tried making my <code>is_colimit_of_is_cofinal</code> into an instance and it did work in the simple use case later... provided I made <code>is_cofinal</code> an instance too. It's infectious!</p>

#### [ Reid Barton (Sep 06 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133431838):
<p>Made <code>is_cofinal</code> a class, I mean.</p>

#### [ Johan Commelin (Sep 06 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133431861):
<p>That's automation, man!</p>

#### [ Reid Barton (Sep 06 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133432716):
<blockquote>
<p>For example maybe you have a cone which is only propositionally equal to one which you have a lemma about.</p>
</blockquote>
<p>I guess the point here is that being a limit cone is a property of a diagram, and diagrams have morphisms in them, and it's really common to have non-syntactic or even non-definitional equalities between morphisms (we call them commutative diagrams). Whereas for the class <code>group</code>, for instance, it's much less common to have non-syntactic equalities <em>between groups</em>.</p>

#### [ Scott Morrison (Sep 06 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133433168):
<p>Okay: for now I will try out having them as <code>structure</code> with <code>class</code> added after the fact. If that doesn't go well, complain and we can just go back to bare structures. I think you're making more use of limits than I am, so I'm happy to follow your direction.</p>

#### [ Scott Morrison (Sep 06 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133433224):
<p>Also on the topic of categories, I'd be curious <span class="user-mention" data-user-id="110032">@Reid Barton</span> and <span class="user-mention" data-user-id="112680">@Johan Commelin</span> if you have any thought about my concerns re: <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span>'s nice framework for building concrete categories from typeclasses.</p>

#### [ Scott Morrison (Sep 06 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133433227):
<p><a href="https://github.com/leanprover/mathlib/pull/316#issuecomment-419039990" target="_blank" title="https://github.com/leanprover/mathlib/pull/316#issuecomment-419039990">https://github.com/leanprover/mathlib/pull/316#issuecomment-419039990</a></p>

#### [ Scott Morrison (Sep 06 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133433231):
<p>My main concern is that it boxes us in to using lots of sigma types and subtypes, where my instinct had been to define lots of custom structures. :-)</p>

#### [ Johan Commelin (Sep 06 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133433281):
<p>hmmm... ring_homs don't form an additive group... but never mind</p>

#### [ Johan Commelin (Sep 06 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133433449):
<p><span class="user-mention" data-user-id="110524">@Scott Morrison</span> One of the reasons I was asking about definitions by meta code yesterday was for this sort of thing. If we make <code>concrete_category</code> meta, then it could make all those bundled defintions for us, couldn't it?</p>

#### [ Johan Commelin (Sep 06 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133433471):
<p>But I'm still too much of an amateur to know what the pros and cons are of these approaches.</p>

#### [ Johan Commelin (Sep 06 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133433482):
<p>My gut feeling is that if Johannes writes something, I won't be able to improve it. (Maybe next year <span class="emoji emoji-1f603" title="smiley">:smiley:</span>)</p>

#### [ Reid Barton (Sep 06 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133433564):
<p>oh I hadn't seen those comments yet, thanks.</p>

#### [ Reid Barton (Sep 06 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133434056):
<p>I also had the same, vague concern about your point 1. I hadn't thought of your point 2, will have to think about that one some more.<br>
I think the example you gave of homeomorphisms isn't that compelling, because you could also build (Top, homeos) as the category- (or groupoid-)of-isomorphisms-in the concrete-category Top. Maybe we can come up with a more interesting example?</p>

#### [ Reid Barton (Sep 06 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133434715):
<p>I commented about point 1 on the issue.</p>

#### [ Kevin Buzzard (Sep 06 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133434982):
<blockquote>
<p>I guess what I desired was that the fact that <code>is_limit c</code> is a subsingleton should imply that it's okay that there are different ways to construct it. But I understand that Lean is not actually that clever, and we will run into problems where two typeclass instances look different, even though a <code>subsingleton</code> instance is available.</p>
</blockquote>
<p>Chris Hughes had typeclass problems with <code>fintype</code> even though it's a subsingleton -- he would occasionally get two instances kicking around and then rewrites would start to fail. He even talked at some point about writing a tactic which might solve his problems, but somehow tactic-writing is not our fort\'e in London, nobody can do it yet, and he just ended up with too many questions which nobody could answer.</p>
<p>Even more interesting -- <code>is_linear_map</code> is a <code>Prop</code> but Johannes made it a structure not a class. I talked to him about this a bit in Orsay. My impression was that he couldn't see the point of adding it to the type class inference system, because the instance that you want to trigger -- composition of two linear maps is a linear map -- tends not to trigger, because in functional languages people compose functions by writing them next to each other rather than using <code>function.comp</code>. We now have a hybrid system where <code>is_group_hom</code> is a class and <code>is_linear_map</code> is not.</p>

#### [ Scott Morrison (Sep 06 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133435098):
<blockquote>
<p>hmmm... ring_homs don't form an additive group... but never mind</p>
</blockquote>
<p>Ooops. <span class="emoji emoji-1f633" title="flushed">:flushed:</span> I'll remove the evidence of that one. :-) There are plenty of less-wrong examples, of course.</p>

#### [ Scott Morrison (Sep 06 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133435184):
<p>The question about <code>is_linear_map</code> being problematic, because people write their functions using lambdas, could be solved by educating everyone to not use lambdas when you're hoping to use typeclass inference, I guess. It's not totally unreasonable. :-)</p>

#### [ Reid Barton (Sep 06 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133435273):
<p>And here I have been wondering how hard it would be to get something like lambda syntax for functors...</p>

#### [ Kevin Buzzard (Sep 06 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133435395):
<p>I actually engaged with Scott's category theory library for the first time yesterday, thanks to <span class="user-mention" data-user-id="120350">@Ned Summers</span> peppering me with questions, and I must say it was a bit scary having to do all the morphism composition using some morphism composition operator...</p>

#### [ Reid Barton (Sep 06 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133435403):
<p>I tried writing down just the expression "colim_{j in J} lim_{i in I} F(i, j)" and it turned into something ugly like <code>colimit ((curry.map F).comp lim)</code></p>

#### [ Reid Barton (Sep 06 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133435457):
<p>Kevin, that's why most of my files contain the magic words <code>local notation f ` ∘ `:80 g:80 := g ≫ f</code> :)</p>

#### [ Scott Morrison (Sep 06 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133435901):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span>, were you referring to having to write some composition operator, rather than a lambda, or to the fact that the composition operator is "backwards"?</p>

#### [ Scott Morrison (Sep 06 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133435982):
<p>(I've been thinking a lot recently about monoidal categories enriched in a braided category, and here it really matters that you write composition "correctly", because every time you move symbols past each other you have to keep track of a braiding.)</p>

#### [ Kevin Buzzard (Sep 06 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133436152):
<p>I can handle "backwards", it was the shock of having to do it at all.</p>

#### [ Scott Morrison (Sep 06 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133436515):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span>, unfortunately I'm having trouble with the <code>structure</code> + <code>attribute [class]</code> approach: I can't ever get it to infer the <code>is_limit</code> instances, making it pretty useless.</p>

#### [ Scott Morrison (Sep 06 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133436520):
<p>I guess I will go back to just structures.</p>

#### [ Kevin Buzzard (Sep 06 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133437816):
<p>If it's any help, I think this (<code>structure + attribute [class]</code>) is how topological spaces are set up.</p>

#### [ Ned Summers (Sep 06 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133455791):
<p>Hey guys,</p>
<p>I've got a situation where I have two objects of a category X and Y, and a theorem that says X = Y. Obviously there then is a f  : X ⟶ Y corresponding to the identity morphism on X (or the identity morphism on Y).  I was wondering if writing/using this has been dealt with so far in the mathlib category theory content?</p>
<p>(this is in the context of lean asking for something of type Y ⟶ Y. I have one of type X ⟶ X in mind but lean is not happy if I give it that here (except using cast or eq.rec and these have already caused a lot of trouble). Kevin and I figured it might be easier to instead compose on either side of this choice these morphisms X ⟶ Y and Y ⟶ X corresponding to those identities. Any ideas about that also welcomed!)<br>
Thanks!</p>

#### [ Reid Barton (Sep 06 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133456083):
<p>Yes, there is something for exactly this situation. See <code>eq_to_iso</code> in <code>category_theory.isomorphism</code>.</p>

#### [ Reid Barton (Sep 06 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133456175):
<p>And there are a couple simp lemmas there which are supposed to make proving things about composition with these morphisms easier than proving things about <code>eq.rec</code>.</p>

#### [ Reid Barton (Sep 06 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133463164):
<p><span class="user-mention" data-user-id="110524">@Scott Morrison</span>, do you have some conversions between <code>equiv</code> and <code>iso</code> in Set somewhere?</p>

#### [ Scott Morrison (Sep 07 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133475856):
<p>No, I don't have that conversion, but it should be added!</p>

#### [ Scott Morrison (Sep 07 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133475863):
<p>"equiv is iso to iso"? :-)</p>

#### [ Kenny Lau (Sep 07 2018 at 03:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133483585):
<p><span class="user-mention" data-user-id="110524">@Scott Morrison</span> Do we have Yoneda? :D</p>

#### [ Scott Morrison (Sep 07 2018 at 03:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133483801):
<p>Sure, it's in &lt;<a href="https://github.com/semorrison/lean-category-theory/blob/master/src/category_theory/yoneda.lean" target="_blank" title="https://github.com/semorrison/lean-category-theory/blob/master/src/category_theory/yoneda.lean">https://github.com/semorrison/lean-category-theory/blob/master/src/category_theory/yoneda.lean</a>&gt;. It's slowly getting towards the head of the queue for PR'ing into mathlib...</p>

#### [ Reid Barton (Sep 10 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133627435):
<p>Mario, do you have an opinion on whether "the category C is connected" and "the functor F is cofinal" should be props or subsingletons?</p>

#### [ Reid Barton (Sep 10 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133627486):
<p>I have a version using subsingletons and it means you can prove cofinal functors preserve colimits constructively (e.g., produce an inverse to the induced map) which is kind of cool, but now I feel it's probably not worth the hassle</p>

#### [ Mario Carneiro (Sep 10 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133627621):
<p><a href="https://ncatlab.org/nlab/show/final+functor" target="_blank" title="https://ncatlab.org/nlab/show/final+functor">https://ncatlab.org/nlab/show/final+functor</a></p>
<blockquote>
<p>A functor F:C→DF : C \to D is final (often called cofinal)</p>
</blockquote>
<p>WHYY</p>

#### [ Mario Carneiro (Sep 10 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133627622):
<blockquote>
<p>Dually, a functor is initial (sometimes called co-cofinal)</p>
</blockquote>
<p>wtf</p>

#### [ Mario Carneiro (Sep 10 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133627628):
<p>I think I'm co-confused</p>

#### [ Mario Carneiro (Sep 10 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133627825):
<p>To me, "connected" sounds like a Prop, I'm not sure how to state it naturally as a subsingleton without using <code>trunc</code></p>

#### [ Mario Carneiro (Sep 10 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133627838):
<p>The definition of cofinal appears to use "nonempty and connected", which sounds like an "is_singleton" statement, which I can see usefully as a type. Is there a natural choice of inhabitant in this case?</p>

#### [ Mario Carneiro (Sep 10 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133627882):
<p>I think that being able to construct inverses to given maps is one of the more relevant uses of doing category theory constructively</p>

#### [ Reid Barton (Sep 10 2018 at 04:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133633778):
<p>Yeah the terminology is unfortunate. The "co-" is not the dualizing "co-", but the "together" one, like the categories have the same behavior as you go towards the "end". In practice people only care about (co)final functors and not the other side I think.</p>

#### [ Reid Barton (Sep 10 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133633825):
<blockquote>
<p>Is there a natural choice of inhabitant in this case?</p>
</blockquote>
<p>There isn't automatically one in general but typically when you prove a functor is cofinal there will be an obvious way to choose an inhabitant.</p>

#### [ Reid Barton (Sep 10 2018 at 04:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133633979):
<p>Oh yes, by connected I mean to include nonempty. That's the only part which is data</p>

#### [ Reid Barton (Sep 10 2018 at 04:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133634088):
<p>The connected components are <code>quot (λ (a b : C), nonempty (a ⟶ b))</code> (for some reason I don't remember ever seeing this very simple and Lean-friendly definition), and then you need to say this type has exactly one inhabitant, which can be constructively or not.</p>

#### [ Reid Barton (Sep 10 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/categories/near/133634200):
<p>I guess I'll continue to try with the constructive definition if you don't have a strong opinion. The pros and cons of both approaches are pretty minor</p>


{% endraw %}
