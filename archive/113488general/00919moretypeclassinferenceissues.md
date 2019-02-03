---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/00919moretypeclassinferenceissues.html
---

## Stream: [general](index.html)
### Topic: [more type class inference issues](00919moretypeclassinferenceissues.html)

---


{% raw %}
#### [ Kevin Buzzard (Apr 19 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125320059):
<p>It seems to me that for classes like <code>ring</code>defined in core lean or mathlib, you are kind of supposed to use type class inference to make them work.</p>

#### [ Kevin Buzzard (Apr 19 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125320070):
<p>For example, <code>class is_ring_hom {α : Type u} {β : Type v} [ring α] [ring β] (f : α → β) : Prop := ...</code> is now in mathlib</p>

#### [ Kevin Buzzard (Apr 19 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125320128):
<p>now I don't actually know how to make type class inference work in all cases, so I spend some of my time working around it.</p>

#### [ Kevin Buzzard (Apr 19 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125320162):
<p>Here's an example. I have the following structure in my code:</p>

#### [ Kevin Buzzard (Apr 19 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125320181):
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">presheaf_of_rings</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">[</span><span class="n">T</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span> <span class="kn">extends</span> <span class="n">presheaf_of_types</span> <span class="n">α</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">Fring</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">U</span><span class="o">}</span> <span class="o">(</span><span class="n">OU</span> <span class="o">:</span> <span class="n">T</span><span class="bp">.</span><span class="n">is_open</span> <span class="n">U</span><span class="o">),</span> <span class="n">comm_ring</span> <span class="o">(</span><span class="n">F</span> <span class="n">OU</span><span class="o">))</span>
<span class="o">(</span><span class="n">res_is_ring_morphism</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">U</span> <span class="n">V</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">OU</span> <span class="o">:</span> <span class="n">T</span><span class="bp">.</span><span class="n">is_open</span> <span class="n">U</span><span class="o">)</span> <span class="o">(</span><span class="n">OV</span> <span class="o">:</span> <span class="n">T</span><span class="bp">.</span><span class="n">is_open</span> <span class="n">V</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">V</span> <span class="err">⊆</span> <span class="n">U</span><span class="o">),</span>
  <span class="n">is_ring_hom</span> <span class="o">(</span><span class="n">res</span> <span class="n">U</span> <span class="n">V</span> <span class="n">OU</span> <span class="n">OV</span> <span class="n">H</span><span class="o">))</span>
</pre></div>

#### [ Kevin Buzzard (Apr 19 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125320267):
<p>Yesterday, <code>is_ring_hom</code> was about <code>comm_ring</code>, and I used it in my code via <code>@is_ring_hom _ _ (FPR.Fring HU) (GPR.Fring HU) ...</code>, explicitly giving the proof that something was a comm_ring.</p>

#### [ Kevin Buzzard (Apr 19 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125320275):
<p>But now it's changed to ring and so either I figure out a way of explicitly turning a comm_ring into a ring</p>

#### [ Kevin Buzzard (Apr 19 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125320318):
<p>or I ask here about how I should be doing this properly.</p>

#### [ Kevin Buzzard (Apr 19 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125320334):
<p>In short, Lean / mathlib seems to want me, by default, to prove that things are rings by type class inference.</p>

#### [ Kevin Buzzard (Apr 19 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125320369):
<p>How do I ensure that every time I access a <code>presheaf_of_rings</code> as defined above, <code>presheaf_of_rings.Fring</code> is added to the type class inference system?</p>

#### [ Kevin Buzzard (Apr 19 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125320463):
<p>Is there some clever trick involving an <code>instance</code> statement directly after the definition of <code>presheaf_of_rings</code>?</p>

#### [ Kevin Buzzard (Apr 19 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125320625):
<p>Oh yeah :-)</p>

#### [ Kevin Buzzard (Apr 19 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125320629):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">presheaf_of_rings_Fring</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">[</span><span class="n">T</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">U</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">FPR</span> <span class="o">:</span> <span class="n">presheaf_of_rings</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">OU</span> <span class="o">:</span> <span class="n">T</span><span class="bp">.</span><span class="n">is_open</span> <span class="n">U</span><span class="o">)</span> <span class="o">:</span> <span class="n">comm_ring</span> <span class="o">(</span><span class="n">FPR</span><span class="bp">.</span><span class="n">F</span> <span class="n">OU</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">FPR</span><span class="bp">.</span><span class="n">Fring</span> <span class="n">OU</span>
</pre></div>

#### [ Kevin Buzzard (Apr 19 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125320631):
<p>As you were :-)</p>

#### [ Kevin Buzzard (Apr 19 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125322233):
<p>What does this mean?</p>

#### [ Kevin Buzzard (Apr 19 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125322237):
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">presheaf_of_rings</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">[</span><span class="n">T</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span> <span class="kn">extends</span> <span class="n">presheaf_of_types</span> <span class="n">α</span> <span class="o">:=</span>
<span class="o">[</span><span class="n">Fring</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">U</span><span class="o">}</span> <span class="o">(</span><span class="n">OU</span> <span class="o">:</span> <span class="n">T</span><span class="bp">.</span><span class="n">is_open</span> <span class="n">U</span><span class="o">),</span> <span class="n">comm_ring</span> <span class="o">(</span><span class="n">F</span> <span class="n">OU</span><span class="o">)]</span>
<span class="o">(</span><span class="n">res_is_ring_morphism</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">U</span> <span class="n">V</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">OU</span> <span class="o">:</span> <span class="n">T</span><span class="bp">.</span><span class="n">is_open</span> <span class="n">U</span><span class="o">)</span> <span class="o">(</span><span class="n">OV</span> <span class="o">:</span> <span class="n">T</span><span class="bp">.</span><span class="n">is_open</span> <span class="n">V</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">V</span> <span class="err">⊆</span> <span class="n">U</span><span class="o">),</span>
  <span class="n">is_ring_hom</span> <span class="o">(</span><span class="n">res</span> <span class="n">U</span> <span class="n">V</span> <span class="n">OU</span> <span class="n">OV</span> <span class="n">H</span><span class="o">))</span>
</pre></div>

#### [ Kevin Buzzard (Apr 19 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125322241):
<p>Is that a thing? It doesn't seem to be a thing.</p>

#### [ Chris Hughes (Apr 19 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125322275):
<p><code>comm_ring.to_ring</code> might help</p>

#### [ Chris Hughes (Apr 19 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125322379):
<p><code>attribute [instance] presheaf_of_rings.Fring</code> might also help</p>

#### [ Chris Hughes (Apr 19 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125322454):
<p>Just add that ^ line after the definition of <code>presheaf_of_rings</code></p>

#### [ Kevin Buzzard (Apr 19 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125323095):
<p>Oh that's a better way :-) Thanks Chris, I'm glad I asked now.</p>

#### [ Kevin Buzzard (Apr 19 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125323244):
<p>I specifically wanted to avoid <code>comm_ring.to_ring</code> as I am pretty sure that the whole point of type class inference is that the end user shouldn't have to use such functions.</p>

#### [ Kevin Buzzard (Apr 19 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125324599):
<p>Actually, is the following a potential problem with the type class system:</p>

#### [ Kevin Buzzard (Apr 19 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125324670):
<p>My understanding (incomplete) of something Johannes was saying a few days ago to Patrick, was that the reason <code>topological_space</code> is defined as a <code>structure</code> with the <code>class</code> attribute added later, rather than a <code>class</code> directly, was that there were occasions when you might want to consider more than one topological space structure on a given type.</p>

#### [ Kevin Buzzard (Apr 19 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125324680):
<p>but ring is defined as a class in core lean</p>

#### [ Kevin Buzzard (Apr 19 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125324721):
<p>so what about the person who wants to prove theorems about putting different ring structures on a type?</p>

#### [ Kevin Buzzard (Apr 19 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125324728):
<p>Are they forced to abandon the type class system, and then they really would have to learn the names of all the theorems mapping a ring to an additive group etc?</p>

#### [ Kevin Buzzard (Apr 19 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125324903):
<p>And here's another question: what if the ring instance is in the same structure?</p>

#### [ Kevin Buzzard (Apr 19 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125324906):
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">presheaf_of_rings_on_basis</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">TX</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">X</span><span class="o">]</span>
  <span class="o">{</span><span class="n">B</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">set</span> <span class="n">X</span><span class="o">)}</span> <span class="o">(</span><span class="n">HB</span> <span class="o">:</span> <span class="n">topological_space</span><span class="bp">.</span><span class="n">is_topological_basis</span> <span class="n">B</span><span class="o">)</span> <span class="kn">extends</span> <span class="n">presheaf_of_types_on_basis</span> <span class="n">HB</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">Fring</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">U</span><span class="o">}</span> <span class="n">BU</span><span class="o">,</span> <span class="n">comm_ring</span> <span class="o">(</span><span class="n">F</span> <span class="n">BU</span><span class="o">))</span>
<span class="o">(</span><span class="n">res_is_ring_morphism</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">U</span> <span class="n">V</span><span class="o">}</span> <span class="o">(</span><span class="n">BU</span> <span class="o">:</span> <span class="n">U</span> <span class="err">∈</span> <span class="n">B</span><span class="o">)</span> <span class="o">(</span><span class="n">BV</span> <span class="o">:</span> <span class="n">V</span> <span class="err">∈</span> <span class="n">B</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">V</span> <span class="err">⊆</span> <span class="n">U</span><span class="o">),</span>
  <span class="bp">@</span><span class="n">is_ring_hom</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="bp">@</span><span class="n">Fring</span> <span class="n">U</span> <span class="n">BU</span><span class="o">)</span> <span class="o">(</span><span class="n">Fring</span> <span class="n">BV</span><span class="o">)</span> <span class="o">(</span><span class="bp">@</span><span class="n">res</span> <span class="n">U</span> <span class="n">V</span> <span class="n">BU</span> <span class="n">BV</span> <span class="n">H</span><span class="o">))</span>
</pre></div>

#### [ Kevin Buzzard (Apr 19 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125324987):
<p>Here a <code>presheaf_of_rings_on_basis</code> has <code>Fring</code> saying something is a commutative ring, and then <code>res_is_ring_morphism</code> which immediately wants to use type class inference to deduce that <code>Fring U BU</code> is a ring. Now do I really have to use <code>comm_ring.to_ring</code>?</p>

#### [ Kevin Buzzard (Apr 19 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125325099):
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">presheaf_of_rings_on_basis</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">TX</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">X</span><span class="o">]</span>
  <span class="o">{</span><span class="n">B</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">set</span> <span class="n">X</span><span class="o">)}</span> <span class="o">(</span><span class="n">HB</span> <span class="o">:</span> <span class="n">topological_space</span><span class="bp">.</span><span class="n">is_topological_basis</span> <span class="n">B</span><span class="o">)</span> <span class="kn">extends</span> <span class="n">presheaf_of_types_on_basis</span> <span class="n">HB</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">Fring</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">U</span><span class="o">}</span> <span class="o">(</span><span class="n">BU</span> <span class="o">:</span> <span class="n">U</span> <span class="err">∈</span> <span class="n">B</span><span class="o">),</span> <span class="n">comm_ring</span> <span class="o">(</span><span class="n">F</span> <span class="n">BU</span><span class="o">))</span>
<span class="o">(</span><span class="n">res_is_ring_morphism</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">U</span> <span class="n">V</span><span class="o">}</span> <span class="o">(</span><span class="n">BU</span> <span class="o">:</span> <span class="n">U</span> <span class="err">∈</span> <span class="n">B</span><span class="o">)</span> <span class="o">(</span><span class="n">BV</span> <span class="o">:</span> <span class="n">V</span> <span class="err">∈</span> <span class="n">B</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">V</span> <span class="err">⊆</span> <span class="n">U</span><span class="o">),</span>
  <span class="bp">@</span><span class="n">is_ring_hom</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="bp">@</span><span class="n">comm_ring</span><span class="bp">.</span><span class="n">to_ring</span> <span class="bp">_</span> <span class="o">(</span><span class="n">Fring</span> <span class="n">BU</span><span class="o">))</span> <span class="o">(</span><span class="bp">@</span><span class="n">comm_ring</span><span class="bp">.</span><span class="n">to_ring</span> <span class="bp">_</span> <span class="o">(</span><span class="n">Fring</span> <span class="n">BV</span><span class="o">))</span> <span class="o">(</span><span class="bp">@</span><span class="n">res</span> <span class="n">U</span> <span class="n">V</span> <span class="n">BU</span> <span class="n">BV</span> <span class="n">H</span><span class="o">))</span>
</pre></div>

#### [ Kevin Buzzard (Apr 19 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125325160):
<p>Type class inference is failing me badly here. Sorry for no MWE, hopefully people can see the problem; Lean wants me to use type class inference to prove that commutative rings are rings but I don't know how to make this happen in this situation.</p>

#### [ Mario Carneiro (Apr 19 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125325164):
<p>that's what the brackets inside the structure are for</p>

#### [ Kevin Buzzard (Apr 19 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125325231):
<p>?</p>

#### [ Kevin Buzzard (Apr 19 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125325233):
<p>Oh!</p>

#### [ Kevin Buzzard (Apr 19 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125325247):
<p>:-)</p>

#### [ Kevin Buzzard (Apr 19 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125325251):
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">presheaf_of_rings_on_basis</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">TX</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">X</span><span class="o">]</span>
  <span class="o">{</span><span class="n">B</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">set</span> <span class="n">X</span><span class="o">)}</span> <span class="o">(</span><span class="n">HB</span> <span class="o">:</span> <span class="n">topological_space</span><span class="bp">.</span><span class="n">is_topological_basis</span> <span class="n">B</span><span class="o">)</span> <span class="kn">extends</span> <span class="n">presheaf_of_types_on_basis</span> <span class="n">HB</span> <span class="o">:=</span>
<span class="o">[</span><span class="n">Fring</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">U</span><span class="o">}</span> <span class="o">(</span><span class="n">BU</span> <span class="o">:</span> <span class="n">U</span> <span class="err">∈</span> <span class="n">B</span><span class="o">),</span> <span class="n">comm_ring</span> <span class="o">(</span><span class="n">F</span> <span class="n">BU</span><span class="o">)]</span>
<span class="o">(</span><span class="n">res_is_ring_morphism</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">U</span> <span class="n">V</span><span class="o">}</span> <span class="o">(</span><span class="n">BU</span> <span class="o">:</span> <span class="n">U</span> <span class="err">∈</span> <span class="n">B</span><span class="o">)</span> <span class="o">(</span><span class="n">BV</span> <span class="o">:</span> <span class="n">V</span> <span class="err">∈</span> <span class="n">B</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">V</span> <span class="err">⊆</span> <span class="n">U</span><span class="o">),</span>
  <span class="n">is_ring_hom</span> <span class="o">(</span><span class="bp">@</span><span class="n">res</span> <span class="n">U</span> <span class="n">V</span> <span class="n">BU</span> <span class="n">BV</span> <span class="n">H</span><span class="o">))</span>
</pre></div>

#### [ Kevin Buzzard (Apr 19 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125325270):
<p>So just to be clear -- the square brackets inside the structure trigger type class inference only within the structure definitions?</p>

#### [ Mario Carneiro (Apr 19 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125325325):
<p>I think they also mark it as an instance, but you should <code>#print</code> to be sure</p>

#### [ Kevin Buzzard (Apr 19 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125325334):
<p>I don't think they do</p>

#### [ Kevin Buzzard (Apr 19 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125325344):
<p>because that was what prompted the question about why the square brackets within the structure definition was even a thing</p>

#### [ Kevin Buzzard (Apr 19 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125325345):
<p>earlier</p>

#### [ Mario Carneiro (Apr 19 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125325421):
<p>you shouldn't need <code>@res</code> either</p>

#### [ Kevin Buzzard (Apr 19 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125325481):
<p>yes, that's gone now</p>

#### [ Kevin Buzzard (Apr 19 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125325517):
<p>But your change of is_ring_hom from [comm_ring] to [ring] has thrown up one final type class inference issue which I can't solve</p>

#### [ Kevin Buzzard (Apr 19 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125325520):
<p>possibly because it's not solvable</p>

#### [ Kevin Buzzard (Apr 19 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125325528):
<p>I think I do need an MWE for this one</p>

#### [ Kevin Buzzard (Apr 19 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125325814):
<p>Oh no it's Ok, indeed I am now pretty convinced that the square brackets in the structure definition do not insert anything into the type class inference system globally</p>

#### [ Kevin Buzzard (Apr 19 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125325890):
<p>because my final problem was solved by Chris' instance trick.</p>

#### [ Kevin Buzzard (Apr 19 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125325902):
<p>Oh this is great. I got stuck on these problems before and blamed it on the type class inference system not being smart enough.</p>

#### [ Kevin Buzzard (Apr 19 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125325907):
<p>I should have asked for help earlier.</p>

#### [ Kevin Buzzard (Apr 19 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125325924):
<p>Patrick said the same thing -- I told him to give up on coercions because they weren't smart enough</p>

#### [ Kevin Buzzard (Apr 19 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125325932):
<p>and he pointed out that whenever he'd got stuck before, you (Mario) had had a trick which got him through.</p>

#### [ Kevin Buzzard (Apr 19 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125326155):
<p>Here's a weird question. It feels to me like <code>comm_ring.to_ring</code> should not be the kind of function which end users have to worry about, because when the devs made <code>ring</code> a typeclass they are somehow declaring that Lean will automatically take care of inferences of this nature.</p>

#### [ Kevin Buzzard (Apr 19 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125326166):
<p>Am I right in thinking that an end user should only have to invoke <code>comm_ring.to_ring</code> in exceptional circumstances?</p>

#### [ Kevin Buzzard (Apr 19 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125326183):
<p>(says the person who just managed to avoid all uses of it when his code broke in lots of places)</p>

#### [ Kevin Buzzard (Apr 19 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125326192):
<p>(when a comm_ring changed to a ring)</p>

#### [ Kevin Buzzard (Apr 19 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125326297):
<p>Aah, more generally should an end user never have to explicitly invoke any theorem tagged with the <code>instance</code> attribute?</p>

#### [ Kevin Buzzard (Apr 19 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125326358):
<p>(unless they are putting more than one structure of a typeclass onto one type, say)</p>

#### [ Chris Hughes (Apr 20 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125328614):
<p>Sorry to hijack your thread, but I have a typeclass issue of my own</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">int</span><span class="bp">.</span><span class="n">modeq</span>

<span class="kn">instance</span> <span class="n">Zmod_setoid</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">}</span> <span class="o">:</span> <span class="n">setoid</span> <span class="bp">ℤ</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">r</span> <span class="o">:=</span> <span class="n">int</span><span class="bp">.</span><span class="n">modeq</span> <span class="n">n</span><span class="o">,</span>
  <span class="n">iseqv</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">int</span><span class="bp">.</span><span class="n">modeq</span><span class="bp">.</span><span class="n">refl</span><span class="o">,</span> <span class="bp">@</span><span class="n">int</span><span class="bp">.</span><span class="n">modeq</span><span class="bp">.</span><span class="n">symm</span> <span class="n">n</span><span class="o">,</span> <span class="bp">@</span><span class="n">int</span><span class="bp">.</span><span class="n">modeq</span><span class="bp">.</span><span class="n">trans</span> <span class="n">n</span><span class="bp">⟩</span> <span class="o">}</span>

<span class="n">def</span> <span class="n">Zmod</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Type</span> <span class="o">:=</span> <span class="n">quotient</span> <span class="o">(</span><span class="bp">@</span><span class="n">Zmod_setoid</span> <span class="n">n</span><span class="o">)</span>

<span class="kn">private</span> <span class="n">def</span> <span class="n">add_aux</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">}</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">Zmod</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span> <span class="n">Zmod</span> <span class="n">n</span> <span class="o">:=</span>
<span class="n">quotient</span><span class="bp">.</span><span class="n">lift_on₂</span> <span class="n">a</span> <span class="n">b</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="err">⟦</span><span class="n">a</span> <span class="bp">+</span> <span class="n">b</span><span class="err">⟧</span><span class="o">)</span> <span class="n">sorry</span>
</pre></div>


