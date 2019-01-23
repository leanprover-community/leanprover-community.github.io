---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/43871unfoldingrepeatingPi.html
---

## Stream: [new members](index.html)
### Topic: [unfolding repeating Pi](43871unfoldingrepeatingPi.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Jesse Michael Han (Sep 21 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/unfolding%20repeating%20Pi/near/134384020):
hello everyone! i'm trying to define the following inductive datatype: 
```quote
```lean
constant A : Π n : nat, Type

inductive hewwo : Type
  | base : nat → hewwo
  | apply : Π n, A n → sorry
```
```
where the intended type of `apply n f` is `hewwo →` ... `→ hewwo`, repeated `n + 1` times.

I defined the following function:

```quote
```lean
definition repeat_Pi : ℕ → Type u → Type (u + 1)
  | 0 A := A
  | (nat.succ n) A := Π A, repeat_Pi n A
```
```
but Lean complains that the following:
```quote
```lean
inductive hewwo : Type
  | base : nat → hewwo
  | apply : Π n, A n → repeat_Pi n hewwo
```
```
(rightly) has an incorrect return type for `hewwo.apply`.

Is there a way to get Lean to treat `repeat_Pi k A` as being equal to `A -> ... -> A`?

(edit: got rid of `punit` and shifted indexing down by 1)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 21 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/unfolding%20repeating%20Pi/near/134400061):
Is it intended that in:

```lean
...
  | (nat.succ n) A := Π A, repeat_Pi n A
```

you ignore `A` that you get as a parameter?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 21 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/unfolding%20repeating%20Pi/near/134400214):
Sorry, that doesn't fix the issue. 

You may need to reflect the repetition into the definition of `hewwo`:

```lean
inductive hewwo : nat → Type
  | base : nat → hewwo 0
  | apply (n) : A n → hewwo n → hewwo (succ n)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 21 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/unfolding%20repeating%20Pi/near/134403199):
@**Jesse Michael Han** I would just use the uncurried `\Pi n, A n -> (fin n -> hewwo) -> hewwo` instead.
I don't think you can do the thing you were trying to do.

