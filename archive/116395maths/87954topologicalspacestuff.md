---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/87954topologicalspacestuff.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [topological space stuff](https://leanprover-community.github.io/archive/116395maths/87954topologicalspacestuff.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (May 12 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20stuff/near/126462782):
<p>I need some standard topological space arguments. Do we have homeomorphisms and/or open immersions in mathlib yet, and if not then where should I put them? Should a homeomorphism be an equiv or a bijection? (i.e. should I demand a map in the other direction?). I need that something homeomorphic to a compact space is compact -- another thing which a mathematician would not need to supply a proof of because "it's obvious".</p>

#### [ Mario Carneiro (May 12 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20stuff/near/126463028):
<p>I think Patrick has a definition of <code>homeo</code>. It extended <code>equiv</code></p>

#### [ Mario Carneiro (May 12 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20stuff/near/126463040):
<p>of course homeos are isos in the category of top spaces so you are going to find many of the same parametricity things there as with your group iso stuff</p>

#### [ Patrick Massot (May 12 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20stuff/near/126464136):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> See <a href="https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/homeos.lean" target="_blank" title="https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/homeos.lean">https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/homeos.lean</a></p>

#### [ Patrick Massot (May 12 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20stuff/near/126464137):
<p>It's focused on the group structure on self-homeomorphisms</p>

#### [ Patrick Massot (May 12 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20stuff/near/126464138):
<p>But mathlib has induced topologies</p>

#### [ Patrick Massot (May 12 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20stuff/near/126464184):
<p>So I would try to prove that an equiv is a homeo iff both maps induce the same topology on their source as the original one</p>

#### [ Patrick Massot (May 12 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20stuff/near/126464187):
<p>and then deduce something homeo to a compact space is compact</p>

#### [ Reid Barton (May 12 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20stuff/near/126465041):
<p>I have a proof of <code>compact s ↔ compact (univ : set (subtype s))</code> lying around if you need that</p>

#### [ Kevin Buzzard (May 12 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20stuff/near/126467384):
<p>Does <code>open_immersion</code> go in the root namespace?</p>

#### [ Reid Barton (May 12 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20stuff/near/126467549):
<p>actually, I basically proved that something homeomorphic to a compact space is compact along the way</p>

#### [ Reid Barton (May 12 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20stuff/near/126467553):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">compact2</span> <span class="o">[</span><span class="n">tβ</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">β</span><span class="o">]</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">}</span> <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">β</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span><span class="n">y</span><span class="err">∈</span><span class="n">s</span><span class="o">,</span> <span class="bp">∃</span><span class="n">x</span><span class="o">,</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">compact</span> <span class="n">s</span> <span class="bp">→</span> <span class="bp">@</span><span class="n">compact</span> <span class="n">α</span> <span class="o">(</span><span class="n">induced</span> <span class="n">f</span> <span class="n">tβ</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="bp">⁻¹</span><span class="err">&#39;</span> <span class="n">s</span><span class="o">)</span> <span class="o">:=</span>
</pre></div>

#### [ Reid Barton (May 12 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20stuff/near/126467594):
<p>Currently almost everything related to topological spaces is in the root namespace, which doesn't seem ideal, but surely it would be no worse than having <code>embedding</code> there which it is already.</p>

#### [ Reid Barton (May 12 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20stuff/near/126467700):
<p>Um, it also just follows from <code>compact_image</code>. <span class="emoji emoji-1f643" title="upside down face">:upside_down_face:</span></p>

#### [ Kevin Buzzard (May 12 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20stuff/near/126467747):
<p>I have never really engaged with namespaces until recently; I had other things to worry about. I never used the namespace command and never opened anything. But it's all dawning on me now about how it might all work. I am surprised this stuff is piling up in the root namespace, and the longer it's there the more it will hurt when someone decides that <code>compact</code> doesn't apply to all types and hence should be moved to somewhere more topological-spacey.</p>

#### [ Kevin Buzzard (May 12 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20stuff/near/126467751):
<p>Yes, continuous image of compact is compact will do and probably I will just cheat and use that :-)</p>

#### [ Reid Barton (May 12 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20stuff/near/126467791):
<p><code>embedding</code> seems even more dubious</p>

#### [ Kevin Buzzard (May 12 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20stuff/near/126467792):
<p>That's in mathlib now, right?</p>

#### [ Reid Barton (May 12 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20stuff/near/126467793):
<p>Yep</p>

#### [ Kevin Buzzard (May 12 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20stuff/near/126467999):
<p>Is there <code>is_finite</code> somewhere, a prop saying that a type is finite?</p>

#### [ Mario Carneiro (May 12 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20stuff/near/126470976):
<p>There is <code>finite</code>, but that applies to sets</p>

#### [ Mario Carneiro (May 12 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20stuff/near/126470981):
<p><code>open_immersion</code> sounds suitably unambiguously topological that it can go in the root namespace</p>

#### [ Kenny Lau (May 12 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20stuff/near/126471039):
<blockquote>
<p>Is there <code>is_finite</code> somewhere, a prop saying that a type is finite?</p>
</blockquote>
<p>there's <code>fintype</code> which isn't a prop</p>

#### [ Kenny Lau (May 12 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20stuff/near/126471044):
<p>the prop is <code>nonempty (fintype \a)</code></p>

