---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/99796cantmanuallydunfoldreals.html
---

## [general](index.html)
### [can't manually `dunfold` reals](99796cantmanuallydunfoldreals.html)

#### [Kevin Buzzard (Nov 21 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can't manually `dunfold` reals/near/148102409):
```lean
import data.real.basic

-- from data.real.basic
-- def real := @cau_seq.completion.Cauchy ℚ _ _ _ abs _

example : real = @cau_seq.completion.Cauchy ℚ _ _ _ abs _ := rfl -- fails



#print prefix real.equations -- equations lemmas for real numbers

#check real.equations._eqn_1

-- real.equations._eqn_1 : ℝ = cau_seq.completion.Cauchy

#print real.equations._eqn_1

/-

@[_refl_lemma]
theorem real.equations._eqn_1 : ℝ = cau_seq.completion.Cauchy :=
eq.refl ℝ

-/

-- this fails too
example : real = (@cau_seq.completion.Cauchy.{0 0} rat rat.discrete_linear_ordered_field rat rat.comm_ring
     (@abs.{0} rat rat.decidable_linear_ordered_comm_group)
     (@abs_is_absolute_value.{0} rat rat.discrete_linear_ordered_field)) := eq.refl ℝ -- fails

set_option pp.all true
definition x : ℝ :=
begin
  -- ⊢ real
  rw real.equations._eqn_1,
  -- this works, and changes goal to
  -- ⊢ @cau_seq.completion.Cauchy.{0 0} rat rat.discrete_linear_ordered_field rat rat.comm_ring
  --  (@abs.{0} rat rat.decidable_linear_ordered_comm_group)
  --  (@abs_is_absolute_value.{0} rat rat.discrete_linear_ordered_field)
  exact 37,
end
```

Are the reals not definitionally equal to their definition? Have I done something silly? I can't reconstruct the proof of the equation lemma.

#### [Keeley Hoek (Nov 21 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can't manually `dunfold` reals/near/148102574):
Does it have anything to do with `real` being marked `irreducible` here?: https://github.com/leanprover/mathlib/blob/9f5099ec2cd933822ba3d422e74189d3508e5d0e/data/real/basic.lean#L198

#### [Rob Lewis (Nov 21 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can't manually `dunfold` reals/near/148102599):
It does. It will work if you add `local attribute [semireducible] real`.

#### [Kevin Buzzard (Nov 21 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can't manually `dunfold` reals/near/148102968):
So irreducibility even stops `rfl` working?

#### [Kevin Buzzard (Nov 21 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can't manually `dunfold` reals/near/148103274):
It seems like a *really* good idea from the point of mathematics to have `real` treated as a constant. There is more than one way to implement it (Dedekind cuts, Cauchy sequences) and hence mathematicians should not care about the implementation. I noticed that even `set_option pp.all true` would not unfold it. This seems like "correct" behaviour. I understand that `rat` is treated as a constant -- from Lean's point of view it *is* a constant, right? It's an inductive type. `real` is the only odd one out, I think -- all the rest are inductive types I guess.

#### [Kevin Buzzard (Nov 21 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can't manually `dunfold` reals/near/148103486):
So what does `set_option pp.all true` unfold? I see I can change its output changing with `dunfold`:

```lean
set_option pp.all true
definition x : ℝ :=
begin
  -- ⊢ real
  rw real.equations._eqn_1,
  -- ⊢ @cau_seq.completion.Cauchy.{0 0} rat rat.discrete.blah...
  dunfold cau_seq.completion.Cauchy,
  -- ⊢ @quotient.{1} (@cau_seq.{0 0} rat... 
  dunfold quotient,
  -- ⊢ @quot.{1} (@cau_seq.{0 0} rat... 
  sorry
end
```

#### [Kevin Buzzard (Nov 21 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can't manually `dunfold` reals/near/148103518):
I thought `pp.all` unfolded as much as it could. But these definitions like `cau_seq.completion.Cauchy` don't seem to be tagged with anything in particular.

#### [Sebastian Ullrich (Nov 21 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can't manually `dunfold` reals/near/148103809):
`pp.all` doesn't unfold anything. It just shows information that is usually omitted, but always there in the term

