---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/72590Fromfieldstosets.html
---

## Stream: [general](index.html)
### Topic: [From fields to sets](72590Fromfieldstosets.html)

---


{% raw %}
#### [ Anthony Bordg (Oct 04 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/From%20fields%20to%20sets/near/135217336):
Hello,

is there an easy way to get the underlying set of a (discrete) field ?
Thanks

#### [ Simon Hudon (Oct 04 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/From%20fields%20to%20sets/near/135217489):
If you have `field α`, `set.univ α` is the underlying set.

#### [ Anthony Bordg (Oct 04 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/From%20fields%20to%20sets/near/135217940):
```quote
If you have `field α`, `set.univ α` is the underlying set.
```
Great! Thank you Simon.

#### [ Simon Hudon (Oct 04 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/From%20fields%20to%20sets/near/135217959):
:+1:

#### [ Simon Hudon (Oct 04 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/From%20fields%20to%20sets/near/135218041):
What do you use it for? Typically, I don't see that set used much because the type does most of the work on its own

#### [ Mario Carneiro (Oct 04 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/From%20fields%20to%20sets/near/135218290):
I think maybe you just want `α`?

#### [ Mario Carneiro (Oct 04 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/From%20fields%20to%20sets/near/135218339):
It's not an "underlying set", it's an "underlying type"

#### [ Mario Carneiro (Oct 04 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/From%20fields%20to%20sets/near/135218382):
and there is no underlying about it because we define "a field on α" rather than just "a field", so α is the carrier

#### [ Anthony Bordg (Oct 04 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/From%20fields%20to%20sets/near/135219190):
```quote
What do you use it for? Typically, I don't see that set used much because the type does most of the work on its own
```
You're right, I realized that I don't need it. :+1:


{% endraw %}
