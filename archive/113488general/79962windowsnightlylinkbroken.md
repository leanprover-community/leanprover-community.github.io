---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/79962windowsnightlylinkbroken.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [windows nightly link broken](https://leanprover-community.github.io/archive/113488general/79962windowsnightlylinkbroken.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Mar 08 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/windows%20nightly%20link%20broken/near/123463240):
<p><a href="https://ci.appveyor.com/api/projects/leodemoura/lean/artifacts/build/lean-nightly-windows.zip?branch=master" target="_blank" title="https://ci.appveyor.com/api/projects/leodemoura/lean/artifacts/build/lean-nightly-windows.zip?branch=master">https://ci.appveyor.com/api/projects/leodemoura/lean/artifacts/build/lean-nightly-windows.zip?branch=master</a> (the usual link to lean nightly windows) doesn't work currently -- I mean the link doens't work, rather than the zip file not compiling.</p>

#### [ Kevin Buzzard (Mar 09 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/windows%20nightly%20link%20broken/near/123481865):
<p>There are issues with the Windows build infrastructure (as spotted by one of my students last night who was hoping to get the new non-leaky Lean). <a href="https://github.com/leanprover/lean" target="_blank" title="https://github.com/leanprover/lean">https://github.com/leanprover/lean</a> reports the build as passing in the readme, the link in the readme seems to report it as failing, and the link at <a href="https://leanprover.github.io/download/" target="_blank" title="https://leanprover.github.io/download/">https://leanprover.github.io/download/</a> to the windows nightly is still failing with the error <code>{"message":"\"job\" parameter must be specified if build contains multiple jobs.\r\nParameter name: job"}</code></p>

#### [ Sebastian Ullrich (Mar 09 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/windows%20nightly%20link%20broken/near/123484446):
<p>The new link is <a href="https://ci.appveyor.com/api/projects/leodemoura/lean/artifacts/build/lean-nightly-windows.zip?branch=master&amp;job=Environment%3A%20CFG%3DMINGW64" target="_blank" title="https://ci.appveyor.com/api/projects/leodemoura/lean/artifacts/build/lean-nightly-windows.zip?branch=master&amp;job=Environment%3A%20CFG%3DMINGW64">https://ci.appveyor.com/api/projects/leodemoura/lean/artifacts/build/lean-nightly-windows.zip?branch=master&amp;job=Environment%3A%20CFG%3DMINGW64</a>. Hopefully I can deploy the new nightly infrastructure in the next few days so that this won't matter.</p>

#### [ Kevin Buzzard (Apr 08 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/windows%20nightly%20link%20broken/near/124795839):
<p>I know Lean is a project not a product, but the link to Windows nightlies on the official download page <code>https://leanprover.github.io/download/</code> currently doesn't work for me. I think Sebastian once told me how to fix this but I forgot. The issue is that I simply don't know where any windows nightlies are any more. At <code>https://github.com/leanprover/lean-nightly/releases</code> there seems to be no Windows nightlies either. Where, if anywhere, is the current Windows nightly?</p>

#### [ Kevin Buzzard (Apr 09 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/windows%20nightly%20link%20broken/near/124832451):
<p>I just told someone about Lean and they said "it's crap, the windows download doesn't even work". Nice.</p>

#### [ Sebastian Ullrich (Apr 09 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/windows%20nightly%20link%20broken/near/124833114):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I updated the nightlies link to the new releases page... which doesn't help for Windows until AppVeyor get their shit together and enable cron builds for us <span class="emoji emoji-1f620" title="angry">:angry:</span></p>

#### [ Sebastian Ullrich (Apr 09 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/windows%20nightly%20link%20broken/near/124835161):
<p>Okay, I've manually triggered a Windows build of the latest nightly</p>

#### [ Simon Hudon (Apr 09 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/windows%20nightly%20link%20broken/near/124835410):
<p>I don't understand why you need cron for that. Doesn't the commit trigger a build on AppVeyor?</p>

#### [ Kevin Buzzard (Apr 09 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/windows%20nightly%20link%20broken/near/124835423):
<p>That is a fine fix Sebastian. Thanks!</p>

#### [ Kevin Buzzard (Apr 09 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/windows%20nightly%20link%20broken/near/124835486):
<p>And we're back to having downloads for all three of the OS's supported by Lean. Hooray!</p>

#### [ Sebastian Ullrich (Apr 09 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/windows%20nightly%20link%20broken/near/124835984):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> Sure, but we don't want a release for every single commit</p>

#### [ Simon Hudon (Apr 09 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/windows%20nightly%20link%20broken/near/124836040):
<p>Ah so you have a daily build that creates the daily, is that it? What do you do if there haven't been any commits since the last time?</p>

#### [ Sebastian Ullrich (Apr 09 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/windows%20nightly%20link%20broken/near/124836093):
<p>Not pushing a build, obviously <span class="emoji emoji-1f604" title="smile">:smile:</span> . We already need to compare against the previous build for the change log anyway.</p>

#### [ Simon Hudon (Apr 09 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/windows%20nightly%20link%20broken/near/124836574):
<p>Cool :)</p>


{% endraw %}
