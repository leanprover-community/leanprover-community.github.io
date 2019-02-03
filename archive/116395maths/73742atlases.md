---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/73742atlases.html
---

## Stream: [maths](index.html)
### Topic: [atlases](73742atlases.html)

---


{% raw %}
#### [ Patrick Massot (Jun 26 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128648910):
<p>I decided to try to move forward in my differential topology project without waiting for experts to sort out the module type class issues. So let's say I'm ready to sorry the definition of a diffeomorphism between two open subsets of R^n. Then the definition to formalize is <a href="https://en.wikipedia.org/wiki/Differentiable_manifold#Atlases" target="_blank" title="https://en.wikipedia.org/wiki/Differentiable_manifold#Atlases">https://en.wikipedia.org/wiki/Differentiable_manifold#Atlases</a> I have no idea how to attack this coercion mess. I'd like to understand the definition of the transitions maps, and understand they are maps between open subsets of R^n</p>

#### [ Patrick Massot (Jun 26 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128648973):
<p>Even restricting a function to a subset is non-trivial in Lean</p>

#### [ Patrick Massot (Jun 26 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128649000):
<p>and here I need that the restriction of a homeo to a subset is a homeo onto its image</p>

#### [ Johan Commelin (Jun 26 2018 at 13:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128651578):
<blockquote>
<p>Even restricting a function to a subset is non-trivial in Lean</p>
</blockquote>
<p>Can't you compose with <code>subtype.val</code>? And then you need that <code>subtype.val</code> is an immersion, and C^k for every value of k.</p>

#### [ Patrick Massot (Jun 26 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128653776):
<p>I need to invert the restriction of an <code>equiv</code> to some subset</p>

#### [ Chris Hughes (Jun 26 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128656888):
<p>Is this any use?</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">topology</span><span class="bp">.</span><span class="n">continuity</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">topological_space</span> <span class="n">β</span><span class="o">]</span>
  <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="err">≃</span> <span class="n">β</span> <span class="bp">//</span> <span class="n">continuous</span> <span class="n">f</span><span class="o">})</span>

<span class="n">def</span> <span class="n">restriction</span> <span class="o">:</span> <span class="o">{</span><span class="n">g</span> <span class="o">:</span> <span class="n">A</span> <span class="err">≃</span> <span class="n">f</span> <span class="err">&#39;&#39;</span> <span class="n">A</span> <span class="bp">//</span> <span class="n">continuous</span> <span class="n">g</span><span class="o">}</span> <span class="o">:=</span>
<span class="bp">⟨</span><span class="o">{</span>  <span class="n">to_fun</span> <span class="o">:=</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">f</span> <span class="n">a</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">a</span><span class="o">,</span> <span class="n">a</span><span class="bp">.</span><span class="mi">2</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span><span class="o">),</span>
    <span class="n">inv_fun</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">b</span><span class="o">,</span> <span class="bp">⟨</span><span class="o">(</span><span class="n">equiv</span><span class="bp">.</span><span class="n">symm</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="err">≃</span> <span class="n">β</span><span class="o">))</span> <span class="n">b</span><span class="o">,</span> <span class="k">let</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span> <span class="n">ha₁</span><span class="o">,</span> <span class="o">(</span><span class="n">ha₂</span> <span class="o">:</span> <span class="n">f</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">b</span><span class="o">)</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">b</span><span class="bp">.</span><span class="mi">2</span> <span class="k">in</span>
      <span class="k">calc</span> <span class="bp">_</span> <span class="bp">=</span> <span class="n">a</span> <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="err">←</span> <span class="n">ha₂</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">inverse_apply_apply</span> <span class="bp">_</span> <span class="bp">_</span>
      <span class="bp">...</span> <span class="err">∈</span> <span class="n">A</span> <span class="o">:</span> <span class="n">ha₁</span><span class="bp">⟩</span><span class="o">,</span>
    <span class="n">left_inv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">⟨_</span><span class="o">,</span> <span class="bp">_⟩</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="o">(</span><span class="n">f</span><span class="bp">.</span><span class="mi">1</span><span class="bp">.</span><span class="mi">3</span> <span class="bp">_</span><span class="o">),</span>
    <span class="n">right_inv</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">⟨_</span><span class="o">,</span> <span class="bp">_⟩</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="o">(</span><span class="n">f</span><span class="bp">.</span><span class="mi">1</span><span class="bp">.</span><span class="mi">4</span> <span class="bp">_</span><span class="o">)</span>  <span class="o">},</span>
  <span class="n">continuous_subtype_mk</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">x</span><span class="bp">.</span><span class="mi">2</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span><span class="o">)</span>
  <span class="o">(</span><span class="n">continuous</span><span class="bp">.</span><span class="n">comp</span> <span class="n">continuous_subtype_val</span> <span class="n">f</span><span class="bp">.</span><span class="mi">2</span><span class="o">)</span><span class="bp">⟩</span>
