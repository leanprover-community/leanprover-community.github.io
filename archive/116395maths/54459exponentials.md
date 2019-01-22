---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/54459exponentials.html
---

## [maths](index.html)
### [exponentials](54459exponentials.html)

#### [Kenny Lau (Apr 27 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/exponentials/near/125775813):
@**Chris Hughes** what happened to your PR's about exp?

#### [Chris Hughes (Apr 27 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/exponentials/near/125779790):
I made this PR https://github.com/leanprover/mathlib/pull/61 in Feb, which is a necessary part of exp, and it hasn't been closed or accepted essentially because I didn't use filters, I used `cau_seq` as defined in `data.real.cau_seq`. I might have to rewrite it using filters over the summer.

#### [Kenny Lau (Apr 27 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/exponentials/near/125779805):
I'm also trying to learn how filters define limit :D

#### [Kenny Lau (Apr 27 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/exponentials/near/125779817):
```lean
theorem const (x : X) (y : Y) : tendsto (λ _ : X, y) (nhds x) (nhds y) :=
λ B HB FX HF1, HF1 _ ⟨set.univ, rfl⟩ $ univ_mem_sets' $
λ x, show y ∈ B, from mem_of_nhds HB
```
This was an exercise I set to myself (I know it's in mathlib already)

