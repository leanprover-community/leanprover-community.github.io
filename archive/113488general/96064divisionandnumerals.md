---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/96064divisionandnumerals.html
---

## Stream: [general](index.html)
### Topic: [division and numerals](96064divisionandnumerals.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 14 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/division%20and%20numerals/near/151792143):
```lean

-- example : 2 ∣ 4 := ⟨2, rfl⟩ -- fails
/-
invalid constructor ⟨...⟩, 'has_dvd.dvd' is not an inductive type
-/
--example : (2 : ℕ) ∣ 4 := ⟨2,rfl⟩ -- fails
--example : 2 ∣ (4 : ℕ) := ⟨2,rfl⟩ -- fails
example : (2 : ℕ) ∣ (4 : ℕ) := ⟨2,rfl⟩ -- works
--example (a : ℕ) : a ∣ a * 2 := ⟨2,rfl⟩ -- fails
example (a : ℕ) : a ∣ (a * 2 : ℕ) := ⟨2,rfl⟩ -- works
example (a : ℕ) : a ∣ a * (2 : ℕ) := ⟨2,rfl⟩ -- works
```

Why do so many of these fail? In particular the fourth one: why does Lean need to be told that `a * 2` is a nat when it knows `a` is a nat? The type of `has_dvd.dvd` (the notation) is `α → α → Prop` and it is looking straight at two nats when it decides how to deal with what alpha is.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Dec 14 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/division%20and%20numerals/near/151793918):
Now you know why `by exact` is so popular. :smile:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Dec 14 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/division%20and%20numerals/near/151794263):
The reason is that while Lean does know at some point that `|` is the divisibility relation on a commutative semiring defined by `∃ x, ...`; Lean only figures this out too late, after `⟨2, rfl⟩` is elaborated.  It looks like a bug that could be fixed by synthesizing instances before elaborating anonymous constructors.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Dec 14 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/division%20and%20numerals/near/151794284):
In this example, you can also force instances to be synthesized before elaborating the proof by using `lemma` instead of `example`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Dec 14 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/division%20and%20numerals/near/151794384):
(Oh, and `by exact foo` also changes the order in which things are elaborated.  Tactics are called last; this has the effect of elaborating `foo` later than the rest of the term, when typeclass instances, etc. will have hopefully been figured out.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 14 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/division%20and%20numerals/near/151798356):
I now feel like I've asked this question several times. I think it's about time I understood the answer properly. My current understanding of the answer, which I guess I already had when I posted, is "it's all to do with when elaboration occurs". I hadn't realised this one was in the "lemma / example makes a difference" category and I know I've asked at least one of these before.


{% endraw %}
