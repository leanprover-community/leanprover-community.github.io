---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/74349provingequalityofstructures.html
---

## Stream: [general](index.html)
### Topic: [proving equality of structures](74349provingequalityofstructures.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 16 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20equality%20of%20structures/near/126644596):
Is there a tactic or something that's like `apply subtype.eq`, but works for a general structure? Or do I have to write down the equality lemma manually?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (May 16 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20equality%20of%20structures/near/126644607):
`congr`, which doesn't always work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 16 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20equality%20of%20structures/near/126644746):
I thought about `congr`, but my goal is literally `e1 = e2` and `congr` made no progress. Somehow I need to eta expand each side first, and then apply `congr`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 16 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20equality%20of%20structures/near/126646065):
From the changelog:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 16 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20equality%20of%20structures/near/126646068):
"simp now reduces equalities c a_1 ... a_n = c b_1 ... b_n to a_1 = b_1 /\ ... /\ a_n = b_n if c is a constructor. This feature can be disabled using simp {constructor_eq := ff}"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (May 16 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20equality%20of%20structures/near/126646116):
of course, simp might do other things as well...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Nicholas Scheel (May 16 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20equality%20of%20structures/near/126654166):
hm I asked a similar question a while ago, but it was about a lemma not a tactic: https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/structure.20equality.20from.20parts/near/124033713

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (May 16 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20equality%20of%20structures/near/126654471):
Yes, same goal. I managed to write my lemma by copying `subtype.eq` very carefully.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (May 17 2018 at 03:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20equality%20of%20structures/near/126674624):
Someone (yikes, I've forgotten who, and my copy doesn't record the name) wrote for me a tactic called `congr_struct` that sometimes is useful for proving equalities of structures. In the presence of fields with dependencies on earlier fields it create new `heq` goals, which isn't always what you want.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (May 17 2018 at 03:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20equality%20of%20structures/near/126674631):
There's a copy at <https://github.com/semorrison/lean-tidy/blob/master/src/tidy/congr_struct.lean> (you can just remove the import if you want to steal a copy).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (May 17 2018 at 03:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20equality%20of%20structures/near/126674640):
If anyone wants it I can PR it into mathlib. I'm not actually using it anywhere myself at the moment.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (May 17 2018 at 03:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20equality%20of%20structures/near/126674691):
I end up writing my own lemmas, e.g. of the form
````
structure NaturalTransformation (F G : C ↝ D) : Type (max (u+1) v) :=
  (components: Π X : C, (F +> X) ⟶ (G +> X))
  (naturality: ∀ {X Y : C} (f : X ⟶ Y), (F &> f) ≫ (components Y) = (components X) ≫ (G &> f))

infixr ` ⟹ `:50  := NaturalTransformation 

lemma NaturalTransformations_componentwise_equal
  (α β : F ⟹ G)
  (w : ∀ X : C, α.components X = β.components X) : α = β :=
  begin
    induction α with α_components α_naturality,
    induction β with β_components β_naturality,
    have hc : α_components = β_components := funext w,
    subst hc
  end
````

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (May 17 2018 at 03:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20equality%20of%20structures/near/126674692):
(and I have lots of these, unfortunately)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 17 2018 at 04:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20equality%20of%20structures/near/126676097):
Mathlib is calling these lemmas "extensionality" theorems, for use with Simon's `ext` tactic. The fastest way to prove them is to case on both structures, then apply `congr` and other extensionality theorems to the resulting goals

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 17 2018 at 04:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20equality%20of%20structures/near/126676208):
I don't have the necessary stuff to test your example, but I think it is possible to have a proof that looks something like `by cases α; cases β; congr; exact funext w`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (May 17 2018 at 05:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proving%20equality%20of%20structures/near/126679010):
Yes, that proof works too.

