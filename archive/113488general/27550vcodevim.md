---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/27550vcodevim.html
---

## Stream: [general](index.html)
### Topic: [vcode vim](27550vcodevim.html)

---


{% raw %}
#### [ Patrick Massot (Sep 20 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vcode%20vim/near/134311142):
@**Gabriel Ebner** I'm trying to use the vim extension together with the VScode extension. I also enjoy being able to use comma instead of \. But then something really weird happens. If I type comma and then enter then it gets expanded to a subscript zero instead of creating a new line. Of course I can type TAB first (which is also a great recent addition). Can you reproduce this bug?

#### [ Patrick Massot (Sep 20 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vcode%20vim/near/134314287):
Actually this has nothing to do with the vim extension! I modified too many parameters at the same time. Simply setting a different leader key gives the bug.

#### [ Gabriel Ebner (Sep 21 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vcode%20vim/near/134346161):
So backslash+newline gives a newline?  That's strange.  Please file a bug.  I'll look into it when I'm back in Vienna.


{% endraw %}
