---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/60330localrecursivefunction.html
---

## Stream: [general](index.html)
### Topic: [local recursive function](60330localrecursivefunction.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Sep 14 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20recursive%20function/near/133958735):
Can you define a recursive function with a `let` inside a `do` block (in a `meta` definition)?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Sep 14 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20recursive%20function/near/133962580):
No

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Sep 14 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20recursive%20function/near/133962812):
Well, you could write a meta `fix`, but that's still not very ergonomical

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 14 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20recursive%20function/near/133964819):
```lean
meta def foo (n : ℕ) : option ℕ :=
do let m : ℕ :=
  match n with
  | 0     := 1
  | (n+1) := by exact _match n + _match n
  end,
return m
 
#eval foo 4 -- some 16

```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Chris Hughes (Sep 14 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20recursive%20function/near/133964837):
I had to do `by exact` for some reason

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Sep 14 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/local%20recursive%20function/near/133964901):
Now that's just terrible :P


{% endraw %}
