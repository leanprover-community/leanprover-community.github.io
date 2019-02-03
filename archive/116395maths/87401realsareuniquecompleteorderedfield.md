---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/87401realsareuniquecompleteorderedfield.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [reals are unique complete ordered field](https://leanprover-community.github.io/archive/116395maths/87401realsareuniquecompleteorderedfield.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Aug 09 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131159069):
<p>The reals are the unique complete ordered field up to unique isomorphism. Is this in Lean already? I thought it might be a good exercise for a student.  <span class="user-mention" data-user-id="110031">@Patrick Massot</span> does "complete" here mean "an ordered field inherits a topology from the order, and the associated uniform space is complete"? Last week I didn't know what that even meant. Is that the same as asking that any non-empty bounded set has a least upper bound? </p>
<p>I think Reid Barton once commented that because of this theorem, one should not prove theorems about the reals, one should instead prove theorems about complete ordered fields :-)</p>

#### [ Mario Carneiro (Aug 09 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131159304):
<p>I think there is a more useful way to characterize this property: <code>real.cast</code></p>

#### [ Mario Carneiro (Aug 09 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131159322):
<p>Any complete field has a unique continuous field hom from the reals</p>

#### [ Mario Carneiro (Aug 09 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131159398):
<p>Also, I think we have a good bit of the infrastructure already, since it was originally used to define functions like addition on the reals by continuous extension from rat.add</p>

#### [ Andrew Ashworth (Aug 09 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131159443):
<p>iirc Reid mentioned that because a synthetic, axiom based real number allowed his code to run much faster</p>

#### [ Mario Carneiro (Aug 09 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131159448):
<p>That's often true</p>

#### [ Mario Carneiro (Aug 09 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131159459):
<p>concrete constructions have the drawback that lean can start unfolding them</p>

#### [ Mario Carneiro (Aug 09 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131159852):
<p>Here, I'll get you started:</p>
<div class="codehilite"><pre><span></span>def real.cast {α} [topological_space α] [division_ring α] : ℝ → α :=
dense_embedding_of_rat.extend coe
</pre></div>


<p>Can you prove that this has all the same properties as <code>rat.cast</code>? What is the analogue of <code>rat.eq_cast</code>?</p>

#### [ Johan Commelin (Aug 09 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131160061):
<p>Mario, did you just write down a map from <code>real</code> to <code>rat</code>?</p>

#### [ Mario Carneiro (Aug 09 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131160072):
<p>heh, I guess I did</p>

#### [ Johan Commelin (Aug 09 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131160080):
<p>Ughh. The mathematician in me is worried, and crying, and has a huge headache. This is not a nice map, is it?</p>

#### [ Mario Carneiro (Aug 09 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131160128):
<p>It is under more assumptions</p>

#### [ Mario Carneiro (Aug 09 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131160131):
<p><code>extend_eq</code> requires that the space be t2</p>

#### [ Mario Carneiro (Aug 09 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131160137):
<p>and <code>tendsto_extend</code> needs that it is regular</p>

#### [ Mario Carneiro (Aug 09 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131160145):
<p>I guess Q is not a regular space?</p>

#### [ Johan Commelin (Aug 09 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131160151):
<p>But, to which <code>rat</code> does that map send <code>pi</code> or <code>e</code>?</p>

#### [ Johan Commelin (Aug 09 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131160163):
<p>I guess we'll never know... because of computability</p>

#### [ Mario Carneiro (Aug 09 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131160171):
<p>If the limit is not defined, it maps to an arbitrary constant in Q</p>

#### [ Johan Commelin (Aug 09 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131160229):
<p>Right, so it is the identity on rationals and maps the rest to 57 (or 37, if you ask Kevin).</p>

#### [ Mario Carneiro (Aug 09 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131160252):
<p>Actually it is <code>classical.choice (_ : nonempty Q)</code></p>

#### [ Patrick Massot (Aug 09 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131160300):
<p>Kevin: <a href="https://en.wikipedia.org/wiki/Real_number#%22The_complete_ordered_field%22" target="_blank" title="https://en.wikipedia.org/wiki/Real_number#%22The_complete_ordered_field%22">https://en.wikipedia.org/wiki/Real_number#%22The_complete_ordered_field%22</a></p>

