---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/68737equationcompileranddependenttypes.html
---

## Stream: [general](index.html)
### Topic: [equation compiler and dependent types](68737equationcompileranddependenttypes.html)

---

#### [Patrick Massot (Dec 23 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler%20and%20dependent%20types/near/152434275):
Is there any way to use the equation compiler with a dependent output? The following works (although I wish the proof part could be `by linarith`):
```lean
def euclid : ℕ → { n : ℕ | 0 < n } → ℕ × ℕ
| m n := if h : m < n then 
           (0, m) 
         else 
           have (0 : ℕ) < n, from n.property,
           have m - n < m, by apply nat.sub_lt ; linarith,
           let ⟨q, r⟩ := euclid (m-n) n in ⟨q+1, r⟩
```
But now suppose I want the output type to be `{ p : ℕ × ℕ | m = n*p.1 + p.2 ∧ p.2 < n}`. Is something like this possible? Of course here Lean complains it doesn't know who are `m` and `n`, which will appear only after matching. Of course I also wish I could write `{ (q, r) : ℕ × ℕ | m = n*q + r ∧ r < n}` (or with angle brackets)instead of those ugly `p.1` and `p.2`, but at least this is not blocking.

#### [Patrick Massot (Dec 23 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler%20and%20dependent%20types/near/152434681):
Sorry about this stupid question

#### [Patrick Massot (Dec 23 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler%20and%20dependent%20types/near/152434684):
I can use a Pi type instead

#### [Patrick Massot (Dec 23 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/equation%20compiler%20and%20dependent%20types/near/152434942):
Note for next time I ask: one possible answer is
```lean
def euclid : Π (m : ℕ) (n : { n : ℕ // 0 < n }), {p : ℕ × ℕ // m = n*p.1 + p.2 ∧ p.2 < n}
| m n := if h : m < n then 
           ⟨(0, m), by simp *⟩ 
         else 
           have (0 : ℕ) < n, from n.property,
           have m - n < m, by apply nat.sub_lt ; linarith,
           let ⟨⟨q, r⟩, ⟨H, H'⟩⟩ := euclid (m-n) n in 
             ⟨(q+1, r), 
              ⟨begin
                rw nat.sub_eq_iff_eq_add (le_of_not_lt h) at H,
                simp [H], ring, 
               end, H'⟩⟩
```

