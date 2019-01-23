---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/37715simptauto.html
---

## Stream: [general](index.html)
### Topic: [simp, tauto](37715simptauto.html)

---


{% raw %}
#### [ Sean Leather (May 31 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%2C%20tauto/near/127356880):
So close and yet so far:

```lean
error: done tactic failed, there are unsolved goals
state:
...
a : b₁ = b₂
⊢ b₂ = b₁
```

#### [ Kevin Buzzard (May 31 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%2C%20tauto/near/127378132):
eq.symm is not a good simp lemma :-)

#### [ Simon Hudon (May 31 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%2C%20tauto/near/127378623):
What is the goal before you call `tauto`?

#### [ Reid Barton (May 31 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%2C%20tauto/near/127379550):
I made a version of `tauto` that calls `cc` (which is how I discovered that `cc` bug I mentioned here a while ago)

#### [ Reid Barton (May 31 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%2C%20tauto/near/127379554):
instead of `done`

#### [ Sean Leather (Jun 01 2018 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%2C%20tauto/near/127401951):
The goal is rather complicated (but seems like it should be automatically solvable), and I don't have it around anymore. The proof doesn't involve `eq.symm`. But I've noticed this same pattern a few times when trying `tauto`. Here's another example that I just tried. It seems that `tauto` can't solve this (which is just `or.inr`)?

```lean
⊢ s ∈ tl → s = hd ∨ s ∈ tl
```


{% endraw %}
