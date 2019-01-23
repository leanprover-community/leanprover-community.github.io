---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/62456typeclassinferencewithparameters.html
---

## Stream: [general](index.html)
### Topic: [type class inference with parameters](62456typeclassinferencewithparameters.html)

---

#### [Floris van Doorn (Nov 07 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20with%20parameters/near/146970992):
Is there a way to tell type class inference to "use the current parameter"? In the following code, the `apply_instance` fails, because the argument of type `decidable_eq A` is a metavariable, and I want Lean to use the parameter.
```
section
parameters {A : Type} {h : decidable_eq A}
def X := A ⊕ A
def decidable_eq_X : decidable_eq X := @sum.decidable_eq _ h _ h
local attribute [instance] decidable_eq_X
set_option trace.class_instances true
def foo : decidable_eq X := by apply_instance
end
```
(note: it is unacceptable in my actual application to let `X` depend on `h`)

#### [Simon Hudon (Nov 07 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20with%20parameters/near/146971329):
What if you use `[ ]` around the declaration of `h`?

#### [Floris van Doorn (Nov 07 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20with%20parameters/near/146971982):
That works, but in my actual example `h` is not a type class parameter, but just some extra data to construct a `setoid`.

#### [Simon Hudon (Nov 07 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20with%20parameters/near/146972041):
You could do something like `by haveI := h; apply_instance`, replacing `h` with whatever you need it to be.

#### [Simon Hudon (Nov 07 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20with%20parameters/near/146972171):
(you need `mathlib` for `haveI` by the way, and to import `tactic`)

#### [Floris van Doorn (Nov 07 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20with%20parameters/near/146972280):
this is a more faithful representation of my actual scenario:
```
constant some_data (α : Type) : Type
definition foo {α : Type} (h : some_data α) : setoid (α ⊕ α) := sorry
section
parameters {α : Type} (h : some_data α)
def X := α ⊕ α
def setoid_X : setoid X := foo h
local attribute [instance] setoid_X
set_option trace.class_instances true
def foo : setoid X := by apply_instance
end
```

#### [Floris van Doorn (Nov 07 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20with%20parameters/near/146972375):
yes, that works, but is still a little annoying.

#### [Floris van Doorn (Nov 07 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20with%20parameters/near/146972463):
I only have a problem with `quotient.mk`, so currently I just have something like `def my_quotient.mk := @quotient.mk _ setoid_X`, which is also a little annoying.

#### [Simon Hudon (Nov 07 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20with%20parameters/near/146972512):
There's been a couple of back-and-forth on the subject. Leo doesn't like to allow instances to be created on the fly but he still granted us a way to do it.

#### [Simon Hudon (Nov 07 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20with%20parameters/near/146972748):
Does it work if you replace `@quotient.mk _ setoid_X` with `by haveI := setoid_X; apply quotient.mk`?

#### [Floris van Doorn (Nov 07 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20with%20parameters/near/146972896):
```quote
There's been a couple of back-and-forth on the subject. Leo doesn't like to allow instances to be created on the fly but he still granted us a way to do it.
```
Yeah, I know, but I don't want to add instances on the fly, I just want that in that section I have an instance of type `setoid X`.

#### [Simon Hudon (Nov 07 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20inference%20with%20parameters/near/146973032):
I see. I mistook your issue. I think the problem is that your instance depend on stuff that can't be inferred. You may have to make `some_data` a class locally.

