---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/66953errorwithletsubstitution.html
---

## [general](index.html)
### [error with let substitution](66953errorwithletsubstitution.html)

#### [Mohammed Eyad Kurd-Misto (Jun 04 2018 at 01:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error with let substitution/near/127518930):
Hello, I'm not sure if this is the correct place to post this. I am Mohammed Eyad Kurd-Misto, a PhD student at Chapman university. I am having an issue with a proof where the let construct does not seem to be working the way I would think. For two steps of the proof, I am simply substituting portions of the current statement from the let, and in one instance there is no issue but in another I am getting an error. The main relevant code is:

`lemma flat_sharp {B : Type} : Π {n : ℕ}, ∀ (ps: @datum_or_data B ff n), (♭ (♯ ps)) = ps
| 0   datum_or_data.nil := rfl 
| (n+1) (datum_or_data.cons p ps) := 
let ⟨as, h⟩ := ♯ ps, a := ♮⁻¹ p in  --let (⟨as, h⟩ : vector B n) := (♯ ps : vector B n), a := ♮⁻¹ p in
  calc
    (♭ (♯ (datum_or_data.cons p ps))) = ♭ (vector.cons (♮⁻¹  p) (♯ ps)) : rfl
    ...                 = ♭ (vector.cons (a) (♯ ps)) : rfl   --this works
    ...                 = ♭ (vector.cons (a) (⟨as, h⟩)) : rfl --@rfl (vector B n)  -- this does not work?
    ...                 = datum_or_data.cons (♮ (a)) (♭ ⟨as, h⟩) : rfl
    ...`

♭ and ♯ are operations for converting data from a vector to a 'datum_or_data' and vice versa so the goal here is simply to show they invert one another.  ♮and ♮⁻¹ are operations for converting the individual elements of the data. I'm really not sure why I can't simply substitute  ⟨as, h⟩ for  ♯ ps since they are defined to be the same in the let and I have been unable to replicate anything similar where I can't simply substitute what is defined in the let construct. Any help would be greatly appreciated!

The error message given is:

Lean]
type mismatch at application
  eq.trans (eq.trans (rfl (♭♯datum_or_data.cons p ps)) (rfl (♭(♮⁻¹p) :: ♯ps))) (rfl ?m_2)
term
  rfl ?m_2
has type
  ?m_2 = ?m_2
but is expected to have type
  (♭a :: ♯ps) = ♭a :: ⟨as, h⟩

Code to support this lemma is: 

`import data.vector`

`variable {α : Type} 
variable {x : α}
variable {xs : list α} `

`lemma list_len_cancel  {n :ℕ} (h : list.length (x::xs) = n+1)
: list.length xs = n := nat.succ.inj h -- injectivity of successor `

`inductive datum_or_data {B : Type} : bool → ℕ → Type 
| sg (a : B) :  datum_or_data tt 0
| nil : datum_or_data ff 0
| cons {n : ℕ} (a : datum_or_data tt 0) (as : datum_or_data ff n) : datum_or_data ff (n+1)`

`@[reducible] def datum_inv {B : Type} : @datum_or_data B tt 0 → B 
| (datum_or_data.sg x) := x`

notation `♮` x := datum_or_data.sg x
notation `♮⁻¹` a := datum_inv a

`@[reducible] definition vector_from_data {B : Type} : Π {n :ℕ }, @datum_or_data B ff n → vector B n 
| 0 _ :=  vector.nil
| (n+1) (datum_or_data.cons p ps)  := vector.cons (♮⁻¹ p) (vector_from_data ps)`

`@[reducible] definition data_from_vector {B : Type} : Π {n :ℕ }, vector B n → @datum_or_data B ff n
| 0 _ :=  datum_or_data.nil
| (n+1) ⟨(a::as), h⟩   := datum_or_data.cons (♮ a) (data_from_vector ⟨as,list_len_cancel h⟩ )`

notation `♯` p := vector_from_data p 
notation `♭` v := data_from_vector v

`-- inverses 
@[simp] lemma natural {B : Type}: ∀ a : B, (♮⁻¹ (♮ a)) = a := assume a, rfl 
@[simp] lemma natural' {B: Type}: ∀ d : @datum_or_data B tt 0, (♮ (♮⁻¹ d)) = d   
  | (♮ b) := rfl `


`--prove that flat and sharp are inverses
lemma flat_sharp {B : Type} : Π {n : ℕ}, ∀ (ps: @datum_or_data B ff n), (♭ (♯ ps)) = ps
| 0   datum_or_data.nil := rfl 
| (n+1) (datum_or_data.cons p ps) := 
let ⟨as, h⟩ := ♯ ps, a := ♮⁻¹ p in  --let (⟨as, h⟩ : vector B n) := (♯ ps : vector B n), a := ♮⁻¹ p in
  calc
    (♭ (♯ (datum_or_data.cons p ps))) = ♭ (vector.cons (♮⁻¹  p) (♯ ps)) : rfl
    ...                 = ♭ (vector.cons (a) (♯ ps)) : rfl  --this works
    ...                 = ♭ (vector.cons (a) (⟨as, h⟩)) : rfl --@rfl (vector B n)   -- this does not work?
    ...                 = datum_or_data.cons (♮ (a)) (♭ ⟨as, h⟩) : rfl
    ...                 = datum_or_data.cons p (♭ (♯ ps)) : congr_arg (λ x, datum_or_data.cons x (♭ (♯ ps))) (natural' p)
    ...                 = datum_or_data.cons p ps : congr_arg (λ x, datum_or_data.cons p x) (flat_sharp ps)`

#### [Simon Hudon (Jun 04 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error with let substitution/near/127519048):
The way you use the let is more like a match statement than a local definition. It works but it makes definitional equality a bit weird.

#### [Simon Hudon (Jun 04 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error with let substitution/near/127519100):
You might need to use an actual match statement an include an equality lemma in the match expression. I'll just try something and get back to you.

#### [Simon Hudon (Jun 04 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error with let substitution/near/127519118):
Btw, you might like to know that it's possible to have nice formatting of Lean code by enclosing it in backticks

#### [Mohammed Eyad Kurd-Misto (Jun 04 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error with let substitution/near/127519350):
Thank you, I reformatted the initial post (though the notation portions actually contain backticks in the lean code so I left them as is).

#### [Simon Hudon (Jun 04 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error with let substitution/near/127519412):
If you put three ticks before the first line and three after the last, you don't need to format it line by line. Even better: if you put three ticks followed by `lean`, you get syntax highlighting

#### [Simon Hudon (Jun 04 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error with let substitution/near/127519472):
What I think you should do is:

```lean
lemma flat_sharp {B : Type} : Π {n : ℕ}, ∀ (ps: @datum_or_data B ff n), (♭ (♯ ps)) = ps
| 0   datum_or_data.nil := rfl 
| (n+1) (datum_or_data.cons p ps) := 
by cases h' : ♯ ps with as h ; 
  calc
    (♭ (♯ (datum_or_data.cons p ps))) = ♭ (vector.cons (♮⁻¹  p) (♯ ps)) : rfl
    ...                 = ♭ (vector.cons (a) (♯ ps)) : rfl   --this works
    ...                 = ♭ (vector.cons (a) (⟨as, h⟩)) : rw h'
    ...                 = datum_or_data.cons (♮ (a)) (♭ ⟨as, h⟩) : rfl
    ...
```

#### [Mohammed Eyad Kurd-Misto (Jun 04 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error with let substitution/near/127520031):
Thank you, I'll look at continuing the proof using cases/rw instead.

