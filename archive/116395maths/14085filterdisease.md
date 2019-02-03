---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/14085filterdisease.html
---

## Stream: [maths](index.html)
### Topic: [filter disease](14085filterdisease.html)

---


{% raw %}
#### [ Patrick Massot (Aug 07 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131057798):
<p>This feels really strange: I just caught  myself writing a long string of manipulations involving filters pull-backed, push-forwarded, multiplied and compared, because it felt easier than thinking in terms of compositions of limits and such things</p>

#### [ Patrick Massot (Aug 07 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131058064):
<p>The key point is how filters allow to talk about limits when x tends to x' while staying in the image of a dense embedding.</p>

#### [ Kevin Buzzard (Aug 07 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131059184):
<p>It's on my to-do list to understand if and when filters can be pulled back and pushed forward</p>

#### [ Patrick Massot (Aug 07 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131059283):
<p>filters live on bare sets, hence can be pulled back and pushed forward by bare set morphisms</p>

#### [ Patrick Massot (Aug 07 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131059294):
<p>aka any map</p>

#### [ Patrick Massot (Aug 07 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131059431):
<p>both operation are order preserving. And f_*F \le G iff F \le f^*G</p>

#### [ Patrick Massot (Aug 07 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131059536):
<p>Now let's do composition of limits. f goes to G along F (I don't know how to pronounce this) if, by definition, f_*F \le G. Now it's an exercise for you</p>

#### [ Patrick Massot (Aug 07 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131059574):
<p>of course f_* is covariantly functorial</p>

#### [ Kevin Buzzard (Aug 07 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131059776):
<p>Are they adjoint functors? <span class="user-mention" data-user-id="110064">@Kenny Lau</span> you'd like this stuff</p>

#### [ Kevin Buzzard (Aug 07 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131059802):
<p>You'll soon be complaining that they teach limits wrong at Imperial. Did you see my  filter blog post? Maybe you know all this stuff already</p>

#### [ Patrick Massot (Aug 07 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131060103):
<p>What would be Hom between two filters?</p>

#### [ Patrick Massot (Aug 07 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131060239):
<p>sorry</p>

#### [ Patrick Massot (Aug 07 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131060254):
<p>you mean for the poset structure?</p>

#### [ Patrick Massot (Aug 07 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131060330):
<p>Yes, we have f_*f^*G \le G  and F \le f^<em>f_</em>F  for all F and G</p>

#### [ Patrick Massot (Aug 07 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131060390):
<p>I must be careful not to be carried away, or else I'll be tempted to teach this to innocent students</p>

#### [ Patrick Massot (Aug 07 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131060872):
<p>where are adjoint functors in mathlib now that we got a category PR accepted?</p>

#### [ Kevin Buzzard (Aug 07 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131062286):
<p>You're right, I guess it must be like the opens in a top space, the inclusions are the only morphisms, and the one equation you mentioned above is I guess precisely the affirmative answer</p>

#### [ Patrick Massot (Aug 07 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131070762):
<p>I managed to abstract the lemma I was using three times in my proof.</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">topology</span><span class="bp">.</span><span class="n">continuity</span>

<span class="kn">open</span> <span class="n">set</span> <span class="n">filter</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">topological_space</span> <span class="n">β</span><span class="o">]</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">δ</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">topological_space</span> <span class="n">δ</span><span class="o">]</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">e</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">}</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">g</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="n">δ</span><span class="o">}</span> <span class="o">{</span><span class="n">h</span> <span class="o">:</span> <span class="n">δ</span> <span class="bp">→</span> <span class="n">β</span><span class="o">}</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm"> γ -f→ α</span>
<span class="cm">g↓     ↓e</span>
<span class="cm"> δ -h→ β</span>
<span class="cm">-/</span>

