---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/72607Useifconditionwithinthenoutput.html
---

## Stream: [new members](index.html)
### Topic: [Use "if" condition within "then" output](72607Useifconditionwithinthenoutput.html)

---

#### [Abhimanyu Pallavi Sudhir (Nov 28 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22if%22%20condition%20within%20%22then%22%20output/near/148749574):
I'm trying to write something like this:

```lean
theorem bob (a : ℕ → ℝ) (rad : ℝ)
(
  hc : ∀ x, -rad < x ∧ x < rad → is_cau_seq abs (λ (n : ℕ), finset.sum (finset.range n) (λ (k : ℕ), a k * x ^ k))
)
(
  f : ℝ → ℝ := λ x, 
  if (hr : - rad < x ∧ x < rad) then
    cau_seq.lim ((⟨λ n, (finset.range n).sum (λ k, a k * x ^ k) , (λ x, hc x hr)   ⟩) : cau_seq ℝ abs)
  else 0
)
: sorry
```
Of course, this doesn't work because I can only put a proposition in the if condition, not a proof -- but shouldn't there be some way of achieving this -- of referring to the condition for the `if` in the output for `then`?

French brackets don't work either because the condition isn't recorded as an assumption at all.

Is this where `dite` comes in?

#### [Reid Barton (Nov 28 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22if%22%20condition%20within%20%22then%22%20output/near/148749758):
try deleting those parentheses?

#### [Reid Barton (Nov 28 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Use%20%22if%22%20condition%20within%20%22then%22%20output/near/148749765):
around `hr : - rad < x ∧ x < rad`

