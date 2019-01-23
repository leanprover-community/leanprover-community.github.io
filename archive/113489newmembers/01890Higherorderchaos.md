---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/01890Higherorderchaos.html
---

## Stream: [new members](index.html)
### Topic: [Higher order chaos](01890Higherorderchaos.html)

---


{% raw %}
#### [ Ken Roe (Jul 15 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129679786):
I was experimenting with lambda reductions.  Can someone help me complete the following theorem:

```lean
theorem testit: (∃ x, ((λ (f : (ℕ → ℕ)), (λ (x:ℕ), (f x)+(f x)))
                         (λ (x:ℕ), x+1)) x = 1) → 3=4 :=
begin
    intro, cases a,sorry
end
```

What should replace the "sorry"?

#### [ Mario Carneiro (Jul 15 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129680026):
here's a proof:
```
theorem testit: (∃ x, ((λ (f : (ℕ → ℕ)), (λ (x:ℕ), (f x)+(f x)))
                         (λ (x:ℕ), x+1)) x = 1) → 3=4 :=
begin
    intro, cases a,
    dsimp at a_h,
    rw [add_assoc, add_left_comm 1] at a_h,
    cases a_h
end

#### [ Kevin Buzzard (Jul 15 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129696201):
Here's a more fleshed-out argument:

```lean
theorem testit: (∃ x, ((λ (f : (ℕ → ℕ)), (λ (x:ℕ), (f x)+(f x)))
                         (λ (x:ℕ), x+1)) x = 1) → 3=4 :=
begin
    intro, cases a with n Hn, -- name the hypotheses
    exfalso, -- we're going to prove by contradiction
    change (n + 1) + (n + 1) = 1 at Hn, -- instead of dsimp do the definitional rewrite yourself
    rw ←add_assoc at Hn, -- Hn now n + 1 + n + 1 = 1
    rw ←add_right_comm n at Hn, -- Hn now (n + n) + 1 + 1 = 1
    have H₂ := nat.succ.inj Hn, -- H₂ now (n+n)+1=0
    exact nat.succ_ne_zero _ H₂,
end
```

#### [ Kenny Lau (Jul 15 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129696426):
```lean
theorem testit: (∃ x, ((λ (f : (ℕ → ℕ)), (λ (x:ℕ), (f x)+(f x)))
                         (λ (x:ℕ), x+1)) x = 1) → 3=4 :=
λ ⟨x, h⟩, nat.cases_on x
  (λ H, nat.no_confusion $ nat.succ_inj H)
  (λ n H, nat.no_confusion $ nat.succ_inj H) h

theorem testit': (∃ x, ((λ (f : (ℕ → ℕ)), (λ (x:ℕ), (f x)+(f x)))
                         (λ (x:ℕ), x+1)) x = 1) → 3=4 :=
λ ⟨x, h⟩, by cases x; from nat.no_confusion (nat.succ_inj h)

theorem testit'': (∃ x, ((λ (f : (ℕ → ℕ)), (λ (x:ℕ), (f x)+(f x)))
                         (λ (x:ℕ), x+1)) x = 1) → 3=4
| ⟨0, h⟩ := nat.no_confusion (nat.succ_inj h)
```

#### [ Patrick Massot (Jul 15 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129696429):
Now let's go for a more mathlib version:
```lean
import tactic.ring

theorem testit: (∃ x, ((λ (f : (ℕ → ℕ)), (λ (x:ℕ), (f x)+(f x)))
                         (λ (x:ℕ), x+1)) x = 1) → 3=4 :=
begin
    rintro ⟨n, Hn⟩, -- name the hypotheses
    by_contradiction, -- we're going to prove by contradiction
    change (n + 1) + (n + 1) = 1 at Hn, -- instead of dsimp do the definitional rewrite yourself
    rw (show (n + 1) + (n + 1) = 2*n+2, by ring) at Hn,
    have H₂ := nat.succ.inj Hn, -- H₂ now 2*n+1=0
    exact nat.succ_ne_zero _ H₂,
end
```

#### [ Kenny Lau (Jul 15 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129696430):
I believe my last version would be the mathlib version :P

#### [ Patrick Massot (Jul 15 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129696469):
I meant using mathlib tactics. Note the use of `rintro` to squash Kevin's first two lines into one, and the use of `ring` for the computation

#### [ Kenny Lau (Jul 15 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129696475):
obfuscated version:
```lean
theorem testit'': (∃ x, ((λ (f : (ℕ → ℕ)), (λ (x:ℕ), (f x)+(f x)))
                         (λ (x:ℕ), x+1)) x = 1) → 3=4
| ⟨0, h⟩ := congr_arg ((+)2) h.symm
```

#### [ Patrick Massot (Jul 15 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129696476):
I also replaced `exfalso` by `by_contradiction`. Here it buys you nothing but it's more powerful in general, so let's remember that one.

#### [ Mario Carneiro (Jul 15 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129696584):
I prefer:
```
theorem testit'': (∃ x, ((λ (f : (ℕ → ℕ)), (λ (x:ℕ), (f x)+(f x)))
                         (λ (x:ℕ), x+1)) x = 1) → 3=4
