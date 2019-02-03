---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/68291latticelesupleftakasmileysinmathlib.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [lattice.le_sup_left' a.k.a. smileys in mathlib](https://leanprover-community.github.io/archive/116395maths/68291latticelesupleftakasmileysinmathlib.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Aug 05 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/lattice.le_sup_left%27%20a.k.a.%20smileys%20in%20mathlib/near/130925919):
<p>I thought it was time to learn about uniform spaces, and then I realised I had to learn about filters before that, and then I realised I had to learn about lattices before that.</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">set</span><span class="bp">.</span><span class="n">lattice</span>

<span class="bp">#</span><span class="kn">check</span> <span class="bp">@</span><span class="n">lattice</span><span class="bp">.</span><span class="n">le_sup_left</span>
<span class="c1">--  lattice.le_sup_left : ∀ {α : Type u_1} [_inst_1 : lattice.semilattice_sup α] {a b : α}, a ≤ a ⊔ b</span>
<span class="bp">#</span><span class="kn">check</span> <span class="bp">@</span><span class="n">lattice</span><span class="bp">.</span><span class="n">le_sup_left&#39;</span>
<span class="c1">-- lattice.le_sup_left&#39; : ∀ {α : Type u_1} [_inst_1 : lattice.semilattice_sup α] {a b : α}, a ≤ (:a ⊔ b:)</span>
</pre></div>


<p>What's with the smileys? This is one of those times when <code>#print notation (:</code> is useless -- it doesn't direct the user to what they actually want to know.</p>

#### [ Kevin Buzzard (Aug 05 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/lattice.le_sup_left%27%20a.k.a.%20smileys%20in%20mathlib/near/130926055):
<p>PS this is as far as I've got:</p>
<p><a href="https://xenaproject.wordpress.com/2018/08/04/what-is-a-filter-how-some-computer-scientists-think-about-limits/" target="_blank" title="https://xenaproject.wordpress.com/2018/08/04/what-is-a-filter-how-some-computer-scientists-think-about-limits/">https://xenaproject.wordpress.com/2018/08/04/what-is-a-filter-how-some-computer-scientists-think-about-limits/</a></p>
<p><a href="https://xenaproject.wordpress.com/2018/08/05/what-is-a-uniform-space-how-some-computer-scientists-think-about-completions/" target="_blank" title="https://xenaproject.wordpress.com/2018/08/05/what-is-a-uniform-space-how-some-computer-scientists-think-about-completions/">https://xenaproject.wordpress.com/2018/08/05/what-is-a-uniform-space-how-some-computer-scientists-think-about-completions/</a></p>
<p>and I'm now thinking of doing one on lattices because I still look at some filter code and see random bits of notation like <code>⊥</code> and <code>⨅</code> and I've not yet internalised what the lattice structure on filters is; I'm currently going about learning things the long way around by just reading some of this basic filter stuff -- I'm sure it can't be hard, but not knowing these basic things is holding me back a bit. I think Patrick went through the same thought process recently and now he's written a bunch of code for the perfectoid project about completions, and a desire to understand that has turned into a wider desire to understand some of these basic mathematical objects like filters and lattices which they don't actually seem to teach mathematicians.</p>

#### [ Chris Hughes (Aug 05 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/lattice.le_sup_left%27%20a.k.a.%20smileys%20in%20mathlib/near/130926161):
<p>I'm guessing it has something to do with the <code>ematch</code> attribute.</p>

#### [ Kevin Buzzard (Aug 05 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/lattice.le_sup_left%27%20a.k.a.%20smileys%20in%20mathlib/near/130926232):
<p>Oh yes they were talking about <code>ematch</code> earlier in the <code>order/lattice.lean</code> file; I'd not made the connection.</p>

#### [ Kevin Buzzard (Aug 05 2018 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/lattice.le_sup_left%27%20a.k.a.%20smileys%20in%20mathlib/near/130926281):
<p>Exhibit A:</p>
<div class="codehilite"><pre><span></span><span class="kn">section</span>
  <span class="kn">variable</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span>

  <span class="c1">-- TODO: this seems crazy, but it also seems to work reasonably well</span>
  <span class="bp">@</span><span class="o">[</span><span class="n">ematch</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">le_antisymm&#39;</span> <span class="o">[</span><span class="n">partial_order</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">},</span> <span class="o">(:</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">b</span> <span class="o">:)</span> <span class="bp">→</span> <span class="n">b</span> <span class="bp">≤</span> <span class="n">a</span> <span class="bp">→</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">b</span> <span class="o">:=</span>
  <span class="bp">@</span><span class="n">le_antisymm</span> <span class="bp">_</span> <span class="bp">_</span>
<span class="kn">end</span>
</pre></div>


<p>It's antiymmetry of &lt;= with some crazy smilies</p>

#### [ Chris Hughes (Aug 05 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/lattice.le_sup_left%27%20a.k.a.%20smileys%20in%20mathlib/near/130926344):
<p>I think <code>ematch</code> might have something to do with the equation compiler's automation for solving inequalities.</p>

#### [ Kevin Buzzard (Aug 05 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/lattice.le_sup_left%27%20a.k.a.%20smileys%20in%20mathlib/near/130926868):
<p>Check this out (from the top of <code>order/lattice.lean</code>)</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">sup_of_le_left</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">≤</span> <span class="n">a</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="err">⊔</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">a</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">apply</span> <span class="n">le_antisymm</span><span class="bp">;</span> <span class="n">finish</span>

<span class="kn">theorem</span> <span class="n">sup_of_le_right</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">b</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="err">⊔</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">b</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">apply</span> <span class="n">le_antisymm</span><span class="bp">;</span> <span class="n">finish</span>

<span class="kn">theorem</span> <span class="n">sup_le_sup</span> <span class="o">(</span><span class="n">h₁</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">h₂</span> <span class="o">:</span> <span class="n">c</span> <span class="bp">≤</span> <span class="n">d</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="err">⊔</span> <span class="n">c</span> <span class="bp">≤</span> <span class="n">b</span> <span class="err">⊔</span> <span class="n">d</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">finish</span>

<span class="kn">theorem</span> <span class="n">sup_le_sup_left</span> <span class="o">(</span><span class="n">h₁</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">c</span><span class="o">)</span> <span class="o">:</span> <span class="n">c</span> <span class="err">⊔</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">c</span> <span class="err">⊔</span> <span class="n">b</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">finish</span>

<span class="kn">theorem</span> <span class="n">sup_le_sup_right</span> <span class="o">(</span><span class="n">h₁</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">c</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="err">⊔</span> <span class="n">c</span> <span class="bp">≤</span> <span class="n">b</span> <span class="err">⊔</span> <span class="n">c</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">finish</span>

<span class="kn">theorem</span> <span class="n">le_of_sup_eq</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">a</span> <span class="err">⊔</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">b</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">b</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">finish</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">sup_idem</span> <span class="o">:</span> <span class="n">a</span> <span class="err">⊔</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">a</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">apply</span> <span class="n">le_antisymm</span><span class="bp">;</span> <span class="n">finish</span>

<span class="kn">instance</span> <span class="n">sup_is_idempotent</span> <span class="o">:</span> <span class="n">is_idempotent</span> <span class="n">α</span> <span class="o">(</span><span class="err">⊔</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">⟨@</span><span class="n">sup_idem</span> <span class="bp">_</span> <span class="bp">_⟩</span>

<span class="kn">theorem</span> <span class="n">sup_comm</span> <span class="o">:</span> <span class="n">a</span> <span class="err">⊔</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">b</span> <span class="err">⊔</span> <span class="n">a</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">apply</span> <span class="n">le_antisymm</span><span class="bp">;</span> <span class="n">finish</span>
</pre></div>


<p>Very slick automated proofs! Now write <code>set_option profiler true</code> at the top:</p>
<div class="codehilite"><pre><span></span>elaboration of sup_of_le_left took 264ms
elaboration of sup_of_le_right took 281ms
elaboration of sup_le_sup took 781ms
elaboration of sup_le_sup_left took 519ms
elaboration of sup_le_sup_right took 396ms
elaboration of le_of_sup_eq took 199ms
elaboration of sup_idem took 203ms
elaboration of sup_comm took 132ms
</pre></div>


<p>and compare with </p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">sup_of_le_left&#39;</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">≤</span> <span class="n">a</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="err">⊔</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">a</span> <span class="o">:=</span>
<span class="n">le_antisymm</span> <span class="o">(</span><span class="n">sup_le</span> <span class="o">(</span><span class="n">le_refl</span> <span class="bp">_</span><span class="o">)</span> <span class="n">h</span><span class="o">)</span> <span class="n">le_sup_left</span>
</pre></div>


<div class="codehilite"><pre><span></span>elaboration of sup_of_le_left&#39; took 7.54ms
</pre></div>


<p>etc. It saved the author of that file 30 seconds using automation instead of writing down the low-level proof, and now everyone who ever compiles mathlib has to pay an extra 250ms every time. Are the mathlib authors OK with that?</p>

#### [ Patrick Massot (Aug 05 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/lattice.le_sup_left%27%20a.k.a.%20smileys%20in%20mathlib/near/130927184):
<p>I think we should rather hope for optimized recompilation and available mathlib builds rather than avoiding automatization</p>

#### [ Kevin Buzzard (Aug 05 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/lattice.le_sup_left%27%20a.k.a.%20smileys%20in%20mathlib/near/130927534):
<p>I see. So in the long term these proofs are fine. Kenny would also point out that they use all three of Lean's spare axioms, but as far as I can see this is irrelevant in practice -- what we need to keep if possible is computation, because it makes proofs easier, and that's a different matter</p>

#### [ Kenny Lau (Aug 05 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/lattice.le_sup_left%27%20a.k.a.%20smileys%20in%20mathlib/near/130927594):
<p>does it use <code>quot.sound</code>?</p>

#### [ Chris Hughes (Aug 05 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/lattice.le_sup_left%27%20a.k.a.%20smileys%20in%20mathlib/near/130927673):
<p>I think a lot of people need to download mathlib before 250ms of their laptop's time is more expensive than 30 seconds of a person's time.</p>

#### [ Kevin Buzzard (Aug 05 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/lattice.le_sup_left%27%20a.k.a.%20smileys%20in%20mathlib/near/130927730):
<p>Finish does</p>

#### [ Kevin Buzzard (Aug 05 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/lattice.le_sup_left%27%20a.k.a.%20smileys%20in%20mathlib/near/130927754):
<p>I guess we need to start worrying when computers start writing mathlib then</p>

#### [ Patrick Massot (Aug 05 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/lattice.le_sup_left%27%20a.k.a.%20smileys%20in%20mathlib/near/130930180):
<blockquote>
<p>PS this is as far as I've got:</p>
<p><a href="https://xenaproject.wordpress.com/2018/08/04/what-is-a-filter-how-some-computer-scientists-think-about-limits/" target="_blank" title="https://xenaproject.wordpress.com/2018/08/04/what-is-a-filter-how-some-computer-scientists-think-about-limits/">https://xenaproject.wordpress.com/2018/08/04/what-is-a-filter-how-some-computer-scientists-think-about-limits/</a></p>
<p><a href="https://xenaproject.wordpress.com/2018/08/05/what-is-a-uniform-space-how-some-computer-scientists-think-about-completions/" target="_blank" title="https://xenaproject.wordpress.com/2018/08/05/what-is-a-uniform-space-how-some-computer-scientists-think-about-completions/">https://xenaproject.wordpress.com/2018/08/05/what-is-a-uniform-space-how-some-computer-scientists-think-about-completions/</a></p>
</blockquote>
<p>Nice posts! But I think the titles are a bit unfair to Bourbaki, and especially to André Weil. Actually this is a story I keep telling people when I try to explain proof assistants. Boubaki invented filters because they were facing the exact same issue that proof assistants are facing. They wanted to prove everything without repeating statements and proofs again and again. It really makes sense that we are using the solution those very clever guys invented for that purpose.</p>

#### [ Patrick Massot (Aug 05 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/lattice.le_sup_left%27%20a.k.a.%20smileys%20in%20mathlib/near/130930237):
<p>Actually your first post may fail to convey the combinatorial explosion here. Filters also handle functions converging at a point or at infinity in  a topological space, or at plus or minus infinity in R, or limits from the left or from the right at some real number.</p>

#### [ Kevin Buzzard (Aug 05 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/lattice.le_sup_left%27%20a.k.a.%20smileys%20in%20mathlib/near/130930238):
<p>I mention Weil briefly, and Bourbaki not at all, despite being well aware that this is where this sort of stuff started to appear. I can add some comments.</p>

#### [ Kevin Buzzard (Aug 05 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/lattice.le_sup_left%27%20a.k.a.%20smileys%20in%20mathlib/near/130930286):
<p>I just sat down and wrote something -- I don't really know what a filter is at all apart from what I read on Wikipedia the other day and what I worked out as a consequence. Patrick do you know how to pronounce <code>tendsto f F_X F_Y</code>? Is it "f of filter F_X tends to F_Y" or what?</p>

#### [ Patrick Massot (Aug 05 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/lattice.le_sup_left%27%20a.k.a.%20smileys%20in%20mathlib/near/130930300):
<p>Also don't forget that filters kill all the epsilon/4 nonsense.</p>

#### [ Patrick Massot (Aug 05 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/lattice.le_sup_left%27%20a.k.a.%20smileys%20in%20mathlib/near/130930344):
<p>I don't know how to pronounce anything here, I never used filters before using Lean</p>

#### [ Kevin Buzzard (Aug 05 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/lattice.le_sup_left%27%20a.k.a.%20smileys%20in%20mathlib/near/130930400):
<p>I realised when I was writing the filter post that I didn't even know how to say the concepts I was trying to explain.</p>

#### [ Patrick Massot (Aug 05 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/lattice.le_sup_left%27%20a.k.a.%20smileys%20in%20mathlib/near/130930448):
<p>Maybe the uniform space post could include a brief description of the separatedness issue, since you describe completeness and then mention a Hausdorff completion</p>

#### [ Patrick Massot (Aug 05 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/lattice.le_sup_left%27%20a.k.a.%20smileys%20in%20mathlib/near/130930698):
<p>Another random comment: about uniform structure, it may be worth pointing out the analogy with distances coming from norms. A norm N measures distance to 0, and one get a distance d(x, y) = N(y-x). In a (commutative) topological group the topology gives a way to say "close to zero" and the same trick applies, giving a uniform structure. I think uniting this case with the metric space case was Weil's motivation.</p>


{% endraw %}
