---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/65806continuousclass.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [continuous class](https://leanprover-community.github.io/archive/116395maths/65806continuousclass.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Jul 30 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20class/near/130544108):
<p>Should we turn <code>continuous</code> into a class <code>is_continuous</code> like we did for group homorphisms? I spent quite a lot of time explicitly invoking lemmas that could be handled by type class inference. Same question for uniform continuity.</p>

#### [ Johan Commelin (Jul 30 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20class/near/130559925):
<p>I think this is a very good idea. It's <del>long</del>high (thanks, Kenny) time it is turned in to a class.</p>

#### [ Kevin Buzzard (Jul 30 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20class/near/130562916):
<p>Should we turn everything which returns a proposition into a class? There will be no diamonds! Why is this not a no-brainer? Johannes wrote <code>def continuous (f : α → β) := ∀s, is_open s → is_open (f ⁻¹' s)</code> in <code>analysis/topology/continuity.lean</code> so he has chosen to make a definition, and he knows what he's doing. Patrick is proposing instead using a class, but propositions are useful sometimes. But you could make the class a proposition, right? <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> why is this not a class "by default"?</p>

#### [ Patrick Massot (Jul 30 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20class/near/130564662):
<p>About what Johannes wrote: I think this was a very long time ago and maybe it wasn't a conscious decision (for me everything written before I started using Lean is ancient).</p>

#### [ Johannes Hölzl (Jul 30 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20class/near/130566344):
<p><code>continuous</code> needs to stay a definition, otherwise a lot of proofs break. I would prefer to use <code>apply_rules</code> and maybe <code>auto_param</code> instead of type classes. The problem with the type class mechanism is that it doesn't handle composition of functions very well. I'm still not sure if using the type class mechanism to handle morphisms is a good idea.</p>

#### [ Kevin Buzzard (Jul 30 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20class/near/130566684):
<p>This is interesting -- I don't understand this at all. It certainly sounds like a proof that not everything which is a proposition should be handled by the type class inference system! So the issue is the instance corresponding to "if f and g are continuous then so is f o g" is poorly behaved? Why is this any different to "if G and H are groups then so is G x H"?</p>

#### [ Kevin Buzzard (Jul 30 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20class/near/130566714):
<p>Is it the difference between <code>f ∘ g</code> and <code>λ x, f (g x)</code>?</p>

#### [ Johannes Hölzl (Jul 30 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20class/near/130567262):
<p>the type class mechanism needs to be very fast, and it is often very annoying if one wants to force a specific type class instance (i.e. writing it down using <code>@t A _inst1 ...</code>). So, yes: many things shouln't be type class instances.</p>

#### [ Patrick Massot (Jul 30 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20class/near/130567582):
<p>Ok, I'll try playing with <code>apply_rules</code> (I had no luck with <code>apply_rules</code> and <code>tendsto</code> so I'm not very optimistic)</p>

#### [ Johannes Hölzl (Jul 30 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20class/near/130567592):
<p>Hm, yes we might have the same problem</p>

#### [ Reid Barton (Jul 30 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20class/near/130575267):
<p>Yes, I had the same experiences.</p>
<ul>
<li>
<p>I tried making a type class <code>is_continuous</code> but I couldn't get inference to work in even some simple cases, I think involving function composition. But it's possible I didn't set things up quite right. Does the type class work well for group homomorphisms? I haven't had occasion to use that.</p>
</li>
<li>
<p>I've been happy with a tactic which just repeatedly tries to apply <code>continuous.comp</code> and <code>continuous_fst</code> and so on. But it doesn't work to literally use <code>apply</code>. Possibly the reason is that <code>continuous</code> is a Pi type and this causes <code>apply</code> to guess the wrong number of <code>_</code>s to insert (I think Mario explained this once). Anyways it works fine to use <code>refine</code> and manually specify the correct number of arguments.</p>
</li>
</ul>

#### [ Reid Barton (Jul 30 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/continuous%20class/near/130575487):
<p>What I'm currently using: <a href="https://gist.github.com/rwbarton/d088776fa881a00c6820a02d14c5c9e0" target="_blank" title="https://gist.github.com/rwbarton/d088776fa881a00c6820a02d14c5c9e0">https://gist.github.com/rwbarton/d088776fa881a00c6820a02d14c5c9e0</a><br>
It's based on (a somewhat old version at this point of) Scott's <code>tidy</code> library.</p>


{% endraw %}
