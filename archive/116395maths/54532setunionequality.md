---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/54532setunionequality.html
---

## Stream: [maths](index.html)
### Topic: [set union equality](54532setunionequality.html)

---


{% raw %}
#### [ Kevin Buzzard (Apr 25 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125683378):
<p><code>example (X : Type) (R : Type) (D : R → set X) (γ : Type) (f : γ → R) :
  ⋃₀(D '' set.range f) = ⋃ (i : γ), D (f i) := sorry</code></p>

#### [ Kevin Buzzard (Apr 25 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125683386):
<p>I was rather hoping simp would do this one...</p>

#### [ Kevin Buzzard (Apr 25 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125683389):
<p>is there some lemma?</p>

#### [ Kevin Buzzard (Apr 25 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125683403):
<p>or do I stick with my 25 line tactic proof :-/</p>

#### [ Mario Carneiro (Apr 25 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125683516):
<p>use <code>D '' range f = range (D o f)</code> and then hopefully <code>U range f = U i, f i</code> is a theorem</p>

#### [ Kenny Lau (Apr 25 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125683659):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">set</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">D</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">set</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="n">R</span><span class="o">)</span> <span class="o">:</span>
  <span class="err">⋃₀</span><span class="o">(</span><span class="n">D</span> <span class="err">&#39;&#39;</span> <span class="n">set</span><span class="bp">.</span><span class="n">range</span> <span class="n">f</span><span class="o">)</span> <span class="bp">=</span> <span class="err">⋃</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">),</span> <span class="n">D</span> <span class="o">(</span><span class="n">f</span> <span class="n">i</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">set</span><span class="bp">.</span><span class="n">ext</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">z</span><span class="o">,</span> <span class="bp">⟨λ</span> <span class="bp">⟨</span><span class="n">x1</span><span class="o">,</span> <span class="bp">⟨⟨</span><span class="n">x2</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">x3</span><span class="o">,</span> <span class="n">h1</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">h2</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">h3</span><span class="bp">⟩⟩</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">x1</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">x3</span><span class="o">,</span> <span class="n">h2</span> <span class="bp">▸</span> <span class="n">h1</span> <span class="bp">▸</span> <span class="n">rfl</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">h3</span><span class="bp">⟩</span><span class="o">,</span>
<span class="bp">λ</span> <span class="bp">⟨</span><span class="n">x1</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">x2</span><span class="o">,</span> <span class="n">h1</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">h3</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">x1</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">f</span> <span class="n">x2</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">x2</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">h1</span><span class="bp">.</span><span class="n">symm</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">h3</span><span class="bp">⟩⟩</span>
</pre></div>

#### [ Kevin Buzzard (Apr 25 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125683764):
<p>That's my 25 line tactic proof!</p>

#### [ Kenny Lau (Apr 25 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125683768):
<p>interesting</p>

#### [ Kevin Buzzard (Apr 25 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125683776):
<div class="codehilite"><pre><span></span><span class="k">begin</span>
  <span class="n">apply</span> <span class="n">set</span><span class="bp">.</span><span class="n">ext</span><span class="o">,</span>
  <span class="n">intro</span> <span class="n">x</span><span class="o">,</span>
  <span class="n">split</span><span class="o">,</span>
  <span class="n">intro</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">H</span> <span class="k">with</span> <span class="n">V</span> <span class="n">HV</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">HV</span> <span class="k">with</span> <span class="n">HV</span> <span class="n">HX</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">HV</span> <span class="k">with</span> <span class="n">r</span> <span class="n">HR</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">HR</span><span class="bp">.</span><span class="mi">1</span> <span class="k">with</span> <span class="n">i</span> <span class="n">Hi</span><span class="o">,</span>
  <span class="n">existsi</span> <span class="n">V</span><span class="o">,</span>
  <span class="n">existsi</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">assumption</span><span class="o">,</span>
  <span class="n">simp</span><span class="o">,</span>
  <span class="n">existsi</span> <span class="n">i</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">Hi</span><span class="o">,</span><span class="n">rw</span> <span class="n">HR</span><span class="bp">.</span><span class="mi">2</span><span class="o">,</span>

  <span class="n">intro</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">H</span> <span class="k">with</span> <span class="n">V</span> <span class="n">HV</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">HV</span> <span class="k">with</span> <span class="n">HV</span> <span class="n">Hx</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">HV</span> <span class="k">with</span> <span class="n">i</span> <span class="n">Hi</span><span class="o">,</span>
  <span class="n">existsi</span> <span class="n">V</span><span class="o">,</span>
  <span class="n">existsi</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">assumption</span><span class="o">,</span>
  <span class="n">existsi</span> <span class="o">(</span><span class="n">f</span> <span class="n">i</span><span class="o">),</span>
  <span class="n">split</span><span class="o">,</span>
  <span class="n">simp</span><span class="o">,</span>
  <span class="n">existsi</span> <span class="n">i</span><span class="o">,</span>
  <span class="n">refl</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">Hi</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Apr 25 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125683779):
<p>use <code>rcases</code> :P</p>

#### [ Kevin Buzzard (Apr 25 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125683783):
<p>It must be, because we both start with the same line and then do nothing</p>

#### [ Kevin Buzzard (Apr 25 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125683795):
<p>other than following our nose</p>

#### [ Kevin Buzzard (Apr 25 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125685487):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">D</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">set</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="n">R</span><span class="o">)</span> <span class="o">:</span>
  <span class="err">⋃₀</span><span class="o">(</span><span class="n">D</span> <span class="err">&#39;&#39;</span> <span class="n">set</span><span class="bp">.</span><span class="n">range</span> <span class="n">f</span><span class="o">)</span> <span class="bp">=</span> <span class="err">⋃</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">),</span> <span class="n">D</span> <span class="o">(</span><span class="n">f</span> <span class="n">i</span><span class="o">)</span> <span class="o">:=</span>
  <span class="k">begin</span>
  <span class="n">rw</span> <span class="o">[</span><span class="err">←</span><span class="n">set</span><span class="bp">.</span><span class="n">image_univ</span><span class="o">,</span><span class="err">←</span><span class="n">set</span><span class="bp">.</span><span class="n">image_comp</span><span class="o">],</span>
  <span class="k">show</span> <span class="err">⋃₀</span><span class="o">(</span><span class="n">D</span> <span class="err">∘</span> <span class="n">f</span> <span class="err">&#39;&#39;</span> <span class="n">set</span><span class="bp">.</span><span class="n">univ</span><span class="o">)</span> <span class="bp">=</span> <span class="err">⋃</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">),</span> <span class="o">(</span><span class="n">D</span> <span class="err">∘</span> <span class="n">f</span><span class="o">)</span> <span class="n">i</span><span class="o">,</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">set</span><span class="bp">.</span><span class="n">Union_eq_sUnion_image</span><span class="o">],</span>
  <span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Apr 25 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125685555):
<p>don't even need the show</p>

#### [ Kevin Buzzard (Apr 25 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125685585):
<p>Mario's insight is that we reduce the number of functions from 2 to 1 and then simp can handle it</p>

#### [ Kenny Lau (Apr 25 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125685871):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">set</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">D</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">set</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="n">R</span><span class="o">)</span> <span class="o">:</span>
  <span class="err">⋃₀</span><span class="o">(</span><span class="n">D</span> <span class="err">&#39;&#39;</span> <span class="n">set</span><span class="bp">.</span><span class="n">range</span> <span class="n">f</span><span class="o">)</span> <span class="bp">=</span> <span class="err">⋃</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">),</span> <span class="n">D</span> <span class="o">(</span><span class="n">f</span> <span class="n">i</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">set</span><span class="bp">.</span><span class="n">Union_eq_sUnion_image</span><span class="o">,</span> <span class="err">←</span> <span class="n">set</span><span class="bp">.</span><span class="n">range_comp</span><span class="o">]</span>
</pre></div>

#### [ Kenny Lau (Apr 25 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125685873):
<p>do I win?</p>

#### [ Kevin Buzzard (Apr 25 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125686366):
<p><a href="/user_uploads/3121/wqULCViCYbpmWIeiX5WCeQ76/IMG_20180425_113712650.jpg" target="_blank" title="IMG_20180425_113712650.jpg">IMG_20180425_113712650.jpg</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/wqULCViCYbpmWIeiX5WCeQ76/IMG_20180425_113712650.jpg" target="_blank" title="IMG_20180425_113712650.jpg"><img src="/user_uploads/3121/wqULCViCYbpmWIeiX5WCeQ76/IMG_20180425_113712650.jpg"></a></div>

#### [ Kevin Buzzard (Apr 25 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125686376):
<p>saw that on the way in today and thought of you</p>

#### [ Scott Morrison (Apr 26 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125697140):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> your 25 line tactic proof doesn't seem to work (fails at <code>cases H with V HV,</code>). I was curious how my tactics cope with this one. :-)</p>

#### [ Mario Carneiro (Apr 26 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125697303):
<p>works for me</p>

#### [ Mario Carneiro (Apr 26 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125697366):
<div class="codehilite"><pre><span></span>import data.set.lattice

example (X : Type) (R : Type) (D : R → set X) (γ : Type) (f : γ → R) :
  ⋃₀(D &#39;&#39; set.range f) = ⋃ (i : γ), D (f i) :=
begin
  apply set.ext,
  ... +25 lines
end
</pre></div>

#### [ Kevin Buzzard (Apr 26 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712128):
<p>Simon's code in the cases thread didn't work for me without a minor fix</p>

#### [ Kevin Buzzard (Apr 26 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712129):
<p>I wonder whether we are using different versions of Lean</p>

#### [ Mario Carneiro (Apr 26 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712137):
<p>I'm running 04-20 now, along with the latest mathlib. Are you?</p>

#### [ Kevin Buzzard (Apr 26 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712138):
<p>you are no doubt bleeding edge, I am enjoying the stability of 4-06</p>

#### [ Kevin Buzzard (Apr 26 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712140):
<p>Upgrading is such a chore</p>

#### [ Kevin Buzzard (Apr 26 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712141):
<p>I need to do it on three machines</p>

#### [ Kevin Buzzard (Apr 26 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712142):
<p>and make all the olean files</p>

#### [ Kevin Buzzard (Apr 26 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712144):
<p>and I just want to concentrate on getting schemes done</p>

#### [ Kevin Buzzard (Apr 26 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712184):
<p>Everything is taking longer than expected</p>

#### [ Kevin Buzzard (Apr 26 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712188):
<p>because I have a bunch of commutative diagrams / exact sequences</p>

#### [ Kevin Buzzard (Apr 26 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712189):
<p>and I continually want to replace an object with a canonically isomorphic object</p>

#### [ Kevin Buzzard (Apr 26 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712190):
<p>and claim that everything is still commutative / exact</p>

#### [ Kevin Buzzard (Apr 26 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712195):
<p>I hate computers</p>

#### [ Kevin Buzzard (Apr 26 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712206):
<p>In maths you just say it works and nobody even notices</p>

#### [ Mario Carneiro (Apr 26 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712261):
<p>My instinct always says there's a proof architectural solution to such problems</p>

#### [ Mario Carneiro (Apr 26 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712268):
<p>but sometimes you just have to do it the long way a few times before you can see the pattern</p>

#### [ Mario Carneiro (Apr 26 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712269):
<p>but once you identify the pattern, it's a short hop to formalized patterns and then lemmas that save you the boilerplate work</p>

#### [ Kevin Buzzard (Apr 26 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712538):
<p>It is that way of thinking which led me to all this "unique-R-algebra-hom" stuff</p>

#### [ Kevin Buzzard (Apr 26 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712543):
<p>The proofs that the diagrams commute are just "this is a map with a property, so it's the only map with the property, so it's equal to the map we want"</p>

#### [ Kevin Buzzard (Apr 26 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712549):
<p>I think a mathematician would instinctively prove commutativity using a diagram chase</p>

#### [ Kevin Buzzard (Apr 26 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712552):
<p>"where does this element go? This way it goes here, that way it goes there, oh look they're the same"</p>

#### [ Kevin Buzzard (Apr 26 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712555):
<p>but seeing as I have a pathological fear of quotient types I had to find another way</p>

#### [ Mario Carneiro (Apr 26 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712597):
<p>I think that was a good idea on your part</p>

#### [ Kevin Buzzard (Apr 26 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712599):
<p>I don't think my universal property methods are much quicker</p>

#### [ Kevin Buzzard (Apr 26 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712601):
<p>in the sense that if I asked Kenny to prove the diagrams commute he would just do the chase</p>

#### [ Kevin Buzzard (Apr 26 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712602):
<p>and the proof would be about as long, I suspect</p>

#### [ Kevin Buzzard (Apr 26 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712603):
<p>but my methods are easier to explain</p>

#### [ Mario Carneiro (Apr 26 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712608):
<p>I think Kenny is good at getting to the end, but he needs to work on his long game</p>

#### [ Kevin Buzzard (Apr 26 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712609):
<p>they just involve setting type class inference resolution depth to 93 occasionally ;-)</p>

#### [ Mario Carneiro (Apr 26 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712654):
<p>there is a lot more possibility for "golfing" at the large scale, planning out the right lemmas that give you the most bang for the buck</p>

#### [ Mario Carneiro (Apr 26 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712668):
<p>and that's where stuff like <code>is_unique_R_hom</code> come in</p>

#### [ Mario Carneiro (Apr 26 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712717):
<p>I think the difference between Kenny's and my answer to your union-image-range question demonstrate this well</p>

#### [ Mario Carneiro (Apr 26 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712726):
<p>on the one hand you can use matches and rfl and anonymous instances to just write out the whole thing from first principles, it's not so hard</p>

#### [ Mario Carneiro (Apr 26 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712729):
<p>and on the other you could chain together two lemmas that were written exactly for the purpose</p>

#### [ Mario Carneiro (Apr 26 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712781):
<p>I think it's a bit unfortunate that proofs from lemmas lose a lot relative to proofs using basic dependent type theory simply because they have names (and lean's naming convention averages 20 characters or so)</p>

#### [ Mario Carneiro (Apr 26 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125712827):
<p>which is a bit misleading since something like <code>λ ⟨a, b⟩,</code> is actually quite a bit more complicated under the hood than it looks</p>

#### [ Kevin Buzzard (Apr 26 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713016):
<p>In practice, my current problem is that I now know enough about the system to be able to prove these things from first principles, I know that ideally this is not what I should be doing, but I do not have an encyclopedic knowledge of the lemmas which are there and to be honest I am unclear about the roadmap for getting this knowledge.</p>

#### [ Kevin Buzzard (Apr 26 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713017):
<p>I am not even sure this qualifies as a "problem"</p>

#### [ Kevin Buzzard (Apr 26 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713020):
<p>but we saw it twice yesterday</p>

#### [ Kevin Buzzard (Apr 26 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713032):
<p>My ability to retain information is not what it was; I can read the source code and think "oh that is cool" but then not remember everything that is there, unlike when I was in my 20s</p>

#### [ Kevin Buzzard (Apr 26 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713034):
<p>I need to develop (as Kenny once pointed out) a good feeling for "what _should_ be there"</p>

#### [ Kevin Buzzard (Apr 26 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713071):
<p>and then simply check that it is</p>

#### [ Kevin Buzzard (Apr 26 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713078):
<p>Having said all that, I would rather be here than where I was 6 months ago</p>

#### [ Kevin Buzzard (Apr 26 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713079):
<p>where I had to ask because I simply had no idea how to prove what I needed</p>

#### [ Mario Carneiro (Apr 26 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713198):
<p>I agree with kenny's quote. I certainly don't remember all the lemmas in mathlib, I just think about the things that should exist and make sure they are actually there. Your question about the union-image-range seems like a step in the right direction, you are getting the sense for what form the lemmas should take, but in that case union-image-range is three things and I like lemmas to talk about two things</p>

#### [ Kevin Buzzard (Apr 26 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713211):
<p>One thing that has helped me terrifically is trying to use Kenny's localization work, because it was written in a completely different style to mathlib. Rather than being written by someone who knew everything and wanted to write an interface, it was written by someone who knew nothing and was learning the material.</p>

#### [ Kevin Buzzard (Apr 26 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713250):
<p>In practice I said to Kenny "can you please give me a function which given a ring R and a multiplicative subset S, returns the ring R[1/S]"</p>

#### [ Mario Carneiro (Apr 26 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713251):
<p>As far as what you should learn by reading printouts, I would say focus on definitions, that's the core around which the lemmas are built</p>

#### [ Kevin Buzzard (Apr 26 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713254):
<p>and he said "sure" and a day or so later I had that ring</p>

#### [ Kevin Buzzard (Apr 26 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713257):
<p>and then I realised I could do nothing with it</p>

#### [ Kevin Buzzard (Apr 26 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713259):
<p>so I kept asking for more and he kept making it (basically by return of post)</p>

#### [ Kevin Buzzard (Apr 26 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713269):
<p>and by the end of it I had a feeling for what it meant to build a mathlib file</p>

#### [ Mario Carneiro (Apr 26 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713313):
<p>writing for others is definitely harder than writing for yourself</p>

#### [ Kevin Buzzard (Apr 26 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713314):
<p>focus on definitions -- thanks for the tip!</p>

#### [ Kevin Buzzard (Apr 26 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713319):
<p>writing for others -- Kenny and I have worked really well as a team, I knew the maths and he did the dirty work</p>

#### [ Mario Carneiro (Apr 26 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713322):
<p>you can look at the lemmas, but your reaction to them should be "oh, well of course"</p>

#### [ Kevin Buzzard (Apr 26 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713381):
<p>and the really cool thing about the localization stuff was once he'd done the really primitive dirty work of proving that some map had some universal property, all the other universal properties which people used in practice could be deduced from Kenny's, and I could write that code myself</p>

#### [ Kevin Buzzard (Apr 26 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713386):
<p>you have probably seen this phenomenon before</p>

#### [ Kevin Buzzard (Apr 26 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713388):
<p>technical code full of [[ ]] and quot.sound or whatever to get stuff off the ground</p>

#### [ Kevin Buzzard (Apr 26 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713389):
<p>but then the proofs get more conceptual after a while</p>

#### [ Mario Carneiro (Apr 26 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713390):
<p>oh yes</p>

#### [ Mario Carneiro (Apr 26 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713430):
<p>I expect that outside the free_group file we will never see <code>list (A x bool)</code></p>

#### [ Kevin Buzzard (Apr 26 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125713434):
<p>it's been a fascinating learning experience.</p>

#### [ Scott Morrison (Apr 26 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125718755):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">D</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">set</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="n">R</span><span class="o">)</span> <span class="o">:</span>
  <span class="err">⋃₀</span><span class="o">(</span><span class="n">D</span> <span class="err">&#39;&#39;</span> <span class="n">set</span><span class="bp">.</span><span class="n">range</span> <span class="n">f</span><span class="o">)</span> <span class="bp">=</span> <span class="err">⋃</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">γ</span><span class="o">),</span> <span class="n">D</span> <span class="o">(</span><span class="n">f</span> <span class="n">i</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">obviously</span>
</pre></div>

#### [ Kevin Buzzard (Apr 26 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125732464):
<p>Well it does look obvious to me.</p>

#### [ Kevin Buzzard (Apr 26 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125732467):
<p>I think we are probably a long way from a tactic which will be able to prove everything which looks obvious to me</p>

#### [ Kevin Buzzard (Apr 26 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125732471):
<p>but I want to start along down that road.</p>

#### [ Patrick Massot (Apr 26 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125732521):
<p>Kevin,  you may have missed the point</p>

#### [ Patrick Massot (Apr 26 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125732527):
<p>Scott <em>does</em> have a tactic called <code>obviously</code> which does the job here</p>

#### [ Patrick Massot (Apr 26 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125732559):
<p><a href="https://github.com/semorrison/lean-tidy/blob/f2303e5376c3520d4432fd073fdb1fd0dfb1f8a8/examples/20180426-kbuzzard.lean" target="_blank" title="https://github.com/semorrison/lean-tidy/blob/f2303e5376c3520d4432fd073fdb1fd0dfb1f8a8/examples/20180426-kbuzzard.lean">https://github.com/semorrison/lean-tidy/blob/f2303e5376c3520d4432fd073fdb1fd0dfb1f8a8/examples/20180426-kbuzzard.lean</a></p>

#### [ Patrick Massot (Apr 26 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125732580):
<p><a href="https://github.com/semorrison/lean-tidy/blob/b8c6661d4ea74d5e8b5df25b2225f4353e5c6bf5/src/tidy/tidy.lean#L136" target="_blank" title="https://github.com/semorrison/lean-tidy/blob/b8c6661d4ea74d5e8b5df25b2225f4353e5c6bf5/src/tidy/tidy.lean#L136">https://github.com/semorrison/lean-tidy/blob/b8c6661d4ea74d5e8b5df25b2225f4353e5c6bf5/src/tidy/tidy.lean#L136</a></p>

#### [ Kevin Buzzard (Apr 26 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125732772):
<p>right</p>

#### [ Kevin Buzzard (Apr 26 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125732776):
<p>but unfortunately I suspect that it will not prove _everything_ which is obvious</p>

#### [ Patrick Massot (Apr 26 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125732826):
<p>He's working on it</p>

#### [ Kevin Buzzard (Apr 26 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125732858):
<p>In particular I bet it won't prove that if there exists a,b,c,d nats with <code>a^2+b^2+c^2+d^2 = 2n</code> then there exists <code>w x y z</code> nats with <code>w^2+x^2+y^2+z^2=2n</code> and <code>w^2+x^2</code> even</p>

#### [ Scott Morrison (Apr 27 2018 at 02:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125750337):
<p>It would be nice to have a better name than <code>obviously</code>. Suggestions welcome. <code>follow_your_nose</code> is a a possibility :-)</p>

#### [ Scott Morrison (Apr 27 2018 at 02:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125750401):
<p>I think your <code>a^2+b^2+c^2+d^2 = 2n</code> is far from "obvious" in this sense. I mean, it's easy, but I don't think "let's think about the parity of the numbers, and the multiplicities of the parities, and solve the problem merely by permuting" counts as "following your nose".</p>

#### [ Simon Hudon (Apr 27 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125750639):
<p><code>left_as_an_exercise_to_the_reader</code></p>

#### [ Simon Hudon (Apr 27 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125750695):
<p>Or <code>beside_the_point</code></p>

#### [ Simon Hudon (Apr 27 2018 at 02:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125750703):
<p>or <code>omitted</code></p>

#### [ Mario Carneiro (Apr 27 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125751085):
<p>I think <code>by beside_the_point</code> is a hilarious substitute for <code>sorry</code></p>

#### [ Mario Carneiro (Apr 27 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125751140):
<p>but none of those suggest that the proof is actually done automatically</p>

#### [ Simon Hudon (Apr 27 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125751148):
<p>How about <code>magic</code> or <code>automagic</code>? :D</p>

#### [ Simon Hudon (Apr 27 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125751215):
<p>I think I might like <code>chocolate</code> even better, since Uncyclopedia mentions it's a respectable proof technique:</p>
<p><a href="http://uncyclopedia.wikia.com/wiki/Proof" target="_blank" title="http://uncyclopedia.wikia.com/wiki/Proof">http://uncyclopedia.wikia.com/wiki/Proof</a></p>

#### [ Mario Carneiro (Apr 27 2018 at 03:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125752084):
<p>Here's a nice proof of that statement: Given any three numbers <code>a b c</code>, I claim that the sum of two of them is even. If <code>a+b</code> is odd, and <code>a+c</code> is odd, and <code>b+c</code> is odd, then <code>(a+b)+(a+c)+(b+c)=2*(a+b+c)</code> is odd, a contradiction.</p>

#### [ Mario Carneiro (Apr 27 2018 at 03:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125752135):
<p>To do this formally you only need to know that every number is even or odd and apply it three times, and then do some simple algebra at the end</p>

#### [ Mario Carneiro (Apr 27 2018 at 03:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/set%20union%20equality/near/125752144):
<p>also you have to know parity rules for adding even and odd</p>


{% endraw %}
