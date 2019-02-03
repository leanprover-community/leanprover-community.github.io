---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/91327producttopology.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [product topology](https://leanprover-community.github.io/archive/116395maths/91327producttopology.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Rohan Mitta (Jul 24 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/product%20topology/near/130223243):
<p>Hi! I'm trying to define the product topology and am running into issues. I may have made a silly mistake somewhere, but it seems  to me that "I" should have type set (set (α × β)), but I get a type mismatch error. Any help would be greatly appreciated.</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">topology</span><span class="bp">.</span><span class="n">continuity</span>
<span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">topology</span><span class="bp">.</span><span class="n">topological_space</span>
<span class="kn">open</span> <span class="n">set</span> <span class="n">filter</span> <span class="n">lattice</span> <span class="n">classical</span>


<span class="n">def</span> <span class="n">product_top</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">Y</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">β</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span><span class="n">is_open</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="o">(</span><span class="n">W</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">β</span><span class="o">),</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">I</span> <span class="o">:</span> <span class="o">(</span><span class="n">set_of</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">b</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">β</span><span class="o">)),</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">U</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">V</span> <span class="o">:</span> <span class="n">set</span> <span class="n">β</span><span class="o">),</span> <span class="n">is_open</span> <span class="n">U</span> <span class="bp">∧</span> <span class="n">is_open</span> <span class="n">V</span> <span class="bp">∧</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">set</span><span class="bp">.</span><span class="n">prod</span> <span class="n">U</span> <span class="n">V</span><span class="o">))),</span> <span class="n">W</span> <span class="bp">=</span> <span class="err">⋃₀</span> <span class="n">I</span><span class="o">,</span>
 <span class="n">is_open_univ</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span> <span class="n">is_open_inter</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span> <span class="n">is_open_sUnion</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">}</span>
</pre></div>

#### [ Johan Commelin (Jul 24 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/product%20topology/near/130223261):
<p>This is already in mathlib. Did you know that?</p>

#### [ Kevin Buzzard (Jul 24 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/product%20topology/near/130223528):
<p>first error for me is at the comma after alpha x beta</p>

#### [ Kevin Buzzard (Jul 24 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/product%20topology/near/130223543):
<p>because it's expecting a close bracket</p>

#### [ Kevin Buzzard (Jul 24 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/product%20topology/near/130223738):
<p>Your I seems to have type <code>↥{b : set (α × β) | ∃ (U : set α) (V : set β), is_open U ∧ is_open V ∧ b = set.prod U V}</code></p>

#### [ Kevin Buzzard (Jul 24 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/product%20topology/near/130223994):
<div class="codehilite"><pre><span></span><span class="bp">#</span><span class="kn">check</span> <span class="bp">λ</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">topological_space</span> <span class="n">β</span><span class="o">],</span> <span class="o">(</span><span class="n">set_of</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">b</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">β</span><span class="o">)),</span>
           <span class="bp">∃</span> <span class="o">(</span><span class="n">U</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">V</span> <span class="o">:</span> <span class="n">set</span> <span class="n">β</span><span class="o">),</span> <span class="n">is_open</span> <span class="n">U</span> <span class="bp">∧</span> <span class="n">is_open</span> <span class="n">V</span> <span class="bp">∧</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">set</span><span class="bp">.</span><span class="n">prod</span> <span class="n">U</span> <span class="n">V</span><span class="o">))</span>
</pre></div>

#### [ Kevin Buzzard (Jul 24 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/product%20topology/near/130224051):
<p>that has type <code>Π (α β : Type) [_inst_1 : topological_space α] [_inst_2 : topological_space β], set (set (α × β))</code></p>

#### [ Kevin Buzzard (Jul 24 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/product%20topology/near/130224168):
<p>So this term: <code>(set_of (λ (b : set (α × β)), 
           ∃ (U : set α) (V : set β), is_open U ∧ is_open V ∧ b = set.prod U V))</code> is the term which has type <code>set (set (α × β))</code></p>

#### [ Kevin Buzzard (Jul 24 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/product%20topology/near/130224281):
<p>and in particular that's just a term. OK so when you ask that there exists a term <code>I</code> which has type [that term above], Lean says "wait, that's a term, not a type, how can he want a term of that type? Oh I know I'll turn that <code>set_of</code> term above into a subtype, and then <code>I</code> can be a term of that type.</p>

#### [ Kevin Buzzard (Jul 24 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/product%20topology/near/130224737):
<p>Yeah it all makes sense -- </p>
<div class="codehilite"><pre><span></span><span class="bp">#</span><span class="kn">check</span> <span class="bp">@</span><span class="n">set_of</span>
<span class="c1">-- set_of : Π {α : Type u_1}, (α → Prop) → set α</span>
</pre></div>


