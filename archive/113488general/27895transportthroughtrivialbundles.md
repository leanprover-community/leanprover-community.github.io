---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/27895transportthroughtrivialbundles.html
---

## Stream: [general](index.html)
### Topic: [transport through trivial bundles](27895transportthroughtrivialbundles.html)

---


{% raw %}
#### [ Scott Morrison (Apr 27 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/transport%20through%20trivial%20bundles/near/125769004):
<p>I find myself needing a few lemmas about parallel transport through trivial bundles. (In the first case, this is literally the case, the later ones are close analogues.)</p>
<div class="codehilite"><pre><span></span>universes u₁ u₂

@[simp] lemma {u₁ u₂} parallel_transport_for_trivial_bundles {α : Sort u₁} {a b : α} {β : Sort u₂} (p : a = b) (x : β) : @eq.rec α a (λ _, β) x b p = x :=
begin
  induction p,
  simp,
end

@[simp] lemma plift.rec.constant {α : Sort u₁} {β : Sort u₂} (b : β) : @plift.rec α (λ _, β) (λ _, b) = λ _, b :=
begin
  apply funext,
  intros,
  cases x,
  refl,
end

@[simp] lemma ulift.rec.constant {α : Type u₁} {β : Sort u₂} (b : β) : @ulift.rec α (λ _, β) (λ _, b) = λ _, b :=
begin
  apply funext,
  intros,
  cases x,
  refl,
end
</pre></div>

#### [ Scott Morrison (Apr 27 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/transport%20through%20trivial%20bundles/near/125769016):
<p>Are these welcome in <code>mathlib</code>? If so, where do they go?</p>

#### [ Scott Morrison (Apr 27 2018 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/transport%20through%20trivial%20bundles/near/125769054):
<p>(These all arise after using <code>cases</code> on hypotheses in fairly harmless ways.)</p>

#### [ Scott Morrison (Apr 28 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/transport%20through%20trivial%20bundles/near/125803956):
<p>I made a PR for this at &lt;<a href="https://github.com/leanprover/mathlib/pull/124" target="_blank" title="https://github.com/leanprover/mathlib/pull/124">https://github.com/leanprover/mathlib/pull/124</a>&gt;.</p>

#### [ Johan Commelin (Apr 28 2018 at 05:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/transport%20through%20trivial%20bundles/near/125805005):
<p>This is all going to follow from your <code>transportable</code> stuff later on, I guess...</p>

#### [ Johan Commelin (Apr 28 2018 at 05:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/transport%20through%20trivial%20bundles/near/125805006):
<p>I mean, parallel transport in maths is an instance of transport of structure...</p>


{% endraw %}
