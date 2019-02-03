---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/67365constructivezerology.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [constructive zerology](https://leanprover-community.github.io/archive/116395maths/67365constructivezerology.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Jul 17 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129817429):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> I have a question for you. Do you have a proof without <code>decidable</code> or <code>classical</code> of:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">closure_empty_iff</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="o">(</span><span class="n">set</span> <span class="n">α</span><span class="o">)]</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span>
<span class="n">closure</span> <span class="n">s</span> <span class="bp">=</span> <span class="err">∅</span> <span class="bp">↔</span> <span class="n">s</span> <span class="bp">=</span> <span class="err">∅</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">split</span> <span class="bp">;</span> <span class="n">intro</span> <span class="n">h</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">by_contradiction</span> <span class="n">h&#39;</span><span class="o">,</span>
    <span class="n">cases</span> <span class="n">set</span><span class="bp">.</span><span class="n">not_eq_empty_iff_exists</span><span class="bp">.</span><span class="mi">1</span> <span class="n">h&#39;</span> <span class="k">with</span> <span class="bp">_</span> <span class="n">H</span><span class="o">,</span>
    <span class="n">simpa</span> <span class="o">[</span><span class="n">h</span><span class="o">]</span> <span class="kn">using</span> <span class="n">subset_closure</span> <span class="n">H</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">exact</span> <span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">symm</span> <span class="n">h</span><span class="o">)</span> <span class="bp">▸</span> <span class="n">closure_empty</span> <span class="o">},</span>
<span class="kn">end</span>
</pre></div>

#### [ Reid Barton (Jul 17 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129817776):
<p>Use <code>set.eq_empty_iff_forall_not_mem</code> instead I think</p>

#### [ Kenny Lau (Jul 17 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129818028):
<p>for this case, contradiction is intuitionistically valid</p>

#### [ Patrick Massot (Jul 17 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129818071):
<p>Thanks Reid!</p>

#### [ Patrick Massot (Jul 17 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129818092):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">closure_empty_iff</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span>
<span class="n">closure</span> <span class="n">s</span> <span class="bp">=</span> <span class="err">∅</span> <span class="bp">↔</span> <span class="n">s</span> <span class="bp">=</span> <span class="err">∅</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">split</span> <span class="bp">;</span> <span class="n">intro</span> <span class="n">h</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">rw</span> <span class="n">set</span><span class="bp">.</span><span class="n">eq_empty_iff_forall_not_mem</span><span class="o">,</span>
    <span class="n">intros</span> <span class="n">x</span> <span class="n">H</span><span class="o">,</span>
    <span class="n">simpa</span> <span class="o">[</span><span class="n">h</span><span class="o">]</span> <span class="kn">using</span> <span class="n">subset_closure</span> <span class="n">H</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">exact</span> <span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">symm</span> <span class="n">h</span><span class="o">)</span> <span class="bp">▸</span> <span class="n">closure_empty</span> <span class="o">},</span>
<span class="kn">end</span>
</pre></div>

#### [ Patrick Massot (Jul 17 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129818174):
<p>I'm very slowly working towards proving that the Hausdorff completion of a uniform space X is nonempty unless X is empty. This is no fun at all.</p>

#### [ Patrick Massot (Jul 17 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129818681):
<p>I can feel the dreaded spiral where I'm upset something is not obvious to Lean and I'm proving more and more stupid lemmas instead of cooling down and figure out what I exactly need</p>

#### [ Patrick Massot (Jul 17 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129819050):
<p>I need a break. If anyone here is bored and loves zerology, I think I may need proofs of:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">nonempty_iff_univ</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">:</span> <span class="n">nonempty</span> <span class="n">α</span> <span class="bp">↔</span> <span class="o">(</span><span class="n">univ</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="bp">≠</span> <span class="err">∅</span> <span class="o">:=</span>
<span class="n">sorry</span>

<span class="kn">lemma</span> <span class="n">nonempty_of_nonempty_range</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">}</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">¬</span><span class="n">range</span> <span class="n">f</span> <span class="bp">=</span> <span class="err">∅</span><span class="o">)</span> <span class="o">:</span> <span class="n">nonempty</span> <span class="n">α</span> <span class="o">:=</span>
<span class="n">sorry</span>
</pre></div>

