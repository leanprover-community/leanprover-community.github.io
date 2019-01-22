---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/50212rfllemmas.html
---

## [general](index.html)
### [rfl lemmas](50212rfllemmas.html)

#### [Kenny Lau (Sep 05 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20lemmas/near/133394916):
how important are rfl-simp-lemmas being rfl?

#### [Chris Hughes (Sep 05 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20lemmas/near/133395794):
I don't understand the question. You mean how important is it that they're proved using rfl, or that they can be proved using rfl or something completely different?

#### [Kenny Lau (Sep 05 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20lemmas/near/133395945):
should we depend on rfl lemmas being rfl (so that we can use dsimp instead of simp)?

#### [Scott Morrison (Sep 06 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl%20lemmas/near/133421379):
Yes, it's important... I think the point is that `dsimp` just `change`s the goal, while `simp` has to actually construct the proof, and sometimes that goes wrong. I should be able to be more specific (as someone explaining to me this difference actually made a big difference in the behaviour of `tidy`), but I'm having trouble thinking of an example now.

