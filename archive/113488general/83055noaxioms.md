---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/83055noaxioms.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [no axioms](https://leanprover-community.github.io/archive/113488general/83055noaxioms.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Apr 28 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/no%20axioms/near/125814400):
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">tower</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">set</span> <span class="o">(</span><span class="n">set</span> <span class="n">α</span><span class="o">))</span>
<span class="bp">|</span> <span class="n">empty</span> <span class="o">:</span> <span class="n">tower</span> <span class="err">∅</span>
<span class="bp">|</span> <span class="n">succ</span>  <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">t</span><span class="o">},</span> <span class="n">tower</span> <span class="n">t</span> <span class="bp">→</span> <span class="n">tower</span> <span class="o">(</span><span class="n">succ</span> <span class="n">S</span> <span class="n">t</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">chain</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">C</span><span class="o">},</span> <span class="n">C</span> <span class="err">⊆</span> <span class="n">chains</span> <span class="n">S</span> <span class="bp">→</span> <span class="n">is_chain</span> <span class="n">C</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">A</span> <span class="err">∈</span> <span class="n">C</span><span class="o">,</span> <span class="n">tower</span> <span class="n">A</span><span class="o">)</span> <span class="bp">→</span> <span class="n">tower</span> <span class="o">{</span> <span class="n">A</span> <span class="bp">|</span> <span class="bp">∃</span> <span class="n">t</span> <span class="err">∈</span> <span class="n">C</span><span class="o">,</span> <span class="n">A</span> <span class="err">∈</span> <span class="n">t</span> <span class="o">}</span>
<span class="bp">#</span><span class="kn">print</span> <span class="n">axioms</span> <span class="n">succ</span> <span class="c1">-- classical.choice quot.sound propext</span>
<span class="bp">#</span><span class="kn">print</span> <span class="n">axioms</span> <span class="n">tower</span> <span class="c1">-- no axioms</span>
</pre></div>


<p>Why does <code>tower</code> use no axioms even though I clearly see <code>succ</code>?</p>

#### [ Kevin Buzzard (Apr 28 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/no%20axioms/near/125821103):
<p>Kenny you are posting code which doesn't run</p>

#### [ Kenny Lau (Apr 28 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/no%20axioms/near/125821104):
<p>oops</p>

#### [ Kevin Buzzard (Apr 28 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/no%20axioms/near/125821105):
<p>so I can only conjecture</p>

#### [ Kevin Buzzard (Apr 28 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/no%20axioms/near/125821106):
<p>but not verify</p>

#### [ Kevin Buzzard (Apr 28 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/no%20axioms/near/125821108):
<p>that if you instead try <code>#print axioms tower.mk</code></p>

#### [ Kevin Buzzard (Apr 28 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/no%20axioms/near/125821109):
<p>you will see the axioms you used</p>

#### [ Kevin Buzzard (Apr 28 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/no%20axioms/near/125821116):
<p>let me know if I answered your question</p>

#### [ Kenny Lau (Apr 28 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/no%20axioms/near/125821118):
<p>it's a prop so it has no k</p>

#### [ Kenny Lau (Apr 28 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/no%20axioms/near/125821119):
<p>mk</p>

#### [ Kevin Buzzard (Apr 28 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/no%20axioms/near/125821170):
<p>If it's a prop then maybe it really does use no axioms</p>

#### [ Kevin Buzzard (Apr 28 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/no%20axioms/near/125821217):
<p>because all those <code>cases H</code> which you had to change to <code>classical.some H</code> when you were working with data</p>

#### [ Simon Hudon (Apr 28 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/no%20axioms/near/125821481):
<p>An inductive type definition is not a definition in the kernel. It's built by postulating that <code>tower</code> is a type of the proper universe, that <code>empty</code>, <code>succ</code> and <code>chain</code> are functions that return a tower and that a recursor exists</p>

#### [ Kevin Buzzard (Apr 28 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/no%20axioms/near/125822337):
<p>sorry, someone came round</p>

#### [ Kevin Buzzard (Apr 28 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/no%20axioms/near/125822338):
<p>was going to finish "...can be changed back somehow"</p>

#### [ Kevin Buzzard (Apr 28 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/no%20axioms/near/125822343):
<p>Actually I really do not understand what is going on here.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/no%20axioms/near/125822346):
<p>Am I right in thinking that in general it is possible to construct Props which don't use axioms but whose construction essentially uses types which are not props and whose construction involves axioms?</p>

#### [ Kevin Buzzard (Apr 28 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/no%20axioms/near/125822347):
<p>How much will Prop let us forget?</p>

#### [ Kevin Buzzard (Apr 28 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/no%20axioms/near/125822386):
<p>I do not know if I can make my question rigorous</p>

#### [ Simon Hudon (Apr 28 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/no%20axioms/near/125825885):
<p>I don't get your question. Do you mean constructing pops that only uses inductive definitions?</p>

#### [ Gabriel Ebner (Apr 29 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/no%20axioms/near/125846688):
<p>The technical answer is that the code for <code>#print axioms</code> does not traverse inductive declarations.  It only looks at the contents and types of definitions, and types of axioms.  This is probably not a problem since you presumably don't require choice if you never use <code>tower.succ</code>.</p>


{% endraw %}