<p>It cannot infer the <code>setoid</code> instance, probably because it requires an argument. Not sure of a good solution to this.</p>

#### [ Mario Carneiro (Apr 20 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125328872):
<p>This is a common problem; I think the <code>lift_on</code> recursor does not correctly deliver the expected type to the lambda. The usual solution is to add an ascription at the lambda:</p>
<div class="codehilite"><pre><span></span>private def add_aux {n : ℤ} (a b : Zmod n) : Zmod n :=
quotient.lift_on₂ a b (λ a b, (⟦a + b⟧ : Zmod n)) sorry
</pre></div>

#### [ Chris Hughes (Apr 20 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125328985):
<p>Still not working I'm getting this message</p>
<div class="codehilite"><pre><span></span>synthesized type class instance is not definitionally equal to expression inferred by typing rules, synthesized
  ⁇
inferred
  Zmod_setoid n
</pre></div>

#### [ Kevin Buzzard (Apr 20 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125331043):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">int</span><span class="bp">.</span><span class="n">modeq</span>

<span class="kn">instance</span> <span class="n">Zmod_setoid</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">}</span> <span class="o">:</span> <span class="n">setoid</span> <span class="bp">ℤ</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">r</span> <span class="o">:=</span> <span class="n">int</span><span class="bp">.</span><span class="n">modeq</span> <span class="n">n</span><span class="o">,</span>
  <span class="n">iseqv</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">int</span><span class="bp">.</span><span class="n">modeq</span><span class="bp">.</span><span class="n">refl</span><span class="o">,</span> <span class="bp">@</span><span class="n">int</span><span class="bp">.</span><span class="n">modeq</span><span class="bp">.</span><span class="n">symm</span> <span class="n">n</span><span class="o">,</span> <span class="bp">@</span><span class="n">int</span><span class="bp">.</span><span class="n">modeq</span><span class="bp">.</span><span class="n">trans</span> <span class="n">n</span><span class="bp">⟩</span> <span class="o">}</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">setoid</span> <span class="bp">ℤ</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span> <span class="c1">-- fails</span>
</pre></div>

#### [ Kevin Buzzard (Apr 20 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125331049):
<p>I'm not sure that I understand how parametrized instances work.</p>

#### [ Kevin Buzzard (Apr 20 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125331179):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">int</span><span class="bp">.</span><span class="n">modeq</span>

<span class="kn">instance</span> <span class="n">Zmod_setoid</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">}</span> <span class="o">:</span> <span class="n">setoid</span> <span class="bp">ℤ</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">r</span> <span class="o">:=</span> <span class="n">int</span><span class="bp">.</span><span class="n">modeq</span> <span class="n">n</span><span class="o">,</span>
  <span class="n">iseqv</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">int</span><span class="bp">.</span><span class="n">modeq</span><span class="bp">.</span><span class="n">refl</span><span class="o">,</span> <span class="bp">@</span><span class="n">int</span><span class="bp">.</span><span class="n">modeq</span><span class="bp">.</span><span class="n">symm</span> <span class="n">n</span><span class="o">,</span> <span class="bp">@</span><span class="n">int</span><span class="bp">.</span><span class="n">modeq</span><span class="bp">.</span><span class="n">trans</span> <span class="n">n</span><span class="bp">⟩</span> <span class="o">}</span>

<span class="n">def</span> <span class="n">Zmod</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Type</span> <span class="o">:=</span> <span class="n">quotient</span> <span class="o">(</span><span class="bp">@</span><span class="n">Zmod_setoid</span> <span class="n">n</span><span class="o">)</span>

<span class="bp">#</span><span class="kn">check</span> <span class="o">(</span><span class="err">⟦</span><span class="mi">3</span><span class="err">⟧</span> <span class="o">:</span> <span class="n">Zmod</span> <span class="mi">5</span><span class="o">)</span> <span class="c1">-- failed to synthesize type class instance for setoid ℤ</span>
</pre></div>

#### [ Kevin Buzzard (Apr 20 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125331180):
<p>I'm even less sure now</p>

#### [ Kevin Buzzard (Apr 20 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125331268):
<p><code>#check (⟦(3 : ℤ)⟧ : Zmod 5</code> gives</p>

#### [ Kevin Buzzard (Apr 20 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125331299):
<p><code>⁇ : Zmod 5</code> for information check result (in green)</p>

#### [ Kevin Buzzard (Apr 20 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125331303):
<p>and fails to synthesize the instance</p>

#### [ Simon Hudon (Apr 20 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125331410):
<p>Try:</p>
<div class="codehilite"><pre><span></span>import data.int.modeq

@[reducible]
def Zmod (n : ℤ) : Type := ℤ

instance Zmod_setoid {n : ℤ} : setoid (Zmod n) :=
{ r := int.modeq n,
  iseqv := ⟨int.modeq.refl, @int.modeq.symm n, @int.modeq.trans n⟩ }

example {n : ℤ} : setoid (Zmod n) := by apply_instance

#check ⟦ (3 : Zmod 5) ⟧
</pre></div>

#### [ Simon Hudon (Apr 20 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125331465):
<p>The problem is that instance inference is only working with <code>ℤ</code> (in your example) to find a setoid instance. It's not enough information to infer the <code>n</code> parameter. Now, I added a synonym for <code>ℤ</code> which provides that information.</p>

#### [ Kevin Buzzard (Apr 20 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125331928):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">int</span><span class="bp">.</span><span class="n">modeq</span>

<span class="bp">@</span><span class="o">[</span><span class="kn">reducible</span><span class="o">]</span>
<span class="n">def</span> <span class="n">Z_aux</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Type</span> <span class="o">:=</span> <span class="bp">ℤ</span>

<span class="kn">instance</span> <span class="n">Zmod_setoid</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">}</span> <span class="o">:</span> <span class="n">setoid</span> <span class="o">(</span><span class="n">Z_aux</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">r</span> <span class="o">:=</span> <span class="n">int</span><span class="bp">.</span><span class="n">modeq</span> <span class="n">n</span><span class="o">,</span>
  <span class="n">iseqv</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">int</span><span class="bp">.</span><span class="n">modeq</span><span class="bp">.</span><span class="n">refl</span><span class="o">,</span> <span class="bp">@</span><span class="n">int</span><span class="bp">.</span><span class="n">modeq</span><span class="bp">.</span><span class="n">symm</span> <span class="n">n</span><span class="o">,</span> <span class="bp">@</span><span class="n">int</span><span class="bp">.</span><span class="n">modeq</span><span class="bp">.</span><span class="n">trans</span> <span class="n">n</span><span class="bp">⟩</span> <span class="o">}</span>

<span class="kn">example</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">}</span> <span class="o">:</span> <span class="n">setoid</span> <span class="o">(</span><span class="n">Z_aux</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>

<span class="n">def</span> <span class="n">Zmod</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Type</span> <span class="o">:=</span> <span class="n">quotient</span> <span class="o">(</span><span class="bp">@</span><span class="n">Zmod_setoid</span> <span class="n">n</span><span class="o">)</span>

<span class="bp">#</span><span class="kn">check</span> <span class="o">(</span><span class="err">⟦</span> <span class="mi">3</span> <span class="err">⟧</span> <span class="o">:</span> <span class="n">Zmod</span> <span class="mi">5</span><span class="o">)</span> <span class="c1">-- 3 is interpreted as being in Z_aux 5 and this works</span>

<span class="kn">private</span> <span class="n">def</span> <span class="n">add_aux</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">}</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">Zmod</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span> <span class="n">Zmod</span> <span class="n">n</span> <span class="o">:=</span>
<span class="n">quotient</span><span class="bp">.</span><span class="n">lift_on₂</span> <span class="n">a</span> <span class="n">b</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span> <span class="n">b</span><span class="o">,</span> <span class="o">(</span><span class="err">⟦</span><span class="n">a</span> <span class="bp">+</span> <span class="n">b</span><span class="err">⟧</span> <span class="o">:</span> <span class="n">Zmod</span> <span class="n">n</span><span class="o">))</span> <span class="n">sorry</span> <span class="c1">-- no error yet</span>
</pre></div>

#### [ Kevin Buzzard (Apr 20 2018 at 01:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125331934):
<p>As a mathematician I'm a bit uneasy about having a thing which is Z but which is called Zmod n</p>

#### [ Kevin Buzzard (Apr 20 2018 at 01:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125331935):
<p>so I renamed it Z_aux, but your trick is excellent all the same :-)</p>

#### [ Kevin Buzzard (Apr 20 2018 at 01:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125331939):
<p>I was worried the check would fail because Lean wouldn't push 3 into Z_aux 5</p>

#### [ Kevin Buzzard (Apr 20 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332001):
<p><code>setoid</code> is a class and this is in core lean.</p>

#### [ Kevin Buzzard (Apr 20 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332004):
<p>I think this means that it's quite hard to have more than one instance of a setoid structure on a given type</p>

#### [ Kevin Buzzard (Apr 20 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332006):
<p>Simon's trick shows how to get around this, by making lots of types, one for each structure</p>

#### [ Kevin Buzzard (Apr 20 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332009):
<p>it's evil :-)</p>

#### [ Simon Hudon (Apr 20 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332056):
<p>In general, if you need more than one instance of a class for a given type, it should make you suspicious</p>

#### [ Mario Carneiro (Apr 20 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332058):
<p>it's also a good way to handle the multiple rings problem</p>

#### [ Kevin Buzzard (Apr 20 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332059):
<p>yes</p>

#### [ Kevin Buzzard (Apr 20 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332060):
<p>I don't think I'd seen it before</p>

#### [ Simon Hudon (Apr 20 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332061):
<p>But you can also name the quotient instead of <code>Z</code>:</p>

#### [ Simon Hudon (Apr 20 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332069):
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">Zmod_setoid</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">setoid</span> <span class="o">(</span><span class="n">Zmod</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">r</span> <span class="o">:=</span> <span class="n">int</span><span class="bp">.</span><span class="n">modeq</span> <span class="n">n</span><span class="o">,</span>
  <span class="n">iseqv</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">int</span><span class="bp">.</span><span class="n">modeq</span><span class="bp">.</span><span class="n">refl</span><span class="o">,</span> <span class="bp">@</span><span class="n">int</span><span class="bp">.</span><span class="n">modeq</span><span class="bp">.</span><span class="n">symm</span> <span class="n">n</span><span class="o">,</span> <span class="bp">@</span><span class="n">int</span><span class="bp">.</span><span class="n">modeq</span><span class="bp">.</span><span class="n">trans</span> <span class="n">n</span><span class="bp">⟩</span> <span class="o">}</span>

<span class="n">def</span> <span class="n">Zmod&#39;</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Type</span> <span class="o">:=</span> <span class="n">quotient</span> <span class="o">(</span><span class="n">Zmod_setoid</span> <span class="n">n</span><span class="o">)</span>

<span class="bp">#</span><span class="kn">check</span> <span class="o">(</span><span class="err">⟦</span> <span class="mi">3</span> <span class="err">⟧</span> <span class="o">:</span> <span class="n">Zmod&#39;</span> <span class="mi">5</span><span class="o">)</span>
</pre></div>

#### [ Simon Hudon (Apr 20 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332072):
<p>And if you equip <code>Zmod' 5</code> with <code>has_one</code>, <code>has_zero</code> and <code>has_add</code>, <code>#check (3 : Zmod' 5)</code> should work</p>

#### [ Kevin Buzzard (Apr 20 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332189):
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">(</span><span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">has_add</span> <span class="n">Y</span><span class="o">]</span> <span class="o">[</span><span class="n">has_one</span> <span class="n">Y</span><span class="o">]</span>
<span class="bp">#</span><span class="kn">check</span> <span class="o">(</span><span class="mi">3</span> <span class="o">:</span> <span class="n">Y</span><span class="o">)</span>
</pre></div>

#### [ Kevin Buzzard (Apr 20 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332191):
<p>no need for zero ;-)</p>

#### [ Simon Hudon (Apr 20 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332193):
<p>Even better!</p>

#### [ Kevin Buzzard (Apr 20 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332195):
<p>sort of...</p>

#### [ Kevin Buzzard (Apr 20 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332198):
<p>:-)</p>

#### [ Simon Hudon (Apr 20 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332241):
<blockquote>
<p>Simon's trick shows how to get around this, by making lots of types, one for each structure</p>
<p>it's evil :-)</p>
</blockquote>
<p>I disagree. If you want the structure to be inferred implicitly, the information must be somewhere. The alternative is to have a different <code>+</code> / <code>*</code> operator for each one of those structures: <code>+_mod_5</code> / <code>*_mod_5</code>. That would be ugly and evil!</p>

#### [ Kevin Buzzard (Apr 20 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332255):
<p>If setoid were a structure rather than a class, do you think Chris' code would be OK?</p>

#### [ Kevin Buzzard (Apr 20 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332260):
<p>The quotient knows the equivalence relation, and the information distinguishing the quotient types is in the equivalence relation</p>

#### [ Kevin Buzzard (Apr 20 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332359):
<p><code>variables (Y : Type) [has_add Y] [has_one Y]</code></p>

#### [ Kevin Buzzard (Apr 20 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332360):
<p>I think I just defined the positive integers :-)</p>

#### [ Simon Hudon (Apr 20 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332361):
<p>Yeah I think that would be good. Maybe rather than making <code>setoid</code> a structure, just make <code>Zmod_setoid</code> into a definition because it is not unique</p>

#### [ Kevin Buzzard (Apr 20 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332379):
<p>then you'll lose access to the \[[ notation</p>

#### [ Kevin Buzzard (Apr 20 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332381):
<p>this goes back to the thing I was talking about earlier</p>

