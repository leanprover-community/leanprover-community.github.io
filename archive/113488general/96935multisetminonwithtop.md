---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/96935multisetminonwithtop.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [multiset min on with_top](https://leanprover-community.github.io/archive/113488general/96935multisetminonwithtop.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Jul 12 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset%20min%20on%20with_top/near/129562759):
<p>Back in the days before <code>with_top</code> I rolled my own instance of <code>decidable_linear_order (option nat)</code> (with <code>none</code> = +infinity), and defined <code>min</code> on <code>multiset (option nat)</code> as <code>lam s, multiset.fold (min) none s</code>. It compiled and worked fine and I thought no more about it. </p>
<p>In a fit of tidying up today, I decided that rather than leaving those 60 lines of code in my repo I could just switch to <code>with_top</code>; however to my mild surprise (because I didn't remember doing anything clever)</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">multiset</span>

<span class="kn">definition</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">min</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">multiset</span> <span class="o">(</span><span class="n">with_top</span> <span class="bp">ℕ</span><span class="o">))</span> <span class="o">:</span> <span class="n">with_top</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="n">multiset</span><span class="bp">.</span><span class="n">fold</span> <span class="n">min</span> <span class="n">none</span> <span class="n">s</span>
</pre></div>


<p>fails -- for <code>fold</code> to work like this on a multiset we need a proof that <code>min</code> is commutative and associative on <code>with_top nat</code>, and type class inference fails to find these things. So I went back to my original work and found that in my home-grown linear order associativity seemed to come from <code>lattice.inf_is_associative</code>, because for me <code>@lattice.has_inf.inf (option nat) _ = min</code> was <code>rfl</code> but for <code>with_top nat</code> it's apparently not. I would just create an instance of <code>is_commutative (with_top nat) min</code> and of <code>is_associative (with_top nat) min</code> (or more generally a proof that if min is commutative on <code>X</code> then it's commutative on <code>with_top X</code> etc) but because I've seen with my own eyes this devious trick which I inadvertently pulled off using lattice infs I wonder whether there is a better approach; I decided that asking here was a better idea than creating noisy irrelevant PRs.</p>

#### [ Mario Carneiro (Jul 18 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset%20min%20on%20with_top/near/129861837):
<p>I think this just needs to be copied from <code>finset.min</code></p>

#### [ Chris Hughes (Jul 19 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset%20min%20on%20with_top/near/129898775):
<p>On a related note, is there a case for making <code>min</code> and <code>max</code> return values in <code>with_top</code>  and <code>with_bot</code> instead of <code>option</code>? I needed the theorem <code>s ⊆ t -&gt; max s ≤ max t</code> for polynomials, but there's no order on option.</p>

#### [ Patrick Massot (Jul 19 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset%20min%20on%20with_top/near/129899857):
<p>Kenny's work on valuations includes putting an order on <code>option a</code> from an order on <code>a</code>. But I'd prefer to see semantic names used instead of <code>option</code></p>

#### [ Kenny Lau (Jul 19 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset%20min%20on%20with_top/near/129899860):
<p>I think that's just what we now call <code>with_bot</code></p>

#### [ Mario Carneiro (Jul 19 2018 at 06:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/multiset%20min%20on%20with_top/near/129910548):
<p>You can use <code>sup</code> and <code>inf</code> instead of <code>min</code> and <code>max</code> for a more order-based definition</p>


{% endraw %}
