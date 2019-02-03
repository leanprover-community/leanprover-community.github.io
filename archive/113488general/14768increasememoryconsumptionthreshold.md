---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/14768increasememoryconsumptionthreshold.html
---

## Stream: [general](index.html)
### Topic: [increase memory consumption threshold](14768increasememoryconsumptionthreshold.html)

---


{% raw %}
#### [ Kevin Buzzard (Aug 02 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/increase%20memory%20consumption%20threshold/near/130780966):
<p>Someone is trying to use Lean on a Win 7 machine here and we're constantly running into memory issues. Lean suggests "increase memory consumption threshold" -- is this something which is possible to do and which might actually work? It's a Windows 7 machine using <code>.olean</code> files which were built on Windows 10 :-/ but that's only because none of us are using Win7 so we can't make the .olean files for Win7.</p>

#### [ Kevin Buzzard (Aug 02 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/increase%20memory%20consumption%20threshold/near/130781134):
<p>Every third time we hit <code>Lean : restart</code> we get away with it :-)</p>

#### [ Kenny Lau (Aug 02 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/increase%20memory%20consumption%20threshold/near/130781144):
<p>go to task manager and look at memory consumption?</p>

#### [ Reid Barton (Aug 02 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/increase%20memory%20consumption%20threshold/near/130781228):
<p>That sometimes means Lean thinks it needs to rebuild things</p>

#### [ Gabriel Ebner (Aug 02 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/increase%20memory%20consumption%20threshold/near/130791589):
<p>1) As <span class="user-mention" data-user-id="110032">@Reid Barton</span> said, try <code>leanpkg build</code> first.  2) In vscode, go to user settings (ctrl+shift+p user settings), and search for lean. <span class="emoji emoji-263a" title="smile">:smile:</span></p>

#### [ Kevin Buzzard (Aug 02 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/increase%20memory%20consumption%20threshold/near/130791671):
<p>It didn't look unreasonable. I initially felt like we were on the boundary of what the machine was capable of, but it didn't make much sense because the machine had 16 gigs of ram and it never got filled up. Maybe it's the dodgy .olean files (and the fact that they were zipped up from some other computer and I'm not sure the timestamps would have survived -- I don't know anything about Windows timestamps).</p>

#### [ Kevin Buzzard (Aug 02 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/increase%20memory%20consumption%20threshold/near/130791708):
<p>I don't think I can run <code>leanpkg build</code> -- I didn't try, but the machine did not have git and I didn't have admin privileges and I think that in the past this has been enough to stop the build from working -- it fails right at the start before trying to build anything. That was the root of the problem.</p>

#### [ Reid Barton (Aug 02 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/increase%20memory%20consumption%20threshold/near/130791965):
<p>The default limit is a mere 1GB, so it makes sense that you did not see the machine's memory fill up.<br>
My guess is also a timestamp issue.</p>

#### [ Reid Barton (Aug 02 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/increase%20memory%20consumption%20threshold/near/130791987):
<p>When lean is invoked by the editor, does it write out <code>.olean</code> files for modules it compiles?</p>

#### [ Reid Barton (Aug 02 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/increase%20memory%20consumption%20threshold/near/130791991):
<p>My impression is that it does not</p>

#### [ Reid Barton (Aug 02 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/increase%20memory%20consumption%20threshold/near/130792165):
<p>It's also easy to accidentally modify a mathlib source file (especially if you are using jump-to-definition) and that also tends to cause this behavior.</p>

#### [ Gabriel Ebner (Aug 02 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/increase%20memory%20consumption%20threshold/near/130793805):
<blockquote>
<p>I don't think I can run <code>leanpkg build</code> -- I didn't try, but the machine did not have git </p>
</blockquote>
<p>You can also do <code>lean --make</code></p>


{% endraw %}
