---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/79962windowsnightlylinkbroken.html
---

## Stream: [general](index.html)
### Topic: [windows nightly link broken](79962windowsnightlylinkbroken.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 08 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/windows%20nightly%20link%20broken/near/123463240):
https://ci.appveyor.com/api/projects/leodemoura/lean/artifacts/build/lean-nightly-windows.zip?branch=master (the usual link to lean nightly windows) doesn't work currently -- I mean the link doens't work, rather than the zip file not compiling.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Mar 09 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/windows%20nightly%20link%20broken/near/123481865):
There are issues with the Windows build infrastructure (as spotted by one of my students last night who was hoping to get the new non-leaky Lean). https://github.com/leanprover/lean reports the build as passing in the readme, the link in the readme seems to report it as failing, and the link at https://leanprover.github.io/download/ to the windows nightly is still failing with the error `{"message":"\"job\" parameter must be specified if build contains multiple jobs.\r\nParameter name: job"}`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Mar 09 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/windows%20nightly%20link%20broken/near/123484446):
The new link is https://ci.appveyor.com/api/projects/leodemoura/lean/artifacts/build/lean-nightly-windows.zip?branch=master&job=Environment%3A%20CFG%3DMINGW64. Hopefully I can deploy the new nightly infrastructure in the next few days so that this won't matter.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 08 2018 at 13:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/windows%20nightly%20link%20broken/near/124795839):
I know Lean is a project not a product, but the link to Windows nightlies on the official download page `https://leanprover.github.io/download/` currently doesn't work for me. I think Sebastian once told me how to fix this but I forgot. The issue is that I simply don't know where any windows nightlies are any more. At `https://github.com/leanprover/lean-nightly/releases` there seems to be no Windows nightlies either. Where, if anywhere, is the current Windows nightly?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/windows%20nightly%20link%20broken/near/124832451):
I just told someone about Lean and they said "it's crap, the windows download doesn't even work". Nice.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 09 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/windows%20nightly%20link%20broken/near/124833114):
@**Kevin Buzzard** I updated the nightlies link to the new releases page... which doesn't help for Windows until AppVeyor get their shit together and enable cron builds for us :angry:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 09 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/windows%20nightly%20link%20broken/near/124835161):
Okay, I've manually triggered a Windows build of the latest nightly

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 09 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/windows%20nightly%20link%20broken/near/124835410):
I don't understand why you need cron for that. Doesn't the commit trigger a build on AppVeyor?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/windows%20nightly%20link%20broken/near/124835423):
That is a fine fix Sebastian. Thanks!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Apr 09 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/windows%20nightly%20link%20broken/near/124835486):
And we're back to having downloads for all three of the OS's supported by Lean. Hooray!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 09 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/windows%20nightly%20link%20broken/near/124835984):
@**Simon Hudon** Sure, but we don't want a release for every single commit

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 09 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/windows%20nightly%20link%20broken/near/124836040):
Ah so you have a daily build that creates the daily, is that it? What do you do if there haven't been any commits since the last time?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Apr 09 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/windows%20nightly%20link%20broken/near/124836093):
Not pushing a build, obviously :smile: . We already need to compare against the previous build for the change log anyway.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Apr 09 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/windows%20nightly%20link%20broken/near/124836574):
Cool :)

