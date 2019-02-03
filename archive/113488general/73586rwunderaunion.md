---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/73586rwunderaunion.html
---

## Stream: [general](index.html)
### Topic: [rw under a union](73586rwunderaunion.html)

---


{% raw %}
#### [ Kevin Buzzard (May 14 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126553772):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">set</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span>  <span class="o">(</span><span class="n">F</span> <span class="n">G</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span>
  <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">),</span> <span class="n">F</span> <span class="n">i</span> <span class="bp">=</span> <span class="n">G</span> <span class="n">i</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="err">⋃</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">),</span> <span class="n">F</span> <span class="n">i</span><span class="o">)</span>  <span class="bp">=</span> <span class="err">⋃</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">),</span> <span class="n">G</span> <span class="n">i</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">refine</span> <span class="n">set</span><span class="bp">.</span><span class="n">subset</span><span class="bp">.</span><span class="n">antisymm</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">apply</span> <span class="n">set</span><span class="bp">.</span><span class="n">Union_subset_Union</span><span class="o">,</span>
    <span class="n">intro</span> <span class="n">i</span><span class="o">,</span><span class="n">rw</span> <span class="o">(</span><span class="n">H</span> <span class="n">i</span><span class="o">),</span>
  <span class="o">},</span>
  <span class="o">{</span> <span class="n">apply</span> <span class="n">set</span><span class="bp">.</span><span class="n">Union_subset_Union</span><span class="o">,</span>
    <span class="n">intro</span> <span class="n">i</span><span class="o">,</span><span class="n">rw</span> <span class="o">(</span><span class="n">H</span> <span class="n">i</span><span class="o">),</span>
  <span class="o">},</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (May 14 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126553840):
<p>Is there a more sensible method to prove that if <code>F i = G i</code> for all <code>i</code> then the union of the <code>F i</code> equals the union of the <code>G i</code>? I couldn't figure out how to rewrite within the union.</p>

#### [ Kevin Buzzard (May 14 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126553854):
<p>Sorry, the Union.</p>

#### [ Chris Hughes (May 14 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126553895):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span>  <span class="o">(</span><span class="n">F</span> <span class="n">G</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span>
  <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">),</span> <span class="n">F</span> <span class="n">i</span> <span class="bp">=</span> <span class="n">G</span> <span class="n">i</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="err">⋃</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">),</span> <span class="n">F</span> <span class="n">i</span><span class="o">)</span>  <span class="bp">=</span> <span class="err">⋃</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">),</span> <span class="n">G</span> <span class="n">i</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">rw</span> <span class="n">funext</span> <span class="n">H</span>
</pre></div>

#### [ Kevin Buzzard (May 14 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126553981):
<p>ha ha that's clever :-)</p>

#### [ Patrick Massot (May 14 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554007):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span>  <span class="o">(</span><span class="n">F</span> <span class="n">G</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span>
  <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">),</span> <span class="n">F</span> <span class="n">i</span> <span class="bp">=</span> <span class="n">G</span> <span class="n">i</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="err">⋃</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">),</span> <span class="n">F</span> <span class="n">i</span><span class="o">)</span>  <span class="bp">=</span> <span class="err">⋃</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">),</span> <span class="n">G</span> <span class="n">i</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">finish</span>
</pre></div>

#### [ Patrick Massot (May 14 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554017):
<p>Use automation Luke</p>

#### [ Kevin Buzzard (May 14 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554071):
<p>What does <code>finish</code> do?</p>

#### [ Patrick Massot (May 14 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554073):
<p>It finishes the proof</p>

#### [ Kevin Buzzard (May 14 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554074):
<p>every time??</p>

#### [ Patrick Massot (May 14 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554079):
<p>Yes, nobody told you?</p>

#### [ Patrick Massot (May 14 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554083):
<p>You could also use <code>congr</code> here</p>

#### [ Kevin Buzzard (May 14 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554095):
<p>I've seen <code>congr</code> do rewrites I couldn't do before, I should have tried this</p>

#### [ Kevin Buzzard (May 14 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554101):
<p>I tried <code>conv</code> but I couldn't get that to work either</p>

#### [ Kevin Buzzard (May 14 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554103):
<p>and it was the last line of a 250 line proof :-)</p>

#### [ Kevin Buzzard (May 14 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554104):
<p>so I cheated and asked here.</p>

#### [ Kevin Buzzard (May 14 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554107):
<p>I should be marking Chris' exam script!</p>

#### [ Kevin Buzzard (May 14 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554147):
<p>But I am sick of affine schemes not being schemes</p>

#### [ Patrick Massot (May 14 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554151):
<p>Recently I got to this situation where the goal is <code>a = a</code> (but not if <code>pp.all</code>) and <code>congr</code> alone finished the proof</p>

#### [ Patrick Massot (May 14 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554164):
<p>You should have made that formalization the exam</p>

#### [ Kevin Buzzard (May 14 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554192):
<p>next year</p>

#### [ Kevin Buzzard (May 14 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554243):
<p>What would I do without this chat. Things would go so much more slowly.</p>

#### [ Patrick Massot (May 14 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554551):
<p>I'm always fighting the temptation to post every lemma I need here</p>

#### [ Patrick Massot (May 14 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554597):
<p>I hope to reduce my dependence a bit</p>

#### [ Patrick Massot (May 14 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554609):
<p>But I'm still interested in learning better ways. Here are two lemmas I proved tonight. Usual questions: are there already there? What is the proof from the book?</p>

