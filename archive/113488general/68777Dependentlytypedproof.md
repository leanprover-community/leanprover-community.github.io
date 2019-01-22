---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/68777Dependentlytypedproof.html
---

## [general](index.html)
### [Dependently typed proof](68777Dependentlytypedproof.html)

#### [Frantisek Silvasi (Feb 27 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently typed proof/near/123038173):
I don't suppose this sorry is provable - how does one convince Lean that whatever it is that I am mapping over comes from the list being mapped over? I can show that: `x ∈ filter P xs -> P x`, but I can't tell map `x ∈ filter P xs`, even though it's "obvious". This is a toy version of what I am trying to do:
```
def positive := {x : ℤ // x > 0}
def x_of_positive : positive → ℤ | ⟨a, _⟩ := a
def is_positive (x : ℤ) := x > 0
instance {x : ℤ} : decidable (is_positive x) := by simp [is_positive]; apply_instance
def make_positive (x : ℤ) (h : x > 0) : positive := ⟨x, h⟩
def test_two (x : positive) :=
  let pos := x_of_positive x in [pos+1, pos-1]
def foo (x : positive) :=
  let to_check  := test_two x in
  let checked   := list.filter is_positive to_check in
  let positives := list.map (λx, make_positive x sorry) checked in
  positives
```

#### [Andrew Ashworth (Feb 27 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently typed proof/near/123039719):
you want the `of_mem_filter` lemma in mathlib

#### [Andrew Ashworth (Feb 27 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently typed proof/near/123039771):
wait, sorry, I didn't look closely enough at your code snippet

#### [Frantisek Silvasi (Feb 27 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently typed proof/near/123039815):
The idea is to escape positive to Z and check x+/-1. Then I filter the ones that are not positive and now I need a way to inject them back to the dependent type.

#### [Chris Hughes (Feb 27 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently typed proof/near/123039868):
list.pmap in mathlib is probably what you want

#### [Andrew Ashworth (Feb 27 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently typed proof/near/123039927):
one way to do it would be to prove that all the operations you use preserve the `is_positive` invariant

#### [Andrew Ashworth (Feb 27 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently typed proof/near/123039980):
this is kind of tedious, i'd be hunting for a appropriate function in the data.list namespace, maybe `pmap` would be appropriate as Chris mentioned

#### [Patrick Massot (Feb 27 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently typed proof/near/123039982):
Don't forget to use````lean` instead of ````` at the beginning of your code blocks to have (partial) syntax highlighting

#### [Frantisek Silvasi (Feb 27 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently typed proof/near/123039988):
I'll take a look at the pmap, thank you.

#### [Frantisek Silvasi (Feb 27 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently typed proof/near/123040083):
Interesting. This `pmap` contraption is basically `map . filter`, which is exactly what I do, except I manage to lose some information in between.

#### [Chris Hughes (Feb 27 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently typed proof/near/123040088):
``` lean
import data.list.basic

def positive := {x : ℤ // x > 0}
def x_of_positive : positive → ℤ | ⟨a, _⟩ := a
def is_positive (x : ℤ) := x > 0
instance {x : ℤ} : decidable (is_positive x) := by simp [is_positive]; apply_instance
def make_positive (x : ℤ) (h : x > 0) : positive := ⟨x, h⟩
def test_two (x : positive) :=
  let pos := x_of_positive x in [pos+1, pos-1]
def foo (x : positive) :=
  let to_check  := test_two x in
  let checked   := list.filter is_positive to_check in
  let positives := list.pmap (λ x (hx : x > 0), make_positive x hx) checked (λ a ha, (list.mem_filter.1 ha).right) in
  positives

```

#### [Frantisek Silvasi (Feb 27 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently typed proof/near/123040098):
Is the `a ha` accidental ;)?

#### [Frantisek Silvasi (Feb 27 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently typed proof/near/123040102):
Thank you kindly for your help, I'm going to take `pmap` for a spin.

#### [Mario Carneiro (Feb 27 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Dependently typed proof/near/123051610):
@**Frantisek Silvasi** The combination of filter and map in the positive case is `filter_map`. You should `filter_map` with the function `if h : x > 0 then some (is_positive x h) else none`

