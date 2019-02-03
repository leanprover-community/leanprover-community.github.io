---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/48901treacheroussorry.html
---

## Stream: [general](index.html)
### Topic: [treacherous sorry](48901treacheroussorry.html)

---


{% raw %}
#### [ Patrick Massot (Jun 28 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128764182):
<p>I'm slowing beginning to understand why trying to formalize math in a top to down way is very dangerous, even if this is very appealing to mathematicians. Today's lesson is about sorried properties. In the minimized version below, say we are trying to build of stub of continuous functions theory.</p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span>

<span class="c1">-- function f is continuous at point x</span>
<span class="n">def</span> <span class="n">continuous_at</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="n">sorry</span>

<span class="n">def</span> <span class="n">continuous</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">continuous_at</span> <span class="n">x</span> <span class="n">f</span>

<span class="kn">lemma</span> <span class="n">continuous_at_comp</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">}</span> <span class="o">{</span><span class="n">g</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">}</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">:</span>
<span class="n">continuous_at</span> <span class="n">x</span> <span class="n">f</span> <span class="bp">→</span> <span class="n">continuous_at</span> <span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">)</span> <span class="n">g</span> <span class="bp">→</span> <span class="n">continuous_at</span> <span class="n">x</span> <span class="o">(</span><span class="n">g</span> <span class="err">∘</span> <span class="n">f</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>

