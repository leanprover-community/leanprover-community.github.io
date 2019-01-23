---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/55725boundedquantifiers.html
---

## Stream: [general](index.html)
### Topic: [bounded quantifiers](55725boundedquantifiers.html)

---


{% raw %}
#### [ Sean Leather (Apr 26 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125723227):
I've seen these referred to in different places. I've inferred that a bounded forall is `{α : Sort*} {p : α → Prop} : ∀ x, p x` and a bounded exists is `{α : Sort*} {p : α → Prop} : ∃ x, p x`. In some places, they're called `ball` and `bex`. In `mathlib/docs/naming.md` (only, it appears), they are called `bforall` and `bexists`.

There is also notation `∀ x ∈ s, t` that refers to a bounded forall and produces `∀ (x : α), x ∈ s → t`. It works similarly for exists. In [`lean/tests/lean/run/cute_binders.lean`](https://github.com/leanprover/lean/blob/f59c2f0ef59fdc1833b6ead6adca721123bd7932/tests/lean/run/cute_binders.lean), there is even this rather interesting code:

```lean
definition range (lower : nat) (upper : nat) : set nat :=
λ a, lower ≤ a ∧ a ≤ upper

local notation `[` L `, ` U `]` := range L U

variables s : set nat
variables p : nat → nat → Prop

-- #check a ∈ s
set_option pp.binder_types true
#check ∀ b c a ∈ s, a + b + c > 0
-- ∀ (b c a : ℕ), b ∈ s → c ∈ s → a ∈ s → a + b + c > 0 : Prop
#check ∀ a < 5, p a (a+1)
-- ∀ (a : ℕ), a < 5 → p a (a + 1) : Prop
#check ∀ a b ∈ [2, 3], p a b
-- ∀ (a b : ℕ), a ∈ [2, 3] → b ∈ [2, 3] → p a b
```

So, to my questions: Where is this bounded quantifier notation defined? Does it work wherever `binders` is found in `notation`? What are its limitations, e.g. w.r.t. the `p : α → Prop` or notation (`∈`, `<`, etc.) used?

#### [ Simon Hudon (Apr 26 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125723696):
I think as you suggest, it's baked into the `binder` notation. I'm actually unclear on what is accepted. I think it might accept any infix operator: `∀ x ⊕ unit, list x`

#### [ Patrick Massot (Apr 26 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125723790):
OMG, I never understood all these "ball". I always thought: "What ball? There is no distance here, why is this called ball?"

#### [ Sean Leather (Apr 26 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125723909):
```quote
OMG, I never understood all these "ball". I always thought: "What ball? There is no distance here, why is this called ball?"
```
Part of the motivation for writing this up was also to help others who were as confused as I was. :simple_smile:

#### [ Patrick Massot (Apr 26 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125724000):
My only excuse is I was seeing this in contexts not too far away from actual balls, like https://github.com/leanprover/mathlib/blob/14a19bf3d2589a9801ef281808d8e4faa90db2b1/data/analysis/topology.lean#L88 which is about topological space but not metric spaces, hence maximising the confusion probability

#### [ Patrick Massot (Apr 26 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125725893):
Sean, what's that orange thing next to the small mathematician in your reaction?

#### [ Sean Leather (Apr 26 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125726857):
A b(ounded for)all. :soccer:

#### [ Johan Commelin (Apr 26 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125732320):
```quote
Sean, what's that orange thing next to the small mathematician in your reaction?
```
If you hover over the emoji with your mouse, a popup will explain what the emoji tries to communicate (-;

#### [ Sean Leather (Apr 30 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125884559):
As Mario [pointed out](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/subject/property.20applies.20to.20all.20elements.20of.20list/near/125884401) to me, there are yet more names for bounded quantifiers: `forall_mem` and `exists_mem`. These are used in (at least) `data/list/basic.lean`, `data/finset.lean`, and `data/multiset.lean`.

#### [ Sean Leather (Apr 30 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125884625):
Arguably, `forall_mem` is more accurate than `ball` because it explicitly describes the `mem` bound of the quantification.

#### [ Mario Carneiro (Apr 30 2018 at 10:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125884752):
There is a reasonable argument for `ball_mem` instead of `forall_mem` since it is a mem bound on a bounded forall, but that's like half overlapping names and a direct reading looks more like `forall_mem`

#### [ Mario Carneiro (Apr 30 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125884797):
Currently, `ball` and `bex` are only used to describe "generic" bounded forall (some predicate) in `logic.basic`

#### [ Sean Leather (Apr 30 2018 at 10:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125884798):
I actually like `forall_mem` for the reason you said.

#### [ Sean Leather (Apr 30 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125884911):
The lack of `forall` in `ball` and `exists` in `bex` means that they don't show up in `grep`, which is unfortunate for those of us who rely on old-school tools. :wink:

#### [ Johan Commelin (Apr 30 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125884914):
```quote
those of us who rely on old-school tools. :wink:
```
Yes, I'm still looking for a Lean plugin for good old `ed`

#### [ Sean Leather (Apr 30 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125884964):
And a punched card computer that supports UTF-8?

#### [ Mario Carneiro (Apr 30 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125885027):
The obvious solution is to shorten `forall` and `exists` to `all` and `ex` :)

#### [ Sean Leather (Apr 30 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125885086):
```quote
The obvious solution is to shorten `forall` and `exists` to `all` and `ex` :)
```
That would be `totally` `canonically` `exact`in the `next` `contextual` `parallel` universe that `extends` this one.

#### [ Mario Carneiro (Apr 30 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125885189):
There's no way I'm going to try and avoid subsequences

#### [ Mario Carneiro (Apr 30 2018 at 10:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125885191):
If you kick vscode enough times it shows prefixes only

#### [ Johan Commelin (Apr 30 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125885205):
Fair enough, we can grep with word boundaries

#### [ Sean Leather (Apr 30 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125885407):
Tee hee, yet more names. `forall_prop` and `exists_prop` in `data/list.lean`:

```lean
theorem all_iff_forall_prop {p : α → Prop} [decidable_pred p] {l} : all l (λ a, p a) ↔ ∀ a ∈ l, p a

theorem any_iff_exists_prop {p : α → Prop} [decidable_pred p] {l} : any l (λ a, p a) ↔ ∃ a ∈ l, p a
```

which are actually used differently in `logic/basic.lean`:

```lean
theorem forall_prop_of_true {p : Prop} {q : p → Prop} (h : p) : (∀ h' : p, q h') ↔ q h
theorem forall_prop_of_false {p : Prop} {q : p → Prop} (hn : ¬ p) : (∀ h' : p, q h') ↔ true

theorem exists_prop {p q : Prop} : (∃ h : p, q) ↔ p ∧ q
theorem exists_prop_of_true {p : Prop} {q : p → Prop} (h : p) : (∃ h' : p, q h') ↔ q h
theorem exists_prop_of_false {p : Prop} {q : p → Prop} : ¬ p → ¬ (∃ h' : p, q h')
```

#### [ Mario Carneiro (Apr 30 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125885859):
the `prop` in `all_iff_forall_prop` is only there for disambiguation, it could just be `all_iff_forall'` which is marginally less descriptive

#### [ Mario Carneiro (Apr 30 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125885877):
Maybe it should be called `all_to_bool` instead, since there is a hidden `to_bool` coercion there

#### [ Sean Leather (Apr 30 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125885971):
But then it seems that `all_iff_forall` should be called `all_iff_forall_mem` to be consistent with the other `forall_mem`s.

#### [ Sean Leather (Apr 30 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125885977):
So you'd have `all_iff_forall_mem` and `all_iff_forall_mem'`.

#### [ Sean Leather (Apr 30 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125885986):
Or even `all_iff_forall_bool` and `all_iff_forall_mem`?

#### [ Mario Carneiro (Apr 30 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125885990):
true, although I reserve the right to start lopping off the right hand side of a theorem name if we all know where it's going

#### [ Kevin Buzzard (Apr 30 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125887758):
```quote
The obvious solution is to shorten `forall` and `exists` to `all` and `ex` :)
```
Let me just make the passing comment that there was a time a few months ago when Mario stopped what he was doing and wrote a bunch of one-line docstrings covering many of the important concepts in mathlib, and after that I found that old-skool grepping suddenly became a lot more effective.

#### [ Kevin Buzzard (Apr 30 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125887801):
For example, I once wanted to know whether surjections were covered in Lean, and I grepped the Lean source code for "surjection" and got nothing at all.

#### [ Kevin Buzzard (Apr 30 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125887805):
then after the docstrings, I grepped again and I found the word in a docstring and then I looked at the correponding theorem and found my mistake -- it's "surjective" I should be looking for.

#### [ Kevin Buzzard (Apr 30 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125887812):
so a better solution is to put the keywords in the docs :-)

#### [ Sean Leather (Apr 30 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125888856):
```quote
so a better solution is to put the keywords in the docs :-)
```
Yes, that is useful in general. But a consistent naming scheme that allows one to consistently associate names with concepts is useful as documentation of the theorem itself *as well as* documentation within a proof using the theorem.

Using the surjective example, I wouldn't like to see one theorem's name use `surjective` while another used `onto`, even though the theorems are referring to the same thing.

#### [ Moses Schönfinkel (Apr 30 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125889121):
That would be `epic`.

#### [ Moses Schönfinkel (Apr 30 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125889184):
Oh using the joy_`cat` is super clever.

#### [ Johan Commelin (Apr 30 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bounded%20quantifiers/near/125889234):
Cool, didn't know that one existed. Will make use of it (-;


{% endraw %}
