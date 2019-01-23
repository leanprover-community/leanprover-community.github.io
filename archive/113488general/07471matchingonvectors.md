---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/07471matchingonvectors.html
---

## Stream: [general](index.html)
### Topic: [matching on vectors](07471matchingonvectors.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Floris van Doorn (Oct 19 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136140175):
Is there a library of vectors, defined inductively?
```
inductive dvector (α : Type u) : ℕ → Type u
| nil {} : dvector 0
| cons : ∀{n}, α → dvector n → dvector (n+1)
```
Alternatively, can I use the equation compiler to pattern match on `vector` in the library in a nice way? I want something resembling the definitions in the following code:
```
universe variables u v w
inductive dvector (α : Type u) : ℕ → Type u
| nil {} : dvector 0
| cons : ∀{n}, α → dvector n → dvector (n+1)

local notation h :: t  := dvector.cons h t
local notation `[` l:(foldr `, ` (h t, dvector.cons h t) dvector.nil `]`) := l

namespace dvector
variables {α : Type u} {β : Type v} {γ : Type w} {n : ℕ}

@[simp] protected def map (f : α → β) : ∀{n : ℕ}, dvector α n → dvector β n
| _ []      := []
| _ (x::xs) := f x :: map xs

@[simp] protected def map_id : ∀{n : ℕ} (xs : dvector α n), xs.map (λx, x) = xs
| _ []      := rfl
| _ (x::xs) := by dsimp; simp*

@[simp] protected def map_congr {f g : α → β} (h : ∀x, f x = g x) : 
  ∀{n : ℕ} (xs : dvector α n), xs.map f = xs.map g
| _ []      := rfl
| _ (x::xs) := by dsimp; simp*

@[simp] protected def map_map (g : β → γ) (f : α → β): ∀{n : ℕ} (xs : dvector α n), 
  (xs.map f).map g = xs.map (λx, g (f x))
  | _ []      := rfl
  | _ (x::xs) := by dsimp; simp*

end dvector
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Floris van Doorn (Oct 19 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136140303):
(and yes, *these* operations are probably already defined for `vector`, but I want to define new operations on vectors using pattern matching, and I kind-of don't want to do it on lists first)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 19 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136140731):
`vector.cons` already has the `pattern` attribute; have you tried using it in the equation compiler?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Floris van Doorn (Oct 19 2018 at 23:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136141401):
What does the `pattern` attribute do?
Yes, I tried matching on vectors using `vector.nil` and `vector.cons`, but something like this doesn't work:
```
protected def vector.my_map {α : Type u} {β : Type v} {γ : Type w} (f : α → β) : 
 ∀{n : ℕ}, vector α n → vector β n
| _ vector.nil         := vector.nil
| _ (vector.cons x xs) := vector.cons (f x) (vector.my_map xs)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 20 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136141888):
It lets you use the definition in a pattern context, I'm not too sure of the details of how it works

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 20 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136142036):
Yeah, it seems not to work, unfortunate...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 20 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136142212):
It seems like maybe the problem is the way that Lean moved the proof field of `vector.nil` into a `theorem`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 20 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136142217):
I wonder whether there is some option to disable that?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 20 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136142222):
though one would like it to not matter, since it is a Prop anyways

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 20 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136143993):
@**Floris van Doorn** There should be a custom recursor for this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 20 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136143995):
that's usually the way we show alternate inductive patterns for types

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Oct 20 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136145108):
But can you use that with the equation compiler?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 20 2018 at 05:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136152692):
@**Floris van Doorn** In `kbb` we experimented with code like this:
```lean
def vector.mk {α : Type*} {n : ℕ} (l : list α) (pr : l.length = n) :
  vector α n := ⟨l, pr⟩

notation `![` l:(foldr `, ` (h t, list.cons h t) list.nil `]`) :=
  vector.mk l rfl

def {u} fast_matrix (m n : ℕ) (α : Type u) : Type u := vector (vector α n) m

example : fast_matrix 2 3 ℤ :=
![![ 1 , 1,  5 ],
  ![ 0 , 1, -2 ]]
```
It is not exactly what you want, but maybe a bit related.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Floris van Doorn (Oct 21 2018 at 00:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136187187):
Yes, a custom recursor for `vector` would be nice. That doesn't affect pattern matching though, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Floris van Doorn (Oct 21 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136187264):
What is the reason to define vectors (and fin) this way, instead of the inductive family with the nicer pattern matching? Is it because the virtual machine can then use its representation of lists (and nat) for efficient computation?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Floris van Doorn (Oct 21 2018 at 00:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136187318):
@**Johan Commelin** that is indeed nice notation. You can get the same effect if you define the notation using `vector.nil` and `vector.cons`, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 21 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136187497):
Yes, both of these types are implemented this way for efficient computation

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 21 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136187550):
The downside of custom recursors is of course that they don't hook in to the equation compiler, so you don't get the nice pattern matching

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 21 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136187558):
An alternative is to define the alternate inductive structure as `vector2` or something, and prove an equiv

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 21 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136187561):
If you want these, `fin2` and `vector2` are defined in `dioph.lean`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Floris van Doorn (Oct 21 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136187742):
Oh, so they do exist, just not in the `data` folder. In `dioph` I only find `vector3` though. Where is `vector2`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 21 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136190101):
oh,  I thought I renamed it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 21 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136190144):
`vector2` used to be just `fin n -> A`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 21 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/matching%20on%20vectors/near/136190149):
or maybe it was `fin2 n -> A`


{% endraw %}
