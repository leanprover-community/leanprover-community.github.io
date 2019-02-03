---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/99635customleaninelan.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [custom lean in elan](https://leanprover-community.github.io/archive/113488general/99635customleaninelan.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Reid Barton (Jan 11 2019 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20lean%20in%20elan/near/154915008):
<p>Is there some low-tech way to just copy files in <code>~/.elan</code> around if I want to try running Lean with a modified core library?<br>
Say by <code>cd ~/.elan; cp -a lean-3.4.1 lean-3.4.1a</code>? Probably I need to do something else, as well?</p>

#### [ Gabriel Ebner (Jan 11 2019 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20lean%20in%20elan/near/154915280):
<p>This should work.  You can also add symlinks to a lean git checkout.</p>

#### [ Reid Barton (Jan 11 2019 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20lean%20in%20elan/near/154919876):
<p>It did just work.</p>


{% endraw %}
