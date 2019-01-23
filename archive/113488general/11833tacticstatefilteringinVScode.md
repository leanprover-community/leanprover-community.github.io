---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/11833tacticstatefilteringinVScode.html
---

## Stream: [general](index.html)
### Topic: [tactic state filtering in VS code](11833tacticstatefilteringinVScode.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Dec 29 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20state%20filtering%20in%20VS%20code/near/152706091):
Recently, a Lean user "ratmice" requested [a feature for the VS code extension](https://github.com/leanprover/vscode-lean/issues/100) which could show/hide variables beginning with `_` from the tactic state in the info view. @**Patrick Massot** suggested that a general filtering feature could be useful. So, I threw together [a "tactic state filtering" PR](https://github.com/leanprover/vscode-lean/pull/101) for the VS code extension. Currently the PR adds a dropdown menu to the info view window which displays a customizable list of filters which can be applied (either "positively" or "negatively") to the tactic state. 

While this does the job, I think it might not be too hard to make the filtering more interactive, e.g. so that you could click on x's next to particular items in the tactic state to hide them. See the PR thread for a more specific proposal. I'd like to get more feedback before I write more code. What would you like to see from a "filtering" feature?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Dec 31 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tactic%20state%20filtering%20in%20VS%20code/near/154073154):
This sounds really good. I can't currently test it... but this is is something I've wished for quite a long time.


{% endraw %}