#### [ Kevin Buzzard (Jul 17 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129819486):
<p>What am I allowed to use?</p>

#### [ Kevin Buzzard (Jul 17 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129819498):
<p>Excluded middle?</p>

#### [ Kevin Buzzard (Jul 17 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129819501):
<p>Or nothing like this?</p>

#### [ Patrick Massot (Jul 17 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129819612):
<p>Of course I don't care. Again, the goal is to prove the completion is empty only if the original space is empty. And this is only needed to implement Mario's trick allowing to totalize the function "lift to completion" so that any function from a uniform space to a complete Hausdorff space lifts, the lift being garbage is the function is not uniformly continuous.</p>

#### [ Patrick Massot (Jul 17 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129819683):
<p>But at some point we hope to put all this into mathlib, so it would be nicer to avoid unnecessary decidability assumption or classical logic</p>

#### [ Kevin Buzzard (Jul 17 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129819773):
<p><code>nonempty</code> needs data for its constructor, and <code>(univ : set α) ≠ ∅</code> is only a proposition</p>

#### [ Patrick Massot (Jul 17 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129819777):
<p>You can have a look at <a href="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean" target="_blank" title="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean">https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean</a>  to see where I stand</p>

#### [ Patrick Massot (Jul 17 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129819790):
<p>Mario style lifting is defined at <a href="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L124" target="_blank" title="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L124">https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L124</a></p>

#### [ Kevin Buzzard (Jul 17 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129819865):
<p>For the first one you need something like <code>¬ (∀ a : α, false) → ∃ a : α, true</code></p>

#### [ Patrick Massot (Jul 17 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129819870):
<p>Maybe I should use <code>inhabited</code> instead of <code>nonempty</code></p>

#### [ Chris Hughes (Jul 17 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129819883):
<p>Assuming α is nonempty, the assumption <code>decidable_eq (set α)</code> implies decidability of all propositions</p>

#### [ Patrick Massot (Jul 17 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129819888):
<p>Or maybe this is too much trouble, given that I already have a working lift for uniformly continuous functions</p>

#### [ Patrick Massot (Jul 17 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129819935):
<p>I'm upset because none of this has any mathematical content</p>

#### [ Kevin Buzzard (Jul 17 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129820225):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">nonempty_iff_univ</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">:</span> <span class="n">nonempty</span> <span class="n">α</span> <span class="bp">↔</span> <span class="o">(</span><span class="n">univ</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="bp">≠</span> <span class="err">∅</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">split</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">intro</span> <span class="n">H</span><span class="o">,</span>
    <span class="n">cases</span> <span class="n">H</span> <span class="k">with</span> <span class="n">a</span><span class="o">,</span>
    <span class="n">intro</span> <span class="n">H2</span><span class="o">,</span>
    <span class="k">show</span> <span class="o">(</span><span class="err">∅</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="n">a</span><span class="o">,</span>
    <span class="n">rw</span> <span class="err">←</span><span class="n">H2</span><span class="o">,</span>
    <span class="n">trivial</span>
  <span class="o">},</span>
  <span class="n">intro</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">classical</span><span class="bp">.</span><span class="n">by_contradiction</span><span class="o">,</span>
  <span class="n">intro</span> <span class="n">H2</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">funext</span><span class="o">,</span>
  <span class="n">exfalso</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">H2</span><span class="o">,</span>
  <span class="n">exact</span> <span class="bp">⟨</span><span class="n">a</span><span class="bp">⟩</span>
<span class="kn">end</span>
</pre></div>

#### [ Mario Carneiro (Jul 17 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129820641):
<p>I used many of these same theorems in the proof of <code>dense_embedding.extend</code></p>

