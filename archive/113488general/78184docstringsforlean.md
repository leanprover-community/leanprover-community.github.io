---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/78184docstringsforlean.html
---

## [general](index.html)
### [docstrings for lean](78184docstringsforlean.html)

#### [Edward Ayers (Oct 27 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docstrings%20for%20lean/near/136609124):
It's not completed yet, but I am incrementally adding documentation to undocumented parts of the lean source code. Would there be any interest in PRing this into the Lean 3 source eventually? Obviously someone would have to go over my changes and make sure that the comments are not wrong/ misleading etc. https://github.com/EdAyers/lean/tree/docstrings

#### [Kevin Buzzard (Oct 27 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docstrings%20for%20lean/near/136610180):
I guess nobody is going to be accepting any PRs to Lean source code any time soon, and perhaps any time ever.

#### [Edward Ayers (Oct 27 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docstrings%20for%20lean/near/136610191):
Yeah I don't want to spend a lot of time on it in case they release Lean 4.

#### [Scott Olson (Oct 27 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docstrings%20for%20lean/near/136614950):
I've been wondering whether the mathlib community should manage its own continuation of Lean 3.x in the meantime, because it seems like there are a number of low-impact improvements that would be worthwhile, and waiting for Lean 4 is a big unknown both in terms of schedule and how difficult porting will be, so otherwise mathlib's Lean could be stagnant for quite a while

#### [Johan Commelin (Oct 27 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docstrings%20for%20lean/near/136615904):
The disadvantage with such a "fork" is that it would bring all sorts of social implications and management issues with it. Your aren't just forking code, you will also need to make a whole bunch of users aware of the fact that latest mathlib won't compile on their vanilla Lean 3.4.1, and so you need to think about whether you want to include pointers all over the place that there is now `Lean'` or something.
I'm not in a position to see through all the ramifications and weigh the pros and cons.

#### [Mario Carneiro (Oct 27 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docstrings%20for%20lean/near/136615973):
I was initially pro-fork, and I think that since development has effectively stopped permanently on 3.x I think the problems associated with forking are greatly lessened. It will be a big change regardless when lean 4 comes around - Leo is essentially working on his own fork already

#### [Johan Commelin (Oct 27 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docstrings%20for%20lean/near/136616320):
Well, I guess it doesn't hurt to list the pros and cons.
The first big pro would be liberating the core library.
I know that @**Keeley Hoek** and @**Edward Ayers** have their private forks. These probably contain some useful patches.
Another pro would be that we can proactively work on caching. Although this is of course very non-trivial.

#### [Scott Olson (Oct 27 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docstrings%20for%20lean/near/136616557):
I think elan could be a big help with dealing with a new version pretty transparently, even if it has to be downloaded from a different location than the official releases

#### [Kevin Buzzard (Oct 27 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docstrings%20for%20lean/near/136617149):
One reason that I am so pro-actively trying to get mathematicians involved is that there is so so much more mathematics that can be done with Lean 3. I know some people are excitedly waiting for Lean 4 for CS reasons but I am quite happy with Lean 3.4.1.

#### [Johan Commelin (Oct 27 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docstrings%20for%20lean/near/136617461):
@**Kevin Buzzard** Right. But would you be happier with Lean-prime 3.4.1?

#### [Mario Carneiro (Oct 27 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docstrings%20for%20lean/near/136617930):
One problem with forking is that we don't know whether any of the bug fixes or whatever will have appropriate analogues in Lean 4

#### [Scott Morrison (Oct 27 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docstrings%20for%20lean/near/136620888):
If we were to make a fork, I think it shouldn't accept anything that will take substantial effort to reimplement in Lean 4. (That would be inviting people to waste their time.)

#### [Scott Morrison (Oct 27 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docstrings%20for%20lean/near/136620940):
But fixing `leanpkg`, adding docstrings to `expr` and elsewhere, both sounds like great reasons.

#### [Scott Morrison (Oct 27 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docstrings%20for%20lean/near/136620953):
If you're using `elan`, it's completely trivial to specify that you want to use a forked version of `lean`. (e.g. Keeley and I do this all the time)

#### [Sebastian Ullrich (Oct 27 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docstrings%20for%20lean/near/136621958):
I've just merged the two recent PRs to leanprover/lean and will release 3.4.2 when there are no more outstanding changes. If someone wants to implement tracking branches in leanpkg, I'll review and merge that, too.

