---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/58237equivalencerelationonwrongtype.html
---

## Stream: [general](index.html)
### Topic: [equivalence relation on wrong type](58237equivalencerelationonwrongtype.html)

---


{% raw %}
#### [ Kevin Buzzard (Aug 10 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equivalence%20relation%20on%20wrong%20type/near/131202972):
<p>Luca defined an equivalence relation (homotopy equivalence) on <code>path x y</code>, the paths from x to y in a topological space. He defined <code>loop x</code> to be <code>path x x</code> and then wanted to define <code>pi_1</code> to be the equivalence classes. Lean seemed to obstinately refuse to put the equivalence relation on <code>loop x</code>, insisting it was on <code>path x x</code>. Here's some code that doesn't run, plus some commented out code which fixes the problem.</p>
<div class="codehilite"><pre><span></span><span class="kn">variable</span> <span class="o">{</span><span class="n">α</span>  <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span>

<span class="n">def</span> <span class="n">path</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="n">def</span> <span class="n">comp_of_path</span> <span class="o">{</span><span class="n">x</span> <span class="n">y</span> <span class="n">z</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">:</span> <span class="n">path</span> <span class="n">x</span> <span class="n">y</span> <span class="bp">→</span> <span class="n">path</span> <span class="n">y</span> <span class="n">z</span> <span class="bp">→</span> <span class="n">path</span> <span class="n">x</span> <span class="n">z</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="n">def</span> <span class="n">is_homotopic_to</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">path</span> <span class="n">x</span> <span class="n">y</span> <span class="bp">→</span> <span class="n">path</span> <span class="n">x</span> <span class="n">y</span> <span class="bp">→</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="kn">definition</span> <span class="n">is_equivalence</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">equivalence</span> <span class="o">(</span><span class="n">is_homotopic_to</span> <span class="n">x</span> <span class="n">y</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="kn">definition</span> <span class="n">loop</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span> <span class="n">path</span> <span class="n">x</span> <span class="n">x</span>


<span class="c">/-</span><span class="cm"></span>
<span class="cm">-- This fixes the problem below -- is it safe to have both instances floating around?</span>

<span class="cm">instance setoid_hom_path (x : α)  :</span>
<span class="cm">setoid (path x x) := setoid.mk (is_homotopic_to x x) (is_equivalence x x)</span>

<span class="cm">instance setoid_hom_loop (x : α) :</span>
<span class="cm">setoid (loop x) := by unfold loop; apply_instance</span>
<span class="cm">-/</span>

<span class="kn">instance</span> <span class="n">setoid_hom_loop</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span>  <span class="o">:</span>
<span class="n">setoid</span> <span class="o">(</span><span class="n">loop</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span> <span class="n">setoid</span><span class="bp">.</span><span class="n">mk</span> <span class="o">(</span><span class="n">is_homotopic_to</span> <span class="n">x</span> <span class="n">x</span> <span class="o">:</span> <span class="n">loop</span> <span class="n">x</span> <span class="bp">→</span> <span class="n">loop</span> <span class="n">x</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span>
  <span class="o">(</span><span class="n">is_equivalence</span> <span class="n">x</span> <span class="n">x</span> <span class="o">:</span> <span class="n">equivalence</span> <span class="o">(</span><span class="n">is_homotopic_to</span> <span class="n">x</span> <span class="n">x</span> <span class="o">:</span> <span class="n">loop</span> <span class="n">x</span> <span class="bp">→</span> <span class="n">loop</span> <span class="n">x</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">))</span>

<span class="n">def</span> <span class="n">space_π_1</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">quotient</span> <span class="o">(</span><span class="n">setoid_hom_loop</span> <span class="n">x</span> <span class="o">:</span> <span class="n">setoid</span> <span class="o">(</span><span class="n">loop</span> <span class="n">x</span><span class="o">))</span>

<span class="c1">-- error here</span>
<span class="n">def</span> <span class="n">mul</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span>  <span class="o">:</span>
<span class="n">space_π_1</span> <span class="n">x</span> <span class="bp">→</span> <span class="n">space_π_1</span> <span class="n">x</span> <span class="bp">→</span> <span class="n">space_π_1</span> <span class="n">x</span> <span class="o">:=</span>
<span class="n">quotient</span><span class="bp">.</span><span class="n">lift₂</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">f</span> <span class="n">g</span> <span class="o">:</span> <span class="n">loop</span> <span class="n">x</span><span class="o">,</span> <span class="err">⟦</span><span class="o">((</span><span class="n">comp_of_path</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">loop</span> <span class="n">x</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">loop</span> <span class="n">x</span><span class="o">))</span> <span class="o">:</span> <span class="n">loop</span> <span class="n">x</span><span class="o">)</span><span class="err">⟧</span><span class="o">)</span> <span class="n">sorry</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">-- error is on ⟦ and it&#39;s</span>

<span class="cm">failed to synthesize type class instance for</span>
<span class="cm">α : Type u_1,</span>
<span class="cm">x : α,</span>
<span class="cm">f g : loop x</span>
<span class="cm">⊢ setoid (path x x)</span>
<span class="cm">-/</span>
</pre></div>


<p>I tell Lean so many times that we're talking about <code>loop x</code> but the error seems to indicate that whilst I beg Lean to believe that <code>comp_of_path f g</code> has type <code>loop x</code>, it complains that <code>path x x</code> is not a setoid.</p>
<p>So I found a fix -- instead of making one instance I make two -- I make an instance on <code>path x x</code> and then deduce one on <code>loop x</code>. I am not sure what's going on here and in some sense I'm now not even sure which of the equivalence relations I'm even using. Does it matter that I now have two instances? Why can't I just get away with my uncommented approach?</p>

#### [ Simon Hudon (Aug 10 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equivalence%20relation%20on%20wrong%20type/near/131203664):
<p>I think the problem is that <code>((comp_of_path (f : loop x) (g : loop x)) : loop x)</code> does not have type <code>loop x</code> because <code>comp_of_path</code> does not have type <code>loop x</code>.  The <code>(_ : _)</code> notation does not change the type of the expression, it only provides hints to fill in gaps in the type information.</p>

#### [ Simon Hudon (Aug 10 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equivalence%20relation%20on%20wrong%20type/near/131203723):
<p>The only alternative I can see to the two instances solution is to create a coercion function. I think I like your solution better. You could make it only one instance (on <code>path x x</code> if you made <code>loop</code> reducible.</p>

#### [ Chris Hughes (Aug 10 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equivalence%20relation%20on%20wrong%20type/near/131203885):
<p>This also works </p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">mul</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">:</span> <span class="n">space_π_1</span> <span class="n">x</span> <span class="bp">→</span> <span class="n">space_π_1</span> <span class="n">x</span> <span class="bp">→</span> <span class="n">space_π_1</span> <span class="n">x</span> <span class="o">:=</span>
<span class="n">quotient</span><span class="bp">.</span><span class="n">lift₂</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">f</span> <span class="n">g</span><span class="o">,</span> <span class="k">show</span> <span class="n">space_π_1</span> <span class="n">x</span><span class="o">,</span> <span class="k">from</span> <span class="err">⟦</span><span class="n">comp_of_path</span> <span class="n">f</span> <span class="n">g</span><span class="err">⟧</span><span class="o">)</span>
<span class="n">sorry</span>
</pre></div>

#### [ Simon Hudon (Aug 10 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equivalence%20relation%20on%20wrong%20type/near/131203956):
<p>Ah! That's true! So this probably works as well: </p>
<div class="codehilite"><pre><span></span><span class="o">(</span><span class="err">⟦</span><span class="o">(</span><span class="n">comp_of_path</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">loop</span> <span class="n">x</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">loop</span> <span class="n">x</span><span class="o">))</span><span class="err">⟧</span> <span class="o">:</span> <span class="n">space_π_1</span> <span class="n">x</span><span class="o">)</span>
</pre></div>

#### [ Chris Hughes (Aug 10 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equivalence%20relation%20on%20wrong%20type/near/131204005):
<p>yes it does, much more sensible</p>

#### [ Kevin Buzzard (Aug 10 2018 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equivalence%20relation%20on%20wrong%20type/near/131230021):
<p>But Luca would then have to write that all through his code, which kind of stinks -- I wanted him to use type class inference precisely because it was supposed to be making his life easier.</p>


{% endraw %}