#### [ Mario Carneiro (Jul 17 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129820666):
<p>for the most part I just brute forced through all of it, using <code>exists_mem_of_ne_empty</code> to get elements out of nonempty sets</p>

#### [ Mario Carneiro (Jul 17 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129820713):
<p>and using <code>mem_closure_iff</code> to get a nonempty set from a closure</p>

#### [ Kevin Buzzard (Jul 17 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129821218):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">nonempty_of_nonempty_range</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">}</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">¬</span><span class="n">range</span> <span class="n">f</span> <span class="bp">=</span> <span class="err">∅</span><span class="o">)</span> <span class="o">:</span> <span class="n">nonempty</span> <span class="n">α</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">apply</span> <span class="n">classical</span><span class="bp">.</span><span class="n">by_contradiction</span><span class="o">,</span>
  <span class="n">intro</span> <span class="n">H2</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">unfold</span> <span class="n">range</span><span class="o">,</span>
  <span class="n">funext</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">propext</span><span class="o">,</span>
  <span class="k">show</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="n">f</span> <span class="n">y</span> <span class="bp">=</span> <span class="n">x</span><span class="o">)</span> <span class="bp">↔</span> <span class="n">false</span><span class="o">,</span>
  <span class="n">split</span><span class="o">,</span><span class="n">swap</span><span class="o">,</span><span class="n">exact</span> <span class="n">false</span><span class="bp">.</span><span class="n">elim</span><span class="o">,</span>
  <span class="n">intro</span> <span class="n">H3</span><span class="o">,</span><span class="n">cases</span> <span class="n">H3</span> <span class="k">with</span> <span class="n">a</span> <span class="n">Ha</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">H2</span><span class="o">,</span>
  <span class="n">exact</span> <span class="bp">⟨</span><span class="n">a</span><span class="bp">⟩</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Jul 17 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129821220):
<p>What's the hurry :-)</p>

#### [ Mario Carneiro (Jul 17 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129821261):
<p>not so cleaned up:</p>
<div class="codehilite"><pre><span></span>lemma nonempty_completion_iff : nonempty (completion α) ↔ nonempty α :=
begin
  split,
  { rintro ⟨c⟩,
    have := eq_univ_iff_forall.1 (to_completion.dense α) c,
    have := mem_closure_iff.1 this _ is_open_univ trivial,
    rcases exists_mem_of_ne_empty this with ⟨_, ⟨_, a, _⟩⟩,
    exact ⟨a⟩ },
  { rintro ⟨a⟩,
    exact ⟨to_completion α a⟩ }
end
</pre></div>

#### [ Patrick Massot (Jul 17 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129821269):
<p>Many thanks to both of you!</p>

#### [ Patrick Massot (Jul 17 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129821281):
<p>In the mean time I saw Kevin's first lemma proof and then found some courage to write:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">nonempty_of_nonempty_range</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">}</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">¬</span><span class="n">range</span> <span class="n">f</span> <span class="bp">=</span> <span class="err">∅</span><span class="o">)</span> <span class="o">:</span> <span class="n">nonempty</span> <span class="n">α</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">cases</span> <span class="n">exists_mem_of_ne_empty</span> <span class="n">H</span> <span class="k">with</span> <span class="n">x</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">mem_range</span><span class="bp">.</span><span class="mi">1</span> <span class="n">h</span> <span class="k">with</span> <span class="n">y</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">exact</span> <span class="bp">⟨</span><span class="n">y</span><span class="bp">⟩</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Jul 17 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129821332):
<p>I don't know any of these lemmas which people are using :-)</p>

#### [ Patrick Massot (Jul 17 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129821337):
<p>I find them using lots of suffering</p>

#### [ Patrick Massot (Jul 17 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129821344):
<p>But now I need to understand Mario's proof</p>

#### [ Kevin Buzzard (Jul 17 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129821346):
<p>I never quite know whether I should somehow attempt to learn exactly what is in mathlib and where it all is</p>

