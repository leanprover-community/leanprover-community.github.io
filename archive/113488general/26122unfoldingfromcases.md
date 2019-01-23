---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/26122unfoldingfromcases.html
---

## Stream: [general](index.html)
### Topic: [unfolding from cases](26122unfoldingfromcases.html)

---


{% raw %}
#### [ Reid Barton (Nov 28 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20from%20cases/near/148714917):
```lean
def x : ℕ := 1 + 1 + 1 + 1

inductive P : ℕ → Type
| p : P x

example {a} (h : P a) : a = 4 := begin
  cases h,
end
```
Goal is `⊢ nat.succ (nat.add (1 + 1 + 1) 0) = 4`. Is all this unfolding expected? I wanted `x = 4`.

#### [ Kenny Lau (Nov 28 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfolding%20from%20cases/near/148716159):
interestingly `induction h` produces the expected `x = 0`:
```lean
def x : ℕ := 0

inductive P : ℕ → Type
| p : P x

example {a} (h : P a) : a = 0 := begin
  induction h,
end
```


{% endraw %}
