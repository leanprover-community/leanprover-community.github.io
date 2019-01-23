---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/18794refertoRtoprovethingsinN.html
---

## Stream: [new members](index.html)
### Topic: [refer to R to prove things in N?](18794refertoRtoprovethingsinN.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Oct 12 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135640902):
I'm proving that there is no natural number such that 2n = 1. One way of doing this would be to point out that multiplication by a non-zero constant is injective, and that multiplication in R generalises multiplication in N, and since we already have 2*(1/2) = 1, this would imply n = 1/2, which is not a natural number.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135640913):
and yet you asked us about why you need universes to prove fermat's last theorem :P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135640918):
they are both valid questions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Oct 12 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135640970):
My question is: Can this be formalised in Lean? How would you state "multiplication in R generalises multiplication in N"?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Oct 12 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135640977):
Ok, wait, you can state that pretty easily, but how would you use that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135640979):
nat.cast_mul, I guess

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135640982):
but you see

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135640987):
how would you prove that 1/2 is not a natural number?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135640994):
There are other ways to prove that theorem, but sure you can do it that way

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Oct 12 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135641022):
@**Kenny Lau**  1/2 is not natural because 1/2 is between 0 and 1, but 1 is the successor of 0 and nothing can be between an element and its successor.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135641070):
so you also want nat.cast_lt :P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135641082):
can't `omega` solve this? @**Mario Carneiro**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135641173):
```lean
example : ∀ n, 2*n ≠ 1 :=
λ n, nat.cases_on n dec_trivial $ λ n H,
nat.no_confusion $ nat.succ_inj H
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135641413):
```lean
example : ¬∃ n, 2*n = 1 :=
by simp only [eq_comm]; exact dec_trivial
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135641434):
```lean
example : ∀ n, 2*n ≠ 1 :=
λ n H, absurd (Exists.intro n H.symm) dec_trivial
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135641688):
I think this is a faithful rendition of your proof:
```lean
example (n : ℕ) : 2 * n ≠ 1 :=
λ h, begin
  have : 2 * (n:ℝ) = 1, {simpa using congr_arg (coe : ℕ → ℝ) h},
  rw [mul_comm, ← div_eq_iff_mul_eq (two_ne_zero : (2:ℝ)≠0)] at this,
  have h0 : ((0:ℕ):ℝ) < (1 / 2 : ℝ), {simp, norm_num},
  have h1 : (1 / 2 : ℝ) < (1:ℕ), {simp, norm_num},
  rw [this, nat.cast_lt] at h0 h1,
  exact not_le_of_lt h1 h0
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135641697):
```
```lean
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135641719):
Also, who needs the reals, we only need Q

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135641721):
I know

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135641766):
but if I did that then I wouldn't be "referring to R to prove things in N"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135641773):
that's mostly a comment to him

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135641779):
If you use Q instead the two lemmas `h0` and `h1` can be proven by `dec_trivial`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135641879):
what's going on in your proof? I'm surprised that `dec_trivial` proves `¬∃ (n : ℕ), 1 = 2 * n`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135641892):
it's dvd in disguise :P

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135641963):
oh whoa, didn't realize `dvd` was reducible

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135641987):
me neither

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135641993):
this is the residue of a longer proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135642023):
to answer your question, yes `omega` can handle this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135642032):
I think `linarith` can too if you fiddle with the statement a bit

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Oct 12 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135642101):
```quote
I think this is a faithful rendition of your proof:
```lean
example (n : ℕ) : 2 * n ≠ 1 :=
λ h, begin
  have : 2 * (n:ℝ) = 1, {simpa using congr_arg (coe : ℕ → ℝ) h},
  rw [mul_comm, ← div_eq_iff_mul_eq (two_ne_zero : (2:ℝ)≠0)] at this,
  have h0 : ((0:ℕ):ℝ) < (1 / 2 : ℝ), {simp, norm_num},
  have h1 : (1 / 2 : ℝ) < (1:ℕ), {simp, norm_num},
  rw [this, nat.cast_lt] at h0 h1,
  exact not_le_of_lt h1 h0
