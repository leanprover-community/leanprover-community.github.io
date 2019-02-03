---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/46635Problemwithloopingoverfinset.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Problem with looping over finset](https://leanprover-community.github.io/archive/113488general/46635Problemwithloopingoverfinset.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ AHan (Jan 15 2019 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problem%20with%20looping%20over%20finset/near/155177808):
<p>Given <code>s : finset ℕ</code>,  how can I construct <code>s' : finset (ℕ × ℕ)</code> s.t.  <code>∀ a b,  a b ∈ s ↔ (a, b) ∈ s'</code> ?</p>

#### [ Patrick Massot (Jan 15 2019 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problem%20with%20looping%20over%20finset/near/155178216):
<p>I think what you wrote doesn't type-check</p>

#### [ Mario Carneiro (Jan 15 2019 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problem%20with%20looping%20over%20finset/near/155178295):
<p>I assume the <code>a b</code> means <code>a * b</code></p>

#### [ Patrick Massot (Jan 15 2019 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problem%20with%20looping%20over%20finset/near/155178398):
<p>aren't you busy merging <a href="https://github.com/leanprover/mathlib/pull/583" target="_blank" title="https://github.com/leanprover/mathlib/pull/583">https://github.com/leanprover/mathlib/pull/583</a>?</p>

#### [ Patrick Massot (Jan 15 2019 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problem%20with%20looping%20over%20finset/near/155178422):
<p>Seriously I'd never thought of that interpretation</p>

#### [ AHan (Jan 15 2019 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problem%20with%20looping%20over%20finset/near/155178633):
<p>I mean looping over s, and  do something with every two distinct element in s.<br>
(Sorry for my bad English, don't know how to express this well...</p>

#### [ Mario Carneiro (Jan 15 2019 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problem%20with%20looping%20over%20finset/near/155178829):
<p>what are you trying to do in your loop? lean doesn't have "looping constructs" as such</p>

#### [ AHan (Jan 15 2019 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problem%20with%20looping%20over%20finset/near/155179031):
<p>if with <code>list</code> I can do something like </p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span>

<span class="n">def</span> <span class="n">test</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">list</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">list</span> <span class="bp">ℕ</span> <span class="o">:=</span>
<span class="n">do</span>
    <span class="n">x</span> <span class="bp">&lt;-</span> <span class="n">s</span><span class="o">,</span>
    <span class="n">y</span> <span class="bp">&lt;-</span> <span class="n">s</span><span class="o">,</span>
    <span class="o">[</span><span class="n">x</span> <span class="bp">+</span> <span class="n">y</span><span class="o">]</span>
</pre></div>

#### [ AHan (Jan 15 2019 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problem%20with%20looping%20over%20finset/near/155179136):
<p>I'm just wondering how to do this in if the given type is finset</p>

#### [ Mario Carneiro (Jan 15 2019 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problem%20with%20looping%20over%20finset/near/155179162):
<p>the left arrow is just notation for <code>list.bind</code>, you can call <code>finset.bind</code> and it's just the same</p>

#### [ Mario Carneiro (Jan 15 2019 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problem%20with%20looping%20over%20finset/near/155179221):
<p>I guess there is a missing monad instance for <code>finset</code> that would allow you to use the same notation</p>

#### [ AHan (Jan 15 2019 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problem%20with%20looping%20over%20finset/near/155179484):
<p>Oh! Thanks a lot !!</p>


{% endraw %}
