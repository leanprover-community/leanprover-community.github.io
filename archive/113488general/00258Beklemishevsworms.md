---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/00258Beklemishevsworms.html
---

## [general](index.html)
### [Beklemishev's worms](00258Beklemishevsworms.html)

#### [Kenny Lau (Dec 31 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beklemishev's worms/near/154084805):
```lean
def next_aux (N : nat) : list nat -> nat
| [] := 0
| (hd :: tl) := if hd < N then 0 else next_aux tl + 1

def next (m : nat) : list nat -> list nat
| [] := []
| (0 :: tl) := tl
| ((n+1) :: tl) := let index := next_aux (n+1) tl,
    B := n :: list.take index tl,
    G := list.drop index tl in
    ((++ B)^[m+1] B) ++ G

-- Beklemishev's worms
def worm_step (initial : nat) : Π step : nat, list nat
| 0 := [initial]
| (m+1) := next m (worm_step m)

#eval (list.range 52).map (worm_step 2)

-- It will terminate
theorem worm_principle : ∀ n, ∃ s, worm_step n s = [] := sorry
```

#### [Kenny Lau (Dec 31 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beklemishev's worms/near/154084808):
Try to fill the sorry :P

#### [Kevin Buzzard (Dec 31 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beklemishev's worms/near/154087365):
It's like Goodstein's theorem. I'd never seen it before. Nice! Is there some proof using ordinals like Goodstein?

#### [Kevin Buzzard (Dec 31 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beklemishev's worms/near/154087416):
Could you make it so that the proof is `dec_trivial`?

#### [Kevin Buzzard (Dec 31 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beklemishev's worms/near/154087424):
add some clever decidability instance

#### [Mario Carneiro (Dec 31 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beklemishev's worms/near/154098834):
Not really. (See https://www.researchgate.net/publication/27709556_The_Worm_principle for the original proof that this function terminates.) You can make any theorem provable by `dec_trivial` because if it's provable then it's decidable, but the really important part of this argument is the well-foundedness of a particular order. I would suggest mapping to `onote`

#### [Mario Carneiro (Jan 01 2019 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Beklemishev's worms/near/154106468):
Here's the ordinal function:
```lean
def build_aux : list nat → list nat × list (list nat)
| ((n+1) :: l) := let (l', L) := build_aux l in (n::l', L)
| (0 :: l) := let (l', L) := build_aux l in ([], l' :: L)
| [] := ([], [])

def build (l : list nat) : list (list nat) :=
let (l', L) := build_aux l in l' :: L

theorem build_lt (l : list nat) : ∀ x ∈ build l, sizeof x < sizeof l :=
sorry

local notation `ω` := ordinal.omega
noncomputable def map : list nat → ordinal | l :=
if ∀ x ∈ l, x = 0 then l.length else
list.sum (list.pmap (λ a h, ω ^ map a) (build l) (build_lt l))
```