</pre></div>

#### [ Patrick Massot (Jun 26 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128656981):
<p>Maybe</p>

#### [ Patrick Massot (Jun 26 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128656994):
<p>I'm exploring a lot of ways to try to make Lean understanding this definition or variations on this definition</p>

#### [ Patrick Massot (Jun 26 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128657042):
<p>I already knew there were plenty of variations on the definition of manifolds but I'm discovering many more</p>

#### [ Patrick Massot (Jun 26 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128657449):
<p>A variation on this kind of effort could be to adapt</p>
<div class="codehilite"><pre><span></span><span class="kn">protected</span> <span class="n">noncomputable</span> <span class="n">def</span> <span class="n">image</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">injective</span> <span class="n">f</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">s</span> <span class="err">≃</span> <span class="o">(</span><span class="n">f</span> <span class="err">&#39;&#39;</span> <span class="n">s</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">h</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">f</span> <span class="n">x</span><span class="o">,</span> <span class="n">mem_image_of_mem</span> <span class="bp">_</span> <span class="n">h</span><span class="bp">⟩</span><span class="o">,</span>
 <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">y</span><span class="o">,</span> <span class="n">h</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">classical</span><span class="bp">.</span><span class="n">some</span> <span class="n">h</span><span class="o">,</span> <span class="o">(</span><span class="n">classical</span><span class="bp">.</span><span class="n">some_spec</span> <span class="n">h</span><span class="o">)</span><span class="bp">.</span><span class="mi">1</span><span class="bp">⟩</span><span class="o">,</span>
 <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">h</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="o">(</span><span class="n">H</span> <span class="o">(</span><span class="n">classical</span><span class="bp">.</span><span class="n">some_spec</span> <span class="o">(</span><span class="n">mem_image_of_mem</span> <span class="n">f</span> <span class="n">h</span><span class="o">))</span><span class="bp">.</span><span class="mi">2</span><span class="o">),</span>
 <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">y</span><span class="o">,</span> <span class="n">h</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="o">(</span><span class="n">classical</span><span class="bp">.</span><span class="n">some_spec</span> <span class="n">h</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span><span class="bp">⟩</span>
</pre></div>


<p>from <code>equiv.lean</code> to a version where <code>H</code> would be <code>inj_on f s</code>, which seems like a much more relevant hypothesis anyway</p>

#### [ Patrick Massot (Jun 26 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128657525):
<p>But maybe I don't care. I don't know. There are so many ways to try to setup this thing...</p>

#### [ Chris Hughes (Jun 26 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128657624):
<p>You're losing computability with that def, though I'm not sure you care.</p>

#### [ Patrick Massot (Jun 26 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128657642):
<p>Ah, at least there is something I know: I don't care about computability.</p>

#### [ Patrick Massot (Jun 26 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128657660):
<p>Chris, this remark worries me. I think you may be spending too much time with Kenny.</p>

#### [ Patrick Massot (Jun 26 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128657843):
<p>I'm completely confused about <a href="https://github.com/leanprover/mathlib/blob/master/data/equiv.lean#L527" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/data/equiv.lean#L527">https://github.com/leanprover/mathlib/blob/master/data/equiv.lean#L527</a> How do you access this definition? It seems to be in namespace <code>set</code> but is obviously not the same as <code>set.range</code></p>

#### [ Kenny Lau (Jun 26 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128657903):
<p>the <code>equiv</code> namespace never ended :)</p>

#### [ Kenny Lau (Jun 26 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128657904):
<p><code>equiv.set.range</code></p>

#### [ Patrick Massot (Jun 26 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128657930):
<p>Oh, that's nasty</p>

#### [ Patrick Massot (Jun 26 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128657932):
<p>thanks Kenny</p>

