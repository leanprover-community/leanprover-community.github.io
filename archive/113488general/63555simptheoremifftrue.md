---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/63555simptheoremifftrue.html
---

## [general](index.html)
### [simp theorem iff true](63555simptheoremifftrue.html)

#### [Sean Leather (May 18 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20theorem%20iff%20true/near/126744334):
What's the difference in `simp` behavior (if any) between these two theorems for `p : Prop`? Is one or the other preferable?

```lean
@[simp] theorem t₁ (...) : p ↔ true := ...
@[simp] theorem t₂ (...) : p := ...
```

#### [Gabriel Ebner (May 18 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20theorem%20iff%20true/near/126744745):
There is a difference if `p` is an equation or another simp relation.

#### [Sean Leather (May 18 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20theorem%20iff%20true/near/126744833):
Can you expand on that? I'm not sure what “another simp relation” is. Is there an example?

#### [Gabriel Ebner (May 18 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20theorem%20iff%20true/near/126745082):
Good question! If you have a relation `R` that is reflexive and transitive (as tagged with `@[refl]` and `@[trans]`), then you can use the simplifier to get proofs of `R x ?m_1` where `?m_1` is the simplified version of `x`.  For example think of equivalence relations such as equality modulo k in the integers.

#### [Gabriel Ebner (May 18 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20theorem%20iff%20true/near/126745137):
In mathlib it is used for the equivalence relation on types, where types are equivalent if they are equinumerous (have a bijection between them).  Then you can simplify `a ⨉ unit` to `a` for example.

#### [Sean Leather (May 18 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20theorem%20iff%20true/near/126745205):
Okay. Suppose I have these:

```lean
@[simp] theorem t₁ (...) : a = b ↔ true := ...
@[simp] theorem t₂ (...) : a = b := ...
```

I would intuitively write `t₂` and not `t₁` because I know `=` is a `simp` relation, right? What happens if you have `t₁` instead of `t₂`?

#### [Gabriel Ebner (May 18 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20theorem%20iff%20true/near/126745206):
https://github.com/leanprover/mathlib/blob/38d553694351f4c23a8a8216038c7c8abcb7cd32/data/equiv.lean#L166-L177

#### [Gabriel Ebner (May 18 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20theorem%20iff%20true/near/126745209):
> What happens if you have t₁ instead of t₂?

Then simp won't be able to solve `b = a`, for instance.  It will only rewrite `a = b` to true.

#### [Sean Leather (May 18 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20theorem%20iff%20true/near/126745224):
Right, makes sense.

#### [Sean Leather (May 18 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20theorem%20iff%20true/near/126745275):
And if `p` is not a `simp` relation, is there any difference between the two?

#### [Gabriel Ebner (May 18 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20theorem%20iff%20true/near/126745277):
I don't think so.

#### [Sean Leather (May 18 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20theorem%20iff%20true/near/126745343):
In mathlib, I see these:

```lean
$ git grep "↔ true"
data/finset.lean:theorem forall_mem_empty_iff (p : α → Prop) : (∀ x, x ∈ (∅ : finset α) → p x) ↔ true :=
data/set/basic.lean:  (∀ x ∈ (∅ : set α), p x) ↔ true :=
logic/basic.lean:@[simp] theorem imp_self : (a → a) ↔ true := iff_true_intro id
logic/basic.lean:@[simp] theorem imp_true_iff {α : Sort*} : (α → true) ↔ true :=
logic/basic.lean:@[simp] theorem forall_true_iff : (α → true) ↔ true :=
logic/basic.lean:theorem forall_true_iff' (h : ∀ a, p a ↔ true) : (∀ a, p a) ↔ true :=
logic/basic.lean:@[simp] theorem forall_2_true_iff {β : α → Sort*} : (∀ a, β a → true) ↔ true :=
logic/basic.lean:  (∀ a (b : β a), γ a b → true) ↔ true :=
logic/basic.lean:@[simp] theorem forall_prop_of_false {p : Prop} {q : p → Prop} (hn : ¬ p) : (∀ h' : p, q h') ↔ true :=
logic/basic.lean:theorem ball_true_iff (p : α → Prop) : (∀ x, p x → true) ↔ true :=
```

#### [Sean Leather (May 18 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20theorem%20iff%20true/near/126745409):
I suppose the `→`/`Π` is special, thus `theorem forall_true_iff : (α → true) ↔ true`.

#### [Gabriel Ebner (May 18 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20theorem%20iff%20true/near/126745419):
Yes, without the iff true, those would be conditional simp lemmas.

#### [Sean Leather (May 18 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20theorem%20iff%20true/near/126745473):
Right. So, with these few exceptions, we should write `@[simp] theorem t₂ (...) : p := ...`.

#### [Sean Leather (May 18 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20theorem%20iff%20true/near/126745495):
(where `t₂` may or may not be conditional)

