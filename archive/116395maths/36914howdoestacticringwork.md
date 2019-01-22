---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/36914howdoestacticringwork.html
---

## [maths](index.html)
### [how does tactic.ring work?](36914howdoestacticringwork.html)

#### [Johan Commelin (Jun 13 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how does tactic.ring work?/near/128000315):
@**Kevin Buzzard** Re 2: Because `znum` is a fast (but somewhat "unmathematical") implementation of `int`.

#### [Johan Commelin (Jun 13 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how does tactic.ring work?/near/128000321):
It computes in binary instead of unary arithmetic.

#### [Kevin Buzzard (Jun 13 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how does tactic.ring work?/near/128000345):
If that's the only reason then I might rip them out and replace them with ints because I am trying to de-obfuscate. I just don't want to rip them all out and then find that some meta code stops working!

#### [Johan Commelin (Jun 13 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how does tactic.ring work?/near/128000410):
Hmm, I can't change the stream... even though I changed the topic... [meeh]

