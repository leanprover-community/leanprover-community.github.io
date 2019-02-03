---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/37715simptauto.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [simp, tauto](https://leanprover-community.github.io/archive/113488general/37715simptauto.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Sean Leather (May 31 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%2C%20tauto/near/127356880):
<p>So close and yet so far:</p>
<div class="codehilite"><pre><span></span><span class="n">error</span><span class="o">:</span> <span class="n">done</span> <span class="n">tactic</span> <span class="n">failed</span><span class="o">,</span> <span class="n">there</span> <span class="n">are</span> <span class="n">unsolved</span> <span class="n">goals</span>
<span class="n">state</span><span class="o">:</span>
<span class="bp">...</span>
<span class="n">a</span> <span class="o">:</span> <span class="n">b₁</span> <span class="bp">=</span> <span class="n">b₂</span>
<span class="err">⊢</span> <span class="n">b₂</span> <span class="bp">=</span> <span class="n">b₁</span>
</pre></div>

#### [ Kevin Buzzard (May 31 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%2C%20tauto/near/127378132):
<p>eq.symm is not a good simp lemma :-)</p>

#### [ Simon Hudon (May 31 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%2C%20tauto/near/127378623):
<p>What is the goal before you call <code>tauto</code>?</p>

#### [ Reid Barton (May 31 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%2C%20tauto/near/127379550):
<p>I made a version of <code>tauto</code> that calls <code>cc</code> (which is how I discovered that <code>cc</code> bug I mentioned here a while ago)</p>

#### [ Reid Barton (May 31 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%2C%20tauto/near/127379554):
<p>instead of <code>done</code></p>

#### [ Sean Leather (Jun 01 2018 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%2C%20tauto/near/127401951):
<p>The goal is rather complicated (but seems like it should be automatically solvable), and I don't have it around anymore. The proof doesn't involve <code>eq.symm</code>. But I've noticed this same pattern a few times when trying <code>tauto</code>. Here's another example that I just tried. It seems that <code>tauto</code> can't solve this (which is just <code>or.inr</code>)?</p>
<div class="codehilite"><pre><span></span><span class="err">⊢</span> <span class="n">s</span> <span class="err">∈</span> <span class="n">tl</span> <span class="bp">→</span> <span class="n">s</span> <span class="bp">=</span> <span class="n">hd</span> <span class="bp">∨</span> <span class="n">s</span> <span class="err">∈</span> <span class="n">tl</span>
</pre></div>


{% endraw %}
