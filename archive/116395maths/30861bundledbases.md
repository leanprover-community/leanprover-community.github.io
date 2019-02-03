---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/30861bundledbases.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [bundled bases](https://leanprover-community.github.io/archive/116395maths/30861bundledbases.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Oct 17 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/135955551):
<p>I pushed the results of yesterdays painful efforts to <a href="https://github.com/leanprover-community/mathlib/blob/open_set/category_theory/examples/topological_spaces.lean" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/open_set/category_theory/examples/topological_spaces.lean">https://github.com/leanprover-community/mathlib/blob/open_set/category_theory/examples/topological_spaces.lean</a>. This wouldn't have been possible without the great help of <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> <br>
I guess that some of the proofs need to be minimised. I obfuscated them as much as possible, and don't see how to squeeze out more. If someone wants to take a look, please go ahead.<br>
The motivation for these changes is that we want to be able to talk about "sheaves on a basis".</p>

#### [ Mario Carneiro (Oct 17 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/135990528):
<p>I think <code>open_set</code> should be unbundled in the topology argument</p>

#### [ Johan Commelin (Oct 17 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/135991087):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span>  What do you mean with that?</p>

#### [ Johan Commelin (Oct 17 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/135991108):
<p>You want an unbundled version in <code>analysis/topology/blah.lean</code>?</p>

#### [ Johan Commelin (Oct 17 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/135991165):
<p>I think we also want the bundled version. But maybe I should first prove things with it, to show that it is useful.</p>

#### [ Mario Carneiro (Oct 17 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/135994508):
<p>I mean that for a fixed topological space, <code>@open_set X top_X</code> is a category</p>

#### [ Mario Carneiro (Oct 17 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/135994589):
<p>On top of that there is an <code>open_set</code> <em>functor</em>  from <code>Top</code> to <code>Type</code>, but that needs its own definition anyway</p>

#### [ Mario Carneiro (Oct 17 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/135994650):
<p>er, I think I mean lattice not category, I see you haven't given it a category structure</p>

#### [ Mario Carneiro (Oct 17 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/135994706):
<p>so in that case it could indeed move to <code>analysis/topology</code>. I would suggest the name <code>opens</code> for this lattice</p>

#### [ Johan Commelin (Oct 17 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/135994710):
<p>It is... every preorder is a category (in mathlib)</p>

#### [ Mario Carneiro (Oct 17 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/135994724):
<p>right, but you haven't made any explicit reference to categories in the definition</p>

#### [ Johan Commelin (Oct 17 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/135994811):
<p>Hmmm... I don't follow exactly. Do you want to change the definition of <code>open_set</code>? Or do you want to define <code>opens</code> and if so, what should it be?</p>

#### [ Johan Commelin (Oct 17 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/135994954):
<p>Also, should we change the definition of <code>open_set X</code> to <code>open_set X := X.str</code>? That is equivalent, and might simplify a lot of the stuff that follows...</p>

#### [ Mario Carneiro (Oct 17 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/135997479):
<p><code>def opens (X : Type*) [topological_space X] : Type* := {s // is_open s}</code></p>

#### [ Mario Carneiro (Oct 17 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/135997602):
<p>I don't understand the idea behind the <code>X.str</code> definition. The point is that <code>open_set X</code> is a type, not a structure</p>

#### [ Mario Carneiro (Oct 17 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/135997659):
<p>my proposal is <code>opens</code> as above, and <code>category.opens : Top ⥤ Cat</code> (or some other prefix?) has that as its object part</p>

#### [ Mario Carneiro (Oct 17 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/135997756):
<p>although maybe we need more functors than just that because it's properly a 2-functor</p>

#### [ Johan Commelin (Oct 18 2018 at 05:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136018803):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> So <code>open_set</code> should go asway, and be replaced by <code>opens</code>?<br>
What is wrong with:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">opens</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">[</span><span class="n">t</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">X</span><span class="o">]</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span> <span class="o">:=</span> <span class="n">subtype</span> <span class="n">t</span><span class="bp">.</span><span class="n">is_open</span>
</pre></div>


<p>That is what I meant with the <code>X.str</code> definition.</p>

#### [ Mario Carneiro (Oct 18 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136018818):
<p>That doesn't typecheck?</p>

#### [ Johan Commelin (Oct 18 2018 at 06:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136018953):
<p>Ok, fair enough. I meant <code>subtype t.is_open</code>. I fixed this above.</p>

#### [ Mario Carneiro (Oct 18 2018 at 06:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136018996):
<p>that's the same as I wrote modulo eta expansion</p>

#### [ Johan Commelin (Oct 18 2018 at 06:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136018999):
<p>Right. So it doesn't matter.</p>

#### [ Mario Carneiro (Oct 18 2018 at 06:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136019003):
<p>well, you are also using a different <code>is_open</code></p>

#### [ Johan Commelin (Oct 18 2018 at 06:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136019018):
<p>Aah, and maybe mine is more painful?</p>

#### [ Mario Carneiro (Oct 18 2018 at 06:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136019025):
<p>there are fewer lemmas about it</p>

#### [ Johan Commelin (Oct 18 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136023764):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Do you mean you would like to see something like this in <code>analysis/topology/topological_space.lean</code>?</p>
<div class="codehilite"><pre><span></span><span class="kn">section</span> <span class="n">opens</span>
<span class="kn">variable</span> <span class="o">(</span><span class="n">α</span><span class="o">)</span>

<span class="n">def</span> <span class="n">opens</span> <span class="o">:=</span> <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span> <span class="bp">//</span> <span class="bp">_</span><span class="n">root_</span><span class="bp">.</span><span class="n">is_open</span> <span class="n">s</span><span class="o">}</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span><span class="o">}</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">has_coe</span> <span class="o">(</span><span class="n">opens</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span> <span class="o">{</span> <span class="n">coe</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">U</span><span class="o">,</span> <span class="n">U</span><span class="bp">.</span><span class="n">val</span> <span class="o">}</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">has_subset</span> <span class="o">(</span><span class="n">opens</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">subset</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">U</span> <span class="n">V</span><span class="o">,</span> <span class="n">U</span><span class="bp">.</span><span class="n">val</span> <span class="err">⊆</span> <span class="n">V</span><span class="bp">.</span><span class="n">val</span> <span class="o">}</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">has_mem</span> <span class="n">α</span> <span class="o">(</span><span class="n">opens</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">mem</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">a</span> <span class="n">U</span><span class="o">,</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">U</span><span class="bp">.</span><span class="n">val</span> <span class="o">}</span>

<span class="bp">@</span><span class="o">[</span><span class="n">extensionality</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">ext</span> <span class="o">{</span><span class="n">U</span> <span class="n">V</span> <span class="o">:</span> <span class="n">opens</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">U</span><span class="bp">.</span><span class="n">val</span> <span class="bp">=</span> <span class="n">V</span><span class="bp">.</span><span class="n">val</span><span class="o">)</span> <span class="o">:</span> <span class="n">U</span> <span class="bp">=</span> <span class="n">V</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">cases</span> <span class="n">U</span><span class="bp">;</span> <span class="n">cases</span> <span class="n">V</span><span class="bp">;</span> <span class="n">congr</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">h</span>

<span class="kn">instance</span> <span class="n">topological_space</span><span class="bp">.</span><span class="n">opens</span><span class="bp">.</span><span class="n">partial_order</span> <span class="o">:</span> <span class="n">partial_order</span> <span class="o">(</span><span class="n">opens</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">refine</span> <span class="o">{</span> <span class="n">le</span> <span class="o">:=</span> <span class="o">(</span><span class="err">⊆</span><span class="o">),</span> <span class="bp">..</span> <span class="o">}</span> <span class="bp">;</span> <span class="n">tidy</span>

<span class="kn">end</span> <span class="n">opens</span>
</pre></div>


<p>Note that I am using <code>tidy</code> in the last line. I don't know if this is too early in the mathlib-tree?</p>

#### [ Johan Commelin (Oct 18 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136023792):
<p>If this is the direction you had in mind, I can continue moving stuff from the category folder into this file; and then PR it.</p>

#### [ Mario Carneiro (Oct 18 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136023793):
<p>We have functions for transfering a partial order</p>

#### [ Mario Carneiro (Oct 18 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136023837):
<p><code>partial_order.lift</code></p>

#### [ Mario Carneiro (Oct 18 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136023849):
<p>I hope you aren't so attached to using blasty tactics that you are reproving theorems that we already have</p>

#### [ Mario Carneiro (Oct 18 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136023856):
<p>in fact, <code>subtype.partial_order</code> is just what you need</p>

#### [ Mario Carneiro (Oct 18 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136023905):
<p><code>ext</code> is <code>subtype.eq</code></p>

#### [ Johan Commelin (Oct 18 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136023910):
<p>Ok, that's fine with me. But about the general direction? Is this what you want?</p>

#### [ Mario Carneiro (Oct 18 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136023918):
<p>yes</p>

#### [ Johan Commelin (Oct 18 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136023966):
<p>But <code>subtype.ext</code> is not an ext-lemma</p>

#### [ Johan Commelin (Oct 18 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136023971):
<p>Should I phrase mine as an ext-lemma, or as an iff?</p>

#### [ Mario Carneiro (Oct 18 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136024115):
<p>I'm not saying you shouldn't state it, but it is a proof by reference to subtype.eq</p>

#### [ Johan Commelin (Oct 18 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136024117):
<p>Right. But which version should I state? Or both?</p>

#### [ Mario Carneiro (Oct 18 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136024159):
<p><code>extensionality</code> requires the one-directional form</p>

#### [ Mario Carneiro (Oct 18 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136024162):
<p>I don't know if it would be better to use set extensionality as well though</p>

#### [ Mario Carneiro (Oct 18 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136024168):
<p>so it says <code>forall a, a \in U \lr a \in V</code></p>

#### [ Johan Commelin (Oct 18 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136024230):
<p><code>ext</code> can chain those together. So I think I'll only do the first step.</p>

#### [ Johan Commelin (Oct 18 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136025567):
<p>Done. See <a href="https://github.com/leanprover/mathlib/issues/427" target="_blank" title="https://github.com/leanprover/mathlib/issues/427">#427</a>.</p>

#### [ Scott Morrison (Oct 18 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136047222):
<blockquote>
<p>But <code>subtype.ext</code> is not an ext-lemma</p>
</blockquote>
<p>I've been wondering about this one --- can we make <code>attribute [extensionality] subtype.eq</code>?</p>

#### [ Mario Carneiro (Oct 18 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bundled%20bases/near/136047463):
<p>ext can chain them, but you will get <code>x \in U.val</code> instead of <code>x \in U</code></p>


{% endraw %}
