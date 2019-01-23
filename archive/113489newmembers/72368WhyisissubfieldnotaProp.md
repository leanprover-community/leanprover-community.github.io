---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/72368WhyisissubfieldnotaProp.html
---

## Stream: [new members](index.html)
### Topic: [Why is is_subfield not a Prop?](72368WhyisissubfieldnotaProp.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Jan 12 2019 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20is%20is_subfield%20not%20a%20Prop%3F/near/154987213):
I want to define
```lean
variables {L : Type}
def subfields : set (set L) := {K' : set L | is_subfield K'}
```
But I run into a problem because `is_subfield` is somehow a `Type`, not a `Prop`. Why is this/how is this possible, and how can I fix the problem?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 12 2019 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20is%20is_subfield%20not%20a%20Prop%3F/near/154987224):
By mistake. It should be changed.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Jan 12 2019 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20is%20is_subfield%20not%20a%20Prop%3F/near/154987515):
Do you know how I can circumvent the problem?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 12 2019 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20is%20is_subfield%20not%20a%20Prop%3F/near/154987518):
you can use `nonempty (is_subfield K')`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Jan 12 2019 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20is%20is_subfield%20not%20a%20Prop%3F/near/154987531):
#588

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Jan 12 2019 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Why%20is%20is_subfield%20not%20a%20Prop%3F/near/154990392):
You can now also just update mathlib :-)


{% endraw %}
