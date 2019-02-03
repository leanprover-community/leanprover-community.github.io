---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/88527idempotentconstructionsanduniverses.html
---

## Stream: [general](index.html)
### Topic: [idempotent constructions and universes](88527idempotentconstructionsanduniverses.html)

---


{% raw %}
#### [ Johan Commelin (Oct 12 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135671325):
<p>I think there might be general theory behind this. I will just start with an example:<br>
There is this thing called a <em>topos</em>. It shows up in geometry, topology, and also logic. It is the natural category theoretic places where a <em>sheaf</em> lives. If you have a topological space <code>X</code>, you can form <code>Sh(X)</code>: the category of all sheaves on <code>X</code>. This is the prototypical example of a topos. It turns out that topological spaces are to restrictive, we need to categorify them, what you get is <em>sites</em>: a category <code>C</code> together with a <em>Grothendieck topology</em> on <code>C</code>. Every Grothendieck topos is (by definition) the category of sheaves on some site.<br>
Now here is a cool thing: every topos can be equipped with a <em>canonical topology</em>. This means that we can talk about sheaves on a topos. In particular we can form <code>Sh(Sh(X))</code>.<br>
It turns out that you don't get anything new if you do this. Except, there is a catch, your universe levels increase. Mathematicians fight their way around this by fixing some <code>κ</code> and looking at the topos of <code>κ</code>-small sheaves, so that they can stay in the same universe, etc... I am afraid that we cannot escape this issue. (This has nothing to do with willing to work with universes or not. We just <em>really</em> don't want "idempotent" operations to bump up universe levels.)<br>
In Lean we have the notion of <code>fintype</code>. Is it easy to speak about <code>ĸ</code>-small types? Is there a good systematic way to attack problems like this?<br>
Related places where this shows up:<br>
- algebraic closures<br>
- valuation spectrum (to make this "idempotent" you probably have to take the ring of functions on <code>Spv</code>)</p>

#### [ Reid Barton (Oct 12 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135673434):
<p>Locally presentable categories are a related idea (and a Grothendieck topos is in particular a locally presentable category). A locally <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>κ</mi></mrow><annotation encoding="application/x-tex">\kappa</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">κ</span></span></span></span>-presentable category <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>C</mi></mrow><annotation encoding="application/x-tex">C</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.07153em;">C</span></span></span></span> is (among other characterizations) the category of those presheaves on a (small) category <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>A</mi></mrow><annotation encoding="application/x-tex">A</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">A</span></span></span></span> which take a designated collection of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>κ</mi></mrow><annotation encoding="application/x-tex">\kappa</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">κ</span></span></span></span>-small cocones in <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>A</mi></mrow><annotation encoding="application/x-tex">A</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">A</span></span></span></span> to limit cones in Set. Then it turns out that we can take <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>A</mi></mrow><annotation encoding="application/x-tex">A</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">A</span></span></span></span> to be <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>C</mi><mi>κ</mi></msub></mrow><annotation encoding="application/x-tex">C_\kappa</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.83333em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.07153em;">C</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.151392em;"><span style="top:-2.5500000000000003em;margin-left:-0.07153em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">κ</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span>, the full subcategory of all <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>κ</mi></mrow><annotation encoding="application/x-tex">\kappa</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">κ</span></span></span></span>-presentable objects of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>C</mi></mrow><annotation encoding="application/x-tex">C</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.07153em;">C</span></span></span></span>, at least after replacing this by an equivalent small category, together with the collection of all <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>κ</mi></mrow><annotation encoding="application/x-tex">\kappa</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">κ</span></span></span></span>-small colimits in <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>C</mi><mi>κ</mi></msub></mrow><annotation encoding="application/x-tex">C_\kappa</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.83333em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.07153em;">C</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.151392em;"><span style="top:-2.5500000000000003em;margin-left:-0.07153em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">κ</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span>.</p>

#### [ Johan Commelin (Oct 12 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135673511):
<p>And you are Leanifying this kind of stuff, right?</p>

#### [ Reid Barton (Oct 12 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135673531):
<p>My intention is just to formalize <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>κ</mi></mrow><annotation encoding="application/x-tex">\kappa</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">κ</span></span></span></span>-smallness as</p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">κ</span> <span class="o">:</span> <span class="n">cardinal</span><span class="bp">.</span><span class="o">{</span><span class="n">u</span><span class="o">})</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">cardinal</span><span class="bp">.</span><span class="n">mk</span> <span class="n">α</span> <span class="bp">&lt;</span> <span class="n">κ</span><span class="o">)</span>
</pre></div>

