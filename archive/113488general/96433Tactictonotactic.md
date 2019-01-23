---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/96433Tactictonotactic.html
---

## Stream: [general](index.html)
### Topic: [Tactic to no tactic](96433Tactictonotactic.html)

---


{% raw %}
#### [ Nima (Apr 21 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20to%20no%20tactic/near/125479107):
Is there an easy way to re-write the last function without using tactic?
```lean
section 
parameters (p : Prop) [decidable p]
def cnd₁ : Prop := sorry
def cnd₂ : Prop := sorry
def check : Prop := if p then cnd₁ else cnd₂
def f₁ (c:cnd₁) : nat := sorry
def f₂ (c:cnd₂) : nat := sorry
def f  (c:check): nat := -- if p then f₁ cnd₁ else f₂ cnd₂ 
begin
  by_cases p ; simp [check,h] at c,
  exact f₁ c,
  exact f₂ c,
end
end
```

#### [ Mario Carneiro (Apr 21 2018 at 05:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20to%20no%20tactic/near/125479500):
```
theorem check_of_p (h : p) : check ↔ cnd₁ := iff_of_eq (if_pos h)
theorem check_of_not_p (h : ¬ p) : check ↔ cnd₂ := iff_of_eq (if_neg h)

def f (c:check) : nat :=
if h : p then
  f₁ ((check_of_p h).1 c)
else
  f₂ ((check_of_not_p h).1 c)
```

#### [ Nima (Apr 21 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20to%20no%20tactic/near/125481942):
Thank you, `if_pos` and `if_neg` are what I was looking for.
```lean
def f' (c:check): nat :=
  if h:p then f₁ (eq.mp (if_pos h) c) 
  else        f₁ (eq.mp (if_neg h) c) 
```

#### [ Kenny Lau (Apr 21 2018 at 07:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20to%20no%20tactic/near/125482384):
Nima beats Mario

#### [ Mario Carneiro (Apr 21 2018 at 07:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20to%20no%20tactic/near/125482438):
I wrote it that way for a reason. You should not rely on definitional expansion in this way as it is brittle. The point of the lemma is to isolate the unfolding of `check` so that this isn't happening in an ambiguous context

#### [ Mario Carneiro (Apr 21 2018 at 07:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20to%20no%20tactic/near/125482447):
The usage of `iff` is by convention since these are propositions


{% endraw %}
