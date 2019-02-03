---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/38567leakingconstruction.html
---

## Stream: [maths](index.html)
### Topic: [leaking construction](38567leakingconstruction.html)

---


{% raw %}
#### [ Patrick Massot (Sep 09 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/leaking%20construction/near/133622397):
<p>Sometimes I see things like: <code>quot.lift (λ (a₁ : cau_seq ℚ abs), quotient.lift (has_lt.lt a₁) _ ε) _</code> in my tactic state when playing with real numbers. It looks like internal details of the constructions are leaking. What does it mean? Can I avoid that?</p>

#### [ Mario Carneiro (Sep 09 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/leaking%20construction/near/133622571):
<p>how are you "playing"?</p>

#### [ Mario Carneiro (Sep 09 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/leaking%20construction/near/133622577):
<p>if you unfold stuff you can see this</p>

#### [ Patrick Massot (Sep 09 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/leaking%20construction/near/133622621):
<p>More precisely, I have:</p>
<div class="codehilite"><pre><span></span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_2</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">metric_space</span> <span class="n">α</span><span class="o">,</span>
<span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_3</span><span class="o">,</span>
<span class="n">u</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">α</span><span class="o">,</span>
<span class="n">f</span> <span class="o">:</span> <span class="n">filter</span> <span class="n">β</span><span class="o">,</span>
<span class="n">ε</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">,</span>
<span class="n">this</span> <span class="o">:</span> <span class="n">ball</span> <span class="n">a</span> <span class="n">ε</span> <span class="err">∈</span> <span class="o">(</span><span class="n">map</span> <span class="n">u</span> <span class="n">f</span><span class="o">)</span><span class="bp">.</span><span class="n">sets</span>
</pre></div>


<p>If I do <code>have:= mem_map.2 this</code> then the new this is the horror</p>
<div class="codehilite"><pre><span></span><span class="n">quot</span><span class="bp">.</span><span class="n">lift</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">a₁</span> <span class="o">:</span> <span class="n">cau_seq</span> <span class="n">ℚ</span> <span class="n">abs</span><span class="o">),</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">lift</span> <span class="o">(</span><span class="n">has_lt</span><span class="bp">.</span><span class="n">lt</span> <span class="n">a₁</span><span class="o">)</span> <span class="bp">_</span> <span class="n">ε</span><span class="o">)</span> <span class="bp">_</span> <span class="err">∈</span>   <span class="o">(</span><span class="n">map</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">dist</span> <span class="n">y</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">map</span> <span class="n">u</span> <span class="n">f</span><span class="o">))</span><span class="bp">.</span><span class="n">sets</span>
</pre></div>


<p>but I can do instead <code>have : {b | u b ∈ ball a ε} ∈ f.sets := mem_map.2 this,</code> and Lean won't unfold it</p>

#### [ Mario Carneiro (Sep 09 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/leaking%20construction/near/133622685):
<p>You are going the wrong way</p>

#### [ Mario Carneiro (Sep 09 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/leaking%20construction/near/133622686):
<p>use <code>mem_map.1 this</code></p>

