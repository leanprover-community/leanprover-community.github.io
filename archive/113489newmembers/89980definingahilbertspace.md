---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/89980definingahilbertspace.html
---

## Stream: [new members](index.html)
### Topic: [defining a hilbert space](89980definingahilbertspace.html)

---


{% raw %}
#### [ Joseph Corneli (Jul 31 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130645249):
<p>Hi, this looks like something that might be near the edge of what's possible to define right now; would a more experienced person be able to give me some guidance?</p>
<blockquote>
<p>"A Hilbert space H is a real or complex inner product space that is also a complete metric space with respect to the distance function induced by the inner product."</p>
</blockquote>
<p>If this is within the range of what's possible to define maybe it's a good exercise -- but as a newbie I'd still appreciate some help!</p>
<p>To begin with, can we define an "<a href="https://en.wikipedia.org/wiki/Inner_product_space" target="_blank" title="https://en.wikipedia.org/wiki/Inner_product_space">inner product space</a>" using <code>prod_module.lean</code>?  That file talks about "Left injection function for the inner product" (resp., right injection).  But the code doesn't seem to have much in common with my idea of an "inner product," however.</p>
<p>On to the next step, <code>metric_space.lean</code> mentions "completeness" but the class <code>complete_space</code> is defined in <code>uniform_space.lean</code>; I guess we can get completeness from the generalisation; how would we insist upon completeness "with respect to the distance function"?</p>
<p>My guess is that the components are not ready "off the shelf" but still are within reach.  Would this be a worthwhile project to tackle?   If not, is there another topic that is more easily within reach?</p>

#### [ Johan Commelin (Jul 31 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130645351):
<p>Hmmm, I fear it is quite hard. <span class="user-mention" data-user-id="110031">@Patrick Massot</span> has been struggling with normed spaces for a long time.</p>

#### [ Kenny Lau (Jul 31 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130645376):
<p>the definition is just a bunch of axioms</p>

#### [ Johan Commelin (Jul 31 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130645392):
<p>Right.</p>

#### [ Patrick Massot (Jul 31 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130646185):
<p>metric spaces have a canonical uniform space structure, so completeness is defined for them as well</p>

#### [ Patrick Massot (Jul 31 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130646189):
<p>I think you can easily define Hilbert spaces</p>

#### [ Kevin Buzzard (Jul 31 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130646196):
<p>Yes, the definition is not hard at all. It's proving the basic properties where you'll start to learn what Lean can and cannot do easily. <span class="user-mention" data-user-id="120943">@Andreas Swerdlow</span> , a first year undergraduate at Imperial College, already formalised Hilbert spaces here: <a href="https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/inner_product_spaces/basic.lean" target="_blank" title="https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/inner_product_spaces/basic.lean">https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/inner_product_spaces/basic.lean</a></p>

#### [ Patrick Massot (Jul 31 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130646206):
<p>Note that I struggle to get a norm on R^n, not to define normed spaces (at least not anymore)</p>

#### [ Kenny Lau (Jul 31 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130646208):
<p>but maybe you're Kevin Buzzard and only care about the definition :P</p>

#### [ Kevin Buzzard (Jul 31 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130646233):
<p>If you have any lemmas which you'd like proved, let Andreas know Kenny!</p>

#### [ Patrick Massot (Jul 31 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130646255):
<p><a href="https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/inner_product_spaces/basic.lean#L655" target="_blank" title="https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/inner_product_spaces/basic.lean#L655">https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/inner_product_spaces/basic.lean#L655</a> is not correct</p>

#### [ Patrick Massot (Jul 31 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130646332):
<p>it does not impose any relation between the uniform structure and the inner product</p>

#### [ Kevin Buzzard (Jul 31 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130646335):
<p>Maybe he's not finished yet :-)</p>

#### [ Joseph Corneli (Jul 31 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130648269):
<p>Thanks for the answers and discussion.</p>

