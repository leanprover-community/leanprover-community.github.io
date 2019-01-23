---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/71472propextquotsoundandeqrec.html
---

## Stream: [general](index.html)
### Topic: [propext, quot.sound and eq.rec](71472propextquotsoundandeqrec.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Oct 09 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135462261):
Is every `nat` defined using `propext`, `quot.sound` and `eq.rec` but without choice guaranteed to reduce to `succ $ succ $ succ ... zero`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Oct 09 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135481037):
You don't even need `quot.sound`:
```lean
lemma not_refl : true = (true ∨ false) :=
propext (by simp)

def does_not_reduce_to_zero : ℕ :=
@eq.rec_on _ _ (λ _, ℕ) _ not_refl $
0

#print axioms does_not_reduce_to_zero
set_option pp.proofs true
#reduce does_not_reduce_to_zero
#eval does_not_reduce_to_zero
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Oct 09 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135481110):
I'm pretty sure @**Mario Carneiro** has an example lying around that doesn't even need `propext`; I think you can do this even with a counterexample to the transitivity of definitional equality.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 09 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135481440):
An excellent question and an excellent answer!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Olson (Oct 09 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135481619):
Here's an example with quotients:

```lean
def s₁ : multiset ℕ := quotient.mk [1, 2, 3]
def s₂ : multiset ℕ := quotient.mk [2, 1, 3]
theorem s₁_eq_s₂ : s₁ = s₂ := quotient.sound (list.perm.swap _ _ _)
def s₃ : multiset ℕ := eq.rec_on s₁_eq_s₂ s₁

#eval s₂.card -- 3
#eval s₃.card -- 3

#reduce s₂.card -- 3
#reduce s₃.card -- quot.lift list.length _ (eq.rec (quot.mk list.perm [1, 2, 3]) _)
```

AIUI, the kernel reduction rules for quotients only know how to reduce terms in the form ` quot.lift _ _ (quot.mk _ _)`, but `quot.sound` introduces an irreducible `eq`.

EDIT: simplified example

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Oct 09 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135482021):
I did manage to prove `does_not_reduce_to_zero = 0`, after quite a bit of fiddling around. Next question, is there an example where it's not provably equal to something of the form `succ $ succ $ ... 0`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Oct 09 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135482155):
This basically means that a lot of computable functions aren't really computable. That is surprising.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Olson (Oct 09 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135482382):
There's a section about the implications of axioms in Lean here https://leanprover.github.io/theorem_proving_in_lean/axioms_and_computation.html

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Olson (Oct 09 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135482525):
In particular Lean makes a distinction between canonicity (being able to evaluate any closed term of type ℕ to `succ $ succ $ ... 0`) and computability

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Oct 09 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135482544):
```quote
This basically means that a lot of computable functions aren't really computable.
```
No, they're perfectly computable.  Just not using the reduction relation of the type theory.  (The easiest way to compute them is using type erasure, i.e., VM execution.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 09 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135494239):
The extra magic sauce that the VM has and the kernel reduction doesn't is the reduction `eq.rec h e ~> e`, regardless of the type of `h`. This is not type correct unless `h : A = A`, in which case the kernel knows about it as well, but the VM just plows ahead anyway

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 09 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135494367):
This means that the VM deals with terms that are not type correct, and this is resolved by saying that types are "erased" so that now the terms have no meaning except for their reduction behavior. Concretely, this means that any term of type `Sort u` is replaced with `*`, as well as any proofs (terms of type `p : Prop`). When you see me talk about "data" vs non-data, this is what I am talking about. Anything which is a type has no runtime representation except as a neutral object that does nothing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Oct 13 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135706032):
```quote
I'm pretty sure @**Mario Carneiro** has an example lying around that doesn't even need `propext`; I think you can do this even with a counterexample to the transitivity of definitional equality.
```
I had a go at this. Most of the non transitivities contain free variables, but I after a little while I found an example with bound variables instead that was provable without `funext`. The trouble was that even though the `rfl` didn't work as a proof, the proof I wrote instead still reduced to `eq.refl _`, so my `nat` did reduce.
```lean
lemma h (P : ℕ → Prop) (b : ℕ) {C : P b → Type 1} (f : Π h : P b, C h) (h₁ : P b) :
(λ h, f h) = (λ h, f h₁) := rfl

lemma acc_rec_lemma : 
(λ (h₁ : acc (λ _ _, false) 0) {C : ℕ → Type}
(f : Π x, (∀ y, false → acc (λ x y : ℕ, false) y) → (Π y, false → C y) → C x) {a : ℕ}
(h : ∀ y, false → acc (λ _ _ : ℕ, false) y),
  @acc.rec ℕ (λ _ _, false) C f 0 h₁) =
