---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/49101NewbquestionnottrueexampleinTPIL.html
---

## Stream: [general](index.html)
### Topic: [Newb question / not-true example in TPIL?](49101NewbquestionnottrueexampleinTPIL.html)

---


{% raw %}
#### [ Ben Weinstein-Raun (Jun 04 2018 at 05:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newb%20question%20/%20not-true%20example%20in%20TPIL%3F/near/127526038):
Hi, I'm a total newb to Lean and to proof assistants generally. I'm working through Chapter 4 of TPIL, and in particular the [example statements in 4.4](https://leanprover.github.io/live/3.4.1/#code=open%20classical%0A%0Avariables%20(%CE%B1%20:%20Type)%20(p%20q%20:%20%CE%B1%20%E2%86%92%20Prop)%0Avariable%20a%20:%20%CE%B1%0Avariable%20r%20:%20Prop%0A%0Aexample%20:%20(%E2%88%83%20x%20:%20%CE%B1,%20r)%20%E2%86%92%20r%20:=%20sorry%0Aexample%20:%20r%20%E2%86%92%20(%E2%88%83%20x%20:%20%CE%B1,%20r)%20:=%20sorry%0Aexample%20:%20(%E2%88%83%20x,%20p%20x%20%E2%88%A7%20r)%20%E2%86%94%20(%E2%88%83%20x,%20p%20x)%20%E2%88%A7%20r%20:=%20sorry%0Aexample%20:%20(%E2%88%83%20x,%20p%20x%20%E2%88%A8%20q%20x)%20%E2%86%94%20(%E2%88%83%20x,%20p%20x)%20%E2%88%A8%20(%E2%88%83%20x,%20q%20x)%20:=%20sorry%0A%0Aexample%20:%20(%E2%88%80%20x,%20p%20x)%20%E2%86%94%20%C2%AC%20(%E2%88%83%20x,%20%C2%AC%20p%20x)%20:=%20sorry%0Aexample%20:%20(%E2%88%83%20x,%20p%20x)%20%E2%86%94%20%C2%AC%20(%E2%88%80%20x,%20%C2%AC%20p%20x)%20:=%20sorry%0Aexample%20:%20(%C2%AC%20%E2%88%83%20x,%20p%20x)%20%E2%86%94%20(%E2%88%80%20x,%20%C2%AC%20p%20x)%20:=%20sorry%0Aexample%20:%20(%C2%AC%20%E2%88%80%20x,%20p%20x)%20%E2%86%94%20(%E2%88%83%20x,%20%C2%AC%20p%20x)%20:=%20sorry%0A%0Aexample%20:%20(%E2%88%80%20x,%20p%20x%20%E2%86%92%20r)%20%E2%86%94%20(%E2%88%83%20x,%20p%20x)%20%E2%86%92%20r%20:=%20sorry%0Aexample%20:%20(%E2%88%83%20x,%20p%20x%20%E2%86%92%20r)%20%E2%86%94%20(%E2%88%80%20x,%20p%20x)%20%E2%86%92%20r%20:=%20sorry%0Aexample%20:%20(%E2%88%83%20x,%20r%20%E2%86%92%20p%20x)%20%E2%86%94%20(r%20%E2%86%92%20%E2%88%83%20x,%20p%20x)%20:=%20sorry). I haven't been able to prove the last two of them, and I'm beginning to suspect that the last one, at least, is actually false.

`example : (∃ x : α, r → p x) ↔ (r → ∃ x : α, p x) := sorry`.

If r is false and α is uninhabited, the left side of this equivalence is false while the right side is true, no?

#### [ Ben Weinstein-Raun (Jun 04 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newb%20question%20/%20not-true%20example%20in%20TPIL%3F/near/127526088):
(sorry if there's a better place to ask this)

#### [ Simon Hudon (Jun 04 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newb%20question%20/%20not-true%20example%20in%20TPIL%3F/near/127526096):
that's the right place to come

#### [ Simon Hudon (Jun 04 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newb%20question%20/%20not-true%20example%20in%20TPIL%3F/near/127526148):
I think you may be right

#### [ Simon Hudon (Jun 04 2018 at 05:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newb%20question%20/%20not-true%20example%20in%20TPIL%3F/near/127526221):
As you say, if `r` is false, the statement reduces to `(∃ x, true) ↔ true` which is another way of saying that `α` is inhabited, which does not seem to be an assumption

#### [ Simon Hudon (Jun 04 2018 at 05:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newb%20question%20/%20not-true%20example%20in%20TPIL%3F/near/127526270):
Sorry, I take it back: I just saw `variable a : α` which means that `α` is inhabited

#### [ Ben Weinstein-Raun (Jun 04 2018 at 05:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newb%20question%20/%20not-true%20example%20in%20TPIL%3F/near/127526272):
oh, wait, there is a line
`variable a : α`
further up; I hadn't noticed this. Is that equivalent to an assumption that α is inhabited?

#### [ Ben Weinstein-Raun (Jun 04 2018 at 05:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newb%20question%20/%20not-true%20example%20in%20TPIL%3F/near/127526273):
ah, yeah, sorry about that

#### [ Simon Hudon (Jun 04 2018 at 05:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newb%20question%20/%20not-true%20example%20in%20TPIL%3F/near/127526274):
No worries

#### [ Ben Weinstein-Raun (Jun 04 2018 at 05:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newb%20question%20/%20not-true%20example%20in%20TPIL%3F/near/127526369):
(also, thanks!)

#### [ Simon Hudon (Jun 04 2018 at 05:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Newb%20question%20/%20not-true%20example%20in%20TPIL%3F/near/127526373):
:smile:  :thumbs_up:


{% endraw %}
