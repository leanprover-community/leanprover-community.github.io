---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/34376hascoetofunquestions.html
---

## [general](index.html)
### [has_coe_to_fun questions](34376hascoetofunquestions.html)

#### [Kevin Buzzard (Oct 31 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_coe_to_fun%20questions/near/136859792):
1) What's going on here?

```lean
import data.equiv.basic

definition ABC : decidable_eq ℕ := by apply_instance
theorem CBA : decidable_eq ℕ := by apply_instance

definition XYZ (α β : Type) : has_coe_to_fun (α ≃ β) := by apply_instance
-- theorem ZYX (α β : Type) : has_coe_to_fun (α ≃ β) := by apply_instance -- fails??
```

2) Does `has_coe_to_fun` work by magic? I hadn't really appreciated this before. I understand how vanilla type class inference works, i.e. how `has_add.add x y` uses unification to figure out the type of x and y and then uses type class inference to figure out what addition I meant, but the reason this works is that the definition of `has_add.add` has some `[]` brackets in. I realise now that in this code

```lean
import data.equiv.basic

example (α β : Type) (H : α ≃ β) : α → β := H
```

nothing I wrote contains a `[]`. So some extra magic is happening. Is this something to do with some C++ type unification algorithm going "oh-oh, `H` doesn't have the right type, but the user is looking for a function, why don't I see if `has_coe_to_fun` can help?" Or is there some more  down-to-earth explanation which I've missed?

#### [Johannes Hölzl (Oct 31 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_coe_to_fun%20questions/near/136860331):
For 1) you see the difference when you activate `set_option pp.all true` in the `definition` case, the inferred function is into an type universe which is still a meta variable (which is important as it will be fixed to 1). In the `theorem` case it is fixed to a universe variable, and hence fails

#### [Johannes Hölzl (Oct 31 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_coe_to_fun%20questions/near/136860427):
`definition` does not require that the type is fully elaborated, quiet the opposite, that's why one can write a definition without a result type. The result type is inferred from the right-hand side.

#### [Johannes Hölzl (Oct 31 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_coe_to_fun%20questions/near/136860469):
`theorem` works different, it fully elaborates the statement, and any universe hole is filled in with a fresh variable.

#### [Floris van Doorn (Oct 31 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_coe_to_fun%20questions/near/136860492):
2) Yes, there is some extra magic happening. If Lean knows that the type of some term `t` is `T`, and knows that the expected type is a function type, then it will automatically fire type-class inference to find an instance of `has_coe_to_fun T`.

#### [Johannes Hölzl (Oct 31 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_coe_to_fun%20questions/near/136860704):
One might wonder why the universe parameters are not filled in by stating `has_coe_to_fun (α ≃ β)` for `α` and `β` in `Type 0` (which is the case in the examples):
   `has_coe_to_fun` actually allows to map to a different type universe!

#### [Kevin Buzzard (Oct 31 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/has_coe_to_fun%20questions/near/136860778):
Thanks to both of you. I remember it taking me a very long time to understand type class inference, and I had always assumed I understood it until I started thinking about it more carefully just the other day. For (1) I remember running into these subtleties with the difference between `definition` and `theorem` before, but maybe I have just never fully understood them. Usually they only show up (for me) when I foolishly use the wrong one :-) I think we should have a little VS Code paperclip that pops up saying "I see you're writing a theorem. Do you want some help with that, specifically because you seem to be constructing a term whose type is not a proposition?".