(λ (h₁ : acc (λ _ _, false) 0) {C : ℕ → Type}
(f : Π x, (∀ y, false → acc (λ x y : ℕ, false) y) → (Π y, false → C y) → C x) {a : ℕ}
(h : ∀ y, false → acc (λ _ _ : ℕ, false) y),
  @acc.rec ℕ (λ _ _, false) C f 0 (acc.intro 0 (λ _, false.elim))) :=
by rw h _ _ _ (show acc (λ _ _, false) 0, from acc.intro 0 (λ _, false.elim))
-- rfl didn't work

def does_reduce : ℕ := @eq.rec _ _ (λ _, ℕ) 0 _ acc_rec_lemma

#print axioms does_reduce

#reduce does_reduce
```
@**Mario Carneiro** Is it possible?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 13 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135706590):
not sure how relevant this is, but maybe one can produce some examples using this:
```lean
inductive bad : Type
| bad : list bad → bad

#print prefix bad

/-
bad : Type
bad.bad : list bad → bad
bad.bad.inj : ∀ {a a_1 : list bad}, bad.bad a = bad.bad a_1 → a = a_1
bad.bad.inj_arrow : Π {a a_1 : list bad}, bad.bad a = bad.bad a_1 → Π ⦃P : Sort l⦄, (a = a_1 → P) → P
bad.bad.inj_eq : ∀ {a a_1 : list bad}, bad.bad a = bad.bad a_1 = (a = a_1)
bad.bad.sizeof_spec : ∀ (a : list bad), bad.sizeof (bad.bad a) = 1 + sizeof a
bad.cases_on : Π (C : bad → Sort l) (x : bad), (Π (a : list bad), C (bad.bad a)) → C x
bad.has_sizeof_inst : has_sizeof bad
bad.pack_0_0 : list bad → _nest_1_1.list.bad
bad.pack_0_0.inj : ∀ (a a_1 : list bad), bad.pack_0_0 a = bad.pack_0_0 a_1 ↔ a = a_1
bad.pack_unpack_0_0 : ∀ (x_packed : _nest_1_1.list.bad), bad.pack_0_0 (bad.unpack_0_0 x_packed) = x_packed
bad.primitive.pack : list bad → _nest_1_1.list.bad
bad.primitive.pack.inj : ∀ (a a_1 : list bad), bad.primitive.pack a = bad.primitive.pack a_1 ↔ a = a_1
bad.primitive.pack.list.cons.spec : ∀ (hd : bad) (tl : list bad), bad.primitive.pack (hd :: tl) = _nest_1_1.list.bad.cons hd (bad.primitive.pack tl)
bad.primitive.pack.list.nil.spec : bad.primitive.pack list.nil = _nest_1_1.list.bad.nil
bad.primitive.pack_unpack : ∀ (x_packed : _nest_1_1.list.bad), bad.primitive.pack (bad.primitive.unpack x_packed) = x_packed
bad.primitive.sizeof_pack : ∀ (x_unpacked : list bad), _nest_1_1.list.bad.sizeof (bad.primitive.pack x_unpacked) = sizeof x_unpacked
bad.primitive.unpack : _nest_1_1.list.bad → list bad
bad.primitive.unpack._nest_1_1.list.bad.cons.spec : ∀ (hd : bad) (tl : _nest_1_1.list.bad),
  bad.primitive.unpack (_nest_1_1.list.bad.cons hd tl) = hd :: bad.primitive.unpack tl
bad.primitive.unpack._nest_1_1.list.bad.nil.spec : bad.primitive.unpack _nest_1_1.list.bad.nil = list.nil
bad.primitive.unpack_pack : ∀ (x_unpacked : list bad), bad.primitive.unpack (bad.primitive.pack x_unpacked) = x_unpacked
bad.rec : Π (C : bad → Sort l), (Π (a : list bad), C (bad.bad a)) → Π (x : bad), C x
bad.sizeof : bad → ℕ
bad.sizeof_pack_0_0 : ∀ (x_unpacked : list bad), _nest_1_1.list.bad.sizeof (bad.pack_0_0 x_unpacked) = sizeof x_unpacked
bad.unpack_0_0 : _nest_1_1.list.bad → list bad
bad.unpack_pack_0_0 : ∀ (x_unpacked : list bad), bad.unpack_0_0 (bad.pack_0_0 x_unpacked) = x_unpacked
-/
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 13 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135706602):
@**Mario Carneiro** what is `pack` and `unpack` and `primitive` and are there any more hidden constructors like this?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 13 2018 at 04:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135712980):
@**Chris Hughes** Actually I think Gabriel's recollection of me is incorrect, that is, I think that canonicity actually holds for closed terms of Lean's DTT with no axioms. I don't have a full proof yet (this is likely a future project), but it's not that hard to show that at least a term can't get stuck, from which the theorem follows assuming strong normalization. Basically, there is a coherent notion of "head position" for a term that determines where to look in a closed term to find a redex, and if there is no redex there then it's a stuck term.

