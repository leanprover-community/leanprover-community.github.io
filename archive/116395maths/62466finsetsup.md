---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/62466finsetsup.html
---

## [maths](index.html)
### [finset sup](62466finsetsup.html)

#### [Sebastien Gouezel (Oct 03 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135087348):
I can't find the lemma saying that, in a linear order (with bot, probably), the sup of a finset is `< a` if all its elements are `< a`(and `\bot < a`). I guess it has to be somewhere, but there are so many files and so many different classes for orders. Some help would be most welcome!

#### [Johannes Hölzl (Oct 03 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135088713):
I don't think we have the variant for `<`. There is `le_max_of_mem`, where `a ∈ s.max` states that there exist a maximum and it is `a`.

#### [Johannes Hölzl (Oct 03 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135088730):
when your order has a bottom element you can use `finset.sup_le`

#### [Sebastien Gouezel (Oct 03 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135090992):
I really need the version with `<`. I think I am lost with the typeclass system. If I want to state my lemma, say, on `nnreal`, then everything works fine:
```lean
variables {β : Type} {s : finset β} {f : β → nnreal}
lemma sup_lt {a : nnreal} : (⊥ < a) → (∀b ∈ s, f b < a) → s.sup f < a :=
by letI := classical.dec_eq β; from
finset.induction_on s (by simp) (by simp [sup_eq_max, max_lt_iff] {contextual := tt})
```
But I would like a lemma that applies in all interesting situations, for instance `ennreal`: a decidable linear order with bot. I don't know how to write this lemma properly. If I try
```lean
variables {α β : Type} {s: finset β} {f : β → α}
lemma sup_lt2 [decidable_linear_order α] [order_bot α]  {a : α} : (⊥ < a) → (∀b ∈ s, f b < a) → s.sup f < a :=
by letI := classical.dec_eq β; from
finset.induction_on s (by simp) (by simp [sup_eq_max, max_lt_iff] {contextual := tt}),
```
then it does not work because `s.sup f` does not make sense as `α` is not of class `semilattice_sup_bot`.

And if I try
```lean
variables {α β : Type} {s: finset β} {f : β → α}
lemma sup_lt3 [decidable_linear_order α] [semilattice_sup_bot α]  {a : α} : (⊥ < a) → (∀b ∈ s, f b < a) → s.sup f < a :=
by letI := classical.dec_eq β; from
finset.induction_on s (by simp) (by simp [sup_eq_max, max_lt_iff] {contextual := tt}),
```
it does not work either as the sup coming from the `decidable_linear_order` and the `semilattice_sup_bot` are not detected to be the same.

Is there a good way to write this lemma?

#### [Mario Carneiro (Oct 03 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135091562):
You could use `is_total α (≤)` as a mixin

#### [Sebastien Gouezel (Oct 03 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135093300):
Got it, thanks!
```lean
variables {α β : Type} {s: finset β} {f : β → α}
lemma sup_lt [semilattice_sup_bot α] [is_total α (≤)] {a : α} : (⊥ < a) → (∀b ∈ q, f b < a) → q.sup f < a :=
have A: ∀ x y : α, x < a → y < a → x ⊔ y < a :=
begin
  assume x y hx hy,
  cases (is_total.total (≤) x y) with h,
  {simpa [sup_of_le_right h] using hy},
  {simpa [sup_of_le_left h] using hx}
end,
by letI := classical.dec_eq β; from
finset.induction_on q (by simp) (by simp [A] {contextual := tt})
```
This applies cleanly in all situations I am interested in.
(And I confirm I am 20 times more slow in Lean than Isabelle, but hopefully this will improve slightly over time :)

#### [Kevin Buzzard (Oct 03 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135096270):
@**Sebastien Gouezel** in the past you have done mathematics in Isabelle with "PhD student level" objects like Gromov-hyperbolic spaces. What attracted me to Lean was that I realised that there seemed to be no obstruction to doing pure mathematics with objects at this kind of level (e.g. we will have a definition of a perfectoid space soon and I'm sure we'll be able to prove basic lemmas about it). Is the same true of Isabelle? Disregarding the fact that Lean's maths library is no doubt much smaller than Isabelle's, are there any other reasons why one might prefer Isabelle to Lean when manipulating complex mathematical objects?

#### [Sebastien Gouezel (Oct 03 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135096989):
There are very serious limitations in Isabelle. Doing perfectoids would be essentially impossible, I guess. For another example, I want to define the space of all compact metric spaces, put a distance on it (the so-called Gromov-Hausdorff distance), and then it makes sense to talk of the convergence of a sequence of compact metric spaces to a compact metric space, and put probability measures on the space of compact metric spaces, and so on. This is very common and useful in geometry and probability, but impossible to formalize in Isabelle, for lack of dependent types. My impression is that this will be perfectly doable in Lean. That's why I want to switch. But I miss a lot the automatisation level of Isabelle, which is way better than anything there is currently in Lean.

