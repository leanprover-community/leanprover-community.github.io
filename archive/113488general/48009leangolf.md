---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/48009leangolf.html
---

## Stream: [general](index.html)
### Topic: [lean golf](48009leangolf.html)

---


{% raw %}
#### [ Sean Leather (Feb 28 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/123089630):
Shortest proof of this?

```lean
a ∧ b ∧ c ∧ d ∧ e ↔ a ∧ b ∧ c ∧ c ∧ d ∧ e
```

#### [ Sebastian Ullrich (Feb 28 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/123089805):
Let's start with the basics
```lean
by split;intro;simp*
```

#### [ Sean Leather (Feb 28 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/123090043):
That's like a sledgehammer using sledgehammers to hit small nails. For some reason, I never think to try `simp *`.

#### [ Sebastian Ullrich (Feb 28 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/123090128):
Well, I don't really need `*` here, but naming the hypothesis obviously is a golf no-go :P

#### [ Sean Leather (Feb 28 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/123090420):
Is it? If the proof is short, I don't see why. :simple_smile:

#### [ Scott Morrison (Feb 28 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/123090434):
I was happy to see `by tidy` works too. Maybe one day I'll get up the courage to PR it.

#### [ Kevin Buzzard (Feb 28 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/123109866):
I wondered whether `by cc` would work -- but it doesn't. I still don't really know what to expect with cc but I think I've seen it prove other goals of this nature.

#### [ Sean Leather (Mar 01 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/123129844):
I'm slowly learning how to use `simp *`:
```lean
namespace list
variables {α : Type} {l : list α} {n : ℕ}

theorem nth_of_map {f : α → α} {a : α} (p : f a = a) :
  option.get_or_else (nth (map f l) n) a = f (option.get_or_else (nth l n) a) :=
by induction l generalizing n; [skip, cases n]; simp [*, option.get_or_else]

end list
```

#### [ Johannes Hölzl (Mar 02 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/123179941):
I guess `cc` doesn't work as it currently doesn't handle idempotent laws (i.e. `c ∧ c`).

#### [ Kevin Buzzard (Mar 13 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/123658195):
Curry:

#### [ Kevin Buzzard (Mar 13 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/123658197):
`example (P Q R : Prop) : (P ∧ Q → R) ↔ (P → (Q → R)) := sorry`

#### [ Kevin Buzzard (Mar 13 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/123658245):
Doing this one taught me something, although it was arguably not very useful

#### [ Kevin Buzzard (Mar 13 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/123658252):
Actually it taught me 2 things, one being that bash shell is not very good at counting unicode characters

#### [ Sean Leather (May 24 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127015438):
I'm sure I've asked this before, but I don't remember the answer. Better/shorter way to do this?

```lean
intro h, simp at h, simp [h]
```

Note that `simp` by itself doesn't work.

#### [ Johannes Hölzl (May 24 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127016063):
`simp {contextual:=tt}` should do it.

#### [ Sean Leather (May 24 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127016150):
Yep, that did it. Thanks!

#### [ Sean Leather (May 24 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127017262):
`simp` doesn't solve this. Is there a theorem I can use with `simp` to solve it?

```lean
⟨a, b⟩ ∈ l ↔ a = a₁ ∧ b == b₁ ∨ ⟨a, b⟩ ∈ l
```

#### [ Johannes Hölzl (May 24 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127017535):
I guess you have `⟨a₁, b₁⟩ ∈ l`?

#### [ Johannes Hölzl (May 24 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127017583):
But I also don't see how to solve it with the simplifier.

#### [ Sean Leather (May 24 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127017645):
Oh wait, I'm stupid. Let me actually think. :simple_smile:

#### [ Kevin Buzzard (May 24 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127017653):
Do you CS people know how to parse that sort of statement?

#### [ Kevin Buzzard (May 24 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127017685):
I look at it (away from Lean) and have no idea about the relative priorities of and, or and iff. Is this just all some standard convention that you CS people know and we maths people just avoid by adding brackets?

#### [ Kevin Buzzard (May 24 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127017716):
I mean -- I know I can go and check them -- my question is whether there are uniform standards or whether Lean made some random choice and you find different choices in other systems.

#### [ Kevin Buzzard (May 24 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127017741):
obviously I can guess the answer in this situation from the context, but in the past I have written statements without brackets and then later on gone "oh crap, that doesn't mean what I wanted it to mean at all"

#### [ Gabriel Ebner (May 24 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127017785):
The precedence is pretty standard.  In most (all?) programming languages as well as logic, and binds more tightly than or.  C doesn't have iff, so its hard to compare.

