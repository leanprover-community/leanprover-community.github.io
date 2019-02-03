---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/85801computabledivisionbynonzeroreal.html
---

## Stream: [maths](index.html)
### Topic: [computable division by non-zero real](85801computabledivisionbynonzeroreal.html)

---


{% raw %}
#### [ Kevin Buzzard (Aug 09 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131188580):
<p>If I have a proof that <code>r : ℝ</code> is non-zero, can I make <code>def f : ℝ → ℝ := λ x, x / r</code> computable?</p>

#### [ Mario Carneiro (Aug 09 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131188609):
<p>if you have <code>r^-1</code>, then it's just multiplication</p>

#### [ Kevin Buzzard (Aug 09 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131188681):
<p>I ask because Luca has a bunch of these, and he's ended up making his entire file <code>noncomputable theory</code> to shut Lean up, with the result that we're going to end up with a noncomputable fundamental group. Is that inevitable though?</p>

#### [ Mario Carneiro (Aug 09 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131188692):
<p>but a proof that r is nonzero is not sufficient to compute a Cauchy sequence, you need a rational lower bound</p>

#### [ Kevin Buzzard (Aug 09 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131188698):
<p>His definition of the topology on [0,1] was noncomputable -- that didn't look like a good start</p>

#### [ Mario Carneiro (Aug 09 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131188755):
<p>topologies are trivially computable</p>

#### [ Kevin Buzzard (Aug 09 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131188789):
<p>I feel like we could fix all this because he wrote a bunch of stuff for general closed intervals <code>[r,s]</code>with only the hypothesis <code>s&gt;r</code>, however his applications tend to be <code>[0,1/2]</code> or <code>[0,1/4]</code></p>

#### [ Mario Carneiro (Aug 09 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131188820):
<p>if you give me a noncomputable definition of a topology, I can define a computable topology that is defeq</p>

#### [ Mario Carneiro (Aug 09 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131188832):
<p>because topologies have no data</p>

#### [ Mario Carneiro (Aug 09 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131188933):
<p>Why is the fundamental group noncomputable?</p>

#### [ Mario Carneiro (Aug 09 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131188944):
<p>what are the steps of construction that are problematic</p>

#### [ Kevin Buzzard (Aug 09 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189025):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">topology</span><span class="bp">.</span><span class="n">topological_space</span>
<span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">real</span>
<span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>

<span class="n">def</span> <span class="n">I01</span> <span class="o">:=</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">|</span> <span class="mi">0</span> <span class="bp">≤</span> <span class="n">x</span> <span class="bp">∧</span> <span class="n">x</span> <span class="bp">≤</span> <span class="mi">1</span><span class="o">}</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">I01</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">unfold</span> <span class="n">I01</span><span class="bp">;</span> <span class="n">apply_instance</span>
<span class="c1">-- definition &#39;I01.topological_space&#39; is noncomputable, it depends on &#39;real.metric_space&#39;</span>
</pre></div>

#### [ Mario Carneiro (Aug 09 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189051):
<p>real.metric_space is noncomputable?</p>

#### [ Mario Carneiro (Aug 09 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189069):
<p>oh of course, the distance function is a max</p>

#### [ Mario Carneiro (Aug 09 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189070):
<p>anyway it doesn't matter</p>

#### [ Kenny Lau (Aug 09 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189074):
<p>why is Kevin worrying about computability?</p>

#### [ Mario Carneiro (Aug 09 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189124):
<p>let the instance be noncomputable</p>

#### [ Mario Carneiro (Aug 09 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189134):
<p>it won't cause any problems</p>

#### [ Kevin Buzzard (Aug 09 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189144):
<p>The fundamental group is noncomputable currently because if you want a map from [0,1/2] to [0,1] you can either define it as lam x, 2 * x, or you can define a general map from [r,s] to [0,1] as lam x, (x-r)/(s-r), and use that function everywhere in your file, and fix all the noncomputable errors by writing <code>noncomputable theory</code> at the top, and nobody noticing until the file is 1000 lines long.</p>

#### [ Mario Carneiro (Aug 09 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189160):
<p>none of that matters</p>

#### [ Kevin Buzzard (Aug 09 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189166):
<p>oh great :-)</p>

#### [ Kevin Buzzard (Aug 09 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189177):
<p>The definition of the multiplication on paths is noncomputable</p>

#### [ Mario Carneiro (Aug 09 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189186):
<p>that checks out</p>

#### [ Kevin Buzzard (Aug 09 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189191):
<p>So that's OK?</p>

#### [ Mario Carneiro (Aug 09 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189237):
<p>you have to define it by cases on whether you are greater or less than 1/2</p>

#### [ Kevin Buzzard (Aug 09 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189238):
<p>right</p>

