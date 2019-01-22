---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/63203updatingvectors.html
---

## [new members](index.html)
### [updating vectors](63203updatingvectors.html)

#### [Marcus Klaas (Dec 11 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/updating vectors/near/151447262):
Hi! Can anyone provide some pointers here? I'm trying to define a function that updates a vector at a given index. This seems to work, but it's very unwieldy:
```lean
def update_nth {n : ℕ} {α : Type} : vector α n → fin n → α → vector α n
| v i a := vector.map₂ (λ b idx, if idx = i then a else b) v $ vector.of_fn id
```

In particular, proving elementary lemmas on it seems near impossible:
```lean
lemma update_nth_helper {n : ℕ} {α : Type} (v : vector α n) (i : fin n) (a b : α)
    : vector.cons b (update_nth v i a) = update_nth (vector.cons b v) (fin.succ i) a :=
sorry
```

I'd like to provide a recursive definition, but I can't get it to work. Lean seems to think `n` is fixed.

Any tips on best approach here?

#### [Mario Carneiro (Dec 11 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/updating vectors/near/151447862):
another way to define that function is using `vector.nth` with `vector.of_fn`

#### [Mario Carneiro (Dec 11 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/updating vectors/near/151447871):
or by referring to `list.update_nth`

#### [Marcus Klaas (Dec 11 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/updating vectors/near/151447990):
ooh, there is a `list.update_nth`? hadn't seen that! thanks!

#### [Mario Carneiro (Dec 11 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/updating vectors/near/151447994):
as for `n` fixed, that happens when you put it left of the colon

#### [Marcus Klaas (Dec 11 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/updating vectors/near/151448014):
I'd like to put it right of the colon, but then I cannot name it any more, correct?

#### [Mario Carneiro (Dec 11 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/updating vectors/near/151448021):
sure you can

#### [Marcus Klaas (Dec 11 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/updating vectors/near/151448026):
and almost all other arguments depend on it :o

#### [Marcus Klaas (Dec 11 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/updating vectors/near/151448036):
oh wow

#### [Marcus Klaas (Dec 11 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/updating vectors/near/151448050):
i feel silly now

#### [Marcus Klaas (Dec 11 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/updating vectors/near/151448115):
can u provide 1 more hint on how `vector.nth` + `vector.of_fn` would work?

#### [Marcus Klaas (Dec 11 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/updating vectors/near/151448713):
`list.update_nth` worked beautifully btw - thanks a million mario!

#### [Rob Lewis (Dec 11 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/updating vectors/near/151448913):
I guess Mario might have been thinking of something like `vector.of_fn (λ k, if k = n then a else v.nth k)`.

#### [Rob Lewis (Dec 11 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/updating vectors/near/151448958):
Depending on your application here, you might consider using `array` instead of `vector`.

#### [Marcus Klaas (Dec 11 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/updating vectors/near/151449413):
:O

#### [Marcus Klaas (Dec 11 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/updating vectors/near/151449421):
what's the trade-off?

#### [Mario Carneiro (Dec 11 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/updating vectors/near/151449598):
array is already basically functions from `fin n`

#### [Mario Carneiro (Dec 11 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/updating vectors/near/151449663):
it's also more efficient for computational purposes, dunno if that matters

#### [Mario Carneiro (Dec 11 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/updating vectors/near/151449711):
plus this function already exists on `array`, it's called `array.write` and it's the most basic array function (everything else is in terms of it) so you should be in a good place wrt lemmas

#### [Marcus Klaas (Dec 11 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/updating vectors/near/151449741):
i like that

#### [Marcus Klaas (Dec 11 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/updating vectors/near/151449751):
thanks a bunch folks!

#### [Marcus Klaas (Dec 11 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/updating vectors/near/151449887):
can't wait to see your presentation on p-adic numbers this thursday btw @**Rob Lewis** :-)

#### [Rob Lewis (Dec 11 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/updating vectors/near/151450160):
Hmm, yeah, I should finish those slides at some point.

#### [Marcus Klaas (Dec 11 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/updating vectors/near/151450283):
^^