#### [ Reid Barton (Oct 12 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135673583):
<p>and it seems to be working okay, for example, I mostly proved that <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>κ</mi></mrow><annotation encoding="application/x-tex">\kappa</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">κ</span></span></span></span>-filtered colimits can be reduced to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>κ</mi></mrow><annotation encoding="application/x-tex">\kappa</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">κ</span></span></span></span>-directed colimits, which involves a somewhat complicated construction and a bunch of simple cardinality estimates</p>

#### [ Johan Commelin (Oct 12 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135673777):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> But do you also have code to turn this into categories that don't increase the universe level?</p>

#### [ Johan Commelin (Oct 12 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135673791):
<p>Or is this what you mean with "after replacing this by an equivalent small category"?</p>

#### [ Reid Barton (Oct 12 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135673978):
<p>Right, good question. I haven't gotten that far yet but at some point the question will be how to replace something which we know as mathematicians is small or essentially small (like the collection of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>κ</mi></mrow><annotation encoding="application/x-tex">\kappa</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">κ</span></span></span></span>-presentable objects) with something which actually lives in the original universe <code>u</code></p>

#### [ Reid Barton (Oct 12 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135674004):
<p>Let me try to think what the simplest example of such a question is</p>

#### [ Johan Commelin (Oct 12 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135674120):
<p>Right, I think you just rephrased in 3 lines what took me about 30 lines <span class="emoji emoji-1f643" title="upside down">:upside_down:</span>  <span class="emoji emoji-1f44d" title="thumbs up">:thumbs_up:</span></p>

#### [ Reid Barton (Oct 12 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135674180):
<p>I guess a typical example is: given a category C, show there is only a <code>Type u</code> of isomorphism classes of diagrams K -&gt; C where K is <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>κ</mi></mrow><annotation encoding="application/x-tex">\kappa</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">κ</span></span></span></span>-small and whose image belongs to a specified <em>set</em> (i.e., another <code>Type u</code>) of objects of C.</p>

#### [ Reid Barton (Oct 12 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135674215):
<p>The obvious attempt <code>structure my_thing := (K : Type u) [small_category K] (F : functor K C) ...</code> fails immediately because we cannot put a <code>Type u</code> in there</p>

#### [ Reid Barton (Oct 12 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135674238):
<p>This isn't the simplest example but I think it has most of the interesting ingredients.</p>

#### [ Reid Barton (Oct 12 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135674371):
<p>Simpler examples would be things like: prove there is only a set of isomorphism classes of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>κ</mi></mrow><annotation encoding="application/x-tex">\kappa</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">κ</span></span></span></span>-small categories K, or even prove that there is only a set of isomorphism classes of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>κ</mi></mrow><annotation encoding="application/x-tex">\kappa</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">κ</span></span></span></span>-small sets.</p>

#### [ Johan Commelin (Oct 12 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135674447):
<p>Prove that there is only a set of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>κ</mi></mrow><annotation encoding="application/x-tex">\kappa</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">κ</span></span></span></span>-small algebraic field extensions.</p>

#### [ Johan Commelin (Oct 12 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135674476):
<p>If I understand it correctly, you can just define <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mover accent="true"><mi>K</mi><mo>¯</mo></mover></mrow><annotation encoding="application/x-tex">\bar K</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8201099999999999em;"></span><span class="strut bottom" style="height:0.8201099999999999em;vertical-align:0em;"></span><span class="base"><span class="mord accent"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8201099999999999em;"><span style="top:-3em;"><span class="pstrut" style="height:3em;"></span><span class="mord mathit" style="margin-right:0.07153em;">K</span></span><span style="top:-3.25233em;"><span class="pstrut" style="height:3em;"></span><span class="accent-body" style="margin-left:0.11112em;"><span>¯</span></span></span></span></span></span></span></span></span></span> with Zorn, after you know that fact.</p>

#### [ Johan Commelin (Oct 12 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135674494):
<p>And it won't have to live in a higher universe.</p>

#### [ Reid Barton (Oct 12 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135674536):
<p>But I think we want some kind of general method or bag of tricks for building these up, rather than just doing them all as one-off constructions. But that probably begins by doing the simplest cases as one-off constructions</p>

#### [ Johan Commelin (Oct 12 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135674588):
<p>Right... that's the kind of thing I'dd like to find out in this thread.</p>

