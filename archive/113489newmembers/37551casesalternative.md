---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/37551casesalternative.html
---

## Stream: [new members](index.html)
### Topic: [cases alternative](37551casesalternative.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sarah Mameche (Dec 18 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/cases%20alternative/near/152139969):
Hi, using ``cases`` on an hypothesis sometimes gives me really huge terms in the resulting hypotheses. It's happened if the hypothesis contains recursive definitions, and I fixed it in one case by marking the definition as ``irreducible``.
However, now I get the same problem for the definition
```lean
def Fin : nat → Type
  | 0 := empty
  | (n+1) := option (Fin n)
```
as soon as I call cases on something like ``x: Fin (n+1)``. In Coq, this goes through, so I guess it has something to do with definitions being compiled to recursors? Is there another way to use cases without unfolding the definition/getting this huge expression? (Marking Fin as irreducible didn't work because I want to match on it in other proofs)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 18 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/cases%20alternative/near/152143374):
Definitions made with the equation compiler in Lean can sometimes come out quite unwieldy. Does it make any difference if you just apply the recursor directly?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Dec 18 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/cases%20alternative/near/152143471):
```lean
def Fin' : nat → Type :=
λ n, nat.rec_on n (empty) (λ n Fn, option Fn)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Dec 18 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/cases%20alternative/near/152143723):
A definition like this one in `number_theory/dioph` is probably easier to use, and gives a similar induction principle
```lean
inductive fin2 : ℕ → Type
| fz {n} : fin2 (succ n)
| fs {n} : fin2 n → fin2 (succ n)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sarah Mameche (Dec 19 2018 at 00:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/cases%20alternative/near/152145711):
That helped, thanks!

