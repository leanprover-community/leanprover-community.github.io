---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/76545rcases.html
---

## [general](index.html)
### [rcases?](76545rcases.html)

#### [Reid Barton (Sep 07 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rcases?/near/133502924):
Is there a way to use `rcases` with `?` to get hints, or just `rintros`?

#### [Reid Barton (Sep 07 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rcases?/near/133503552):
Wait, how do I use `rintros?` again? It's telling me "unexpected token".

#### [Kevin Buzzard (Sep 07 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rcases?/near/133505329):
`rintros` works for me. Is it in `tactic.interactive`? Looks like it. Note also `meta def rintros := rintro` ;-)

#### [Kenny Lau (Sep 07 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rcases?/near/133508220):
@**Kevin Buzzard** note the question mark in `rintros?`

#### [Johan Commelin (Sep 07 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rcases?/near/133508629):
@**Kenny Lau** You missed a chance to formulate that as a question.

