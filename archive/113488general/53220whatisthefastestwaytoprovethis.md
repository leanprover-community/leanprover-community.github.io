---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/53220whatisthefastestwaytoprovethis.html
---

## Stream: [general](index.html)
### Topic: [what is the fastest way to prove this](53220whatisthefastestwaytoprovethis.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 25 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125675713):
```lean
p q t : ℕ+,
xp xq : ℤ,
m n : ℕ,
hm : ↑t = ↑p * m,
hn : ↑t = ↑q * n,
hpqt : xp * ↑m = xq * ↑n
⊢ xp * ↑q = xq * ↑p
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 25 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125680907):
Best I could do. It's not easy to keep it short.
```lean
example {p q t : ℕ+} {xp xq : ℤ} {m n : ℕ} (hm : (t : ℕ) = ↑p * m) (hn : (t : ℕ) = ↑q * n) 
    (hpqt : xp * m = xq * n) : xp * q = xq * p :=
have hm0 : (m : ℤ) ≠ 0 := int.coe_nat_ne_zero.2 (λ h, lt_irrefl (0 : ℕ) (trans_rel_left 
    (<) t.2 (by rwa [h, mul_zero] at hm))),
have hm' : (t : ℤ) = p * m := show ((t : ℕ) : ℤ) = p * m, from hm.symm ▸ by simp,
have hn' : (t : ℤ) = q * n := show ((t : ℕ) : ℤ) = q * n, from hn.symm ▸ by simp,
(domain.mul_right_inj hm0).1 
  (by rw [mul_assoc xq, ← hm', hn', mul_left_comm, ← hpqt, mul_left_comm, mul_assoc])
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 25 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125680964):
thanks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 25 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125680967):
What's the fastest way to prove this?
```lean
even_sum_four_squares {n a b c d : ℤ}
    (H : a * a + b * b + c * c + d * d = 2 * n) :
    ∃ w x y z, w * w + x * x + y * y + z * z = 2 * n ∧ 
    w * w + x * x ≡ 0 [ZMOD 2] ∧ y * y + z * z ≡ 0 [ZMOD 2]
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 25 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125680971):
aha

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 25 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125680977):
That was horrible

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 25 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125680996):
I just did a bazillion cases on whether things were odd or even.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 25 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125684665):
A mathematician would say that clearly two of a,b,c have the same parity

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 25 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125684677):
so let w and x be those two

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 25 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125684692):
I would like to prove it in Lean with some kind of WLOG

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 25 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125684696):
"wlog a and b have the same parity"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 25 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125684699):
because I can switch c with either a or b if necessary

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 25 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125684705):
So here the symmetry is three-fold.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 25 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125684749):
The question is invariant under any permutation of the set {a,b,c}

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 25 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125684753):
and I know two of those elements must be congruent mod 2

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 25 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125684754):
so WLOG they're a and b

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 25 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125684855):
Very difficult to say nicely in lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 25 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125684879):
This was my proof
```lean
have h' : a * a + b * b + c * c + d * d ≡ 0 [ZMOD 2] :=
  modeq_zero_iff.2 (H.symm ▸ dvd_mul_right _ _),
