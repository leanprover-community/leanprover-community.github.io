---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/28546provingtrivialfactsabouttypes.html
---

## Stream: [new members](index.html)
### Topic: [proving trivial facts about types](28546provingtrivialfactsabouttypes.html)

---


{% raw %}
#### [ Joseph Corneli (Jan 24 2019 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20trivial%20facts%20about%20types/near/156773638):
<p>I can <code>#check ff</code> but can I <em>prove</em> ff : bool or similar facts?</p>
<p>Let's see:</p>
<div class="codehilite"><pre><span></span><span class="c1">-- works</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">ff</span> <span class="o">:</span> <span class="n">bool</span><span class="o">)</span> <span class="o">:=</span> <span class="n">tt</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">ff</span> <span class="o">:</span> <span class="n">bool</span><span class="o">)</span> <span class="o">:=</span> <span class="n">ff</span>

<span class="c1">-- breaks</span>
<span class="kn">example</span> <span class="o">(</span><span class="mi">1</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="mi">1</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span>

<span class="c1">-- breaks</span>
<span class="kn">theorem</span> <span class="n">ff_is_a_bool</span> <span class="o">:</span> <span class="o">(</span><span class="n">ff</span> <span class="o">:</span> <span class="n">bool</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="err">↥</span><span class="n">ff</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">)</span>
</pre></div>


<p>Oh dear, I am confused again.</p>

#### [ Reid Barton (Jan 24 2019 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20trivial%20facts%20about%20types/near/156774268):
<p>The typing relation is not something you can prove or really talk about at all internal to the system.</p>

#### [ Reid Barton (Jan 24 2019 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20trivial%20facts%20about%20types/near/156774301):
<p>In logic terminology it's a <a href="https://en.wikipedia.org/wiki/Judgment_(mathematical_logic)" target="_blank" title="https://en.wikipedia.org/wiki/Judgment_(mathematical_logic)">judgment</a>, not a proposition.</p>

#### [ Joseph Corneli (Jan 24 2019 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20trivial%20facts%20about%20types/near/156774426):
<p>I guess I can say tautological things like "every bool is a bool"...</p>
<div class="codehilite"><pre><span></span>theorem t (x : bool) : bool := x
</pre></div>

#### [ Joseph Corneli (Jan 24 2019 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20trivial%20facts%20about%20types/near/156774553):
<p>but it's interesting, these type judgments don't live in the hierarchy of types?</p>

#### [ Joseph Corneli (Jan 24 2019 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20trivial%20facts%20about%20types/near/156774707):
<blockquote>
<p>In general, a judgment may be any inductively definable assertion in the metatheory. </p>
</blockquote>
<p>So is Lean's metatheory accessible somewhere?</p>

#### [ Reid Barton (Jan 24 2019 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20trivial%20facts%20about%20types/near/156774974):
<p>Metatheory here means whatever logical framework you are using to define and reason about the formal system (Lean in this case).</p>

#### [ Reid Barton (Jan 24 2019 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20trivial%20facts%20about%20types/near/156774981):
<p>For example, it can just be ordinary informal mathematics.</p>

#### [ Reid Barton (Jan 24 2019 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20trivial%20facts%20about%20types/near/156775246):
<p>For example, you could prove a "unique typing" theorem like "if <code>e : t1</code> and <code>e : t2</code> [are derivable judgments], then <code>t1 = t2</code> [is a derivable judgment]".</p>

#### [ Reid Barton (Jan 24 2019 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20trivial%20facts%20about%20types/near/156775340):
<p>that's a theorem you would prove in an ordinary math paper, probably using induction on the ordinary natural numbers and so on</p>

#### [ Reid Barton (Jan 24 2019 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20trivial%20facts%20about%20types/near/156777001):
<p>I should add that encoding "<code>ff</code> is a <code>bool</code>" as a judgment <code>ff : bool</code> is part of what it means to use type theory as a foundation. In a system based on set theory, for example, <code>ff</code> would be represented by some set and <code>bool</code> would be represented by some other set and <code>ff ∈ bool</code> would be a proposition that you could prove.</p>

#### [ Reid Barton (Jan 24 2019 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20trivial%20facts%20about%20types/near/156777257):
<p><a href="https://github.com/digama0/lean-type-theory/releases" target="_blank" title="https://github.com/digama0/lean-type-theory/releases">https://github.com/digama0/lean-type-theory/releases</a> is Mario's paper on the theory of Lean in particular, though it doesn't have much in the way of background material</p>

#### [ Kevin Buzzard (Jan 24 2019 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20trivial%20facts%20about%20types/near/156779977):
<blockquote>
<p>I guess I can say tautological things like "every bool is a bool"...</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">t</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">bool</span><span class="o">)</span> <span class="o">:</span> <span class="n">bool</span> <span class="o">:=</span> <span class="n">x</span>
</pre></div>


</blockquote>
<p>That's not a theorem. That's a definition of a function t from <code>bool</code> to <code>bool</code>; you can check the type of <code>t</code> to see this. Theorems are terms whose type is <code>Prop</code>.</p>

#### [ Kevin Buzzard (Jan 24 2019 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/proving%20trivial%20facts%20about%20types/near/156780011):
<p>PS if you write <code> ```lean </code> rather than just <code> ``` </code> then you get cool syntax highlighting :-)</p>


{% endraw %}
