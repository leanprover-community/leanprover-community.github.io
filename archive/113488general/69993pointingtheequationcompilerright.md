---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/69993pointingtheequationcompilerright.html
---

## Stream: [general](index.html)
### Topic: [pointing the equation compiler right](69993pointingtheequationcompilerright.html)

---


{% raw %}
#### [ James Wood (May 13 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126495867):
Hi, I'm new to Lean. I'm trying to write the following, but termination checking fails for `weaken_term` in the second recursive call for `app` and the recursive call for `lam`. Each time, the reported problem is that `m` does not decrease, but that should be irrelevant because the induction is on the term. How can I give Lean this hint? Or is the Lean termination checker not sufficiently Foetus-like, so I have to do something else?

```
open nat

inductive fin' : nat → Type
| zero {n} : fin' (succ n)
| succ {n} : fin' n → fin' (succ n)
open fin'

inductive dir : Type
| syn : dir
| chk : dir
open dir

inductive term : nat → dir → Type
| var {n} (i : fin' n)                      : term n syn
| app {n} (e : term n syn) (s : term n chk) : term n syn
| lam {n} (s : term (succ n) chk)           : term n chk
open term

def plus : nat → nat → nat
| zero n := n
| (succ m) n := succ (plus m n)

def weaken_fin' {n} : ∀ m, fin' (plus m n) → fin' (plus m (succ n))
| zero i := succ i
| (succ m) zero := zero
| (succ m) (succ i) := succ (weaken_fin' m i)

def weaken_term {n} : ∀ m {d}, term (plus m n) d → term (plus m (succ n)) d
| m syn (var i) := var (weaken_fin' m i)
| m syn (app e s) := app (weaken_term m e) (weaken_term m s)
| m chk (lam s) := lam (weaken_term (succ m) s)
```

#### [ Mario Carneiro (May 13 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126496313):
It can't be done directly by induction on `term`, since you would forget the relation to m and n

#### [ Mario Carneiro (May 13 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126496355):
Here's a way to write that you want to do induction explicitly with the equation compiler:
```
def weaken_term' {n} : ∀ {k d}, term k d → ∀ m, plus m n = k → term (plus m (succ n)) d
| _ syn (var i) m rfl := var (weaken_fin' m i)
| _ syn (app e s) m rfl := app (weaken_term' e m rfl) (weaken_term' s m rfl)
| _ chk (lam s) m rfl := lam (weaken_term' s (succ m) rfl)

def weaken_term {n} (m) {d} (s : term (plus m n) d) : term (plus m (succ n)) d :=
weaken_term' s m rfl
```

#### [ James Wood (May 13 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126496552):
Thanks! Where exactly is the relation to `m` and `n` being lost? I can't quite pick out why the term is allowed to depend on the index `d` like it does.

#### [ Mario Carneiro (May 13 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126496755):
It might help to try using the `induction` tactic to get a sense of what lean is doing under the hood

#### [ Mario Carneiro (May 13 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126497036):
```
def weaken_term {n} : ∀ m {d}, term (plus m n) d → term (plus m (succ n)) d :=
begin
  intros m d s,
  induction s with n' i n' e s IH1 IH2 n' s IH,
  exact var (weaken_fin' m i), --fail
end.
```
Notice that you won't be able to prove the first goal because the type is `fin' n'` instead of `fin' (plus m n)`. This is where the equality assumption comes in

#### [ Mario Carneiro (May 13 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126497123):
You can actually prove this directly in tactic mode by starting with
```
  intros m d s,
  generalize h : plus m n = k,
  induction s with n' i n' e s IH1 IH2 n' s IH generalizing k; subst k,
```
which has the effect of introducing the equality before doing the induction

#### [ James Wood (May 13 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126497175):
Can the problem be restated in terms of induction principles, rather than tactics? If so, I think I can work that out.

#### [ Mario Carneiro (May 13 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126497229):
Look at the proof produced by the naive induction tactic approach:
```
def weaken_term {n} : ∀ m {d}, term (plus m n) d → term (plus m (succ n)) d :=
begin
  intros m d s,
  induction s; admit
