---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/94743Insight.html
---

## [general](index.html)
### [Insight](94743Insight.html)

#### [Patrick Massot (Nov 26 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Insight/near/148393158):
Do we know how much of https://www.youtube.com/watch?v=bGD_YF64Nwk has been formally certified?

#### [Scott Morrison (Nov 26 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Insight/near/148394235):
Interesting question. I was wondering the same earlier today. Looks like it was certified enough. :-)

#### [Scott Morrison (Nov 26 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Insight/near/148394259):
https://lars-lab.jpl.nasa.gov/

#### [Patrick Massot (Nov 26 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Insight/near/148394845):
Indeed

#### [Patrick Massot (Nov 26 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Insight/near/148395406):
https://lars-lab.jpl.nasa.gov/JPL_Coding_Standard_C.pdf is pretty scary reading. It makes me wonder why they still use C

#### [Patrick Massot (Nov 26 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Insight/near/148395488):
(not that  I know anything about this)

#### [Andrew Ashworth (Nov 26 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Insight/near/148398421):
Embedded systems are still mainly programmed in C and assembly, since you need to interface directly with hardware

#### [Andrew Ashworth (Nov 26 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Insight/near/148398437):
C++ is getting some traction though

#### [Kevin Buzzard (Nov 26 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Insight/near/148400439):
How difficult can it be to formally verify C code? Doesn't C only have about 8 commands?

#### [Simon Cruanes (Nov 26 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Insight/near/148402018):
C is pretty difficult to verify due to the tons of undefined behaviors, but people have done a lot of work on it. I'm more surprised that they never switched to Ada…

#### [Chris Hughes (Nov 26 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Insight/near/148402097):
`nat` only has two.

#### [Kevin Buzzard (Nov 27 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Insight/near/148408016):
```quote
`nat` only has two.
```
 Yeah, but their behaviour is well-defined :-)

#### [Kenny Lau (Nov 27 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Insight/near/148408161):
```quote
How difficult can it be to formally verify C code? Doesn't C only have about 8 commands?
```
 ... so... verify brainfuck?

#### [Keeley Hoek (Nov 27 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Insight/near/148408641):
Most of those rules are more benign than I would have thought
Pretty sensible for any embedded system which wants to be careful I guess
Also, classic:
````
Rule 30 (type conversion) 
Conversions shall not be performed between a pointer to a
function and any type other than an integral type.
````

#### [Keeley Hoek (Nov 27 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Insight/near/148408657):
"Sorry team, I cast my function pointer to a double, then added five"

