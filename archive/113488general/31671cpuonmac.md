---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/31671cpuonmac.html
---

## Stream: [general](index.html)
### Topic: [cpu on mac](31671cpuonmac.html)

---


{% raw %}
#### [ Yulia Zaplatina (Aug 13 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cpu%20on%20mac/near/132034358):
<p>Anyone had an issue with lean using &gt; 95% cpu on mac?</p>

#### [ Mario Carneiro (Aug 13 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cpu%20on%20mac/near/132034433):
<p>lean often takes up as much cpu as it can. It depends on what you are doing</p>

#### [ Yulia Zaplatina (Aug 13 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cpu%20on%20mac/near/132034448):
<p>Just opened the workspace</p>

#### [ Mario Carneiro (Aug 13 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cpu%20on%20mac/near/132034604):
<p>If you import a heavy theory, it may take a few minutes</p>

#### [ Mario Carneiro (Aug 13 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cpu%20on%20mac/near/132034617):
<p>You can also try building the lean files with <code>lean --make</code> to help speed it up</p>

#### [ Yulia Zaplatina (Aug 13 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cpu%20on%20mac/near/132034639):
<p>thanks, I'll try</p>

#### [ Kevin Buzzard (Aug 13 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cpu%20on%20mac/near/132034729):
<p>Yulia -- I'll be in the MLC in about an hour. You might want to build your mathlib (make all the .olean files) if this is constantly happening.</p>

#### [ Yulia Zaplatina (Aug 13 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cpu%20on%20mac/near/132034783):
<p>it went down to 20%, but now that i've open</p>

#### [ Yulia Zaplatina (Aug 13 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cpu%20on%20mac/near/132034787):
<p>*opened a file, it's back up to over 300%</p>

#### [ Yulia Zaplatina (Aug 13 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cpu%20on%20mac/near/132034805):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I'll do that now <span class="emoji emoji-1f44d" title="+1">:+1:</span>🏼</p>

#### [ Kevin Buzzard (Aug 13 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cpu%20on%20mac/near/132035136):
<p>This is not abnormal behaviour -- the first time Lean starts up it might have to do a lot of work. It could be building the real numbers from the axioms of mathematics, for example. It only needs to do this once though.</p>

#### [ Yulia Zaplatina (Aug 13 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cpu%20on%20mac/near/132036385):
<p>Ok, so I've built lean and the cpu remains around 90% - is that normal? or is there a way of decreasing it even more?</p>

#### [ Mario Carneiro (Aug 13 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cpu%20on%20mac/near/132036480):
<p>are there yellow bars in the gutter of vscode?</p>

#### [ Yulia Zaplatina (Aug 13 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cpu%20on%20mac/near/132036563):
<p>nope</p>

#### [ Yulia Zaplatina (Aug 13 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cpu%20on%20mac/near/132036614):
<p>only green, blue and red</p>

#### [ Mario Carneiro (Aug 13 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cpu%20on%20mac/near/132036632):
<p>does lean have the <span class="emoji emoji-2705" title="check">:check:</span> in the status bar?</p>

#### [ Yulia Zaplatina (Aug 13 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cpu%20on%20mac/near/132036633):
<p>oh actually, yes, in some files</p>

#### [ Yulia Zaplatina (Aug 13 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cpu%20on%20mac/near/132036698):
<p>yep, there's a <span class="emoji emoji-2705" title="check">:check:</span> but some files are highlighted yellow</p>

#### [ Mario Carneiro (Aug 13 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cpu%20on%20mac/near/132036726):
<p>maybe it would be best to wait for Kevin</p>

#### [ Yulia Zaplatina (Aug 13 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cpu%20on%20mac/near/132036829):
<p>O</p>

#### [ Yulia Zaplatina (Aug 13 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cpu%20on%20mac/near/132036883):
<p>it's down to 10 now <span class="emoji emoji-1f605" title="sweat smile">:sweat_smile:</span> I think it should be fine, thank you!</p>


{% endraw %}
