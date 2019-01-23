---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/77274Awesomestuff.html
---

## Stream: [general](index.html)
### Topic: [Awesome stuff](77274Awesomestuff.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 08 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Awesome%20stuff/near/123464026):
My mind was just blown by how useful `has_coe_to_fun` is. I constructed a morphism between applicative functors:

```
variables (f : Type u → Type v) [applicative f]
variables (g : Type u → Type w) [applicative g]

structure applicative_morphism : Type (max (u+1) v w) :=
  (F : ∀ {α : Type u}, f α → g α)
  (preserves_pure' : ∀ {α : Type u} (x : α), F (pure x) = pure x)
  (preserves_seq' : ∀ {α β : Type u} (x : f (α → β)) (y : f α), F (x <*> y) = F x <*> F y)
```

and defined the following instance:

```
instance : has_coe_to_fun (applicative_morphism f g) :=
{ F := λ _, ∀ {α}, f α → g α,
  coe := λ m, m.F }
```

It's already pretty cool that, given `x : f int` and `m : applicative_morphism f g` I can write `f x` to just apply it. What really blew my mind is that I can write `@f int x` to make the `{α : Type u}` of `F` explicit.

