---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/92357finsetofsubtypefromfilter.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [finset of subtype from filter](https://leanprover-community.github.io/archive/113489newmembers/92357finsetofsubtypefromfilter.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Bryan Gin-ge Chen (Sep 25 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finset%20of%20subtype%20from%20filter/near/134577961):
<p>I don't have a good feeling for how to manipulate subtypes. How do I do this?</p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">α</span><span class="o">]</span>

<span class="n">def</span> <span class="n">foo</span> <span class="o">(</span><span class="n">m</span> <span class="n">X</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">finset</span> <span class="o">(</span><span class="n">finset</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">//</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">X</span><span class="o">})</span> <span class="o">:=</span>
<span class="n">m</span><span class="bp">.</span><span class="n">filter</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">I</span><span class="o">,</span> <span class="n">I</span> <span class="err">⊆</span> <span class="n">X</span><span class="o">)</span> <span class="c1">-- wrong type: finset (finset α)</span>
</pre></div>


<p>I messed around with <code>map</code> and <code>subtype.mk</code> to no avail.</p>

#### [ Mario Carneiro (Sep 25 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finset%20of%20subtype%20from%20filter/near/134578112):
<p>I would suggest using <code>filter_map</code>, but I guess there is no <code>filter_map</code> on multiset</p>

#### [ Mario Carneiro (Sep 25 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finset%20of%20subtype%20from%20filter/near/134578175):
<p>I get the sense you are asking the wrong question. Why do you need this?</p>

#### [ Bryan Gin-ge Chen (Sep 25 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finset%20of%20subtype%20from%20filter/near/134578319):
<p>I'm trying to redefine a restriction function on matroids; <a href="https://github.com/bryangingechen/lean-matroids/blob/master/src/matroid.lean#L787" target="_blank" title="https://github.com/bryangingechen/lean-matroids/blob/master/src/matroid.lean#L787">my original implementation</a> used a bunch of subset hypotheses and I got the impression from what you said earlier that working with fintypes might be easier. So far everything else has indeed gotten simpler.</p>

#### [ Mario Carneiro (Sep 25 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finset%20of%20subtype%20from%20filter/near/134578412):
<p>I think instead of a subset relation, you want an injective function in that definition (or possibly its partial inverse function)</p>

#### [ Mario Carneiro (Sep 25 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finset%20of%20subtype%20from%20filter/near/134578502):
<p>also, this definition doesn't typecheck, not even loosely:</p>
<div class="codehilite"><pre><span></span>def foo (m X : finset α) : finset (finset {x : α // x ∈ X}) :=
m.filter (λ I, I ⊆ X) -- wrong type: finset (finset α)
</pre></div>


<p><code>m</code> here is a <code>finset α</code> so if you filter over it you get elements of <code>α</code>, which can't be subsets of <code>X</code></p>

#### [ Bryan Gin-ge Chen (Sep 25 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finset%20of%20subtype%20from%20filter/near/134578566):
<p>Oh damn, I meant to have <code>m: finset (finset α)</code>. Sorry about that.</p>

#### [ Mario Carneiro (Sep 25 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finset%20of%20subtype%20from%20filter/near/134578668):
<p>This works, but it won't be so easy to work with</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">finset</span><span class="bp">.</span><span class="n">filter_map</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span><span class="o">}</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">β</span><span class="o">]</span>
  <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">option</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">β</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">s</span><span class="bp">.</span><span class="mi">1</span><span class="bp">.</span><span class="n">filter_map</span> <span class="n">f</span><span class="o">)</span><span class="bp">.</span><span class="n">to_finset</span>

<span class="n">def</span> <span class="n">foo</span> <span class="o">(</span><span class="n">m</span> <span class="o">:</span> <span class="n">finset</span> <span class="o">(</span><span class="n">finset</span> <span class="n">α</span><span class="o">))</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">finset</span> <span class="o">(</span><span class="n">finset</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">//</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">X</span><span class="o">})</span> <span class="o">:=</span>
<span class="n">m</span><span class="bp">.</span><span class="n">filter_map</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">I</span><span class="o">,</span> <span class="k">if</span> <span class="n">h</span><span class="o">:</span><span class="bp">_</span> <span class="k">then</span> <span class="n">some</span>
  <span class="bp">⟨</span><span class="n">I</span><span class="bp">.</span><span class="mi">1</span><span class="bp">.</span><span class="n">pmap</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span> <span class="n">h&#39;</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">h&#39;</span><span class="bp">⟩</span><span class="o">)</span> <span class="n">h</span><span class="o">,</span>
   <span class="n">multiset</span><span class="bp">.</span><span class="n">nodup_pmap</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">mk_eq_mk</span><span class="bp">.</span><span class="mi">1</span><span class="o">)</span> <span class="n">I</span><span class="bp">.</span><span class="mi">2</span><span class="bp">⟩</span> <span class="k">else</span> <span class="n">none</span>
</pre></div>

#### [ Bryan Gin-ge Chen (Sep 25 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finset%20of%20subtype%20from%20filter/near/134578983):
<p>I'm not sure what you had in mind for using an injective function instead but the theorems and definitions are naturally phrased in terms of subsets. The whole theory is basically about relations between collections of subsets of some "ground set".</p>
<p>Thanks for the code! I'll see how far I can get with this.</p>

#### [ Mario Carneiro (Sep 25 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finset%20of%20subtype%20from%20filter/near/134578997):
<p>I guess the point of using <code>fintype</code> is to get away from the "ground set"</p>

#### [ Mario Carneiro (Sep 25 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finset%20of%20subtype%20from%20filter/near/134579008):
<p>because type theory supplies you with a "ground set" already, that is, the whole type</p>

#### [ Bryan Gin-ge Chen (Sep 25 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finset%20of%20subtype%20from%20filter/near/134579063):
<p>Right. It looks like it could be awkward whenever we want to change the ground set though.</p>

#### [ Mario Carneiro (Sep 25 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finset%20of%20subtype%20from%20filter/near/134579068):
<p>That's what the injective function is for</p>

#### [ Mario Carneiro (Sep 25 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finset%20of%20subtype%20from%20filter/near/134579080):
<p>In type theory you want to think about subsets as monos in the category theory sense</p>

#### [ Bryan Gin-ge Chen (Sep 26 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finset%20of%20subtype%20from%20filter/near/134704613):
<p>I tried working more with finsets of subtypes and found myself needing a whole bunch of stuff like the following:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">fintype</span>

<span class="kn">open</span> <span class="n">finset</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">α</span><span class="o">]</span>

<span class="n">def</span> <span class="n">finset_embed</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">S</span> <span class="o">:</span> <span class="n">finset</span> <span class="o">{</span><span class="n">x</span> <span class="bp">//</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">X</span><span class="o">})</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span> <span class="o">:=</span>
<span class="n">S</span><span class="bp">.</span><span class="n">map</span> <span class="err">$</span> <span class="n">function</span><span class="bp">.</span><span class="n">embedding</span><span class="bp">.</span><span class="n">subtype</span> <span class="bp">_</span>

<span class="kn">lemma</span> <span class="n">finset_embed_inj</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">}</span> <span class="o">:</span> <span class="n">function</span><span class="bp">.</span><span class="n">injective</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">S</span> <span class="o">:</span> <span class="n">finset</span> <span class="o">{</span><span class="n">x</span> <span class="bp">//</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">X</span><span class="o">}),</span> <span class="n">finset_embed</span> <span class="n">S</span><span class="o">):=</span>
<span class="k">begin</span>
  <span class="n">unfold</span> <span class="n">function</span><span class="bp">.</span><span class="n">injective</span><span class="o">,</span>
  <span class="n">intros</span> <span class="n">S</span> <span class="n">T</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">ext</span><span class="o">]</span> <span class="n">at</span> <span class="n">h</span> <span class="err">⊢</span><span class="o">,</span>
  <span class="n">intros</span> <span class="n">a</span> <span class="n">ha</span><span class="o">,</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">finset_embed</span><span class="o">,</span> <span class="n">function</span><span class="bp">.</span><span class="n">embedding</span><span class="bp">.</span><span class="n">subtype</span><span class="o">]</span> <span class="n">at</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">iff</span><span class="bp">.</span><span class="n">intro</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">H</span><span class="o">,</span> <span class="n">exists</span><span class="bp">.</span><span class="n">elim</span> <span class="o">((</span><span class="n">h</span> <span class="n">a</span><span class="o">)</span><span class="bp">.</span><span class="n">mp</span> <span class="o">(</span><span class="n">exists</span><span class="bp">.</span><span class="n">intro</span> <span class="n">ha</span> <span class="n">H</span><span class="o">))</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">ha_</span><span class="o">,</span> <span class="n">id</span><span class="o">))</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="n">H</span><span class="o">,</span> <span class="n">exists</span><span class="bp">.</span><span class="n">elim</span> <span class="o">((</span><span class="n">h</span> <span class="n">a</span><span class="o">)</span><span class="bp">.</span><span class="n">mpr</span> <span class="o">(</span><span class="n">exists</span><span class="bp">.</span><span class="n">intro</span> <span class="n">ha</span> <span class="n">H</span><span class="o">))</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">ha_</span><span class="o">,</span> <span class="n">id</span><span class="o">))</span>
<span class="kn">end</span>

<span class="kn">instance</span> <span class="n">finset_embed_coe</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">has_coe</span> <span class="o">(</span><span class="n">finset</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">//</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">X</span><span class="o">})</span> <span class="o">(</span><span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">⟨</span><span class="n">finset_embed</span><span class="bp">⟩</span>

<span class="kn">instance</span> <span class="n">finset_finset_embed_coe</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">has_coe</span> <span class="o">(</span><span class="n">finset</span> <span class="o">(</span><span class="n">finset</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">//</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">X</span><span class="o">}))</span> <span class="o">(</span><span class="n">finset</span> <span class="o">(</span><span class="n">finset</span> <span class="n">α</span><span class="o">))</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="o">(</span><span class="n">S</span> <span class="o">:</span> <span class="n">finset</span> <span class="o">(</span><span class="n">finset</span> <span class="o">{</span><span class="n">a</span> <span class="bp">//</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">X</span><span class="o">})),</span> <span class="n">S</span><span class="bp">.</span><span class="n">map</span> <span class="err">$</span> <span class="bp">⟨</span><span class="n">finset_embed</span><span class="o">,</span> <span class="n">finset_embed_inj</span><span class="bp">⟩⟩</span>

<span class="kn">lemma</span> <span class="n">finset_embed_mem</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">S</span> <span class="o">:</span> <span class="n">finset</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">//</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">X</span><span class="o">}}</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">//</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">X</span><span class="o">}}</span> <span class="o">:</span>
  <span class="n">x</span> <span class="err">∈</span> <span class="n">S</span> <span class="bp">↔</span> <span class="n">x</span><span class="bp">.</span><span class="n">val</span> <span class="err">∈</span> <span class="o">(</span><span class="err">↑</span><span class="n">S</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">sorry</span>

<span class="kn">lemma</span> <span class="n">finset_embed_subset</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">finset</span> <span class="o">{</span><span class="n">a</span> <span class="bp">//</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">X</span><span class="o">}}</span> <span class="o">:</span>
  <span class="n">x</span> <span class="err">⊆</span> <span class="n">y</span> <span class="bp">↔</span> <span class="err">↑</span><span class="n">x</span> <span class="err">⊆</span> <span class="o">(</span><span class="err">↑</span><span class="n">y</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">sorry</span>

<span class="kn">lemma</span> <span class="n">finset_embed_univ</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">finset</span> <span class="o">{</span><span class="n">a</span> <span class="bp">//</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">X</span><span class="o">})</span> <span class="o">:</span> <span class="err">↑</span><span class="n">x</span> <span class="err">⊆</span> <span class="n">X</span> <span class="o">:=</span>
<span class="n">sorry</span>

