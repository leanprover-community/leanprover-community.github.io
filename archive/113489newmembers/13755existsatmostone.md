---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/13755existsatmostone.html
---

## [new members](index.html)
### [exists at most one](13755existsatmostone.html)

#### [Ali Sever (Jul 25 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/exists at most one/near/130274521):
I want to state `p a b → ∃ (at most one) c, q c`, and if such `c` exists, I want `f a b = c`.  Is there a smart/efficient way to do this?

#### [Kevin Buzzard (Jul 25 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/exists at most one/near/130275258):
you'll need the axiom of choice, because you're constructing data from a proof :-)

#### [Simon Hudon (Jul 25 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/exists at most one/near/130275840):
Are you trying to build such a `f`?

The assertion I think could be made as `p a b -> ∀ c₀ c₁, q c₀ → q c₁ → c₀ = c₁`

#### [Simon Hudon (Jul 25 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/exists at most one/near/130276240):
If you're defining `f`, you can do it in two ways:

```lean
noncomputable def f {a b} (h : p a b) := classical.epsilon (λ c, q c)
```

If a proper `c` exists (and your type is nonempty), the above `f` will return it (but you can't evaluate it). If such a `c` doesn't exist, we don't know what value `f` has.

We can be more defensive and write:

```lean
noncomputable def f {a b} (h : p a b) (h' : ∃ c, q c) := classical.some h'
```

This `f` can only used with a proof that a proper `c` exists and it will return that `c` (non-constructively, again).

