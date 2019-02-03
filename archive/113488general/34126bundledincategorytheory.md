---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/34126bundledincategorytheory.html
---

## Stream: [general](index.html)
### Topic: [bundled in category_theory](34126bundledincategorytheory.html)

---


{% raw %}
#### [ Sean Leather (Oct 04 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bundled%20in%20category_theory/near/135174961):
<p>I just discovered <code>bundled</code> in <code>category_theory.category</code>:</p>
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">bundled</span> <span class="o">(</span><span class="n">c</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span>
<span class="o">[</span><span class="n">str</span> <span class="o">:</span> <span class="n">c</span> <span class="n">α</span><span class="o">]</span>
</pre></div>


<p>This seems very useful. In particular, I'm thinking it can help me remove <code>[decidable_eq α]</code> that I have to state everywhere by allowing me to bundle the condition. So, I have a couple of questions:</p>
<p>1. I think it would be helpful to define this outside the <code>category_theory</code> directory because it's not inherently tied to category theory. Do people agree? Should it be in <code>data/bundled.lean</code> or somewhere else?<br>
2. Do the <code>[</code>/<code>]</code> brackets do anything different from <code>(</code>/<code>)</code> here? <code>#print bundled</code> doesn't give any clue.<br>
3. What does <code>str</code> abbreviate? I've typically seen <code>str</code> for string, but I don't think that makes sense here. Is it <code>structure</code>? If so, why? It seems more like a type function being bundled with its parameter, so I'm not clear where the <code>structure</code> comes in.</p>

#### [ Kevin Buzzard (Oct 04 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bundled%20in%20category_theory/near/135175752):
<p>I <em>believe</em> that the only difference the <code>[]</code> makes within the structure is that you can use type class inference within the structure itself. So I am going to stick my neck out and suggest that in this case, where we don't need str to be inferred in any of the other fields, the <code>[]</code> is no different to <code>()</code>. Apologies if I've written something misleading / wrong here. I think the way to make type class inference pick up on <code>str</code> is to have the obvious instance immediately after the definition of the structure.</p>

#### [ Scott Morrison (Oct 04 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bundled%20in%20category_theory/near/135177519):
<p>I think Johannes suggested the <code>[ ]</code> here, and I never thought too hard about it.</p>

#### [ Scott Morrison (Oct 04 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bundled%20in%20category_theory/near/135177627):
<p><code>str</code> is indeed for <code>structure</code>. We earlier had <code>carrier</code> instead of <code>a</code>.</p>

#### [ Scott Morrison (Oct 04 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bundled%20in%20category_theory/near/135177784):
<p>Regarding <code>bundled</code>, I've found that it has limited use, because as soon as you're past the first round of examples, you want to bundle up multiple typeclasses, and you're back to writing a custom structure for each set of typeclasses you're interested in.</p>

#### [ Sean Leather (Oct 04 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bundled%20in%20category_theory/near/135183550):
<p>I can see how it is not suitable for more involved structures. This applies as well to <code>sigma</code>, <code>subtype</code>, etc. (And, even for cases that fit those, it often seems better to define your own structure.) That said, it is still a unique point in the design space and useful for many cases in which you don't need/want to define a structure.</p>

#### [ Sebastian Ullrich (Oct 04 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bundled%20in%20category_theory/near/135197885):
<p>The binder types (brackets) used in a structure declaration are reflected in the structure's constructor</p>

#### [ Kevin Buzzard (Oct 04 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bundled%20in%20category_theory/near/135199650):
<p>Aah so my post is inaccurate. Thanks Sebastian.</p>

#### [ Sean Leather (Oct 05 2018 at 08:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bundled%20in%20category_theory/near/135236416):
<blockquote>
<p>The binder types (brackets) used in a structure declaration are reflected in the structure's constructor</p>
</blockquote>
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> Ah, of course. Thanks!</p>

#### [ Sean Leather (Oct 05 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bundled%20in%20category_theory/near/135242468):
<p>Here's the resulting <a href="https://github.com/leanprover/mathlib/pull/390" target="_blank" title="https://github.com/leanprover/mathlib/pull/390">PR</a>.</p>

#### [ Johan Commelin (Oct 06 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bundled%20in%20category_theory/near/135303706):
<p>I added a comment: <a href="https://github.com/leanprover/mathlib/pull/390#discussion_r223174490" target="_blank" title="https://github.com/leanprover/mathlib/pull/390#discussion_r223174490">https://github.com/leanprover/mathlib/pull/390#discussion_r223174490</a></p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="kn">reducible</span><span class="o">]</span> <span class="n">def</span> <span class="n">Meas</span> <span class="o">:</span> <span class="kt">Type</span> <span class="o">(</span><span class="n">u</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="n">bundled</span> <span class="n">measurable_space</span>
<span class="kn">instance</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">Meas</span><span class="o">)</span> <span class="o">:</span> <span class="n">measurable_space</span> <span class="n">x</span> <span class="o">:=</span> <span class="n">x</span><span class="bp">.</span><span class="n">inst</span>
</pre></div>


<p>The comment says:<br>
Would it be possible to autogenerate these instances? Everytime we bundle a class we want an instance like this. This probably means that <code>bundled</code> has to become meta. I don't know. But I think it would take away one of those "minor annoyances" if all these instances would just be there, automagically.</p>

#### [ Mario Carneiro (Oct 06 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bundled%20in%20category_theory/near/135303758):
<p>You can't hook in to inductive aux theorem generation, but you can have a derive handler</p>

#### [ Mario Carneiro (Oct 06 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bundled%20in%20category_theory/near/135303764):
<p>You could add an attribute to <code>Meas</code> that does the instance generation</p>

#### [ Mario Carneiro (Oct 06 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bundled%20in%20category_theory/near/135303766):
<p>but I don't think you will gain much over just writing that one line</p>

#### [ Mario Carneiro (Oct 06 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bundled%20in%20category_theory/near/135303809):
<p>it's not like there are that many bundled classes. This is a negligible fraction of the work</p>


{% endraw %}