#### [Scott Morrison (Oct 27 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docstrings%20for%20lean/near/136622496):
Hi, @**Keeley Hoek**, have you already done this in your fork? (Allowing `leanpkg` to track a specified branch of a repo.) I know we talked about this at some point, but can't remember if it's something you've already done.

#### [Keeley Hoek (Oct 28 2018 at 04:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docstrings%20for%20lean/near/136634305):
@**Scott Morrison|110087**, unfortunately for the life of me I've never really figured out what the problem with the branch tracking was. As far as I have been able to tell on my own computer, replacing a revision SHA1 with a branch name instead works, and `leanpkg upgrade` fetches a new copy of that branch properly (instead of reverting back to the SHA1 at the top of  `master`, or `lean-3.4.1`, or whatever).

I guess this is a bit crude though---was the problem that we wanted to be able to type specific SHA1s and have `leanpkg upgrade` walk up that commit to the top of a branch or something? I think the obvious problem there is that the same commit can be a part of multiple branches. We could have some `rev = "branch:SHA1"` syntax for that too keep track, though. I have not implemented this last thing (at some point I went away to do the first thing, but then realised it seemed like it already worked).

#### [Keeley Hoek (Oct 28 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docstrings%20for%20lean/near/136634354):
I am sitting on a small patch which drops the `leanpkg` requirement for `coreutils`, though. Makes it work on windows without git bash (I suppose you still need `git` in your path).

#### [Sebastian Ullrich (Oct 28 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docstrings%20for%20lean/near/136645288):
@**Keeley Hoek** Putting anything but a commit hash in `rev` is a no-go and should ideally not even be accepted by leanpkg. You lose all reproducibility with that. Instead there should be a new key `branch` that is used for `leanpkg upgrade`.

#### [Sebastian Ullrich (Nov 08 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docstrings%20for%20lean/near/147290881):
```quote
If someone wants to implement tracking branches in leanpkg, I'll review and merge that, too.
```
No takers? Anything else that should be part of 3.4.2?

#### [Keeley Hoek (Nov 08 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docstrings%20for%20lean/near/147291696):
I can't do it this week. :(

#### [Patrick Massot (Nov 08 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docstrings%20for%20lean/near/147292396):
Would you do it next week? I guess Sebastian could wait one more week.

#### [Keeley Hoek (Nov 08 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docstrings%20for%20lean/near/147293498):
I can promise to do it over the weekend

#### [Johan Commelin (Nov 09 2018 at 05:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docstrings%20for%20lean/near/147350080):
@**Sebastian Ullrich** Maybe this is unrealistic, but I would hope it isn't too hard. It would be very helpful if Lean could expose the current namespace and active `variables` and `include`s. Whether this is exposed via a message/trace/set_option/#print I wouldn't really care. As long as we can get hold of that information. Is this possible?

#### [Keeley Hoek (Nov 12 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docstrings%20for%20lean/near/147503284):
@**Sebastian Ullrich** filed at https://github.com/leanprover/lean/pull/1981
Please let me know if you'd like anything changed---I'll be speedy!

#### [Keeley Hoek (Nov 12 2018 at 04:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docstrings%20for%20lean/near/147503373):
@**Johan Commelin**, based on my previous experimentation it is possible to write a command in vanilla Lean which gets the current namespace, and I think I know a way to do that with `include`s as well (i.e. this is implementable as a `#whereami` command or something). The same tricks won't work for `variables` I don't think.

#### [Keeley Hoek (Nov 12 2018 at 04:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docstrings%20for%20lean/near/147503378):
Actually, I can think of a super hacky way to do it with variables as well, if they have ever been used already in the current `namespace`/`section`.

#### [Keeley Hoek (Nov 12 2018 at 04:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docstrings%20for%20lean/near/147503387):
I'd need an afternoon to remember how to use the code I wrote which does this

#### [Johan Commelin (Nov 12 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docstrings%20for%20lean/near/147507218):
@**Keeley Hoek** That sounds good and would be very helpful!

#### [Keeley Hoek (Nov 12 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/docstrings%20for%20lean/near/147511031):
Sure, but I'm going to have to do it early next week unless I'm lucky I think

