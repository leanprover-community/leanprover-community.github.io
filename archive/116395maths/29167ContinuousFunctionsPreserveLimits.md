---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/29167ContinuousFunctionsPreserveLimits.html
---

## Stream: [maths](index.html)
### Topic: [Continuous Functions Preserve Limits](29167ContinuousFunctionsPreserveLimits.html)

---

#### [Rohan Mitta (Sep 26 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134671259):
Is this in mathlib (or anything like this)? 

```lean
import analysis.metric_space 
import order.filter
example {X : Type*} {Y : Type*} [metric_space X] [metric_space Y] (f : X → Y) (H1 : continuous f) (seq : ℕ → X) 
  (a : X) (H : filter.tendsto seq filter.at_top (nhds a)) : filter.tendsto (f ∘ seq) filter.at_top (nhds (f a))
  := sorry
```

#### [Johannes Hölzl (Sep 26 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134671293):
this doesn't hold. `f` needs to be continuous at `a`

#### [Kevin Buzzard (Sep 26 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134671306):
he's just editing :-)

#### [Rohan Mitta (Sep 26 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134671321):
Sorry I've just updated it with continuous f

#### [Johannes Hölzl (Sep 26 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134671367):
otherwise it is composition of `continuous.tendsto`, `tendsto.comp` and `H`

#### [Kevin Buzzard (Sep 26 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134671383):
Thanks again Johannes. I've never used this stuff before.

