---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/11191Mutualinductionproblem.html
---

## [general](index.html)
### [Mutual induction problem](11191Mutualinductionproblem.html)

#### [Neil Strickland (Nov 02 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mutual induction problem/near/137068101):
Here is an attempt at a mutually inductive definition, which is a bit more intricate than the ones in the book.  
```lean
open nat

mutual inductive partition,blocks
with partition : ∀ (n : ℕ), Type
| null : partition 0
| add (n : ℕ) (p : partition n) : partition (succ n)
| join (n : ℕ) (p : partition n) (b : blocks n p) : partition (succ n)
with blocks : ∀ (n : ℕ), ∀ (p : partition n),Type
| old_block (n : ℕ) (p : partition n) (b : blocks n p): blocks (succ n) (add n p)
| new_block (n : ℕ) (p : partition n) : blocks (succ n) (add n p)
| join_block (n : ℕ) (p : partition n) (b : blocks n p) (c : blocks n p) :
                blocks (succ n) (join n p b)
```
Lean rejects it with the following message:
```
mutually inductive types compiled to invalid basic inductive type
nested exception message:
universe level of type_of(arg #3) of 'partition._mut_.join_0' is too big for the corresponding inductive datatype
```
Is there a way to fix this?  I have not really absorbed much of the story about universe levels so I do not know whether this is hard or not.

(The intended interpretation is as follows.  `partitions n` is supposed to represent the set of partitions of the set $$\{0,\ldots,n-1\}$$, and `blocks n p` is supposed to represent the set of blocks of the partition `p`.  Obviously `n` should be implicit here but I am leaving it explicit until I have fixed the other issues. In the case $$n=0$$ there is a unique partition which we call `null`.   One way to partition $$\{0,\ldots,n\}$$ is to take a partition `p` of $$\{0,\ldots,n-1\}$$ and add $$\{n\}$$ as an extra block; we call this `add n p`.  Another way is to take `p` and a block `b` of `p` and use $$b \cup \{n\}$$ as one block of a new partition which we call `join n p b`.  )

#### [Reid Barton (Nov 02 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mutual induction problem/near/137068768):
I think this is an [inductive-inductive type](https://ncatlab.org/nlab/show/inductive-inductive+type), which I think Lean doesn't support.
Sometimes you get that error about universe levels when the real issue is that Lean got confused for another reason--here there's also an error on the use of `partition` in the declaration of `blocks`; it looks like Lean doesn't know what `partition` is yet.

#### [Reid Barton (Nov 02 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mutual induction problem/near/137068999):
A less innocuous-looking example of an inductive-inductive type:
```lean
mutual inductive code,el
with code : Type
| cempty : code
| cnat : code
| csigma (a : code) (b : el a → code) : code
| cpi (a : code) (b : el a → code) : code
with el : Π (c : code), Type
| enat (n : ℕ) : el cnat
| esigma (a : code) (b : el a → code) (x : el a) (y : el (b x)) : el (csigma a b)
| epi (a : code) (b : el a → code) (x : Π (i : el a), el (b i)) : el (cpi a b)
```

#### [Reid Barton (Nov 02 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mutual induction problem/near/137069482):
Though my example involves recursion in negative positions in a few places, so maybe I've got the example wrong

#### [Reid Barton (Nov 02 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mutual induction problem/near/137071550):
I tried defining `partition` and `blocks` by mutual recursion, rather than making them inductive types, but Lean wasn't happy with my attempt either.

#### [Reid Barton (Nov 02 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mutual induction problem/near/137071648):
I think the best you can do is define the types by some other means and then try to approximate the interface you would get from an inductive definition, for example by defining your own "induction principle".

#### [Mario Carneiro (Nov 02 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mutual induction problem/near/137077383):
@**Neil Strickland** Another way to read "this is inductive-inductive" is "lean does not have the axioms to justify that this is a valid construction". So you have to find another way to justify it to lean. In this case, the important part is that `n` increases in all the constructors, so this is actually a mutually recursive definition of a family of types, which lean can do well enough. We have
```
partition 0 = unit
partition (succ n) = partition n + Σ p : partition n, blocks n p
blocks 0 p = empty
blocks (succ n) (inl p) = blocks n p + 1
blocks (succ n) (inr <p, b>) = blocks n p
```

#### [Reid Barton (Nov 02 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mutual induction problem/near/137077658):
This looks a lot like my attempt which Lean rejected, so I'm curious to see how you convince it the definition is valid...

#### [Mario Carneiro (Nov 02 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mutual induction problem/near/137077666):
and you can define the pair <partition n, blocks n> by plain primitive recursion

#### [Neil Strickland (Nov 02 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mutual induction problem/near/137078327):
Thanks, I will try that approach.

#### [Mario Carneiro (Nov 02 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mutual induction problem/near/137078422):
```lean
def partblock : ℕ → Σ T : Type, T → Type
| 0 := ⟨unit, λ _, empty⟩
| (n+1) := ⟨(partblock n).1 ⊕ Σ p : (partblock n).1, (partblock n).2 p,
  λ x, sum.cases_on x
    (λ p, option ((partblock n).2 p))
    (λ p, (partblock n).2 p.1)⟩

def partition (n : ℕ) := (partblock n).1
def blocks {n : ℕ} : partition n → Type := (partblock n).2
def partition.null : partition 0 := unit.star
def partition.add {n} : partition n → partition (n+1) := sum.inl
def partition.join {n} (p : partition n) (b : blocks p) : partition (n+1) := sum.inr ⟨p, b⟩
def old_block {n} {p : partition n} : blocks p → blocks p.add := option.some
def new_block {n} {p : partition n} : blocks p.add := option.none
def join_block {n} {p : partition n} (b : blocks p) : blocks p → blocks (p.join b) := id
```

#### [Mario Carneiro (Nov 02 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mutual induction problem/near/137078448):
the recursion principle is left as an exercise for the reader ;)

#### [Reid Barton (Nov 02 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mutual induction problem/near/137078522):
Interesting--I wonder if eliminating the mutual recursion by hand is essential, then

#### [Mario Carneiro (Nov 02 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mutual induction problem/near/137078554):
Unfortunately, since `blocks n` refers to `partitions n` the default well founded metric for mutual recursion fails

#### [Mario Carneiro (Nov 02 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Mutual induction problem/near/137078619):
you can hack together the right well founded relation, but dealing with that relation will dominate the size of the definition itself

