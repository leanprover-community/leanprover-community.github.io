---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/15802functionextensionalityandtransports.html
---

## Stream: [new members](index.html)
### Topic: [function extensionality and transports](15802functionextensionalityandtransports.html)

---


{% raw %}
#### [ Edward Ayers (Aug 08 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/function%20extensionality%20and%20transports/near/131125621):
```lean
lemma my_ext 
    : ∀ (α :Type) 
      (P Q : α -> Type) 
      (f : Π (a : α), P a ) 
      (g : Π (a : α), Q a) 
      (p : ∀ (a : α), P a = Q a), 
        (∀ (a : α), ((p a) ▸ (f a)) = g a) 
        -> ((funext p) ▸ f) = g 
    := by sorry
```
Some questions:
1. How do I get the transport triangles to work? I get the same error if I reverse the arguments so I don't even know if I'm using it the right way round
2. How do I prove it?
3. Is it crazy to want to do this?

#### [ Chris Hughes (Aug 08 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/function%20extensionality%20and%20transports/near/131125836):
The triangles are for `eq.subst` which can only make proofs, not data. You have to use `eq.rec` I think. You could also use heq `==`

#### [ Mario Carneiro (Aug 08 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/function%20extensionality%20and%20transports/near/131126052):
```lean
lemma my_ext (α :Type)
  (P Q : α -> Type)
  (f : Π (a : α), P a )
  (g : Π (a : α), Q a)
  (p : ∀ (a : α), P a = Q a) :
    (∀ (a : α), (eq.rec_on (p a) (f a) : Q a) = g a)
    -> (eq.rec_on (funext p : P = Q) f : Π (a : α), Q a) = g :=
by cases (funext p : P = Q); exact funext
```


{% endraw %}
