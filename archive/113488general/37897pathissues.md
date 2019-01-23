---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/37897pathissues.html
---

## Stream: [general](index.html)
### Topic: [path issues?](37897pathissues.html)

---


{% raw %}
#### [ Jakob von Raumer (Mar 12 2018 at 13:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/path%20issues%3F/near/123606101):
I'm getting the following error whenever I run lean from the console instead of vscode:
```
/usr/local/lib/lean/library/init/data/default.lean:1:0: error: ambiguous import, it can be '/usr/local/lib/lean/library/init/data/ordering/default.lean' or '/usr/local/lib/lean/library/init/data/ordering.lean'
```

#### [ Jakob von Raumer (Mar 12 2018 at 13:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/path%20issues%3F/near/123606102):
Any ideas?

#### [ Jakob von Raumer (Mar 12 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/path%20issues%3F/near/123606162):
Hm, okay, removing `/usr/local/lib/lean` and re-installing helped

#### [ Sebastian Ullrich (Mar 12 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/path%20issues%3F/near/123606258):
Yeah, this is a known general issue with `make install`. I don't recommend using it.

#### [ Jakob von Raumer (Mar 12 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/path%20issues%3F/near/123609287):
Because it just doesn't clear the directories?

#### [ Sebastian Ullrich (Mar 12 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/path%20issues%3F/near/123609394):
Yes

#### [ Sebastian Ullrich (Mar 12 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/path%20issues%3F/near/123609406):
And I don't recommend using it because adjusting PATH is so much easier :)


{% endraw %}
