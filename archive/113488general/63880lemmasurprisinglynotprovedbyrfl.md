---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/63880lemmasurprisinglynotprovedbyrfl.html
---

## Stream: [general](index.html)
### Topic: [lemma surprisingly not proved by rfl](63880lemmasurprisinglynotprovedbyrfl.html)

---


{% raw %}
#### [ Chris Hughes (Jul 02 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lemma%20surprisingly%20not%20proved%20by%20rfl/near/128969240):
Is there a shorter way to prove this and why isn't `rfl` working? Is it because the type of the lhs is `with_bot ℕ` and the rhs is `option ℕ`? (The types are defeq)

```lean
import algebra.ordered_group

example : (0 : with_bot ℕ) = some 0 := rfl -- doesn't work

example : (0 : with_bot ℕ) = some 0 :=
by unfold has_zero.zero add_monoid.zero has_one.one monoid.one 
  add_comm_monoid.zero semiring.zero ordered_semiring.zero linear_ordered_semiring.zero
  decidable_linear_ordered_semiring.zero comm_semiring.zero
```

#### [ Chris Hughes (Jul 02 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lemma%20surprisingly%20not%20proved%20by%20rfl/near/128970431):
Looked a little deeper and it seems `(0 : with_bot ℕ)` is defeq to `some (1 : multplicative ℕ)`. I feel like perhaps the fact that this lemma is not `rfl` means the definition ought to be changed.

#### [ Mario Carneiro (Jul 02 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lemma%20surprisingly%20not%20proved%20by%20rfl/near/128986937):
Oh, this is weird! It is in fact the case that `(0 : with_bot ℕ) = some 0`, but the tactics are very confused about it. Here's `simp` proving that they are different, and then the kernel says it's a wrong proof:
```
example : (0 : with_bot ℕ) ≠ (some 0 : option ℕ) :=
show some _ ≠ some 0, begin
  simp [multiplicative.monoid],
end
```

#### [ Mario Carneiro (Jul 02 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lemma%20surprisingly%20not%20proved%20by%20rfl/near/128986953):
I will add a lemma for it

#### [ Mario Carneiro (Jul 02 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lemma%20surprisingly%20not%20proved%20by%20rfl/near/128986995):
as a slight hack, you can instead prove it by `dec_trivial`

#### [ Kevin Buzzard (Jul 02 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lemma%20surprisingly%20not%20proved%20by%20rfl/near/128987480):
```
failed to synthesize type class instance for
⊢ has_zero (with_bot ℕ)
```

-- am I missing an import?

#### [ Mario Carneiro (Jul 02 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lemma%20surprisingly%20not%20proved%20by%20rfl/near/128987708):
`algebra.ordered_group`

#### [ Mario Carneiro (Jul 02 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lemma%20surprisingly%20not%20proved%20by%20rfl/near/128988232):
@**Sebastian Ullrich** Minimized:
```
def nat2 := nat
instance : has_one nat2 := ⟨(0 : ℕ)⟩
example : (0 : ℕ) ≠ (1 : nat2) := by simp
```

#### [ Mario Carneiro (Jul 02 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lemma%20surprisingly%20not%20proved%20by%20rfl/near/128988318):
In this example `example : (0 : ℕ) = (1 : nat2) := rfl` also fails

#### [ Sebastian Ullrich (Jul 02 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lemma%20surprisingly%20not%20proved%20by%20rfl/near/128988873):
@**Mario Carneiro** Thanks, this seems to be an imprecise term pattern match at https://github.com/leanprover/lean/blob/master/src/library/type_context.cpp#L2906-L2907

#### [ Mario Carneiro (Jul 02 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lemma%20surprisingly%20not%20proved%20by%20rfl/near/128988933):
Ooh, that's a tricky one. I'd hate for you to have to do defeq checks constantly there out of paranoia for tricks like I showed...

#### [ Sebastian Ullrich (Jul 02 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lemma%20surprisingly%20not%20proved%20by%20rfl/near/128989538):
Yeah. It's probably not a good idea in general to declare instances on semireducible defs like `multiplicative`. Is it feasible to change that?

#### [ Mario Carneiro (Jul 02 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lemma%20surprisingly%20not%20proved%20by%20rfl/near/128989548):
Not really, I mean that is the point

#### [ Sebastian Ullrich (Jul 02 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lemma%20surprisingly%20not%20proved%20by%20rfl/near/128989559):
Sorry, I meant making it irreducible or a newtype.

#### [ Mario Carneiro (Jul 02 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lemma%20surprisingly%20not%20proved%20by%20rfl/near/128989625):
Probably not. An important aspect of the semireducible part is that you can prove multiplicative versions of additive theorems by defeq

#### [ Mario Carneiro (Jul 02 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lemma%20surprisingly%20not%20proved%20by%20rfl/near/128989657):
It's fine as long as it gives way to a sufficiently forceful "unfold", but I'm not sure irreducible will

#### [ Mario Carneiro (Jul 02 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lemma%20surprisingly%20not%20proved%20by%20rfl/near/128989728):
I would say that users should avoid having things of type `multiplicative A` in their goal at all

#### [ Mario Carneiro (Jul 02 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lemma%20surprisingly%20not%20proved%20by%20rfl/near/128989802):
so I think I will change the definition of the `with_bot` instance so that it unfolds directly rather than showing the multiplicative stuff

#### [ Mario Carneiro (Jul 03 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lemma%20surprisingly%20not%20proved%20by%20rfl/near/128992229):
fixed


{% endraw %}
