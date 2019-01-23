---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/51666Potentialvmbug.html
---

## Stream: [general](index.html)
### Topic: [Potential vm bug](51666Potentialvmbug.html)

---

#### [Keeley Hoek (Aug 11 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Potential%20vm%20bug/near/131950146):
The following code typechecks:
````
meta def oopsie : list string → tactic (option string)
| [] := none                          -- I'm being naughty on this line
| (a :: rest) := oopsie rest

#eval oopsie ["a"]
````
I don't understand why it should. If I inspect the output of the `#eval`, I see the output "failed". Have I found a bug in the VM?

#### [Edward Ayers (Aug 11 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Potential%20vm%20bug/near/131950892):
There is a coercion from `option ` to `tactic` in `tactic.lean`:
```lean
meta instance opt_to_tac : has_coe (option α) (tactic α) :=
⟨returnopt⟩
```

#### [Edward Ayers (Aug 11 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Potential%20vm%20bug/near/131950909):
So your tactic will throw if you give it an empty list

#### [Keeley Hoek (Aug 11 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Potential%20vm%20bug/near/131951022):
Ah, cheers!

#### [Edward Ayers (Aug 11 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Potential%20vm%20bug/near/131951093):
I only spotted this because I happen to be reading `tactic.lean` currently. Does anyone know if there is a way to discover what coercions are occurring in a given expression? Or a `#command` which will tell me coercions to a particular type?

#### [Edward Ayers (Aug 11 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Potential%20vm%20bug/near/131951679):
I can't figure out how to use
`set_option pp.coercions true`

#### [Simon Hudon (Aug 11 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Potential%20vm%20bug/near/131960579):
```quote
I only spotted this because I happen to be reading tactic.lean currently.
```

Good read! Don't spoil the ending though!

#### [Simon Hudon (Aug 11 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Potential%20vm%20bug/near/131960581):
```quote
Does anyone know if there is a way to discover what coercions are occurring in a given expression?
```
```lean
#print instances has_coe
```

