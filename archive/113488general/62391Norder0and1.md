---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/62391Norder0and1.html
---

## Stream: [general](index.html)
### Topic: [N, order, 0 and 1](62391Norder0and1.html)

---


{% raw %}
#### [ Ned Summers (Aug 18 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/N%2C%20order%2C%200%20and%201/near/132369398):
Hey, I'm trying to prove the seemingly very simple
```
example (n : ℕ) (h : n < 1) : n = 0 := sorry
```
It's revealing a lot about what I don't know in lean (like getting stuck getting 1>n from n<1) and would welcome any advice/solutions. I'm not working very much at all with order or N at any other stage so, despite wading through theorems the past couple of days trying to find what I need, I'm giving up a bit. Thanks.

(Also, I'm using this to show that if you take any `(a : fin 1)` then `a = 0`. I suspect too that this is probably much simpler than what I'm doing.)

#### [ Mario Carneiro (Aug 18 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/N%2C%20order%2C%200%20and%201/near/132369562):
you should be able to do it by cases

#### [ Mario Carneiro (Aug 18 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/N%2C%20order%2C%200%20and%201/near/132369628):
not my favorite proof:
```
example (n : ℕ) (h : n < 1) : n = 0 :=
by cases h with _ h; [refl, cases h]
```

#### [ Mario Carneiro (Aug 18 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/N%2C%20order%2C%200%20and%201/near/132369681):
```
example (n : fin 1) : n = 0 :=
fin.cases rfl (λ i, i.elim0) n
```

#### [ Mario Carneiro (Aug 18 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/N%2C%20order%2C%200%20and%201/near/132370212):
```
example : ∀ (n : fin 1), n = 0 := dec_trivial
```

#### [ Patrick Massot (Aug 18 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/N%2C%20order%2C%200%20and%201/near/132371079):
```quote
It's revealing a lot about what I don't know in lean (like getting stuck getting 1>n from n<1) and would welcome any advice/solutions. 
```
This is literaly the same thing.
```lean
example (n : ℕ) (h : 1 > n) : n < 1 := h

example (n : ℕ) (h : 1 > n) : n < 1 := 
begin
change 1 > n,
assumption
end
```

#### [ Patrick Massot (Aug 18 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/N%2C%20order%2C%200%20and%201/near/132371124):
Note that the `change` is here so you see it in the interative message window, but it's useless

#### [ Kenny Lau (Aug 18 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/N%2C%20order%2C%200%20and%201/near/132376851):
```lean
import data.nat.basic

example : ∀ (n : ℕ), n < 1 → n = 0 :=
dec_trivial
```

#### [ Ned Summers (Aug 20 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/N%2C%20order%2C%200%20and%201/near/132445610):
Thanks everyone, dec_trivial is a nice thing to know about. Will be using this to ponder where my break in understanding was.


{% endraw %}