#### [ Andreas Swerdlow (Aug 01 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130708575):
<blockquote>
<p>it does not impose any relation between the uniform structure and the inner product</p>
</blockquote>
<p>Hi Patrick,</p>
<p>I see the problem with my definition, but after looking through the definition of a complete space in lean, I realised I don't know enough to fix it.  Do you have any suggestions?</p>

#### [ Johan Commelin (Aug 01 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130709091):
<p>After <code>class hilbert_space (V : Type u) extends herm_inner_product_space V, complete_space V</code> you should have one or more fields that demand compatibility between the inner product space and the complete space.</p>

#### [ Kevin Buzzard (Aug 01 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130713865):
<p>I'm in the same room as Andreas but haven't thought about how Lean does these things. I guess he's defined an inner product so I know about that. But the definition of <code>complete_space</code> involves Cauchy filters. I would imagine that there are right and wrong ways to do this. Oh -- do we just demand that the topology induced by the metric on <code>V</code> (<span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>d</mi><mo>(</mo><mi>x</mi><mo separator="true">,</mo><mi>y</mi><mo>)</mo><mo>=</mo><mi mathvariant="normal">∣</mi><mi mathvariant="normal">∣</mi><mi>y</mi><mo>−</mo><mi>x</mi><mi mathvariant="normal">∣</mi><mi mathvariant="normal">∣</mi></mrow><annotation encoding="application/x-tex">d(x,y)=||y-x||</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit">d</span><span class="mopen">(</span><span class="mord mathit">x</span><span class="mpunct">,</span><span class="mord mathit" style="margin-right:0.03588em;">y</span><span class="mclose">)</span><span class="mrel">=</span><span class="mord mathrm">∣</span><span class="mord mathrm">∣</span><span class="mord mathit" style="margin-right:0.03588em;">y</span><span class="mbin">−</span><span class="mord mathit">x</span><span class="mord mathrm">∣</span><span class="mord mathrm">∣</span></span></span></span>) equals the topology which <code>complete_space</code> is using? Andreas -- can you make any sense of what I'm saying?</p>

#### [ Johan Commelin (Aug 01 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130713913):
<p>Hmm, but I guess they have to be def.eq. Because of <span class="emoji emoji-2666" title="diamonds">:diamonds:</span></p>

#### [ Kevin Buzzard (Aug 01 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130714094):
<p>Only if there's some sort of inbuilt instance going from <code>herm_inner_product_space</code> to <code>topological_space</code> right?</p>

#### [ Johan Commelin (Aug 01 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130714208):
<p>Right, but I suppose that we do want instances for that.</p>

#### [ Andreas Swerdlow (Aug 01 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130714256):
<p>I've proved that the inner product induces the natural metric</p>

#### [ Johan Commelin (Aug 01 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130714269):
<p>Yes, but proofs are not enough.</p>

#### [ Johan Commelin (Aug 01 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130714280):
<p>Alas..., this is not mathematics. And beyond my pay-grade.</p>

#### [ Kevin Buzzard (Aug 01 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130715205):
<p>The issue I think is that there is no "natural metric", if I've understood things correctly. You wrote <code>class hilbert_space (V : Type u) extends herm_inner_product_space V, complete_space V</code> -- so this says "there's some inner product on V -- this is an assumption -- we don't know any more about it" and "there's some topology on V that makes V complete -- this is an assumption -- we don't know any more about it", so there are now perhaps two topologies on V if I've understood correctly what these typeclasses are.</p>

#### [ Joseph Corneli (Aug 01 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130715968):
<p>According to a comment in <code>uniform_space.lean</code>, "A uniform space is complete if every Cauchy filter converges." Would it not be necessary to show the latter fact?  I see three equivalent Bourbakian conditions (in the case of metric spaces) mentioned on page 8 of <a href="https://arxiv.org/pdf/1802.08521.pdf" target="_blank" title="https://arxiv.org/pdf/1802.08521.pdf">https://arxiv.org/pdf/1802.08521.pdf</a>, referring to Bourbaki, General Topology, II3.3, Def. 3.  Looks like heavy going.</p>