#### [ Kevin Buzzard (Apr 20 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332382):
<p>once setoid is deemed to be a class</p>

#### [ Kevin Buzzard (Apr 20 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332385):
<p>then pretty much whenever it's mentioned in a definition or theorem, it's in a square bracket</p>

#### [ Simon Hudon (Apr 20 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332386):
<blockquote>
<p>I think I just defined the positive integers :-)</p>
</blockquote>
<p>That looks like the Church numerals</p>

#### [ Simon Hudon (Apr 20 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332428):
<p>Sorry, I kind of jumped in the middle your conversation</p>

#### [ Kevin Buzzard (Apr 20 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332434):
<p>so it's a pain to work with if you decide not to use the type class inference system</p>

#### [ Simon Hudon (Apr 20 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332443):
<p>Yes, I see now</p>

#### [ Kevin Buzzard (Apr 20 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332444):
<p>As Mario points out, it's the same sort of thing as the (hypothetical but not completely impossible) possibility of having more than one ring structure on a type</p>

#### [ Simon Hudon (Apr 20 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332445):
<p>Is it ever necessary to have it inferred?</p>

#### [ Kevin Buzzard (Apr 20 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332492):
<p>it's just inconvenient not to have it inferred, if Lean wants it to be inferred.</p>

#### [ Kevin Buzzard (Apr 20 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332499):
<p>That was what I discovered when I had a commutative ring earlier -- if you use the type class inference system then you also automatically have a ring, an additive group, and a whole bunch of other things</p>

#### [ Kevin Buzzard (Apr 20 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332504):
<p>and if you don't then you're stuck making all of these yourself</p>

#### [ Simon Hudon (Apr 20 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332521):
<p>What if you skip <code>\[[</code> and instead rely on <code>coe</code> to convert integers to <code>Zmod</code> and <code>has_one</code> / <code>has_add</code> to use numerals?</p>

#### [ Kevin Buzzard (Apr 20 2018 at 02:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332584):
<p>I guess the proof of the pudding would be in the eating</p>

#### [ Kevin Buzzard (Apr 20 2018 at 02:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332628):
<p>I was fine explictly writing my proofs that various types were commutative rings up to a point</p>

#### [ Kevin Buzzard (Apr 20 2018 at 02:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332632):
<p>and then it got inconvenient and then I figured out how to use type class inference.</p>

#### [ Kevin Buzzard (Apr 20 2018 at 02:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332637):
<p>Those things aren't quite church numerals</p>

#### [ Kevin Buzzard (Apr 20 2018 at 02:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332638):
<p>as far as I can see at least</p>

#### [ Kevin Buzzard (Apr 20 2018 at 02:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332647):
<p>but they do have a similar flavour</p>

#### [ Kevin Buzzard (Apr 20 2018 at 02:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332757):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">hudon_numeral</span> <span class="o">:=</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">),</span> <span class="o">(</span><span class="n">Y</span> <span class="bp">→</span> <span class="n">Y</span> <span class="bp">→</span> <span class="n">Y</span><span class="o">)</span> <span class="bp">→</span> <span class="n">Y</span> <span class="bp">→</span> <span class="n">Y</span>
<span class="n">def</span> <span class="n">one</span> <span class="o">:</span> <span class="n">hudon_numeral</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">Y</span> <span class="n">h_add</span> <span class="n">h_one</span><span class="o">,</span> <span class="n">h_one</span>
<span class="n">def</span> <span class="n">two</span> <span class="o">:</span> <span class="n">hudon_numeral</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">Y</span> <span class="n">h_add</span> <span class="n">h_one</span><span class="o">,</span> <span class="n">h_add</span> <span class="n">h_one</span> <span class="n">h_one</span>
</pre></div>

#### [ Kevin Buzzard (Apr 20 2018 at 02:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332760):
<p>etc</p>

#### [ Simon Hudon (Apr 20 2018 at 02:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125332812):
<p>Ah yes I see! 0 is missing and Church encodes <code>succ</code> rather than <code>add</code></p>

#### [ Chris Hughes (Apr 20 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125443745):
<p>Any advice about how to deal with this issue? </p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">Zmod_fintype</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">}</span> <span class="o">(</span><span class="n">hn</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">≠</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:</span> <span class="n">fintype</span> <span class="o">(</span><span class="n">Zmod</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">fintype</span><span class="bp">.</span><span class="n">of_equiv</span> <span class="bp">_</span> <span class="o">(</span><span class="n">equiv_fin</span> <span class="n">hn</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span>
</pre></div>


<p>I can't make this an instance, because it's only true if <code>n ≠ 0</code></p>

#### [ Kevin Buzzard (Apr 20 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125444830):
<p>Why not let n be in pnat (positive integers) instead of Z?</p>

#### [ Chris Hughes (Apr 20 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125444960):
<p>Probably the best thing. Alternative is to define the equivalence relation differently in the case <code>n = 0</code>, so <code>Zmod 0</code> is a fintype.</p>

#### [ Chris Hughes (Apr 20 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125445223):
<p>Then there's also the issue of proving it's a field in the case <code>prime p</code></p>

#### [ Kenny Lau (Apr 20 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125445230):
<p><code>fintype (Zmod $ nat.succ m)</code></p>

#### [ Chris Hughes (Apr 20 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125445289):
<p><code>n</code> is an int currently</p>

#### [ Kevin Buzzard (Apr 20 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125458960):
<p>I have another type class inference issue and this one is rather frustrating.</p>

#### [ Kevin Buzzard (Apr 20 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125458969):
<p>I am making a definition, so I really want to stay in term mode.</p>

#### [ Kevin Buzzard (Apr 20 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125458971):
<p>I wrote down something which should work</p>

#### [ Kevin Buzzard (Apr 20 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125458983):
<p>and Lean complained that it could not prove that a certain composition of two maps was a ring homomorphism.</p>

#### [ Kevin Buzzard (Apr 20 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125458987):
<p>So I tried again in tactic mode</p>

#### [ Kevin Buzzard (Apr 20 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125459006):
<p>(each map is a ring hom, with an instance, and the composite of two ring homs is a ring hom, and this is an instance too, so it should work)</p>

#### [ Kevin Buzzard (Apr 20 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125459058):
<p>and in tactic mode I have managed to get Lean into a state where the goal is to show that the map is a ring hom (I did this using <code>refine</code>)</p>

#### [ Kevin Buzzard (Apr 20 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125459059):
<p>and <code>apply_instance</code> fails</p>

#### [ Kevin Buzzard (Apr 20 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125459063):
<p>but <code>show ([cut and paste the goal])</code></p>

#### [ Kevin Buzzard (Apr 20 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125459066):
<p>followed by <code>apply_instance</code> succeeds.</p>

#### [ Kevin Buzzard (Apr 20 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125459079):
<p>In term mode, the proof should look like this:</p>

#### [ Kevin Buzzard (Apr 20 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125459080):
<p><code>to_fun := away.extend_map_of_im_unit ((of_comm_ring (away f) _) ∘ (of_comm_ring R (powers f))) H,</code></p>

#### [ Kevin Buzzard (Apr 20 2018 at 19:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125459087):
<p>(it's some part of a structure I'm defining)</p>

#### [ Kevin Buzzard (Apr 20 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125459144):
<p>but <code>away.extend_map_of_im_unit</code> requires that the map (a composite of two ring homs) is a ring hom</p>

#### [ Kevin Buzzard (Apr 20 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125459165):
<p>So here it feels to me like Lean is not working as well as it could be.</p>

#### [ Kevin Buzzard (Apr 20 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125459169):
<p>But I don't have any feeling as to why not</p>

#### [ Kevin Buzzard (Apr 20 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125459242):
<p>If I set <code>pp.all true</code> I can see that the <code>show</code> command is doing something</p>

#### [ Kevin Buzzard (Apr 20 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125459251):
<p>but unfortunately these are complex maps defined between complex rings</p>

#### [ Kevin Buzzard (Apr 20 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125459257):
<p>and so I am having trouble figuring out what I have done wrong</p>

#### [ Kevin Buzzard (Apr 20 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125459260):
<p>and whether it's Lean's fault or mine</p>

#### [ Kevin Buzzard (Apr 20 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125459438):
<p>Here are the two (rather lengthy) goals.</p>

#### [ Kevin Buzzard (Apr 20 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125459440):
<p><a href="https://gist.github.com/kbuzzard/a09dc87e290c0497db65c4c702b37c2f" target="_blank" title="https://gist.github.com/kbuzzard/a09dc87e290c0497db65c4c702b37c2f">https://gist.github.com/kbuzzard/a09dc87e290c0497db65c4c702b37c2f</a></p>

#### [ Kevin Buzzard (Apr 20 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125459524):
<p>Just to be clear: my problem is that I need to prove something in term mode because it's part of a definition. Type class inference fails me and I don't know why. In tactic mode I can make type class inference succeed.</p>

#### [ Kevin Buzzard (Apr 20 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125459544):
<p>I could go down the awful route of adding <code>@</code>s and explicitly chasing up the proof, but I would rather let type class inference do its job properly and just add hints.</p>

#### [ Simon Hudon (Apr 20 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125459604):
<p>if it's a proof (i.e. it's type is a <code>Prop</code>) I think you can use a tactic:</p>
<div class="codehilite"><pre><span></span>to_fun :=
have local_proof : something, by ...,
definition_using_local_proof,
</pre></div>

#### [ Simon Hudon (Apr 20 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125459924):
<p>To my memory, <code>local_proof</code> gets compiled to an auxiliary definition / lemma and you'll have <code>to_fun := definition_using_local_proof</code> with a reference to that auxiliary definition (which will not be displayed because of proof erasure).</p>

#### [ Kevin Buzzard (Apr 20 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460308):
<p>Unfortunately this fails, because my local proof is not a proof of the correct thing.</p>

#### [ Kevin Buzzard (Apr 20 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460313):
<p>My local proof is a proof of the second monstrous expression in the gist, which can be proved by type class inference.</p>

#### [ Kevin Buzzard (Apr 20 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460320):
<p>I have two maps phi and psi</p>

#### [ Kevin Buzzard (Apr 20 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460361):
<p>and I can prove <code>is_ring_hom (phi comp psi)</code> with <code>apply_instance</code></p>

#### [ Kevin Buzzard (Apr 20 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460370):
<p>but when I write <code>foo (phi comp psi)</code></p>

#### [ Kevin Buzzard (Apr 20 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460372):
<p>for some function foo which needs (phi comp psi) to be a ring hom</p>

#### [ Kevin Buzzard (Apr 20 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460374):
<p>then type class inference fails</p>

#### [ Kevin Buzzard (Apr 20 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460384):
<p>well, this is my understanding of the situation.</p>

#### [ Kevin Buzzard (Apr 20 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460405):
<p>I tried to create a MWE but I could not reproduce the problem in a controlled environment</p>

#### [ Simon Hudon (Apr 20 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460490):
<p>What do you know about <code>phi comp psi</code> that makes it a <code>is_ring_hom</code>? Could you create:</p>
<div class="codehilite"><pre><span></span>instance [... some context about (phi comp psi) ...] : is_ring_hom (phi comp psi) := ...
</pre></div>


<p>right before the structure you're trying to define?</p>

#### [ Johan Commelin (Apr 20 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460538):
<p><code>phi</code> and <code>psi</code> are both ring homs themselves, if I understand Kevin correctly</p>

#### [ Kevin Buzzard (Apr 20 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460635):
<p>Type class inference will make it a ring hom</p>

#### [ Kevin Buzzard (Apr 20 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460684):
<p>Here is a very clear explanation of the situation I find myself in:</p>

#### [ Kevin Buzzard (Apr 20 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460694):
<div class="codehilite"><pre><span></span>  <span class="n">to_fun</span> <span class="o">:=</span> <span class="k">have</span> <span class="n">XXX</span> <span class="o">:</span> <span class="n">is_ring_hom</span>
    <span class="o">(</span><span class="n">of_comm_ring</span> <span class="o">(</span><span class="n">away</span> <span class="n">f</span><span class="o">)</span> <span class="o">(</span><span class="n">powers</span> <span class="o">(</span><span class="n">of_comm_ring</span> <span class="n">R</span> <span class="o">(</span><span class="n">powers</span> <span class="n">f</span><span class="o">)</span> <span class="n">g</span><span class="o">))</span> <span class="err">∘</span> <span class="o">(</span><span class="n">of_comm_ring</span> <span class="n">R</span> <span class="o">(</span><span class="n">powers</span> <span class="n">f</span><span class="o">))</span> <span class="o">)</span>
    <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span><span class="o">,</span>
  <span class="n">away</span><span class="bp">.</span><span class="n">extend_map_of_im_unit</span>
              <span class="o">(</span><span class="n">of_comm_ring</span> <span class="o">(</span><span class="n">away</span> <span class="n">f</span><span class="o">)</span> <span class="o">(</span><span class="n">powers</span> <span class="o">(</span><span class="n">of_comm_ring</span> <span class="n">R</span> <span class="o">(</span><span class="n">powers</span> <span class="n">f</span><span class="o">)</span> <span class="n">g</span><span class="o">))</span> <span class="err">∘</span> <span class="o">(</span><span class="n">of_comm_ring</span> <span class="n">R</span> <span class="o">(</span><span class="n">powers</span> <span class="n">f</span><span class="o">)))</span>
              <span class="n">sorry</span><span class="o">,</span>
</pre></div>

#### [ Kevin Buzzard (Apr 20 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460701):
<p>(the sorry at the end is just to save you from having to look at another term)</p>

#### [ Kevin Buzzard (Apr 20 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460708):
<p>So this definition fails</p>

#### [ Kevin Buzzard (Apr 20 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460711):
<p>there's a red squiggle under <code>away</code></p>

#### [ Kevin Buzzard (Apr 20 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460715):
<p>and the error is</p>

#### [ Kevin Buzzard (Apr 20 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460727):
<div class="codehilite"><pre><span></span><span class="n">failed</span> <span class="n">to</span> <span class="n">synthesize</span> <span class="n">type</span> <span class="n">class</span> <span class="kn">instance</span> <span class="n">for</span>
<span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">comm_ring</span> <span class="n">R</span><span class="o">,</span>
<span class="n">f</span> <span class="n">g</span> <span class="o">:</span> <span class="n">R</span><span class="o">,</span>
<span class="n">H</span> <span class="o">:</span> <span class="n">Spec</span><span class="bp">.</span><span class="n">D&#39;</span> <span class="n">g</span> <span class="err">⊆</span> <span class="n">Spec</span><span class="bp">.</span><span class="n">D&#39;</span> <span class="n">f</span><span class="o">,</span>
<span class="n">XXX</span> <span class="o">:</span> <span class="n">is_ring_hom</span> <span class="o">(</span><span class="n">of_comm_ring</span> <span class="o">(</span><span class="n">away</span> <span class="n">f</span><span class="o">)</span> <span class="o">(</span><span class="n">powers</span> <span class="o">(</span><span class="n">of_comm_ring</span> <span class="n">R</span> <span class="o">(</span><span class="n">powers</span> <span class="n">f</span><span class="o">)</span> <span class="n">g</span><span class="o">))</span> <span class="err">∘</span> <span class="n">of_comm_ring</span> <span class="n">R</span> <span class="o">(</span><span class="n">powers</span> <span class="n">f</span><span class="o">))</span>
<span class="err">⊢</span> <span class="n">is_ring_hom</span> <span class="o">(</span><span class="n">of_comm_ring</span> <span class="o">(</span><span class="n">away</span> <span class="n">f</span><span class="o">)</span> <span class="o">(</span><span class="n">powers</span> <span class="o">(</span><span class="n">of_comm_ring</span> <span class="n">R</span> <span class="o">(</span><span class="n">powers</span> <span class="n">f</span><span class="o">)</span> <span class="n">g</span><span class="o">))</span> <span class="err">∘</span> <span class="n">of_comm_ring</span> <span class="n">R</span> <span class="o">(</span><span class="n">powers</span> <span class="n">f</span><span class="o">))</span>
</pre></div>

#### [ Kevin Buzzard (Apr 20 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460736):
<p>Note that the goal looks exactly like <code>XXX</code></p>

#### [ Kevin Buzzard (Apr 20 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460745):
<p>and what is even more frustrating is that the goal and <code>XXX</code> were both created in the same way</p>

#### [ Kevin Buzzard (Apr 20 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460790):
<p>by typing the same string twice</p>

#### [ Kevin Buzzard (Apr 20 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460794):
<p>namely the string which appears in the goal</p>

#### [ Kevin Buzzard (Apr 20 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460800):
<p>however if I set pp.all true</p>

#### [ Kevin Buzzard (Apr 20 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460808):
<p>then XXX and the goal expand into the two distinct, but defeq, monsters</p>

#### [ Kevin Buzzard (Apr 20 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460830):
<p>and note that XXX was proved by type class inference</p>

#### [ Kevin Buzzard (Apr 20 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460885):
<p>What I need to understand to proceed, I think, is that I'd like to understand how Lean can unfold the same string in two different ways in these two situations.</p>

#### [ Kevin Buzzard (Apr 20 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460896):
<p>I am scared to use a let to define the function, because I am scared it will cause me problems further down the line</p>

#### [ Kevin Buzzard (Apr 20 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460917):
<p>I am trying to prove that a map is a bijection and if I do something screwy when defining the map then I'm worried I won't be able to use it later</p>

#### [ Simon Hudon (Apr 20 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460977):
<p>The problem might be in the two terms that are defeq but not identical. Cosmetic differences in the syntax can take the instance inference process in a different direction. Do you think you can make them exactly identical?</p>

#### [ Kevin Buzzard (Apr 20 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460979):
<p>this is exactly what I cannot do</p>

#### [ Kevin Buzzard (Apr 20 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460982):
<p>because as you can see from my term</p>

#### [ Kevin Buzzard (Apr 20 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460989):
<p>I created <code>XXX</code> and the input to <code>away.extend_map_of_im_unit </code> by typing exactly the same string of characters.</p>

#### [ Simon Hudon (Apr 20 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125460992):
<p>including the <code>@</code>?</p>

#### [ Kevin Buzzard (Apr 20 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125461035):
<p>aah I see</p>

#### [ Kevin Buzzard (Apr 20 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125461038):
<p>I can try to be more persuasive</p>

#### [ Simon Hudon (Apr 20 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125461051):
<p>It will probably not be concise but we can work on that once we know it works</p>

#### [ Kevin Buzzard (Apr 20 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125461063):
<p>by the way, am I right in thinking that I should not be using <code>let</code> in a defintion of a map?</p>

#### [ Kevin Buzzard (Apr 20 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125461117):
<p>Many thanks Simon</p>

#### [ Kevin Buzzard (Apr 20 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125461123):
<p>Explicitly telling Lean what the type of the composition was has solved the problem</p>

#### [ Kevin Buzzard (Apr 20 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125461141):
<p>Thanks a <em>lot</em> for persevering with this very awkward problem which was completely blocking me.</p>

#### [ Kevin Buzzard (Apr 20 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125461152):
<p>Many thanks indeed.</p>

#### [ Simon Hudon (Apr 20 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125461200):
<p>You're very welcome :)</p>

#### [ Simon Hudon (Apr 20 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125461268):
<blockquote>
<p>by the way, am I right in thinking that I should not be using <code>let</code> in a defintion of a map?</p>
</blockquote>
<p>I would avoid it especially if you're going to prove stuff about it. Maybe you're asking about the ùmathlibù style though. I haven't seen that mentioned anywhere but facilitating proofs using your definitions is likely to make you popular with the <code>mathlib</code> team.</p>

#### [ Mario Carneiro (Apr 21 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125472229):
<p>Have you tried using <code>by exact</code> in your definition? There is nothing wrong with using tactics in the definition of a term, although you may need to be more conscientious about junk added to your term by lean (or use <code>by clean</code>)</p>

#### [ Mario Carneiro (Apr 21 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125472249):
<p>there is not a problem with using <code>let</code> or other techniques in defining a complicated function, although you will probably want to write simp lemmas providing your interface so you don't need to rely on definitional expansion</p>

#### [ Kevin Buzzard (Apr 21 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504684):
<p>Gaargh I have another one. Here's a MWE.</p>

#### [ Kevin Buzzard (Apr 21 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504686):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">ring</span>
<span class="n">universes</span> <span class="n">u</span> <span class="n">v</span> <span class="n">w</span> <span class="n">uu</span>

<span class="kn">structure</span> <span class="n">is_unique_R_alg_hom</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">w</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">β</span><span class="o">]</span>
<span class="o">(</span><span class="n">sα</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">sβ</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">sα</span><span class="o">]</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">sβ</span><span class="o">]</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">f</span><span class="o">]</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">R_alg_hom</span> <span class="o">:</span> <span class="n">sβ</span> <span class="bp">=</span> <span class="n">f</span> <span class="err">∘</span> <span class="n">sα</span><span class="o">)</span>
<span class="o">(</span><span class="n">is_unique</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">g</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">,</span> <span class="n">is_ring_hom</span> <span class="n">g</span> <span class="bp">→</span> <span class="n">sβ</span> <span class="bp">=</span> <span class="n">g</span> <span class="err">∘</span> <span class="n">sα</span> <span class="bp">→</span> <span class="n">g</span> <span class="bp">=</span> <span class="n">f</span><span class="o">)</span>

