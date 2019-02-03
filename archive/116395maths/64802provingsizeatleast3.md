---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/64802provingsizeatleast3.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [proving size at least 3](https://leanprover-community.github.io/archive/116395maths/64802provingsizeatleast3.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Aug 13 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/proving%20size%20at%20least%203/near/132037729):
<p>I would be interested in a relatively slick proof of either of the below examples:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">fintype</span>
<span class="kn">import</span> <span class="n">set_theory</span><span class="bp">.</span><span class="n">cardinal</span>

<span class="c1">-- fintype</span>
<span class="kn">open</span> <span class="n">fintype</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">Hab</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≠</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">Hbc</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">≠</span> <span class="n">c</span><span class="o">)</span> <span class="o">(</span><span class="n">Hac</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≠</span> <span class="n">c</span><span class="o">)</span> <span class="o">:</span>
<span class="n">card</span> <span class="n">α</span> <span class="bp">≥</span> <span class="mi">3</span> <span class="o">:=</span> <span class="n">sorry</span>

<span class="c1">-- general</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">Hab</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≠</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">Hbc</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">≠</span> <span class="n">c</span><span class="o">)</span> <span class="o">(</span><span class="n">Hac</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≠</span> <span class="n">c</span><span class="o">)</span> <span class="o">:</span>
<span class="n">cardinal</span><span class="bp">.</span><span class="n">mk</span> <span class="n">α</span> <span class="bp">≥</span> <span class="mi">3</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>This is for pedagogical purposes and I don't really mind if we stick to fintypes or not.</p>
<p>As a side issue, is <code>cardinal.mk</code> really the way to talk about the cardinality of a type? Is there not some interface function?</p>

#### [ Mario Carneiro (Aug 13 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/proving%20size%20at%20least%203/near/132037883):
<p><code>cardinal.mk</code> is the interface function</p>

#### [ Kenny Lau (Aug 13 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/proving%20size%20at%20least%203/near/132038796):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">fintype</span>
<span class="kn">import</span> <span class="n">set_theory</span><span class="bp">.</span><span class="n">cardinal</span>

<span class="bp">@</span><span class="o">[</span><span class="n">derive</span> <span class="n">decidable_eq</span><span class="o">]</span>
<span class="kn">inductive</span> <span class="n">three</span> <span class="o">:</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">A</span> <span class="o">:</span> <span class="n">three</span>
<span class="bp">|</span> <span class="n">B</span> <span class="o">:</span> <span class="n">three</span>
<span class="bp">|</span> <span class="n">C</span> <span class="o">:</span> <span class="n">three</span>

<span class="kn">open</span> <span class="n">three</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">fintype</span> <span class="n">three</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">elems</span> <span class="o">:=</span> <span class="o">{</span><span class="n">A</span><span class="o">,</span> <span class="n">B</span><span class="o">,</span> <span class="n">C</span><span class="o">},</span>
  <span class="n">complete</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="k">by</span> <span class="n">cases</span> <span class="n">x</span><span class="bp">;</span> <span class="n">simp</span> <span class="o">}</span>

<span class="kn">theorem</span> <span class="n">three</span><span class="bp">.</span><span class="n">cardinal</span> <span class="o">:</span> <span class="n">cardinal</span><span class="bp">.</span><span class="n">mk</span> <span class="n">three</span> <span class="bp">=</span> <span class="mi">3</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">cardinal</span><span class="bp">.</span><span class="n">fintype_card</span> <span class="n">three</span><span class="o">)</span><span class="bp">.</span><span class="n">trans</span> <span class="err">$</span>
<span class="k">show</span> <span class="o">((</span><span class="mi">3</span> <span class="o">:</span> <span class="n">nat</span><span class="o">)</span> <span class="o">:</span> <span class="n">cardinal</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">3</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span>

<span class="c1">-- fintype</span>
<span class="kn">open</span> <span class="n">fintype</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">Hab</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≠</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">Hbc</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">≠</span> <span class="n">c</span><span class="o">)</span> <span class="o">(</span><span class="n">Hac</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≠</span> <span class="n">c</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">card</span> <span class="n">α</span> <span class="bp">≥</span> <span class="mi">3</span> <span class="o">:=</span>
<span class="k">show</span> <span class="n">card</span> <span class="n">three</span> <span class="bp">≤</span> <span class="n">card</span> <span class="n">α</span><span class="o">,</span> <span class="k">from</span>
<span class="n">card_le_of_injective</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">n</span><span class="o">,</span> <span class="n">three</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">n</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span><span class="o">)</span> <span class="err">$</span>
<span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span> <span class="n">h</span><span class="o">,</span> <span class="k">by</span> <span class="n">cases</span> <span class="n">x</span><span class="bp">;</span> <span class="n">cases</span> <span class="n">y</span><span class="bp">;</span> <span class="n">dsimp</span> <span class="n">at</span> <span class="n">h</span><span class="bp">;</span> <span class="n">cc</span>

