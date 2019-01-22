---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/22471copyingstructurefieldsfromtwoplaces.html
---

## [general](index.html)
### [copying structure fields from two places?](22471copyingstructurefieldsfromtwoplaces.html)

#### [Scott Morrison (May 13 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/copying%20structure%20fields%20from%20two%20places%3F/near/126489488):
I want to write `{ X and Y with .. }` to copy fields from two different structures. How is this meant to be done?

#### [Scott Morrison (May 13 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/copying%20structure%20fields%20from%20two%20places%3F/near/126489546):
Ah: `{ ..X, ..Y }`

