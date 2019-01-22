---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/79327finitesumpuzzle.html
---

## [general](index.html)
### [finite sum puzzle](79327finitesumpuzzle.html)

#### [Kevin Buzzard (Mar 30 2018 at 01:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390119):
```
import tactic.ring

theorem  finset_sum_is_list_sum (f : ℕ → ℕ) (n : ℕ) :
(finset.range n).sum f = ((list.range n).map f).sum :=  sorry
```

#### [Kevin Buzzard (Mar 30 2018 at 01:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390133):
I've been thinking a lot about induction today.

#### [Kevin Buzzard (Mar 30 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390183):
@**Mario Carneiro** Is there some super-cute way of doing this already?

#### [Kevin Buzzard (Mar 30 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390201):
I have been trying to formalise quite an abstract approach to questions like these but for all I know this sort of thing is completely well-known. Note that a mathematician would say this proof was trivial and indeed it would be hard to explain to a mathematician why this needed a proof.

#### [Mario Carneiro (Mar 30 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390250):
It should be by definition, more or less

#### [Mario Carneiro (Mar 30 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390252):
does `rfl` work?

#### [Mario Carneiro (Mar 30 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390310):
Also, of course that needs a proof, stop thinking that proofs that are simple by induction are trivial enough to not need a proof

#### [Ching-Tsun Chou (Mar 30 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390311):
Don't you need the commutativity of "+" on natural numbers?

#### [Mario Carneiro (Mar 30 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390315):
that's on the same lines as saying commutativity of natural numbers is trivial

#### [Mario Carneiro (Mar 30 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390473):
Ah, it's not quite by definition, because multiset prod is not defined in terms of list prod but instead is defined using foldl. This works:
```
theorem finset_sum_is_list_sum (f : ℕ → ℕ) (n : ℕ) :
  (finset.range n).sum f = ((list.range n).map f).sum :=
multiset.coe_sum _
```

#### [Mario Carneiro (Mar 30 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390533):
Here's a slightly less magical way to write it:
```
theorem finset_sum_is_list_sum (f : ℕ → ℕ) (n : ℕ) :
  (finset.range n).sum f = ((list.range n).map f).sum :=
show ((list.range n).map f : multiset ℕ).sum = ((list.range n).map f).sum, from
multiset.coe_sum _
```

#### [Kevin Buzzard (Mar 30 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390583):
`f` can map to an `add_comm_monoid`

#### [Mario Carneiro (Mar 30 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390587):
sure

#### [Kevin Buzzard (Mar 30 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390588):
that's what you need, I believe.

#### [Mario Carneiro (Mar 30 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390594):
the theorem you stated is not maximally general

#### [Kevin Buzzard (Mar 30 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390597):
So this one seems genuinely easier than Chris' problem?

#### [Mario Carneiro (Mar 30 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390600):
yes, because finset sum is defined as a multiset sum over the map

#### [Kevin Buzzard (Mar 30 2018 at 02:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390837):
Here's three more trivial statements:

#### [Kevin Buzzard (Mar 30 2018 at 02:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390842):
```
import tactic.ring 
universe u 
open nat 

theorem list_range_map_sum_induction {X : Type u} [has_add X] [has_zero X] {n : ℕ} (f : ℕ → X) : 
  ((list.range (succ n)).map f).sum = ((list.range n).map f).sum + f n := sorry

theorem finset_range_sum_induction {R : Type u} [add_comm_monoid R] {f : ℕ → R} {d : ℕ} :
  (finset.range (succ d)).sum f = (finset.range d).sum f + f d := sorry 

theorem finset_univ_sum_fin_induction {R : Type u} [add_comm_monoid R] {d : ℕ}
  {f : fin (nat.succ d) → R} :
  finset.univ.sum f = 
    finset.univ.sum (λ i : fin d, f ⟨i.val,lt_trans i.is_lt $ nat.lt_succ_self d⟩) -- d or _?
    + f ⟨d,nat.lt_succ_self _⟩ -- is _ or d better style at the end?
  := sorry 
```

#### [Kevin Buzzard (Mar 30 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390886):
They all say the same trivial thing in maths

