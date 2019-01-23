---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/90398binomialcoefficients.html
---

## Stream: [maths](index.html)
### Topic: [binomial coefficients](90398binomialcoefficients.html)

---

#### [Kevin Buzzard (Nov 07 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/146974762):
Preparing a lecture on the binomial and multinomial theorem. For pedagogical reasons I will not prove the binomial theorem the way it's proved in Lean (although the students who come to the "extra material" session will see the Lean proof). In Lean I guess the binomial coefficient $$\binom{n}{r}$$ is defined to be $$\frac{n!}{r!(n-r)!}. $$ So is there in Lean a proof that $$\binom{n}{r}$$ equals the number of $$r$$-element subtypes of a a type of size $$n$$? [this is my definition of the binomial coefficient in my lectures]

#### [Johan Commelin (Nov 07 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/146974999):
Do we know that the powerset of a type of size `n` has size `2 ^ n`?

#### [Johan Commelin (Nov 07 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/146975085):
@**Kevin Buzzard** Wouldn't it make sense to define $$n \choose r$$ via Pascal's triangle?

#### [Johannes Hölzl (Nov 07 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/146975630):
it is defined recursively in `mathlib` (in `mathlib/data/nat/choose.lean`):
```lean

def choose : ℕ → ℕ → ℕ
| _             0 := 1
| 0       (k + 1) := 0
| (n + 1) (k + 1) := choose n k + choose n (succ k)
```

#### [Kevin Buzzard (Nov 07 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/146975661):
Sure, that would be another way; then you can prove it's what I said it is by induction on n. Hmm and I guess you could then prove the result about the subsets of size r of a set of size n by induction on n.

#### [Kevin Buzzard (Nov 07 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147108963):
I guess I was just checking that everything I said today was in Lean. I am giving this awful proof of the binomial theorem of the form "imagine multiplying out (a+b)(a+b)(a+b)...(a+b) n times -- now think about what the general term looks like? You choose r brackets and choose a from them, and choose b from the rest -- done"

#### [Kevin Buzzard (Nov 07 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147109092):
but actually I think everything is either there or could be there. @**Johan Commelin** the sum of the binomial coefficients being $$2^n$$ is easy: you can deduce it from the binomial theorem with $$a=b=1$$ ;-)

#### [Johan Commelin (Nov 07 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147109115):
Sure. But that's not exactly what I asked :wink:

