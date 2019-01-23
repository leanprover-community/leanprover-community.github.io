---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/46635Problemwithloopingoverfinset.html
---

## Stream: [general](index.html)
### Topic: [Problem with looping over finset](46635Problemwithloopingoverfinset.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) AHan (Jan 15 2019 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problem%20with%20looping%20over%20finset/near/155177808):
Given `s : finset ℕ`,  how can I construct `s' : finset (ℕ × ℕ)` s.t.  `∀ a b,  a b ∈ s ↔ (a, b) ∈ s'` ?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problem%20with%20looping%20over%20finset/near/155178216):
I think what you wrote doesn't type-check

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problem%20with%20looping%20over%20finset/near/155178295):
I assume the `a b` means `a * b`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problem%20with%20looping%20over%20finset/near/155178398):
aren't you busy merging https://github.com/leanprover/mathlib/pull/583?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problem%20with%20looping%20over%20finset/near/155178422):
Seriously I'd never thought of that interpretation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) AHan (Jan 15 2019 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problem%20with%20looping%20over%20finset/near/155178633):
I mean looping over s, and  do something with every two distinct element in s.
(Sorry for my bad English, don't know how to express this well...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problem%20with%20looping%20over%20finset/near/155178829):
what are you trying to do in your loop? lean doesn't have "looping constructs" as such

#### [![Click to go to Zulip](../../assets/img/zulip2.png) AHan (Jan 15 2019 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problem%20with%20looping%20over%20finset/near/155179031):
if with `list` I can do something like 
```lean
variables {α : Type*}

def test (s : list ℕ) : list ℕ := 
do 
    x <- s,
    y <- s,
    [x + y]
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) AHan (Jan 15 2019 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problem%20with%20looping%20over%20finset/near/155179136):
I'm just wondering how to do this in if the given type is finset

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problem%20with%20looping%20over%20finset/near/155179162):
the left arrow is just notation for `list.bind`, you can call `finset.bind` and it's just the same

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 15 2019 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problem%20with%20looping%20over%20finset/near/155179221):
I guess there is a missing monad instance for `finset` that would allow you to use the same notation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) AHan (Jan 15 2019 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Problem%20with%20looping%20over%20finset/near/155179484):
Oh! Thanks a lot !!


{% endraw %}
