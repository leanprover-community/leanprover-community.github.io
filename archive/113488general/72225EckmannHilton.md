---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/72225EckmannHilton.html
---

## Stream: [general](index.html)
### Topic: [Eckmann–Hilton](72225EckmannHilton.html)

---

#### [Johan Commelin (Sep 07 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Eckmann%E2%80%93Hilton/near/133496192):
Today I thought it was a good idea to stretch the type class system a bit. In fact, I ended up not using it at all :rolling_on_the_floor_laughing:
https://gist.github.com/jcommelin/2e031b5446ca54089576ea9f66f12abf
Statement: Two unital binary operations that distribute over each other are in fact one and the same. Also, they are commutative and associative, so in fact a monoid structure.
This is used to prove that homotopy groups are abelian.

#### [Johan Commelin (Sep 07 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Eckmann%E2%80%93Hilton/near/133496199):
Any comments are welcome.

#### [Johan Commelin (Sep 07 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Eckmann%E2%80%93Hilton/near/133496250):
In particular, feel free to shoehorn this into the type class system.
Golfing is appreciated.

#### [Johan Commelin (Sep 07 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Eckmann%E2%80%93Hilton/near/133496443):
@**Reid Barton** Did you already have this somewhere in your repo?

#### [Reid Barton (Sep 07 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Eckmann%E2%80%93Hilton/near/133496454):
Nope I hadn't gotten that far. Cool!

#### [Reid Barton (Sep 07 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Eckmann%E2%80%93Hilton/near/133496542):
```lean
local notation a ` `m` ` b := @has_mul.mul X m a b
```
Does this really work? Also, it doesn't work for me. :)

#### [Reid Barton (Sep 07 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Eckmann%E2%80%93Hilton/near/133496632):
Oh nice. Copy and paste from github (even the raw page) doesn't preserve the source text correctly.

#### [Reid Barton (Sep 07 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Eckmann%E2%80%93Hilton/near/133496705):
Maybe you could choose something less sneaky like ``local notation a `<`m`>` b := @has_mul.mul X m a b``

#### [Johan Commelin (Sep 07 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Eckmann%E2%80%93Hilton/near/133496835):
Hmm, maybe I should.

#### [Johan Commelin (Sep 07 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Eckmann%E2%80%93Hilton/near/133496843):
But those are non-breaking spaces.

#### [Johan Commelin (Sep 07 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Eckmann%E2%80%93Hilton/near/133496999):
Hmmm... that's really nasty of GitHub.

#### [Johan Commelin (Sep 07 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Eckmann%E2%80%93Hilton/near/133497000):
They should know better.

#### [Johan Commelin (Sep 07 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Eckmann%E2%80%93Hilton/near/133497006):
I'll use fishhooks, like you suggested.

#### [Reid Barton (Sep 07 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Eckmann%E2%80%93Hilton/near/133497009):
Somehow when I pasted the source into emacs, they turned into regular spaces.
Not sure whether github or firefox or emacs is to blame

#### [Johan Commelin (Sep 07 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Eckmann%E2%80%93Hilton/near/133497108):
Ok, fair enough.

#### [Johan Commelin (Sep 07 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Eckmann%E2%80%93Hilton/near/133497111):
Anyway, it is fixed now.

#### [Reid Barton (Sep 07 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Eckmann%E2%80%93Hilton/near/133497452):
Haha, Lean prints both mul operations as `*`. It knows!!

#### [Johan Commelin (Sep 07 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Eckmann%E2%80%93Hilton/near/133497578):
Yes! I thought that was hilarious :rolling_on_the_floor_laughing:

#### [Johan Commelin (Sep 07 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Eckmann%E2%80%93Hilton/near/133501859):
@**Mario Carneiro** @**Johannes Hölzl** What would be the proper place for this in mathlib? Somewhere in `group_theory`?

#### [Johan Commelin (Sep 10 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Eckmann%E2%80%93Hilton/near/133684290):
PR'd this: https://github.com/leanprover/mathlib/pull/335