#### [ Patrick Massot (Jun 26 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128657987):
<p>hum, I hear I urgently need to go to the main lecture hall in IHES</p>

#### [ Patrick Massot (Jun 26 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128657994):
<p>it seems the match started already</p>

#### [ Sebastien Gouezel (Jun 26 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128677951):
<p>Are you planning to implement only C^\infty manifolds over the reals, or manifolds with different classes of smoothness (say C^0, or C^1, or C^k, or analytic, or PL, or whatever you like, over R or C)? It seems to me that it would be better to implement various classes of smoothness in the same framework. For instance, one could axiomatize what one needs to have a "smoothness class" (families of maps which are all homeos between open subsets of a given topological space, stable under restriction and composition and inverses), and then one could define a manifold with respect to this smoothness class. Two advantages of this approach: <br>
- this is more general, and useful<br>
- you don't need to define R^n and smooth maps to start working with this definition (but of course, you will have no example at the beginning, except maybe for C^0 manifolds which would be the first example to work out)<br>
Any thoughts?</p>

#### [ Patrick Massot (Jun 26 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128678095):
<p>Unfortunately I'm pretty far from being able to do that. The trouble is partially defined functions are everywhere. A chart is defined on part of the manifold, a transition function is defined on the image of part of the domain of a chart. I really struggle with this. How is this handled in Isabelle? Do you have smooth functions defined on open subsets of R^n and a convenient way to restrict a smooth function to an open subset?</p>

#### [ Patrick Massot (Jun 26 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128678162):
<p>But, to answer your question, I was indeed hoping to implement manifolds modeled on any pseudo-group</p>

#### [ Patrick Massot (Jun 26 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128678223):
<p>I also find it very interesting to see that, once again, the only source which seems to be suitable for formalization is Bourbaki.</p>

#### [ Sebastien Gouezel (Jun 26 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128678435):
<p>In Isabelle, I would model a smoothness class by a set of pairs <code>(U, f)</code> where <code>U</code> is an open subset of <code>R^n</code> and <code>f</code> is a map from <code>R^n</code>to itself such that its restriction to <code>U</code> is a homeomorphism. So, I would have a predicate <code>homeomorphism_on U f</code> saying that <code>f</code> is a homeomorphism on <code>U</code>, together with basic properties of homeomorphisms (say, if <code>f</code> is a homeomorphism on <code>U</code> and <code>g</code>is a homeomorphism on <code>V</code> and <code>f(U) \subseteq V</code>, then <code>g o f</code> is a homeomorphism on <code>U</code>). Then you don't ever need to restrict your functions to subsets, and you avoid a lot of trouble.</p>

#### [ Sebastien Gouezel (Jun 26 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128678493):
<p>and the smoothness on open subsets is also defined for total functions, using a predicate as above.</p>

#### [ Patrick Massot (Jun 26 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128678843):
<p>I thought about trying to get functions defined everywhere and asking for injectivity and smoothness only on subsets. But I fear it will be a nightmare when trying to prove things because every function would be defined by <code>lambda x, if x in U then real_thing x else 42</code>.</p>

#### [ Patrick Massot (Jun 26 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128678861):
<p>And also I don't like this has nothing to do with math</p>

#### [ Patrick Massot (Jun 26 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128678876):
<p>It's purely an artefact of the type theoretic foundations</p>

#### [ Sebastien Gouezel (Jun 26 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128679380):
<p>You would never have any <code>if</code> in your definitions. The composition of two homeomorphisms <code>f</code>on <code>U</code> and <code>g</code> on <code>V</code> is just <code>g o f</code> on <code>U</code> (and it only makes sense if <code>f(U) \subseteq V</code>, but this is also the case with the true definition). The restriction of a homeomorphism <code>f</code>on <code>U</code> to a smaller subset <code>U'</code> is still <code>f </code>. And so on. This may seem surprising at first sight, but in fact it is not so surprising: if you only do meaningful constructions, then the values of your function outside of its "domain of definition" should never play any role, so what happens there is never relevant, and it can behave in the way it wants.</p>

#### [ Patrick Massot (Jun 26 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128679475):
<p>I know it's the theory, I've seen it countless times with 0/0 and other crazy stuff. But you still need to define an arbitrary crazy value. For 0/0 you can choose 0, fine. What if the target is a manifold?</p>

