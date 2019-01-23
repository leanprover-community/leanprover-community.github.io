---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/67899existsdata.html
---

## Stream: [general](index.html)
### Topic: [exists data](67899existsdata.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 24 2018 at 06:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20data/near/152455922):
Is there a clean way to avoid the `, true` in this condition?
```lean
def generate_sieve (c : covering_family U) : covering_family U :=
{ V : over U | ∃ (Ui : over U) (hUi : Ui ∈ c) (f : V ⟶ Ui), true }
```
I guess I should use `nonempty`? Somehow, that doesn't feel clean to me, and in the past I found it harder to use.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 24 2018 at 07:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20data/near/152456610):
that's `nonempty`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Dec 24 2018 at 07:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20data/near/152456613):
`{ V : over U | ∃ Ui ∈ c, nonempty (V ⟶ Ui) }`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 24 2018 at 07:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/exists%20data/near/152456723):
Ok, I'll try using it again.


{% endraw %}
