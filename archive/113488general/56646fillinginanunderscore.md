---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/56646fillinginanunderscore.html
---

## Stream: [general](index.html)
### Topic: [filling in an underscore](56646fillinginanunderscore.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filling%20in%20an%20underscore/near/124374909):
```
import data.fintype
import algebra 

universes u v
-- Chris multiset example

theorem meh {i : ℕ} {n : ℕ} : i < n → i < nat.succ n := λ H, lt.trans H $ nat.lt_succ_self _

theorem miracle (f : ℕ → ℕ)
(d : ℕ)
(Hd :
  ∀ (g : fin d → ℕ),
    (∀ (i : fin d), f (i.val) = g i) → 
      finset.sum (finset.range d) f = finset.sum finset.univ g)
(g : fin (nat.succ d) → ℕ)
(h : ∀ (i : fin (nat.succ d)), f (i.val) = g i)
: finset.sum (finset.range d) f = finset.sum finset.univ (λ (i : fin d), g ⟨i.val, meh i.is_lt⟩)
:= 
let gres : fin d → ℕ := λ (i : fin d), g ⟨i.val, meh i.is_lt⟩ in 
begin
rw Hd gres (λ i, h ⟨i.val,_⟩)
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filling%20in%20an%20underscore/near/124374951):
Lean magically filled in the underscore in the last but one line

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filling%20in%20an%20underscore/near/124374971):
It either guessed that `i<n -> i<succ n`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filling%20in%20an%20underscore/near/124374972):
or proved it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filling%20in%20an%20underscore/near/124374973):
or decided it didn't care if it was true

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filling%20in%20an%20underscore/near/124374979):
Note that the result is proved in the definition of gres

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filling%20in%20an%20underscore/near/124375018):
(gres is the restriction of `g : fin (d+1) -> nat`, to fin d)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Mar 29 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filling%20in%20an%20underscore/near/124375687):
I think it proved it. Looking at the proof term, it used `lt_succ_of_lt`. I didn't know lean could do that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 29 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filling%20in%20an%20underscore/near/124376073):
What triggered that? Is it the `rw` ? I tried to minimise this but didn't get far.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 30 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filling%20in%20an%20underscore/near/124418473):
@**Mario Carneiro** can you clarify what is going on here?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Mar 30 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filling%20in%20an%20underscore/near/124423248):
The `rw` is a confounder here. You could equally well use `exact Hd gres (λ i, h ⟨i.val, _⟩)` to close the goal. Here are some intermediate data points:
```
Hd gres (λ i, _) -- -> looking for proof of ⊢ f (i.val) = gres i
```
```
Hd gres (λ i, h _)
type mismatch at application
  Hd gres (λ (i : fin d), h ?m_1[i])
term
  λ (i : fin d), h ?m_1[i]
has type
  ∀ (i : fin d), f (?m_1[i].val) = g ?m_1[i]
but is expected to have type
  ∀ (i : fin d), f (i.val) = gres i 
```
```
Hd gres (λ i, h ⟨_, _⟩) -- works
```
Lean isn't magically guessing the proof, it's unfolding `gres` and unifying with the enclosed proof

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 31 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filling%20in%20an%20underscore/near/124433011):
Oh I see. The moment I saw rw I thought "I don't understand that tactic properly, maybe it's doing something under the hood,  so I give in"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 31 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filling%20in%20an%20underscore/near/124433012):
But now you tell me exact works I can just debug it myself with `pp.proofs true`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 31 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filling%20in%20an%20underscore/near/124433025):
I used to think of stuff like type class inference and proofs being magicked around was just all part of some magic, it's only now I begin to realise that everything that happens, happens for a really precise reason.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 31 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filling%20in%20an%20underscore/near/124433076):
In some sense I still draw the line at reading `tactic.interactive` (partly because I know it will be incomprehensible).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 31 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filling%20in%20an%20underscore/near/124433093):
but really it's because I feel like "end users" shouldn't have to know anything about a tactic other than what is documented.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filling%20in%20an%20underscore/near/124433142):
```quote
I used to think of stuff like type class inference and proofs being magicked around was just all part of some magic, it's only now I begin to realise that everything that happens, happens for a really precise reason.
```
there is no magic in lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 31 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filling%20in%20an%20underscore/near/124433202):
No, just sufficiently advanced technology.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Mar 31 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filling%20in%20an%20underscore/near/124433205):
which is canonically isomorphic though

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 31 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filling%20in%20an%20underscore/near/124433208):
so I heard

