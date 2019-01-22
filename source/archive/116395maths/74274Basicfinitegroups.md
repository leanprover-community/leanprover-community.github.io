---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/74274Basicfinitegroups.html
---

## [maths](index.html)
### [Basic finite groups](74274Basicfinitegroups.html)

#### [Kenny Lau (Jul 27 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130387854):
Do we have the symmetry group of order n!?

#### [Mario Carneiro (Jul 27 2018 at 07:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130389188):
There is `perm (fin n)`, and you should be able to prove it is finite with the right cardinality using `list.length_permutations`

#### [Kenny Lau (Jul 27 2018 at 07:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130389202):
`equiv.perm (fin n)`

#### [Kenny Lau (Jul 27 2018 at 07:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130389504):
Do we have C_2 and in general C_n?

#### [Kenny Lau (Jul 27 2018 at 07:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130389505):
i.e. the cyclic group of order 2 and n

#### [Kenny Lau (Jul 27 2018 at 07:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130389653):
hmm, Lean doesn't know that `equiv.perm` and `list.perm` are the same thing, so it might be hard to use `list.length_permutations`...

#### [Mario Carneiro (Jul 27 2018 at 07:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130389875):
hm, I'll put that on the todo list

#### [Johan Commelin (Jul 27 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130393507):
We have $$\mathbb{Z}/n\mathbb{Z}$$, right?

#### [Kenny Lau (Jul 27 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130393508):
oh right that's in the not-mathlib

#### [Kenny Lau (Jul 27 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130393522):
I don't think they proved that it is a group

#### [Johan Commelin (Jul 27 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130393533):
Aaah, I didn't keep track of what exactly ended up in mathlib.

#### [Kenny Lau (Jul 27 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130393536):
by "not-mathlib" I mean the initial library

#### [Johan Commelin (Jul 27 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130393537):
I assumed it was a ring by now.

#### [Kenny Lau (Jul 27 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130393583):
no, there's no algebraic structure of `fin n` proven

#### [Johan Commelin (Jul 27 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130393593):
But Chris did a lot of stuff mod `n`, right?

#### [Kenny Lau (Jul 27 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130393594):
ah

#### [Johan Commelin (Jul 27 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130393597):
Anyway, got to run... some talk on K-theory and motives is calling me.

#### [Kevin Buzzard (Jul 27 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130395310):
@**Johan Commelin** The problem with fin n (the subtype of N) is that addition and subtraction are defined in core Lean in...umm...not really the way that a mathematician would expect. Chris Hughes did a bunch of stuff mod n yes, but not with fin n.

#### [Kenny Lau (Jul 27 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130395382):
@**Kevin Buzzard** I don't really understand the problem with `fin n` though

#### [Kevin Buzzard (Jul 27 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130395464):
```lean
definition two : fin 4 := 2
definition three : fin 4 := 3
#reduce (two-three).val -- 0
#reduce (two+three).val -- 1
```

Addition rolls over, subtraction stops at 0. It's in core so can never be fixed. But of course one couls just define Zmodn n to be fin n and start again.

#### [Kenny Lau (Jul 27 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130395470):
oh, the definition in core is wrong

#### [Kevin Buzzard (Jul 27 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130395471):
right

#### [Kenny Lau (Jul 27 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130400454):
```lean
import data.fintype data.equiv.basic

namespace list

@[simp] lemma length_attach {α} (L : list α) :
  L.attach.length = L.length :=
length_pmap

@[simp] lemma nth_le_attach {α} (L : list α) (i) (H : i < L.attach.length) :
  (L.attach.nth_le i H).1 = L.nth_le i (length_attach L ▸ H) :=
calc  (L.attach.nth_le i H).1
    = (L.attach.map subtype.val).nth_le i (by simpa using H) : by rw nth_le_map'
... = L.nth_le i _ : by congr; apply attach_map_val

@[simp] lemma nth_le_range {n} (i) (H : i < (range n).length) :
  nth_le (range n) i H = i :=
option.some.inj $ by rw [← nth_le_nth _, nth_range (by simpa using H)]

attribute [simp] length_of_fn
attribute [simp] nth_le_of_fn

-- Congratulations, I proved that two things which have
-- equally few lemmas are equal.
theorem of_fn_eq_pmap {α n} {f : fin n → α} :
  of_fn f = pmap (λ i hi, f ⟨i, hi⟩) (range n) (λ _, mem_range.1) :=
by rw [pmap_eq_map_attach]; from ext_le (by simp)
  (λ i hi1 hi2, by simp at hi1; simp [nth_le_of_fn f ⟨i, hi1⟩])

theorem nodup_of_fn {α n} {f : fin n → α} (hf : function.injective f) :
  nodup (of_fn f) :=
by rw of_fn_eq_pmap; from nodup_pmap
  (λ _ _ _ _ H, fin.veq_of_eq $ hf H) (nodup_range n)

end list



variable (n : ℕ)

def Sym : Type :=
equiv.perm (fin n)

instance : has_coe_to_fun (Sym n) :=
equiv.has_coe_to_fun

@[extensionality] theorem Sym.ext (σ τ : Sym n)
  (H : ∀ i, σ i = τ i) : σ = τ :=
equiv.ext _ _ H

instance : group (Sym n) :=
equiv.perm_group

section perm

variable {n}

def Sym.to_list (σ : Sym n) : list (fin n) :=
list.of_fn σ

theorem Sym.to_list_perm (σ : Sym n) :
  σ.to_list ~ list.of_fn (1 : Sym n) :=
(list.perm_ext
  (list.nodup_of_fn $ σ.bijective.1)
  (list.nodup_of_fn $ (1 : Sym n).bijective.1)).2 $ λ f,
by rw [list.of_fn_eq_pmap, list.of_fn_eq_pmap, list.mem_pmap, list.mem_pmap]; from
⟨λ _, ⟨f.1, by simp [f.2], fin.eq_of_veq rfl⟩,
λ _, ⟨(σ⁻¹ f).1, by simp [(σ⁻¹ f).2], by convert equiv.apply_inverse_apply σ f;
  from congr_arg _ (fin.eq_of_veq rfl)⟩⟩

def list.to_sym (L : list (fin n))
  (HL : L ~ list.of_fn (1 : Sym n)) : Sym n :=
{ to_fun := λ f, list.nth_le L f.1 $
    by rw [list.perm_length HL, list.length_of_fn]; from f.2,
  inv_fun := λ f, ⟨list.index_of f L,
    begin
      convert list.index_of_lt_length.2 _,
      { rw [list.perm_length HL, list.length_of_fn] },
      { rw [list.mem_of_perm HL, list.mem_iff_nth_le],
        refine ⟨f.1, _, _⟩,
        { rw list.length_of_fn,
          exact f.2 },
        { apply list.nth_le_of_fn } }
    end⟩,
  left_inv := λ f, fin.eq_of_veq $ list.nth_le_index_of
    ((list.perm_nodup HL).2 $ list.nodup_of_fn $ λ _ _, id) _ _,
  right_inv := λ f, list.index_of_nth_le $ list.index_of_lt_length.2 $
    (list.mem_of_perm HL).2 $ list.mem_iff_nth_le.2 $
    ⟨f.1, by rw list.length_of_fn; from f.2,
      list.nth_le_of_fn _ _⟩ }

@[simp] lemma list.to_sym_apply (L : list (fin n))
  (HL : L ~ list.of_fn (1 : Sym n)) (i) :
  (L.to_sym HL) i = L.nth_le i.1 (by simp [list.perm_length HL, i.2]) :=
rfl

@[simp] lemma Sym.to_list_to_sym (σ : Sym n) :
  σ.to_list.to_sym σ.to_list_perm = σ :=
Sym.ext _ _ _ $ λ i, fin.eq_of_veq $ by simp [Sym.to_list]

end perm

instance : decidable_eq (Sym n) :=
@function.injective.decidable_eq _ _ Sym.to_list _ $ λ σ τ h,
Sym.ext n _ _ $ λ i,
have H1 : σ.to_list.nth_le i.1 _ = _,
  from list.nth_le_of_fn _ _,
have H2 : τ.to_list.nth_le i.1 _ = _,
  from list.nth_le_of_fn _ _,
by rw [← H1, ← H2]; congr; exact h

instance : fintype (Sym n) :=
fintype.of_list (list.pmap
  (λ L HL, list.to_sym L HL)
  (list.permutations (list.of_fn (1 : Sym n)))
  (λ _, (list.mem_permutations _ _).1)) $ λ σ,
list.mem_pmap.2 ⟨σ.to_list,
  (list.mem_permutations _ _).2 σ.to_list_perm,
  by simp⟩

/-
theorem Sym.card : fintype.card (Sym n) = nat.fact n :=
calc  fintype.card (Sym n)
    = _ : _
... = (list.of_fn ((1 : Sym n) : fin n → fin n)).permutations.length : list.to_finset_card_of_nodup sorry
... = nat.fact (list.of_fn ((1 : Sym n) : fin n → fin n)).length : list.length_permutations _
... = nat.fact n : by simp
-/
```

