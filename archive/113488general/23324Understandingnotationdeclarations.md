---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/23324Understandingnotationdeclarations.html
---

## Stream: [general](index.html)
### Topic: [Understanding notation declarations](23324Understandingnotationdeclarations.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Brendan Seamas Murphy (Mar 04 2018 at 03:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Understanding%20notation%20declarations/near/123248290):
Hi all! I'm kind of confused about how notation works. I have a setup like this:
```lean
constant SQL : Type
constant groupBy : SQL → SQL → SQL → SQL

notation `SELECT` `*` x := x
notation `FROM1` a := a
notation `SELECT` proj `FROM1`:1 a `GROUP` `BY` v := groupBy proj a v
```
And I can't write `SELECT a FROM1 b GROUP BY c`, I need to write `SELECT (a) FROM1 b GROUP BY c`. I also need the `:1` after `FROM1` to get it to parse at all, and I don't know why.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Mar 04 2018 at 05:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Understanding%20notation%20declarations/near/123250724):
The `:1` is for precedence. If the parser meets `... x + y FROM1` the precedence tells Lean whether to keep reading to the right or to build the `x + y` expression some more with stuff on the left


{% endraw %}