#### [Kevin Buzzard (Mar 30 2018 at 02:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390888):
so I am really interested in the slickest possible proofs in Lean

#### [Kevin Buzzard (Mar 30 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390892):
because I suspect that occasionally my students will want statements like this to just go away

#### [Kevin Buzzard (Mar 30 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390947):
If these get unsorried then we get the following proof of Chris' problem from yesterday:

#### [Kevin Buzzard (Mar 30 2018 at 02:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390956):
```
theorem chris_example (n : ℕ) (f : ℕ → ℕ) (g : fin n → ℕ) (h : ∀ i : fin n, f i.1  = g i) : 
(finset.range n).sum f = finset.univ.sum g := begin
induction n with d Hd, refl, -- base case trivial 
-- for the inductive step it's handy to have notation for the restriction of g,
let gres : fin d → ℕ := λ i,g ⟨i.val,lt_trans i.is_lt $ nat.lt_succ_self d⟩,
-- goal now of form "first kind of sum to succ d equals second kind"
rw finset_range_sum_induction,
rw finset_univ_sum_fin_induction,
-- goal now "first sum to d + f d = second sum to d + g d"
rw [(Hd gres (λ i, h ⟨i.val,_⟩))], -- first sum equals second sum
rw h ⟨d,_⟩, -- f d = g d -- so done
end
```

#### [Kevin Buzzard (Mar 30 2018 at 02:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124390957):
with not a `pmap` in sight

#### [Kevin Buzzard (Mar 30 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391040):
I would argue that this was a "natural" proof which hides away the abstraction.

#### [Kevin Buzzard (Mar 30 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391103):
@**Chris Hughes** Here's what another proof of your fin n question might look like.

#### [Mario Carneiro (Mar 30 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391106):
By the way, here's a(nother) proof of chris's theorem:
```
example (n : ℕ) (f : ℕ → ℕ) (g : fin n → ℕ) (h : ∀ i : fin n, f i.1 = g i) :
  (finset.range n).sum f = finset.univ.sum g :=
show ((list.range n).map f : multiset ℕ).sum =
   (((list.range n).pmap fin.mk _).map g : multiset ℕ).sum,
by rw [multiset.coe_sum, multiset.coe_sum, ← (funext h : _ = g),
       list.map_pmap, ← list.pmap_eq_map]
```

#### [Kevin Buzzard (Mar 30 2018 at 02:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391190):
What I don't like about your proofs is that they seem (to me) to involve knowing about some internal implementation of things. My proof is implementation-free. The library maintainer just creates those `blah_sum_induction` proofs (the three things sorried above) , and then the end user can construct proofs of Chris' theorem without having to worry about any other implementation.

#### [Kevin Buzzard (Mar 30 2018 at 02:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391225):
Each of the induction laws gives rise to an abstraction which looks like this:

#### [Mario Carneiro (Mar 30 2018 at 02:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391233):
I agree, chris has found a hole in the mathlib coverage here

#### [Mario Carneiro (Mar 30 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391244):
Your second theorem is provable by `simp`, but `list.range` doesn't break up nicely because the numbers are listed in increasing order

#### [Mario Carneiro (Mar 30 2018 at 02:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391303):
I'm not a big fan of your statement of `finset_univ_sum_fin_induction`, it's all too complicated in the theorem statement

#### [Kevin Buzzard (Mar 30 2018 at 02:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391308):
```
@[reducible] definition sum_map_range {R : Type u} [add_comm_monoid R] (addend : ℕ → R) : ℕ → R
| zero := (0 : R)
| (succ n) := sum_map_range n + addend n

theorem list_range_map_sum_abstraction {R : Type} [add_comm_monoid R] 
  (f : ℕ → R) (n : ℕ) : ((list.range n).map f).sum = sum_map_range f n := sorry

theorem finset_range_sum_abstraction {R : Type u} [add_comm_monoid R] (f : ℕ → R) (n : ℕ) : 
  (finset.range n).sum f = sum_map_range f n := sorry 

theorem finset_univ_sum_fin_abstraction {R : Type u} [add_comm_monoid R] (f : ℕ → R) (n : ℕ) :
  finset.univ.sum (λ i : fin n, f(i.val)) = sum_map_range f n := sorry
```

