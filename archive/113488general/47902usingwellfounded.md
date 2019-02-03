---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/47902usingwellfounded.html
---

## Stream: [general](index.html)
### Topic: [using_well_founded](47902usingwellfounded.html)

---


{% raw %}
#### [ Edward Ayers (Aug 28 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using_well_founded/near/132934326):
<p>I'm looking at RB trees again. I found a really good implementation in Coq that I am copying over to Lean: <a href="https://github.com/coq/coq/blob/a1fc621b943dbf904705dc88ed27c26daf4c5e72/theories/MSets/MSetRBT.v" target="_blank" title="https://github.com/coq/coq/blob/a1fc621b943dbf904705dc88ed27c26daf4c5e72/theories/MSets/MSetRBT.v">https://github.com/coq/coq/blob/a1fc621b943dbf904705dc88ed27c26daf4c5e72/theories/MSets/MSetRBT.v</a><br>
Here is the start of my code:<br>
<a href="https://github.com/EdAyers/mathlib/blob/rb/data/rb.lean" target="_blank" title="https://github.com/EdAyers/mathlib/blob/rb/data/rb.lean">https://github.com/EdAyers/mathlib/blob/rb/data/rb.lean</a><br>
My problem is that it can't prove that my definition of <code>append</code> is terminating automatically. Is there a quick fix for this kind of thing or am I going to have to use well_founded.fix? I can't figure out how to use the <code>using_well_founded</code> keyword.</p>

#### [ Kevin Buzzard (Aug 28 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using_well_founded/near/132934439):
<p>Did you look at the docs at <a href="https://github.com/EdAyers/mathlib/blob/rb/docs/extras/well_founded_recursion.md" target="_blank" title="https://github.com/EdAyers/mathlib/blob/rb/docs/extras/well_founded_recursion.md">https://github.com/EdAyers/mathlib/blob/rb/docs/extras/well_founded_recursion.md</a> ?</p>

#### [ Edward Ayers (Aug 28 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using_well_founded/near/132934463):
<p>Ah thanks I haven't read that one yet</p>

#### [ Kevin Buzzard (Aug 28 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using_well_founded/near/132934551):
<p>I'm not saying it solves your problem, but it does have a bunch of cool tricks.</p>

#### [ Edward Ayers (Aug 28 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using_well_founded/near/132934673):
<p>One of the things it can't show is</p>
<div class="codehilite"><pre><span></span><span class="err">⊢</span> <span class="n">tr</span><span class="bp">.</span><span class="n">sizeof</span> <span class="n">α</span> <span class="n">lr</span> <span class="bp">&lt;</span> <span class="n">tr</span><span class="bp">.</span><span class="n">sizeof</span> <span class="n">α</span> <span class="n">ll</span> <span class="bp">+</span> <span class="o">(</span><span class="n">tr</span><span class="bp">.</span><span class="n">sizeof</span> <span class="n">α</span> <span class="n">lr</span> <span class="bp">+</span> <span class="mi">2</span><span class="o">)</span>
</pre></div>


<p>Is there a tactic that will solve that instantaneously?</p>

#### [ Patrick Massot (Aug 28 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using_well_founded/near/132940133):
<p><a href="https://github.com/leanprover-community/mathlib-nursery/blob/master/src/tactic/monotonicity/interactive.lean#L571-L595" target="_blank" title="https://github.com/leanprover-community/mathlib-nursery/blob/master/src/tactic/monotonicity/interactive.lean#L571-L595">https://github.com/leanprover-community/mathlib-nursery/blob/master/src/tactic/monotonicity/interactive.lean#L571-L595</a> presumably</p>

#### [ Patrick Massot (Aug 28 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using_well_founded/near/132940151):
<p>not yet in mathlib, but you can temporarily add a dependency to this repo</p>

#### [ Patrick Massot (Aug 28 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using_well_founded/near/132940196):
<p>What's the problem with corelib rbtrees?</p>

#### [ Edward Ayers (Aug 28 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using_well_founded/near/132940302):
<p>Corelib rbtrees don't have <code>erase</code></p>

#### [ Edward Ayers (Aug 28 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using_well_founded/near/132940317):
<p>And there are no proofs about them.</p>

#### [ Patrick Massot (Aug 28 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using_well_founded/near/132940341):
<p>oh</p>

#### [ Edward Ayers (Aug 28 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using_well_founded/near/132941632):
<p>I fixed this by adding my own has_well_founded instance</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">custom_wf</span> <span class="o">:</span> <span class="n">has_well_founded</span> <span class="o">(</span><span class="n">tr</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">tr</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span> <span class="n">has_well_founded_of_has_sizeof</span> <span class="o">(</span><span class="n">tr</span> <span class="n">α</span> <span class="bp">×</span> <span class="n">tr</span> <span class="n">α</span><span class="o">)</span>
</pre></div>

#### [ Edward Ayers (Aug 28 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using_well_founded/near/132941692):
<p>Before it was using wf using lexical ordering which was throwing it.</p>

#### [ Edward Ayers (Aug 28 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using_well_founded/near/132941711):
<p>at least I think that's why</p>

#### [ Leonardo de Moura (Aug 28 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using_well_founded/near/132952390):
<p><span class="user-mention" data-user-id="121918">@Edward Ayers</span> The proofs are here <a href="https://github.com/leanprover/lean/tree/master/library/data/rbtree" target="_blank" title="https://github.com/leanprover/lean/tree/master/library/data/rbtree">https://github.com/leanprover/lean/tree/master/library/data/rbtree</a></p>

#### [ Kevin Buzzard (Aug 28 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using_well_founded/near/132953705):
<p>(deleted)</p>

#### [ Edward Ayers (Aug 28 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/using_well_founded/near/132953908):
<p>thanks Leo! sorry I didn't spot them.</p>


{% endraw %}
