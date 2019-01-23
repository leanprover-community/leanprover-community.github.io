---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/22683mathlibpullrequests.html
---

## Stream: [general](index.html)
### Topic: [mathlib pull requests](22683mathlibpullrequests.html)

---

#### [Sean Leather (Jun 19 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20pull%20requests/near/128290679):
@**Mario Carneiro** and @**Johannes Hölzl**: There are a lot of pending [PRs](https://github.com/leanprover/mathlib/pulls). What would you like to do with them?

I understand you were busy in Hanoi for a while. And perhaps you're still busy with other things. This is just a friendly ping to see what your status is.

Every now and then, something comes up that I want to contribute to mathlib, but then I see the list of pending PRs, and I get a bit discouraged, thinking that it might not be worth it. Some pretty simple PRs have not seen any response to indicate what will happen to them.

That said, if you need help managing contributions, I can volunteer some time. I can do commenting, labeling, and merging of simple PRs, while leaving the more interesting ones to you. (Of course, it's `git`, so things can always be changed later.)

#### [Sean Leather (Jun 19 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20pull%20requests/near/128301673):
@**Mario Carneiro** Thanks for all your recent PR merges and comments. Just so you know, if you'd like more help with mathlib maintenance, my offer stands.

#### [Mario Carneiro (Jun 19 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20pull%20requests/near/128301799):
I did all the easy stuff. I'm still a bit busy with Tom Hales' conference this week, but some organization or prioritization of existing PRs would be a thing third parties could do to make it easier. Unfortunately in many of the remaining PRs there is something I see a problem with but I haven't found the time to write about it, so for those you may have to just wait or guess (or ask).

#### [Simon Hudon (Jun 19 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20pull%20requests/near/128301866):
Anything I should be doing for `refine_struct`?

#### [Mario Carneiro (Jun 19 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20pull%20requests/near/128301943):
I'd rather not merge conflicts from github, could you do that? Otherwise it's okay (the conversation and travis failure made it look more complicated than it is, but I see it's ready for merge now.)

#### [Simon Hudon (Jun 19 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20pull%20requests/near/128301948):
Cool, sure thing

#### [Sean Leather (Jun 19 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20pull%20requests/near/128302469):
```quote
some organization or prioritization of existing PRs would be a thing third parties could do to make it easier.
```

Yeah, that's basically what I was thinking: triage with labels, assign issues and reviewers, ping the various parties every now and then, and update statuses. If it's an easy/obvious PR, merge it.

```quote
Unfortunately in many of the remaining PRs there is something I see a problem with but I haven't found the time to write about it, so for those you may have to just wait or guess (or ask).
```

Yep.

#### [Simon Hudon (Jun 19 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20pull%20requests/near/128307611):
The build time for mathlib is truly incredible. I wonder if we could minimize the rebuild size on every change

#### [Simon Hudon (Jun 19 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20pull%20requests/near/128307764):
This is where a lint tool would be very useful: we could find dead code and spurious dependencies

#### [Scott Morrison (Jun 20 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20pull%20requests/near/128347867):
The `refine_struct` in mathlib seems to be misbehaving. Here's my MWE:
````
import tactic.interactive

variable (α : Type)
def foo : semigroup α := 
begin
  refine_struct ({ .. } : semigroup α),
end
````

#### [Scott Morrison (Jun 20 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20pull%20requests/near/128347907):
Which just says `failed` on the `refine_struct`. It seems that it's failing at the very first line `str ← e.get_structure_instance_info,` of `refine_struct`.

#### [Scott Morrison (Jun 20 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20pull%20requests/near/128347909):
(@**Simon Hudon**)

#### [Sean Leather (Jun 20 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20pull%20requests/near/128347969):
@**Scott Morrison** Would you mind creating a [new GitHub issue](https://github.com/leanprover/mathlib/issues/new) with this information? It will make tracking the problem and its solution easier.

#### [Scott Morrison (Jun 20 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20pull%20requests/near/128347984):
Can do! I thought that since it was such a basic thing I might be doing something stupid, and should ask here first. :-)

#### [Sean Leather (Jun 20 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20pull%20requests/near/128348032):
```quote
Can do! I thought that since it was such a basic thing I might be doing something stupid, and should ask here first. :-)
```
Even if it is something stupid, others might run into it, too. And it's still easier to search GitHub than Zulip. :wink:

#### [Sean Leather (Jun 20 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20pull%20requests/near/128348046):
(That's my personal experience, anyway. Others may have different thoughts.)

#### [Sean Leather (Jun 20 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20pull%20requests/near/128348091):
Of course, you can always check here first and put it there later, I suppose. But I think that creates extra work for you.

#### [Scott Morrison (Jun 20 2018 at 08:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20pull%20requests/near/128348372):
https://github.com/leanprover/mathlib/issues/160

#### [Simon Hudon (Jun 20 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20pull%20requests/near/128358661):
(deleted)