<span class="c1">-- general</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">Hab</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≠</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">Hbc</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">≠</span> <span class="n">c</span><span class="o">)</span> <span class="o">(</span><span class="n">Hac</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≠</span> <span class="n">c</span><span class="o">)</span> <span class="o">:</span>
<span class="n">cardinal</span><span class="bp">.</span><span class="n">mk</span> <span class="n">α</span> <span class="bp">≥</span> <span class="mi">3</span> <span class="o">:=</span>
<span class="n">three</span><span class="bp">.</span><span class="n">cardinal</span> <span class="bp">▸</span> <span class="n">nonempty</span><span class="bp">.</span><span class="n">intro</span> <span class="bp">⟨λ</span> <span class="n">n</span><span class="o">,</span> <span class="n">three</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">n</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span><span class="o">,</span>
<span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span> <span class="n">h</span><span class="o">,</span> <span class="k">by</span> <span class="n">cases</span> <span class="n">x</span><span class="bp">;</span> <span class="n">cases</span> <span class="n">y</span><span class="bp">;</span> <span class="n">dsimp</span> <span class="n">at</span> <span class="n">h</span><span class="bp">;</span> <span class="n">cc</span><span class="bp">⟩</span>
</pre></div>

#### [ Mario Carneiro (Aug 13 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/proving%20size%20at%20least%203/near/132038797):
<p>hm, I needed some additional library functions for this, attached. The main proof is not so hard:</p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">fintype</span><span class="bp">.</span><span class="n">card_coe</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">fintype</span><span class="bp">.</span><span class="n">card</span> <span class="o">(</span><span class="err">↑</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="bp">=</span> <span class="n">s</span><span class="bp">.</span><span class="n">card</span> <span class="o">:=</span> <span class="n">card_attach</span>

<span class="kn">theorem</span> <span class="n">card_le_of_finset</span> <span class="o">{</span><span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span>
  <span class="o">(</span><span class="n">s</span><span class="bp">.</span><span class="n">card</span> <span class="o">:</span> <span class="n">cardinal</span><span class="o">)</span> <span class="bp">≤</span> <span class="n">cardinal</span><span class="bp">.</span><span class="n">mk</span> <span class="n">α</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">rw</span> <span class="o">(</span><span class="bp">_</span> <span class="o">:</span> <span class="o">(</span><span class="n">s</span><span class="bp">.</span><span class="n">card</span> <span class="o">:</span> <span class="n">cardinal</span><span class="o">)</span> <span class="bp">=</span> <span class="n">cardinal</span><span class="bp">.</span><span class="n">mk</span> <span class="o">(</span><span class="err">↑</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)),</span>
  <span class="o">{</span> <span class="n">exact</span> <span class="bp">⟨</span><span class="n">function</span><span class="bp">.</span><span class="n">embedding</span><span class="bp">.</span><span class="n">subtype</span> <span class="bp">_⟩</span> <span class="o">},</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">cardinal</span><span class="bp">.</span><span class="n">fintype_card</span><span class="o">,</span> <span class="n">fintype</span><span class="bp">.</span><span class="n">card_coe</span><span class="o">]</span>
<span class="kn">end</span>

<span class="c1">-- fintype</span>
<span class="kn">open</span> <span class="n">fintype</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">Hab</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≠</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">Hbc</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">≠</span> <span class="n">c</span><span class="o">)</span> <span class="o">(</span><span class="n">Hac</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≠</span> <span class="n">c</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">card</span> <span class="n">α</span> <span class="bp">≥</span> <span class="mi">3</span> <span class="o">:=</span>
<span class="n">finset</span><span class="bp">.</span><span class="n">card_le_of_subset</span> <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">subset_univ</span> <span class="bp">⟨</span><span class="n">a</span><span class="bp">::</span><span class="n">b</span><span class="bp">::</span><span class="n">c</span><span class="bp">::</span><span class="mi">0</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span> <span class="bp">*⟩</span><span class="o">)</span>

<span class="c1">-- general</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">Hab</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≠</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">Hbc</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">≠</span> <span class="n">c</span><span class="o">)</span> <span class="o">(</span><span class="n">Hac</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≠</span> <span class="n">c</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">cardinal</span><span class="bp">.</span><span class="n">mk</span> <span class="n">α</span> <span class="bp">≥</span> <span class="mi">3</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">suffices</span> <span class="o">:</span> <span class="o">((</span><span class="mi">3</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">cardinal</span><span class="o">)</span> <span class="bp">≤</span> <span class="n">cardinal</span><span class="bp">.</span><span class="n">mk</span> <span class="n">α</span><span class="o">,</span> <span class="o">{</span><span class="n">simpa</span><span class="o">},</span>
  <span class="n">exact</span> <span class="n">card_le_of_finset</span> <span class="bp">⟨</span><span class="n">a</span><span class="bp">::</span><span class="n">b</span><span class="bp">::</span><span class="n">c</span><span class="bp">::</span><span class="mi">0</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span> <span class="bp">*⟩</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Aug 13 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/proving%20size%20at%20least%203/near/132038801):
