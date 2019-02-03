---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/97907classesTypeorProp.html
---

## Stream: [general](index.html)
### Topic: [classes Type or Prop](97907classesTypeorProp.html)

---


{% raw %}
#### [ Reid Barton (Apr 27 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/classes%20Type%20or%20Prop/near/125747081):
<p>Is there any particular reason not to make <code>t2_space</code> and similar classes a Prop?</p>
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">t2_space</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">topological_space</span> <span class="n">α</span><span class="o">]</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">t2</span> <span class="o">:</span> <span class="bp">∀</span><span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="n">x</span> <span class="bp">≠</span> <span class="n">y</span> <span class="bp">→</span> <span class="bp">∃</span><span class="n">u</span> <span class="n">v</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">,</span> <span class="n">is_open</span> <span class="n">u</span> <span class="bp">∧</span> <span class="n">is_open</span> <span class="n">v</span> <span class="bp">∧</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">u</span> <span class="bp">∧</span> <span class="n">y</span> <span class="err">∈</span> <span class="n">v</span> <span class="bp">∧</span> <span class="n">u</span> <span class="err">∩</span> <span class="n">v</span> <span class="bp">=</span> <span class="err">∅</span><span class="o">)</span>
</pre></div>

#### [ Reid Barton (Apr 27 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/classes%20Type%20or%20Prop/near/125747084):
<p>I actually had sort of assumed that a structure with only Prop fields would automatically be a Prop by default.</p>

#### [ Kevin Buzzard (Apr 27 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/classes%20Type%20or%20Prop/near/125747703):
<p>I noticed earlier this week that this wasn't happening</p>

#### [ Kevin Buzzard (Apr 27 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/classes%20Type%20or%20Prop/near/125747761):
<p>As I'm sure you know, if you are defining your own class you can just tell it to be a Prop</p>

#### [ Kevin Buzzard (Apr 27 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/classes%20Type%20or%20Prop/near/125747764):
<p>but that won't help you here</p>

#### [ Reid Barton (Apr 27 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/classes%20Type%20or%20Prop/near/125747940):
<p>I don't really need it to be a Prop, I just tried to use it as a Prop and was surprised when it didn't work, but it's easy enough for me to avoid doing that.</p>

#### [ Reid Barton (Apr 27 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/classes%20Type%20or%20Prop/near/125747991):
<p>I came across this comment later in the same file which makes me think the statuses of these structures are a bit accidental:</p>
<div class="codehilite"><pre><span></span><span class="c">/-</span><span class="cm"> countability axioms</span>

<span class="cm">For our applications we are interested that there exists a countable basis, but we do not need the</span>
<span class="cm">concrete basis itself. This allows us to declare these type classes as `Prop` to use them as mixins.</span>
<span class="cm">-/</span>
</pre></div>

#### [ Reid Barton (Apr 27 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/classes%20Type%20or%20Prop/near/125748028):
<p>(It's followed by a structure which is indeed declared to be a Prop.)</p>

#### [ Mario Carneiro (Apr 27 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/classes%20Type%20or%20Prop/near/125751920):
<p>I think that's a typo. I'll change it</p>


{% endraw %}
