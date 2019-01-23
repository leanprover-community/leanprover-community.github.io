---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/30239filterLeanmessages.html
---

## Stream: [general](index.html)
### Topic: [filter Lean messages](30239filterLeanmessages.html)

---


{% raw %}
#### [ Patrick Massot (Aug 08 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20Lean%20messages/near/131101820):
@**Gabriel Ebner** it would be nice to add a button next to the "Updating/Stopped" toggle which would allow filtering out certain context lines, especially everything starting with `_inst_`. Because of mixin classes, I currently work on a proof whose starting context goes up to `_inst_24`. Very quickly I need to scroll down to see the current goal...

#### [ Patrick Massot (Aug 08 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20Lean%20messages/near/131119745):
An even more aggressive option would be to also filter out `.* : Type .*`

#### [ Patrick Massot (Aug 08 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20Lean%20messages/near/131119811):
We could have a toggle cycling between default (show every line), filter out instances, filter out instances and types.


{% endraw %}
