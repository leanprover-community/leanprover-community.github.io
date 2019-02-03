---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/73892maximalfinsetinfinsetoffinsets.html
---

## Stream: [new members](index.html)
### Topic: [maximal finset in finset of finsets](73892maximalfinsetinfinsetoffinsets.html)

---


{% raw %}
#### [ Bryan Gin-ge Chen (Sep 13 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133904539):
<p>Excuse the weird title. I'm trying to prove that a finset of subsets of a finset must contain an element of largest size, without relying on classical choice:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">not_empty_has_max_size</span> <span class="o">{</span><span class="n">E</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">F</span> <span class="o">:</span> <span class="n">finset</span> <span class="o">(</span><span class="n">finset</span> <span class="n">α</span><span class="o">)}</span> <span class="o">:</span>
<span class="n">F</span> <span class="err">⊆</span> <span class="n">powerset</span> <span class="n">E</span> <span class="bp">→</span> <span class="n">F</span> <span class="bp">≠</span> <span class="err">∅</span> <span class="bp">→</span> <span class="bp">∃</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">F</span><span class="o">,</span> <span class="bp">∀</span> <span class="n">g</span> <span class="err">∈</span> <span class="n">F</span><span class="o">,</span> <span class="n">card</span> <span class="n">g</span> <span class="bp">≤</span> <span class="n">card</span> <span class="n">x</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>Here's my attempt so far, which seems to have taken me down a strange path:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">finset</span>

<span class="kn">variable</span> <span class="n">α</span><span class="o">:</span><span class="kt">Type</span><span class="bp">*</span>
<span class="kn">variable</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">α</span><span class="o">]</span>

<span class="kn">open</span> <span class="n">finset</span>

<span class="kn">lemma</span> <span class="n">finset</span><span class="bp">.</span><span class="n">card_one_eq</span> <span class="o">{</span><span class="n">E</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">}</span> <span class="o">:</span> <span class="n">card</span> <span class="n">E</span> <span class="bp">=</span> <span class="mi">1</span> <span class="bp">↔</span> <span class="bp">∃</span> <span class="n">a</span><span class="o">,</span> <span class="n">E</span> <span class="bp">=</span> <span class="n">finset</span><span class="bp">.</span><span class="n">singleton</span> <span class="n">a</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">have</span> <span class="n">h</span> <span class="o">:</span> <span class="bp">_</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">multiset</span><span class="bp">.</span><span class="n">card_eq_one</span> <span class="n">α</span> <span class="n">E</span><span class="bp">.</span><span class="n">val</span><span class="o">,</span>
  <span class="n">unfold</span> <span class="n">card</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">iff_congr</span> <span class="n">h</span><span class="o">,</span> <span class="n">exists_congr</span><span class="o">],</span>
  <span class="n">intro</span> <span class="n">a</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="err">←</span><span class="n">singleton_val</span><span class="o">,</span> <span class="n">val_inj</span><span class="o">],</span>
  <span class="n">refl</span>
<span class="kn">end</span>

