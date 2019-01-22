---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/39790Parser.html
---

## [new members](index.html)
### [Parser](39790Parser.html)

#### [Pablo Le Hénaff (Aug 08 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Parser/near/131100158):
Hello !

#### [Kenny Lau (Aug 08 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Parser/near/131100172):
bienvenu

#### [Pablo Le Hénaff (Aug 08 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Parser/near/131100173):
Can one use lean.parser to actually parse strings? If so, how do I run a parser on a string? That's what I want to do.

#### [Pablo Le Hénaff (Aug 08 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Parser/near/131102457):
Should I ask this on the other #**general**  stream?

#### [Sean Leather (Aug 08 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Parser/near/131102527):
You could try pinging @**Gabriel Ebner** and @**Sebastian Ullrich**. (Actually, I just did that. :smile:)

#### [Rob Lewis (Aug 08 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Parser/near/131102655):
@**Pablo Le Hénaff** You can. Here's an example: https://github.com/robertylewis/mathematica/blob/master/mathematica_parser.lean

#### [Scott Morrison (Aug 08 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Parser/near/131102723):
@**Rob Lewis** cool! Last time I asked about this, I got the impression it couldn't be done.

#### [Rob Lewis (Aug 08 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Parser/near/131102733):
Er, wait a sec. `lean.parser` is different from `data.buffer.parser`.

#### [Pablo Le Hénaff (Aug 08 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Parser/near/131102760):
I didn't know about `data.buffer.parser`

#### [Rob Lewis (Aug 08 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Parser/near/131102828):
`data.buffer.parser` is a parser monad. `lean.parser` exposes a bit of the built-in parser, I think.

#### [Rob Lewis (Aug 08 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Parser/near/131102840):
So you can use the former to write your own string parser. But you don't get access to any of the built in stuff.

#### [Pablo Le Hénaff (Aug 08 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Parser/near/131102853):
I think `data.buffer.parser` is what I need, thanks!

#### [Rob Lewis (Aug 08 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Parser/near/131102949):
@**Scott Morrison** What can't be done (easily, anyway) is parsing a string into an expr.

#### [Scott Morrison (Aug 08 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Parser/near/131103152):
ah, okay. The thing I really wanted to do was parse a string into a tactic.

#### [Scott Morrison (Aug 08 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Parser/near/131103215):
(I have some "self-describing" tactics, which you can ask to output a string, which is meant to be a tactic block that achieves whatever the invoked tactic just did (probably only using lower-level tactics). I really want to verify the output by parsing it and replaying it on the original goal, but never worked out how to do the parsing step.)

#### [Rob Lewis (Aug 08 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Parser/near/131103543):
Yeah, you'd need to access the Lean parser to do that.

#### [Rob Lewis (Aug 08 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Parser/near/131103549):
Can you make them output an expr instead of a string?

#### [Johan Commelin (Aug 08 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Parser/near/131103550):
Hmm, can't you save the tactics from just before you generate the strings

#### [Scott Morrison (Aug 08 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Parser/near/131103754):
Sure, certainly I can save the tactics: the point is to double-check that the copy-and-pasteable text you're about to present to the human really does what you promise.

