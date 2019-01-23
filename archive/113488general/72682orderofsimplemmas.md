---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/72682orderofsimplemmas.html
---

## Stream: [general](index.html)
### Topic: [order of simp lemmas](72682orderofsimplemmas.html)

---

#### [Sebastien Gouezel (Nov 25 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/order%20of%20simp%20lemmas/near/148324441):
There are in `data/set/basic.lean` the following two simp lemmas, in this order:
```lean
@[simp] theorem mem_image (f : α → β) (s : set α) (y : β) : y ∈ f '' s ↔ ∃ x, x ∈ s ∧ f x = y
@[simp] theorem ball_image_iff {f : α → β} {s : set α} {p : β → Prop} : (∀ y ∈ f '' s, p y) ↔ (∀ x ∈ s, p (f x))
```
After these, if you try
```lean
lemma foo {α : Type*} {β : Type*} {f : α → β} {s : set α} {p : β → Prop} (h : ∀ x ∈ s, p (f x)) : ∀ y ∈ f '' s, p y :=
begin
  simp,
end
```
the hope would be that `ball_image_iff` fires and reduces the conclusion to the assumption `h`. Unfortunately, the other lemma `mem_image` also matches, and it fires before, so that `simp` reduces the goal to the less useful `∀ (y : β) (x : α), x ∈ s → f x = y → p y`. This means that, in fact, the attribute `@[simp]` on `ball_image_iff` is useless as it will never fire.

Is there a way to tell Lean that it should try `ball_image_iff` before `mem_image`? I tried reversing the order of the lemmas in the file, but this does nothing. 

A somewhat hackish (but working) solution is to add another simp lemma that starts from the result of the simplification under `mem_image`, and brings it to what we want. But this is not really satisfactory...

