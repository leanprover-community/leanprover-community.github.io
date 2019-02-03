---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/61377importeverything.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [import everything](https://leanprover-community.github.io/archive/113488general/61377importeverything.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Feb 01 2019 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/import%20everything/near/157389923):
<p>should / do we have a test file that imports every file?</p>

#### [ Simon Hudon (Feb 01 2019 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/import%20everything/near/157389990):
<p>Why?</p>

#### [ Kenny Lau (Feb 01 2019 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/import%20everything/near/157390000):
<p>to test for conflict?</p>

#### [ Simon Hudon (Feb 01 2019 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/import%20everything/near/157390078):
<p>You mean declarations with the same name?</p>

#### [ Kenny Lau (Feb 01 2019 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/import%20everything/near/157390087):
<p>right</p>

#### [ Simon Hudon (Feb 01 2019 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/import%20everything/near/157390124):
<p>This is what</p>
<div class="codehilite"><pre><span></span>        - lean --recursive --export=mathlib.txt src/
        - leanchecker mathlib.txt
</pre></div>


<p>accomplishes</p>

#### [ Kenny Lau (Feb 01 2019 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/import%20everything/near/157390130):
<p>oh, neat</p>

#### [ Simon Hudon (Feb 01 2019 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/import%20everything/near/157390197):
<p>Travis does it every time and you can get git to check it when you commit or push a branch</p>

#### [ Simon Hudon (Feb 01 2019 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/import%20everything/near/157390306):
<p>Or, if you know how to build a VS Code feature, you can create a command to run exactly that</p>


{% endraw %}
