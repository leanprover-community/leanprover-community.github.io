---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/86181Nonetheorem.html
---

## Stream: [new members](index.html)
### Topic: [None theorem](86181Nonetheorem.html)

---


{% raw %}
#### [ Ken Roe (Sep 01 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/None%20theorem/near/133185891):
<p>Does someone know what tactic to use to prove the following:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">nonethm</span> <span class="o">{</span><span class="n">t</span><span class="o">}</span> <span class="o">:</span> <span class="o">(</span><span class="n">none</span> <span class="bp">&lt;|&gt;</span> <span class="n">none</span><span class="o">)</span><span class="bp">=@</span><span class="n">none</span> <span class="n">t</span><span class="o">:=</span>
<span class="k">begin</span>
    <span class="bp">...</span>
<span class="kn">end</span>
</pre></div>

#### [ Chris Hughes (Sep 01 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/None%20theorem/near/133186005):
<p><code>theorem nonethm {t} : (none &lt;|&gt; none)=@none t:= rfl</code></p>

#### [ Mario Carneiro (Sep 01 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/None%20theorem/near/133186270):
<p>lol. <code>by simp</code> also works if you have <code>import data.option</code></p>

#### [ Patrick Massot (Sep 01 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/None%20theorem/near/133188061):
<p>Chris, you lose: Ken asked for a tactic. The best answer was <code>refl</code> <span class="emoji emoji-1f60b" title="yum">:yum:</span></p>

#### [ Patrick Massot (Sep 01 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/None%20theorem/near/133188364):
<p>A slightly more serious answer: I think stating the result as <code>theorem nonethm {t} : (none &lt;|&gt; none)= (none : option t)</code> makes it easier to read. I mention this because it's a general trick: you can often avoid using <code>@</code> by adding a type ascription.</p>

#### [ Ken Roe (Sep 01 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/None%20theorem/near/133189198):
<p>Thanks.  A couple more questions:<br>
1) I found data/option.lean in mathlib.  Where should I place the mathlib repository with respect to the Lean repository?  How do I configure VSCode so that it starts Lean with the appropriate search path?</p>
<p>2) Next, how do I prove the theorem:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">nonethm</span> <span class="o">{</span><span class="n">t</span><span class="o">}</span> <span class="o">{</span><span class="n">x</span><span class="o">:</span><span class="n">option</span> <span class="n">t</span><span class="o">}</span> <span class="o">:</span> <span class="o">(</span><span class="n">x</span> <span class="bp">&lt;|&gt;</span> <span class="n">none</span><span class="o">)</span><span class="bp">=</span><span class="n">x</span><span class="o">:=</span> <span class="k">begin</span>
    <span class="bp">...</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Sep 01 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/None%20theorem/near/133189244):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">nonethm</span> <span class="o">{</span><span class="n">t</span><span class="o">}</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">option</span> <span class="n">t</span><span class="o">}</span> <span class="o">:</span> <span class="o">(</span><span class="n">x</span> <span class="bp">&lt;|&gt;</span> <span class="n">none</span><span class="o">)</span> <span class="bp">=</span> <span class="n">x</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">cases</span> <span class="n">x</span><span class="bp">;</span> <span class="n">refl</span>
<span class="kn">end</span>
</pre></div>

#### [ Bryan Gin-ge Chen (Sep 01 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/None%20theorem/near/133189359):
<p>For question 1 I recommend using leanpkg. The advice on the <a href="https://xenaproject.wordpress.com/2017/12/02/how-to-install-mathlib-and-keep-it-up-to-date/" target="_blank" title="https://xenaproject.wordpress.com/2017/12/02/how-to-install-mathlib-and-keep-it-up-to-date/">xena blog</a> is a little old but still worked for me a month or so ago.</p>


{% endraw %}
