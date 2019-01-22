---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/47318Exerciseschapter4xrr.html
---

## [new members](index.html)
### [Exercises chapter 4 - α → (( ∀ x: α, r ) ↔ r)](47318Exerciseschapter4xrr.html)

#### [Carlesso Diego (Dec 04 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Exercises chapter 4 - α → (( ∀ x: α, r ) ↔ r)/near/150837580):
Hello! First time I write here! I'm trying to learn Lean step by step following the online tutorial "theorem proving in Lean" doing as many exercises as I can. 
At the moment I'm having a problem (probably more on the logic part of the thing) on the first one of exercise 2 in chapter 4:
α → (( ∀ x: α, r ) ↔ r)

theorem e1: α → (( ∀ x: α, r ) ↔ r) :=
assume y:α,
iff.intro
(assume h: (∀ x, r),
show r, from h y
)
-- wrong from now on
(assume hr: r,
assume x : α,
assume hyr : (∀ x , r),
show (∀ x: α , r), from hyr
)

First of all, I don't know if assuming y:α solve the "α →" part, but I'm struggling in the second part of the iff.intro (I think that the first part is correct) 
the error is : 

" type mismatch at application
{mp := λ (h : α → r), show r, from h y, mpr := λ (hr : r) (x : α) (hyr : α → r), show α → r, from hyr}
term
λ (hr : r) (x : α) (hyr : α → r), show α → r, from hyr
has type
r → α → (α → r) → α → r
but is expected to have type
r → α → r "

And I understand why it returns that error, but, how am I supposed to show (∀ x: α , r) from r otherwise? It's probably something stupid I'm missing but as stupid as it is I can't see it. Looking at the others in ex2 I think it's probably something I'm getting wrong in bringing outside a universal quantifier.
Also, I've never used Zulip or something like that, so let me know if I did something wrong.

#### [Kevin Buzzard (Dec 04 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Exercises chapter 4 - α → (( ∀ x: α, r ) ↔ r)/near/150837685):
For Zulip -- if you write your code between triple backticks ` ``` ` then it gets formatted nicely. Even better, if you write ` ```lean ` for the top triple backtick then you get syntax highlighting as well.

#### [Kevin Buzzard (Dec 04 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Exercises chapter 4 - α → (( ∀ x: α, r ) ↔ r)/near/150837694):
```lean
theorem e1: α → (( ∀ x: α, r ) ↔ r) :=
assume y:α,
iff.intro
(assume h: (∀ x, r),
show r, from h y
)
-- wrong from now on
(assume hr: r,
assume x : α,
assume hyr : (∀ x , r),
show (∀ x: α , r), from hyr
)
```

#### [Kevin Buzzard (Dec 04 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Exercises chapter 4 - α → (( ∀ x: α, r ) ↔ r)/near/150837731):
But your code doesn't run for me -- can you post some fully working example so I can get it to compile without having to think?

#### [Patrick Massot (Dec 04 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Exercises chapter 4 - α → (( ∀ x: α, r ) ↔ r)/near/150837935):
Carlesso, What Kevin means is you should include your `variables (α : Type) (r : Prop)` line as well, so that anyone can copy-paste your code right away

#### [Patrick Massot (Dec 04 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Exercises chapter 4 - α → (( ∀ x: α, r ) ↔ r)/near/150837993):
About the question itself, you are complicating things needlessly. It's probably because the question is a bit silly

#### [Patrick Massot (Dec 04 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Exercises chapter 4 - α → (( ∀ x: α, r ) ↔ r)/near/150838017):
The proof of the second implication is simply `assume hr _, hr`

#### [Patrick Massot (Dec 04 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Exercises chapter 4 - α → (( ∀ x: α, r ) ↔ r)/near/150838020):
The whole point is that `r` does not depend on anything

#### [Patrick Massot (Dec 04 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Exercises chapter 4 - α → (( ∀ x: α, r ) ↔ r)/near/150838222):
and the first one can be shortened to `assume h, h y`. If you really want to use term mode, you can go all the way down the obfuscation road until you reach `theorem e1 (α : Type) (r : Prop): α → (( ∀ x: α, r ) ↔ r) := λ y, ⟨λ h, h y, λ h _, h⟩`

