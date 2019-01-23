---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/36914howdoestacticringwork.html
---

## Stream: [maths](index.html)
### Topic: [how does tactic.ring work?](36914howdoestacticringwork.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 13 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how%20does%20tactic.ring%20work%3F/near/128000315):
@**Kevin Buzzard** Re 2: Because `znum` is a fast (but somewhat "unmathematical") implementation of `int`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 13 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how%20does%20tactic.ring%20work%3F/near/128000321):
It computes in binary instead of unary arithmetic.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jun 13 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how%20does%20tactic.ring%20work%3F/near/128000345):
If that's the only reason then I might rip them out and replace them with ints because I am trying to de-obfuscate. I just don't want to rip them all out and then find that some meta code stops working!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jun 13 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/how%20does%20tactic.ring%20work%3F/near/128000410):
Hmm, I can't change the stream... even though I changed the topic... [meeh]


{% endraw %}