#### [ Patrick Massot (May 14 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554618):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">foldr_ext</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">l</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="n">f&#39;</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">β</span><span class="o">)</span>
  <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">l</span><span class="o">,</span> <span class="bp">∀</span> <span class="n">b</span> <span class="o">:</span> <span class="n">β</span><span class="o">,</span> <span class="n">f</span> <span class="n">a</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">f&#39;</span> <span class="n">a</span> <span class="n">b</span><span class="o">)</span> <span class="o">:</span> <span class="n">foldr</span> <span class="n">f</span> <span class="n">s</span> <span class="n">l</span> <span class="bp">=</span> <span class="n">foldr</span> <span class="n">f&#39;</span> <span class="n">s</span> <span class="n">l</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">induction</span> <span class="n">l</span> <span class="k">with</span> <span class="n">h</span> <span class="n">t</span> <span class="n">IH</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">simp</span> <span class="o">},</span>
  <span class="o">{</span> <span class="k">have</span> <span class="n">H&#39;</span> <span class="o">:=</span> <span class="n">H</span> <span class="n">h</span> <span class="o">(</span><span class="k">by</span> <span class="n">simp</span><span class="o">),</span>
    <span class="n">suffices</span> <span class="o">:</span> <span class="n">foldr</span> <span class="n">f</span> <span class="n">s</span> <span class="n">t</span> <span class="bp">=</span> <span class="n">foldr</span> <span class="n">f&#39;</span> <span class="n">s</span> <span class="n">t</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">H&#39;</span><span class="o">,</span> <span class="n">this</span><span class="o">],</span>
    <span class="n">apply</span> <span class="n">IH</span><span class="o">,</span>
    <span class="n">intros</span> <span class="n">a</span> <span class="n">a_t</span><span class="o">,</span>
    <span class="n">exact</span> <span class="n">H</span> <span class="n">a</span> <span class="o">(</span><span class="k">by</span> <span class="n">simp</span><span class="o">[</span><span class="n">a_t</span><span class="o">])</span> <span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Patrick Massot (May 14 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554683):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">filter_ext</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">r</span><span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">P</span> <span class="n">P&#39;</span><span class="o">)</span> <span class="o">[</span><span class="n">decidable_pred</span> <span class="n">P</span><span class="o">]</span> <span class="o">[</span><span class="n">decidable_pred</span> <span class="n">P&#39;</span><span class="o">]</span>
  <span class="o">(</span><span class="n">HP</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">i</span> <span class="err">∈</span> <span class="n">r</span><span class="o">,</span> <span class="n">P</span> <span class="n">i</span> <span class="bp">=</span> <span class="n">P&#39;</span> <span class="n">i</span><span class="o">)</span> <span class="o">:</span> <span class="n">filter</span> <span class="n">P</span> <span class="n">r</span> <span class="bp">=</span> <span class="n">filter</span> <span class="n">P&#39;</span> <span class="n">r</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">induction</span> <span class="n">r</span> <span class="k">with</span> <span class="n">h</span> <span class="n">t</span> <span class="n">IH</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">simp</span> <span class="o">},</span>
  <span class="o">{</span> <span class="k">have</span> <span class="n">HPh</span> <span class="o">:</span> <span class="n">P</span> <span class="n">h</span> <span class="bp">=</span> <span class="n">P&#39;</span> <span class="n">h</span> <span class="o">:=</span> <span class="n">HP</span> <span class="n">h</span> <span class="o">(</span><span class="k">by</span> <span class="n">simp</span><span class="o">),</span>
    <span class="k">have</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">i</span> <span class="err">∈</span> <span class="n">t</span> <span class="bp">→</span> <span class="n">P</span> <span class="n">i</span> <span class="bp">=</span> <span class="n">P&#39;</span> <span class="n">i</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">intros</span> <span class="n">i</span> <span class="n">i_t</span><span class="o">,</span>
      <span class="n">exact</span> <span class="o">(</span><span class="n">HP</span> <span class="n">i</span> <span class="err">$</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">i_t</span><span class="o">])</span> <span class="o">},</span>
    <span class="n">by_cases</span> <span class="n">H</span> <span class="o">:</span> <span class="n">P</span> <span class="n">h</span><span class="o">,</span>
    <span class="o">{</span> <span class="k">have</span> <span class="n">H&#39;</span> <span class="o">:</span> <span class="n">P&#39;</span> <span class="n">h</span> <span class="o">:=</span> <span class="n">HPh</span> <span class="bp">▸</span> <span class="n">H</span><span class="o">,</span>
      <span class="n">simp</span> <span class="o">[</span><span class="n">H</span><span class="o">,</span> <span class="n">H&#39;</span><span class="o">,</span> <span class="n">IH</span> <span class="n">this</span><span class="o">]</span> <span class="o">},</span>
    <span class="o">{</span> <span class="k">have</span> <span class="n">H&#39;</span> <span class="o">:</span> <span class="bp">¬</span> <span class="n">P&#39;</span> <span class="n">h</span> <span class="o">:=</span> <span class="n">HPh</span> <span class="bp">▸</span> <span class="n">H</span><span class="o">,</span>
      <span class="n">simp</span> <span class="o">[</span><span class="n">H</span><span class="o">,</span> <span class="n">H&#39;</span><span class="o">,</span> <span class="n">IH</span> <span class="n">this</span><span class="o">]</span> <span class="o">}</span> <span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Patrick Massot (May 14 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554698):
<p>I haven't tried to obfuscate the proofs</p>

#### [ Kevin Buzzard (May 14 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554707):
<p>ha ha can you do the first one with Chris' trick?</p>

#### [ Patrick Massot (May 14 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554754):
<p>But I'm sure two lines are enough</p>

#### [ Patrick Massot (May 14 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554775):
<p>I don't think so, you must not forget we have informations only on elements of the list</p>

#### [ Kevin Buzzard (May 14 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554779):
<p>oh yes</p>

#### [ Patrick Massot (May 14 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554780):
<p>This condition seems a bit too specific</p>

#### [ Patrick Massot (May 14 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554786):
<p>For instance, start with <code>congr</code> and you loose</p>

#### [ Kevin Buzzard (May 14 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554788):
<p>Do I need an import for these? I just this minute upgraded mathlib in my project and I'm re-building it</p>

#### [ Kevin Buzzard (May 14 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554829):
<p>so maybe I just have to wait</p>

#### [ Kevin Buzzard (May 14 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554831):
<p>but I have complaints about foldr currently</p>

#### [ Patrick Massot (May 14 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554836):
<p><code>import data.list.basic</code></p>

#### [ Patrick Massot (May 14 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126554837):
<p>sorry</p>

#### [ Kevin Buzzard (May 14 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126555316):
<p><code>list.foldr_hom</code> is too strong</p>

#### [ Patrick Massot (May 14 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126555384):
<p>Too strong?</p>

#### [ Kevin Buzzard (May 14 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126555393):
<p>For your application</p>

#### [ Kevin Buzzard (May 14 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126555398):
<p>like Chris' idea</p>

#### [ Kevin Buzzard (May 14 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126555403):
<p>Same problem</p>

#### [ Patrick Massot (May 14 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126555410):
<p>right</p>

#### [ Chris Hughes (May 14 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126555898):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">foldr_ext</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">l</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="n">f&#39;</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">β</span><span class="o">)</span>
  <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">l</span><span class="o">,</span> <span class="bp">∀</span> <span class="n">b</span> <span class="o">:</span> <span class="n">β</span><span class="o">,</span> <span class="n">f</span> <span class="n">a</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">f&#39;</span> <span class="n">a</span> <span class="n">b</span><span class="o">)</span> <span class="o">:</span> <span class="n">foldr</span> <span class="n">f</span> <span class="n">s</span> <span class="n">l</span> <span class="bp">=</span> <span class="n">foldr</span> <span class="n">f&#39;</span> <span class="n">s</span> <span class="n">l</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">induction</span> <span class="n">l</span><span class="bp">;</span> <span class="n">simp</span> <span class="bp">*</span> <span class="o">{</span><span class="n">contextual</span> <span class="o">:=</span> <span class="n">tt</span><span class="o">}</span>
</pre></div>

#### [ Patrick Massot (May 14 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126555909):
<p><span class="emoji emoji-1f62e" title="open mouth">:open_mouth:</span></p>

#### [ Kenny Lau (May 14 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126555923):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> can you derive normal and curvature for r=xi+f(x)j?</p>

#### [ Patrick Massot (May 14 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126555943):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> is this the mechanics exam running joke again?</p>

#### [ Kenny Lau (May 14 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126555948):
<p>is it a joke when the exam is tomorrow?</p>

#### [ Patrick Massot (May 14 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556102):
<p>Thank you Chris for not revising mechanics</p>

#### [ Patrick Massot (May 14 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556105):
<p>I disapprove of course</p>

#### [ Patrick Massot (May 14 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556108):
<p>But I still take your proof</p>

#### [ Chris Hughes (May 14 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556116):
<p>I can as of today. <span class="user-mention" data-user-id="110064">@Kenny Lau</span></p>

#### [ Kenny Lau (May 14 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556133):
<p>ok you win</p>

#### [ Chris Hughes (May 14 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556183):
<p>curvature is dn / ds, where s is arc length I think.</p>

#### [ Chris Hughes (May 14 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556192):
<p>and n is normal</p>

#### [ Patrick Massot (May 14 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556199):
<p>He can golf <em>and</em> compute curvature. What a man!</p>

#### [ Kevin Buzzard (May 14 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556397):
<p>So what is going on with Chris' proof? I feel like I can learn something important here</p>

#### [ Kevin Buzzard (May 14 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556399):
<p>Induction -- sure. Simp does the base case</p>

#### [ Kevin Buzzard (May 14 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556403):
<p>simp doesn't do the inductive step.</p>

#### [ Kevin Buzzard (May 14 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556405):
<p>by itself.</p>

#### [ Kenny Lau (May 14 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556407):
<p>it's a semicolon</p>

#### [ Kenny Lau (May 14 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556450):
<p><code>simp</code> is simultaneously applied to both goals</p>

#### [ Kenny Lau (May 14 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556451):
<p>the base case and the inductive step</p>

#### [ Patrick Massot (May 14 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556453):
<p><code>contextual</code> seems to do the magic trick</p>

#### [ Kenny Lau (May 14 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556457):
<p>what does <code>contextual</code> do?</p>

#### [ Patrick Massot (May 14 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556461):
<p>uses context</p>

#### [ Kenny Lau (May 14 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556465):
<p>isn't that <code>simp *</code>?</p>

#### [ Patrick Massot (May 14 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556496):
<p>I hate natural number arithmetic, so I'm cheating for this one. Who could prove me <code>b &lt; a</code> implies <code>b + 1 - a = 0</code>?</p>

#### [ Kevin Buzzard (May 14 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556576):
<p>maybe b &lt; a -&gt; (b + 1) &lt;= a</p>

#### [ Kenny Lau (May 14 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556581):
<p>they are equivalent</p>

#### [ Kenny Lau (May 14 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556584):
<p>definitionally</p>

#### [ Patrick Massot (May 14 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556587):
<p>That could be a step yes</p>

#### [ Kevin Buzzard (May 14 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556590):
<p>oh they are defeq right? ;-)</p>

#### [ Kenny Lau (May 14 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556596):
<p>so something like <code>sub_le_zero_of_le</code>?</p>

#### [ Kenny Lau (May 14 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556601):
<p>(deleted)</p>

#### [ Kenny Lau (May 14 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556649):
<p>oh wait nothing</p>

#### [ Kenny Lau (May 14 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556657):
<p>maybe you want <code>nat.eq_zero_of_le_zero</code> if it exists</p>

#### [ Kevin Buzzard (May 14 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556661):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">list</span><span class="bp">.</span><span class="n">basic</span>
<span class="kn">open</span> <span class="n">list</span>
<span class="kn">lemma</span> <span class="n">foldr_ext</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">l</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="n">f&#39;</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">β</span><span class="o">)</span>
  <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">l</span><span class="o">,</span> <span class="bp">∀</span> <span class="n">b</span> <span class="o">:</span> <span class="n">β</span><span class="o">,</span> <span class="n">f</span> <span class="n">a</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">f&#39;</span> <span class="n">a</span> <span class="n">b</span><span class="o">)</span> <span class="o">:</span> <span class="n">foldr</span> <span class="n">f</span> <span class="n">s</span> <span class="n">l</span> <span class="bp">=</span> <span class="n">foldr</span> <span class="n">f&#39;</span> <span class="n">s</span> <span class="n">l</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">induction</span> <span class="n">l</span> <span class="k">with</span> <span class="n">h</span> <span class="n">t</span> <span class="n">IH</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">simp</span> <span class="o">},</span>
  <span class="n">simp</span> <span class="bp">*</span> <span class="o">{</span><span class="n">contextual</span> <span class="o">:=</span> <span class="n">tt</span><span class="o">},</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (May 14 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556663):
<p>The semicolon isn't important</p>

#### [ Kenny Lau (May 14 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556664):
<p>it is, because it allows you to apply <code>simp</code> to both goals</p>

#### [ Kevin Buzzard (May 14 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556669):
<p>but the contextual is</p>

#### [ Kenny Lau (May 14 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556671):
<p>without the semicolon you need to write it twice</p>

#### [ Kevin Buzzard (May 14 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556674):
<p>sure</p>

#### [ Kevin Buzzard (May 14 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556684):
<p>Oh I see what you're saying -- what I am saying is trivial.</p>

#### [ Kevin Buzzard (May 14 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556688):
<p>I'm just unravelling the semicolon</p>

#### [ Kevin Buzzard (May 14 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556692):
<p>the contextual isn't important for the base case but for the inductive step we have an inductive hypothesis which needs to be used</p>

#### [ Kenny Lau (May 14 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556700):
<p>does <code>simp [*]</code> work?</p>

#### [ Gabriel Ebner (May 14 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556778):
<p>Contextual does not refer to context as in "induction hypothesis" but to the left-hand side of implications: in <code>a = b -&gt; P a</code>, contextual allows simp to use the equation <code>a=b</code> to simplify <code>P a</code>.</p>

#### [ Kenny Lau (May 14 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556780):
<p>oh</p>

#### [ Kevin Buzzard (May 14 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556790):
<p><code>nat.sub_eq_zero_iff_le</code></p>

#### [ Kevin Buzzard (May 14 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556860):
<p><code>example (a b : ℕ) : b &lt; a → b + 1 - a = 0 := nat.sub_eq_zero_of_le</code></p>

#### [ Kenny Lau (May 14 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556865):
<p>aha</p>

#### [ Kevin Buzzard (May 14 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556867):
<p>using the trick that b &lt; a is by definition b+1 &lt;= a</p>

#### [ Kevin Buzzard (May 14 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556869):
<p>as Kenny pointed out</p>

#### [ Kevin Buzzard (May 14 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556916):
<p>(see <code>#print nat.lt</code>)</p>

#### [ Patrick Massot (May 14 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556928):
<p>Thank you very much</p>

#### [ Kevin Buzzard (May 14 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556989):
<p>This <code>contextual</code> thing is not documented in my simp docs -- I looked through the source or the docs (I don't remember, maybe the source), saw it was there and mentioned it but basically also said I didn't know what it di.</p>

#### [ Kevin Buzzard (May 14 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126556990):
<p>d</p>

#### [ Kevin Buzzard (May 14 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126557009):
<p>I don't quite understand Gabriel's explanation -- is <code>a = b -&gt; P a</code> supposed to be a hypothesis or a goal?</p>

#### [ Kenny Lau (May 14 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126557013):
<p>goal</p>

#### [ Kenny Lau (May 14 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126557022):
<p>hmm, but the goal is not an implication</p>

#### [ Kevin Buzzard (May 14 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126557030):
<blockquote>
<p>does <code>simp [*]</code> work?</p>
</blockquote>
<p>no</p>

#### [ Kevin Buzzard (May 14 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126557125):
<p>right -- the implications are in the hypotheses</p>

#### [ Kevin Buzzard (May 14 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126557127):
<p>Maybe it's just magic</p>

#### [ Kevin Buzzard (May 14 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126557131):
<p>"Lean does not do magic" -- K. Lau, a couple of months ago</p>

#### [ Kevin Buzzard (May 14 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126557175):
<p>The comment inspired me to start really thinking about how some of the techniques I had picked up actually worked</p>

#### [ Mario Carneiro (May 14 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126557393):
<div class="codehilite"><pre><span></span>lemma filter_congr {p q : α → Prop} [decidable_pred p] [decidable_pred q]
  : ∀ {l : list α}, (∀ x ∈ l, p x ↔ q x) → filter p l = filter q l
| [] _     := rfl
| (a::l) h := by simp at h; by_cases pa : p a;
  [simp [pa, h.1.1 pa, filter_congr h.2],
   simp [pa, mt h.1.2 pa, filter_congr h.2]]
</pre></div>


<p>Regarding naming: A theorem of the form <code>a = b -&gt; F a = F b</code> is a "congruence" theorem, named with <code>congr</code> at the end. An "extensionality" theorem has the form <code>F a = F b -&gt; a = b</code> where <code>F</code> is some appropriate (collection of) projection-like operations</p>

#### [ Mario Carneiro (May 14 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126557415):
<p><code>map_congr</code> exists in <code>list.basic</code> but not all list theorems have congr theorems stated for them</p>

#### [ Patrick Massot (May 14 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126557583):
<p>Thanks!</p>

#### [ Patrick Massot (May 14 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126557592):
<p>Is there any difference between my <code>p x = q x</code> and your <code>p x ↔ q x</code> here?</p>

#### [ Mario Carneiro (May 14 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126557609):
<p>No, given <code>propext</code>, but mathlib convention is to use <code>iff</code> instead of <code>eq</code> for equivalent propositions</p>

#### [ Mario Carneiro (May 14 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126557632):
<p>Otherwise you have to face weird theorems like <code>(a = b) = c = b</code></p>

#### [ Chris Hughes (May 14 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126557712):
<p>It more or less does <code>intros; simp *</code> I think</p>

#### [ Chris Hughes (May 14 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126557713):
<p>But I just realise that can't be what it does, because my example didn't have anything to intro.</p>

#### [ Chris Hughes (May 14 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126557714):
<p>and <code>simp *</code> doesn't work</p>

#### [ Patrick Massot (May 14 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126558301):
<p>Going from = to iff broke a magic <code>finish</code> success</p>

#### [ Patrick Massot (May 14 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126558311):
<p>Probably by breaking a magic <code>cc</code> under the hood</p>

#### [ Patrick Massot (May 14 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126558380):
<p>This natural number substraction is really a nightmare. Now I want <code>b + k + 1 - (a + k) = b + 1 - a</code>. It's almost the same I had a couple of days ago. But I'm stuck again...</p>

#### [ Patrick Massot (May 14 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126558463):
<p>It seems like I really need <code>omega</code> in the end</p>

#### [ Patrick Massot (May 14 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126558972):
<p>Is there any hope to use Coq to tell me a proof Lean could understand?</p>

#### [ Andrew Ashworth (May 14 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126559159):
<p>No, in general the names of the lemmas used in Coq would be different</p>

#### [ Patrick Massot (May 14 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126559200):
<p>But can you get the sequence of Coq lemmas used by omega?</p>

#### [ Andrew Ashworth (May 14 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126559219):
<p>I do not have a Coq installation in front of me to look at the output of omega, so I don't know</p>

#### [ Andrew Ashworth (May 14 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126559407):
<p>What I did when i had a lot of similar problems was write down a cheat sheet of relevant cancellation lemmas in my notebook... looking them all up was my biggest hurdle</p>

#### [ Patrick Massot (May 14 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126559611):
<p>Now I need <code>H : a ≤ b ⊢ 2 * a + (b + 1 - a) - i - 1 = a - i + b</code>. I give up for today</p>

#### [ Patrick Massot (May 14 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126559664):
<p>I have four proofs stuck because of such stupid goals</p>

#### [ Kenny Lau (May 14 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126559670):
<p>I understand your feeling</p>

#### [ Kevin Buzzard (May 15 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126563181):
<blockquote>
<p>Going from = to iff broke a magic <code>finish</code> success</p>
</blockquote>
<p>You can just deduce your old version from Mario's version of course...</p>

#### [ Kevin Buzzard (May 15 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126563201):
<blockquote>
<p>This natural number substraction is really a nightmare. Now I want <code>b + k + 1 - (a + k) = b + 1 - a</code>. It's almost the same I had a couple of days ago. But I'm stuck again...</p>
</blockquote>
<p>I really like doing these. Patrick -- just type nat.sub and then ctrl-space escape ctrl-space to see what Lean has, you can just browse through stuff.</p>

#### [ Kevin Buzzard (May 15 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126563696):
<p>Actually I don't understand how ctrl-space works at all. I just managed to type <code>nat.sub</code> and get it to display <code>nat.add_sub_add_left</code> (which is useful for you) and then after esc ctrl-space I don't see it any more</p>

#### [ Kevin Buzzard (May 15 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126563797):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">k</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">+</span> <span class="n">k</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">-</span> <span class="o">(</span><span class="n">a</span> <span class="bp">+</span> <span class="n">k</span><span class="o">)</span> <span class="bp">=</span> <span class="n">b</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">-</span> <span class="n">a</span> <span class="o">:=</span> <span class="k">calc</span>
<span class="n">b</span> <span class="bp">+</span> <span class="n">k</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">-</span> <span class="o">(</span><span class="n">a</span> <span class="bp">+</span> <span class="n">k</span><span class="o">)</span> <span class="bp">=</span> <span class="n">k</span> <span class="bp">+</span> <span class="o">(</span><span class="n">b</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">-</span> <span class="o">(</span><span class="n">k</span> <span class="bp">+</span> <span class="n">a</span><span class="o">)</span> <span class="o">:</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">add_assoc</span><span class="o">,</span><span class="n">add_comm</span><span class="o">]</span>
<span class="bp">...</span> <span class="bp">=</span> <span class="n">b</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">-</span> <span class="n">a</span> <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">nat</span><span class="bp">.</span><span class="n">add_sub_add_left</span>
</pre></div>

#### [ Kevin Buzzard (May 15 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126563842):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">k</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">+</span> <span class="n">k</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">-</span> <span class="o">(</span><span class="n">a</span> <span class="bp">+</span> <span class="n">k</span><span class="o">)</span> <span class="bp">=</span> <span class="n">b</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">-</span> <span class="n">a</span> <span class="o">:=</span> <span class="k">calc</span>
<span class="n">b</span> <span class="bp">+</span> <span class="n">k</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">-</span> <span class="o">(</span><span class="n">a</span> <span class="bp">+</span> <span class="n">k</span><span class="o">)</span> <span class="bp">=</span> <span class="n">b</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">+</span> <span class="n">k</span> <span class="bp">-</span> <span class="o">(</span><span class="n">a</span> <span class="bp">+</span> <span class="n">k</span><span class="o">)</span> <span class="o">:</span> <span class="k">by</span> <span class="n">simp</span>
<span class="bp">...</span> <span class="bp">=</span> <span class="n">b</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">-</span> <span class="n">a</span> <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">nat</span><span class="bp">.</span><span class="n">add_sub_add_right</span>
</pre></div>

#### [ Kevin Buzzard (May 15 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126564406):
<blockquote>
<p>Now I need <code>H : a ≤ b ⊢ 2 * a + (b + 1 - a) - i - 1 = a - i + b</code>. I give up for today</p>
</blockquote>
<p>If <code>i &gt; a</code> but <code>i &lt;= a + b</code> then this one won't be true, because <code>a - i + b</code> is <code>(a - i) + b</code></p>

#### [ Kevin Buzzard (May 15 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126564613):
<p>Here's some true version:</p>

#### [ Kevin Buzzard (May 15 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126564616):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">i</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">b</span><span class="o">)</span> <span class="o">:</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">a</span> <span class="bp">+</span> <span class="o">(</span><span class="n">b</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">-</span> <span class="n">a</span><span class="o">)</span> <span class="bp">-</span> <span class="n">i</span> <span class="bp">-</span> <span class="mi">1</span> <span class="bp">=</span> <span class="n">a</span> <span class="bp">+</span> <span class="n">b</span> <span class="bp">-</span> <span class="n">i</span> <span class="o">:=</span>
<span class="k">calc</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">a</span> <span class="bp">+</span> <span class="o">(</span><span class="n">b</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">-</span> <span class="n">a</span><span class="o">)</span> <span class="bp">-</span> <span class="n">i</span> <span class="bp">-</span> <span class="mi">1</span> <span class="bp">=</span> <span class="n">a</span> <span class="bp">+</span> <span class="o">(</span><span class="n">a</span> <span class="bp">+</span> <span class="o">(</span><span class="n">b</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">-</span> <span class="n">a</span><span class="o">))</span> <span class="bp">-</span> <span class="n">i</span> <span class="bp">-</span> <span class="mi">1</span> <span class="o">:</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">two_mul</span><span class="o">]</span>
<span class="bp">...</span> <span class="bp">=</span> <span class="n">a</span> <span class="bp">+</span> <span class="o">(</span><span class="n">b</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">-</span> <span class="n">i</span> <span class="bp">-</span> <span class="mi">1</span> <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">nat</span><span class="bp">.</span><span class="n">add_sub_of_le</span> <span class="o">(</span><span class="n">le_trans</span> <span class="n">H</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">le_succ</span> <span class="bp">_</span><span class="o">))</span>
<span class="bp">...</span> <span class="bp">=</span> <span class="o">(</span><span class="n">a</span> <span class="bp">+</span> <span class="n">b</span><span class="o">)</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">-</span> <span class="o">(</span><span class="n">i</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span>  <span class="o">:</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">add_assoc</span><span class="o">,</span><span class="n">nat</span><span class="bp">.</span><span class="n">sub_sub</span><span class="o">]</span>
<span class="bp">...</span> <span class="bp">=</span> <span class="n">a</span> <span class="bp">+</span> <span class="n">b</span> <span class="bp">-</span> <span class="n">i</span> <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">nat</span><span class="bp">.</span><span class="n">add_sub_add_right</span>
</pre></div>

#### [ Andrew Ashworth (May 15 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126564908):
<blockquote>
<blockquote>
<p>This natural number substraction is really a nightmare. Now I want <code>b + k + 1 - (a + k) = b + 1 - a</code>. It's almost the same I had a couple of days ago. But I'm stuck again...</p>
</blockquote>
<p>I really like doing these. Patrick -- just type nat.sub and then ctrl-space escape ctrl-space to see what Lean has, you can just browse through stuff.</p>
</blockquote>
<p>Ctrl-T and typing sub brings up lemmas with sub inside</p>

#### [ Mario Carneiro (May 15 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126574769):
<p>By the way patrick, your "stupid goals" are exactly why I wrote <code>range'</code> to take a start and length instead of start and end. Remember, the value of a good modeling decision is not in the beauty of the statements but in the beauty of the proofs. When things are done right, the proof is like everything is given to you just as you need it, but when you write things in a cumbersome way the proofs become orders of magnitude more cumbersome.</p>

#### [ Mario Carneiro (May 15 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126574827):
<p>If your desire for clean statements overrides this concern, then just have two versions and write from the "porcelain" version (which looks nice but is hard to work with) to the "plumbing" version (optimized for proofs) before proving anything, and just translate back at the end.</p>

#### [ Mario Carneiro (May 15 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126575178):
<p>But cumbersome is as cumbersome does, here's a proof:</p>
<div class="codehilite"><pre><span></span>example (a b k : ℕ) : b + k + 1 - (a + k) = b + 1 - a :=
by rw [add_comm a, ← nat.sub_sub, add_right_comm, nat.add_sub_cancel]
</pre></div>


<p>and a counterexample:</p>
<div class="codehilite"><pre><span></span>#eval do
  a ← list.range 3,
  b ← list.range 3,
  i ← list.range 3,
  return $ to_bool (∀ (_:a ≤ b), 2 * a + (b + 1 - a) - i - 1 = a - i + b)
 -- [tt, tt, tt, tt, ff, ff, tt, ff, ff, tt, tt, tt, tt, tt, ff, tt, tt, ff, tt, tt, tt, tt, tt, tt, tt, tt, tt]
</pre></div>


<p>That's my version of isabelle quickcheck - I just evaluated the theorem at some small numbers and it sometimes fails.</p>

#### [ Mario Carneiro (May 15 2018 at 06:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126575374):
<p>Assuming you don't want to learn the beautiful theory of monus on the naturals, but just want to pretend it's regular subtraction, I recommend you treat it like a partial function, in the sense that you never state a theorem about <code>-</code> unless the fact that the RHS is less or equal to the LHS is in the context or otherwise deducible. Your second theorem fails this, since it has a variable <code>i</code> being subtracted from stuff even though there is no upper bound on it.</p>

#### [ Mario Carneiro (May 15 2018 at 07:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126575537):
<p>hm, maybe this is a slightly nicer quickcheck:</p>
<div class="codehilite"><pre><span></span>#eval do
  a ← list.range 5,
  b ← list.range 5,
  i ← list.range 5,
  guardb (a ≤ b),
  guardb (2 * a + (b + 1 - a) - i - 1 ≠ a - i + b),
  return (a, b, i)
</pre></div>


<p>it returns a list of counterexample triples</p>

#### [ Chris Hughes (May 15 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579115):
<blockquote>
<p>hmm, but the goal is not an implication</p>
</blockquote>
<p>I think it's because some of the hypotheses are an implication</p>

#### [ Gabriel Ebner (May 15 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579186):
<p>Indeed, look at the (condition of the) induction hypothesis.</p>

#### [ Patrick Massot (May 15 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579580):
<p>Sorry I messed up the last statement. What I really need is <code>2 * a + (b + 1 - a) - i - 1 = a+b-i</code> assuming <code>a ≤ b</code> and <code>i ∈ range' a (b + 1 - a)</code></p>

#### [ Patrick Massot (May 15 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579628):
<p>I do have all the right bounds, that's what my <code>foldr_congr</code> and <code>filter_ext</code> are made for</p>

#### [ Patrick Massot (May 15 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579681):
<p>But I should probably think about first proving stuff with cumbersome statements and then try to deduce the natural statements from their twisted versions</p>

#### [ Kevin Buzzard (May 15 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579683):
<p>Patrick I proved what you wanted, right?</p>

#### [ Patrick Massot (May 15 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579684):
<p>This is all about summing for n from a to b, instead of n from a to a+k</p>

#### [ Patrick Massot (May 15 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579691):
<p>You proved one of the things I wanted, thank you very much to you and Mario, but this is another one</p>

#### [ Kevin Buzzard (May 15 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579692):
<p>The "true version" above</p>

#### [ Kevin Buzzard (May 15 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579695):
<p>I thought I'd done everything for oyu</p>

#### [ Kevin Buzzard (May 15 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579696):
<p>what is missing?</p>

#### [ Patrick Massot (May 15 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579697):
<p>Oh sorry</p>

#### [ Kevin Buzzard (May 15 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579699):
<p>:-)</p>

#### [ Patrick Massot (May 15 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579701):
<p>I missed that one</p>

#### [ Kevin Buzzard (May 15 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579739):
<p>I can believe that these things are not to everyone's tastes. I only did it because I quite like them.</p>

#### [ Patrick Massot (May 15 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579742):
<p>I'm glad you're such a pervert</p>

#### [ Patrick Massot (May 15 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579744):
<p>Thank you very much</p>

#### [ Kevin Buzzard (May 15 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579746):
<p>What I especially like is that Mario's proof is only about 30% shorter :-)</p>

#### [ Kevin Buzzard (May 15 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579755):
<p>[and that I was aware that something like this would probably work after I finished mine...]</p>

#### [ Kevin Buzzard (May 15 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579799):
<blockquote>
<p>Indeed, look at the (condition of the) induction hypothesis.</p>
</blockquote>
<p>Right -- that's what I'm unclear about. Explicitly -- <code>simp * {contextual := tt}</code> does something different to <code>simp</code> in a situation where there is a _hypothesis_ of the form <code>X -&gt; Y</code>, in which case it does...what?</p>

#### [ Kevin Buzzard (May 15 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579815):
<p>Oh -- maybe I do understand.</p>

#### [ Chris Hughes (May 15 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579858):
<p>It's hard to tell because trace.simplify doesn't show you where the rewrites are happening.</p>

#### [ Kenny Lau (May 15 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579860):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> can you derive Kepler's laws?</p>

#### [ Kevin Buzzard (May 15 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579865):
<p>Where are the mods? Honestly, this place is going down the pan</p>

#### [ Mario Carneiro (May 15 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579919):
<p>Hi there, it's your friendly neighborhood mod</p>

#### [ Patrick Massot (May 15 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579927):
<p>Are we still rewriting under a union?</p>

#### [ Mario Carneiro (May 15 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579932):
<p>It's all connected, I'm sure</p>

#### [ Patrick Massot (May 15 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579933):
<p>What about this one: <code>lemma reverse_range' (a b : ℕ) : reverse (range' a b) = map (λ i, 2*a+b-i-1) (range' a b) </code>?</p>

#### [ Mario Carneiro (May 15 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579935):
<p>even Kepler's laws get involved in some rewrites</p>

#### [ Patrick Massot (May 15 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579936):
<p>I need a topic "I hate natural numbers"</p>

#### [ Mario Carneiro (May 15 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579979):
<p>That statement reminds me a lot of Kevin's theorem on reversing sums</p>

#### [ Patrick Massot (May 15 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579982):
<p>Of course this is what I'm doing</p>

#### [ Patrick Massot (May 15 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579985):
<p>I'm working on my big_op project</p>

#### [ Patrick Massot (May 15 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579992):
<p>And this statement is partly what motivated my <code>nth_le_map</code> question</p>

#### [ Patrick Massot (May 15 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126579997):
<p>I wanted to use <code>ext_le</code> on that one</p>

#### [ Mario Carneiro (May 15 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580039):
<p>suggestion: don't use <code>2*a+b-i-1</code>, use <code>a-(b+1-a)-i</code></p>

#### [ Mario Carneiro (May 15 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580049):
<p>otherwise you will spend the whole proof showing that the first thing rewrites to the second</p>

#### [ Patrick Massot (May 15 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580050):
<p>That's part of the nightmare: each time I change my mind on something like this, I must redo all the natural numbers computations lemmas</p>

#### [ Patrick Massot (May 15 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580096):
<p>With <code>2*a+b-i-1</code> I can use what Kevin proved last night down the road. Otherwise I return to having nothing</p>

#### [ Mario Carneiro (May 15 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580103):
<p>We call that cruft</p>

#### [ Mario Carneiro (May 15 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580112):
<p>Here's a suggestion: write the theorem so as to minimize the number of rewrites. That is, as soon as you get something technically the same as what you want (in this case, <code>range' a b = map ... (range' a b)</code>), go with it, even if it's written in a kind of weird way</p>

#### [ Mario Carneiro (May 15 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580116):
<p>if you do that for two or three theorems the idioms will stand out</p>

#### [ Mario Carneiro (May 15 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580156):
<p>like in this case keeping <code>b+1-a</code> together as a unit</p>

#### [ Kevin Buzzard (May 15 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580158):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">list</span><span class="bp">.</span><span class="n">basic</span>
<span class="kn">open</span> <span class="n">list</span>
<span class="kn">lemma</span> <span class="n">foldr_ext</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">l</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="n">f&#39;</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">β</span><span class="o">)</span>
  <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">l</span><span class="o">,</span> <span class="bp">∀</span> <span class="n">b</span> <span class="o">:</span> <span class="n">β</span><span class="o">,</span> <span class="n">f</span> <span class="n">a</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">f&#39;</span> <span class="n">a</span> <span class="n">b</span><span class="o">)</span> <span class="o">:</span> <span class="n">foldr</span> <span class="n">f</span> <span class="n">s</span> <span class="n">l</span> <span class="bp">=</span> <span class="n">foldr</span> <span class="n">f&#39;</span> <span class="n">s</span> <span class="n">l</span> <span class="o">:=</span>
<span class="k">begin</span> <span class="n">induction</span> <span class="n">l</span> <span class="k">with</span> <span class="n">A</span> <span class="n">B</span> <span class="n">C</span><span class="o">,</span> <span class="o">{</span><span class="n">simp</span><span class="o">},</span> <span class="c1">-- base case}</span>
  <span class="n">simp</span> <span class="n">at</span> <span class="n">H</span> <span class="o">{</span><span class="n">contextual</span> <span class="o">:=</span> <span class="n">tt</span><span class="o">},</span>
  <span class="n">sorry</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (May 15 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580159):
<p>I have isolated <code>contextual := tt</code> doing something</p>

#### [ Gabriel Ebner (May 15 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580165):
<blockquote>
<p>Right -- that's what I'm unclear about. Explicitly -- <code>simp * {contextual := tt}</code> does something different to <code>simp</code> in a situation where there is a _hypothesis_ of the form <code>X -&gt; Y</code>, in which case it does...what?</p>
</blockquote>
<p>Oh no, there is no difference in how simp treats implications in assumptions.  If you have a simp lemma/assumption <code>forall x, p x -&gt; f x=g x</code>, then <code>simp</code> will try to prove <code>p a</code> before rewriting <code>f a</code> to <code>g a</code>.  And it proves this condition using <code>simp</code> itself!  Small demo:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">n</span><span class="o">}</span> <span class="o">{</span><span class="n">q</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">(</span><span class="n">h1</span> <span class="o">:</span> <span class="n">n</span><span class="bp">=</span><span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="n">h2</span> <span class="o">:</span> <span class="n">n</span><span class="bp">*</span><span class="n">n</span><span class="bp">=</span><span class="n">n</span> <span class="bp">→</span> <span class="n">q</span><span class="o">)</span> <span class="o">:</span> <span class="n">q</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span> <span class="bp">*</span>
</pre></div>


<p>Here <code>simp</code> first proves the condition <code>n*n = n</code> (using <code>simp</code>) before rewriting <code>q</code> to <code>true</code>.</p>

#### [ Kevin Buzzard (May 15 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580167):
<p>darn no I haven't</p>

#### [ Kevin Buzzard (May 15 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580178):
<p>but Gabriel has. Thanks!</p>

#### [ Kevin Buzzard (May 15 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580221):
<p>Wait -- there is no <code>contextual</code> here?</p>

#### [ Gabriel Ebner (May 15 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580229):
<p>No, <code>simp</code> can use conditional simp lemmas without <code>contextual:=tt</code>.  It uses <code>simp</code> to prove the condition.</p>

#### [ Patrick Massot (May 15 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580233):
<p>Mario, the trouble is I want to prove </p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">big</span><span class="bp">.</span><span class="n">range_anti_mph</span> <span class="o">{</span><span class="n">φ</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">R</span><span class="o">}</span> <span class="o">(</span><span class="n">P</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">[</span><span class="n">decidable_pred</span> <span class="n">P</span><span class="o">]</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">R</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span>
  <span class="o">(</span><span class="n">Hop</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">R</span><span class="o">,</span> <span class="n">φ</span> <span class="o">(</span><span class="n">a</span> <span class="err">◆</span> <span class="n">b</span><span class="o">)</span> <span class="bp">=</span> <span class="n">φ</span> <span class="n">b</span> <span class="err">◆</span> <span class="n">φ</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">Hnil</span> <span class="o">:</span> <span class="n">φ</span> <span class="n">nil</span> <span class="bp">=</span> <span class="n">nil</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">φ</span> <span class="o">(</span><span class="n">big</span><span class="o">[(</span><span class="err">◆</span><span class="o">)</span><span class="bp">/</span><span class="n">nil</span><span class="o">]</span><span class="bp">_</span><span class="o">(</span><span class="n">i</span><span class="bp">=</span><span class="n">a</span><span class="bp">..</span><span class="n">b</span> <span class="bp">|</span> <span class="o">(</span><span class="n">P</span> <span class="n">i</span><span class="o">))</span> <span class="n">F</span> <span class="n">i</span><span class="o">)</span> <span class="bp">=</span> <span class="n">big</span><span class="o">[(</span><span class="err">◆</span><span class="o">)</span><span class="bp">/</span><span class="n">nil</span><span class="o">]</span><span class="bp">_</span><span class="o">(</span><span class="n">i</span><span class="bp">=</span><span class="n">a</span><span class="bp">..</span><span class="n">b</span> <span class="bp">|</span> <span class="o">(</span><span class="n">P</span> <span class="o">(</span><span class="n">a</span><span class="bp">+</span><span class="n">b</span><span class="bp">-</span><span class="n">i</span><span class="o">)))</span> <span class="n">φ</span> <span class="o">(</span><span class="n">F</span> <span class="o">(</span><span class="n">a</span><span class="bp">+</span><span class="n">b</span><span class="bp">-</span><span class="n">i</span><span class="o">))</span>
</pre></div>


<p>I don't want the <code>a+b-i</code> in the conclusion to be some weird formula which is the same after a dozen rewrites</p>

#### [ Kevin Buzzard (May 15 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580245):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">list</span><span class="bp">.</span><span class="n">basic</span>
<span class="kn">open</span> <span class="n">list</span>
<span class="kn">lemma</span> <span class="n">foldr_ext</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">l</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="n">f&#39;</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">β</span><span class="o">)</span>
  <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">l</span><span class="o">,</span> <span class="bp">∀</span> <span class="n">b</span> <span class="o">:</span> <span class="n">β</span><span class="o">,</span> <span class="n">f</span> <span class="n">a</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">f&#39;</span> <span class="n">a</span> <span class="n">b</span><span class="o">)</span> <span class="o">:</span> <span class="n">foldr</span> <span class="n">f</span> <span class="n">s</span> <span class="n">l</span> <span class="bp">=</span> <span class="n">foldr</span> <span class="n">f&#39;</span> <span class="n">s</span> <span class="n">l</span> <span class="o">:=</span>
<span class="k">begin</span> <span class="n">induction</span> <span class="n">l</span> <span class="k">with</span> <span class="n">A</span> <span class="n">B</span> <span class="n">C</span><span class="o">,</span> <span class="o">{</span><span class="n">simp</span><span class="o">},</span> <span class="c1">-- base case}</span>
  <span class="n">simp</span> <span class="n">at</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">simp</span> <span class="bp">*</span><span class="o">,</span>
  <span class="c1">-- dammit simp, prove it without using contextual</span>
  <span class="n">simp</span> <span class="bp">*</span> <span class="o">{</span><span class="n">contextual</span> <span class="o">:=</span> <span class="n">tt</span><span class="o">},</span> <span class="c1">-- what just happened?</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (May 15 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580277):
<p>That's what I don't get</p>

#### [ Mario Carneiro (May 15 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580283):
<p>I don't either. But I don't see that <code>2*a+whatever</code> anywhere in the statement either</p>

#### [ Kevin Buzzard (May 15 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580284):
<p>Can I break that last line down into simpler steps?</p>

#### [ Patrick Massot (May 15 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580286):
<p>Knowing of course that I proved</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">big</span><span class="bp">.</span><span class="n">anti_mph</span> <span class="o">{</span><span class="n">φ</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">R</span><span class="o">}</span>
  <span class="o">(</span><span class="n">Hop</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">R</span><span class="o">,</span> <span class="n">φ</span> <span class="o">(</span><span class="n">a</span> <span class="err">◆</span> <span class="n">b</span><span class="o">)</span> <span class="bp">=</span> <span class="n">φ</span> <span class="n">b</span> <span class="err">◆</span> <span class="n">φ</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">Hnil</span> <span class="o">:</span> <span class="n">φ</span> <span class="n">nil</span> <span class="bp">=</span> <span class="n">nil</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">φ</span> <span class="o">(</span><span class="n">big</span><span class="o">[(</span><span class="err">◆</span><span class="o">)</span><span class="bp">/</span><span class="n">nil</span><span class="o">]</span><span class="bp">_</span><span class="o">(</span><span class="n">i</span> <span class="err">∈</span> <span class="n">r</span> <span class="bp">|</span> <span class="o">(</span><span class="n">P</span> <span class="n">i</span><span class="o">))</span> <span class="n">F</span> <span class="n">i</span><span class="o">)</span> <span class="bp">=</span> <span class="n">big</span><span class="o">[(</span><span class="err">◆</span><span class="o">)</span><span class="bp">/</span><span class="n">nil</span><span class="o">]</span><span class="bp">_</span><span class="o">(</span><span class="n">i</span> <span class="err">∈</span> <span class="n">r</span><span class="bp">.</span><span class="n">reverse</span> <span class="bp">|</span> <span class="o">(</span><span class="n">P</span> <span class="n">i</span><span class="o">))</span> <span class="n">φ</span> <span class="o">(</span><span class="n">F</span> <span class="n">i</span><span class="o">)</span>
</pre></div>


<p>a long time ago</p>

#### [ Patrick Massot (May 15 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580300):
<p>I'm only fighting the <code>range'</code> stuff</p>

#### [ Patrick Massot (May 15 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580345):
<p>And I have </p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">big</span><span class="bp">.</span><span class="n">map</span> <span class="o">{</span><span class="n">J</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">I</span> <span class="bp">→</span> <span class="n">J</span><span class="o">)</span> <span class="o">(</span><span class="n">P</span> <span class="o">:</span> <span class="n">J</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">[</span><span class="n">decidable_pred</span> <span class="n">P</span><span class="o">]</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">J</span> <span class="bp">→</span> <span class="n">R</span><span class="o">)</span> <span class="o">:</span>
  <span class="o">(</span><span class="n">big</span><span class="o">[(</span><span class="err">◆</span><span class="o">)</span><span class="bp">/</span><span class="n">nil</span><span class="o">]</span><span class="bp">_</span><span class="o">(</span><span class="n">j</span> <span class="err">∈</span> <span class="n">map</span> <span class="n">f</span> <span class="n">r</span> <span class="bp">|</span> <span class="o">(</span><span class="n">P</span> <span class="n">j</span><span class="o">))</span> <span class="o">(</span><span class="n">F</span> <span class="n">j</span><span class="o">))</span> <span class="bp">=</span> <span class="o">(</span><span class="n">big</span><span class="o">[(</span><span class="err">◆</span><span class="o">)</span><span class="bp">/</span><span class="n">nil</span><span class="o">]</span><span class="bp">_</span><span class="o">(</span><span class="n">i</span> <span class="err">∈</span> <span class="n">r</span> <span class="bp">|</span> <span class="o">(</span><span class="n">P</span> <span class="o">(</span><span class="n">f</span> <span class="n">i</span><span class="o">)))</span> <span class="o">(</span><span class="n">F</span> <span class="o">(</span><span class="n">f</span> <span class="n">i</span><span class="o">)))</span>
</pre></div>

#### [ Patrick Massot (May 15 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580348):
<p>So I wanted to write <code>reverse (range' ...)</code> as a <code>map ... (range' ...)</code></p>

#### [ Mario Carneiro (May 15 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580357):
<p>What are you going to do with the <code>map</code> once you have it?</p>

#### [ Gabriel Ebner (May 15 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580362):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span>  Look at the left-hand side of the implication in the induction hypothesis in foldr_ext.  Contextual simplification makes a difference here: simp then has the additional assumption <code>a ∈ l</code>, which it can use to apply <code>H</code>.</p>

#### [ Mario Carneiro (May 15 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580404):
<p>Okay I think it is time to split this convo in two</p>

#### [ Patrick Massot (May 15 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580405):
<p>Yes sorry</p>

#### [ Kevin Buzzard (May 15 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580428):
<blockquote>
<p>Okay I think it is time to split this convo in two</p>
</blockquote>
<p>...given that neither thread is about the topic name ;-)</p>

#### [ Gabriel Ebner (May 15 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580490):
<div class="codehilite"><pre><span></span><span class="n">case</span> <span class="n">list</span><span class="bp">.</span><span class="n">cons</span>
<span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">,</span>
<span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_2</span><span class="o">,</span>
<span class="n">f</span> <span class="n">f&#39;</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">β</span><span class="o">,</span>
<span class="n">s</span> <span class="o">:</span> <span class="n">β</span><span class="o">,</span>
<span class="n">h</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span>
<span class="n">t</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">,</span>
<span class="n">IH</span> <span class="o">:</span> <span class="o">(</span><span class="bp">∀</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">t</span> <span class="bp">→</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">b</span> <span class="o">:</span> <span class="n">β</span><span class="o">),</span> <span class="n">f</span> <span class="n">a</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">f&#39;</span> <span class="n">a</span> <span class="n">b</span><span class="o">)</span> <span class="bp">→</span> <span class="n">foldr</span> <span class="n">f</span> <span class="n">s</span> <span class="n">t</span> <span class="bp">=</span> <span class="n">foldr</span> <span class="n">f&#39;</span> <span class="n">s</span> <span class="n">t</span><span class="o">,</span>
<span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">h</span> <span class="bp">::</span> <span class="n">t</span> <span class="bp">→</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">b</span> <span class="o">:</span> <span class="n">β</span><span class="o">),</span> <span class="n">f</span> <span class="n">a</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">f&#39;</span> <span class="n">a</span> <span class="n">b</span>
<span class="err">⊢</span> <span class="n">foldr</span> <span class="n">f</span> <span class="n">s</span> <span class="o">(</span><span class="n">h</span> <span class="bp">::</span> <span class="n">t</span><span class="o">)</span> <span class="bp">=</span> <span class="n">foldr</span> <span class="n">f&#39;</span> <span class="n">s</span> <span class="o">(</span><span class="n">h</span> <span class="bp">::</span> <span class="n">t</span><span class="o">)</span>
</pre></div>


<p>This is the case for cons. ^^   In order to apply <code>IH</code>, you need to prove its left-hand side using <code>H</code>.  And to prove <code>a ∈ h :: t</code>, you need the <code>a ∈ t</code> from <code>IH</code>.</p>

#### [ Kevin Buzzard (May 15 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580729):
<p>I am beginning to understand now. I'm writing out the proof in full, and I have to apply <code>IH</code> and then apply <code>H</code>.</p>

#### [ Kevin Buzzard (May 15 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580768):
<p>So everything is there but somehow it's all in a bit of a tangle</p>

#### [ Kevin Buzzard (May 15 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580909):
<p>I think I have it now</p>

#### [ Kevin Buzzard (May 15 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580911):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">got_it</span> <span class="o">(</span><span class="n">P</span> <span class="n">Q</span> <span class="n">R</span> <span class="n">S</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">IH</span> <span class="o">:</span> <span class="o">(</span><span class="n">P</span> <span class="bp">→</span> <span class="n">R</span><span class="o">)</span> <span class="bp">→</span> <span class="n">S</span><span class="o">)</span> <span class="o">(</span><span class="n">H0</span> <span class="o">:</span> <span class="n">P</span> <span class="bp">→</span> <span class="n">Q</span><span class="o">)</span> <span class="o">(</span><span class="n">H&#39;</span> <span class="o">:</span> <span class="n">Q</span> <span class="bp">→</span> <span class="n">R</span><span class="o">)</span> <span class="o">:</span> <span class="n">S</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="c1">--simp *, -- fails</span>
<span class="n">simp</span> <span class="bp">*</span> <span class="o">{</span><span class="n">contextual</span> <span class="o">:=</span> <span class="n">tt</span><span class="o">},</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (May 15 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580956):
<p>I want to use <code>IH</code> to prove <code>S</code> but the hypothesis of <code>IH</code> isn't immediately true; however simp can prove it using other hypotheses.</p>

#### [ Kevin Buzzard (May 15 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126580975):
<p>Thanks Gabriel. To show your time isn't being wasted here I'll add it to the simp docs (once I've done another 8 hours of marking..)</p>

#### [ Kevin Buzzard (May 15 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126581149):
<p>All of these conversations (threads about what simp does and doesn't do, threads about how to make type class inference work etc) -- it's in some sense sad that they just appear here and then disappear. The type class inference thread especially contains some really useful tips (in the sense that I was genuinely stuck about three times and then got unstucked by the contents of that thread). I will try to write some notes on that thread too, but I have so much marking at the minute and I have decided that it is time to prove an affine scheme is a scheme so I spend all my spare time on that. I am using the zulip "star" functionality a lot at the minute -- star meaning "get back to this later and write it up properly".</p>

#### [ Kevin Buzzard (May 15 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126581151):
<p>Thanks to all as ever.</p>

#### [ Patrick Massot (May 15 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126581273):
<p>Next year Lean will mark all this for you</p>

#### [ Kevin Buzzard (May 15 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126581275):
<p>That's the plan!</p>

#### [ Patrick Massot (May 17 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126718080):
<p>Because this <code>{contextual := true}</code> discussion I'm back to beginner level. Except that, instead of trying <code>simp</code> whatever the goal and hope for the best, I try <code>simp * at * { contextual := true}</code></p>

#### [ Patrick Massot (May 17 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20under%20a%20union/near/126718124):
<p>And often it works!</p>


{% endraw %}
