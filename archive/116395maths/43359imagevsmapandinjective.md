---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/43359imagevsmapandinjective.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [image vs map and injective](https://leanprover-community.github.io/archive/116395maths/43359imagevsmapandinjective.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Sean Leather (Jun 22 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20vs%20map%20and%20injective/near/128459841):
<p>In <code>data.finset</code>, <code>finset.map</code> is defined as mapping an <code>embedding</code> or an injective function over a <code>finset</code>, and <code>finset.image</code> is mapping a function over a <code>finset</code>. Other mathlib components (e.g <code>set</code>, <code>multiset</code>, <code>list</code>, <code>array</code>, etc.) do not make this distinction using this naming scheme.</p>
<p>I think there is a useful distinction to be made here. For example, grep <code>data/list/basic.lean</code> for <code>injective</code>: these declarations could be changed to use <code>embedding</code>. But I'm not sure about the <code>image</code> vs <code>map</code> naming. Is this a standard thing? If so, can we implement it for other components? If not, can we come up with a meaningful naming distinction for mapping a function and mapping an injective function and implement that?</p>

#### [ Reid Barton (Jun 22 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20vs%20map%20and%20injective/near/128474541):
<p>The purpose of the distinction is that while <code>finset.map</code> and <code>finset.image</code> do the same thing, namely compute the image of a finite set under a function, they do so under incomparable hypotheses. Some hypothesis is necessary because we somehow need to ensure that the resulting <code>finset</code> has no duplicates. <code>finset.image</code> requires the target to have decidable equality, which is a free assumption when doing classical mathematics. <code>finset.map</code> requires the function to be injective.</p>

#### [ Reid Barton (Jun 22 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20vs%20map%20and%20injective/near/128474621):
<p><code>finset.map</code> is also much cheaper computationally, since it just has to apply the given function n times. I guess this is where the name <code>map</code> comes from; computationally, it's just mapping a function over a data structure (the <code>Prop</code> part does not exist computationally). <code>finset.image</code> has to check the resulting list for duplicates and remove them, which takes time O(n^2).</p>

#### [ Reid Barton (Jun 22 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20vs%20map%20and%20injective/near/128474724):
<p>As far as the other types you mentioned are concerned, the "positive" types <code>multiset</code>, <code>list</code>, <code>array</code> have no constraints analogous to the uniqueness in a <code>finset</code>, so we can just use the <code>map</code> implementation in all cases. For the "negative" type <code>set</code> (<code>set t = t -&gt; Prop</code>) we can't really hope to compute the image, so we can just use the logical definition.</p>

#### [ Sean Leather (Jun 25 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20vs%20map%20and%20injective/near/128586002):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> Thanks for the very informative response! I neither noticed the <code>[decidable_eq β]</code> on <code>finset.image</code> nor realized its impact, so that's good to know.</p>
<p>I'm still not quite clear on what should be named what. Let me propose what I infer and anybody can shoot it down:</p>
<ul>
<li><code>set.image</code> is the <a href="https://en.wikipedia.org/wiki/Image_(mathematics)" target="_blank" title="https://en.wikipedia.org/wiki/Image_(mathematics)">logical image</a> of a set.</li>
<li><code>finset.image</code> is the analog to <code>set.image</code> for a finite set. Since <code>set.image</code> involves a equality test, it makes since that <code>finset.image</code> require <code>decidable_eq</code> on <code>β</code>.</li>
<li><code>list.map</code>, <code>multiset.map</code>, etc. are the standard (functor) mappings.</li>
<li><code>finset.map</code> is the implementation equivalent of <code>list.map</code>, etc. but requires injectivity to preserve the <code>finset</code> properties.</li>
</ul>
<p>If I describe the situation as above, it makes sense to me.</p>
<p>That said, there are some cases where mapping an injective function over a list is useful. Is it worth creating an additional definition for <code>list.map</code> using <code>embedding</code> along with associated theorems?</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">list</span><span class="bp">.</span><span class="n">imap</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="err">↪</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">list</span> <span class="n">β</span> <span class="o">:=</span> <span class="n">list</span><span class="bp">.</span><span class="n">map</span> <span class="n">f</span><span class="bp">.</span><span class="n">to_fun</span>
</pre></div>


<p>I don't have any good thoughts on the name. Is there a standard here?</p>

#### [ Mario Carneiro (Jun 25 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20vs%20map%20and%20injective/near/128586287):
<p>I don't see a reason to have such a definition, since you can just write <code>list.map f</code> with the inserted coercion</p>

#### [ Sean Leather (Jun 25 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20vs%20map%20and%20injective/near/128586401):
<p>Right. The only reason would be for convenience, not for necessity of proof.</p>

#### [ Sean Leather (Jun 25 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20vs%20map%20and%20injective/near/128586527):
<blockquote>
<p>The only reason would be for convenience, not for necessity of proof.</p>
</blockquote>
<p>In fact, however, could you not say the same thing about <code>finset.map</code>?</p>

#### [ Sean Leather (Jun 25 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20vs%20map%20and%20injective/near/128586591):
<p>The main difference, of course, is that <code>list.map</code> is useful without injectivity and <code>finset.map</code> is not.</p>

#### [ Mario Carneiro (Jun 25 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20vs%20map%20and%20injective/near/128586724):
<p>I mean that there is no gain besides a slightly longer name</p>

#### [ Mario Carneiro (Jun 25 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20vs%20map%20and%20injective/near/128586731):
<p>If you want to use <code>map</code> on an injective function, just use it</p>

#### [ Mario Carneiro (Jun 25 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20vs%20map%20and%20injective/near/128586773):
<p>with <code>finset.map</code> there is a clear difference since the definition is different</p>

#### [ Sean Leather (Jun 25 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/image%20vs%20map%20and%20injective/near/128587364):
<p>Oh, I see. You're referring to the use of <code>list.map</code> with an injective function. I was referring to the convenience of writing proofs for <code>map</code> with injectivity: you wouldn't have to specify <code>injective f</code>. Nonetheless, I concede that it's a pretty weak motivation.</p>


{% endraw %}
