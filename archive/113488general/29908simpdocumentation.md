---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/29908simpdocumentation.html
---

## Stream: [general](index.html)
### Topic: [simp documentation](29908simpdocumentation.html)

---


{% raw %}
#### [ Simon Hudon (Mar 15 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20documentation/near/123728672):
@**Kevin Buzzard** I'm having a look at your recent PR. In "When it is unadvisable to use simp", why not use `show` instead of `suffices`?

#### [ Kevin Buzzard (Mar 15 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20documentation/near/123728716):
I think that's kind of backwards

#### [ Kevin Buzzard (Mar 15 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20documentation/near/123728718):
let's say you're a long way from a goal

#### [ Kevin Buzzard (Mar 15 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20documentation/near/123728719):
and simp makes tiny progress

#### [ Kevin Buzzard (Mar 15 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20documentation/near/123728727):
no wait

#### [ Kevin Buzzard (Mar 15 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20documentation/near/123728728):
simp changes your goal slightly

#### [ Kevin Buzzard (Mar 15 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20documentation/near/123728729):
it makes it into X

#### [ Kevin Buzzard (Mar 15 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20documentation/near/123728730):
then `suffices X, simpa [this]` does the same thing

#### [ Kevin Buzzard (Mar 15 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20documentation/near/123728731):
but show won't work

#### [ Kevin Buzzard (Mar 15 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20documentation/near/123728734):
becuase X isn't defeq to the original goal

#### [ Kevin Buzzard (Mar 15 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20documentation/near/123728777):
The idiom (is that the right word?) is that if simp changes your goal to X, then why not make a new goal and instantly close it with simp.

#### [ Simon Hudon (Mar 15 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20documentation/near/123728825):
Good point. Then you can only choose `show` in the special case where the new goal is `defeq` to the old one.

#### [ Simon Hudon (Mar 15 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20documentation/near/123728831):
It might be worth having a shortcut for `suffices : (simplified thing), by simpa [this]`

#### [ Kevin Buzzard (Mar 15 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20documentation/near/123728985):
yeah, it's `simp` ;-)

#### [ Kevin Buzzard (Mar 15 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20documentation/near/123728992):
`simp to (simplified thing)`?

#### [ Mario Carneiro (Mar 15 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20documentation/near/123728999):
`simpa` was intended for basically exactly that use case. It's not exactly wasting that many keywords as it is

#### [ Kevin Buzzard (Mar 15 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20documentation/near/123729000):
yeah but golf

#### [ Mario Carneiro (Mar 15 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20documentation/near/123729002):
for golf, `simpa [bla] using bla` is even more effective

#### [ Kevin Buzzard (Mar 15 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20documentation/near/123729041):
`simp {answer := simplified thing}`

#### [ Mario Carneiro (Mar 15 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20documentation/near/123729053):
also, you can just write `suffices : (simplified thing), {simpa}`


{% endraw %}
