---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/79634leanhangs.html
---

## Stream: [general](index.html)
### Topic: [lean hangs](79634leanhangs.html)

---


{% raw %}
#### [ Floris van Doorn (Jan 24 2019 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20hangs/near/156737206):
<p>I don't know if there is any place for bug reports for Lean 3, but Lean will hang on these two lines (and start to slowly fill up your memory): </p>
<div class="codehilite"><pre><span></span>notation S`[`:95 ϕ `]`:90 := 0
variables (α : Type) [add_group α]
</pre></div>


<p>(I am not implying that declaring this notation is a good idea)</p>
<p>On a related note: does someone know how to kill <code>lean</code> processes which are spawned by <code>leanpkg build</code> in <code>msys2</code> on Windows? Killing the command with <code>ctrl+C</code> does not kill the Lean processes (which is a problem if they are busy filling up your memory).</p>

#### [ Neil Strickland (Jan 24 2019 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20hangs/near/156757420):
<p>You can use the commands <code>taskkill</code> and/or <code>tasklist</code> under <code>cmd.exe</code>.  Specifically, <code>taskkill /f /fi "imagename eq lean.exe"</code> should do the job.  Or you can open a new <code>msys</code> terminal window and use <code>ps</code> and <code>kill</code> as in Linux.</p>

#### [ Kenny Lau (Jan 24 2019 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20hangs/near/156757477):
<p>I just kill it in Task Manager because it's always the one occupying the most memory</p>


{% endraw %}