#### [ Johannes Hölzl (Aug 01 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130716250):
<p>this is the definition of completeness</p>
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">complete_space</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">uniform_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">complete</span> <span class="o">:</span> <span class="bp">∀</span><span class="o">{</span><span class="n">f</span><span class="o">:</span><span class="n">filter</span> <span class="n">α</span><span class="o">},</span> <span class="n">cauchy</span> <span class="n">f</span> <span class="bp">→</span> <span class="bp">∃</span><span class="n">x</span><span class="o">,</span> <span class="n">f</span> <span class="bp">≤</span> <span class="n">nhds</span> <span class="n">x</span><span class="o">)</span>
</pre></div>


<p>Which says that <code>[complete_space A]</code> is defined to be that each Cauchy filter converges.</p>

#### [ Joseph Corneli (Aug 01 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130716885):
<p>Yep, I'm of the view that this must be derived from Andreas's  assertions about Hermitian inner product space.  Without that condition it sounds like he has what's called a "pre-Hilbert space" <em>"An (incomplete) space with an inner product is called a pre-Hilbert space, since its completion with respect to the norm induced by the inner product is a Hilbert space."</em></p>

#### [ Joseph Corneli (Aug 01 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130717776):
<p>Though I guess the point is that the condition of completeness is precisely what cannot be shown in general, otherwise there would not be such a thing as pre-Hilbert spaces.  So, to round out <code>inner_product_space/basic.lean</code> it would be good to have an <em>example</em> of a Hilbert space.</p>

#### [ Kevin Buzzard (Aug 01 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130718011):
<p>So I don't quite know the best way of doing this. Andreas has defined an instance from his <code>herm_inner_product_space</code> to metric spaces, and hence to topological space. So now how to define a class Hilbert space? Should he extend <code>hern_inner_product_space</code> and then add precisely the axioms needed to prove <code>complete_space</code> -- I mean -- rewrite them all again in full? Just cutting and pasting from <code>#print complete_space</code>? And then he can make an instance from <code>Hilbert_space</code> to <code>complete_space</code>? I guess there's also the other approach -- he could have it extend <code>complete_space</code> and then write down precisely the axioms of an inner product space that aren't there already -- eew --- and then he'd have to supply a proof that the topology defined by the norm equals the original topology. Is this how to think about things? The first approach is the correct one, right?</p>

#### [ Gabriel Ebner (Aug 01 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130718081):
<blockquote>
<p>add precisely the axioms needed to prove complete_space</p>
</blockquote>
<p>That's just the one line Johannes posted.</p>

#### [ Kevin Buzzard (Aug 01 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130719157):
<p>Got it :-) I didn't see Johannes' post -- too much going on! Thanks all!</p>

#### [ Kevin Buzzard (Aug 01 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130719242):
<p><a href="https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/92b9d48860f0f68de78ccdd3c103335d9b55d5c8/src/inner_product_spaces/basic.lean#L669" target="_blank" title="https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/92b9d48860f0f68de78ccdd3c103335d9b55d5c8/src/inner_product_spaces/basic.lean#L669">https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/92b9d48860f0f68de78ccdd3c103335d9b55d5c8/src/inner_product_spaces/basic.lean#L669</a></p>

#### [ Kevin Buzzard (Aug 01 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130719243):
<p>Think we got it</p>

#### [ Joseph Corneli (Aug 01 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130721333):
<p>To test it out can we now prove, e.g., that "The real numbers R^n with &lt;v,u&gt; the vector dot product of v and u" forms a Hilbert space?</p>

#### [ Kevin Buzzard (Aug 01 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130721998):
<p>That's going to need a whole lot of lemmas</p>

#### [ Kevin Buzzard (Aug 01 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130722018):
<p>...which are probably there already.</p>

#### [ Kevin Buzzard (Aug 01 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130722123):
<p>...actually maybe they're not all in mathlib. You'll need things like if n sequences all tend to zero then their sum tends to zero, you'll need that if a_n tends to zero and 0 &lt;= b_n &lt;= a_n then b_n tends to zero etc. This sort of stuff is not really mathlib's strong point at this stage.</p>

