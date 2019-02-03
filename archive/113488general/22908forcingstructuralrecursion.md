---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/22908forcingstructuralrecursion.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [forcing structural recursion](https://leanprover-community.github.io/archive/113488general/22908forcingstructuralrecursion.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Simon Hudon (Feb 28 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/123064431):
<p>I have a mutually inductive type of tree (which is not a type family) and I'm trying to define a recursive function on it but the termination checker seems to default to well founded recursion while it should be clear that structural recursion works. Is there a way to nudge Lean in the right direction?</p>

#### [ Simon Hudon (Feb 28 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/123064513):
<p>In case that helps, here's my type definition and my function:</p>
<div class="codehilite"><pre><span></span><span class="n">mutual</span> <span class="kn">inductive</span> <span class="n">proxy_v</span><span class="o">,</span> <span class="n">proxy_leaf_v</span> <span class="o">(</span><span class="n">var</span> <span class="o">:</span> <span class="kt">Type</span> <span class="o">(</span><span class="n">max</span> <span class="n">u</span> <span class="n">v</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span>
<span class="k">with</span> <span class="n">proxy_v</span> <span class="o">:</span> <span class="kt">Type</span> <span class="o">(</span><span class="n">max</span> <span class="n">u</span> <span class="n">v</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span>
  <span class="bp">|</span> <span class="n">ret</span> <span class="o">{}</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">proxy_v</span>
  <span class="bp">|</span> <span class="n">action</span> <span class="o">{}</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">β</span><span class="o">,</span> <span class="n">m</span> <span class="n">β</span> <span class="bp">→</span> <span class="o">(</span><span class="n">β</span> <span class="bp">→</span> <span class="n">proxy_leaf_v</span><span class="o">)</span> <span class="bp">→</span> <span class="n">proxy_v</span>
  <span class="bp">|</span> <span class="n">yield</span> <span class="o">{}</span>  <span class="o">:</span> <span class="n">y&#39;</span> <span class="bp">→</span> <span class="o">(</span><span class="n">y</span> <span class="bp">→</span> <span class="n">proxy_leaf_v</span><span class="o">)</span>  <span class="bp">→</span> <span class="n">proxy_v</span>
  <span class="bp">|</span> <span class="n">await</span> <span class="o">{}</span> <span class="o">:</span>  <span class="n">x</span>  <span class="bp">→</span> <span class="o">(</span><span class="n">x&#39;</span> <span class="bp">→</span> <span class="n">proxy_leaf_v</span><span class="o">)</span> <span class="bp">→</span> <span class="n">proxy_v</span>
  <span class="bp">|</span> <span class="n">think</span> <span class="o">{}</span> <span class="o">:</span> <span class="n">proxy_leaf_v</span> <span class="bp">→</span> <span class="n">proxy_v</span>
<span class="k">with</span> <span class="n">proxy_leaf_v</span> <span class="o">:</span> <span class="kt">Type</span> <span class="o">(</span><span class="n">max</span> <span class="n">u</span> <span class="n">v</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span>
  <span class="bp">|</span> <span class="n">hole</span> <span class="o">{}</span> <span class="o">:</span> <span class="n">var</span> <span class="bp">→</span> <span class="n">proxy_leaf_v</span>
  <span class="bp">|</span> <span class="n">more</span> <span class="o">{}</span> <span class="o">:</span> <span class="n">proxy_v</span> <span class="bp">→</span> <span class="n">proxy_leaf_v</span>

<span class="bp">@</span><span class="o">[</span><span class="kn">reducible</span><span class="o">]</span>
<span class="n">def</span> <span class="n">proxy</span>  <span class="o">:</span> <span class="kt">Type</span> <span class="o">(</span><span class="n">max</span> <span class="n">u</span> <span class="n">v</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">proxy_v</span> <span class="o">(</span><span class="n">proxy_intl</span> <span class="n">α</span><span class="o">)</span> <span class="n">α</span>

<span class="bp">@</span><span class="o">[</span><span class="kn">reducible</span><span class="o">]</span>
<span class="n">def</span> <span class="n">proxy_leaf</span>  <span class="o">:</span> <span class="kt">Type</span> <span class="o">(</span><span class="n">max</span> <span class="n">u</span> <span class="n">v</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">proxy_leaf_v</span> <span class="o">(</span><span class="n">proxy_intl</span> <span class="n">α</span><span class="o">)</span> <span class="n">α</span>
</pre></div>


<div class="codehilite"><pre><span></span><span class="n">mutual</span> <span class="n">def</span> <span class="n">to_intl_aux</span><span class="o">,</span> <span class="n">to_intl</span>
<span class="k">with</span> <span class="n">to_intl_aux</span> <span class="o">:</span> <span class="n">proxy_leaf</span> <span class="n">x</span> <span class="n">x&#39;</span> <span class="n">y</span> <span class="n">y&#39;</span> <span class="n">m</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">proxy_intl</span> <span class="n">x</span> <span class="n">x&#39;</span> <span class="n">y</span> <span class="n">y&#39;</span> <span class="n">m</span> <span class="n">α</span>
 <span class="bp">|</span> <span class="o">(</span><span class="n">hole</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span> <span class="n">x</span>
 <span class="bp">|</span> <span class="o">(</span><span class="n">more</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span> <span class="n">to_intl</span> <span class="n">x</span>
<span class="k">with</span> <span class="n">to_intl</span> <span class="o">:</span> <span class="n">proxy</span> <span class="n">x</span> <span class="n">x&#39;</span> <span class="n">y</span> <span class="n">y&#39;</span> <span class="n">m</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">proxy_intl</span> <span class="n">x</span> <span class="n">x&#39;</span> <span class="n">y</span> <span class="n">y&#39;</span> <span class="n">m</span> <span class="n">α</span>
 <span class="bp">|</span> <span class="o">(</span><span class="n">ret</span> <span class="n">i</span><span class="o">)</span> <span class="o">:=</span> <span class="n">cofix</span><span class="bp">.</span><span class="n">mk</span> <span class="o">(</span><span class="n">proxy_node</span><span class="bp">.</span><span class="n">ret</span> <span class="n">i</span><span class="o">)</span> <span class="n">empty</span><span class="bp">.</span><span class="n">rec&#39;</span>
 <span class="bp">|</span> <span class="o">(</span><span class="n">action</span> <span class="n">β</span> <span class="n">cmd</span> <span class="n">f</span><span class="o">)</span> <span class="o">:=</span> <span class="n">cofix</span><span class="bp">.</span><span class="n">mk</span> <span class="o">(</span><span class="n">proxy_node</span><span class="bp">.</span><span class="n">action</span> <span class="n">cmd</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">i</span><span class="o">,</span> <span class="n">to_intl_aux</span> <span class="o">(</span><span class="n">f</span> <span class="n">i</span><span class="o">))</span>
 <span class="bp">|</span> <span class="o">(</span><span class="n">yield</span> <span class="n">o</span> <span class="n">f</span><span class="o">)</span> <span class="o">:=</span> <span class="n">cofix</span><span class="bp">.</span><span class="n">mk</span> <span class="o">(</span><span class="n">proxy_node</span><span class="bp">.</span><span class="n">yield</span> <span class="n">o</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">i</span><span class="o">,</span> <span class="n">to_intl_aux</span> <span class="o">(</span><span class="n">f</span> <span class="n">i</span><span class="o">))</span>
 <span class="bp">|</span> <span class="o">(</span><span class="n">await</span> <span class="n">o</span> <span class="n">f</span><span class="o">)</span> <span class="o">:=</span> <span class="n">cofix</span><span class="bp">.</span><span class="n">mk</span> <span class="o">(</span><span class="n">proxy_node</span><span class="bp">.</span><span class="n">await</span> <span class="n">o</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">i</span><span class="o">,</span> <span class="n">to_intl_aux</span> <span class="o">(</span><span class="n">f</span> <span class="n">i</span><span class="o">))</span>
 <span class="bp">|</span> <span class="o">(</span><span class="n">think</span> <span class="n">cmd</span><span class="o">)</span> <span class="o">:=</span> <span class="n">cofix</span><span class="bp">.</span><span class="n">mk</span> <span class="o">(</span><span class="n">proxy_node</span><span class="bp">.</span><span class="n">think</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">to_intl_aux</span> <span class="n">cmd</span><span class="o">)</span>
</pre></div>

#### [ Sebastian Ullrich (Feb 28 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/123064798):
<p>The equations compiler does not support mutual structural recursion <a href="https://github.com/leanprover/lean/blob/8a93d2770e5e4c349d761ded334f8fb7119e7082/src/library/equations_compiler/compiler.cpp#L52" target="_blank" title="https://github.com/leanprover/lean/blob/8a93d2770e5e4c349d761ded334f8fb7119e7082/src/library/equations_compiler/compiler.cpp#L52">https://github.com/leanprover/lean/blob/8a93d2770e5e4c349d761ded334f8fb7119e7082/src/library/equations_compiler/compiler.cpp#L52</a></p>

#### [ Simon Hudon (Feb 28 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/123064927):
<p>Arrg! <em>tears hair out</em></p>

#### [ Simon Hudon (Feb 28 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/123064943):
<p>I have a feeling that recursion based on <code>sizeof</code> will be difficult because of that components of type <code>something -&gt; proxy_v</code></p>

#### [ Simon Hudon (Feb 28 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/123064944):
<p>Any advice?</p>

#### [ Sebastian Ullrich (Feb 28 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/123065002):
<p>I don't think I've really used mutual recursion so far</p>

#### [ Simon Hudon (Feb 28 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/123065237):
<p>Ok here's my next attempt: I'm inlining the function <code>to_intl_aux</code> </p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">to_intl</span> <span class="o">:</span> <span class="n">proxy</span> <span class="n">x</span> <span class="n">x&#39;</span> <span class="n">y</span> <span class="n">y&#39;</span> <span class="n">m</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">proxy_intl</span> <span class="n">x</span> <span class="n">x&#39;</span> <span class="n">y</span> <span class="n">y&#39;</span> <span class="n">m</span> <span class="n">α</span>
 <span class="bp">|</span> <span class="o">(</span><span class="n">ret</span> <span class="n">i</span><span class="o">)</span> <span class="o">:=</span> <span class="n">cofix</span><span class="bp">.</span><span class="n">mk</span> <span class="o">(</span><span class="n">proxy_node</span><span class="bp">.</span><span class="n">ret</span> <span class="n">i</span><span class="o">)</span> <span class="n">empty</span><span class="bp">.</span><span class="n">rec&#39;</span>
 <span class="bp">|</span> <span class="o">(</span><span class="n">action</span> <span class="n">β</span> <span class="n">cmd</span> <span class="n">f</span><span class="o">)</span> <span class="o">:=</span> <span class="n">cofix</span><span class="bp">.</span><span class="n">mk</span> <span class="o">(</span><span class="n">proxy_node</span><span class="bp">.</span><span class="n">action</span> <span class="n">cmd</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">i</span><span class="o">,</span>
   <span class="k">match</span> <span class="o">(</span><span class="n">f</span> <span class="n">i</span><span class="o">)</span> <span class="k">with</span>
    <span class="bp">|</span> <span class="o">(</span><span class="n">hole</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span> <span class="n">x</span>
    <span class="bp">|</span> <span class="o">(</span><span class="n">more</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span> <span class="n">to_intl</span> <span class="n">x</span>
   <span class="kn">end</span> <span class="o">)</span>
 <span class="bp">|</span> <span class="o">(</span><span class="n">yield</span> <span class="n">o</span> <span class="n">f</span><span class="o">)</span> <span class="o">:=</span> <span class="n">cofix</span><span class="bp">.</span><span class="n">mk</span> <span class="o">(</span><span class="n">proxy_node</span><span class="bp">.</span><span class="n">yield</span> <span class="n">o</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">i</span><span class="o">,</span>
   <span class="k">match</span> <span class="o">(</span><span class="n">f</span> <span class="n">i</span><span class="o">)</span> <span class="k">with</span>
    <span class="bp">|</span> <span class="o">(</span><span class="n">hole</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span> <span class="n">x</span>
    <span class="bp">|</span> <span class="o">(</span><span class="n">more</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span> <span class="n">to_intl</span> <span class="n">x</span>
   <span class="kn">end</span> <span class="o">)</span>
 <span class="bp">|</span> <span class="o">(</span><span class="n">await</span> <span class="n">o</span> <span class="n">f</span><span class="o">)</span> <span class="o">:=</span> <span class="n">cofix</span><span class="bp">.</span><span class="n">mk</span> <span class="o">(</span><span class="n">proxy_node</span><span class="bp">.</span><span class="n">await</span> <span class="n">o</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">i</span><span class="o">,</span>
   <span class="k">match</span> <span class="o">(</span><span class="n">f</span> <span class="n">i</span><span class="o">)</span> <span class="k">with</span>
    <span class="bp">|</span> <span class="o">(</span><span class="n">hole</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span> <span class="n">x</span>
    <span class="bp">|</span> <span class="o">(</span><span class="n">more</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span> <span class="n">to_intl</span> <span class="n">x</span>
   <span class="kn">end</span> <span class="o">)</span>
 <span class="bp">|</span> <span class="o">(</span><span class="n">think</span> <span class="n">cmd</span><span class="o">)</span> <span class="o">:=</span> <span class="n">cofix</span><span class="bp">.</span><span class="n">mk</span> <span class="o">(</span><span class="n">proxy_node</span><span class="bp">.</span><span class="n">think</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span>
   <span class="k">match</span> <span class="n">cmd</span> <span class="k">with</span>
    <span class="bp">|</span> <span class="o">(</span><span class="n">hole</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span> <span class="n">x</span>
    <span class="bp">|</span> <span class="o">(</span><span class="n">more</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span> <span class="n">to_intl</span> <span class="n">x</span>
   <span class="kn">end</span> <span class="o">)</span>
</pre></div>


<p>Again, it's falling back on well founded recursion and trying to prove that, in many cases <code>sizeof x &lt; 1</code></p>

#### [ Simon Hudon (Feb 28 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/123065334):
<p>Is there any theoretical limitation that prevents the use of structural recursion in mutually recursive functions?</p>

#### [ Simon Hudon (Feb 28 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/123065741):
<p>Good news everyone! I made it work by hardcoding the details of the mutually inductive type</p>

#### [ Simon Hudon (Feb 28 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/123066278):
<p>Is there any plan to make <code>io</code> universe polymorphic?</p>

#### [ Sebastian Ullrich (Feb 28 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/123083059):
<blockquote>
<p>Is there any theoretical limitation that prevents the use of structural recursion in mutually recursive functions?</p>
</blockquote>
<p>I don't think so</p>

#### [ Sebastian Ullrich (Feb 28 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/123083113):
<blockquote>
<p>Is there any plan to make <code>io</code> universe polymorphic?</p>
</blockquote>
<p>No plans, but I don't see why not</p>

#### [ Simon Hudon (Mar 01 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/123152522):
<p>With regards to structural recursion, would it be any better if instead of having a <code>proxy_leaf_v</code> branch, I would just use <code>⊕</code>? Would that block my structural recursion then too?</p>

#### [ Sebastian Ullrich (Mar 01 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/123157356):
<p>Ah, that should probably work...?</p>

#### [ Simon Hudon (Mar 01 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/123157415):
<p>Maybe that's better than coding my own mutually inductive type then. I'll give it a try</p>

#### [ Sebastian Ullrich (Apr 25 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/125670451):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> Did you ever make progress on this issue? Should mutual inductives in Lean 3 simply be avoided?</p>

#### [ Simon Hudon (Apr 25 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/125670898):
<p>I ended up encoding my mutually inductive type by hand using an inductive family. I think that was the only way to do it.</p>

#### [ Simon Hudon (Apr 25 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/125671041):
<p>It's been a few months since I touched that project but I'm wondering if the situation would improved if <code>has_well_founded</code> had two type parameter. When you're using polymorphic recursion, i.e. your function <code>foo</code> has type <code>foo : Π {α : Type*}, my_type α</code> and that your recursive call is on <code>my_type β</code>, I wonder if that would make well founded recursion work nonetheless</p>

#### [ Sebastian Ullrich (Apr 25 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/125672470):
<p>Good to know, thanks. I'm not sure I understand your <code>has_well_founded</code> idea. Do you not have a (monomorphic) measure on your type?</p>

#### [ Simon Hudon (Apr 25 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/125672886):
<p>Yes, the one based on <code>has_sizeof</code> should do.</p>

#### [ Simon Hudon (Apr 25 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/125673041):
<p>What I mean is that <code>has_well_founded.r x y</code> might be the appropriate proof obligation in situations where <code>x : my_type α</code> and <code>y : my_type β</code> but that's not well typed. That where the only solution is structural recursion</p>

#### [ Sebastian Ullrich (Apr 25 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/125676961):
<p>I think the current equation compiler may actually be... acceptable... if we had tactics that could deal with these usually very simple inequations. We don't currently, do we? :)</p>

#### [ Simon Hudon (Apr 25 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/125685933):
<p>Are you suggesting that it could be fixed using a <code>using_well_founded</code> clause?</p>

#### [ Sebastian Ullrich (Apr 26 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/125695965):
<p>Yes. The first issue is that the default wf tactic pair uses the sum of the measures of all arguments, which makes the inequations harder, or possibly even contradictory. So the first step may be a <code>rel_tac</code> tactic that uses the measure of only a single argument (probably the first one that is discriminated), which should generate inequations of the form <code>x &lt; ... + x + ... + 1</code>. It should not be too hard to write a <code>dec_tac</code> to solve those. With that we should get a wf tactic pair that proves all mutual structural recursions over a single argument.</p>

#### [ Simon Hudon (Apr 26 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/125696149):
<p>Nice! Do you think there might be a way to integrate it to the default well founded recursion tactic?</p>

#### [ Sebastian Ullrich (Apr 26 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/forcing%20structural%20recursion/near/125696389):
<p>Well, I hope that in the next version of Lean there will simply be native support for mutual structural recursion</p>


{% endraw %}
