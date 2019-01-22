---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/92357finsetofsubtypefromfilter.html
---

## [new members](index.html)
### [finset of subtype from filter](92357finsetofsubtypefromfilter.html)

#### [Bryan Gin-ge Chen (Sep 25 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/finset of subtype from filter/near/134577961):
I don't have a good feeling for how to manipulate subtypes. How do I do this?
```lean
variables {α : Type*} [decidable_eq α] [fintype α]

def foo (m X : finset α) : finset (finset {x : α // x ∈ X}) :=
m.filter (λ I, I ⊆ X) -- wrong type: finset (finset α) 
```
I messed around with `map` and `subtype.mk` to no avail.

#### [Mario Carneiro (Sep 25 2018 at 08:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/finset of subtype from filter/near/134578112):
I would suggest using `filter_map`, but I guess there is no `filter_map` on multiset

#### [Mario Carneiro (Sep 25 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/finset of subtype from filter/near/134578175):
I get the sense you are asking the wrong question. Why do you need this?

#### [Bryan Gin-ge Chen (Sep 25 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/finset of subtype from filter/near/134578319):
I'm trying to redefine a restriction function on matroids; [my original implementation](https://github.com/bryangingechen/lean-matroids/blob/master/src/matroid.lean#L787) used a bunch of subset hypotheses and I got the impression from what you said earlier that working with fintypes might be easier. So far everything else has indeed gotten simpler.

#### [Mario Carneiro (Sep 25 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/finset of subtype from filter/near/134578412):
I think instead of a subset relation, you want an injective function in that definition (or possibly its partial inverse function)

#### [Mario Carneiro (Sep 25 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/finset of subtype from filter/near/134578502):
also, this definition doesn't typecheck, not even loosely:
```
def foo (m X : finset α) : finset (finset {x : α // x ∈ X}) :=
m.filter (λ I, I ⊆ X) -- wrong type: finset (finset α)
```
`m` here is a `finset α` so if you filter over it you get elements of `α`, which can't be subsets of `X`

#### [Bryan Gin-ge Chen (Sep 25 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/finset of subtype from filter/near/134578566):
Oh damn, I meant to have `m: finset (finset α)`. Sorry about that.

#### [Mario Carneiro (Sep 25 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/finset of subtype from filter/near/134578668):
This works, but it won't be so easy to work with
```lean
def finset.filter_map {α β} [decidable_eq β]
  (f : α → option β) (s : finset α) : finset β :=
(s.1.filter_map f).to_finset

def foo (m : finset (finset α)) (X : finset α) : finset (finset {x : α // x ∈ X}) :=
m.filter_map $ λ I, if h:_ then some
  ⟨I.1.pmap (λ x h', ⟨x, h'⟩) h,
   multiset.nodup_pmap (λ _ _ _ _, subtype.mk_eq_mk.1) I.2⟩ else none
```

#### [Bryan Gin-ge Chen (Sep 25 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/finset of subtype from filter/near/134578983):
I'm not sure what you had in mind for using an injective function instead but the theorems and definitions are naturally phrased in terms of subsets. The whole theory is basically about relations between collections of subsets of some "ground set".

Thanks for the code! I'll see how far I can get with this.

#### [Mario Carneiro (Sep 25 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/finset of subtype from filter/near/134578997):
I guess the point of using `fintype` is to get away from the "ground set"

#### [Mario Carneiro (Sep 25 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/finset of subtype from filter/near/134579008):
because type theory supplies you with a "ground set" already, that is, the whole type

#### [Bryan Gin-ge Chen (Sep 25 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/finset of subtype from filter/near/134579063):
Right. It looks like it could be awkward whenever we want to change the ground set though.

#### [Mario Carneiro (Sep 25 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/finset of subtype from filter/near/134579068):
That's what the injective function is for

#### [Mario Carneiro (Sep 25 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/finset of subtype from filter/near/134579080):
In type theory you want to think about subsets as monos in the category theory sense

