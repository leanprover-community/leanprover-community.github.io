---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/70396Provefalsefromnottrue.html
---

## [new members](index.html)
### [Prove false from not true?](70396Provefalsefromnottrue.html)

#### [Abhimanyu Pallavi Sudhir (Oct 05 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prove%20false%20from%20not%20true%3F/near/135283394):
Hi, I have an elementary question -- I'm proving something, and am down to having the proved statement "¬true", and the goal is "false". Is there a quick way to finish this?

#### [Andrew Ashworth (Oct 05 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prove%20false%20from%20not%20true%3F/near/135283461):
are you in term mode or tactic mode?

#### [Kenny Lau (Oct 05 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prove%20false%20from%20not%20true%3F/near/135283469):
if `h : ¬true` then `exact h trivial`

#### [Abhimanyu Pallavi Sudhir (Oct 05 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prove%20false%20from%20not%20true%3F/near/135283500):
Oh ok -- thanks, that works.

#### [Abhimanyu Pallavi Sudhir (Oct 05 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prove%20false%20from%20not%20true%3F/near/135284011):
By the way, is there a statement that automatically proves the goal "true"?

#### [Abhimanyu Pallavi Sudhir (Oct 05 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prove%20false%20from%20not%20true%3F/near/135284074):
I.e. "anything -> true" just like ex falso is "false -> anything"

#### [Kenny Lau (Oct 05 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prove%20false%20from%20not%20true%3F/near/135284181):
`trivial`

#### [Andrew Ashworth (Oct 05 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prove%20false%20from%20not%20true%3F/near/135284285):
as an aside, I think `trivial` is named weirdly. Why does it exist when `true.intro` is the canonical name?

#### [Abhimanyu Pallavi Sudhir (Oct 05 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prove%20false%20from%20not%20true%3F/near/135284287):
Thanks. Didn't know that could be used as a standalone statement.

#### [Abhimanyu Pallavi Sudhir (Oct 05 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prove%20false%20from%20not%20true%3F/near/135284298):
Re:true.intro Doesn't that apply to exfalso too? false.elim having a special name.

#### [Andrew Ashworth (Oct 05 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prove%20false%20from%20not%20true%3F/near/135284312):
`exfalso` is an eliminator

#### [Andrew Ashworth (Oct 05 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prove%20false%20from%20not%20true%3F/near/135284384):
but yes, i also prefer using `false.elim` ;)

#### [Chris Hughes (Oct 05 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prove%20false%20from%20not%20true%3F/near/135284568):
My favourite is `induction h` if `h : false`

#### [Kenny Lau (Oct 05 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prove%20false%20from%20not%20true%3F/near/135284579):
my favourite is `cases h`

#### [Charles Rezk (Oct 06 2018 at 02:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prove%20false%20from%20not%20true%3F/near/135290869):
Where can I get help for installing lean?

#### [Bryan Gin-ge Chen (Oct 06 2018 at 02:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prove%20false%20from%20not%20true%3F/near/135290928):
Feel free to ask in this chat! But we may want to use a different "thread".

#### [Charles Rezk (Oct 06 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prove%20false%20from%20not%20true%3F/near/135290937):
OK how do I do that?

