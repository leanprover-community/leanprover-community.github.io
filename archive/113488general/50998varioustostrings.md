---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/50998varioustostrings.html
---

## Stream: [general](index.html)
### Topic: [various to_strings](50998varioustostrings.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Oct 01 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/various%20to_strings/near/134964035):
Hi all, when should I use the following typeclasses to display information?
- `has_repr`
- `has_to_string`
- `has_to_format`
- `has_to_tactic_format` -- the tactic version of `has_to_format`?
In particular, why bother having both `has_repr` and `has_to_string`?
Thanks!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Oct 01 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/various%20to_strings/near/134964119):
Some background: https://github.com/leanprover/lean/issues/1664

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Edward Ayers (Oct 01 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/various%20to_strings/near/134964230):
Ok, so they are exactly the same except with how they deal with chars and strings?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sean Leather (Oct 01 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/various%20to_strings/near/134964311):
```quote
Ok, so they are exactly the same except with how they deal with chars and strings?
```
I suppose so. I haven't looked into it myself.


{% endraw %}
