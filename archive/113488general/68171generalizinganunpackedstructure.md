---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/68171generalizinganunpackedstructure.html
---

## Stream: [general](index.html)
### Topic: [generalizing an unpacked structure](68171generalizinganunpackedstructure.html)

---

#### [Moses Schönfinkel (Oct 25 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalizing%20an%20unpacked%20structure/near/136460837):
I have something like `{to_structure := {x := X, y := Y}}` in my goal's conclusion. Is it possible to express `generalize h : {to_structure := {x := X, y := Y}} = a` somehow? (This particular formulation errors with `invalid structure instance, identifier expected`.)

#### [Simon Hudon (Oct 25 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalizing%20an%20unpacked%20structure/near/136468338):
You may need to give the name of each structure as `generalize h : {foo . to_structure := {bar . x := X, y := Y}} = a`

#### [Moses Schönfinkel (Oct 25 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalizing%20an%20unpacked%20structure/near/136502451):
Oh. Thanks. That's going to be a little painful.

