---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/29713formalizingexactsequence.html
---

## [general](index.html)
### [formalizing exact sequence](29713formalizingexactsequence.html)

#### [Kenny Lau (Mar 27 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124273688):
How would you formalize exact sequences in Lean? Let's say they are R-modules for a commutative ring R.
I have the following exact sequences in mind:

1. 0->A->B
2. A->B->C
3. A->B->C
4. 0->A->B->C
5. 0->A->B->C->0
6. A->B->C->0
7. ...->An->...->A3->A2->A1->A0

#### [Kenny Lau (Mar 27 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124273698):
0->A->B->C->D->0 is relatively rare but are still used

#### [Kenny Lau (Mar 27 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124273706):
short exact sequences could be a special case

#### [Simon Hudon (Mar 27 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124273899):
What is the difference between an exact sequence and a list?

#### [jmc (Mar 27 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274112):
@**Simon Hudon**  The fact that you have morphisms f_n: A_n \to A_{n-1} that satisfy the condition im(f_n) = ker(f_{n-1}).

#### [Simon Hudon (Mar 27 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274177):
So if you take A -> B -> C, that sequence has to have a morphism from A to B and from B to C? Is it meaningful to have an empty sequence?

#### [jmc (Mar 27 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274206):
Hmmm, I guess one can give it meaning.

#### [jmc (Mar 27 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274253):
But probably it is never used.

#### [jmc (Mar 27 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274256):
I can't remember ever seeing it

#### [Kevin Buzzard (Mar 27 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274259):
You have n>=1 objects in a list, and n-1 morphisms from A[i] to A[i+1]

#### [Simon Hudon (Mar 27 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274261):
Ok, let's leave it out if we have to

#### [Kevin Buzzard (Mar 27 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274268):
and you demand that in the n-2 situations for which it makes sense,

#### [Simon Hudon (Mar 27 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274270):
(the empty sequence that is)

#### [Kevin Buzzard (Mar 27 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274276):
image of j'th map is kernel of (j+1)st

#### [Kevin Buzzard (Mar 27 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274285):
It says nothing for n<3

#### [Kevin Buzzard (Mar 27 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274293):
and nobody ever uses it either (i.e. it's not a useful special case of anything, in contrast to sum(i=1,n,f(i)) which can be sensibly and usefully interpreted as zero when n=0)

#### [Simon Hudon (Mar 27 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274340):
Ok, I have an idea, I'll just write up something and show it to you guys

#### [Kevin Buzzard (Mar 27 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274342):
it's also a useful concept for Z_{>=0} and Z_{<=0} and Z

#### [Kevin Buzzard (Mar 27 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274346):
i.e. A0->A1->A2->... being exact

#### [Kevin Buzzard (Mar 27 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274353):
and ...->B2->B1->B0 being exact

#### [Kevin Buzzard (Mar 27 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274358):
and ...->A_{n-1}->A_n->A_{n+1}->... being exact

#### [Kevin Buzzard (Mar 27 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274360):
and I think that covers everything

#### [Kevin Buzzard (Mar 27 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274361):
that I see in practice

#### [Simon Hudon (Mar 27 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274364):
Thanks! What's the type of `im` and `ker`?

#### [jmc (Mar 27 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274425):
@**Simon Hudon** so there are two conventions: either `target(f_n) = source(f_{n+1})`, or `source(f_n) = target(f_{n+1})`

#### [jmc (Mar 27 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274432):
im and ker are both also R-modules

#### [Kevin Buzzard (Mar 27 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274434):
depending on whether you're doing homology or cohomology

#### [jmc (Mar 27 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274436):
or maybe R-submodules of the object that they are a sub of

#### [jmc (Mar 27 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274496):
Do you guys think it might be useful to first formalise complexes? That is `im(f_n) \subset ker(f_{n+1})` or equivalently `f_{n+1} \circ f_n = 0`.

#### [Simon Hudon (Mar 27 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274644):
I have encoded something without the relationship between morphisms, I just want to check if that makes sense to you guys before encoding that condition

#### [Simon Hudon (Mar 27 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274648):
```
universe u

constant morphism : Type u → Type u → Type u

inductive exact_seq : list (Type u) → Type (u+1)
 | nil (a : Type u) : exact_seq [a]
 | cons (a b : Type u) (tail : list (Type u)) : 
   morphism a b → 
   exact_seq (b :: tail) → 
   exact_seq (a :: b :: tail)
```

#### [Johannes Hölzl (Mar 27 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274669):
There are also exact sequences in HoTT Lean 2: https://github.com/cmu-phil/Spectral, see https://github.com/cmu-phil/Spectral/blob/master/algebra/exactness.hlean 
But this is HoTT Lean, so there are a lot of differences now to current Lean. Also the definitions might be very constructive...

#### [jmc (Mar 27 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274734):
@**Simon Hudon** What is `constant morphism` supposed to do? Because I don't really get it...

#### [Simon Hudon (Mar 27 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274745):
It's just a way of having morphisms in my definition without depending on any specific definition of morphism.

#### [jmc (Mar 27 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274801):
I see, makes sense now

#### [Simon Hudon (Mar 27 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274867):
You could actually make it a parameter of the whole thing

#### [jmc (Mar 27 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274875):
@**Simon Hudon**  I think this works, but not for sequences indexed by Z, right?

#### [Simon Hudon (Mar 27 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274921):
Meaning that instead of a list as the index of your sequence, you'd like a function from a contiguous interval of Z to the type in question?

#### [Simon Hudon (Mar 27 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274935):
You could match this with a single Z which is an offset for every index of the N based indices of the list

#### [Simon Hudon (Mar 27 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274989):
Otherwise, you could replace the list but such a sequence not being an inductive type might not be pretty when you pattern match on an `exact_seq`

#### [jmc (Mar 27 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274993):
yes, but you the interval need not be bounded

#### [Simon Hudon (Mar 27 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124274998):
Ah yes, I see

#### [jmc (Mar 27 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124275003):
so then it won't be inductive... probably

#### [jmc (Mar 27 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124275007):
So intuitively it is a function: Z -> morphisms

#### [jmc (Mar 27 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124275047):
but the problem is that actually the target depends on the element n \in Z

#### [Simon Hudon (Mar 27 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124275053):
Yeah ... alternatively, I'm working on a construction for coinductive types. You could use that to make a possibly "doubly" infinite, Z indexed sequence

#### [Simon Hudon (Mar 27 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124275127):
At the moment, maybe the best thing to do is have an interval type and make functions from that interval to the types that your sequence contains

#### [Kenny Lau (Mar 27 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124275459):
so what's the verdict

#### [jmc (Mar 27 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124275514):
@**Kenny Lau** Do you want/need unbounded sequences?

#### [jmc (Mar 27 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124275516):
Or is finite enough?

#### [Kenny Lau (Mar 27 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124275518):
preferably

#### [Kenny Lau (Mar 27 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124275522):
indexing by N is good

#### [Simon Hudon (Mar 27 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124275573):
should finite and infinite sequences be the same type or would it be good enough to have separate constructions?

#### [jmc (Mar 27 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124275574):
then I guess the inductive definition that Simon proposed is the best option

#### [Kenny Lau (Mar 27 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124275582):
I can do with separate

#### [Kenny Lau (Mar 27 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124275588):
or just make finite a special case of infinite (with all objects being eventually 0)

#### [jmc (Mar 27 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124275592):
@**Simon Hudon** I think they can be different types, and then an `extend_with_zeros` function from the finite to infinite sequences

#### [Simon Hudon (Mar 27 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124275594):
Cool

#### [Simon Hudon (Mar 27 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124275712):
I have not covered the ` im(f_n) \subset ker(f_{n+1}) ` bit but I think an inductive predicate would be a nice way of asserting that

#### [Simon Hudon (Mar 27 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276058):
Here's how I would build that predicate (I'm not sure for the type of `ker` and `im` but it seems to capture part of the idea at least)

