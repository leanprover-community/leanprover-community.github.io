---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/37897pathissues.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [path issues?](https://leanprover-community.github.io/archive/113488general/37897pathissues.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Jakob von Raumer (Mar 12 2018 at 13:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/path%20issues%3F/near/123606101):
<p>I'm getting the following error whenever I run lean from the console instead of vscode:</p>
<div class="codehilite"><pre><span></span>/usr/local/lib/lean/library/init/data/default.lean:1:0: error: ambiguous import, it can be &#39;/usr/local/lib/lean/library/init/data/ordering/default.lean&#39; or &#39;/usr/local/lib/lean/library/init/data/ordering.lean&#39;
</pre></div>

#### [ Jakob von Raumer (Mar 12 2018 at 13:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/path%20issues%3F/near/123606102):
<p>Any ideas?</p>

#### [ Jakob von Raumer (Mar 12 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/path%20issues%3F/near/123606162):
<p>Hm, okay, removing <code>/usr/local/lib/lean</code> and re-installing helped</p>

#### [ Sebastian Ullrich (Mar 12 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/path%20issues%3F/near/123606258):
<p>Yeah, this is a known general issue with <code>make install</code>. I don't recommend using it.</p>

#### [ Jakob von Raumer (Mar 12 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/path%20issues%3F/near/123609287):
<p>Because it just doesn't clear the directories?</p>

#### [ Sebastian Ullrich (Mar 12 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/path%20issues%3F/near/123609394):
<p>Yes</p>

#### [ Sebastian Ullrich (Mar 12 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/path%20issues%3F/near/123609406):
<p>And I don't recommend using it because adjusting PATH is so much easier :)</p>


{% endraw %}