#### [ Reid Barton (Aug 01 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130722355):
<p>Maybe try n = 1 first...</p>

#### [ Kevin Buzzard (Aug 01 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130722518):
<p>...and then prove that a direct sum of two Hilbert spaces is a Hilbert space...</p>

#### [ Andreas Swerdlow (Aug 01 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130722847):
<p>I need to rewrite the definition of <code>herm_inner_product_space</code> so that it works over any subfield of the complex numbers. At the moment you can only prove that C^n is a Hilbert space</p>

#### [ Joseph Corneli (Aug 01 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130723051):
<p>No L^2 functions as yet?</p>

#### [ Joseph Corneli (Aug 01 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130723247):
<p>Anyway I do think an example, say C, would be great to include in the file.  Some test-driven development would be useful  if you're going to generalise!  If it works for C but fails for R, that would be interesting.</p>

#### [ Patrick Massot (Aug 01 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130735854):
<p>I'm sorry I didn't help earlier, I was on the road all afternoon. Your definition is still not correct. You still have an inner product and a uniform space with no relation whatsoever.</p>

#### [ Patrick Massot (Aug 01 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130735888):
<p>Did you look at <a href="https://github.com/leanprover/mathlib/pull/208" target="_blank" title="https://github.com/leanprover/mathlib/pull/208">https://github.com/leanprover/mathlib/pull/208</a>?</p>

#### [ Patrick Massot (Aug 01 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130736158):
<p>The way this problem is handled is really weird for mathematicians. In <a href="https://github.com/leanprover/mathlib/pull/208/files#diff-81ed9f450352da041af7e0c731a22cdbR10" target="_blank" title="https://github.com/leanprover/mathlib/pull/208/files#diff-81ed9f450352da041af7e0c731a22cdbR10">https://github.com/leanprover/mathlib/pull/208/files#diff-81ed9f450352da041af7e0c731a22cdbR10</a> a normed group gather the attributes of a commutative additive group and a metric space, together with a function <code>norm</code> and an axiom saying that the distance of the metric space comes from the norm. Note that the <code>extends</code> keyword automatically creates an instance deriving a metric space from a normed group.</p>

#### [ Patrick Massot (Aug 01 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130736345):
<p>The weirdest comes next. A metric space is also defined in the kind of way, it bundles what you think should be there together with a uniform space structure and an axiom saying the uniform space structure equals what you would define from a structure. And a uniform space structure is defined in turn as extending both a topological structure and what you would call a uniform structure, together with an axiom relating both worlds.</p>

#### [ Patrick Massot (Aug 01 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130736482):
<p>The reason for this contrived setup is kind of subtle, it's meant to ensure that some stuff are definitionally equal, not only provably equal. It doesn't prevent us from using these structures, because there are various tricks (custom constructors or mechanisms to give default values to some fields) which hide them from us when building instances.</p>

#### [ Patrick Massot (Aug 01 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130736544):
<p>But really the problem with your current definition if much more basic: you don't enforce any relation between the norm and the topology</p>

#### [ Patrick Massot (Aug 01 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130736627):
<p>If you are serious about bringing Hilbert spaces to Lean, it would probably make more sense to pester <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> until he either merges my norms PR or ditches it and rolls his own, and then you could try to build Hilbert spaces on top of it.</p>

#### [ Simon Hudon (Aug 01 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130736917):
<p>The other alternative is to work off of <span class="user-mention" data-user-id="110031">@Patrick Massot</span> 's branch of mathlib</p>

#### [ Kevin Buzzard (Aug 01 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130736929):
<p>Patrick I think we're OK -- line 666 is the relation. It's my fault -- I linked to the wrong line. The definition is above where I linked -- sorry. Do you think we're OK?</p>

#### [ Simon Hudon (Aug 01 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130736932):
<p>... taking the risk that <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> will request changes and that you'll have to adapt your definitions to reflect them</p>

#### [ Patrick Massot (Aug 01 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130737271):
<p>Line 666 is a relation between the uniform structure and the topology it generates, it has nothing to do with the norm</p>