#### [Sebastien Gouezel (Oct 03 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135097163):
An important feature of Isabelle I dream to have in Lean is the simprocs. When you call `simp`, if it detects some pattern then it will automatically apply some algorithms. For instance, if it detects some algebraic expression, then it will simplify it within reasonable bouds. If you have something like `a+ exp( b + c + d - b + c) - a` and you just apply `simp`, it will transform it to `exp (2 * c+d)`, without the need to call an additional tactic like `ring` or `abel` -- note that both `ring` and `abel` would fail on this simple example.

#### [Mario Carneiro (Oct 03 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135097464):
I think `ring` will actually do that

#### [Mario Carneiro (Oct 03 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135097473):
this is the "failure mode" of `ring`

#### [Sebastien Gouezel (Oct 03 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135097488):
Will it also simplify inside the exponential?

#### [Johan Commelin (Oct 03 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135097662):
@**Sebastien Gouezel** But there are not theoretical reasons to why this sort of thing couldn't happen in Lean, right? It is just a matter of Lean being very young compared to Isabelle. Is that right?

#### [Patrick Massot (Oct 03 2018 at 13:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135097679):
It seems it's also easier to build automation without dependent type

#### [Mario Carneiro (Oct 03 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135097699):
I think @**Johannes Hölzl** was looking into simpprocs, not sure what progress has been made there

#### [Johannes Hölzl (Oct 03 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135097703):
no a lot yet

#### [Johan Commelin (Oct 03 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135097704):
```quote
It seems it's also easier to build automation without dependent type
```
Ok, so maybe Lean has a theoretical disadvantage...

#### [Sebastien Gouezel (Oct 03 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135098086):
```quote
@**Sebastien Gouezel** But there are not theoretical reasons to why this sort of thing couldn't happen in Lean, right? It is just a matter of Lean being very young compared to Isabelle. Is that right?
```
I think so, yes. But to implement it you need to know the inner workings of simp, and I guess it is also very easy to run into performance issues.

#### [Kevin Buzzard (Oct 03 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135102923):
I dream of a future where we simply do not care about performance issues -- like in normal maths. You write it once, you compile it once, you forget about it and only come back to it when someone else changes something and your proof actually breaks.

#### [Kevin Buzzard (Oct 03 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135102950):
This is some sort of analogue of a mathematician proving a theorem and then publishing it and then everyone can use the result without having to wait for it to compile.

#### [Mario Carneiro (Oct 03 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135103468):
Wait, are you saying that when you start working on a problem, you *don't* remind yourself what facts are known by proving them and the rest of basic maths from the axioms?

#### [Mario Carneiro (Oct 03 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135103539):
I mean, who knows, maybe something you wrote today invalidates everything you have ever learned, how can you be sure unless you go over it all every day?

#### [Kevin Buzzard (Oct 03 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135104075):
Naah -- often we rely on random facts which we read on the internet and for which the proof term is currently unavailable or incomplete. One makes much faster progress this way!

#### [Patrick Massot (Oct 03 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135104095):
And this won't change until we get that module refactor

#### [Kevin Buzzard (Oct 03 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135104102):
We even sometimes rely on "facts" for which it turns out that there is no proof term at all!

#### [Patrick Massot (Oct 03 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135104153):
Waiting for Lean 4 is completely out of fashion now that we have this other fantasy

#### [Jared Corduan (Oct 03 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135114883):
some folks aren't afraid to assume GCH :)

#### [Kevin Buzzard (Oct 03 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135128633):
```quote
There are very serious limitations in Isabelle. [snip] ...but impossible to formalize in Isabelle, for lack of dependent types.
```
What do people mean by Isabelle here? Are we talking about Isabelle-HOL or something? Can there be an Isabelle-DTT?

#### [Kevin Buzzard (Oct 03 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135128950):
```quote
 But I miss a lot the automatisation level of Isabelle, which is way better than anything there is currently in Lean.
```
We need a plan for this. I am not sure I would be capable of supervising an MSc student to write tactics for automation. Of course it should probably all wait for Lean 4. @**Johannes Hölzl** will you be supervising any more MSc students in the near future?

#### [Patrick Massot (Oct 03 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135128967):
I'm not sure MSc is enough

#### [Kevin Buzzard (Oct 03 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135129210):
Is writing a bunch of killer automation in Lean a PhD project for a CS student? And would you be able to get a post-doc afterwards?

#### [Patrick Massot (Oct 03 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135129236):
It seems like Johannes, Rob and Jasmin are working on Lean automation and don't feel like this is MSc student level...

#### [Patrick Massot (Oct 03 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135129248):
It seems to be more like a ERC grant proposal project

#### [Sebastien Gouezel (Oct 03 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135130316):
```quote
```quote
There are very serious limitations in Isabelle. [snip] ...but impossible to formalize in Isabelle, for lack of dependent types.
```
What do people mean by Isabelle here? Are we talking about Isabelle-HOL or something? Can there be an Isabelle-DTT?
```
Yes, I am talking about Isabelle/HOL.

#### [Sebastien Gouezel (Oct 03 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/finset%20sup/near/135130413):
You can develop any logic in Isabelle, this is a framework, in a sense. But Isabelle/HOL is the most developed (and usable, and used) instance.