<span class="kn">lemma</span> <span class="n">comp_unique</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">w</span><span class="o">}</span> <span class="o">{</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">uu</span><span class="o">}</span>
  <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">β</span><span class="o">]</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">γ</span><span class="o">]</span>
  <span class="o">(</span><span class="n">sα</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">sβ</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">sγ</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">)</span>
  <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">sα</span><span class="o">]</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">sβ</span><span class="o">]</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">sγ</span><span class="o">]</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">f</span><span class="o">]</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">g</span><span class="o">]</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">h</span><span class="o">]</span> <span class="o">:</span>
  <span class="n">is_unique_R_alg_hom</span> <span class="n">sα</span> <span class="n">sβ</span> <span class="n">f</span> <span class="bp">→</span> <span class="n">is_unique_R_alg_hom</span> <span class="n">sβ</span> <span class="n">sγ</span> <span class="n">g</span> <span class="bp">→</span> <span class="n">is_unique_R_alg_hom</span> <span class="n">sα</span> <span class="n">sγ</span> <span class="n">h</span> <span class="bp">→</span> <span class="n">g</span> <span class="err">∘</span> <span class="n">f</span> <span class="bp">=</span> <span class="n">h</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">Uf</span> <span class="n">Ug</span> <span class="n">Uh</span><span class="o">,</span> <span class="n">Uh</span><span class="bp">.</span><span class="n">is_unique</span> <span class="o">(</span><span class="n">g</span> <span class="err">∘</span> <span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">)</span> <span class="o">(</span><span class="k">by</span> <span class="n">apply_instance</span><span class="o">)</span> <span class="o">(</span><span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">Uf</span><span class="bp">.</span><span class="n">R_alg_hom</span><span class="o">,</span><span class="n">Ug</span><span class="bp">.</span><span class="n">R_alg_hom</span><span class="o">])</span>
</pre></div>

#### [ Kevin Buzzard (Apr 21 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504689):
<p>Note the <code>by apply_instance</code> on the last line!</p>

#### [ Kevin Buzzard (Apr 21 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504698):
<p>If I replace that with <code>_</code> then I get</p>

#### [ Kevin Buzzard (Apr 21 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504699):
<div class="codehilite"><pre><span></span>don&#39;t know how to synthesize placeholder
context:
R : Type u,
α : Type v,
β : Type w,
γ : Type uu,
_inst_1 : comm_ring R,
_inst_2 : comm_ring α,
_inst_3 : comm_ring β,
_inst_4 : comm_ring γ,
sα : R → α,
sβ : R → β,
sγ : R → γ,
f : α → β,
g : β → γ,
h : α → γ,
_inst_5 : is_ring_hom sα,
_inst_6 : is_ring_hom sβ,
_inst_7 : is_ring_hom sγ,
_inst_8 : is_ring_hom f,
_inst_9 : is_ring_hom g,
_inst_10 : is_ring_hom h,
Uf : is_unique_R_alg_hom sα sβ f,
Ug : is_unique_R_alg_hom sβ sγ g,
Uh : is_unique_R_alg_hom sα sγ h
⊢ is_ring_hom (g ∘ f)
</pre></div>

#### [ Kevin Buzzard (Apr 21 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504701):
<p>How does type class inference work? Is <code>_</code> something other than <code>by apply_instance</code>?</p>

#### [ Mario Carneiro (Apr 21 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504758):
<p>yes</p>

#### [ Kevin Buzzard (Apr 21 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504796):
<p>I guess I just proved that :-)</p>

#### [ Mario Carneiro (Apr 21 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504799):
<p><code>_</code> only does unification</p>

#### [ Mario Carneiro (Apr 21 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504804):
<p>when it is omitted and the binder type is <code>[tc A]</code> it uses typeclass inference</p>

#### [ Patrick Massot (Apr 21 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504805):
<p>You need <code>is_unique_R_alg_hom.is_unique</code> to take a square bracket argument</p>

#### [ Mario Carneiro (Apr 21 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504807):
<p><code>by apply_instance</code> does the same thing but manually</p>

#### [ Kevin Buzzard (Apr 21 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504815):
<p>So "don't know how to synthesize placeholder" -- what did it try??</p>

#### [ Mario Carneiro (Apr 21 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504817):
<p>unification</p>

#### [ Mario Carneiro (Apr 21 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504820):
<p>and nothing else</p>

#### [ Kevin Buzzard (Apr 21 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504822):
<p>I don't know what unification means</p>

#### [ Kevin Buzzard (Apr 21 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504860):
<p>isn't that something to do with finding something of the right type?</p>

#### [ Kevin Buzzard (Apr 21 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504865):
<p>Oh</p>

#### [ Kevin Buzzard (Apr 21 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504866):
<p>I remember</p>

#### [ Kevin Buzzard (Apr 21 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504869):
<p>it means "I will call this ?m_6"</p>

#### [ Kevin Buzzard (Apr 21 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504871):
<p>"and sort it out later"</p>

#### [ Kevin Buzzard (Apr 21 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504884):
<p>Thanks Patrick:</p>

#### [ Kevin Buzzard (Apr 21 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504885):
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">is_unique_R_alg_hom</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">w</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">β</span><span class="o">]</span>
<span class="o">(</span><span class="n">sα</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">sβ</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">sα</span><span class="o">]</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">sβ</span><span class="o">]</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">f</span><span class="o">]</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">R_alg_hom</span> <span class="o">:</span> <span class="n">sβ</span> <span class="bp">=</span> <span class="n">f</span> <span class="err">∘</span> <span class="n">sα</span><span class="o">)</span>
<span class="o">(</span><span class="n">is_unique</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">g</span><span class="o">],</span> <span class="n">sβ</span> <span class="bp">=</span> <span class="n">g</span> <span class="err">∘</span> <span class="n">sα</span> <span class="bp">→</span> <span class="n">g</span> <span class="bp">=</span> <span class="n">f</span><span class="o">)</span>

<span class="kn">lemma</span> <span class="n">comp_unique</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">w</span><span class="o">}</span> <span class="o">{</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">uu</span><span class="o">}</span>
  <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">β</span><span class="o">]</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">γ</span><span class="o">]</span>
  <span class="o">(</span><span class="n">sα</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">sβ</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">sγ</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">)</span>
  <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">sα</span><span class="o">]</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">sβ</span><span class="o">]</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">sγ</span><span class="o">]</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">f</span><span class="o">]</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">g</span><span class="o">]</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">h</span><span class="o">]</span> <span class="o">:</span>
  <span class="n">is_unique_R_alg_hom</span> <span class="n">sα</span> <span class="n">sβ</span> <span class="n">f</span> <span class="bp">→</span> <span class="n">is_unique_R_alg_hom</span> <span class="n">sβ</span> <span class="n">sγ</span> <span class="n">g</span> <span class="bp">→</span> <span class="n">is_unique_R_alg_hom</span> <span class="n">sα</span> <span class="n">sγ</span> <span class="n">h</span> <span class="bp">→</span> <span class="n">g</span> <span class="err">∘</span> <span class="n">f</span> <span class="bp">=</span> <span class="n">h</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">Uf</span> <span class="n">Ug</span> <span class="n">Uh</span><span class="o">,</span> <span class="n">Uh</span><span class="bp">.</span><span class="n">is_unique</span> <span class="o">(</span><span class="n">g</span> <span class="err">∘</span> <span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">)</span> <span class="o">(</span><span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">Uf</span><span class="bp">.</span><span class="n">R_alg_hom</span><span class="o">,</span><span class="n">Ug</span><span class="bp">.</span><span class="n">R_alg_hom</span><span class="o">])</span>
</pre></div>

#### [ Patrick Massot (Apr 21 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504929):
<p>You're welcome</p>

#### [ Kevin Buzzard (Apr 21 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504934):
<p>I have abstracted a standard trick :-)</p>

#### [ Kevin Buzzard (Apr 21 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504986):
<p>I see, I was not even asking type class inference to do its job here. So this one is my bad.</p>

#### [ Patrick Massot (Apr 21 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125504987):
<p>Indeed</p>

#### [ Kevin Buzzard (Apr 22 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125508966):
<p>How do I do this one:</p>

#### [ Kevin Buzzard (Apr 22 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125508967):
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">foo</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">bar</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">group</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="kt">Prop</span><span class="o">)</span>

<span class="kn">definition</span> <span class="n">X</span> <span class="o">:</span> <span class="n">foo</span> <span class="o">:=</span>
<span class="o">{</span><span class="n">bar</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span> <span class="n">Hα</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span><span class="o">,</span> <span class="o">(</span><span class="n">mul_assoc</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span><span class="o">)}</span>
</pre></div>

#### [ Kevin Buzzard (Apr 22 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509119):
<p>Can I use type class inference here?</p>

#### [ Kenny Lau (Apr 22 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509132):
<p>you need a prop</p>

#### [ Kenny Lau (Apr 22 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509133):
<p>that isn't a prop</p>

#### [ Kenny Lau (Apr 22 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509135):
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">foo</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">bar</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">group</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="kt">Prop</span><span class="o">)</span>

