---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/29660leanpkgtakesforeveronWindows.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [leanpkg takes forever on Windows](https://leanprover-community.github.io/archive/113488general/29660leanpkgtakesforeveronWindows.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Jul 19 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20takes%20forever%20on%20Windows/near/129937135):
<p>I just typed <code>leanpkg init</code> on Windows, and it sat there for around a minute before saying "you meant <code>leanpkg init name_of_package</code> so please start again". I just typed <code>leanpkg init my_package</code> and in the time it took me to write this the Windows machine still hasn't finished mulling over this command. I've seen this several times before on Windows. What's going on?</p>

#### [ Mario Carneiro (Jul 19 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20takes%20forever%20on%20Windows/near/129937894):
<p>probably lean core files aren't compiled</p>

#### [ Kevin Buzzard (Jul 19 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20takes%20forever%20on%20Windows/near/129944576):
<p>They seem to be -- this was from the most recent nightly and there was a bunch of .olean files where there should be..</p>

#### [ Kevin Buzzard (Jul 19 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/leanpkg%20takes%20forever%20on%20Windows/near/129944633):
<p>(I mean in <code>lib</code> with the <code>.lean</code> files)</p>


{% endraw %}
