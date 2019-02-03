---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/83465setisacompletelattice.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [set is a complete lattice](https://leanprover-community.github.io/archive/113488general/83465setisacompletelattice.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Apr 13 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set%20is%20a%20complete%20lattice/near/125037337):
<p>mathlib proof:</p>
<div class="codehilite"><pre><span></span>instance lattice_set : complete_lattice (set α) :=
{ lattice.complete_lattice .
  le           := (⊆),
  le_refl      := subset.refl,
  le_trans     := assume a b c, subset.trans,
  le_antisymm  := assume a b, subset.antisymm,

  lt           := λ x y, x ⊆ y ∧ ¬ y ⊆ x,
  lt_iff_le_not_le := λ x y, iff.refl _,

  sup          := (∪),
  le_sup_left  := subset_union_left,
  le_sup_right := subset_union_right,
  sup_le       := assume a b c, union_subset,

  inf          := (∩),
  inf_le_left  := inter_subset_left,
  inf_le_right := inter_subset_right,
  le_inf       := assume a b c, subset_inter,

  top          := {a | true },
  le_top       := assume s a h, trivial,

  bot          := ∅,
  bot_le       := assume s a, false.elim,

  Sup          := λs, {a | ∃ t ∈ s, a ∈ t },
  le_Sup       := assume s t t_in a a_in, ⟨t, ⟨t_in, a_in⟩⟩,
  Sup_le       := assume s t h a ⟨t&#39;, ⟨t&#39;_in, a_in⟩⟩, h t&#39; t&#39;_in a_in,

  Inf          := λs, {a | ∀ t ∈ s, a ∈ t },
  le_Inf       := assume s t h a a_in t&#39; t&#39;_in, h t&#39; t&#39;_in a_in,
  Inf_le       := assume s t t_in a h, h _ t_in }
</pre></div>


<p>my proof:</p>
<div class="codehilite"><pre><span></span>instance lattice_set : complete_lattice (set α) :=
lattice.complete_lattice_fun
</pre></div>

#### [ Kenny Lau (Apr 13 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set%20is%20a%20complete%20lattice/near/125037338):
<p>I win</p>

#### [ Gabriel Ebner (Apr 13 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set%20is%20a%20complete%20lattice/near/125037562):
<p>I guess <code>Sup</code> and <code>Inf</code> are defined differently now?</p>

#### [ Kenny Lau (Apr 13 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set%20is%20a%20complete%20lattice/near/125037602):
<p>really?</p>

#### [ Gabriel Ebner (Apr 13 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set%20is%20a%20complete%20lattice/near/125037907):
<p>They should be equal.   However I don't think they are definitionally equal.  <code>Sup s a = (∃ b ∈ set.image (λ f, f a) s, b) = (∃ b, (∃ c, s c ∧ s c a = b) → b)</code> which is different</p>

#### [ Kenny Lau (Apr 13 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set%20is%20a%20complete%20lattice/near/125037929):
<p>well one could prove that they are equal</p>

#### [ Kenny Lau (Apr 13 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set%20is%20a%20complete%20lattice/near/125037930):
<p>simp lemma</p>

#### [ Gabriel Ebner (Apr 13 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set%20is%20a%20complete%20lattice/near/125037988):
<p>This still doesn't give you definitional reduction.  If you want to prove <code>a ∈ Sup s</code>, you'll now always need to <code>simp</code> first.  There are quite a few places where we accept some additional complexity in order to guarantee good definitional reduction, the <code>lt</code> in preorder is another place.  We can define <code>lt</code> in terms of <code>le</code>, but we want it to reduce differently for natural numbers.</p>

#### [ Kenny Lau (Apr 13 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set%20is%20a%20complete%20lattice/near/125037998):
<p>I see</p>

#### [ Kevin Buzzard (Apr 13 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set%20is%20a%20complete%20lattice/near/125038503):
<p>Yes, for nat, <code>a&lt;b</code> is _defined_ to be <code>succ a &lt;= b</code> and if you know this you can write some neat obfuscated code :-)</p>

#### [ Kenny Lau (Apr 13 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set%20is%20a%20complete%20lattice/near/125038512):
<p>such as?</p>

#### [ Kevin Buzzard (Apr 13 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set%20is%20a%20complete%20lattice/near/125038557):
<p>I believe I used this to do some golf question here a week or two ago. Either a question of Chris or of Nima.</p>

#### [ Chris Hughes (Apr 13 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set%20is%20a%20complete%20lattice/near/125038813):
<p>It just means that you never have to use the lemma <code>succ_le_of_lt</code></p>

#### [ Johannes Hölzl (Apr 13 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set%20is%20a%20complete%20lattice/near/125039063):
<p>you can <code>match</code> or use the equation compiler to do case analysis and inductionon <code>&lt;</code>, with the definition following the default setup this would be not possible.</p>


{% endraw %}
