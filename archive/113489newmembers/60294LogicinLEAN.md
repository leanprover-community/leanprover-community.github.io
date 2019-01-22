---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/60294LogicinLEAN.html
---

## [new members](index.html)
### [Logic in LEAN](60294LogicinLEAN.html)

#### [Sean G McCain (Nov 01 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Logic%20in%20LEAN/near/136955882):
Is someone able to send me a private message regarding first order logic in LEAN? I am working a homework that requires it and it is difficult, for LEAN is very new to me.

#### [Bryan Gin-ge Chen (Nov 02 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Logic%20in%20LEAN/near/136956419):
If you have specific questions you should feel free to ask them (publicly) in this thread. Have you seen the relevant chapters of [Logic & Proof](http://avigad.github.io/logic_and_proof/first_order_logic.html)?

#### [Sean G McCain (Nov 02 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Logic%20in%20LEAN/near/136956754):
I have seen them, and that is the book that I use for reference. However, I am yet to be able to figure out the issue.

#### [Sean G McCain (Nov 02 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Logic%20in%20LEAN/near/136956856):
Here is the code I have: 
I am needing to prove the statement following example:
     
  section
         variable U : Type
         variables A B : U → Prop

         example : (∀ x, A x ∧ B x) → ∀ x, A x :=
         assume (x : U),
         assume h1 :∀ x, A x ∧ B x,
         assume h2 : ∀ x, A x,
         assume y,
         have hy : A y, from h2 y,
         show ∀ y, A y, from h2 y (hy) 
       end

Here is the error  I am getting:  
However, A y is a function, so I dont understand this error. 

function expected at
  h2 y
term has type
  A y

#### [Chris Hughes (Nov 02 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Logic%20in%20LEAN/near/136956965):
`A y` is not a function, it's a `Prop`.

#### [Chris Hughes (Nov 02 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Logic%20in%20LEAN/near/136956985):
`A` is a function.

#### [Sean G McCain (Nov 02 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Logic%20in%20LEAN/near/136957170):
So, what would need to follow the 'from'

#### [Bryan Gin-ge Chen (Nov 02 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Logic%20in%20LEAN/near/136957338):
I would reconsider the strategy for proving this. In particular, your `assume` statements are out-of-order / some of them are unnecessary.

#### [Bryan Gin-ge Chen (Nov 02 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Logic%20in%20LEAN/near/136957526):
As a hint, `assume h1:∀ x, A x ∧ B x` should come first, and then `assume x:U`. You can see this by breaking down what you're trying to prove from left to right. Remember that you can use an underscore `_` and lean will tell you the type of what you're still missing.

#### [Sean G McCain (Nov 02 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Logic%20in%20LEAN/near/136958036):
After doing so, I am given more errors than before.

#### [Andrew Ashworth (Nov 02 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Logic%20in%20LEAN/near/136958542):
add more underscores, the compiler will tell you what you're doing wrong

#### [Bryan Gin-ge Chen (Nov 02 2018 at 00:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Logic%20in%20LEAN/near/136958565):
Maybe this will help. Let me go through the last example from section 9.2 of Logic & Proof which is very similar. 

Let's start by just putting an underscore in for the entire proof:
```lean
variable U : Type
variables A B : U → Prop

example : (∀ x, A x) → (∀ x, B x) → (∀ x, A x ∧ B x) :=
_ 
/-
don't know how to synthesize placeholder
context:
U : Type,
A B : U → Prop
⊢ (∀ (x : U), A x) → (∀ (x : U), B x) → ∀ (x : U), A x ∧ B x
-/
```
No surprise here, lean just restates the goal for us. We see from the arrows in the goal that it is a function. To construct a function we should begin by assuming things:
```lean
example : (∀ x, A x) → (∀ x, B x) → (∀ x, A x ∧ B x) :=
example : (∀ x, A x) → (∀ x, B x) → (∀ x, A x ∧ B x) :=
assume hA,
_
/-
don't know how to synthesize placeholder
context:
U : Type,
A B : U → Prop,
hA : ∀ (x : U), A x
⊢ (∀ (x : U), B x) → ∀ (x : U), A x ∧ B x
-/
```
There's still an error, but we see that it's telling us that we're making progress. Indeed, lean actually has inferred the right type for `hA`, which we can put back in if we want to be fully explicit. The goal is still a function so we continue assuming:
```lean
example : (∀ x, A x) → (∀ x, B x) → (∀ x, A x ∧ B x) :=
assume hA : (∀ x, A x),
assume hB,
_
/-
don't know how to synthesize placeholder
context:
U : Type,
A B : U → Prop,
hA : ∀ (x : U), A x,
hB : ∀ (x : U), B x
⊢ ∀ (x : U), A x ∧ B x
-/
```
So that's what `hB` is. We still have a function (the goal depends on a bound variable) so let's try assuming one more time:
```lean
example : (∀ x, A x) → (∀ x, B x) → (∀ x, A x ∧ B x) :=
assume hA: (∀ x, A x) ,
assume hB: (∀ x, B x),
assume y,
_
/-
don't know how to synthesize placeholder
context:
U : Type,
A B : U → Prop,
hA : ∀ (x : U), A x,
hB : ∀ (x : U), B x,
y : U
⊢ A y ∧ B y
-/
```
Now we're in a place where we have a term that we can construct by applying hA and hB. The final answer:
```lean
example : (∀ x, A x) → (∀ x, B x) → (∀ x, A x ∧ B x) :=
assume hA,
assume hB,
assume y,
⟨hA y, hB y⟩
```
Which is equivalent to the proof given in the book. 

To summarize, if you look carefully at the type errors you get, they may help guide you to the proof you're looking for.