#### [Kenny Lau (Jul 27 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130400457):
@**Mario Carneiro** I think this all can go to mathlib

#### [Kenny Lau (Jul 27 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130401051):
```lean
theorem Cayley (α : Type*) [group α] [fintype α] :
  ∃ f : α → Sym (fintype.card α), function.injective f ∧ is_group_hom f :=
nonempty.rec_on (fintype.card_eq.1 $ fintype.card_fin $ fintype.card α) $ λ φ,
⟨λ x, ⟨λ i, φ.symm (x * φ i), λ i, φ.symm (x⁻¹ * φ i),
  λ i, by simp, λ i, by simp⟩,
λ x y H, have H1 : _ := congr_fun (equiv.mk.inj H).1 (φ.symm 1), by simpa using H1,
⟨λ x y, Sym.ext _ _ _ $ λ i, by simp [mul_assoc]⟩⟩
```

#### [Kenny Lau (Jul 27 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130401056):
Cayley's theorem :P

#### [Kenny Lau (Jul 27 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130401160):
TODO: prove that your list of permutations has no duplicates

#### [Kevin Buzzard (Jul 27 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130401457):
I think @**Chris Hughes** and @**Morenikeji Neri** were thinking about this sort of thing last week (they were interested in proving that the size of S_n was n!). Chris also defined the signature of a permutation --  it was interesting to think of a workable definition. Eventually we settled on $$sgn(\sigma)=(-1)^{N(\sigma)}$$ where $$N(\sigma)$$ is the number of pairs $$(i,j)$$ with $$i<j$$ and $$\sigma(i)>\sigma(j)$$.

#### [Kenny Lau (Jul 27 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130401462):
did they prove that it is a homomorphism?

#### [Johan Commelin (Jul 27 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130401479):
```quote
@**Johan Commelin** The problem with fin n (the subtype of N) is that addition and subtraction are defined in core Lean in...umm...not really the way that a mathematician would expect. Chris Hughes did a bunch of stuff mod n yes, but not with fin n.
```
Right, but no-one said that C_n needed to have `fin n` as carrier type. I don't know what Chris used as carrier type, but I suppose one could use that. Or, like you suggest, just define C_n to be `fin n`, use that the definition is not reducible, and put new algebraic structures on it that behave properly.

#### [Kevin Buzzard (Jul 27 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130401652):
```quote
did they prove that it is a homomorphism?
```
You need both that, and the fact that the signature of a transposition is -1. Neither are too hard ("in maths") and I would imagine that Chris could manage them in Lean, but I don't know if he did it.

#### [Chris Hughes (Jul 27 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130402534):
I
```quote
```quote
did they prove that it is a homomorphism?
```
You need both that, and the fact that the signature of a transposition is -1. Neither are too hard ("in maths") and I would imagine that Chris could manage them in Lean, but I don't know if he did it.
```
I'm working on it now. After that I plan to find the product of disjoint cycles representation computably.

#### [Kevin Buzzard (Jul 27 2018 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130402699):
I know that this disjoint cycles result is presented to the first years as one of the highlights of the group theory course, but is it actually useful? I think the only reason they do this is that they have to do something group-ish and for some unknown reason they do not define homomorphisms of groups until the 2nd year at Imperial! All this will change with the new syllabus. This disjoint cycle stuff feels to me to be very much a product of a bygone era, when the classification was an active area of research (I suspect the course was written by one of the old school finite group theorists that used to work here).

#### [Kevin Buzzard (Jul 27 2018 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130402702):
OTOH maybe the philosophy is "do everything"

#### [Chris Hughes (Jul 27 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130415994):
Maybe I won't do that then. I thought it would be cool to do a `has_repr`, for `perm` with disjoint cycle notation. I've proved sign is a hom, but not surjectivity yet.

#### [Kevin Buzzard (Jul 27 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130419142):
```quote
 I thought it would be cool to do a `has_repr`, for `perm` with disjoint cycle notation.
```
That is a good point! The other possibility for `has_repr` is just listing `(sigma(1),sigma(2),...,sigma(n))`but that is (a) unnecessarily big and (b) hard to interpret, so I'm not sure it's of much use. Go with disjoint cycles if you can face it -- making stuff look nice is important!

