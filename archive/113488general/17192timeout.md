---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/17192timeout.html
---

## Stream: [general](index.html)
### Topic: [timeout](17192timeout.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 08 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout/near/147329792):
```lean
theorem is_noetherian_ring_mv_polynomial_fin {n : ℕ}
  (hnr : is_noetherian_ring R) : is_noetherian_ring (mv_polynomial (fin n) R) :=
begin
try_for 4000 {
  induction n with n ih,
  { refine is_noetherian_ring_of_equiv R _ _ hnr,
    { exact (mv_polynomial.pempty_equiv.symm.trans $ mv_polynomial.equiv_of_equiv
      ⟨pempty.elim, fin.elim0, λ x, pempty.elim x, λ x, fin.elim0 x⟩) },
    { dsimp only [equiv.trans, equiv.symm, equiv.coe_fn_mk],
      exact @@is_ring_hom.comp _ _ _
        (mv_polynomial.C.is_ring_hom) _ _
        (@@mv_polynomial.eval₂.is_ring_hom _ _ _ _ _
          (mv_polynomial.C : R → mv_polynomial (fin 0) R) mv_polynomial.C.is_ring_hom
          (mv_polynomial.X ∘ pempty.elim : pempty → mv_polynomial (fin 0) R)) } },
}, try_for 100000 {
  refine is_noetherian_ring_of_equiv (polynomial (mv_polynomial (fin n) R)) _ _ (is_noetherian_ring_polynomial ih),
  { exact mv_polynomial.option_equiv.symm.trans (mv_polynomial.equiv_of_equiv
      ⟨λ x, option.rec_on x 0 fin.succ, λ x, fin.cases none some x,
      by rintro ⟨none | x⟩; [refl, exact fin.cases_succ _],
      λ x, fin.cases rfl (λ i, show (option.rec_on (fin.cases none some (fin.succ i) : option (fin n))
        0 fin.succ : fin n.succ) = _, by rw fin.cases_succ) x⟩) },
  { dsimp only [equiv.trans, equiv.symm, equiv.coe_fn_mk],
    exact is_ring_hom.comp _ _ }
}
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 08 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout/near/147329805):
Even 100 seconds is not enough

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 08 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout/near/147329817):
@**Mario Carneiro** I don't really know how to deal with this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 08 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout/near/147330186):
(it's from https://github.com/leanprover/mathlib/pull/461/commits/b3f1efbe02638a2793b48e9a28a1d8f0df371690#diff-1f7cb4d661f00b6d887925434b41ad5dR286)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 08 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout/near/147335661):
https://github.com/leanprover/mathlib/pull/461/commits/f80e9fce6b081cf26f551b3ae2e5c83327f9bd59#diff-1f7cb4d661f00b6d887925434b41ad5dR293

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 08 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout/near/147335662):
@**Mario Carneiro** more ridiculousness

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 09 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout/near/147358487):
@**Sebastian Ullrich** what do you think about this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Nov 09 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout/near/147358506):
not much

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 09 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout/near/147358544):
good idea

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 09 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout/near/147359835):
I think it's a serious problem if I provided every implicit argument and it still takes 16 seconds to elaborate

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 09 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout/near/147362908):
I basically changed the definitions of polynomial and mv_polynomial and that cut down 6 seconds

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 09 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout/near/147368074):
Kenny can you make a MWE? It's hard to run your code.


{% endraw %}
