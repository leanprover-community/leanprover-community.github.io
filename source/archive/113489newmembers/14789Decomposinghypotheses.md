---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/14789Decomposinghypotheses.html
---

## [new members](index.html)
### [Decomposing hypotheses](14789Decomposinghypotheses.html)

#### [Ken Roe (Jul 25 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130287397):
```lean
theorem test_split { P : Prop } { Q : Prop } { R : Prop } { S : Prop } :
    (P ∧ (Q ∨ R)) → (Q → S) → (R → S) → (P ∧ S) :=
begin
    intros, sorry
end
```
Is there a nice way to decompose the hypotheses to prove the above theorem?  What should "sorry" be replaced with?

#### [Reid Barton (Jul 25 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130287654):
`tauto` gets the job done in this case

#### [Reid Barton (Jul 25 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130287735):
Manually, you could use `cases`, for example
```lean
    cases pqr with p qr,
    refine ⟨p, _⟩,
    cases qr with q r,
    { exact qs q },
    { exact rs r }
```

#### [Ken Roe (Jul 25 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130288011):
Where can I find tauto?  It is not in the standard libraries.

#### [Reid Barton (Jul 25 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130288034):
It's in mathlib

#### [Ken Roe (Jul 25 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130292466):
Now for a more complex example,
```lean
theorem test_split { P : ℕ → Prop } { Q : ℕ → Prop } { R : ℕ → Prop } { S : ℕ → Prop } :
    (∀ x, P x ∧ (Q x ∨ R x)) → (∀ x, Q x → S x) → (∀ x, R x → S x) → (∀ x, P x ∧ S x) :=
begin
    intros, sorry
end
```
After the intros, is there a nice way to decompose these hypotheses?

#### [Patrick Massot (Jul 25 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130292689):
I'm not sure what you are looking for, but here is a short proof using `tauto`:

#### [Patrick Massot (Jul 25 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130292693):
```lean
theorem test_split { P : ℕ → Prop } { Q : ℕ → Prop } { R : ℕ → Prop } { S : ℕ → Prop } :
    (∀ x, P x ∧ (Q x ∨ R x)) → (∀ x, Q x → S x) → (∀ x, R x → S x) → (∀ x, P x ∧ S x) :=
begin
    intros h h' h'' x,
    specialize h x,
    specialize h' x,
    specialize h'' x,
    tauto
end
```

#### [Patrick Massot (Jul 25 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130292772):
I'm not sure we currently have any tactic that can guess the `specialize` steps.

#### [Patrick Massot (Jul 25 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130292790):
If you really really want one, then the standard procedure is to hope Simon will pity you.

#### [Simon Hudon (Jul 25 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130293761):
Haha! I'm pretty merciful though

#### [Simon Hudon (Jul 25 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130293765):
Have you tried `solve_by_elim`?

#### [Patrick Massot (Jul 25 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130293837):
It doesn't work

#### [Patrick Massot (Jul 25 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130294047):
Btw Simon, how was your tauto lecture?

#### [Simon Hudon (Jul 25 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130294182):
You can shrink the proof down to:

```lean
theorem test_split { P : ℕ → Prop } { Q : ℕ → Prop } { R : ℕ → Prop } { S : ℕ → Prop } :
    (∀ x, P x ∧ (Q x ∨ R x)) → (∀ x, Q x → S x) → (∀ x, R x → S x) → (∀ x, P x ∧ S x) :=
begin
    intros h h' h'' x,
    specialize h x, 
    split; tauto,
end
```

#### [Simon Hudon (Jul 25 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130294259):
I'm giving it tonight and I decided to talk about `pi_instances` after all. 5 minutes is so incredibly short :D

#### [Patrick Massot (Jul 25 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130294306):
Did you prepare a heavily commented version of the source?

#### [Simon Hudon (Jul 25 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130294601):
What I decided to do is write an instance for `group` and show how automation shrinks it. And then I mention that `refine_struct` is written in Lean

#### [Mario Carneiro (Jul 26 2018 at 03:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130314506):
`rintro` is a really nice way of doing all that
```
theorem test_split {P Q R S : Prop} :
  P ∧ (Q ∨ R) → (Q → S) → (R → S) → P ∧ S :=
begin
  rintro ⟨hp, hq | hr⟩ qs rs,
  { exact ⟨hp, qs hq⟩ },
  { exact ⟨hp, rs hr⟩ }
end
```