#### [ Kevin Buzzard (Aug 09 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189246):
<p>but Luca's implementation uses the map from [r,s] to [0,1] defined using division</p>

#### [ Kevin Buzzard (Aug 09 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189249):
<p>with r=0 and s=1/2</p>

#### [ Kevin Buzzard (Aug 09 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189253):
<p>and then with r=1/2 and s=1</p>

#### [ Mario Carneiro (Aug 09 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189256):
<p>I often claim that when the function being defined is continuous you can do it without noncomputability, but in a general top space I'm not sure</p>

#### [ Mario Carneiro (Aug 09 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189282):
<p>division by 2?</p>

#### [ Mario Carneiro (Aug 09 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189332):
<p>I thought you meant real division - division by 2 is easy</p>

#### [ Kevin Buzzard (Aug 09 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189333):
<blockquote>
<p>why is Kevin worrying about computability?</p>
</blockquote>
<p>I don't worry about it in general, I was just surprised to see it here. Were you virtually at my lecture a week last Monday? The example of G(3) made it clear to me what computability was.</p>

#### [ Kevin Buzzard (Aug 09 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189345):
<p>we're dividing by s-r</p>

#### [ Kevin Buzzard (Aug 09 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189354):
<p>using a general function which divides by s-r</p>

#### [ Kevin Buzzard (Aug 09 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189359):
<p>in the special case where s-r=1/2</p>

#### [ Kevin Buzzard (Aug 09 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189391):
<p>and when doing associativity s-r will be 1/4</p>

#### [ Mario Carneiro (Aug 09 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189448):
<p>those could all be rationals</p>

#### [ Mario Carneiro (Aug 09 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189460):
<p>just do your s-r trick where s and r are rationals</p>

#### [ Kevin Buzzard (Aug 09 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189462):
<p>rofl</p>

#### [ Mario Carneiro (Aug 09 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189501):
<p>But path multiplication will still be noncomputable because of the pasting you have to do</p>

#### [ Mario Carneiro (Aug 09 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189571):
<p>if you have f g : [0,1] -&gt; X and you want to concatenate them, you define <code>(f * g) x = if x &lt; 1/2 then f(2*x) else g(2*x-1)</code></p>

#### [ Kevin Buzzard (Aug 09 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189662):
<p>aie you're right</p>

#### [ Mario Carneiro (Aug 09 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189663):
<p>I think if you wanted to do that computably, you could define it by that equation on rationals, then take the limit as the sequence of rationals approaches some real</p>

#### [ Mario Carneiro (Aug 09 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189679):
<p>but then you have to have a computable limit operation on the target topological space</p>

#### [ Kevin Buzzard (Aug 09 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189691):
<p>I think this is all too much for Luca's project, I think we might stick to noncomputable</p>

#### [ Kevin Buzzard (Aug 09 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189697):
<p>I'm glad I mentioned this now, I can go back to thinking computable maths is all a bit silly for a while.</p>

#### [ Kevin Buzzard (Aug 09 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189716):
<p>What I'm trying to do nowadays is to get some sort of feeling for when I am actually being noncomputable. Like when I was a PhD student and I got some sort of a feeling for when I was actually using the axiom of choice</p>

#### [ Kevin Buzzard (Aug 09 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189759):
<p>or when I was a post-doc and I got some sort of a feeling for when I was actually using universes</p>

#### [ Mario Carneiro (Aug 09 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189768):
<p>rule of thumb: if you use anything descendent from <code>topological_space.lean</code> or <code>analysis/real.lean</code>, just put <code>noncomputable theory</code> and don't attempt to get away from it</p>

#### [ Kevin Buzzard (Aug 09 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189772):
<p>[answer: probably never, although it was difficult to find a reference sometimes]</p>

#### [ Mario Carneiro (Aug 09 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189788):
<p>If all your imports are in <code>data</code> you should try to be computable</p>

#### [ Kevin Buzzard (Aug 09 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189817):
<p>Well Luca's file uses lots of stuff from both of those files, so we'll have to be noncomputable for now. Kenny can fix it all up when he's finished</p>

#### [ Mario Carneiro (Aug 09 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189824):
<p>topology is 100% classical maths</p>

#### [ Kevin Buzzard (Aug 09 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189888):
<p>I'm surprised. I didn't realise that.</p>

#### [ Mario Carneiro (Aug 09 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189893):
<p>and metric spaces and uniform spaces...</p>

#### [ Kevin Buzzard (Aug 09 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189914):
<p>Metric spaces I can understand because they mention reals.</p>

#### [ Mario Carneiro (Aug 09 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189922):
<p>it could conceivably be different but it would require a major rewrite of the library</p>

