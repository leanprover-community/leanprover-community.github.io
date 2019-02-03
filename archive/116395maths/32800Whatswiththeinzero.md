---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/32800Whatswiththeinzero.html
---

## Stream: [maths](index.html)
### Topic: [What's with the `_` in `zero_`?](32800Whatswiththeinzero.html)

---


{% raw %}
#### [ Kevin Buzzard (Oct 07 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20with%20the%20%60_%60%20in%20%60zero_%60%3F/near/135330352):
<p>I've seen this in a few places now:</p>
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">is_submodule</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="n">ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">module</span> <span class="n">α</span> <span class="n">β</span><span class="o">]</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">set</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">zero_</span> <span class="o">:</span> <span class="o">(</span><span class="mi">0</span><span class="o">:</span><span class="n">β</span><span class="o">)</span> <span class="err">∈</span> <span class="n">p</span><span class="o">)</span>
<span class="o">(</span><span class="n">add_</span>  <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">x</span> <span class="n">y</span><span class="o">},</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">p</span> <span class="bp">→</span> <span class="n">y</span> <span class="err">∈</span> <span class="n">p</span> <span class="bp">→</span> <span class="n">x</span> <span class="bp">+</span> <span class="n">y</span> <span class="err">∈</span> <span class="n">p</span><span class="o">)</span>
<span class="o">(</span><span class="n">smul</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">c</span> <span class="o">{</span><span class="n">x</span><span class="o">},</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">p</span> <span class="bp">→</span> <span class="n">c</span> <span class="err">•</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">p</span><span class="o">)</span>
</pre></div>


<p>Why <code>zero_</code> and <code>add_</code> but not <code>smul_</code>?</p>

#### [ Mario Carneiro (Oct 07 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20with%20the%20%60_%60%20in%20%60zero_%60%3F/near/135331864):
<p>I think we are using <code>'</code> for this now</p>

#### [ Mario Carneiro (Oct 07 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20with%20the%20%60_%60%20in%20%60zero_%60%3F/near/135331865):
<p>it's avoiding a name clash with a restated axiom just below it</p>

#### [ Kevin Buzzard (Oct 07 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/What%27s%20with%20the%20%60_%60%20in%20%60zero_%60%3F/near/135342852):
<p>Once we decide on a convention will it mean that a lot of code needs to be rewritten? The idea is that we are separating off the actual constructor (which is supposed to be thought of as hidden?) from the user interface? Of course <code>'</code> is used in other situations in mathlib to mean something else -- like "oh if you don't want that <code>add_sub_cancel</code> you might instead find <code>add_sub_cancel'</code> useful", right?</p>


{% endraw %}