#### [Kevin Buzzard (Mar 30 2018 at 02:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391312):
yes, the fin one stinks.

#### [Kevin Buzzard (Mar 30 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391365):
If you use lists or finsets then f is a function on N, but to do Chris' problem you had to use a function on fin n

#### [Mario Carneiro (Mar 30 2018 at 02:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391367):
I think there are functions for raising `fin n` to `fin (n+1)`. Alternatively, you could use `fin2`, which has a natural inductive construction instead of being a subtype of nat

#### [Mario Carneiro (Mar 30 2018 at 02:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391379):
`fin2` is not really developed much, but it is defined in `dioph.lean`

#### [Kevin Buzzard (Mar 30 2018 at 02:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391432):
I specifically wanted to design functions which gave me the biggest chance of being covered for all variants of the following question:"this Lean statement is trivially true in maths because it says $$f(0)+f(1)+\cdots+f(n-1)=f(0)+f(1)+\cdots+f(n-1)$$, so how do you prove it in Lean?"

#### [Kevin Buzzard (Mar 30 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391442):
I feel like I have convinced myself that for any way of representing the set $$\{0,1,...,n-1\}$$ in Lean

#### [Kevin Buzzard (Mar 30 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391447):
there is an induction principle and an abstraction principle.

#### [Kevin Buzzard (Mar 30 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391448):
Do I have the right names for these things?

#### [Kevin Buzzard (Mar 30 2018 at 02:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391500):
As you can see, the examples I have attempted to work out are `list.range n`, `fin n` and `finset.range n`

#### [Kevin Buzzard (Mar 30 2018 at 02:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391502):
Sounds like I need to do `fin2 n`

#### [Kevin Buzzard (Mar 30 2018 at 02:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391541):
I should say that I have not proved the induction hypotheses in all cases yet.

#### [Mario Carneiro (Mar 30 2018 at 02:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391544):
It's mostly used for technical reasons; you can also define recursion principles on `fin n` with the same structure as `fin2`

#### [Mario Carneiro (Mar 30 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391552):
but I think that `fz` and `fs` are the right way to think about induction on `fin n`

