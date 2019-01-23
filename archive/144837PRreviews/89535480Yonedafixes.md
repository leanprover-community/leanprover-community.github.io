---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/89535480Yonedafixes.html
---

## Stream: [PR reviews](index.html)
### Topic: [#480 Yoneda fixes](89535480Yonedafixes.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 28 2018 at 04:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23480%20Yoneda%20fixes/near/148686856):
Travis seems to be screwing something up with https://github.com/leanprover/mathlib/pull/480. It’s complaining about invalid imports in files that aren’t even in this PR anymore. @**Mario Carneiro**, are you able to reset it somehow?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 28 2018 at 04:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23480%20Yoneda%20fixes/near/148687461):
@**Scott Morrison|110087** have you tried clearing the cache for that branch? I think I can do it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 28 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23480%20Yoneda%20fixes/near/148687515):
Ah, I thought only some people could do that. If you see how to do it, teach me. :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 28 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23480%20Yoneda%20fixes/near/148687524):
https://travis-ci.org/leanprover-community/mathlib/caches

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 28 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23480%20Yoneda%20fixes/near/148687526):
And just click the lil bin

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 28 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23480%20Yoneda%20fixes/near/148687529):
I retriggered a build

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 28 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23480%20Yoneda%20fixes/near/148687531):
after

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 28 2018 at 04:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23480%20Yoneda%20fixes/near/148687643):
We can because everything is really on mathlib-community, which we can push to

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 28 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23480%20Yoneda%20fixes/near/148692162):
Thanks @**Keeley Hoek**. Curiously this doesn't seem to have fixed the PR, however. :-(

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 28 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23480%20Yoneda%20fixes/near/148692163):
Ah yes
But it did build successfully
https://travis-ci.org/leanprover-community/mathlib/builds/460592170

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 28 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23480%20Yoneda%20fixes/near/148692164):
I was wrong about it updating the thingo for the main repo though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 28 2018 at 07:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23480%20Yoneda%20fixes/near/148692210):
Okay, I'll just push a whitespace change and see if that fixes things.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 28 2018 at 07:58)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23480%20Yoneda%20fixes/near/148693645):
@**Mario Carneiro** could you restart the build for #480 on travis? I've tried deleting caches, force pushing again, etc. but it won't rebuild and the error message is nonsense (because of the cache).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 28 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23480%20Yoneda%20fixes/near/148696110):
Ok, this is ready.
It just does two small things: a few lemmas about
```
def ulift_functor : (Type u) ⥤ (Type (max u v))
```
and states as a separate lemma the componentwise version of the Yoneda lemma:
```
@[simp] def yoneda_sections (X : C) (F : Cᵒᵖ ⥤ Type v₁) : (yoneda.obj X ⟹ F) ≅ ulift.{u₁} (F.obj X)
```
Oh -- and adds the definition of `representable`, which will be needed shortly for the limits PRs.


{% endraw %}
