---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/26591palindromes.html
---

## Stream: [general](index.html)
### Topic: [palindromes](26591palindromes.html)

---


{% raw %}
#### [ Kevin Buzzard (Apr 03 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124591860):
For recreational reasons I was interested in working with lists which were palindromes, i.e. lists `G` satisfying `G = list.reverse G`. I wanted to prove a bunch of stuff about these things but I couldn't prove anything by induction because lists don't decompose like that. I wanted to write a general `G` of length 2 or more as `G=[head G] ++ middle G ++ [head G]` and have a recursor of the form `C [] -> C [x] -> forall palindromes H, C H -> C ([a] ++ H ++ [a]) -> forall palindromes G, C G`

#### [ Kevin Buzzard (Apr 03 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124591884):
What is the idiomatic way to do this in Lean? I am at the stage now where I could probably get several methods to go through

#### [ Kevin Buzzard (Apr 03 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124591886):
but I would like to choose the one with the least pain.

#### [ Kevin Buzzard (Apr 03 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124591890):
Should I actually make a new inductive type?

#### [ Mario Carneiro (Apr 03 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124593010):
You should look at `list.reverse_rec_on` for a similar eliminator. You could encode it as an inductive predicate, and then prove that it is equivalent to `g = list.reverse g`, or you could prove the eliminator you wrote with `palindromes` defined using reverse

#### [ Chris Hughes (Apr 03 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124593011):
I stopped as soon as it got hard
```lean
inductive  palindrome : list α →  Prop
| nil : palindrome []
| singleton : ∀ a, palindrome [a]
| cons : ∀ (a) (l), palindrome l → palindrome ([a] ++ l ++ [a])

lemma  palindrome_iff_eq_reverse {l : list α} : palindrome l ↔ l = list.reverse l :=
⟨λ h, palindrome.rec_on h rfl (λ a, rfl) (λ a l h₁ h₂,
begin
conv {to_lhs, rw h₂},
rw ← list.reverse_singleton a,
simp,
end), list.rec_on l (λ h, palindrome.nil)
(λ a l h, begin apply list.reverse_rec_on l, end)⟩
```

#### [ Mario Carneiro (Apr 03 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124593343):
In the cons case you have `a::l = list.reverse (a::l) = l.reverse ++ [a]`. By cases on `l.reverse`, if `l.reverse = []` then `a::l = [a]` is a palindrome, and if `l.reverse = b::l'` then `a::l = b::l'++[a]` so `a = b` and `l = l' ++ [a]`, so `a :: l'.reverse = l.reverse = a::l'` and hence `l' = l'.reverse`, so `l'` is a palindrome by IH and hence `a::l` is a palindrome

#### [ Chris Hughes (Apr 03 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124594253):
Is there a lemma saying `a :: l = b :: m -> a = b`?

#### [ Kevin Buzzard (Apr 03 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124594260):
no_confusion

#### [ Kevin Buzzard (Apr 03 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124594271):
or cons_inj or whatever

#### [ Chris Hughes (Apr 03 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124594377):
cons_inj tells me about the lists being equal.

#### [ Sebastian Ullrich (Apr 03 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124594398):
or the `injection` tactic

#### [ Chris Hughes (Apr 03 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124594462):
Thanks @**Sebastian Ullrich** I'd never used injection successfully before.

#### [ Kevin Buzzard (Apr 03 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124595081):
`example {β : Type*} (a b : β) (l m : list β) : a :: l = b :: m -> a = b :=  λ H, (list.cons.inj H).1`

#### [ Kevin Buzzard (Apr 03 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124595142):
I feel confident with this sort of stuff now I've seen how it all works.

#### [ Kevin Buzzard (Apr 03 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124595241):
`example {β : Type*} (a b : β) (l m : list β) : a :: l = b :: m -> a = b := λ H, @list.no_confusion _ _ (a::l) (b::m) H (λ x y,x)`

