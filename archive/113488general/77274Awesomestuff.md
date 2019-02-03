---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/77274Awesomestuff.html
---

## Stream: [general](index.html)
### Topic: [Awesome stuff](77274Awesomestuff.html)

---


{% raw %}
#### [ Simon Hudon (Mar 08 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Awesome%20stuff/near/123464026):
<p>My mind was just blown by how useful <code>has_coe_to_fun</code> is. I constructed a morphism between applicative functors:</p>
<div class="codehilite"><pre><span></span>variables (f : Type u → Type v) [applicative f]
variables (g : Type u → Type w) [applicative g]

structure applicative_morphism : Type (max (u+1) v w) :=
  (F : ∀ {α : Type u}, f α → g α)
  (preserves_pure&#39; : ∀ {α : Type u} (x : α), F (pure x) = pure x)
  (preserves_seq&#39; : ∀ {α β : Type u} (x : f (α → β)) (y : f α), F (x &lt;*&gt; y) = F x &lt;*&gt; F y)
</pre></div>


<p>and defined the following instance:</p>
<div class="codehilite"><pre><span></span>instance : has_coe_to_fun (applicative_morphism f g) :=
{ F := λ _, ∀ {α}, f α → g α,
  coe := λ m, m.F }
</pre></div>


<p>It's already pretty cool that, given <code>x : f int</code> and <code>m : applicative_morphism f g</code> I can write <code>f x</code> to just apply it. What really blew my mind is that I can write <code>@f int x</code> to make the <code>{α : Type u}</code> of <code>F</code> explicit.</p>


{% endraw %}