#### [Bryan Gin-ge Chen (Sep 26 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/finset of subtype from filter/near/134704613):
I tried working more with finsets of subtypes and found myself needing a whole bunch of stuff like the following:
```lean
import data.fintype

open finset
variables {α : Type*} [decidable_eq α] [fintype α]

def finset_embed {X : finset α} (S : finset {x // x ∈ X}) : finset α :=
S.map $ function.embedding.subtype _

lemma finset_embed_inj {X : finset α} : function.injective
  (λ (S : finset {x // x ∈ X}), finset_embed S):=
begin
  unfold function.injective,
  intros S T h,
  simp [ext] at h ⊢,
  intros a ha,
  simp [finset_embed, function.embedding.subtype] at h,
  exact iff.intro (λ H, exists.elim ((h a).mp (exists.intro ha H)) (λ ha_, id))
    (λ H, exists.elim ((h a).mpr (exists.intro ha H)) (λ ha_, id))
end

instance finset_embed_coe (X : finset α) : has_coe (finset {x : α // x ∈ X}) (finset α) :=
⟨finset_embed⟩

instance finset_finset_embed_coe (X : finset α) : has_coe (finset (finset {x : α // x ∈ X})) (finset (finset α)) :=
⟨λ (S : finset (finset {a // a ∈ X})), S.map $ ⟨finset_embed, finset_embed_inj⟩⟩

lemma finset_embed_mem {X : finset α} {S : finset {a : α // a ∈ X}} {x : {a : α // a ∈ X}} :
  x ∈ S ↔ x.val ∈ (↑S : finset α) :=
sorry

lemma finset_embed_subset {X : finset α} {x y : finset {a // a ∈ X}} :
  x ⊆ y ↔ ↑x ⊆ (↑y : finset α) :=
sorry

lemma finset_embed_univ {X : finset α} (x : finset {a // a ∈ X}) : ↑x ⊆ X :=
sorry

lemma finset_embed_card {X : finset α} (x : finset {a // a ∈ X}) : card x = card (↑x : finset α) :=
sorry

/-- def by Mario Carneiro -/
def finset.filter_map {α β} [decidable_eq β] (f : α → option β) (s : finset α) : finset β :=
(s.1.filter_map f).to_finset

/-- def by Mario Carneiro -/
def restriction (m : finset (finset α)) (X : finset α) : finset (finset {x : α // x ∈ X}) :=
m.filter_map $ λ I, if h : _ then some
  ⟨I.1.pmap (λ x h', ⟨x, h'⟩) h,
    multiset.nodup_pmap (λ _ _ _ _, subtype.mk_eq_mk.1) I.2⟩ else none

lemma mem_restriction {m : finset (finset α)} {X : finset α} {x : finset {y : α // y ∈ X}} :
x ∈ restriction m X ↔ ↑x ∈ m ∧ ↑x ⊆ X :=
sorry

lemma aux {X : finset α} {e : α} {x : finset {a // a ∈ X} } {h : e ∈ X} : insert e ↑x = (↑(insert (subtype.mk e h) x) : finset α) := sorry
```
I feel like I might be going about this all wrong. Recall that what I'm ultimately trying to do is reprove [this stuff](https://github.com/bryangingechen/lean-matroids/blob/master/src/matroid.lean#L782) using fintypes rather than carrying around a bunch of (`hX : X ⊆ E`) everywhere.

Is there a file in mathlib that takes this approach via monomorphisms to subobjects that I could study, or could someone give me a motivational explanation? In e.g. subgroup.lean it looks like there's a new class `is_subgroup` but I don't see how that fits.

#### [Bryan Gin-ge Chen (Sep 27 2018 at 06:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/finset of subtype from filter/near/134720517):
Update: I was able to prove almost all of the above. Just stuck on `mem_restriction`, which I realized should just be:
```lean
lemma mem_restriction {m : finset (finset α)} {X : finset α} {x : finset {y : α // y ∈ X}} :
x ∈ restriction m X ↔ ↑x ∈ m :=
sorry
```

#### [Mario Carneiro (Sep 27 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/finset of subtype from filter/near/134720961):
I still think you should not be dealing with subtypes so much. I assume your definition looks like this now?
```
structure indep (α : Type*) [decidable_eq α] :=
(indep : finset (finset α))
-- (I1)
(empty_mem_indep : ∅ ∈ indep)
-- (I2)
(indep_of_subset_indep {x y} (hx : x ∈ indep) (hyx : y ⊆ x) : y ∈ indep)
-- (I3)
(indep_exch {x y} (hx : x ∈ indep) (hy : y ∈ indep) (hcard : card x < card y)
    : ∃ e ∈ y \ x, insert e x ∈ indep)
```

#### [Mario Carneiro (Sep 27 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/finset of subtype from filter/near/134721194):
Also, I notice that this notion of restriction just throws away sets that are not in the subset, rather than taking an intersection like in topology. Is this the same?

#### [Mario Carneiro (Sep 27 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/finset of subtype from filter/near/134721323):
Ah, yes it is because of the subset axiom. If `A ∈ I` is an independent set and `E` is the subset, then `A ∩ E ∈ I` as well by the subset axiom, so the set of independent sets that are subsets of `E` is also the set of intersections of `E` with independent sets in `I`

#### [Bryan Gin-ge Chen (Sep 27 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/finset of subtype from filter/near/134721703):
That's right. What do you suggest instead of subtypes?