#### [ Sebastien Gouezel (Jun 26 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128679491):
<p>It is just like the fact that the division is total on real numbers: surprising and annoying at the beginning, and then when you get used to it you realize you don't care at all what it does at zero because you're not stupid and you never apply it at <code>0</code> (and of course you always have to check that the denominator is nonzero -- here in the same way you would always have to check that the points you apply your function to are in the "domain of definition")</p>

#### [ Patrick Massot (Jun 26 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128679603):
<p>Do you have the same crazyness in Isabelle then?</p>

#### [ Sebastien Gouezel (Jun 26 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128679604):
<p>At least for the definition of a manifold in terms of an atlas of compatible charts, you would never need to specify a value, it is just some axioms you want to satisfy.<br>
Probably, when you define a manifold structure on some object, yes, you will have to make some arbitrary and irrelevant choice at some point. But that would be very rare, I guess.</p>

#### [ Patrick Massot (Jun 26 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128679660):
<p>Yes, I want to define actual manifolds, like smooth affine varieties in R^n (say S^{n-1})</p>

#### [ Sebastien Gouezel (Jun 26 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128679662):
<p>The crazyness of what? Every function is total, yes. And it turns out to be a non-issue once you're used to it. (Takes some time to get used to it :)</p>

#### [ Patrick Massot (Jun 26 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128679687):
<p>thanks</p>

#### [ Sebastien Gouezel (Jun 26 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128679765):
<p>Think of S^{n-1}. Take the two natural stereographic charts: they are defined on the whole of R^{n-1}, so no issue of arbitrary choice when you define them. And then you just have to check the axiom that the composition of one chart and the inverse of the other one, restricted to the good sets, are smooth. No arbitrary choice again.</p>

#### [ Sebastien Gouezel (Jun 26 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128679794):
<p>Same think if you define Grassmannians, say: the natural local charts using linear maps are defined on the whole R^k. No arbitrary choice again.</p>

#### [ Patrick Massot (Jun 26 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128679801):
<p>This is not the definition I want to use. This one is only an exercise in understanding the internal plumbing that is the precise definition of a manifold. I want S^{n-1} defined by |x|² = 1</p>

#### [ Patrick Massot (Jun 26 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128679809):
<p>I want submanifolds of manifolds to be manifolds</p>

#### [ Patrick Massot (Jun 26 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128679869):
<p>But I'll try this total function road</p>

#### [ Sebastien Gouezel (Jun 26 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128679884):
<p>Then you want to use two theorems, that the preimage of a regular value by a map is a submanifold, and that a submanifold is a manifold. Again no choice :)</p>

#### [ Patrick Massot (Jun 26 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128679902):
<p>Are you sure the second one will require no choice? Maybe.</p>

#### [ Sebastien Gouezel (Jun 26 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128679961):
<p>The way answers are intermingled is really strange in such a chat. Anyway, to prove that a submanifold is a manifold, essentially you will first straighten your submanifold, and then restrict your charts to the submanifold. Then there should be no <code>if</code>in the involved arguments.</p>

#### [ Patrick Massot (Jun 26 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128680079):
<p>I'll try all this tomorrow (what I tried today is on <a href="https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/manifold.lean" target="_blank" title="https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/manifold.lean">https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/manifold.lean</a> if you are curious (there may be stupid things there, I switched gears so many times...)</p>

#### [ Patrick Massot (Jun 26 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128680108):
<p>thank you very much for this conversation</p>

#### [ Patrick Massot (Jun 26 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128680117):
<p>good night!</p>

#### [ Patrick Massot (Jun 27 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128716143):
<p>I try to get used to totalization of functions. What do people think about:</p>
<div class="codehilite"><pre><span></span><span class="n">universes</span> <span class="n">u</span> <span class="n">v</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">inhabited</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span>

<span class="n">def</span> <span class="n">inverse_on</span>  <span class="o">{</span><span class="n">U</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">}</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">inj_on</span> <span class="n">f</span> <span class="n">U</span><span class="o">)</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">α</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">b</span><span class="o">,</span> <span class="k">if</span> <span class="n">h</span> <span class="o">:</span> <span class="n">b</span> <span class="err">∈</span> <span class="n">f</span> <span class="err">&#39;&#39;</span> <span class="n">U</span> <span class="k">then</span> <span class="n">classical</span><span class="bp">.</span><span class="n">some</span> <span class="n">h</span> <span class="k">else</span> <span class="n">default</span> <span class="n">α</span>

