---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/96400quotientsandliftsforfunctionsofarbitraryarity.html
---

## Stream: [maths](index.html)
### Topic: [quotients and lifts for functions of arbitrary arity](96400quotientsandliftsforfunctionsofarbitraryarity.html)

---


{% raw %}
#### [ William DeMeo (Dec 02 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotients%20and%20lifts%20for%20functions%20of%20arbitrary%20arity/near/150709555):
I'm trying to learn how to implement general quotient structures.  Unfortunately, I've only been able to figure out how to lift unary operations.  How does one lift operations of arbitrary arity?

More specifically, here's what I'm trying to do. 

Given a type $$\alpha$$, and an "arity" type $$\rho$$, an operation on $$\alpha$$ of arity $$\rho$$ has the following type signature:
$$f : (\rho \to \alpha) \to \alpha$$. 

Now suppose I have an equivalence relation $$r : \alpha \to \alpha \to \mathsf{Prop}$$, and I want to lift $$f$$ to a $$\rho$$-ary operation $$\tilde{f} : (\rho \to \alpha/r) \to \alpha/r$$.  That is, $$\tilde{f}$$ should be a $$\rho$$-ary operation on the quotient $$\alpha / r$$.  It's obvious how to express this mathematically:

$$\tilde{f} (a/[[r]]) = (f a)/r$$,

where $$[[ r ]]$$ is the binary relation on $$\rho \to \alpha$$ induced by $$r$$.  That is, $$a \mathrel{[[ r ]]} b$$ iff $$\forall i, (a i) \mathrel{r} (b i)$$.  

For example, if $$f$$ is $$n$$-ary, then $$\tilde{f}$$ maps an $$n$$-tuple $$(a_0/r, \ldots, a_{n-1}/r)$$ of $$r$$-classes to the $$r$$-class $$f(a_0, \ldots, a_{n-1})/r$$.

I got this to work when $$f$$ is unary (so, $$f : \alpha \to \alpha$$), by first defining the projection $$\pi f : \alpha \to \alpha/r$$ as `quot.mk r (f a)`, and then using the built in `quot.lift`, defined in quot.lean of the standard library.  (The code for that is below, but it's not pretty.)

Unfortunately, this doesn't work for higher arity operations because quot.lift expects a relation $$r : \alpha \to \alpha \to \mathsf{Prop}$$ and a proof of $$\forall a b,  a \mathrel{ r } b \to (f a)/r = (f b)/r$$.  But in the higher arity case, to say that the operation  $$f : (\rho \to \alpha) \to \alpha$$ "respects" $$r$$ means the following:

$$\forall (a b : \rho \to \alpha), (\forall i, r (a i) (b i)) \to (f a)/r = (f b)/r$$

If you provide quot.lift with that as the proof of "respecting r", the resulting lift will not be what we want.

Any ideas, pointers, suggestions would be much appreciated.  Thanks!


Here's the code for the unary case.  There's probably an easier way to do this, and suggestions are welcome... but I'm more interested in the general case.

```lean
  parameters {α : Type*} {ρ : Type*} 
  local notation a`/`r := quot.mk r a

  def πᵤ (f : α → α) (r : α → α → Prop) : α → quot r := λ a, (f a) / r

  def compatible_unary (f : α → α) (r : α → α → Prop) := ∀ a b, r a b → r (f a) (f b)

  lemma resp_proj_of_compatible_unary 
  (f : α → α) (r : α → α → Prop) (h : compatible_unary f r) :
  ∀ a b, r a b → (f a)/r = (f b)/r :=  
  assume a b (h₀ : r a b), 
  have h₃ : r (f a) (f b), from h a b h₀, 
  show (f a)/r = (f b)/r, from quot.sound h₃

  def lift_proj (f : α → α) (r : α → α → Prop) (h : compatible_unary f r) : 
  quot r → quot r := 
  quot.lift (πᵤ  f r) (resp_proj_of_compatible_unary f r h) 
```

#### [ Chris Hughes (Dec 02 2018 at 07:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotients%20and%20lifts%20for%20functions%20of%20arbitrary%20arity/near/150712210):
One way of doing this is to put a relation on $$\rho \rightarrow \alpha$$ defined as $$\lambda x y, \forall a : \alpha, r (x (a)) (y( a))$$. I don't think you can define a function of this type `quotient.lift_onₙ (x : Π a : α, quotient (s a)) 
  (f : (Π a : α, β a) → γ) (h : ∀ x₁ x₂ : Π a, β a, 
  (∀ a, x₁ a ≈ x₂ a) → f x₁ = f x₂) : γ` without choice though. There is something in `data.fintype` that let's you do it computably when your indexing type is finite, but the fact that that's only defined on fintypes suggestsit might not be possible on infinite types.

#### [ Reid Barton (Dec 02 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotients%20and%20lifts%20for%20functions%20of%20arbitrary%20arity/near/150725987):
@**William DeMeo** You can use `quotient.choice` in mathlib to turn a product of quotients into a quotient of the product, and then `lift` on that to define a function.

#### [ Reid Barton (Dec 02 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotients%20and%20lifts%20for%20functions%20of%20arbitrary%20arity/near/150725999):
As far as I know you can't do this computably/without axioms, though it would be possible to implement by extending Lean.

#### [ Kevin Buzzard (Dec 02 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotients%20and%20lifts%20for%20functions%20of%20arbitrary%20arity/near/150726048):
By "without axioms" you just mean "without some standard axioms which are inbuilt into Lean but which break computability", right?

#### [ Reid Barton (Dec 02 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotients%20and%20lifts%20for%20functions%20of%20arbitrary%20arity/near/150726086):
Yes

#### [ William DeMeo (Dec 02 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotients%20and%20lifts%20for%20functions%20of%20arbitrary%20arity/near/150727665):
@**Chris Hughes** Great, thanks for the hints!  I will look at data.fintype.  I'd like to be able to do this *computably* at least for finitary operations.  (By the way, just to be sure I understand your suggestions, I think you meant to put $$\rho$$ in place of $$\alpha$$ in the two places where $$\alpha$$ appears... correct?)  Thanks again for your help!

#### [ Chris Hughes (Dec 02 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotients%20and%20lifts%20for%20functions%20of%20arbitrary%20arity/near/150727708):
Yes I did mean to put rho instead of alpha

#### [ William DeMeo (Dec 02 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotients%20and%20lifts%20for%20functions%20of%20arbitrary%20arity/near/150727794):
```quote
@**William DeMeo** You can use `quotient.choice` in mathlib to turn a product of quotients into a quotient of the product, and then `lift` on that to define a function.
```
 Thanks @**Reid Barton** , maybe I'll try that if after I get it to work computably for fintype.

#### [ Reid Barton (Dec 02 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotients%20and%20lifts%20for%20functions%20of%20arbitrary%20arity/near/150727839):
https://github.com/leanprover/mathlib/commit/ddbb81389b6d6cd3d0395f474896dcd59e1ed9e4

#### [ Reid Barton (Dec 02 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotients%20and%20lifts%20for%20functions%20of%20arbitrary%20arity/near/150727841):
added both `quotient.choice` and a computable `finset` version

#### [ William DeMeo (Dec 02 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotients%20and%20lifts%20for%20functions%20of%20arbitrary%20arity/near/150729558):
```quote
added both `quotient.choice` and a computable `finset` version
```
 Awesome!  Thanks @**Reid Barton**  I'll see if I can use those types to do exactly what I want.  If not, I'll have to roll my own, but it's good to see these examples that show how things should be done.


{% endraw %}
