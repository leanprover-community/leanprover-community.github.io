---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/84538intmod.html
---

## [new members](index.html)
### [int.mod](84538intmod.html)

#### [petercommand (Nov 01 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136906477):
Trying to prove `int.mod (int.of_nat a_1) ↑p < ↑p` in lean, but I wasn't able to unfold int.mod.

#### [Mario Carneiro (Nov 01 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136906517):
there should be a theorem called `int.mod_lt` for this

#### [Mario Carneiro (Nov 01 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136906523):
it is `int.mod_lt_of_pos` and it isn't true when `a_1 = 0`

#### [petercommand (Nov 01 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136906589):
I can't find int.mod_lt in C-c C-d

#### [petercommand (Nov 01 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136906637):
There is nat.mod_lt though

#### [Johan Commelin (Nov 01 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136906692):
@**petercommand** Welcome! Can you tell if Mario's suggestion works?

#### [petercommand (Nov 01 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136906699):
no

#### [Johan Commelin (Nov 01 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136906705):
Ok, can you give a more detailed version of what you want to prove? A "minimal working example" (MWE)

#### [Johan Commelin (Nov 01 2018 at 08:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136906750):
So something of the form
```lean
lemma foobar (p : ??) (a_1 : int) : int.mod (int.of_nat a_1) ↑p < ↑p := sorry
```

#### [petercommand (Nov 01 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136906810):
`def test : Π (a b : ℤ) (p : ℕ), (a + b) % p < p := sorry `

#### [Johan Commelin (Nov 01 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136906902):
That isn't true if `p = 0`, right?

#### [Mario Carneiro (Nov 01 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136906960):
Do you have mathlib? `int.mod_lt_of_pos` is in `data.int.basic`

#### [petercommand (Nov 01 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136906989):
@**Johan Commelin**  ah, it should be `def test : Π (a b : ℤ) (p : ℕ) (p >= 2), (a + b) % p < p := sorry`

#### [petercommand (Nov 01 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136907038):
@**Mario Carneiro**  Ah..Thanks! I didn't set up mathlib

#### [petercommand (Nov 01 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136907099):
why wasn't I able to unfold `int.mod` though

#### [Johan Commelin (Nov 01 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136907272):
I guess it is some sort of inductive definition

#### [Kevin Buzzard (Nov 01 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136907273):
`int` is an inductive type with two constructors. `int.mod` eats an `int`, and how it unfolds depends on which constructor you use -- `int.mod` can't unfold unless it knows which it is.

#### [petercommand (Nov 01 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136907290):
Which, in `int.of_nat a_1`, is `of_nat`

#### [Kevin Buzzard (Nov 01 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136907291):
But on the other hand you probably don't want to be unfolding `int.mod`. The devs will have made all the infrastructure you need, at least that's the philosophy.

#### [petercommand (Nov 01 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136907296):
True

#### [Kevin Buzzard (Nov 01 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136907297):
If you post a MWE I can try to help.

#### [petercommand (Nov 01 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136907354):
`def test : Π (a p : ℕ) (p > 0) , int.mod (int.of_nat a) ↑p < ↑p := sorry ` something like this

#### [petercommand (Nov 01 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136907408):
Thanks

#### [petercommand (Nov 01 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136907429):
My first MWE wasn't clear, this one should be a bit better

#### [Kevin Buzzard (Nov 01 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136907479):
the answer appears to be that the exact definition of `int.mod` uses `↑a` instead of `int.of_nat a`

#### [Kevin Buzzard (Nov 01 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136907498):
```lean
def test : Π (a p : ℕ) (p > 0) , int.mod (int.of_nat a) ↑p < ↑p := 
begin
--  unfold int.mod, -- fails
  change Π (a p : ℕ) (p > 0), int.mod (a : ℕ) ↑p < ↑p,
  unfold int.mod,
  sorry
end
```

#### [Kevin Buzzard (Nov 01 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136907500):
All the more reason why you shouldn't be unfolding it ;-)

#### [Kevin Buzzard (Nov 01 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136907578):
I just wrote `#check int.mod` and then right clicked on `int.mod` and peeked the actual definition.

#### [Kevin Buzzard (Nov 01 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136907650):
Of course the two things are definitionally equal: `example (a : ℕ) : int.of_nat a = ↑a := rfl `

#### [Kevin Buzzard (Nov 01 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136907654):
But under the hood `unfold` is using `simp`, and I think `simp` can be fussy about not changing things to definitionally equal things.

#### [Kevin Buzzard (Nov 01 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136907658):
Well, that's my amateur diagnosis anyway.

#### [Kenny Lau (Nov 01 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136907777):
```lean
def test (a b : ℤ) (p : ℕ) (Hp : p ≥ 2) : (a + b) % p < p :=
match a+b with
| (n:ℕ) := show ↑(n%p:ℕ) < (p:ℤ), from int.coe_nat_lt_coe_nat_of_lt
    (nat.mod_lt _ (lt_of_le_of_lt dec_trivial Hp))
| -[1+ n] := show ↑p + -[1+ n%p] < ↑p, from add_lt_of_le_of_neg
    (le_refl p) (int.neg_succ_lt_zero (n%p))
end

```

