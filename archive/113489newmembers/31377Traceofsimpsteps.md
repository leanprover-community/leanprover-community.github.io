---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/31377Traceofsimpsteps.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [Trace of "simp" steps](https://leanprover-community.github.io/archive/113489newmembers/31377Traceofsimpsteps.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Ken Roe (Jul 25 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trace%20of%20%22simp%22%20steps/near/130300149):
<p>I applied "simp" to a complex hypothesis and got an unexpected result.  Is there a way to get a trace of the steps taken by simp?</p>

#### [ Kenny Lau (Jul 25 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trace%20of%20%22simp%22%20steps/near/130300168):
<div class="codehilite"><pre><span></span><span class="kn">set_option</span> <span class="n">trace</span><span class="bp">.</span><span class="n">simp_lemmas</span> <span class="n">true</span>
<span class="kn">set_option</span> <span class="n">trace</span><span class="bp">.</span><span class="n">simplify</span> <span class="n">true</span>
</pre></div>

#### [ Kenny Lau (Jul 25 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trace%20of%20%22simp%22%20steps/near/130300170):
<p>I think it's the second one</p>

#### [ Kenny Lau (Jul 25 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trace%20of%20%22simp%22%20steps/near/130300172):
<p>but why not both</p>

#### [ Reid Barton (Jul 25 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Trace%20of%20%22simp%22%20steps/near/130300213):
<p>trace.simplify.rewrite will show just the successful steps</p>


{% endraw %}
