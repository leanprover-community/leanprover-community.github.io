---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/70126CoqsProgramtactic.html
---

## Stream: [new members](index.html)
### Topic: [Coq's Program tactic](70126CoqsProgramtactic.html)

---

#### [Wojciech Nawrocki (Dec 16 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coq%27s%20Program%20tactic/near/151888312):
Is there something akin to Coq's [Program](https://coq.inria.fr/refman/addendum/program.html) tactic in Lean? I thought that the equation compiler is basically that, but it seems to fail in the case when it should generate an equality at the type level. In my example:
```lean
-- type-level list
inductive InList: list ℕ → ℕ → Type
| Z: ∀ {L n}, InList (n::L) n
| S: ∀ {L n n'}, InList L n → InList (n'::L) n

-- type of functions that map the list L to natural numbers
def ListMap (L) := ∀ {n}, InList L n → ℕ

def id_map {L}: ListMap L := λ n (v: InList L n), n

-- extends m with n
def extend_map {L} (n: ℕ) (m: ListMap L): ListMap (n::L)
:= λ n' (v: InList (n::L) n'),
  match v with
  | InList.Z := sorry -- i would like to synthesize n = n' here
  | InList.S := sorry
  end
```
the `match` fails with
```lean
type mismatch at application
  _match InList.Z
term
  InList.Z
has type
  InList (?m_1 :: ?m_2) ?m_1
but is expected to have type
  InList (n :: L) n'
```

#### [Kenny Lau (Dec 16 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coq%27s%20Program%20tactic/near/151888604):
```lean
-- type-level list
inductive InList: list ℕ → ℕ → Type
| Z: ∀ {L n}, InList (n::L) n
| S: ∀ {L n n'}, InList L n → InList (n'::L) n

-- type of functions that map the list L to natural numbers
def ListMap (L) := ∀ {n}, InList L n → ℕ

def id_map {L}: ListMap L := λ n (v: InList L n), n

-- extends m with n
def extend_map {L} (n: ℕ) (m: ListMap L): ListMap (n::L)
:= λ n' (v: InList (n::L) n'),
  match n, n', v with
  | n, n', InList.Z := have n = n' := rfl, sorry
  | n, n', InList.S h := sorry
  end
```

#### [Wojciech Nawrocki (Dec 16 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coq%27s%20Program%20tactic/near/151889015):
Thank you, I was hoping it could be done automatically, but this is fairly concise :)

#### [Kenny Lau (Dec 16 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coq%27s%20Program%20tactic/near/151889146):
no, it is done automatically, `have n = n' := rfl` is just demonstrating it

#### [Kenny Lau (Dec 16 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coq%27s%20Program%20tactic/near/151889151):
if you put an underscore to replace `sorry` you will see the lemma being `n = n`

#### [Wojciech Nawrocki (Dec 16 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coq%27s%20Program%20tactic/near/151889297):
Oh indeed, so it seems the compiler will only equate variables which are being matched rather than everything that `v` in `match v with` depends on.

#### [Kenny Lau (Dec 16 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coq%27s%20Program%20tactic/near/151889365):
right

#### [Wojciech Nawrocki (Dec 16 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coq%27s%20Program%20tactic/near/151895563):
Hm no that's not right, it generalizes the matched variable and the state I get in
```lean
  match n, n', v with
  | _, _, InList.Z := begin
     -- state here
  end
  | n, n', (InList.S h) := n
  end
```
is 
```lean
L : list ℕ,
n : ℕ,
m : ListMap L,
n' : ℕ,
v : InList (n :: L) n',
_match : Π (_a _a_1 : ℕ), InList (_a :: L) _a_1 → ℕ,
_x : ℕ
⊢ ℕ
```
where `n` and `n'` are not equal

#### [Chris Hughes (Dec 16 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coq%27s%20Program%20tactic/near/151895778):
In this state `n` and `n` have both effectively been replaced with `_x`, it just hasn't cleared the old `n` and `n'`

#### [Wojciech Nawrocki (Dec 16 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coq%27s%20Program%20tactic/near/151896024):
The example posted here is a bit simplified to make sense without context, but basically I need the `n` and `n'` to be equal in the type of `v`, since my obligation for the return value is that they match, and for that I need the "old" values to be `_x` so that they can be substituted within `v`.

#### [Chris Hughes (Dec 16 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coq%27s%20Program%20tactic/near/151896140):
Can you not use `InList.Z` instead of `v`. `v` isn't a variable any more, since you're dealing with the case `v = InList.Z`

#### [Wojciech Nawrocki (Dec 16 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coq%27s%20Program%20tactic/near/151896583):
Sorry, I oversimplified again. The return type is dependent on `n` and needs to be a value given as an argument to `extend_map`. A fuller example:
```lean
-- type-level list
inductive InList: list ℕ → ℕ → Type
| Z: ∀ {L n}, InList (n::L) n
| S: ∀ {L n n'}, InList L n → InList (n'::L) n

inductive Foo: ∀ n: ℕ, Type
| A: ∀ n, Foo n
| B: Foo 1
| C: Foo 2

-- type of functions that map the list L to dependent `Foo`s in the list
def ListMap (L) := ∀ {n}, InList L n → Foo n

def id_map {L}: ListMap L := λ n (v: InList L n), Foo.A n

-- extends m with e
def extend_map {L n} (e: Foo n) (m: ListMap L): ListMap (n::L)
:= λ n' (v: InList (n::L) n'),
  match n, n', v with
  | _, _, InList.Z := _ -- needs to be e and have type `Foo n`, but Lean generalizes to type `Foo _x`
  | n, n', (InList.S h) := sorry
  end
```

#### [Chris Hughes (Dec 16 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coq%27s%20Program%20tactic/near/151896987):
```lean
def extend_map {L n} (e: Foo n) (m: ListMap L): ListMap (n::L)
:= λ n' (v: InList (n::L) n'),
  match n, n', v, e with
  | _, _, InList.Z := id -- needs to be e and have type `Foo n`, but Lean generalizes to type `Foo _x`
  | n, n', (InList.S h) := sorry
  end
```

#### [Wojciech Nawrocki (Dec 16 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Coq%27s%20Program%20tactic/near/151897653):
Hm that seems to work 🧙, thanks!