#### [ Mario Carneiro (Aug 09 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131160330):
<p>Oh, I was wrong, you need more than just regular space for it to be defined, you need this condition</p>
<div class="codehilite"><pre><span></span>(hf : ∀b, ∃c, tendsto f (vmap e (nhds b)) (nhds c))
</pre></div>

#### [ Mario Carneiro (Aug 09 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131160388):
<p>There should be a simple assumption giving this property, but I guess you need a uniform structure</p>

#### [ Mario Carneiro (Aug 09 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131160647):
<p>if you assume <code>archimedean A</code> and <code>discrete_linear_ordered_field A</code>, then you can prove that <code>rat.cast</code> is a dense embedding by just generalizing the existing proof <code>dense_embedding_of_rat</code>, and hence define a function like <code>real.cast</code> out of <code>A</code></p>

#### [ Mario Carneiro (Aug 09 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131160661):
<p>and then you have your isomorphism</p>

#### [ Kevin Buzzard (Aug 09 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131161921):
<blockquote>
<p>Kevin: <a href="https://en.wikipedia.org/wiki/Real_number#%22The_complete_ordered_field%22" target="_blank" title="https://en.wikipedia.org/wiki/Real_number#%22The_complete_ordered_field%22">https://en.wikipedia.org/wiki/Real_number#%22The_complete_ordered_field%22</a></p>
</blockquote>
<p>Oh thanks for this Patrick! That clears this mess up!</p>

#### [ Patrick Massot (Aug 09 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131161973):
<p>Remember: if it's not formalized, you don't even know what you are talking about.</p>

#### [ Kevin Buzzard (Aug 09 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131163511):
<p>this is a fabulous example of this! I was talking to Chris about this last week and just ended up confused. I said "did you know that the reals are the unique complete ordered field?" and he replied "don't you need some archimedean property" and I said "oh yeah, what happens if you adjoin an infinitesimal?" and it was at this point that I realised I was no longer quite sure what I was talking about.</p>

#### [ Mario Carneiro (Aug 09 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131163998):
<p>what is an example of a complete nonarchimedean field?</p>

#### [ Johan Commelin (Aug 09 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164008):
<p>Q_p</p>

#### [ Mario Carneiro (Aug 09 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164014):
<p>ordered field?</p>

#### [ Johan Commelin (Aug 09 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164020):
<p>Hmmm. Don't know about those.</p>

#### [ Mario Carneiro (Aug 09 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164102):
<p>In my proof sketch, you definitely need archimedean to prove dense embedding, but I think you can use completeness to prove archimedean</p>

#### [ Johan Commelin (Aug 09 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164111):
<p>Seems reasonable</p>

#### [ Mario Carneiro (Aug 09 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164141):
<p>If completeness means dedekind-complete, then the sup of N is contradictory so you get archimedean that way</p>

#### [ Mario Carneiro (Aug 09 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164218):
<p>but if it is only complete relative to the uniformity it's not obvious to me</p>

