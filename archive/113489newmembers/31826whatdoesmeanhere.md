---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/31826whatdoesmeanhere.html
---

## [new members](index.html)
### [what does . mean here?](31826whatdoesmeanhere.html)

#### [Bryan Gin-ge Chen (Aug 30 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/what%20does%20.%20mean%20here%3F/near/133063613):
I copied this from [library/init/data/nat/basic.lean](https://github.com/leanprover/lean/blob/master/library/init/data/nat/basic.lean#L84).
```lean
lemma not_succ_le_zero : ∀ (n : ℕ), nat.succ n ≤ 0 → false 
.
```

#### [cbailey (Aug 30 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/what%20does%20.%20mean%20here%3F/near/133063790):
It's syntax to execute a method inside a module (the nat module). If you do 
```lean
open nat
```
you can access succ without the nat. prefix by opening the nat namespace. There's a section in "Theorem Proving in Lean" about the module/namespace keywords.

#### [Bryan Gin-ge Chen (Aug 30 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/what%20does%20.%20mean%20here%3F/near/133063859):
Sorry, I meant the . on the line all by itself, which somehow suffices as a proof of this lemma.

#### [Patrick Massot (Aug 30 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/what%20does%20.%20mean%20here%3F/near/133063917):
Usually an dot at the end of something is there only to help the parser

#### [Bryan Gin-ge Chen (Aug 30 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/what%20does%20.%20mean%20here%3F/near/133064379):
What do you mean by "help the parser" here? Is the dot shorthand for something?

#### [Patrick Massot (Aug 30 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/what%20does%20.%20mean%20here%3F/near/133064406):
I mean it tells the parser that something ends here.

#### [Patrick Massot (Aug 30 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/what%20does%20.%20mean%20here%3F/near/133064419):
But really I don't know why there is something to end here. The statement is trivial but many other trivial things still require a proof

#### [Rob Lewis (Aug 30 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/what%20does%20.%20mean%20here%3F/near/133064512):
It's being used to indicate that this is an empty pattern match. Structurally, there's no `n` for which you can have a proof of `succ n ≤ 0`.

#### [Rob Lewis (Aug 30 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/what%20does%20.%20mean%20here%3F/near/133064535):
So you're proving the lemma by induction on `n`, except there are no cases because none of them make sense.

#### [Rob Lewis (Aug 30 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/what%20does%20.%20mean%20here%3F/near/133064601):
You need the `.` so that Lean knows the proof is over and doesn't confuse the next line with a continuation of the lemma statement.

#### [Bryan Gin-ge Chen (Aug 30 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/what%20does%20.%20mean%20here%3F/near/133064617):
OK, that makes sense, thanks!

#### [cbailey (Aug 30 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/what%20does%20.%20mean%20here%3F/near/133064965):
Oh I was way off lol. My apologies.