<span class="kn">lemma</span> <span class="n">inverse_on_spec</span> <span class="o">{</span><span class="n">U</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">}</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">inj_on</span> <span class="n">f</span> <span class="n">U</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">inv_on</span> <span class="o">(</span><span class="n">inverse_on</span> <span class="n">H</span><span class="o">)</span> <span class="n">f</span> <span class="n">U</span> <span class="o">(</span><span class="n">f</span> <span class="err">&#39;&#39;</span> <span class="n">U</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">split</span> <span class="bp">;</span> <span class="n">intros</span> <span class="n">x</span> <span class="n">h</span><span class="o">,</span>
  <span class="o">{</span> <span class="k">have</span> <span class="n">H&#39;</span> <span class="o">:=</span> <span class="n">mem_image_of_mem</span> <span class="n">f</span> <span class="n">h</span><span class="o">,</span>
    <span class="n">cases</span> <span class="n">classical</span><span class="bp">.</span><span class="n">some_spec</span> <span class="n">H&#39;</span> <span class="k">with</span> <span class="n">h1</span> <span class="n">h2</span><span class="o">,</span>
    <span class="n">simp</span> <span class="o">[</span><span class="n">inverse_on</span><span class="o">,</span> <span class="n">H&#39;</span><span class="o">,</span> <span class="n">H</span> <span class="n">h1</span> <span class="n">h</span> <span class="n">h2</span><span class="o">]</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">cases</span> <span class="n">classical</span><span class="bp">.</span><span class="n">some_spec</span> <span class="n">h</span> <span class="k">with</span> <span class="n">h1</span> <span class="n">h2</span><span class="o">,</span>
    <span class="n">simpa</span> <span class="o">[</span><span class="n">inverse_on</span><span class="o">,</span> <span class="n">h</span><span class="o">]</span> <span class="kn">using</span> <span class="n">h2</span> <span class="o">}</span>
<span class="kn">end</span>
</pre></div>


<p>Is it something I should be doing?</p>

#### [ Reid Barton (Jun 27 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128717488):
<p>I don't see why it should be necessary to work with total functions here, and this approach has its own disadvantages. I think the root problem is that you currently lack a sufficient Lean vocabulary to work with partial functions and partial bijections</p>

#### [ Patrick Massot (Jun 27 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128717549):
<p>What would be that vocabulary?</p>

#### [ Reid Barton (Jun 27 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128717677):
<p>For example, looking at the definition of pseudogroup, you could state most of these axioms immediately given:</p>
<ul>
<li>A type <code>pequiv a b</code> representing a bijection between a subset of the type <code>a</code> and a subset of the type <code>b</code>. Note that the subsets of <code>a</code> and <code>b</code> are not indices of the type <code>pequiv a b</code>.</li>
<li>A "restricted composition" operation <code>pequiv a b \to pequiv b c \to pequiv a c</code>.</li>
<li>A "restricted identity" of type <code>pequiv a a</code> for each <code>s : set a</code>, which is the identity bijection between <code>s</code> and itself. From this and the previous one, you can implement restriction of a <code>pequiv</code> to a subset of the domain or codomain.</li>
<li>A way to extract from a <code>pequiv a b</code> the domain <code>s</code> as a <code>set a</code>, and a function <code>subtype s \to b</code>, which you can then check for continuity or smoothness or whatever.</li>
</ul>

#### [ Patrick Massot (Jun 27 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128717764):
<p>What would be a "restricted composition" in a world where all functions are total? That's precisely the trouble.</p>

#### [ Reid Barton (Jun 27 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128717766):
<p>Also I forgot the "symmetry" <code>pequiv a b \to pequiv b a</code>.</p>

#### [ Reid Barton (Jun 27 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128717822):
<p>Well then you are asking about how to implement this interface, right?</p>

#### [ Patrick Massot (Jun 27 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128717830):
<p>Everything is about implementation in this discussion, I already know what is a manifold.</p>

#### [ Reid Barton (Jun 27 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128717834):
<p>Or are you asking about the meaning of the operation? It's just the one which, given partial bijections f and g, is defined on x when f(x) is defined and g(f(x)) is also defined</p>

#### [ Patrick Massot (Jun 27 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128717858):
<p>Indeed having the subsets as fields instead of parameters may be enough to do the trick</p>

#### [ Patrick Massot (Jun 27 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128717952):
<p>I guess this is closer in spirit to the <code>option a</code> type than totalizing functions</p>

#### [ Reid Barton (Jun 27 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128718006):
<p>You might also want to check out <code>roption</code> and the <code>data.pfun</code> module</p>

#### [ Reid Barton (Jun 27 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128718021):
<p>But the main point is that for a computer, everything is hard, even these utterly trivial notions like "bijection between a subset of <code>a</code> and a subset of <code>b</code>".</p>

#### [ Reid Barton (Jun 27 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128718077):
<p>It helps to decompose the problem into pieces, so you are not thinking about manifolds when trying to define the composition of partial bijections. Of course this concept is not foreign to mathematicians, but here the pieces are much smaller than we are used to.</p>

#### [ Patrick Massot (Jun 27 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128718180):
<p>Yes I noticed all this (but noticing doesn't make it easy to use Lean)</p>

#### [ Reid Barton (Jun 27 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128718181):
<p>Once you have settled on the right interface for <code>pequiv</code>, the choice of implementation is not so important</p>

#### [ Patrick Massot (Jun 27 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128718183):
<p>I'll look at roption and pfun</p>

#### [ Reid Barton (Jun 27 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128718297):
<p>Something that may not be obvious from the pfun module is that because <code>roption</code> is a monad, you get a composition operation <code>(a -&gt; roption b) -&gt; (b -&gt; roption c) -&gt; (a -&gt; roption c)</code> for free</p>

#### [ Reid Barton (Jun 27 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128718526):
<p>Apparently it doesn't really have a name in Lean aside from <code> &gt;=&gt; </code></p>

#### [ Patrick Massot (Jun 27 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128718545):
<p>I hope I'll be able to avoid this kind of notations...</p>

#### [ Reid Barton (Jun 27 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128718555):
<p>Again, only a question of implementation</p>

#### [ Reid Barton (Jun 27 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128718559):
<p>Of course for <code>pequiv</code>, you can choose whichever notation you like</p>

#### [ Reid Barton (Jun 27 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128718733):
<p>By the way, even though you don't care about constructiveness, I think things will be easier in the long run if you keep the maps in both directions as data in a bijection</p>

#### [ Patrick Massot (Jun 27 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128718770):
<p>as in using <code>equiv</code> rather than <code>bijective</code> you mean?</p>

#### [ Reid Barton (Jun 27 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128718777):
<p>Otherwise, when defining the canonical manifold structure on R^n for example, I think the transition maps will turn out to be something like <code>lam x, classical.choice (\ex y, y = x)</code> rather than <code>lam x, x</code></p>

#### [ Reid Barton (Jun 27 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128718779):
<p>Exactly</p>

#### [ Sebastien Gouezel (Jun 27 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128719255):
<p>What about defining rather </p>
<div class="codehilite"><pre><span></span>def inverse_on  (U : set α) (f : α → β) : β → α :=
λ b, if h : b ∈ f &#39;&#39; U then classical.some h else default α
</pre></div>


<p>and having the injectivity as an assumption in your lemma <code>inverse_on_spec</code>. So that <code>inverse_on</code> is really taking as argument a function, and not a proof: formulas with <code>inverse_on U f</code> should be much more understandable than <code>inverse_on H</code> where you don't remember what <code>H</code> is. (This is really an implementation detail, everything is clearly equivalent, but still aiming at readability is always good!)</p>

#### [ Reid Barton (Jun 27 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128719339):
<p>If you keep track of both directions, then you can always produce the inverse using <code>bijective</code> and "unique choice" whenever it would be less convenient to provide it manually. But if you throw away the inverse direction and only keep the <code>Prop</code> of bijectivity, you can only recover the inverse function up to propositional equality. Then you may be faced with proving some equality these reconstructed inverses, where if you had kept the original inverses the proof would just be <code>rfl</code></p>

#### [ Patrick Massot (Jun 27 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128719435):
<p>Thanks to both of you, this is all very interesting. I'll keep on working on the totalization path until I can define manifolds modulo the definition of smooth maps (it looks like it will work). But then I'll try to redo everything using the <code>pequiv</code> idea, and compare.</p>

#### [ Patrick Massot (Jun 27 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128719536):
<p>The definition of <code>inverse_on</code> without injectivity assumption really looks weird</p>

#### [ Patrick Massot (Jun 27 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128719552):
<p>I don't care at all about constructivism, and I don't mind using the axiom of choice. But this really doesn't feel like defining a function.</p>

#### [ Sebastien Gouezel (Jun 27 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128719704):
<p>I like my functions to be total :) So <code>inverse_on</code> is also total with this definition. <br>
More seriously, in some settings, just taking one (any) preimage will make sense. For instance if you are working in a coarse geometry setting and you know that the preimages of any point have bounded diameter. This is the way one inverts quasi-isometries.</p>

#### [ Kevin Buzzard (Jun 27 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128719719):
<p>The axiom of choice is a pain to use in practice, because you need to keep track of random proof terms. I had two types X and Y in bijection recently, with a computable map X -&gt; Y and a noncomptable map Y -&gt; X, and after failing to construct something of type <code>equiv X Y</code> directly because of proof terms giving me problems I just proved X-&gt;Y was a bijection and then invoked <code>equiv.of_bijection</code>. Working with the axiom of choice can be a pain. Basically if you invoke it twice then there's no guaranteeing you got the same answer twice, so you can only invoke it once and then you have to keep a very careful track of where you invoked it and what you got.</p>

#### [ Sebastien Gouezel (Jun 27 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128719812):
<p>The idea would be that you never ever come back to the definition of inverse_on, but only use the two lemmas saying that <code>f (inverse_on U f y) = y</code> if <code>y \in f''(U)</code>, and that <code>inverse_on U f( f x) = x</code> if <code>x \in U</code> and <code>f</code> is injective on <code>U</code>.</p>

#### [ Patrick Massot (Jun 27 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128719876):
<p>My <code>inverse_on_spec</code> is the conjunction of these two statements</p>

#### [ Sebastien Gouezel (Jun 27 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128719883):
<p>Yes, but for one of them you don't need the injectivity.</p>

#### [ Patrick Massot (Jun 27 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128719894):
<p>Sure. But I needed injectivity in the definition for psychological confort.</p>

#### [ Patrick Massot (Jun 27 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128719895):
<p>:)</p>

#### [ Sebastien Gouezel (Jun 27 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128719914):
<p>Go for the minimal assumptions. It will simplify your proofs if there are less assumptions to check!</p>

#### [ Patrick Massot (Jun 27 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128722751):
<p>I noticed Mario sometimes goes for biconditional statements in this situation. It indeed feels weird.</p>

#### [ Patrick Massot (Jun 27 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128722771):
<p>I will need a more precise stub for smoothness if I want to prove that equivalence of atlases is an equivalence relation...</p>

#### [ Johannes Hölzl (Jul 02 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128951168):
<p><code>inverse_on</code> is <code>inv_fun_on</code> in <code>logic/function.lean</code>. For surjective functions there is also <code>surj_inv</code> (there the range doesn't need to be inhabited).</p>

#### [ Patrick Massot (Jul 02 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128954811):
<p>Thanks! I completely failed to see that file. I still don't understand the criterion separating stuff in <code>data/set/function.lean</code> and <code>logic/function.lean</code>.</p>

#### [ Mario Carneiro (Jul 02 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128954993):
<p>I would say that the difference is the use of sets</p>

#### [ Patrick Massot (Jul 02 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128955000):
<p>There are sets everywhere in both</p>

#### [ Mario Carneiro (Jul 02 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128955013):
<p><code>logic.function</code> does not import <code>data.set.basic</code></p>

#### [ Mario Carneiro (Jul 02 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128955023):
<p>so the only set stuff is what is available in core</p>

#### [ Patrick Massot (Jul 02 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128955079):
<p>Would putting everything in the same file create dependency issues?</p>

#### [ Mario Carneiro (Jul 02 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128955081):
<p>yes</p>

#### [ Mario Carneiro (Jul 02 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128955093):
<p>although it is likely that <code>inv_fun_on</code> can be moved to set safely</p>

#### [ Mario Carneiro (Jul 02 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/atlases/near/128955147):
<p>I like to think of the <code>logic</code> directory as covering more or less the "pure type theory" part of lean, just functions and pis and such</p>


{% endraw %}
