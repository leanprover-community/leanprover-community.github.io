---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/74298filters.html
---

## Stream: [general](index.html)
### Topic: [filters](74298filters.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rohan Mitta (Sep 05 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filters/near/133377621):
Hi,

I'm attempting to prove a proposition from a Topology book and am getting stuck using filters, which I'm not very comfortable with in lean. Can anyone help me with the first sorry? I'm pretty sure that step is true due to the uniform continuity of f but I can't figure out what to do with it.

```lean
import analysis.topology.topological_space
import analysis.topology.continuity
import analysis.metric_space
import analysis.topology.uniform_space
import order.filter

noncomputable theory

theorem complete_iff_of_uniform_cts_bij {α : Type*} [metric_space α] {β : Type*} [metric_space β] (f : α → β) 
    (g : β → α) (Hf : uniform_continuous f) (Hg : uniform_continuous g) (left_inv : function.left_inverse g f)
    (right_inv : function.right_inverse g f) : complete_space α ↔ complete_space β := 
begin
  split,
    intro H1,
    cases H1, split,
    intros filt Hfilt, 
  
    have H2 := H1 (cauchy_map Hg Hfilt),
    cases H2 with x H_converges_to_x,
    existsi f x,
    rw filter.map_le_iff_le_vmap at H_converges_to_x,
    have Hmaps := filter.map_eq_vmap_of_inverse (function.id_of_right_inverse right_inv) (function.id_of_left_inverse left_inv),
    rw ← Hmaps at H_converges_to_x,
    have H3 : filter.map f (nhds x) = nhds (f x),
          
      sorry,
    rw H3 at H_converges_to_x, exact H_converges_to_x,
  sorry,
  
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 05 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filters/near/133378115):
H3 must be true because `nhds` only depends on the topology and f and g are homeomorphisms.
One direction of the equality will be from continuous.tendsto. The other one should require the continuity of g

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 05 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filters/near/133378211):
Also, you have an uniform isomorphism (i.e. `f` with `g` as inverse). This implies that it is an topological `embedding`, a `dense_embedding` and `uniform_embedding`. If you look for them this should give you enough rules to prove your statement.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 05 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filters/near/133378251):
... plus either left_inv or right_inv, and filter.map_map

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 05 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filters/near/133378669):
@**Rohan Mitta** don't listen to them, you were almost done. Stating only only implication since the other one follows by symmetry:
```lean
theorem complete_iff_of_uniform_cts_bij {α : Type*} [metric_space α] {β : Type*} [metric_space β] (f : α → β)
    (g : β → α) (Hf : uniform_continuous f) (Hg : uniform_continuous g) (left_inv : function.left_inverse g f)
    (right_inv : function.right_inverse g f) : complete_space α → complete_space β :=
begin
  
  intro H1,
  cases H1, split,
  intros filt Hfilt,

  have H2 := H1 (cauchy_map Hg Hfilt),
  cases H2 with x H_converges_to_x,
  existsi f x,
  rw filter.map_le_iff_le_vmap at H_converges_to_x,
  have Hmaps := filter.map_eq_vmap_of_inverse (function.id_of_right_inverse right_inv) (function.id_of_left_inverse left_inv),
  rw ← Hmaps at H_converges_to_x,
  have := continuous.tendsto Hf.continuous x,
  exact le_trans H_converges_to_x this
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 05 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filters/near/133378866):
Thanks all of you (I'm sitting next to Rohan)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rohan Mitta (Sep 05 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filters/near/133378965):
Amazing, thanks everyone!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 05 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filters/near/133379170):
Small cleanup:
```lean
open function
theorem complete_iff_of_uniform_cts_bij {α : Type*} [metric_space α] {β : Type*} [metric_space β] (f : α → β)
    (g : β → α) (Hf : uniform_continuous f) (Hg : uniform_continuous g) (left_inv : function.left_inverse g f)
    (right_inv : function.right_inverse g f) : complete_space α → complete_space β :=
begin
  rintro ⟨H1⟩,
  split,
  intros filt Hfilt,

  cases H1 (cauchy_map Hg Hfilt) with x H_converges_to_x,
  existsi f x,
  rw [filter.map_le_iff_le_vmap,
      ←filter.map_eq_vmap_of_inverse (id_of_right_inverse right_inv) (id_of_left_inverse left_inv)] at H_converges_to_x,
  
  exact le_trans H_converges_to_x (continuous.tendsto Hf.continuous x)
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Sep 05 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filters/near/133379874):
Thanks Patrick to actually look at the proof (obviously, I didn't ...)


{% endraw %}
