---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/68652HowdoIincreasethememoryconsumptionlimit.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [How do I increase the memory consumption limit?](https://leanprover-community.github.io/archive/113489newmembers/68652HowdoIincreasethememoryconsumptionlimit.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Abhimanyu Pallavi Sudhir (Nov 11 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20do%20I%20increase%20the%20memory%20consumption%20limit%3F/near/147477161):
<p>I keep getting "excessive memory consumption" errors in Lean. How can I increase the memory consumption limit? Presumably this is a Lean setting, right?</p>

#### [ Abhimanyu Pallavi Sudhir (Nov 11 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20do%20I%20increase%20the%20memory%20consumption%20limit%3F/near/147477225):
<p>From the docs for the extension, it's <code>lean.memoryLimit</code> or <code>-M</code> but I'm not sure how to use this.</p>

#### [ Reid Barton (Nov 11 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20do%20I%20increase%20the%20memory%20consumption%20limit%3F/near/147477291):
<p>Have you built your project (e.g. with <code>leanpkg build</code>) recently? The most common reason for running into the memory consumption error is that you don't have up-to-date compiled versions of your dependencies, and so Lean has to do a lot more work every time it processes your file.</p>

#### [ Reid Barton (Nov 11 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20do%20I%20increase%20the%20memory%20consumption%20limit%3F/near/147477302):
<p>You may need to restart the Lean server afterwards too</p>

#### [ Kevin Buzzard (Nov 11 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20do%20I%20increase%20the%20memory%20consumption%20limit%3F/near/147477359):
<p>Yes -- increasing the memory is ironically probably not the way to solve these errors -- you have maybe got buggy code or you need to compile stuff</p>

#### [ Kevin Buzzard (Nov 11 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20do%20I%20increase%20the%20memory%20consumption%20limit%3F/near/147477397):
<p>And whenever you get it you should  restart lean I guess, eg with ctrl shift p lean: restart</p>

#### [ Abhimanyu Pallavi Sudhir (Nov 11 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20do%20I%20increase%20the%20memory%20consumption%20limit%3F/near/147477478):
<p>Buggy code isn't the issue, since it works after restarting (albeit after a very long time). As for the installation -- I installed from the binaries you (<span class="user-mention" data-user-id="110038">@Kevin Buzzard</span>) uploaded as of October. Is this too old?</p>

#### [ Reid Barton (Nov 11 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20do%20I%20increase%20the%20memory%20consumption%20limit%3F/near/147477530):
<p>Are you working on mathlib, or your own project which uses mathlib, or something else?</p>

#### [ Abhimanyu Pallavi Sudhir (Nov 11 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20do%20I%20increase%20the%20memory%20consumption%20limit%3F/near/147477754):
<p>A project which uses a local download of mathlib.</p>

#### [ Kenny Lau (Nov 11 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20do%20I%20increase%20the%20memory%20consumption%20limit%3F/near/147477914):
<p><code>lean --make</code></p>

#### [ Kenny Lau (Nov 11 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20do%20I%20increase%20the%20memory%20consumption%20limit%3F/near/147477918):
<p>or <code>leanpkg build</code></p>

#### [ Kevin Buzzard (Nov 11 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/How%20do%20I%20increase%20the%20memory%20consumption%20limit%3F/near/147480220):
<p>If code takes a long time to run you can try and figure out what's going on by sticking #exit in the code and working out which line is causing the problem. October binaries are fine I'm sure. But there is perhaps a line which is bad style or could be rewritten to solve your problems</p>


{% endraw %}
