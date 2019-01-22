---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/74056hasoneforwithbotnat.html
---

## [maths](index.html)
### [`has_one` for `with_bot nat`](74056hasoneforwithbotnat.html)

#### [Chris Hughes (Jul 06 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/`has_one` for `with_bot nat`/near/129214870):
Is this a bad idea, since I'll be introducing 2 coercions from`nat` to `with_bot nat`
```lean
instance with_bot.has_one : has_one (with_bot ℕ) := ⟨(1 : ℕ)⟩
```