#### [Kevin Buzzard (Mar 30 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391555):
But as a mathematician I would find a proof of these sorts of thing rather distasteful (they're all "obvious by induction")

#### [Kevin Buzzard (Mar 30 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391597):
so I feel like they should be hidden from view.

#### [Mario Carneiro (Mar 30 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391601):
It's always messy when the function is only partially defined, so that you can't even talk about it out of domain

#### [Mario Carneiro (Mar 30 2018 at 02:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391603):
that's what makes `list.pmap` necessary, and also what makes it a pain to work with

#### [Mario Carneiro (Mar 30 2018 at 02:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391610):
What makes Chris's problem hard is the usage of `g : fin n -> N`

#### [Mario Carneiro (Mar 30 2018 at 02:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391614):
same for your induction principle, `fin (succ n) -> N` is even worse

#### [Mario Carneiro (Mar 30 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391671):
I get the sense that you want to put everything in the form `map_sum_range` of something, but that doesn't work for partial functions

#### [Kevin Buzzard (Mar 30 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391812):
Here's a 4th one

#### [Kevin Buzzard (Mar 30 2018 at 02:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391815):
```
theorem multiset_sum_map_range_induction {X : Type u} [add_comm_monoid X] {n : ℕ} (f : ℕ → X) : 
  ((multiset.range (succ n)).map f).sum = 
   ((multiset.range n).map f).sum + f n := sorry
```

#### [Kevin Buzzard (Mar 30 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391855):
Corresponding to $$\{0,1,\ldots,n-1\}$$ = `multiset.range n`

#### [Kevin Buzzard (Mar 30 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391859):
Each model gives you a new induction principle

#### [Kevin Buzzard (Mar 30 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391867):
which I think mathlib could offer with a standard name

#### [Kevin Buzzard (Mar 30 2018 at 02:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391914):
There are only a finite number of ways that a mathematician can say this trivial thing, and it would be nice if we could just pull a proof out of a hat for each one.

#### [Kevin Buzzard (Mar 30 2018 at 02:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391923):
Could I even write a tactic which proves all these things? Just in some stupid way -- it just tries all the proofs and chooses the one that works.

#### [Kevin Buzzard (Mar 30 2018 at 02:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391932):
aah, `simp` works on that one.

#### [Mario Carneiro (Mar 30 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391981):
I support the definition of your `map_sum_range`, which I and I think chris called `series`; it's on my to do list

#### [Mario Carneiro (Mar 30 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391984):
That would make your `multiset_sum_map_range_induction` theorem, which I might otherwise call `multiset.range_succ_map_sum`, just `series_succ`

#### [Mario Carneiro (Mar 30 2018 at 02:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124391992):
It's not called `induction` because it's not an induction principle

#### [Mario Carneiro (Mar 30 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124392042):
As I've said, I think it will alleviate many of the issues you are having with these sums. If you urgently need it, why not try writing it yourself? Don't worry about connecting it to `finset.range`, just prove everything directly by induction. Then we can relate it to the other ways to talk about finite sums

#### [Kevin Buzzard (Mar 30 2018 at 02:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124392084):
`simp` does the multiset and finset variants, but not the list variant.

#### [Kevin Buzzard (Mar 30 2018 at 02:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124392096):
Can you tell me exactly what you are suggesting I prove? I am interested in getting this done ASAP and I have some time now, term finished.

#### [Kevin Buzzard (Mar 30 2018 at 02:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124392135):
I think your sketches above should enable me to prove everything

#### [Kevin Buzzard (Mar 30 2018 at 02:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124392154):
Sorry about the induction name. I thought carefully about the abstract syntax of the names but I seem to have used the wrong term.

#### [Kevin Buzzard (Mar 30 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124392315):
I love `dioph.lean`

#### [Kevin Buzzard (Mar 30 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124392316):
```
(D∃4 $ D∃5 $ D∃6 $ D∃7 $ D∃8 $
D&7 D* D&7 D- (D&5 D* D&5 D- D.1) D* D&8 D* D&8 D= D.1 D∧
D&4 D* D&4 D- (D&5 D* D&5 D- D.1) D* D&3 D* D&3 D= D.1 D∧
D&2 D* D&2 D- (D&0 D* D&0 D- D.1) D* D&1 D* D&1 D= D.1 D∧
```

#### [Kevin Buzzard (Mar 30 2018 at 03:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124392318):
who could fail to love that bit

#### [Kevin Buzzard (Mar 30 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124392359):
whatever is going on in that file

#### [Mario Carneiro (Mar 30 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124392429):
That's the closest lean comes to a domain specific language right now

#### [Kevin Buzzard (Mar 30 2018 at 03:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124392482):
So there is `vector` and `vector3`. Is there a `vector2`? I can't find it. (`fin2` is used to build `vector3`)

#### [Kevin Buzzard (Mar 30 2018 at 03:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124392530):
I have a Masters student working on Matiesevich's theorem for their project, so I showed them `dioph.lean`. They know no Lean. I'm not sure they found it very helpful.

#### [Mario Carneiro (Mar 30 2018 at 03:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124392536):
There was once a vector2, but I deleted it because it wasn't needed. `vector2` was inductively defined by
```
inductive vector2 (A : Type u) : nat -> Type u
| nil : vector2 0
| cons (n) : A -> vector2 n -> vector2 (succ n)

#### [Mario Carneiro (Mar 30 2018 at 03:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124392542):
From the names, you can guess that `vector`, `vector2` and `vector3` are all isomorphic

#### [Mario Carneiro (Mar 30 2018 at 03:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124392596):
I think you can find it in the file history of `dioph.lean`

#### [Kevin Buzzard (Mar 30 2018 at 03:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124393725):
I can't believe it. I feel like I have learnt something new about induction today, and I have been teaching it for 20 years.

#### [Kenny Lau (Mar 30 2018 at 03:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124393765):
what is it?

#### [Kenny Lau (Mar 30 2018 at 03:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124393769):
well there's always more to learn :P

#### [Kevin Buzzard (Mar 30 2018 at 03:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124393775):
yes but I'm usually trying to look nearer the top

#### [Kevin Buzzard (Mar 30 2018 at 03:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124393844):
There is one abstract principle of induction `g := lam n, sum_to_n f`

#### [Kevin Buzzard (Mar 30 2018 at 04:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124393898):
which you can prove assuming a hypothesis of the form `\forall n, g (succ n) = g n + f n`

#### [Kevin Buzzard (Mar 30 2018 at 04:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124393911):
but the problem is that there are several ways to encode `sum_to_n`in Lean

#### [Kevin Buzzard (Mar 30 2018 at 04:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124393915):
e.g. the "pure" way via an inductive type

#### [Kevin Buzzard (Mar 30 2018 at 04:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124393963):
or ways which create an auxiliary type along the way, like `sum_to_n f = ((list.range n).map f).sum` which at some point builds a list and then sums over it

#### [Kevin Buzzard (Mar 30 2018 at 04:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124394065):
and for each of these design decisions about how you're going to sum this series (e.g. a design decision that some other program has forced upon you) you are given a definition of `sum_to_n : (ℕ → R) → (ℕ → R)`

#### [Kevin Buzzard (Mar 30 2018 at 04:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124394071):
(e.g. `λ f, λ n ((list.range n).map f).sum` )

#### [Kevin Buzzard (Mar 30 2018 at 04:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124394119):
it's now your job to prove `∀ n, sum_to_n (succ n) = sum_to_n n + f n`

#### [Kevin Buzzard (Mar 30 2018 at 04:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124394220):
And that's quite annoying because list doesn't deconstruct like that.

#### [Kenny Lau (Mar 30 2018 at 04:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124394520):
@**Kevin Buzzard** do you have a list of goals?

#### [Kevin Buzzard (Mar 30 2018 at 04:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124394527):
I'm writing a blog post about it. This has been a most enjoyable day.

#### [Kenny Lau (Mar 30 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124394727):
```quote
it's now your job to prove `∀ n, sum_to_n (succ n) = sum_to_n n + f n`
```
done

#### [Kenny Lau (Mar 30 2018 at 04:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124394764):
```
theorem sum_to_n.succ : sum_to_n (n+1) = sum_to_n n + f n :=
begin
  dsimp [sum_to_n],
  rw [list.range_concat],
  rw [list.map_append],
  rw [list.sum_append],
  rw [list.map_singleton],
  rw [list.sum_cons],
  rw [list.sum_nil],
  rw [add_zero]
end

#### [Kenny Lau (Mar 30 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124394965):
version 2

#### [Kenny Lau (Mar 30 2018 at 04:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124394966):
```
theorem sum_to_n.succ : sum_to_n (n+1) = sum_to_n n + f n :=
by simp [sum_to_n, list.range_concat]

#### [Kevin Buzzard (Mar 30 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124399570):
https://wordpress.com/post/xenaproject.wordpress.com/1344

#### [Kenny Lau (Mar 30 2018 at 07:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124399701):
@**Kevin Buzzard** did you sleep?

#### [Kevin Buzzard (Mar 30 2018 at 07:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124399746):
Meh https://xenaproject.wordpress.com/2018/03/30/proofs-by-induction/ is better

#### [Kevin Buzzard (Mar 30 2018 at 07:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124399747):
@**Chris Hughes** or @**Kenny Lau** Feel free to leave comments if you have definitions for `sum_to_n`

#### [Andrew Ashworth (Mar 30 2018 at 07:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124399750):
> but, unfortunately, because I fear that in practice people really might occasionally find themselves in a situation where they need a new kind of proof by induction 

writing new recursion principles is common and expected, from what i've seen out there

#### [Kenny Lau (Mar 30 2018 at 07:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124399807):
“using the fucking ring tactic”

#### [Andrew Ashworth (Mar 30 2018 at 07:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124399819):
you can see some of this in mathlib, where new elimination lemmas are defined fairly frequently

#### [Andrew Ashworth (Mar 30 2018 at 07:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124399859):
if we go back to the nats, strong induction is commonplace yet requires a proof

#### [Kevin Buzzard (Mar 30 2018 at 07:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124399920):
In lean web editor link, `tactic.ring` is not available so I had to prove it the old skool way! Thank you @**Mario Carneiro** for `tactic.ring`. No, it appears I didn't go to sleep and now the sun is up. Crap. I'm behaving like a kid.

#### [Kenny Lau (Mar 30 2018 at 07:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124399923):
lol

#### [Kenny Lau (Mar 30 2018 at 07:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124399972):
i am shocked

#### [Kevin Buzzard (Mar 30 2018 at 07:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124399975):
```quote
writing new recursion principles is common and expected, from what i've seen out there
```
I realised that Chris could solve his problem with good recursion principles.

#### [Kevin Buzzard (Mar 30 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124399979):
I don't have to be up at 7am though, because the kids have finished school now.

#### [Kenny Lau (Mar 30 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124399987):
so the philosophy is to always write eliminators for the things you create?

#### [Kevin Buzzard (Mar 30 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124399988):
If I don't get my act together I'll be up at 7am anyway.

#### [Kevin Buzzard (Mar 30 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124399992):
I guess that might be what I am saying.

#### [Andrew Ashworth (Mar 30 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124399993):
also as a matter of style, you could give names to your function variables as opposed to always lambda-ing them

#### [Kevin Buzzard (Mar 30 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124399994):
Or some version of this.

#### [Kenny Lau (Mar 30 2018 at 07:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124399995):
i am still shocked 😛

#### [Andrew Ashworth (Mar 30 2018 at 07:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124400038):
for example `def square : ℕ → ℕ := λ i, i ^ 2 ` could be `def square n : nat := n ^ 2`

#### [Kenny Lau (Mar 30 2018 at 07:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124400039):
fin has no eliminator though

#### [Kenny Lau (Mar 30 2018 at 07:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124400040):
hence the problem

#### [Kevin Buzzard (Mar 30 2018 at 07:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124400041):
yes, my approach with fin was not much fun.

#### [Kevin Buzzard (Mar 30 2018 at 07:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124400042):
But I need to sleep.

#### [Kenny Lau (Mar 30 2018 at 07:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124400045):
@**Andrew Ashworth** I think he decided he does not care about styles

#### [Kevin Buzzard (Mar 30 2018 at 07:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124400048):
I just wrote it in the way that appealed to me most.

#### [Kevin Buzzard (Mar 30 2018 at 07:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124400052):
I have also written three solutions to the problems.

#### [Andrew Ashworth (Mar 30 2018 at 07:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124400053):
when you're a professor, you can write your homework exercises however you like, haha

#### [Kevin Buzzard (Mar 30 2018 at 07:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124400093):
One of them is just "axiom axiom constant" etc etc, and it's very cool, you can still do the last part :-)

#### [Kenny Lau (Mar 30 2018 at 07:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124400096):
constant name : false

#### [Kenny Lau (Mar 30 2018 at 07:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124400097):
theorem RH : sorry := false.elim name

#### [Kevin Buzzard (Mar 30 2018 at 07:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124400099):
I might be a professor but I am still very much a learner at this game. I'd be happy for any more stylistic comments.

#### [Andrew Ashworth (Mar 30 2018 at 07:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124400142):
it's only really meaningful in large, complicated definitions

#### [Andrew Ashworth (Mar 30 2018 at 07:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124400143):
of which square does not count

#### [Andrew Ashworth (Mar 30 2018 at 07:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124400146):
i will continue to file nitpicking issues if i see them, though

#### [Andrew Ashworth (Mar 30 2018 at 08:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124400603):
actually later on you give summand a nice name so i take back everything i wrote, haha

#### [Kevin Buzzard (Mar 30 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124400647):
In fact my initial draft had an error in which I only spotted when I tried to prove that my genuine summing function was equal the one I defined with constants and axioms

#### [Chris Hughes (Mar 30 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/finite%20sum%20puzzle/near/124407580):
@**Kevin Buzzard** I did define sums and sums between nats here. https://github.com/dorhinj/lean/blob/master/sum_between_nats.lean The proofs aren't mathlib ready and I don't think series is a particularly good name. I proved various basic properties as well.

