---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/36527determinants.html
---

## Stream: [PR reviews](index.html)
### Topic: [determinants](36527determinants.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Oct 07 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/determinants/near/135357675):
I did some tidying on the determinants PR. I got rid of all the relics of `Sym` that weren't actually used for determinants - It's now only a 130 line Pr, versus 481. I also made the proofs hopefully more readable, if longer. Result is here https://github.com/leanprover/mathlib/compare/master...dorhinj:determinants2?expand=1

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Oct 07 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/determinants/near/135357687):
Old version https://github.com/leanprover/mathlib/pull/378/files

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/determinants/near/135371096):
is it PR'd? I want

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 08 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/determinants/near/135384959):
So now we have determinants, but we don't know that it is a monoid hom. For this we need https://github.com/leanprover/mathlib/pull/375

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/determinants/near/135385095):
I don't understand why that thing is called the `free_module`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 08 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/determinants/near/135385119):
Should I just remove that code for now?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 08 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/determinants/near/135385131):
The bit on scalar matrices is more important to me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/determinants/near/135385179):
Why do we need it? Like I said `diagonal` subsumes it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 08 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/determinants/near/135385205):
I think it is nice to have

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/determinants/near/135385217):
We also have `a * I`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/determinants/near/135385228):
which is the way the rest of the world notates this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 08 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/determinants/near/135385242):
Hmm... ok

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 08 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/determinants/near/135385245):
I don't really care

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/determinants/near/135385257):
I'm trying to understand what is needed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 08 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/determinants/near/135385302):
What is needed is that `det` is a monoid hom

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 08 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/determinants/near/135385306):
That PR doesn't say anything about monoid homs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 08 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/determinants/near/135385314):
No, but `det_one` uses `det_scalar`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 08 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/determinants/near/135385319):
That stuff was commented out in my `det` PR

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 08 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/determinants/near/135385325):
I don't know if Chris preserved those comments. Let me check

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 08 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/determinants/near/135385343):
No, those are gone

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Oct 08 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/determinants/near/135386346):
We have `det_one` so it is proven to be a monoid hom. Are monoid Homs defined yet?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 08 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/determinants/near/135386450):
Yes they are

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 08 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/determinants/near/135386455):
So my new PR is a 4-liner.


{% endraw %}
