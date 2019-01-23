---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/47853inductionmissingconstraint.html
---

## Stream: [new members](index.html)
### Topic: [induction missing constraint](47853inductionmissingconstraint.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Etienne Laurin (Sep 01 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/induction%20missing%20constraint/near/133180811):
Given `(a b : ℕ) (h : a ≤ b)`, after doing `induction h`, the `case less_than_or_equal.refl` doesn't have any hypothesis allowing to conclude `a = b`. Why not? Is there another way to perform induction that does introduce `a = b` in that case?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 01 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/induction%20missing%20constraint/near/133180865):
in the refl case, you should already have `b` replaced by `a` in the goal

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 01 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/induction%20missing%20constraint/near/133180929):
By the way, I don't recommend doing induction on an le hypothesis. Instead, do induction on `a` and/or `b` and use lemmas on le to satisfy the induction hypothesis

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Etienne Laurin (Sep 01 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/induction%20missing%20constraint/near/133181092):
What if a and b are expressions? In this example, the goal is still `a ≤ b`
```
example (a b : ℕ) (h : nat.succ a ≤ nat.succ b) : a ≤ b := begin
  induction h,
  case nat.less_than_or_equal.refl { sorry }
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 01 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/induction%20missing%20constraint/near/133181104):
use cases instead for that

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 01 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/induction%20missing%20constraint/near/133181150):
If you need to combine induction with the parameter equalities, you should first use `generalize h : nat.succ a` with all the variables you are holding fixed in the induction, then use `induction`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Etienne Laurin (Sep 01 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/induction%20missing%20constraint/near/133181412):
Thanks, that seems to work

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Etienne Laurin (Sep 01 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/induction%20missing%20constraint/near/133181414):
 I haven't used a lot of explicit lemmas so far, I often have trouble finding the right one. I usually get by with a lot of unfold/delta/induction/cases followed by simp

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 01 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/induction%20missing%20constraint/near/133181437):
That's not very sustainable. I suggest learning to browse the source files of core lib and/or mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Etienne Laurin (Sep 01 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/induction%20missing%20constraint/near/133181486):
I recently discovered M-. will jump to lean and mathlib sources, I'll start using it more

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 01 2018 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/induction%20missing%20constraint/near/133181487):
autocompletion also helps for discoverability, once you learn the naming convention

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Etienne Laurin (Sep 01 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/induction%20missing%20constraint/near/133181653):
Oh nice. But I notice that doesn't work too well if I haven't imported the right theory. Is there a better way to find lemmas than grep?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 01 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/induction%20missing%20constraint/near/133181720):
`#find` might be helpful for you. But I would definitely recommend (a) learning the rules of thumb for lemma names and (b) the ctrl-space dance for auto-completion. If you're trying to prove something about int then just import `data.int.basic`


{% endraw %}
