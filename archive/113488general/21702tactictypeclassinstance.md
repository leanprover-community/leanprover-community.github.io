---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/21702tactictypeclassinstance.html
---

## Stream: [general](index.html)
### Topic: [tactic type class instance](21702tactictypeclassinstance.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) petercommand (Jan 09 2019 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708014):
```
meta def opt_fst (a: tactic unit) (b: tactic unit) : tactic unit := (a >> b) <|> b
```
I am trying to define a tactic combinator, but it seems that I cannot use it like this:
```
opt_fst { symmetry } { symmetry }
```
and I am getting errors like
```
failed to synthesize type class instance for
|- has_emptyc (tactic unit)
```
Am I doing something wrong here?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) petercommand (Jan 09 2019 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708130):
I want the tactic to accept begin...end blocks or {...} blocks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jan 09 2019 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708169):
You'll want your parameters to have type `itactic` (for "interactive tactic"). Try searching for itactic in core or mathlib for examples.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Jan 09 2019 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708213):
`meta def tactic.interactive.opt_fst (a: tactic.interactive.itactic) (b: tactic.interactive.itactic) : tactic unit := (a >> b) <|> b`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) petercommand (Jan 09 2019 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708254):
Isn't ```tactic.interactive.itactic``` defined as ```tactic unit```?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jan 09 2019 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708297):
Yes, but it's special-cased in the tactic block parser

#### [![Click to go to Zulip](../../assets/img/zulip2.png) petercommand (Jan 09 2019 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708301):
Ah

#### [![Click to go to Zulip](../../assets/img/zulip2.png) petercommand (Jan 09 2019 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708303):
Hmm..I am still getting the same error

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Jan 09 2019 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708334):
You need to call it inside `begin..end`: `begin opt_fst {} {} end`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) petercommand (Jan 09 2019 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708347):
do I have to prefix the name of the tactic with ```tactic.interactive.```?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Jan 09 2019 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708385):
No.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jan 09 2019 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708394):
(if you're in `tactic.interactive`, which your definition should be)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) petercommand (Jan 09 2019 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708400):
after changing the name of the tactic, it worked..

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Jan 09 2019 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708416):
The tactic should be named `tactic.interactive.whatever`. You don't need to write the `tactic.interactive` part when you use it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) petercommand (Jan 09 2019 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708478):
```quote
The tactic should be named `tactic.interactive.whatever`. You don't need to write the `tactic.interactive` part when you use it.
```
Hmm..seems that this is also hardcoded

#### [![Click to go to Zulip](../../assets/img/zulip2.png) petercommand (Jan 09 2019 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708504):
Thanks!

