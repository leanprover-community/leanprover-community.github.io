---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/59310Perfectfield.html
---

## Stream: [maths](index.html)
### Topic: [Perfect field](59310Perfectfield.html)

---

#### [Kenny Lau (Oct 17 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfect%20field/near/135957480):
Currently this is my definition:
```lean
/-- A perfect field is a field of characteristic p that has p-th root. -/
class perfect_field (α : Type u) [field α] (p : ℕ) [char_p α p] : Type u :=
(pth_root : α → α)
(frobenius_pth_root : ∀ x, frobenius α p (pth_root x) = x)
```

#### [Kenny Lau (Oct 17 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfect%20field/near/135957484):
Do you guys have a better suggestion?

#### [Kenny Lau (Oct 17 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfect%20field/near/135957489):
My idea is that we can change the definition once we have enough theory about separable polynomials.

#### [Kenny Lau (Oct 17 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfect%20field/near/135957495):
And go with this definition for now.

#### [Mario Carneiro (Oct 17 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfect%20field/near/135990765):
use `discrete_field`

#### [Mario Carneiro (Oct 17 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Perfect%20field/near/135990773):
`field` is deprecated

