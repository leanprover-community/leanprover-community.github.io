---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/96301mutualinductivedefinition.html
---

## Stream: [new members](index.html)
### Topic: [mutual inductive definition](96301mutualinductivedefinition.html)

---


{% raw %}
#### [ Shaun Steenkamp (Nov 16 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mutual%20inductive%20definition/near/147808981):
<p>can one of you explain why I cannot get this mutual inductive definition to work?</p>
<div class="codehilite"><pre><span></span><span class="n">mutual</span> <span class="kn">inductive</span> <span class="n">Foo</span><span class="o">,</span> <span class="n">Bar</span>
<span class="k">with</span> <span class="n">Foo</span> <span class="o">:</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">bizz</span> <span class="o">:</span> <span class="n">Foo</span>
<span class="bp">|</span> <span class="n">buzz</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">Foo</span><span class="o">}</span> <span class="o">:</span> <span class="n">Bar</span> <span class="n">f</span> <span class="bp">→</span> <span class="n">Foo</span>
<span class="k">with</span> <span class="n">Bar</span> <span class="o">:</span> <span class="n">Foo</span> <span class="bp">→</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">baz</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">Foo</span><span class="o">)</span> <span class="o">:</span> <span class="n">Bar</span> <span class="n">f</span>
</pre></div>


<p>For reference, the following works in Agda</p>
<div class="codehilite"><pre><span></span><span class="kr">mutual</span>
  <span class="kr">data</span> Foo <span class="ow">:</span> <span class="kt">Set</span> <span class="kr">where</span>
    <span class="nf">bizz</span> <span class="ow">:</span> Foo
    <span class="nf">buzz</span> <span class="ow">:</span> <span class="o">{</span>f <span class="ow">:</span> Foo<span class="o">}</span> <span class="ow">→</span> Bar f <span class="ow">→</span> Foo

  <span class="kr">data</span> Bar <span class="ow">:</span> Foo <span class="ow">→</span> <span class="kt">Set</span> <span class="kr">where</span>
    <span class="nf">baz</span> <span class="ow">:</span> <span class="o">(</span>f <span class="ow">:</span> Foo<span class="o">)</span> <span class="ow">→</span> Bar f
</pre></div>

#### [ Mario Carneiro (Nov 16 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mutual%20inductive%20definition/near/147809137):
<p>this is called an inductive-recursive definition, and it is stronger than lean's axiomatics</p>

#### [ Mario Carneiro (Nov 16 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mutual%20inductive%20definition/near/147809215):
<p>There may be another way to encode the type you want, but inductive recursive definitions can be used to prove DTT is consistent, so lean can't do it</p>

#### [ Keeley Hoek (Nov 16 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mutual%20inductive%20definition/near/147809656):
<p>Incidentally, Mario, were you working on a Lean consistency project at some point?</p>

#### [ Shaun Steenkamp (Nov 16 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mutual%20inductive%20definition/near/147809895):
<p>What is DTT?</p>

#### [ Patrick Massot (Nov 16 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mutual%20inductive%20definition/near/147810111):
<p>dependent type theory</p>

#### [ Patrick Massot (Nov 16 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mutual%20inductive%20definition/near/147810119):
<p>That's the name of the game we are playing</p>

#### [ Mario Carneiro (Nov 16 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mutual%20inductive%20definition/near/147811271):
<p>yes, I'll be defending my masters thesis in a few weeks and lean consistency is in it</p>

#### [ Mario Carneiro (Nov 16 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mutual%20inductive%20definition/near/147811346):
<p><a href="https://github.com/digama0/lean-type-theory/releases/tag/v0.21" target="_blank" title="https://github.com/digama0/lean-type-theory/releases/tag/v0.21">https://github.com/digama0/lean-type-theory/releases/tag/v0.21</a></p>

#### [ Kenny Lau (Nov 16 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mutual%20inductive%20definition/near/147811386):
<p>so, is lean consistent?</p>

#### [ Abhimanyu Pallavi Sudhir (Nov 16 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mutual%20inductive%20definition/near/147811742):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> How is that not independent?</p>

#### [ Mario Carneiro (Nov 16 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mutual%20inductive%20definition/near/147812715):
<p>yes, assuming some large cardinal assumptions</p>

#### [ Mario Carneiro (Nov 16 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mutual%20inductive%20definition/near/147812723):
<p>which is the usual story with consistency proofs</p>

#### [ Johannes Hölzl (Nov 16 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mutual%20inductive%20definition/near/147813619):
<p>I think this shape is called inductive-inductive: mutual inductive types where at least one is indexed by the other one, inductive-recursive means to mutually define inductive types and recursive definitions where at least one inductive type depends on the recursive definition.<br>
I think inductive-inductive can be reduced to inductive, inductive-recursive cannot</p>

#### [ Mario Carneiro (Nov 16 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mutual%20inductive%20definition/near/147813885):
<p>you might be right about the name, but I'm pretty sure inductive-inductive is also axiomatically strong</p>

#### [ Mario Carneiro (Nov 16 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mutual%20inductive%20definition/near/147813968):
<p>because you can define the well typed terms of DTT by induction-induction with the set of well formed contexts and the set of types in a context</p>

#### [ Mario Carneiro (Nov 16 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mutual%20inductive%20definition/near/147814054):
<p>Inductive recursive can be reduced to inductive inductive, I think, where the recursive function becomes a functional relation</p>

#### [ Johannes Hölzl (Nov 16 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mutual%20inductive%20definition/near/147814450):
<p>Ah, or it was this way round</p>

#### [ Shaun Steenkamp (Nov 16 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mutual%20inductive%20definition/near/147817435):
<blockquote>
<p>There may be another way to encode the type you want, but inductive recursive definitions can be used to prove DTT is consistent, so lean can't do it</p>
</blockquote>
<p>Consistent with respect to what?</p>

#### [ Johannes Hölzl (Nov 16 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mutual%20inductive%20definition/near/147821293):
<p>with respect to DTT with a larger type universe and inductive recursive definitions (I guess)</p>

#### [ Floris van Doorn (Nov 16 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/mutual%20inductive%20definition/near/147821961):
<p>This is indeed an inductive-inductive definition. I think adding these won't increase the proof stength of the system. In extensional type theory, inductive-inductive definitions can be defined from indexed inductive types, but I don't think it's known in whether this is the case in intensional type theory.<br>
Inductive-recursive definitions indeed do increase the proof stength of the system: you can build a (Tarski) universe using induction-recursion.<br>
Ncatlab links:<br>
<a href="https://ncatlab.org/nlab/show/inductive-inductive+type" target="_blank" title="https://ncatlab.org/nlab/show/inductive-inductive+type">https://ncatlab.org/nlab/show/inductive-inductive+type</a><br>
<a href="https://ncatlab.org/nlab/show/inductive-recursive+type" target="_blank" title="https://ncatlab.org/nlab/show/inductive-recursive+type">https://ncatlab.org/nlab/show/inductive-recursive+type</a></p>


{% endraw %}
