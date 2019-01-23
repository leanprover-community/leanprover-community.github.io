---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/09722598analysisreorganization.html
---

## Stream: [PR reviews](index.html)
### Topic: [#598 analysis reorganization](09722598analysisreorganization.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Jan 17 2019 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/155347359):
I am confused: is it normal that there are still several references to `general_topology`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 17 2019 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/155360700):
Arggg Lean using olean of deleted lean files is really confusing. I'm sorry about this mess

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 17 2019 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/155360707):
I'll try again

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 17 2019 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/155361577):
just delete all .oleans

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 17 2019 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/155363096):
While we're on the topic of renaming and reorganization, is there a better name for the `category/` folder? It's not obvious what the difference between `category/` and `category_theory/` is on a first reading.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 17 2019 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/155364349):
`cs_category/` :see_no_evil:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 17 2019 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/155364387):
I was actually thinking the same thing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 17 2019 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/155364494):
it seems a bit crude though, surely there's a better description. "that thing that haskellers think is a category but isn't"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 17 2019 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/155364504):
It also helps with tab-completion (-;

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Jan 17 2019 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/155365107):
So is it the same as what they call "Hask"?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 17 2019 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/155365188):
Lol, we can call the directory `hask/` to troll them (-;

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 17 2019 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/155365233):
yeah, have you ever read Andrej Bauer's rant on why Hask isn't a category and they should stop pretending it exists?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 17 2019 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/155365344):
http://math.andrej.com/2016/08/06/hask-is-not-a-category/

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Jan 17 2019 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/155365532):
Maybe we should call it `not_a_category/` instead?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 17 2019 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/155365650):
`categoroid`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 17 2019 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/155365973):
I think Travis is fighting its cache again. It complains about errors that don't exist as far as I can see

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Jan 17 2019 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/155366751):
the import namespace for Monads etc in Haskell is `Control`, so we could rename it to `control`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 17 2019 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/155368296):
@**Mario Carneiro** I just merged today's commts. I hope Travis will stop inventing non-existent files, but I don't see what I could do if not

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 17 2019 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/155368363):
I just cleared the cache and restarted the build for your PR, so it should work this time

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 17 2019 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/155368377):
Ok, thanks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 18 2019 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/156353639):
Travis is now happy, I think you can merge now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Jan 18 2019 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/156357499):
merged

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Jan 18 2019 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/156358360):
the build failed, but I think this was due to the cache. (I think) I cleared the chache, and restarted it now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/156358441):
note: if you clear the PR cache, it falls back on the main cache (master), so you have to clear that too

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/156358462):
I discovered this after my first attempts to rebuild the PR failed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Jan 18 2019 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/156359224):
ah good to now. But I think I cleared the master cache anyway. The failure is happening at the master branch

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 18 2019 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/156362168):
Now it works on the main repository, but fails on lean-community...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jan 18 2019 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/156394463):
On the subject of Hask, I think the point may be valid but what we have in Lean actually looks like a category. We do not need to denounce it here. We could put everything in `category_theory.types` and generalize over time.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jan 18 2019 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/156394513):
I have a general definition for monad and applicative functors in my files so it should be coming soon ... right after we agree on a definition of monoidal categories

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Jan 18 2019 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/156394520):
Except that your functors aren't functors!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jan 18 2019 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/156394907):
That's a minor terminology detail. You can `functor` + `is_lawful_functor` as our notion of functor and that's fixed

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/156395489):
The question is what to call the structure built on `functor` alone

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jan 18 2019 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/156395682):
A while back, you proposed `functor_struct` (in the context of `category`, actually)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 18 2019 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/156395950):
and you want that to be the folder name?