#### [ Kevin Buzzard (Jul 17 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129821369):
<p>I'm doing a lot of work with multisets at the minute for a student, and now I really know my way around multiset.lean</p>

#### [ Kevin Buzzard (Jul 17 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129821424):
<p>but I don't know my way around data.set.basic in that way</p>

#### [ Mario Carneiro (Jul 17 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129821456):
<p>It's worth a perusal (data.set.lattice is the other important one)</p>

#### [ Mario Carneiro (Jul 17 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129821507):
<p>but ideally you should be able to guess beforehand what is in there</p>

#### [ Patrick Massot (Jul 17 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129821513):
<p><code>rintro ⟨c⟩</code> is already a nice trick</p>

#### [ Patrick Massot (Jul 17 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129821533):
<p>But then I'm not sure this isn't too efficient. Don't you think <code>closure_empty_iff</code> should be in mathlib anyway?</p>

#### [ Kevin Buzzard (Jul 17 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129821603):
<p>I hope <code>rintro</code> isn't as slow as <code>rsimp</code></p>

#### [ Patrick Massot (Jul 17 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129821608):
<p>Never noticed any slowness there</p>

#### [ Patrick Massot (Jul 17 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129821678):
<p>If you don't fear <code>rcases</code> then you don't fear <code>rintro</code></p>

#### [ Patrick Massot (Jul 17 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129821701):
<p>and, together, they really make a difference in conciseness, without obfuscation (it's all about unpacking stuff that our mind would unpack unconsciously)</p>

#### [ Patrick Massot (Jul 17 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129822053):
<p>Mario, I tried to use your trick in <a href="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L124" target="_blank" title="https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L124">https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L124</a> but I needed to assume uniform continuity of <code>f</code> is decidable. Now I want to state lemmas assuming uniform continuity, but Lean asks me for an instance of <code>decidable (uniform_continuous f)</code>. Did I do it wrong? What should I do?</p>

#### [ Mario Carneiro (Jul 17 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129822112):
<p>since that proof uses only structural tactics, I would normally compress it into a term proof</p>

#### [ Patrick Massot (Jul 17 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129822131):
<p>which proof?</p>

#### [ Mario Carneiro (Jul 17 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129822190):
<p>the one I gave</p>

#### [ Mario Carneiro (Jul 17 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129822230):
<p>you should have local instance prop_decidable</p>

#### [ Patrick Massot (Jul 17 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129822292):
<p>Oh I will happily add that if you don't tell me this will be an issue when trying to get all this into mathlib</p>

#### [ Patrick Massot (Jul 17 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129822318):
<p>My original version (with unique exists!) had no such assumption, but if course it makes no difference to me</p>

#### [ Mario Carneiro (Jul 17 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129822369):
<p>of course cases on uniform continuity is firmly classical, but we are not working in the constructive fragment here</p>

#### [ Patrick Massot (Jul 17 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129822444):
<p>Nice. I should be able to move on tonight. But right now I'm too hungry, I need diner.</p>

#### [ Patrick Massot (Jul 17 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129822446):
<p>Thanks!</p>

#### [ Mario Carneiro (Jul 17 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129822721):
<p>totalizing functions often requires classical axioms</p>

#### [ Patrick Massot (Jul 17 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129832556):
<p>I'm done totalizing. Now I'm back exactly where I was yesterday except that, in <code>uniform_space.completion_lift f</code>, <code>f</code> is now a function rather than a proof that a function is uniformly continuous. In particular fonctoriality now reads <code>completion_lift (g ∘ f) = (completion_lift g) ∘ completion_lift f</code>, as it should</p>

#### [ Patrick Massot (Jul 17 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129832572):
<p>All this for the cheap price of a few hours and a <code>local attribute [instance] classical.prop_decidable</code></p>

#### [ Patrick Massot (Jul 17 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129832630):
<p>And I can see wisdom is coming to Kenny. He didn't write anything about that last classical detail.</p>


{% endraw %}