#### [Kevin Buzzard (Nov 21 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can't manually `dunfold` reals/near/148104280):
Aah! So when one gets huge expansion in term length after switching `pp.all` on -- as often happens to me -- this is perhaps often due to type class inference, which is always there in the term because it "works via `@`" rather than working by unfolding definitions.

#### [Kevin Buzzard (Nov 21 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can't manually `dunfold` reals/near/148104837):
So what's going on here?
```lean
import data.real.basic

set_option pp.all true
theorem hard : (2 : ℝ) + 2 = 5 := begin
  -- 13 lines of output; excerpts below. 

  -- ⊢ ... @has_add.add.{0} real ...
  unfold has_add.add,
  -- ⊢ ... @distrib.add.{0} real ...
  unfold distrib.add,
  -- ⊢ ... @ring.add.{0} real real.ring ...
  unfold ring.add,
  -- ... @comm_ring.add.{0} real real.comm_ring ...
  unfold comm_ring.add,
  -- ... @comm_ring.add.{0} real real.comm_ring_aux ...
  -- next line fails
  unfold comm_ring.add, -- simplify tactic failed to simplify
  sorry
end
```

#### [Rob Lewis (Nov 21 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can't manually `dunfold` reals/near/148104929):
https://github.com/leanprover/mathlib/blob/master/data/real/basic.lean#L198

#### [Kevin Buzzard (Nov 21 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can't manually `dunfold` reals/near/148104956):
but I can presumably keep going somehow? Is there an equation lemma I can use?

#### [Kevin Buzzard (Nov 21 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can't manually `dunfold` reals/near/148105101):
got it

#### [Rob Lewis (Nov 21 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can't manually `dunfold` reals/near/148105102):
You can `rw real.comm_ring_aux`. Or, in general, you can use `#print prefix` to look for specific equation lemmas. `#print prefix real.comm_ring_aux`

#### [Kevin Buzzard (Nov 21 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can't manually `dunfold` reals/near/148105109):
```lean
  rw real.comm_ring_aux.equations._eqn_1,
  unfold comm_ring.add,
```
So again irreducibility stopped me from proceeding.

#### [Kevin Buzzard (Nov 21 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can't manually `dunfold` reals/near/148105127):
But it was difficult for me to guess that the problem was with `real.comm_ring_aux` -- I just thought `comm_ring.add` was being silly.

#### [Mario Carneiro (Nov 21 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can't manually `dunfold` reals/near/148106480):
if you really really want to unfold `real`, you can use `delta`

#### [Kevin Buzzard (Nov 21 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can't manually `dunfold` reals/near/148107368):
I am confused about whether one should regard `real` and `@cau_seq.completion.Cauchy ℚ _ _ _ abs _` as definitionally equal. They are equal by definition, but `rfl` will not prove it.

#### [Patrick Massot (Nov 21 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can't manually `dunfold` reals/near/148107369):
Kevin, could you explain what you are trying to do? I didn't manage to guess from messages in this thread.

#### [Kevin Buzzard (Nov 21 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can't manually `dunfold` reals/near/148107378):
This is not mathematics.

#### [Patrick Massot (Nov 21 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can't manually `dunfold` reals/near/148107379):
What would be a realistic lemma you'd want to prove?

#### [Kevin Buzzard (Nov 21 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can't manually `dunfold` reals/near/148107386):
I am trying to understand equality better; I was thinking of making a blog post about it.

#### [Kevin Buzzard (Nov 21 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can't manually `dunfold` reals/near/148107395):
Every time I think about it, I understand it a little more.

#### [Kevin Buzzard (Nov 21 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can't manually `dunfold` reals/near/148107469):
Sometimes when I was just completely stuck at Lean in the early days, it was because I didn't understand equality well enough. As you know Patrick, computer science equality is far harder than mathematics equality. I was trying to write some post where I explain this to mathematicians, but then I realised I didn't really understand it well enough to explain it myself.

#### [Sebastian Ullrich (Nov 21 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can't manually `dunfold` reals/near/148107546):
The short answer is: the kernel says they are defeq, but the elaborator says they are not. Because the elaborator respects reducibility hints for efficiency reasons.

#### [Kevin Buzzard (Nov 21 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/can't manually `dunfold` reals/near/148108095):
Sebastian many thanks for your succinct but extremely helpful contributions to this thread.

