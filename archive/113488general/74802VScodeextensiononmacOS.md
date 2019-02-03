---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/74802VScodeextensiononmacOS.html
---

## Stream: [general](index.html)
### Topic: [VScode extension on macOS](74802VScodeextensiononmacOS.html)

---


{% raw %}
#### [ Ryan Smith (Oct 04 2018 at 07:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension%20on%20macOS/near/135152447):
<p>Do you need to append your lean/bin directory onto $PATH and then launch vscode from the command line in order for the extension to locate lean on macOS?</p>

#### [ Bryan Gin-ge Chen (Oct 04 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension%20on%20macOS/near/135152540):
<p>I put my elan path into my .bash_profile and then VS code was able to figure out the rest</p>

#### [ Ryan Smith (Oct 04 2018 at 07:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension%20on%20macOS/near/135152787):
<p>On mac or linux?</p>

#### [ Bryan Gin-ge Chen (Oct 04 2018 at 07:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension%20on%20macOS/near/135152852):
<p>On macOS 10.13 until a few days ago and macOS 10.14 since then.</p>

#### [ Bryan Gin-ge Chen (Oct 04 2018 at 07:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension%20on%20macOS/near/135152905):
<p>It's also possible to just put the full path to your lean executable in the lean VS code extension settings and that ought to work as well.</p>

#### [ Ryan Smith (Oct 04 2018 at 07:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension%20on%20macOS/near/135153376):
<p>Invoking lean from the command line as a sanity check produces:<br>
dyld: Library not loaded: /usr/local/opt/gmp/lib/libgmp.10.dylib<br>
  Referenced from: /Users/bixbyr/lean-3.4.1/bin/./lean<br>
  Reason: image not found<br>
Abort trap: 6</p>

#### [ Ryan Smith (Oct 04 2018 at 07:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension%20on%20macOS/near/135153522):
<p>Nvm that looks like a more general brew issue to fix and probably doesn't have anything to do with lean</p>

#### [ Bryan Gin-ge Chen (Oct 04 2018 at 07:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension%20on%20macOS/near/135153538):
<p>yeah, you just need to do <code>brew install gmp</code>. The fact that this isn't stated anywhere obvious is a well-known issue.</p>

#### [ Bryan Gin-ge Chen (Oct 04 2018 at 07:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension%20on%20macOS/near/135153606):
<p><a href="https://github.com/leanprover/lean/issues/1971" target="_blank" title="https://github.com/leanprover/lean/issues/1971">https://github.com/leanprover/lean/issues/1971</a> Supposedly, installing lean itself via homebrew should include gmp</p>

#### [ Ryan Smith (Oct 04 2018 at 07:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension%20on%20macOS/near/135153658):
<p>ah I just installed lean via binary download</p>

#### [ Bryan Gin-ge Chen (Oct 04 2018 at 07:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension%20on%20macOS/near/135153705):
<p>Yeah, I think the current recommended procedure might be to use elan <a href="https://github.com/Kha/elan" target="_blank" title="https://github.com/Kha/elan">https://github.com/Kha/elan</a></p>

#### [ Ryan Smith (Oct 04 2018 at 08:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension%20on%20macOS/near/135153990):
<p>git clone mathlib to include/ or is there a more elegant way to get it and bring it into scope?</p>

#### [ Bryan Gin-ge Chen (Oct 04 2018 at 08:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension%20on%20macOS/near/135154139):
<p>I've been using <code>leanpkg</code> as described <a href="https://xenaproject.wordpress.com/2017/12/02/how-to-install-mathlib-and-keep-it-up-to-date/" target="_blank" title="https://xenaproject.wordpress.com/2017/12/02/how-to-install-mathlib-and-keep-it-up-to-date/">here</a>.</p>

#### [ Bryan Gin-ge Chen (Oct 04 2018 at 08:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension%20on%20macOS/near/135154204):
<p>There's a strong possibility that you'll run into <a href="#narrow/stream/113488-general/subject/leanpkg/near/134435061" title="#narrow/stream/113488-general/subject/leanpkg/near/134435061">this issue</a> if you're running lean 3.4.1.</p>

#### [ Kevin Buzzard (Oct 04 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension%20on%20macOS/near/135162102):
<p>A push was made to document <code>elan</code> properly at <a href="https://github.com/leanprover-community/mathlib/blob/elan-docs/docs/elan.md" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/elan-docs/docs/elan.md">https://github.com/leanprover-community/mathlib/blob/elan-docs/docs/elan.md</a> . If this document does not answer all your questions then please flag this here or even better submit a PR. It's time this was fixed. Sebastian is very busy with Lean 4, but we as a community can definitely make things like this better.</p>

#### [ Bryan Gin-ge Chen (Oct 04 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension%20on%20macOS/near/135187195):
<p>I think <a href="https://github.com/leanprover/mathlib/blob/master/docs/elan.md" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/docs/elan.md">the merged version of that file in mathlib</a> is actually more recent. However, as mentioned <a href="https://github.com/leanprover/mathlib/issues/365" target="_blank" title="https://github.com/leanprover/mathlib/issues/365">here</a> and in the zulip conversation I linked above, Reid pointed out that those instructions won't get you the most recent version of mathlib since mathlib's <code>leanpkg.toml</code> specifies lean 3.4.1 and <code>leanpkg add</code> gives you the lean-3.4.1 branch, which is several months out of date.</p>

#### [ Reid Barton (Oct 04 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension%20on%20macOS/near/135194622):
<p>You can ignore that part of the instructions though and still use the instructions for installing elan</p>

#### [ Bryan Gin-ge Chen (Oct 04 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension%20on%20macOS/near/135195074):
<p>Right. To be fully explicit, I think the instructions should be edited to say something like "If you want to include an up-to-date version of mathlib in your project, use <code>elan install nightly</code> to install the latest version of lean. Then use <code>leanpkg new my-project</code> and <code>leanpkg add &lt;link to mathlib&gt;</code>. Make sure that <code>leanpkg.toml</code> in  <code>my-project</code> has a line saying <code>lean_version = nightly-something</code>. Then run <code>leanpkg upgrade</code>, etc."</p>

#### [ Kevin Sullivan (Oct 08 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension%20on%20macOS/near/135405425):
<p>On OSX, do "brew install gmp"</p>


{% endraw %}
