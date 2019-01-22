---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/68252Typecheckingahigherorderdefinition.html
---

## [new members](index.html)
### [Type checking a higher order definition](68252Typecheckingahigherorderdefinition.html)

#### [Ken Roe (Jul 12 2018 at 02:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Type checking a higher order definition/near/129508130):
Can someone fix the following definition so that it can be type checked:

```lean
def absAll {t : Type} : (t → ℕ → Prop) → (ℕ → Prop) :=
    (λ (st : t → ℕ → Prop), (∀ (q:t), (st q))).
```

#### [Simon Hudon (Jul 12 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Type checking a higher order definition/near/129508344):
What happens if you write this:

```lean
def absAll {t : Type} : (t → ℕ → Prop) → (ℕ → Prop) :=
    (λ (st : t → ℕ → Prop) (i : ℕ), (∀ (q:t), (st q i))).
```

#### [Ken Roe (Jul 12 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Type checking a higher order definition/near/129509851):
It works--maybe I should file a bug report.

#### [Simon Hudon (Jul 12 2018 at 03:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Type checking a higher order definition/near/129509899):
That's not a bug, you made a mistake

#### [Simon Hudon (Jul 12 2018 at 03:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Type checking a higher order definition/near/129509927):
The term of the definition has to be a function that takes two parameters (`st : t → ℕ → Prop` and `i : ℕ`) and returns a `Prop` (`∀ (q:t), (st q i)`)

#### [Simon Hudon (Jul 12 2018 at 03:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Type checking a higher order definition/near/129509976):
You wrote `st q` which has type `ℕ -> Prop`. But the body of a `∀` must be a `Prop`

#### [Simon Hudon (Jul 12 2018 at 03:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Type checking a higher order definition/near/129510098):
I encourage you to use typed holes (i.e. `_`) to explore what are the types expected from you. For instance, look at what Lean tells you when you write the following in your definition:

- `(λ (st : t → ℕ → Prop), _)`
- `(λ (st : t → ℕ → Prop) (i : ℕ), _)`
- `(λ (st : t → ℕ → Prop) (i : ℕ), (∀ (q:t), _))`

#### [Simon Hudon (Jul 12 2018 at 03:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Type checking a higher order definition/near/129510432):
I'm not sure what you're going for but you may prefer this definition:

```lean
def absAll {t : Type} (st : t → ℕ → Prop) (i : ℕ) : Prop := 
∀ (q:t), (st q i)
```

It is clearer and its equations are nicer too

#### [Kevin Buzzard (Jul 12 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Type checking a higher order definition/near/129521382):
What does "its equations are nicer" mean in this context?

Edit: I think I've answered my own question using `#print prefix absAll`. I am surprised! I knew that if you defined a fancy inductive type you got a bunch of generated equations, but I don't think I'd internalised that this was happening for just some random definition of a function.

Simon's version gives
```
absAll : Π {t : Type}, (t → ℕ → Prop) → ℕ → Prop
absAll.equations._eqn_1 : ∀ {t : Type} (st : t → ℕ → Prop) (i : ℕ), absAll st i = ∀ (q : t), st q i
```
I guess my revised question is why this equation is there at all! It just seems to be the definition of `absAll`.

#### [Sean Leather (Jul 12 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Type checking a higher order definition/near/129521823):
```quote
I guess my revised question is why this equation is there at all! It just seems to be the definition of `absAll`.
```

If you use `simp [absAll]`, I believe it uses that equation in the simplifier.

#### [Kevin Buzzard (Jul 12 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/Type checking a higher order definition/near/129521916):
Aah that would make sense. I don't use `simp` like this usually -- I am only just beginning to get the hang of what `simp` does, and now I tend to only feed it equalities (I used to feed it arbitrary strings of symbols which I hoped made sense :-) )

