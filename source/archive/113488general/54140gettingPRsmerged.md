---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/54140gettingPRsmerged.html
---

## [general](index.html)
### [getting PRs merged](54140gettingPRsmerged.html)

#### [Johan Commelin (Dec 17 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152025635):
@**Mario Carneiro** @**Johannes Hölzl** Is there anything we can do so that a bunch of PRs get merged before the Christmas break? Merging these PRs would mean that we can spend our Christmas holidays on interesting maths stuff, instead of boring parties with food and fire crackers...

#### [Johan Commelin (Dec 17 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030063):
Yuchai! We're down to 29!

#### [Kenny Lau (Dec 17 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030287):
:o

#### [Mario Carneiro (Dec 17 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030337):
...and now mathlib is broken

#### [Kenny Lau (Dec 17 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030342):
:o

#### [Mario Carneiro (Dec 17 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030494):
oh, I think it was the `squeeze_simp` PR

#### [Mario Carneiro (Dec 17 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030509):
@**Johan Commelin** did you actually check that your import works?

#### [Johan Commelin (Dec 17 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030593):
Hmm, it looked like it, but I didn't do a full compile.

#### [Johan Commelin (Dec 17 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030604):
Can you revert that commit?

#### [Johan Commelin (Dec 17 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030611):
Then I will do a more careful check.

#### [Johan Commelin (Dec 17 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030618):
Sorry for the mess.

#### [Chris Hughes (Dec 17 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030659):
I think it's a cyclic import

#### [Chris Hughes (Dec 17 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030670):
Maybe two PRs added imports somewhere

#### [Mario Carneiro (Dec 17 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030803):
`tactic.squeeze` imports `meta.rb_map` which imports `data.option` which imports `tactic.interactive`

#### [Kenny Lau (Dec 17 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030821):
where's the cycle?

#### [Chris Hughes (Dec 17 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030930):
`tactic.interactive` imports `tactic.squeeze`

#### [Kenny Lau (Dec 17 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030940):
why would it...

#### [Johan Commelin (Dec 17 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152031077):
Because then it makes it a lot easier for mere mortals to squeeze their simps. Would save you a lot of work.

#### [Johan Commelin (Dec 17 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152032030):
@**Mario Carneiro** Do you want me to PR a reverting commit?

#### [Mario Carneiro (Dec 17 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152032040):
no, I'm working on it

#### [Kenny Lau (Dec 17 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152032050):
thanks @**Mario Carneiro**

#### [Johan Commelin (Dec 17 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152032234):
I can make `data.option` work without `tactic.interactive`, it just used two `simpa`s

#### [Johan Commelin (Dec 17 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152032244):
But there is another cycle.

#### [Johan Commelin (Dec 17 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152032277):
`category.traversable.instances` imports `-- import data.list.basic data.set.lattice`

#### [Johan Commelin (Dec 17 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152032305):
It needs those for
```lean
lemma mem_traverse {f : α' → set β'} :
  ∀(l : list α') (n : list β'), n ∈ traverse f l ↔ forall₂ (λb a, b ∈ f a) n l
| []      []      := by simp
| (a::as) []      := by simp; exact assume h, match h with end
| []      (b::bs) := by simp
| (a::as) (b::bs) :=
  suffices (b :: bs : list β') ∈ traverse f (a :: as) ↔ b ∈ f a ∧ bs ∈ traverse f as,
    by simpa [mem_traverse as bs],
  iff.intro
    (assume ⟨_, ⟨b, hb, rfl⟩, _, hl, rfl⟩, ⟨hb, hl⟩)
    (assume ⟨hb, hl⟩, ⟨_, ⟨b, hb, rfl⟩, _, hl, rfl⟩)
```

#### [Johan Commelin (Dec 17 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152032361):
If we kick that to another file, it seems that the world would be happy again.

#### [Johan Commelin (Dec 17 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152032457):
Once again, I apologize for breaking stuff. I'll take this as a lesson that I shouldn't lightly PR things that are low in the dependency chain...

#### [Johan Commelin (Dec 17 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152032612):
Aahrg... it's even worse. `tactic.squeeze` depends on `simpa` (of course :face_palm:).

#### [Johan Commelin (Dec 17 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152044631):
@**Mario Carneiro** Thanks for all the merges! And thanks for fixing what I broke. :thank_you: :thumbs_up: :tada:

