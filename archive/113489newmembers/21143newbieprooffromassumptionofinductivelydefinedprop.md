---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/21143newbieprooffromassumptionofinductivelydefinedprop.html
---

## Stream: [new members](index.html)
### Topic: [newbie: proof from assumption of inductively defined prop](21143newbieprooffromassumptionofinductivelydefinedprop.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 17 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/newbie%3A%20proof%20from%20assumption%20of%20inductively%20defined%20prop/near/135989819):
[moving to `new members` stream]. You could prove that `ev n` was decidable, and then use `dec_trivial` to decide it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Oct 17 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/newbie%3A%20proof%20from%20assumption%20of%20inductively%20defined%20prop/near/135991991):
Proving decidability is the right way to do it in general, but for this example:
```lean
example : ¬ ev 7 :=
begin
  intro h,
  repeat {cases h with _ h}
end
```