#### [ Reid Barton (Oct 12 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135675036):
<p>Okay so let's break your claim down in mind-numbing detail. There is a category of field extensions of K, which I guess is relevant because the conclusion is "every [...] field extension of K is isomorphic [over K] to one selected from [some type]".</p>

#### [ Reid Barton (Oct 12 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135675075):
<p>It has a forgetful functor to Set. We're interested in the field extensions whose underlying set is <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>κ</mi></mrow><annotation encoding="application/x-tex">\kappa</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">κ</span></span></span></span>-small and which satisfy some other property (algebraic over K) whose details don't matter here I think.</p>

#### [ Johan Commelin (Oct 12 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135675137):
<p>Well, algebraic implies <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>κ</mi></mrow><annotation encoding="application/x-tex">\kappa</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">κ</span></span></span></span>-small.</p>

#### [ Johan Commelin (Oct 12 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135675164):
<p>If <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>κ</mi></mrow><annotation encoding="application/x-tex">\kappa</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">κ</span></span></span></span> is bigger than the cardinality of the ground field.</p>

#### [ Reid Barton (Oct 12 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135675186):
<p>I guess we should say a category C is essentially small when there's an equivalence D -&gt; C with <code>D : Type u</code> a small category</p>

#### [ Reid Barton (Oct 12 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135675201):
<p>Oh true, but then the rest of the argument goes through the fact that the extensions we care about are <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>κ</mi></mrow><annotation encoding="application/x-tex">\kappa</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">κ</span></span></span></span>-small, right?</p>

#### [ Johan Commelin (Oct 12 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135675251):
<p>Yes</p>

#### [ Reid Barton (Oct 12 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135675292):
<p>So, the subcategory of Set on the <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>κ</mi></mrow><annotation encoding="application/x-tex">\kappa</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">κ</span></span></span></span>-small sets is essentially small. This must be some primitive ingredient because it is tied closely to the notion of cardinality</p>

#### [ Reid Barton (Oct 12 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135675298):
<p>and surely we can just prove it directly</p>

#### [ Reid Barton (Oct 12 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135675343):
<p>Then, we want to argue like: a set can only be made into a field in a set's worth of ways</p>

#### [ Reid Barton (Oct 12 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135675359):
<p>that is just the statement that <code>discrete_field</code> has type <code>Type u -&gt; Type u</code>, I guess</p>

#### [ Reid Barton (Oct 12 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135675387):
<p>Or here, you could just substitute <code>algebraic_extension_of k : Type u -&gt; Type u</code> and then be done with the whole argument at the end of this step.</p>

#### [ Reid Barton (Oct 12 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135675565):
<p>So I suppose the missing piece is something like: if F : C' -&gt; C is a functor and the fibers of F.obj are small then the preimage of an essentially small subcategory of C is an essentially small subcategory of C'</p>

#### [ Reid Barton (Oct 12 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135675582):
<p>Well, I didn't state that quite right (that statement is false)</p>

#### [ Reid Barton (Oct 12 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135675615):
<p>for this F also needs to be an isofibration, i.e. if FX' = X and X -&gt; Y is an isomorphism in C then it lifts to at least one isomorphism X' -&gt; Y' in C'</p>

#### [ Reid Barton (Oct 12 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135675691):
<p>(aka "transport of structure")</p>

#### [ Reid Barton (Oct 12 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135675886):
<p>I guess I never thought about the fact that this is required. But I think it really is. After all, you <em>could</em> define a field extension of K in the same way but then say that the only maps between field extensions are identity maps (not even isomorphisms) and then even though there is only a set of ways to equip each set with a field extension structure, it's no longer true that every <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>κ</mi></mrow><annotation encoding="application/x-tex">\kappa</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">κ</span></span></span></span>-small field extension is isomorphic to one from a set of representatives.</p>

#### [ Reid Barton (Oct 12 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135676375):
<p>I think what's going on here is:<br>
1. The pullback of an equivalence D -&gt; C by an isofibration C' -&gt; C is an equivalence D' -&gt; C'. ("The canonical model category structure on Cat is right proper.")<br>
2. We can choose the pullback D' here to belong to Type u. This isn't a general fact about pullbacks because C' belongs to Type (u+1). Instead it is some statement about the way pullbacks interact with <code>bundled</code> categories.</p>

#### [ Johan Commelin (Oct 12 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135677129):
<p>Right. This is looking good. The only problem is that it will take some time to convince Lean of this <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Reid Barton (Oct 12 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135677326):
<p>So I suppose we can hide all the category theory language maybe.</p>

