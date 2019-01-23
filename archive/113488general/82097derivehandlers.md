---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/82097derivehandlers.html
---

## Stream: [general](index.html)
### Topic: [derive handlers](82097derivehandlers.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 31 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/derive%20handlers/near/133148060):
I'm writing a derive handler,  and while testing it on my third example, I get the following error:

```
declaration contains macro with trust-level higher than the one allowed (possible solution: unfold macro, or increase trust-level)
```

But the term that my handler produces contains no macros that I can see (I'm using `expr.fold` to enumerate them). Has anyone seen this before?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 31 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/derive%20handlers/near/133148298):
Update: I checked a part of the derived term which produces `perm_ac` and `ac_app`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Aug 31 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/derive%20handlers/near/133149243):
Update 2: I wrote a tactic `expand_untrusted` that takes care of those macros. It solves the problem. I'm surprised `instance_derive_handler` doesn't do that by default


{% endraw %}