#### [Kevin Buzzard (Nov 01 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136907786):
A side comment -- I think `test` is not quite what you want to prove (AFK)

#### [Kenny Lau (Nov 01 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136907800):
```lean
def test (a b : ℤ) (p : ℕ) (Hp : p > 0) : (a + b) % p < p :=
match a+b with
| (n:ℕ) := show ↑(n%p:ℕ) < (p:ℤ), from int.coe_nat_lt_coe_nat_of_lt (nat.mod_lt _ Hp)
| -[1+ n] := show ↑p + -[1+ n%p] < ↑p, from add_lt_of_le_of_neg
    (le_refl p) (int.neg_succ_lt_zero (n%p))
end
```
(I just noticed that you changed the condition again)

#### [petercommand (Nov 01 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136907877):
hmm, this is quite annoying..I thought `int.mod` was directly matching on the constructor

#### [petercommand (Nov 01 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136907942):
@**Kenny Lau** thanks

#### [Kenny Lau (Nov 01 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136907960):
```lean
def test (a b : ℤ) (p : ℕ) (Hp : p > 0) : (a + b) % p < p :=
match a+b with
| (n:ℕ) := show ↑(n%p:ℕ) < (p:ℤ), from int.coe_nat_lt_coe_nat_of_lt (nat.mod_lt _ Hp)
| -[1+ n] := show ↑p + -[1+ n%p] < ↑p, from int.lt.intro (neg_add_cancel_right (p:ℤ) (n%p+1))
end
```

#### [Kenny Lau (Nov 01 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136907961):
it is

#### [Kenny Lau (Nov 01 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136907966):
oh, and it isn't `def`

#### [Kenny Lau (Nov 01 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136907967):
it's `theorem`

#### [Kenny Lau (Nov 01 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908008):
```lean
theorem test (a b : ℤ) (p : ℕ) (Hp : p > 0) : (a + b) % p < p :=
match a+b with
| (n:ℕ) := show ↑(n%p:ℕ) < (p:ℤ), from int.coe_nat_lt_coe_nat_of_lt (nat.mod_lt _ Hp)
| -[1+ n] := show ↑p + -[1+ n%p] < ↑p, from int.lt.intro (neg_add_cancel_right (p:ℤ) (n%p+1))
end
```

#### [petercommand (Nov 01 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908019):
aren't they synonyms?

#### [Kenny Lau (Nov 01 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908020):
no

#### [petercommand (Nov 01 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908028):
what's different between def and thoerem?

#### [Kenny Lau (Nov 01 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908031):
def is data

#### [Kenny Lau (Nov 01 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908032):
theorem is proof

#### [petercommand (Nov 01 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908082):
I mean, semantically, are they different?

#### [Kenny Lau (Nov 01 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908095):
yes

#### [petercommand (Nov 01 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908114):
proof irrelevance?

#### [petercommand (Nov 01 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908179):
https://leanprover.github.io/theorem_proving_in_lean/propositions_and_proofs.html
Ah, it says that 
`by proof irrelevance, any two proofs of that theorem are definitionally equal.`

#### [Kenny Lau (Nov 01 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908184):
```lean
theorem x : nat := 5
def test : x=5 := sorry
```

#### [Kenny Lau (Nov 01 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908186):
```quote
https://leanprover.github.io/theorem_proving_in_lean/propositions_and_proofs.html
Ah, it says that 
`by proof irrelevance, any two proofs of that theorem are definitionally equal.`
```
that's irrelevant

#### [Kevin Buzzard (Nov 01 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908209):
Kenny, independent of that def/theorem business, what's happening below? @**petercommand** 's original formulation of the MWE has something wrong with it I think:

```lean
def test : Π (a p : ℕ) (p > 0) , int.mod (int.of_nat a) ↑p < ↑p := 
begin
  intro a,
  intro b, -- ??
  intro p,
  intro HP,
  -- ⊢ int.mod (int.of_nat a) ↑p < ↑p
  sorry
end
```

#### [Kenny Lau (Nov 01 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908253):
```lean
def test : 5=5 := rfl
#print prefix test
/-
test : 5 = 5
test.equations._eqn_1 : test = rfl
-/

theorem test2 : 5=5 := rfl
#print prefix test2
/-
test2 : 5 = 5
-/
```

#### [Kenny Lau (Nov 01 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908274):
@**Kevin Buzzard** lol the conditions keep changing

#### [Kevin Buzzard (Nov 01 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908278):
I think the `p` in `forall p` isn't the same as the `p` in `p > 0`.

#### [Kenny Lau (Nov 01 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908282):
@**petercommand** can you make up your mind?

#### [Kevin Buzzard (Nov 01 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908284):
I never changed anything, I just copied his MWE.

#### [Kenny Lau (Nov 01 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908289):
```quote
I think the `p` in `forall p` isn't the same as the `p` in `p > 0`.
```
I think it's the same

#### [Kevin Buzzard (Nov 01 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908332):
Did you look at my tactic mode post?

