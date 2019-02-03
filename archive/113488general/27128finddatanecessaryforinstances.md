---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/27128finddatanecessaryforinstances.html
---

## Stream: [general](index.html)
### Topic: [find data necessary for instances](27128finddatanecessaryforinstances.html)

---


{% raw %}
#### [ Joey van Langen (Jan 09 2019 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/find%20data%20necessary%20for%20instances/near/154708830):
<p>Is there an easy way to find which fields should be provided when defining an instance?<br>
For example making an instance of a ring requires you to fill in a lot of data from different classes and manually going through each class in the hierarchy and finding the names of the respective data is quite some work</p>

#### [ Rob Lewis (Jan 09 2019 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/find%20data%20necessary%20for%20instances/near/154708917):
<p>One method is a hole command, as seen briefly in Mario's coding session yesterday:</p>
<div class="codehilite"><pre><span></span><span class="kn">variable</span> <span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span>
<span class="kn">example</span> <span class="o">:</span> <span class="n">ring</span> <span class="n">α</span> <span class="o">:=</span>
<span class="o">{</span><span class="bp">!</span> <span class="bp">!</span><span class="o">}</span>
</pre></div>


<p>In VSCode, click on the lightbulb and choose "generate a skeleton for the structure."</p>

#### [ Rob Lewis (Jan 09 2019 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/find%20data%20necessary%20for%20instances/near/154708931):
<p>(You'll need the right import, probably mathlib's <code>tactic.interactive</code>, I don't remember.)</p>

#### [ Kevin Buzzard (Jan 09 2019 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/find%20data%20necessary%20for%20instances/near/154708988):
<p>If I type</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">:</span> <span class="n">ring</span> <span class="n">R</span> <span class="o">:=</span>
<span class="o">{</span>

<span class="o">}</span>
</pre></div>


<p>then (in VS Code) in the "problems" window (which I sometimes need to create by "pulling up" near the bottom of VS Code) then I see 15 problems, one for each field I need to create. Does this help?</p>

#### [ Rob Lewis (Jan 09 2019 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/find%20data%20necessary%20for%20instances/near/154708993):
<p>Alternatively, you can just write an empty structure {} and look at the error messages. (What Kevin said.)</p>

#### [ Kevin Buzzard (Jan 09 2019 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/find%20data%20necessary%20for%20instances/near/154709008):
<p>Within the <code>{ }</code> Lean is expecting me to write <code>add := blah</code> etc, and I get a problem for each missing field.</p>

#### [ Kevin Buzzard (Jan 09 2019 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/find%20data%20necessary%20for%20instances/near/154709107):
<p>Rob's import is correct -- I just tried it.</p>

#### [ Joey van Langen (Jan 09 2019 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/find%20data%20necessary%20for%20instances/near/154709132):
<p>Thanks! Is there also a generate skeleton for emacs?</p>

#### [ Reid Barton (Jan 09 2019 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/find%20data%20necessary%20for%20instances/near/154709175):
<p>Yes, move the cursor inside the <code>{! !}</code> and press C-c SPC</p>

#### [ Joey van Langen (Jan 09 2019 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/find%20data%20necessary%20for%20instances/near/154709342):
<p>Not having much succes with the C-c SPC. What should I enter when asked for a hole command?</p>

#### [ Reid Barton (Jan 09 2019 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/find%20data%20necessary%20for%20instances/near/154709443):
<p>If you press tab, one of the options should be "Instance Stub — Generate a skeleton for the structure under construction."</p>

#### [ Reid Barton (Jan 09 2019 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/find%20data%20necessary%20for%20instances/near/154709450):
<p>It requires importing the mathlib module that Rob mentioned</p>


{% endraw %}
