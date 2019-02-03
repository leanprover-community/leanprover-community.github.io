---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/28527bytecode.html
---

## Stream: [general](index.html)
### Topic: [bytecode?](28527bytecode.html)

---


{% raw %}
#### [ Sebastien Gouezel (Oct 17 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bytecode%3F/near/135998701):
<p>In a file with <code>noncomputable theory</code>, I get the trace message</p>
<div class="codehilite"><pre><span></span>failed to generate bytecode for &#39;locally_compact_of_compact&#39;
code generation failed, VM does not have code for &#39;locally_compact_of_compact_nhds&#39;
</pre></div>


<p>What does this mean, and should I worry?</p>

#### [ Bryan Gin-ge Chen (Oct 17 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bytecode%3F/near/135999111):
<p><a href="#narrow/stream/113489-new-members/subject/finsets.2C.20decidable_mem.2C.20and.20filter/near/133708032" title="#narrow/stream/113489-new-members/subject/finsets.2C.20decidable_mem.2C.20and.20filter/near/133708032">I got that message before</a> when I had accidentally labeled a def as a theorem / lemma. Not sure if that applies in your case or not.</p>

#### [ Reid Barton (Oct 17 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bytecode%3F/near/135999119):
<p>Usually it means there is a lemma whose type is not a Prop, yes. In this case it is because I forgot to mark <code>locally_compact_space</code> as a Prop.</p>

#### [ Sebastien Gouezel (Oct 17 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bytecode%3F/near/135999225):
<p>Indeed, it solves the problem. Thanks!</p>

#### [ Johannes Hölzl (Oct 17 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bytecode%3F/near/136000581):
<p>I have a fix for mathlib</p>

#### [ Reid Barton (Oct 18 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/bytecode%3F/near/136006536):
<p>Thanks <span class="emoji emoji-1f44d" title="+1">:+1:</span></p>


{% endraw %}
