---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/55574parsingonly.html
---

## Stream: [general](index.html)
### Topic: [`parsing_only`](55574parsingonly.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 10 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60parsing_only%60/near/147438292):
What does the `parsing_only` attribute, as in
````
notation [parsing_only] `command`:max := tactic unit
````
do?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Nov 10 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60parsing_only%60/near/147438358):
It makes the pretty printer ignore that notation