<span class="kn">lemma</span> <span class="n">powerset_empty</span> <span class="o">:</span> <span class="n">powerset</span> <span class="o">(</span><span class="err">∅</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="bp">=</span> <span class="n">finset</span><span class="bp">.</span><span class="n">singleton</span> <span class="err">∅</span> <span class="o">:=</span> <span class="n">rfl</span>

<span class="kn">lemma</span> <span class="n">subset_singleton</span> <span class="o">{</span><span class="n">F</span> <span class="o">:</span> <span class="n">finset</span> <span class="o">(</span><span class="n">finset</span> <span class="n">α</span><span class="o">)}</span> <span class="o">:</span>
<span class="n">F</span> <span class="err">⊆</span> <span class="n">finset</span><span class="bp">.</span><span class="n">singleton</span> <span class="o">(</span><span class="err">∅</span><span class="o">:</span><span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="bp">↔</span>
<span class="n">F</span> <span class="bp">=</span> <span class="err">∅</span> <span class="bp">∨</span> <span class="n">F</span> <span class="bp">=</span> <span class="n">finset</span><span class="bp">.</span><span class="n">singleton</span> <span class="err">∅</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">split</span><span class="o">,</span>
  <span class="n">intro</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">by_cases</span> <span class="n">h1</span> <span class="o">:</span> <span class="n">F</span> <span class="bp">=</span> <span class="err">∅</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="n">h1</span><span class="o">,</span>
  <span class="k">have</span> <span class="o">:</span> <span class="n">F</span> <span class="bp">=</span> <span class="n">finset</span><span class="bp">.</span><span class="n">singleton</span> <span class="err">∅</span> <span class="o">:=</span> <span class="k">begin</span>
    <span class="n">sorry</span>
  <span class="kn">end</span><span class="o">,</span>
  <span class="n">sorry</span><span class="o">,</span>
  <span class="n">intro</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">or</span><span class="bp">.</span><span class="n">elim</span> <span class="n">h</span> <span class="o">(</span><span class="k">begin</span>
    <span class="n">intro</span> <span class="n">h1</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">h1</span><span class="o">,</span>
    <span class="n">simp</span>
  <span class="kn">end</span><span class="o">)</span> <span class="o">(</span><span class="k">begin</span>
    <span class="n">intro</span> <span class="n">h1</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">h1</span><span class="o">,</span>
    <span class="n">simp</span>
  <span class="kn">end</span><span class="o">)</span>
<span class="kn">end</span>

<span class="kn">lemma</span> <span class="n">not_empty_has_max_size</span> <span class="o">{</span><span class="n">E</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">F</span> <span class="o">:</span> <span class="n">finset</span> <span class="o">(</span><span class="n">finset</span> <span class="n">α</span><span class="o">)}</span> <span class="o">:</span>
<span class="n">F</span> <span class="err">⊆</span> <span class="n">powerset</span> <span class="n">E</span> <span class="bp">→</span> <span class="n">F</span> <span class="bp">≠</span> <span class="err">∅</span> <span class="bp">→</span> <span class="bp">∃</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">F</span><span class="o">,</span> <span class="bp">∀</span> <span class="n">g</span> <span class="err">∈</span> <span class="n">F</span><span class="o">,</span> <span class="n">card</span> <span class="n">g</span> <span class="bp">≤</span> <span class="n">card</span> <span class="n">x</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">intros</span> <span class="n">FPE</span> <span class="n">Fne</span><span class="o">,</span>
  <span class="n">induction</span> <span class="n">E</span> <span class="kn">using</span> <span class="n">finset</span><span class="bp">.</span><span class="n">induction</span> <span class="k">with</span> <span class="n">a</span> <span class="n">E</span> <span class="n">ha</span> <span class="n">hE</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">powerset_empty</span><span class="o">,</span> <span class="n">subset_singleton</span><span class="o">]</span> <span class="n">at</span> <span class="n">FPE</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">or</span><span class="bp">.</span><span class="n">elim</span> <span class="n">FPE</span> <span class="o">(</span><span class="k">by</span> <span class="n">contradiction</span><span class="o">)</span> <span class="k">begin</span>
    <span class="n">intro</span> <span class="n">h</span><span class="o">,</span>
    <span class="n">exact</span> <span class="n">exists</span><span class="bp">.</span><span class="n">intro</span> <span class="err">∅</span> <span class="k">begin</span>
      <span class="n">rw</span> <span class="n">h</span><span class="o">,</span>
      <span class="n">exact</span> <span class="n">exists</span><span class="bp">.</span><span class="n">intro</span> <span class="o">(</span><span class="n">mem_singleton_self</span> <span class="err">∅</span><span class="o">)</span> <span class="o">(</span><span class="k">begin</span>
        <span class="n">intros</span> <span class="n">g</span> <span class="n">hg</span><span class="o">,</span>
        <span class="n">rw</span> <span class="n">mem_singleton</span> <span class="n">at</span> <span class="n">hg</span><span class="o">,</span>
        <span class="n">rw</span> <span class="n">hg</span>
      <span class="kn">end</span><span class="o">)</span>
    <span class="kn">end</span>
  <span class="kn">end</span><span class="o">,</span>
  <span class="n">by_cases</span> <span class="n">hh1</span> <span class="o">:</span> <span class="n">F</span> <span class="err">⊆</span> <span class="n">powerset</span> <span class="n">E</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">hE</span> <span class="n">hh1</span><span class="o">,</span>
  <span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>


<p>I'm hoping someone can point me in a smarter direction. Thanks as always!</p>

#### [ Reid Barton (Sep 13 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133904686):
<p>Doesn't every finset of finsets contain an element of largest size, regardless of <code>E</code> and the associated condition?</p>

#### [ Bryan Gin-ge Chen (Sep 13 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133904800):
<p>Maybe, I got worried that without having some kind of bound on the size of the finsets I wouldn't be able to prove it without choice.</p>

#### [ Kevin Buzzard (Sep 13 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905022):
<p>just use finset.map (I'm assuming this exists!) on finset.card to get a finset of nats and then take the max and work your way back?</p>

#### [ Reid Barton (Sep 13 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905060):
<p>A finset is basically a list, and you could write a program that takes a list of lists and returns one of the maximum length, so there should be no trouble proving it constructively.</p>

#### [ Reid Barton (Sep 13 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905178):
<p>Yeah, I was looking for a function on finset which is max after applying a function, but I guess since nat has decidable equality you can use <code>finset.map</code> in this case.</p>

#### [ Reid Barton (Sep 13 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905214):
<p>Sorry, not <code>finset.map</code> but <code>finset.image</code>.</p>

#### [ Chris Hughes (Sep 13 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905271):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">not_empty_has_max_size</span> <span class="o">{</span><span class="n">E</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">F</span> <span class="o">:</span> <span class="n">finset</span> <span class="o">(</span><span class="n">finset</span> <span class="n">α</span><span class="o">)}</span> <span class="o">:</span>
<span class="n">F</span> <span class="err">⊆</span> <span class="n">powerset</span> <span class="n">E</span> <span class="bp">→</span> <span class="n">F</span> <span class="bp">≠</span> <span class="err">∅</span> <span class="bp">→</span> <span class="bp">∃</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">F</span><span class="o">,</span> <span class="bp">∀</span> <span class="n">g</span> <span class="err">∈</span> <span class="n">F</span><span class="o">,</span> <span class="n">card</span> <span class="n">g</span> <span class="bp">≤</span> <span class="n">card</span> <span class="n">x</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="bp">_</span> <span class="n">h</span><span class="o">,</span> <span class="k">let</span> <span class="bp">⟨</span><span class="n">n</span><span class="o">,</span> <span class="n">hn</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="o">(</span><span class="n">max_of_ne_empty</span> <span class="o">(</span><span class="n">mt</span> <span class="n">image_eq_empty</span><span class="bp">.</span><span class="mi">1</span> <span class="n">h</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">a</span><span class="o">,</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">finset</span><span class="bp">.</span><span class="n">max</span> <span class="o">(</span><span class="n">F</span><span class="bp">.</span><span class="n">image</span> <span class="n">card</span><span class="o">))</span> <span class="k">in</span>
<span class="k">let</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">hx₁</span><span class="o">,</span> <span class="n">hx₂</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">mem_image</span><span class="bp">.</span><span class="mi">1</span> <span class="o">(</span><span class="n">mem_of_max</span> <span class="n">hn</span><span class="o">)</span> <span class="k">in</span>
<span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">hx₁</span><span class="o">,</span> <span class="n">hx₂</span><span class="bp">.</span><span class="n">symm</span> <span class="bp">▸</span> <span class="bp">λ</span> <span class="n">g</span> <span class="n">hg</span><span class="o">,</span> <span class="n">le_max_of_mem</span> <span class="o">(</span><span class="n">mem_image</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">⟨</span><span class="n">g</span><span class="o">,</span> <span class="n">hg</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span><span class="o">)</span> <span class="n">hn</span><span class="bp">⟩</span>
</pre></div>

#### [ Bryan Gin-ge Chen (Sep 13 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905289):
<p>Wow, thanks!</p>

#### [ Mario Carneiro (Sep 13 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905350):
<p>That uses decidable_eq, doesn't it?</p>

#### [ Kevin Buzzard (Sep 13 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905394):
<p>rofl</p>

#### [ Mario Carneiro (Sep 13 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905407):
<p>My suggestion:</p>
<div class="codehilite"><pre><span></span>import data.finset

section
variables {α : Type*} (r : α → α → Prop) [is_preorder α r]
local infix ` ≼ `:50 := r

theorem list_zorn : ∀ l : list α, l ≠ [] → ∃ a ∈ l, ∀ b, a ≼ b → b ≼ a := sorry
theorem finset_zorn : ∀ s : finset α, s ≠ ∅ → ∃ a ∈ s, ∀ b, a ≼ b → b ≼ a := sorry

end
</pre></div>

#### [ Bryan Gin-ge Chen (Sep 13 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905415):
<p>I would have never thought of using finset.image. And yes, decidable_eq is allowed.</p>

#### [ Mario Carneiro (Sep 13 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905436):
<p>here the relation is <code>card s &lt;= card t</code> on finsets</p>

#### [ Kenny Lau (Sep 13 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905447):
<blockquote>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">not_empty_has_max_size</span> <span class="o">{</span><span class="n">E</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">F</span> <span class="o">:</span> <span class="n">finset</span> <span class="o">(</span><span class="n">finset</span> <span class="n">α</span><span class="o">)}</span> <span class="o">:</span>
<span class="n">F</span> <span class="err">⊆</span> <span class="n">powerset</span> <span class="n">E</span> <span class="bp">→</span> <span class="n">F</span> <span class="bp">≠</span> <span class="err">∅</span> <span class="bp">→</span> <span class="bp">∃</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">F</span><span class="o">,</span> <span class="bp">∀</span> <span class="n">g</span> <span class="err">∈</span> <span class="n">F</span><span class="o">,</span> <span class="n">card</span> <span class="n">g</span> <span class="bp">≤</span> <span class="n">card</span> <span class="n">x</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="bp">_</span> <span class="n">h</span><span class="o">,</span> <span class="k">let</span> <span class="bp">⟨</span><span class="n">n</span><span class="o">,</span> <span class="n">hn</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="o">(</span><span class="n">max_of_ne_empty</span> <span class="o">(</span><span class="n">mt</span> <span class="n">image_eq_empty</span><span class="bp">.</span><span class="mi">1</span> <span class="n">h</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">a</span><span class="o">,</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">finset</span><span class="bp">.</span><span class="n">max</span> <span class="o">(</span><span class="n">F</span><span class="bp">.</span><span class="n">image</span> <span class="n">card</span><span class="o">))</span> <span class="k">in</span>
<span class="k">let</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">hx₁</span><span class="o">,</span> <span class="n">hx₂</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">mem_image</span><span class="bp">.</span><span class="mi">1</span> <span class="o">(</span><span class="n">mem_of_max</span> <span class="n">hn</span><span class="o">)</span> <span class="k">in</span>
<span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">hx₁</span><span class="o">,</span> <span class="n">hx₂</span><span class="bp">.</span><span class="n">symm</span> <span class="bp">▸</span> <span class="bp">λ</span> <span class="n">g</span> <span class="n">hg</span><span class="o">,</span> <span class="n">le_max_of_mem</span> <span class="o">(</span><span class="n">mem_image</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">⟨</span><span class="n">g</span><span class="o">,</span> <span class="n">hg</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span><span class="o">)</span> <span class="n">hn</span><span class="bp">⟩</span>
</pre></div>


