---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/00992rflandwildcardpattern.html
---

## [general](index.html)
### [rfl and wildcard pattern](00992rflandwildcardpattern.html)

#### [Patrick Massot (Jun 08 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127771996):
Have a look at https://github.com/kbuzzard/lean-perfectoid-spaces/blob/b1e6489145be504e64a009226c6811bfd84a5070/src/valuations.lean#L143-L151:
```lean
theorem mul_assoc : ∀ (x y z : option α), mul (mul x y) z = mul x (mul y z)
| (some x) (some y) (some z) := congr_arg some $ _root_.mul_assoc x y z
| (some _) (some _) none     := rfl
| (some _) none     (some z) := rfl
| (some _) none     none     := rfl
| none     (some _) (some z) := rfl
| none     (some _) none     := rfl
| none     none     (some z) := rfl
| none none none := rfl
```
What would be a way to compress this down to three lines?  Replacing lines 3 to N by `|_ _ _ := rfl` doesn' work.

#### [Simon Hudon (Jun 08 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127772157):
I would try something like:

```lean
theorem mul_assoc : ∀ (x y z : option α), mul (mul x y) z = mul x (mul y z) :=
by { intros, casesm* option _ ; (apply congr_arg some (_root_.mul_assoc x y z) <|> refl)) }
```

#### [Simon Hudon (Jun 08 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127772285):
Maybe this would be clearer and faster:

```lean
theorem mul_assoc : ∀ (x y z : option α), mul (mul x y) z = mul x (mul y z) :=
by { intros, casesm* option _, 
     { exact congr_arg some (_root_.mul_assoc x y z) }, 
     all_goals { exact rfl } }
```

#### [Patrick Massot (Jun 08 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127774966):
Thanks. You need to try `rfl` first or replace names by wildcards since `x`, `y`, `z` are defined only in one case

#### [Patrick Massot (Jun 08 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127774970):
```lean
theorem mul_assoc : ∀ (x y z : option α), mul (mul x y) z = mul x (mul y z) :=
by { intros, casesm* option _,
     all_goals { exact congr_arg some (_root_.mul_assoc _ _ _) <|>  exact rfl } }
```

#### [Johan Commelin (Jun 08 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127775025):
Isn't the correct answer to your initial question `obviously`?

#### [Patrick Massot (Jun 08 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127775053):
Ok, it's time for some tactic lecture. How to you get Lean to see the name of the theorem we are proving is `mul_assoc` and there are three variables in order to use this information instead of explicitly writing `_root_.mul_assoc _ _ _`? Then you can do a bunch of other proofs with the same tactic

#### [Patrick Massot (Jun 08 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127775095):
I don't think we have `obviously` yet. But indeed it would be the correct answer

#### [Patrick Massot (Jun 08 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127775102):
Maybe we can add Scott's repo as a dependency

#### [Johan Commelin (Jun 08 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127775105):
Exactly.

#### [Johan Commelin (Jun 08 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127775112):
But I think it requires adding lots of attribute through mathlib.

#### [Johan Commelin (Jun 08 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127775113):
So it might not go as smoothly as we hope.

#### [Johan Commelin (Jun 08 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127775144):
His library is not orthogonal to mathlib, so it won't be an easy PR, I guess.

#### [Patrick Massot (Jun 08 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127775194):
I don't think it's true

#### [Simon Hudon (Jun 08 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127775202):
My pull request has not been merged yet but if you want to use my branch the code would end up very similar to your indexed product.

#### [Johan Commelin (Jun 08 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127775278):
@**Patrick Massot** I would love to be proved wrong. But what I've seen so far, is that you need to put a lot of attributes at a lot of definitions. And then afterwards life becomes easy.

#### [Patrick Massot (Jun 08 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127775330):
At least you can add lean-tidy to the project and then `import tidy.tidy` and get access to `obviously`. Then it doesn't prove this lemma

#### [Patrick Massot (Jun 08 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127775340):
Simon I don't understand what you wrote

#### [Johan Commelin (Jun 08 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127775402):
```quote
At least you can add lean-tidy to the project and then `import tidy.tidy` and get access to `obviously`. Then it doesn't prove this lemma
```
Right... but your point is that it might still prove other lemma's?

#### [Patrick Massot (Jun 08 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127775419):
I hope so

#### [Patrick Massot (Jun 08 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127775434):
Let's see what time is it in Australia.

#### [Simon Hudon (Jun 08 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127775439):
I made a pull request with `refine_struct` that would be useful here. It hasn't been merged yet but you can still use it.

#### [Patrick Massot (Jun 08 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127775487):
@**Scott Morrison** We currently have this proof:
```lean
theorem mul_assoc : ∀ (x y z : option α), mul (mul x y) z = mul x (mul y z) :=
by { intros, casesm* option _,
      all_goals { exact congr_arg some (_root_.mul_assoc _ _ _) <|>  refl } }
```
Question: should this be killed by one of your magic tactics?

#### [Patrick Massot (Jun 08 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127775493):
Simon: But the question at hand has no structure to refine

#### [Simon Hudon (Jun 08 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127775587):
Aren't you building up to a monoid or semigroup?