If you look at the left-most part of an application (i.e. follow all apps up the left part), you may find:
* if you find a lambda then it is a redex or already in whnf (because the whole term is a lambda)
* if you find a definition then you can reduce it
* if you find an inductive recursor then you can try to reduce the major premise to a constructor (inductively by canonicity), and then it is a redex
* if you find an inductive constructor then it is in whnf
* if you find a universe or pi or inductive type constructor then it is in whnf
* you can't find a variable because it is in the empty context

The part where this proof breaks down if you add axioms is in, well, the case analysis. If we have another constant we have another case, and it is not the case that i.e. `propext iff.rfl` reduces to `rfl`, which can spoil the inductive recursor case later. The same happens with any of the other axioms - they can be used to inhabit inductive types without giving any hint at what they should reduce to.

> Next question, is there an example where it's not provably equal to something of the form `succ $ succ $ ... 0`

This is a more interesting question. For the first two axioms I am inclined to say "yes"; the claim for `propext` seems to be some kind of univalence conservativity statement which is at least intuitively plausible (i.e. any ground terms you prove using `propext` can be proven without it). For `quot.sound` this is again a conservativity result - quotients are unnecessary because you can use setoids instead, as in Coq.

For `choice` it's clearly false; `@classical.choice nat <0>` is a term of type `nat` which is not provably equal to any numeral.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 13 2018 at 04:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135713102):
In fact, I think conservativity of `propext` should follow from conservativity of `A ~= B -> A = B`, that is, any two types with the same cardinality are consistently equal

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 13 2018 at 04:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135713753):
@**Kenny Lau** Luckily (for me), nested and mutual inductives are compiled down to regular inductives by lean when you write them, so the kernel knows nothing of them and they don't affect any metatheoretic properties like canonicity. I'm not sure why it's a prefix instead of a suffix (@**Sebastian Ullrich** bug?), but the real inductive type is `_nest_1_1._nest_1_1.bad._mut_`, and there are a bunch more theorems in that namespace:
```lean
#print prefix _nest_1_1
/-
_nest_1_1._nest_1_1.bad._mut_ : psum unit unit → Type
_nest_1_1._nest_1_1.bad._mut_.bad_0 : _nest_1_1._nest_1_1.bad._mut_ ((λ (idx : unit), psum.inr idx) ()) →
_nest_1_1._nest_1_1.bad._mut_ ((λ (idx : unit), psum.inl idx) ())
_nest_1_1._nest_1_1.bad._mut_.cons_1 : _nest_1_1._nest_1_1.bad._mut_ ((λ (idx : unit), psum.inl idx) ()) →
  _nest_1_1._nest_1_1.bad._mut_ ((λ (idx : unit), psum.inr idx) ()) →
  _nest_1_1._nest_1_1.bad._mut_ ((λ (idx : unit), psum.inr idx) ())
_nest_1_1._nest_1_1.bad._mut_.nil_1 : _nest_1_1._nest_1_1.bad._mut_ ((λ (idx : unit), psum.inr idx) ())
_nest_1_1._nest_1_1.bad._mut_.rec : Π {C : Π (a : psum unit unit), _nest_1_1._nest_1_1.bad._mut_ a → Sort l},
  (Π (a : _nest_1_1._nest_1_1.bad._mut_ ((λ (idx : unit), psum.inr idx) ())),
     C ((λ (idx : unit), psum.inr idx) ()) a →
     C ((λ (idx : unit), psum.inl idx) ()) (_nest_1_1._nest_1_1.bad._mut_.bad_0 a)) →
  C ((λ (idx : unit), psum.inr idx) ()) _nest_1_1._nest_1_1.bad._mut_.nil_1 →
  (Π (hd : _nest_1_1._nest_1_1.bad._mut_ ((λ (idx : unit), psum.inl idx) ()))
   (tl : _nest_1_1._nest_1_1.bad._mut_ ((λ (idx : unit), psum.inr idx) ())),
     C ((λ (idx : unit), psum.inl idx) ()) hd →
     C ((λ (idx : unit), psum.inr idx) ()) tl →
     C ((λ (idx : unit), psum.inr idx) ()) (_nest_1_1._nest_1_1.bad._mut_.cons_1 hd tl)) →
  Π {a : psum unit unit} (n : _nest_1_1._nest_1_1.bad._mut_ a), C a n
_nest_1_1.bad : Type
_nest_1_1.bad.bad : _nest_1_1.list.bad → _nest_1_1.bad
_nest_1_1.bad.rec : Π (C : _nest_1_1.bad → Sort l),
  (Π (a : _nest_1_1.list.bad), C (_nest_1_1.bad.bad a)) → Π (x : _nest_1_1.bad), C x
_nest_1_1.list.bad : Type
_nest_1_1.list.bad.cons : _nest_1_1.bad → _nest_1_1.list.bad → _nest_1_1.list.bad
_nest_1_1.list.bad.nil : _nest_1_1.list.bad
_nest_1_1.list.bad.rec : Π (C : _nest_1_1.list.bad → Sort l),
  C _nest_1_1.list.bad.nil →
  (Π (hd : _nest_1_1.bad) (tl : _nest_1_1.list.bad), C tl → C (_nest_1_1.list.bad.cons hd tl)) →
  Π (x : _nest_1_1.list.bad), C x
...
-/
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 13 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135713821):
When Lean 4 comes around, though, I will have to add another chapter on this mess because nested inductives are coming to a kernel near you

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 13 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135720885):
```quote
but the real inductive type is `_nest_1_1._nest_1_1.bad._mut_`, and there are a bunch more theorems in that namespace:
```
o_O so many consequences of one definition! I had no idea that these ones were there.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 13 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135721078):
that's not even all of them, I removed the usual theorems about `cases_on` and `rec_on` and `brec_on` and `ibelow` and `no_confusion` and `has_sizeof`. . .

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 13 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135721090):
nested inductive translation seems kind of overcomplicated

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 13 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135722421):
```lean
inductive bad : Type
| bad : list bad → bad

