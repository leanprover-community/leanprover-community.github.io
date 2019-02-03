---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/69594Windowsinstaller.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Windows installer](https://leanprover-community.github.io/archive/113488general/69594Windowsinstaller.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Neil Strickland (Jan 14 2019 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Windows%20installer/near/155051937):
<p>I made an attempt at a Windows installer, which you can find (for the moment) at <a href="http://bim.shef.ac.uk/lean/installer.html" target="_blank" title="http://bim.shef.ac.uk/lean/installer.html">http://bim.shef.ac.uk/lean/installer.html</a>.  It installs Git, Elan with nightly, VS Code, and the Lean extension, then it sets up a project directory with mathlib + a few sample files, then it opens that directory in VS Code.  At this stage I would only recommend it to people who already know what they are doing.  The installer does not currently tidy up after itself: it will leave a bunch of stuff in C:\Program Files (x86)\Lean installer, including a log file, so that is a good place to look if something goes wrong.  If you try it, please let me know how it goes.  There is relevant code at <a href="https://github.com/NeilStrickland/lean_installer" target="_blank" title="https://github.com/NeilStrickland/lean_installer">https://github.com/NeilStrickland/lean_installer</a>.</p>


{% endraw %}
