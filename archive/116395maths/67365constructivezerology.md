---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/67365constructivezerology.html
---

## Stream: [maths](index.html)
### Topic: [constructive zerology](67365constructivezerology.html)

---


{% raw %}
#### [ Patrick Massot (Jul 17 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129817429):
@**Kenny Lau** I have a question for you. Do you have a proof without `decidable` or `classical` of:
```lean
lemma closure_empty_iff {α : Type*} [topological_space α] [decidable_eq (set α)] (s : set α) :
closure s = ∅ ↔ s = ∅ :=
begin
  split ; intro h,
  { by_contradiction h',
    cases set.not_eq_empty_iff_exists.1 h' with _ H,
    simpa [h] using subset_closure H },
  { exact (eq.symm h) ▸ closure_empty },
end
```

#### [ Reid Barton (Jul 17 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129817776):
Use `set.eq_empty_iff_forall_not_mem` instead I think

#### [ Kenny Lau (Jul 17 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129818028):
for this case, contradiction is intuitionistically valid

#### [ Patrick Massot (Jul 17 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129818071):
Thanks Reid!

#### [ Patrick Massot (Jul 17 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129818092):
```lean
lemma closure_empty_iff {α : Type*} [topological_space α] (s : set α) :
closure s = ∅ ↔ s = ∅ :=
begin
  split ; intro h,
  { rw set.eq_empty_iff_forall_not_mem,
    intros x H,
    simpa [h] using subset_closure H },
  { exact (eq.symm h) ▸ closure_empty },
end
```

#### [ Patrick Massot (Jul 17 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129818174):
I'm very slowly working towards proving that the Hausdorff completion of a uniform space X is nonempty unless X is empty. This is no fun at all.

#### [ Patrick Massot (Jul 17 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129818681):
I can feel the dreaded spiral where I'm upset something is not obvious to Lean and I'm proving more and more stupid lemmas instead of cooling down and figure out what I exactly need

#### [ Patrick Massot (Jul 17 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129819050):
I need a break. If anyone here is bored and loves zerology, I think I may need proofs of:
```lean
lemma nonempty_iff_univ {α : Type*} : nonempty α ↔ (univ : set α) ≠ ∅ :=
sorry

lemma nonempty_of_nonempty_range {α : Type*} {β : Type*} {f : α → β} (H : ¬range f = ∅) : nonempty α :=
sorry
```

#### [ Kevin Buzzard (Jul 17 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129819486):
What am I allowed to use?

#### [ Kevin Buzzard (Jul 17 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129819498):
Excluded middle?

#### [ Kevin Buzzard (Jul 17 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129819501):
Or nothing like this?

#### [ Patrick Massot (Jul 17 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129819612):
Of course I don't care. Again, the goal is to prove the completion is empty only if the original space is empty. And this is only needed to implement Mario's trick allowing to totalize the function "lift to completion" so that any function from a uniform space to a complete Hausdorff space lifts, the lift being garbage is the function is not uniformly continuous.

#### [ Patrick Massot (Jul 17 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129819683):
But at some point we hope to put all this into mathlib, so it would be nicer to avoid unnecessary decidability assumption or classical logic

#### [ Kevin Buzzard (Jul 17 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129819773):
`nonempty` needs data for its constructor, and `(univ : set α) ≠ ∅` is only a proposition

#### [ Patrick Massot (Jul 17 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129819777):
You can have a look at https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean  to see where I stand

#### [ Patrick Massot (Jul 17 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129819790):
Mario style lifting is defined at https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L124

#### [ Kevin Buzzard (Jul 17 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129819865):
For the first one you need something like `¬ (∀ a : α, false) → ∃ a : α, true`

#### [ Patrick Massot (Jul 17 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129819870):
Maybe I should use `inhabited` instead of `nonempty`

#### [ Chris Hughes (Jul 17 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129819883):
Assuming α is nonempty, the assumption `decidable_eq (set α)` implies decidability of all propositions

#### [ Patrick Massot (Jul 17 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129819888):
Or maybe this is too much trouble, given that I already have a working lift for uniformly continuous functions

#### [ Patrick Massot (Jul 17 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129819935):
I'm upset because none of this has any mathematical content

#### [ Kevin Buzzard (Jul 17 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129820225):
```lean
lemma nonempty_iff_univ {α : Type*} : nonempty α ↔ (univ : set α) ≠ ∅ :=
begin
  split,
  { intro H,
    cases H with a,
    intro H2,
    show (∅ : set α) a,
    rw ←H2,
    trivial
  },
  intro H,
  apply classical.by_contradiction,
  intro H2,
  apply H,
  funext,
  exfalso,
  apply H2,
  exact ⟨a⟩
end 
```

#### [ Mario Carneiro (Jul 17 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129820641):
I used many of these same theorems in the proof of `dense_embedding.extend`

#### [ Mario Carneiro (Jul 17 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129820666):
for the most part I just brute forced through all of it, using `exists_mem_of_ne_empty` to get elements out of nonempty sets

#### [ Mario Carneiro (Jul 17 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129820713):
and using `mem_closure_iff` to get a nonempty set from a closure

#### [ Kevin Buzzard (Jul 17 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129821218):
```lean
lemma nonempty_of_nonempty_range {α : Type*} {β : Type*} {f : α → β} (H : ¬range f = ∅) : nonempty α :=
begin
  apply classical.by_contradiction,
  intro H2,
  apply H,
  unfold range,
  funext,
  apply propext,
  show (∃ y : α, f y = x) ↔ false,
  split,swap,exact false.elim,
  intro H3,cases H3 with a Ha,
  apply H2,
  exact ⟨a⟩
end 
```

