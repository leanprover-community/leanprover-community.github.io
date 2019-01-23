---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/33174fixesagainstthelatestmathlib.html
---

## Stream: [general](index.html)
### Topic: [fixes against the latest mathlib](33174fixesagainstthelatestmathlib.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fixes%20against%20the%20latest%20mathlib/near/124799280):
now there is a global `^` called `pow`, and now the type of `n` will not be inferred from `f^n` (you need to manually state that `n` is of type `nat`). In that case, `pow` unfolds to `monoid.pow`, which can be unfolded as before the latest version.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 08 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fixes%20against%20the%20latest%20mathlib/near/124799512):
Are you talking about the nightly from the 6th?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fixes%20against%20the%20latest%20mathlib/near/124799513):
right

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 08 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fixes%20against%20the%20latest%20mathlib/near/124800387):
So no more nat.pow?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fixes%20against%20the%20latest%20mathlib/near/124800392):
I have not tested, but I believe Lean figures out whether you mean `monoid.pow` or `nat.pow`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 08 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fixes%20against%20the%20latest%20mathlib/near/124800393):
depending on the first argument

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Apr 08 2018 at 19:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/fixes%20against%20the%20latest%20mathlib/near/124804713):
Getting rid of `local  infix ` ^ ` := monoid.pow` seems to help, so it uses `has_pow.pow` which is definitionally equal, but has rw lemmas.

