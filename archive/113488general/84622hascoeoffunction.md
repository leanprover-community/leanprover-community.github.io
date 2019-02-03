---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/84622hascoeoffunction.html
---

## Stream: [general](index.html)
### Topic: [has_coe of function](84622hascoeoffunction.html)

---


{% raw %}
#### [ Sean Leather (Aug 08 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_coe%20of%20function/near/131112779):
<p>Are there any problems with a coercion of a function?</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">:</span> <span class="n">has_coe</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">a</span><span class="o">,</span> <span class="n">β₁</span> <span class="n">a</span> <span class="bp">→</span> <span class="n">β₂</span> <span class="n">a</span><span class="o">)</span> <span class="o">(</span><span class="n">embedding</span> <span class="n">β₁</span> <span class="n">β₂</span><span class="o">)</span>
</pre></div>


<p>where <code>embedding</code> is a structure.</p>

#### [ Mario Carneiro (Aug 08 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_coe%20of%20function/near/131112953):
<p>does it work?</p>

#### [ Mario Carneiro (Aug 08 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_coe%20of%20function/near/131113020):
<p>I don't see any obvious issues that it would cause, although it might not work</p>

#### [ Sean Leather (Aug 08 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_coe%20of%20function/near/131113066):
<p>In one place, <code>↑</code> worked. In another, I had to use <code>: sigma.embedding β₁ β₂</code>.</p>

#### [ Mario Carneiro (Aug 08 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_coe%20of%20function/near/131113128):
<p>If <code>B1</code> and <code>B2</code> are metavariables, it will have trouble</p>

#### [ Mario Carneiro (Aug 08 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_coe%20of%20function/near/131113168):
<p>I now recall seeing issues like this with the coercion from <code>order_iso</code> to <code>order_embedding</code></p>

#### [ Sean Leather (Aug 08 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_coe%20of%20function/near/131113221):
<p>Hmm. If I have to use an annotation, it's not really worth it.</p>

#### [ Gabriel Ebner (Aug 08 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_coe%20of%20function/near/131114775):
<p>Yeah, function coercions only trigger if there are no metavariables at all.  This includes universe metavariables as well.</p>

#### [ Simon Hudon (Aug 08 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_coe%20of%20function/near/131130618):
<p>It might be worth defining your own up arrow instead (e.g. <code>⟰</code>)</p>

#### [ Joe Hendrix (Aug 09 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_coe%20of%20function/near/131136017):
<p>I'm actually working through a similar issue, but where I want coercions to trigger over. type with. a single parameter.  I have two types <code>reg : type -&gt; Type</code> and <code>lhs : type -&gt; Type</code>, and <code>\forall tp, has_coe (reg tp) (lhs tp)</code> that I want to trigger even when <code>tp</code> contains metavariables.</p>

#### [ Joe Hendrix (Aug 09 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_coe%20of%20function/near/131136165):
<p>I wish there was some way to control how defined a term had to be before searching for coercions.</p>

#### [ Sebastian Ullrich (Aug 09 2018 at 05:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_coe%20of%20function/near/131147896):
<p><span class="user-mention" data-user-id="110994">@jhx</span> Yes, that is the biggest issue of using type class inference for coercions. We definitely want to fix this in the future, but we don't have a convincing alternative design yet <a href="https://github.com/leanprover/lean/issues/1402" target="_blank" title="https://github.com/leanprover/lean/issues/1402">https://github.com/leanprover/lean/issues/1402</a></p>

#### [ Joe Hendrix (Aug 09 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_coe%20of%20function/near/131152344):
<p>As a workaround, I've introduces a type class <code>has_coe1</code>, and explicitly tell the functions that expect an argument of the given type to use it.</p>
<div class="codehilite"><pre><span></span>class has_coe1 {α:Sort w} (f : α → Sort u) (g : α → Sort v) := (coe : Π{a : α}, f a → g a)

instance has_coe1_refl (α:Sort w) (f : α → Sort u) : has_coe1 f f := ⟨λa f, f⟩
instance all_reg_is_lhs   : has_coe1 reg lhs := sorry

...

section
parameter {f:type → Type}
parameter [has_coe1 f value]

def sext {w:ℕ} {f} [has_coe1 f value] (x:f (bv w)) (o:ℕ) : value (bv o) := ...
</pre></div>


<p>This approach might provide a more general solution to the monad special case mentioned in issue 1402, but still feels fairly special case.</p>


{% endraw %}