#### [ Sean Leather (May 24 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127017792):
The “usual conventions:” https://groups.google.com/d/msg/lean-user/lbFwVL21Az4/1erXpLqBAwAJ

#### [ Gabriel Ebner (May 24 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127017838):
Excerpt from a proof theory textbook lying around here (Troelstra & Schwichtenberg):

> Notation (Saving on parentheses) In writing formulas we save on parentheses by assuming that ∀, ∃,  ¬ bind more strongly than ∧, ∨, and that in turn ∨, ∧ bind more strongly than →, ↔. [...]

#### [ Gabriel Ebner (May 24 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127017848):
I guess you will find similar boilerplate in most texts that deal with logical formulas.

#### [ Sean Leather (May 24 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127017854):
One that I struggled with was `=` vs. `↔`, but now I'm used to it.

#### [ Kevin Buzzard (May 24 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127018118):
```quote
I guess you will find similar boilerplate in most texts that deal with logical formulas.
```
I follow a text which deals with logical formulas in my introduction to proof class and I can find no mention of binding preferences anywhere!

#### [ Kevin Buzzard (May 24 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127018119):
But I do see a lot of brackets :-)

#### [ Kevin Buzzard (May 24 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127018159):
I conclude that the guy who wrote it (who is in the office a few doors down from me) was also a mathematician who had no idea of standard CS conventions :-)

#### [ Gabriel Ebner (May 24 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127018330):
There is one confusing difference between proof theory and CS though: the precedence of ∀, ∃ is different.
```
  ∃x P(x) → Q     means:

  (∃x P(x)) → Q       for everyone in my research group
  ∃x (P(x) → Q)       in Lean, Coq, etc.
```

#### [ Chris Hughes (May 24 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127018489):
`(∃x P(x)) → Q` seems like really stupid precedence, since you would usually write `∀ x , P x → Q` instead of that.

#### [ Sean Leather (May 24 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127018550):
Interesting. Pierce (Types and Programming Languages) uses explicit bracketing : `{∃x, P(x)}`

#### [ Gabriel Ebner (May 24 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127018815):
@**Chris Hughes** The same precedence is also used for ∀: `(∀x P(x)) → Q` vs. `∀x (P(x) → Q)`, which is just as confusing.

#### [ Kevin Buzzard (May 24 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/127019269):
In fact it was exactly this forall point which I was referring to in my earlier "that doesn't mean what I wanted it to mean" comment

#### [ Sean Leather (Aug 20 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132455368):
Shortest proof of this?

```lean
a : ℕ
b : ℕ
p : a < b + 1,
q : a ≠ b
⊢ a < b
```

#### [ Sean Leather (Aug 20 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132455921):
This is what I came up with:

```lean
nat.lt_of_le_and_ne (nat.le_of_lt_succ p) q
```

#### [ Kenny Lau (Aug 20 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132456748):
```lean
example (a b : ℕ) (p : a < b + 1) (q : a ≠ b) : a < b :=
by cases p; [cc, assumption]
```

#### [ Johan Commelin (Aug 20 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132457185):
I'm not on a Lean machine atm, but could `cooper` or `tidy` kill this one?

#### [ Kenny Lau (Aug 21 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132529548):
```lean
import data.fintype

universe u

variables (α : Type u) [decidable_eq α] (S T : finset α)

example (H1 : S ⊆ T) (H2 : T.card ≤ S.card) : S = T :=
have H3 : disjoint S (T \ S), by simp [disjoint],
have H4 : _, from finset.card_disjoint_union H3,
have H5 : S ∪ T \ S = T, from finset.ext' $ λ x,
  ⟨λ H, or.cases_on (finset.mem_union.1 H) (finset.mem_of_subset H1) (and.left ∘ finset.mem_sdiff.1),
  λ H, classical.by_cases (finset.mem_union_left _) (λ H', finset.mem_union_right _ $ finset.mem_sdiff.2 ⟨H, H'⟩)⟩,
have H6 : S.card = T.card, from le_antisymm (finset.card_le_of_subset H1) H2,
have H7 : T \ S = ∅, from finset.card_eq_zero.1 $
  nat.add_left_cancel $ eq.symm $ by rwa [H5, H6] at H4,
have H8 : T ⊆ S, from finset.subset_iff.2 $ λ x H,
  classical.by_contradiction $ λ H',
  finset.ne_empty_of_mem (finset.mem_sdiff.2 ⟨H, H'⟩) H7,
finset.subset.antisymm H1 H8
```

#### [ Kenny Lau (Aug 21 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132529552):
is there a shorter proof?

