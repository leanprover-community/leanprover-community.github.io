---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/66073finsetsdecidablememandfilter.html
---

## Stream: [new members](index.html)
### Topic: [finsets, decidable_mem, and filter](66073finsetsdecidablememandfilter.html)

---


{% raw %}
#### [ Bryan Gin-ge Chen (Sep 11 2018 at 06:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finsets%2C%20decidable_mem%2C%20and%20filter/near/133708032):
<p>I have a filter on a finset (of finsets) that I want to construct and for some reason I'm stubbornly trying to do it constructively. Here's a stripped down version of what I have (which is part of some stuff on matroids):</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">finset</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">G</span> <span class="o">:</span> <span class="n">finset</span> <span class="o">(</span><span class="n">finset</span> <span class="n">α</span><span class="o">))</span>

<span class="c1">-- copied from init.logic</span>
<span class="kn">variable</span> <span class="n">p</span> <span class="o">:</span> <span class="kt">Prop</span>
<span class="kn">lemma</span> <span class="n">dec_not</span> <span class="o">[</span><span class="n">decidable</span> <span class="n">p</span><span class="o">]</span> <span class="o">:</span> <span class="n">decidable</span> <span class="o">(</span><span class="bp">¬</span><span class="n">p</span><span class="o">)</span> <span class="o">:=</span>
  <span class="k">if</span> <span class="n">hp</span> <span class="o">:</span> <span class="n">p</span> <span class="k">then</span> <span class="n">is_false</span> <span class="o">(</span><span class="n">absurd</span> <span class="n">hp</span><span class="o">)</span> <span class="k">else</span> <span class="n">is_true</span> <span class="n">hp</span>

