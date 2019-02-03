---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/98259Coercion.html
---

## Stream: [general](index.html)
### Topic: [Coercion](98259Coercion.html)

---


{% raw %}
#### [ Ned Summers (Jul 23 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coercion/near/130142384):
<p>For context, in Scott Morrison's category theory code he introduces isomorphism as the structure:</p>
<div class="codehilite"><pre><span></span>structure Isomorphism {C : Type u} [category.{u v} C] (X Y : C) :=
  (morphism : X ⟶ Y)
  (inverse : Y ⟶ X)
  (witness_1 : morphism ≫ inverse = 𝟙 X . obviously)
  (witness_2 : inverse ≫ morphism = 𝟙 Y . obviously)
</pre></div>


<p>This seems like a perfectly fine way of doing this. Later in the document he uses</p>
<div class="codehilite"><pre><span></span>instance Isomorphism_coercion_to_morphism : has_coe (Isomorphism.{u v} X Y) (X ⟶ Y) :=
{ coe := Isomorphism.morphism }
</pre></div>


<p>I can't seem to figure out what a coercion actually is, or what it's use is. It seems like it might be useful. I'm currently trying to state and prove a theorem where a morphism is shown to be an isomorphism and this looks like a promising way of moving from isomorphic objects to isomorphisms. Help much appreciated.</p>

#### [ Patrick Massot (Jul 23 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coercion/near/130143610):
<p><a href="https://leanprover.github.io/theorem_proving_in_lean/type_classes.html#coercions-using-type-classes" target="_blank" title="https://leanprover.github.io/theorem_proving_in_lean/type_classes.html#coercions-using-type-classes">https://leanprover.github.io/theorem_proving_in_lean/type_classes.html#coercions-using-type-classes</a></p>

#### [ Ned Summers (Jul 23 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coercion/near/130144000):
<p>Thanks</p>

#### [ Kevin Buzzard (Jul 23 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coercion/near/130170341):
<p>A coercion is just a way of moving from one type to another by applying a function which you don't want to continually mention, you just want Lean to do it automatically. See that the coercion is defined using <code>instance</code> not <code>definition</code>? That means "define it, and let the type class inference system use it". The type class inference system will then apply it whenever necessary.</p>

#### [ Chris Hughes (Jul 23 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coercion/near/130170444):
<p>Shouldn't that be a <code>has_coe_to_fun</code> not a <code>has_coe</code>?</p>

#### [ Mario Carneiro (Jul 24 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coercion/near/130180701):
<p>No, because the target isn't a function type (that arrow is not a regular arrow)</p>

#### [ Anthony Bordg (Oct 05 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coercion/near/135248099):
<p>Hi,<br>
in the current library is there already a coercion to see a field as a comm_semiring ? <br>
One can combine <code>field.to_comm_ring </code> with <code>comm_ring.to_comm_semiring</code>, but maybe there is a more direct way.<br>
Thanks</p>

#### [ Johan Commelin (Oct 05 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coercion/near/135248182):
<p>The typeclass system should do that for you. Usually you don't need to touch it.</p>

#### [ Johan Commelin (Oct 05 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coercion/near/135248235):
<p>If you really need it:</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">{</span><span class="n">K</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">field</span> <span class="n">K</span><span class="o">]</span> <span class="o">:</span> <span class="n">comm_semiring</span> <span class="n">K</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>
</pre></div>

#### [ Johan Commelin (Oct 05 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coercion/near/135248242):
<p>You can usually also insert the <code>by apply_instance</code> into your proofs if you need it.</p>

#### [ Anthony Bordg (Oct 05 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coercion/near/135248929):
<blockquote>
<p>The typeclass system should do that for you. Usually you don't need to touch it.</p>
</blockquote>
<p>The typeclass system doesn't help here, but the code you gave me with "instance" works fine.<br>
Thank you <span class="user-mention" data-user-id="112680">@Johan Commelin</span></p>

#### [ Kevin Buzzard (Oct 05 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coercion/near/135259239):
<p>This instance code is exactly using the type class inference system to construct the term which you asked for. But usually the type class inference system can be trusted to handle this question completely, and users don't have to construct this term at all. Why did you want this coercion?</p>

#### [ Anthony Bordg (Oct 05 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coercion/near/135265433):
<blockquote>
<p>This instance code is exactly using the type class inference system to construct the term which you asked for. But usually the type class inference system can be trusted to handle this question completely, and users don't have to construct this term at all. Why did you want this coercion?</p>
</blockquote>
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span>  I want to use <code>polynomial.eval</code> with a field (the default argument is a commutative semiring).</p>

#### [ Johan Commelin (Oct 05 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coercion/near/135265444):
<p>That should work out of the box</p>

#### [ Kevin Buzzard (Oct 05 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coercion/near/135265490):
<p>Are these typeclasses not just all resolved using type class inference?</p>

#### [ Kevin Buzzard (Oct 05 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coercion/near/135265684):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">polynomial</span>
<span class="kn">definition</span> <span class="n">KX</span> <span class="o">(</span><span class="n">K</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">field</span> <span class="n">K</span><span class="o">]</span> <span class="o">:=</span> <span class="n">polynomial</span> <span class="n">K</span>
</pre></div>


<p>It just works when you do it this way <span class="user-mention" data-user-id="125073">@Anthony Bordg</span></p>

#### [ Kevin Buzzard (Oct 05 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Coercion/near/135265787):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">polynomial</span>

<span class="kn">definition</span> <span class="n">KX</span> <span class="o">(</span><span class="n">K</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">field</span> <span class="n">K</span><span class="o">]</span> <span class="o">:=</span> <span class="n">polynomial</span> <span class="n">K</span>

<span class="kn">open</span> <span class="n">polynomial</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">K</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">[</span><span class="n">field</span> <span class="n">K</span><span class="o">]</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">K</span><span class="o">]</span>

<span class="kn">lemma</span> <span class="n">eval_works</span> <span class="o">(</span><span class="n">k</span> <span class="o">:</span> <span class="n">K</span><span class="o">)</span> <span class="o">:</span> <span class="kn">eval</span> <span class="n">k</span> <span class="n">X</span> <span class="bp">=</span> <span class="n">k</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span>
</pre></div>


{% endraw %}