#### [Kenny Lau (Jul 28 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130462095):
https://github.com/kckennylau/Lean/blob/master/Sym.lean

#### [Kenny Lau (Jul 28 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130462099):
```lean
def Sym.equiv : Sym n ≃ fin n.fact :=
nat.rec_on n Sym.equiv_0 $ λ n ih,
calc  Sym (n+1)
    ≃ (fin (n+1) × fin n.fact) : Sym.equiv_succ ih
... ≃ fin (n+1).fact : fin_prod

instance : decidable_eq (Sym n) :=
equiv.decidable_eq_of_equiv Sym.equiv

instance : fintype (Sym n) :=
fintype.of_equiv _ Sym.equiv.symm

theorem Sym.card : fintype.card (Sym n) = nat.fact n :=
(fintype.of_equiv_card Sym.equiv.symm).trans $
fintype.card_fin _
```

#### [Kenny Lau (Jul 28 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130462918):
@**Mario Carneiro** into which files should the content of my file go?

#### [Kevin Buzzard (Jul 28 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130463370):
Mathematicians do a huge amount of work under various finiteness hypotheses. It's very easy to write down the definition of a vector space in Lean, but nobody ever proves theorems about vector spaces other than the most trivial things. The vector spaces that people care about have extra structure on, for example they're finite-dimensional, or they're separable Hilbert spares or whatever -- some extra finiteness assumptions. As a simple example, my students seem to need "order of the element divides the order of the group" a lot at the minute, and this is a theorem about finite groups. As a more complex example, a commutative ring is *Noetherian* if all its ideals are finitely-generated. I have a several-hundred-page-long book about etale cohomology which on page 1, when explaining assumptions and notation, says "all rings are assumed Noetherian". [and they're also all commutative]. 

This makes me wonder whether "finite group" should be promoted in the heierarchy, to be a class of its own, extending `group`, and that theorems about finite groups like "order of the element divides order of the group" and "Sym n is a finite group" could go in there.

#### [Chris Hughes (Jul 28 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130464126):
What's the advantage of `[finite_group G]` over `[fintype G]` and `[group G]`? Bundling classes only really makes sense when there are fields that depend on both  structures, like `left_distrib` depending on both `monoid` and `add_monoid`

#### [Kevin Buzzard (Jul 28 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130464301):
Well I guess that's what I wanted to discuss. Could one not also ask what the advantage of `[group G]` was over `[monoid G]` and `[has_inv G]` and `[has_mul_left_inv G]` or some such question?

#### [Kevin Buzzard (Jul 28 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130464392):
We decide that `group` is important somehow, important enough to have its own typeclass. I am suggesting that finite-dimensional vector spaces, finite groups and Noetherian rings are also important enough to have their own typeclasses because these are the things that people study in practice. A group is a basic foundational concept in mathematics but there are only a few theorems that you can prove about all groups without any hypotheses because a general group is extremely general.

#### [Kevin Buzzard (Jul 28 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130464489):
I see. You are arguing that `finite_group G` should be interpreted as "group for which the underlying type is finite" because in some sense these are completely unrelated concepts. But a *theorem* like "order of the element divides the order of the group" depends on both structures. This is not a field though, it's a theorem. So is that the design principle? If you have 100 theorems about finite groups then that's not enough -- the user is expected to say "a group, for which the underlying set is finite" 100 times?

And of course there are 100 theorems about finite groups -- Sylow's theorems are just the tip of the iceberg Chris :-) The 3rd year group theory course (at least the one I took as an UG) was just 24 lectures of definitions and theorems about finite groups. Maybe that's changed now the landscape has changed, I'm not sure, but all our definitions of solvable, nilpotent etc were almost immediately implied to the finite group case, and only applied to that case.

#### [Mario Carneiro (Jul 28 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130465381):
maybe `group_theory`? It's pretty basic, but I'm not sure about the restriction to `fin n` entailed here. Anything that doesn't mention `Sym` can go in its respective files

#### [Kenny Lau (Jul 28 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130470650):
Let's say we want to define the signature/parity of the permutation. In which type should the signature/parity live?

#### [Kevin Buzzard (Jul 28 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130470896):
That's an interesting question. I am not sure anyone ever adds signatures together. I would argue that mathematically it lives in an abstract group with two elements called +1 and -1. However the CS people might want to choose a concrete implementation of this group rather than building it from scratch I guess.

#### [Kevin Buzzard (Jul 28 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130470938):
I will remark that the people defining quadratic residues / non-residues in my summer project just defined the values of the Legendre symbol to be integers.

#### [Chris Hughes (Jul 28 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130471146):
I defined it to be an integer mod 2.

#### [Chris Hughes (Jul 28 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130471196):
I imagine you probably want a group structure on the image, so you can prove it's a group_hom, and it's kernel is a subgroup etc.

#### [Kenny Lau (Jul 28 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130471198):
right

#### [Chris Hughes (Jul 28 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130471244):
Unfortunately, the add groups not being groups issue comes into play here.

#### [Chris Hughes (Jul 28 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130471291):
And it would be nice if all tactics like `finish` also worked on anything isomorphic to `Prop`

#### [Kenny Lau (Jul 28 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130471364):
then which group should i define it on?

#### [Kevin Buzzard (Jul 28 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130471481):
the subtype of Z consisting of things which square to 1?

#### [Kenny Lau (Jul 28 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130471483):
is that the best group?

#### [Kevin Buzzard (Jul 28 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130471484):
What about an abstract group of order 2 equipped with a coercion to Z?

#### [Kenny Lau (Jul 28 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130471485):
or maybe I should just create an inductive type

#### [Kevin Buzzard (Jul 28 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130471486):
right

#### [Kevin Buzzard (Jul 28 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130471496):
Maybe forget about the coercion to Z and see how long it takes people to complain.

#### [Kenny Lau (Jul 28 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130471500):
why do we need coercion to Z?

#### [Chris Hughes (Jul 28 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130471545):
It seems like the best thing is to choose a canonical group of order 2, and always use that for anything that requires a group of order 2. That group should be called either C2, or integers mod 2,

#### [Kenny Lau (Jul 28 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130471548):
but we would also need Cn

#### [Chris Hughes (Jul 28 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130471551):
Exactly.

#### [Kenny Lau (Jul 28 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130471596):
and how would we build that?

#### [Chris Hughes (Jul 28 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130471760):
But there's no point having C2 and some other group of order 2 with a different name

