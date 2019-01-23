---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/20999cachingproofs.html
---

## Stream: [new members](index.html)
### Topic: [caching proofs](20999cachingproofs.html)

---

#### [Johan Commelin (Sep 18 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/caching%20proofs/near/134149890):
Re @**Keeley Hoek**'s dream. ( :warning: everything that follows should be taken with a fair amount of :four_leaf_clover:)
We now have two crawlers that spit out dependency graphs of statements in mathlib. What I wish is that this would be integrated with Lean. I don't think it is unreasonable that Lean could have some `cache.sqlite` in the root of every project. It could store dependencies there (not per file, but per statement!) and also cache proofs that have been computed by hammer/big-gun tactics.
This would have the side benefit that Lean could use more fine-grained dependency management on recompilation. Currently if someone *adds* a lemma to some basic file like `data/list/basic.lean` almost half of mathlib has to be recompiled. But nothing changed! We only added a lemma!
I understand that if you want reproducible builds, this might require some modification of the binary format, but that shouldn't be impossible.
This recompilation could also combine this cache and proof-irrelevance. If someone changed the *proof* of a `Prop`, but left the statement alone, then one only needs to chech that the new proof is in fact a proof. But it isn't necessary to recompile everything that depended on it.
Basically, when someone adds a lemma to `data/list/basic.lean` I want the recompile to be done in 5 seconds.

#### [Sean Leather (Sep 18 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/caching%20proofs/near/134150071):
I definitely think dependency tracking should be per-theorem and per-definition. I think the proof changing bit could probably be taken care by tracking changes to the theorem's interface (i.e. what you see with `set_option pp.all true`, `#check @theorem`).

#### [Scott Morrison (Sep 18 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/caching%20proofs/near/134150093):
Unfortunately too much proof caching becomes dangerous, especially when combined with hammers.

#### [Johan Commelin (Sep 18 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/caching%20proofs/near/134150095):
Why?

#### [Scott Morrison (Sep 18 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/caching%20proofs/near/134150096):
The problem can be that of course merely adding a lemma can't break a proof, but it can very much break a hammer.

#### [Scott Morrison (Sep 18 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/caching%20proofs/near/134150141):
Perhaps my hammer spends a certain amount of time searching a graph of rewrites, but has heuristics for aborting if things starting looking too bad.

#### [Sean Leather (Sep 18 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/caching%20proofs/near/134150144):
For example, adding a `@[simp]` theorem can change the way `simp` works?

#### [Johan Commelin (Sep 18 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/caching%20proofs/near/134150145):
Right, I see where this is going...

#### [Sean Leather (Sep 18 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/caching%20proofs/near/134150148):
That's true.

#### [Scott Morrison (Sep 18 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/caching%20proofs/near/134150153):
An innocuous extra lemma can cause it to waste time searching consequences of that lemma, and not only cause it to run longer, but to actually fail.

#### [Scott Morrison (Sep 18 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/caching%20proofs/near/134150166):
We want to allow people to leave the big hammers in their proofs, but also to be confident these proof scripts are still correct.

#### [Scott Morrison (Sep 18 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/caching%20proofs/near/134150170):
I can imagine a "two pass" compilation, which we could display e.g. with two colours of sidebars instead of the current yellow one.

#### [Scott Morrison (Sep 18 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/caching%20proofs/near/134150213):
On a first pass, we very aggressively use cached proofs, and if they work completely ignore the "expensive to check" tactic scripts.

#### [Sean Leather (Sep 18 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/caching%20proofs/near/134150214):
This leads to something I've been thinking about for a while: storing the proof structure directly to allow for fast builds.

#### [Scott Morrison (Sep 18 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/caching%20proofs/near/134150216):
On the second pass we actually check the tactic scripts still work.

#### [Scott Morrison (Sep 18 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/caching%20proofs/near/134150218):
By the way --- this discussion, which is great, definitely doesn't belong on this thread.

#### [Johan Commelin (Sep 18 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/caching%20proofs/near/134150221):
But that second pass has to go all over mathlib. Not just the 5 files that I have open.

#### [Johan Commelin (Sep 18 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/caching%20proofs/near/134151223):
Discussion continued here: https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/caching.20proofs

