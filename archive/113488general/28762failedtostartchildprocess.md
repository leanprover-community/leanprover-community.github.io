---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/28762failedtostartchildprocess.html
---

## Stream: [general](index.html)
### Topic: [failed to start child process](28762failedtostartchildprocess.html)

---


{% raw %}
#### [ Scott Morrison (Jul 25 2018 at 08:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failed%20to%20start%20child%20process/near/130257139):
<p>I have a student who can't run leanpkg on Windows: <code>leanpkg.bat new test</code> says: "failed to start child process", and doesn't create a new directory.</p>

#### [ Scott Morrison (Jul 25 2018 at 08:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failed%20to%20start%20child%20process/near/130257148):
<p>Has anyone experienced this, and knows the fix?</p>

#### [ Scott Morrison (Jul 25 2018 at 08:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failed%20to%20start%20child%20process/near/130257151):
<p>I know nothing about Windows anymore.</p>

#### [ Johan Commelin (Jul 25 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failed%20to%20start%20child%20process/near/130257829):
<blockquote>
<p>Has anyone experienced this, and knows the fix?</p>
</blockquote>
<p>The fix would obviously be to wipe Windows and install a proper OS.</p>

#### [ Minchao Wu (Jul 25 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failed%20to%20start%20child%20process/near/130260741):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> one of my colleagues has experienced this. The simplest solution would be using Git Bash if Git is installed.</p>

#### [ Kevin Buzzard (Jul 25 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failed%20to%20start%20child%20process/near/130263893):
<p>I've had several problems with git on Windows. There appears to be more than one canonical installation of git.</p>

#### [ Chris Hughes (Jul 25 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failed%20to%20start%20child%20process/near/130265519):
<p>I always get that error if I use the windows command line instead of Msys.</p>

#### [ Kevin Buzzard (Jul 25 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failed%20to%20start%20child%20process/near/130265849):
<p>The mantra I tell Windows users is msys2, git, lean binary, set msys2 path variable so it can see git and leanpkg, then follow instructions in reference manual</p>

#### [ Kevin Buzzard (Jul 25 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failed%20to%20start%20child%20process/near/130265881):
<p>Oh -- and don't put lean in a directory whose full name has a space in</p>

#### [ Scott Morrison (Jul 25 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failed%20to%20start%20child%20process/near/130266683):
<p>We found yet another solution: activate the "Linux Subsystem for Windows", install the "Ubuntu" app, and use <code>elan</code> there. It was incredibly painless and fast (15 minutes?)</p>

#### [ Mario Carneiro (Jul 25 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failed%20to%20start%20child%20process/near/130267031):
<p>really? I've never had much success with WSL</p>

#### [ Olli (Sep 12 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failed%20to%20start%20child%20process/near/133811905):
<p>Any ideas what the "failed to start child process" might be due to? I am on Windows 10 and I get it when trying to use <code>leanpkg</code> for basically anything. I see that it originates in the C++ code base of Lean itself.</p>
<p>I saw some mentions of this issue in the mailing list, where it was mentioned that it occasionally happens, but for me I'm unable to do almost anything with <code>leanpkg</code>, which means I can't use <code>mathlib</code> as far as I can tell.</p>
<p>I might give using WSL a try, although I'm afraid that configuring VSCode might become a pain in that case.</p>

#### [ Olli (Sep 12 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/failed%20to%20start%20child%20process/near/133812101):
<p>I suppose another thing I could try is compiling Lean from source and hoping that that fixes the issue.</p>


{% endraw %}