#### [Kevin Buzzard (Jul 28 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130472238):
```lean
inductive mu2
| plus_one : mu2
| minus_one : mu2

open mu2 

definition neg : mu2 → mu2
| plus_one := minus_one 
| minus_one := plus_one 

instance : has_one mu2 := ⟨plus_one⟩ 
instance : has_neg mu2 := ⟨neg⟩

#check (-1 : mu2)
#check (1 : mu2) 
```

#### [Kenny Lau (Jul 28 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130472246):
ok

#### [Kevin Buzzard (Jul 28 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130472247):
I think the group law for the target of the signature map is traditionally multiplication

#### [Chris Hughes (Jul 28 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130472373):
But I think it's worth breaking with that tradition for the sake of only having one group of order 2 in lean to deal with.

#### [Kenny Lau (Jul 28 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130472489):
```lean
section mu2

@[derive decidable_eq]
inductive mu2 : Type
| plus_one : mu2
| minus_one : mu2

open mu2

definition neg : mu2 → mu2
| plus_one := minus_one
| minus_one := plus_one

instance : has_one mu2 := ⟨plus_one⟩
instance : has_neg mu2 := ⟨neg⟩

instance : comm_group mu2 :=
{ mul := λ x y, mu2.rec_on x (mu2.rec_on y 1 (-1)) (mu2.rec_on y (-1) 1),
  mul_assoc := λ x y z, by cases x; cases y; cases z; refl,
  mul_one := λ x, by cases x; refl,
  one_mul := λ x, by cases x; refl,
  inv := id,
  mul_left_inv := λ x, by cases x; refl,
  mul_comm := λ x y, by cases x; cases y; refl,
  .. mu2.has_one }

instance : fintype mu2 :=
{ elems := {1, -1},
  complete := λ x, mu2.cases_on x (or.inr $ or.inl rfl) (or.inl rfl) }

theorem mu2.card : fintype.card mu2 = 2 :=
rfl

end mu2
```

#### [Kenny Lau (Jul 28 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130472494):
```lean
theorem mu2.card : fintype.card mu2 = 2 :=
rfl
```

#### [Kenny Lau (Jul 28 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130473038):
```lean
instance : decidable_linear_order (fin n) :=
{ le_refl := λ ⟨i, hi⟩, nat.le_refl i,
  le_trans := λ ⟨i, hi⟩ ⟨j, hj⟩ ⟨k, hk⟩ hij hjk, nat.le_trans hij hjk,
  le_antisymm := λ ⟨i, hi⟩ ⟨j, hj⟩ hij hji, fin.eq_of_veq $ nat.le_antisymm hij hji,
  le_total := λ ⟨i, hi⟩ ⟨j, hj⟩, or.cases_on (@nat.le_total i j) or.inl or.inr,
  decidable_le := fin.decidable_le,
  .. fin.has_le, .. }
```

#### [Johan Commelin (Jul 28 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130478700):
We want 2 cyclic groups of order n, one multiplicative, the other additive.

#### [Johan Commelin (Jul 28 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130478772):
The mu_n example by Kevin will pop up a lot in number theory.

#### [Johan Commelin (Jul 28 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130478783):
I suppose that Lean Forward is going to do quite a bit of number theory pretty soon.

#### [Johan Commelin (Jul 28 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130478789):
And then additive cyclic groups also show up everywhere (e.g. integers mod n).

#### [Johan Commelin (Jul 28 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130478861):
If R is a ring, do we already know that `units R` is a group? If R is in fact a field, then every finite subgroup of `units R` is a cyclic group. This is a cute theorem about (finite!) groups. And those cyclic groups are pretty multiplicative.

#### [Kenny Lau (Jul 28 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482261):
```lean
def Sym.is_valid (L : list (Sym n)) : Prop :=
∀ τ ∈ L, ∃ i j, i ≠ j ∧ τ = Sym.swap i j

Sym.list_swap_valid : ∀ (σ : Sym ?M_1), Sym.is_valid (Sym.list_swap σ)

Sym.list_swap_prod : ∀ (σ : Sym ?M_1), list.prod (Sym.list_swap σ) = σ
```

#### [Kenny Lau (Jul 28 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482264):
I proved constructively that every permutation can be written as the product of transpositions

#### [Kenny Lau (Jul 28 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482266):
I actually didn't know that it is possible with at most n transpositions

#### [Kenny Lau (Jul 28 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482267):
so I actually learnt (discovered) something new

#### [Kenny Lau (Jul 28 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482280):
I also learnt how to use `well_founded.fix` and `well_founded.induction`

#### [Johan Commelin (Jul 28 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482411):
You can do it with `\le (n-1)` transpositions, right?

#### [Kenny Lau (Jul 28 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482414):
yes

#### [Kenny Lau (Jul 28 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482428):
https://github.com/kckennylau/Lean/blob/master/Sym.lean

#### [Johan Commelin (Jul 28 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482430):
So now we only need disjoint cycle representation.

#### [Kenny Lau (Jul 28 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482431):
although I didn't prove the bound

#### [Kenny Lau (Jul 28 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482435):
no, we don't need DCR

#### [Kenny Lau (Jul 28 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482436):
it is way overrated

#### [Johan Commelin (Jul 28 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482441):
It is nice for printing stuff.

#### [Kenny Lau (Jul 28 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482618):
we should prove the homomorphism first

#### [Johan Commelin (Jul 28 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482714):
That shouldn't be too hard anymore, right?

#### [Kenny Lau (Jul 28 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482715):
no, that's a whole nother business

#### [Kenny Lau (Jul 28 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482716):
they involve completely different skills

#### [Johan Commelin (Jul 28 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482731):
What, the homomorphism?

#### [Kenny Lau (Jul 28 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482732):
yes

#### [Johan Commelin (Jul 28 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482737):
Hmmm, does it help if you change the definition of sgn?

#### [Johan Commelin (Jul 28 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482777):
Maybe not

#### [Kenny Lau (Jul 28 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482782):
you need to prove that if a bunch of transpositions multiply to 1, then you have an even number of transpositions

#### [Kenny Lau (Jul 28 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482784):
that involves somehow traversing the whole list

#### [Johan Commelin (Jul 28 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482797):
Fair enough

#### [Kenny Lau (Jul 28 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482858):
which I'm not exactly comfortable with doing in Lean

#### [Kevin Buzzard (Jul 28 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130482998):
```quote
you need to prove that if a bunch of transpositions multiply to 1, then you have an even number of transpositions
```
AFAIK the best way to do this is to compute with signatures via the definition Chris used -- signature of sigma is (-1) ^ (the number of pairs (i,j) with i < j and sigma(i) > sigma(j) )