#### [ Reid Barton (Oct 12 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135677428):
<p>For each cardinal <code>k : cardinal.{u}</code>, there's a type <code>R k : Type u</code> and a function <code>U : R k -&gt; Type u</code> with the property that every type of cardinality &lt; k is <code>equiv</code> to <code>U r</code> for some <code>r : R k</code>. (<code>R k</code> = representatives of isomorphism classes of sets of size &lt; k.) In fact, <code>R k</code> is just <code>k.out</code> or something.</p>

#### [ Johan Commelin (Oct 12 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135677528):
<p>Right. Did you just reduce the problem to "transport of structure"?</p>

#### [ Reid Barton (Oct 12 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135677544):
<p>Then we can define a new structure</p>
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">kappa_small_algebraic_extension</span> <span class="o">(</span><span class="n">K</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">discrete_field</span> <span class="n">K</span><span class="o">]</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">R</span> <span class="n">k</span><span class="o">)</span>
<span class="o">(</span><span class="n">str</span> <span class="o">:</span> <span class="n">algebraic_extension_of</span> <span class="n">K</span> <span class="o">(</span><span class="n">U</span> <span class="n">r</span><span class="o">))</span>
</pre></div>

#### [ Reid Barton (Oct 12 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135677609):
<p>and we will need transport of structure to show that every <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>κ</mi></mrow><annotation encoding="application/x-tex">\kappa</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">κ</span></span></span></span>-small algebraic extension is "isomorphic" to one that comes from <code>kappa_small_algebraic_extension</code>, yes</p>

#### [ Reid Barton (Oct 12 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135677620):
<p>but then the point is that <code>kappa_small_algebraic_extension K</code> is also a <code>Type u</code></p>

#### [ Johan Commelin (Oct 12 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135677629):
<p>Exactly. That is really nice.</p>

#### [ Johan Commelin (Oct 12 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135677651):
<p>This would allow us to do universe resizing (is this what it is called) for the valuation spectrum, for algebraic closures, etc...</p>

#### [ Johan Commelin (Oct 12 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135677704):
<p>We probably still want "constructions" in the end. But it is nice to also have this option available.</p>

#### [ Johan Commelin (Oct 12 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135677731):
<p>And in the case of topoi, I think this is maybe the only option.</p>

#### [ Reid Barton (Oct 12 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135678808):
<p>Maybe we should try to actually prove the existence of algebraic closures modulo whatever field theory results we need (a composition of algebraic extensions is algebraic?)</p>

#### [ Johan Commelin (Oct 12 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135679028):
<p>Kenny already did some of that stuff in his LL repo</p>

#### [ Kevin Buzzard (Oct 12 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135695603):
<p>Polynomials are currently quite hard to work with because module refactoring hasn't landed yet.</p>

#### [ Reid Barton (Oct 12 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135696715):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> I'm actually not sure exactly what proof you had in mind for which you need to know that there is only a set of isomorphism classes of algebraic extensions of K.</p>

#### [ Reid Barton (Oct 12 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135696795):
<p>To apply Zorn's lemma you need a poset, but the collection of algebraic extensions of K only forms a filtered diagram because there will typically be several embeddings <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>F</mi><mo>→</mo><mi>E</mi></mrow><annotation encoding="application/x-tex">F \to E</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="mrel">→</span><span class="mord mathit" style="margin-right:0.05764em;">E</span></span></span></span> between two extensions <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>F</mi></mrow><annotation encoding="application/x-tex">F</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.13889em;">F</span></span></span></span> and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>E</mi></mrow><annotation encoding="application/x-tex">E</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.05764em;">E</span></span></span></span>.</p>

#### [ Reid Barton (Oct 12 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135696807):
<p>Actually it's not even filtered, I guess</p>

