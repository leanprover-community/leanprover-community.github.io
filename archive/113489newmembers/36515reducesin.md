---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/36515reducesin.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [reduce sin](https://leanprover-community.github.io/archive/113489newmembers/36515reducesin.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Joseph Corneli (Jan 30 2019 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/reduce%20sin/near/157193193):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">complex</span><span class="bp">.</span><span class="n">exponential</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">exponential</span>

<span class="kn">open</span> <span class="n">real</span>
<span class="bp">#</span><span class="kn">check</span> <span class="n">sin_pi_div_two</span>
<span class="bp">#</span><span class="n">reduce</span> <span class="n">sin</span> <span class="n">pi</span><span class="bp">/</span><span class="mi">2</span>
</pre></div>


<blockquote>
<p>(deterministic) timeout</p>
</blockquote>
<p>Morally speaking, should <code>#reduce sin pi/2</code> work?</p>

#### [ Reid Barton (Jan 30 2019 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/reduce%20sin/near/157193399):
<p>no</p>

#### [ Reid Barton (Jan 30 2019 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/reduce%20sin/near/157193636):
<p>I think the definition of <code>pi</code> is nonconstructive, but even if everything involved was constructive, in the best case this expression would reduce to the equivalence class of some particular Cauchy sequence of rationals, and you still would need to prove a theorem to know whether or not it was equal to 1. (By the way, I guess you mean <code>sin (pi/2)</code>?)</p>

#### [ Joseph Corneli (Jan 30 2019 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/reduce%20sin/near/157194006):
<p>True, I did mean that.</p>

#### [ Kenny Lau (Jan 30 2019 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/reduce%20sin/near/157194149):
<p>I thought you can reduce noncomputable things</p>

#### [ Kenny Lau (Jan 30 2019 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/reduce%20sin/near/157194172):
<p>but you might need to define "work": what output do you expect? an infinite stream of digits?</p>

#### [ Joseph Corneli (Jan 30 2019 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/reduce%20sin/near/157194396):
<p>I would have expected "1" but a stream would be interesting too.</p>

#### [ Reid Barton (Jan 30 2019 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/reduce%20sin/near/157194401):
<p>I agree "work" should be clarified, but in this case, the answer will turn out to be "no" for any reasonable interpretation.</p>

#### [ Johan Commelin (Jan 30 2019 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/reduce%20sin/near/157210893):
<p>Is there some sort of <code>#simp</code>? I imagine that you give it an expression, and it runs the simplifier against it and prints the result.</p>

#### [ Simon Hudon (Jan 30 2019 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/reduce%20sin/near/157211226):
<p>That could be arranged</p>

#### [ Johan Commelin (Jan 30 2019 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/reduce%20sin/near/157211493):
<p>I would imagine that <code>#simp sin (pi/2)</code> would in fact return <code>1</code>. (Provided we have the right simp-lemmas in place.)</p>


{% endraw %}
