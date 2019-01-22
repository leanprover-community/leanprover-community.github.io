---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/11952metatheorylibrariesframeworks.html
---

## [general](index.html)
### [metatheory libraries/frameworks](11952metatheorylibrariesframeworks.html)

#### [Brendan Zabarauskas (May 17 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126680432):
Hello, I was wondering if anybody was working on libraries/frameworks for making defining metatheory stuff in Lean easier. I'm thinking like LN for Coq: http://www.chargueraud.org/softs/ln/ - Context is that I'd like to prove some properties about my language Pikelet. See this issue: https://github.com/brendanzab/pikelet/issues/39

#### [Sean Leather (May 17 2018 at 08:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126682736):
Hi @**Brendan Zabarauskas**!

I'm currently working on a Lean proof of part of the Coq locally nameless library predecessor to the one you've linked to. I've forked [that library](https://github.com/spl/formal_binders) for my own reference. The reason I'm using the predecessor is because it had the Core ML typing formalization example, which seems to have been lost. (Also, are you familiar with [Metalib](https://github.com/plclub/metalib), a successor to that library?)

[My own work](https://github.com/spl/tts/) is currently strictly focused on what I need to get working for my research. However, I have certainly thought about making it useful more generally. As it is, I try to push into [mathlib](https://github.com/leanprover/mathlib/) small improvements/additions that have helped me as I go. I think that the better mathlib gets — and it is well-maintained! — the less one needs another library.

All that said, it will probably be a lot of work to formalize what you need in Lean. There's a lot of existing knowledge, including libraries/frameworks, of how to do it in Coq. But I do find Lean easier to use, faster to compile, and more enjoyable. If you do plan on trying it out, you may want to take at look at [my work](https://github.com/spl/tts/). It's still in progress, but I'll do my best to answer questions or help out.

#### [Brendan Zabarauskas (May 17 2018 at 08:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126682850):
Oh cool, glad to know work is being done! I'll check out your stuff.

I definitely find the ergonomics of Lean much more pleasant than Coq, but the ecosystem is still lacking. In the future I will definitely start needing some kind of separation logic, but earlier on I can probably get by without (need to tackle the higher level metatheory before then).

#### [Brendan Zabarauskas (May 17 2018 at 08:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126682930):
What in particular is interesting to look at in mathlib? I saw it before but didn't make the connection that it might have interesting things for metatheory in it.

#### [Sean Leather (May 17 2018 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126682973):
Mathlib has a lot of basic theories and data structures. It's really like a standard library for Lean.

#### [Brendan Zabarauskas (May 17 2018 at 08:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126682981):
Oh that's good to know. I'm guessing folks like it because it can move faster than the builtin libs?

#### [Sean Leather (May 17 2018 at 08:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126682982):
In particular `data.finset` is very useful for my work. But the wealth of  list-related proofs (`data.list`) also make it easy to work with lists.

#### [Sean Leather (May 17 2018 at 08:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126683036):
```quote
Oh that's good to know. I'm guessing folks like it because it can move faster than the builtin libs?
```
Yeah... Currently, the developers of Lean are working on the next version. They're not too keen on other changes right now. But mathlib, on the other hand, has had a lot of changes and is constantly growing.

#### [Brendan Zabarauskas (May 17 2018 at 08:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126683045):
Are you using a locally nameless representation in tts? Also would be handy to get a quick description of what tts is. Is the README opaque by design? :P

#### [Sean Leather (May 17 2018 at 08:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126683047):
Mathlib used to *be* the standard library before it was extracted from the Lean core.

#### [Sean Leather (May 17 2018 at 08:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126683052):
Not by design, just by fact of me focusing on proofs and less on evangelism. :wink:

#### [Sean Leather (May 17 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126683108):
It's based on a let-polymorphic lambda-calculus.

#### [Sean Leather (May 17 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126683111):
Core ML is another term for it.

#### [Sean Leather (May 17 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126683112):
`exp` has the expression language.

#### [Brendan Zabarauskas (May 17 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126683114):
Ah, right! Still, can be handy for folks like me searching for Lean examples on Github. I did a survey a few weeks ago, but had a hard time finding examples that I could learn off. Your work would have been super handy! <3

#### [Sean Leather (May 17 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126683126):
Sorry. I've just been too busy to make it usable for others to read. I still have a lot to do.

#### [Sean Leather (May 17 2018 at 08:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126683180):
When I'm closer to writing about it, the documentation will be a paper and/or thesis, I hope.

#### [Sean Leather (May 17 2018 at 08:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126683188):
But, just FYI, every `core.lean` file has the definitions. Every other `.lean` file (except `default.lean`) has proofs.

#### [Brendan Zabarauskas (May 17 2018 at 08:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126683229):
Yeah, perfectly understandable that it's a WIP. I'm cool if it's messy - don't let me looking put any pressure on your stuff. Thanks a bunch for linking! Would be neat to extract some common stuff at some stage though!

#### [Brendan Zabarauskas (May 17 2018 at 08:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126683233):
Have you put it under a License?

#### [Sean Leather (May 17 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126683242):
```quote
Would be neat to extract some common stuff at some stage though!
```
Indeed. I try to put as much common stuff as I can in mathlib. There's still more of that I have planned.

#### [Brendan Zabarauskas (May 17 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126683246):
Oooh, this is super handy :clap:  https://github.com/spl/tts/blob/master/src/exp/core.lean

#### [Sean Leather (May 17 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126683288):
```quote
Have you put it under a License?
```
Not at the moment. I suppose I should. Apache 2.0 since that what mathlib uses? I don't feel strongly about it.

#### [Brendan Zabarauskas (May 17 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126683359):
Yeah, I normally go with Apache 2.0. Sometimes I dual license with MIT. But that's cause I'm used to the Rust ecosystem. I tend to adapt to whatever is generally accepted in the ecosystem

#### [Sean Leather (May 17 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126683483):
LICENSE added.

#### [Brendan Zabarauskas (May 17 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126683544):
Thanks! Might be a while till I actually get around to getting started on formalisation, but it's handy to have your stuff around as reference.

