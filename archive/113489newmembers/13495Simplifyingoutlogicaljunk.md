---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/13495Simplifyingoutlogicaljunk.html
---

## Stream: [new members](index.html)
### Topic: [Simplifying out logical junk](13495Simplifyingoutlogicaljunk.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Ken Roe (Jul 28 2018 at 03:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Simplifying%20out%20logical%20junk/near/130445253):
How can the following theorem be proven:

```lean
theorem junk { p : Prop } { q : Prop } : (p ∨ (q → false))=p :=
begin
    sorry
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jul 28 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Simplifying%20out%20logical%20junk/near/130445495):
I don't think the theorem hold. If `p` is false and `q` is false too, the left hand side is true and the right hand side is false