<span class="kn">lemma</span> <span class="n">key</span>  <span class="o">{</span><span class="n">d</span> <span class="o">:</span> <span class="n">δ</span><span class="o">}</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">tendsto</span> <span class="n">h</span> <span class="o">(</span><span class="n">nhds</span> <span class="n">d</span><span class="o">)</span> <span class="o">(</span><span class="n">nhds</span> <span class="o">(</span><span class="n">e</span> <span class="n">a</span><span class="o">)))</span> <span class="o">(</span><span class="n">comm</span> <span class="o">:</span> <span class="n">h</span> <span class="err">∘</span> <span class="n">g</span> <span class="bp">=</span> <span class="n">e</span> <span class="err">∘</span> <span class="n">f</span><span class="o">)</span>
  <span class="o">(</span><span class="n">de</span> <span class="o">:</span> <span class="n">dense_embedding</span> <span class="n">e</span><span class="o">)</span> <span class="o">:</span>  <span class="n">tendsto</span> <span class="n">f</span> <span class="o">(</span><span class="n">vmap</span> <span class="n">g</span> <span class="o">(</span><span class="n">nhds</span> <span class="n">d</span><span class="o">))</span> <span class="o">(</span><span class="n">nhds</span> <span class="n">a</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">have</span> <span class="n">lim1</span> <span class="o">:</span> <span class="n">map</span> <span class="n">g</span> <span class="o">(</span><span class="n">vmap</span> <span class="n">g</span> <span class="o">(</span><span class="n">nhds</span> <span class="n">d</span><span class="o">))</span> <span class="bp">≤</span> <span class="n">nhds</span> <span class="n">d</span> <span class="o">:=</span> <span class="n">map_vmap_le</span><span class="o">,</span>
  <span class="n">replace</span> <span class="n">lim1</span> <span class="o">:</span> <span class="n">map</span> <span class="n">h</span> <span class="o">(</span><span class="n">map</span> <span class="n">g</span> <span class="o">(</span><span class="n">vmap</span> <span class="n">g</span> <span class="o">(</span><span class="n">nhds</span> <span class="n">d</span><span class="o">)))</span> <span class="bp">≤</span> <span class="n">map</span> <span class="n">h</span> <span class="o">(</span><span class="n">nhds</span> <span class="n">d</span><span class="o">)</span> <span class="o">:=</span> <span class="n">map_mono</span> <span class="n">lim1</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">filter</span><span class="bp">.</span><span class="n">map_map</span><span class="o">,</span> <span class="n">comm</span><span class="o">,</span> <span class="err">←</span> <span class="n">filter</span><span class="bp">.</span><span class="n">map_map</span><span class="o">,</span> <span class="n">map_le_iff_le_vmap</span><span class="o">]</span> <span class="n">at</span> <span class="n">lim1</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">lim2</span> <span class="o">:</span>  <span class="n">vmap</span> <span class="n">e</span> <span class="o">(</span><span class="n">map</span> <span class="n">h</span> <span class="o">(</span><span class="n">nhds</span> <span class="n">d</span><span class="o">))</span> <span class="bp">≤</span>  <span class="n">vmap</span> <span class="n">e</span>  <span class="o">(</span><span class="n">nhds</span> <span class="o">(</span><span class="n">e</span> <span class="n">a</span><span class="o">))</span> <span class="o">:=</span> <span class="n">vmap_mono</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">de</span><span class="bp">.</span><span class="n">induced</span> <span class="n">at</span> <span class="n">lim2</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">le_trans</span> <span class="n">lim1</span> <span class="n">lim2</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Patrick Massot (Aug 07 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131070803):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> I hope you're proud of me. But I'd still be interested if there is a smarter proof (or if it's already in mathlib).</p>

#### [ Patrick Massot (Aug 07 2018 at 23:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131070879):
<p>By the way, why isn't <code>dense_embedding</code> a class?</p>

#### [ Patrick Massot (Aug 07 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131070901):
<p>Also, I find it a bit painful that the map is an implicit argument in <code>map_mono</code> and <code>vmap_mono</code>.</p>

#### [ Patrick Massot (Aug 07 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131070985):
<p>Now I'll go sleeping, feeling I've learned some nice stuff today.</p>

#### [ Kevin Buzzard (Aug 07 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131071488):
<p>+1 for the commutative diagram!</p>

#### [ Scott Morrison (Aug 08 2018 at 03:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131079718):
<blockquote>
<p>where are adjoint functors in mathlib now that we got a category PR accepted?</p>
</blockquote>
<p>Sorry to disappoint, <span class="user-mention" data-user-id="110031">@Patrick Massot</span>, but only the first epsilon of category theory has been PR'd. It's a ways to go before you have adjoint functors.</p>

#### [ Reid Barton (Aug 08 2018 at 05:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131084690):
<p>However, adjoint functors between posets are Galois connections, and they are in mathlib (<code>order/galois_connection.lean</code>).</p>

#### [ Johannes Hölzl (Aug 08 2018 at 07:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131089180):
<blockquote>
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> I hope you're proud of me. But I'd still be interested if there is a smarter proof (or if it's already in mathlib).</p>
</blockquote>
<p>Looks good to me. I don't think there is a related proof in mathlib. I'm on a bike trip this week, I can check out next Monday.</p>

#### [ Patrick Massot (Aug 08 2018 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131100297):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> Sorry about this joke. I know it's only the beginning, I did look at your PR.</p>

#### [ Patrick Massot (Aug 08 2018 at 13:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131101008):
<p>There is no hurry at all. The more difficult question is: how should we name that?</p>

#### [ Patrick Massot (Aug 08 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20disease/near/131101650):
<p>And also I'm a bit confused by the relation between <code>dense_embedding</code> and <code>embedding</code> in mathlib. My lemma actually doesn't use the dense part, but it uses the way the <code>induced</code> axiom is stated. But I guess it could be stated that way for embeddings too, right?</p>


{% endraw %}