</blockquote>
<p>what is the role of E in your theorem?</p>

#### [ Kevin Buzzard (Sep 13 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905450):
<p>you can just prove this using the zorn in mathlib</p>

#### [ Mario Carneiro (Sep 13 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905467):
<p>of course, but this (1) doesn't use nonconstructive axioms and (2) doesn't need the chain condition</p>

#### [ Bryan Gin-ge Chen (Sep 13 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905518):
<p>If E is unnecessary here all the better. In the "application", it's the ground set of a matroid.</p>

#### [ Reid Barton (Sep 13 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905536):
<p><code>decidable_eq nat</code> doesn't use axioms either</p>

#### [ Mario Carneiro (Sep 13 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905569):
<p>yes, but the theorem can be proven constructively without that assumption</p>

#### [ Reid Barton (Sep 13 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905579):
<p>Yeah, the max/min stuff should be on multisets.</p>

#### [ Mario Carneiro (Sep 13 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905596):
<p>Unfortunately, here max/min don't work directly since it's not a poset</p>

#### [ Kenny Lau (Sep 13 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905633):
<p>you can have zorn on a set (i.e. type) S as long as you have a choice function on P(P(S))\{{}}, right</p>

#### [ Mario Carneiro (Sep 13 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905662):
<p>yes, but we don't have that here and I claim it's still provable</p>

