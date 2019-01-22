---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/49404Unexpectedequationcompilerbehaviour.html
---

## [general](index.html)
### [Unexpected equation compiler behaviour](49404Unexpectedequationcompilerbehaviour.html)

#### [Chris Hughes (Jul 12 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20equation%20compiler%20behaviour/near/129536505):
Is this a bug?
```lean
inductive xnat
| zero : xnat
| succ : xnat → xnat

open xnat

def one := succ zero

def is_even : xnat → bool
| zero := tt
| one := ff -- works, but shouldn't

def is_even : xnat → bool
| zero := tt
| (succ zero) := ff -- error, as expected
```

#### [Mario Carneiro (Jul 12 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20equation%20compiler%20behaviour/near/129536612):
`one` is a variable in the first definition

#### [Reid Barton (Jul 12 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20equation%20compiler%20behaviour/near/129536615):
`one` doesn't have the `pattern` attribute, so... ^

#### [Patrick Massot (Jul 12 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20equation%20compiler%20behaviour/near/129542371):
That's a nice one! Note that:
```lean
inductive xnat
| zero : xnat
| succ : xnat → xnat

open xnat

def one := succ zero

def is_even : xnat → bool
| zero := tt
| one := ff -- works, as it should

example : is_even one := rfl -- fails, as it should
```

#### [Kenny Lau (Jul 12 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20equation%20compiler%20behaviour/near/129542467):
```quote
`one` is a variable in the first definition
```
how does `succ zero` define a variable?

#### [Patrick Massot (Jul 12 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20equation%20compiler%20behaviour/near/129542478):
it doesn't

#### [Kenny Lau (Jul 12 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20equation%20compiler%20behaviour/near/129542486):
then why does it work?

#### [Chris Hughes (Jul 12 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20equation%20compiler%20behaviour/near/129542491):
`one` doesn't refer to the def it's the same as writing `n`

#### [Patrick Massot (Jul 12 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20equation%20compiler%20behaviour/near/129542497):
Try replacing `one` by `three` in the def of `is_even`

#### [Patrick Massot (Jul 12 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20equation%20compiler%20behaviour/near/129542531):
Lean is guaranteed to be correct, not to be non-confusing

#### [Kenny Lau (Jul 12 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20equation%20compiler%20behaviour/near/129542540):
oh!