<span class="kn">lemma</span> <span class="n">continuous_comp</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">continuous</span> <span class="n">f</span> <span class="bp">→</span> <span class="n">continuous</span> <span class="n">g</span> <span class="bp">→</span> <span class="n">continuous</span> <span class="o">(</span><span class="n">g</span> <span class="err">∘</span> <span class="n">f</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">assume</span> <span class="n">cont_f</span> <span class="n">cont_g</span> <span class="n">x</span><span class="o">,</span> <span class="n">continuous_at_comp</span> <span class="o">(</span><span class="n">cont_f</span> <span class="n">x</span><span class="o">)</span> <span class="o">(</span><span class="n">cont_g</span> <span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">))</span>
</pre></div>


<p>Looks good to me. It tells the story of continuity being a property of a function that can be checked near each point, and the composition property of this local thing implies composition for the global thing.</p>

#### [ Patrick Massot (Jun 28 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128764231):
<p>Now let's look at the following "simplified" version:</p>

#### [ Patrick Massot (Jun 28 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128764236):
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span>

<span class="c1">-- function f is continuous at point x</span>
<span class="n">def</span> <span class="n">continuous_at</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="n">sorry</span>

<span class="n">def</span> <span class="n">continuous</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">continuous_at</span> <span class="n">x</span> <span class="n">f</span>

<span class="kn">lemma</span> <span class="n">continuous_comp</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">continuous</span> <span class="n">f</span> <span class="bp">→</span> <span class="n">continuous</span> <span class="n">g</span> <span class="bp">→</span> <span class="n">continuous</span> <span class="o">(</span><span class="n">g</span> <span class="err">∘</span> <span class="n">f</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">assume</span> <span class="n">cont_f</span> <span class="n">cont_g</span> <span class="n">x</span><span class="o">,</span> <span class="n">cont_g</span> <span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">)</span>
</pre></div>


<p><span class="emoji emoji-1f631" title="scream">:scream:</span></p>

#### [ Patrick Massot (Jun 28 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128764253):
<p>It reminds me of traps of unit testing using mocks.</p>

#### [ Mario Carneiro (Jun 28 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128765257):
<p>The problem is that <code>continuous_at</code> has been defined as a constant wrt <code>x</code> and <code>f</code>, since <code>sorry : Prop</code> has no stated dependence on <code>x</code> and <code>f</code>. One solution is to sorry at the function level:</p>
<div class="codehilite"><pre><span></span>def continuous_at : α → (α → β) → Prop := sorry
</pre></div>


<p>(you can also write <code>∀ (x : α) (f : α → β), Prop</code> if you prefer to name the variables)</p>

#### [ Mario Carneiro (Jun 28 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128765385):
<p>That said, I completely agree with you about the dangers of axiomatizing things without a cross-check. I did not notice the issue in the first code block until you pointed it out</p>

#### [ Patrick Massot (Jun 28 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128765392):
<p>Indeed this fixes this problem. But my point remains: one needs to be extremely careful with this kind of sorries</p>

#### [ Patrick Massot (Jun 28 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128765402):
<p>I'd like to understand better what you call "cross-check".</p>

#### [ Mario Carneiro (Jun 28 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128765448):
<p>It is hard to check an axiom or a definition for correctness, since lean can't help you</p>

#### [ Mario Carneiro (Jun 28 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128765515):
<p>In a sense, proving theorems about a definition or theorems that follow from axioms form a kind of testing on the definition, since they can (but not necessarily will) expose issues and edge cases that were not originally considered</p>

#### [ Patrick Massot (Jun 28 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128765518):
<p>Something else mysterious to me: replacing <code>def continuous_at (x : α) (f : α → β) : Prop := sorry</code> by <code>constant continuous_at (x : α) (f : α → β) : Prop</code> also allows to uncover the issue</p>

#### [ Mario Carneiro (Jun 28 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128765536):
<p>That's because in <code>axiom</code> and <code>constant</code> it is always defined as a single global constant abstracted over any variables</p>

#### [ Mario Carneiro (Jun 28 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128765576):
<p>so it's exactly the same as <code>constant continuous_at : α → (α → β) → Prop</code></p>

#### [ Mario Carneiro (Jun 28 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128765597):
<p>You should think of <code>sorry</code> as providing a term of the specified type, without necessarily pulling in all the assumptions in the context but only the ones needed to typecheck the type of the sorry</p>

#### [ Mario Carneiro (Jun 28 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128765640):
<p>while <code>axiom</code> / <code>constant</code> only produces terms in the empty context so it gets all the variables</p>

#### [ Patrick Massot (Jun 28 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128765641):
<p>Indeed that clearly explains the flaw: <code>x</code> and <code>f</code> are not needed to construct a term with type <code>Prop</code></p>

#### [ Patrick Massot (Jun 28 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128765648):
<p>I mean: it explains why <code>sorry</code> is dangerous here, it doesn't quite explain why <code>constant</code> works</p>

#### [ Mario Carneiro (Jun 28 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128765652):
<p>another option would be to write <code>sorry x f</code>, but this doesn't typecheck so you have to annotate the type, which kind of defeats the point</p>

#### [ Mario Carneiro (Jun 28 2018 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128765696):
<p>i.e.</p>
<div class="codehilite"><pre><span></span>def continuous_at (x : α) (f : α → β) : Prop :=
(sorry : α → (α → β) → Prop) x f
</pre></div>

#### [ Mario Carneiro (Jun 28 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128765755):
<div class="codehilite"><pre><span></span>constant continuous_at (x : α) (f : α → β) : Prop
#print continuous_at
-- constant continuous_at : Π {α β : Type}, α → (α → β) → Prop
</pre></div>


<p>what else would it do? A <code>def</code> doesn't randomly drop variables that are given in its statement, so it would be weird for <code>constant</code> to do so</p>

#### [ Patrick Massot (Jun 28 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128765766):
<p>Ok, thanks</p>

#### [ Mario Carneiro (Jun 28 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128765769):
<p>note that even with <code>def continuous_at (x : α) (f : α → β) : Prop := sorry</code>, <code>continuous_at</code> has exactly that same type</p>

#### [ Mario Carneiro (Jun 28 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128765779):
<p>the only difference is that <code>constant continuous_at</code> can't be unfolded</p>

#### [ Patrick Massot (Jun 28 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128765781):
<p>My train ride is almost finished, I'll disappear from here (I love trains with WIFI).</p>

#### [ Patrick Massot (Jun 28 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128765792):
<p>You can answer emails in the meantime <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Sebastien Gouezel (Jun 28 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128780496):
<p>Instead of sorrying stuff, you could work in an axiomatic kind of way, just putting as assumptions all the stuff you need and starting from there. If you want to work with general pseudo-groups, maybe this is the way to go. For instance, if you define a smoothness class as follows, then I guess this is enough to define manifolds based on the smoothness class. And then you will just need to show that your favorite class (say symplectomorphisms, but maybe it is better to work with homeos to start with) satisfies your axioms, to get symplectic manifolds or C^0 manifolds.</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">real</span> <span class="n">data</span><span class="bp">.</span><span class="n">set</span><span class="bp">.</span><span class="n">function</span>

<span class="n">noncomputable</span> <span class="n">theory</span>
<span class="n">local</span> <span class="n">attribute</span> <span class="o">[</span><span class="kn">instance</span><span class="o">]</span> <span class="n">classical</span><span class="bp">.</span><span class="n">decidable_inhabited</span> <span class="n">classical</span><span class="bp">.</span><span class="n">prop_decidable</span>

<span class="n">universes</span> <span class="n">u</span> <span class="n">v</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">inhabited</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span>

<span class="kn">open</span> <span class="n">set</span>

<span class="n">def</span> <span class="n">inverse_on</span> <span class="o">(</span><span class="n">U</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">α</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">b</span><span class="o">,</span> <span class="k">if</span> <span class="n">h</span> <span class="o">:</span> <span class="n">b</span> <span class="err">∈</span> <span class="n">f</span> <span class="err">&#39;&#39;</span> <span class="n">U</span> <span class="k">then</span> <span class="n">classical</span><span class="bp">.</span><span class="n">some</span> <span class="n">h</span> <span class="k">else</span> <span class="n">default</span> <span class="n">α</span>

<span class="n">def</span> <span class="n">homeomorphism_on</span> <span class="o">(</span><span class="n">U</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">:=</span> <span class="n">inj_on</span> <span class="n">f</span> <span class="n">U</span> <span class="c1">-- agreed, this definition is not optimal</span>

<span class="kn">structure</span> <span class="n">smoothness_class</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">inhabited</span> <span class="n">α</span><span class="o">]</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">smooth_on</span> <span class="o">:</span> <span class="o">(</span><span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="n">α</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span>
<span class="o">(</span><span class="n">open_domain</span><span class="o">:</span> <span class="bp">∀</span><span class="n">U</span> <span class="n">f</span><span class="o">,</span> <span class="n">smooth_on</span> <span class="n">U</span> <span class="n">f</span> <span class="bp">→</span> <span class="n">is_open</span> <span class="n">U</span><span class="o">)</span>
<span class="o">(</span><span class="n">homeo</span><span class="o">:</span> <span class="bp">∀</span><span class="n">U</span> <span class="n">f</span><span class="o">,</span> <span class="n">smooth_on</span> <span class="n">U</span> <span class="n">f</span> <span class="bp">→</span> <span class="n">homeomorphism_on</span> <span class="n">U</span> <span class="n">f</span><span class="o">)</span>
<span class="o">(</span><span class="n">restriction</span><span class="o">:</span> <span class="bp">∀</span><span class="n">U</span> <span class="n">V</span> <span class="n">f</span><span class="o">,</span> <span class="n">smooth_on</span> <span class="n">U</span> <span class="n">f</span> <span class="bp">→</span> <span class="n">is_open</span> <span class="n">V</span> <span class="bp">→</span> <span class="n">V</span> <span class="err">⊆</span> <span class="n">U</span> <span class="bp">→</span> <span class="n">smooth_on</span> <span class="n">V</span> <span class="n">f</span><span class="o">)</span>
<span class="o">(</span><span class="n">composition</span><span class="o">:</span> <span class="bp">∀</span><span class="n">U</span> <span class="n">V</span> <span class="n">f</span> <span class="n">g</span><span class="o">,</span> <span class="n">smooth_on</span> <span class="n">U</span> <span class="n">f</span> <span class="bp">→</span> <span class="n">smooth_on</span> <span class="n">V</span> <span class="n">g</span> <span class="bp">→</span> <span class="n">f</span> <span class="err">&#39;&#39;</span><span class="o">(</span><span class="n">U</span><span class="o">)</span> <span class="err">⊆</span> <span class="n">V</span> <span class="bp">→</span> <span class="n">smooth_on</span> <span class="n">U</span> <span class="o">(</span><span class="n">g</span> <span class="err">∘</span> <span class="n">f</span><span class="o">))</span>
<span class="o">(</span><span class="n">inversion</span><span class="o">:</span> <span class="bp">∀</span><span class="n">U</span> <span class="n">f</span><span class="o">,</span> <span class="n">smooth_on</span> <span class="n">U</span> <span class="n">f</span> <span class="bp">→</span> <span class="n">smooth_on</span> <span class="o">(</span><span class="n">f</span> <span class="err">&#39;&#39;</span><span class="o">(</span><span class="n">U</span><span class="o">))</span> <span class="o">(</span><span class="n">inverse_on</span> <span class="n">U</span> <span class="n">f</span><span class="o">))</span>

<span class="kn">variables</span> <span class="o">[</span><span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">S</span><span class="o">:</span> <span class="n">smoothness_class</span> <span class="n">α</span><span class="o">)</span>
<span class="c1">-- and now I want to define manifolds based on the class of maps S...</span>
</pre></div>


<p>Maybe I forgot some important axiom, but you see the idea.</p>
<p>And I also enjoy the wifi on trains :)</p>

#### [ Kevin Buzzard (Jun 28 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128781917):
<p>This is very interesting to me because we started at the top with perfectoid spaces: <a href="https://github.com/kbuzzard/lean-perfectoid-spaces/blob/master/src/perfectoid_space.lean" target="_blank" title="https://github.com/kbuzzard/lean-perfectoid-spaces/blob/master/src/perfectoid_space.lean">https://github.com/kbuzzard/lean-perfectoid-spaces/blob/master/src/perfectoid_space.lean</a> ; and I had no idea that this could cause any problems at all. The perfectoid space link is what looks like a fully written definition of a perfectoid space, but the import contains a gazillion sorries.</p>

#### [ Simon Hudon (Jun 28 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/treacherous%20sorry/near/128782917):
<p>Is <code>gazillion</code> defined as <code>def gazillion : nat := sorry</code>?</p>


{% endraw %}
