---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/11881overlappingcasesandwellfoundedness.html
---

## [new members](index.html)
### [overlapping cases and well-foundedness](11881overlappingcasesandwellfoundedness.html)

#### [Mark Dickinson (Oct 21 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/overlapping%20cases%20and%20well-foundedness/near/136220983):
I'm trying to define a simple `ℕ → ℕ → ℕ` function using well-founded recursion. At top-level, I'm splitting on cases, and those cases overlap:

#### [Mark Dickinson (Oct 21 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/overlapping%20cases%20and%20well-foundedness/near/136221041):
```lean
def isqrt_inner : ℕ → ℕ → ℕ
| 0 _ := 0
| 1 _ := 1
| b n :=
    let k := shiftr b 1 in
    let a := have b - k < b, from sorry,
                    isqrt_inner (b - k) (shiftr n (2*k)) in
    shiftl a (k - 1) + (shiftr n (k + 1)) / a
```

Question: how would I go about replacing the `sorry` here? I need to be able to use the hypotheses that `b` is neither `0` nor `1`, but I'm not sure how to get at those.

#### [Kenny Lau (Oct 21 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/overlapping%20cases%20and%20well-foundedness/near/136221179):
```lean
def isqrt_inner : ℕ → ℕ → ℕ
| 0 _ := 0
| 1 _ := 1
| b@(p+2) n :=
    let k := shiftr b 1 in
    let a := have b - k < b, from _,
                    isqrt_inner (b - k) (shiftr n (2*k)) in
    shiftl a (k - 1) + (shiftr n (k + 1)) / a
```

#### [Mark Dickinson (Oct 21 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/overlapping%20cases%20and%20well-foundedness/near/136221244):
Beautiful! Thank you.

