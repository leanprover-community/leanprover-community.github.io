---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/96716inductionbug.html
---

## Stream: [general](index.html)
### Topic: [induction bug](96716inductionbug.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Nov 20 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/induction%20bug/near/148074216):
```lean
theorem wtf {α : Type u} (C : multiset α → Prop) (r) : C r :=
begin
  induction r using multiset.induction
  /-
2 goals
case h₁
α : Type u,
C : multiset α → Prop
⊢ C 0

case h₂
α : Type u,
C : multiset α → Prop,
r_a : list α,
r_s : multiset (list α),
r_a_1 : C r_s
⊢ C (r_a :: r_s)
  -/,
  sorry, sorry
end

/-
type mismatch at application
  @multiset.induction (list α)
term
  list α
has type
  Type u
but is expected to have type
  Type (u+1)
-/
```


{% endraw %}