#### [ Mario Carneiro (Aug 09 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189937):
<p><code>data.real.basic</code> is computable, <code>analysis.real</code> is not</p>

#### [ Kevin Buzzard (Aug 09 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131189960):
<p>Metric spaces also often use countable dependent choice, because the two definitions of closure only coincide when you are able to choose a sequence of points in your space tending to a point in the closure, which involves choosing <code>x_n</code> at distance at most <code>1/n</code> from the boundary point</p>

#### [ Mario Carneiro (Aug 09 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131190030):
<p>well, that's just first countable spaces in general</p>

#### [ Mario Carneiro (Aug 09 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131190053):
<p>but there I'm not so worried because all the claims are propositional anyway</p>

#### [ Mario Carneiro (Aug 09 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131190069):
<p>we make no attempt to avoid the axiom of choice in theorems</p>

#### [ Chris Hughes (Aug 09 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131190413):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>

<span class="n">def</span> <span class="n">computable_inv</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">≠</span> <span class="mi">0</span> <span class="bp">→</span> <span class="n">ℝ</span> <span class="o">:=</span>
<span class="n">quotient</span><span class="bp">.</span><span class="n">hrec_on</span> <span class="n">x</span>
<span class="o">(</span><span class="bp">λ</span> <span class="n">x</span> <span class="o">(</span><span class="n">hx</span> <span class="o">:</span> <span class="n">real</span><span class="bp">.</span><span class="n">mk</span> <span class="n">x</span> <span class="bp">≠</span> <span class="mi">0</span><span class="o">),</span> <span class="n">real</span><span class="bp">.</span><span class="n">mk</span>
  <span class="o">(</span><span class="n">cau_seq</span><span class="bp">.</span><span class="n">inv</span> <span class="n">x</span> <span class="o">(</span><span class="n">mt</span> <span class="n">real</span><span class="bp">.</span><span class="n">mk_eq_zero</span><span class="bp">.</span><span class="mi">2</span> <span class="n">hx</span><span class="o">)))</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span> <span class="n">h</span><span class="o">,</span> <span class="k">begin</span>
    <span class="k">have</span> <span class="o">:</span> <span class="n">real</span><span class="bp">.</span><span class="n">mk</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">real</span><span class="bp">.</span><span class="n">mk</span> <span class="n">b</span> <span class="o">:=</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">sound</span> <span class="n">h</span><span class="o">,</span>
    <span class="n">refine</span> <span class="n">function</span><span class="bp">.</span><span class="n">hfunext</span> <span class="o">(</span><span class="k">by</span> <span class="n">rw</span> <span class="n">this</span><span class="o">)</span>
      <span class="o">(</span><span class="bp">λ</span> <span class="n">h₁</span> <span class="n">h₂</span> <span class="bp">_</span><span class="o">,</span> <span class="n">heq_of_eq</span> <span class="bp">_</span><span class="o">),</span>
    <span class="n">refine</span> <span class="o">(</span><span class="n">domain</span><span class="bp">.</span><span class="n">mul_right_inj</span> <span class="n">h₁</span><span class="o">)</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">_</span><span class="o">,</span>
    <span class="n">conv</span> <span class="o">{</span><span class="n">to_rhs</span><span class="o">,</span> <span class="n">congr</span><span class="o">,</span> <span class="n">skip</span><span class="o">,</span> <span class="n">rw</span> <span class="n">this</span><span class="o">},</span>
    <span class="n">refine</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">sound</span> <span class="bp">_</span><span class="o">,</span>
    <span class="n">refine</span> <span class="n">setoid</span><span class="bp">.</span><span class="n">trans</span> <span class="o">(</span><span class="n">cau_seq</span><span class="bp">.</span><span class="n">inv_mul_cancel</span> <span class="o">(</span><span class="n">mt</span> <span class="n">real</span><span class="bp">.</span><span class="n">mk_eq_zero</span><span class="bp">.</span><span class="mi">2</span> <span class="n">h₁</span><span class="o">))</span>
      <span class="o">(</span><span class="n">setoid</span><span class="bp">.</span><span class="n">symm</span> <span class="o">(</span><span class="n">cau_seq</span><span class="bp">.</span><span class="n">inv_mul_cancel</span> <span class="o">(</span><span class="n">mt</span> <span class="n">real</span><span class="bp">.</span><span class="n">mk_eq_zero</span><span class="bp">.</span><span class="mi">2</span> <span class="n">h₂</span><span class="o">)))</span>
  <span class="kn">end</span><span class="o">)</span>
</pre></div>

#### [ Mario Carneiro (Aug 09 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131190434):
<p>Yeah, I double checked the proof in data.real.basic and it can definitely be defined... I'm not sure why I didn't try</p>

