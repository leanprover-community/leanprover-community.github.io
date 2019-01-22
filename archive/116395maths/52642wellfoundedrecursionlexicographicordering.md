---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/52642wellfoundedrecursionlexicographicordering.html
---

## [maths](index.html)
### [well-founded recursion & lexicographic ordering ?](52642wellfoundedrecursionlexicographicordering.html)

#### [Jack Crawford (Sep 14 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/well-founded%20recursion%20%26%20lexicographic%20ordering%20%3F/near/133941390):
Hi, I have a pleb question about how Lean infers whether recursion is well-founded or not.
I'm writing a recursive function whose first two arguments are of type `fin m` and `fin n`,  and my algorithm:
 1) always decreases the size of my `fin n`
 2) sometimes decreases the size of my `fin m`
I would think that Lean should be able to work out that my recursion is well-founded from the first fact alone, but it does not seem able.
However, when I simply change the order that my arguments appear from `fin m -> fin n -> ...` to `fin n -> fin m -> ...` and nothing else (nontrivial), suddenly Lean recognises well-foundedness!

It seems that Lean is only trying to show well-foundedness from my first argument and can't work out that there should be well-foundedness on the lexicographic order of my `fin m` and `fin n`, or that just my `fin n` alone should suffice. Everything's sort of "doing what I want it to" except that I have to write the arguments to my function in an unconventional way. How can I tell Lean to just look for well-foundedness on my second argument (the `fin n`), or on the lexicographic pair of `fin m` and `fin n`, and not just purely on my `fin m`? Thanks!

#### [Kenny Lau (Sep 14 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/well-founded%20recursion%20%26%20lexicographic%20ordering%20%3F/near/133941463):
MWE

#### [Kevin Buzzard (Sep 14 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/well-founded%20recursion%20%26%20lexicographic%20ordering%20%3F/near/133941803):
By default Lean uses lexicographic ordering when trying to prove recursive functions are well-defined, so definitely the input order matters. The notes at https://github.com/leanprover/mathlib/blob/master/docs/extras/well_founded_recursion.md probably tell you all you need to know

#### [Jack Crawford (Sep 14 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/well-founded%20recursion%20%26%20lexicographic%20ordering%20%3F/near/133941855):
@**Kenny Lau** 
here's an MWE, compare the pair:
``` 
def mwe_aux {m n : ℕ} : Π (i : fin m) (j : fin n), bool
| ⟨0, h₁⟩ ⟨k₂, h₂⟩ := ff 
| ⟨k₁+1, h₁⟩ ⟨0, h₂⟩ := ff
| ⟨k₁+1, h₁⟩ ⟨k₂+1, h₂⟩ := 
begin
    apply mwe_aux,
    from if k₂%2 = 0 then ⟨k₁, nat.lt_of_succ_lt h₁⟩ else ⟨k₁+1, h₁⟩,
    from ⟨k₂, nat.lt_of_succ_lt h₂⟩
end

def mwe_aux2 {m n : ℕ} : Π (j : fin n) (i : fin m), bool
| ⟨k₂, h₂⟩ ⟨0, h₁⟩ := ff 
| ⟨0, h₂⟩ ⟨k₁+1, h₁⟩ := ff
| ⟨k₂+1, h₂⟩ ⟨k₁+1, h₁⟩ := 
begin
    apply mwe_aux2,
    from ⟨k₂, nat.lt_of_succ_lt h₂⟩,
    from if k₂%2 = 0 then ⟨k₁, nat.lt_of_succ_lt h₁⟩ else ⟨k₁+1, h₁⟩,
end
```

#### [Kevin Buzzard (Sep 14 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/well-founded%20recursion%20%26%20lexicographic%20ordering%20%3F/near/133941878):
the linked notes explain how to change the well-order on your input.

#### [Jack Crawford (Sep 14 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/well-founded%20recursion%20%26%20lexicographic%20ordering%20%3F/near/133941927):
@**Kevin Buzzard**  ah oops I didn't see that before I responded to Kenny, thanks, I'll have a look!

#### [Kenny Lau (Sep 14 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/well-founded%20recursion%20%26%20lexicographic%20ordering%20%3F/near/133941991):
well I mean, what are you trying to do, instead of MWE of the error

