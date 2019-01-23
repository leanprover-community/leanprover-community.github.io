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
I find myself needing a few lemmas about parallel transport through trivial bundles. (In the first case, this is literally the case, the later ones are close analogues.)

````
universes u₁ u₂ 

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
````

#### [ Scott Morrison (Apr 27 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/transport%20through%20trivial%20bundles/near/125769016):
Are these welcome in `mathlib`? If so, where do they go?

#### [ Scott Morrison (Apr 27 2018 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/transport%20through%20trivial%20bundles/near/125769054):
(These all arise after using `cases` on hypotheses in fairly harmless ways.)

#### [ Scott Morrison (Apr 28 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/transport%20through%20trivial%20bundles/near/125803956):
I made a PR for this at <https://github.com/leanprover/mathlib/pull/124>.

#### [ Johan Commelin (Apr 28 2018 at 05:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/transport%20through%20trivial%20bundles/near/125805005):
This is all going to follow from your `transportable` stuff later on, I guess...

#### [ Johan Commelin (Apr 28 2018 at 05:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/transport%20through%20trivial%20bundles/near/125805006):
I mean, parallel transport in maths is an instance of transport of structure...


{% endraw %}