```
universe u

constant morphism : Type u → Type u → Type u

constant ker : Π {a b : Type u}, morphism a b → a
constant im : Π {a b : Type u}, morphism a b → b

inductive exact_seq : list (Type u) → Type (u+1)
 | nil (a : Type u) : exact_seq [a]
 | cons {a b : Type u} {tail : list (Type u)} :
   morphism a b →
   exact_seq (b :: tail) →
   exact_seq (a :: b :: tail)

inductive is_exact : Π {s}, exact_seq s → Type (u+1)
 | nil {a b : Type u} (f : morphism a b) : is_exact (exact_seq.cons f $ exact_seq.nil b)
 | cons (a b c : Type u) (tail : list (Type u))
        (f : morphism a b) (g : morphism b c)
        (s : exact_seq (c :: tail)) :
   ker g = im f →
   is_exact (exact_seq.cons g s) →
   is_exact (exact_seq.cons f $ exact_seq.cons g s)
```

#### [Patrick Massot (Mar 27 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276259):
Guys... you are really crazy about inductive types

#### [Simon Hudon (Mar 27 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276271):
... in a bad way?

#### [Patrick Massot (Mar 27 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276277):
I think this would be a nightmare to work with

#### [Patrick Massot (Mar 27 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276282):
How are you going to define morphisms of complexes?

#### [Patrick Massot (Mar 27 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276294):
Why do you need to complicate everything

#### [Patrick Massot (Mar 27 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276356):
Why not defining a sequence to be a map C from I to R-mod (where I is an interval in integers) and a map d from I to linear maps from C i to C (i+1)?

#### [Patrick Massot (Mar 27 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276412):
and then adding condition on d (i + 1) and d i  for all i

#### [Patrick Massot (Mar 27 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276417):
to get either complexes or exact sequences

#### [Patrick Massot (Mar 27 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276433):
Anyway, did anyone check whether @**Scott Morrison** already did all that in his category lib, for arbitraray abelian categories?

#### [Simon Hudon (Mar 27 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276435):
You mean a bit like this?

```
open nat
variable s : stream (Type u)

def inf_seq := Π n, morphism (s n) (s $ succ n)
variables {s} (x : inf_seq s)
def inf_exact_seq := Π n, im (x n) = ker (x _)
```

#### [Simon Hudon (Mar 27 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276442):
I thought of doing that for intervals of integers too

#### [Patrick Massot (Mar 27 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276444):
What is stream?

#### [Simon Hudon (Mar 27 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276493):
What annoys me is the `+1` for which you need some tricks to make it type correct

#### [Simon Hudon (Mar 27 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276497):
`def stream (a) := ℕ -> a`

#### [Patrick Massot (Mar 27 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276512):
What is this `+1` issue?

#### [Simon Hudon (Mar 27 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276565):
If you use it directly, with `I` an interval on integers and `i : I`, `↑i + 1 : ℤ` so you need to feed in a proof that it's also part of the interval

#### [Simon Hudon (Mar 27 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276607):
Actually, now that I write it out loud, it doesn't seem that bad

#### [Patrick Massot (Mar 27 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276611):
Don't do that

#### [Simon Hudon (Mar 27 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276614):
It's just going to be one ugly index

#### [Simon Hudon (Mar 27 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276618):
What would you do?

#### [Patrick Massot (Mar 27 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276620):
Define `C i` to be the zero module if `i` is not in the interval

#### [Patrick Massot (Mar 27 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276636):
So all sequences are indexed by `ℤ`

#### [Simon Hudon (Mar 27 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276683):
Ok, so do you overload the function application operator or do you actually work with `ℤ → Type`? In the second case, you'll get into ugliness with defining extensionality

#### [Simon Hudon (Mar 27 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276691):
But in the first case ... I think it can work

#### [Patrick Massot (Mar 27 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276702):
What ugliness?

#### [Patrick Massot (Mar 27 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276709):
what extensionality?

#### [Simon Hudon (Mar 27 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276753):
If you want to prove the equality of two sequences ... *trail off*

#### [Patrick Massot (Mar 27 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276757):
I hope you're not about to write the c word

#### [Simon Hudon (Mar 27 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276769):
I'm not sure what your c word is ... comparison?

#### [Patrick Massot (Mar 27 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276774):
constructively

#### [Simon Hudon (Mar 27 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124276828):
Haha! I'm more into classical reasoning, relax :stuck_out_tongue_closed_eyes:

#### [Simon Hudon (Mar 27 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124277060):
Here's what I would do then:

```
structure interval (left right : option ℤ) :=
  (val : ℤ)
  (left_bounded : ∀ h₀, @option.get _ left h₀ ≤ val)
  (right_bounded : ∀ h₀, val ≤ @option.get _ right h₀)

structure seq (x y : option ℤ) (a : Type u) :=
  (f : interval x y → a)

instance {x y : option ℤ} {a} [has_zero a] : has_coe_to_fun (seq x y a) := 
  { F := λ _, ℤ → a
  , coe := λ ⟨f⟩ i, if h : _ ∧ _ then f ⟨i,h.1,h.2⟩ else 0 }
```

#### [Kenny Lau (Mar 27 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124277134):
@**Patrick Massot** you really hate inductive definitions

#### [Patrick Massot (Mar 27 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124277135):
Nice. I need to go but I'm sure Kenny and Kevin will get something here

#### [Patrick Massot (Mar 27 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124277143):
@**Kenny Lau** I don't hate them, I try to formalize maths using the same kind of thinking used in real world maths

#### [Patrick Massot (Mar 27 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124277145):
This may be a mistake

#### [Patrick Massot (Mar 27 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124277159):
But I'd like to try that for a while before switching to an orthogonal way of thinking about maths

#### [Patrick Massot (Mar 27 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124277161):
And those days I have zero time for serious Lean :disappointed:

#### [Patrick Massot (Mar 27 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124277162):
only a bit of Zulip chat

#### [Patrick Massot (Mar 27 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124277209):
And now I really need to go

