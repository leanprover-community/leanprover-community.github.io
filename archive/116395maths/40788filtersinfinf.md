---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/40788filtersinfinf.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [filters inf inf](https://leanprover-community.github.io/archive/116395maths/40788filtersinfinf.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Jun 16 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128166284):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> I have difficulties setting up my uniform space structure on topological groups. Basically the trouble is the definition involves dependent nested infimum. I tried to mimick the metric space case where you wrote:</p>
<div class="codehilite"><pre><span></span><span class="n">uniformity</span> <span class="o">:=</span> <span class="o">(</span><span class="err">⨅</span> <span class="n">ε</span><span class="bp">&gt;</span><span class="mi">0</span><span class="o">,</span> <span class="n">principal</span> <span class="o">{</span><span class="n">p</span><span class="o">:</span><span class="n">α</span><span class="bp">×</span><span class="n">α</span> <span class="bp">|</span> <span class="n">dist</span> <span class="n">p</span><span class="bp">.</span><span class="mi">1</span> <span class="n">p</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">&lt;</span> <span class="n">ε</span><span class="o">}),</span>
</pre></div>


<p>(nested inf is somewhat hidden but still there). Question 1: would it be a good idea to rather use the subtype of positive real number as the indexing set?</p>

#### [ Patrick Massot (Jun 16 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128166325):
<p>So, in the context of a topological add group R, I wrote, with obvious notations:</p>
<div class="codehilite"><pre><span></span><span class="n">uniformity</span>  <span class="o">:=</span> <span class="err">⨅</span> <span class="n">U</span> <span class="err">∈</span> <span class="n">nhd_zero</span> <span class="n">R</span><span class="o">,</span> <span class="n">principal</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="n">R</span><span class="bp">×</span><span class="n">R</span> <span class="bp">|</span> <span class="n">p</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">-</span> <span class="n">p</span><span class="bp">.</span><span class="mi">1</span> <span class="err">∈</span> <span class="n">U</span><span class="o">}</span>
</pre></div>

#### [ Patrick Massot (Jun 16 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128166331):
<p>But again this is somewhat inconvenient to use.</p>

#### [ Patrick Massot (Jun 16 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128166332):
<p>I have the following lemma, which is a restatement of something already there:</p>

#### [ Patrick Massot (Jun 16 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128166335):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">filter</span><span class="bp">.</span><span class="n">mem_sets_of_mem_infi</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">ι</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">ι</span> <span class="bp">→</span> <span class="n">filter</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">A</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">}</span>
  <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">directed</span> <span class="o">(</span><span class="bp">≤</span><span class="o">)</span> <span class="n">f</span><span class="o">)</span> <span class="o">(</span><span class="n">ne</span> <span class="o">:</span> <span class="n">nonempty</span> <span class="n">ι</span><span class="o">)</span> <span class="o">:</span> <span class="n">A</span> <span class="err">∈</span> <span class="o">(</span><span class="err">⨅</span> <span class="n">i</span><span class="o">,</span><span class="n">f</span> <span class="n">i</span><span class="o">)</span><span class="bp">.</span><span class="n">sets</span> <span class="bp">→</span> <span class="bp">∃</span> <span class="n">i</span><span class="o">,</span> <span class="n">A</span> <span class="err">∈</span> <span class="o">(</span><span class="n">f</span> <span class="n">i</span><span class="o">)</span><span class="bp">.</span><span class="n">sets</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">intro</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">finish</span> <span class="o">[</span><span class="n">infi_sets_eq</span><span class="o">]</span>
<span class="kn">end</span>
</pre></div>

#### [ Patrick Massot (Jun 16 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128166375):
<p>but already I'd like to deduced <code>ne</code> from existence of <code>A</code></p>

#### [ Patrick Massot (Jun 16 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128166385):
<p>And then I need a version for dependent nested inf that, I think, would be something like:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">filter</span><span class="bp">.</span><span class="n">mem_sets_of_mem_infi&#39;</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">ι</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">P</span> <span class="o">:</span> <span class="n">ι</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="bp">Π</span> <span class="n">i</span><span class="o">,</span> <span class="n">P</span> <span class="n">i</span> <span class="bp">→</span> <span class="n">filter</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">A</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">}</span>
  <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">A</span> <span class="err">∈</span> <span class="o">(</span><span class="err">⨅</span> <span class="n">i</span><span class="o">,</span> <span class="err">⨅</span> <span class="n">h</span> <span class="o">:</span> <span class="n">P</span> <span class="n">i</span><span class="o">,</span> <span class="n">f</span> <span class="n">i</span> <span class="n">h</span><span class="o">)</span><span class="bp">.</span><span class="n">sets</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">i</span><span class="o">,</span> <span class="bp">∃</span> <span class="n">h</span> <span class="o">:</span> <span class="n">P</span> <span class="n">i</span><span class="o">,</span> <span class="n">A</span> <span class="err">∈</span> <span class="o">(</span><span class="n">f</span> <span class="n">i</span> <span class="n">h</span><span class="o">)</span><span class="bp">.</span><span class="n">sets</span> <span class="o">:=</span>
</pre></div>


<p>but with some directedness assumption somewhere</p>

#### [ Patrick Massot (Jun 16 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128166424):
<p>Any help would be appreciated</p>

#### [ Chris Hughes (Jun 16 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128168185):
<p>I tried to prove it, but then realised it wasn't true.</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">analysis</span><span class="bp">.</span><span class="n">filter</span>
<span class="kn">open</span> <span class="n">set</span> <span class="n">list</span> <span class="n">filter</span> <span class="n">lattice</span>

<span class="kn">lemma</span> <span class="n">filter</span><span class="bp">.</span><span class="n">mem_sets_of_mem_infi&#39;</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">ι</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">P</span> <span class="o">:</span> <span class="n">ι</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="bp">Π</span> <span class="n">i</span><span class="o">,</span> <span class="n">P</span> <span class="n">i</span> <span class="bp">→</span> <span class="n">filter</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">A</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">}</span>
  <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">A</span> <span class="err">∈</span> <span class="o">(</span><span class="err">⨅</span> <span class="n">i</span><span class="o">,</span> <span class="err">⨅</span> <span class="n">h</span> <span class="o">:</span> <span class="n">P</span> <span class="n">i</span><span class="o">,</span> <span class="n">f</span> <span class="n">i</span> <span class="n">h</span><span class="o">)</span><span class="bp">.</span><span class="n">sets</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">i</span><span class="o">,</span> <span class="bp">∃</span> <span class="n">h</span> <span class="o">:</span> <span class="n">P</span> <span class="n">i</span><span class="o">,</span> <span class="n">A</span> <span class="err">∈</span> <span class="o">(</span><span class="n">f</span> <span class="n">i</span> <span class="n">h</span><span class="o">)</span><span class="bp">.</span><span class="n">sets</span> <span class="o">:=</span> <span class="n">sorry</span>

<span class="kn">lemma</span> <span class="n">proof_of_false</span> <span class="o">:</span> <span class="n">false</span> <span class="o">:=</span>
<span class="k">let</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">hx</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">filter</span><span class="bp">.</span><span class="n">mem_sets_of_mem_infi&#39;</span> <span class="bp">ℕ</span> <span class="n">empty</span> <span class="n">empty</span><span class="bp">.</span><span class="n">elim</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">i</span><span class="o">,</span> <span class="n">i</span><span class="bp">.</span><span class="n">elim</span><span class="o">)</span> <span class="n">set</span><span class="bp">.</span><span class="n">univ</span> <span class="o">(</span><span class="k">by</span> <span class="n">simp</span><span class="o">)</span> <span class="k">in</span>
<span class="n">x</span><span class="bp">.</span><span class="n">elim</span>
</pre></div>

#### [ Chris Hughes (Jun 16 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128168190):
<p>Not sure how helpful that is.</p>

#### [ Chris Hughes (Jun 16 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128168559):
<p>Probably need <code>A ≠ univ</code>, because <code>univ</code> is in every filter, but you might as well just have <code>nonempty ι</code>, which is implied by <code>A ≠ univ</code>,</p>

#### [ Reid Barton (Jun 16 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128168701):
<blockquote>
<p>but already I'd like to deduced <code>ne</code> from existence of <code>A</code></p>
</blockquote>
<p>You should be deducing <code>ne</code> from the fact that <code>f</code> is directed, but I guess mathlib's definition leaves out that condition, oops.</p>

#### [ Reid Barton (Jun 16 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128169091):
<p>Apparently not assuming that a directed set is nonempty is a Bourbaki thing.</p>

#### [ Reid Barton (Jun 16 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128169188):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> There is</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">infi_sets_eq&#39;</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">filter</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">β</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">directed_on</span> <span class="o">(</span><span class="bp">λ</span><span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">f</span> <span class="n">y</span><span class="o">)</span> <span class="n">s</span><span class="o">)</span> <span class="o">(</span><span class="n">ne</span> <span class="o">:</span> <span class="bp">∃</span><span class="n">i</span><span class="o">,</span> <span class="n">i</span> <span class="err">∈</span> <span class="n">s</span><span class="o">)</span> <span class="o">:</span>
  <span class="o">(</span><span class="err">⨅</span> <span class="n">i</span><span class="err">∈</span><span class="n">s</span><span class="o">,</span> <span class="n">f</span> <span class="n">i</span><span class="o">)</span><span class="bp">.</span><span class="n">sets</span> <span class="bp">=</span> <span class="o">(</span><span class="err">⋃</span> <span class="n">i</span> <span class="err">∈</span> <span class="n">s</span><span class="o">,</span> <span class="o">(</span><span class="n">f</span> <span class="n">i</span><span class="o">)</span><span class="bp">.</span><span class="n">sets</span><span class="o">)</span>
</pre></div>

#### [ Johannes Hölzl (Jun 16 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128172055):
<p>Hm, I think you don't need the infimum at all, it should be possible to use <code>vmap</code> and <code>nhds_zero</code>:<br>
<code>uniformity := vmap (fun p, p.1 - p.2) (nhds_zero R)</code></p>

#### [ Patrick Massot (Jun 16 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128178252):
<p>Oh. That's a completely different start</p>

#### [ Patrick Massot (Jun 16 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128178253):
<p>But maybe it's more natural</p>

#### [ Patrick Massot (Jun 16 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128178255):
<p>It means I need to learn a completely new set of lemmas</p>

#### [ Patrick Massot (Jun 16 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128179700):
<p>It's worse than my original method</p>

#### [ Patrick Massot (Jun 16 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128179701):
<p>I can't prove any single property</p>

#### [ Mario Carneiro (Jun 16 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128179709):
<p>like what?</p>

#### [ Patrick Massot (Jun 16 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128180101):
<p>like <code>principal id_rel ≤ vmap (λ (p : R × R), p.fst - p.snd) (nhds 0)</code></p>

#### [ Patrick Massot (Jun 16 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128180103):
<p>and <code>tendsto prod.swap (vmap (λ (p : R × R), p.fst - p.snd) (nhds 0)) (vmap (λ (p : R × R), p.fst - p.snd) (nhds 0))</code></p>

#### [ Patrick Massot (Jun 16 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128180142):
<p><code>filter.lift' (vmap (λ (p : R × R), p.fst - p.snd) (nhds 0)) (λ (s : set (R × R)), comp_rel s s) ≤  vmap (λ (p : R × R), p.fst - p.snd) (nhds 0)</code></p>

#### [ Mario Carneiro (Jun 16 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128180145):
<p>I assume you know <code>nhds_zero = nhds 0</code>?</p>

#### [ Patrick Massot (Jun 16 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128180146):
<p>and <code>∀ (s : set R),    topological_space.is_open _inst_2 s ↔  ∀ (x : R),   x ∈ s → {p : R × R | p.fst = x → p.snd ∈ s} ∈ (vmap (λ (p : R × R), p.fst - p.snd) (nhds 0)).sets</code></p>

#### [ Patrick Massot (Jun 16 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128180152):
<p>Johannes suggestion doesn't use <code>nhds_zero</code> (which I defined earlier by <code>def nhd_zero := (nhds (0 : R)).sets</code>)</p>

#### [ Mario Carneiro (Jun 16 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128180192):
<p>What do you mean? I see <code>nhds_zero</code> in his post</p>

#### [ Patrick Massot (Jun 16 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128180195):
<p>this is based on him incorrectly guessing my definition</p>

#### [ Mario Carneiro (Jun 16 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128180202):
<p>For the first one, you have <code>tendsto_iff_vmap</code></p>

#### [ Patrick Massot (Jun 16 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128180203):
<p>he probably thought I had <code>def nhd_zero := nhds (0 : R)</code></p>

#### [ Mario Carneiro (Jun 16 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128180204):
<p>Well, <code>nhds_zero</code> has a special place in the theory of top groups</p>

#### [ Patrick Massot (Jun 16 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128180205):
<p>Indeed the first thing I wrote is <code>rw tendsto_vmap_iff</code></p>

#### [ Patrick Massot (Jun 16 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128180245):
<p>I also tried <code>rw tendsto_iff_vmap,</code></p>

#### [ Patrick Massot (Jun 16 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128180254):
<p>but then I'm stuck</p>

#### [ Mario Carneiro (Jun 16 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128180256):
<p>then use that <code>-</code> is continuous</p>

#### [ Mario Carneiro (Jun 16 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128180258):
<p><code>continuous.tendsto</code></p>

#### [ Patrick Massot (Jun 16 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128180449):
<p>I'd love to continue this discussion but I must leave at 6:30 tomorrow morning to get a plane to go to a conference in Cagliari</p>

#### [ Patrick Massot (Jun 16 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128180450):
<p>so I should sleep</p>

#### [ Patrick Massot (Jun 16 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128180451):
<p>thank you very much for these hints</p>

#### [ Johannes Hölzl (Jun 17 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128206302):
<p>I guessed <code>nhds_zero</code> from your equation <code>uniformity  := ⨅ U ∈ nhd_zero R, principal {p : R×R | p.2 - p.1 ∈ U}</code>.<br>
(by the way: why is it okay to call the support type of a group <code>R</code> but not alpha?)</p>
<p>There are two important rules to convert between <code>map</code> and <code>vmap</code>: <code>map_le_iff_le_vmap</code>, and <code>map_eq_vmap_of_inverse</code>.</p>
<p>To prove the first rule use the rule  <code>map_le_iff_le_vmap</code> to move the<code>-</code> to the left side, then using rewriting to end up with <code>principal {a | a = 0} = pure 0 &lt;= nhds 0</code>.</p>
<p>The second rule (using prod.swap): use <code>map_le_iff_le_vmap</code>, and then <code>map_comp</code> the left side by <code>(fun x, - x) o (fun p, p.1 - p.2)</code> Then use <code>tendsto_vmap</code> (together with <code>tendsto_comp</code>).</p>
<p>And for the last one I guess we want to  use <code>vmap_eq_lift'</code> (which essentially proofs that your and my definition are the equal)</p>

#### [ Johannes Hölzl (Jun 17 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128214709):
<p><a href="https://gist.github.com/johoelzl/ca90562c46b49a1bbb1be36272ec3b1a" target="_blank" title="https://gist.github.com/johoelzl/ca90562c46b49a1bbb1be36272ec3b1a">https://gist.github.com/johoelzl/ca90562c46b49a1bbb1be36272ec3b1a</a><br>
transitivity, i.e. the <code>uniform_space.comp</code> rule, is a little bit harder to show</p>

#### [ Johannes Hölzl (Jun 17 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filters%20inf%20inf/near/128214772):
<p>Would you suggest any changes to this? if not I will just add this to mathlib</p>


{% endraw %}
