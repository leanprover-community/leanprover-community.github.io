---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/29488unfoldlocaldefinitions.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [unfold local definitions](https://leanprover-community.github.io/archive/113488general/29488unfoldlocaldefinitions.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Reid Barton (May 10 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfold%20local%20definitions/near/126372867):
<p>Is there a way in tactic mode to unfold something bound by a surrounding <code>let</code>?</p>

#### [ Reid Barton (May 10 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfold%20local%20definitions/near/126373312):
<p>I guess I also want to do a beta reduction, since the thing I want to unfold is a function whose definition is <code>assume x, ...</code></p>

#### [ Gabriel Ebner (May 10 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfold%20local%20definitions/near/126373507):
<p>You can do <code>dsimp [x]</code> if <code>x</code> is the let-binding in the local context.</p>

#### [ Gabriel Ebner (May 10 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfold%20local%20definitions/near/126373529):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="k">let</span> <span class="n">x</span> <span class="o">:=</span> <span class="mi">5</span> <span class="k">in</span> <span class="n">x</span> <span class="bp">+</span> <span class="n">x</span> <span class="bp">&gt;</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">intro</span> <span class="n">x</span><span class="o">,</span>
<span class="n">dsimp</span> <span class="o">[</span><span class="n">x</span><span class="o">],</span>
<span class="c1">-- 5 + 5 &gt; 0</span>
<span class="kn">end</span>
</pre></div>

#### [ Reid Barton (May 10 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/unfold%20local%20definitions/near/126375254):
<p>Oh. Thanks!<br>
I guess I never tried precisely this, but only <code>unfold</code> and <code>rw</code>.</p>


{% endraw %}
