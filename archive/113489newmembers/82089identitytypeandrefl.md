---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/82089identitytypeandrefl.html
---

## [new members](index.html)
### [identity type and refl](82089identitytypeandrefl.html)

#### [Shaun Steenkamp (Nov 13 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/identity type and refl/near/147599492):
Is it possible to pattern match on the refl constructor of the identity type (eq.refl) in Lean similar to what one can do in Agda? I tried defining one by pattern matching but it didn't seem to work.

#### [Mario Carneiro (Nov 13 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/identity type and refl/near/147599789):
yes, there are several ways

#### [Mario Carneiro (Nov 13 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/identity type and refl/near/147599806):
`subst` and `cases` both work, as does the pattern matcher

#### [Mario Carneiro (Nov 13 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/identity type and refl/near/147599845):
note that one side of the equality must be a variable and must participate in the pattern match (be right of the colon) for it to work

#### [Reid Barton (Nov 13 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/identity type and refl/near/147599908):
Can you give an example of code you expect to work but doesn't?

#### [Shaun Steenkamp (Nov 13 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/identity type and refl/near/147599959):
```lean
def subst {A : Type ℓ}(P : A → Type ℓ'){a b : A} : a = b → P a → P b :=
  assume p : a = b,
  assume x : P a,
  show P b, from eq.cases_on p x

```

#### [Shaun Steenkamp (Nov 13 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/identity type and refl/near/147600005):
works fine

#### [Shaun Steenkamp (Nov 13 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/identity type and refl/near/147600010):
but then

#### [Shaun Steenkamp (Nov 13 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/identity type and refl/near/147600023):
```lean
def subst_const
  {A : Type ℓ}
  {B : Type ℓ'}
  {x y : A}
  : Π
  (p : x = y)
  (b : B)
  , ---------------------
  subst (λ _ , B) p b = b
| (eq.refl) _ := eq.refl
```
doesn't work

#### [Shaun Steenkamp (Nov 13 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/identity type and refl/near/147600110):
This is something I've used a lot in Agda, and I figured if I try to do some of these "basic" things in Lean that could help me learn it, but I think that maybe I don't understand the basic syntax well enough yet...

#### [Reid Barton (Nov 13 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/identity type and refl/near/147600115):
Yes, that is because the requirement "one side of the equality must be a variable and must participate in the pattern match (be right of the colon)" (or in this case, below the colon :slight_smile:) is not met

#### [Reid Barton (Nov 13 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/identity type and refl/near/147600331):
`y` needs to move past the colon, and the last line should read `| _ (eq.refl _) _ := eq.refl _`

#### [Reid Barton (Nov 13 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/identity type and refl/near/147600352):
or replace `eq.refl _` with `rfl`

#### [Shaun Steenkamp (Nov 13 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/identity type and refl/near/147600361):
okay, got it, can I still keep y implicit?

#### [Shaun Steenkamp (Nov 13 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/identity type and refl/near/147600498):
it seems I can

#### [Shaun Steenkamp (Nov 13 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/identity type and refl/near/147600555):
thank you very much for your help!! ^_^