#### [Patrick Massot (Jun 08 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127775601):
True

#### [Patrick Massot (Jun 08 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127775607):
I don't know what I was thinking

#### [Simon Hudon (Jun 08 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127775614):
You may be able to have only one proof for the whole instance

#### [Patrick Massot (Jun 08 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127775662):
I was carelessly browsing code in lean-perfectoid and saw this lemma with seven stupid lines and focussed on it. But of course its only use is in an instance later.

#### [Simon Hudon (Jun 08 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127775784):
That's a pretty common mindset for me. That's actually a fun part of doing engineering: some days I don't feel smart so I can do some mindless tasks until I feel inspired again. The downside is that I don't consider much contexts while doing that so I end up improving the minutia of solutions that should just scrapped altogether

#### [Patrick Massot (Jun 08 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127775861):
It's a bit annoying that this PR is not merged because it's content is scattered among several files, so it's not immediate to incorporate it into another project

#### [Simon Hudon (Jun 08 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127775950):
What you can do is link to my repo in your toml file

#### [Simon Hudon (Jun 08 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127775976):
I may have to update that branch first but I can do that right now

#### [Patrick Massot (Jun 08 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127776127):
That may be a good solution if @**Mario Carneiro** and @**Johannes Hölzl** need more time to review your PR, because the Perfectoid project will need a lot of instances of algebraic objects.

#### [Simon Hudon (Jun 08 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127777679):
It's ready when you are.

#### [Patrick Massot (Jun 08 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127779269):
After doing `field ← get_current_field,` how would you replace `whatever.something` with `_root_.something` inside `field` so that I can later use it in the relevant version of `derive_field`?

#### [Simon Hudon (Jun 08 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127779369):
Is `whatever` something like `semigroup`?

#### [Patrick Massot (Jun 08 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127779372):
yes

#### [Simon Hudon (Jun 08 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127779429):
Why do you need to strip it away?

#### [Patrick Massot (Jun 08 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127779454):
because it doesn't work otherwise

#### [Patrick Massot (Jun 08 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127779456):
see the handcrafted proof above

#### [Simon Hudon (Jun 08 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127779538):
Do you have an instance of `semigroup` for `α`?

#### [Patrick Massot (Jun 08 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127779562):
`linear_ordered_comm_group` actually

#### [Patrick Massot (Jun 08 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127779564):
and the goal is to build `linear_ordered_comm_monoid (option α)`

#### [Patrick Massot (Jun 08 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127779611):
but `to_string field` turns out to be `comm_monoid.mul_assoc` here

#### [Patrick Massot (Jun 08 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127779616):
but the proof then needs `_root_.mul_assoc`

#### [Simon Hudon (Jun 08 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127779821):
I find it odd: the types are very similar. Can you give me the error you get when your proof fails?

#### [Simon Hudon (Jun 08 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127779827):
(It is possible to do what you ask but I think we're better off taking a different approach)

#### [Patrick Massot (Jun 08 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127780142):
I minimized to 
```lean
import algebra.pi_instances

class linear_ordered_comm_group (α : Type)
    extends comm_group α, linear_order α :=
(mul_le_mul_left : ∀ {a b : α}, a ≤ b → ∀ c : α, c * a ≤ c * b)

class linear_ordered_comm_monoid (α : Type)
    extends comm_monoid α, linear_order α :=
(mul_le_mul_left : ∀ {a b : α}, a ≤ b → ∀ c : α, c * a ≤ c * b)

variables {α : Type} [linear_ordered_comm_group α] 


def mul : option α → option α → option α
| (some x) (some y) := some (x * y)
| _        _        := none

def one : option α := some 1

def le : option α → option α → Prop
| (some x) (some y) := x ≤ y
| (some _) none     := false
| none     _        := true

instance : linear_ordered_comm_monoid (option α) :=
by refine_struct { mul := mul, one := one, le := le, .. }; { tactic.derive_field_option }
```
The game is to add `derive_field_option` to `algebra.pi_instances` (from your branch of course) to make it work

#### [Patrick Massot (Jun 08 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127780175):
Again, this is not crucial, Kenny did it by hand, I'm only trying to slowly learn tactic writing for specialized automation

#### [Simon Hudon (Jun 08 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127780177):
Nice :) I'm going to play a bit :D

#### [Patrick Massot (Jun 08 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127780228):
I should go and take care of my family (I'm not even talking about the work I should have been doing)

#### [Simon Hudon (Jun 08 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127780239):
Ah family! They keep interrupting math, don't they? :D

#### [Patrick Massot (Jun 08 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127780314):
The version which doesn't work is:
```lean
meta def derive_field_option : tactic unit :=
do b ← target >>= is_prop,
  if b then do
     field ← get_current_field,
     trace (to_string field),
     intros,
     `[casesm* option _],
     `[all_goals { exact congr_arg some (field _ _ _) <|> exact rfl }]
  else do skip
```

#### [Scott Morrison (Jun 11 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rfl and wildcard pattern/near/127888806):
Just arrived back from underwater. I've starred the proof you asked about, @Patrick, and will try out `obviously`. I suspect it requires more case bashing (on `option`) than obviously is by default willing to do.

