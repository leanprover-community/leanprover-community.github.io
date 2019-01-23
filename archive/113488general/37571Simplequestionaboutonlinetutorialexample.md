---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/37571Simplequestionaboutonlinetutorialexample.html
---

## Stream: [general](index.html)
### Topic: [Simple question about online tutorial example](37571Simplequestionaboutonlinetutorialexample.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) M. Andrew Moshier (May 20 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simple%20question%20about%20online%20tutorial%20example/near/126819103):
The following from the online Lean tutorial (Lean 2) doesn't work as is in Lean 3. I figured out that I needed to change underscores in the tutorial into inaccessibles in the mutual theorem. Fine. But I still don't see how to prove `not_odd_zero`.

```
mutual inductive even, odd
with even : ℕ → Prop
| even_zero : even 0
| even_succ : ∀ n, odd n → even (n + 1)
with odd : ℕ → Prop
| odd_succ : ∀ n, even n → odd (n + 1)

open even odd

theorem not_odd_zero : ¬ (odd 0). 
 
mutual theorem even_of_odd_succ, odd_of_even_succ
with even_of_odd_succ : ∀ n, odd (n + 1) → even n
| .(n) (odd_succ n h) := h
with odd_of_even_succ : ∀ n, even (n + 1) → odd n
| .(n) (even_succ n h) := h
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 20 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simple%20question%20about%20online%20tutorial%20example/near/126819111):
that works for me in 3.4.1

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (May 20 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simple%20question%20about%20online%20tutorial%20example/near/126819197):
There is also no need for the mutual theorem, since the proof is non-recursive. This works too:
```
theorem even_of_odd_succ : ∀ n, odd (n + 1) → even n
| .(n) (odd_succ n h) := h

theorem odd_of_even_succ : ∀ n, even (n + 1) → odd n
| .(n) (even_succ n h) := h
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) M. Andrew Moshier (May 20 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Simple%20question%20about%20online%20tutorial%20example/near/126836719):
I know it doesn't need to be mutual. This is lifted as is (except the change to inaccessibles) from the tutorial. My vscode is using 3.2.x; Emacs is using 3.4.x.  I'll fix that. Thanks.

