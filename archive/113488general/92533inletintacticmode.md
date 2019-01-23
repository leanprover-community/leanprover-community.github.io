---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/92533inletintacticmode.html
---

## Stream: [general](index.html)
### Topic: [$ in let in tactic mode](92533inletintacticmode.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 12 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20in%20let%20in%20tactic%20mode/near/126468511):
```lean
definition n : ℕ :=
begin
  let d := nat.succ $ nat.zero, -- fails
  exact d,
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 12 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20in%20let%20in%20tactic%20mode/near/126468513):
Replacing the $ with brackets (or in this case not even brackets) fixes it. It seems to me that the $ wants to eat the comma and things after it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 12 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20in%20let%20in%20tactic%20mode/near/126468514):
Is that expected behaviour?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (May 12 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20in%20let%20in%20tactic%20mode/near/126469412):
It's not that `$` eats too much input, but that it has a lower precedence than is used to parse the argument to `let`. `$` has the same precedence as `;`, and `let a := b; c` is supposed to be parsed as `(let a := b); c`. Perhaps it should have a higher precedence than `;`, but it's never quite clear what would be the best order in all contexts

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (May 12 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20in%20let%20in%20tactic%20mode/near/126469413):
I.e. `let d := (nat.succ $ nat.zero)` should work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (May 14 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%24%20in%20let%20in%20tactic%20mode/near/126524735):
See also [Use of $ in tactics](https://groups.google.com/d/msg/lean-user/B5tG4xj4xHc/6z8Ipx1pBQAJ).