#### [Kenny Lau (Mar 27 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124277345):
@**Simon Hudon** ok now I have two new things:
1. exact sequences should be a subtype (not the {x // p x} kind of subtype) of sequences in general, where sequences in this context mean sequences with morphisms. to give more context, there's a type of sequences with im f_n subset ker f_(n+1) instead of equal, i.e. if I call the maps d we have d^2=0.
2. we need to think about what our objects can be

#### [Simon Hudon (Mar 27 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124277598):
When you say ` im f_n subset ker f_(n+1) `, is this strictly in the sense of sets or are you thinking about subsets of various structures like modules?

#### [Kenny Lau (Mar 27 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124277791):
well both would be subset of the object Cn

#### [Kenny Lau (Mar 27 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124277797):
and also I meant im f_(n+1) subset ker f_n

#### [Simon Hudon (Mar 27 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278160):
So maybe this would help. If needed, we can change the `=` with `\subset`

#### [Simon Hudon (Mar 27 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278162):
```
structure exact_seq (x y : option ℤ) (A : Type u) [has_zero A] :=
  (f : seq x y A)
  (m : Π n, morphism (f n) (f $ n+1))
  (eq : Π n, ker (m $ n + 1) = im (m n))
```

#### [Simon Hudon (Mar 27 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278217):
That would involve a morphism from the last object to 0 and from the first object to 0 of which I don't know if it makes sense

#### [Kenny Lau (Mar 27 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278222):
hmm, it seems you're doing it very generally

#### [Kenny Lau (Mar 27 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278224):
in regards to my second question

#### [Simon Hudon (Mar 27 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278226):
Maybe we can choose a better constant than 0 to make it make sense

#### [Kenny Lau (Mar 27 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278237):
no, 0 always makes sense

#### [Kenny Lau (Mar 27 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278241):
but what do you mean from the last object to 0

#### [Simon Hudon (Mar 27 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278243):
And morphisms to and from 0 make sense to?

#### [Kenny Lau (Mar 27 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278246):
yes

#### [Kenny Lau (Mar 27 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278254):
it's called the zero object in category theory

#### [Simon Hudon (Mar 27 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278305):
Thanks, I'll read up on that

#### [Kenny Lau (Mar 27 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278307):
it has a unique morphism to and from every object

#### [Simon Hudon (Mar 27 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278324):
The morphisms have type `m : Π n : ℤ, morphism (f n) (f $ n+1)` which means that there exists a morphism for every integer even when your sequence is finite

#### [Kenny Lau (Mar 27 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278331):
so your answer to my second question is basically any type with a zero object?

#### [Simon Hudon (Mar 27 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278333):
Exactly

#### [Simon Hudon (Mar 27 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278375):
Sorry, not quite

#### [Simon Hudon (Mar 27 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278381):
I used `morphism` as a sort of place holder. Maybe you should have `A` be a category

#### [Simon Hudon (Mar 27 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278385):
and take the morphism from there

#### [Kenny Lau (Mar 27 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278388):
"there exists a morphism for every integer even when your sequence is finite" fits with the convention that short exact sequences are special cases of long exact sequences with objects being eventually zero

#### [Kenny Lau (Mar 27 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278392):
so that makes sense

#### [Kenny Lau (Mar 27 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278397):
in the category setting, exact sequences only make sense in abelian categories

#### [Kenny Lau (Mar 27 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278404):
but i don't know whether it would be more useful to have any abelian categories, or just modules

#### [Simon Hudon (Mar 27 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278478):
Are the Abelian categories where the 0 is defined?

#### [Kenny Lau (Mar 27 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278490):
abelian categories have 0

#### [Kenny Lau (Mar 27 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278492):
it has more things

#### [Simon Hudon (Mar 27 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278549):
I'd be tempted to suggest to keep it a general definition with the Abelian category and use additional information (e.g. is a module) in the lemmas where it is relevant

#### [Kenny Lau (Mar 27 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278569):
alright

#### [Simon Hudon (Mar 27 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278570):
You might also want to layer the structure in such a way that you can vary on ` Π n, ker (m $ n + 1) = im (m n)`

#### [Kenny Lau (Mar 27 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278571):
what do you mean?

#### [Simon Hudon (Mar 27 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278628):
you were mentioning subsets relations so here is how I would encode the different flavors:

#### [Kenny Lau (Mar 27 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278650):
oh and my first point means that maybe it can be a hierarchy, complex -> exact sequences

#### [Simon Hudon (Mar 27 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278652):
```
structure base_exact_seq (x y : option ℤ) (A : Type u) [has_zero A] :=
  (f : seq x y A)
  (m : Π n, morphism (f n) (f $ n+1))

structure exact_seq_eq (x y : option ℤ) (A : Type u) [has_zero A] extends base_exact_seq x y A :=
  (eq : Π n, ker (m $ n + 1) = im (m n))

structure exact_seq_sub (x y : option ℤ) (A : Type u) [has_zero A] extends base_exact_seq x y A :=
  (eq : Π n, ker (m $ n + 1) ⊆ im (m n))

structure exact_seq_super (x y : option ℤ) (A : Type u) [has_zero A] extends base_exact_seq x y A :=
  (eq : Π n, ker (m $ n + 1) ⊇ im (m n))
```

#### [Simon Hudon (Mar 27 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278714):
```quote
oh and my first point means that maybe it can be a hierarchy, complex -> exact sequences
```
I don't understand that. Are you saying that complex numbers are somehow a more general notion than exact sequences?

#### [Kenny Lau (Mar 27 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278782):
complexes are instead of having im=ker, you have im subset ker

#### [Kenny Lau (Mar 27 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278783):
more compactly, f_(n+1) f_n = 0

#### [Kenny Lau (Mar 27 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278785):
even more compactly, f^2=0

#### [Simon Hudon (Mar 27 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278813):
Ah! I see

#### [Simon Hudon (Mar 27 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278858):
You might want instances of `has_coe` between those. Otherwise you'll hit the new structure constraint against repeated fields

#### [Simon Hudon (Mar 27 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278929):
Alright, I'll need to sign off now and get some writing done. I hope this helped

#### [Kenny Lau (Mar 27 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124278935):
ok thanks

#### [Kenny Lau (Mar 27 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124279770):
I think I'm wrong. You can't just fill in zeroes to make a long exact sequence from a short one

#### [Kenny Lau (Mar 27 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124279772):
you can do that for complexes, not exact sequences

#### [Kenny Lau (Mar 27 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124279775):
oh well it's more troublesome

#### [Kenny Lau (Mar 27 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124279782):
if you have A->B->C

#### [Kenny Lau (Mar 27 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124279784):
you can encode it inside ...->0->0->ker f->A->B->C->coker g->0->0->...

#### [Kenny Lau (Mar 27 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124279785):
but that's troublesome

#### [Kenny Lau (Mar 27 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124279786):
but most short exact sequences end and start with zero

#### [Kenny Lau (Mar 27 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124279790):
but there are also those that do not, e.g. in dealing with tensors

#### [jmc (Mar 27 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124280782):
But Simon's proposal includes bounded sequences, right?

#### [Andrew Ashworth (Mar 27 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124283973):
maybe you could ask Floris about exact sequences, seeing as how they are working with spectral sequences in HoTT

#### [Andrew Ashworth (Mar 27 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124284031):
the sequences repository linked earlier is really quite extensive

#### [Simon Hudon (Mar 28 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124331318):
```quote
But Simon's proposal includes bounded sequences, right?
```
Yes exactly. The sequence has no information from outside its bounds except that you can still look beyond the bounds and get `0`. Right now, it requires you to provide morphisms even for (non-)elements outside the bounds of the sequence. We can probably change that

#### [Mario Carneiro (Mar 28 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124331770):
Although it's possible to represent N, Z, fin sequences all as special cases of the same thing, I'm not convinced it's worth it - when you want to work with it you will have a lot of redundant structure and it will be cumbersome to talk about the objects

#### [Mario Carneiro (Mar 28 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124331815):
Maybe you could have both the general structure and the special cases, with coercions or similar embeddings

#### [Simon Hudon (Mar 28 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124332292):
That was my first proposal but I got some push back because I was representing finite sequences as inductive types

#### [Mario Carneiro (Mar 28 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124332552):
I need to figure out how Patrick got traumatized by inductive types, because they are much easier in lean formalization than index arithmetic

#### [Simon Hudon (Mar 28 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124332704):
I'm wondering in this situation if having one construction instead of four might be easier to work with

#### [Mario Carneiro (Mar 28 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124332730):
I think it is important how the construction is to be used to answer that question

#### [Simon Hudon (Mar 28 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124332813):
Yeah, that makes sense.

#### [Mario Carneiro (Mar 28 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124332827):
One way to encode the +1 stuff is to have a graph relation predicate, so that it becomes closer to a diagram in the category theory sense

#### [Mario Carneiro (Mar 28 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124332835):
i.e. using `inductive P : I -> I -> Prop | mk (n) : P n (n+1)`

#### [Simon Hudon (Mar 28 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124332995):
You would use that with the construction with intervals?

#### [Kevin Buzzard (Mar 28 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333093):
The thing about inductive types is that whilst they're clearly a very cute computer science way to do things, especially if you want to prove things by induction,

#### [Kevin Buzzard (Mar 28 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333100):
when a mathematician thinks of an exact sequence they really do not think of it as an "inductive gadget"

#### [Kevin Buzzard (Mar 28 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333110):
and the same is true probably for lots of things like graphs or trees or something, which CS people seem to love constructing via inductive data types

#### [Kevin Buzzard (Mar 28 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333119):
but which mathematicians just build in a completely different way.

#### [Kevin Buzzard (Mar 28 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333129):
Probably because they rarely prove anything by induction, they're just interested in other questions.

#### [Kevin Buzzard (Mar 28 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333134):
I mean, on things like trees or exact sequences

#### [Mario Carneiro (Mar 28 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333175):
I think the mathematician is generally not worried about the particular representation, because they never go into the gory details anyway

#### [Kevin Buzzard (Mar 28 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333181):
You might be right.

#### [Kevin Buzzard (Mar 28 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333184):
I remember Patrick saying something like "this is so far from what I would write on the blackboard"

#### [Kevin Buzzard (Mar 28 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333204):
but perhaps what he means by this is that the informal idea is so clear to a mathematician that they don't need to spell out such a recursive definition.

#### [Kevin Buzzard (Mar 28 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333218):
Perhaps the natural numbers are a great example. They're just "the natural numbers, duh"

#### [Kevin Buzzard (Mar 28 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333222):
and you learn them when you're 4 years old

#### [Kevin Buzzard (Mar 28 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333230):
and you don't learn proof by induction until you're 17 (at least in the UK)

#### [Kevin Buzzard (Mar 28 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333238):
So I define the natural numbers in my class as "N := {1,2,3,...}"

#### [Kevin Buzzard (Mar 28 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333281):
and Patrick defines them as "N := {0,1,2,3,...}"

#### [Kevin Buzzard (Mar 28 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333289):
and that's what gets written on the blackboard, forget about nat.succ etc

#### [Kevin Buzzard (Mar 28 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333356):
I'm just reading the part about formal v informal proofs in Software Foundations. You might want to argue that mathematicians often give "informal definitions".

#### [Kevin Buzzard (Mar 28 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333447):
Mathematicians use the word induction like this: "Theorem: $$\Sigma_{i=1}^n i^2=n(n+1)(2n+1)/6.$$ Proof: induction. $$\qed$$

#### [Kevin Buzzard (Mar 28 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333457):
not "definition of natural numbers by induction"

#### [Mario Carneiro (Mar 28 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333579):
I think we should encourage an agnosticism wrt representations in lean as well, by means of abstracting a construction into its important properties. Once you've done this the exact definition doesn't matter. CS people know about this by the name "interface", mathematicians know this in the big cases via structures like "ring" that abstract a bunch of properties, but I think they are less used to doing this with every construction

#### [Simon Hudon (Mar 28 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333581):
I think even if they don't see natural numbers as Peano's construction, "by induction" assumes an inductive definition underneath, often a well-founded relation ... unless you define induction as "a thing natural numbers can do"

#### [Mario Carneiro (Mar 28 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333612):
For example, once you have defined the addition and multiplication on C, it stops mattering that the definition was R x R as opposed to something else

#### [Kevin Buzzard (Mar 28 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333721):
The projectors are super-important on C

#### [Kevin Buzzard (Mar 28 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333733):
I don't think mathematicians see N as any different to R in some sense

#### [Kevin Buzzard (Mar 28 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333739):
sure you can do induction on one but not the other

#### [Kevin Buzzard (Mar 28 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333743):
but who cares about some random property like induction.

#### [Kevin Buzzard (Mar 28 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333748):
You guys are putting it on some sort of pedestal

#### [Kevin Buzzard (Mar 28 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333751):
N and R are just sets of numbers that you can do stuff with

#### [Kevin Buzzard (Mar 28 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333820):
I think I might spend some time over the summer making stuff into interfaces somehow. I am still concerned about manipulating finite sums. I want $$\Sigma_{i=1}^na_i = \Sigma_{i=1}^na_{n+1-i}$$ to be trivial

#### [Kevin Buzzard (Mar 28 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333824):
or at least "something with a name you can guess"

#### [Kevin Buzzard (Mar 28 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333878):
and $$\Sigma_{i=1}^n\Sigma_{j=1}^i ... = \Sigma_{j=1}^n\Sigma_{i=j}^n ...$$

#### [Kevin Buzzard (Mar 28 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333885):
because unfortunately for mathematicians this is "proof by obvious"

#### [Kevin Buzzard (Mar 28 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333887):
and I'm well aware that in this world it's not

#### [Kenny Lau (Mar 28 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333888):
there is real induction :P

#### [Kenny Lau (Mar 28 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333889):
it is used to prove that [0,1] is compact and connected

#### [Kenny Lau (Mar 28 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333893):
(both proofs use real induction)

#### [Kenny Lau (Mar 28 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333908):
it can also be used to reason about differential equations

#### [Kevin Buzzard (Mar 28 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333912):
Even $$\Sigma_{i=1}^a\Sigma_{j=1}^b...=\Sigma_{j=1}^b\Sigma_{i=1}^a...$$

#### [Kevin Buzzard (Mar 28 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333916):
I'm not sure I'd call the $$[0,1]$$ thing induction

#### [Kevin Buzzard (Mar 28 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333917):
it's just the completeness axiom

#### [Kenny Lau (Mar 28 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333921):
which one?

#### [Kenny Lau (Mar 28 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333962):
oh and real induction is basically "every non-empty clopen subset of R is R itself"

#### [Kevin Buzzard (Mar 28 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333967):
That's precisely the statement of connectedness.

#### [Kenny Lau (Mar 28 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333970):
they're so intertwined that you can't distinguish them

#### [Kevin Buzzard (Mar 28 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333977):
You might want to think of various things as induction but if you want to communicate with mathematicians you'd better know what they call these facts (and have called them for 100 years)

#### [Kenny Lau (Mar 28 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124333982):
https://math.stackexchange.com/a/4204/328173

#### [Chris Hughes (Mar 28 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334035):
```quote
I think I might spend some time over the summer making stuff into interfaces somehow. I am still concerned about manipulating finite sums. I want $$\Sigma_{i=1}^na_i = \Sigma_{i=1}^na_{n+1-i}$$ to be trivial
```
It is trivial, because I proved it. Most of these "obvious things that aren't obvious in lean" problems are solved by proving a few lemmas.

#### [Kenny Lau (Mar 28 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334050):
master of finite sums

#### [Kevin Buzzard (Mar 28 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334051):
Chris -- we need an "obvious_sum_thing" tactic :-)

#### [Kevin Buzzard (Mar 28 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334102):
it's probably defined as "apply thing_chris_proved <|> apply _other_thing_chris_proved <|> apply some_other_thing_chris_proved"

#### [Kevin Buzzard (Mar 28 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334122):
My goal is to make Lean so that mathematicians can use it the way they do mathematics.

#### [Kevin Buzzard (Mar 28 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334126):
I think this will be hard, but that's what I'm striving for.

#### [Kevin Buzzard (Mar 28 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334178):
So when they are faced with some dumb sum re-arrangement they just look at the page on sums in some reference document and they see exactly the thing they want, spelt out.

#### [Kevin Buzzard (Mar 28 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334180):
and if even that's too much, then we write a tactic

#### [Kevin Buzzard (Mar 28 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334190):
Do you remember that Kenny you and I were talking about things being "maths hard" or "Lean hard" (i.e. "obvious" but a pain to formalise)

#### [Kenny Lau (Mar 28 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334193):
I don't

#### [Kevin Buzzard (Mar 28 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334194):
those are the bits I want to formalise, those last bits, and I hide them all in xena directory

#### [Kenny Lau (Mar 28 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334198):
you want to formalize the property of being difficult to be formalized?

#### [Kevin Buzzard (Mar 28 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334206):
I want to formalise all the instances that my students discover

#### [Kevin Buzzard (Mar 28 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334259):
Maybe it was me and Chris and you. I think it was even you that coined the phrase "Lean hard" (which I interpreted informally as meaning "trivial for a mathematician but rfl doesn't work")

#### [Kevin Buzzard (Mar 28 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334268):
Maybe it was Chris.

#### [Kenny Lau (Mar 28 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334269):
how is "Kenny you and I" different from "me and Chris and you"

#### [Kevin Buzzard (Mar 28 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334312):
Oh I just misread what I wrote so restated something I'd already stated

#### [Kenny Lau (Mar 28 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334320):
lol

#### [Kenny Lau (Mar 28 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334322):
simp [and_comm, and_assoc, and_left_comm]

#### [Kenny Lau (Mar 28 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334324):
rfl

#### [Andrew Ashworth (Mar 28 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334401):
```quote
So when they are faced with some dumb sum re-arrangement they just look at the page on sums in some reference document and they see exactly the thing they want, spelt out.
```
that would be an interesting project. formalizing a handbook on sequences, sums, integrals, and derivatives

#### [Andrew Ashworth (Mar 28 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334405):
i have one such handbook sitting on my shelf, it's quite thick

#### [Kevin Buzzard (Mar 28 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334524):
fortunately integrals and derivatives are not my problem

#### [Kevin Buzzard (Mar 28 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334530):
at least not at the minute

#### [Kevin Buzzard (Mar 28 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334539):
and I'm not worried about the mathematical content

#### [Kevin Buzzard (Mar 28 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334543):
it's the trivial stuff that I want to make trivial

#### [Andrew Ashworth (Mar 28 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334651):
i'm so uncomfortable with this word trivial

#### [Andrew Ashworth (Mar 28 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334704):
i don't think under the hood these things are actually trivial

#### [Mario Carneiro (Mar 28 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334708):
I think mathematicians are really good at fooling themselves here

#### [Mario Carneiro (Mar 28 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334729):
But I think Chris was right. "Trivial" is a synonym for "proved"

#### [Andrew Ashworth (Mar 28 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334731):
for example, you could ask any high schooler if real numbers are trivial... if they can rattle off the value of pi and know how to use e with logarithms... but they're in a shock if they ever figure out how they're built

#### [Andrew Ashworth (Mar 28 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334796):
in a similar manner any programmer can use javascript and python to staple together a vast array of libraries to do anything under the sun

#### [Kenny Lau (Mar 28 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334810):
to Kevin "trivial" means "things that are repeated 100 times and so have become part of the intuition"

#### [Andrew Ashworth (Mar 28 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334811):
but using is not understanding

#### [Andrew Ashworth (Mar 28 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334895):
i think a general tactic would be difficult to write

#### [Andrew Ashworth (Mar 28 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334900):
but a library of common results is very feasible

#### [Andrew Ashworth (Mar 28 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334904):
like the lemmas Chris has proved

#### [Kevin Buzzard (Mar 28 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334973):
I've seen PhD students prove hard theorems and then claim that all their results are trivial.

#### [Kevin Buzzard (Mar 28 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124334978):
I've had to explain to them that everything is trivial once you fully understand the proof.

#### [Mario Carneiro (Mar 28 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335000):
Right, that's exactly the point. A trivial fact need not be trivial to lean, until lean understands it, i.e. it is formally proven

#### [Mario Carneiro (Mar 28 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335152):
Perhaps part of the issue is conflating meanings of "trivial". If "trivial" means "I understand it and there are no surprising things in it", then the PhD may well find their results to be trivial. But this is by no means the same as "an outsider would immediately see how to construct the proof"

#### [Simon Hudon (Mar 28 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335290):
I agree. I find the word more obfuscating than enlightening. I usually take it to mean "I can't be bothered to elaborate"

#### [Simon Hudon (Mar 28 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335318):
Already, if you say "by basic calculus" you're not giving a lot of details but the reader knows where to go if they don't want to take your word for it

#### [Kevin Buzzard (Mar 28 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335471):
Another issue is that trained mathematicians become extremely proficient at their art. I would expect anyone at my university to see that once you've been told what the sum of the first n squares is, you can see that there will be a trivial proof by induction. However

#### [Kevin Buzzard (Mar 28 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335524):
what happens later on is that you make assertions about more complex objects (or even classes of complex objects, like schemes) and you say "fact X is true, and the proof is just that you generalise the standard proof of theorem T to this situation"

#### [Kevin Buzzard (Mar 28 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335533):
and in general mathematicians (in my experience at least) are _extremely_ good at processing this idea and coming up with an opinion on whether this proof strategy will work.

#### [Kevin Buzzard (Mar 28 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335552):
The problem is that sometimes you see people getting this wrong: you can have conversations of the form "X will be true, you can prove it by using technique Y...and then probably you can finish the job by induction"

#### [Kevin Buzzard (Mar 28 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335554):
and two people agree, but one other person goes very quiet

#### [Kevin Buzzard (Mar 28 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335560):
and then 30 seconds later they say "what if pathology Z occurs?"

#### [Kevin Buzzard (Mar 28 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335607):
and then all of a sudden the conversation gets very animated and perhaps 1 minute later they have either proved that Z can't occur and everyone is now convinced that the theorem is proved

#### [Kevin Buzzard (Mar 28 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335617):
or someone has concocted an example of a scheme with pathology Z and all of a sudden X is an open question again, or perhaps even we have a counterexample.

#### [Kevin Buzzard (Mar 28 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335623):
This is normal communication amongst mathematicians.

#### [Kevin Buzzard (Mar 28 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335655):
In some sense what I am worried about in my area of mathematics is that this has now gone too far, and there are so many subtleties that one has to be aware of, and so few people that are on top of most or all of them, that the process actually produces inaccurate results.

#### [Kevin Buzzard (Mar 28 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335703):
And what is frustrating is that in many cases, X is true, because there's a far more elaborate argument which deals with the pathology that everyone overlooked

#### [Chris Hughes (Mar 28 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335704):
I think Kevin is right that there are some things that are "obvious", hard to prove, but don't come up often enough for them to be in the library. Here's an example
```lean
example (n : ℕ) (f : ℕ → ℕ) (g : fin n → ℕ) (h : ∀ i : fin n, f i.1  = g i) : (range n).sum f = univ.sum g

```

#### [Kevin Buzzard (Mar 28 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335705):
so you can't just say "your theorem is wrong, here is a counterexample"

#### [Kevin Buzzard (Mar 28 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335711):
you have to just say "I don't understand this bit of the argument"

#### [Kevin Buzzard (Mar 28 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335720):
to which the response is sometimes "oh yeah this needs clarification"

#### [Kevin Buzzard (Mar 28 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335722):
and sometimes "you should just work harder then"

#### [Kevin Buzzard (Mar 28 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335787):
Right -- to a mathematician Chris' statement is trivial.

#### [Kevin Buzzard (Mar 28 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335791):
Now is that because the human brain is not a computer?

#### [Kevin Buzzard (Mar 28 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335793):
Or is it because Lean is bad?

#### [Kevin Buzzard (Mar 28 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335795):
Or is it because I am not thinking about the question in the right way?

#### [Kevin Buzzard (Mar 28 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335882):
This seems to me to be a great example of "too many notions of finiteness". It's quite hard to actually even write down something a mathematician would understand which is not of the form "prove X = X" here. The issue is that range n is not fin n

#### [Kevin Buzzard (Mar 28 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335889):
And I'm sure Mario could come up with a one-liner

#### [Kevin Buzzard (Mar 28 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335892):
but I am not at all sure that my first year students could.

#### [Kevin Buzzard (Mar 28 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124335983):
The idea is that because this is a question only about f's values on range(n), f is somehow "mathematically equivalent" to g

#### [Kevin Buzzard (Mar 28 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336040):
` example (n : ℕ) (f : ℕ → ℕ) (g : fin n → ℕ) (h : ∀ i : fin n, f i.1  = g i) : (range n).sum (\lam x, (x + f x)^2) = univ.sum (\lam i, (g i + i.1)*(g i + i.1)`

#### [Kevin Buzzard (Mar 28 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336048):
You could imagine something like that happening in practice, and again the mathematician wants to invoke the "it's obvious" axiom.

#### [Kevin Buzzard (Mar 28 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336050):
tactic.

#### [Mario Carneiro (Mar 28 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336052):
Looking at Chris's problem, my first instinct is to see if it follows from appropriate compositions of theorems

#### [Kevin Buzzard (Mar 28 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336057):
I'm sure you can prove it in one line.

#### [Kevin Buzzard (Mar 28 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336059):
But the question is how to make so that any mathematician can prove it in one line.

#### [Mario Carneiro (Mar 28 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336100):
Once you have the right theorems you can just chain them

#### [Chris Hughes (Mar 28 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336101):
I'm struggling to prove it at all.

#### [Mario Carneiro (Mar 28 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336103):
that's what a good library does for you

#### [Kevin Buzzard (Mar 28 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336105):
Right.

#### [Kevin Buzzard (Mar 28 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336107):
and then a good reference manual guides you through.

#### [Chris Hughes (Mar 28 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336112):
`sum_attach` almost does it

#### [Mario Carneiro (Mar 28 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336124):
First of all, `g` is unnecessary

#### [Kevin Buzzard (Mar 28 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336129):
yes

#### [Mario Carneiro (Mar 28 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336131):
although it's probably nice for use in a lemma

#### [Mario Carneiro (Mar 28 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336191):
Now how do we know `fin n` is finite, so that `univ` exists? It is surely a map of `finset.range n`

#### [Mario Carneiro (Mar 28 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336223):
Sure enough, it is defined from `list.pmap fin.mk (list.range n) (λ a, list.mem_range.1) `

#### [Mario Carneiro (Mar 28 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336270):
so you want a lemma about mapping over `list.pmap` or its finset equivalent

#### [Kevin Buzzard (Mar 28 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336505):
An alternative approach is just to prove it by induction. Then you'd need four theorems

#### [Kevin Buzzard (Mar 28 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336515):
Empty sums, and sums to n+1 being sum to n then one more

#### [Kevin Buzzard (Mar 28 2018 at 22:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336663):
This, by the way, is an even simpler example of the thing I was trying (but not really succeeding) to ask about a couple of weeks ago. If a mathematician wants to sum the first n squares in Lean, then I am very unclear about whether they should use the f approach or the g approach. In maths they are one and the same thing. The question I was trying to ask a couple of weeks ago is whether in situations like this there is "a correct Lean answer".

#### [Chris Hughes (Mar 28 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336669):
Induction is quite difficult. I got stuck here.
```lean
g : fin (succ n) → ℕ
⊢ sum univ (λ (i : fin n), g ⟨i.val, _⟩) = sum (erase univ ⟨n, _⟩) g
```

#### [Kevin Buzzard (Mar 28 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336680):
But it can just be a theorem in a library once Mario has written the one-liner

#### [Kevin Buzzard (Mar 28 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336732):
You need some sum erase lemma Chris

#### [Chris Hughes (Mar 28 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336743):
It's not as simple as that. My two finsets have different types.

#### [Kevin Buzzard (Mar 28 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336744):
Yes

#### [Kevin Buzzard (Mar 28 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336748):
It's always about the type changing

#### [Kevin Buzzard (Mar 28 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336787):
Presumably it's much easier to do the range induction

#### [Kevin Buzzard (Mar 28 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336795):
The issue is that mathematicians have a really powerful notion of equality

#### [Chris Hughes (Mar 28 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336807):
I think you need to prove it for m \le n, for a finset of type fin n containing elements less than m.

#### [Kevin Buzzard (Mar 28 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124336809):
Where fin succ n "equals" fin n and then n

#### [Kevin Buzzard (Mar 28 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337090):
The finset of type fin n defined as the elements whose value is less than m, is canonically isomorphic (and hence, in a mathematician's mind, equal) to fin m. Just like computer scientists can formulate the recursor for an inductive type, mathematicians have some sort of construction which enables them to pass effortlessly between canonically isomorphic objects. For me, range n and fin n are canonically isomorphic, and your result is an immediate application of some sort of theorem formalising the assertion that doing the same thing to two canonically isomorphic situations results in the same answer.

#### [Kevin Buzzard (Mar 28 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337115):
It's a fact that fin n and range n are canonically isomorphic via the map sending i to i.1

#### [Kevin Buzzard (Mar 28 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337158):
Chris' assumption ` (h : ∀ i : fin n, f i.1  = g i) ` is the statement that this canonical isomorphism extends to a canonical isomorphism between the pair (f restricted to range n,range n) and (g,fin n)

#### [Kevin Buzzard (Mar 28 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337173):
and now a general "thing" analogous to a recursor says that any construction which spits out an object which is unique up to unique isomorphism (such as a natural number) will spit out the same object if it is applied to two canonically isomorphic situations.

#### [Kevin Buzzard (Mar 28 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337174):
That is the way a mathematician thinks about this question.

#### [Kevin Buzzard (Mar 28 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337225):
More generally g i could have been some group

#### [Kevin Buzzard (Mar 28 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337229):
and f (i.1) could have been a canonically isomorphic group

#### [Kevin Buzzard (Mar 28 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337231):
and then the product of the f(i.1) would only have been canonically isomorphic to the product of the g(i)

#### [Kevin Buzzard (Mar 28 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337296):
Where are these notions in dependent type theory?

#### [Kevin Buzzard (Mar 28 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337530):
I want a general theorem which takes an inputs (1) a bijection `fin n = range n` (mathematicians would even write this map as = ) and (2) a construction on the fin n side (such as the function sending `g : fin n -> nat` to `univ.sum g`) and spits out (a) a function f from range n to nat (b) a proof of ` ∀ i : fin n, f i.1  = g i ` and (c) a proof of ` (range n).sum f = univ.sum g `. All of this is internalised somehow in mathematics as being sufficiently obvious as to not need a proof. Unfortunately what I write somehow doesn't make sense because range n is not a type.

#### [Kevin Buzzard (Mar 28 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337580):
I can't even formalise what I want.

#### [Chris Hughes (Mar 28 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337596):
Finally proved it. Not pretty
```lean
example (n : ℕ) (f : ℕ → ℕ) (g : fin n → ℕ) (h : ∀ i : fin n, f i.1  = g i) :
(range n).sum f = univ.sum g :=
show ((range n).1.map f).sum = (univ.1.map g).sum,
from
have h₂ : (univ : finset (fin n)).1  = (range n).1.pmap (λ m hm, fin.mk m hm) (λ m, (@mem_range _ _).1) :=
  show (↑(list.pmap fin.mk (list.range n) _) : multiset _) = multiset.pmap fin.mk ((range n).val) _,
  by rw ← multiset.coe_pmap; refl,
have h₁ : (range n).1.map f = univ.1.map g :=
begin
  rw [h₂, multiset.map_pmap],
  simp only [(h _).symm],
  rw multiset.pmap_eq_map,
end,
by rw h₁
```

#### [Kevin Buzzard (Mar 28 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337657):
I thought you were supposed to be revising mechanics?

#### [Kevin Buzzard (Mar 28 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337748):
Chris if I now asked you to prove something like: if `f : nat -> {2,4,6}` and `g : fin n -> {2,4,6}` and h is the same, then max of f over range(n) equalled max of g over fin n, would the proof be "the same"?

#### [Kevin Buzzard (Mar 28 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337754):
Or would you have to change some application of some theorem in the library to an application of another theorem?

#### [Kevin Buzzard (Mar 28 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337810):
or if f : nat -> bool and g : fin n -> bool, and I asked you to prove that f(0) and f(1) and ... and f(n-1) = g(0) and g(1) and ... and g(n-1), would the proof be "the same"?

#### [Kevin Buzzard (Mar 28 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337823):
(assuming the functions existed which and'd together a list of bools)

#### [Chris Hughes (Mar 28 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337836):
More or less, but with fold instead of sum. I actually got a fair amount of revision done today, so I thought I'd treat myself to lean.

#### [Kevin Buzzard (Mar 28 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337837):
(oh crap there would be two such functions? One for fin n and one for range(n)?

#### [Mario Carneiro (Mar 28 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337892):
It is not true that `fin n` and `range n` are canonically isomorphic, because they aren't even the same kind of thing

#### [Kevin Buzzard (Mar 28 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337902):
I know

#### [Kevin Buzzard (Mar 28 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337903):
but they are

#### [Kevin Buzzard (Mar 28 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337913):
it's impossible to decide either way because there is no definition of canonical

#### [Mario Carneiro (Mar 28 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337921):
`range n` is to be thought of as the LIST `[0,1,2,...,n-1]`, `fin n` is the SET of numbers less than n

#### [Mario Carneiro (Mar 28 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337926):
What can be said is that `range n` enumerates `fin n`

#### [Kevin Buzzard (Mar 28 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337927):
and I completely understand that in type theory it doesn't make sense to write down a map from one to the other

#### [Mario Carneiro (Mar 28 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337935):
and that's what `pmap` is doing

#### [Kevin Buzzard (Mar 28 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337952):
` unknown identifier 'pmap' `

#### [Mario Carneiro (Mar 28 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124337994):
`{list,multiset}.pmap`

#### [Kevin Buzzard (Mar 28 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338005):
It's really annoying that imports have to be on line 1. Is that just something that can never change?

#### [Mario Carneiro (Mar 28 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338018):
I don't think it would be a good idea to change

#### [Kevin Buzzard (Mar 28 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338023):
I don't think it's true in python

#### [Kevin Buzzard (Mar 28 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338024):
that well-known functional language

#### [Mario Carneiro (Mar 28 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338025):
The collection of imports allows you to easily see file-level dependencies

#### [Mario Carneiro (Mar 28 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338031):
It's standard practice in C/C++/java

#### [Kevin Buzzard (Mar 28 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338115):
`#check multiset.pmap` (rolls eyes) `#check  @multiset.pmap`

#### [Kevin Buzzard (Mar 28 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338165):
How was I supposed to know that `?M_3` was a map from `?M_1` to `Prop`?

#### [Kevin Buzzard (Mar 28 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338245):
Mario you're right, there is somehow a difference between objects which are superficially in bijection to a naive eye and types which really do biject. So one of the problems here is that this underlying set with size n is being modelled both as a type and as data, and one has to find a route from one to the other.

#### [Kevin Buzzard (Mar 28 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338337):
So my "general principle" needs to be broken down into several specific instances. This is somehow what I was trying to ask a couple of weeks ago. I was asking a too high-powered question. I was asking "let's say someone proves Lagrange's theorem for some notion of a finite group. However are we now going to port this to a proof of Lagrange's theorem for some other notion of a finite group?" I am not sure anyone ever understood what I was asking.

#### [Kevin Buzzard (Mar 28 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338402):
But Chris' question is much better. "Say I have formalised the notion of sum of f(i) for 0<=i<n in some way in dependent type theory. How am I going to prove that my sum equals the sum as formalised in a different way?"

#### [Kevin Buzzard (Mar 28 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338421):
Let me stress and stress and stress that in mathematics there is only one way to formalise this, and it's $$\Sigma_{i=0}^{n-1}f(i).$$

#### [Kevin Buzzard (Mar 28 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338491):
You guys even might need to prove that if f and g are two functions nat -> nat and f(i) = g(i) for all i < n, then the sums are equal.

#### [Kevin Buzzard (Mar 28 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338505):
The proof of this is not rfl. And yet it is manifestly obvious in some way.

#### [Kevin Buzzard (Mar 28 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338509):
What is going on here?

#### [Kevin Buzzard (Mar 28 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338519):
I have to prove it by induction on n.

#### [Kevin Buzzard (Mar 28 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338534):
In Lean. But it wouldn't make it to the blackboard ;-)

#### [Chris Hughes (Mar 28 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338580):
```quote
You guys even might need to prove that if f and g are two functions nat -> nat and f(i) = g(i) for all i < n, then the sums are equal.
```
`finset.sum_congr` already does that.

#### [Kevin Buzzard (Mar 28 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338590):
aah but only for finsets :-)

#### [Kevin Buzzard (Mar 28 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338597):
What about if I make the sum over fin n?

#### [Kevin Buzzard (Mar 28 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338601):
f(i.1) etc

#### [Kevin Buzzard (Mar 28 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338604):
now you have to provide me with another lemma.

#### [Kevin Buzzard (Mar 28 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338647):
And what if I then wanted it over the multiset {1,2,...,n}?

#### [Kevin Buzzard (Mar 28 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338659):
And then over the list [1,2,...,n]?

#### [Kevin Buzzard (Mar 28 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338672):
These are all different lemmas, right?

#### [Kevin Buzzard (Mar 28 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338680):
all saying the same thing which 95% of mathematicians do not even realise needs a proof.

#### [Kevin Buzzard (Mar 28 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338729):
"If your system doesn't do that automatically what kind of a stupid system is that?"

#### [Kevin Buzzard (Mar 28 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338730):
I can hear the taunts now.

#### [Chris Hughes (Mar 28 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338750):
Computers are stupid. People have been dealing with that fact forever, but it's okay, because they still do a lot of things better than people. The key is to persuade people that lean can do some things better than people.

#### [Kevin Buzzard (Mar 28 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338792):
All of this stuff has to be collected up and curated in a good way. Sounds like Mario and his group have proved most (but possibly not quite all) the lemmas, and now we just need someone to write down their names. I have been carrying round some printouts of lean files for a while now. Did you know `multiset.lean` is 91k long?!

#### [Kevin Buzzard (Mar 28 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338796):
I want Lean to do some things better than people, but as little as possible much much worse than people

#### [Kevin Buzzard (Mar 28 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338800):
and by people I mean mathematicians

#### [Kevin Buzzard (Mar 28 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338802):
obviously

#### [Kevin Buzzard (Mar 28 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338805):
;-)

#### [Kevin Buzzard (Mar 28 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338812):
over 2000 lines of multiset.lean. I read it in the bath occasionally.

#### [Kevin Buzzard (Mar 28 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338839):
My copy is covered in comments.

#### [Mario Carneiro (Mar 28 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338876):
I believe in comprehensive libraries - and that is an achievable goal

#### [Chris Hughes (Mar 28 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338878):
The names already are written down in mathlib. Writing them in a different format won't make any difference. Mostly they don't need to much of an explanation, and mostly they're part of a manageably short list of lemmas with the right word in the name.

#### [Kevin Buzzard (Mar 28 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338893):
I absolutely agree with you that comprehensive libraries are really important and that you are extremely good at providing them.

#### [Mario Carneiro (Mar 28 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338900):
Those examples you gave are not different lemmas for the most part

#### [Mario Carneiro (Mar 28 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338902):
most of it comes from `funext`

#### [Kevin Buzzard (Mar 28 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338904):
What I need to do is to somehow distill from these comprehensive libraries the results which are "so obvious that a mathematician needs to be told how to prove them in Lean"

#### [Mario Carneiro (Mar 28 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338946):
All of it?

#### [Kevin Buzzard (Mar 28 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338949):
Maybe.

#### [Kevin Buzzard (Mar 28 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338952):
Or lots of it, at least.

#### [Kevin Buzzard (Mar 28 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338955):
But somehow I wonder whether we can ignore much of the lower level stuff

#### [Mario Carneiro (Mar 28 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338962):
You shouldn't need to consult the construction of R for work based on it, for example

#### [Kevin Buzzard (Mar 28 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338964):
but I think I really need to concentrate on documenting the stuff which shows up in practice when people are manipulating finite types.

#### [Kevin Buzzard (Mar 28 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338969):
Aah yes, R is a good example. People need to know the name of the theorem which says non-empty and bounded implies LUB

#### [Kevin Buzzard (Mar 28 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338970):
and add_assoc etc

#### [Kevin Buzzard (Mar 28 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124338972):
but they should hopefully never have to open real.lean

#### [Kevin Buzzard (Mar 28 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124339012):
By people I mean mathematicians

#### [Mario Carneiro (Mar 28 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124339013):
I have a long postponed development of sums over nat (similar to Chris's earlier attempt)

#### [Kevin Buzzard (Mar 28 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124339020):
Over July and August I think I will be bombarded with people asking me how to do mathematics that they thought was trivial, in Lean.

#### [Kevin Buzzard (Mar 28 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124339022):
I will answer as best I can.

#### [Kevin Buzzard (Mar 28 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124339032):
I like Zulip. I know I've said this before but starring stuff really is useful. You star it, you forget it, you find the time a week later by which time you've forgotten the name of the topic, and there it is right there in your list of starred messages. Really helps my workflow. I have to go and clean a kitchen.

#### [Kevin Buzzard (Mar 28 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124339071):
Thanks to everyone as ever. This has been really instructive.

#### [Kenny Lau (Mar 29 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124343487):
@**Kevin Buzzard** what is it with you asking everyone to revise mechanics :P

#### [Kevin Buzzard (Mar 29 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124355080):
It's just what I'd be doing if I was your age.

#### [Kenny Lau (Mar 29 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124355092):
@**Kevin Buzzard** I mean, of course we need to revise

#### [Kenny Lau (Mar 29 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124355094):
but what is it with the obsession with mechanics

#### [Kevin Buzzard (Mar 29 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124355291):
It's just what I'd be doing if I was your age.

#### [Kevin Buzzard (Mar 29 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124355298):
Because that one was the course where there seemed to be no axioms :-)

#### [Kenny Lau (Mar 29 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124355300):
fair enough

#### [Kevin Buzzard (Mar 29 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124355301):
"Apply conservation of energy" -> "contradiction" -> "teacher says `obviously energy is lost to heat in this question`

#### [Kevin Buzzard (Mar 29 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124355341):
My conclusion was that conservation of energy was an axiom which should only be applied if desperate.

#### [Kenny Lau (Mar 29 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124355348):
I thought conservation of energy isn't an axiom

#### [Kevin Buzzard (Mar 29 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124355412):
I'd better revise mechanics

#### [Kenny Lau (Mar 29 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124355413):
https://en.wikipedia.org/wiki/Noether%27s_theorem

#### [Andrew Ashworth (Mar 29 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124355459):
+1 for anything that gets closer to formalizing the calculus of variations

#### [Chris Hughes (Mar 30 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124422668):
Shortest proof I can manage of the stupid lemma. More or less wrote itself once I saw `sum_bij` existed.
```lean
example (n : ℕ) (f : ℕ → ℕ) (g : fin n → ℕ) (h : ∀ i : fin n, f i.1  = g i) :
    (range n).sum f = univ.sum g :=
sum_bij (λ i h, ⟨i, mem_range.1 h⟩) (λ _ _, mem_univ _) (λ a ha, h ⟨a, mem_range.1 ha⟩)
(λ _ _ _ _, fin.veq_of_eq) (λ ⟨b, hb⟩ _, ⟨b, mem_range.2 hb, rfl⟩)

```

#### [Kenny Lau (Mar 30 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124422695):
oh wow you proved it

#### [Kenny Lau (Mar 30 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124422696):
congratulations

#### [Kenny Lau (Mar 30 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124422845):
@**Chris Hughes** which modules did you import and which namespaces did you open?

#### [Chris Hughes (Mar 30 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124422940):
`algebra.big_operators` and `data.fintype` and namespace `finset`

#### [Kenny Lau (Mar 30 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124423056):
thanks

#### [Kenny Lau (Mar 30 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124424620):
```
tactic failed, there are unsolved goals
state:
summand : ℕ → ℕ,
n : ℕ
⊢ finset.sum finset.univ (λ (x : fin (succ n)), summand (x.val)) =
    summand n + finset.sum finset.univ (λ (x : fin n), summand (x.val))

#### [Kenny Lau (Mar 30 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124424622):
any guidance?

#### [Mario Carneiro (Mar 30 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124424655):
You shouldn't prove that by induction, you should use chris's lemma

#### [Kenny Lau (Mar 30 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124424675):
no that isn't the same thing

#### [Kenny Lau (Mar 30 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124424677):
and I need to prove that thing

#### [Mario Carneiro (Mar 30 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124424736):
it relates the univ sum to a sum over nat, which has good inductive properties

#### [Chris Hughes (Mar 30 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124424761):
`rw \l sum_insert n` on the `succ n` univ.

#### [Chris Hughes (Mar 30 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124424771):
Then `sum_bij`

#### [Kenny Lau (Mar 30 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124424777):
I see

#### [Chris Hughes (Mar 30 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124425042):
`rw [← insert_erase (mem_univ (⟨n, lt_succ_self n⟩: fin (succ n))), sum_insert (not_mem_erase _ _)], ` is a good start.

#### [Mario Carneiro (Mar 30 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124425141):
```
import algebra.big_operators data.fintype
open finset nat

theorem chris (n : ℕ) (f : ℕ → ℕ) (g : fin n → ℕ) (h : ∀ i : fin n, f i.1  = g i) :
    (range n).sum f = univ.sum g :=
sum_bij
  (λ i h, ⟨i, mem_range.1 h⟩)
  (λ i h, mem_univ _)
  (λ a ha, h ⟨a, _⟩)
  (λ _ _ _ _, fin.veq_of_eq)
  (λ ⟨b, hb⟩ _, ⟨b, mem_range.2 hb, rfl⟩)

example (summand : ℕ → ℕ) (n : ℕ) :
  finset.sum finset.univ (λ (x : fin (succ n)), summand (x.val)) =
    summand n + finset.sum finset.univ (λ (x : fin n), summand (x.val)) :=
by rw [← chris _ _ _ (λ _, rfl), ← chris _ _ _ (λ _, rfl)]; simp
```

#### [Chris Hughes (Mar 30 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124425956):
Don't know why I didn't think of that.

#### [Kenny Lau (Mar 30 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124427350):
@**Kevin Buzzard** in your blog you told us to `apply funext`, but actually you can just `funext`

#### [Kevin Buzzard (Mar 30 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124427917):
I wouldn't believe anything I say :-)

#### [Kenny Lau (Mar 30 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/formalizing%20exact%20sequence/near/124427966):
@**Kevin Buzzard** please moderate my comment

