---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/14789Decomposinghypotheses.html
---

## Stream: [new members](index.html)
### Topic: [Decomposing hypotheses](14789Decomposinghypotheses.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ken Roe (Jul 25 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130287397):
```lean
theorem test_split { P : Prop } { Q : Prop } { R : Prop } { S : Prop } :
    (P ∧ (Q ∨ R)) → (Q → S) → (R → S) → (P ∧ S) :=
begin
    intros, sorry
end
```
Is there a nice way to decompose the hypotheses to prove the above theorem?  What should "sorry" be replaced with?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jul 25 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130287654):
`tauto` gets the job done in this case

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jul 25 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130287735):
Manually, you could use `cases`, for example
```lean
    cases pqr with p qr,
    refine ⟨p, _⟩,
    cases qr with q r,
    { exact qs q },
    { exact rs r }
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ken Roe (Jul 25 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130288011):
Where can I find tauto?  It is not in the standard libraries.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jul 25 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130288034):
It's in mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ken Roe (Jul 25 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130292466):
Now for a more complex example,
```lean
theorem test_split { P : ℕ → Prop } { Q : ℕ → Prop } { R : ℕ → Prop } { S : ℕ → Prop } :
    (∀ x, P x ∧ (Q x ∨ R x)) → (∀ x, Q x → S x) → (∀ x, R x → S x) → (∀ x, P x ∧ S x) :=
begin
    intros, sorry
end
```
After the intros, is there a nice way to decompose these hypotheses?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 25 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130292689):
I'm not sure what you are looking for, but here is a short proof using `tauto`:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 25 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130292693):
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

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 25 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130292772):
I'm not sure we currently have any tactic that can guess the `specialize` steps.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 25 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130292790):
If you really really want one, then the standard procedure is to hope Simon will pity you.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 25 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130293761):
Haha! I'm pretty merciful though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 25 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130293765):
Have you tried `solve_by_elim`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 25 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130293837):
It doesn't work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 25 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130294047):
Btw Simon, how was your tauto lecture?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 25 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130294182):
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

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 25 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130294259):
I'm giving it tonight and I decided to talk about `pi_instances` after all. 5 minutes is so incredibly short :D

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jul 25 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130294306):
Did you prepare a heavily commented version of the source?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 25 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130294601):
What I decided to do is write an instance for `group` and show how automation shrinks it. And then I mention that `refine_struct` is written in Lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jul 26 2018 at 03:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130314506):
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