#### [ Reid Barton (Oct 12 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135696994):
<p><a href="http://www2.im.uj.edu.pl/actamath/PDF/30-131-132.pdf" target="_blank" title="http://www2.im.uj.edu.pl/actamath/PDF/30-131-132.pdf">http://www2.im.uj.edu.pl/actamath/PDF/30-131-132.pdf</a> has a proof which is the kind of thing I was imagining, but it looks at fields whose underlying set is a subset of some fixed set <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>S</mi></mrow><annotation encoding="application/x-tex">S</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.05764em;">S</span></span></span></span> containing <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>K</mi></mrow><annotation encoding="application/x-tex">K</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.07153em;">K</span></span></span></span>, so that there is a partial order defined by inclusion. (Actually the collection <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mi mathvariant="script">R</mi></mrow></mrow><annotation encoding="application/x-tex">\mathcal{R}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathcal">R</span></span></span></span></span> defined there makes no sense as defined, since a subset <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>L</mi></mrow><annotation encoding="application/x-tex">L</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">L</span></span></span></span> of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>S</mi></mrow><annotation encoding="application/x-tex">S</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.05764em;">S</span></span></span></span> is not a field, but it can be fixed by considering pairs of a subset and a field structure on the subset, and defining the poset relation so that <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>L</mi><mo>≤</mo><msup><mi>L</mi><mo mathvariant="normal">′</mo></msup></mrow><annotation encoding="application/x-tex">L \le L'</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.751892em;"></span><span class="strut bottom" style="height:0.887862em;vertical-align:-0.13597em;"></span><span class="base"><span class="mord mathit">L</span><span class="mrel">≤</span><span class="mord"><span class="mord mathit">L</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span></span></span></span> if <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>L</mi><mo>⊂</mo><msup><mi>L</mi><mo mathvariant="normal">′</mo></msup></mrow><annotation encoding="application/x-tex">L \subset L'</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.751892em;"></span><span class="strut bottom" style="height:0.790992em;vertical-align:-0.0391em;"></span><span class="base"><span class="mord mathit">L</span><span class="mrel">⊂</span><span class="mord"><span class="mord mathit">L</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span></span></span></span> and the inclusion is a field extension.)</p>

#### [ Reid Barton (Oct 12 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135697233):
<p><a href="http://www.cs.bsu.edu/~hfischer/math412/Closure.pdf" target="_blank" title="http://www.cs.bsu.edu/~hfischer/math412/Closure.pdf">http://www.cs.bsu.edu/~hfischer/math412/Closure.pdf</a> seems to be a rather more careful version of the same proof</p>

#### [ Kenny Lau (Oct 12 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135697336):
<p>a construction that needs to deal with set-theoretic issues would be very ugly if implemented, I think.</p>

#### [ Kenny Lau (Oct 12 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135697340):
<p>it wouldn't be natural.</p>

#### [ Mario Carneiro (Oct 12 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135697437):
<p>I've talked here before about alternatives to cardinal bounds. The key is to find a set (type) that indexes all the relevant objects up to isomorphism</p>

#### [ Kenny Lau (Oct 12 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135697497):
<p>I'm talking about the added difficulty and unnaturality when proving the universal properties</p>

#### [ Mario Carneiro (Oct 12 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135697504):
<p>These things are usually best done on a case by case basis though, which complicates matters</p>

#### [ Mario Carneiro (Oct 12 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135697532):
<p>Unfortunately, there's nothing that can be done about this Kenny. The perfect system would allow you to just write down these types over an impredicative universe so you get the right universal property, but that's inconsistent</p>

#### [ Mario Carneiro (Oct 12 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135697597):
<p>The fact that in some particular case you can do it without an impredicative universe is a nontrivial fact that must be proved</p>

#### [ Kenny Lau (Oct 12 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135697603):
<p>of course there's something that can be done. That isn't the only construction of algebraic closure. The one that I know has no universe issues.</p>

#### [ Mario Carneiro (Oct 12 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135697621):
<p>The key is picking the right indexing type, like I said</p>

#### [ Mario Carneiro (Oct 12 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135697630):
<p>if you do it right you don't have universe issues</p>

#### [ Mario Carneiro (Oct 12 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135697785):
<p>Kenny what is your proof of existence of algebraic closure?</p>

#### [ Reid Barton (Oct 12 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135697844):
<p>There's another one where you sort of adjoin roots of all polynomials at once and then use the existence of maximal ideals to form a quotient which is a field</p>

#### [ Kevin Buzzard (Oct 12 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135697905):
<p>Kenny has thought about algebraic closure quite a bit and I'd be interested to hear his response. He did embark upon a construction some weeks ago but had problems using polynomials. I cannot remember the specific issue but I think that we got confirmation from Mario that the issues would be fixed by the module refactoring.</p>

#### [ Kevin Buzzard (Oct 12 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135697949):
<p>I am pretty sure that Kenny was going to adjoin all polynomials at once and use the existence of maximal ideals. However there is then the issue that this new field L is only guaranteed to contain all roots of polynomials with coefficients in the original field K.</p>

#### [ Mario Carneiro (Oct 12 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135697951):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> So is the idea that every element of the algebraic closure is expressible as a root of some polynomial over the base field?</p>