<span class="n">def</span> <span class="n">is_in</span> <span class="o">(</span><span class="n">S</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">G</span> <span class="o">:</span> <span class="n">finset</span> <span class="o">(</span><span class="n">finset</span> <span class="n">α</span><span class="o">))</span> <span class="o">:</span> <span class="kt">Prop</span>
<span class="o">:=</span> <span class="n">S</span> <span class="err">∈</span> <span class="n">G</span>

<span class="n">def</span> <span class="n">is_out</span> <span class="o">(</span><span class="n">S</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">G</span> <span class="o">:</span> <span class="n">finset</span> <span class="o">(</span><span class="n">finset</span> <span class="n">α</span><span class="o">))</span> <span class="o">:</span> <span class="kt">Prop</span>
<span class="o">:=</span> <span class="bp">¬</span> <span class="n">S</span> <span class="err">∈</span> <span class="n">G</span>

<span class="kn">lemma</span> <span class="n">is_out_iff_not_in</span> <span class="o">(</span><span class="n">S</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">G</span> <span class="o">:</span> <span class="n">finset</span> <span class="o">(</span><span class="n">finset</span> <span class="n">α</span><span class="o">))</span> <span class="o">:</span>
<span class="n">is_out</span> <span class="n">S</span> <span class="n">G</span> <span class="bp">↔</span> <span class="bp">¬</span>  <span class="n">is_in</span> <span class="n">S</span> <span class="n">G</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">unfold</span> <span class="n">is_in</span> <span class="n">is_out</span><span class="bp">;</span> <span class="n">simp</span>

<span class="kn">instance</span> <span class="n">decidable_in</span> <span class="o">(</span><span class="n">S</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">G</span> <span class="o">:</span> <span class="n">finset</span> <span class="o">(</span><span class="n">finset</span> <span class="n">α</span><span class="o">))</span> <span class="o">:</span> <span class="n">decidable</span> <span class="o">(</span><span class="n">is_in</span> <span class="n">S</span> <span class="n">G</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">finset</span><span class="bp">.</span><span class="n">decidable_mem</span> <span class="n">S</span> <span class="n">G</span>

<span class="c">/-</span><span class="cm"> failed to generate bytecode for &#39;decidable_out&#39;</span>
<span class="cm">code generation failed, VM does not have code for &#39;dec_not&#39;</span>
<span class="cm">... ??? -/</span>
<span class="kn">instance</span> <span class="n">decidable_out</span> <span class="o">(</span><span class="n">S</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">G</span> <span class="o">:</span> <span class="n">finset</span> <span class="o">(</span><span class="n">finset</span> <span class="n">α</span><span class="o">))</span> <span class="o">:</span> <span class="n">decidable</span> <span class="o">(</span><span class="n">is_out</span> <span class="n">S</span> <span class="n">G</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">rw</span> <span class="n">is_out_iff_not_in</span><span class="o">,</span>
<span class="n">exact</span> <span class="n">dec_not</span> <span class="o">(</span><span class="n">is_in</span> <span class="n">S</span> <span class="n">G</span><span class="o">)</span>
<span class="kn">end</span>

<span class="n">def</span> <span class="n">is_min_out</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">G</span> <span class="o">:</span><span class="n">finset</span> <span class="o">(</span><span class="n">finset</span> <span class="n">α</span><span class="o">))</span> <span class="o">:</span> <span class="kt">Prop</span>
<span class="o">:=</span> <span class="n">is_out</span> <span class="n">x</span> <span class="n">G</span> <span class="bp">∧</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">y</span><span class="o">,</span> <span class="n">y</span> <span class="err">⊂</span> <span class="n">x</span> <span class="bp">→</span> <span class="n">is_in</span> <span class="n">y</span> <span class="n">G</span><span class="o">)</span>

<span class="n">def</span> <span class="n">min_out</span> <span class="o">(</span><span class="n">G</span> <span class="o">:</span> <span class="n">finset</span> <span class="o">(</span><span class="n">finset</span> <span class="n">α</span><span class="o">))</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">):</span> <span class="n">finset</span> <span class="o">(</span><span class="n">finset</span> <span class="n">α</span><span class="o">)</span>
<span class="o">:=</span> <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">powerset</span> <span class="n">F</span><span class="o">)</span><span class="bp">.</span><span class="n">filter</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">is_min_out</span> <span class="n">x</span> <span class="n">G</span><span class="o">)</span>
</pre></div>


<p>First, you can see how in proving <code>decidable_out</code>, I used <code>dec_not</code>, a lemma which is copied from an instance from lean's <code>init.logic</code>. Is there a way of just convincing the elaborator to figure this out for me?</p>
<p>Second, what does the weird warning message by <code>decidable_out</code> mean?</p>
<p>Third and finally, is it even possible to construct an instance of <code>decidable_pred</code> for <code>is_min_out</code> so that I can define <code>min_out</code> constructively? What if I assume a little bit more about α? Do I need to figure out how to use <code>data.equiv.encodable</code>or something?</p>
<p>Thanks again!</p>

#### [ Mario Carneiro (Sep 11 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finsets%2C%20decidable_mem%2C%20and%20filter/near/133708513):
<blockquote>
<p>First, you can see how in proving decidable_out, I used dec_not, a lemma which is copied from an instance from lean's init.logic. Is there a way of just convincing the elaborator to figure this out for me?</p>
</blockquote>
<p>As you say, this is already in core lean, under the (autogenerated) name <code>not.decidable</code>. The elaborator will infer it automatically in most places, but if you need to trigger typeclass inference manually use the tactic <code>apply_instance</code>.</p>
<blockquote>
<p>Second, what does the weird warning message by decidable_out mean?</p>
</blockquote>
<p><code>lemma</code>s and <code>theorem</code>s don't generate code in the VM. This means that you should basically always mark any inhabitant of a Type as a <code>def</code> not a <code>lemma</code>, or else you will get these strange error messages when you use the <code>def</code>-that-isn't.</p>

#### [ Mario Carneiro (Sep 11 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finsets%2C%20decidable_mem%2C%20and%20filter/near/133708566):
<p>I'm not sure why you are redefining all these symbols. You are just making typeclass inference harder for no reason</p>

#### [ Mario Carneiro (Sep 11 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finsets%2C%20decidable_mem%2C%20and%20filter/near/133708937):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">is_min_out</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">G</span> <span class="o">:</span> <span class="n">finset</span> <span class="o">(</span><span class="n">finset</span> <span class="n">α</span><span class="o">))</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="n">x</span> <span class="err">∉</span> <span class="n">G</span> <span class="bp">∧</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">y</span><span class="o">,</span> <span class="n">y</span> <span class="err">⊂</span> <span class="n">x</span> <span class="bp">→</span> <span class="n">y</span> <span class="err">∈</span> <span class="n">G</span><span class="o">)</span>

<span class="kn">instance</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">G</span> <span class="o">:</span> <span class="n">finset</span> <span class="o">(</span><span class="n">finset</span> <span class="n">α</span><span class="o">))</span> <span class="o">:</span> <span class="n">decidable</span> <span class="o">(</span><span class="n">is_min_out</span> <span class="n">x</span> <span class="n">G</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">decidable_of_iff</span> <span class="o">(</span><span class="n">x</span> <span class="err">∉</span> <span class="n">G</span> <span class="bp">∧</span> <span class="bp">∀</span> <span class="n">y</span> <span class="err">∈</span> <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">powerset</span> <span class="n">x</span><span class="o">)</span><span class="bp">.</span><span class="n">erase</span> <span class="n">x</span><span class="o">,</span> <span class="n">y</span> <span class="err">∈</span> <span class="n">G</span><span class="o">)</span> <span class="k">begin</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">is_min_out</span><span class="o">,</span> <span class="o">(</span><span class="err">⊂</span><span class="o">),</span> <span class="n">finset</span><span class="bp">.</span><span class="n">ssubset_iff</span><span class="o">],</span>
  <span class="n">refine</span> <span class="n">and_congr</span> <span class="n">iff</span><span class="bp">.</span><span class="n">rfl</span> <span class="o">(</span><span class="n">forall_congr</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">y</span><span class="o">,</span> <span class="bp">_</span><span class="o">),</span>
  <span class="n">refine</span> <span class="bp">⟨λ</span> <span class="n">H</span> <span class="n">h₁</span> <span class="n">h₂</span><span class="o">,</span> <span class="n">H</span> <span class="o">(</span><span class="n">mt</span> <span class="bp">_</span> <span class="n">h₂</span><span class="o">)</span> <span class="n">h₁</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">H</span> <span class="n">h₁</span> <span class="n">h₂</span><span class="o">,</span> <span class="n">H</span> <span class="n">h₂</span> <span class="o">(</span><span class="n">mt</span> <span class="bp">_</span> <span class="n">h₁</span><span class="o">)</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">rintro</span> <span class="n">rfl</span><span class="o">,</span> <span class="n">refl</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">exact</span> <span class="n">finset</span><span class="bp">.</span><span class="n">subset</span><span class="bp">.</span><span class="n">antisymm</span> <span class="n">h₂</span> <span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Bryan Gin-ge Chen (Sep 11 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finsets%2C%20decidable_mem%2C%20and%20filter/near/133709166):
<p>Thanks so much Mario!</p>
<blockquote>
<p>I'm not sure why you are redefining all these symbols. You are just making typeclass inference harder for no reason</p>
</blockquote>
<p>The honest reason is that I don't know any better. What precisely should I be avoiding?</p>

#### [ Bryan Gin-ge Chen (Sep 11 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finsets%2C%20decidable_mem%2C%20and%20filter/near/133709251):
<p>Oh, you mean just the names <code>is_in</code> and <code>is_out</code>. Those are artifacts of my making a MWE; in reality, there's a structure that I have to pull the finset from.</p>


{% endraw %}
