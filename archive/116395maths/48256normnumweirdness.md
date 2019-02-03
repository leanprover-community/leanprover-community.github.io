---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/48256normnumweirdness.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [norm_num weirdness](https://leanprover-community.github.io/archive/116395maths/48256normnumweirdness.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Jan 18 2019 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156327693):
<p>What's going on here?</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">norm_num</span>
<span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">lemma</span> <span class="n">floor_iff_bounds</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">z</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span>
<span class="err">↑</span><span class="n">z</span> <span class="bp">≤</span> <span class="n">r</span> <span class="bp">∧</span> <span class="n">r</span> <span class="bp">&lt;</span> <span class="o">(</span><span class="n">z</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">↔</span> <span class="err">⌊</span> <span class="n">r</span> <span class="err">⌋</span> <span class="bp">=</span> <span class="n">z</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span><span class="n">le_floor</span><span class="o">,</span> <span class="err">←</span><span class="n">int</span><span class="bp">.</span><span class="n">cast_one</span><span class="o">,</span> <span class="err">←</span><span class="n">int</span><span class="bp">.</span><span class="n">cast_add</span><span class="o">,</span> <span class="err">←</span><span class="n">floor_lt</span><span class="o">,</span>
  <span class="n">int</span><span class="bp">.</span><span class="n">lt_add_one_iff</span><span class="o">,</span> <span class="n">le_antisymm_iff</span><span class="o">,</span> <span class="n">and</span><span class="bp">.</span><span class="n">comm</span><span class="o">]</span>

<span class="c1">-- set_option pp.all true</span>
<span class="kn">theorem</span> <span class="n">floor_example</span> <span class="o">:</span> <span class="n">floor</span> <span class="o">(</span><span class="mi">71</span><span class="bp">/</span><span class="mi">10</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">7</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">rw</span> <span class="err">←</span><span class="n">floor_iff_bounds</span><span class="o">,</span>
  <span class="n">split</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">norm_num</span><span class="o">},</span>
  <span class="c1">-- ⊢ 71 / 10 &lt; ↑7 + 1</span>
  <span class="c1">-- norm_num, -- seems to hang</span>
<span class="n">suffices</span> <span class="o">:</span> <span class="o">(</span><span class="mi">71</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">/</span> <span class="mi">10</span> <span class="bp">&lt;</span> <span class="mi">7</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">,</span>
  <span class="n">simpa</span> <span class="kn">using</span> <span class="n">this</span><span class="o">,</span>
  <span class="c1">-- ⊢ 71 / 10 &lt; 7 + 1</span>
  <span class="c1">-- norm_num -- deterministic timeout</span>
  <span class="n">sorry</span>
<span class="kn">end</span>

<span class="kn">example</span> <span class="o">:</span> <span class="o">(</span><span class="mi">71</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">/</span> <span class="mi">10</span> <span class="bp">&lt;</span> <span class="mi">7</span> <span class="bp">+</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="c1">-- ⊢ 71 / 10 &lt; 7 + 1</span>
  <span class="c1">-- exactly the same term as the sorry above</span>
  <span class="c1">-- even with pp.all true</span>
  <span class="n">norm_num</span> <span class="c1">-- works fine?!</span>
<span class="kn">end</span>
</pre></div>


<p>Inside the bigger proof, I can't get norm_num to work, even though with pp.all on the goal seems to be exactly the same as the simpler example, where <code>norm_num</code> works fine. I checked the types with diff and there was no difference (unless I did something stupid)</p>

#### [ Bryan Gin-ge Chen (Jan 18 2019 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156328876):
<p>And lean is happy with this:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">norm_num</span>
<span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">lemma</span> <span class="n">floor_iff_bounds</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">z</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span>
<span class="err">↑</span><span class="n">z</span> <span class="bp">≤</span> <span class="n">r</span> <span class="bp">∧</span> <span class="n">r</span> <span class="bp">&lt;</span> <span class="o">(</span><span class="n">z</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">↔</span> <span class="err">⌊</span> <span class="n">r</span> <span class="err">⌋</span> <span class="bp">=</span> <span class="n">z</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span><span class="n">le_floor</span><span class="o">,</span> <span class="err">←</span><span class="n">int</span><span class="bp">.</span><span class="n">cast_one</span><span class="o">,</span> <span class="err">←</span><span class="n">int</span><span class="bp">.</span><span class="n">cast_add</span><span class="o">,</span> <span class="err">←</span><span class="n">floor_lt</span><span class="o">,</span>
  <span class="n">int</span><span class="bp">.</span><span class="n">lt_add_one_iff</span><span class="o">,</span> <span class="n">le_antisymm_iff</span><span class="o">,</span> <span class="n">and</span><span class="bp">.</span><span class="n">comm</span><span class="o">]</span>

<span class="kn">set_option</span> <span class="n">pp</span><span class="bp">.</span><span class="n">all</span> <span class="n">true</span>
<span class="kn">lemma</span> <span class="n">aux</span> <span class="o">:</span> <span class="o">(</span><span class="mi">71</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">/</span> <span class="mi">10</span> <span class="bp">&lt;</span> <span class="mi">7</span> <span class="bp">+</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="c1">-- ⊢ 71 / 10 &lt; 7 + 1</span>
  <span class="c1">-- exactly the same term as the sorry above</span>
  <span class="c1">-- even with pp.all true</span>
  <span class="n">norm_num</span> <span class="c1">-- works fine?!</span>
<span class="kn">end</span>

<span class="kn">theorem</span> <span class="n">floor_example</span> <span class="o">:</span> <span class="n">floor</span> <span class="o">(</span><span class="mi">71</span><span class="bp">/</span><span class="mi">10</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">7</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">rw</span> <span class="err">←</span><span class="n">floor_iff_bounds</span><span class="o">,</span>
  <span class="n">split</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">norm_num</span><span class="o">},</span>
  <span class="c1">-- ⊢ 71 / 10 &lt; ↑7 + 1</span>
  <span class="c1">-- norm_num, -- seems to hang</span>
<span class="n">suffices</span> <span class="o">:</span> <span class="o">(</span><span class="mi">71</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">/</span> <span class="mi">10</span> <span class="bp">&lt;</span> <span class="mi">7</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">,</span>
  <span class="n">simpa</span> <span class="kn">using</span> <span class="n">this</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">aux</span><span class="o">,</span>
  <span class="c1">-- ⊢ 71 / 10 &lt; 7 + 1</span>
  <span class="c1">-- norm_num -- deterministic timeout</span>
  <span class="c1">-- sorry</span>
<span class="kn">end</span>
</pre></div>


<p>Weird.</p>

#### [ Bryan Gin-ge Chen (Jan 18 2019 at 00:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156329084):
<p>And this works too:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">norm_num</span>
<span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">lemma</span> <span class="n">floor_iff_bounds</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">z</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span>
<span class="err">↑</span><span class="n">z</span> <span class="bp">≤</span> <span class="n">r</span> <span class="bp">∧</span> <span class="n">r</span> <span class="bp">&lt;</span> <span class="o">(</span><span class="n">z</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">↔</span> <span class="err">⌊</span> <span class="n">r</span> <span class="err">⌋</span> <span class="bp">=</span> <span class="n">z</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span><span class="n">le_floor</span><span class="o">,</span> <span class="err">←</span><span class="n">int</span><span class="bp">.</span><span class="n">cast_one</span><span class="o">,</span> <span class="err">←</span><span class="n">int</span><span class="bp">.</span><span class="n">cast_add</span><span class="o">,</span> <span class="err">←</span><span class="n">floor_lt</span><span class="o">,</span>
  <span class="n">int</span><span class="bp">.</span><span class="n">lt_add_one_iff</span><span class="o">,</span> <span class="n">le_antisymm_iff</span><span class="o">,</span> <span class="n">and</span><span class="bp">.</span><span class="n">comm</span><span class="o">]</span>

<span class="kn">set_option</span> <span class="n">pp</span><span class="bp">.</span><span class="n">all</span> <span class="n">true</span>
<span class="kn">theorem</span> <span class="n">floor_example</span> <span class="o">:</span> <span class="n">floor</span> <span class="o">(</span><span class="mi">71</span><span class="bp">/</span><span class="mi">10</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">7</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">rw</span> <span class="err">←</span><span class="n">floor_iff_bounds</span><span class="o">,</span>
  <span class="n">split</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">norm_num</span><span class="o">},</span>
  <span class="c1">-- ⊢ 71 / 10 &lt; ↑7 + 1</span>
  <span class="c1">-- norm_num, -- seems to hang</span>
<span class="n">suffices</span> <span class="o">:</span> <span class="o">(</span><span class="mi">71</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">/</span> <span class="mi">10</span> <span class="bp">&lt;</span> <span class="mi">7</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">,</span>
  <span class="n">simpa</span> <span class="kn">using</span> <span class="n">this</span><span class="o">,</span>
  <span class="k">have</span>  <span class="o">:</span> <span class="o">(</span><span class="mi">71</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">/</span> <span class="mi">10</span> <span class="bp">&lt;</span> <span class="mi">7</span> <span class="bp">+</span> <span class="mi">1</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">norm_num</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">this</span><span class="o">,</span>
  <span class="c1">-- ⊢ 71 / 10 &lt; 7 + 1</span>
  <span class="c1">-- norm_num -- deterministic timeout</span>
  <span class="c1">-- sorry</span>
<span class="kn">end</span>
</pre></div>

#### [ Rob Lewis (Jan 18 2019 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156329174):
<p>This is really weird. The second norm_num works if you sorry the first. But then, bizarrely, if you change the first one to <code>{suffices : (7 : ℝ) ≤ 71/10, simpa, sorry}</code> the second norm_num fails.</p>

#### [ Bryan Gin-ge Chen (Jan 18 2019 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156329293):
<p>Last one, I promise! This works too (probably should have tried this first):</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">norm_num</span>
<span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">lemma</span> <span class="n">floor_iff_bounds</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">z</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span>
<span class="err">↑</span><span class="n">z</span> <span class="bp">≤</span> <span class="n">r</span> <span class="bp">∧</span> <span class="n">r</span> <span class="bp">&lt;</span> <span class="o">(</span><span class="n">z</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">↔</span> <span class="err">⌊</span> <span class="n">r</span> <span class="err">⌋</span> <span class="bp">=</span> <span class="n">z</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span><span class="n">le_floor</span><span class="o">,</span> <span class="err">←</span><span class="n">int</span><span class="bp">.</span><span class="n">cast_one</span><span class="o">,</span> <span class="err">←</span><span class="n">int</span><span class="bp">.</span><span class="n">cast_add</span><span class="o">,</span> <span class="err">←</span><span class="n">floor_lt</span><span class="o">,</span>
  <span class="n">int</span><span class="bp">.</span><span class="n">lt_add_one_iff</span><span class="o">,</span> <span class="n">le_antisymm_iff</span><span class="o">,</span> <span class="n">and</span><span class="bp">.</span><span class="n">comm</span><span class="o">]</span>

<span class="c1">--set_option pp.all true</span>

<span class="kn">theorem</span> <span class="n">floor_example</span> <span class="o">:</span> <span class="n">floor</span> <span class="o">(</span><span class="mi">71</span><span class="bp">/</span><span class="mi">10</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">7</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">rw</span> <span class="err">←</span><span class="n">floor_iff_bounds</span><span class="o">,</span>
  <span class="n">split</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">norm_num</span><span class="o">},</span>
  <span class="c1">-- ⊢ 71 / 10 &lt; ↑7 + 1</span>
  <span class="c1">-- norm_num, -- seems to hang</span>
<span class="n">suffices</span> <span class="o">:</span> <span class="o">(</span><span class="mi">71</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">/</span> <span class="mi">10</span> <span class="bp">&lt;</span> <span class="mi">7</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">,</span>
  <span class="n">simpa</span> <span class="kn">using</span> <span class="n">this</span><span class="o">,</span>
  <span class="c1">-- have  : (71 : ℝ) / 10 &lt; 7 + 1 := by norm_num1,</span>
  <span class="n">exact</span> <span class="k">by</span> <span class="n">norm_num</span><span class="o">,</span>
  <span class="c1">-- ⊢ 71 / 10 &lt; 7 + 1</span>
  <span class="c1">-- norm_num -- deterministic timeout</span>
  <span class="c1">-- sorry</span>
<span class="kn">end</span>
</pre></div>

#### [ Rob Lewis (Jan 18 2019 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156329529):
<p>My best guess is that it has something to do with the type class instance cache. But it's bedtime now.</p>

#### [ Rob Lewis (Jan 18 2019 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156357776):
<p>This localizes to the same place as <a href="#narrow/stream/113488-general/topic/norm_num" title="#narrow/stream/113488-general/topic/norm_num">https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/norm_num</a> . If you add some tracing around <code>norm_num.lean:162</code> you see what's going on: the <code>guard</code> is failing because <code>e2</code> and <code>e2'</code> have different <code>has_one</code> instances. I'm still not 100% sure why <code>norm_num</code> creates different instances in different circumstances, but I guess it's some kind of a cache issue.</p>

#### [ Rob Lewis (Jan 18 2019 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156357872):
<p>One solution: guarding for structural equality is maybe too strong there, but checking that they unify is too weak. We really want to check that the numeral structures match exactly, and the type class instances unify.</p>

#### [ Rob Lewis (Jan 18 2019 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156357929):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> what do you think?</p>

#### [ Mario Carneiro (Jan 18 2019 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156358300):
<p>I see that <code>norm_num</code> is replacing one instance with another, but I don't see how that makes the later stage fail</p>

#### [ Mario Carneiro (Jan 18 2019 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156358319):
<p>even if the bottom up simp decides to replace the instance, normalizing the lt should still work</p>

#### [ Rob Lewis (Jan 18 2019 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156358810):
<p><code>norm_num1</code> should kill the second goal. But it fails at that <code>guard</code> call, because the output of C++ <code>norm_num</code> uses a different <code>has_one</code> instance than the one that (I think) came from the elaborator. It made some progress though, which <code>simp</code> then reverts, so it loops.</p>

#### [ Mario Carneiro (Jan 18 2019 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156358900):
<p>doesn't the guard just make sure that something has changed before changing it? It should be harmless</p>

#### [ Mario Carneiro (Jan 18 2019 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156358938):
<p>oh, different guard</p>

#### [ Mario Carneiro (Jan 18 2019 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156358946):
<p>that guard is just an assert, it can be removed if it's causing trouble</p>

#### [ Rob Lewis (Jan 18 2019 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156358948):
<p>The guard makes sure that the output of C++ <code>norm_num</code> is what Lean <code>norm_num</code> was expecting.</p>

#### [ Mario Carneiro (Jan 18 2019 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156359001):
<p>I guess it could be defeq instead</p>

#### [ Rob Lewis (Jan 18 2019 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156359035):
<p>defeq doesn't really make sense here. The point of the guard is to catch mistakes, I guess. If you check for defeq and there is a mistake, you could force the kernel to normalize numerals.</p>

#### [ Rob Lewis (Jan 18 2019 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156359038):
<p>Removing the guard completely seems better than that.</p>

#### [ Mario Carneiro (Jan 18 2019 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156359050):
<p>is there an option in <code>is_def_eq</code> for don't try too hard?</p>

#### [ Rob Lewis (Jan 18 2019 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156359126):
<p>But then "bugs" like this one are harder to notice. I could imagine this slowing down <code>norm_num</code> noticeably in some cases, instead of failing, but that's harder for Kevin to notice/point out here.</p>

#### [ Mario Carneiro (Jan 18 2019 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156359127):
<p>I'm not sure what <code>approx</code> does, but <code>md := reducible</code> should help</p>

#### [ Kevin Buzzard (Jan 18 2019 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156359157):
<p>By the way -- thanks <span class="user-mention" data-user-id="123965">@Bryan Gin-ge Chen</span> for the <code>exact by</code> workaround! I've heard of <code>by exact</code> but never this way round. This works great in my use case.</p>

#### [ Rob Lewis (Jan 18 2019 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156359228):
<p><code>approx</code> has something to do with the higher order unification strategy, I think? Not sure. Are the relevant type class defs reducible?</p>

#### [ Mario Carneiro (Jan 18 2019 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156359234):
<p>eh, I guess not</p>

#### [ Mario Carneiro (Jan 18 2019 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156359279):
<p>I think <code>is_def_eq</code> should be okay as long as they are actually defeq</p>

#### [ Mario Carneiro (Jan 18 2019 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156359282):
<p>if they aren't it will start unfolding numerals but that's still impossible to my knowledge</p>

#### [ Rob Lewis (Jan 18 2019 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156359283):
<p>Heh. If they're actually defeq we don't need the check at all.</p>

#### [ Mario Carneiro (Jan 18 2019 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156359333):
<p>maybe you are right - failing would be great if it made norm_num fail, but this is deep in an inner function and failure has a particular meaning</p>

#### [ Mario Carneiro (Jan 18 2019 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156359347):
<p>it just causes these funny loops instead</p>

#### [ Rob Lewis (Jan 18 2019 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156359648):
<p>Yeah. A "structurally equal numeral, up to type classes" test would work here, and could maybe be useful elsewhere. The instances will be unified somewhere regardless (if we want this example to succeed).</p>

#### [ Rob Lewis (Jan 18 2019 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156359738):
<p>Again, the alternative is just removing the guard, which also doesn't seem so bad.</p>

#### [ Mario Carneiro (Jan 18 2019 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156359755):
<p>I think <code>n1.to_nat = n2.to_nat</code> should work for that</p>

#### [ Rob Lewis (Jan 18 2019 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/norm_num%20weirdness/near/156359764):
<p>The two "bugs" that it's identified are only kind of bugs.</p>


{% endraw %}