#### [ Kevin Buzzard (Apr 03 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124595265):
Chris, it was your questioning a week last Thurs which pushed me to learn this stuff. We didn't quite go as far as we should have done. We looked at no_confusion for bool and nat, but if you look at it for list you see how all the terms involved in the constructors are used.

#### [ Kevin Buzzard (Apr 03 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124595342):
``` 
variables {a b : β} {L M : list β} {P : Type}
#reduce list.no_confusion_type P (a::L) (b::M) -- (a = b → L = M → P) → P
```

#### [ Kevin Buzzard (Apr 03 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124595391):
You use no_confusion to make an instance of that type.

#### [ Kevin Buzzard (Apr 03 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124595732):
```quote
In the cons case you have `a::l = list.reverse (a::l) = l.reverse ++ [a]`. By cases on `l.reverse`, if `l.reverse = []` then `a::l = [a]` is a palindrome, and if `l.reverse = b::l'` then `a::l = b::l'++[a]` so `a = b` and `l = l' ++ [a]`, so `a :: l'.reverse = l.reverse = a::l'` and hence `l' = l'.reverse`, so `l'` is a palindrome by IH and hence `a::l` is a palindrome
```
For me, I can prove l' = l'.reverse but the inductive hypothesis doesn't let me conclude l' is a palindrome, the inductive hypothesis the way I've set it up says at this point that if (a::l') is its own reverse then (a::l') is a palindrome.

#### [ Kevin Buzzard (Apr 03 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124595764):
Somehow this is exactly the issue I keep running into: list has the wrong recursor for me.

#### [ Kevin Buzzard (Apr 03 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124595820):
I can see that because I have `list.rec_on` and `list.reverse_rec_on` I should have all I need, but I don't know what `C` should be in some sense (what is `C` called? The motive?)

#### [ Chris Hughes (Apr 04 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124596524):
I've been struggling with this too. I think the best would be some sort of strong induction on the list.

#### [ Mario Carneiro (Apr 04 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124597147):
You should do strong induction on the length of the list

#### [ Kenny Lau (Apr 04 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124597485):
@**Kevin Buzzard** you could use a custom recursor

#### [ Kenny Lau (Apr 04 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124597486):
see https://github.com/kckennylau/Lean/blob/master/recursion.lean

#### [ Kenny Lau (Apr 04 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124597487):
for an example

#### [ Ching-Tsun Chou (Apr 04 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124599343):
The trick to prove the lemma Chris wants to prove is to consider the two cases (a) length l = 2*n and (b) length l = 2*n + 1 separately and then use induction on n in each case.

#### [ Kenny Lau (Apr 04 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124599350):
omg someone from hong kong

#### [ Chris Hughes (Apr 04 2018 at 21:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124638255):
Finally did it. 
```lean
inductive palindrome : list α → Prop
| nil       : palindrome []
| singleton : ∀ a, palindrome [a]
| cons      : ∀ (a) (l), palindrome l → palindrome ([a] ++ l ++ [a])

lemma eq_reverse_of_palindrome {l : list α} : palindrome l → l = list.reverse l :=
λ h, palindrome.rec_on h rfl (λ a, rfl) (λ a l h₁ h₂, 
begin 
  conv {to_lhs, rw h₂},
  rw ← list.reverse_singleton a,
  simp,
end)

open list
lemma palindrome_of_eq_reverse  : ∀ {l : list α}, l = list.reverse l → palindrome l 
| list.nil := λ _, palindrome.nil
| (a :: l) := begin
  rw reverse_cons',
  generalize hl' : l.reverse = l',
  cases l'  with b l',
  { assume h,
    rw h,
    exact palindrome.singleton _  },
  { assume h,
    have : a = b := by injection h,
    rw this at *,
    have h₁ : l = l' ++ [b] := by injection h,
    have h₂ :  b :: l' = reverse [b] ++ reverse l' := 
      by rwa  [← reverse_inj, hl', reverse_append] at h₁, 
    have : l' = l'.reverse := by injection h₂,
    rw h,
    exact have h₂ : length l' < 1 + length l := 
      by rw [h₁, add_comm, length_append];
        exact lt_trans (lt_succ_self _) (lt_succ_self _),
      palindrome.cons _ _ (palindrome_of_eq_reverse this) }
end
using_well_founded {rel_tac := λ _ _, `[exact ⟨_, measure_wf length⟩]}
```

#### [ Kevin Buzzard (Apr 04 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124638434):
Yes, I did it too. Here's the reason I was asking: Q1(c) of http://www.olympiad.org.uk/papers/2015/bio/round_one.html

#### [ Kevin Buzzard (Apr 04 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124638445):
My son wrote code to do Q1(a) so I thought I'd write code to do Q1(c) because I thought that the idea of writing code to do 1c would be interesting to him.

#### [ Kevin Buzzard (Apr 04 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124639841):
FWIW:
```lean
import data.list
open list 
universes u v
variables {α : Type u} {β : Type v}
inductive palindrome : list α → Prop
| nil : palindrome []
| one : ∀ a, palindrome [a] 
| cons : ∀ a L, palindrome L → palindrome ((a :: L) ++ [a])

