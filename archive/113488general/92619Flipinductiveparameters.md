---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/92619Flipinductiveparameters.html
---

## Stream: [general](index.html)
### Topic: [Flip inductive parameters](92619Flipinductiveparameters.html)

---

#### [Nicholas Scheel (Jun 05 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Flip%20inductive%20parameters/near/127578848):
Is there a way to flip the `Type` and `ℕ` parameters around so I can make this a functor?
```
inductive Bezier (β : Type) : ℕ → Type
| point : β → Bezier 0
| curve : Π {n}, Bezier n → β → Bezier (n+1)
```

#### [Simon Hudon (Jun 05 2018 at 04:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Flip%20inductive%20parameters/near/127578914):
You can do 

```lean
def Bezier' (n : ℕ) (β : Type) := Bezier β n
```

#### [Simon Hudon (Jun 05 2018 at 04:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Flip%20inductive%20parameters/near/127578955):
And make `Bezier'` a functor (or switch the names)

#### [Nicholas Scheel (Jun 05 2018 at 04:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Flip%20inductive%20parameters/near/127578967):
okay, that should work :)

#### [Nicholas Scheel (Jun 05 2018 at 05:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Flip%20inductive%20parameters/near/127579887):
wat
```
invalid type ascription, term has type
  g <$> @Bezier'.curve α n (@pure (Bezier' n) (@Bezier'.has_pure n) α x) x =
    @Bezier'.curve β n (g <$> @pure (Bezier' n) (@Bezier'.has_pure n) α x) (g x)
but is expected to have type
  g <$> @Bezier'.curve α n (@pure (Bezier' n) (@Bezier'.has_pure n) α x) x = ?m_1
```

#### [Simon Hudon (Jun 05 2018 at 05:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Flip%20inductive%20parameters/near/127579928):
try `set_option pp.all true` before your proof. It will display all the implicit parameters, universe levels and expand notations

#### [Nicholas Scheel (Jun 05 2018 at 05:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Flip%20inductive%20parameters/near/127580056):
aha, thank you! it was using `applicative.to_functor` and applicative's default map :face_palm:

#### [Simon Hudon (Jun 05 2018 at 05:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Flip%20inductive%20parameters/near/127580100):
Do you by any chance have a `functor` and a `applicative` instance available in your context?

#### [Simon Hudon (Jun 05 2018 at 05:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Flip%20inductive%20parameters/near/127580101):
If you're used to Haskell, you'll see that Lean does not ensure that instances are globally unique

#### [Nicholas Scheel (Jun 05 2018 at 05:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Flip%20inductive%20parameters/near/127580114):
I get that :) and yes, I have `functor` and `applicative`, working on `is_lawful_applicative`

#### [Simon Hudon (Jun 05 2018 at 05:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Flip%20inductive%20parameters/near/127580157):
I suggest you make sure that only one is available at any time