#### [Kenny Lau (Jul 28 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130483008):
hmm, maybe

#### [Kevin Buzzard (Jul 28 2018 at 21:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130484672):
It's not so hard to prove that this is multiplicative. You can say that an *un*ordered pair is "switched" if their order is switched -- this is well-defined. if sigma switches a pair and tau switches them back then the composite scores 0 and each of sigma and tau scores 1.

#### [Chris Hughes (Jul 28 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130484741):
I have proved it's multiplicative, and that transpositions are odd. My proof that transpositions are conjugate was brilliant, I did `split_ifs` and then solved 84 goals at once with `cc`

#### [Patrick Massot (Jul 28 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130484843):
I have a challenge for all the permutation experts. From a permutation of `fin n` (or any version) define a map from a product of  n topological space to the permuted product and prove it's continuous. When n=2, this is `continuous_id` and `continuous_swap`. Part of the challenge is that `A × B × C` is not the type of triple `(x.1, x.2, x.3)`, it's secretely  `A × (B × C)` with elements `(x.1, (x.2.1, x.2.2))`

#### [Patrick Massot (Jul 28 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130484853):
Note that I don't need this, I only want to make sure you don't get bored

#### [Kenny Lau (Jul 28 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130484904):
can you give us the inputs? i.e. how is the n topological space represented?

#### [Johan Commelin (Jul 28 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130485013):
```quote
I have proved it's multiplicative, and that transpositions are odd. My proof that transpositions are conjugate was brilliant, I did `split_ifs` and then solved **84** goals at once with `cc`
```
Hmm, that crazy number 84 really has some special place in mathematics... (https://en.wikipedia.org/wiki/Hurwitz%27s_automorphisms_theorem)

#### [Kevin Buzzard (Jul 28 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130487017):
That's great! Somehow I'm surprised it's quite so many. You have the transposition (a b) and then you're trying to figure out whether the pair (i j) got re-aranged. So you have cases depending on whether i<a,i=a,a<i<b,i=b,i>b and the same with j. The clever thing is to get it so that the goals are solvable afterwards I guess, rather than just counting.

#### [Chris Hughes (Jul 28 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130487184):
The proof had nothing to do with sign. This was the proof
```lean
lemma transpose_conj {α : Type*} [decidable_eq α] {a b x y : α} 
  (hab : a ≠ b) (hxy : x ≠ y) :
  ∃ f : perm α, f * transpose x y * f⁻¹ = transpose a b :=
⟨if x = b then transpose y a 
else if y = a then transpose x b
else transpose x a * transpose y b, equiv.ext _ _ $ λ n, 
begin 
  unfold_coes,
  dsimp [transpose, inv_def, mul_def, equiv.symm, equiv.trans, function.comp],
  simp only [ite_apply, ite_inv_apply],
  split_ifs; cc
end⟩
```

#### [Kenny Lau (Jul 28 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130487194):
TIL `unfold_coes`

#### [Patrick Massot (Jul 28 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130487907):
```quote
can you give us the inputs? i.e. how is the n topological space represented?
```
The example that I actually needed is at https://github.com/PatrickMassot/lean-perfectoid-spaces/blob/652422a5e5dd00f07ef3dc768bc774784904cb00/src/for_mathlib/topological_structures.lean#L7-L19

#### [Kenny Lau (Jul 29 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130512068):
@**Kevin Buzzard** unfortunately this theorem is not true: `sgn.inversion (σ * τ) i j = sgn.inversion τ i j * sgn.inversion σ (τ i) (τ j)`

#### [Kenny Lau (Jul 29 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130512069):
and it makes my life defining sign using inversion hard

#### [Kenny Lau (Jul 29 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130512075):
```lean
def sgn.inversion (σ : Sym n) (i j : fin n) : mu2 :=
if i < j ∧ σ i > σ j then -1 else 1
```

#### [Kevin Buzzard (Jul 29 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130518707):
How about you define it on unordered pairs? Then it's ok

#### [Kenny Lau (Jul 29 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130518711):
how do you define unordered pairs?

#### [Chris Hughes (Jul 29 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130518804):
quotient

#### [Kenny Lau (Jul 29 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130518807):
did you use quotient?

#### [Chris Hughes (Jul 29 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130518819):
No. I used pairs such that x.2 > x.1

#### [Kenny Lau (Jul 29 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130518826):
and you still managed to prove that it is multiplicative? :o

#### [Chris Hughes (Jul 29 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130518834):
A lot of `ite` faffing

#### [Kenny Lau (Jul 29 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130518841):
it's mainly the finset prod that I'm uncomfortable with

#### [Kevin Buzzard (Jul 29 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130518916):
Also allow the possibility that i>j and sigma i < sigma j

#### [Chris Hughes (Jul 29 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130518919):
I used `sum_bij` where the `bij` was one of the perms I was multiplying, subject to some `ite` faffing to get the order right.

#### [Kenny Lau (Jul 29 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130518927):
ok

#### [Chris Hughes (Jul 29 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130518928):
```quote
Also allow the possibility that i>j and sigma i < sigma j
```
Won't you always get even if you do that?

#### [Kenny Lau (Jul 29 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130518931):
just prove that it is divisible by 2 and then divide by 2 :P

#### [Kevin Buzzard (Jul 29 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130518983):
Or just count over unordered pairs :-)

#### [Chris Hughes (Jul 29 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130534903):
Done product of transpositions as well. Not sure there was any point making the very last definition computable or not, but it might have some usage. https://github.com/dorhinj/leanstuff/blob/master/signatures.lean

#### [Kenny Lau (Jul 29 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535153):
https://github.com/kckennylau/Lean/blob/master/Sym.lean
```lean
def sgn (σ : Sym n) : mu2 :=
(-1) ^ σ.list_step.length

instance sgn.is_group_hom : is_group_hom (@sgn n) :=
begin
  constructor,
  intros σ τ,
  unfold sgn,
  rw [← pow_add, ← list.length_append],
  rw [mu2.neg_one_pow, eq_comm, mu2.neg_one_pow],
  refine congr_arg _ _,
  apply length_mod_two_eq,
  simp
end

theorem sgn_step (s : step n) :
  sgn s.eval = -1 :=
suffices s.eval.list_step.length % 2 = [s].length % 2,
  by unfold sgn; rw [mu2.neg_one_pow, this]; refl,
length_mod_two_eq _ _ $ by simp
```

#### [Kenny Lau (Jul 29 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535156):
10 minutes behind you :-)

#### [Kevin Buzzard (Jul 29 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535197):
So now you can both define determinant of an n x n matrix!

