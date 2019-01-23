---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/09525addingfacttotypeclassinferencesystem.html
---

## Stream: [general](index.html)
### Topic: [adding fact to type class inference system](09525addingfacttotypeclassinferencesystem.html)

---

#### [Kevin Buzzard (Apr 17 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20fact%20to%20type%20class%20inference%20system/near/125208403):
Occasionally I run into a situation where Lean's type class inference system fails in the middle of a tactic mode proof -- say, for concreteness, that I attempted to infer that R was a ring, but type class inference didn't do it. Usually what happened was that I applied lemma X, perhaps to some elements of R, and this lemma needed R to be a ring but expected this proof to be supplied by type class inference but I have managed to construct R so that Lean didn't notice it was a ring. I can supply my own proof `H` that R is a ring though, and my fix is usually to replace `X` with `@X _ _ H _ _ ...`. Are there other ways of doing this though? I don't like that big pile of `_`s and I think that in the particular case I'm working on now I'd rather just inject `H` directly into the type class inference system somehow rather than using the `@` notation and then adding a whole bunch of `_`s. Is there a trick for doing this? In term mode I would create an instance but I'm in tactic mode.

#### [Kenny Lau (Apr 17 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20fact%20to%20type%20class%20inference%20system/near/125208450):
`letI := H`

#### [Kevin Buzzard (Apr 17 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20fact%20to%20type%20class%20inference%20system/near/125208489):
Oh, that's what it does ;-)

#### [Kevin Buzzard (Apr 17 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20fact%20to%20type%20class%20inference%20system/near/125211480):
Oh -- does this mean that my code is now likely to break in Lean 4? :-/

#### [Chris Hughes (Apr 17 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20fact%20to%20type%20class%20inference%20system/near/125211571):
Yes, but I don't see why it would be more likely than it was otherwise. There'll be a way to do that in lean4 I imagine, even if Mario has to write it.

#### [Kevin Buzzard (Apr 17 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20fact%20to%20type%20class%20inference%20system/near/125215430):
The reason I mentioned this specifically was that I believe this might have been something which Leo (probably for an important reason) actively tried to stop people from doing.

#### [Chris Hughes (Apr 17 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/adding%20fact%20to%20type%20class%20inference%20system/near/125215510):
I think it was just that `have` could previously be used for introducing instances, which wasn't the intended behaviour, since most of the time, you don't want a `have` to be an instance, and it might confuse the type class system when every single `have` is marked instance.

