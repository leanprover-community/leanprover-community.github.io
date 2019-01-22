---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/25708triviallyfalse.html
---

## [general](index.html)
### [trivially false](25708triviallyfalse.html)

#### [Kevin Buzzard (Aug 04 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trivially false/near/130883663):
Am I supposed to resolve situations like
```
H : (1 / 2).denom = 1
⊢ false
```
with `revert H,exact dec_trivial` or is there some less clunky way where I apply something to H directly?

#### [Mario Carneiro (Aug 04 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trivially false/near/130883713):
I use `absurd H dec_trivial` for this kind of thing

#### [Kevin Buzzard (Aug 04 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trivially false/near/130883727):
Thanks

#### [Kenny Lau (Aug 04 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trivially false/near/130883827):
```lean
import data.rat

theorem test (H : (1 / 2 : ℚ).denom = 1) : false :=
nat.no_confusion (nat.succ_inj H)
```

#### [Kenny Lau (Aug 04 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trivially false/near/130883896):
@**Mario Carneiro** interestingly `cases` fails on `H` or on `nat.succ_inj H`, and so does `injections with H`

#### [Kevin Buzzard (Aug 04 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trivially false/near/130883927):
ha ha, I'll let you know the next time I'm in this situation Kenny and you can come up with some bespoke solution for me :-)

#### [Mario Carneiro (Aug 04 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trivially false/near/130883999):
I get timeouts on everything that does something equivalent to cases on H, even `match H with end` times out

#### [Mario Carneiro (Aug 04 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trivially false/near/130884058):
`match (show 2 = 1, from H) with end` works, and other equivalent things

#### [Mario Carneiro (Aug 04 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/trivially false/near/130884100):
it must be unfolding things in a weird order

