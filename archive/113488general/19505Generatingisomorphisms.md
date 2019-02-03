---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/19505Generatingisomorphisms.html
---

## Stream: [general](index.html)
### Topic: [Generating isomorphisms?](19505Generatingisomorphisms.html)

---


{% raw %}
#### [ Kevin Buzzard (Mar 04 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Generating%20isomorphisms%3F/near/123269348):
<p>I have some definition <code>definition foo (X : Type) : Type := blah</code></p>

#### [ Kevin Buzzard (Mar 04 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Generating%20isomorphisms%3F/near/123269349):
<p>If I have two types <code>X</code> and <code>Y</code> plus isomorphisms <code>f:X\to Y</code> and <code>g:Y\to X</code> (i.e. the composites both ways are the identity functions)</p>

#### [ Kevin Buzzard (Mar 04 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Generating%20isomorphisms%3F/near/123269389):
<p>can I deduce that foo X is isomorphic to foo Y? Does this even make sense?</p>

#### [ Kevin Buzzard (Mar 04 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Generating%20isomorphisms%3F/near/123269490):
<p>an isomorphism version of eq.subst?</p>

#### [ Kevin Buzzard (Mar 04 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Generating%20isomorphisms%3F/near/123269539):
<p>Or does this have to somehow be proved on a case by case basis?</p>

#### [ Kevin Buzzard (Mar 04 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Generating%20isomorphisms%3F/near/123269552):
<p>Mathematicians are so happy to identify objects which are canonically isomorphic and I find this much more of a struggle in Lean.</p>

#### [ Gabriel Ebner (Mar 04 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Generating%20isomorphisms%3F/near/123269600):
<blockquote>
<p>can I deduce that foo X is isomorphic to foo Y?</p>
</blockquote>
<p>Yes, if you define isomorphic as "there exist isomorphisms f and g such that ...". <span class="emoji emoji-1f604" title="smile">:smile:</span></p>
<p>This notion of isomorphism does not allow you to substitute isomorphic structures in arbitrary contexts, though.</p>

#### [ Kevin Buzzard (Mar 04 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Generating%20isomorphisms%3F/near/123269640):
<p>yes this is absolutely how I want to define isomorphic.</p>

#### [ Kevin Buzzard (Mar 04 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Generating%20isomorphisms%3F/near/123269641):
<p>How do I construct the map <code>foo X -&gt; foo Y</code>?</p>

#### [ Gabriel Ebner (Mar 04 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Generating%20isomorphisms%3F/near/123269642):
<p>The axiom of univalence would allow you to lift isomorphisms to equality, then you can substitute in arbitrary contexts.</p>

#### [ Gabriel Ebner (Mar 04 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Generating%20isomorphisms%3F/near/123269648):
<p>Ooops, sorry missed the foo part.</p>

#### [ Kevin Buzzard (Mar 04 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Generating%20isomorphisms%3F/near/123269649):
<p>Oh great :-)</p>

#### [ Kevin Buzzard (Mar 04 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Generating%20isomorphisms%3F/near/123269652):
<p>I don't see any reason why I should be able to get a map foo X -&gt; foo Y just given a map X -&gt; Y</p>

#### [ Kevin Buzzard (Mar 04 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Generating%20isomorphisms%3F/near/123269653):
<p>but can I use the inverse somehow?</p>

#### [ Kevin Buzzard (Mar 04 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Generating%20isomorphisms%3F/near/123269654):
<p>Or is what I want not even true?</p>

#### [ Gabriel Ebner (Mar 04 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Generating%20isomorphisms%3F/near/123269655):
<p>So yeah, univalence is the axiomatic principle that would allow you to do that (in HoTT).</p>

#### [ Gabriel Ebner (Mar 04 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Generating%20isomorphisms%3F/near/123269713):
<p>In Lean, you need to prove it yourself for each instance, such as <code>foo</code> here.</p>

#### [ Mario Carneiro (Mar 04 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Generating%20isomorphisms%3F/near/123269716):
<p>It's definitely not true in general; for example if <code>foo X</code> was <code>X = nat</code></p>

#### [ Mario Carneiro (Mar 04 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Generating%20isomorphisms%3F/near/123269727):
<p>(not true without univalence that is)</p>

#### [ Mario Carneiro (Mar 04 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Generating%20isomorphisms%3F/near/123269789):
<p><span class="user-mention" data-user-email="gebner@gebner.org" data-user-id="110043">@Gabriel Ebner</span> do you know if you can get a contradiction in classical lean from <code>X ~= Y -&gt; X = Y</code>?</p>

#### [ Gabriel Ebner (Mar 04 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Generating%20isomorphisms%3F/near/123270257):
<p>This is an interesting question.  I think it is strictly weaker than univalence because it is not an isomorphism.  It looks inconsistent, but I don't immediately see how to derive a contradiction from it.</p>


{% endraw %}
