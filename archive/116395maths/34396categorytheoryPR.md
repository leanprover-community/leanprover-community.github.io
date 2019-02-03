---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/34396categorytheoryPR.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [category theory PR](https://leanprover-community.github.io/archive/116395maths/34396categorytheoryPR.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Jun 04 2018 at 05:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20PR/near/127526777):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span>, <span class="user-mention" data-user-id="110032">@Reid Barton</span>, <span class="user-mention" data-user-id="112680">@Johan Commelin</span>, the first cut of my category theory PR has just landed as <a href="https://github.com/leanprover/mathlib/pull/152" target="_blank" title="https://github.com/leanprover/mathlib/pull/152">https://github.com/leanprover/mathlib/pull/152</a>. Criticisms welcome!</p>

#### [ Johan Commelin (Jun 04 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20PR/near/127531032):
<p>Newbie comment: In line 39 of your <code>category.lean</code>, you write</p>
<div class="codehilite"><pre><span></span><span class="n">attribute</span> <span class="o">[</span><span class="n">ematch</span><span class="o">]</span> <span class="n">category</span><span class="bp">.</span><span class="n">associativity_lemma</span>
</pre></div>


<p>But isn't this also on the previous line?</p>

#### [ Scott Morrison (Jun 04 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20PR/near/127531414):
<p>Ooh, good catch. I didn't mean to have associativity marked as a simp, and will have to fix this. It shouldn't be a problem, but won't happen right now.</p>

#### [ Johan Commelin (Jun 04 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20PR/near/127531557):
<p>Ok</p>

#### [ Johan Commelin (Jun 04 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20PR/near/127531564):
<p>I submitted a review with 6 trivial comments.</p>

#### [ Sean Leather (Jun 04 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20PR/near/127533096):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> You might want to just review your usage of variables. I saw a number of duplicates mentioned in both a <code>variables</code> declaration <em>and</em> used in a def or theorem. I mentioned one on the PR, but there are more.</p>

#### [ Scott Morrison (Jun 04 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20PR/near/127535271):
<p>Thanks, <span class="user-mention" data-user-id="110045">@Sean Leather</span>. I'm not sure that there were any actual errors, but I have definitely been writing code that sometimes has an explicit argument in a definition, when there is an implicit variable of the same name in scope. I'll be careful to avoid this.</p>

#### [ Sean Leather (Jun 04 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20PR/near/127535472):
<p>No, there were no errors. It's just a comment on readability. Looks better now.</p>

#### [ Johan Commelin (Jun 04 2018 at 13:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20PR/near/127540230):
<p>Another point is that I think so far in mathlib there is no camel casing. I don't have a strong opinion on this, butI noticed that you use <code>NaturalTransformation</code>.</p>

#### [ Johan Commelin (Jun 06 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20PR/near/127670781):
<p>Once this PR has been merged we can formalise <a href="http://pijul.org" target="_blank" title="http://pijul.org">pijul.org</a>. Once code extraction is in place we will have a fully verified abstract nonsense version control system!</p>

#### [ Ned Summers (Jul 25 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20PR/near/130280546):
<p>I'm working with this and I was wondering why <code>is_Isomorphism</code> is defined as it is. In particular, under the label I'd expect it to be a Prop? I'm new to lean in general so I'm sure it's justified, just having difficulty with any statements that involved "f is an isomorphism".</p>

#### [ Reid Barton (Jul 25 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20PR/near/130281159):
<p>If f is an isomorphism, one wants to be able to talk about the inverse of f (compose it with other morphisms, and so on). Even though the inverse of f is uniquely determined by f, from Lean's point of view it is still additional data. If <code>is_Isomorphism</code> was a Prop, it would throw away this data and you would need to use the axiom of choice to get a hold of f's inverse, which is generally less convenient.</p>

#### [ Reid Barton (Jul 25 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20PR/near/130281667):
<p>If you want the Prop version, you can use <code>nonempty (is_Isomorphism f)</code>.</p>

#### [ Reid Barton (Jul 25 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20PR/near/130281941):
<p>This way you have a choice.</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">blah1</span> <span class="bp">...</span> <span class="o">:</span> <span class="n">is_Isomorphism</span> <span class="n">f</span> <span class="o">:=</span> <span class="bp">...</span>  <span class="c1">-- show f is an isomorphism by exhibiting an inverse;</span>
<span class="c1">-- Lean now knows that the inverse is given by definition by whatever formula you gave</span>

<span class="kn">lemma</span> <span class="n">blah2</span> <span class="bp">...</span> <span class="o">:</span> <span class="n">nonempty</span> <span class="o">(</span><span class="n">is_Isomorphism</span> <span class="n">f</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">...</span>  <span class="c1">-- show f is an isomorphism but don&#39;t specify the inverse;</span>
<span class="c1">-- Lean knows nothing about the inverse other than the equations contained in is_Isomorphism</span>
</pre></div>


<p>Sometimes you don't care about the exact construction of the inverse, and then the second option is appropriate.</p>

#### [ Kevin Buzzard (Jul 25 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20PR/near/130293640):
<p>If <code>is_Isomorphism</code> is not a prop, isn't the name contrary to mathlib conventions?</p>

#### [ Patrick Massot (Jul 25 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20PR/near/130293672):
<p>I agree, but this is in a not yet revised PR.</p>

#### [ Ned Summers (Jul 26 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/category%20theory%20PR/near/130344859):
<p>Thanks, Reid. Makes a lot of sense; just getting used to this hesitance about choice. Thanks for the suggestion too of the Prop version.</p>


{% endraw %}