#### [Kevin Buzzard (Nov 01 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908334):
There's an extra nat

#### [Kevin Buzzard (Nov 01 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908337):
`-- ??`

#### [Kenny Lau (Nov 01 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908349):
I don't know why you have 4 `intro`s

#### [Kevin Buzzard (Nov 01 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908354):
because Lean is asking for 4. That's the point I'm trying to make

#### [Kenny Lau (Nov 01 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908359):
what do you mean Lean is asking for 4

#### [Kevin Buzzard (Nov 01 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908366):
What do you mean? The function wants 4 inputs

#### [Kenny Lau (Nov 01 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908367):
that's spooky

#### [Kevin Buzzard (Nov 01 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908369):
Must be Halloween.

#### [Kenny Lau (Nov 01 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908412):
oh!

#### [petercommand (Nov 01 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908413):
o.o

#### [Kenny Lau (Nov 01 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908420):
lol

#### [Kenny Lau (Nov 01 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908427):
```lean
theorem test : Π (a : ℕ) (p > 0) , int.mod (int.of_nat a) ↑p < ↑p :=
```

#### [Kenny Lau (Nov 01 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908428):
`>` is a binder or something

#### [Kevin Buzzard (Nov 01 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908432):
right

#### [Kevin Buzzard (Nov 01 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908489):
@**petercommand** this is fine: `theorem test : ∀ (a p : ℕ), (p > 0) → int.mod (int.of_nat a) ↑p < ↑p :=`

#### [Kevin Buzzard (Nov 01 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908504):
but `(p > 0)` before the comma gets interpreted as "and there's another variable p, different to the p you just mentioned"

#### [Kenny Lau (Nov 01 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908516):
I don't think @**petercommand** has tested his "MWE" before posting

#### [Kevin Buzzard (Nov 01 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908518):
`def test' : Π (a : ℕ) (p > 0) , int.mod (int.of_nat a) ↑p < ↑p := ` is OK

#### [Kevin Buzzard (Nov 01 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908521):
I just made it a bit more minimal, that's all ;-)

#### [petercommand (Nov 01 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908569):
```quote
I don't think @**petercommand** has tested his "MWE" before posting
```
Yeah, I should've tested the MWEs o.o Thought that was simple enough

#### [Kenny Lau (Nov 01 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908575):
```lean
theorem test' (a : ℕ) (p > 0) : int.mod (int.of_nat a) ↑p < ↑p :=
int.coe_nat_lt_coe_nat_of_lt (nat.mod_lt _ H)
```

#### [petercommand (Nov 01 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908636):
Hmm, actually, I tested the MWEs, but didn't discover that I got one more variable

#### [petercommand (Nov 01 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908637):
anyway

#### [Kevin Buzzard (Nov 01 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908828):
```lean
import data.int.basic

theorem test' (a p : ℕ) (H : p > 0) : int.mod (int.of_nat a) ↑p < ↑p :=
int.mod_lt_of_pos a (int.coe_nat_lt_coe_nat_of_lt H)
```

#### [AHan (Nov 01 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908830):
@**Kenny Lau**  About the difference between "def" and "theorem", why is there test.eqations._eqn_1 appeared in your example
`def test : 5=5 := rfl
#print prefix test`

#### [Kevin Buzzard (Nov 01 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908835):
because Kenny (intentionally) wrote bad code

#### [Kenny Lau (Nov 01 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908842):
because `test` is now a definition so it has definitional equations

#### [Kenny Lau (Nov 01 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908844):
just write any old definition

#### [Kevin Buzzard (Nov 01 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908846):
If you use def instead of theorem or theorem instead of def, expect random things

#### [Kevin Buzzard (Nov 01 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908858):
because they were not designed to be used in these circumstances

#### [Kenny Lau (Nov 01 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908901):
undocumented behaviour... lul

#### [Kevin Buzzard (Nov 01 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908906):
I think "garbage in, garbage out" is well documented in the literature

#### [AHan (Nov 01 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136908975):
What does the definitional equations refers to here?
And how to use it in a normal def?

#### [Kenny Lau (Nov 01 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136909036):
you don't really use it

#### [Kenny Lau (Nov 01 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136909041):
it's internal mechanism

#### [Kevin Buzzard (Nov 01 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136909042):
Every time you make a definition (especially a nice complicated one, maybe with pattern matching) Lean creates some secret "equation lemmas"

#### [Kevin Buzzard (Nov 01 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136909043):
and when you try and unfold the definition, Lean uses these lemmas

#### [Kevin Buzzard (Nov 01 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136909058):
As Kenny says, this is all done internally and the user is not supposed to have to worry about it. It's basically the trick which makes "unfold" work.

#### [Kevin Buzzard (Nov 01 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136909070):
`unfold X` is `simp only [equation lemmas for X]`

#### [Kevin Buzzard (Nov 01 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136909131):
(this is my slightly amateurish understanding of it -- I am a mathematician so shouldn't really be talking about implementation issues)

#### [AHan (Nov 01 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/int.mod/near/136909163):
Are they the beta reduction rules?

