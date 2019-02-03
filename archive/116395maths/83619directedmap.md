---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/83619directedmap.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [directed map](https://leanprover-community.github.io/archive/116395maths/83619directedmap.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Mario Carneiro (Nov 06 2018 at 06:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/directed%20map/near/146847285):
<p>Does this concept look familiar to anyone?</p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">[</span><span class="n">preorder</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">preorder</span> <span class="n">β</span><span class="o">]</span> <span class="o">(</span><span class="n">m</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span>
<span class="n">class</span> <span class="n">directed_map</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">mono</span> <span class="o">:</span> <span class="n">monotone</span> <span class="n">m</span><span class="o">)</span>
<span class="o">(</span><span class="n">dir</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">directed_on</span> <span class="o">(</span><span class="bp">≥</span><span class="o">)</span> <span class="o">{</span><span class="n">a</span> <span class="bp">|</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">m</span> <span class="n">a</span><span class="o">})</span>
</pre></div>

#### [ Mario Carneiro (Nov 06 2018 at 07:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/directed%20map/near/146847552):
<p>Turns out this is what you need to map a preorder filter. It's a category</p>

#### [ Mario Carneiro (Nov 06 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/directed%20map/near/146847622):
<p>By the way, does anyone have any naming suggestions for preorder filters vs set filters?</p>

#### [ Mario Carneiro (Nov 06 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/directed%20map/near/146847624):
<p>"prefilter" just occurred to me</p>

#### [ Patrick Massot (Nov 06 2018 at 07:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/directed%20map/near/146849018):
<p>What is a preorder filter?</p>

#### [ Mario Carneiro (Nov 06 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/directed%20map/near/146849250):
<p>It is a subset of a preorder which is nonempty, upward closed, and has an element below any two elements in the filter (downward directed)</p>

#### [ Mario Carneiro (Nov 06 2018 at 08:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/directed%20map/near/146849262):
<p>basically you generalize the part about filters being sets of sets to sets in a more general ordered structure</p>

#### [ Reid Barton (Nov 06 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/directed%20map/near/146872338):
<p>It looks similar to (and implies) the notion of <a href="https://ncatlab.org/nlab/show/final+functor#definition" target="_blank" title="https://ncatlab.org/nlab/show/final+functor#definition">(co)final functor</a>, but I don't remember seeing this exact notion before.</p>

#### [ Reid Barton (Nov 06 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/directed%20map/near/146872406):
<p>I like the name "directed map", because you have the property: <code>\a</code> is directed if and only if the unique map <code>\a \to unit</code> is directed</p>

#### [ Reid Barton (Nov 06 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/directed%20map/near/146872843):
<p>"prefilter" however strikes me as a word which should mean a filter minus some property, or something like a filter basis. Compare presheaf/sheaf, (historically) prescheme/scheme = (scheme/separated scheme).</p>

#### [ Reid Barton (Nov 06 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/directed%20map/near/146873026):
<p>I suppose using <code>filter</code> for both cases is infeasible, or you wouldn't be asking the question?</p>

#### [ Floris van Doorn (Nov 06 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/directed%20map/near/146874734):
<p><code>filter</code> and <code>set_filter</code>? Or is renaming the current one out of the question?</p>

#### [ Sebastien Gouezel (Nov 06 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/directed%20map/near/146874798):
<p><code>order_filter</code> and <code>filter</code>?</p>

#### [ Reid Barton (Nov 06 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/directed%20map/near/146874970):
<p>We could also make use of namespacing perhaps</p>


{% endraw %}
