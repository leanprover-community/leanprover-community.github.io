---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/70299Functioncomposition.html
---

## [new members](index.html)
### [Function composition](70299Functioncomposition.html)

#### [Kevin Buzzard (Sep 17 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Function%20composition/near/134102575):
So I wondered if one could just prove Guillermo's `for_all_not_all` using function composition. In some sense this is one of the disadvantages of the currying approach: if a mathematician has functions $$(A\times B)\to C$$ and $$C\to D$$ they can just compose them and get a function $$(A\times B)\to D$$. This is a bit harder in the curried approach, because `A -> B -> C` is `A -> (B -> C)` and `C` is a bit more embedded than function composition would like. I wrote a blog post about it once: https://xenaproject.wordpress.com/2018/05/19/function-composition/  containing Sebastian's cool `((∘) ∘ (∘))` trick. But to apply this trick in Guillermo's situation one needs to get this working for pi types. Here's a formalisation of the situation:

```lean
variables (AA BB CC DD : Type) (ff : AA → BB → CC) (gg : CC → DD)

definition comp : AA → BB → DD := λ a b, gg (ff a b)

definition comp' : AA → BB → DD := ((∘) ∘ (∘)) gg ff -- cool thing Sebastian showed me

example : comp = comp' := rfl

variables {A C D : Type} {B : A → Type} (f : Π (a : A), (B a → C)) (g : C → D)

definition picomp : Π (a : A), (B a → D) := λ a b, g $ f a b

definition picomp' : Π (a : A), (B a → D) := _ g f -- Is there a cool thing which can go here?

def boring : (C → D) → (Π (a : A), (B a → C)) → (Π (a : A), (B a → D)) := λ g f a b, g (f a b) 

definition picomp'' : Π (a : A), (B a → D) := boring g f -- not cool
```

I want to "compose f and g". Function `picomp` does this explicitly, but it really looks like `g $ f` is the composition and that I should be able to remove `a` and `b` completely. Basically I want to define the function `boring` just using `function.comp`. Is this possible? @**Sebastian Ullrich** is there a trick?

#### [Johan Commelin (Sep 17 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Function%20composition/near/134103193):
Close, but not so close: `example : Π (a : A), (B a → D) := λ _, g ∘ f _`

#### [Kevin Buzzard (Sep 17 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Function%20composition/near/134103346):
The question isn't really even well-posed. I want no lambdas, but in some sense the boring answer does this -- and function.comp's definition uses lambdas...

