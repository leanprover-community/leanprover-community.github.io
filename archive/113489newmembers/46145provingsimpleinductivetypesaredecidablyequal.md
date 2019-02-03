---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/46145provingsimpleinductivetypesaredecidablyequal.html
---

## Stream: [new members](index.html)
### Topic: [proving simple inductive types are decidably equal](46145provingsimpleinductivetypesaredecidablyequal.html)

---


{% raw %}
#### [ Edward Ayers (Nov 06 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20simple%20inductive%20types%20are%20decidably%20equal/near/146870382):
<p>Suppose I make</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">foo</span> <span class="bp">|</span><span class="n">A</span> <span class="bp">|</span><span class="n">B</span> <span class="bp">|</span><span class="n">C</span> <span class="bp">|</span><span class="n">D</span> <span class="bp">|</span><span class="n">E</span>
</pre></div>


<p>How can I show that<code>foo</code> is decidably equal with minimal faff?</p>

#### [ Floris van Doorn (Nov 06 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20simple%20inductive%20types%20are%20decidably%20equal/near/146870461):
<div class="codehilite"><pre><span></span>@[derive decidable_eq] inductive foo |A |B |C |D |E
</pre></div>

#### [ Edward Ayers (Nov 06 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20simple%20inductive%20types%20are%20decidably%20equal/near/146870516):
<p>win for Lean</p>

#### [ Edward Ayers (Nov 06 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20simple%20inductive%20types%20are%20decidably%20equal/near/146870537):
<p>What else can I <code>@[derive ...]</code>?</p>

#### [ Floris van Doorn (Nov 06 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20simple%20inductive%20types%20are%20decidably%20equal/near/146870660):
<p>Not sure. In mathlib, if I search for derive, I only find <code>derive decidable_eq</code> and <code>derive has_reflect</code>.</p>

#### [ Edward Ayers (Nov 06 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20simple%20inductive%20types%20are%20decidably%20equal/near/146870661):
<p>I found <code>has_sizeof</code> in the wild</p>

#### [ Scott Morrison (Nov 06 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20simple%20inductive%20types%20are%20decidably%20equal/near/146895917):
<p>I would love to write some "functorial" derive handlers, for automatically showing constructions are functorial with respect to either morphisms in their arguments, or isomorphisms in their arguments. This would be part of a bigger program to do transport of structure.</p>

#### [ Patrick Massot (Nov 06 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20simple%20inductive%20types%20are%20decidably%20equal/near/146896228):
<p>Today Cyril worked quite a lot on transport stuff.</p>

#### [ Scott Morrison (Nov 06 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20simple%20inductive%20types%20are%20decidably%20equal/near/146897672):
<p>Ah, okay, what approach are they taking?</p>

#### [ Patrick Massot (Nov 06 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20simple%20inductive%20types%20are%20decidably%20equal/near/146897712):
<p>parametricity for free, or something like that</p>

#### [ Patrick Massot (Nov 06 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20simple%20inductive%20types%20are%20decidably%20equal/near/146897752):
<p><a href="https://hal.inria.fr/hal-01559073" target="_blank" title="https://hal.inria.fr/hal-01559073">https://hal.inria.fr/hal-01559073</a></p>

#### [ Scott Morrison (Nov 06 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20simple%20inductive%20types%20are%20decidably%20equal/near/146897881):
<p>I would really like some feedback on my <code>iso_induction</code> approach sketched in the comments of <a href="https://github.com/leanprover/mathlib/issues/408" target="_blank" title="https://github.com/leanprover/mathlib/issues/408">https://github.com/leanprover/mathlib/issues/408</a>, and the very initial branch at <a href="https://github.com/leanprover-community/mathlib/commit/fc31a8c81040f2a7e087df890f1c848ff6d34eff" target="_blank" title="https://github.com/leanprover-community/mathlib/commit/fc31a8c81040f2a7e087df890f1c848ff6d34eff">https://github.com/leanprover-community/mathlib/commit/fc31a8c81040f2a7e087df890f1c848ff6d34eff</a>. </p>
<p>It needs more examples of definitions shown to be functorial in their arguments (hopefully automatically) before you can really see how it would work.</p>


{% endraw %}
