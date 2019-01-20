---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: PRreviews/598analysisreorganization.html
---

## [PR reviews](index.html)
### [#598 analysis reorganization](598analysisreorganization.html)

#### Mario Carneiro (Jan 17 2019 at 21:18):
`categoroid`

#### Patrick Massot (Jan 17 2019 at 21:23):
I think Travis is fighting its cache again. It complains about errors that don't exist as far as I can see

#### Johannes Hölzl (Jan 17 2019 at 21:35):
the import namespace for Monads etc in Haskell is `Control`, so we could rename it to `control`?

#### Patrick Massot (Jan 17 2019 at 21:55):
@**Mario Carneiro** I just merged today's commts. I hope Travis will stop inventing non-existent files, but I don't see what I could do if not

#### Mario Carneiro (Jan 17 2019 at 21:56):
I just cleared the cache and restarted the build for your PR, so it should work this time

#### Patrick Massot (Jan 17 2019 at 21:56):
Ok, thanks

#### Patrick Massot (Jan 18 2019 at 10:02):
Travis is now happy, I think you can merge now

#### Johannes Hölzl (Jan 18 2019 at 11:13):
merged

#### Johannes Hölzl (Jan 18 2019 at 11:31):
the build failed, but I think this was due to the cache. (I think) I cleared the chache, and restarted it now

#### Mario Carneiro (Jan 18 2019 at 11:32):
note: if you clear the PR cache, it falls back on the main cache (master), so you have to clear that too

#### Mario Carneiro (Jan 18 2019 at 11:33):
I discovered this after my first attempts to rebuild the PR failed

#### Johannes Hölzl (Jan 18 2019 at 11:46):
ah good to now. But I think I cleared the master cache anyway. The failure is happening at the master branch

#### Patrick Massot (Jan 18 2019 at 12:50):
Now it works on the main repository, but fails on lean-community...

#### Simon Hudon (Jan 18 2019 at 20:46):
On the subject of Hask, I think the point may be valid but what we have in Lean actually looks like a category. We do not need to denounce it here. We could put everything in `category_theory.types` and generalize over time.

#### Simon Hudon (Jan 18 2019 at 20:47):
I have a general definition for monad and applicative functors in my files so it should be coming soon ... right after we agree on a definition of monoidal categories

#### Johan Commelin (Jan 18 2019 at 20:47):
Except that your functors aren't functors!

#### Simon Hudon (Jan 18 2019 at 20:53):
That's a minor terminology detail. You can `functor` + `is_lawful_functor` as our notion of functor and that's fixed

#### Mario Carneiro (Jan 18 2019 at 21:01):
The question is what to call the structure built on `functor` alone

#### Simon Hudon (Jan 18 2019 at 21:04):
A while back, you proposed `functor_struct` (in the context of `category`, actually)

#### Mario Carneiro (Jan 18 2019 at 21:08):
and you want that to be the folder name?

