---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/07374refinecantgowith.html
---

## [general](index.html)
### ["refine" can't go with λ ⟨_, _⟩, _](07374refinecantgowith.html)

#### [Kenny Lau (Sep 15 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/"refine" can't go with λ ⟨_, _⟩, _/near/134001592):
```lean
example : ∀ i : @subtype ℕ (λ _, true), 0 = 0 :=
begin
  refine λ ⟨n, hn⟩, _,
end
```

#### [Kenny Lau (Sep 15 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/"refine" can't go with λ ⟨_, _⟩, _/near/134001614):
```
don't know how to synthesize placeholder
context:
_x : {_x // true},
_fun_match : {_x // true} → 0 = 0,
n : ℕ,
hn : true
⊢ 0 = 0
state:
⊢ {_x // true} → 0 = 0
```

#### [Mario Carneiro (Sep 15 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/"refine" can't go with λ ⟨_, _⟩, _/near/134001717):
no, it can't

#### [Mario Carneiro (Sep 15 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/"refine" can't go with λ ⟨_, _⟩, _/near/134001720):
obvious workarounds include using `rintro` instead

#### [Mario Carneiro (Sep 15 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/"refine" can't go with λ ⟨_, _⟩, _/near/134001759):
Neither will using `match` or anything else that triggers the equation compiler

