---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/17472funextcongrfailsinconv.html
---

## Stream: [general](index.html)
### Topic: ["funext, congr" fails in conv](17472funextcongrfailsinconv.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 10 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22funext%2C%20congr%22%20fails%20in%20conv/near/133645086):
```lean
import data.finset algebra.big_operators

example (α β) (s : finset α) [comm_monoid β] : s.prod (λ x, s.attach.prod (λ _, (1:β))) = 1 :=
begin
  conv { to_lhs, congr, skip, funext, congr }
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 10 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22funext%2C%20congr%22%20fails%20in%20conv/near/133645096):
```lean
Tactic State

α : Type ?,
β : Type ?,
s : finset α,
_inst_1 : comm_monoid β,
x : α
| finset.prod (finset.attach s) (λ (_x : {x // x ∈ s}), 1)
```

```lean
unify tactic failed, failed to unify
  ?m_1 : finset.prod (finset.attach s) (λ (_x : {x // x ∈ s}), 1) = ?m_2 x
and
  (λ {α : Type ?} {β : Type ?} [_inst_1 : comm_monoid β] (s s_1 : finset α) (e_4 : s = s_1) (f f_1 : α → β)
   (e_5 : f = f_1), congr (congr_arg finset.prod e_4) e_5)
    (finset.attach s)
    ?m_3
    ?m_4
    (λ (_x : {x // x ∈ s}), 1)
    ?m_5
    ?m_6
  : finset.prod (finset.attach s) (λ (_x : {x // x ∈ s}), 1) = finset.prod ?m_3 ?m_5
state:
α : Type ?,
β : Type ?,
s : finset α,
_inst_1 : comm_monoid β,
x : α
⊢ finset.prod (finset.attach s) (λ (_x : {x // x ∈ s}), 1) = ?m_1 x
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 10 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22funext%2C%20congr%22%20fails%20in%20conv/near/133674125):
@**Mario Carneiro**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 15 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22funext%2C%20congr%22%20fails%20in%20conv/near/134001585):
is nobody going to care about this

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Sep 15 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22funext%2C%20congr%22%20fails%20in%20conv/near/134001595):
Hmm, I care a little :-) I would like more tactics inside conv, too :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Sep 15 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22funext%2C%20congr%22%20fails%20in%20conv/near/134001767):
@**Mario Carneiro**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 15 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22funext%2C%20congr%22%20fails%20in%20conv/near/134001871):
There is very little I can do about bugs in `conv`


{% endraw %}
