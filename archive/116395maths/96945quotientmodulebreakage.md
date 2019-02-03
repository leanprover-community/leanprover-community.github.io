---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/96945quotientmodulebreakage.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [quotient_module breakage](https://leanprover-community.github.io/archive/116395maths/96945quotientmodulebreakage.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Sep 20 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134325716):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">set</span><span class="bp">.</span><span class="n">basic</span>
<span class="kn">import</span> <span class="n">linear_algebra</span><span class="bp">.</span><span class="n">quotient_module</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">(</span><span class="n">S</span> <span class="o">:</span> <span class="n">set</span> <span class="n">R</span><span class="o">)</span> <span class="o">[</span><span class="n">ring</span> <span class="n">S</span><span class="o">]</span> <span class="o">:</span> <span class="n">S</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">exact</span> <span class="o">(</span><span class="mi">4</span> <span class="o">:</span> <span class="n">S</span><span class="o">)</span>
<span class="kn">end</span>

<span class="c">/-</span><span class="cm"></span>

<span class="cm">maximum class-instance resolution depth has been reached (the limit can be increased by setting option &#39;class.instance_max_depth&#39;) (the class-instance resolution trace can be visualized by setting option &#39;trace.class_instances&#39;)</span>
<span class="cm">state:</span>
<span class="cm">R : Type ?,</span>
<span class="cm">S : set R,</span>
<span class="cm">_inst_1 : ring ↥S</span>
<span class="cm">⊢ ↥S</span>

<span class="cm">-/</span>
</pre></div>


<p>What is going on here? If I remove the import of <code>linear_algebra.quotient_module</code> then this compiles fine. <span class="user-mention" data-user-id="110044">@Chris Hughes</span> you thought about quotient module instances maybe -- do you know how to diagnose these things?</p>
<p>Related -- I have to ask here because I cannot diagnose the issue myself.  I cannot read the <code>trace.class_instances</code> output and I would really love to be able to. For what it's worth, just before it chokes it looks like this gist (and it's quite funny, manifestly something has gone wrong and it's a nice change from the usual, it's not a loop, it's a recursive hell).</p>
<p><a href="https://gist.github.com/kbuzzard/2582db6593c7b7467f3e0020909af467" target="_blank" title="https://gist.github.com/kbuzzard/2582db6593c7b7467f3e0020909af467">https://gist.github.com/kbuzzard/2582db6593c7b7467f3e0020909af467</a></p>

#### [ Patrick Massot (Sep 20 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134325803):
<p>nice picture</p>

#### [ Patrick Massot (Sep 20 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134325866):
<p>Could you give a more realistic example?</p>

#### [ Patrick Massot (Sep 20 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134325879):
<p>Is R actually a ring and S a subring?</p>

#### [ Chris Hughes (Sep 20 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134325883):
<p>I don't understand why that would compile. If S is empty, it's trivial to get a contradiction from this.</p>

#### [ Patrick Massot (Sep 20 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134325972):
<p>Also note I had to modify stuff like this recently in the perfectoid project</p>

#### [ Mario Carneiro (Sep 20 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134326401):
<p>There's nothing wrong with the statement of the theorem. It is a set with a ring structure, which is therefore nonempty and has a <code>4</code></p>

#### [ Mario Carneiro (Sep 20 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134326574):
<p>As usual, modules are acting up because of the search for a ring instance</p>

#### [ Kevin Buzzard (Sep 20 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134326633):
<p>Chris : you're happy with <code>(x : nat) (h : x &gt; 4)</code>, right? But if x was 2 it's trivial to get a contradiction from this.</p>

#### [ Mario Carneiro (Sep 20 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134326662):
<p>As long as it's a nonempty set there is a ring structure on it and a <code>4</code></p>

#### [ Mario Carneiro (Sep 20 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134326675):
<p>and being a ring implies it is nonempty</p>

#### [ Kevin Buzzard (Sep 20 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134326693):
<p>Patrick -- it was trying to fix up the perfectoid project which led me to this. We need p in R^o for the definition to be OK. The statement that p divides something in R is vacuous because p is a unit in R -- R is like Q_p and R^o is like Z_p</p>

#### [ Mario Carneiro (Sep 20 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134326712):
<p>I don't think the offending instances are in <code>quotient_module</code>. Do you get the same problem with <code>algebra.pi_instances</code> and <code>algebra.module</code>?</p>

#### [ Mario Carneiro (Sep 20 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134326777):
<p>anyway this is yet another problem that will be solved by my refactor</p>

#### [ Kevin Buzzard (Sep 20 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134326801):
<p>OK, I can definitely wait. I was planning on spending tomorrow thinking about the perfectoid project in a top-down way; this issue came up because the definition of a perfectoid ring is currently broken :-)</p>

#### [ Kevin Buzzard (Sep 20 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134327608):
<p>I'm having a day off real life tomorrow; my last day off for a while.</p>

#### [ Patrick Massot (Sep 20 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134331345):
<blockquote>
<p>Patrick -- it was trying to fix up the perfectoid project which led me to this. We need p in R^o for the definition to be OK. The statement that p divides something in R is vacuous because p is a unit in R -- R is like Q_p and R^o is like Z_p</p>
</blockquote>
<p>I told you to carefully review that PR. I fixed the compilation error but I was really unsure I didn't change the maths</p>

#### [ Patrick Massot (Sep 20 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134331353):
<blockquote>
<p>I'm having a day off real life tomorrow; my last day off for a while.</p>
</blockquote>
<p>Do you mean you'll have a Lean day or a no-Lean day?</p>

#### [ Patrick Massot (Sep 20 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134331541):
<blockquote>
<p>anyway this is yet another problem that will be solved by my refactor</p>
</blockquote>
<p>Do you have any estimation about when this refactor will be ready for use?</p>

#### [ Kevin Buzzard (Sep 20 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134331826):
<p>I am going to have a Lean day, but it's a bit cheeky -- I should really be doing other things.</p>

#### [ Patrick Massot (Sep 20 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134331861):
<p>Do you have stuff you can do without modules? Do you want to have fun with uniform spaces?</p>

#### [ Kevin Buzzard (Sep 20 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134331952):
<p>ha ha, I have been working from the bottom up during the little time I've had over the last month or so. I was going to try defining the presheaf on Spa(A), sorrying whatever I couldn't do.</p>

#### [ Patrick Massot (Sep 20 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134331983):
<p>Great!</p>

#### [ Patrick Massot (Sep 20 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/quotient_module%20breakage/near/134331986):
<p>It gets my vote</p>


{% endraw %}