#### [Kenny Lau (Jul 29 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535205):
oh no, we could already define determinant just fine, it's the multiplicative part that needs this result

#### [Chris Hughes (Jul 29 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535210):
Is your sign defined using the list of transpositions?

#### [Kenny Lau (Jul 29 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535211):
yes

#### [Kenny Lau (Jul 29 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535212):
oh, and trust me, do not look at Lines 720 - 831

#### [Kenny Lau (Jul 29 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535252):
https://github.com/kckennylau/Lean/blob/master/Sym.lean#L720

#### [Kenny Lau (Jul 29 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535259):
```quote
Is your sign defined using the list of transpositions?
```
```lean
def sgn (σ : Sym n) : mu2 :=
(-1) ^ σ.list_step.length
```

#### [Kenny Lau (Jul 29 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535261):
and `list_step` is a computable (!) function

#### [Kenny Lau (Jul 29 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535266):
```lean
def list_step (σ : Sym n) : list (step n) :=
by refine well_founded.fix list_step.aux.wf _ σ; from
λ σ ih, if H : σ.support = ∅ then []
  else let ⟨i, hi⟩ := σ.support_choice H in
    step.mk' (σ i) i (support_def.1 hi)
    :: ih (swap (σ i) i * σ) (support_swap_mul hi)
```

#### [Kenny Lau (Jul 29 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535267):
by induction (recursion) on the support

#### [Chris Hughes (Jul 29 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535268):
What's it do?

#### [Kenny Lau (Jul 29 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535272):
it expresses a permutation as a product of transpositions

#### [Kenny Lau (Jul 29 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535324):
I just realized kernel of group hom is not in mathlib

#### [Kenny Lau (Jul 29 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535372):
(btw if anyone is reading my code, all my "choice" functions are computable :P)

#### [Kevin Buzzard (Jul 29 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535806):
I think kernel of a group hom is somewhere in mathlib...`is_group_hom.ker`?

#### [Kenny Lau (Jul 29 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535849):
ah right

#### [Kenny Lau (Jul 29 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535903):
```lean
def Alt : Type :=
is_group_hom.ker (@Sym.sgn n)

instance : group (Alt n) :=
by unfold Alt; apply_instance
```

#### [Kevin Buzzard (Jul 29 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535921):
You can now prove A_5 is simple by counting conjugacy classes.

#### [Kenny Lau (Jul 29 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535960):
hmm, not the proof of simple that i know

#### [Kenny Lau (Jul 29 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535961):
is there an easier proof?

#### [Kevin Buzzard (Jul 29 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535963):
```quote
oh no, we could already define determinant just fine, it's the multiplicative part that needs this result
```
Yes, in fact Keji did it already, by expanding along the top row. He could prove nothing about it from this definition :-)

#### [Kenny Lau (Jul 29 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130535974):
how about Chris proving that any simple group must have order at least 60 lol

#### [Kevin Buzzard (Jul 29 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130536023):
```quote
is there an easier proof?
```
You could use Sylow to prove that group of order strictly dividing 60 was solvable, and then there's some crappy trick with 3-cycles (which I used to set on the 2nd year group theory course) which shows that A_5 has no non-trivial cyclic quotients. The counting proof is pretty trivial! Any normal subgroup is a union of conjugacy classes but any non-trivial sum of conj class sizes doesn't even equal a divisor of 60.

#### [Kenny Lau (Jul 29 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130537317):
[2018-07-30.png](/user_uploads/3121/tJtctbAOJKrPMftkcpbbkPt3/2018-07-30.png)

#### [Kenny Lau (Jul 29 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130537318):
glorious

#### [Kenny Lau (Jul 29 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130537319):
```lean
theorem eq_sgn (f : Sym n → mu2) [is_group_hom f]
  (s : step n) (H1 : f s.eval = -1) (σ : Sym n) :
  f σ = sgn σ :=
begin
  have H2 : ∀ t : step n, f t.eval = -1,
  { intro t,
    by_cases H2 : s.1 = t.1,
    { by_cases H3 : s.2 = t.2,
      { rw [← step.ext _ _ H2 H3, H1] },
      have H4 : t.eval = swap s.2 t.2 * s.eval * swap s.2 t.2,
      { dsimp [step.eval, swap], ext k, dsimp,
        have := ne_of_lt s.3, have := ne_of_lt t.3,
        split_ifs; cc },
      simp [H4, is_group_hom.mul f, H1] },
    by_cases H3 : s.1 = t.2,
    { have H4 : t.eval = swap s.2 t.1 * s.eval * swap s.2 t.1,
      { dsimp [step.eval, swap], ext k, dsimp,
        have := ne_of_lt s.3, have := ne_of_lt t.3,
        split_ifs; cc },
      simp [H4, is_group_hom.mul f, H1] },
    by_cases H4 : s.2 = t.1,
    { have H5 : t.eval = swap s.1 t.2 * s.eval * swap s.1 t.2,
      { dsimp [step.eval, swap], ext k, dsimp,
        have := ne_of_lt s.3, have := ne_of_lt t.3,
        split_ifs; cc },
      simp [H5, is_group_hom.mul f, H1] },
    by_cases H5 : s.2 = t.2,
    { have H6 : t.eval = swap s.1 t.1 * s.eval * swap s.1 t.1,
      { dsimp [step.eval, swap], ext k, dsimp,
        have := ne_of_lt s.3, have := ne_of_lt t.3,
        split_ifs; cc },
      simp [H6, is_group_hom.mul f, H1] },
    have H6 : t.eval = swap s.1 t.1 * swap s.2 t.2 * s.eval * swap s.2 t.2 * swap s.1 t.1,
    { dsimp [step.eval, swap], ext k, dsimp,
      have := ne_of_lt s.3, have := ne_of_lt t.3,
      split_ifs; cc },
    rw H6,
    repeat { rw is_group_hom.mul f },
    rw [H1, mul_assoc (f (swap s.1 t.1)), mul_assoc (f (swap s.1 t.1))],
    rw [mu2.mul_neg_one, mu2.neg_mul_self], simp },
  have H3 := list_step_prod σ,
  revert H3, generalize : list_step σ = L, intro H3, subst H3,
  induction L with hd tl ih, { simp [is_group_hom.one f] },
  simp [is_group_hom.mul f, ih, H2]
end
```

#### [Kenny Lau (Jul 29 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130537320):
@**Kevin Buzzard** @**Chris Hughes**

#### [Kevin Buzzard (Jul 29 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130537326):
Ouch

