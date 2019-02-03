---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/25792zeroideal.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [zero ideal](https://leanprover-community.github.io/archive/116395maths/25792zeroideal.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Dec 17 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ideal/near/152032669):
<p>I lost the zero ideal during the module refactor. Does anyone know where it ended up?</p>

#### [ Johan Commelin (Dec 17 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ideal/near/152032688):
<p>I guess it is now <code>⊥</code></p>

#### [ Patrick Massot (Dec 17 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ideal/near/152032759):
<p>Thanks</p>

#### [ Patrick Massot (Dec 17 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ideal/near/152032784):
<p>I'm a very slow learner. I was looking for something named zero</p>

#### [ Kenny Lau (Dec 17 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ideal/near/152032827):
<p>lol</p>

#### [ Kenny Lau (Dec 17 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ideal/near/152032844):
<p>"I lost something" -- what is it? "I lost the zero ideal"</p>

#### [ Johan Commelin (Dec 17 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ideal/near/152032859):
<blockquote>
<p>I'm a very slow learner. I was looking for something named zero</p>
</blockquote>
<p>That would be too easy.</p>

#### [ Patrick Massot (Dec 17 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ideal/near/152032888):
<p>Who would think that zero is a more natural thing than the bottom of a lattice nowadays?</p>

#### [ Patrick Massot (Dec 17 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ideal/near/152033162):
<p><code>ideal.mul_mem_left : ∀ {α : Type u_1} [_inst_1 : comm_ring α] (I : ideal α) {a b : α}, b ∈ I → a * b ∈ I</code> What happened to binder types here?</p>

#### [ Kenny Lau (Dec 17 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ideal/near/152033212):
<p>what binder types?</p>

#### [ Patrick Massot (Dec 17 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ideal/near/152033393):
<p>Why not</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">ideal</span><span class="bp">.</span><span class="n">mul_mem_left&#39;</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">I</span> <span class="o">:</span> <span class="n">ideal</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">{</span><span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">b</span> <span class="err">∈</span> <span class="n">I</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">*</span> <span class="n">b</span> <span class="err">∈</span> <span class="n">I</span> <span class="o">:=</span>
<span class="n">ideal</span><span class="bp">.</span><span class="n">mul_mem_left</span> <span class="bp">_</span> <span class="n">h</span>
</pre></div>

#### [ Patrick Massot (Dec 17 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ideal/near/152033413):
<p>Like, I want <code>a</code> and <code>b ∈ I</code> to be explicit, and everything else implicit</p>

#### [ Kenny Lau (Dec 17 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ideal/near/152033432):
<p>because we want to write <code>I.mul_mem_left _ _</code></p>

#### [ Patrick Massot (Dec 17 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ideal/near/152033567):
<p>And how does it guess who is <code>a</code>?</p>

#### [ Kenny Lau (Dec 17 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ideal/near/152033607):
<p>from the type</p>

#### [ Patrick Massot (Dec 17 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/zero%20ideal/near/152033761):
<p>hmm</p>


{% endraw %}