#### [ Kevin Buzzard (Jul 17 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129821220):
What's the hurry :-)

#### [ Mario Carneiro (Jul 17 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129821261):
not so cleaned up:
```
lemma nonempty_completion_iff : nonempty (completion α) ↔ nonempty α :=
begin
  split,
  { rintro ⟨c⟩,
    have := eq_univ_iff_forall.1 (to_completion.dense α) c,
    have := mem_closure_iff.1 this _ is_open_univ trivial,
    rcases exists_mem_of_ne_empty this with ⟨_, ⟨_, a, _⟩⟩,
    exact ⟨a⟩ },
  { rintro ⟨a⟩,
    exact ⟨to_completion α a⟩ }
end
```

#### [ Patrick Massot (Jul 17 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129821269):
Many thanks to both of you!

#### [ Patrick Massot (Jul 17 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129821281):
In the mean time I saw Kevin's first lemma proof and then found some courage to write:
```lean
lemma nonempty_of_nonempty_range {α : Type*} {β : Type*} {f : α → β} (H : ¬range f = ∅) : nonempty α :=
begin
  cases exists_mem_of_ne_empty H with x h,
  cases mem_range.1 h with y _,
  exact ⟨y⟩
end
```

#### [ Kevin Buzzard (Jul 17 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129821332):
I don't know any of these lemmas which people are using :-)

#### [ Patrick Massot (Jul 17 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129821337):
I find them using lots of suffering

#### [ Patrick Massot (Jul 17 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129821344):
But now I need to understand Mario's proof

#### [ Kevin Buzzard (Jul 17 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129821346):
I never quite know whether I should somehow attempt to learn exactly what is in mathlib and where it all is

#### [ Kevin Buzzard (Jul 17 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129821369):
I'm doing a lot of work with multisets at the minute for a student, and now I really know my way around multiset.lean

#### [ Kevin Buzzard (Jul 17 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129821424):
but I don't know my way around data.set.basic in that way

#### [ Mario Carneiro (Jul 17 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129821456):
It's worth a perusal (data.set.lattice is the other important one)

#### [ Mario Carneiro (Jul 17 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129821507):
but ideally you should be able to guess beforehand what is in there

#### [ Patrick Massot (Jul 17 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129821513):
`rintro ⟨c⟩` is already a nice trick

#### [ Patrick Massot (Jul 17 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129821533):
But then I'm not sure this isn't too efficient. Don't you think `closure_empty_iff` should be in mathlib anyway?

#### [ Kevin Buzzard (Jul 17 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129821603):
I hope `rintro` isn't as slow as `rsimp`

#### [ Patrick Massot (Jul 17 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129821608):
Never noticed any slowness there

#### [ Patrick Massot (Jul 17 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129821678):
If you don't fear `rcases` then you don't fear `rintro`

#### [ Patrick Massot (Jul 17 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129821701):
and, together, they really make a difference in conciseness, without obfuscation (it's all about unpacking stuff that our mind would unpack unconsciously)

#### [ Patrick Massot (Jul 17 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129822053):
Mario, I tried to use your trick in https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/completions/src/for_mathlib/completion.lean#L124 but I needed to assume uniform continuity of `f` is decidable. Now I want to state lemmas assuming uniform continuity, but Lean asks me for an instance of `decidable (uniform_continuous f)`. Did I do it wrong? What should I do?

#### [ Mario Carneiro (Jul 17 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129822112):
since that proof uses only structural tactics, I would normally compress it into a term proof

#### [ Patrick Massot (Jul 17 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129822131):
which proof?

#### [ Mario Carneiro (Jul 17 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129822190):
the one I gave

#### [ Mario Carneiro (Jul 17 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129822230):
you should have local instance prop_decidable

#### [ Patrick Massot (Jul 17 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129822292):
Oh I will happily add that if you don't tell me this will be an issue when trying to get all this into mathlib

#### [ Patrick Massot (Jul 17 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129822318):
My original version (with unique exists!) had no such assumption, but if course it makes no difference to me

#### [ Mario Carneiro (Jul 17 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129822369):
of course cases on uniform continuity is firmly classical, but we are not working in the constructive fragment here

#### [ Patrick Massot (Jul 17 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129822444):
Nice. I should be able to move on tonight. But right now I'm too hungry, I need diner.

#### [ Patrick Massot (Jul 17 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129822446):
Thanks!

#### [ Mario Carneiro (Jul 17 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129822721):
totalizing functions often requires classical axioms

#### [ Patrick Massot (Jul 17 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129832556):
I'm done totalizing. Now I'm back exactly where I was yesterday except that, in `uniform_space.completion_lift f`, `f` is now a function rather than a proof that a function is uniformly continuous. In particular fonctoriality now reads `completion_lift (g ∘ f) = (completion_lift g) ∘ completion_lift f`, as it should

#### [ Patrick Massot (Jul 17 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129832572):
All this for the cheap price of a few hours and a `local attribute [instance] classical.prop_decidable`

#### [ Patrick Massot (Jul 17 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/constructive%20zerology/near/129832630):
And I can see wisdom is coming to Kenny. He didn't write anything about that last classical detail.


{% endraw %}