namespace palindrome
open palindrome 

def is_rev_self (L : list β) : Prop := L = reverse L 

lemma rev_aux (a b : β) (L : list β) : is_rev_self (a :: (L ++ [b])) → a = b ∧ is_rev_self L :=
begin
unfold is_rev_self,intro H,
rw reverse_cons' at H,
rw reverse_append at H,
have H2 : a = b ∧ L ++ [b] = reverse L ++ [a],
  simpa using H,
split,exact H2.1,
rw H2.1 at H2,
have H3 := H2.2,
rw H2.1 at H3,
exact append_inj_left' H3 rfl,
end 


theorem palindrome_of_is_rev_self.aux (n : ℕ) : ∀ L : list β, L.length = n → is_rev_self L → palindrome L :=
begin
  unfold is_rev_self,
  apply nat.strong_induction_on n,
  clear n,intro n,
  intro IH,
  intro L,
  cases L with a M,
  { intros _ _,exact nil },
  apply list.reverse_rec_on M,
  { intros _ _, exact one a},
  intros L b X,clear X,
  intros HLL HRL,
  have H2 := rev_aux a b L HRL,
  rw ←cons_append,
  rw H2.1,
  apply cons,
  have H3 : 1 + (1 + length L) = n,
    simpa using HLL,
  rw [←add_assoc,add_comm] at H3,
  have H4 : length L < n,
  rw ←H3,exact nat.lt_add_of_zero_lt_left (length L) 2 dec_trivial,
  exact IH (length L) H4 L rfl H2.2,
end 

theorem palindrome_of_rev_self (L : list α) : is_rev_self L → palindrome L := 
  palindrome_of_is_rev_self.aux (length L) L rfl 

theorem is_rev_self_of_palindrome (L : list α) : palindrome L → is_rev_self L :=
begin
  intro H,
  induction H with a b M HPM HRM,
  { unfold is_rev_self,refl},
  { unfold is_rev_self,refl},
  { unfold is_rev_self,unfold is_rev_self at HRM,
    rw reverse_append,
    rw reverse_singleton,
    rw cons_append,
    rw reverse_cons',
    rw ←HRM,
    simp,
  }