#### [ Kenny Lau (Sep 13 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905694):
<p>sure</p>

#### [ Reid Barton (Sep 13 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905726):
<p>I mean we should just define <code>max</code> for a set in the same style as <code>prod</code>, in terms of <code>max</code> on multiset, and nat is already a decidable linear whatever so there would be no problem there.</p>
<div class="codehilite"><pre><span></span><span class="kn">protected</span> <span class="n">def</span> <span class="n">prod</span> <span class="o">[</span><span class="n">comm_monoid</span> <span class="n">β</span><span class="o">]</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="n">β</span> <span class="o">:=</span> <span class="o">(</span><span class="n">s</span><span class="bp">.</span><span class="mi">1</span><span class="bp">.</span><span class="n">map</span> <span class="n">f</span><span class="o">)</span><span class="bp">.</span><span class="n">prod</span>
</pre></div>

#### [ Mario Carneiro (Sep 13 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905781):
<p>what is this about <code>nat</code>? I don't see it in the question</p>

#### [ Reid Barton (Sep 13 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905798):
<p><code>nat</code> is the codomain of <code>finset.card</code> (I assume)</p>

#### [ Mario Carneiro (Sep 13 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905829):
<p>sure but that doesn't really matter; we are doing the choosing on <code>finset A</code> which is not decidable (unless you assume so)</p>

