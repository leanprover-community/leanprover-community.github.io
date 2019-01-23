---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/28663addtheoremby.html
---

## Stream: [general](index.html)
### Topic: [add_theorem_by](28663addtheoremby.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jakob von Raumer (Mar 24 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/add_theorem_by/near/124151486):
Why does this fail?
```
meta  def  foo : tactic unit :=
do tactic.add_theorem_by `bar [] (expr.const `unit []) (do tactic.constructor, return ()),
tactic.add_theorem_by `baz [] (expr.const `unit []) (do
bar ← tactic.get_local `bar,
tactic.exact bar,
return ()),
return ()
 
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 24 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/add_theorem_by/near/124151531):
What error do you get?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jakob von Raumer (Mar 24 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/add_theorem_by/near/124151537):
"get_local tactic failed, unknown 'bar'"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 24 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/add_theorem_by/near/124151623):
Ah I see! You need `resolve_name`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 24 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/add_theorem_by/near/124151626):
`get_local` is only for local constants

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jakob von Raumer (Mar 24 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/add_theorem_by/near/124151804):
Is there a resource for more beautiful fresh local names than `mk_fresh_name`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 24 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/add_theorem_by/near/124151860):
yes, I think it is called `get_unused_name`

