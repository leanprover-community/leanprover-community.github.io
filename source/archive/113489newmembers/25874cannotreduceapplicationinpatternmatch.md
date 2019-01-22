---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/25874cannotreduceapplicationinpatternmatch.html
---

## [new members](index.html)
### [cannot reduce  application in pattern match](25874cannotreduceapplicationinpatternmatch.html)

#### [Shaun Steenkamp (Nov 14 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/cannot%20reduce%20%20application%20in%20pattern%20match/near/147663171):
I'm trying to fill in the `sorry` in the code below with `h x`. I expect this to work but it says that
```
26:23: equation type mismatch, term
  h x
has type
  f x = g x
but is expected to have type
  k x st.s = k x st.t
```
even though I define `k x st.s =def= f x` and `k x st.t =def= g x`

code:
```lean
universe ℓ
universe ℓ'

inductive st : Type
|  s : st
|  t : st

inductive R : st → st → Type
| r : R st.s st.t

def fex
  {A : Type ℓ}
  {B : A → Type ℓ'}
  {f g : Π (x : A) , B x}
  (h : Π (x : A) , f x = g x)
  : -------------------------
  (A → A)
:=
  have k : Π (x : A) (_ : st) , B x, from
    λ x h , match h with
      | st.s := f x
      | st.t := g x
    end,
  have l : Π (x : A)(b b' : st)(_ : R b b') , k x b = k x b', from
    λ x b b' r' , match b, b', r' with
      st.s, st.t, R.r := sorry -- h x
    end,
  show A → A, from λ x , x
```
Can someone tell me why it's not reducing?

#### [Mario Carneiro (Nov 14 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/cannot%20reduce%20%20application%20in%20pattern%20match/near/147663912):
use `let` instead of `have`

#### [Shaun Steenkamp (Nov 14 2018 at 13:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/cannot%20reduce%20%20application%20in%20pattern%20match/near/147664076):
okay, now I get a message saying I need to use `set_option eqn_compiler.zeta true`

#### [Shaun Steenkamp (Nov 14 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/cannot%20reduce%20%20application%20in%20pattern%20match/near/147664128):
and then it works fine

