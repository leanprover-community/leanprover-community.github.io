---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/21702tactictypeclassinstance.html
---

## [general](index.html)
### [tactic type class instance](21702tactictypeclassinstance.html)

#### [petercommand (Jan 09 2019 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708014):
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

#### [petercommand (Jan 09 2019 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708130):
I want the tactic to accept begin...end blocks or {...} blocks

#### [Sebastian Ullrich (Jan 09 2019 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708169):
You'll want your parameters to have type `itactic` (for "interactive tactic"). Try searching for itactic in core or mathlib for examples.

#### [Rob Lewis (Jan 09 2019 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708213):
`meta def tactic.interactive.opt_fst (a: tactic.interactive.itactic) (b: tactic.interactive.itactic) : tactic unit := (a >> b) <|> b`

#### [petercommand (Jan 09 2019 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708254):
Isn't ```tactic.interactive.itactic``` defined as ```tactic unit```?

#### [Sebastian Ullrich (Jan 09 2019 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708297):
Yes, but it's special-cased in the tactic block parser

#### [petercommand (Jan 09 2019 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708301):
Ah

#### [petercommand (Jan 09 2019 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708303):
Hmm..I am still getting the same error

#### [Gabriel Ebner (Jan 09 2019 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708334):
You need to call it inside `begin..end`: `begin opt_fst {} {} end`

#### [petercommand (Jan 09 2019 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708347):
do I have to prefix the name of the tactic with ```tactic.interactive.```?

#### [Gabriel Ebner (Jan 09 2019 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708385):
No.

#### [Sebastian Ullrich (Jan 09 2019 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708394):
(if you're in `tactic.interactive`, which your definition should be)

#### [petercommand (Jan 09 2019 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708400):
after changing the name of the tactic, it worked..

#### [Rob Lewis (Jan 09 2019 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708416):
The tactic should be named `tactic.interactive.whatever`. You don't need to write the `tactic.interactive` part when you use it.

#### [petercommand (Jan 09 2019 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708478):
```quote
The tactic should be named `tactic.interactive.whatever`. You don't need to write the `tactic.interactive` part when you use it.
```
Hmm..seems that this is also hardcoded

#### [petercommand (Jan 09 2019 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20type%20class%20instance/near/154708504):
Thanks!