#### [ Chris Hughes (Aug 09 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131190547):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">computable_inv_mul_cancel</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:</span> <span class="bp">Π</span> <span class="n">hx</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">≠</span> <span class="mi">0</span><span class="o">,</span>
  <span class="n">computable_inv</span> <span class="n">x</span> <span class="n">hx</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="n">quotient</span><span class="bp">.</span><span class="n">induction_on</span> <span class="n">x</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span> <span class="n">hx</span><span class="o">,</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">sound</span> <span class="o">(</span><span class="n">cau_seq</span><span class="bp">.</span><span class="n">inv_mul_cancel</span> <span class="bp">_</span><span class="o">))</span>
</pre></div>

#### [ Chris Hughes (Aug 09 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131190657):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> you still haven't explained why you care about computable reals?</p>

#### [ Mario Carneiro (Aug 09 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131190733):
<p>Oh, I found a counterexample for the computability claim. Let <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>X</mi></mrow><annotation encoding="application/x-tex">X</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.07847em;">X</span></span></span></span> be a quotient of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi mathvariant="double-struck">R</mi></mrow><annotation encoding="application/x-tex">\Bbb R</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68889em;"></span><span class="strut bottom" style="height:0.68889em;vertical-align:0em;"></span><span class="base"><span class="mord mathbb">R</span></span></span></span> identifying all points in <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>[</mo><mn>1</mn><mo separator="true">,</mo><mn>2</mn><mo>]</mo></mrow><annotation encoding="application/x-tex">[1,2]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mopen">[</span><span class="mord mathrm">1</span><span class="mpunct">,</span><span class="mord mathrm">2</span><span class="mclose">]</span></span></span></span>. Let <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>x</mi></mrow><annotation encoding="application/x-tex">f(x)=x</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mopen">(</span><span class="mord mathit">x</span><span class="mclose">)</span><span class="mrel">=</span><span class="mord mathit">x</span></span></span></span> and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>g</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>x</mi><mo>+</mo><mn>2</mn></mrow><annotation encoding="application/x-tex">g(x)=x+2</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.03588em;">g</span><span class="mopen">(</span><span class="mord mathit">x</span><span class="mclose">)</span><span class="mrel">=</span><span class="mord mathit">x</span><span class="mbin">+</span><span class="mord mathrm">2</span></span></span></span>; these are continuous functions on <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>[</mo><mn>0</mn><mo separator="true">,</mo><mn>1</mn><mo>]</mo></mrow><annotation encoding="application/x-tex">[0,1]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mopen">[</span><span class="mord mathrm">0</span><span class="mpunct">,</span><span class="mord mathrm">1</span><span class="mclose">]</span></span></span></span> such that <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>f</mi><mo>(</mo><mn>1</mn><mo>)</mo><mo>=</mo><mo>[</mo><mn>1</mn><mo>]</mo><mo>=</mo><mo>[</mo><mn>2</mn><mo>]</mo><mo>=</mo><mi>g</mi><mo>(</mo><mn>0</mn><mo>)</mo></mrow><annotation encoding="application/x-tex">f(1)=[1]=[2]=g(0)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mopen">(</span><span class="mord mathrm">1</span><span class="mclose">)</span><span class="mrel">=</span><span class="mopen">[</span><span class="mord mathrm">1</span><span class="mclose">]</span><span class="mrel">=</span><span class="mopen">[</span><span class="mord mathrm">2</span><span class="mclose">]</span><span class="mrel">=</span><span class="mord mathit" style="margin-right:0.03588em;">g</span><span class="mopen">(</span><span class="mord mathrm">0</span><span class="mclose">)</span></span></span></span>, and both functions are computable. The path concatenation <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>f</mi><mo>∗</mo><mi>g</mi></mrow><annotation encoding="application/x-tex">f\ast g</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mbin">∗</span><span class="mord mathit" style="margin-right:0.03588em;">g</span></span></span></span> is discontinuous at <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mn>1</mn><mi mathvariant="normal">/</mi><mn>2</mn></mrow><annotation encoding="application/x-tex">1/2</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathrm">1</span><span class="mord mathrm">/</span><span class="mord mathrm">2</span></span></span></span> (in the real topology), so it is not computably definable.</p>

#### [ Kevin Buzzard (Aug 09 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/computable%20division%20by%20non-zero%20real/near/131190754):
<p>Because Luca was dividing by a positive real which I could prove was greater than 1/10 and so I realised that probably I could make some of his noncomputable code computable. I hence wondered whether it would be an easy fix to make his fundamental group computable. But as Mario pointed out, there are other problems with computability, and I've now decided not to worry about it.</p>


{% endraw %}
