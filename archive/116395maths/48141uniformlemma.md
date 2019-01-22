---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/48141uniformlemma.html
---

## [maths](index.html)
### [uniform lemma](48141uniformlemma.html)

#### [Patrick Massot (Jul 14 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform lemma/near/129677243):
Is the following lemma already hidden somewhere in mathlib? Or is it too trivial to be stated? What would be his canonical name?
```lean
import analysis.topology.uniform_space

local attribute [instance] separation_setoid

variables {α : Type*} [uniform_space α]
variables {β : Type*} [uniform_space β]

lemma separation_rel_of_uniform_continuous {f : α → β} (H : uniform_continuous f) {x y : α} 
(h : x ≈ y) : f x ≈ f y :=
assume _ h', h _ (H h')
```

#### [Patrick Massot (Jul 14 2018 at 23:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform lemma/near/129677487):
Same question for the obvious corollary
```lean
lemma image_eq_of_uniform_continuous_of_separated [separated β] {f : α → β} (H : uniform_continuous f) {x y : α} 
(h : x ≈ y) : f x = f y :=
separated_def.1 (by apply_instance) _ _ $ separation_rel_of_uniform_continuous H h
```

#### [Patrick Massot (Jul 14 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform lemma/near/129677492):
@**Mario Carneiro** I know this is Johannes domain, but I'd be interested in your opinion about naming here

#### [Mario Carneiro (Jul 15 2018 at 04:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform lemma/near/129684119):
That's a tough one. I don't like the use of the word `image` in the second one, that connotes `''` but it doesn't appear in the statement

#### [Mario Carneiro (Jul 15 2018 at 04:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform lemma/near/129684167):
Maybe `apply_eq_of_separated` for the second?

#### [Patrick Massot (Jul 15 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform lemma/near/129696241):
Ok. It leaves out most of the statement but I don't see how to avoid that when there are so many hypotheses.

#### [Johannes Hölzl (Jul 15 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform lemma/near/129699884):
I think `separated_of_uniform_continuous` and `eq_of_separated_of_uniform_continuous` would be also okay.

#### [Patrick Massot (Jul 15 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform lemma/near/129700368):
Thanks. I now use these names since you will have to review a PR containing all this at some point.

#### [Patrick Massot (Jul 15 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform lemma/near/129701065):
Now, for something really weird, I'll try to go read Bourbaki GT in a bar, hoping this will secure me some place to watch the game. It may be too late already.

#### [Patrick Massot (Jul 15 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform lemma/near/129701130):
Maybe  I should point out that my wife and kids are in vacations, so I'm alone at home. Otherwise I wouldn't do that :-)

#### [Kenny Lau (Jul 15 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform lemma/near/129701134):
I think every mathematician should read Bourbaki in a bar

#### [Patrick Massot (Jul 15 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform lemma/near/129710662):
It worked out pretty nicely. Now I know what are the supporting lemmas that I need to prove about completions.

#### [Patrick Massot (Jul 15 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/uniform lemma/near/129710670):
Kenny, reading and doing math in bar is very standard, what was slightly weird was the atmosphere around me. But I was able to mostly work until about 15 minutes before the beginning.

