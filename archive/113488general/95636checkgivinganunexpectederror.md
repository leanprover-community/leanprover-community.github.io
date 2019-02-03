---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/95636checkgivinganunexpectederror.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [#check giving an unexpected error](https://leanprover-community.github.io/archive/113488general/95636checkgivinganunexpectederror.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ M. Andrew Moshier (Apr 27 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23check%20giving%20an%20unexpected%20error/near/125761013):
<p>This example illustrates behavior I am not able to explain. #check gives expected answers for sub-expressions, but not for <code>G.arr A B</code> unless I explicitly decorate <code>G.arr</code> with its type. But the example shows that #check already correctly inferred the type.</p>
<p>Any ideas why?</p>
<div class="codehilite"><pre><span></span>class {u} graph (α : Type u) :=
    (arr : α  → α  → Sort u)

variable α : Type 1
variables A B : α
variable G : graph α


#check G         -- G : graph α
#check G.arr     -- graph.arr : α → α → Type
#check A         -- A : α
#check G.arr A B -- error &quot;invalid field notation,
                 -- function &#39;graph.arr&#39; does not have explicit argument
                 -- with type (graph ...)&quot;
#check (G.arr : α → α → Type) A B
                 -- G.arr A B : Type   (as expected)
</pre></div>

#### [ Kenny Lau (Apr 27 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23check%20giving%20an%20unexpected%20error/near/125761057):
<p>what does <code>#check @graph.arr</code> give?</p>

#### [ Kenny Lau (Apr 27 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23check%20giving%20an%20unexpected%20error/near/125761061):
<div class="codehilite"><pre><span></span><span class="n">graph</span><span class="bp">.</span><span class="n">arr</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">}</span> <span class="o">[</span><span class="n">c</span> <span class="o">:</span> <span class="n">graph</span> <span class="n">α</span><span class="o">],</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">Sort</span> <span class="n">u_1</span>
</pre></div>

#### [ Kenny Lau (Apr 27 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23check%20giving%20an%20unexpected%20error/near/125761062):
<p>the <code>graph</code> is not the <strong>first explicit argument</strong> of <code>graph.arr</code>, so projection fails</p>

#### [ Kenny Lau (Apr 27 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23check%20giving%20an%20unexpected%20error/near/125761070):
<p>If you make it a <code>structure</code>, then you can use projections, as it becomes:</p>
<div class="codehilite"><pre><span></span><span class="n">graph</span><span class="bp">.</span><span class="n">arr</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">},</span> <span class="n">graph</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">Sort</span> <span class="n">u_1</span>
</pre></div>

#### [ M. Andrew Moshier (Apr 27 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23check%20giving%20an%20unexpected%20error/near/125761080):
<p><code> Π {α : Type u_1} [c : graph α], α → α → Sort u_1</code></p>

#### [ Kenny Lau (Apr 27 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23check%20giving%20an%20unexpected%20error/near/125761161):
<p>alternative solution:</p>
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="o">{</span><span class="n">u</span><span class="o">}</span> <span class="n">graph</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">:=</span>
    <span class="o">(</span><span class="n">arr</span> <span class="o">:</span> <span class="n">α</span>  <span class="bp">→</span> <span class="n">α</span>  <span class="bp">→</span> <span class="n">Sort</span> <span class="n">u</span><span class="o">)</span>

<span class="n">def</span> <span class="n">graph</span><span class="bp">.</span><span class="n">arr_proj</span> <span class="o">{</span><span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">G</span> <span class="o">:</span> <span class="n">graph</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">Sort</span> <span class="bp">_</span> <span class="o">:=</span>
<span class="bp">@</span><span class="n">graph</span><span class="bp">.</span><span class="n">arr</span> <span class="n">α</span> <span class="n">G</span>

<span class="kn">variable</span> <span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="mi">1</span>
<span class="kn">variables</span> <span class="n">A</span> <span class="n">B</span> <span class="o">:</span> <span class="n">α</span>
<span class="kn">variable</span> <span class="n">G</span> <span class="o">:</span> <span class="n">graph</span> <span class="n">α</span>

<span class="bp">#</span><span class="kn">check</span> <span class="n">G</span><span class="bp">.</span><span class="n">arr_proj</span> <span class="n">A</span> <span class="n">B</span>
</pre></div>

#### [ M. Andrew Moshier (Apr 27 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23check%20giving%20an%20unexpected%20error/near/125761175):
<p>I think my problem is I don't quite understand how <code>[...]</code> arguments are dealt with. My intuition is that <code>G.arr</code> ought to resolve correctly to the right type. I see why your soln works, but not why mine does not. Anyway, thanks.</p>

#### [ Kenny Lau (Apr 27 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23check%20giving%20an%20unexpected%20error/near/125761220):
<p>I already told you</p>

#### [ Kenny Lau (Apr 27 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23check%20giving%20an%20unexpected%20error/near/125761222):
<blockquote>
<p>the <code>graph</code> is not the <strong>first explicit argument</strong> of <code>graph.arr</code>, so projection fails</p>
</blockquote>

#### [ Mario Carneiro (Apr 27 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23check%20giving%20an%20unexpected%20error/near/125761223):
<p>Alternative solution, don't mention <code>G</code> at all</p>
<div class="codehilite"><pre><span></span>class {u} graph (α : Type u) :=
    (arr : α  → α  → Sort u)

variable α : Type 1
variables A B : α
variable G : graph α
include G

#check graph.arr A B
</pre></div>

#### [ Mario Carneiro (Apr 27 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23check%20giving%20an%20unexpected%20error/near/125761231):
<p>when you use typeclass arguments (by marking <code>graph</code> as <code>class</code>), the idea is that you don't mention the variables of those types at all, they are inferred from context</p>

#### [ Kenny Lau (Apr 27 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23check%20giving%20an%20unexpected%20error/near/125761239):
<p>you win</p>

#### [ Mario Carneiro (Apr 27 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23check%20giving%20an%20unexpected%20error/near/125761243):
<p>Actually the usual way to write <code>G</code> there is <code>variable [graph α]</code> and skip the <code>include</code> line</p>

#### [ Kenny Lau (Apr 27 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23check%20giving%20an%20unexpected%20error/near/125761291):
<p>right, you don't give names to instances of class</p>

#### [ Kenny Lau (Apr 27 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23check%20giving%20an%20unexpected%20error/near/125761293):
<p>confer how partial orders are defined</p>

#### [ Kenny Lau (Apr 27 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23check%20giving%20an%20unexpected%20error/near/125761294):
<p>and used</p>

#### [ M. Andrew Moshier (Apr 27 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23check%20giving%20an%20unexpected%20error/near/125761349):
<p>Thanks both.</p>


{% endraw %}
