---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/03820finhasnorecursor.html
---

## Stream: [general](index.html)
### Topic: [fin has no recursor](03820finhasnorecursor.html)

---


{% raw %}
#### [ Kenny Lau (Mar 30 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fin%20has%20no%20recursor/near/124402350):
<p>fin doesn’t have the morally correct recursor. we should prove it maybe.</p>

#### [ Mario Carneiro (Mar 30 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fin%20has%20no%20recursor/near/124402455):
<p>There are two obvious approaches: using <code>fz</code> and <code>fs</code> like in <code>fin2</code>, or by peeling off the right end instead, with <code>raise_fin</code> and <code>last</code> or whatever you want to call them</p>

#### [ Mario Carneiro (Mar 30 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fin%20has%20no%20recursor/near/124402457):
<p>there should be more consistent naming here...</p>

#### [ Mario Carneiro (Mar 30 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fin%20has%20no%20recursor/near/124402660):
<div class="codehilite"><pre><span></span>@[elab_as_eliminator] def fin.succ_rec
  {C : ∀ n, fin n → Sort*}
  (H0 : ∀ n, C (succ n) 0)
  (Hs : ∀ n i, C n i → C (succ n) i.succ) : ∀ {n : ℕ} (i : fin n), C n i
| 0 i := i.elim0
| (succ n) ⟨0, _⟩ := H0 _
| (succ n) ⟨succ i, h⟩ := Hs _ _ (fin.succ_rec ⟨i, lt_of_succ_lt_succ h⟩)

@[elab_as_eliminator] def fin.succ_rec_on {n : ℕ} (i : fin n)
  {C : ∀ n, fin n → Sort*}
  (H0 : ∀ n, C (succ n) 0)
  (Hs : ∀ n i, C n i → C (succ n) i.succ) : C n i :=
i.succ_rec H0 Hs
</pre></div>


{% endraw %}
