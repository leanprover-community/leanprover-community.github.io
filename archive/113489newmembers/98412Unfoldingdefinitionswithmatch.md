---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/98412Unfoldingdefinitionswithmatch.html
---

## Stream: [new members](index.html)
### Topic: [Unfolding definitions with match](98412Unfoldingdefinitionswithmatch.html)

---


{% raw %}
#### [ Ken Roe (Jul 25 2018 at 01:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Unfolding%20definitions%20with%20match/near/130244220):
I'm trying to prove the following:
```lean
def evv (x :ℕ → ℕ) (y: ℕ):=
    match x y with
    | 0 := tt
    | 1 := ff
    | _ := tt
    end

theorem test: ∀ x (f: ℕ → ℕ), f x=1 → evv f x :=
begin
    intros, unfold evv, ...
end
```
At the point of the "...", I have the following state:

```lean
x : ℕ,
f : ℕ → ℕ,
a : f x = 1
⊢ ↥(evv._match_1 (f x))
```

How do I complete the theorem?

#### [ Ken Roe (Jul 25 2018 at 01:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Unfolding%20definitions%20with%20match/near/130244421):
I was using quotation, however, I would like to find a way to construct the expression without the quotation.

#### [ Kevin Buzzard (Jul 25 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Unfolding%20definitions%20with%20match/near/130244494):
Your theorem is false so it's hard to complete.

#### [ Kevin Buzzard (Jul 25 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Unfolding%20definitions%20with%20match/near/130244551):
```lean
theorem test: ∀ x (f: ℕ → ℕ), f x=1 → evv f x :=
begin
    intros, 
    unfold evv,
    rw a,
    simp only [evv._match_1],
    -- suffices to prove ff 
    sorry
end
```

#### [ Kevin Buzzard (Jul 25 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Unfolding%20definitions%20with%20match/near/130244565):
The arrow business is because you are talking about booleans as if they're propositions, so a coercion is happening.

#### [ Chris Hughes (Jul 25 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Unfolding%20definitions%20with%20match/near/130244705):
It wasn't true so I changed it.
```lean
theorem test: ∀ x (f: ℕ → ℕ), f x=0 → evv f x :=
begin
  intros, 
  unfold evv, 
  rw a,
  exact rfl,
end
```


{% endraw %}
