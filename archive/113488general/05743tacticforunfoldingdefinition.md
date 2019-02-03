---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/05743tacticforunfoldingdefinition.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [tactic for unfolding definition](https://leanprover-community.github.io/archive/113488general/05743tacticforunfoldingdefinition.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Mar 15 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20unfolding%20definition/near/123764614):
<p>If I've defined <code>def A := B</code> and my goal / hypothesis contains A, how do I replace A with B?</p>

#### [ Moses Schönfinkel (Mar 15 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20unfolding%20definition/near/123764700):
<p><code>unfold</code> :)</p>

#### [ Kenny Lau (Mar 15 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20unfolding%20definition/near/123764708):
<p>I tried it already</p>

#### [ Kenny Lau (Mar 15 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20unfolding%20definition/near/123764717):
<p>here's the context that might help: I'm defining <code>A</code> in the middle of a structure</p>

#### [ Kenny Lau (Mar 15 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20unfolding%20definition/near/123764727):
<div class="codehilite"><pre><span></span>class foo :=
(A := B)
</pre></div>

#### [ Simon Hudon (Mar 15 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20unfolding%20definition/near/123764731):
<p>What happens when you try it?</p>

#### [ Kenny Lau (Mar 15 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20unfolding%20definition/near/123764794):
<div class="codehilite"><pre><span></span>unfold tactic failed, A does not have equational lemmas nor is a projection
</pre></div>

#### [ Moses Schönfinkel (Mar 15 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20unfolding%20definition/near/123764801):
<p>ok first let's eliminate one problem; try <code>delta</code> instead of <code>unfold</code></p>

#### [ Moses Schönfinkel (Mar 15 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20unfolding%20definition/near/123764806):
<p>if that works, you're trying to unfold something you have no "business" unfolding</p>

#### [ Kenny Lau (Mar 15 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20unfolding%20definition/near/123764810):
<div class="codehilite"><pre><span></span>dsimplify tactic failed to simplify
</pre></div>

#### [ Reid Barton (Mar 15 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20unfolding%20definition/near/123764838):
<p>isn't <code>(A := B)</code> there just a default value?</p>

#### [ Kenny Lau (Mar 15 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20unfolding%20definition/near/123764884):
<p>oh... I can't define things inside a structure?</p>

#### [ Simon Hudon (Mar 15 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20unfolding%20definition/near/123764908):
<p>No, that's not possible</p>

#### [ Kenny Lau (Mar 15 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20unfolding%20definition/near/123764913):
<p>ok</p>

#### [ Simon Hudon (Mar 15 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20unfolding%20definition/near/123764956):
<p>That would be useful</p>

#### [ Simon Hudon (Mar 15 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20unfolding%20definition/near/123764972):
<p>They might consider it in the future. Recently, they have adopted implicit fields</p>

#### [ Reid Barton (Mar 15 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20for%20unfolding%20definition/near/123765042):
<p>You can sort of emulate it with multiple structures, like how the algebraic classes are build on top of <code>has_foo</code> classes and so can take advantage of intervening <code>notation</code> declarations</p>


{% endraw %}