#### [Kenny Lau (Jul 29 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539514):
I think I just discovered a uniform definition of a permutation that can conjugate (ab) to become (cd)

#### [Kenny Lau (Jul 29 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539519):
uniform as in doesn't rely on casing

#### [Chris Hughes (Jul 29 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539530):
How would you manage that?

#### [Kenny Lau (Jul 29 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539531):
exercise to the reader :P

#### [Kenny Lau (Jul 29 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539533):
to be fair, I did use `swap`, which relies on casing

#### [Kenny Lau (Jul 29 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539536):
`swap a b` swaps `a` and `b` regardless of whether they are distinct

#### [Chris Hughes (Jul 29 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539573):
That's easy then.

#### [Chris Hughes (Jul 29 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539578):
Probably

#### [Kenny Lau (Jul 29 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539579):
what's your answer?

#### [Kenny Lau (Jul 29 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539585):
oh btw a and b are distinct; and c and d are distinct

#### [Chris Hughes (Jul 29 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539659):
I give up

#### [Chris Hughes (Jul 29 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539660):
I can shorten a proof by a few lines if I work it out.

#### [Kenny Lau (Jul 29 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539661):
```lean
def eq_sgn_aux4 (s t : step n) : Sym n :=
swap (swap s.1 t.1 s.2) t.2 * swap s.1 t.1

theorem eq_sgn_aux3 (s t : step n) :
  eq_sgn_aux4 s t s.1 = t.1 :=
begin
  dsimp [eq_sgn_aux4, swap],
  have := ne_of_lt s.3,
  have := ne_of_lt t.3,
  simp, split_ifs; cc
end

theorem eq_sgn_aux2 (s t : step n) :
  eq_sgn_aux4 s t s.2 = t.2 :=
begin
  dsimp [eq_sgn_aux4, swap],
  simp
end
```

#### [Chris Hughes (Jul 29 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539698):
But also probably massively slow down cimpilation time

#### [Kenny Lau (Jul 29 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539702):
looks like I'm finally useful :P

#### [Kevin Buzzard (Jul 29 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539708):
(ac)(bd) conjugates (ab) into (cd). In general conjugating by g sends (abc) to (ga gb gc) and the same for products of cycles

#### [Kenny Lau (Jul 29 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539710):
your thing only works when we have more separation axioms

#### [Kenny Lau (Jul 29 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539711):
here we only know that `a != b` and `c != d`

#### [Kevin Buzzard (Jul 29 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539712):
No

#### [Kenny Lau (Jul 29 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539758):
wait what

#### [Kenny Lau (Jul 29 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539769):
ok now I'm shocked

#### [Kenny Lau (Jul 29 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539770):
I don't believe it

#### [Kenny Lau (Jul 29 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539816):
ah

#### [Kenny Lau (Jul 29 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130539942):
/me finds a hole to hide from his embarrassment

#### [Kenny Lau (Jul 29 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130540157):
in my defense, my definition is easier to work with

#### [Kenny Lau (Jul 29 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130540186):
```lean
def eq_sgn_aux4 (s t : step n) : Sym n :=
swap (swap s.1 t.1 s.2) t.2 * swap s.1 t.1

theorem eq_sgn_aux3 (s t : step n) :
  eq_sgn_aux4 s t s.1 = t.1 :=
begin
  dsimp [eq_sgn_aux4, swap],
  have := ne_of_lt s.3,
  have := ne_of_lt t.3,
  simp, split_ifs; cc
end

theorem eq_sgn_aux2 (s t : step n) :
  eq_sgn_aux4 s t s.2 = t.2 :=
begin
  dsimp [eq_sgn_aux4, swap],
  simp
end

theorem eq_sgn_aux (s t : step n) :
  eq_sgn_aux4 s t * s.eval * (eq_sgn_aux4 s t)⁻¹ = t.eval :=
begin
  ext k,
  by_cases H1 : k = t.1,
  { subst H1,
    dsimp [step.eval],
    simp [equiv.symm_apply_eq.2 (eq_sgn_aux3 s t).symm, eq_sgn_aux2] },
  by_cases H2 : k = t.2,
  { subst H2,
    dsimp [step.eval],
    simp [equiv.symm_apply_eq.2 (eq_sgn_aux2 s t).symm, eq_sgn_aux3] },
  dsimp [step.eval, swap],
  simp [H1, H2, eq_sgn_aux2, eq_sgn_aux3]
end

theorem eq_sgn (f : Sym n → mu2) [is_group_hom f]
  (s : step n) (H1 : f s.eval = -1) (σ : Sym n) :
  f σ = sgn σ :=
begin
  have H2 : ∀ t : step n, f t.eval = -1,
  { intro t,
    rw [← eq_sgn_aux s t],
    simp [is_group_hom.mul f, is_group_hom.inv f, H1] },
  have H3 := list_step_prod σ,
  revert H3, generalize : list_step σ = L, intro H3, subst H3,
  induction L with hd tl ih, { simp [is_group_hom.one f] },
  simp [is_group_hom.mul f, ih, H2]
end
```

#### [Kenny Lau (Jul 29 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130540187):
@**Chris Hughes** did it help you?

#### [Chris Hughes (Jul 29 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130540227):
If a = d then (ac)(bd)(ab)(bd)(ac) a = (ac)(ba)(ab)(ba)(ac) a = a != c = (cd) a. What's my mistake? I'm probably being an idiot.

#### [Kenny Lau (Jul 29 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130540231):
hmm...

#### [Kenny Lau (Jul 29 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130540884):
@**Chris Hughes** how did you find that counter-example?

#### [Kevin Buzzard (Jul 29 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130540885):
(cd)a=a.

#### [Kenny Lau (Jul 29 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130540886):
(cd)a = (ca)a = c

#### [Kevin Buzzard (Jul 29 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130540927):
It's certainly true that if sigma sends x to y, then g sigma g^{-1} sends gx to gy.

#### [Kenny Lau (Jul 29 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130540928):
yes, that is true

#### [Chris Hughes (Jul 29 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130540929):
```lean
example : ∃ x y a b : fin 3, x ≠ y ∧ a ≠ b ∧ 
  transpose x b * transpose y a * transpose x y * (transpose x b * transpose y a)⁻¹ ≠ 
  transpose a b := dec_trivial
```

#### [Kenny Lau (Jul 29 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130540930):
ah

#### [Kenny Lau (Jul 29 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130540933):
relying on the automation

#### [Kevin Buzzard (Jul 29 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130540940):
Oh ha ha (ac)(bd) is not the map sending a to c and b to d

#### [Kevin Buzzard (Jul 29 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130540981):
The map that conjugates (ab) into (cd) is "anything sending a to c and b to d"

