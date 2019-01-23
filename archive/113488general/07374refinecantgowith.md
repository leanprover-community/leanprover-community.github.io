---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/07374refinecantgowith.html
---

## Stream: [general](index.html)
### Topic: ["refine" can't go with λ ⟨_, _⟩, _](07374refinecantgowith.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 15 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22refine%22%20can%27t%20go%20with%20%CE%BB%20%E2%9F%A8_%2C%20_%E2%9F%A9%2C%20_/near/134001592):
```lean
example : ∀ i : @subtype ℕ (λ _, true), 0 = 0 :=
begin
  refine λ ⟨n, hn⟩, _,
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 15 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22refine%22%20can%27t%20go%20with%20%CE%BB%20%E2%9F%A8_%2C%20_%E2%9F%A9%2C%20_/near/134001614):
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

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 15 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22refine%22%20can%27t%20go%20with%20%CE%BB%20%E2%9F%A8_%2C%20_%E2%9F%A9%2C%20_/near/134001717):
no, it can't

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 15 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22refine%22%20can%27t%20go%20with%20%CE%BB%20%E2%9F%A8_%2C%20_%E2%9F%A9%2C%20_/near/134001720):
obvious workarounds include using `rintro` instead

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 15 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22refine%22%20can%27t%20go%20with%20%CE%BB%20%E2%9F%A8_%2C%20_%E2%9F%A9%2C%20_/near/134001759):
Neither will using `match` or anything else that triggers the equation compiler


{% endraw %}
