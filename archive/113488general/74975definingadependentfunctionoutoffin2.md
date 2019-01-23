---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/74975definingadependentfunctionoutoffin2.html
---

## Stream: [general](index.html)
### Topic: [defining a dependent function out of `fin 2`](74975definingadependentfunctionoutoffin2.html)

---


{% raw %}
#### [ Scott Morrison (Sep 16 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134038733):
I'm stuck on something basic to do with `fin n`.

#### [ Scott Morrison (Sep 16 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134038734):
Suppose I have `T : fin 2 → Type`, and I happen to have `X : T ⟨ 0, by tidy ⟩` and a `Y : T ⟨ 1, by tidy ⟩`.

#### [ Scott Morrison (Sep 16 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134038736):
How do I construct the dependent function `Π n : fin 2, T n` which sends 0 to `X` and 1 to `Y`?

#### [ Simon Hudon (Sep 16 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134038784):
What about using an `if _ then _ else _`?

#### [ Scott Morrison (Sep 16 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134038797):
How would that work?

#### [ Scott Morrison (Sep 16 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134038812):
I remember someone showing me a trick to do `match` on `fin n`, but I can't find it anywhere now. :-(

#### [ Simon Hudon (Sep 16 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134038819):
```lean
def T : fin 2 → Type | x :=
if x = 0 then X else Y
```

#### [ Simon Hudon (Sep 16 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134038867):
If you find it again, please show me.

#### [ Scott Morrison (Sep 16 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134038944):
I don't see how your suggestion helps, @**Simon Hudon**:
```
import tactic.tidy

def T : fin 2 → Type := sorry
def X : T ⟨ 0, by tidy ⟩ := sorry
def Y : T ⟨ 1, by tidy ⟩ := sorry

def S : Π n : fin 2, T n
| x := if x = 0 then X else Y
```

#### [ Scott Morrison (Sep 16 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134038950):
errors with 
```
type mismatch at application
  ite (x = 0) X
term
  X
has type
  T ⟨0, X._proof_1⟩
but is expected to have type
  T x
```

#### [ Simon Hudon (Sep 16 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134038961):
Ah ok, I misunderstood your problem

#### [ Scott Morrison (Sep 16 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039161):
Here's a example of my problem:
```
import tactic.tidy

def T : fin 2 → Type := ([ℕ, ℤ].to_array).data
def X : T ⟨ 0, by tidy ⟩ := begin show ℕ, exact 1 end
def Y : T ⟨ 1, by tidy ⟩ := begin show ℤ, exact -1 end

def S : Π n : fin 2, T n
| ⟨ 0, _ ⟩ := X
| ⟨ 1, _ ⟩ := Y
| _ := sorry
```

#### [ Scott Morrison (Sep 16 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039167):
The question is to define `S`, following the intention shown, but without a `sorry`.

#### [ Scott Morrison (Sep 16 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039171):
(Side questions include better ways to write `T` in the first place.)

#### [ Simon Hudon (Sep 16 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039173):
One thing you can do is:

```lean
def S : Π n : fin 2, T n
| ⟨0,_⟩ := X
| ⟨1,_⟩ := Y
| ⟨succ (succ n),h⟩ := false.elim $ by { admit, }
```

#### [ Scott Morrison (Sep 16 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039233):
Excellent! That works, now the question becomes --- is my distant memory that there's an even better solution, correct? :-)

#### [ Simon Hudon (Sep 16 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039281):
My brain times out looking for one

#### [ Scott Morrison (Sep 16 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039283):
And what is the canonical way to fill in that admit, these days?

#### [ Scott Morrison (Sep 16 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039291):
I'd hoped that `linarith` was up to proving discharging `n+2 < 2` implies `false`, but apparently not.

#### [ Simon Hudon (Sep 16 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039293):
There's a `linarith` tactic coming down the pipes. Maybe it can handle `nat` now? We'd have to check

#### [ Simon Hudon (Sep 16 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039294):
Oh, that's too bad

