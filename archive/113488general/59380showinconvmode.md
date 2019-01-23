---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/59380showinconvmode.html
---

## Stream: [general](index.html)
### Topic: [show in conv mode](59380showinconvmode.html)

---

#### [Kevin Buzzard (Mar 10 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20in%20conv%20mode/near/123540735):
I have some goal of the form `X = Y` where `Y` is one of these annoying terms that I can't cut and paste from pretty printer output (in this case, I believe, because it has replaced a proof with `_`). I want to use `show` to rewrite `X` as `X'` but I can't write `show X'=Y` because my problems with Y. I could prove `X=X'` using rfl and then use a rewrite. But it would be cool to use conv mode, use `to_lhs` to restrict to `X` and then use some conv version of show to replace `X` with `X'`. Can this be done?

