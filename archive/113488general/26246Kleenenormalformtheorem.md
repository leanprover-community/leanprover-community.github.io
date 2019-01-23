---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/26246Kleenenormalformtheorem.html
---

## Stream: [general](index.html)
### Topic: [Kleene normal form theorem](26246Kleenenormalformtheorem.html)

---

#### [Mario Carneiro (May 21 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Kleene%20normal%20form%20theorem/near/126877954):
Yay, milestone achieved. The statement that I actually proved shows that `eval : code -> N ->. N` which evaluates a partial recursive function given by a code, is itself a partial recursive function. This is also known as a universal Turing machine in the language of Turing machines.

#### [Patrick Massot (May 21 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Kleene%20normal%20form%20theorem/near/126878601):
Congratulations!

#### [Patrick Massot (May 21 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Kleene%20normal%20form%20theorem/near/126878604):
Do you plan to return to maths now?

#### [Mario Carneiro (May 21 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Kleene%20normal%20form%20theorem/near/126878738):
Lol this is math

#### [Mario Carneiro (May 21 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Kleene%20normal%20form%20theorem/near/126878775):
I'm aiming for proper computability theory at the moment, with r.e. sets and such

#### [Patrick Massot (May 21 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Kleene%20normal%20form%20theorem/near/126878826):
What is "r.e. sets"?

#### [Mario Carneiro (May 21 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Kleene%20normal%20form%20theorem/near/126878833):
recursively enumerable

#### [Mario Carneiro (May 21 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Kleene%20normal%20form%20theorem/near/126878851):
the set of turing machines that halt is a r.e. set

#### [Mario Carneiro (May 21 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Kleene%20normal%20form%20theorem/near/126878866):
but its complement isn't

#### [Sebastian Ullrich (May 21 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Kleene%20normal%20form%20theorem/near/126878932):
IOW the set of machines that reset is a r.e.set

#### [Patrick Massot (May 21 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Kleene%20normal%20form%20theorem/near/126878969):
Thanks

#### [Sebastian Ullrich (May 21 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Kleene%20normal%20form%20theorem/near/126879054):
This looks like a really nice development. Though I have to wonder what we did wrong when building leanpkg to encourage putting everything in a single monolithic package :smile: .

#### [Mario Carneiro (May 21 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Kleene%20normal%20form%20theorem/near/126879058):
I want to finish the MDRP theorem I started last year

#### [Patrick Massot (May 21 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Kleene%20normal%20form%20theorem/near/126880128):
Sebastian: do you refer to mathlib here?

#### [Sebastian Ullrich (May 21 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Kleene%20normal%20form%20theorem/near/126888386):
@**Patrick Massot** Yes. Not that it's a real issue until we start prebuilding dependencies on `leanpkg configure`.

#### [Patrick Massot (May 21 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Kleene%20normal%20form%20theorem/near/126888402):
It seems it makes it easier for Mario and Johannes to guarantee a consistent mathlib

#### [Patrick Massot (May 21 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Kleene%20normal%20form%20theorem/near/126888415):
But I think we really need precompiled mathlib nightlies