<p>just 3 seconds apart!</p>

#### [ Kevin Buzzard (Aug 13 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/proving%20size%20at%20least%203/near/132063967):
<p>Thanks to both of you! [I've only just seen these].</p>

#### [ Kevin Buzzard (Aug 14 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/proving%20size%20at%20least%203/near/132075090):
<p>This is one of those "easy in maths, hard in Lean" moments :-/ I am going to need stuff like "card X = 3 iff there exists a,b,c all distinct and every element of X must be a, b or c" [but I've gotta scoot]. I think I can take it from here but this is all a bit ugly. Mathematicians are so good at 3 :-/</p>

#### [ Mario Carneiro (Aug 14 2018 at 04:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/proving%20size%20at%20least%203/near/132084120):
<p>that latter fact is essentially exactly the definition of a fintype instance where the underlying multiset has three elements</p>

#### [ Kevin Buzzard (Aug 14 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/proving%20size%20at%20least%203/near/132131438):
<p>Here's a proof for the cardinal case:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">set_theory</span><span class="bp">.</span><span class="n">cardinal</span>

<span class="kn">lemma</span> <span class="n">three</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">Hthree</span> <span class="o">:</span> <span class="n">cardinal</span><span class="bp">.</span><span class="n">mk</span> <span class="n">α</span> <span class="bp">=</span> <span class="mi">3</span><span class="o">)</span> <span class="o">:</span>
  <span class="bp">∃</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="n">a</span> <span class="bp">≠</span> <span class="n">b</span> <span class="bp">∧</span> <span class="n">b</span> <span class="bp">≠</span> <span class="n">c</span> <span class="bp">∧</span> <span class="n">c</span> <span class="bp">≠</span> <span class="n">a</span> <span class="bp">∧</span> <span class="bp">∀</span> <span class="n">d</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="n">d</span> <span class="bp">=</span> <span class="n">a</span> <span class="bp">∨</span> <span class="n">d</span> <span class="bp">=</span> <span class="n">b</span> <span class="bp">∨</span> <span class="n">d</span> <span class="bp">=</span> <span class="n">c</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">rw</span> <span class="err">←</span><span class="o">(</span><span class="k">show</span> <span class="n">cardinal</span><span class="bp">.</span><span class="n">mk</span> <span class="o">(</span><span class="n">fin</span> <span class="mi">3</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">3</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span><span class="o">)</span> <span class="n">at</span> <span class="n">Hthree</span><span class="o">,</span>
  <span class="n">cases</span> <span class="o">(</span><span class="n">quotient</span><span class="bp">.</span><span class="n">exact</span> <span class="n">Hthree</span><span class="o">)</span> <span class="k">with</span> <span class="n">Hequiv</span><span class="o">,</span>
  <span class="k">let</span> <span class="n">a</span> <span class="o">:=</span> <span class="n">Hequiv</span><span class="bp">.</span><span class="n">symm</span> <span class="mi">0</span><span class="o">,</span><span class="k">let</span> <span class="n">b</span> <span class="o">:=</span> <span class="n">Hequiv</span><span class="bp">.</span><span class="n">symm</span> <span class="mi">1</span><span class="o">,</span><span class="k">let</span> <span class="n">c</span> <span class="o">:=</span> <span class="n">Hequiv</span><span class="bp">.</span><span class="n">symm</span> <span class="mi">2</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">H12</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≠</span> <span class="n">b</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">Hequiv</span><span class="o">]</span><span class="bp">;</span><span class="n">exact</span> <span class="n">dec_trivial</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">H23</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">≠</span> <span class="n">c</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">Hequiv</span><span class="o">]</span><span class="bp">;</span><span class="n">exact</span> <span class="n">dec_trivial</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">H31</span> <span class="o">:</span> <span class="n">c</span> <span class="bp">≠</span> <span class="n">a</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">Hequiv</span><span class="o">]</span><span class="bp">;</span><span class="n">exact</span> <span class="n">dec_trivial</span><span class="o">,</span>
  <span class="n">existsi</span> <span class="n">a</span><span class="o">,</span><span class="n">existsi</span> <span class="n">b</span><span class="o">,</span><span class="n">existsi</span> <span class="n">c</span><span class="o">,</span>
  <span class="n">refine</span> <span class="bp">⟨</span><span class="n">H12</span><span class="o">,</span><span class="n">H23</span><span class="o">,</span><span class="n">H31</span><span class="o">,</span><span class="bp">λ</span> <span class="n">d</span><span class="o">,</span><span class="bp">_⟩</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">H</span> <span class="o">:</span> <span class="o">(</span><span class="n">Hequiv</span> <span class="n">d</span><span class="o">)</span> <span class="k">with</span> <span class="n">n</span> <span class="n">Hn</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">n</span> <span class="k">with</span> <span class="n">e</span> <span class="n">He</span><span class="o">,</span>
    <span class="n">left</span><span class="o">,</span><span class="k">show</span> <span class="n">d</span> <span class="bp">=</span> <span class="n">Hequiv</span><span class="bp">.</span><span class="n">symm</span> <span class="bp">⟨</span><span class="mi">0</span><span class="o">,</span><span class="n">Hn</span><span class="bp">⟩</span><span class="o">,</span><span class="n">rw</span> <span class="err">←</span><span class="n">H</span><span class="o">,</span><span class="n">simp</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">e</span> <span class="k">with</span> <span class="n">e</span> <span class="n">He</span><span class="o">,</span>
    <span class="n">right</span><span class="o">,</span><span class="n">left</span><span class="o">,</span><span class="k">show</span> <span class="n">d</span> <span class="bp">=</span> <span class="n">Hequiv</span><span class="bp">.</span><span class="n">symm</span> <span class="bp">⟨</span><span class="mi">1</span><span class="o">,</span><span class="n">Hn</span><span class="bp">⟩</span><span class="o">,</span><span class="n">rw</span> <span class="err">←</span><span class="n">H</span><span class="o">,</span><span class="n">simp</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">e</span> <span class="k">with</span> <span class="n">e</span> <span class="n">He</span><span class="o">,</span>
    <span class="n">right</span><span class="o">,</span><span class="n">right</span><span class="o">,</span><span class="k">show</span> <span class="n">d</span> <span class="bp">=</span> <span class="n">Hequiv</span><span class="bp">.</span><span class="n">symm</span> <span class="bp">⟨</span><span class="mi">2</span><span class="o">,</span><span class="n">Hn</span><span class="bp">⟩</span><span class="o">,</span><span class="n">rw</span> <span class="err">←</span><span class="n">H</span><span class="o">,</span><span class="n">simp</span><span class="o">,</span>
  <span class="n">exfalso</span><span class="o">,</span><span class="n">apply</span> <span class="n">not_le_of_gt</span> <span class="n">Hn</span><span class="o">,</span><span class="n">exact</span> <span class="n">dec_trivial</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p>Now I need to do <code>four</code> <span class="emoji emoji-1f622" title="cry">:cry:</span> (but that's the last one)</p>

#### [ Mario Carneiro (Aug 14 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/proving%20size%20at%20least%203/near/132131694):
<p>noo... my heart, it hurts</p>

#### [ Mario Carneiro (Aug 14 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/proving%20size%20at%20least%203/near/132131735):
<p><code>n</code> is easier than <code>3</code></p>

#### [ Kevin Buzzard (Aug 14 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/proving%20size%20at%20least%203/near/132131957):
<p>So 4 is easier than 3? :-)</p>

