---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/92378ringfailsbutsimpworks.html
---

## [general](index.html)
### [ring fails but simp works](92378ringfailsbutsimpworks.html)

#### [Chris Hughes (Apr 08 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/ring%20fails%20but%20simp%20works/near/124808425):
In the following context `simp [mul_comm, mul_left_comm, mul_assoc]` solved the goal, but `ring` failed. What's going on?
```lean
R : Type u_1,
_inst_2 : comm_ring R,
L : list R,
H : 1 ∈ generate {x : R | x ∈ L},
s : Π (i : fin (list.length L)), loc R (powers (f L i)),
h : β L s = 0,
t : Π (i : fin (list.length L)), R × ↥(powers (f L i)) := λ (i : fin (list.length L)), out (s i),
r : fin (list.length L) → ℕ := λ (i : fin (list.length L)), some _,
hst : ∀ (i : fin (list.length L)), s i = ⟦((t i).fst, ⟨f L i ^ r i, _⟩)⟧,
hi : ∀ (i : fin (list.length L)), s i = ⟦((t i).fst, ⟨((t i).snd).val, _⟩)⟧,
hβ :
  ∀ (i j : fin (list.length L)),
    ⟦((t i).fst * f L j ^ r i, ⟨(f L i * f L j) ^ r i, _⟩)⟧ =
      ⟦((t j).fst * f L i ^ r j, ⟨(f L i * f L j) ^ r j, _⟩)⟧,
this :
  ∀ (i j : fin (list.length L)),
    ∃ (n : ℕ),
      ((f L i * f L j) ^ r i * ((t j).fst * f L i ^ r j) - (f L i * f L j) ^ r j * ((t i).fst * f L j ^ r i)) *
          (f L i * f L j) ^ n =
        0,
n : fin (list.length L) → fin (list.length L) → ℕ := λ (i j : fin (list.length L)), some _ + r i + r j,
hn : ∀ (i j : fin (list.length L)), (f L i ^ r i * (t j).fst - f L j ^ r j * (t i).fst) * (f L i * f L j) ^ n i j = 0,
N : ℕ := sum univ (λ (ij : fin (list.length L) × fin (list.length L)), n (ij.fst) (ij.snd)),
Nlt : ∀ (i j : fin (list.length L)), n i j ≤ N,
i j : fin (list.length L)
⊢ f L i ^ r i * (t j).fst * (f L i ^ (N - n i j) * f L j ^ (N - n i j) * (f L i ^ n i j * f L j ^ n i j)) +
      -(f L j ^ r j * (t i).fst * (f L i ^ (N - n i j) * f L j ^ (N - n i j) * (f L i ^ n i j * f L j ^ n i j))) =
    f L i ^ r i * (t j).fst * (f L i ^ n i j * f L j ^ n i j) * (f L i ^ (N - n i j) * f L j ^ (N - n i j)) +
      -(f L j ^ r j * (t i).fst * (f L i ^ n i j * f L j ^ n i j) * (f L i ^ (N - n i j) * f L j ^ (N - n i j)))
```

