---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/32946Watiswrongwiththisdefinition.html
---

## Stream: [new members](index.html)
### Topic: [Wat is wrong with this definition?](32946Watiswrongwiththisdefinition.html)

---


{% raw %}
#### [ Ken Roe (Jul 24 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Wat%20is%20wrong%20with%20this%20definition%3F/near/130214027):
```lean
inductive evv : ℕ -> Prop
| Base := (evv 0)
| Inductive := ∀ x, even x → even (x+2).
```
gives the following error:
```lean
invalid return type for 'evv.Base'
```

#### [ Simon Hudon (Jul 24 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Wat%20is%20wrong%20with%20this%20definition%3F/near/130214285):
Try:

```lean
inductive evv : ℕ -> Prop
| Base : (evv 0)
| Inductive : ∀ x, evv x → evv (x+2).
```


{% endraw %}