#### [ Kevin Buzzard (Aug 01 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130738460):
<p>I am not so sure. <code>Hilbert_space V</code> extends <code>herm_inner_product_space V</code>. There's an instance sending <code>herm_inner_product_space V</code> to <code>topological_space V</code> [not that you can easily spot this -- it's somewhere else in this huge file]. I think that the <code>is_open</code> on line 666 refers to this topological space structure. I quite agree that if we had a topology generated by the uniform structure we'd be in trouble and this is exactly why we extend <code>uniform_space.core V</code> and not <code>uniform_space V</code>. Did I convince you yet?</p>

#### [ Kevin Buzzard (Aug 01 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130738520):
<p>The instance is in line 613 and it's noncomputable because Andreas had to take the square root of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>(</mo><mi>v</mi><mo separator="true">,</mo><mi>v</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">(v,v)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.03588em;">v</span><span class="mpunct">,</span><span class="mord mathit" style="margin-right:0.03588em;">v</span><span class="mclose">)</span></span></span></span> and square root is noncomputable!</p>

#### [ Mario Carneiro (Aug 01 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130738615):
<p>if there are two active topologies on the structure, it should be an axiom or theorem that they are equal</p>

#### [ Mario Carneiro (Aug 01 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130738688):
<p>although in this case I think you can actually get a uniform space from the inner product</p>

#### [ Mario Carneiro (Aug 01 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130738699):
<p>noncomputability of a uniform space structure means nothing since it is not data</p>

#### [ Patrick Massot (Aug 01 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130738818):
<p>I just realized that we don't talk about the same version</p>

#### [ Patrick Massot (Aug 01 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130738827):
<p>I cloned your repo, and there were several commits on those files in the mean time</p>

#### [ Patrick Massot (Aug 01 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130738857):
<p>In particular I didn't look at that instance on line 613 which is currently commented out</p>

#### [ Kevin Buzzard (Aug 01 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130739715):
<p>Oh! :-)</p>

#### [ Kevin Buzzard (Aug 01 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130739904):
<p>We specifically avoided two topologies on the structure, I believe. This was exactly the problem which Patrick pointed out the first time around. Yes, we get a uniform space structure from the inner product -- that's exactly what we do now. Andreas extends uniform_space.core and then we make an instance of the uniform space using the topology coming from the norm plus an axiom that it agrees with the topology which comes from the uniform space. I am in the middle of doing something else right now but I assume there is no instance which gives a topology from a uniform_space.core -- I'm assuming that that's precisely the point of the structure, it's like a distrib.</p>

#### [ Mario Carneiro (Aug 01 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130739993):
<p>You probably shouldn't use <code>uniform_space.core</code> in this case</p>

#### [ Mario Carneiro (Aug 01 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130740044):
<p>you already have a topology coming from somewhere else, so use that in <code>uniform_space</code> and prove the equality axiom rather than letting <code>uniform_space.core</code> fill it in for you</p>

#### [ Kevin Buzzard (Aug 01 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130740761):
<p>V is just a vector space -- the only metric/topology we have on it is coming from the norm. All we want to do is to say that the metric is complete. We have no uniform structure or anything. I don't want to do uniform anything -- I just want to say that the metric space is complete. The only reason we're extending uniform_space.core is that this is the only way I know how to say this in Lean! What am I missing?</p>

#### [ Mario Carneiro (Aug 01 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130741388):
<p>if it has a norm then it extends <code>normed_vector_space</code>, with the attendant norm, metric, uniform space and topology</p>

#### [ Mario Carneiro (Aug 01 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130741406):
<p>the "agreement" here with the inner product says <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>(</mo><mi>v</mi><mo separator="true">,</mo><mi>v</mi><mo>)</mo><mo>=</mo><mi mathvariant="normal">∥</mi><mi>v</mi><msup><mi mathvariant="normal">∥</mi><mn>2</mn></msup></mrow><annotation encoding="application/x-tex">(v, v) = \|v\|^2</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8141079999999999em;"></span><span class="strut bottom" style="height:1.064108em;vertical-align:-0.25em;"></span><span class="base"><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.03588em;">v</span><span class="mpunct">,</span><span class="mord mathit" style="margin-right:0.03588em;">v</span><span class="mclose">)</span><span class="mrel">=</span><span class="mord mathrm">∥</span><span class="mord mathit" style="margin-right:0.03588em;">v</span><span class="mord"><span class="mord mathrm">∥</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">2</span></span></span></span></span></span></span></span></span></span></span></p>

