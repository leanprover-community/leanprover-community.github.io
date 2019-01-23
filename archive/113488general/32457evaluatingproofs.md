---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/32457evaluatingproofs.html
---

## Stream: [general](index.html)
### Topic: [evaluating proofs?](32457evaluatingproofs.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 12 2018 at 02:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/evaluating%20proofs%3F/near/151495074):
@**Mario Carneiro** I think you said that it is possible to evaluate proofs... do you have an example? can we also break proof irrelevance? maybe have an unsound but computable `non-classical.some`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 12 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/evaluating%20proofs%3F/near/151495093):
the axiom of choice is definitely nonconstructive

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 12 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/evaluating%20proofs%3F/near/151495102):
You can evaluate proofs by using `#reduce`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 12 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/evaluating%20proofs%3F/near/151495105):
```quote
the axiom of choice is definitely nonconstructive
```
 even unsound?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 12 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/evaluating%20proofs%3F/near/151495107):
no...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 12 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/evaluating%20proofs%3F/near/151495151):
wait, I don't think I understand what you are asking

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 12 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/evaluating%20proofs%3F/near/151495165):
it's easy to compute a value if you are allowed to be wrong

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 12 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/evaluating%20proofs%3F/near/151495173):
so I want a function that `reduce`s to `0` when given the input `(⟨0, rfl⟩ : ∃ n, n = n)`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 12 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/evaluating%20proofs%3F/near/151495179):
Not in the VM

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 12 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/evaluating%20proofs%3F/near/151495180):
```lean
#reduce (⟨0, rfl⟩ : ∃ n, n = n) -- Exists.intro 0 (eq.refl 0)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 12 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/evaluating%20proofs%3F/near/151495182):
why not?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 12 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/evaluating%20proofs%3F/near/151495187):
because that term has no representation in the VM

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 12 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/evaluating%20proofs%3F/near/151495190):
it is a neutral value, a "unit"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 12 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/evaluating%20proofs%3F/near/151495232):
so `reduce` is not VM?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 12 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/evaluating%20proofs%3F/near/151495233):
no

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 12 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/evaluating%20proofs%3F/near/151495235):
it is kernel reduction

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Dec 12 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/evaluating%20proofs%3F/near/151495236):
interesting