#### [Kevin Buzzard (Jul 29 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130540985):
In fact the general solution is "either send a to c and b to d, or send a to d and b to c -- and do anything you like with everything else"

#### [Chris Hughes (Jul 29 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130541149):
How briefly can you write down such a function?

#### [Kenny Lau (Jul 29 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130541150):
I just did

#### [Kenny Lau (Jul 29 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130541151):
```lean
def eq_sgn_aux4 (s t : step n) : Sym n :=
swap (swap s.1 t.1 s.2) t.2 * swap s.1 t.1

theorem eq_sgn_aux3 (s t : step n) :
  eq_sgn_aux4 s t s.1 = t.1 :=
begin
  dsimp [eq_sgn_aux4, swap],
  have := ne_of_lt s.3,
  have := ne_of_lt t.3,
  simp, split_ifs; cc
end

theorem eq_sgn_aux2 (s t : step n) :
  eq_sgn_aux4 s t s.2 = t.2 :=
begin
  dsimp [eq_sgn_aux4, swap],
  simp
end

theorem eq_sgn_aux (s t : step n) :
  eq_sgn_aux4 s t * s.eval * (eq_sgn_aux4 s t)⁻¹ = t.eval :=
begin
  ext k,
  by_cases H1 : k = t.1,
  { subst H1,
    dsimp [step.eval],
    simp [equiv.symm_apply_eq.2 (eq_sgn_aux3 s t).symm, eq_sgn_aux2] },
  by_cases H2 : k = t.2,
  { subst H2,
    dsimp [step.eval],
    simp [equiv.symm_apply_eq.2 (eq_sgn_aux2 s t).symm, eq_sgn_aux3] },
  dsimp [step.eval, swap],
  simp [H1, H2, eq_sgn_aux2, eq_sgn_aux3]
end
```

#### [Chris Hughes (Jul 29 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130541190):
Why does swap have 3 arguments?

#### [Chris Hughes (Jul 29 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130541192):
I see

#### [Kenny Lau (Jul 29 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130541193):
it only has 2, then it is coerced to become a function

#### [Kenny Lau (Jul 29 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130541360):
I finally proved that my `step` is a fintype

#### [Kenny Lau (Jul 29 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130541361):
```lean
example : ∃ s t : step 3,
  swap s.1 t.1 * swap s.2 t.2 * s.eval * swap s.2 t.2 * swap s.1 t.1
  ≠ t.eval :=
dec_trivial
```

#### [Chris Hughes (Jul 29 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130541420):
What is step?

#### [Kenny Lau (Jul 29 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130541422):
```lean
@[derive decidable_eq]
structure step : Type :=
(fst : fin n)
(snd : fin n)
(lt  : fst < snd)
```

#### [Kenny Lau (Jul 29 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130541462):
it represents a transposition

#### [Kenny Lau (Jul 29 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130541465):
https://github.com/kckennylau/Lean/blob/master/Sym.lean

#### [Chris Hughes (Jul 29 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130541473):
I used something similar 
```lean
def fin_pairs_lt (n : ℕ) : finset (Σ a : fin n, fin n) :=
(univ : finset (fin n)).sigma (λ a, (range a.1).attach_fin
  (λ m hm, lt_trans (mem_range.1 hm) a.2))
```

#### [Kevin Buzzard (Jul 29 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130541533):
The fact that if sigma sends x to y then g sigma g^{-1} sends gx to gy is a special case of "transport de structure". It's more easily seen if you generalise. If sigma is a permutation of a set X, and if g is a bijection between X and another set Y, then g identifies X and Y, so sigma transports over to a permutation of Y. The explicit formula for the permutation of Y is g sigma g^{-1}. If you think of g as a dictionary identifying X and Y, then a in X gets identified with ga in Y, and b in X gets identified with gb in Y. If sigma sends a to b, then the transported sigma sends ga to gb. The counterintuitive idea now is to imagine that X = Y and that g is not the identity map but perhaps some other bijection. If you think about things this way then the fact that e.g. conjugate permutations have the same cycle type becomes trivial.

#### [Chris Hughes (Jul 30 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130542126):
I had to think about it like that when I defined `sign` on an arbitrary `fintype`, and not just `fin`. I used `equiv_fin` to define the `sign`, but I had to prove that `sign` did not depend on which `equiv_fin` I chose, which i used the conjugation property for by combining my two different `equiv_fins` together to make a `perm` and conjugating by that `perm`

#### [Kenny Lau (Jul 30 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130562395):
```lean
theorem inversions_eq_sgn : ∀ σ : Sym n, inversions σ = sgn σ :=
nat.cases_on n dec_trivial $ λ n,
nat.cases_on n dec_trivial $ λ n σ,
eq_sgn inversions (step01 n) inversions_step01 σ
```

#### [Kevin Buzzard (Jul 30 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130562545):
```quote
```lean
example : ∃ x y a b : fin 3, x ≠ y ∧ a ≠ b ∧ 
  transpose x b * transpose y a * transpose x y * (transpose x b * transpose y a)⁻¹ ≠ 
  transpose a b := dec_trivial
```
```
Did this work out of the box? I was going to use it in my talk today! But

```lean
theorem A : ∃ a b : fin 3, a = b := dec_trivial 
```

doesn't work for me. Do I need an import?

#### [Kenny Lau (Jul 30 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130562550):
maybe import fintype

#### [Kenny Lau (Jul 30 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130562722):
this is interesting. `fintype.decidable_exists_fintype` isn't in the online Lean

#### [Kenny Lau (Jul 30 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130562763):
it was added [18 days ago](https://github.com/leanprover/mathlib/commit/21b918b3083ce42c495ab48b7ea19e486e3eae6b#diff-de2c770e28fdceb296e807697c00ad8a)

#### [Kevin Buzzard (Jul 30 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130562986):
Oh I think that might have been because of some other problem I had, which Chris fixed. Oh I remember -- it was for Ellen's dots and boxes project. She wanted to write basic definitions like "if the number of times this multiset contains 3 is at most 1, and if ..., then blah" and Lean was demanding decidability proofs. I asked why and Chris and Simon just fixed everything up so it worked.

#### [Kenny Lau (Jul 30 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130562995):
'tis a small world

#### [Kevin Buzzard (Jul 30 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130563038):
rofl I had a scratch file open with the "not working" theorem A, and I just imported analysis.topology.continuity to think about Patrick's comment about continuous being a class and it fixed my proof :-)

#### [Kenny Lau (Jul 30 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Basic%20finite%20groups/near/130563041):
lol

