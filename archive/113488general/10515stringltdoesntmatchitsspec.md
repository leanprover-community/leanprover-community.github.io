---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/10515stringltdoesntmatchitsspec.html
---

## [general](index.html)
### [string_lt doesn't match its spec](10515stringltdoesntmatchitsspec.html)

#### [Mario Carneiro (Jun 21 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/string_lt doesn't match its spec/near/128386824):
@**Gabriel Ebner** @**Sebastian Ullrich** I started trying to prove that `string.lt` is a total order, and then I discovered it's not true:
```
#eval to_bool ([1, 2] < [2, 1]) -- tt
#eval to_bool ([2, 1] < [1, 2]) -- tt
```
Surely this is a bug?

#### [Mario Carneiro (Jun 21 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/string_lt doesn't match its spec/near/128386901):
Even worse, it behaves differently (correctly) on actual strings:
```
#eval to_bool ("ab" < "ba") -- tt
#eval to_bool ("ba" < "ab") -- ff
#reduce to_bool ("ba" < "ab") -- tt
example : "ba" < "ab" := dec_trivial
```

#### [Sebastian Ullrich (Jun 21 2018 at 02:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/string_lt doesn't match its spec/near/128392824):
[oops](https://github.com/leanprover/lean/blob/a4aae537fe771ee92d746d4a2be1e73c543e48b9/library/init/data/list/basic.lean#L278)

#### [Mario Carneiro (Jun 21 2018 at 03:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/string_lt doesn't match its spec/near/128393318):
I'm using this in mathlib:
```
inductive lex (r : α → α → Prop) : list α → list α → Prop
| nil {} {a l} : lex [] (a :: l)
| cons {a l₁ l₂} (h : lex l₁ l₂) : lex (a :: l₁) (a :: l₂)
| rel {a₁ l₁ a₂ l₂} (h : r a₁ a₂) : lex (a₁ :: l₁) (a₂ :: l₂)
```
Feel free to poach

#### [Sebastian Ullrich (Jun 21 2018 at 03:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/string_lt doesn't match its spec/near/128393382):
Right, an inductive definition is certainly nicer here

#### [Mario Carneiro (Jun 21 2018 at 03:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/string_lt doesn't match its spec/near/128393430):
here's the decidability proof, although it needs rejiggering for core:
```
instance decidable_rel [decidable_eq α] (r : α → α → Prop)
  [decidable_rel r] : decidable_rel (lex r)
| l₁ [] := is_false $ λ h, by cases h
| [] (b::l₂) := is_true lex.nil
| (a::l₁) (b::l₂) := begin
  haveI := decidable_rel l₁ l₂,
  refine decidable_of_iff (r a b ∨ a = b ∧ lex r l₁ l₂) ⟨λ h, _, λ h, _⟩,
  { rcases h with h | ⟨rfl, h⟩,
    { exact lex.rel h },
    { exact lex.cons h } },
  { rcases h with _|⟨_,_,_,h⟩|⟨_,_,_,_,h⟩,
    { exact or.inr ⟨rfl, h⟩ },
    { exact or.inl h } }
end
```