#### [ Patrick Massot (Aug 01 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130741409):
<p>Sorry, I was interrupted by a phone call</p>

#### [ Patrick Massot (Aug 01 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130741454):
<p>What Mario says is why I suggested you build upon my normed space stuff</p>

#### [ Mario Carneiro (Aug 01 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130741461):
<p>(or something like it - is this a real inner product space or a more general kind?)</p>

#### [ Patrick Massot (Aug 01 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130741709):
<p>Also, try at the end of your file: </p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">(</span><span class="n">V</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">Hilbert_space</span> <span class="n">V</span><span class="o">)</span>
<span class="kn">example</span> <span class="o">:</span> <span class="n">H</span><span class="bp">.</span><span class="n">to_core</span><span class="bp">.</span><span class="n">to_topological_space</span> <span class="bp">=</span> <span class="n">uniform_space</span><span class="bp">.</span><span class="n">to_topological_space</span> <span class="n">V</span> <span class="o">:=</span> <span class="n">rfl</span>
</pre></div>


<p>seeing this fail is a bad omen</p>

#### [ Simon Hudon (Aug 01 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130741898):
<p>You're so superstitious!</p>

#### [ Kevin Buzzard (Aug 01 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130741905):
<p>This file has changed since I understood it ;-)</p>

#### [ Patrick Massot (Aug 01 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130742139):
<blockquote>
<p>you'll need that if a_n tends to zero and 0 &lt;= b_n &lt;= a_n then b_n tends to zero etc. This sort of stuff is not really mathlib's strong point at this stage.</p>
</blockquote>
<p>That one is in mathlib</p>

#### [ Patrick Massot (Aug 01 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130742165):
<p><a href="https://github.com/leanprover/mathlib/blob/29639b31a9808f601fa434aeed0f5756f040f0e8/analysis/topology/topological_structures.lean#L434" target="_blank" title="https://github.com/leanprover/mathlib/blob/29639b31a9808f601fa434aeed0f5756f040f0e8/analysis/topology/topological_structures.lean#L434">https://github.com/leanprover/mathlib/blob/29639b31a9808f601fa434aeed0f5756f040f0e8/analysis/topology/topological_structures.lean#L434</a></p>

#### [ Mario Carneiro (Aug 01 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130742168):
<p>also completeness is defined in terms of filters not sequences</p>

#### [ Andreas Swerdlow (Aug 02 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130768355):
<blockquote>
<p>Also, try at the end of your file: </p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">(</span><span class="n">V</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">Hilbert_space</span> <span class="n">V</span><span class="o">)</span>
<span class="kn">example</span> <span class="o">:</span> <span class="n">H</span><span class="bp">.</span><span class="n">to_core</span><span class="bp">.</span><span class="n">to_topological_space</span> <span class="bp">=</span> <span class="n">uniform_space</span><span class="bp">.</span><span class="n">to_topological_space</span> <span class="n">V</span> <span class="o">:=</span> <span class="n">rfl</span>
</pre></div>


<p>seeing this fail is a bad omen</p>
</blockquote>
<p>Just tried this and it fails</p>

#### [ Kevin Buzzard (Aug 02 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130768700):
<p>This sounds related to Mario's comment. We do not care one bit about the uniform space structure. Here is the actual question. Let M be a metric space. How do I make the assertion in Lean that M is complete? And the meta-question is why this isn't a darn sight easier than it is (the answer to this possibly being "it's because of diamonds and the type class inference system not really being designed for this sort of thing"). At the minute we make M an instance a class of uniform_space.core and then add an axiom that the open sets of M are equal to the open sets of the uniformity. What's the correct way to do it? Note that Andreas is a 1st year undergrad and is just doing this to learn the theory and to learn Lean, this just an educational experiment at this point rather than a project to get Hilbert spaces into mathlib.</p>