def bad.to_list : bad → list bad
| (bad.bad L) := L

example (L : list bad ): bad.to_list (bad.bad L) = L := rfl
/-
type mismatch, term
  rfl
has type
  ?m_2 = ?m_2
but is expected to have type
  bad.to_list (bad.bad L) = L
-/
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 13 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135722527):
I don't think I need to say it since you've already found out: equation compiler on nested inductives doesn't produce defeq equation lemmas

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 13 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135722530):
this is one of the reasons equation lemmas are a thing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 13 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135722531):
what does canonicity mean?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 13 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135722577):
the exact statement is a bit tricky, but basically every closed term reduces to a normal form which can be described explicitly by the type

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 13 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135722580):
i.e. for nat this means `succ $ ... $ 0`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 13 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135722584):
but this error I found, it doesn't affect canonicity?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 13 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135722596):
no because nothing there is an axiomatic constant

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 13 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135722603):
it's all a layer over the real inductive type

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 13 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135722605):
That theorem has to be proven by cases or induction or something internally so it's not defeq

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 13 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135722841):
(warning: amateur alert). So this is exactly the situation where you can't prove your example by `rfl` (even though to naive eyes it looks like it should be `rfl`) so you prove it by hand (possibly using some weird theorems with weird names with `_` at the beginning), give it a good name, mark it as a simp lemma, and move on.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 13 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135722854):
yes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 13 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135722855):
except in this case lean did it all for you and slapped a nice API over the whole thing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 13 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135722865):
In this case you can write `by rw bad.to_list` and it will use the equation lemmas for `bad.to_list`, which in this case are actually nontrivial theorems

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Oct 13 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135722965):
```lean
inductive bad : Type
| bad : list bad → bad

def bad.to_list : bad → list bad
| (bad.bad L) := L

theorem bad.very_bad (L : list bad ): bad.to_list (bad.bad L) = L :=
by rw bad.to_list

#print bad.very_bad
/-
theorem bad.very_bad : ∀ (L : list bad), bad.to_list (bad.bad L) = L :=
λ (L : list bad),
  eq.mpr (id (eq.rec (eq.refl (bad.to_list (bad.bad L) = L)) (bad.to_list.equations._eqn_1 L))) (eq.refl L)
-/
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 13 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135723063):
this is just a funny way of writing `bad.to_list.equations._eqn_1 L` of course

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Oct 13 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/propext%2C%20quot.sound%20and%20eq.rec/near/135725329):
@**Mario Carneiro** Thanks for the explanation, I'm looking forward to the canonicity result.  Tiny nitpick:
```quote
 it is not the case that i.e. `propext iff.rfl` reduces to `rfl`, which can spoil the inductive recursor case later. 
```
In this particular case it actually works out since `propext iff.rfl` has type `a = a` for some `a`, and then `eq.rec` reduces by axiom K.


{% endraw %}
