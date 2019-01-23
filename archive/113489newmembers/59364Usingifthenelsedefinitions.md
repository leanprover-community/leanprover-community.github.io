---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/59364Usingifthenelsedefinitions.html
---

## Stream: [new members](index.html)
### Topic: [Using if-then-else definitions](59364Usingifthenelsedefinitions.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mark Dickinson (Nov 03 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20if-then-else%20definitions/near/137127809):
I'm missing something fundamental. If I've defined a function `ℕ → ℕ` by making use of the if-then-else construct, how do I go about proving anything about that function? For example, given:
```lean
definition nat_max (m n : ℕ) := if m < n then n else m
```
How do I prove something like
```lean
lemma max_right (m n : ℕ) : m < n → nat_max m n = n := sorry
```
? This seems as though it should be trivial, but I'm struggling. `unfold nat_max, by_cases (m < n)`gives me two cases, one of which is an easy contradiction. The other then looks like:
```lean
m n : ℕ,
h : m < n
⊢ m < n → @ite (m < n) (nat.decidable_lt m n) ℕ n m = n
```
and at that point I'm stuck.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 03 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20if-then-else%20definitions/near/137127855):
`rw if_pos h`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mark Dickinson (Nov 03 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20if-then-else%20definitions/near/137127916):
Ah, and `if_pos` was the fundamental thing I was missing. Thank you!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mark Dickinson (Nov 03 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20if-then-else%20definitions/near/137128090):
Meta-question: what's the right way for a newcomer to find out about things like `if_pos`? Is it reasonable to say that any attempt to learn Lean has to include reading through the source of the standard library at some point?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mark Dickinson (Nov 03 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20if-then-else%20definitions/near/137128134):
Though looking at the definition of `if_pos`, I really _should_ have been able to construct it from first principles ...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Nov 03 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20if-then-else%20definitions/near/137128145):
Speaking as another relatively new member, [the naming convention](https://github.com/leanprover/mathlib/blob/master/docs/naming.md) + the VS code extension's "Intellisense" window and then `tactic.find` are usually what I go to first. Then I ask here.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Nov 03 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20if-then-else%20definitions/near/137128147):
Ask on Zulip probably. Usually Ctrl-clicking on `ite` will take you to the file where it was defined, and there'll usually be all the obvious lemmas about it there, but that seems to not be the case this time.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mark Dickinson (Nov 03 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20if-then-else%20definitions/near/137128386):
Thanks, both.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 03 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20if-then-else%20definitions/near/137128585):
This time last year I remember Kenny and I fretting over exactly this question -- a constructor for `ite` -- and I found `if_pos` by grepping through the source code :-)


{% endraw %}