#### [ Johan Commelin (Aug 02 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130768984):
<blockquote>
<p>Note that Andreas is a 1st year undergrad and is just doing this to learn the theory and to learn Lean, this just an educational experiment at this point rather than a project to get Hilbert spaces into mathlib.</p>
</blockquote>
<p>Kudos! <span class="emoji emoji-1f419" title="octopus">:octopus:</span> Your UG's are amazing Kevin!</p>

#### [ Kevin Buzzard (Aug 02 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130769069):
<p>They're producing so much stuff that I find it difficult to keep track of it all. Every few hours I pull <a href="https://github.com/ImperialCollegeLondon/xena-UROP-2018/" target="_blank" title="https://github.com/ImperialCollegeLondon/xena-UROP-2018/">https://github.com/ImperialCollegeLondon/xena-UROP-2018/</a> and there's more stuff; it's got to the stage where there aren't enough hours in the day to look at it all. If anyone wants to review any of the code there then feel free :-)</p>

#### [ Johan Commelin (Aug 02 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130769206):
<blockquote>
<p>Excluding merges, 16 authors have pushed 84 commits to master and 83 commits to all branches. On master, 37 files have changed and there have been 5,920 additions and 1,071 deletions.  -- quote from github, insights</p>
</blockquote>
<p>That's over the last week!</p>

#### [ Joseph Corneli (Aug 02 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130771212):
<p>With latest version of the file I get an error: <code>invalid import: norm_space</code>.  Am I missing a dependency?  There's a file <code>src/inner_product_spaces/norm_spaces</code> (no <code>.lean</code>).  Renaming the file and adjusting the import line as follows, the error goes away:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">linear_algebra</span><span class="bp">.</span><span class="n">basic</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">field</span> <span class="n">inner_product_spaces</span><span class="bp">.</span><span class="n">norm_space</span> <span class="n">data</span><span class="bp">.</span><span class="n">complex</span><span class="bp">.</span><span class="n">basic</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">metric_space</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">topology</span><span class="bp">.</span><span class="n">uniform_space</span>
</pre></div>


<p><span class="user-mention" data-user-id="120943">@Andreas Swerdlow</span>  is this roughly what's intended?</p>

#### [ Kevin Buzzard (Aug 02 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130771225):
<p>Apologies for this. When I was involved yesterday afternoon it was all working fine but there have been some commits since then and I've not had the time to look at it all.</p>

#### [ Patrick Massot (Aug 02 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130771650):
<p>I also needed to modify this yesterday to get it to compile. I know this UROP thing is very free form, but maybe you could encourage commits which compile (I'm not talking about sorry, this is a different question)</p>

#### [ Andreas Swerdlow (Aug 02 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130771710):
<p><span class="user-mention" data-user-id="122022">@Joseph Corneli</span>  Yes sorry, am currently working on a version of the file that is saved on my hard drive and just copied over without thinking. That is the correct import.</p>

#### [ Joseph Corneli (Aug 02 2018 at 13:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130772322):
<p>Another small suggestion would be a doc string for the main <code>class</code> in <code>basic.lean</code>:</p>
<div class="codehilite"><pre><span></span><span class="c">/-</span><span class="cm">-</span>
<span class="cm">`herm_inner_product_space` defined such the inner product of two vectors is a value in ℂ.</span>
<span class="cm">This definition would have to be modified to work for any field of scalars.</span>
<span class="cm">-/</span>
</pre></div>

#### [ Kevin Buzzard (Aug 02 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/defining%20a%20hilbert%20space/near/130772943):
<p><span class="user-mention" data-user-id="120943">@Andreas Swerdlow</span> I have located <span class="user-mention" data-user-id="120435">@Minh Hieu Le (Kai)</span>  -- he's sitting opposite me right now :-)</p>


{% endraw %}
