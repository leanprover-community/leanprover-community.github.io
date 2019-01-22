---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/08643partialordernoobquestions.html
---

## [general](index.html)
### [partial order noob questions](08643partialordernoobquestions.html)

#### [Kevin Buzzard (Sep 04 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20order%20noob%20questions/near/133302203):
OK so I appear to be engaging with orders for the first time in my Lean career.

1) Is this a good instance?

```lean
instance (X) [h : partial_order X] (p : X → Prop) : partial_order ({x : X // p x}) := ...
```

[I still feel very ill-equipped to answer such questions.]

2) Stupid class noob question: what am I doing wrong here:

```lean
definition subtype.partial_order (X) [h : partial_order X] (p : X → Prop) : partial_order ({x : X // p x}) :=
{ le := λ a b, (a : X) ≤ b,
  le_refl := λ a, h.le_refl (a : X), -- error
/-
invalid field notation, function 'partial_order.le_refl'
 does not have explicit argument with type (partial_order ...)
-/
  le_trans := sorry,
  le_antisymm := sorry
  }
```

This "invalid field notation" stuff is something I see a lot, because I don't understand fields very well (indeed in an earlier post today I managed to fail to even remember the word "field"). How am I supposed to prove `le_refl` like a boss?

3) Is it called `subtype.partial_order` or `partial_order.subtype` or something else? Is it already there?

#### [Kevin Buzzard (Sep 04 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20order%20noob%20questions/near/133302294):
`  le_refl := λ a, le_refl (a : X),` works. Why does what I did not work?

#### [Kenny Lau (Sep 04 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20order%20noob%20questions/near/133302298):
2) don't use projection (the `x.y` notation) if `x` is an instance of a class
3) subrel

#### [Kenny Lau (Sep 04 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20order%20noob%20questions/near/133302306):
and in particular 2) don't name instances of classes

#### [Kenny Lau (Sep 04 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20order%20noob%20questions/near/133302344):
i.e. `[h : partial_order X]` is wrong in the first place

#### [Kevin Buzzard (Sep 04 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20order%20noob%20questions/near/133302433):
`subrel` just gives me the relation on the subtype, not that it is also a partial order.

#### [Kevin Buzzard (Sep 04 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20order%20noob%20questions/near/133302457):
I wanted to use projection because I wanted to prove `le_refl` by "use X's le_refl"

#### [Kenny Lau (Sep 04 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20order%20noob%20questions/near/133302524):
I don't think it's in mathlib

#### [Kevin Buzzard (Sep 04 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20order%20noob%20questions/near/133302553):
Kenny, I have a partial order structure on `submodule R M`, the type of $$R$$-submodules of $$M$$. I want a partial order structure on the subtype of this consisting of submodules which are contained in a given submodule `N`. I was going to make this general subtype nonsense above and then use it to get an induced partial order on this subtype, and then prove that this was order isomorphic to `submodule R N`. Does this sound sensible?

#### [Kevin Buzzard (Sep 04 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20order%20noob%20questions/near/133302605):
I'm currently trying to work out a way of doing this which won't make Mario's head hurt when he sees the PR.

#### [Kevin Buzzard (Sep 04 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20order%20noob%20questions/near/133302626):
Then I get an order embedding `submodule R N -> submodule R M` and I can deduce that `N` is Noetherian from the already-proved theoerem that Noetherian iff > is well-founded.

#### [Kenny Lau (Sep 04 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20order%20noob%20questions/near/133302646):
that sounds very sensible

#### [Kevin Buzzard (Sep 04 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20order%20noob%20questions/near/133302845):
?! `#print partial_order` gives `partial_order.le_antisymm : ∀ {α : Type u} [c : partial_order α] (a b : α), a ≤ b → b ≤ a → a = b` with `a` and `b` explicit, but hovering over `@le_antisymm` in the middle of the definition I'm writing gives me `le_antisymm : ∀ {α : Type u} [_inst_1 : partial_order α] {a b : α}, a ≤ b → b ≤ a → a = b` with `a` and `b` implicit. Who am I to believe?

#### [Kenny Lau (Sep 04 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20order%20noob%20questions/near/133302925):
both

#### [Kevin Buzzard (Sep 04 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20order%20noob%20questions/near/133302988):
```lean
instance subtype.partial_order (X) [partial_order X] (p : X → Prop) : partial_order ({x : X // p x}) :=
{ le := λ a b, (a : X) ≤ b,
  le_refl := λ a, le_refl (a : X),
  le_trans := λ a b c hab hbc, @le_trans X _ a b c hab hbc,
  le_antisymm := λ a b hab hba, subtype.eq $ @le_antisymm X _ _ _ hab hba
}
```

So I still don't know if this should be an instance. Should I just suck it and see?

#### [Kevin Buzzard (Sep 04 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20order%20noob%20questions/near/133303450):
and the presence of `@`s makes me feel like I'm missing a trick.

#### [Kenny Lau (Sep 04 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20order%20noob%20questions/near/133303540):
this is my code in the `temp` file in our stacks project:
```lean
instance : partial_order {x // p x} :=
{ le := subrel (≤) p,
  le_refl := λ x, le_refl x,
  le_trans := λ x y z, le_trans,
  le_antisymm := λ x y hx hy, subtype.eq $ le_antisymm hx hy }
```

#### [Kevin Buzzard (Sep 04 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20order%20noob%20questions/near/133304072):
heh, so I switched to @ because I couldn't get `le_antisymm` working, and after the switch I still couldn't, and then I realised  `subtype.eq` was missing, and then I didn't switch back :-)

#### [Kevin Buzzard (Sep 04 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20order%20noob%20questions/near/133304099):
`le_refl := λ x, le_refl x` I am surprised this works. How does Lean know which `le_refl` to use?

#### [Kevin Buzzard (Sep 04 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/partial%20order%20noob%20questions/near/133331784):
This is kind of annoying. This `order_iso` stuff just seems to work with not an actual partial order or preorder or anything, but any binary relation at all. So I was expecting to see a lemma saying "if X and Y are equivalent partial orders, i.e. they have the same <=, then they have the same < too", but somehow this isn't covered by what `order_iso` does, despite its name.

