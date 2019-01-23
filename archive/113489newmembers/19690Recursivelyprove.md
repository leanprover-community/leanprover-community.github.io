---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/19690Recursivelyprove.html
---

## Stream: [new members](index.html)
### Topic: [Recursively prove](19690Recursivelyprove.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) AHan (Nov 03 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Recursively%20prove/near/137105029):
Sorry, this might seems to be stupid, but I just can't figure out how to prove the problem inductively....

`lemma add_nat_ge_self {a :  ℕ} (b : ℕ) : a + b ≥ b :=
  match b with
  | 0 := begin simp, apply nat.zero_le end
  | succ n := sorry`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 03 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Recursively%20prove/near/137107106):
In lean we write inductive definitions by pattern matching in the definition itself, not using match blocks like coq

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 03 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Recursively%20prove/near/137107116):
```
lemma add_nat_ge_self {a :  ℕ} : ∀(b : ℕ), a + b ≥ b
| 0 := begin simp, apply nat.zero_le end
| (succ n) := sorry
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 03 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Recursively%20prove/near/137107156):
at the `sorry` you should now have access to `add_nat_ge_self` which you can apply recursively

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Nov 03 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Recursively%20prove/near/137113734):
What Mario wrote is cleaner but I want to point out that the following is probably what you were going for:
```lean
lemma add_nat_ge_self {a :  ℕ} (b : ℕ) : a + b ≥ b :=
  match a, b with
  | a, 0 := begin simp, apply nat.zero_le end
  | a, (nat.succ n) := sorry
  end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 03 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Recursively%20prove/near/137113794):
well if you write it like that you won't be able to fill in the `sorry` because you don't have access to the recursive function

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Nov 03 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Recursively%20prove/near/137114175):
It's there, but it gets a funny name:
```lean
lemma add_nat_ge_self {a :  ℕ} (b : ℕ) : a + b ≥ b :=
match a, b with
| a, 0 := begin simp, apply nat.zero_le end
| a, (nat.succ n) := begin
  refine nat.succ_le_succ _,
  exact _match a n
end
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Nov 03 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Recursively%20prove/near/137114468):
And I guess you only get access to it if you go into tactic mode; i.e. I can't remove the `by exact` below:
```lean
lemma add_nat_ge_self {a :  ℕ} (b : ℕ) : a + b ≥ b :=
match a, b with
| a, 0 := begin simp, apply nat.zero_le end
| a, (nat.succ n) := nat.succ_le_succ (by exact _match a n)
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) AHan (Nov 04 2018 at 04:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Recursively%20prove/near/137140650):
Oh!! Thanks a lot for the explanation!!


{% endraw %}