| ⟨0, h⟩ := by cases h
```

#### [ Kenny Lau (Jul 15 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129696589):
nice

#### [ Mario Carneiro (Jul 15 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129696590):
the match against `0` at the beginning is clever

#### [ Mario Carneiro (Jul 15 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129696631):
(but of course none of these is the mathlib version because the statement is ridiculous)

#### [ Patrick Massot (Jul 15 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129696640):
Again, my "mathlib version" story was only about rewriting Kevin's proof in the same spirit but using more mathlib power

#### [ Patrick Massot (Jul 15 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129696642):
Anyway, hopefully Ken will be able to learn many things from this discussion

#### [ Mario Carneiro (Jul 15 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129696702):
I think lean golf is a nice way to learn new tricks, although its actual applicability is debatable

#### [ Patrick Massot (Jul 15 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129696706):
Actually I'd like to be sure I understand your trick. You let the equation compiler do the job of checking that 0 is the only possibility for x, right?

#### [ Kenny Lau (Jul 15 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129696717):
```lean
import logic.basic

theorem testit: (∃ x, ((λ (f : (ℕ → ℕ)), (λ (x:ℕ), (f x)+(f x)))
                         (λ (x:ℕ), x+1)) x = 1) → 3=4 :=
by simp; intros x H; cases H
```

#### [ Mario Carneiro (Jul 15 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129696756):
Right. The equation compiler figures out a sequence of case splits that produce the cases that I give. Since I wrote `0` instead of `n` for the first thing, it deduces that we have a case split on the nat, but that requires a second branch, for `<succ n, h>`. But here `h` has a type like `succ stuff = 0`, so it does a second case split on `h` and deduces that this case is impossible

#### [ Patrick Massot (Jul 15 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129696763):
Ok, this is what I thought. Well done, equation compiler!

#### [ Mario Carneiro (Jul 15 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129696803):
I like to take advantage of this for doing things like pattern matching on `l : list A` and `h : length l = 2` and only providing a case for `[a, b], _`

#### [ Kenny Lau (Jul 15 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129696805):
```lean
theorem testit: (∃ x, ((λ (f : (ℕ → ℕ)), (λ (x:ℕ), (f x)+(f x)))
                         (λ (x:ℕ), x+1)) x = 1) → 3=4 :=
λ ⟨x, H⟩, by simp at H; cases H
```

#### [ Kevin Buzzard (Jul 15 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129696815):
I like the way that the title of this thread was once a bit of an overstatement but has now become true. Something here for everyone now :-)

#### [ Kevin Buzzard (Jul 15 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129697094):
```quote
Actually I'd like to be sure I understand your trick. 
```
I'm still struggling with the `cases a_h` line in the very first proof :rolling_on_the_floor_laughing:

`cases` seems to be much more powerful than I'd realised. Applied to `n + (n + (1 + 1)) = 1` it realises that both nats are `succ (something)` so reduces to `succ (n+n)=0` and then tries again, realises that the nats are made with different constructors this time, and solves the goal. At least that's my understanding of what's going on.

#### [ Kevin Buzzard (Jul 15 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129697236):
```quote
```lean
theorem testit: (∃ x, ((λ (f : (ℕ → ℕ)), (λ (x:ℕ), (f x)+(f x)))
                         (λ (x:ℕ), x+1)) x = 1) → 3=4 :=
λ ⟨x, H⟩, by simp at H; cases H
```
```
You lose a point for proof instability

#### [ Kevin Buzzard (Jul 15 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129697237):
When Leo removes `add_assoc` from simp you're in trouble

#### [ Kenny Lau (Jul 15 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129697238):
you sound like Mario

#### [ Kevin Buzzard (Jul 15 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129697240):
I'm practising.

#### [ Kenny Lau (Jul 15 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129697246):
```lean
theorem testit: (∃ x, ((λ (f : (ℕ → ℕ)), (λ (x:ℕ), (f x)+(f x)))
                         (λ (x:ℕ), x+1)) x = 1) → 3=4 :=
λ ⟨x, H⟩, by cases x; injections
```

#### [ Kevin Buzzard (Jul 15 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129697293):
```lean
theorem testit4: (∃ x, ((λ (f : (ℕ → ℕ)), (λ (x:ℕ), (f x)+(f x)))
                         (λ (x:ℕ), x+1)) x = 1) → 3=4 
| ⟨0, H⟩ := by injections 
```

#### [ Mario Carneiro (Jul 15 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129697294):
yes, `cases` basically has `injection` built in

#### [ Kevin Buzzard (Jul 15 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129697296):
I don't think I'd internalised that before.

#### [ Mario Carneiro (Jul 15 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129697336):
That's what makes doing cases on an inductive predicate so powerful (like Coq's `inversion` tactic)

#### [ Mario Carneiro (Jul 15 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129697339):
because it can skip all the cases where the indices don't match up

#### [ Kevin Buzzard (Jul 15 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129697344):
That's funny, because last week my son discovered this. IIRC `inversion` is introduced in Software Foundations well after `cases` and in Lean you can just do cases anyway. I think that when I did those exercises in Lean myself I was still at the "let's try `cases;simp` and see if it works" stage.

#### [ Kevin Buzzard (Jul 15 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Higher%20order%20chaos/near/129697434):
In my experiments trying to understand `cases` on `eq` I found that it could be used to do a rewrite for either the left or the right hand side (`cases a = blah` and `cases blah = a` both remove `a` and substitute `blah` everywhere). The only disconcerting thing is that the order of the hypotheses gets randomised a bit (presumably because they're reverted and then unreverted under the hood or something)


{% endraw %}
