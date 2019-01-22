---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/68652HowdoIincreasethememoryconsumptionlimit.html
---

## [new members](index.html)
### [How do I increase the memory consumption limit?](68652HowdoIincreasethememoryconsumptionlimit.html)

#### [Abhimanyu Pallavi Sudhir (Nov 11 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20do%20I%20increase%20the%20memory%20consumption%20limit%3F/near/147477161):
I keep getting "excessive memory consumption" errors in Lean. How can I increase the memory consumption limit? Presumably this is a Lean setting, right?

#### [Abhimanyu Pallavi Sudhir (Nov 11 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20do%20I%20increase%20the%20memory%20consumption%20limit%3F/near/147477225):
From the docs for the extension, it's `lean.memoryLimit` or `-M` but I'm not sure how to use this.

#### [Reid Barton (Nov 11 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20do%20I%20increase%20the%20memory%20consumption%20limit%3F/near/147477291):
Have you built your project (e.g. with `leanpkg build`) recently? The most common reason for running into the memory consumption error is that you don't have up-to-date compiled versions of your dependencies, and so Lean has to do a lot more work every time it processes your file.

#### [Reid Barton (Nov 11 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20do%20I%20increase%20the%20memory%20consumption%20limit%3F/near/147477302):
You may need to restart the Lean server afterwards too

#### [Kevin Buzzard (Nov 11 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20do%20I%20increase%20the%20memory%20consumption%20limit%3F/near/147477359):
Yes -- increasing the memory is ironically probably not the way to solve these errors -- you have maybe got buggy code or you need to compile stuff

#### [Kevin Buzzard (Nov 11 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20do%20I%20increase%20the%20memory%20consumption%20limit%3F/near/147477397):
And whenever you get it you should  restart lean I guess, eg with ctrl shift p lean: restart

#### [Abhimanyu Pallavi Sudhir (Nov 11 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20do%20I%20increase%20the%20memory%20consumption%20limit%3F/near/147477478):
Buggy code isn't the issue, since it works after restarting (albeit after a very long time). As for the installation -- I installed from the binaries you (@**Kevin Buzzard**) uploaded as of October. Is this too old?

#### [Reid Barton (Nov 11 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20do%20I%20increase%20the%20memory%20consumption%20limit%3F/near/147477530):
Are you working on mathlib, or your own project which uses mathlib, or something else?

#### [Abhimanyu Pallavi Sudhir (Nov 11 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20do%20I%20increase%20the%20memory%20consumption%20limit%3F/near/147477754):
A project which uses a local download of mathlib.

#### [Kenny Lau (Nov 11 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20do%20I%20increase%20the%20memory%20consumption%20limit%3F/near/147477914):
`lean --make`

#### [Kenny Lau (Nov 11 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20do%20I%20increase%20the%20memory%20consumption%20limit%3F/near/147477918):
or `leanpkg build`

#### [Kevin Buzzard (Nov 11 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20do%20I%20increase%20the%20memory%20consumption%20limit%3F/near/147480220):
If code takes a long time to run you can try and figure out what's going on by sticking #exit in the code and working out which line is causing the problem. October binaries are fine I'm sure. But there is perhaps a line which is bad style or could be rewritten to solve your problems