<span class="kn">lemma</span> <span class="n">finset_embed_card</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">finset</span> <span class="o">{</span><span class="n">a</span> <span class="bp">//</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">X</span><span class="o">})</span> <span class="o">:</span> <span class="n">card</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">card</span> <span class="o">(</span><span class="err">↑</span><span class="n">x</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">sorry</span>

<span class="c">/-</span><span class="cm">- def by Mario Carneiro -/</span>
<span class="n">def</span> <span class="n">finset</span><span class="bp">.</span><span class="n">filter_map</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span><span class="o">}</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">β</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">option</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">β</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">s</span><span class="bp">.</span><span class="mi">1</span><span class="bp">.</span><span class="n">filter_map</span> <span class="n">f</span><span class="o">)</span><span class="bp">.</span><span class="n">to_finset</span>

<span class="c">/-</span><span class="cm">- def by Mario Carneiro -/</span>
<span class="n">def</span> <span class="n">restriction</span> <span class="o">(</span><span class="n">m</span> <span class="o">:</span> <span class="n">finset</span> <span class="o">(</span><span class="n">finset</span> <span class="n">α</span><span class="o">))</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">finset</span> <span class="o">(</span><span class="n">finset</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">//</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">X</span><span class="o">})</span> <span class="o">:=</span>
<span class="n">m</span><span class="bp">.</span><span class="n">filter_map</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">I</span><span class="o">,</span> <span class="k">if</span> <span class="n">h</span> <span class="o">:</span> <span class="bp">_</span> <span class="k">then</span> <span class="n">some</span>
  <span class="bp">⟨</span><span class="n">I</span><span class="bp">.</span><span class="mi">1</span><span class="bp">.</span><span class="n">pmap</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span> <span class="n">h&#39;</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">h&#39;</span><span class="bp">⟩</span><span class="o">)</span> <span class="n">h</span><span class="o">,</span>
    <span class="n">multiset</span><span class="bp">.</span><span class="n">nodup_pmap</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">mk_eq_mk</span><span class="bp">.</span><span class="mi">1</span><span class="o">)</span> <span class="n">I</span><span class="bp">.</span><span class="mi">2</span><span class="bp">⟩</span> <span class="k">else</span> <span class="n">none</span>

