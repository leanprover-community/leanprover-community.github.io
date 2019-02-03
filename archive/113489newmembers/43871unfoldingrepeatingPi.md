---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/43871unfoldingrepeatingPi.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [unfolding repeating Pi](https://leanprover-community.github.io/archive/113489newmembers/43871unfoldingrepeatingPi.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Jesse Michael Han (Sep 21 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/unfolding%20repeating%20Pi/near/134384020):
<p>hello everyone! i'm trying to define the following inductive datatype: </p>
<blockquote>
<div class="codehilite"><pre><span></span><span class="kn">constant</span> <span class="n">A</span> <span class="o">:</span> <span class="bp">Π</span> <span class="n">n</span> <span class="o">:</span> <span class="n">nat</span><span class="o">,</span> <span class="kt">Type</span>

<span class="kn">inductive</span> <span class="n">hewwo</span> <span class="o">:</span> <span class="kt">Type</span>
  <span class="bp">|</span> <span class="n">base</span> <span class="o">:</span> <span class="n">nat</span> <span class="bp">→</span> <span class="n">hewwo</span>
  <span class="bp">|</span> <span class="n">apply</span> <span class="o">:</span> <span class="bp">Π</span> <span class="n">n</span><span class="o">,</span> <span class="n">A</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">sorry</span>
</pre></div>


</blockquote>
<p>where the intended type of <code>apply n f</code> is <code>hewwo →</code> ... <code>→ hewwo</code>, repeated <code>n + 1</code> times.</p>
<p>I defined the following function:</p>
<blockquote>
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">repeat_Pi</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">u</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="o">(</span><span class="n">u</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span>
  <span class="bp">|</span> <span class="mi">0</span> <span class="n">A</span> <span class="o">:=</span> <span class="n">A</span>
  <span class="bp">|</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="n">n</span><span class="o">)</span> <span class="n">A</span> <span class="o">:=</span> <span class="bp">Π</span> <span class="n">A</span><span class="o">,</span> <span class="n">repeat_Pi</span> <span class="n">n</span> <span class="n">A</span>
</pre></div>


</blockquote>
<p>but Lean complains that the following:</p>
<blockquote>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">hewwo</span> <span class="o">:</span> <span class="kt">Type</span>
  <span class="bp">|</span> <span class="n">base</span> <span class="o">:</span> <span class="n">nat</span> <span class="bp">→</span> <span class="n">hewwo</span>
  <span class="bp">|</span> <span class="n">apply</span> <span class="o">:</span> <span class="bp">Π</span> <span class="n">n</span><span class="o">,</span> <span class="n">A</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">repeat_Pi</span> <span class="n">n</span> <span class="n">hewwo</span>
</pre></div>


</blockquote>
<p>(rightly) has an incorrect return type for <code>hewwo.apply</code>.</p>
<p>Is there a way to get Lean to treat <code>repeat_Pi k A</code> as being equal to <code>A -&gt; ... -&gt; A</code>?</p>
<p>(edit: got rid of <code>punit</code> and shifted indexing down by 1)</p>

#### [ Simon Hudon (Sep 21 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/unfolding%20repeating%20Pi/near/134400061):
<p>Is it intended that in:</p>
<div class="codehilite"><pre><span></span><span class="bp">...</span>
  <span class="bp">|</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="n">n</span><span class="o">)</span> <span class="n">A</span> <span class="o">:=</span> <span class="bp">Π</span> <span class="n">A</span><span class="o">,</span> <span class="n">repeat_Pi</span> <span class="n">n</span> <span class="n">A</span>
</pre></div>


<p>you ignore <code>A</code> that you get as a parameter?</p>

#### [ Simon Hudon (Sep 21 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/unfolding%20repeating%20Pi/near/134400214):
<p>Sorry, that doesn't fix the issue. </p>
<p>You may need to reflect the repetition into the definition of <code>hewwo</code>:</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">hewwo</span> <span class="o">:</span> <span class="n">nat</span> <span class="bp">→</span> <span class="kt">Type</span>
  <span class="bp">|</span> <span class="n">base</span> <span class="o">:</span> <span class="n">nat</span> <span class="bp">→</span> <span class="n">hewwo</span> <span class="mi">0</span>
  <span class="bp">|</span> <span class="n">apply</span> <span class="o">(</span><span class="n">n</span><span class="o">)</span> <span class="o">:</span> <span class="n">A</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">hewwo</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">hewwo</span> <span class="o">(</span><span class="n">succ</span> <span class="n">n</span><span class="o">)</span>
</pre></div>

#### [ Reid Barton (Sep 21 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/unfolding%20repeating%20Pi/near/134403199):
<p><span class="user-mention" data-user-id="116045">@Jesse Michael Han</span> I would just use the uncurried <code>\Pi n, A n -&gt; (fin n -&gt; hewwo) -&gt; hewwo</code> instead.<br>
I don't think you can do the thing you were trying to do.</p>


{% endraw %}
