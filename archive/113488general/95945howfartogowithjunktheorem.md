---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/95945howfartogowithjunktheorem.html
---

## Stream: [general](index.html)
### Topic: [how far to go with junk theorem](95945howfartogowithjunktheorem.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 14 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20far%20to%20go%20with%20junk%20theorem/near/147692754):
If `noncomputable definition nth_root (x : ℝ) (n : ℕ) : ℝ :=
exp (log x / n)` then because log of a non-positive real is explicitly defined to be zero (log going out of its way to not ask for positivity there), we have that
```lean
lemma nth_root_pow_left' {x : ℝ} {m n : ℕ} (Hn : 0 < n) : --(Hm : 0 < m) (Hx : 0 < x) :
(nth_root x (m * n)) ^ n = nth_root x m := sorry
```
happens to be true for all m and x. However to prove the result for `x <= 0` I would like to use the fact that if `x <= 0` then `log x = 0`. Should this be a named lemma, even though it's a junk theorem? I can't find it.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Nov 14 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20far%20to%20go%20with%20junk%20theorem/near/147692769):
Am I supposed to put the effort in to prove the result for `x<=0` even though nobody will ever need this case?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20far%20to%20go%20with%20junk%20theorem/near/147695777):
yes to both questions

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20far%20to%20go%20with%20junk%20theorem/near/147695835):
If you use the fact at least once, there should be a theorem describing "out of domain" behavior of a totalized function (although in general we want to limit the number of such theorems)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Nov 14 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20far%20to%20go%20with%20junk%20theorem/near/147695912):
and if it eliminates a hypothesis you should use "out of domain" behavior of functions in the proof


{% endraw %}
