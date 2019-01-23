---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/92980vscodesettingsbug.html
---

## Stream: [general](index.html)
### Topic: [vscode settings bug](92980vscodesettingsbug.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Aug 13 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20settings%20bug/near/132051901):
There is a bug in the vscode plugin where in the "User Settings" panel the default settings for numerical constants like "lean.memoryLimit" are given in inverted commas (e.g. "4096"), when they actually shouldn't be.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 13 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20settings%20bug/near/132052062):
why is that a problem?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 13 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20settings%20bug/near/132052114):
are you sure only a number can appear there?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Aug 13 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20settings%20bug/near/132052152):
i.e. `"32M"`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Aug 13 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20settings%20bug/near/132057724):
Both formats (`4096` and `"4096"`) work, and no, you can't append a `M`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Aug 13 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20settings%20bug/near/132057784):
Default value changed to bare number a second ago.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Aug 16 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20settings%20bug/near/132251465):
(deleted)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Aug 16 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20settings%20bug/near/132252299):
At least on my computer, using inverted commas gives the vscode error "Incorrect type. Expected 'number'."

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Aug 16 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20settings%20bug/near/132252469):
It's a warning, and it will probably still work.  Nevertheless, use `"lean.memoryLimit": 4096`.  Just a bare number.


{% endraw %}