#### [Patrick Massot (Dec 04 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Exercises chapter 4 - α → (( ∀ x: α, r ) ↔ r)/near/150838259):
The opposite extreme is to load mathlib and replace the proof by `by tauto`.

#### [Carlesso Diego (Dec 04 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Exercises chapter 4 - α → (( ∀ x: α, r ) ↔ r)/near/150842750):
```quote
Carlesso, What Kevin means is you should include your `variables (α : Type) (r : Prop)` line as well, so that anyone can copy-paste your code right away
```
 Ok!, sorry about that, I will keep that in mind.

About the problem you are right! and what you suggest work well; I was aware of ```r```  but I wasn't able to "say" that in Lean.

```quote
About the question itself, you are complicating things needlessly. It's probably because the question is a bit silly
```
I was trying to be consistent with the "solution scheme" that the chapter has, for example ```(∀x, p x ∧ q x ) ↔ (∀ x, p x) ∧ (∀ x, q x) ``` is :

```lean
variables ( α : Type) ( r : Prop) (p q : α → Prop)
theorem e2: (∀x, p x ∧ q x ) ↔ (∀ x, p x) ∧ (∀ x, q x) := 
iff.intro 
    (  
    assume h: (∀ x : α , p x ∧ q x),
    show(∀ x, p x) ∧ (∀ x, q x), from and.intro 
        (assume y: α, show p y, from and.left(h y))
        (assume y: α, show q y, from and.right(h y))
    )
    (assume h1:(∀ x, p x) ∧ (∀ x, q x),
    assume y:α,  
    have hp: (∀ x, p x), from h1.left,
    have hq: (∀ x, q x), from h1.right,
    have hp2: p y, from hp y,
    have hq2 : q y, from hq y,
    show p y ∧ q y, from and.intro hp2 hq2
    )
```
It's a different exercise; I don't know if it could be solved with your method (right now it works), I have not reached that part on TPIL yet I think, or I'm not very practical to use it right now;  but it's just to show you what an exercise there looks like and what I was trying to get. 
Thank you by the way, problem solved!

#### [Mario Carneiro (Dec 04 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Exercises chapter 4 - α → (( ∀ x: α, r ) ↔ r)/near/150843010):
here's a compactified proof of that theorem:
```lean
variables {α : Type} {p q : α → Prop}
theorem e2 : (∀x, p x ∧ q x) ↔ (∀ x, p x) ∧ (∀ x, q x) :=
⟨λ H, ⟨λ x, (H x).left, λ x, (H x).right⟩, λ ⟨H₁, H₂⟩ x, ⟨H₁ x, H₂ x⟩⟩
```

#### [Mario Carneiro (Dec 04 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Exercises chapter 4 - α → (( ∀ x: α, r ) ↔ r)/near/150843154):
and a proof of the first theorem in that style:
```lean
theorem e1 : α → ((∀ x : α, r) ↔ r) :=
assume y : α,
iff.intro
  ( assume h : (∀ x, r),
    show r, from h y )
  ( assume hr : r,
    assume x : α,
    show r, from hr )
```

#### [Carlesso Diego (Dec 04 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Exercises chapter 4 - α → (( ∀ x: α, r ) ↔ r)/near/150844606):
Thank you!, that's perfect!

#### [Kevin Buzzard (Dec 04 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Exercises chapter 4 - α → (( ∀ x: α, r ) ↔ r)/near/150845046):
```quote
Carlesso, What Kevin means is you should include your `variables (α : Type) (r : Prop)` line as well, so that anyone can copy-paste your code right away
```
 Yes -- sorry for the brevity! I just had 2 minutes before a lecture and I wanted to help but then the code didn't run so I had to give up :-)

#### [Carlesso Diego (Dec 04 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Exercises chapter 4 - α → (( ∀ x: α, r ) ↔ r)/near/150845940):
```quote
```quote
Carlesso, What Kevin means is you should include your `variables (α : Type) (r : Prop)` line as well, so that anyone can copy-paste your code right away
```
 Yes -- sorry for the brevity! I just had 2 minutes before a lecture and I wanted to help but then the code didn't run so I had to give up :-)
```
 Don't worry!, I didn't think about the variables thing, I'm working with different exercises in the same file and I forgot about them, totally my fault. Thank you for your time anyway! :)