end
```
```
I'm trying to unpack that, but Lean says it fails to synthesise type class instance (I fixed one bracket).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135642174):
where is the error, and where did you fix a bracket?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135642177):
you need `import data.real.basic tactic.norm_num` in the header

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Oct 12 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135642186):
Yeah, I've done that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Oct 12 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135642196):
Wait, I put the wrong bracket. It works now.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135642317):
kenny, here is a marginally less obfuscatory (and shorter!) version of your proof:
```lean
example (n : ℕ) : 2*n ≠ 1 :=
λ h, (dec_trivial : ¬ 2 ∣ 1) ⟨n, h.symm⟩
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135642546):
```lean
import data.real.basic

example (n : ℕ) : 2 * n ≠ 1 :=
λ h, begin
  have h1 : 0 < 2 * n ∧ 2 * n < 2,
  { rw h,
    exact dec_trivial },
  rw [← @nat.cast_lt ℝ, ← @nat.cast_lt ℝ, nat.cast_mul] at h1,
  rw [nat.cast_zero, nat.cast_bit0, nat.cast_one] at h1,
  have h2 : 0 < (2:ℝ),
  { exact two_pos },
  have h3 : (2:ℝ) ≠ 0,
  { exact ne_of_gt h2 },
  rw [← div_lt_div_right h2, mul_div_cancel_left _ h3, and_comm] at h1,
  rw [← div_lt_div_right h2, mul_div_cancel_left _ h3, and_comm] at h1,
  rw [div_self h3, zero_div, ← nat.cast_zero, ← nat.cast_one] at h1,
  rw [nat.cast_lt, nat.cast_lt] at h1,
  cases h1 with h4 h5, clear h h2 h3,
  revert n h5,
  exact dec_trivial
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135642548):
is this a more faithful rendition?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135642556):
(sorry, can't get `nat.cast_div` to work, guess it doesn't exist)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135642585):
lol, of course not

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135642637):
it's not true... I'm not even sure what the statement would be

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135642643):
cast it to a char_zero decidable_division_ring or something like that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Oct 12 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135642852):
```quote
```lean
import data.real.basic

example (n : ℕ) : 2 * n ≠ 1 :=
λ h, begin
  have h1 : 0 < 2 * n ∧ 2 * n < 2,
  { rw h,
    exact dec_trivial },
  rw [← @nat.cast_lt ℝ, ← @nat.cast_lt ℝ, nat.cast_mul] at h1,
  rw [nat.cast_zero, nat.cast_bit0, nat.cast_one] at h1,
  have h2 : 0 < (2:ℝ),
  { exact two_pos },
  have h3 : (2:ℝ) ≠ 0,
  { exact ne_of_gt h2 },
  rw [← div_lt_div_right h2, mul_div_cancel_left _ h3, and_comm] at h1,
  rw [← div_lt_div_right h2, mul_div_cancel_left _ h3, and_comm] at h1,
  rw [div_self h3, zero_div, ← nat.cast_zero, ← nat.cast_one] at h1,
  rw [nat.cast_lt, nat.cast_lt] at h1,
  cases h1 with h4 h5, clear h h2 h3,
  revert n h5,
  exact dec_trivial