end
end palindrome
```

#### [ Kevin Buzzard (Apr 04 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124639896):
My code didn't get highlighted. Possibly because the FWIW was in the same post.

#### [ Kevin Buzzard (Apr 04 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124639900):
No wait Chris also didn't post a pure code post

#### [ Kevin Buzzard (Apr 04 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124639914):
Aah got it, you have to write `lean` after the three backticks

#### [ Kevin Buzzard (Apr 04 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124640132):
Oh Chris you didn't use strong induction for the main theorem! (`palindrome_of_eq_reverse`). I made an aux lemma saying "forall n, if list length is n then blah" and applied strong induction to n, and then deduced the statement we wanted as a trivial corollary.

#### [ Chris Hughes (Apr 04 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124640484):
I did use strong induction, note ` using_well_founded {rel_tac := λ _ _, ``[exact ⟨_, measure_wf length⟩]} `

I also did question 1a, although in 2^(2^n) time, so I might lose some points for that.
```lean
instance [decidable_eq α] (l : list α) : decidable (palindrome l) :=
decidable_of_iff (l = l.reverse) ⟨λ h, palindrome_of_eq_reverse h, λ h, eq_reverse_of_palindrome h⟩

def  block_palindromes (l : list α) [decidable_eq α] := (sublists (sublists l)).filter
(λ m : list (list α), palindrome m ∧ m.foldl (++) nil = l)
```

#### [ Mario Carneiro (Apr 04 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124641990):
haha that solution

#### [ Mario Carneiro (Apr 04 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124642031):
You should write the deterministic bogosort, which enumerates permutations until it finds the sorted one

#### [ Kevin Buzzard (Apr 04 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124642035):
The mark scheme is just a bunch of tests, and you have to pass each one in under a second to get the marks.

#### [ Kevin Buzzard (Apr 05 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124644819):
So I finished the proof that the word has to have an even number of letters.

#### [ Kevin Buzzard (Apr 05 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124644823):
My proof was 240 lines, longer than my son's program to do 1(a).

#### [ Kevin Buzzard (Apr 05 2018 at 00:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124644873):
But I had to develop some concepts from scratch; in a parallel universe they would have already been in some library.

#### [ Kevin Buzzard (Apr 05 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124644889):
It was quite an interesting task. The question is about the following definition:

#### [ Kevin Buzzard (Apr 05 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124644891):
```lean
definition  listunfold : list (list α) → list α
| [] := []
| (a :: L) := a ++ (listunfold L)
```

#### [ Kevin Buzzard (Apr 05 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124644939):
but then I had to write `listunfold_append : listunfold (G1 ++ G2) = listunfold G1 ++ listunfold G2` and `listunfold_singleton`and so on

#### [ Kevin Buzzard (Apr 05 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124644960):
And similarly for `palindrome` (the inductive prop) I had to prove palindrome iff L = reverse L

#### [ Chris Hughes (Apr 05 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124644967):
Listunfold could also be defined as a fold. Then those two lemmas are probably there already because of associativity

#### [ Kevin Buzzard (Apr 05 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124645013):
Is that right?

#### [ Kevin Buzzard (Apr 05 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124645022):
I feel like if I defined it as a fold then I would then have to prove the two things I've used for my definition immediately afterwards

#### [ Chris Hughes (Apr 05 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124645024):
Not in that exact form, but they'd be quite easy.

#### [ Kevin Buzzard (Apr 05 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124645025):
and then the same proof for my append and singleton :-)

#### [ Kevin Buzzard (Apr 05 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124645031):
Oh everything was easy, but of course because this was recreational I did it all in tactic mode so my proofs go on for ages :-)

#### [ Chris Hughes (Apr 05 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124645032):
Those two things are lemmas about fold probably

#### [ Kevin Buzzard (Apr 05 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124645079):
You might well be right. I feel like I know enough Lean to write the definitions and basic properties of these new concepts like listunfold or palindrome

#### [ Kevin Buzzard (Apr 05 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124645080):
but

#### [ Kevin Buzzard (Apr 05 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124645084):
I feel like if I really knew everything that was already there, properly, then I would write things far more efficiently.

#### [ Chris Hughes (Apr 05 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124645097):
It's not about knowing what's there, it's knowing what's probably there.

#### [ Mario Carneiro (Apr 05 2018 at 03:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/palindromes/near/124650234):
Your `listunfold` is defined in core and proven in mathlib, by the name `list.join`. It is the monad "flattening" operation for lists


{% endraw %}
