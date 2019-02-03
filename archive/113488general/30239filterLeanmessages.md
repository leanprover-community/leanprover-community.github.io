---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/30239filterLeanmessages.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [filter Lean messages](https://leanprover-community.github.io/archive/113488general/30239filterLeanmessages.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Aug 08 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20Lean%20messages/near/131101820):
<p><span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> it would be nice to add a button next to the "Updating/Stopped" toggle which would allow filtering out certain context lines, especially everything starting with <code>_inst_</code>. Because of mixin classes, I currently work on a proof whose starting context goes up to <code>_inst_24</code>. Very quickly I need to scroll down to see the current goal...</p>

#### [ Patrick Massot (Aug 08 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20Lean%20messages/near/131119745):
<p>An even more aggressive option would be to also filter out <code>.* : Type .*</code></p>

#### [ Patrick Massot (Aug 08 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/filter%20Lean%20messages/near/131119811):
<p>We could have a toggle cycling between default (show every line), filter out instances, filter out instances and types.</p>


{% endraw %}