#### [ Mario Carneiro (May 12 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20stuff/near/126471048):
<p>For <code>compact2</code>, I would recommend against theorems that have "weird" topologies inserted in the top space component. It makes them very hard to use. Instead, I would want a hypothesis that says that the topology on <code>A</code> is induced from <code>f</code> by the topology on <code>B</code> (i.e. <code>topA = induced f topB</code>, and then you can just use regular typeclass inference to state <code>compact</code> on each side</p>

#### [ Johan Commelin (May 12 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20stuff/near/126471234):
<blockquote>
<p><code>open_immersion</code> sounds suitably unambiguously topological that it can go in the root namespace</p>
</blockquote>
<p>But there are also <em>open immersions</em> in other categories (manifolds, schemes, etc). Wouldn't that create confusion?</p>

#### [ Kevin Buzzard (May 22 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20stuff/near/126932789):
<p>I have to make a design decision.</p>

#### [ Kevin Buzzard (May 22 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20stuff/near/126932818):
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">topological_space</span><span class="bp">.</span><span class="n">open_immersion</span>
  <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">Tα</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span>
  <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">Tβ</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">β</span><span class="o">]</span>
  <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">fcont</span> <span class="o">:</span> <span class="n">continuous</span> <span class="n">f</span><span class="o">)</span>
<span class="o">(</span><span class="n">finj</span> <span class="o">:</span> <span class="n">function</span><span class="bp">.</span><span class="n">injective</span> <span class="n">f</span><span class="o">)</span>
<span class="o">(</span><span class="n">fopens</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">U</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">,</span> <span class="n">is_open</span> <span class="n">U</span> <span class="bp">↔</span> <span class="n">is_open</span> <span class="o">(</span><span class="n">f</span> <span class="err">&#39;&#39;</span> <span class="n">U</span><span class="o">))</span>
</pre></div>

#### [ Kevin Buzzard (May 22 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20stuff/near/126932819):
<p>I don't care either way</p>

#### [ Kevin Buzzard (May 22 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20stuff/near/126932820):
<p>or</p>

#### [ Kevin Buzzard (May 22 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20stuff/near/126932821):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">topological_space</span><span class="bp">.</span><span class="n">open_immersion</span> <span class="o">{</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">tX</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">X</span><span class="o">]</span> <span class="o">[</span><span class="n">tY</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">Y</span><span class="o">]</span> <span class="o">(</span><span class="n">φ</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">Y</span><span class="o">)</span> <span class="o">:=</span>
  <span class="n">continuous</span> <span class="n">φ</span> <span class="bp">∧</span>
  <span class="n">function</span><span class="bp">.</span><span class="n">injective</span> <span class="n">φ</span> <span class="bp">∧</span>
  <span class="bp">∀</span> <span class="n">U</span> <span class="o">:</span> <span class="n">set</span> <span class="n">X</span><span class="o">,</span> <span class="n">tX</span><span class="bp">.</span><span class="n">is_open</span> <span class="n">U</span> <span class="bp">→</span> <span class="n">tY</span><span class="bp">.</span><span class="n">is_open</span> <span class="o">(</span><span class="n">set</span><span class="bp">.</span><span class="n">image</span> <span class="n">φ</span> <span class="n">U</span><span class="o">)</span>
</pre></div>

#### [ Kevin Buzzard (May 22 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20stuff/near/126932822):
<p>and don't know enough about how things work to know which choice is best</p>

#### [ Reid Barton (May 22 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20stuff/near/126933209):
<p>There's already <code>embedding</code>, by the way. So you could also just add <code>is_open (range f)</code> to that and use <code>embedding_open</code>.</p>

#### [ Reid Barton (May 22 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20stuff/near/126933294):
<p>I doubt it matters much which exact definition you take, as you can write lemmas to prove that other definitions are equivalent. Whether to use a <code>structure</code> or not is probably more important, but depends on what you want to do with it.</p>

#### [ Reid Barton (May 22 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20stuff/near/126933483):
<p>Oh, your structure is indexed on <code>f</code> also; then it's just a matter of taste I think.</p>

#### [ Andrew Ashworth (May 22 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20stuff/near/126939770):
<p>I like structures for organizing things that are linked by and statements, I prefer giving names to the hypotheses rather than referring to them as <code>and.left and.left ...</code> etc</p>

#### [ Sean Leather (May 23 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20stuff/near/126962847):
<p>One thing to consider is how you use <code>simp</code> and <code>@[simp]</code> theorems. With a structure, you have control over what is simplified by carefully choosing where you place your <code>@[simp]</code>s. With nested conjunctions, you are at the mercy of the existing <code>@[simp]</code> theorems. (Of course, you can “work around” this; it's just a matter of how simple your proofs will be.) On the other hand, with conjunctions, you may find that it's easier to work with simplified proofs, given how much already exists to simplify them. (Of course, you can recover this ease by writing <code>@[simp]</code> theorems to do the conversion from the structure to conjunctions. But there goes your control, too.)</p>

#### [ Reid Barton (May 23 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20stuff/near/126969745):
<p>Another advantage of giving the fields names is that if for some reason you want to change the underlying definition, you can do it in a way that's somewhat transparent by making functions with the names of the old fields.</p>

#### [ Reid Barton (May 23 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/topological%20space%20stuff/near/126969806):
<p>Though this doesn't help if you tend to use pattern matching / implicit constructor syntax</p>


{% endraw %}
