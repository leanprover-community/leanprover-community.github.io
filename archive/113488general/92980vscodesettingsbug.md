---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/92980vscodesettingsbug.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [vscode settings bug](https://leanprover-community.github.io/archive/113488general/92980vscodesettingsbug.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Keeley Hoek (Aug 13 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20settings%20bug/near/132051901):
<p>There is a bug in the vscode plugin where in the "User Settings" panel the default settings for numerical constants like "lean.memoryLimit" are given in inverted commas (e.g. "4096"), when they actually shouldn't be.</p>

#### [ Mario Carneiro (Aug 13 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20settings%20bug/near/132052062):
<p>why is that a problem?</p>

#### [ Mario Carneiro (Aug 13 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20settings%20bug/near/132052114):
<p>are you sure only a number can appear there?</p>

#### [ Mario Carneiro (Aug 13 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20settings%20bug/near/132052152):
<p>i.e. <code>"32M"</code></p>

#### [ Gabriel Ebner (Aug 13 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20settings%20bug/near/132057724):
<p>Both formats (<code>4096</code> and <code>"4096"</code>) work, and no, you can't append a <code>M</code>.</p>

#### [ Gabriel Ebner (Aug 13 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20settings%20bug/near/132057784):
<p>Default value changed to bare number a second ago.</p>

#### [ Keeley Hoek (Aug 16 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20settings%20bug/near/132251465):
<p>(deleted)</p>

#### [ Keeley Hoek (Aug 16 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20settings%20bug/near/132252299):
<p>At least on my computer, using inverted commas gives the vscode error "Incorrect type. Expected 'number'."</p>

#### [ Gabriel Ebner (Aug 16 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20settings%20bug/near/132252469):
<p>It's a warning, and it will probably still work.  Nevertheless, use <code>"lean.memoryLimit": 4096</code>.  Just a bare number.</p>


{% endraw %}
