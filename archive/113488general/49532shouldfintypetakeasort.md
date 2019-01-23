---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/49532shouldfintypetakeasort.html
---

## Stream: [general](index.html)
### Topic: [should fintype take a sort?](49532shouldfintypetakeasort.html)

---

#### [Chris Hughes (Aug 06 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/should%20fintype%20take%20a%20sort%3F/near/130982613):
This instance would be possible if `fintype` took a sort instead of a Type. Is it worth changing?
`instance (p : fin 3 → Prop) [decidable_pred p] : fintype (Π a, p a → fin 3) := by apply_instance`

#### [Mario Carneiro (Aug 06 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/should%20fintype%20take%20a%20sort%3F/near/130982981):
I thought about it, I have also seen this come up, but I don't know a clean way to do it without making lots of later stuff harder

#### [Chris Hughes (Aug 06 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/should%20fintype%20take%20a%20sort%3F/near/130983001):
What would be harder?

#### [Mario Carneiro (Aug 06 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/should%20fintype%20take%20a%20sort%3F/near/130983027):
you have to ulift somewhere, and this will affect proofs that don't care about Prop

#### [Mario Carneiro (Aug 06 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/should%20fintype%20take%20a%20sort%3F/near/130983244):
of course another way to solve the particular problem you show is to have a second pi instance for Props

#### [Chris Hughes (Aug 06 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/should%20fintype%20take%20a%20sort%3F/near/130983543):
I forgot that `list` didn't take a `Sort`.

#### [Mario Carneiro (Aug 06 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/should%20fintype%20take%20a%20sort%3F/near/130983761):
Actually, I'm not sure it can be done at all, assuming that `list` and `finset` stay as is

#### [Mario Carneiro (Aug 06 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/should%20fintype%20take%20a%20sort%3F/near/130983876):
What would be the type of `fintype`? If it is `Sort u -> Type u` then it bumps the universe level in unwanted circumstances (i.e. `fintype nat : Type 1`), and if it is `Sort u -> Sort (max 1 u)` then you can't define it

#### [Mario Carneiro (Aug 06 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/should%20fintype%20take%20a%20sort%3F/near/130984035):
since `Sort (max 1 u) = Sort (?+1)` is unsolvable (you would need a `pred u` function but that doesn't exist)

#### [Chris Hughes (Aug 06 2018 at 19:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/should%20fintype%20take%20a%20sort%3F/near/130990940):
Is there any reason not to just make everything a Sort, just in case some random thing like this comes up where it's useful?

#### [Simon Hudon (Aug 06 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/should%20fintype%20take%20a%20sort%3F/near/130994870):
I think the main thing has to do with elimination. If your type is`Sort 0`, there's a special case that you can only eliminate to `Sort 0`. Otherwise, in `Sort 1`, you can eliminate anywhere you like.

#### [Simon Hudon (Aug 06 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/should%20fintype%20take%20a%20sort%3F/near/130995291):
Btw, your instance type checks for me. Are you sure your issues have to do with universes?

#### [Chris Hughes (Aug 06 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/should%20fintype%20take%20a%20sort%3F/near/130995344):
It type checks, but it can't synthesize the instance

#### [Chris Hughes (Aug 06 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/should%20fintype%20take%20a%20sort%3F/near/130995413):
But if there was an instance saying `Pi p : Prop, fintype p` it would synthesize the instance from `pi.fintype`

#### [Simon Hudon (Aug 06 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/should%20fintype%20take%20a%20sort%3F/near/130996568):
I think you could make it work with an instance like this:

```lean
instance pi.fintype' {α : Prop} {β : α → Type*}
  [decidable α] [∀a, fintype (β a)] : fintype (Πa, β a) :=
```

#### [Chris Hughes (Aug 06 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/should%20fintype%20take%20a%20sort%3F/near/130996873):
```quote
I think the main thing has to do with elimination. If your type is`Sort 0`, there's a special case that you can only eliminate to `Sort 0`. Otherwise, in `Sort 1`, you can eliminate anywhere you like.
```
So that makes sense for making inductive types Types rather than sorts, but for functions defined on an arbitrary Type, I don't see a downside.

#### [Chris Hughes (Aug 06 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/should%20fintype%20take%20a%20sort%3F/near/130997539):
I should probably PR both of these
```lean
instance decidable_eq_pfun_fintype (P : Prop) [decidable P] (α : P → Type*) [Π hp : P, fintype (α hp)] 
  [Π hp : P, decidable_eq (α hp)] : decidable_eq (Π hp : P, α hp) :=
λ f g, if hp : P then decidable_of_iff (f hp = g hp) (⟨λ h, funext $ λ _, h, λ h, congr_fun h _⟩)
else is_true (funext $ λ h, (hp h).elim)

instance fintype_pfun (P : Prop) [decidable P] (α : P → Type*) [Π hp : P, fintype (α hp)] 
  [Π hp : P, decidable_eq (α hp)] : fintype (Π hp : P, α hp) :=
if hp : P then fintype.of_equiv (α hp) ⟨λ a _, a, λ f, f hp, λ _, rfl, λ _, rfl⟩
else ⟨finset.singleton (λ h, (hp h).elim), λ x, by simp [hp, funext_iff]⟩

```

#### [Simon Hudon (Aug 06 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/should%20fintype%20take%20a%20sort%3F/near/130998223):
```quote
but for functions defined on an arbitrary Type, I don't see a downside.
```

I agree. Although, I find that universe constraints have a way of propagating to infect every definition once you have one. Being more polymorphic seems easier said than done.

