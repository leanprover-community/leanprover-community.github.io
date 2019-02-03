---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/48739euclideandomain.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [euclidean domain](https://leanprover-community.github.io/archive/116395maths/48739euclideandomain.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Nov 15 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domain/near/147742225):
<p>Euclidean domains are extending integral domains, but the entire file doesn't use this. We could just as well extend <code>comm_ring</code>. <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> Do you know if every <em>Euclidean ring</em> is automatically an integral domain?</p>

#### [ Chris Hughes (Nov 15 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domain/near/147742459):
<p>I think the following theorems imply they are</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">mul_div_cancel</span> <span class="o">(</span><span class="n">a</span><span class="o">)</span> <span class="o">{</span><span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">b0</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">≠</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">a</span> <span class="bp">*</span> <span class="n">b</span><span class="o">)</span> <span class="bp">/</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">a</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">rw</span> <span class="n">mul_comm</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">mul_div_cancel_left</span> <span class="n">a</span> <span class="n">b0</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">zero_div</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">a0</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≠</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">/</span> <span class="n">a</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">simpa</span> <span class="n">only</span> <span class="o">[</span><span class="n">zero_mul</span><span class="o">]</span> <span class="kn">using</span> <span class="n">mul_div_cancel</span> <span class="mi">0</span> <span class="n">a0</span>
</pre></div>

#### [ Johan Commelin (Nov 15 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domain/near/147742484):
<p>Good catch!</p>

#### [ Johan Commelin (Nov 15 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domain/near/147742532):
<p>Chris and Lean helped me prove a theorem!</p>

#### [ Chris Hughes (Nov 15 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domain/near/147744070):
<p>Wait, I was wrong. There's no way to prove <code>zero_ne_one</code>.</p>

#### [ Reid Barton (Nov 15 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domain/near/147744291):
<p>Both a theorem, and a counterexample <span class="emoji emoji-1f642" title="slight smile">:slight_smile:</span></p>

#### [ Johan Commelin (Nov 15 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domain/near/147745230):
<p>Haha, sure. Zerology bites me again.</p>

#### [ Chris Hughes (Nov 15 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domain/near/147755173):
<p>Maybe it should extend <code>nonzero_comm_ring</code> instead.</p>

#### [ Johan Commelin (Nov 15 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domain/near/147758098):
<p>Wouldn't that create a possibility for diamonds? Say we prove that integral closures are integral domains. And then for certain of those we prove that they are euclidean rings. And then this would give a new proof that those things are integral domains...</p>

#### [ Johan Commelin (Nov 15 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domain/near/147758146):
<p>Maybe we should just have <code>euclidean.core</code> and then <code>of_core</code>... that seems to be a common trick.</p>

#### [ Chris Hughes (Nov 15 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domain/near/147758439):
<p>Yes, but they would be definitionally equal diamonds, which happen all the time and are fine.</p>

#### [ Johan Commelin (Nov 15 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domain/near/147758480):
<p>Why would they be defeq? Because <code>integral_domain</code> extends <code>comm_ring</code> by a <code>Prop</code>?</p>

#### [ Chris Hughes (Nov 15 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domain/near/147758635):
<p>But all the fields would be the same, because they all come from the same place ultimately.</p>

#### [ Johan Commelin (Nov 15 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domain/near/147758657):
<p>No we would have two different proofs that certain rings are integral domains...</p>

#### [ Johan Commelin (Nov 15 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domain/near/147758675):
<p>One coming from the fact that it's an integral closure, the other from the fact that it is a euclidean ring</p>

#### [ Chris Hughes (Nov 15 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domain/near/147758682):
<p>Proofs are irrelevant.</p>
<p>The same thing happens with say, polynomials over an integral domain are an integral domain which means they're a ring, but polynomials over a ring are a ring. So there's two different paths, but they're defeq.</p>

#### [ Johan Commelin (Nov 15 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domain/near/147758765):
<p>Ok, good.</p>

#### [ Chris Hughes (Nov 15 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domain/near/147759127):
<p>This worked when I tried changing integral domain.</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="n">euclidean_domain</span><span class="bp">.</span><span class="n">integral_domain</span> <span class="bp">ℤ</span> <span class="bp">=</span> <span class="n">linear_ordered_comm_ring</span><span class="bp">.</span><span class="n">to_integral_domain</span> <span class="o">:=</span> <span class="n">rfl</span>
</pre></div>

#### [ Johan Commelin (Nov 15 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domain/near/147762970):
<p>Great!</p>


{% endraw %}