#### [ Scott Morrison (Sep 16 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039334):
There was a recent addition saying it could do nat.

#### [ Scott Morrison (Sep 16 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039335):
Oh, maybe I haven't pulled that one yet...

#### [ Simon Hudon (Sep 16 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039342):
It feels like the kind of proposition that you should be able to prove in two steps. All I can think of takes more

#### [ Simon Hudon (Sep 16 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039389):
```lean
| ⟨succ (succ n),h⟩ := false.elim $ by { apply not_lt_of_ge _ h, repeat { apply succ_le_succ <|> apply zero_le } }
```

#### [ Scott Morrison (Sep 16 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039444):
(deleted)

#### [ Simon Hudon (Sep 16 2018 at 06:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039503):
Ah! This is even shorter:

```lean
  by { repeat { have h := lt_of_succ_lt_succ h }, cases h }
```

#### [ Mario Carneiro (Sep 16 2018 at 07:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039568):
that should be false by matching

#### [ Scott Morrison (Sep 16 2018 at 07:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039570):
hmm, that doesn't work for me?

#### [ Scott Morrison (Sep 16 2018 at 07:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039575):
but Kenny just showed me:
```
import tactic.tidy
-- import tactic.linarith

def T : fin 2 → Type := ([ℕ, ℤ].to_array).data
def X : T ⟨ 0, by tidy ⟩ := begin show ℕ, exact 1 end
def Y : T ⟨ 1, by tidy ⟩ := begin show ℤ, exact -1 end

def S : Π n : fin 2, T n
| ⟨ 0, _ ⟩ := X
| ⟨ 1, _ ⟩ := Y
| ⟨ nat.succ (nat.succ n), H ⟩ := false.elim $ by cases H with H H; cases H with H H; cases H
```

#### [ Mario Carneiro (Sep 16 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039620):
You can also use `fin.succ_rec_on` to get the right induction principle

#### [ Scott Morrison (Sep 16 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039621):
ah, and the new `linarith` really does it!

#### [ Kenny Lau (Sep 16 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039622):
how about
```lean
@[elab_as_eliminator]
def fin2.rec_on {C : fin 2 → Sort*} : ∀ (n : fin 2), C 0 → C 1 → C n
| ⟨0, _⟩ C0 _ := C0
| ⟨1, _⟩ _ C1 := C1
| ⟨n+2, H⟩ _ _ := false.elim $ not_le_of_gt H $ nat.le_add_left _ _
```

#### [ Scott Morrison (Sep 16 2018 at 07:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039668):
```
import tactic.tidy
import tactic.linarith

def T : fin 2 → Type := ([ℕ, ℤ].to_array).data
def X : T ⟨ 0, by tidy ⟩ := begin show ℕ, exact 1 end
def Y : T ⟨ 1, by tidy ⟩ := begin show ℤ, exact -1 end

def S : Π n : fin 2, T n
| ⟨ 0, _ ⟩ := X
| ⟨ 1, _ ⟩ := Y
| ⟨ n + 2, H ⟩ := by exfalso; linarith
```

#### [ Mario Carneiro (Sep 16 2018 at 07:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134039891):
```
import data.fin data.list.basic

def T : fin 2 → Type := ([ℕ, ℤ].to_array).data
def X : T ⟨0, dec_trivial⟩ := (1 : ℕ)
def Y : T ⟨1, dec_trivial⟩ := (-1 : ℤ)

def S : Π n : fin 2, T n :=
fin.cases X (λ i, fin.cases Y (λ i, i.elim0) i)
```

#### [ Scott Morrison (Sep 16 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134043762):
Thanks, Mario. I think I might use the `match` version, even if it depends on linarith, for decipherability.

#### [ Scott Morrison (Sep 16 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134043805):
I think I'll also write a `fin_cases` tactic, that works with a `fin n` hypothesis with `n` a numeral.

#### [ Scott Morrison (Sep 16 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/defining%20a%20dependent%20function%20out%20of%20%60fin%202%60/near/134043808):
(and actually gives you all the cases)


{% endraw %}