<span class="kn">lemma</span> <span class="n">mem_restriction</span> <span class="o">{</span><span class="n">m</span> <span class="o">:</span> <span class="n">finset</span> <span class="o">(</span><span class="n">finset</span> <span class="n">α</span><span class="o">)}</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">finset</span> <span class="o">{</span><span class="n">y</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">//</span> <span class="n">y</span> <span class="err">∈</span> <span class="n">X</span><span class="o">}}</span> <span class="o">:</span>
<span class="n">x</span> <span class="err">∈</span> <span class="n">restriction</span> <span class="n">m</span> <span class="n">X</span> <span class="bp">↔</span> <span class="err">↑</span><span class="n">x</span> <span class="err">∈</span> <span class="n">m</span> <span class="bp">∧</span> <span class="err">↑</span><span class="n">x</span> <span class="err">⊆</span> <span class="n">X</span> <span class="o">:=</span>
<span class="n">sorry</span>

<span class="kn">lemma</span> <span class="n">aux</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">e</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">finset</span> <span class="o">{</span><span class="n">a</span> <span class="bp">//</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">X</span><span class="o">}</span> <span class="o">}</span> <span class="o">{</span><span class="n">h</span> <span class="o">:</span> <span class="n">e</span> <span class="err">∈</span> <span class="n">X</span><span class="o">}</span> <span class="o">:</span> <span class="n">insert</span> <span class="n">e</span> <span class="err">↑</span><span class="n">x</span> <span class="bp">=</span> <span class="o">(</span><span class="err">↑</span><span class="o">(</span><span class="n">insert</span> <span class="o">(</span><span class="n">subtype</span><span class="bp">.</span><span class="n">mk</span> <span class="n">e</span> <span class="n">h</span><span class="o">)</span> <span class="n">x</span><span class="o">)</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>I feel like I might be going about this all wrong. Recall that what I'm ultimately trying to do is reprove <a href="https://github.com/bryangingechen/lean-matroids/blob/master/src/matroid.lean#L782" target="_blank" title="https://github.com/bryangingechen/lean-matroids/blob/master/src/matroid.lean#L782">this stuff</a> using fintypes rather than carrying around a bunch of (<code>hX : X ⊆ E</code>) everywhere.</p>
<p>Is there a file in mathlib that takes this approach via monomorphisms to subobjects that I could study, or could someone give me a motivational explanation? In e.g. subgroup.lean it looks like there's a new class <code>is_subgroup</code> but I don't see how that fits.</p>

#### [ Bryan Gin-ge Chen (Sep 27 2018 at 06:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finset%20of%20subtype%20from%20filter/near/134720517):
<p>Update: I was able to prove almost all of the above. Just stuck on <code>mem_restriction</code>, which I realized should just be:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">mem_restriction</span> <span class="o">{</span><span class="n">m</span> <span class="o">:</span> <span class="n">finset</span> <span class="o">(</span><span class="n">finset</span> <span class="n">α</span><span class="o">)}</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">finset</span> <span class="o">{</span><span class="n">y</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">//</span> <span class="n">y</span> <span class="err">∈</span> <span class="n">X</span><span class="o">}}</span> <span class="o">:</span>
<span class="n">x</span> <span class="err">∈</span> <span class="n">restriction</span> <span class="n">m</span> <span class="n">X</span> <span class="bp">↔</span> <span class="err">↑</span><span class="n">x</span> <span class="err">∈</span> <span class="n">m</span> <span class="o">:=</span>
<span class="n">sorry</span>
</pre></div>

#### [ Mario Carneiro (Sep 27 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finset%20of%20subtype%20from%20filter/near/134720961):
<p>I still think you should not be dealing with subtypes so much. I assume your definition looks like this now?</p>
<div class="codehilite"><pre><span></span>structure indep (α : Type*) [decidable_eq α] :=
(indep : finset (finset α))
-- (I1)
(empty_mem_indep : ∅ ∈ indep)
-- (I2)
(indep_of_subset_indep {x y} (hx : x ∈ indep) (hyx : y ⊆ x) : y ∈ indep)
-- (I3)
(indep_exch {x y} (hx : x ∈ indep) (hy : y ∈ indep) (hcard : card x &lt; card y)
    : ∃ e ∈ y \ x, insert e x ∈ indep)
</pre></div>

#### [ Mario Carneiro (Sep 27 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finset%20of%20subtype%20from%20filter/near/134721194):
<p>Also, I notice that this notion of restriction just throws away sets that are not in the subset, rather than taking an intersection like in topology. Is this the same?</p>

#### [ Mario Carneiro (Sep 27 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finset%20of%20subtype%20from%20filter/near/134721323):
<p>Ah, yes it is because of the subset axiom. If <code>A ∈ I</code> is an independent set and <code>E</code> is the subset, then <code>A ∩ E ∈ I</code> as well by the subset axiom, so the set of independent sets that are subsets of <code>E</code> is also the set of intersections of <code>E</code> with independent sets in <code>I</code></p>

#### [ Bryan Gin-ge Chen (Sep 27 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finset%20of%20subtype%20from%20filter/near/134721703):
<p>That's right. What do you suggest instead of subtypes?</p>

#### [ Mario Carneiro (Sep 27 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finset%20of%20subtype%20from%20filter/near/134721936):
<p>filter_map, like before. Here's what I've got so far:</p>
<div class="codehilite"><pre><span></span>@[simp] theorem finset.mem_filter_map {α β} [decidable_eq β] {f : α → option β} {s : finset α}
  {b : β} : b ∈ s.filter_map f ↔ ∃ a ∈ s, b ∈ f a :=
by simp [finset.filter_map]; refl

def {u v} indep.filter_map {α : Type u} {β : Type v} [decidable_eq α] [decidable_eq β] (f : α → option β)
  (m : indep α) : indep β :=
{ indep := m.indep.image (finset.filter_map f),
  empty_mem_indep := finset.mem_image.2 ⟨∅, m.empty_mem_indep, rfl⟩,
  indep_of_subset_indep := λ x y, begin
    rw [mem_image, mem_image],
    rintro ⟨x, hx, rfl⟩ xy,
    refine ⟨x.filter (λ a, ∃ b ∈ f a, b ∈ y),
      m.indep_of_subset_indep hx (filter_subset _), _⟩,
    ext b, simp; split,
    { rintro ⟨a, ⟨ha, b&#39;, hb&#39;, hy⟩, hb⟩,
      rcases option.some_inj.1 (hb.symm.trans hb&#39;),
      exact hy },
    { intro hb,
      rcases finset.mem_filter_map.1 (xy hb) with ⟨a, ha, ab⟩,
      exact ⟨a, ⟨ha, b, ab, hb⟩, ab⟩ }
  end,
  indep_exch := λ x y, begin

  end }
</pre></div>

#### [ Mario Carneiro (Sep 27 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finset%20of%20subtype%20from%20filter/near/134722144):
<p>How important is it that this theory be constructive? Are you trying to construct an algorithm, or are you trying to avoid LEM, or does it not matter?</p>

#### [ Bryan Gin-ge Chen (Sep 27 2018 at 07:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finset%20of%20subtype%20from%20filter/near/134722343):
<p>Here's my version of that, using the lemmas I listed above:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">restriction</span> <span class="o">(</span><span class="n">m</span> <span class="o">:</span> <span class="n">indep</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">indep</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">//</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">X</span><span class="o">}</span> <span class="o">:=</span>
<span class="bp">⟨</span><span class="n">indep_of_restriction</span> <span class="n">m</span> <span class="n">X</span><span class="o">,</span>
<span class="n">mem_restriction</span><span class="bp">.</span><span class="n">mpr</span> <span class="n">m</span><span class="bp">.</span><span class="n">empty_mem_indep</span><span class="o">,</span>
<span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span> <span class="n">hx</span> <span class="n">hyx</span><span class="o">,</span> <span class="k">have</span> <span class="n">hx&#39;</span> <span class="o">:</span> <span class="err">↑</span><span class="n">x</span> <span class="err">∈</span> <span class="n">m</span><span class="bp">.</span><span class="n">indep</span> <span class="o">:=</span> <span class="n">mem_restriction</span><span class="bp">.</span><span class="n">mp</span> <span class="n">hx</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">hyx&#39;</span> <span class="o">:</span> <span class="err">↑</span><span class="n">y</span> <span class="err">⊆</span> <span class="o">(</span><span class="err">↑</span><span class="n">x</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span> <span class="n">finset_embed_subset</span><span class="bp">.</span><span class="n">mp</span> <span class="n">hyx</span><span class="o">,</span>
  <span class="n">mem_restriction</span><span class="bp">.</span><span class="n">mpr</span> <span class="o">(</span><span class="n">m</span><span class="bp">.</span><span class="n">indep_of_subset_indep</span> <span class="n">hx&#39;</span> <span class="n">hyx&#39;</span><span class="o">),</span>
<span class="k">by</span> <span class="o">{</span> <span class="n">intros</span> <span class="n">x</span> <span class="n">y</span> <span class="n">hx</span> <span class="n">hy</span> <span class="n">hcard</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">hx&#39;</span> <span class="o">:</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">mem_restriction</span><span class="bp">.</span><span class="n">mp</span> <span class="n">hx</span><span class="o">,</span> <span class="k">have</span> <span class="n">hy&#39;</span> <span class="o">:</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">mem_restriction</span><span class="bp">.</span><span class="n">mp</span> <span class="n">hy</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">hcard&#39;</span> <span class="o">:</span> <span class="n">card</span> <span class="o">(</span><span class="err">↑</span><span class="n">x</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="bp">&lt;</span> <span class="n">card</span> <span class="err">↑</span><span class="n">y</span> <span class="o">:=</span> <span class="k">calc</span>
    <span class="n">card</span> <span class="o">(</span><span class="err">↑</span><span class="n">x</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="bp">=</span> <span class="n">card</span> <span class="n">x</span> <span class="o">:</span> <span class="o">(</span><span class="n">finset_embed_card</span> <span class="n">x</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span>
    <span class="bp">...</span> <span class="bp">&lt;</span> <span class="n">card</span> <span class="n">y</span> <span class="o">:</span> <span class="n">hcard</span>
    <span class="bp">...</span> <span class="bp">=</span> <span class="n">card</span> <span class="err">↑</span><span class="n">y</span> <span class="o">:</span> <span class="n">finset_embed_card</span> <span class="n">y</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">H</span> <span class="o">:</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">m</span><span class="bp">.</span><span class="n">indep_exch</span> <span class="n">hx&#39;</span> <span class="n">hy&#39;</span> <span class="n">hcard&#39;</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">exists</span><span class="bp">.</span><span class="n">elim</span> <span class="n">H</span> <span class="o">(</span><span class="k">by</span> <span class="o">{</span> <span class="n">intros</span> <span class="n">e</span> <span class="n">he</span><span class="o">,</span> <span class="n">simp</span> <span class="n">at</span> <span class="n">he</span><span class="o">,</span>
    <span class="k">have</span> <span class="n">He</span> <span class="o">:</span> <span class="n">e</span> <span class="err">∈</span> <span class="n">X</span> <span class="o">:=</span> <span class="n">mem_of_subset</span> <span class="o">(</span><span class="n">finset_embed_subset_univ</span> <span class="n">y</span><span class="o">)</span> <span class="n">he</span><span class="bp">.</span><span class="mi">1</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span>
    <span class="k">let</span> <span class="n">e&#39;</span> <span class="o">:=</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">mk</span> <span class="n">e</span> <span class="n">He</span><span class="o">,</span>
    <span class="k">have</span> <span class="n">heyx</span> <span class="o">:</span> <span class="n">e&#39;</span> <span class="err">∈</span> <span class="n">y</span> <span class="err">\</span> <span class="n">x</span> <span class="o">:=</span> <span class="n">mem_sdiff</span><span class="bp">.</span><span class="n">mpr</span> <span class="bp">⟨</span><span class="n">finset_embed_mem</span><span class="bp">.</span><span class="n">mpr</span> <span class="n">he</span><span class="bp">.</span><span class="mi">1</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span>
      <span class="bp">λ</span> <span class="n">H</span><span class="o">,</span> <span class="n">he</span><span class="bp">.</span><span class="mi">1</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="n">finset_embed_mem</span><span class="bp">.</span><span class="n">mp</span> <span class="n">H</span><span class="bp">⟩</span><span class="o">,</span>
    <span class="k">have</span> <span class="n">heinsert</span> <span class="o">:</span> <span class="err">↑</span><span class="o">(</span><span class="n">insert</span> <span class="n">e&#39;</span> <span class="n">x</span><span class="o">)</span> <span class="err">∈</span> <span class="n">m</span><span class="bp">.</span><span class="n">indep</span> <span class="o">:=</span> <span class="k">by</span> <span class="o">{</span>
      <span class="k">have</span> <span class="o">:</span> <span class="o">(</span><span class="err">↑</span><span class="o">(</span><span class="n">insert</span> <span class="n">e&#39;</span> <span class="n">x</span><span class="o">)</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="bp">=</span> <span class="n">insert</span> <span class="n">e</span> <span class="err">↑</span><span class="n">x</span> <span class="o">:=</span>
        <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">ext</span><span class="o">,</span> <span class="n">finset_embed_coe_def</span><span class="o">,</span> <span class="n">finset_embed</span><span class="o">,</span> <span class="n">function</span><span class="bp">.</span><span class="n">embedding</span><span class="bp">.</span><span class="n">subtype</span><span class="o">],</span>
      <span class="n">exact</span> <span class="n">this</span><span class="bp">.</span><span class="n">symm</span> <span class="bp">▸</span> <span class="n">he</span><span class="bp">.</span><span class="mi">2</span>
    <span class="o">},</span>
    <span class="k">have</span> <span class="n">H</span> <span class="o">:</span> <span class="n">insert</span> <span class="n">e&#39;</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">indep_of_restriction</span> <span class="n">m</span> <span class="n">X</span> <span class="o">:=</span>
      <span class="n">mem_restriction</span><span class="bp">.</span><span class="n">mpr</span> <span class="n">heinsert</span><span class="o">,</span>
    <span class="n">exact</span> <span class="n">exists</span><span class="bp">.</span><span class="n">intro</span> <span class="n">e&#39;</span> <span class="bp">⟨</span><span class="n">heyx</span><span class="o">,</span> <span class="n">H</span><span class="bp">⟩</span>
  <span class="o">})}</span><span class="bp">⟩</span>
</pre></div>


<p>I'd like to preserve computability if possible. I think it's really neat that I'm able to compute different descriptions of matroids with #eval right now. Constructive everything might be beyond my capabilities. I'm already using <code>finset.ssubset_iff</code> which uses <code>classical</code>.</p>

#### [ Mario Carneiro (Sep 27 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finset%20of%20subtype%20from%20filter/near/134729214):
<p><span class="user-mention" data-user-id="123965">@Bryan Gin-ge Chen</span> I managed to finish the proof of this theorem. <a href="https://gist.github.com/digama0/edc2a9fe4d468c3921c87650eea5b77a" target="_blank" title="https://gist.github.com/digama0/edc2a9fe4d468c3921c87650eea5b77a">https://gist.github.com/digama0/edc2a9fe4d468c3921c87650eea5b77a</a></p>
<p>It is a lot more complicated than your proof, but it also deals with the case when the filter map is not injective. You can also get subtypes and map out of the filter map construction.</p>

#### [ Mario Carneiro (Sep 27 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finset%20of%20subtype%20from%20filter/near/134729325):
<p>(the stuff about <code>finset.filter_map</code> should go into mathlib)</p>

#### [ Bryan Gin-ge Chen (Sep 27 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finset%20of%20subtype%20from%20filter/near/134747360):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Wow, thanks for all the effort! So, the first thing that matroid restrictions will be used for is to define a notion of rank on subsets (as the cardinality of a maximal independent subset of the subset). Would the best way to apply the filter_map construction be to imitate what you did with <code>foo</code> and subtypes a few days ago in this thread?</p>
<p>Regarding mathlib, should I try to put together a PR, or would it be faster for you just to directly commit the <code>finset.filter_map</code> stuff yourself?</p>

#### [ Mario Carneiro (Sep 27 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finset%20of%20subtype%20from%20filter/near/134750167):
<p>Let me get this straight: given an <code>indep</code> structure <code>m</code>, the rank of a subset <code>S</code> is the largest cardinality of subsets of <code>S</code> in <code>m</code>?</p>

#### [ Mario Carneiro (Sep 27 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finset%20of%20subtype%20from%20filter/near/134752685):
<p>or is it the largest cardinality of an <code>indep</code> that is a restriction of <code>m</code> to <code>S</code>?</p>

#### [ Bryan Gin-ge Chen (Sep 27 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finset%20of%20subtype%20from%20filter/near/134753717):
<p>Given <code>m : indep α</code>, a set <code>B : finset α</code>is a _basis_ for <code>m</code> if it is contained in <code>m.indep</code> and is maximal with regard to inclusion. The definition of the rank of a subset (of the ground set) that I'm trying to formalize is the following. The rank of <code>S : finset α</code>(with respect to <code>m</code>) is defined to be the cardinality of any basis of the restriction of <code>m</code> to <code>S</code> (which should be of type <code>indep {x // x ∈ S}</code>); I've formalized bases in an earlier section and proven e.g. that the cardinality of any two bases is equal.</p>

#### [ Mario Carneiro (Sep 27 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finset%20of%20subtype%20from%20filter/near/134754363):
<p>My suggestion:</p>
<div class="codehilite"><pre><span></span>def indep.supported {α} [decidable_eq α] (m : indep α) (s : finset α) : Prop :=
∀ t ∈ m.indep, t ⊆ s

def indep.restriction {α} [decidable_eq α] (m : indep α) (s : finset α) : indep α :=
m.filter_map (option.guard (∈ s))

theorem indep.restriction_supported {α} [decidable_eq α]
  (m : indep α) (s : finset α) : (m.restriction s).supported s := sorry

def indep.rank {α} [decidable_eq α] (m : indep α) : ℕ := m.indep.sup card

def rank_of {α} [decidable_eq α] (m : indep α) (s : finset α) : ℕ :=
(m.restriction s).rank
</pre></div>

#### [ Mario Carneiro (Sep 27 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finset%20of%20subtype%20from%20filter/near/134754503):
<div class="codehilite"><pre><span></span>def indep.basis {α} [decidable_eq α] (m : indep α) : finset (finset α) :=
m.indep.filter (λ s, ∀ t ∈ m.indep, ¬ s ⊂ t)
</pre></div>

#### [ Mario Carneiro (Sep 27 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finset%20of%20subtype%20from%20filter/near/134754571):
<p>although maybe this last one should be a predicate instead of a finset</p>

#### [ Bryan Gin-ge Chen (Sep 27 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finset%20of%20subtype%20from%20filter/near/134757675):
<p>That's an interesting way to avoid using subtypes. I'm not convinced that we shouldn't change the underlying type of the restriction though. For instance, one prototypical way of getting a matroid is to take a matrix over a field and let the ground set consist of the set of rows and the independent sets be the linearly independent sets of rows. The restriction of such a matroid to a certain subset of its elements should be equal (or maybe "equivalent" is a safer word) to the matroid constructed from the matrix consisting of the corresponding subset of rows; similar remarks hold for most other constructions of matroids that are coming to mind. I think following your approach I would end up with extra elements in the underlying fintype / ground set of the restriction which would violate this principle.</p>
<p>I think <a href="https://github.com/bryangingechen/lean-matroids/blob/fintype/src/matroid.lean#L572" target="_blank" title="https://github.com/bryangingechen/lean-matroids/blob/fintype/src/matroid.lean#L572">the function <code>bases_bases_of_indep</code></a> is the equivalent of <code>indep.basis</code>. (The name was supposed to suggest getting <code>bases.bases</code> from <code>indep</code>).  Though I see it's more efficient to filter on <code>m.indep</code> than on <code>powerset univ</code>.</p>

#### [ Mario Carneiro (Sep 27 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finset%20of%20subtype%20from%20filter/near/134774700):
<p>I'm not saying you should never use subtypes, but they shouldn't be your bread and butter because it entails additional complications that can be avoided by just using the flexibility that you already have inside the type.</p>
<p>As for <code>bases</code>, I see that you have a separate axiomatization of bases rather than just using the collection of independent sets that also satisfy <code>is_basis</code>. Another advantage of not using <code>powerset univ</code> is that I have yet to invoke the assumption that <code>A</code> is finite; all of the above results have only needed <code>decidable_eq A</code>. I imagine you can add that assumption when you need it, but so far it hasn't come up.</p>

#### [ Bryan Gin-ge Chen (Sep 27 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/finset%20of%20subtype%20from%20filter/near/134775211):
<p>OK, point well-taken. I haven't had a chance to work more on this yet, but doubtless I'll have more questions when I try to push on with my way of doing things. Thanks once again for being so helpful!</p>
<blockquote>
<p>I see that you have a separate axiomatization of bases</p>
</blockquote>
<p>Yes, part of the fun of matroids is the existence of so many distinct but equivalent axiomatizations, a phenomenon often referred to as <a href="https://en.wikipedia.org/wiki/Cryptomorphism" target="_blank" title="https://en.wikipedia.org/wiki/Cryptomorphism">cryptomorphism</a>. I've been idly wondering whether something based on the "TFAE" PR might be able to treat this sort of thing, but in practice it's probably not hard just to compose the relevant maps by hand.</p>


{% endraw %}