#### [Mario Carneiro (Sep 27 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/finset of subtype from filter/near/134721936):
filter_map, like before. Here's what I've got so far:
```
@[simp] theorem finset.mem_filter_map {α β} [decidable_eq β] {f : α → option β} {s : finset α}
  {b : β} : b ∈ s.filter_map f ↔ ∃ a ∈ s, b ∈ f a :=
by simp [finset.filter_map]; refl

def {u v} indep.filter_map {α : Type u} {β : Type v} [decidable_eq α] [decidable_eq β] (f : α → option β)
  (m : indep α) : indep β :=
{ indep := m.indep.image (finset.filter_map f),
  empty_mem_indep := finset.mem_image.2 ⟨∅, m.empty_mem_indep, rfl⟩,
  indep_of_subset_indep := λ x y, begin
    rw [mem_image, mem_image],
    rintro ⟨x, hx, rfl⟩ xy,
    refine ⟨x.filter (λ a, ∃ b ∈ f a, b ∈ y),
      m.indep_of_subset_indep hx (filter_subset _), _⟩,
    ext b, simp; split,
    { rintro ⟨a, ⟨ha, b', hb', hy⟩, hb⟩,
      rcases option.some_inj.1 (hb.symm.trans hb'),
      exact hy },
    { intro hb,
      rcases finset.mem_filter_map.1 (xy hb) with ⟨a, ha, ab⟩,
      exact ⟨a, ⟨ha, b, ab, hb⟩, ab⟩ }
  end,
  indep_exch := λ x y, begin
    
  end }
```

#### [Mario Carneiro (Sep 27 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/finset of subtype from filter/near/134722144):
How important is it that this theory be constructive? Are you trying to construct an algorithm, or are you trying to avoid LEM, or does it not matter?

#### [Bryan Gin-ge Chen (Sep 27 2018 at 07:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/finset of subtype from filter/near/134722343):
Here's my version of that, using the lemmas I listed above:
```lean
def restriction (m : indep α) (X : finset α) : indep {x : α // x ∈ X} :=
⟨indep_of_restriction m X,
mem_restriction.mpr m.empty_mem_indep,
λ x y hx hyx, have hx' : ↑x ∈ m.indep := mem_restriction.mp hx,
  have hyx' : ↑y ⊆ (↑x : finset α) := finset_embed_subset.mp hyx,
  mem_restriction.mpr (m.indep_of_subset_indep hx' hyx'),
by { intros x y hx hy hcard,
  have hx' : _ := mem_restriction.mp hx, have hy' : _ := mem_restriction.mp hy,
  have hcard' : card (↑x : finset α) < card ↑y := calc
    card (↑x : finset α) = card x : (finset_embed_card x).symm
    ... < card y : hcard
    ... = card ↑y : finset_embed_card y,
  have H : _ := m.indep_exch hx' hy' hcard',
  exact exists.elim H (by { intros e he, simp at he,
    have He : e ∈ X := mem_of_subset (finset_embed_subset_univ y) he.1.1,
    let e' := subtype.mk e He,
    have heyx : e' ∈ y \ x := mem_sdiff.mpr ⟨finset_embed_mem.mpr he.1.1,
      λ H, he.1.2 $ finset_embed_mem.mp H⟩,
    have heinsert : ↑(insert e' x) ∈ m.indep := by {
      have : (↑(insert e' x) : finset α) = insert e ↑x :=
        by simp [ext, finset_embed_coe_def, finset_embed, function.embedding.subtype],
      exact this.symm ▸ he.2
    },
    have H : insert e' x ∈ indep_of_restriction m X :=
      mem_restriction.mpr heinsert,
    exact exists.intro e' ⟨heyx, H⟩
  })}⟩
```
I'd like to preserve computability if possible. I think it's really neat that I'm able to compute different descriptions of matroids with #eval right now. Constructive everything might be beyond my capabilities. I'm already using `finset.ssubset_iff` which uses `classical`.

#### [Mario Carneiro (Sep 27 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/finset of subtype from filter/near/134729214):
@**Bryan Gin-ge Chen** I managed to finish the proof of this theorem. https://gist.github.com/digama0/edc2a9fe4d468c3921c87650eea5b77a

It is a lot more complicated than your proof, but it also deals with the case when the filter map is not injective. You can also get subtypes and map out of the filter map construction.

#### [Mario Carneiro (Sep 27 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/finset of subtype from filter/near/134729325):
(the stuff about `finset.filter_map` should go into mathlib)

#### [Bryan Gin-ge Chen (Sep 27 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/finset of subtype from filter/near/134747360):
 @**Mario Carneiro** Wow, thanks for all the effort! So, the first thing that matroid restrictions will be used for is to define a notion of rank on subsets (as the cardinality of a maximal independent subset of the subset). Would the best way to apply the filter_map construction be to imitate what you did with `foo` and subtypes a few days ago in this thread?

