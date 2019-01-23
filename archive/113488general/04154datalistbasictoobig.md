---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/04154datalistbasictoobig.html
---

## Stream: [general](index.html)
### Topic: [data/list/basic too big?](04154datalistbasictoobig.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 22 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/data/list/basic%20too%20big%3F/near/128444963):
Is this output from travis:
````
/home/travis/build/semorrison/lean-tidy/_target/deps/mathlib/data/list/basic.lean: list.last_append
No output has been received in the last 10m0s, this potentially indicates a stalled build or something wrong with the build itself.
Check the details on how to adjust your build configuration on: https://docs.travis-ci.com/user/common-build-problems/#Build-times-out-because-no-output-was-received
````
(taken from https://travis-ci.org/semorrison/lean-tidy/builds/395245684?utm_source=email&utm_medium=notification) an indication that `data/list/basic.lean` has grown too big?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Jun 22 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/data/list/basic%20too%20big%3F/near/128445006):
Another piece of evidence of this is that when a I compile all of mathlib on a many core machine, there seems to be a bottleneck in data/list/basic, when most of the cores have to pause to wait for the thread dealing with this file to finish.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 22 2018 at 02:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/data/list/basic%20too%20big%3F/near/128447691):
AFAIK the unit of granularity for threading is a single declaration, so I don't think the file size itself is the issue.
Of course there could be bottlenecks in the dependency graph of declarations, individual declarations which take a long time to compile, etc.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 22 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/data/list/basic%20too%20big%3F/near/128459145):
I think Reid is right. We would need to look at which declaration is causing the slowdown and optimize that. I've seen it myself but haven't taken the time to look into it. I wonder if it's as simple as looking at the printed declaration (`list.last_append` as you have it), or if there is another culprit.

Perhaps a Lean expert would want to commit a little time here?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jun 22 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/data/list/basic%20too%20big%3F/near/128475720):
I think that usually when lean's output seems to get "stuck" on one declaration for a long time, that declaration usually is the one that's taking all the time. In the past there were a couple of uses of `finish` which were very expensive, and easy to spot if you watched the build output.
I notice that `list.last_append` uses `rsimp`, which I didn't even know existed; maybe it can also be very slow?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 25 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/data/list/basic%20too%20big%3F/near/128588093):
I just sped up the build by simplifying `list.last_append`. `rsimp` was definitely the problem and turned out to be unnecessary. `list.last_append` now builds very quickly. PR forthcoming. :tada:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 25 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/data/list/basic%20too%20big%3F/near/128588103):
I already fixed this in my local copy

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 25 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/data/list/basic%20too%20big%3F/near/128588142):
not sure if there are any other issues, I'm working on better profiling

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 25 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/data/list/basic%20too%20big%3F/near/128588153):
(I just replaced `rsimp` with `simp` and the proof went through)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 25 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/data/list/basic%20too%20big%3F/near/128588164):
https://github.com/leanprover/mathlib/pull/167

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 25 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/data/list/basic%20too%20big%3F/near/128588331):
```quote
I already fixed this in my local copy
```
@**Mario Carneiro** So I wasted my time. In the future, can you please communicate this to the rest of us? It would be most helpful if you or anyone else created GitHub issues for such things. They tend to get lost in Zulip.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 25 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/data/list/basic%20too%20big%3F/near/128588335):
Sorry, been busy these days

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 25 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/data/list/basic%20too%20big%3F/near/128588346):
... which is why I offered to help maintain mathlib. :smile:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jun 25 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/data/list/basic%20too%20big%3F/near/128588395):
of course it's not necessarily a waste of time, depending on how you discovered that theorem

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 25 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/data/list/basic%20too%20big%3F/near/128588521):
```quote
of course it's not necessarily a waste of time, depending on how you discovered that theorem
```
I discovered it because I saw the same issue mentioned above in this thread (which means that it was taking a long time to compile `last_append`, which means I wasted time waited for it to compile :wink:).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 25 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/data/list/basic%20too%20big%3F/near/128600209):
I think one thing that might help streamline maintenance is write a lint tool. I was thinking of using grep to spot the most obvious stylistic mistakes and that you we could add as a git hook

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Jun 25 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/data/list/basic%20too%20big%3F/near/128600221):
It might help use the maintainers' time more sparingly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 25 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/data/list/basic%20too%20big%3F/near/128605048):
Yet another speedup by replacing an `rsimp` proof with something else: https://github.com/leanprover/mathlib/pull/169

I like this [proof](https://github.com/spl/mathlib/blob/16c1915e22d62d29f0a2a8a15d31d93ce1372b03/order/boolean_algebra.lean#L42-L47). I think it's very readable, unlike many of my other proofs. :stuck_out_tongue_winking_eye: 

```lean
calc -x = -x ⊓ (x ⊔ y)    : by simp [s]
    ... = -x ⊓ x ⊔ -x ⊓ y : inf_sup_left
    ... = y ⊓ x ⊔ y ⊓ -x  : by simp [i, inf_comm]
    ... = y ⊓ (x ⊔ -x)    : inf_sup_left.symm
    ... = y               : by simp
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Jun 25 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/data/list/basic%20too%20big%3F/near/128605112):
I don't often write `calc` proofs, so that probably has something to do with it.

