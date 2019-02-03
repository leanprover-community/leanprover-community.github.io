---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/49532shouldfintypetakeasort.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [should fintype take a sort?](https://leanprover-community.github.io/archive/113488general/49532shouldfintypetakeasort.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Chris Hughes (Aug 06 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/should%20fintype%20take%20a%20sort%3F/near/130982613):
<p>This instance would be possible if <code>fintype</code> took a sort instead of a Type. Is it worth changing?<br>
<code>instance (p : fin 3 → Prop) [decidable_pred p] : fintype (Π a, p a → fin 3) := by apply_instance</code></p>

#### [ Mario Carneiro (Aug 06 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/should%20fintype%20take%20a%20sort%3F/near/130982981):
<p>I thought about it, I have also seen this come up, but I don't know a clean way to do it without making lots of later stuff harder</p>

#### [ Chris Hughes (Aug 06 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/should%20fintype%20take%20a%20sort%3F/near/130983001):
<p>What would be harder?</p>

#### [ Mario Carneiro (Aug 06 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/should%20fintype%20take%20a%20sort%3F/near/130983027):
<p>you have to ulift somewhere, and this will affect proofs that don't care about Prop</p>

#### [ Mario Carneiro (Aug 06 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/should%20fintype%20take%20a%20sort%3F/near/130983244):
<p>of course another way to solve the particular problem you show is to have a second pi instance for Props</p>

#### [ Chris Hughes (Aug 06 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/should%20fintype%20take%20a%20sort%3F/near/130983543):
<p>I forgot that <code>list</code> didn't take a <code>Sort</code>.</p>

#### [ Mario Carneiro (Aug 06 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/should%20fintype%20take%20a%20sort%3F/near/130983761):
<p>Actually, I'm not sure it can be done at all, assuming that <code>list</code> and <code>finset</code> stay as is</p>

#### [ Mario Carneiro (Aug 06 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/should%20fintype%20take%20a%20sort%3F/near/130983876):
<p>What would be the type of <code>fintype</code>? If it is <code>Sort u -&gt; Type u</code> then it bumps the universe level in unwanted circumstances (i.e. <code>fintype nat : Type 1</code>), and if it is <code>Sort u -&gt; Sort (max 1 u)</code> then you can't define it</p>

#### [ Mario Carneiro (Aug 06 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/should%20fintype%20take%20a%20sort%3F/near/130984035):
<p>since <code>Sort (max 1 u) = Sort (?+1)</code> is unsolvable (you would need a <code>pred u</code> function but that doesn't exist)</p>

#### [ Chris Hughes (Aug 06 2018 at 19:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/should%20fintype%20take%20a%20sort%3F/near/130990940):
<p>Is there any reason not to just make everything a Sort, just in case some random thing like this comes up where it's useful?</p>

#### [ Simon Hudon (Aug 06 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/should%20fintype%20take%20a%20sort%3F/near/130994870):
<p>I think the main thing has to do with elimination. If your type is<code>Sort 0</code>, there's a special case that you can only eliminate to <code>Sort 0</code>. Otherwise, in <code>Sort 1</code>, you can eliminate anywhere you like.</p>

#### [ Simon Hudon (Aug 06 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/should%20fintype%20take%20a%20sort%3F/near/130995291):
<p>Btw, your instance type checks for me. Are you sure your issues have to do with universes?</p>

#### [ Chris Hughes (Aug 06 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/should%20fintype%20take%20a%20sort%3F/near/130995344):
<p>It type checks, but it can't synthesize the instance</p>

#### [ Chris Hughes (Aug 06 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/should%20fintype%20take%20a%20sort%3F/near/130995413):
<p>But if there was an instance saying <code>Pi p : Prop, fintype p</code> it would synthesize the instance from <code>pi.fintype</code></p>

#### [ Simon Hudon (Aug 06 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/should%20fintype%20take%20a%20sort%3F/near/130996568):
<p>I think you could make it work with an instance like this:</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">pi</span><span class="bp">.</span><span class="n">fintype&#39;</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span>
  <span class="o">[</span><span class="n">decidable</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="bp">∀</span><span class="n">a</span><span class="o">,</span> <span class="n">fintype</span> <span class="o">(</span><span class="n">β</span> <span class="n">a</span><span class="o">)]</span> <span class="o">:</span> <span class="n">fintype</span> <span class="o">(</span><span class="bp">Π</span><span class="n">a</span><span class="o">,</span> <span class="n">β</span> <span class="n">a</span><span class="o">)</span> <span class="o">:=</span>
</pre></div>

#### [ Chris Hughes (Aug 06 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/should%20fintype%20take%20a%20sort%3F/near/130996873):
<blockquote>
<p>I think the main thing has to do with elimination. If your type is<code>Sort 0</code>, there's a special case that you can only eliminate to <code>Sort 0</code>. Otherwise, in <code>Sort 1</code>, you can eliminate anywhere you like.</p>
</blockquote>
<p>So that makes sense for making inductive types Types rather than sorts, but for functions defined on an arbitrary Type, I don't see a downside.</p>

#### [ Chris Hughes (Aug 06 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/should%20fintype%20take%20a%20sort%3F/near/130997539):
<p>I should probably PR both of these</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">decidable_eq_pfun_fintype</span> <span class="o">(</span><span class="n">P</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">[</span><span class="n">decidable</span> <span class="n">P</span><span class="o">]</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="n">P</span> <span class="bp">→</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">[</span><span class="bp">Π</span> <span class="n">hp</span> <span class="o">:</span> <span class="n">P</span><span class="o">,</span> <span class="n">fintype</span> <span class="o">(</span><span class="n">α</span> <span class="n">hp</span><span class="o">)]</span>
  <span class="o">[</span><span class="bp">Π</span> <span class="n">hp</span> <span class="o">:</span> <span class="n">P</span><span class="o">,</span> <span class="n">decidable_eq</span> <span class="o">(</span><span class="n">α</span> <span class="n">hp</span><span class="o">)]</span> <span class="o">:</span> <span class="n">decidable_eq</span> <span class="o">(</span><span class="bp">Π</span> <span class="n">hp</span> <span class="o">:</span> <span class="n">P</span><span class="o">,</span> <span class="n">α</span> <span class="n">hp</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">f</span> <span class="n">g</span><span class="o">,</span> <span class="k">if</span> <span class="n">hp</span> <span class="o">:</span> <span class="n">P</span> <span class="k">then</span> <span class="n">decidable_of_iff</span> <span class="o">(</span><span class="n">f</span> <span class="n">hp</span> <span class="bp">=</span> <span class="n">g</span> <span class="n">hp</span><span class="o">)</span> <span class="o">(</span><span class="bp">⟨λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">funext</span> <span class="err">$</span> <span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">h</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">congr_fun</span> <span class="n">h</span> <span class="bp">_⟩</span><span class="o">)</span>
<span class="k">else</span> <span class="n">is_true</span> <span class="o">(</span><span class="n">funext</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="o">(</span><span class="n">hp</span> <span class="n">h</span><span class="o">)</span><span class="bp">.</span><span class="n">elim</span><span class="o">)</span>

<span class="kn">instance</span> <span class="n">fintype_pfun</span> <span class="o">(</span><span class="n">P</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">[</span><span class="n">decidable</span> <span class="n">P</span><span class="o">]</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="n">P</span> <span class="bp">→</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">[</span><span class="bp">Π</span> <span class="n">hp</span> <span class="o">:</span> <span class="n">P</span><span class="o">,</span> <span class="n">fintype</span> <span class="o">(</span><span class="n">α</span> <span class="n">hp</span><span class="o">)]</span>
  <span class="o">[</span><span class="bp">Π</span> <span class="n">hp</span> <span class="o">:</span> <span class="n">P</span><span class="o">,</span> <span class="n">decidable_eq</span> <span class="o">(</span><span class="n">α</span> <span class="n">hp</span><span class="o">)]</span> <span class="o">:</span> <span class="n">fintype</span> <span class="o">(</span><span class="bp">Π</span> <span class="n">hp</span> <span class="o">:</span> <span class="n">P</span><span class="o">,</span> <span class="n">α</span> <span class="n">hp</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">if</span> <span class="n">hp</span> <span class="o">:</span> <span class="n">P</span> <span class="k">then</span> <span class="n">fintype</span><span class="bp">.</span><span class="n">of_equiv</span> <span class="o">(</span><span class="n">α</span> <span class="n">hp</span><span class="o">)</span> <span class="bp">⟨λ</span> <span class="n">a</span> <span class="bp">_</span><span class="o">,</span> <span class="n">a</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">f</span><span class="o">,</span> <span class="n">f</span> <span class="n">hp</span><span class="o">,</span> <span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">rfl</span><span class="o">,</span> <span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span>
<span class="k">else</span> <span class="bp">⟨</span><span class="n">finset</span><span class="bp">.</span><span class="n">singleton</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="o">(</span><span class="n">hp</span> <span class="n">h</span><span class="o">)</span><span class="bp">.</span><span class="n">elim</span><span class="o">),</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">hp</span><span class="o">,</span> <span class="n">funext_iff</span><span class="o">]</span><span class="bp">⟩</span>
</pre></div>

#### [ Simon Hudon (Aug 06 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/should%20fintype%20take%20a%20sort%3F/near/130998223):
<blockquote>
<p>but for functions defined on an arbitrary Type, I don't see a downside.</p>
</blockquote>
<p>I agree. Although, I find that universe constraints have a way of propagating to infect every definition once you have one. Being more polymorphic seems easier said than done.</p>


{% endraw %}