or.cases_on (int.mod_two_eq_zero_or_one (a * a))
  (λ ha, or.cases_on (int.mod_two_eq_zero_or_one (b * b))
    (λ hb, ⟨a, b, c, d, H, even_add_even ha hb, 
      modeq_add_cancel_left (show a * a + b * b ≡ 0 [ZMOD 2], from even_add_even ha hb) 
      (int.modeq.trans (by simp) h')⟩)
    (λ hb, or.cases_on (int.mod_two_eq_zero_or_one (c * c))
      (λ hc, ⟨a, c, b, d, by simp [H.symm], even_add_even ha hc,
        modeq_add_cancel_left (show a * a + c * c ≡ 0 [ZMOD 2], from even_add_even ha hc) 
          (int.modeq.trans (by simp) h')⟩)
      (λ hc, ⟨a, d, b, c, by simp [H.symm], 
        modeq_add_cancel_left (show b * b + c * c ≡ 0 [ZMOD 2], from odd_add_odd hb hc)
          (int.modeq.trans (by simp) h'),      
        odd_add_odd hb hc⟩))) 
  (λ ha, or.cases_on (int.mod_two_eq_zero_or_one (b * b))
    (λ hb, or.cases_on (int.mod_two_eq_zero_or_one (c * c))
      (λ hc, ⟨b, c, a, d, by simp [H.symm], even_add_even hb hc, 
        modeq_add_cancel_left (show b * b + c * c ≡ 0 [ZMOD 2], from even_add_even hb hc) 
          (int.modeq.trans (by simp) h')⟩)
      (λ hc, ⟨a, c, b, d, by simp [H.symm], odd_add_odd ha hc, 
        modeq_add_cancel_left (show a * a + c * c ≡ 0 [ZMOD 2], from odd_add_odd ha hc) 
          (int.modeq.trans (by simp) h')⟩))
    (λ hb, ⟨a, b, c, d, by simp [H.symm], odd_add_odd ha hb,
      modeq_add_cancel_left (show a * a + b * b ≡ 0 [ZMOD 2], from odd_add_odd ha hb) 
          (int.modeq.trans (by simp) h')⟩))
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 25 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125684938):
It looks a bit like a sonnet

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 25 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125685035):
My WLOG observation was that, just as we have a 2-variable WLOG which says that if the question is invariant under switching the two variables and we know that some predicate must be satisfied by some arrangement of the variables (e.g. x <= y), then we may assume that the predicate is satisfied by the default arrangement,

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 25 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125685084):
there is a 3-variable generalisation which says that if the question is invariant under all permutations of three variables and you can find some predicate which is true for some arrangement (e.g. "two of these three variables get sent to the same element under a map to a type with two elements") then WLOG it's true for the default arrangement

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 25 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125685158):
I am very interested in making Lean do things which mathematicians find trivial, painlessly, so I quite like thinking about things such as this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 25 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125685188):
I regard issues such as the one you brought up as a barrier to getting mathematicians to adopt automated proof checking as part of their routine

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 25 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125685241):
If you find yourself needing this kind of WLOG again I'd be interested to hear.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 25 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125685282):
I'd happily spend some time over the summer trying to learn how to write tactics such as this. In this case it feel like it's a generalisation of Simon's WLOG

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 25 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125685390):
If you had it then the proof would be Wlog3 a %2 = b % 2, by tactic.ring (showing that permuting the variables doesn't change the assumption)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 25 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125685395):
and then let w be a, x be b etc

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 25 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125685490):
So now we need @**Simon Hudon** to write an n-variable WLOG tactic... (-;

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 25 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125685677):
I think that the 2-variable WLOG is a powerful tool which genuinely does come up in practice

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 25 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125685686):
I am less convinced that the 3-variable WLOG shows up so much

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 25 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125685689):
however it sounds like a good exercise for the beginner

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 25 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125685692):
or possibly an incredibly difficult one

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 25 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125685739):
I think the n-variable one should definitely be left to Hudon ;-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 25 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125685774):
Interesting! In my previous prover, I had n-variable permutations in wlog but after talking to Assia, I started thinking that it was not the most useful generalization

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 25 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125685793):
n-pairs of swaps seemed more interesting

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 25 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125685855):
If you come up with another example where 3+ variable permutation is useful, I'll implement it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 25 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125686172):
I agree that one should find out what users actually need in practice before leaping into multi-variable WLOG. I can't believe I just said that phrase.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 25 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125686237):
The reason I suggested 3-variable WLOG is that at some point I suspect that it will do my Lean understanding some good if I were to actually write a tactic, and Chris and I will be spending the summer working on Lean together (with 13 other people)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 25 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125686426):
Are you becoming a ... pragmatist?  *gasp*

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 25 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125686446):
no, I just want to learn

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 25 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/what%20is%20the%20fastest%20way%20to%20prove%20this/near/125686447):
But seriously, it is certainly a fun exercise. Let me know if you have questions