#### [ Kevin Buzzard (Aug 09 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164262):
<p>I am in the middle of something else at the minute but I convinced myself last week that you could put an order on <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mi mathvariant="double-struck">R</mi></mrow><mo>(</mo><mi>ϵ</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">\mathbb{R}(\epsilon)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord"><span class="mord mathbb">R</span></span><span class="mopen">(</span><span class="mord mathit">ϵ</span><span class="mclose">)</span></span></span></span> with <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>ϵ</mi></mrow><annotation encoding="application/x-tex">\epsilon</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">ϵ</span></span></span></span> smaller than any positive real but greater than zero. Can one complete this, for some notion of completion?</p>

#### [ Mario Carneiro (Aug 09 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164335):
<p>wait, Q_p isn't nonarchimedean</p>

#### [ Mario Carneiro (Aug 09 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164339):
<p>it isn't ordered so the term doesn't apply</p>

#### [ Kevin Buzzard (Aug 09 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164340):
<p>It is for some definition</p>

#### [ Rob Lewis (Aug 09 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164349):
<p>It has a nonarchimedean norm.</p>

#### [ Johan Commelin (Aug 09 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164361):
<p>What the hack does "nonarchimedean" mean if even Q_p is no longer an example.... (shakes head...)</p>

#### [ Kevin Buzzard (Aug 09 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164364):
<p>I have a book called "nonarchimedean analysis" which defines a nonarchimedean field to be a field complete with respect to a non-trivial nonarchimedean norm.</p>

#### [ Kevin Buzzard (Aug 09 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164399):
<p>and a nonarchimedean norm is a function from the field to the non-negative reals satisfying F(x)=0 iff x=0, F(xy)=F(x)F(y) and F(x+y)&lt;=max(F(x),F(y))</p>

#### [ Kevin Buzzard (Aug 09 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164418):
<p>and non-trivial means "not the one with F(x)=1 for x non-zero and F(0)=0"</p>

#### [ Kevin Buzzard (Aug 09 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164493):
<p>and complete in this context means the underlying metric space is complete with d(x,y)=F(x-y)</p>

#### [ Mario Carneiro (Aug 09 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164500):
<p>what does an archimedean norm have to do with the archimedean property? the definitions look completely different</p>

#### [ Kevin Buzzard (Aug 09 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164538):
<p>Oh sorry, I defined a nonarchimedean norm above, I'll edit</p>

#### [ Mario Carneiro (Aug 09 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164570):
<p>wiki says a nonarchimedean norm is one that defines an ultrametric, but I don't see what that has to do with 1+1+1+...</p>

#### [ Kevin Buzzard (Aug 09 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164613):
<p>A norm is F as above but with F(x+y)&lt;=max(F(x),F(y)) weakened to F(x+y)&lt;=F(x)+F(y)</p>

#### [ Kevin Buzzard (Aug 09 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164623):
<p>and a norm is defined to be archimedean if it is not nonarchimedean (seriously)</p>

#### [ Kevin Buzzard (Aug 09 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164666):
<p>I think the two uses of archimedean are unfortunate, and are probably just related to the fact that the reals satisfies both properties</p>

#### [ Kevin Buzzard (Aug 09 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164681):
<p>As Patrick says, if you haven't formalised it, you don't know what you're talking about</p>

#### [ Mario Carneiro (Aug 09 2018 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164726):
<p>I want to call that an ultranorm, it makes more sense</p>

#### [ Kevin Buzzard (Aug 09 2018 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164750):
<p>What would you like my book to be called?</p>

#### [ Mario Carneiro (Aug 09 2018 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164768):
<p>ultra analysis?</p>

#### [ Kevin Buzzard (Aug 09 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164786):
<p>I think it would have sold more copies with that title</p>

#### [ Kevin Buzzard (Aug 09 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164797):
<p>Bosch--Guentzer--Remmert</p>

#### [ Kevin Buzzard (Aug 09 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164810):
<p>It's a classic. I read it from cover to cover.</p>

#### [ Mario Carneiro (Aug 09 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164887):
<p>anyway, which of these archimedeans is the one we care about?</p>

#### [ Johan Commelin (Aug 09 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164899):
<p>Number theorists care about the normy version.</p>

#### [ Mario Carneiro (Aug 09 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164905):
<p>I mean for uniqueness of R</p>

#### [ Kevin Buzzard (Aug 09 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131164993):
<p>Did you see Patrick's Wikipedia link? That says something about the confusion. But the definition of an archimedean norm is, I believe, nothing to do with the uniqueness statement about the reals.</p>

#### [ Kevin Buzzard (Aug 09 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131165049):
<p>The only role I've ever seen that "archimedean = not non-archimedean" definition play is when classifying all norms on number fields. I am honestly not sure it's used anywhere else.</p>

#### [ Kevin Buzzard (Aug 09 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131165097):
<p>Maybe in Cassels' "Local Fields" there'a a section on archimedean norms, and it might even say that every field with an archimedean norm is a subfield of the complexes or something.</p>

#### [ Kevin Buzzard (Aug 09 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131165135):
<p>I forget the lemma. Certainly the theorem is that the archimedean norms on a number field are all induced from embeddings into the complexes (modulo some equivalence relation on norms which is "induced metrics define the same topology")</p>

#### [ Mario Carneiro (Aug 09 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131165193):
<p>wait, so does R have any uniqueness property that does not reference the order?</p>

#### [ Kevin Buzzard (Aug 09 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131165327):
<p>The complexes are the unique algebraically closed field of characteristic zero and cardinality 2^aleph_0 (proof: transcendence basic; probably I'm assuming AC here). If you take an element of order 2 in Aut(complexes) then its fixed points are a field which I think is not in general isomorphic to the reals but which is quite difficult to tell apart from the reals if you don't think about the ordering.</p>

#### [ Kevin Buzzard (Aug 09 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131165373):
<p>Hmm, maybe the fixed points do even have an ordering, perhaps it's this unboundedness of 1+1+1+... which fails in these general fields (are they called "real closed fields"?)</p>

#### [ Mario Carneiro (Aug 09 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131165374):
<p>If you allow the topology, you should be able to get R exactly, right?</p>

#### [ Mario Carneiro (Aug 09 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131165377):
<p>there is only one nontrivial continuous automorphism of C</p>

#### [ Kevin Buzzard (Aug 09 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131165378):
<p>right</p>

#### [ Kevin Buzzard (Aug 09 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131165386):
<p>but I defined it as an abstract field</p>

#### [ Kevin Buzzard (Aug 09 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131165389):
<p>Take Q, adjoin 2^aleph_0 independent transcendental elements, and then take the alg closure</p>

#### [ Kevin Buzzard (Aug 09 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131165390):
<p>This proves that C is isomorphic to an algebraic closure of Q_p</p>

#### [ Kevin Buzzard (Aug 09 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131165440):
<p>and an algebraic closure of Q_p has a non-archimedean norm on it, which makes it a metric space, and this metric space is not complete, and if you complete it then you get something called C_p, which by the same argument is also isomorphic to C</p>

#### [ Mario Carneiro (Aug 09 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131165448):
<p>isomorphic as fields?</p>

#### [ Kevin Buzzard (Aug 09 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131165450):
<p>So there's lots of different topologies on C</p>

#### [ Johan Commelin (Aug 09 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131165456):
<blockquote>
<p>isomorphic as fields?</p>
</blockquote>
<p>yes</p>

#### [ Kevin Buzzard (Aug 09 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131165457):
<p>Yes, any two alg closed fields of char 0 and cardinality 2^aleph_0 are isomorphic</p>

#### [ Mario Carneiro (Aug 09 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131165463):
<p>but if you want to capture "complete" from the original statement, you want a topological field structure</p>

#### [ Kevin Buzzard (Aug 09 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131165465):
<p>Proof is "take a transcendence basis over Q, check it has size 2^aleph_0, hence your field must be iso to an alg closure of Q(X_i:i in reals)</p>

#### [ Kevin Buzzard (Aug 09 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131165522):
<p>So if c is a random automorphism of order 2 of (alg closure of Q(X_i : i in reals)) then I think you can define an order on the fixed subfield, by x &gt; 0 iff x is a non-zero square</p>

#### [ Kevin Buzzard (Aug 09 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131165562):
<p>but before I say too much more I should look at the Wikipedia article on real closed fields and I'm trying to read a student's work on homotopy theory :-/</p>

#### [ Johan Commelin (Aug 09 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131165970):
<p>I think <em>real closed fields</em> would be a really cool topic to formalise as well.</p>

#### [ Johan Commelin (Aug 09 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131165972):
<p>There is lots of interesting logic there.</p>

#### [ Johan Commelin (Aug 09 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131166026):
<p>Quantifier elimination. Semialgebraic sets. <a href="https://en.wikipedia.org/wiki/Cylindrical_algebraic_decomposition" target="_blank" title="https://en.wikipedia.org/wiki/Cylindrical_algebraic_decomposition">https://en.wikipedia.org/wiki/Cylindrical_algebraic_decomposition</a></p>

#### [ Johan Commelin (Aug 09 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131166039):
<p>Anyway, I'm derailing this topic.</p>

#### [ Kenny Lau (Aug 09 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131171804):
<p>there is an order on Q_p</p>

#### [ Kenny Lau (Aug 09 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reals%20are%20unique%20complete%20ordered%20field/near/131171889):
<p>wait the order isn't compatible with the ring structure</p>


{% endraw %}
