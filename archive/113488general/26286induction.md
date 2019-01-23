---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/26286induction.html
---

## Stream: [general](index.html)
### Topic: [induction](26286induction.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 23 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction/near/130145340):
Occasionally I find myself having the goal `\forall n, P n` that I want to prove by induction. But (as a mathematician) I always allow myself to use `P m` for all `m < n` in the induction step. So I would like to rewrite my initial goal into `\forall n m, m < n \to P m`. Is a statement like that already in mathlib?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 23 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction/near/130145429):
```quote
Occasionally I find myself having the goal `\forall n, P n` that I want to prove by induction. But (as a mathematician) I always allow myself to use `P m` for all `m < n` in the induction step. So I would like to rewrite my initial goal into `\forall n m, m < n \to P m`. Is a statement like that already in mathlib?
```
strong induction?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jul 23 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction/near/130145449):
I don't know anything about strong induction. Is that the name for the thing I am talking about?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jul 23 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction/near/130145519):
it's called strong induction.
```lean
#check @nat.strong_induction_on
-- nat.strong_induction_on :
--  ∀ {p : ℕ → Prop} (n : ℕ), (∀ (n : ℕ), (∀ (m : ℕ), m < n → p m) → p n) → p n
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jul 23 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction/near/130157350):
Read the section in TPIL on the equation compiler and the docs in mathlib on the equation compiler.

