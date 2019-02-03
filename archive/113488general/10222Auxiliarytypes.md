---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/10222Auxiliarytypes.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Auxiliary types](https://leanprover-community.github.io/archive/113488general/10222Auxiliarytypes.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Dec 12 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Auxiliary%20types/near/151490448):
<p>I've been thinking about auxiliary types. Types like <code>additive</code> and <code>multiplicative</code>. Types that help the type-class inference system do its job. Interestingly I don't see a wide use of auxiliary types. I understand that one of the inconveniences is that sometimes you want to refer to elements of the original type, and transferring between the real type and the auxiliary type might prove a bit troublesome. What are your thoughts on auxiliary types?</p>

#### [ Kenny Lau (Dec 12 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Auxiliary%20types/near/151490470):
<p>So for example there are <code>def</code>initions that should be instances, but is not so because the typeclass system could not possibly figure out the argument. What if we then created auxiliary types to solve this problem?</p>

#### [ Mario Carneiro (Dec 12 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Auxiliary%20types/near/151490751):
<p>auxiliary types can be used to help here</p>

#### [ Mario Carneiro (Dec 12 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Auxiliary%20types/near/151490855):
<p>for example, if you have a module on <code>B</code> from a ring hom <code>f : A -&gt; B</code>, then this is a bad instance because the ring hom <code>f</code> is not a typeclass but it is required for the instance. If you have a wrapper type <code>ring_hom_module f := B</code>, then lean can handle it because it is now inferred by unification instead of typeclass inference</p>

#### [ Mario Carneiro (Dec 12 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Auxiliary%20types/near/151490860):
<p>This is how <code>Qp</code> works, for example</p>

#### [ Kenny Lau (Dec 12 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Auxiliary%20types/near/151490927):
<p>what is Qp?</p>

#### [ Mario Carneiro (Dec 12 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Auxiliary%20types/near/151490931):
<p>actually never mind, that's not a good example (it is an example of something else)</p>

#### [ Mario Carneiro (Dec 12 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Auxiliary%20types/near/151490937):
<p>padic rats</p>

#### [ Kenny Lau (Dec 12 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Auxiliary%20types/near/151490940):
<p>actually I've been using exactly the same example and it has been working great</p>

#### [ Kenny Lau (Dec 12 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Auxiliary%20types/near/151490947):
<p>I'm now experimenting them on semidirect products</p>

#### [ Mario Carneiro (Dec 12 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Auxiliary%20types/near/151490959):
<p>aha, <code>zmodp</code> is an example</p>

#### [ Mario Carneiro (Dec 12 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Auxiliary%20types/near/151491042):
<p>it has an explicit argument <code>hp : prime p</code> so that lean can derive the field instance</p>

#### [ Mario Carneiro (Dec 12 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Auxiliary%20types/near/151491051):
<p>semidirect product is a pretty good example</p>

#### [ Kenny Lau (Dec 12 2018 at 02:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Auxiliary%20types/near/151494819):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> it worked great with dihedral</p>

#### [ Kenny Lau (Dec 12 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Auxiliary%20types/near/151494900):
<p><a href="https://github.com/kckennylau/Lean/blob/master/semidirect_product.lean" target="_blank" title="https://github.com/kckennylau/Lean/blob/master/semidirect_product.lean">https://github.com/kckennylau/Lean/blob/master/semidirect_product.lean</a></p>

#### [ Simon Hudon (Dec 12 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Auxiliary%20types/near/151494983):
<p>(deleted)</p>

#### [ Kenny Lau (Dec 16 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Auxiliary%20types/near/151873964):
<p>I think we should use auxiliary types for modules</p>

#### [ Kevin Buzzard (Dec 16 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Auxiliary%20types/near/151874110):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> you hoped that Kenny would know how to fix modules but he knows several possible solutions. Which is best?</p>

#### [ Mario Carneiro (Dec 16 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Auxiliary%20types/near/151874162):
<p>what is the proposal exactly?</p>

#### [ Kevin Buzzard (Dec 16 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Auxiliary%20types/near/151876446):
<p>I don't even understand the outparam proposal, I am still an outparam amateur</p>

#### [ Kevin Buzzard (Dec 16 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Auxiliary%20types/near/151876486):
<p>There's an old thread which goes through it which I will dig up at some point</p>

#### [ Kenny Lau (Dec 16 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Auxiliary%20types/near/151876777):
<p>something like:</p>
<div class="codehilite"><pre><span></span><span class="n">universes</span> <span class="n">u</span> <span class="n">v</span>

<span class="n">class</span> <span class="n">has_scalar</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">(</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="n">smul</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">γ</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">)</span>

<span class="kn">infixr</span> <span class="bp">`</span> <span class="err">•</span> <span class="bp">`</span><span class="o">:</span><span class="mi">73</span> <span class="o">:=</span> <span class="n">has_scalar</span><span class="bp">.</span><span class="n">smul</span>


<span class="kn">structure</span> <span class="n">module</span><span class="bp">.</span><span class="n">core</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">(</span><span class="n">M</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="o">[</span><span class="n">add_comm_group</span> <span class="n">M</span><span class="o">]</span> <span class="kn">extends</span> <span class="n">has_scalar</span> <span class="n">R</span> <span class="n">M</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">smul_add</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">r</span><span class="o">:</span><span class="n">R</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span><span class="o">:</span><span class="n">M</span><span class="o">),</span> <span class="n">r</span> <span class="err">•</span> <span class="o">(</span><span class="n">x</span> <span class="bp">+</span> <span class="n">y</span><span class="o">)</span> <span class="bp">=</span> <span class="n">r</span> <span class="err">•</span> <span class="n">x</span> <span class="bp">+</span> <span class="n">r</span> <span class="err">•</span> <span class="n">y</span><span class="o">)</span>

<span class="n">def</span> <span class="n">module_type</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">{</span><span class="n">M</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="n">add_comm_group</span> <span class="n">M</span><span class="o">]</span> <span class="o">(</span><span class="n">m</span> <span class="o">:</span> <span class="n">module</span><span class="bp">.</span><span class="n">core</span> <span class="n">R</span> <span class="n">M</span><span class="o">)</span> <span class="o">:=</span> <span class="n">M</span>
</pre></div>


{% endraw %}
