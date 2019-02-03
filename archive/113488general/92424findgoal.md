---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/92424findgoal.html
---

## Stream: [general](index.html)
### Topic: [#find goal](92424findgoal.html)

---


{% raw %}
#### [ Johan Commelin (May 01 2018 at 07:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23find%20goal/near/125929630):
<p>I occasionally find myself in the situation where I would like to know if there is a theorem that I can apply to the current goal (in tactic mode). It would be nice if I could run a tactic <code>find_goal</code> that does not change the proof state, but just prints messages of the theorems that I could apply. Is this reasonable?</p>

#### [ Reid Barton (May 01 2018 at 07:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23find%20goal/near/125929697):
<p>Interesting idea. But I bet there would be too many theorems that would always apply, like <code>eq.symm</code> or <code>iff.symm</code>. How to reject the uninteresting ones?</p>

#### [ Mario Carneiro (May 01 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23find%20goal/near/125929901):
<p>An idea I have contemplated as a crude relevance filter is measuring the degree to which the target matches the theorem (i.e. how many exact symbol matches before it starts instantiating metavariables). This could be combined with a (harsh?) penalty for the number of new metavariables not in the goal</p>

#### [ Mario Carneiro (May 01 2018 at 07:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23find%20goal/near/125929940):
<p>But the only obvious way I see to implement this is literally to <code>try{apply T}</code> for all T in the environment, so it will be very slow</p>

#### [ Kenny Lau (May 01 2018 at 08:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23find%20goal/near/125931438):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span></p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">find</span>

<span class="kn">open</span> <span class="n">nat</span>

<span class="bp">#</span><span class="n">find</span> <span class="bp">_</span> <span class="bp">+</span> <span class="bp">_</span> <span class="bp">=</span> <span class="bp">_</span> <span class="bp">+</span> <span class="bp">_</span>
</pre></div>


{% endraw %}
