---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/24947Unexpectederrors.html
---

## Stream: [general](index.html)
### Topic: [Unexpected errors](24947Unexpectederrors.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (May 27 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20errors/near/127171623):
Just finished proving this theorem about roots of polynomials, but I'm getting the following errors and I don't understand why
```
unexpected occurrence of recursive function
univariate_poly.lean:574:18: warning
definition 'roots_aux' was incorrectly marked as noncomputable
```
It clearly should be marked as noncomputable, and I have no idea what `unexpected occurence of recursive function means

```lean
noncomputable def roots_aux : Π {p : polynomial α} (hp : p ≠ 0), 
  {s : finset α // s.card ≤ degree p ∧ ∀ x, root p x ↔ x ∈ s}
| p :=
λ hp, @dite (∃ x, root p x) (classical.prop_decidable _) 
  {s : finset α // s.card ≤ degree p ∧ ∀ x, root p x ↔ x ∈ s}
  (λ h, let ⟨x, hx⟩ := classical.indefinite_description _ h in
  have hpd : 0 < degree p := nat.pos_of_ne_zero 
    (λ h, begin 
      rw [eq_C_of_degree_eq_zero h, root, eval_C] at hx, 
      have h1 : p (degree p) ≠ 0 := leading_coeff_ne_zero hp,
      rw h at h1,
      contradiction,
    end),
  have hd0 : div_by_monic p (monic_X_sub_C x) ≠ 0 :=
    λ h, by have := mul_div_eq_iff_root.2 hx;
      simp * at *,
  have wf : degree (div_by_monic p _) < degree p := 
    degree_div_by_monic_lt _ (monic_X_sub_C x) 
    ((degree_X_sub_C x).symm ▸ nat.succ_pos _) hpd,
  let ⟨t, htd, htr⟩ := @roots_aux (div_by_monic p (monic_X_sub_C x)) hd0 in
  ⟨insert x t, calc (insert x t).card ≤ t.card + 1 : finset.card_insert_le _ _
    ... ≤ degree (div_by_monic p (monic_X_sub_C x)) + 1 : nat.succ_le_succ htd
    ... ≤ _ : nat.succ_le_of_lt wf,
  begin
    assume y,
    rw [mem_insert, ← htr, eq_comm, ← root_X_sub_C],
    conv {to_lhs, rw ← mul_div_eq_iff_root.2 hx},
    exact ⟨root_or_root_of_root_mul, λ h, or.cases_on h (root_mul_right_of_root _) (root_mul_left_of_root _)⟩  
  end⟩)
  (λ h, ⟨∅, nat.zero_le _, by finish⟩)
using_well_founded {rel_tac := λ _ _, `[exact ⟨_, measure_wf degree⟩]}
```
The full file is here https://github.com/dorhinj/leanstuff/blob/master/univariate_poly.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 27 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20errors/near/127171663):
it happens with equation compilers

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 27 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20errors/near/127171666):
since they provide you with the theorem you're trying to prove, in case you want to do recursion

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 27 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20errors/near/127171669):
but some tactics touch every local hypothesis

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 27 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20errors/near/127171714):
Suspects I spot: `contradiction`, `simp * at *`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 27 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20errors/near/127171715):
the latter has a higher chance of being the perpetrator

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (May 27 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20errors/near/127171716):
I don't think it's that or it would have asked me to prove something. I replaced both of those with `admit` and I still get the error.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 27 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20errors/near/127171808):
how did you define `polynomial`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 27 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20errors/near/127171809):
can you prove strong induction?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (May 27 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20errors/near/127172447):
polynomial is `ℕ →₀ α`. I have proved and defined stuff in this manner before. I have just rewritten this function using `well_founded.fix`, and it works, but it would be nice to know what's going on.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 27 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20errors/near/127172498):
https://i.imgflip.com/2b3qrs.jpg

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20errors/near/127172737):
noooo lean memes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 27 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20errors/near/127172770):
I wouldn't feel bad about directly using `well_founded.fix`... the using_well_founded tactic is undocumented and hard to debug unless you know what's going on behind the scenes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20errors/near/127172776):
I don't think this should be a problematic definition, but I can't run it as is

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 27 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20errors/near/127172824):
(but maybe I'm just bad at Lean)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20errors/near/127172828):
(it's not actually a tactic, it's a keyword)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (May 27 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20errors/near/127172883):
(shows how much I've used it... I needed wf recursion a few months ago and struggled with `well_founded.fix`, and since it worked, never bothered to figure out `using_well_founded`)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20errors/near/127172932):
the offending tactic is `by finish` at the end

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 27 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20errors/near/127172933):
I must be blind

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20errors/near/127172938):
use `by clear roots_aux; finish` instead

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 27 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20errors/near/127172981):
I found it by just replacing things by `sorry` until the error went away