<p><code>set_of</code> eventually produces a term <code>t</code> of type <code>set X</code> for some <code>X</code>, and your <code>I</code> is a term of type <code>t</code> so you're one layer too deep</p>

#### [ Rohan Mitta (Jul 24 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/product%20topology/near/130235708):
<p>Thanks, that's made it a lot clearer. I think I'll be able to figure it out from there.</p>

#### [ Rohan Mitta (Jul 24 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/product%20topology/near/130235779):
<p>Hi Johan,</p>
<blockquote>
<p>This is already in mathlib. Did you know that?</p>
</blockquote>
<p>I did not know that. Where can I find it?</p>

#### [ Luca Gerolla (Jul 24 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/product%20topology/near/130240623):
<p>Hi Rohan, it's an instance at line 909 of topological_space</p>

#### [ Luca Gerolla (Jul 24 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/product%20topology/near/130240646):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">[</span><span class="n">t₁</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">t₂</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">β</span><span class="o">]</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="o">(</span><span class="n">α</span> <span class="bp">×</span> <span class="n">β</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">induced</span> <span class="n">prod</span><span class="bp">.</span><span class="n">fst</span> <span class="n">t₁</span> <span class="err">⊔</span> <span class="n">induced</span> <span class="n">prod</span><span class="bp">.</span><span class="n">snd</span> <span class="n">t₂</span>
</pre></div>

#### [ Luca Gerolla (Jul 25 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/product%20topology/near/130240856):
<p>Should be equivalent to the "canonical" product topology you defined, but don't know if that easy to prove :/</p>

#### [ Kevin Buzzard (Jul 25 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/product%20topology/near/130242698):
<p>In maths this says "define a topology on <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>α</mi><mo>×</mo><mi>β</mi></mrow><annotation encoding="application/x-tex">\alpha\times\beta</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.0037em;">α</span><span class="mbin">×</span><span class="mord mathit" style="margin-right:0.05278em;">β</span></span></span></span> to be the smallest topology such that the following sets are all open: first all the <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>U</mi><mo>×</mo><mi>β</mi></mrow><annotation encoding="application/x-tex">U\times\beta</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10903em;">U</span><span class="mbin">×</span><span class="mord mathit" style="margin-right:0.05278em;">β</span></span></span></span> for <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>U</mi><mo>⊆</mo><mi>α</mi></mrow><annotation encoding="application/x-tex">U\subseteq\alpha</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.8193em;vertical-align:-0.13597em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10903em;">U</span><span class="mrel">⊆</span><span class="mord mathit" style="margin-right:0.0037em;">α</span></span></span></span> open, and second all the <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>α</mi><mo>×</mo><mi>V</mi></mrow><annotation encoding="application/x-tex">\alpha\times V</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.76666em;vertical-align:-0.08333em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.0037em;">α</span><span class="mbin">×</span><span class="mord mathit" style="margin-right:0.22222em;">V</span></span></span></span> for <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>V</mi><mo>⊆</mo><mi>β</mi></mrow><annotation encoding="application/x-tex">V\subseteq\beta</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.22222em;">V</span><span class="mrel">⊆</span><span class="mord mathit" style="margin-right:0.05278em;">β</span></span></span></span> open."</p>

#### [ Kevin Buzzard (Jul 25 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/product%20topology/near/130242868):
<p>The reason it says this is that the induced topology on <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>α</mi><mo>×</mo><mi>β</mi></mrow><annotation encoding="application/x-tex">\alpha\times\beta</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.0037em;">α</span><span class="mbin">×</span><span class="mord mathit" style="margin-right:0.05278em;">β</span></span></span></span> coming from the projection down to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>α</mi></mrow><annotation encoding="application/x-tex">\alpha</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.0037em;">α</span></span></span></span> that's what <code>prod.fst</code> is) is precisely the one where the open sets are pre-images of opens in <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>α</mi></mrow><annotation encoding="application/x-tex">\alpha</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.0037em;">α</span></span></span></span>.</p>

#### [ Kevin Buzzard (Jul 25 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/product%20topology/near/130242945):
<p>And the reason that this is the product topology is first that all those sets are open in the product topology, and conversely that in any topology where these sets are all open, the intersection of two such sets is open, and that's precisely <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>U</mi><mo>×</mo><mi>V</mi></mrow><annotation encoding="application/x-tex">U\times V</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.76666em;vertical-align:-0.08333em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10903em;">U</span><span class="mbin">×</span><span class="mord mathit" style="margin-right:0.22222em;">V</span></span></span></span>, so any such topology will contain all the sets which are open in the product topology.</p>


{% endraw %}