#### [ Mario Carneiro (Sep 13 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905887):
<p>all that decidability of nat gives you is decidability of the relation <code>≼</code> given by <code>s ≼ t ↔ card s ≤ card t</code></p>

#### [ Kenny Lau (Sep 13 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905902):
<p>I guess Kevin ran away from all this decidable nonsense :P</p>

#### [ Reid Barton (Sep 13 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133905936):
<p>I'm a bit confused.<br>
All I am saying is that the original thing should be a direct conclusion of some lemma about <code>max</code> of a <code>multiset nat</code>, applied to <code>F.1.map finset.card</code>.</p>

#### [ Reid Barton (Sep 13 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133906034):
<p>That lemma being the analogue for multisets of <code>finset.max_of_ne_empty</code> and <code>finset.le_max_of_mem</code></p>

#### [ Reid Barton (Sep 13 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133906232):
<p>But I guess maybe <code>decidable_linear_order</code> is stronger than <code>decidable_eq</code> anyways, so it doesn't really matter.</p>

#### [ Mario Carneiro (Sep 13 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133906443):
<p>the point is this isn't a question about decidable linear orders, but decidable preorders. Lack of uniqueness of the maximum makes it hard to define a function like <code>max</code> directly</p>

#### [ Reid Barton (Sep 13 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133906534):
<p>You mean something like a "pre-total order"?</p>

#### [ Mario Carneiro (Sep 13 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133906805):
<p><code>is_total_preorder</code> exists in core btw</p>

#### [ Mario Carneiro (Sep 13 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133906808):
<p>but totality is not needed</p>

#### [ Reid Barton (Sep 13 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133906861):
<p>Finding the maximum value of a function on a finite set is a pretty standard thing to do. Of course there might not be a unique element of the set which maximizes the function, but the maximum value of the function is still well-defined. And often you only need some statement about the existence of a maximizing element.<br>
It's not very obvious how you're supposed to get this from only the ability to take the maximum element of a finite set (in a totally ordered type).</p>

#### [ Mario Carneiro (Sep 13 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133906917):
<p>like kenny and chris have shown, you can take the image of the finset and get the maximum</p>

#### [ Mario Carneiro (Sep 13 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133906965):
<p>unless you care about  constructivity and then you have to prove it from scratch</p>

#### [ Mario Carneiro (Sep 13 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133906991):
<p>that works in any total preorder</p>

#### [ Mario Carneiro (Sep 13 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133907005):
<p>in a partial order, I don't see any easy way to get it except zorn's lemma</p>

#### [ Kenny Lau (Sep 13 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133907255):
<blockquote>
<p>like kenny and chris have shown, you can take the image of the finset and get the maximum</p>
</blockquote>
<p>I don't think I did anything</p>

#### [ Bryan Gin-ge Chen (Sep 13 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133907303):
<p>I care a little bit about constructivity, but maybe I'll see how far I can get with Chris's solution first.</p>

#### [ Mario Carneiro (Sep 13 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/maximal%20finset%20in%20finset%20of%20finsets/near/133909339):
<p>oops, I didn't see that you just quoted chris's solution</p>


{% endraw %}
