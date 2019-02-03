---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/74447leanpkgupgradenolongerworking.html
---

## Stream: [general](index.html)
### Topic: [`leanpkg upgrade` no longer working?](74447leanpkgupgradenolongerworking.html)

---


{% raw %}
#### [ Scott Morrison (Jun 03 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60leanpkg%20upgrade%60%20no%20longer%20working%3F/near/127502598):
<p>Since I've switched all my repositories to have <code>lean_version = "3.4.1"</code> in the <code>leanpkg.toml</code> file, it seems that <code>leanpkg upgrade</code> no longer has any effect: that is, commits to downstream repositories aren't pulled.</p>

#### [ Scott Morrison (Jun 03 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60leanpkg%20upgrade%60%20no%20longer%20working%3F/near/127502600):
<p>Did something change?</p>

#### [ Scott Morrison (Jun 03 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60leanpkg%20upgrade%60%20no%20longer%20working%3F/near/127502608):
<p>Can anyone guess what I'm doing wrong? I just want my <code>leanpkg.toml</code> file to be automatically updated to the latest commit of the downstream repos.</p>

#### [ Sebastian Ullrich (Jun 03 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60leanpkg%20upgrade%60%20no%20longer%20working%3F/near/127510205):
<p>leanpkg is looking for a branch <code>lean-3.4.1</code>. You should switch to that from <code>master</code> if you only want to support that version. You should not set stable Lean versions on the <code>master</code> branch.</p>

#### [ Scott Morrison (Jun 04 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60leanpkg%20upgrade%60%20no%20longer%20working%3F/near/127519975):
<p>Okay --- I'm a bit confused. The <code>leanpkg.toml</code> file in <code>mathlib</code> currently says: <code>lean_version = "3.4.1"</code>, so I'd copied that over into my little chain of dependencies. What should the <code>lean_version</code> in my <code>leanpkg.toml</code> files be?</p>

#### [ Sebastian Ullrich (Jun 04 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60leanpkg%20upgrade%60%20no%20longer%20working%3F/near/127533855):
<p>mathlib now keeps the <code>master</code> and a new <code>lean-3.4.1</code> branch in sync, but I'd recommend just moving to the latter altogether <a href="#narrow/stream/113488-general/subject/lean-3.2E4.2E1.20branch/near/127075441" title="#narrow/stream/113488-general/subject/lean-3.2E4.2E1.20branch/near/127075441">https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/lean-3.2E4.2E1.20branch/near/127075441</a></p>

#### [ Scott Morrison (Jun 04 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60leanpkg%20upgrade%60%20no%20longer%20working%3F/near/127535112):
<p>I'm sorry, I still don't understand. What am I meant to do in my repos, so that <code>leanpkg upgrade</code> actually upgrades? Should I set all the <code>lean_version</code> lines back to <code>master</code>?</p>

#### [ Sebastian Ullrich (Jun 04 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60leanpkg%20upgrade%60%20no%20longer%20working%3F/near/127535287):
<p>You should keep <code>lean_version = "3.4.1"</code> but push that as a new branch <code>lean-3.4.1</code> to your repo(s) and use that branch for development against Lean 3.4.1.</p>

#### [ Scott Morrison (Jun 04 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60leanpkg%20upgrade%60%20no%20longer%20working%3F/near/127535465):
<p>ooooh. That hadn't even occurred to me. For lame git-newbs like me, it's so much easier to just do everything in the master branch. (Okay, I think I could cope, but I'm not sure <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> could. :-)</p>

#### [ Sebastian Ullrich (Jun 04 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60leanpkg%20upgrade%60%20no%20longer%20working%3F/near/127535529):
<p>You can set the default branch on Github to the new branch, then there shouldn't be all that much difference</p>

#### [ Johan Commelin (Jun 04 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60leanpkg%20upgrade%60%20no%20longer%20working%3F/near/127535555):
<p>In his book "Lean for the working mathematician", I think Kevin will have to spend the first 30 pages on "Git for the working mathematician".</p>

#### [ Scott Morrison (Jun 15 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60leanpkg%20upgrade%60%20no%20longer%20working%3F/near/128114390):
<p>Is there any possibility of changing the tooling so people can continue developing their repositories on <code>master</code> branches, and still have <code>leanpkg upgrade</code> work?</p>

#### [ Scott Morrison (Jun 15 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60leanpkg%20upgrade%60%20no%20longer%20working%3F/near/128114399):
<p>(Sorry to restart a two week old thread --- for quick context, apparently the advice was that if you want to be able to use <code>leanpkg upgrade</code>, you need to work in a branch called <code>lean-3.4.1</code>.)</p>

#### [ Sebastian Ullrich (Jun 15 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60leanpkg%20upgrade%60%20no%20longer%20working%3F/near/128116038):
<p>Well, Lean 3 is frozen. We can add a <code>branch</code> config field to leanpkg.toml dependencies in Lean 4 so that users can stay on non-canonical branches.</p>


{% endraw %}
