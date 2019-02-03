---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/59048leanfailingquietly.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [lean failing quietly](https://leanprover-community.github.io/archive/113488general/59048leanfailingquietly.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Mar 06 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20failing%20quietly/near/123370593):
<p>Lean has got worse and worse recently, at least for me. I am sorely tempted to just check out a version from a week or two ago and compile that and use it instead. I have a largeish file open (350 lines) and after Lean: Restart in VS Code I get the orange "compiling" lines and then they just disappear, there are no red failure lines, nothing in lean messages, and lean isn't running any more in the sense that none of my <code>#check</code>s are underlined in green.</p>

#### [ Kevin Buzzard (Mar 06 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20failing%20quietly/near/123370607):
<p>I am getting those memory overflow messages on a regular basis and having to restart</p>

#### [ Kevin Buzzard (Mar 06 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20failing%20quietly/near/123370610):
<p>I appreciate it's super-complex software but it didn't used to be like this</p>

#### [ Kevin Buzzard (Mar 06 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20failing%20quietly/near/123370750):
<p>I am actually missing the overflow messages now I am having to deal with silent failures. I removed all olean files and hopefully things will be a bit better (I thought we did not have to do this any more but it seems to have made some difference).</p>

#### [ Kevin Buzzard (Mar 06 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20failing%20quietly/near/123370760):
<p>Is there any way I can give user feedback about all the overflow errors? They strike all the time.</p>

#### [ Kevin Buzzard (Mar 06 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20failing%20quietly/near/123371413):
<p><code>excessive memory consumption detected at 'replace' (potential solution: increase memory consumption threshold)</code></p>

#### [ Kevin Buzzard (Mar 06 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20failing%20quietly/near/123371418):
<p>that one</p>

#### [ Scott Morrison (Mar 07 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20failing%20quietly/near/123372294):
<p>Have you increased your memory limit, or are you just running with the default? I think most people are running with more than the default.</p>

#### [ Scott Morrison (Mar 07 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20failing%20quietly/near/123372370):
<p>Note that it’s not just the file you have open that affects memory requirements: imports matter too, although I don’t have any sense of the relative memory requirements of stuff loaded from olean files vs processed in this session.</p>

#### [ Scott Morrison (Mar 07 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20failing%20quietly/near/123372428):
<p>Probably the default memory limit in the VS Code and emacs extensions should just be raised, so newcomers don’t get tripped up by this.</p>

#### [ Scott Morrison (Mar 07 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20failing%20quietly/near/123372504):
<p>On the other hand, Lean silently failing is bad news. If you’ve got something that reproducibly causes VS Code’s Lean extension to silently fail, you should 1. Check if <code>lean —make</code> also fails (it may tell you something more informative) 2. Post it here!</p>


{% endraw %}