#### [ Mario Carneiro (Aug 21 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132531216):
```
example (H1 : S ⊆ T) (H2 : T.card ≤ S.card) : S = T :=
finset.eq_of_veq $ multiset.eq_of_le_of_card_le (finset.val_le_iff.2 H1) H2
```

#### [ Mario Carneiro (Aug 21 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132531244):
this should be in mathlib though

#### [ Kenny Lau (Aug 21 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132531591):
ah it's in multiset lol

#### [ Chris Hughes (Aug 21 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132531934):
Pretty sure it's there for finsets. I remember seeing it.

#### [ Chris Hughes (Aug 21 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132532050):
`finset.eq_of_subset_of_card_le`

#### [ Kenny Lau (Aug 21 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132532088):
genius

#### [ Kenny Lau (Aug 21 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132533414):
```lean
import data.fintype

universe u

variables (α : Type u) [decidable_eq α]

example [fintype α] (f : α → α) (H : function.injective f) : function.surjective f :=
have H : _ := finset.eq_univ_iff_forall.1 $ finset.eq_of_subset_of_card_le (finset.subset_univ _)
  (le_of_eq $ eq.symm $ finset.card_image_of_injective _ H),
λ y, let ⟨x, _, H2⟩ := finset.mem_image.1 (H y) in ⟨x, H2⟩
```

#### [ Kenny Lau (Aug 21 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132533415):
how about this?

#### [ Chris Hughes (Aug 21 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132533791):
Already in mathlib. `fintype.injective_iff_surjective` Your proof  is shorter though

#### [ Kenny Lau (Aug 21 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132534113):
```lean
import data.fintype

universe u

variables (α : Type u) [fintype α] [decidable_eq α]

theorem something (f : α → α) (H : function.injective f) : function.surjective f :=
have H : _ := finset.eq_univ_iff_forall.1 $ finset.eq_of_subset_of_card_le (finset.subset_univ _)
  (le_of_eq $ eq.symm $ finset.card_image_of_injective _ H),
λ y, let ⟨x, _, H2⟩ := finset.mem_image.1 (H y) in ⟨x, H2⟩

theorem something2 [integral_domain α] (x : α) (H : x ≠ 0) : ∃ r , r * x = 1 :=
something α (λ r, r * x)
  (λ r s (H' : r * x = s * x), eq_of_sub_eq_zero $ or.resolve_right
    (eq_zero_or_eq_zero_of_mul_eq_zero $ show (r - s) * x = 0, by rw [sub_mul, H', sub_self]) H) 1

noncomputable instance field_of_fintype_of_integral_domain [integral_domain α] : field α :=
{ inv := λ x, if H : x = 0 then 0 else classical.some $ something2 α x H,
  mul_inv_cancel := λ x H, by unfold has_inv.inv; rw [dif_neg H, mul_comm, classical.some_spec (something2 α x H)],
  inv_mul_cancel := λ x H, by unfold has_inv.inv; rw [dif_neg H, classical.some_spec (something2 α x H)],
  .. (by apply_instance : integral_domain α) }
```

#### [ Kenny Lau (Aug 21 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132534118):
```quote
Already in mathlib. `fintype.injective_iff_surjective` Your proof  is shorter though
```
well I didn't prove the other direction

#### [ Chris Hughes (Aug 21 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132534147):
Don't make that an instance or we have a cycle.

#### [ Kenny Lau (Aug 21 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132534161):
also I can't find `injective_iff_surjective`

#### [ Chris Hughes (Aug 21 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132534228):
It's quite new. Last month or so.

#### [ Kevin Buzzard (Aug 22 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132601084):
```lean
example (α : Type) (a b : α) : a = b = (b = a) := sorry
```

Too embarrassed to post my effort. @**Chris Hughes** this came up with that countp v count thing. The proof isn't refl even though the predicates are whatever they call it -- eta equivalent or something.

#### [ Patrick Massot (Aug 22 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132601170):
`by cc`

#### [ Mario Carneiro (Aug 22 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132601195):
`propext eq_comm`

#### [ Patrick Massot (Aug 22 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132601255):
Mine is shorter! :trophy:

#### [ Patrick Massot (Aug 22 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132601261):
I know, yours is probably faster

#### [ Mario Carneiro (Aug 22 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132601274):
Mine is smaller with `pp.all` :)

#### [ Kevin Buzzard (Aug 22 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132603490):
Here's the context this came up in:

```lean
import data.multiset

open multiset 

example (α : Type) [decidable_eq α] (s : multiset α) (a : α) : count a s = card (filter (λ b, b = a) s) :=
begin
  rw ←countp_eq_card_filter,
  unfold count,
  congr,
  funext,
  by cc,
end 
```

