---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/99238finnfinm.html
---

## [general](index.html)
### [(fin n) ≃ (fin m)](99238finnfinm.html)

#### [Kevin Buzzard (Dec 08 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/(fin n) ≃ (fin m)/near/151189960):
I was looking at the full Lean proof that if `fin n` bijects with `fin m` then `n = m`. It seems to me to be very long. It follows from the theorem that two fintypes biject with each other if and only if they have the same cardinality, but the cardinality of a fintype is defined to be the cardinality of the underlying list, and one now has to prove that this is well-defined. One might argue that this can be done relatively straightforwardly using `list.perm`, but the permutation equivalence relation on list is not defined to be "there's a bijection", it's defined to be the statement that we can make one list from another using some sequence of moves which define the inductive `perm` type, so now this reduces us to the statement that any bijection between lists comes from a perm, and this seems to be a fair amount of effort -- and all this is just to define the cardinality of a fintype. One still has to prove the theorem after this. Are there much shorter proofs available or is this what an actual proof of this statement looks like? In ZFC is there a shorter proof that if $$\{1,2,3,\ldots,n\}$$ bijects with $$\{1,2,\ldots,m\}$$ then $$n=m$$? Can one for example use the pigeonhole principle, arguing that if $$n\not=m$$ then wlog $$n>m$$ and now any map from a set with $$n$$ elements to a set with $$m$$ elements cannot be an injection by the pigeonhole principle?  Is this in Lean? Is this just the same work expressed in another way?

#### [Chris Hughes (Dec 09 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/(fin n) ≃ (fin m)/near/151215999):
My attempt
```lean
import data.equiv.basic data.fin

@[simp] lemma fin.mk.inj_eq' {a b n : ℕ} (ha : a < n) (hb : b < n) :
  (⟨a, ha⟩ : fin n) = ⟨b, hb⟩ ↔ a = b :=
⟨fin.veq_of_eq, λ h, by subst h⟩

@[simp] lemma fin.coe_inj {n : ℕ} {a b : fin n} :
  (a : ℕ) = b ↔ a = b :=
function.injective.eq_iff (λ _ _ h, fin.eq_of_veq h)

@[simp] lemma fin.eta' {a n : ℕ} (h : a < n) :
  ((⟨a, h⟩ : fin n) : ℕ) = a := rfl

open nat

lemma pigeonhole : ∀ {n m : ℕ} (f : fin m → fin n)
  (hf : function.injective f), m ≤ n
| 0     m f hf := (le_of_not_gt (λ h, nat.not_lt_zero _ (f ⟨0, h⟩).2))
| (n+1) 0 f hf := nat.zero_le _
| (n+1) (m+1) f hf := nat.succ_le_succ 
  (pigeonhole 
    (λ x : fin m, 
      if hfx : (⟨n, lt_succ_self n⟩ : fin (n + 1)) = (f ⟨x.1, lt_succ_of_lt x.2⟩)
      then ⟨f (fin.last m), 
        lt_of_not_ge 
          (λ hfm, 
            have hfm : (f (fin.last m) : ℕ) = n,
              from le_antisymm (nat.le_of_lt_succ (f (fin.last m)).2) hfm,
            have hfx : (f ⟨x, lt_succ_of_lt x.2⟩ : ℕ) = n,
              from le_antisymm (nat.le_of_lt_succ (f ⟨x, lt_succ_of_lt x.2⟩).2) 
                (trans_rel_left (≤) (le_refl _) (fin.veq_of_eq hfx)),
            have (⟨x, lt_succ_of_lt x.2⟩ : fin (m + 1)) = fin.last m, 
              from hf (fin.eq_of_veq (hfx.trans hfm.symm)),
            have x.1 = m, from fin.veq_of_eq this,
            absurd x.2 (this.symm ▸ lt_irrefl _))⟩
      else ⟨f ⟨x, lt_succ_of_lt x.2⟩, lt_of_le_of_ne (le_of_lt_succ (f ⟨x, lt_succ_of_lt x.2⟩).2) 
        (fin.vne_of_ne (ne.symm hfx))⟩)
    (λ ⟨x, hx⟩ ⟨y, hy⟩,
      have _ := (@function.injective.eq_iff _ _ _ hf ⟨x, lt_succ_of_lt hx⟩
        ⟨y, lt_succ_of_lt hy⟩).symm,
      begin
        clear _fun_match _fun_match _x _x,
        simp, 
        split_ifs,
        { simp * at *; cc },
        { intro h,
          exact absurd hy (by simp [*, fin.last, hf.eq_iff] at *) },
        { intro h,
          exact absurd hx (by simp [*, fin.last, hf.eq_iff] at *) },
        { simp [hf.eq_iff] }
      end))

example {n m : ℕ} (e : fin n ≃ fin m) : n = m :=
le_antisymm 
  (pigeonhole e e.bijective.1) 
  (pigeonhole e.symm e.symm.bijective.1)
```

#### [Kevin Buzzard (Dec 09 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/(fin n) ≃ (fin m)/near/151220117):
Chris I suspect that your life would have been easier if you'd used results involving `fintype.card`. But I think you have proved my point. I am telling all the students "look, the composite of injective functions is injective" and the proof is something which is just a few lines long in Lean. I am also telling them "the reals have this cool completeness property" but here I am clear that this is actually a lot of work, it is just work that we are not going to do. 

But I am also telling them "look, the pigeonhole principle is obvious" and I don't see any way of proving it which doesn't involve some pretty messy induction. My course contains lies. I say to them "look, if X and Y are finite sets and X injects into Y then the size of X is at most the size of Y, this is obvious because consider the image of the map" and yet I do not even tell them what I mean by the size of a set and if I need this sort of result for X and Y of the form $$\{1,2,3,\ldots,n\}$$ before I can define "size" then these arguments are circular.

#### [Reid Barton (Dec 09 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/(fin n) ≃ (fin m)/near/151228257):
I think at some point you have to use this idea that if f is a bijection from {1,...,n}  to {1,...,m} then by permuting the input (or output) we can assume that f sends n to m and then the restriction of f to {1,...,n-1] is a bijection to {1,...,m-1}.

#### [Chris Hughes (Dec 09 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/(fin n) ≃ (fin m)/near/151228807):
That's the messy part.

#### [Mario Carneiro (Dec 09 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/(fin n) ≃ (fin m)/near/151229379):
You could leverage some theorems about `equiv.swap` here, I think?

