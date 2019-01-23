---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/69594Windowsinstaller.html
---

## Stream: [general](index.html)
### Topic: [Windows installer](69594Windowsinstaller.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Neil Strickland (Jan 14 2019 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Windows%20installer/near/155051937):
I made an attempt at a Windows installer, which you can find (for the moment) at http://bim.shef.ac.uk/lean/installer.html.  It installs Git, Elan with nightly, VS Code, and the Lean extension, then it sets up a project directory with mathlib + a few sample files, then it opens that directory in VS Code.  At this stage I would only recommend it to people who already know what they are doing.  The installer does not currently tidy up after itself: it will leave a bunch of stuff in C:\Program Files (x86)\Lean installer, including a log file, so that is a good place to look if something goes wrong.  If you try it, please let me know how it goes.  There is relevant code at https://github.com/NeilStrickland/lean_installer.