end
set_option pp.implicit true
#print weaken_term
```
```
def weaken_term : Π {n : ℕ} (m : ℕ) {d : dir}, term (plus m n) d → term (plus m (succ n)) d :=
λ {n : ℕ} (m : ℕ) (d : dir) (s : term (plus m n) d),
  (λ (s : term (plus m n) d),
     @term.rec (λ (_x : ℕ) {d : dir} (s : term _x d), term (plus m (succ n)) d)
       (λ {s_n : ℕ} (s_i : fin' s_n), sorry)
       (λ {s_n : ℕ} (s_e : term s_n syn) (s_s : term s_n chk) (s_ih_e : term (plus m (succ n)) syn)
        (s_ih_s : term (plus m (succ n)) chk), sorry)
       (λ {s_n : ℕ} (s_s : term (succ s_n) chk) (s_ih : term (plus m (succ n)) chk), sorry)
       (plus m n)
       d
       s)
    s
```

#### [ Mario Carneiro (May 13 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126497230):
Notice that the motive to the `term.rec` is `λ (_x : ℕ) {d : dir} (s : term _x d), term (plus m (succ n)) d`

#### [ Mario Carneiro (May 13 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126497271):
In other words, it has assumed you are trying to prove `def not_true {n} : ∀ m {d} k, term k d → term (plus m (succ n)) d`

#### [ Mario Carneiro (May 13 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126497278):
where it has "forgotten" that the `k` there is actually `plus m n`

#### [ Mario Carneiro (May 13 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126497464):
By the way, something seems off about your inductive:
```
theorem no_chk {n} : term n chk → false := 
begin
  generalize h : chk = d,
  intro s,
  induction s generalizing h; injection h,
  exact s_ih rfl
end
```

#### [ James Wood (May 13 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126497469):
That's fixed now.

#### [ James Wood (May 13 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126497994):
```quote
You can actually prove this directly in tactic mode by starting with
...
which has the effect of introducing the equality before doing the induction
```
I tried doing this, but I get a lot of weird-looking errors, like “vm check failed”, “invalid 'begin-end' expression, ',' expected”, and “sync”.

#### [ James Wood (May 13 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126497995):
Code (supporting definitions have changed a bit):
```
def weaken_term' {m} : ∀ n {d}, term' (m + n) d → term' ((m + 1) + n) d :=
begin
  intros n d t,
  generalize h : m + n = k
  induction t with n' i n' e s ihe ihs n' s ih generalizing k; subst k,
  { _ },
  { _ },
  { _ },
  { _ },
  { _ }
end
```

#### [ Mario Carneiro (May 13 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126498056):
You shouldn't use `{ _ }` as a tactic. Lean doesn't like being asked to run tactics that are not yet determined

#### [ Mario Carneiro (May 13 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126498057):
instead you can just write `{ }`

#### [ Mario Carneiro (May 13 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126498058):
meaning "run no tactic", and then it will fail at the right bracket because you aren't done yet

#### [ James Wood (May 13 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126498099):
Aah, thanks.

#### [ James Wood (May 13 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126498100):
The problem seemed to be a missing comma, so that's sorted.

#### [ James Wood (May 13 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126498155):
Is `_` the best way to leave a hole in a pattern-matching definition?

#### [ James Wood (May 13 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126498157):
Or is there some way to introduce an interactive hole?

#### [ Mario Carneiro (May 13 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126498199):
I don't quite understand what you mean

#### [ Mario Carneiro (May 13 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126498204):
I can't think of what an interactive hole is, but `_` is useful as a wildcard in patterns

#### [ James Wood (May 13 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126498247):
Hole à la Agda (or Idris, to some extent).

#### [ James Wood (May 13 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126498303):
Maybe it's not necessary with the way lean-mode works, though I still feels like a hack to use the “this should be inferrable by unification” thing to mean “I'm going to write something here”.

#### [ Mario Carneiro (May 13 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126498349):
Lean actually has holes in term mode, `{! !}`, but they are not well developed at all and never made it past alpha

#### [ Mario Carneiro (May 13 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pointing%20the%20equation%20compiler%20right/near/126498354):
for the most part you can use `begin end` or `_` where stuff is expected


{% endraw %}