Regarding mathlib, should I try to put together a PR, or would it be faster for you just to directly commit the `finset.filter_map` stuff yourself?

#### [Mario Carneiro (Sep 27 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/finset of subtype from filter/near/134750167):
Let me get this straight: given an `indep` structure `m`, the rank of a subset `S` is the largest cardinality of subsets of `S` in `m`?

#### [Mario Carneiro (Sep 27 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/finset of subtype from filter/near/134752685):
or is it the largest cardinality of an `indep` that is a restriction of `m` to `S`?

#### [Bryan Gin-ge Chen (Sep 27 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/finset of subtype from filter/near/134753717):
Given `m : indep α`, a set `B : finset α`is a _basis_ for `m` if it is contained in `m.indep` and is maximal with regard to inclusion. The definition of the rank of a subset (of the ground set) that I'm trying to formalize is the following. The rank of `S : finset α`(with respect to `m`) is defined to be the cardinality of any basis of the restriction of `m` to `S` (which should be of type `indep {x // x ∈ S}`); I've formalized bases in an earlier section and proven e.g. that the cardinality of any two bases is equal.

#### [Mario Carneiro (Sep 27 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/finset of subtype from filter/near/134754363):
My suggestion:
```
def indep.supported {α} [decidable_eq α] (m : indep α) (s : finset α) : Prop :=
∀ t ∈ m.indep, t ⊆ s

def indep.restriction {α} [decidable_eq α] (m : indep α) (s : finset α) : indep α :=
m.filter_map (option.guard (∈ s))

theorem indep.restriction_supported {α} [decidable_eq α]
  (m : indep α) (s : finset α) : (m.restriction s).supported s := sorry

def indep.rank {α} [decidable_eq α] (m : indep α) : ℕ := m.indep.sup card

def rank_of {α} [decidable_eq α] (m : indep α) (s : finset α) : ℕ :=
(m.restriction s).rank
```

#### [Mario Carneiro (Sep 27 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/finset of subtype from filter/near/134754503):
```
def indep.basis {α} [decidable_eq α] (m : indep α) : finset (finset α) :=
m.indep.filter (λ s, ∀ t ∈ m.indep, ¬ s ⊂ t)
```

#### [Mario Carneiro (Sep 27 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/finset of subtype from filter/near/134754571):
although maybe this last one should be a predicate instead of a finset

#### [Bryan Gin-ge Chen (Sep 27 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/finset of subtype from filter/near/134757675):
That's an interesting way to avoid using subtypes. I'm not convinced that we shouldn't change the underlying type of the restriction though. For instance, one prototypical way of getting a matroid is to take a matrix over a field and let the ground set consist of the set of rows and the independent sets be the linearly independent sets of rows. The restriction of such a matroid to a certain subset of its elements should be equal (or maybe "equivalent" is a safer word) to the matroid constructed from the matrix consisting of the corresponding subset of rows; similar remarks hold for most other constructions of matroids that are coming to mind. I think following your approach I would end up with extra elements in the underlying fintype / ground set of the restriction which would violate this principle.

I think [the function `bases_bases_of_indep`](https://github.com/bryangingechen/lean-matroids/blob/fintype/src/matroid.lean#L572) is the equivalent of `indep.basis`. (The name was supposed to suggest getting `bases.bases` from `indep`).  Though I see it's more efficient to filter on `m.indep` than on `powerset univ`.

#### [Mario Carneiro (Sep 27 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/finset of subtype from filter/near/134774700):
I'm not saying you should never use subtypes, but they shouldn't be your bread and butter because it entails additional complications that can be avoided by just using the flexibility that you already have inside the type.

As for `bases`, I see that you have a separate axiomatization of bases rather than just using the collection of independent sets that also satisfy `is_basis`. Another advantage of not using `powerset univ` is that I have yet to invoke the assumption that `A` is finite; all of the above results have only needed `decidable_eq A`. I imagine you can add that assumption when you need it, but so far it hasn't come up.

#### [Bryan Gin-ge Chen (Sep 27 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/finset of subtype from filter/near/134775211):
OK, point well-taken. I haven't had a chance to work more on this yet, but doubtless I'll have more questions when I try to push on with my way of doing things. Thanks once again for being so helpful!

>I see that you have a separate axiomatization of bases

Yes, part of the fun of matroids is the existence of so many distinct but equivalent axiomatizations, a phenomenon often referred to as [cryptomorphism](https://en.wikipedia.org/wiki/Cryptomorphism). I've been idly wondering whether something based on the "TFAE" PR might be able to treat this sort of thing, but in practice it's probably not hard just to compose the relevant maps by hand.