I was surprised this wasn't there, but perhaps the issue is that you can filter on `λ b, b = a` or `λ b, a = b`

#### [ Kenny Lau (Aug 22 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132603835):
```lean
import data.multiset

open multiset

example (α : Type) [decidable_eq α] (s : multiset α) (a : α) : count a s = card (filter (λ b, b = a) s) :=
begin
  convert countp_eq_card_filter s,
  funext b,
  cc
end
```

#### [ Mario Carneiro (Aug 22 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132603896):
`by simp [count, countp_eq_card_filter, eq_comm]; congr`

#### [ Kenny Lau (Aug 22 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132604013):
`by convert countp_eq_card_filter s; simp [eq_comm]`

#### [ Kevin Buzzard (Aug 23 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132604473):
If I hover over `convert` in VS Code I get "convert <- expr <error while executing interactive.param_desc: don't know how to pretty print lean.parser.small_nat>  Similar to `refine` but generates equality proof obligations for every discrepancy between the goal and the type of the rule"

#### [ Mario Carneiro (Aug 23 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/132604528):
that's because `small_nat` doesn't have a description - compare with `congr'`

#### [ Sean Leather (Sep 12 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/133795530):
```lean
example (m n : ℕ) : m < 1 + max m n := _
```

#### [ Reid Barton (Sep 12 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/133796099):
not very creative, but `by rw [add_comm, nat.lt_succ_iff]; apply le_max_left`

#### [ Kenny Lau (Oct 18 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/136055689):
```lean
import analysis.topology.topological_space

example (α : Type*) [topological_space α] [t1_space α] [fintype α] (s : set α) : is_open s :=
by letI := classical.dec_pred (λ x, x ∈ -s); exact
(is_closed_compl_iff.1 $ set.bUnion_of_singleton (-s) ▸ is_closed_Union
  ⟨set.fintype_of_finset (finset.univ.filter (λ x, x ∈ -s))
    (λ x, by simp only [finset.mem_filter, finset.mem_univ, true_and])⟩
  (λ _ _, is_closed_singleton))
```

#### [ Mario Carneiro (Oct 18 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/136059466):
I think this theorem could also be stated as `t = \top`

#### [ Mario Carneiro (Oct 18 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/136060001):
```lean
class t2_space' (α : Type u) [topological_space α] :=
(t2 : ∀x y, (∀ u v : set α, is_open u → is_open v →
   x ∈ u → y ∈ v → ∃ z, z ∈ u ∧ z ∈ v) → x = y)

variables (α : Type u) [t : topological_space α]
include t

def Hausdorffification.setoid : setoid α :=
{ r := λ x y, ∀ (s : setoid α) [t2_space' (quotient s)], @setoid.r α s x y,
  iseqv := ⟨λ _ s _, s.2.1 _, λ _ _ H s ht2, s.2.2.1 (@H s ht2),
    λ _ _ _ H1 H2 s ht2, s.2.2.2 (@H1 s ht2) (@H2 s ht2)⟩ }

local attribute [instance] Hausdorffification.setoid

@[reducible] def Hausdorffification : Type u :=
quotient (Hausdorffification.setoid α)

instance Hausdorffification.t2_space' :
  t2_space' (Hausdorffification α) :=
{ t2 := λ x y, quotient.induction_on₂ x y $ λ m n H,
    quot.sound $ λ r ht2, begin
      resetI,
      let f : Hausdorffification α → quotient r,
      { refine λ e, quotient.lift_on' e quotient.mk _,
        intros a b H, apply quotient.sound, apply H },
      have hf : continuous f,
      { intros s hs,
        change is_open (quotient.mk ⁻¹' _),
        rw ← set.preimage_comp,
        exact hs },
      refine quotient.exact (t2_space'.t2 _ _ $ λ u v h1 h2 h3 h4, _),
      rcases H _ _ (hf _ h1) (hf _ h2) h3 h4 with ⟨z, zu, zv⟩,
      exact ⟨fz, zu, zv⟩
    end }
```

#### [ Johannes Hölzl (Oct 18 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/136060806):
By the way: this T2 space definition is equal to `not (disjoint (nhds x) (nhds y)) -> x = y`.

#### [ Mario Carneiro (Oct 18 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/136061226):
not constructively

#### [ Mario Carneiro (Oct 18 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20golf/near/136061506):
(oops, wrong thread, this should be in [Hausdorffification](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/subject/Hausdorffification/near/136026443))


{% endraw %}
