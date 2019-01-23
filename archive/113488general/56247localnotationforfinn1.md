---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/56247localnotationforfinn1.html
---

## Stream: [general](index.html)
### Topic: [local notation for fin (n+1)](56247localnotationforfinn1.html)

---


{% raw %}
#### [ Johan Commelin (May 24 2018 at 10:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127019139):
How do I make the following work?
```lean
local notation ` [n] ` := fin (n+1)
```
I need this notation a lot, and all the explicit `fin (n+1)`'s are driving me crazy. Plus all the off-by-one errors that creep into my code...

#### [ Kevin Buzzard (May 24 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127019201):
hmm

#### [ Kevin Buzzard (May 24 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127019204):
`[n]` already means something else

#### [ Kevin Buzzard (May 24 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127019208):
Oh -- I think that the n in quotes is a literal n

#### [ Kevin Buzzard (May 24 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127019213):
so at the very least you'll want `` ` [ ` n ` ] ` ``

#### [ Kevin Buzzard (May 24 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127019219):
but I am not sure how over-riding already-used notation works

#### [ Johan Commelin (May 24 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127019343):
Thanks, it is working now. I didn't know about the existing notation; but using `local notation` I can override it just fine (-;

#### [ Kevin Buzzard (May 24 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127019774):
```lean
variable (n : ℕ)
#check [n] -- list ℕ
```

#### [ Kevin Buzzard (May 24 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127019779):
you just broke list ;-)

#### [ Kevin Buzzard (May 24 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127019780):
at least locally

#### [ Kevin Buzzard (May 24 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127019783):
of course, this might be clever :-)

#### [ Kevin Buzzard (May 24 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127019795):
although given your smiley convention I think I would have recommended `` ` (-; ` n ` ;-) ` ``

#### [ Johan Commelin (May 24 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127020026):
Hmm, but I guess that the `local` prefix means that I am still safe. I'm not using lists...

#### [ Patrick Massot (May 24 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127020289):
Johan, there are plenty of brackets available. See how I use brackets for commutators in https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/support.lean#L115 for instance

#### [ Kevin Buzzard (May 24 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127020333):
But `[n]` is standard in this game, isn't it?

#### [ Patrick Massot (May 24 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127020336):
Sure. `[a, b]` for commutators is also standard

#### [ Kevin Buzzard (May 24 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127020337):
CS : "overloading is bad"; Math "but we do it so well!"

#### [ Patrick Massot (May 24 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127020344):
But waiting for CS people to change their notation for lists won't help

#### [ Kevin Buzzard (May 24 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127020345):
I don't think Johan should even make the notation local

#### [ Kevin Buzzard (May 24 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127020348):
I think Lean should just infer which notation is being used

#### [ Kevin Buzzard (May 24 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127020350):
it has an elaborator, right?

#### [ Patrick Massot (May 24 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127020351):
Sometimes it does

#### [ Patrick Massot (May 24 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127020406):
Sean, I meant: "sometimes it infers which notation is being used", not "sometimes it has an elaborator"...

#### [ Sean Leather (May 24 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127020458):
Patrick: Aww, I liked the latter interpretation better.

#### [ Kevin Buzzard (May 24 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127020591):
Man, that would be a pretty crazy Lean 4 development

#### [ Kevin Buzzard (May 24 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127020594):
"we removed the elaborator to encourage users to write better code"

#### [ Kevin Buzzard (May 24 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127020596):
the metamath approach

#### [ Patrick Massot (May 24 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127020637):
This time we are happy Mario isn't working on Lean 4

#### [ Sean Leather (May 24 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127020640):
Slogan: How To Be Lean: Elaborate It Yourself!

#### [ Reid Barton (May 24 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127041620):
I wish there was something between `notation` and `local notation`, so that modules could export notation without forcing every downstream client to see it.
For example, something like notation which is tied to the current namespace, so that it is only visible when that namespace is open.

#### [ Reid Barton (May 24 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127041638):
(I think that exact idea is probably not very good, but something of that flavor.)

#### [ Mario Carneiro (May 24 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127041848):
This is exactly how lean 2 notation used to work. Why it changed, I don't know, and I'm not clear on whether to expect this to be different in lean 4.

#### [ Mario Carneiro (May 24 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127041932):
I think that lean 3 notation is not handled very well at all, this is why I avoid all notation overloading in mathlib

#### [ Johan Commelin (May 24 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127041951):
Hmmm, ok. Does that mean that my `local notation` for `fin (n+1)` is dangerous?

#### [ Mario Carneiro (May 24 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127041964):
A local notation is fine, assuming you never use lists in that file

#### [ Mario Carneiro (May 24 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127042026):
but global notations require global coordination

#### [ Johan Commelin (May 24 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20notation%20for%20fin%20%28n%2B1%29/near/127042033):
Ok, understood


{% endraw %}
