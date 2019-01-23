---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/90813Provingbasicinequalitiesofnaturalnumbers.html
---

## Stream: [new members](index.html)
### Topic: [Proving basic inequalities of natural numbers](90813Provingbasicinequalitiesofnaturalnumbers.html)

---


{% raw %}
#### [ Sebastian Zimmer (Oct 13 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20basic%20inequalities%20of%20natural%20numbers/near/135737118):
linarith doesn't seem to be good enough to prove this basic inequality
```lean
lemma simple_order_lemma (k : ℕ) (h1 : k > 0) (h2 : ¬ k > 1) : k = 1 := begin
sorry
end 
```

#### [ Sebastian Zimmer (Oct 13 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20basic%20inequalities%20of%20natural%20numbers/near/135737158):
What's the best way of proving this sort of result?

#### [ Kenny Lau (Oct 13 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20basic%20inequalities%20of%20natural%20numbers/near/135737269):
```lean
import data.nat.basic

lemma simple_order_lemma (k : ℕ) (h1 : k > 0) (h2 : ¬ k > 1) : k = 1 :=
(dec_trivial : ∀ k, k ≤ 1 → k > 0 → k = 1) k (le_of_not_gt h2) h1
```

#### [ Kenny Lau (Oct 13 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20basic%20inequalities%20of%20natural%20numbers/near/135737317):
```lean
lemma simple_order_lemma (k : ℕ) (h1 : k > 0) (h2 : ¬ k > 1) : k = 1 :=
begin
  have h3 := le_of_not_gt h2,
  cases h3 with h3 h3, {refl},
  cases h3, cases h1
end
```

#### [ Sebastian Zimmer (Oct 13 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Proving%20basic%20inequalities%20of%20natural%20numbers/near/135737406):
Thanks, I would have never thought of that first solution.


{% endraw %}
