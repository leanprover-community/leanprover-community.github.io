---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/50863transfinitecompositions.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [transfinite compositions](https://leanprover-community.github.io/archive/116395maths/50863transfinitecompositions.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Reid Barton (Sep 17 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transfinite%20compositions/near/134128023):
<p>Suppose P is a complete lattice. I can define an increasing sequence of finite length in P either as a subtype of a function type or as an inductive type, as shown below.</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">order</span><span class="bp">.</span><span class="n">complete_lattice</span>
<span class="kn">open</span> <span class="n">lattice</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">P</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">[</span><span class="n">complete_lattice</span> <span class="n">P</span><span class="o">]</span>

<span class="n">def</span> <span class="n">seq1</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Type</span> <span class="o">:=</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">fin</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="bp">→</span> <span class="n">P</span> <span class="bp">//</span> <span class="bp">∀</span> <span class="n">i</span> <span class="n">j</span><span class="o">,</span> <span class="n">i</span> <span class="bp">≤</span> <span class="n">j</span> <span class="bp">→</span> <span class="n">f</span> <span class="n">i</span> <span class="bp">≤</span> <span class="n">f</span> <span class="n">j</span><span class="o">}</span>
<span class="kn">inductive</span> <span class="n">seq2</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">P</span><span class="o">)</span> <span class="o">:</span> <span class="n">P</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">nil</span> <span class="o">:</span> <span class="n">seq2</span> <span class="n">a</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="n">cons</span> <span class="o">:</span> <span class="bp">Π</span> <span class="n">b</span> <span class="n">b&#39;</span> <span class="n">n</span><span class="o">,</span> <span class="n">seq2</span> <span class="n">b</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">b</span> <span class="bp">≤</span> <span class="n">b&#39;</span> <span class="bp">→</span> <span class="n">seq2</span> <span class="n">b&#39;</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span>
</pre></div>

#### [ Reid Barton (Sep 17 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transfinite%20compositions/near/134128069):
<p>The first one generalizes easily to any ordinal (or any well-ordered set). Is there a way to generalize the second?<br>
I mention that P is a complete lattice because I'm happy to assume (if it helps) that at each limit stage, the value of the sequence is equal to the sup of all the previous values.</p>

#### [ Reid Barton (Sep 17 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transfinite%20compositions/near/134128599):
<p>The only way I can think to handle limit ordinal stages is to ask for an increasing sequence of every smaller ordinal length, such that for any α ≤ β, the sequence of length α is a prefix of the sequence of length β</p>

#### [ Reid Barton (Sep 17 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transfinite%20compositions/near/134128603):
<p>But this seems a bit awkward.</p>

#### [ Reid Barton (Sep 17 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transfinite%20compositions/near/134128630):
<p>(What I'm really trying to do is model <a href="https://ncatlab.org/nlab/show/transfinite+composition" target="_blank" title="https://ncatlab.org/nlab/show/transfinite+composition">https://ncatlab.org/nlab/show/transfinite+composition</a>)</p>

#### [ Johannes Hölzl (Sep 17 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transfinite%20compositions/near/134128804):
<p>I'm not sure if this is what you're looking for. The following is used in Isabelle to model transfinite recursion:</p>
<div class="codehilite"><pre><span></span><span class="k">inductive_set</span> <span class="n">iterates</span> <span class="o">::</span> <span class="s">&quot;(&#39;a ⇒ &#39;a) ⇒ &#39;a set&quot;</span> <span class="kp">for</span> <span class="n">f</span> <span class="o">::</span> <span class="s">&quot;&#39;a ⇒ &#39;a&quot;</span> <span class="kp">where</span>
<span class="o">|</span> <span class="n">step</span><span class="o">:</span> <span class="s">&quot;x ∈ iterates f ⟹ f x ∈ iterates f&quot;</span>
<span class="o">|</span> <span class="n">Sup</span><span class="o">:</span> <span class="s">&quot;chain (≤) M ⟹ ∀x∈M. x ∈ iterates f ⟹ Sup M ∈ iterates f&quot;</span>
</pre></div>


<p>Maybe you can use a similar approach?</p>

#### [ Reid Barton (Sep 17 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transfinite%20compositions/near/134128831):
<p>Hmm, interesting</p>

#### [ Reid Barton (Sep 17 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transfinite%20compositions/near/134128899):
<p>Indeed we basically always construct such transfinite compositions by iterating some construction at successor stages, and taking a sup/colimit at limit stages</p>

#### [ Reid Barton (Sep 17 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transfinite%20compositions/near/134128922):
<p>What kind of thing is M there? a subset of 'a?</p>

#### [ Reid Barton (Sep 17 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transfinite%20compositions/near/134129010):
<p>and <code>chain (≤)</code> means it's totally ordered?</p>

#### [ Reid Barton (Sep 17 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transfinite%20compositions/near/134129169):
<p>Ah, I found the source.</p>

#### [ Johannes Hölzl (Sep 17 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transfinite%20compositions/near/134129173):
<p>Yes, <code>M</code> is a subset of <code>'a</code> and <code>chain (≤) M</code> says that <code>M</code> is totally ordered</p>

#### [ Johannes Hölzl (Sep 18 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transfinite%20compositions/near/134129410):
<p>the interesting part is that <code>iterates</code> is a <code>chain</code> in itself, so it contains its supremum, which is the fixed point of <code>f</code>.  In this theory <code>'a</code> is a chain complete partial order (i.e. all non-empty chains have a supremum)</p>

#### [ Reid Barton (Sep 18 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/transfinite%20compositions/near/134133872):
<p>One thing that occurs to me is that my finite sequences are themselves partially ordered by "extends", and the finite prefixes of a countable sequence form a chain</p>


{% endraw %}
