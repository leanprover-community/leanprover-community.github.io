---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/13255generalize.html
---

## Stream: [general](index.html)
### Topic: [generalize](13255generalize.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 19 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125297691):
Could someone build a tactic that allows us to generalize at hypotheses?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 20 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125329985):
Can you give an example?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 20 2018 at 07:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125342330):
```lean
example (m n p q : nat) (H : m + n = p) : m + n = q :=
begin
  generalize h : m + n = x at h ⊢,
  guard_hyp h := m + n = x,
  guard_hyp H := x = p,
  guard_target x = q,
  admit
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 20 2018 at 07:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125342331):
@**Simon Hudon**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 20 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125445414):
I see. So it reverts your hypotheses for you. That should be doable. I'll look into it. Any idea what it should be called?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 20 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125445638):
I think one can extend generalize?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 20 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125445648):
i.e. still call it generalize, since it builds upon the current generalize (so there won’t be beackwards compatibility problem)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 20 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125445755):
`generalize` is defined in the core library and they usually don't take pull requests there. We may have to give it a different name and put it in `mathlib`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 20 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125447182):
I’m not sure what I would call it. What do you think?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 20 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125447233):
`generalized_generalize`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Apr 20 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125447264):
Can't you have tactic modifying tactics? Then you could just write `generalize simp` or `generalize wlog` and of course also `generalize generalize`.
Life would be so much `simp`ler.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 20 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125447272):
Or `ageneralize`. `a` for assumption. We can also call it `generalizea` (not to be confused with the Canadian `generalize`, eh?)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 20 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125447334):
some tactics have `generalizing` clauses like `induction xs generalizing h`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 20 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125447851):
(kudos for the hockey stick, @**Sean Leather** :rolling_on_the_floor_laughing: )

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Apr 20 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125447949):
Bienvenue, eh!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 20 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125450421):
I have a truly marvelous idea

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 20 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125450422):
I have a truly marvelous idea

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 20 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125450423):
we can call it `generalise`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 20 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125450448):
You are truly evil, @**Kenny Lau**

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Apr 20 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125452634):
```quote
You are truly evil, @**Kenny Lau**
```
Don't forget we learned this morning that Kenny is nothing but Kevin's evil part.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 20 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125452831):
I wasn't there for that. It all adds up ... his constructivism should really have been a dead give away

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 20 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125452840):
Btw @**Kenny Lau** I just made a pull request with your requested feature:

https://github.com/leanprover/mathlib/pull/110

Let me know if you like it!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 20 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125453447):
@**Simon Hudon** does it work with more than one local hypothesis?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 20 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125453452):
Yes it does

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 20 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125453456):
I like it, thanks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 20 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125453463):
let's test if it works with induction

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 20 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125453469):
could you test if you can generalize a list and then do induction?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 20 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125453519):
Can you show me what you have in mind?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 20 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125453523):
yes, wait a minute

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 20 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125453683):
```lean
example (α : Sort*) (L₁ L₂ L₃ : list α)
  (H : L₁ ++ L₂ = L₃) : L₁ ++ L₂ = L₂ :=
begin
  generalize_a h : L₁ ++ L₂ = L at H,
  induction L with hd tl ih,
  case list.nil
  { guard_hyp H := list.nil = L₃ },
  case list.cons
  { guard_hyp H := hd :: tl = L₃ },
  admit
end
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 20 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125453686):
@**Simon Hudon** there you go

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 20 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125453952):
I had to change it to: 

```
example (α : Sort*) (L₁ L₂ L₃ : list α)
  (H : L₁ ++ L₂ = L₃) : L₁ ++ L₂ = L₂ :=
begin
  generalize_a h : L₁ ++ L₂ = L at H,
  induction L with hd tl ih,
  case list.nil
  { tactic.cleanup,
    change list.nil = L₃ at H,
    admit },
  case list.cons
  { change hd :: tl = L₃ at H,
    admit },
end
```

but it worked

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 20 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125453958):
why?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 20 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125453963):
but thanks

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 20 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125454026):
`guard_hyp` and `guard_target` are fairly intolerant. If your expressions contain meta variables and that they don't match, it will fail. At least, I believe that's the reason

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Apr 20 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125454027):
I see

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 20 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125454034):
And you're welcome :)


{% endraw %}
