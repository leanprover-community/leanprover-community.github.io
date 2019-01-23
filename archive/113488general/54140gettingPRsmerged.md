---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/54140gettingPRsmerged.html
---

## Stream: [general](index.html)
### Topic: [getting PRs merged](54140gettingPRsmerged.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 17 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152025635):
@**Mario Carneiro** @**Johannes Hölzl** Is there anything we can do so that a bunch of PRs get merged before the Christmas break? Merging these PRs would mean that we can spend our Christmas holidays on interesting maths stuff, instead of boring parties with food and fire crackers...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 17 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030063):
Yuchai! We're down to 29!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 17 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030287):
:o

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 17 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030337):
...and now mathlib is broken

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 17 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030342):
:o

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 17 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030494):
oh, I think it was the `squeeze_simp` PR

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 17 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030509):
@**Johan Commelin** did you actually check that your import works?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 17 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030593):
Hmm, it looked like it, but I didn't do a full compile.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 17 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030604):
Can you revert that commit?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 17 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030611):
Then I will do a more careful check.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 17 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030618):
Sorry for the mess.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Dec 17 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030659):
I think it's a cyclic import

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Dec 17 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030670):
Maybe two PRs added imports somewhere

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 17 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030803):
`tactic.squeeze` imports `meta.rb_map` which imports `data.option` which imports `tactic.interactive`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 17 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030821):
where's the cycle?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Dec 17 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030930):
`tactic.interactive` imports `tactic.squeeze`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 17 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152030940):
why would it...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 17 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152031077):
Because then it makes it a lot easier for mere mortals to squeeze their simps. Would save you a lot of work.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 17 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152032030):
@**Mario Carneiro** Do you want me to PR a reverting commit?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 17 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152032040):
no, I'm working on it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 17 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152032050):
thanks @**Mario Carneiro**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 17 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152032234):
I can make `data.option` work without `tactic.interactive`, it just used two `simpa`s

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 17 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152032244):
But there is another cycle.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 17 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152032277):
`category.traversable.instances` imports `-- import data.list.basic data.set.lattice`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 17 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152032305):
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

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 17 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152032361):
If we kick that to another file, it seems that the world would be happy again.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 17 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152032457):
Once again, I apologize for breaking stuff. I'll take this as a lesson that I shouldn't lightly PR things that are low in the dependency chain...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 17 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152032612):
Aahrg... it's even worse. `tactic.squeeze` depends on `simpa` (of course :face_palm:).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 17 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/getting%20PRs%20merged/near/152044631):
@**Mario Carneiro** Thanks for all the merges! And thanks for fixing what I broke. :thank_you: :thumbs_up: :tada:

