---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/09475Shamelesslean4request.html
---

## Stream: [general](index.html)
### Topic: [Shameless lean 4 request](09475Shamelesslean4request.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 23 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Shameless%20lean%204%20request/near/148202175):
In Lean 4 could we please please please have something like Haskell's `error`, just a pure function which takes a `string` or `format` or something and otherwise acts just like `sorry` (but gives no `sorry` used warnings). Of course, it would have to be meta.

It would be a really big aid to metaprogramming, since right now every time I want to define a pure function used in a program which has some invalid arguments I have to make it fail silently for that invalid input, instead of returning a nice warning---or more likely from a practical perspective, make everything tactic for absolutely no reason and corrupt my entire program with `tactic`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 23 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Shameless%20lean%204%20request/near/148202217):
I thought there was something like this already. `undefined_core`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 23 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Shameless%20lean%204%20request/near/148202274):
Praise be! weird name

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Nov 23 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Shameless%20lean%204%20request/near/148202315):
Haha, yes