#### [ Mario Carneiro (Aug 14 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/proving%20size%20at%20least%203/near/132131963):
<p>3 is easier than 3</p>

#### [ Kevin Buzzard (Aug 14 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/proving%20size%20at%20least%203/near/132132062):
<p>I did think about doing the general case but at the end of the day I want to extract exactly those things in the conclusion, and I wasn't entirely sure how easy it would be if I had a list of size n or whatever, so I decided to bite the bullet now rather than later.</p>

#### [ Mario Carneiro (Aug 14 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/proving%20size%20at%20least%203/near/132132086):
<p>trust me, it's way easier to conclude from the general statement, even if the final goal is exactly the statement you wrote</p>

#### [ Mario Carneiro (Aug 14 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/proving%20size%20at%20least%203/near/132132147):
<p>hint: if you have a list of length 3, then you can <code>match</code> it against <code>[a, b, c]</code></p>

#### [ Kevin Buzzard (Aug 14 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/proving%20size%20at%20least%203/near/132132148):
<p>I was a bit surprised to see <code>simp</code> leave me with a goal <code>not 0 = 1</code> in the H12 proof.</p>

#### [ Mario Carneiro (Aug 14 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/proving%20size%20at%20least%203/near/132132170):
<p>and <code>d \in [a, b, c]</code> and <code>list.nodup [a, b, c]</code> will simplify to the disjunctions you wrote</p>

#### [ Kevin Buzzard (Aug 14 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/proving%20size%20at%20least%203/near/132132192):
<p>This is the stupid cardinal version, because Richard Thomas complained that I was assuming unnecessary finiteness hypotheses.</p>

#### [ Mario Carneiro (Aug 14 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/proving%20size%20at%20least%203/near/132132241):
<p>there are theorems showing equivalence to the finite versions in <code>cardinal</code></p>

#### [ Kevin Buzzard (Aug 14 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/proving%20size%20at%20least%203/near/132132253):
<p>Oh OK, maybe I'll take it from here. Thanks!</p>

#### [ Kevin Buzzard (Aug 14 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/proving%20size%20at%20least%203/near/132132278):
<p>It's just my lack of experience which made me do the 3 case explicitly. I could see I could try for the n case, but I figured that doing the 3 case directly would be less painful. I guess your instincts immediately told you otherwise.</p>

#### [ Mario Carneiro (Aug 14 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/proving%20size%20at%20least%203/near/132132331):
<p>even 2 is sometimes tricky, but certainly <code>2 &lt; n &lt; 3</code></p>


{% endraw %}
