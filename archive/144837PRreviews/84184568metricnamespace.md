---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/84184568metricnamespace.html
---

## Stream: [PR reviews](index.html)
### Topic: [#568 metric namespace](84184568metricnamespace.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Jan 13 2019 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23568%20metric%20namespace/near/155045224):
After Mario's alternative proposition for the metric namespace, I fixed the build. The following line in `normed_space.lean`
```lean
by simpa using tendsto_mul limf' limg',
```
became a timeout. I can fix the build by replacing this line with
```lean
{ have := tendsto_mul limf' limg',
  simp at this,
  exact this },
```
(which should be essentially equivalent if I understand what `simpa` does) but this is not really satisfactory.

If I understand what is going on, the problem is that I have a fact `limg' : tendsto (λ (x : γ), ∥g x∥) e (nhds ∥b∥)` in the context. The `simpa` call tries to close the goal using `by assumption`, which tries all the things in the context to close the goal. In particular, it tries `limg'`, but the unifier is not able to realize that it does not match the goal, and times out while trying. Indeed, if I replace the last line `exact this` with `exact limg'`, I get a timeout.

My guess is that the namespace change has changed the order in which things are tried by `by assumption` (alphabetical order or something?): before the change, `limg'` was tried after `this` and everything went smoothly, and now this is not the case any more, but only by accident. It seems to me that the change only reveals a problem that was already there before.

Mario has already written on this chat that `by assumption`is not always safe, and this is another instance. Is there anything to be done here (marking something as irreducible somewhere?), or should we just accept this as a fact of life?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 13 2019 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23568%20metric%20namespace/near/155045311):
`clear limg'` first. A long term solution is to stop assumption unfolding things quite as aggressively, I think it even unfold irreducibles at the moment.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 13 2019 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23568%20metric%20namespace/near/155045370):
Why does the `using` form of `simpa` need to use assumption though? Shouldn't it just use `exact`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 13 2019 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23568%20metric%20namespace/near/155045432):
I see it is documented that it uses `assumption`, but I don't understand the purpose--surely we always want to use the thing specified with `using` when it is present

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Jan 13 2019 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23568%20metric%20namespace/near/155045449):
I can not clear `limg'`, I need it below. Replacing one line by three lines is not too bad, as a workaround, but fixing `simpa` or `assumption` would definitely be better.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Jan 13 2019 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23568%20metric%20namespace/near/155045580):
```quote
I see it is documented that it uses `assumption`, but I don't understand the purpose--surely we always want to use the thing specified with `using` when it is present
```
 My guess is that it is for implementation purposes: it makes it possible to use the same code for the versions with and without `using`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 13 2019 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23568%20metric%20namespace/near/155045703):
I'll try to make it use the provided term to close the goal and see whether it breaks everything.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 13 2019 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23568%20metric%20namespace/near/155045718):
I guess you could probably use `have lim1 : tendsto (λ x, ∥f x - s∥ * ∥g x∥) e (nhds 0) := (zero_mul ∥b∥) ▸ tendsto_mul limf' limg', ` but this is very annoying. I think that every single time I used `tendsto_add` or `tendsto_mul` I was frustrated by having to care about such trivial computation, either explicitly or using `simp`. It probably means we need a limit computation tactic.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Jan 13 2019 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23568%20metric%20namespace/near/155045954):
A one-liner, yeah!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Jan 13 2019 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23568%20metric%20namespace/near/155046024):
Normally, `back` (together with marking most limit lemmas with, say, `limit_rules`) should make limits much less painful, but it will not work before Lean 4 as `apply` unfolds too much...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 13 2019 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23568%20metric%20namespace/near/155046081):
It should still be possible to write some tactic, even in Lean 3, but I have too much to do. For instance I need to prepare a lecture for tomorrow  morning...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 13 2019 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23568%20metric%20namespace/near/155046281):
I think `clear` only clears for the current goal, so it should be possible to use it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 13 2019 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23568%20metric%20namespace/near/155046969):
@**Sebastien Gouezel** , try with https://github.com/leanprover-community/mathlib/tree/rwbarton-simpa?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastien Gouezel (Jan 13 2019 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23568%20metric%20namespace/near/155048122):
Works like a charm! And it should be a definitive improvement on all points on view, including clarity (the proof in padics you had to fix was probably a mistake) and speed (no need to check everything in the context).