#### [ Mario Carneiro (Sep 09 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/leaking%20construction/near/133622735):
<p>(it works because the two sides are defeq so it doesn't really matter if you apply it, but then the matching goes crazy)</p>

#### [ Patrick Massot (Sep 09 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/leaking%20construction/near/133622736):
<p>oh</p>

#### [ Patrick Massot (Sep 09 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/leaking%20construction/near/133622737):
<p>weird</p>

#### [ Patrick Massot (Sep 09 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/leaking%20construction/near/133622751):
<p>That's biconditional in action: try one direction at random and, if Lean is willing to apply it, never look back</p>

#### [ Mario Carneiro (Sep 09 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/leaking%20construction/near/133622752):
<p>notice that you have another <code>map</code> in the result</p>

#### [ Mario Carneiro (Sep 09 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/leaking%20construction/near/133622755):
<p><code>(map (λ (y : α), dist y a) (map u f)).sets</code></p>

#### [ Patrick Massot (Sep 09 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/leaking%20construction/near/133622757):
<p>true</p>

#### [ Mario Carneiro (Sep 09 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/leaking%20construction/near/133622809):
<p>so it tried to figure out how to read <code>ball a ε</code> as <code>{x | m x ∈ t}</code> for some <code>m, t</code> and chaos ensues</p>

#### [ Patrick Massot (Sep 09 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/leaking%20construction/near/133622819):
<p>That's wonderful. In the proof I posted earlier:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">u</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">tendsto</span> <span class="n">u</span> <span class="n">at_top</span> <span class="o">(</span><span class="n">nhds</span> <span class="n">a</span><span class="o">)</span> <span class="bp">↔</span>
  <span class="bp">∀</span> <span class="n">ε</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">,</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">N</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">n</span><span class="o">},</span> <span class="n">n</span> <span class="bp">≥</span> <span class="n">N</span> <span class="bp">→</span> <span class="n">dist</span> <span class="o">(</span><span class="n">u</span> <span class="n">n</span><span class="o">)</span> <span class="n">a</span> <span class="bp">&lt;</span> <span class="n">ε</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">H</span> <span class="n">ε</span> <span class="n">εpos</span><span class="o">,</span> <span class="n">mem_at_top_sets</span><span class="bp">.</span><span class="mi">1</span> <span class="err">$</span> <span class="n">mem_map</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="n">H</span> <span class="o">(</span><span class="n">ball_mem_nhds</span> <span class="bp">_</span> <span class="n">εpos</span><span class="o">),</span>
 <span class="bp">λ</span> <span class="n">H</span> <span class="n">s</span> <span class="n">s_nhd</span><span class="o">,</span> <span class="k">let</span> <span class="bp">⟨</span><span class="n">ε</span><span class="o">,</span> <span class="n">εpos</span><span class="o">,</span> <span class="n">sub</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">mem_nhds_iff_metric</span><span class="bp">.</span><span class="mi">1</span> <span class="n">s_nhd</span> <span class="k">in</span>
   <span class="k">let</span> <span class="bp">⟨</span><span class="n">N</span><span class="o">,</span> <span class="n">H&#39;</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">H</span> <span class="n">ε</span> <span class="n">εpos</span> <span class="k">in</span> <span class="n">mem_at_top_sets</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">⟨</span><span class="n">N</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">n</span> <span class="n">nN</span><span class="o">,</span>
   <span class="n">sub</span> <span class="err">$</span> <span class="n">mem_ball</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="n">H&#39;</span> <span class="n">nN</span><span class="bp">⟩⟩</span>
</pre></div>


<p>There is a <code>$ mem_map.2 $ </code>. You can change 2 into 1, it still works. Then you can remove that bit entirely and it still works!</p>

#### [ Mario Carneiro (Sep 09 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/leaking%20construction/near/133622825):
<p>because the proof is <code>rfl</code></p>

#### [ Patrick Massot (Sep 09 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/leaking%20construction/near/133622827):
<p>Yeah, I understand</p>

#### [ Johannes Hölzl (Sep 10 2018 at 04:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/leaking%20construction/near/133633334):
<p><code>simp</code> can do this:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">tendsto_at_top_nhds_metric</span> <span class="o">[</span><span class="n">metric_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">:</span>
  <span class="n">tendsto</span> <span class="n">f</span> <span class="n">at_top</span> <span class="o">(</span><span class="n">nhds</span> <span class="n">a</span><span class="o">)</span> <span class="bp">↔</span> <span class="o">(</span><span class="bp">∀</span><span class="n">ε</span><span class="bp">&gt;</span><span class="mi">0</span><span class="o">,</span> <span class="bp">∃</span><span class="n">N</span><span class="o">,</span> <span class="bp">∀</span><span class="n">n</span><span class="bp">≥</span><span class="n">N</span><span class="o">,</span> <span class="n">dist</span> <span class="o">(</span><span class="n">f</span> <span class="n">n</span><span class="o">)</span> <span class="n">a</span> <span class="bp">&lt;</span> <span class="n">ε</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">tendsto_infi</span><span class="o">,</span> <span class="n">tendsto_principal</span><span class="o">,</span> <span class="n">nhds_eq_metric</span><span class="o">]</span>
</pre></div>


<p>The trick is to unfold <code>nhds_eq_metric</code> and rhen focus on the right side: An infimum is equal to a quantifier around the <code>tendsto</code>, until it reaches <code>principal</code>, then it is reduced to membership in <code>at_top</code>.<br>
Other examples</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">tendsto_at_top_at_top</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">:</span>
  <span class="n">tendsto</span> <span class="n">f</span> <span class="n">at_top</span> <span class="n">at_top</span> <span class="bp">↔</span> <span class="o">(</span><span class="bp">∀</span><span class="n">M</span><span class="o">,</span> <span class="bp">∃</span><span class="n">N</span><span class="o">,</span> <span class="bp">∀</span><span class="n">n</span><span class="bp">≥</span><span class="n">N</span><span class="o">,</span> <span class="n">M</span> <span class="bp">≤</span> <span class="n">f</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">conv</span> <span class="o">{</span> <span class="n">to_lhs</span><span class="o">,</span> <span class="n">congr</span><span class="o">,</span> <span class="n">skip</span><span class="o">,</span> <span class="n">skip</span><span class="o">,</span> <span class="n">rw</span> <span class="o">[</span><span class="n">at_top</span><span class="o">]</span> <span class="o">}</span><span class="bp">;</span> <span class="n">simp</span> <span class="o">[</span><span class="n">tendsto_infi</span><span class="o">,</span> <span class="n">tendsto_principal</span><span class="o">]</span>
</pre></div>


<p>or</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">tendsto_nhds_metric_nhds_metric</span> <span class="o">[</span><span class="n">metric_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">metric_space</span> <span class="n">β</span><span class="o">]</span>
  <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">}</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">b</span> <span class="o">:</span> <span class="n">β</span><span class="o">}:</span>
  <span class="n">tendsto</span> <span class="n">f</span> <span class="o">(</span><span class="n">nhds</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">nhds</span> <span class="n">b</span><span class="o">)</span> <span class="bp">↔</span> <span class="o">(</span><span class="bp">∀</span><span class="n">ε</span><span class="bp">&gt;</span><span class="mi">0</span><span class="o">,</span> <span class="bp">∃</span><span class="n">δ</span><span class="bp">&gt;</span><span class="mi">0</span><span class="o">,</span> <span class="bp">∀</span><span class="n">x</span><span class="o">,</span> <span class="n">dist</span> <span class="n">x</span> <span class="n">a</span> <span class="bp">&lt;</span> <span class="n">δ</span> <span class="bp">→</span> <span class="n">dist</span> <span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">)</span> <span class="n">b</span> <span class="bp">&lt;</span> <span class="n">ε</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">conv</span> <span class="o">{</span> <span class="n">to_lhs</span><span class="o">,</span> <span class="n">congr</span><span class="o">,</span> <span class="n">skip</span><span class="o">,</span> <span class="n">skip</span><span class="o">,</span> <span class="n">rw</span> <span class="o">[</span><span class="n">nhds_eq_metric</span><span class="o">]</span> <span class="o">},</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">tendsto_infi</span><span class="o">,</span> <span class="n">tendsto_principal</span><span class="o">,</span> <span class="n">mem_nhds_iff_metric</span><span class="o">,</span> <span class="n">set</span><span class="bp">.</span><span class="n">subset_def</span><span class="o">]</span>
<span class="kn">end</span>
</pre></div>


<p>Here the annoying part is that we need to focus on the right <code>nhds</code> or <code>at_top</code>.</p>


{% endraw %}
