---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/05925Proofexamples.html
---

## [general](index.html)
### [Proof examples?](05925Proofexamples.html)

#### [Ryan Smith (Sep 21 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof examples?/near/134356151):
Hi, I'm entirely new to lean. I've read the docs, but I'm struggling to see what it would look like to prove anything in practice. The homepage didn't have much of a gallery, do we have examples of what a simple proof of the infinitude of primes or Lagrange's theorem for finite groups would look like?

#### [Bryan Gin-ge Chen (Sep 21 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof examples?/near/134356286):
You may want to check out [the lean mathlib project](https://github.com/leanprover/mathlib); many of the contributors are quite active in this chat.  [Here's the proof of the infinitude of primes](https://github.com/leanprover/mathlib/blob/master/data/nat/prime.lean#L212) in mathlib, and [here's the proof of Lagrange's theorem](https://github.com/leanprover/mathlib/blob/master/group_theory/order_of_element.lean#L126).

#### [Mario Carneiro (Sep 21 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof examples?/near/134356350):
Yay, mathlib already contains two theorems selected at random from math. Thus, mathlib has 75% of math, QED

#### [Johan Commelin (Sep 21 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof examples?/near/134356351):
Welcom @**Ryan Smith** If you want you can write a little introduction about your background in https://leanprover.zulipchat.com/#narrow/stream/113489-new-members/subject/Introductions. We're a bunch of enthousiastic mathematicians and computer scientists trying to build a library of data structures, automation and of course a bunch of mathematics.

#### [Bryan Gin-ge Chen (Sep 21 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof examples?/near/134356352):
I also forgot to say welcome! I'm also fairly new to lean and I've been asking silly questions in the #**new members**  stream for the past month or so.

#### [Johan Commelin (Sep 21 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof examples?/near/134356410):
Since a couple of weeks we try to post in https://leanprover.zulipchat.com/#narrow/stream/116395-maths/subject/What's.20new.20in.20Lean.20maths.3F to tell people about new stuff in the library

#### [Mario Carneiro (Sep 21 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof examples?/near/134356426):
Johan, could you summarize the results of the kbb project in that thread?

#### [Johan Commelin (Sep 21 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof examples?/near/134356470):
I will try :smiley:

#### [Simon Hudon (Sep 21 2018 at 06:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof examples?/near/134356499):
Btw, why is that thread in #**maths** ? That's a stream I don't follow

#### [Ryan Smith (Sep 21 2018 at 07:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof examples?/near/134356612):
Oh cool, a number of basic primitives are already implemented. I thought things were a bit more rudimentary from reading the documentation.

#### [Johan Commelin (Sep 21 2018 at 07:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof examples?/near/134356959):
@**Simon Hudon** Because it really is about What's new in maths in Lean. We could probably have a similar thread in general where we post about new tactics and data structures and so on. But that thread is really about "Yeah, we have the fact that quotients of Noetherian modules are Noetherian!".

#### [Johan Commelin (Sep 21 2018 at 07:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof examples?/near/134356964):
Also see my latest post there :wink:

#### [Simon Hudon (Sep 21 2018 at 07:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof examples?/near/134357028):
The one summarize Kevin's birthday present?

#### [Johan Commelin (Sep 21 2018 at 07:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof examples?/near/134357077):
Right, that one.

#### [Johan Commelin (Sep 21 2018 at 07:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof examples?/near/134357081):
Is that the kind of stuff you would be interested in to know?

#### [Simon Hudon (Sep 21 2018 at 07:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof examples?/near/134357190):
I think I misread, I thought you also announced tactics there (like `linarith`). To be frank, I didn't understand too much of what was put in Kevin's present.

#### [Johan Commelin (Sep 21 2018 at 07:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof examples?/near/134357205):
We also announced `linarith` there. So there might be some overlap... but I think we could cross post those announcements to a "What's new in Lean thread in `#general`"

#### [Simon Hudon (Sep 21 2018 at 07:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof examples?/near/134357251):
That sounds like a good idea. Thanks :)

#### [Mario Carneiro (Sep 21 2018 at 07:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof examples?/near/134357417):
I cross posted `abel` there since there is an overlap of interest, but also because people always want to have a conversation about these news items and I would rather not clutter up an announcement thread with that

#### [Mario Carneiro (Sep 21 2018 at 07:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof examples?/near/134357488):
In fact, I suggest we get in the habit of linking each news item to a thread about it specifically so people can use it as a hub

#### [Johan Commelin (Sep 21 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Proof examples?/near/134357742):
Done.