#### [Bryan Gin-ge Chen (Nov 07 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147109165):
I think what you asked for is [here](https://github.com/leanprover/mathlib/blob/89431cf4f01ff0f6b4005f96795a23571258cbf0/data/finset.lean#L1198).

#### [Kevin Buzzard (Nov 07 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147242495):
...as long as you can prove that the size of a subset is at most the size of the set (which I am pretty sure is there) and the result about subsets of size r (which should be fine by induction on n).

#### [Bryan Gin-ge Chen (Nov 13 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147613115):
>So is there in Lean a proof that $$\binom{n}{r}$$ equals the number of $$r$$-element subtypes of a type of size $$n$$?

I couldn't find this in mathlib so I've been working off-and-on on this. I finally have a proof, but it seems excessively long and ugly. Well, actually what I have is [a proof of this](https://gist.github.com/bryangingechen/3f8e3fa3664bb4b044e9e607725cab1b):
```lean
lemma card_subsets_of_range_eq_choose (n k : ℕ) :
  card ((powerset (range n)).filter (λ t, card t = k)) = choose n k :=
```
(what should be the name?) though what you really want is this:
```lean
lemma card_subsets_card_eq_choose  {s : finset α} (k : ℕ) : card ((powerset s).filter (λ t, card t = k)) = choose (card s) k :=
sorry
```
[Last time I ran into something like this](https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/tutorial/near/135254614), @**Simon Hudon** ended up writing a bunch of stuff for me which is now in the tutorials branch. This one's probably much easier but I haven't tried to tackle it yet...

Anyways, if anyone wants to golf this down to something reasonable or give advice on making it nicer, I'd really appreciate it!

#### [Mario Carneiro (Nov 13 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147613222):
I would hope to have a function on `list` that constructs all k element sublists

#### [Mario Carneiro (Nov 13 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147613231):
maybe we have it already?

#### [Bryan Gin-ge Chen (Nov 13 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147613251):
Oh that sounds like a good idea.

#### [Mario Carneiro (Nov 13 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147613290):
I don't think we have it

#### [Mario Carneiro (Nov 13 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147613355):
The nice thing about this is that the proof that this list has length `choose n k` will be obvious from the construction

#### [Mario Carneiro (Nov 13 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147613375):
and the rest is just lifting to the quotient

#### [Bryan Gin-ge Chen (Nov 13 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147613405):
right, this is like the approach to finite partitions you suggested before that I still haven't managed to do

#### [Chris Hughes (Nov 13 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147615848):
@**Bryan Gin-ge Chen** 
```lean
def sublists_of_length {α : Type*} : Π (l : list α) (n : ℕ), list (list α) 
| l      0     := [[]]
| []     (n+1) := []
| (a::l) (n+1) := (sublists_of_length l n).map (list.cons a) ++
  (sublists_of_length l (n + 1)) 
```
@**Mario Carneiro** The definition of `list.sublists` in mathlib is totally incomprehensible to me, but is faster than the most natural definition. This approach to `sublist_of_length` is presumably not the fastest. What's the general policy on fast definitions versus comprehensible definitions?

#### [Mario Carneiro (Nov 13 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147615890):
fast is better than comprehensible

#### [Mario Carneiro (Nov 13 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147615949):
you can often prove the comprehensible definition as a lemma though

#### [Mario Carneiro (Nov 13 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147615968):
I think the definition of `list.sublists` is based on haskell's

#### [Chris Hughes (Nov 13 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147615988):
Even if fast means much longer proofs?

#### [Mario Carneiro (Nov 13 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147616009):
yes, although we can also retrofit a faster definition

#### [Johannes Hölzl (Nov 13 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147616013):
for me comprehensible is better than fast. For fast we often need a different solution anyway

#### [Johannes Hölzl (Nov 13 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147616086):
With Lean4 :four_leaf_clover:  we hopefully can simply redefine constants for fast evaluation

#### [Mario Carneiro (Nov 13 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147616098):
Note that in the case of `sublists` there is actually a separate version `sublists'` that is basically the comprehensible one, to which we prove equivalence

#### [Johannes Hölzl (Nov 13 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147616131):
Hm, then it would be better to have `sublist` to be the comprehensible one?!

#### [Mario Carneiro (Nov 13 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147616160):
The idea is that the default one should be VM-fast

#### [Mario Carneiro (Nov 13 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147616174):
because this is in the computational part

#### [Mario Carneiro (Nov 13 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147616280):
(there is an additional complication, in that `sublists` and `sublists'` are not equal but differ by a complicated permutation)

#### [Mario Carneiro (Nov 13 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147616338):
They actually both have fast VM definitions, but `sublists` is faster

#### [Mario Carneiro (Nov 13 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147616348):
and `sublists'` has nicer equation lemmas

#### [Mario Carneiro (Nov 13 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147618019):
here's a faster version of the same definition:
```
def sublists_of_length_aux {α : Type*} : list α → ℕ → (list α → list α) → list (list α) → list (list α)
| l      0     f r := f [] :: r
| []     (n+1) f r := r
| (a::l) (n+1) f r := sublists_of_length_aux l n (f ∘ list.cons a)
  (sublists_of_length_aux l (n + 1) f r)

def sublists_of_length {α : Type*} (l : list α) (n : ℕ) : list (list α) :=
sublists_of_length_aux l n id []
```
the idea is to define `(sublists_of_length l n).map f ++ r` by recursion without stacking recursive calls to `map` or `append`

#### [Mario Carneiro (Nov 13 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147618069):
You can prove without too much difficulty that `sublists_of_length_aux l n f r = (sublists_of_length l n).map f ++ r` and then you can prove your equation lemmas as theorems

#### [Jeremy Avigad (Nov 15 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147712036):
We used to have this in Lean 2 (but it would be nice to have cleaner proofs).
https://github.com/leanprover/lean2/blob/master/library/theories/combinatorics/choose.lean#L208-L220

#### [Bryan Gin-ge Chen (Nov 19 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147980872):
```quote
You can prove without too much difficulty that `sublists_of_length_aux l n f r = (sublists_of_length l n).map f ++ r` and then you can prove your equation lemmas as theorems
```
 Could I get a hint on this step? I'm not sure what to do even to get started:
```lean
def sublists_of_length_aux {α : Type*} : list α → ℕ → (list α → list α) → list (list α) → list (list α)
| l      0     f r := f [] :: r
| []     (n+1) f r := r
| (a::l) (n+1) f r := sublists_of_length_aux l n (f ∘ list.cons a)
  (sublists_of_length_aux l (n + 1) f r)

def sublists_of_length {α : Type*} (l : list α) (n : ℕ) : list (list α) :=
sublists_of_length_aux l n id []

lemma foo {α : Type*} : ∀(l : list α) (n : ℕ) (f : list α → list α) (r : list (list α)),
  sublists_of_length_aux l n f r = (sublists_of_length l n).map f ++ r
| l 0 f r :=
begin
  --unfold sublists_of_length_aux,
  sorry
end
| [] (n+1) f r := sorry
| (a::l) (n+1) f r := sorry
```
I was hoping I could make the first one `refl`, but it seems I need to do something else first, and I'm having trouble working with the definitions.

#### [Mario Carneiro (Nov 19 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147981987):
ah, it looks like lean did a case split on `l` first, then `n`, in the definition of `sublists_of_length_aux`, so that the first equation isn't true by `refl` but rather by `cases l; refl`

#### [Mario Carneiro (Nov 19 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147981997):
you can fix this by swapping the order of the first two arguments to `sublists_of_length_aux`

#### [Bryan Gin-ge Chen (Nov 19 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147982276):
Cool, that did the trick.

#### [Mario Carneiro (Nov 19 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147982611):
but actually I think you want to generalize the lemma a bit to prove it:
```lean
def sublists_of_length_aux {α : Type*} : ℕ → list α → (list α → list α) → list (list α) → list (list α)
| 0     l      f r := f [] :: r
| (n+1) []     f r := r
| (n+1) (a::l) f r := sublists_of_length_aux n l (f ∘ list.cons a)
  (sublists_of_length_aux (n + 1) l f r)

def sublists_of_length {α : Type*} (l : list α) (n : ℕ) : list (list α) :=
sublists_of_length_aux n l id []

lemma foo {α : Type*} : ∀ (n : ℕ) (l : list α) (f g : list α → list α) (r s : list (list α)),
  sublists_of_length_aux n l (g ∘ f) (r.map g ++ s) =
  (sublists_of_length_aux n l f r).map g ++ s
| 0     l      f g r s := rfl
| (n+1) []     f g r s := rfl
| (n+1) (a::l) f g r s := by unfold sublists_of_length_aux;
  rw [foo, show ((g ∘ f) ∘ list.cons a) = (g ∘ f ∘ list.cons a), by refl, foo]
```
The theorem you want is now a simple corollary