<span class="kn">definition</span> <span class="n">X</span> <span class="o">:</span> <span class="n">foo</span> <span class="o">:=</span>
<span class="o">{</span><span class="n">bar</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">g</span> <span class="n">Hg</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span><span class="o">,</span> <span class="k">by</span> <span class="n">letI</span> <span class="o">:=</span> <span class="n">Hg</span><span class="bp">;</span> <span class="k">from</span> <span class="n">mul_assoc</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span><span class="o">}</span>
</pre></div>

#### [ Kenny Lau (Apr 22 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509173):
<div class="codehilite"><pre><span></span><span class="n">invalid</span> <span class="n">type</span> <span class="n">ascription</span><span class="o">,</span> <span class="n">term</span> <span class="n">has</span> <span class="n">type</span>
  <span class="n">a</span> <span class="bp">*</span> <span class="n">b</span> <span class="bp">*</span> <span class="n">c</span> <span class="bp">=</span> <span class="n">a</span> <span class="bp">*</span> <span class="o">(</span><span class="n">b</span> <span class="bp">*</span> <span class="n">c</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span>
<span class="n">but</span> <span class="n">is</span> <span class="n">expected</span> <span class="n">to</span> <span class="k">have</span> <span class="n">type</span>
  <span class="kt">Prop</span> <span class="o">:</span> <span class="kt">Type</span>
<span class="n">state</span><span class="o">:</span>
<span class="n">g</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">,</span>
<span class="n">Hg</span> <span class="o">:</span> <span class="n">group</span> <span class="n">g</span><span class="o">,</span>
<span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="n">g</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst</span> <span class="o">:</span> <span class="n">group</span> <span class="n">g</span> <span class="o">:=</span> <span class="n">Hg</span>
<span class="err">⊢</span> <span class="kt">Prop</span>
</pre></div>

#### [ Kevin Buzzard (Apr 22 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509187):
<p>I have some type mismatch error, I think I have more than one problem here</p>

#### [ Kenny Lau (Apr 22 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509237):
<p>which is?</p>

#### [ Kenny Lau (Apr 22 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509242):
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">foo</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">bar</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">group</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="kt">Prop</span><span class="o">)</span>

<span class="kn">definition</span> <span class="n">X</span> <span class="o">:</span> <span class="n">foo</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">bar</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">g</span> <span class="n">Hg</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span><span class="o">,</span> <span class="bp">@</span><span class="n">mul_assoc</span> <span class="bp">_</span>
    <span class="o">(</span><span class="bp">@</span><span class="n">monoid</span><span class="bp">.</span><span class="n">to_semigroup</span> <span class="n">g</span> <span class="err">$</span> <span class="bp">@</span><span class="n">group</span><span class="bp">.</span><span class="n">to_monoid</span> <span class="n">g</span> <span class="n">Hg</span><span class="o">)</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">}</span>
</pre></div>

#### [ Kevin Buzzard (Apr 22 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509394):
<p><code>mul_assoc a b c</code> isn't a prop, it's a proof.</p>

#### [ Kevin Buzzard (Apr 22 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509395):
<p>I know I can do it using @, I want to do it using type class inference</p>

#### [ Kevin Buzzard (Apr 22 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509397):
<p>I want to understand how to make type class inference work, not to understand how to work around it (which I already know)</p>

#### [ Kevin Buzzard (Apr 22 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509405):
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">foo</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">bar</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">group</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="mi">1</span> <span class="bp">*</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">a</span><span class="o">)</span>

<span class="kn">definition</span> <span class="n">X</span> <span class="o">:</span> <span class="n">foo</span> <span class="o">:=</span>
<span class="o">{</span><span class="n">bar</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span> <span class="n">Hα</span> <span class="n">a</span><span class="o">,</span> <span class="n">group</span><span class="bp">.</span><span class="n">one_mul</span> <span class="n">a</span><span class="o">}</span>
</pre></div>

#### [ Kevin Buzzard (Apr 22 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509406):
<div class="codehilite"><pre><span></span>failed to synthesize type class instance for
α : Type,
Hα : group α,
a : α
⊢ group α
</pre></div>

#### [ Kenny Lau (Apr 22 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509408):
<p>then just letI</p>

#### [ Kevin Buzzard (Apr 22 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509445):
<p>Where do I put the letI?</p>

#### [ Kevin Buzzard (Apr 22 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509448):
<p>I am in the middle of a structure</p>

#### [ Kenny Lau (Apr 22 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509449):
<p><code>by letI := H\a; from group.one_mul a</code></p>

#### [ Kevin Buzzard (Apr 22 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509450):
<p>What if I don't want to go into tactic mode because I am actually defining something?</p>

#### [ Kevin Buzzard (Apr 22 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509455):
<p>What exactly are yuo suggesting?</p>

#### [ Kevin Buzzard (Apr 22 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509461):
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">X</span> <span class="o">:</span> <span class="n">foo</span> <span class="o">:=</span>
<span class="o">{</span><span class="n">bar</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span> <span class="n">Hα</span> <span class="n">a</span><span class="o">,</span> <span class="k">by</span> <span class="n">letI</span> <span class="o">:=</span> <span class="n">Hα</span><span class="bp">;</span> <span class="k">from</span> <span class="n">group</span><span class="bp">.</span><span class="n">one_mul</span> <span class="n">a</span><span class="o">}</span>
</pre></div>

#### [ Kevin Buzzard (Apr 22 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509493):
<p>?</p>

#### [ Kenny Lau (Apr 22 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509494):
<p>yes</p>

#### [ Kevin Buzzard (Apr 22 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509499):
<p>7 errors</p>

#### [ Kevin Buzzard (Apr 22 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509502):
<p>including "unknown identifier <code>letI</code>"</p>

#### [ Kevin Buzzard (Apr 22 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509506):
<p>But even if we can get this to work</p>

#### [ Kenny Lau (Apr 22 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509509):
<p>import anything from mathlib</p>

#### [ Kevin Buzzard (Apr 22 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509512):
<p>I would rather just make type class inference work.</p>

#### [ Kenny Lau (Apr 22 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509514):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">group</span>

<span class="kn">structure</span> <span class="n">foo</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">bar</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">group</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="mi">1</span> <span class="bp">*</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">a</span><span class="o">)</span>

<span class="kn">definition</span> <span class="n">X</span> <span class="o">:</span> <span class="n">foo</span> <span class="o">:=</span>
<span class="o">{</span><span class="n">bar</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">α</span> <span class="n">Hα</span> <span class="n">a</span><span class="o">,</span> <span class="k">by</span> <span class="n">letI</span> <span class="o">:=</span> <span class="n">Hα</span><span class="bp">;</span> <span class="k">from</span> <span class="n">group</span><span class="bp">.</span><span class="n">one_mul</span> <span class="n">a</span><span class="o">}</span>

<span class="bp">#</span><span class="kn">print</span> <span class="n">X</span><span class="bp">._</span><span class="n">proof_1</span>

<span class="c">/-</span><span class="cm"></span>
<span class="cm">theorem X._proof_1 : ∀ (α : Type) (Hα : group α) (a : α), 1 * a = a :=</span>
<span class="cm">λ (α : Type) (Hα : group α) (a : α), let _inst : group α := Hα in group.one_mul a</span>
<span class="cm">-/</span>
</pre></div>

#### [ Kevin Buzzard (Apr 22 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509518):
<p>?!</p>

#### [ Kenny Lau (Apr 22 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509520):
<p>!?</p>

#### [ Kevin Buzzard (Apr 22 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509561):
<p>which version of Lean are you using?</p>

#### [ Kevin Buzzard (Apr 22 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509562):
<p>aah</p>

#### [ Kevin Buzzard (Apr 22 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509563):
<p>I have no import</p>

#### [ Kevin Buzzard (Apr 22 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509568):
<p><code>letI</code> is some mathlib magic I guess</p>

#### [ Kenny Lau (Apr 22 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509569):
<p>it is.</p>

#### [ Kenny Lau (Apr 22 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509571):
<p>it is Mario's workaround of Leo's changes.</p>

#### [ Kenny Lau (Apr 22 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509572):
<p>So it's in mathlib.</p>

#### [ Kevin Buzzard (Apr 22 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509573):
<p>Well thank you for your answer, which kind of stinks</p>

#### [ Kevin Buzzard (Apr 22 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509612):
<p>Your answer seems to indicate that <code>[group \a]</code> is useless in my structure</p>

#### [ Kevin Buzzard (Apr 22 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509614):
<p>i.e. it didn't insert H\a into the type class inference system anyway</p>

#### [ Kevin Buzzard (Apr 22 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509622):
<p>but wait a minute, isn't this what Patrick told me to do earlier?</p>

#### [ Kenny Lau (Apr 22 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509623):
<p>only typeclasses before the colon are inserted</p>

#### [ Kenny Lau (Apr 22 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509624):
<p>that is Leo's changes</p>

#### [ Kevin Buzzard (Apr 22 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509626):
<p>I am writing another localization interface by the way</p>

#### [ Kevin Buzzard (Apr 22 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509627):
<p>rewriting your universal properties</p>

#### [ Kenny Lau (Apr 22 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509628):
<p>heh</p>

#### [ Mario Carneiro (Apr 22 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125509979):
<p>you don't need to use <code>letI</code>, <code>by exactI</code> is the right solution for this application</p>

#### [ Kenny Lau (Apr 22 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125510034):
<p>aha</p>

#### [ Kevin Buzzard (Apr 22 2018 at 02:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125510848):
<p><a href="https://github.com/kbuzzard/lean-stacks-project/blob/master/src/localization_UMP.lean" target="_blank" title="https://github.com/kbuzzard/lean-stacks-project/blob/master/src/localization_UMP.lean">https://github.com/kbuzzard/lean-stacks-project/blob/master/src/localization_UMP.lean</a></p>

#### [ Kevin Buzzard (Apr 22 2018 at 02:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125510887):
<p>I have finally battled through all my typeclass inference issues.</p>

#### [ Kevin Buzzard (Apr 22 2018 at 02:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125510888):
<p>Kenny, I wrote an even better interface for localization</p>

#### [ Kevin Buzzard (Apr 22 2018 at 02:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125510889):
<p>I put all the stuff which makes up the universal properties into one structure</p>

#### [ Kevin Buzzard (Apr 22 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125510892):
<p><code>is_unique_R_alg_hom</code></p>

#### [ Kevin Buzzard (Apr 22 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125510895):
<p>Mario, it's not quite mathlib-ready, but one day this should probably be in mathlib in some form if localization is in</p>

#### [ Kevin Buzzard (Apr 22 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125510897):
<p>because this file makes the localization stuff usable without ever having to touch the quotient type itself</p>

#### [ Kevin Buzzard (Apr 22 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125510936):
<p>I know because I'm using localization all the time in my schemes work and this work is what led me to the formalisation and the instances in the file I just linked to</p>

#### [ Kevin Buzzard (Apr 22 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125510937):
<p>There's one more instance of the structure which is commonly used which we still have to fill in</p>

#### [ Mario Carneiro (Apr 22 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125511151):
<p>Shouldn't <code>comp_unique</code> read something like <code>is_unique_R_alg_hom sα sβ f → is_unique_R_alg_hom sβ sγ g → is_unique_R_alg_hom sα sγ (g ∘ f)</code>?</p>

#### [ Mario Carneiro (Apr 22 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125511244):
<blockquote>
<p><code>by rw ←HR.symm</code></p>
</blockquote>
<p>what?</p>

#### [ Patrick Massot (Apr 22 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125523403):
<p>Nice one!</p>

#### [ Patrick Massot (Apr 22 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125523409):
<p>Kevin, is there is reason why your file doesn't have <code>open classical</code> towards the top? You write <code>classical.</code> quite a lot</p>

#### [ Kevin Buzzard (Apr 22 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125523921):
<blockquote>
<p>Shouldn't <code>comp_unique</code> read something like <code>is_unique_R_alg_hom sα sβ f → is_unique_R_alg_hom sβ sγ g → is_unique_R_alg_hom sα sγ (g ∘ f)</code>?</p>
</blockquote>
<p>No. That's not even true in general. The standard use of the universal property to prove that certain maps are isomorphisms is via the following argument: "We are given maps X-&gt; Y and Y -&gt; X. The given map from X to Y is the only map X -&gt; Y with a certain property (e.g. being an R-algebra map). The map given Y -&gt; X is the only map Y -&gt; X with a certain property. Composition of two maps with the property has the property. The identity map X -&gt; X is the only map X -&gt; X with the property. Hence X -&gt; Y -&gt; X is the identity map by comp_unique. Furthermore the identity map Y -&gt; Y is the only map Y -&gt; Y with the property. Hence Y -&gt; X -&gt; Y is also the identity. So X isomorphic to Y".</p>

#### [ Kevin Buzzard (Apr 22 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125523973):
<p>The reason your suggestion is not true is that there could be plenty of maps from A to C which don't factor through B.</p>

#### [ Kevin Buzzard (Apr 22 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125524012):
<p>I don't open classical because I typically don't open anything. I am very bad at namespaces in general. A whole bunch of my code is incorrectly sitting in the root namespace. The whole thing needs a clear-up.</p>

#### [ Kevin Buzzard (Apr 22 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125524203):
<blockquote>
<blockquote>
<p><code>by rw ←HR.symm</code></p>
</blockquote>
<p>what?</p>
</blockquote>
<p>ha ha. I think it was getting late at that point. This was kind of stupid. I had that composition of f and g was h, but needed to show <code>forall x, f (g x) = h x</code>and I felt that this should just be an application of a standard lemma but I couldn't find it. So I just wrote "lambda x, by rw (proof that f circ g = h)" a few times, but then something was the other way round so I switched it and then something else was the other way around so I had to switch it back</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125628730):
<blockquote>
<p>Shouldn't <code>comp_unique</code> read something like <code>is_unique_R_alg_hom sα sβ f → is_unique_R_alg_hom sβ sγ g → is_unique_R_alg_hom sα sγ (g ∘ f)</code>?</p>
</blockquote>
<p>Maybe you'll like this one:</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125628734):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">unique_R_of_unique_R_of_unique_Rloc</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">w</span><span class="o">}</span> <span class="o">{</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">uu</span><span class="o">}</span>
<span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">β</span><span class="o">]</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">γ</span><span class="o">]</span>
<span class="o">(</span><span class="n">sα</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">sα</span><span class="o">]</span> <span class="o">(</span><span class="n">fαβ</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">fαβ</span><span class="o">]</span> <span class="o">(</span><span class="n">fβγ</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">)</span> <span class="o">[</span><span class="n">is_ring_hom</span> <span class="n">fβγ</span><span class="o">]</span> <span class="o">:</span>
<span class="n">is_unique_R_alg_hom</span> <span class="n">sα</span> <span class="o">(</span><span class="n">fβγ</span> <span class="err">∘</span> <span class="n">fαβ</span> <span class="err">∘</span> <span class="n">sα</span><span class="o">)</span> <span class="o">(</span><span class="n">fβγ</span> <span class="err">∘</span> <span class="n">fαβ</span><span class="o">)</span>
<span class="bp">→</span> <span class="n">is_unique_R_alg_hom</span> <span class="n">fαβ</span> <span class="o">(</span><span class="n">fβγ</span> <span class="err">∘</span> <span class="n">fαβ</span><span class="o">)</span> <span class="n">fβγ</span>
<span class="bp">→</span> <span class="n">is_unique_R_alg_hom</span> <span class="o">(</span><span class="n">fαβ</span> <span class="err">∘</span> <span class="n">sα</span><span class="o">)</span> <span class="o">(</span><span class="n">fβγ</span>  <span class="err">∘</span> <span class="n">fαβ</span> <span class="err">∘</span> <span class="n">sα</span><span class="o">)</span> <span class="o">(</span><span class="n">fβγ</span><span class="o">)</span> <span class="o">:=</span>
</pre></div>

#### [ Kevin Buzzard (Apr 24 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125628799):
<p>If there's a unique R-alg hom from alpha to gamma and a unique alpha-alg hom from beta to gamma then there's a unique R-alg hom from beta to gamma (and it's the same map)</p>

#### [ Kevin Buzzard (Apr 24 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125628813):
<p>(oh, the R-alg hom from alpha to gamma must be the composite of a given map alpha -&gt; beta and our given alpha-alg map from beta to gamma)</p>

#### [ Johan Commelin (Apr 24 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125629917):
<p>This feels like you want to hit it with Yoneda and reduce it to some basic set-theoretic fact... But that is only instinct</p>

#### [ Johan Commelin (Apr 24 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125629948):
<p>You're looking at both R-alg-homs and alpha-alg-homs... so maybe it is not that straightforward actually</p>

#### [ Kenny Lau (Apr 24 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125629956):
<p>don't get him started on alpha</p>

#### [ Johan Commelin (Apr 24 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125629960):
<p>What do you mean?</p>

#### [ Johan Commelin (Apr 24 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125629968):
<p>There is alpha's everywhere in his code</p>

#### [ Johan Commelin (Apr 24 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125630009):
<p>I was actually surprised when I saw that</p>

#### [ Kenny Lau (Apr 24 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125630023):
<p>don't say "alpha" and any mathematical object in the same sentence in front of kevin buzzard</p>

#### [ Johan Commelin (Apr 24 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125630032):
<p>But he just did that himself!</p>

#### [ Kenny Lau (Apr 24 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125630039):
<p>it doesn't matter</p>

#### [ Kevin Buzzard (Apr 24 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125630634):
<p>Did you notice that when we were doing groups earlier I used alpha to be a group homomorphism just to wind up the CS folk?</p>

#### [ Kevin Buzzard (Apr 24 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125630639):
<p>alpha : G to H</p>

#### [ Kevin Buzzard (Apr 24 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125630684):
<p>The reason I am using alpha for a ring</p>

#### [ Kevin Buzzard (Apr 24 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125630687):
<p>is that the most important ring is called R</p>

#### [ Kevin Buzzard (Apr 24 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125630689):
<p>and then I needed three more</p>

#### [ Kevin Buzzard (Apr 24 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125630693):
<p>but I couldn't face S T U</p>

#### [ Kevin Buzzard (Apr 24 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125630696):
<p>so I thought alpha beta gamma was OK</p>

#### [ Kevin Buzzard (Apr 24 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125630729):
<div class="codehilite"><pre><span></span><span class="k">begin</span>
  <span class="n">intros</span> <span class="n">Hαβ</span> <span class="n">Hβγ</span><span class="o">,</span>
  <span class="n">constructor</span><span class="o">,</span><span class="n">refl</span><span class="o">,</span>
  <span class="n">intros</span> <span class="n">gβγ</span> <span class="n">Hgβγ</span> <span class="n">H1</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">Hαγ</span> <span class="o">:</span> <span class="n">fβγ</span> <span class="err">∘</span> <span class="n">fαβ</span> <span class="bp">=</span> <span class="n">gβγ</span> <span class="err">∘</span> <span class="n">fαβ</span><span class="o">,</span>
    <span class="n">exactI</span> <span class="o">(</span><span class="n">Hαβ</span><span class="bp">.</span><span class="n">is_unique</span> <span class="o">(</span><span class="n">gβγ</span> <span class="err">∘</span> <span class="n">fαβ</span><span class="o">)</span> <span class="n">H1</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span><span class="o">,</span>
  <span class="n">exactI</span> <span class="n">Hβγ</span><span class="bp">.</span><span class="n">is_unique</span> <span class="n">gβγ</span> <span class="n">Hαγ</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Apr 24 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125630733):
<p>That was the proof</p>

#### [ Reid Barton (Apr 24 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125631047):
<p>Haha, I seriously thought up to now that an "alpha-alg-hom" was a map of rings equipped with some fancy extra additional structure, like <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>λ</mi></mrow><annotation encoding="application/x-tex">\lambda</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.69444em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">λ</span></span></span></span>-rings or divided power rings or something.</p>

#### [ Kevin Buzzard (Apr 24 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125631446):
<p>no, it's an alpha-algebra hom :-)</p>

#### [ Kevin Buzzard (Apr 24 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125631453):
<p>YOU SEE YOU CS PEOPLE</p>

#### [ Kevin Buzzard (Apr 24 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125631456):
<p>THE MOMENT YOU CALL RINGS ALPHA</p>

#### [ Kevin Buzzard (Apr 24 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125631461):
<p>WE GET THINGS LIKE THIS HAPPENING</p>

#### [ Johan Commelin (Apr 24 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125631555):
<p>wow, that was pretty <code>α</code>-male</p>

#### [ Kevin Buzzard (Apr 27 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125747509):
<p>Here's today's type class inference issue:</p>

#### [ Kevin Buzzard (Apr 27 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125747511):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">canonical_iso_is_canonical_hom</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">{</span><span class="n">f</span> <span class="n">g</span> <span class="o">:</span> <span class="n">R</span><span class="o">}</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">Spec</span><span class="bp">.</span><span class="n">D&#39;</span> <span class="n">g</span> <span class="err">⊆</span> <span class="n">Spec</span><span class="bp">.</span><span class="n">D&#39;</span> <span class="n">f</span><span class="o">)</span> <span class="o">:</span>
<span class="k">let</span> <span class="n">gbar</span> <span class="o">:=</span> <span class="n">of_comm_ring</span> <span class="n">R</span> <span class="o">(</span><span class="n">powers</span> <span class="n">f</span><span class="o">)</span> <span class="n">g</span> <span class="k">in</span>
<span class="k">let</span> <span class="n">sα</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">loc</span> <span class="o">(</span><span class="n">away</span> <span class="n">f</span><span class="o">)</span> <span class="o">(</span><span class="n">powers</span> <span class="n">gbar</span><span class="o">)</span> <span class="o">:=</span>
  <span class="n">of_comm_ring</span> <span class="o">(</span><span class="n">away</span> <span class="n">f</span><span class="o">)</span> <span class="o">(</span><span class="n">powers</span> <span class="n">gbar</span><span class="o">)</span> <span class="err">∘</span> <span class="n">of_comm_ring</span> <span class="n">R</span> <span class="o">(</span><span class="n">powers</span> <span class="n">f</span><span class="o">)</span> <span class="k">in</span>
<span class="k">let</span> <span class="n">sγ</span> <span class="o">:=</span> <span class="o">(</span><span class="n">of_comm_ring</span> <span class="n">R</span> <span class="o">(</span><span class="n">non_zero_on_U</span> <span class="o">(</span><span class="n">Spec</span><span class="bp">.</span><span class="n">D&#39;</span> <span class="n">g</span><span class="o">)))</span> <span class="k">in</span>
<span class="k">let</span> <span class="n">H2</span> <span class="o">:=</span> <span class="o">(</span><span class="n">canonical_iso</span> <span class="n">H</span><span class="o">)</span><span class="bp">.</span><span class="n">is_ring_hom</span> <span class="k">in</span>
<span class="n">is_unique_R_alg_hom</span> <span class="n">sγ</span> <span class="n">sα</span> <span class="o">(</span><span class="n">canonical_iso</span> <span class="n">H</span><span class="o">)</span><span class="bp">.</span><span class="n">to_fun</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Kevin Buzzard (Apr 27 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125747515):
<p>that won't run</p>

#### [ Kevin Buzzard (Apr 27 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125747523):
<p>but hopefully I can explain the issue</p>

#### [ Kevin Buzzard (Apr 27 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125747533):
<p>I am trying to prove <code>is_unique_R_alg_hom sγ sα (canonical_iso H).to_fun</code></p>

#### [ Kevin Buzzard (Apr 27 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125747592):
<p>but the definition of <code>is_unique_R_alg_hom</code> expects H2 to be deduced from type class inference</p>

#### [ Kevin Buzzard (Apr 27 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125747595):
<p>and I've only managed to prove it the line before</p>

#### [ Kevin Buzzard (Apr 27 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125747597):
<p>so I can solve this with @</p>

#### [ Kevin Buzzard (Apr 27 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125747612):
<p>but given that it would then look like</p>

#### [ Kevin Buzzard (Apr 27 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125747672):
<p>...erm</p>

#### [ Kevin Buzzard (Apr 27 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125747674):
<p>even that didn't work</p>

#### [ Kevin Buzzard (Apr 27 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125747690):
<p><code>@is_unique_R_alg_hom _ _ _ _ _ _ sγ sα (canonical_iso H).to_fun _ _ H2 </code></p>

#### [ Kevin Buzzard (Apr 27 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125747691):
<p>actually it did work, I now have an unrelated problem</p>

#### [ Kevin Buzzard (Apr 27 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125747701):
<p>So can I insert H2 into the type class inference system before I have even started my proof, because I need it to make my term typecheck?</p>

#### [ Kevin Buzzard (Apr 27 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125748084):
<p>I have got it working with <code>@</code></p>

#### [ Kevin Buzzard (Apr 27 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125748085):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">canonical_iso_is_canonical_hom</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">{</span><span class="n">f</span> <span class="n">g</span> <span class="o">:</span> <span class="n">R</span><span class="o">}</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">Spec</span><span class="bp">.</span><span class="n">D&#39;</span> <span class="n">g</span> <span class="err">⊆</span> <span class="n">Spec</span><span class="bp">.</span><span class="n">D&#39;</span> <span class="n">f</span><span class="o">)</span> <span class="o">:</span>
<span class="k">let</span> <span class="n">gbar</span> <span class="o">:=</span> <span class="n">of_comm_ring</span> <span class="n">R</span> <span class="o">(</span><span class="n">powers</span> <span class="n">f</span><span class="o">)</span> <span class="n">g</span> <span class="k">in</span>
<span class="k">let</span> <span class="n">sα</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">loc</span> <span class="o">(</span><span class="n">away</span> <span class="n">f</span><span class="o">)</span> <span class="o">(</span><span class="n">powers</span> <span class="n">gbar</span><span class="o">)</span> <span class="o">:=</span>
  <span class="n">of_comm_ring</span> <span class="o">(</span><span class="n">away</span> <span class="n">f</span><span class="o">)</span> <span class="o">(</span><span class="n">powers</span> <span class="n">gbar</span><span class="o">)</span> <span class="err">∘</span> <span class="n">of_comm_ring</span> <span class="n">R</span> <span class="o">(</span><span class="n">powers</span> <span class="n">f</span><span class="o">)</span> <span class="k">in</span>
<span class="k">let</span> <span class="n">sγ</span> <span class="o">:=</span> <span class="o">(</span><span class="n">of_comm_ring</span> <span class="n">R</span> <span class="o">(</span><span class="n">non_zero_on_U</span> <span class="o">(</span><span class="n">Spec</span><span class="bp">.</span><span class="n">D&#39;</span> <span class="n">g</span><span class="o">)))</span> <span class="k">in</span>
<span class="k">let</span> <span class="n">H2</span> <span class="o">:=</span> <span class="o">(</span><span class="n">canonical_iso</span> <span class="n">H</span><span class="o">)</span><span class="bp">.</span><span class="n">is_ring_hom</span> <span class="k">in</span>
<span class="k">let</span> <span class="n">H3</span> <span class="o">:</span> <span class="n">is_ring_hom</span> <span class="n">sα</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span> <span class="k">in</span>
<span class="k">let</span> <span class="n">H4</span> <span class="o">:</span> <span class="n">is_ring_hom</span> <span class="n">sγ</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span> <span class="k">in</span>
<span class="bp">@</span><span class="n">is_unique_R_alg_hom</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">sγ</span> <span class="n">sα</span> <span class="o">(</span><span class="n">canonical_iso</span> <span class="n">H</span><span class="o">)</span><span class="bp">.</span><span class="n">to_fun</span> <span class="n">H4</span> <span class="n">H3</span> <span class="n">H2</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Kevin Buzzard (Apr 27 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125748090):
<p>The first three lets are simply there to make the statement look clearer</p>

#### [ Kevin Buzzard (Apr 27 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125748098):
<p>the last three are there because type class inference asked for them all</p>

#### [ Reid Barton (Apr 27 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125748163):
<p>Change those last three <code>let</code>s to <code>letI</code> I think</p>

#### [ Kevin Buzzard (Apr 27 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125748209):
<p><code>letI</code> doesn't work there</p>

#### [ Kevin Buzzard (Apr 27 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125748210):
<p>well, it doesn't work for me</p>

#### [ Kevin Buzzard (Apr 27 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125748212):
<p>It works in a proof</p>

#### [ Reid Barton (Apr 27 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125748213):
<p>Sorry, I just noticed this was in term mode</p>

#### [ Kevin Buzzard (Apr 27 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125748214):
<p>but this is before the proof</p>

#### [ Kevin Buzzard (Apr 27 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125748215):
<p>the issue is that we're before the colon</p>

#### [ Kevin Buzzard (Apr 27 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125748216):
<p>I think</p>

#### [ Reid Barton (Apr 27 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125748217):
<p>But I think <code>by letI ...; exact</code> is fine</p>

#### [ Kevin Buzzard (Apr 27 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125748219):
<p>I have only seen letI after the colon</p>

#### [ Reid Barton (Apr 27 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125748230):
<p>Though, it does make me vaguely uneasy to put it in the theorem statement.</p>

#### [ Reid Barton (Apr 27 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125748310):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">canonical_iso_is_canonical_hom</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">{</span><span class="n">f</span> <span class="n">g</span> <span class="o">:</span> <span class="n">R</span><span class="o">}</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">Spec</span><span class="bp">.</span><span class="n">D&#39;</span> <span class="n">g</span> <span class="err">⊆</span> <span class="n">Spec</span><span class="bp">.</span><span class="n">D&#39;</span> <span class="n">f</span><span class="o">)</span> <span class="o">:</span>
<span class="k">let</span> <span class="n">gbar</span> <span class="o">:=</span> <span class="n">of_comm_ring</span> <span class="n">R</span> <span class="o">(</span><span class="n">powers</span> <span class="n">f</span><span class="o">)</span> <span class="n">g</span> <span class="k">in</span>
<span class="k">let</span> <span class="n">sα</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">loc</span> <span class="o">(</span><span class="n">away</span> <span class="n">f</span><span class="o">)</span> <span class="o">(</span><span class="n">powers</span> <span class="n">gbar</span><span class="o">)</span> <span class="o">:=</span>
  <span class="n">of_comm_ring</span> <span class="o">(</span><span class="n">away</span> <span class="n">f</span><span class="o">)</span> <span class="o">(</span><span class="n">powers</span> <span class="n">gbar</span><span class="o">)</span> <span class="err">∘</span> <span class="n">of_comm_ring</span> <span class="n">R</span> <span class="o">(</span><span class="n">powers</span> <span class="n">f</span><span class="o">)</span> <span class="k">in</span>
<span class="k">let</span> <span class="n">sγ</span> <span class="o">:=</span> <span class="o">(</span><span class="n">of_comm_ring</span> <span class="n">R</span> <span class="o">(</span><span class="n">non_zero_on_U</span> <span class="o">(</span><span class="n">Spec</span><span class="bp">.</span><span class="n">D&#39;</span> <span class="n">g</span><span class="o">)))</span> <span class="k">in</span>
<span class="k">by</span> <span class="n">letI</span> <span class="n">H2</span> <span class="o">:=</span> <span class="o">(</span><span class="n">canonical_iso</span> <span class="n">H</span><span class="o">)</span><span class="bp">.</span><span class="n">is_ring_hom</span><span class="bp">;</span> <span class="n">exact</span>
<span class="n">is_unique_R_alg_hom</span> <span class="n">sγ</span> <span class="n">sα</span> <span class="o">(</span><span class="n">canonical_iso</span> <span class="n">H</span><span class="o">)</span><span class="bp">.</span><span class="n">to_fun</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>(untested, hopefully I deleted the right amount of stuff)</p>

#### [ Mario Carneiro (Apr 27 2018 at 02:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125751156):
<p>Using <code>letI</code> in theorem types is fine, and <code>by letI ...; exact</code> or <code>by exactI</code> is the recommended way to introduce a typeclass thing from the context in term mode</p>

#### [ Chris Hughes (Apr 27 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761174):
<p>Don't use let in the statement of a theorem.</p>

#### [ Kevin Buzzard (Apr 27 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761407):
<blockquote>
<p>Don't use let in the statement of a theorem.</p>
</blockquote>
<p>This is easy to fix -- the let is in some sense for my own sanity.</p>

#### [ Mario Carneiro (Apr 27 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761455):
<p>Note that <code>haveI</code> when used in a tactic doesn't actually produce a <code>have</code> term, the result is just like you would get if it were actually inferred by regular tc inference</p>

#### [ Mario Carneiro (Apr 27 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761462):
<p>If in doubt, just <code>#print</code> the statement to make sure it doesn't look weird</p>

#### [ Kevin Buzzard (Apr 27 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761464):
<p>I can't get the syntax right for this</p>

#### [ Kevin Buzzard (Apr 27 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761465):
<p>having tried for 10 seconds</p>

#### [ Kevin Buzzard (Apr 27 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761507):
<p>I need to insert three hypotheses into the type class inference box</p>

#### [ Kevin Buzzard (Apr 27 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761511):
<p>and I don't understand the syntax of this by thing</p>

#### [ Kevin Buzzard (Apr 27 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761521):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">canonical_iso_is_canonical_hom</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">{</span><span class="n">f</span> <span class="n">g</span> <span class="o">:</span> <span class="n">R</span><span class="o">}</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">Spec</span><span class="bp">.</span><span class="n">D&#39;</span> <span class="n">g</span> <span class="err">⊆</span> <span class="n">Spec</span><span class="bp">.</span><span class="n">D&#39;</span> <span class="n">f</span><span class="o">)</span> <span class="o">:</span>
<span class="k">let</span> <span class="n">gbar</span> <span class="o">:=</span> <span class="n">of_comm_ring</span> <span class="n">R</span> <span class="o">(</span><span class="n">powers</span> <span class="n">f</span><span class="o">)</span> <span class="n">g</span> <span class="k">in</span>
<span class="k">let</span> <span class="n">sα</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">loc</span> <span class="o">(</span><span class="n">away</span> <span class="n">f</span><span class="o">)</span> <span class="o">(</span><span class="n">powers</span> <span class="n">gbar</span><span class="o">)</span> <span class="o">:=</span>
  <span class="n">of_comm_ring</span> <span class="o">(</span><span class="n">away</span> <span class="n">f</span><span class="o">)</span> <span class="o">(</span><span class="n">powers</span> <span class="n">gbar</span><span class="o">)</span> <span class="err">∘</span> <span class="n">of_comm_ring</span> <span class="n">R</span> <span class="o">(</span><span class="n">powers</span> <span class="n">f</span><span class="o">)</span> <span class="k">in</span>
<span class="k">let</span> <span class="n">sγ</span> <span class="o">:=</span> <span class="o">(</span><span class="n">of_comm_ring</span> <span class="n">R</span> <span class="o">(</span><span class="n">non_zero_on_U</span> <span class="o">(</span><span class="n">Spec</span><span class="bp">.</span><span class="n">D&#39;</span> <span class="n">g</span><span class="o">)))</span> <span class="k">in</span>
<span class="k">let</span> <span class="n">H2</span> <span class="o">:=</span> <span class="o">(</span><span class="n">canonical_iso</span> <span class="n">H</span><span class="o">)</span><span class="bp">.</span><span class="n">is_ring_hom</span> <span class="k">in</span>
<span class="k">let</span> <span class="n">H3</span> <span class="o">:</span> <span class="n">is_ring_hom</span> <span class="n">sα</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span> <span class="k">in</span>
<span class="k">let</span> <span class="n">H4</span> <span class="o">:</span> <span class="n">is_ring_hom</span> <span class="n">sγ</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span> <span class="k">in</span>
<span class="bp">@</span><span class="n">is_unique_R_alg_hom</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">sγ</span> <span class="n">sα</span> <span class="o">(</span><span class="n">canonical_iso</span> <span class="n">H</span><span class="o">)</span><span class="bp">.</span><span class="n">to_fun</span> <span class="n">H4</span> <span class="n">H3</span> <span class="n">H2</span> <span class="o">:=</span>
</pre></div>

#### [ Kevin Buzzard (Apr 27 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761522):
<p>This works</p>

#### [ Kenny Lau (Apr 27 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761524):
<p>good luck proving that</p>

#### [ Kevin Buzzard (Apr 27 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761562):
<div class="codehilite"><pre><span></span><span class="k">begin</span>
<span class="n">letI</span> <span class="o">:=</span> <span class="o">(</span><span class="n">canonical_iso</span> <span class="n">H</span><span class="o">)</span><span class="bp">.</span><span class="n">is_ring_hom</span><span class="o">,</span>
<span class="k">have</span> <span class="n">H5</span> <span class="o">:=</span> <span class="n">unique_R_alg_from_loc</span> <span class="o">(</span><span class="n">canonical_iso</span> <span class="n">H</span><span class="o">)</span><span class="bp">.</span><span class="n">to_fun</span><span class="o">,</span>
<span class="k">have</span> <span class="n">H6</span> <span class="o">:=</span> <span class="o">(</span><span class="n">canonical_iso</span> <span class="n">H</span><span class="o">)</span><span class="bp">.</span><span class="n">R_alg_hom</span><span class="bp">.</span><span class="n">symm</span><span class="o">,</span>
<span class="n">simp</span> <span class="o">[</span><span class="n">H6</span><span class="o">]</span> <span class="n">at</span> <span class="n">H5</span><span class="o">,</span>
<span class="n">exact</span> <span class="n">H5</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Apr 27 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761565):
<p>done</p>

#### [ Kenny Lau (Apr 27 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761566):
<p>ok you win</p>

#### [ Kevin Buzzard (Apr 27 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761569):
<p>Now I have good interface</p>

#### [ Kevin Buzzard (Apr 27 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761570):
<p>so all the proofs are "this canonical thing is canonical"</p>

#### [ Kevin Buzzard (Apr 27 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761571):
<p>or "this canonical thing is unique"</p>

#### [ Kevin Buzzard (Apr 27 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761573):
<p>or "this unique thing is canonical"</p>

#### [ Kevin Buzzard (Apr 27 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761635):
<p>I was trying to put all three hypotheses into one "by"</p>

#### [ Kevin Buzzard (Apr 27 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761638):
<p>but I don't understand the syntax</p>

#### [ Kevin Buzzard (Apr 27 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761644):
<p>but I've got it working</p>

#### [ Kevin Buzzard (Apr 27 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761645):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">canonical_iso_is_canonical_hom</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">{</span><span class="n">f</span> <span class="n">g</span> <span class="o">:</span> <span class="n">R</span><span class="o">}</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">Spec</span><span class="bp">.</span><span class="n">D&#39;</span> <span class="n">g</span> <span class="err">⊆</span> <span class="n">Spec</span><span class="bp">.</span><span class="n">D&#39;</span> <span class="n">f</span><span class="o">)</span> <span class="o">:</span>
<span class="k">let</span> <span class="n">gbar</span> <span class="o">:=</span> <span class="n">of_comm_ring</span> <span class="n">R</span> <span class="o">(</span><span class="n">powers</span> <span class="n">f</span><span class="o">)</span> <span class="n">g</span> <span class="k">in</span>
<span class="k">let</span> <span class="n">sα</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">loc</span> <span class="o">(</span><span class="n">away</span> <span class="n">f</span><span class="o">)</span> <span class="o">(</span><span class="n">powers</span> <span class="n">gbar</span><span class="o">)</span> <span class="o">:=</span>
  <span class="n">of_comm_ring</span> <span class="o">(</span><span class="n">away</span> <span class="n">f</span><span class="o">)</span> <span class="o">(</span><span class="n">powers</span> <span class="n">gbar</span><span class="o">)</span> <span class="err">∘</span> <span class="n">of_comm_ring</span> <span class="n">R</span> <span class="o">(</span><span class="n">powers</span> <span class="n">f</span><span class="o">)</span> <span class="k">in</span>
<span class="k">let</span> <span class="n">sγ</span> <span class="o">:=</span> <span class="o">(</span><span class="n">of_comm_ring</span> <span class="n">R</span> <span class="o">(</span><span class="n">non_zero_on_U</span> <span class="o">(</span><span class="n">Spec</span><span class="bp">.</span><span class="n">D&#39;</span> <span class="n">g</span><span class="o">)))</span> <span class="k">in</span>
<span class="k">by</span> <span class="n">letI</span> <span class="n">H2</span> <span class="o">:=</span> <span class="o">(</span><span class="n">canonical_iso</span> <span class="n">H</span><span class="o">)</span><span class="bp">.</span><span class="n">is_ring_hom</span><span class="bp">;</span> <span class="n">exact</span>
<span class="k">by</span> <span class="n">letI</span> <span class="n">H3</span> <span class="o">:</span> <span class="n">is_ring_hom</span> <span class="n">sα</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span><span class="bp">;</span> <span class="n">exact</span>
<span class="k">by</span> <span class="n">letI</span> <span class="n">H4</span> <span class="o">:</span> <span class="n">is_ring_hom</span> <span class="n">sγ</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span><span class="bp">;</span> <span class="n">exact</span>
<span class="bp">@</span><span class="n">is_unique_R_alg_hom</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">sγ</span> <span class="n">sα</span> <span class="o">(</span><span class="n">canonical_iso</span> <span class="n">H</span><span class="o">)</span><span class="bp">.</span><span class="n">to_fun</span> <span class="n">H4</span> <span class="n">H3</span> <span class="n">H2</span> <span class="o">:=</span>
</pre></div>

#### [ Kevin Buzzard (Apr 27 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761646):
<p>I can't even parse that</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761649):
<p>and now the moment of truth...</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761698):
<p>wooah</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761699):
<p>stop everything</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761701):
<p>lean has silently crashed</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761761):
<p>OK great, when I restart Lean it just quietly exits</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761771):
<p>Restarting VS Code and I am back up and running</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761814):
<p>and it doesn't work after all</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761869):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">canonical_iso_is_canonical_hom</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">{</span><span class="n">f</span> <span class="n">g</span> <span class="o">:</span> <span class="n">R</span><span class="o">}</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">Spec</span><span class="bp">.</span><span class="n">D&#39;</span> <span class="n">g</span> <span class="err">⊆</span> <span class="n">Spec</span><span class="bp">.</span><span class="n">D&#39;</span> <span class="n">f</span><span class="o">)</span> <span class="o">:</span>
<span class="k">let</span> <span class="n">gbar</span> <span class="o">:=</span> <span class="n">of_comm_ring</span> <span class="n">R</span> <span class="o">(</span><span class="n">powers</span> <span class="n">f</span><span class="o">)</span> <span class="n">g</span> <span class="k">in</span>
<span class="k">let</span> <span class="n">sα</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">loc</span> <span class="o">(</span><span class="n">away</span> <span class="n">f</span><span class="o">)</span> <span class="o">(</span><span class="n">powers</span> <span class="n">gbar</span><span class="o">)</span> <span class="o">:=</span>
  <span class="n">of_comm_ring</span> <span class="o">(</span><span class="n">away</span> <span class="n">f</span><span class="o">)</span> <span class="o">(</span><span class="n">powers</span> <span class="n">gbar</span><span class="o">)</span> <span class="err">∘</span> <span class="n">of_comm_ring</span> <span class="n">R</span> <span class="o">(</span><span class="n">powers</span> <span class="n">f</span><span class="o">)</span> <span class="k">in</span>
<span class="k">let</span> <span class="n">sγ</span> <span class="o">:=</span> <span class="o">(</span><span class="n">of_comm_ring</span> <span class="n">R</span> <span class="o">(</span><span class="n">non_zero_on_U</span> <span class="o">(</span><span class="n">Spec</span><span class="bp">.</span><span class="n">D&#39;</span> <span class="n">g</span><span class="o">)))</span> <span class="k">in</span>
<span class="k">by</span> <span class="n">letI</span> <span class="n">H2</span> <span class="o">:=</span> <span class="o">(</span><span class="n">canonical_iso</span> <span class="n">H</span><span class="o">)</span><span class="bp">.</span><span class="n">is_ring_hom</span><span class="bp">;</span>
<span class="n">letI</span> <span class="n">H3</span> <span class="o">:</span> <span class="n">is_ring_hom</span> <span class="n">sα</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span><span class="bp">;</span>
<span class="n">letI</span> <span class="n">H4</span> <span class="o">:</span> <span class="n">is_ring_hom</span> <span class="n">sγ</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span><span class="bp">;</span> <span class="n">exact</span>
<span class="bp">@</span><span class="n">is_unique_R_alg_hom</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">sγ</span> <span class="n">sα</span> <span class="o">(</span><span class="n">canonical_iso</span> <span class="n">H</span><span class="o">)</span><span class="bp">.</span><span class="n">to_fun</span> <span class="n">H4</span> <span class="n">H3</span> <span class="n">H2</span> <span class="o">:=</span>
</pre></div>


<p>doesn't work</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761871):
<p>It's not a problem because my multi-let <code>@</code> solution works</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125761872):
<p>I'll construct a MWE. I think this is just a syntax thing</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125762346):
<p>gaargh it's not a syntax thing, my MWE is too minimal and strings of <code>by letI ...; exact</code> work fine</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125762486):
<p>My <code>by apply_instance</code> proofs seem to be failing when wrapped up in the outer <code>by</code></p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125762657):
<p>I am torn between giving up and constructing a MWE</p>

#### [ Kenny Lau (Apr 27 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125762659):
<p>lemme help you</p>

#### [ Kenny Lau (Apr 27 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125762660):
<p>give up.</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125762661):
<p>OK</p>

#### [ Kevin Buzzard (Apr 27 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125762662):
<p>thanks</p>

#### [ Kenny Lau (Apr 27 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125762663):
<p>no probs</p>

#### [ Mario Carneiro (Apr 27 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125763632):
<p>Your <code>letI : ... := by apply_instance</code> lines are redundant. If the typeclass system can already find it, there's no reason to add it to the typeclass system. Unless you are trying to limit search depth?</p>

#### [ Mario Carneiro (Apr 27 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125763651):
<p>Also I recommend <code>haveI</code> over <code>letI</code> when possible. The only time you need <code>letI</code> is if you are unfolding the exact definition of the inferred ring or whatever later on in the same proof</p>

#### [ Patrick Massot (Apr 27 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125764739):
<p>About type classes, let me quickly share <a href="https://gist.github.com/PatrickMassot/0d28b74be6f7bc9c0814a87393c91663" target="_blank" title="https://gist.github.com/PatrickMassot/0d28b74be6f7bc9c0814a87393c91663">https://gist.github.com/PatrickMassot/0d28b74be6f7bc9c0814a87393c91663</a> It's a draft of documentation of something that took me an embarrassingly long time to understand (I don't say it's directly related to your issues, it's only general knowledge about type class magic)</p>

#### [ Mario Carneiro (Apr 27 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125764855):
<p>I think the <code>..prod.has_op</code> on the last instance is unnecessary</p>

#### [ Mario Carneiro (Apr 27 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125764861):
<p>it is inferred if you don't specify</p>

#### [ Patrick Massot (Apr 27 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125764904):
<p>oooh</p>

#### [ Patrick Massot (Apr 27 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125764906):
<p>that's even better</p>

#### [ Patrick Massot (Apr 27 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125764909):
<p>How does this new magic trick work?</p>

#### [ Patrick Massot (Apr 27 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125764911):
<p>This file is all about understanding more magic</p>

#### [ Mario Carneiro (Apr 27 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125764989):
<p>The <code>comm_magma.mk</code> structure constructor has the <code>to_has_op</code> parent field as instance implicit, and in structure notation that translates to an optional field</p>

#### [ Mario Carneiro (Apr 27 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125765037):
<p>same with anonymous constructor notation, you could write it as just <code>⟨proof of commutativity⟩</code> instead of <code>{op_comm := proof of commutativity}</code></p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125801928):
<p>Today's typeclass tale of woe:</p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125801930):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">equiv</span>
<span class="n">universes</span> <span class="n">u</span> <span class="n">v</span> <span class="n">w</span> <span class="n">u&#39;</span> <span class="n">v&#39;</span> <span class="n">w&#39;</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">{</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">w</span><span class="o">}</span> <span class="o">{</span><span class="n">α&#39;</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u&#39;</span><span class="o">}</span> <span class="o">{</span><span class="n">β&#39;</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v&#39;</span><span class="o">}</span> <span class="o">{</span><span class="n">γ&#39;</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">w&#39;</span><span class="o">}</span>

<span class="kn">structure</span> <span class="n">canonically_isomorphic_add_group_homs</span> <span class="o">(</span><span class="n">Cα</span> <span class="o">:</span> <span class="n">equiv</span> <span class="n">α</span> <span class="n">α&#39;</span><span class="o">)</span> <span class="o">(</span><span class="n">Cβ</span> <span class="o">:</span> <span class="n">equiv</span> <span class="n">β</span> <span class="n">β&#39;</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">f&#39;</span> <span class="o">:</span> <span class="n">α&#39;</span> <span class="bp">→</span> <span class="n">β&#39;</span><span class="o">)</span>
<span class="o">[</span><span class="n">add_group</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">add_group</span> <span class="n">β</span><span class="o">]</span> <span class="o">[</span><span class="n">add_group</span> <span class="n">α&#39;</span><span class="o">]</span> <span class="o">[</span><span class="n">add_group</span> <span class="n">β&#39;</span><span class="o">]</span>
<span class="o">[</span><span class="n">is_group_hom</span> <span class="n">f</span><span class="o">]</span> <span class="o">[</span><span class="n">is_group_hom</span> <span class="n">f&#39;</span><span class="o">]</span>
<span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Kevin Buzzard (Apr 28 2018 at 03:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125801936):
<div class="codehilite"><pre><span></span>failed to synthesize type class instance for
α : Type u,
β : Type v,
α&#39; : Type u&#39;,
β&#39; : Type v&#39;,
Cα : α ≃ α&#39;,
Cβ : β ≃ β&#39;,
f : α → β,
f&#39; : α&#39; → β&#39;,
_inst_1 : add_group α,
_inst_2 : add_group β,
_inst_3 : add_group α&#39;,
_inst_4 : add_group β&#39;,
_inst_5 : is_group_hom f
⊢ group β&#39;
</pre></div>

#### [ Kevin Buzzard (Apr 28 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125802086):
<p>dammit</p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125802087):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">equiv</span>
<span class="n">universes</span> <span class="n">u</span> <span class="n">v</span> <span class="n">w</span> <span class="n">u&#39;</span> <span class="n">v&#39;</span> <span class="n">w&#39;</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">{</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">w</span><span class="o">}</span> <span class="o">{</span><span class="n">α&#39;</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u&#39;</span><span class="o">}</span> <span class="o">{</span><span class="n">β&#39;</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v&#39;</span><span class="o">}</span> <span class="o">{</span><span class="n">γ&#39;</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">w&#39;</span><span class="o">}</span>

<span class="kn">structure</span> <span class="n">canonically_isomorphic_add_group_homs</span> <span class="o">(</span><span class="n">Cα</span> <span class="o">:</span> <span class="n">equiv</span> <span class="n">α</span> <span class="n">α&#39;</span><span class="o">)</span> <span class="o">(</span><span class="n">Cβ</span> <span class="o">:</span> <span class="n">equiv</span> <span class="n">β</span> <span class="n">β&#39;</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">f&#39;</span> <span class="o">:</span> <span class="n">α&#39;</span> <span class="bp">→</span> <span class="n">β&#39;</span><span class="o">)</span>
<span class="o">[</span><span class="n">Hα</span> <span class="o">:</span> <span class="n">add_group</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">Hβ</span> <span class="o">:</span> <span class="n">add_group</span> <span class="n">β</span><span class="o">]</span> <span class="o">[</span><span class="n">add_group</span> <span class="n">α&#39;</span><span class="o">]</span> <span class="o">[</span><span class="n">Hβ&#39;</span> <span class="o">:</span> <span class="n">add_group</span> <span class="n">β&#39;</span><span class="o">]</span>
<span class="o">[</span><span class="bp">@</span><span class="n">is_group_hom</span> <span class="n">α</span> <span class="n">β</span> <span class="n">Hα</span> <span class="o">(</span><span class="k">by</span> <span class="n">apply_instance</span><span class="o">)</span> <span class="n">f</span><span class="o">]</span> <span class="o">[</span><span class="bp">@</span><span class="n">is_group_hom</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">Hβ&#39;</span> <span class="n">f&#39;</span><span class="o">]</span>
<span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Kevin Buzzard (Apr 28 2018 at 03:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125802128):
<div class="codehilite"><pre><span></span>type mismatch at application
  is_group_hom
term
  Hα
has type
  add_group α
but is expected to have type
  group α
</pre></div>

#### [ Kevin Buzzard (Apr 28 2018 at 03:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125802133):
<p>Damn you Lean</p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125802135):
<p>finding out how to turn an <code>add_group</code> to a <code>group</code> is <em>exactly</em> the kind of question which you should be good at.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125802141):
<p>thus saving me from having to remember the details about names of instances.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125802181):
<p>Why am I constantly running into type class inference issues <span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> ? Is this sort of thing going to change in Lean 4, do you think?</p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125802182):
<p>I find the whole <code>letI</code> stuff both essential and extremely confusing</p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125802185):
<p>I probably need to write some <code>letI</code> docs</p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125802192):
<p>but am I right in thinking that <code>letI</code> is just a hack which we will be doing away with in Lean 4 as the amazing new type class inference system / syntax comes in?</p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125802231):
<p>I know that Mario has work hard to keep up with Leo's changes in the type class inference system</p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125802232):
<p>but that means that it's currently really confusing for end users</p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125802234):
<p>I believe in Lean so much</p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125802239):
<p>and I am really hoping for a beautiful solution.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125802279):
<p>Type class inference issues are stopping me from working right now.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 03:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125802460):
<div class="codehilite"><pre><span></span><span class="kn">variable</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span>
<span class="kn">lemma</span> <span class="n">to_group</span> <span class="o">[</span><span class="n">H</span> <span class="o">:</span> <span class="n">add_group</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span> <span class="n">group</span> <span class="n">α</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>
</pre></div>

#### [ Kevin Buzzard (Apr 28 2018 at 03:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125802462):
<div class="codehilite"><pre><span></span>tactic.mk_instance failed to generate instance for
  group α
state:
α : Type,
H : add_group α
⊢ group α
</pre></div>

#### [ Sebastian Ullrich (Apr 28 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125814582):
<p>There are no plans to change class inference for Lean 4. On the other hand, lifting the distinction between <code>group</code> and <code>add_group</code> is the primary motivation behind refactoring the algebraic hierarchy.</p>

#### [ Kenny Lau (Apr 28 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125814583):
<p>but the algebraic hierarchy also has its own problems, right</p>

#### [ Kenny Lau (Apr 28 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125814601):
<blockquote>
<p>Today's typeclass tale of woe:</p>
</blockquote>
<p>look, I already wrote you an <code>is_add_group_hom</code></p>

#### [ Kevin Buzzard (Apr 28 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125820595):
<p>Oh, I see, I am an idiot. Lean regards the <code>add_group</code> hierarchy as completely different to, the <code>group</code> hierarchy. I have mixed my hierarchies without noticing</p>

#### [ Kevin Buzzard (Apr 28 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125820600):
<p>The reason I have made this mistake</p>

#### [ Kevin Buzzard (Apr 28 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125820603):
<p>is that the two heirarchies are canonically isomorphic</p>

#### [ Kevin Buzzard (Apr 28 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125820604):
<p>and indeed there is a unique canonical isomorphism in each direction</p>

#### [ Kevin Buzzard (Apr 28 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125820609):
<p>however the type class inference procedure might not use these canonical isomorphisms</p>

#### [ Kevin Buzzard (Apr 28 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125820610):
<p>because neither of the hierarchies is "better" than the other one</p>

#### [ Kevin Buzzard (Apr 28 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125820611):
<p>so it would be asymmetric to let type class inference move from one to the other</p>

#### [ Kevin Buzzard (Apr 28 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125820653):
<p>and there is a risk of diamonds if we let it move between them freely</p>

#### [ Kevin Buzzard (Apr 28 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125820654):
<p>On the other hand, to a mathematician, they are the same object</p>

#### [ Kevin Buzzard (Apr 28 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125820655):
<p>canonical isomorphism is different to type class resolution</p>

#### [ Kevin Buzzard (Apr 28 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/125820656):
<p>and I was applying canonical isomorphism</p>

#### [ Johan Commelin (Jun 15 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128108229):
<p>Does this mean I introduced a diamond:</p>
<blockquote>
<p>synthesized type class instance is not definitionally equal to expression inferred by typing rules, synthesized<br>
  subset.submodule 𝔥<br>
inferred<br>
  lie_algebra.to_module ↥𝔥</p>
</blockquote>

#### [ Johan Commelin (Jun 15 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128112522):
<p>So the context is as follows:</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">subset</span><span class="bp">.</span><span class="n">lie_algebra</span> <span class="o">{</span><span class="err">𝔥</span> <span class="o">:</span> <span class="n">set</span> <span class="err">𝔤</span><span class="o">}</span> <span class="o">[</span><span class="n">H</span> <span class="o">:</span> <span class="bp">@</span><span class="n">is_lie_subalgebra</span> <span class="n">R</span> <span class="n">ri</span> <span class="err">𝔤</span> <span class="n">la</span> <span class="err">𝔥</span><span class="o">]</span> <span class="o">:</span>
<span class="n">lie_algebra</span> <span class="n">R</span> <span class="err">𝔥</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">bracket</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="bp">⟨</span><span class="o">[</span><span class="n">x</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span><span class="n">y</span><span class="bp">.</span><span class="mi">1</span><span class="o">],</span> <span class="n">is_lie_subalgebra</span><span class="bp">.</span><span class="n">closed</span> <span class="bp">_</span> <span class="n">x</span><span class="bp">.</span><span class="mi">2</span> <span class="n">y</span><span class="bp">.</span><span class="mi">2</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">left_linear</span> <span class="o">:=</span> <span class="k">begin</span>
    <span class="n">intro</span> <span class="n">y</span><span class="o">,</span>
    <span class="n">constructor</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">intros</span> <span class="n">x₁</span> <span class="n">x₂</span><span class="o">,</span>
      <span class="n">apply</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span><span class="o">,</span>
      <span class="n">simp</span><span class="o">,</span>
      <span class="n">apply</span> <span class="o">(</span><span class="n">lie_algebra</span><span class="bp">.</span><span class="n">left_linear</span> <span class="n">y</span><span class="o">)</span><span class="bp">.</span><span class="n">add</span><span class="o">,</span> <span class="c1">-- FAILS</span>
      <span class="n">sorry</span> <span class="o">},</span>
    <span class="o">{</span> <span class="n">intros</span> <span class="n">r</span> <span class="n">x</span><span class="o">,</span>
      <span class="n">apply</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span><span class="o">,</span>
      <span class="c1">-- apply (lie_algebra.left_linear y).smul, FAILS</span>
      <span class="n">sorry</span> <span class="o">}</span>
  <span class="kn">end</span><span class="o">,</span>
  <span class="n">right_linear</span> <span class="o">:=</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">alternating</span> <span class="o">:=</span> <span class="k">assume</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span><span class="bp">_⟩</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="err">$</span> <span class="n">lie_algebra</span><span class="bp">.</span><span class="n">alternating</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">Jacobi_identity</span> <span class="o">:=</span> <span class="k">assume</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span><span class="bp">_⟩</span> <span class="bp">⟨</span><span class="n">y</span><span class="o">,</span><span class="bp">_⟩</span> <span class="bp">⟨</span><span class="n">z</span><span class="o">,</span><span class="bp">_⟩</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="err">$</span> <span class="n">lie_algebra</span><span class="bp">.</span><span class="n">Jacobi_identity</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">anti_comm</span> <span class="o">:=</span> <span class="k">assume</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span><span class="bp">_⟩</span> <span class="bp">⟨</span><span class="n">y</span><span class="o">,</span><span class="bp">_⟩</span><span class="o">,</span> <span class="n">subtype</span><span class="bp">.</span><span class="n">eq</span> <span class="err">$</span> <span class="n">lie_algebra</span><span class="bp">.</span><span class="n">anti_comm</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span>
<span class="o">}</span>
</pre></div>

#### [ Johan Commelin (Jun 15 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128112567):
<p>How do I tell Lean that it should infer <code>subset.submodule 𝔥</code>, instead of <code>lie_algebra.to_module ↥𝔥</code>.</p>

#### [ Johan Commelin (Jun 15 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128112594):
<p>I really don't get why the type class system is tripping up in this case. After all, the first instance unifies completely. The second instance has one meta-variable in it (and rightly so, because it can't infer that <code>𝔥</code> is a <code>lie_algebra</code> since that is exactly what I'm trying to prove.</p>

#### [ Johan Commelin (Jun 15 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128112638):
<p>So it seems to me like the type class inference went down a wrong path, but still got convinced that it did a good job. (While the correct path is actually there in Lean.)</p>

#### [ Johan Commelin (Jun 15 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128114320):
<p>Aaaahhrg.....</p>
<div class="codehilite"><pre><span></span><span class="o">[</span><span class="n">class_instances</span><span class="o">]</span>  <span class="n">class</span><span class="bp">-</span><span class="kn">instance</span> <span class="n">resolution</span> <span class="n">trace</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">0</span><span class="o">)</span> <span class="err">?</span><span class="n">x_0</span> <span class="o">:</span> <span class="n">has_bracket</span> <span class="err">𝔤</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">commutator_bracket</span> <span class="err">?</span><span class="n">x_1</span> <span class="err">?</span><span class="n">x_2</span> <span class="err">?</span><span class="n">x_3</span> <span class="err">?</span><span class="n">x_4</span> <span class="err">?</span><span class="n">x_5</span> <span class="err">?</span><span class="n">x_6</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">1</span><span class="o">)</span> <span class="err">?</span><span class="n">x_2</span> <span class="o">:</span> <span class="n">comm_ring</span> <span class="err">?</span><span class="n">x_1</span> <span class="o">:=</span> <span class="n">ri</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">1</span><span class="o">)</span> <span class="err">?</span><span class="n">x_4</span> <span class="o">:</span> <span class="bp">@</span><span class="n">lie_algebra</span> <span class="n">R</span> <span class="err">?</span><span class="n">x_3</span> <span class="n">ri</span> <span class="o">:=</span> <span class="n">la</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">1</span><span class="o">)</span> <span class="err">?</span><span class="n">x_6</span> <span class="o">:</span> <span class="n">ring</span> <span class="err">𝔤</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">nonneg_ring</span><span class="bp">.</span><span class="n">to_ring</span> <span class="err">?</span><span class="n">x_7</span> <span class="err">?</span><span class="n">x_8</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">2</span><span class="o">)</span> <span class="err">?</span><span class="n">x_8</span> <span class="o">:</span> <span class="n">nonneg_ring</span> <span class="err">𝔤</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">linear_nonneg_ring</span><span class="bp">.</span><span class="n">to_nonneg_ring</span> <span class="err">?</span><span class="n">x_9</span> <span class="err">?</span><span class="n">x_10</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">1</span><span class="o">)</span> <span class="err">?</span><span class="n">x_6</span> <span class="o">:</span> <span class="n">ring</span> <span class="err">𝔤</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">domain</span><span class="bp">.</span><span class="n">to_ring</span> <span class="err">?</span><span class="n">x_7</span> <span class="err">?</span><span class="n">x_8</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">2</span><span class="o">)</span> <span class="err">?</span><span class="n">x_8</span> <span class="o">:</span> <span class="n">domain</span> <span class="err">𝔤</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">linear_nonneg_ring</span><span class="bp">.</span><span class="n">to_domain</span> <span class="err">?</span><span class="n">x_9</span> <span class="err">?</span><span class="n">x_10</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">2</span><span class="o">)</span> <span class="err">?</span><span class="n">x_8</span> <span class="o">:</span> <span class="n">domain</span> <span class="err">𝔤</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">to_domain</span> <span class="err">?</span><span class="n">x_9</span> <span class="err">?</span><span class="n">x_10</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">3</span><span class="o">)</span> <span class="err">?</span><span class="n">x_10</span> <span class="o">:</span> <span class="n">linear_ordered_ring</span> <span class="err">𝔤</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">linear_nonneg_ring</span><span class="bp">.</span><span class="n">to_linear_ordered_ring</span> <span class="err">?</span><span class="n">x_11</span> <span class="err">?</span><span class="n">x_12</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">3</span><span class="o">)</span> <span class="err">?</span><span class="n">x_10</span> <span class="o">:</span> <span class="n">linear_ordered_ring</span> <span class="err">𝔤</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">linear_ordered_field</span><span class="bp">.</span><span class="n">to_linear_ordered_ring</span> <span class="err">?</span><span class="n">x_11</span> <span class="err">?</span><span class="n">x_12</span>
<span class="o">[</span><span class="n">class_instances</span><span class="o">]</span> <span class="o">(</span><span class="mi">4</span><span class="o">)</span> <span class="err">?</span><span class="n">x_12</span> <span class="o">:</span> <span class="n">linear_ordered_field</span> <span class="err">𝔤</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">discrete_linear_ordered_field</span><span class="bp">.</span><span class="n">to_linear_ordered_field</span> <span class="err">?</span><span class="n">x_13</span> <span class="err">?</span><span class="n">x_14</span>
</pre></div>


<p>[the list goes on and on...]</p>

#### [ Johan Commelin (Jun 15 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128114327):
<p>No stupid! It's a Lie algebra!</p>

#### [ Johan Commelin (Jun 15 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128114337):
<p>Everywhere in this file it has realised immediately that <code>𝔤</code> is a Lie algebra, and therefore has a bracket.</p>

#### [ Johan Commelin (Jun 15 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128114338):
<p>But somehow, here it messes up completely.</p>

#### [ Andrew Ashworth (Jun 15 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128114684):
<p>I notice type class inference issues are quite common in this chat. Maybe in the future a visualization aide would be helpful for people trying to debug  the process</p>

#### [ Andrew Ashworth (Jun 15 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128114691):
<p>Actually for myself I don't know any better method to debug it than to write out the expression in full, and then in order work forwards as if I was doing the search by hand...</p>

#### [ Johan Commelin (Jun 15 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128114731):
<p>Right... which is not really what you would expect in this "computer-era"</p>

#### [ Andrew Ashworth (Jun 15 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128115009):
<p>you'd be disappointed in how much paper I go through while using a computerized theorem prover... or programming in general</p>

#### [ Mario Carneiro (Jun 15 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128115071):
<p>I have mentioned this in previous instance issues, but <code>comm_ring ?x_1</code> is a bad sign in an instance trace, that will usually run away</p>

#### [ Mario Carneiro (Jun 15 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128115074):
<p>what is the type of <code>commutator_bracket</code>?</p>

#### [ Johan Commelin (Jun 15 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128115592):
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">{</span><span class="n">S</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">ring</span> <span class="n">S</span><span class="o">]</span>
<span class="kn">instance</span> <span class="n">commutator_bracket</span> <span class="o">:</span> <span class="n">has_bracket</span> <span class="n">S</span> <span class="o">:=</span> <span class="bp">⟨λ</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="n">x</span><span class="bp">*</span><span class="n">y</span> <span class="bp">-</span> <span class="n">y</span><span class="bp">*</span><span class="n">x</span><span class="bp">⟩</span>
</pre></div>

#### [ Mario Carneiro (Jun 15 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128115668):
<p>That can't be right, the printout has six variables not two</p>

#### [ Mario Carneiro (Jun 15 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128115709):
<p>what does <code>#print commutator_bracket</code> show?</p>

#### [ Johan Commelin (Jun 15 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128115711):
<p>Anyway, my point is that <code>𝔤</code> is a Lie algebra, and by definition that means it <code>extends has_bracket</code>. So I would hope that Lean could figure this one out.</p>

#### [ Johan Commelin (Jun 15 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128115718):
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="kn">instance</span><span class="o">]</span>
<span class="kn">protected</span> <span class="n">def</span> <span class="n">commutator_bracket</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">}</span> <span class="o">[</span><span class="n">ri</span> <span class="o">:</span> <span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">{</span><span class="err">𝔤</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_2</span><span class="o">}</span> <span class="o">[</span><span class="n">la</span> <span class="o">:</span> <span class="n">lie_algebra</span> <span class="n">R</span> <span class="err">𝔤</span><span class="o">]</span> <span class="o">{</span><span class="n">S</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_3</span><span class="o">}</span> <span class="o">[</span><span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">ring</span> <span class="n">S</span><span class="o">],</span>
  <span class="n">has_bracket</span> <span class="n">S</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="o">{</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">}</span> <span class="o">[</span><span class="n">ri</span> <span class="o">:</span> <span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">{</span><span class="err">𝔤</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_2</span><span class="o">}</span> <span class="o">[</span><span class="n">la</span> <span class="o">:</span> <span class="n">lie_algebra</span> <span class="n">R</span> <span class="err">𝔤</span><span class="o">]</span> <span class="o">{</span><span class="n">S</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_3</span><span class="o">}</span> <span class="o">[</span><span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">ring</span> <span class="n">S</span><span class="o">],</span>
  <span class="o">{</span><span class="n">bracket</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">S</span><span class="o">),</span> <span class="n">x</span> <span class="bp">*</span> <span class="n">y</span> <span class="bp">-</span> <span class="n">y</span> <span class="bp">*</span> <span class="n">x</span><span class="o">}</span>
</pre></div>

#### [ Mario Carneiro (Jun 15 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128115721):
<p>there's your problem</p>

#### [ Johan Commelin (Jun 15 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128115722):
<p>Which is crazy...</p>

#### [ Johan Commelin (Jun 15 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128115728):
<p>It pulls in way too much stuff.</p>

#### [ Mario Carneiro (Jun 15 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128115732):
<p>did you <code>include</code> stuff at the top maybe?</p>

#### [ Mario Carneiro (Jun 15 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128115807):
<p>try defining it outside the section, this instance has nothing to do with lie algebras</p>

#### [ Johan Commelin (Jun 15 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128115819):
<p>Yes... thanks for catching that!</p>

#### [ Johan Commelin (Jun 15 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128115879):
<p>Hmm, I need to run. In fact, I should try to get rid of those <code>include ri la</code>, but that seems to be non-trivial.</p>

#### [ Johan Commelin (Jun 15 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/more%20type%20class%20inference%20issues/near/128115887):
<p>Anyway, I'll be back later. AFK</p>


{% endraw %}