end
```
```
Ok, I'm lost here -- what exactly does nat.cast do?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Oct 12 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135642875):
And what are the up-arrow signs lean gives in the feedback?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135642919):
it's the coercion function from `nat` to `real`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135642924):
the up arrows are `nat.cast`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135642934):
`n` is a natural number and "up-arrow n" is a real number

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Oct 12 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135642941):
Ah ok.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135642964):
and there are theorems saying `↑(n + m) = ↑n + ↑m` and so on, that's `nat.cast_add`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135642975):
this is how you turn a whole equation from talking about naturals to talking about reals or vice versa

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 12 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135643024):
Coercions are discussed [here](https://leanprover.github.io/theorem_proving_in_lean/type_classes.html#coercions-using-type-classes) in TPiL.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Oct 12 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135643026):
And nat.cast_lt means "n < m implies ↑n < ↑m"?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135643029):
it's an iff

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135643037):
so you can turn a nat inequality into a real inequality or vice versa

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Oct 12 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135643122):
I see. And perhaps a ridiculously elementary question, but what exactly are the @ signs?  Why does nat.cast_mul not have them while the others do?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 12 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135643241):
`@function` means that you have to provide the implicit arguments to `function`. Implicit arguments are those that lean tries to infer and are denoted by curly braces.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 12 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135643284):
See [this section](https://leanprover.github.io/theorem_proving_in_lean/dependent_type_theory.html#implicit-arguments) of TPiL.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Oct 12 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135643316):
Oh ok, that makes sense. So e.g. if I was simplifying a calculational proof and had to simplify `1*x` to `x`, then I could use `@one_mul x` if `one_mul` didn't work?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135643320):
you would need way more arguments than `x`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135643323):
it would be something like `@one_mul \R _ x`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Oct 12 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135643374):
What does the underscore do?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 12 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135643378):
Yeah, I forgot to say you have to provide type class arguments as well (stuff in square brackets).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 12 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135643382):
The underscore tells lean to try to infer that argument.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Oct 12 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135643403):
(deleted)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135643404):
you know, there was a time when I tried to type something and decided that part of a sentence can be inferred from the previous part of the sentence, and subconsciously typed an underscore

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Oct 12 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135643460):
Oh wait, do you mean the brackets in the definitions themselves?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135643530):
if you do `#check @one_mul` then you can see all of the arguments required

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135643599):
The reason `nat.cast_lt` got a `@` and none of the others did is because at the beginning it's not clear what we are casting *to*. `nat.cast` actually works for a whole bunch of target types not just `ℝ`. Once the up arrows are introduced they carry enough information to figure out what type we are talking about

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Oct 12 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135643748):
Ok, that makes sense. I also don't understand the bit0 stuff. Doesn't bit0 just double things? Why does it matter that the thing being casted is written as twice of something?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 01:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135643868):
`2` is just a notation. it really means `bit0 1`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 01:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135643870):
try `set_option pp.notations false`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Oct 12 2018 at 01:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135643955):
Yeah I get that, but if we were dealing with 1000 instead of 2, do we need to write a series of bit1's and bit0's there? What if we were dealing with a general natural number instead of 2?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135644009):
`simp` will deal with it for you, I just don't really like using `simp`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135644013):
change that to, I just really don't like using `simp`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Oct 12 2018 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135644108):
You mean just "simp at h1"? Ok, yeah, that works.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135644112):
If we are dealing with a general natural number it is easier because it is just `\u n`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135644164):
The problem with `\u 1000` vs `1000` is that the terms are completely different (the type of the expression is stored in all the subterms), and so we have to rewrite all the way through the term

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135644249):
```
set_option pp.all true
#check (1000:ℤ)
-- @bit0.{0} int int.has_add
--   (@bit0.{0} int int.has_add
--      (@bit0.{0} int int.has_add
--         (@bit1.{0} int int.has_one int.has_add
--            (@bit0.{0} int int.has_add
--               (@bit1.{0} int int.has_one int.has_add
--                  (@bit1.{0} int int.has_one int.has_add
--                     (@bit1.{0} int int.has_one int.has_add
--                        (@bit1.{0} int int.has_one int.has_add (@has_one.one.{0} int int.has_one))))))))) :
--   int
#check ((1000:ℕ):ℤ)
-- @coe.{1 1} nat int (@coe_to_lift.{1 1} nat int (@coe_base.{1 1} nat int int.has_coe))
--   (@bit0.{0} nat nat.has_add
--      (@bit0.{0} nat nat.has_add
--         (@bit0.{0} nat nat.has_add
--            (@bit1.{0} nat nat.has_one nat.has_add
--               (@bit0.{0} nat nat.has_add
--                  (@bit1.{0} nat nat.has_one nat.has_add
--                     (@bit1.{0} nat nat.has_one nat.has_add
--                        (@bit1.{0} nat nat.has_one nat.has_add
--                           (@bit1.{0} nat nat.has_one nat.has_add (@has_one.one.{0} nat nat.has_one)))))))))) :
--   int
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135644569):
The thing is, `simp` is somewhat expensive, although not as expensive as `norm_num`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135644581):
is `norm_num` actually more expensive?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135644592):
oops, I was thinking about `ring`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135644600):
I was typing one thing and thinking about another thing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135644649):
Anyway, I've been replacing `simp` with less expensive tactics from files in mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Oct 12 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135644868):
Ok, I managed to work through and understand the proofs (at least the two longer ones -- will be a while before I can understand Kenny's two-line proofs). Thanks a lot! (that was my missing little lemma in proving p even if p^2 even).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135644917):
the two line proofs are easy: your theorem is by definition the same as "2 does not divide 1" and this is decidable (there is an instance in mathlib for it)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Oct 12 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135644920):
Why does expense/efficiency matter? You only need to run it once anyway.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Oct 12 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135644924):
```quote
the two line proofs are easy: your theorem is by definition the same as "2 does not divide 1" and this is decidable (there is an instance in mathlib for it)
```
Oh, ok. I just couldn't see through the notation.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135644945):
It doesn't matter too much, but once you start building up a huge library of maths the costs add up, and everyone who downloads mathlib will need to compile it, and mathlib itself changes on a daily basis and needs to be recompiled

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135644985):
so it's not really a one time cost unless you view mathlib as fixed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 12 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135645000):
Most users can do so, but I can't since I'm a maintainer and neither can many contributors that jump between branches of mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 12 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135658125):
@**Abhimanyu Pallavi Sudhir** just to let you know that theorems like this (real 1/2 not the image of an integer), which are needed to do my problem sheets but which I would not expect a general undergraduate with 1 week's Lean experience to be able to do, are actually part of a small library I am writing which enables a generic UG to solve the problem sheet questions. See here https://github.com/ImperialCollegeLondon/M1F_example_sheets/tree/master/src/xenalib and in particular note the file called `real_half_not_an_integer.lean`. I am trying to do these messy parts for the students so they can just use them instead of running into walls.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Oct 12 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135658275):
@**Kevin Buzzard**  Oh ok -- I wasn't really doing this for a problem sheet, though.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 12 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135658544):
Kevin, why do you keep up arrows in statement? Is it meant to clarify the statement for human readers?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 12 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135685726):
@**Abhimanyu Pallavi Sudhir** -- ha! I assumed you were working on Q7! @**Patrick Massot** you mean things like `¬ ∃ n : ℤ, (1/2 : ℚ) = ↑n`? I guess so! I think the fact that Z is not a subset of Q is quite confusing for beginners. Maybe the arrow means "note: something a bit funny is going on here."

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 12 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135687841):
Yes, I meant that line. Lean wouldn't care if you wrote it without that up arrow

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 12 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135691331):
Right (although you'd see the arrow in the goal ;-) ).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Oct 12 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135694355):
You don't have to: `set_option pp.coercions false` :wink:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Oct 12 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135701610):
I managed to prove the statement in a "morally similar" way but without casting to R (or Q) -- it ends up being kinda long, see `theorem one_not_even` at https://github.com/abhimanyupallavisudhir/lean/blob/master/num_theo_theorems.lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135701630):
`de_morgan` is `not_exists`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135701678):
all your `by norm_num` is `rfl`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 12 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135702112):
We don't teach the first years complicated tactics like rfl

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 12 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135702117):
we stick to the simple ones like norm_num

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 12 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135702166):
they're a darn sight easier to learn

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Oct 12 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135703007):
`rfl` is not necessarily faster than `norm_num`. The main idea of `norm_num` is actually to do things faster than than `rfl` and I think it worked out pretty well.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 12 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135703077):
fair enough


{% endraw %}
