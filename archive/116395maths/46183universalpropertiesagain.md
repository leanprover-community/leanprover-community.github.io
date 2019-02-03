---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/46183universalpropertiesagain.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [universal properties again](https://leanprover-community.github.io/archive/116395maths/46183universalpropertiesagain.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Jul 19 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129954498):
<p>Since everybody is doing universal properties and fight reluctant universes and type class inference, let me try to get help. Remember I'm working with Hausdorff completions of uniform space. I have a nice proof of their universal properties and I'd like to run the usual stuff on it. Especially today I need uniqueness for this construction. So I forget about my explicit construction and try to run abstract arguments. See <a href="https://gist.github.com/PatrickMassot/beb3b40bec8888b3061d9c410c229467" target="_blank" title="https://gist.github.com/PatrickMassot/beb3b40bec8888b3061d9c410c229467">https://gist.github.com/PatrickMassot/beb3b40bec8888b3061d9c410c229467</a> First trouble: I had to setup explicit universe level in order to get Lean to accept <code>compare</code>. Then the instances buried in the structure are hard to get out. I guess I'm on a completely wrong track here.</p>

#### [ Patrick Massot (Jul 19 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129955775):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I'm afraid you were busy typing some advertisement when that thread started (and stopped).</p>

#### [ Patrick Massot (Jul 19 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129955820):
<p>Do you have any hint for me?</p>

#### [ Mario Carneiro (Jul 19 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956129):
<p>What explicit universe?</p>

#### [ Patrick Massot (Jul 19 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956140):
<p>u</p>

#### [ Mario Carneiro (Jul 19 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956197):
<p>Oh yes that is true</p>

#### [ Patrick Massot (Jul 19 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956205):
<p>If I put <code>Type*</code> everywhere you see <code>Type u</code> I can shadowing errors</p>

#### [ Patrick Massot (Jul 19 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956216):
<p>Same if I try <code>Type v</code> for all beta variables</p>

#### [ Mario Carneiro (Jul 19 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956224):
<p>That's the same thing I was talking about with Kevin</p>

#### [ Mario Carneiro (Jul 19 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956242):
<p>the <code>u</code> in <code>space : Type u</code> is an internal universe variable</p>

#### [ Mario Carneiro (Jul 19 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956258):
<p>so if you make it <code>v</code> instead then you will have a bad day</p>

#### [ Mario Carneiro (Jul 19 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956295):
<p>so that means you have to explicitly make them the same, which means you need to name the variable</p>

#### [ Patrick Massot (Jul 19 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956363):
<p>same as who?</p>

#### [ Mario Carneiro (Jul 19 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956389):
<p>same as <code>α : Type u</code></p>

#### [ Patrick Massot (Jul 19 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956393):
<p>I'm having a bad day even with named u</p>

#### [ Mario Carneiro (Jul 19 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956414):
<p>At least I don't see <code>.{u}</code> anywhere in your file</p>

#### [ Mario Carneiro (Jul 19 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956427):
<p>I get an error in <code>uniform_continuous_compare</code>?</p>

#### [ Patrick Massot (Jul 19 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956433):
<p>I'm fine with α and its completion living in the same universe. That sounds nice and is actually true for my explicit construction (I think)</p>

#### [ Mario Carneiro (Jul 19 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956443):
<p>about synthesized instance different from inferred</p>

#### [ Patrick Massot (Jul 19 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956453):
<p>exactly, that's the heart of my question</p>

#### [ Patrick Massot (Jul 19 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956514):
<p>But why beta has to be in the same universe?</p>

#### [ Mario Carneiro (Jul 19 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956515):
<p>That's easy enough to fix, use <code>letI</code> instead of  <code>haveI</code></p>

#### [ Mario Carneiro (Jul 19 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956544):
<p>Better yet, add this</p>
<div class="codehilite"><pre><span></span><span class="n">attribute</span> <span class="o">[</span><span class="kn">instance</span><span class="o">]</span>
  <span class="n">completion_package</span><span class="bp">.</span><span class="n">uniform_structure</span>
  <span class="n">completion_package</span><span class="bp">.</span><span class="n">completeness</span>
  <span class="n">completion_package</span><span class="bp">.</span><span class="n">separation</span>
</pre></div>


<p>and it won't be necessary</p>

#### [ Mario Carneiro (Jul 19 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956587):
<p>beta is also an internal universe variable</p>

#### [ Patrick Massot (Jul 19 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956661):
<p>I'm sure I've seen this trick in the sheaf discussion, but I forgot. Thanks a lot</p>

#### [ Mario Carneiro (Jul 19 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956668):
<p>it doesn't <em>have</em> to be in the sense that you can define it with a different variable, but this will make your life harder and furthermore it doesn't mean what you think it means</p>

#### [ Mario Carneiro (Jul 19 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956712):
<p>It is impossible to define a field which quantifies over multiple universe levels</p>

#### [ Patrick Massot (Jul 19 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956728):
<p>I was worried I would have a lot of trouble with these instances but this trick seems to fix everything (including removing <code>@uniform_continuous</code> ugliness in the definition of <code>compare</code>)</p>

#### [ Mario Carneiro (Jul 19 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956744):
<p>that is, something like this doesn't work: <code>(lift : ∀ {u} {β : Type u} (f : α → β), space → β)</code></p>

#### [ Mario Carneiro (Jul 19 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956756):
<p>where <code>u</code> is somehow quantified inside the structure</p>

#### [ Patrick Massot (Jul 19 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956821):
<p>What do you think I thought it meant and what would it actually mean? (Grammar clearly tell us we are in the middle of a tricky discussion involving multiple universes)</p>

#### [ Patrick Massot (Jul 19 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956836):
<p>Oh, <code>(lift : ∀ {u} {β : Type u} (f : α → β), space → β)</code> is what I would have liked to mean</p>

#### [ Patrick Massot (Jul 19 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956846):
<p>But I don't mind, really</p>

#### [ Mario Carneiro (Jul 19 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956877):
<p>Luckily, in the vast majority of cases, having a lift in universe u implies a lift in higher universes too</p>

#### [ Mario Carneiro (Jul 19 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129956890):
<p>usually this is due to some zfc style size considerations</p>

#### [ Patrick Massot (Jul 19 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129957005):
<p>I certainly don't want to run into zfc size considerations. Actually I mostly want to prove that the completion of a product is nicely isomorphic to the product of the completions, taking the opportunity to try abstract non-sense in Lean</p>

#### [ Mario Carneiro (Jul 19 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129957143):
<p>I think you should just stick to universe u</p>

#### [ Mario Carneiro (Jul 19 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129957223):
<p>it's not quite as strong a theorem as you could state, but all the constructions will go through without any added headache</p>

#### [ Patrick Massot (Jul 19 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129957318):
<p>Great, I like that</p>

#### [ Patrick Massot (Jul 19 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/universal%20properties%20again/near/129957364):
<p>I'll try to move on. Thanks!</p>


{% endraw %}
