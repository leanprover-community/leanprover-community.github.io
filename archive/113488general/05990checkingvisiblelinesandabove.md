---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/05990checkingvisiblelinesandabove.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [checking visible lines and above](https://leanprover-community.github.io/archive/113488general/05990checkingvisiblelinesandabove.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Jul 11 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20visible%20lines%20and%20above/near/129473320):
<p>Whilst the VS Code option "checking visible lines and above" is probably a useful mode to be in if you're working on a large file, for my users it causes more problems than it solves. I know how to change it to "checking visible files", but every time I open a new folder it changes back. Is there a way to globally change the default once and for all?</p>

#### [ Gabriel Ebner (Jul 11 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20visible%20lines%20and%20above/near/129481006):
<p>There is a setting to change the default.  Open user settings and search for lean to see the configuration options.</p>

#### [ Gabriel Ebner (Jul 11 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20visible%20lines%20and%20above/near/129481027):
<p>Maybe we should change the default as well given the troubles it causes.</p>

#### [ Elliott Macneil (Jul 12 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20visible%20lines%20and%20above/near/129526984):
<p>I'm looking at the user settings to change the default.</p>
<div class="codehilite"><pre><span></span><span class="bp">//</span> <span class="n">Set</span> <span class="n">the</span> <span class="n">default</span> <span class="n">region</span> <span class="n">of</span> <span class="n">interest</span> <span class="n">mode</span> <span class="o">(</span><span class="n">nothing</span><span class="o">,</span> <span class="n">visible</span><span class="o">,</span> <span class="n">lines</span><span class="o">,</span> <span class="n">linesAndAbove</span><span class="o">,</span> <span class="kn">open</span><span class="o">,</span> <span class="n">or</span> <span class="n">project</span><span class="o">)</span> <span class="n">for</span> <span class="n">the</span> <span class="n">Lean</span> <span class="n">extension</span><span class="bp">.</span>
  <span class="s2">&quot;lean.roiModeDefault&quot;</span><span class="o">:</span> <span class="s2">&quot;linesAndAbove&quot;</span><span class="o">,</span>
</pre></div>


<p>It doesn't seem to say what the "checking visible files" option would be - could anyone tell me what that would be?</p>

#### [ Mario Carneiro (Jul 12 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking%20visible%20lines%20and%20above/near/129527279):
<p><code>visible</code> is the visible files option</p>


{% endraw %}
