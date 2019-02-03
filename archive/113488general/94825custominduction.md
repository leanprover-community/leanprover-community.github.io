---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/94825custominduction.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [custom induction](https://leanprover-community.github.io/archive/113488general/94825custominduction.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Sep 12 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20induction/near/133786062):
<p>Can we tag our induction lemmas and have the tactic <code>induction</code> recognize it? Maybe create a new tactic <code>induction'</code>?</p>

#### [ Chris Hughes (Sep 12 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20induction/near/133786384):
<p>You can do <code>induction using</code></p>

#### [ Kenny Lau (Sep 12 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20induction/near/133787915):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> I can't work it out for polynomials</p>

#### [ Chris Hughes (Sep 12 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20induction/near/133788643):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">polynomial</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="mi">1</span> <span class="bp">=</span> <span class="mi">2</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">induction</span> <span class="n">p</span> <span class="kn">using</span> <span class="n">polynomial</span><span class="bp">.</span><span class="n">induction_on</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Sep 12 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20induction/near/133788749):
<p>can you put p in the result?</p>

#### [ Chris Hughes (Sep 12 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20induction/near/133788807):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">polynomial</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">=</span> <span class="mi">2</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">induction</span> <span class="n">p</span> <span class="kn">using</span> <span class="n">polynomial</span><span class="bp">.</span><span class="n">induction_on</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


{% endraw %}