#### [Kevin Buzzard (Sep 26 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134671392):
so all I do is offer encouragement and tell Rohan to ask his questions here :-) [he's sitting next to me]

#### [Johannes Hölzl (Sep 26 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134671475):
hehe, peer proving

#### [Johannes Hölzl (Sep 26 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134671498):
But this lemma is the reason why we use filters. We can express a lot of things as filters, and then just compose them

#### [Kevin Buzzard (Sep 26 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134671516):
I encourage Rohan to formalise precisely the statement he needs and ask it here. I think that's a good way of learning how to think about Lean.

#### [Kevin Buzzard (Sep 26 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134671528):
He's almost proved the contraction mapping theorem, this is just the last bit.

#### [Kevin Buzzard (Sep 26 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134671615):
I could see it was going to follow from standard filter stuff, I just don't yet know how to drive filters. I am all over the road.

#### [Rohan Mitta (Sep 26 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134671746):
Brilliant, that worked!

#### [Patrick Massot (Sep 26 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134672107):
For those reading without typing: the proof that Rohan wanted is `tendsto.comp H (H1.tendsto a)` This is the point of filters: the limit lemmas don't care whether you take the limit of a sequence at infinity, the limit of a function at a point or whatever

#### [Patrick Massot (Sep 26 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134672226):
Extra tip for Rohan: `f`, `seq` and `a` can be implicit arguments, they can be inferred from `H` and `H1` by unification

#### [Patrick Massot (Sep 26 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134672326):
a last one: your assumptions that `X` and `Y` are metric spaces are useless. You can replace them by `topological_space` without changing anything else

#### [Patrick Massot (Sep 26 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134672489):
Note also that the proof is much shorter than the statement, and very easy to remember, so the final tip may be to erase the lemma...

#### [Kevin Buzzard (Sep 26 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134672534):
`tendsto (λ (n : ℕ), n + 1) at_top at_top`

#### [Kevin Buzzard (Sep 26 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134672542):
We're so close :-)

#### [Kevin Buzzard (Sep 26 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134672559):
Do I have to actually unravel things here?

#### [Patrick Massot (Sep 26 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134673138):
I did the beginning up to the point where I hate those things:
```lean
example : tendsto (λ (n : ℕ), n + 1) at_top at_top :=
begin
  intros s s_in,
  rw mem_at_top_sets at s_in,
  cases s_in with a h, 
  rw [mem_map, mem_at_top_sets],
  existsi a, 
  intros b H,
  change b+1 ∈ s,
  apply h,
  sorry
end
```

#### [Patrick Massot (Sep 26 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134673171):
State is now ` b ≥ a ⊢ b + 1 ≥ a`

#### [Patrick Massot (Sep 26 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134673260):
Of course the `change` in the middle is purely psychological, you can remove it

#### [Patrick Massot (Sep 26 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134673463):
Full proof is
```lean
example : tendsto (λ (n : ℕ), n + 1) at_top at_top :=
begin
  intros s s_in,
  rw mem_at_top_sets at s_in,
  cases s_in with a h, 
  rw [mem_map, mem_at_top_sets],
  existsi a, 
  intros b H,
  exact h _ (le_trans H (nat.le_succ b))
end
```

#### [Kenny Lau (Sep 26 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134673487):
try `constructor`

#### [Patrick Massot (Sep 26 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134673511):
@**Simon Hudon** I guess this is yet another test for mono

#### [Patrick Massot (Sep 26 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134673602):
Kenny, this works but it's even more ridiculous

#### [Patrick Massot (Sep 26 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134673625):
The only acceptable answer here is a finishing tactic (mono should do the trick)

#### [Rob Lewis (Sep 26 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134673662):
`linarith` should work too.

#### [Patrick Massot (Sep 26 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134673672):
true

#### [Patrick Massot (Sep 26 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134673741):
It does!

#### [Patrick Massot (Sep 26 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134673758):
And it's already in mathlib

#### [Patrick Massot (Sep 26 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134673780):
Do we have the contraction mapping theorem then?

#### [Patrick Massot (Sep 26 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134673899):
That being said, this proof is still too handcrafted. We should prove a lemma saying that the identity of a linearly_ordered type goes to top at top, and then use a version of squeeze

#### [Rohan Mitta (Sep 26 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134674225):
I've just finished a very long proof of 

```lean
theorem Banach_fixed_point {α : Type*} [metric_space α] [complete_space α] (H1 : nonempty α) {f : α → α} (H : is_contraction f)
: ∃! (p : α), f p = p := sorry
```

#### [Patrick Massot (Sep 26 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134674398):
Now you can try to break it into ten lemmas

#### [Patrick Massot (Sep 26 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134674664):
I need to go and do real work, but I'll be happy to read your proof once it's available

#### [Kenny Lau (Sep 26 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134675116):
```lean
import order.filter

open filter

example : tendsto (λ (n : ℕ), n + 1) at_top at_top :=
begin
  intros s,
  rw [mem_at_top_sets, mem_map_sets_iff],
  rintro ⟨N, h1⟩,
  refine ⟨{b | b ≥ N}, mem_at_top_sets.2 ⟨_, λ _, id⟩, _⟩,
  rintro n ⟨k, h2, h3⟩, subst h3,
  apply h1,
  constructor,
  exact h2
end
```

#### [Kevin Buzzard (Sep 26 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134675982):
```lean
example (X : Type*) (f : ℕ → X) (F : filter X) (H : tendsto f at_top F) :
tendsto (λ n, f (n + 1)) at_top F :=
tendsto.comp (tendsto_def.2 $ λ U HU,
  let ⟨a,Ha⟩ := mem_at_top_sets.1 HU in 
  mem_at_top_sets.2 ⟨a,λ x Hx,Ha _ $ le_trans Hx $ by simp⟩) H
```

#### [Kevin Buzzard (Sep 26 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134676038):
```lean
example : tendsto (λ (n : ℕ), n + 1) at_top at_top :=
tendsto_def.2 $ λ U HU,
  let ⟨a,Ha⟩ := mem_at_top_sets.1 HU in 
  mem_at_top_sets.2 ⟨a,λ x Hx,Ha _ $ le_trans Hx $ by simp⟩
```

#### [Kevin Buzzard (Sep 26 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134677014):
https://github.com/ImperialCollegeLondon/xena-UROP-2018/blob/master/src/Topology/Material/banach_contraction.lean

#### [Kevin Buzzard (Sep 26 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134677027):
He's pushed!

#### [Kevin Buzzard (Sep 26 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134677164):
rofl he has the vmap version of filter so it doesn't compile for me :-) I'll fix it. @**Rohan Mitta** I'm editing your file so that it compiles with the most recent mathlib

#### [Kevin Buzzard (Sep 26 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134677333):
*rofl* there's still a sorry! Rohan I think you hadn't saved before you pushed :-) OK so the current state of the contraction mapping theorem is that the only finished version is on a laptop owned by an undergraduate who has just gone off to prepare a treasure hunt for Fresher's week.

#### [Rohan Mitta (Sep 26 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134683456):
Okay whoops, I've saved and pushed again. Hopefully its all there now?

#### [Patrick Massot (Sep 26 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Continuous%20Functions%20Preserve%20Limits/near/134684774):
Congratulations Rohan!

