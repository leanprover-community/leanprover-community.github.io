---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/00411composingtactics.html
---

## Stream: [general](index.html)
### Topic: [composing tactics](00411composingtactics.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 02 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/composing%20tactics/near/127458510):
Suppose I prove a goal using `by repeat {constructor}`. What is the syntax for creating a new def of type `tactic unit` that does the same thing? Do I have to drop down into using the non-interactive tactics?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 02 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/composing%20tactics/near/127458561):
I guess handling the context and goals explicitly in a `do` block isn't so bad, but I was wondering if this is the correct way to do it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Jun 02 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/composing%20tactics/near/127459735):
ahh, figured it out. it's just `interactive.repeat interactive.constructor`. I didn't know about the `itactic` type

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Jun 02 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/composing%20tactics/near/127460627):
1) Go to the definition of `tactic.interactive.repeat`and look how its defined.  I don't know if we have any documentation on how to write interactive tactics beyond the ICFP paper.  Short version: when you use `begin foo bar end`, lean looks for a definition named `tactic.interactive.foo`.  The type of the arguments of `tactic.interactive.foo` determine how the arguments to the tactic are parsed.  For example, `itactic` tells lean to parse a tactic block in curly braces.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Jun 02 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/composing%20tactics/near/127460634):
2) You can use `` `[repeat {constructor}] `` to use interactive tactic syntax outside of begin-end blocks.

