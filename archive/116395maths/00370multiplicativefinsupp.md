---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/00370multiplicativefinsupp.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [multiplicative finsupp](https://leanprover-community.github.io/archive/116395maths/00370multiplicativefinsupp.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Jan 22 2019 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multiplicative%20finsupp/near/156594377):
<p>I'm trying to stress test my adjunctions code. A natural example is <code>mv_polynomial</code> being left adjoint to <code>forget</code>. This adjunction is actually a composite of two adjunctions: the free monoid construction, and monoid rings. While trying to write these things down, I got stuck in the whole additive-multiplicative business again. So, let's forget about this motivation for now.</p>
<p>Has anyone ever attempted to turn <code>data/finsupp</code> into a file that supports both multiplicative and additive coefficients? Are there any expected problems? Or is this just something that has to be done by someone?</p>

#### [ Mario Carneiro (Jan 22 2019 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multiplicative%20finsupp/near/156594586):
<p>use <code>multiplicative A</code> for the coefficients</p>

#### [ Johan Commelin (Jan 22 2019 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multiplicative%20finsupp/near/156595162):
<p>I know I can do that. But it becomes pretty messy. And it feels to me like it defeats the purpose of the <code>add</code>/<code>mul</code> distinction.</p>

#### [ Johan Commelin (Jan 22 2019 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multiplicative%20finsupp/near/156595211):
<p>All of a sudden I'm having proofs like</p>
<div class="codehilite"><pre><span></span><span class="o">{</span> <span class="n">map_one</span> <span class="o">:=</span> <span class="n">map_domain_zero</span><span class="o">,</span> <span class="n">map_mul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">map_domain_add</span> <span class="o">}</span>
</pre></div>


<p>which creates cognitive dissonance.</p>

#### [ Johan Commelin (Jan 22 2019 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multiplicative%20finsupp/near/156595229):
<p>I think that if we want to use <code>multiplicative</code> (or <code>additive</code>, I don't care) we should just use it everywhere.</p>

#### [ Mario Carneiro (Jan 22 2019 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multiplicative%20finsupp/near/156595240):
<p>well we did, and now you want the other one</p>

#### [ Johan Commelin (Jan 22 2019 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multiplicative%20finsupp/near/156595315):
<p>No, I mean everywhere in mathlib.</p>

#### [ Mario Carneiro (Jan 22 2019 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multiplicative%20finsupp/near/156595320):
<p>I have argued since day 1 that it would be much nicer to use add for group theory and forget about mul except in specialized circumstances, but mathematicians get hissy about non-commutative addition</p>

#### [ Kevin Buzzard (Jan 22 2019 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multiplicative%20finsupp/near/156596112):
<p>Mathematicians definitely want both.</p>

#### [ Kevin Buzzard (Jan 22 2019 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multiplicative%20finsupp/near/156596116):
<p>Non-commutative addition is the least of our worries here.</p>

#### [ Mario Carneiro (Jan 22 2019 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multiplicative%20finsupp/near/156596745):
<p>If I said "all groups must use addition", what exactly would be the downside? AFAICT there are very few places where you actually need multiplicative groups besides "it looks better"</p>

#### [ Mario Carneiro (Jan 22 2019 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multiplicative%20finsupp/near/156596829):
<p>by contrast it is quite common to use the group structure of additive groups embedded in rings and other things</p>

#### [ Mario Carneiro (Jan 22 2019 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multiplicative%20finsupp/near/156596867):
<p>Note that a ring does not have a multiplicative group; multiplication is not a group operation. Instead there is an associated structure, the "units group", that is a group</p>

#### [ Kevin Buzzard (Jan 22 2019 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multiplicative%20finsupp/near/156597285):
<p>If you said "all groups must use addition" then mathematicians would consistently be utterly confused about why the unit group of a ring had group law addition. I guess there's nothing stopping this convention -- equally, there is nothing stopping the convention that you use a little heart symbol. It's just that mathematicians would then find this stuff even harder to understand. Notation conveys meaning and notation which mathematicians have fixed on is <em>very</em> hard to change. I personally loathe the standard symbol for quadratic residues / non-residues, because it's a fraction in a bracket -- but there's very little I can do about this.</p>

#### [ Johan Commelin (Jan 22 2019 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multiplicative%20finsupp/near/156597691):
<p>We have proof irrelevance. Why can't we have notation irrelevance. (I know that the current implementation via type classes makes it hard. But that just means we need a better solution.)</p>

#### [ Johan Commelin (Jan 22 2019 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multiplicative%20finsupp/near/156599282):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I can see why you would want all groups to be additive (although adding invertible matrices feels very wrong). But with monoids you wouldn't have a clean solution, right? Every ring gives you two monoids, one for addition, the other for multiplication. I'm interested in knowing what you would do there.</p>

#### [ Kevin Buzzard (Jan 22 2019 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multiplicative%20finsupp/near/156615639):
<p>I thought about this more. A mathematician has a fixed notation for a ring, so you can't change it -- it uses <code>+</code> and <code>*</code>. And a ring is a group under <code>+</code> and the units of a ring are a group under <code>*</code>, and these come up again and again, so you can't change these either :-/ And the point is that in mathematics we are capable of rewriting these group axioms from <code>+</code> to <code>*</code> seamlessly because <em>it is true that it works fine</em>, yet Lean struggles to do it seamlessly. There clearly is some sort of a problem here, but I don't think mathematicians will accept removal of <code>*</code> because it goes the wrong way. For us, the units of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi></mrow><annotation encoding="application/x-tex">R</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span></span></span></span> are a subset of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi></mrow><annotation encoding="application/x-tex">R</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span></span></span></span>. This is not how it works in DTT and somehow we need a better solution :-/</p>

#### [ Johan Commelin (Jan 22 2019 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multiplicative%20finsupp/near/156615711):
<p>How about <code>End(V)</code>? We'll use <code>\circ</code> instead of <code>*</code>, without blinking an eye.</p>

#### [ Reid Barton (Jan 22 2019 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multiplicative%20finsupp/near/156615835):
<p>A unit is just an automorphism of a ring as a module over itself, what's the problem?</p>

#### [ Reid Barton (Jan 22 2019 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/multiplicative%20finsupp/near/156615884):
<p>(<a href="https://stackoverflow.com/questions/3870088/a-monad-is-just-a-monoid-in-the-category-of-endofunctors-whats-the-problem" target="_blank" title="https://stackoverflow.com/questions/3870088/a-monad-is-just-a-monoid-in-the-category-of-endofunctors-whats-the-problem">https://stackoverflow.com/questions/3870088/a-monad-is-just-a-monoid-in-the-category-of-endofunctors-whats-the-problem</a>)</p>


{% endraw %}