#### [ Reid Barton (Oct 12 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135697952):
<p>Yes, I read some notes by someone with the initials "KMB" about this</p>

#### [ Kevin Buzzard (Oct 12 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135697957):
<p>There are then two ways of proceeding. One is to iterate this construction countably infinitely often and to take a direct limit</p>

#### [ Kevin Buzzard (Oct 12 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698001):
<p>and the other is to work harder and prove that L is algebraically closed anyway.</p>

#### [ Kevin Buzzard (Oct 12 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698014):
<p>But the natural way of doing the latter is I guess via the theory of integral closures.</p>

#### [ Mario Carneiro (Oct 12 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698018):
<p>I would be inclined to go for the "work harder" route</p>

#### [ Mario Carneiro (Oct 12 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698025):
<p>since it keeps the complexity of the object itself down</p>

#### [ Kenny Lau (Oct 12 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698026):
<p>me too</p>

#### [ Kevin Buzzard (Oct 12 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698030):
<p>[and for integral closures you need Hilbert basis and for that you need the module refactoring]</p>

#### [ Kenny Lau (Oct 12 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698055):
<p>I need this big lemma that for any polynomial f, there is a separable polynomial h and integer n such that f(x) = h(x^(p^n)), where p is the characteristic of the field (p=1 for Q)</p>

#### [ Kevin Buzzard (Oct 12 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698110):
<p>Now you are talking about separable closure maybe?</p>

#### [ Kenny Lau (Oct 12 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698122):
<p>no...</p>

#### [ Kenny Lau (Oct 12 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698132):
<p>the proof that L is algebraically closed anyway is to consider M the maximally purely inseparable subextension</p>

#### [ Mario Carneiro (Oct 12 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698144):
<p>wait so Q is characteristic 1 now?</p>

#### [ Kevin Buzzard (Oct 12 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698146):
<p>The advantage of doing separable closure would be that you could then state the abelian local Langlands conjectures in full and correct generality.</p>

#### [ Kenny Lau (Oct 12 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698156):
<p>and show that every polynomial f in M still has a root in L (by considering f^(p^n) for a large n and observing that (x+y)^p = x^p+y^p so eventually you get a polynomial f^(p^n) in K which has a root in L by construction)</p>

#### [ Kenny Lau (Oct 12 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698245):
<p>and then show that every polynomial f in M splits in L, which requires Primitive Element Theorem</p>

#### [ Kevin Buzzard (Oct 12 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698273):
<p>What is wrong with the proof I'm about to sketch for the fact that L is alg closed.</p>

#### [ Kevin Buzzard (Oct 12 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698387):
<p>Say M/L is a finite field extension. Say degree &gt; 1 for a contradiction. Choose m in M not L. Consider the min poly p(x) of m. Its coefficients generate a finite extension K' of K. Now K'(m) is a finite extension of K, so m has a min poly over K. But we already added the roots of all the polys with coefficients in K.</p>

#### [ Kenny Lau (Oct 12 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698441):
<p>I only added one root</p>

#### [ Kevin Buzzard (Oct 12 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698449):
<p>Is this a serious issue?</p>

#### [ Kevin Buzzard (Oct 12 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698466):
<p>I see what you mean though.</p>

#### [ Kenny Lau (Oct 12 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698503):
<p>also I can shorten "Say M/L is a finite field extension. Say degree &gt; 1 for a contradiction. Choose m in M not L. Consider the min poly p(x) of m" to "consider an irred. poly. p in L[X]"</p>

#### [ Kevin Buzzard (Oct 12 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698564):
<p>Yes, I was just spelling it out because your comment made me wonder where my mistake was.</p>

#### [ Kevin Buzzard (Oct 12 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698569):
<p>So we are reduced to showing that L is normal or something like that?</p>

#### [ Kenny Lau (Oct 12 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698606):
<p>I still don't see why K'(m) is a finite extension of K</p>

#### [ Kevin Buzzard (Oct 12 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698674):
<p>oh that's just because K'/K was generated by finitely many elements of L over K and L/K is algebraic.</p>

#### [ Kenny Lau (Oct 12 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698692):
<p>ok</p>

#### [ Kevin Buzzard (Oct 12 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698695):
<p>Do you need the theory of integral extensions here? Sum of two elements integral over K is integral over K?</p>

#### [ Kevin Buzzard (Oct 12 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idempotent%20constructions%20and%20universes/near/135698778):
<p>Honestly this code should be waiting until after the module refactoring :-/</p>


{% endraw %}
