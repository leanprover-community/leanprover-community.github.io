---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/14275showisslow.html
---

## Stream: [general](index.html)
### Topic: [show is slow](14275showisslow.html)

---


{% raw %}
#### [ Kevin Buzzard (Aug 04 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130888169):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">set_option</span> <span class="n">profiler</span> <span class="n">true</span>

<span class="kn">theorem</span> <span class="n">works_fine</span> <span class="o">:</span> <span class="o">(</span><span class="mi">3</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">=</span> <span class="o">((</span><span class="mi">3</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:=</span> <span class="n">rfl</span>
<span class="c1">-- elaboration of works_fine took 31.9ms</span>

<span class="kn">theorem</span> <span class="n">very_slow</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">H1</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">=</span> <span class="err">↑</span><span class="n">n</span><span class="o">)</span> <span class="o">(</span><span class="n">H2</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">&lt;</span> <span class="mi">3</span><span class="o">)</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="mi">3</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">show</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="o">((</span><span class="mi">3</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">),</span> <span class="c1">-- this is the bad line</span>
  <span class="n">rw</span> <span class="n">H1</span><span class="o">,</span>
  <span class="n">rwa</span> <span class="n">int</span><span class="bp">.</span><span class="n">cast_lt</span><span class="o">,</span>
<span class="kn">end</span>

<span class="c1">-- elaboration of very_slow took 5.4s</span>

<span class="kn">theorem</span> <span class="n">much_faster</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">H1</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">=</span> <span class="err">↑</span><span class="n">n</span><span class="o">)</span> <span class="o">(</span><span class="n">H2</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">&lt;</span> <span class="mi">3</span><span class="o">)</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="mi">3</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">rw</span> <span class="o">(</span><span class="k">show</span> <span class="o">(</span><span class="mi">3</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">=</span> <span class="o">((</span><span class="mi">3</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">),</span> <span class="k">from</span> <span class="n">rfl</span><span class="o">),</span>
  <span class="n">rw</span> <span class="n">H1</span><span class="o">,</span>
  <span class="n">rwa</span> <span class="n">int</span><span class="bp">.</span><span class="n">cast_lt</span><span class="o">,</span>
<span class="kn">end</span>
<span class="c1">-- elaboration of much_faster took 61.6ms</span>
</pre></div>


<p>Note one elaboration time is in seconds not milliseconds. What have I done wrong here? I have somehow misused <code>show</code>, it seems.</p>

#### [ Kevin Buzzard (Aug 04 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130888235):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">very_slow</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">H1</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">=</span> <span class="err">↑</span><span class="n">n</span><span class="o">)</span> <span class="o">(</span><span class="n">H2</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">&lt;</span> <span class="o">(</span><span class="mi">3</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">))</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="o">(</span><span class="mi">3</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">show</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="o">((</span><span class="mi">3</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">),</span> <span class="c1">-- this is the bad line</span>
  <span class="n">rw</span> <span class="n">H1</span><span class="o">,</span>
  <span class="n">rwa</span> <span class="n">int</span><span class="bp">.</span><span class="n">cast_lt</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p>doesn't fix it. I can't imagine what <code>show</code> is doing.</p>

#### [ Mario Carneiro (Aug 04 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130888627):
<p>does <code>change</code> do any better?</p>

#### [ Kevin Buzzard (Aug 04 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130888631):
<p>Progress:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">set_option</span> <span class="n">profiler</span> <span class="n">true</span>

<span class="kn">theorem</span> <span class="n">works_fine</span> <span class="o">:</span> <span class="o">(</span><span class="mi">3</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">=</span> <span class="o">((</span><span class="mi">3</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:=</span> <span class="n">rfl</span>
<span class="c1">-- elaboration of works_fine took 14.3ms</span>

<span class="kn">theorem</span> <span class="n">very_slow2</span> <span class="o">:</span> <span class="o">(</span><span class="mi">3</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">=</span> <span class="o">((</span><span class="mi">3</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">have</span> <span class="n">H</span> <span class="o">:</span> <span class="o">(</span><span class="mi">3</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">=</span> <span class="o">((</span><span class="mi">3</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:=</span> <span class="n">rfl</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">H</span>
<span class="kn">end</span>
<span class="c1">-- elaboration of very_slow2 took 5.83s</span>
</pre></div>

#### [ Kevin Buzzard (Aug 04 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130888638):
<p>(progress in the sense that the problem is now simpler and even more confusing)</p>

#### [ Chris Hughes (Aug 04 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130888802):
<p>Don't use definitional reduction for reals is probably the best solution.</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">very_slow</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">H1</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">=</span> <span class="err">↑</span><span class="n">n</span><span class="o">)</span> <span class="o">(</span><span class="n">H2</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">&lt;</span> <span class="o">(</span><span class="mi">3</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">))</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="o">(</span><span class="mi">3</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">have</span> <span class="o">:</span> <span class="o">(</span><span class="mi">3</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">=</span> <span class="o">((</span><span class="mi">3</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span><span class="o">,</span>
  <span class="n">rwa</span> <span class="o">[</span><span class="n">H1</span><span class="o">,</span> <span class="n">this</span><span class="o">,</span> <span class="n">int</span><span class="bp">.</span><span class="n">cast_lt</span><span class="o">],</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Aug 04 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130888858):
<p>Sure there are workarounds, but what is surprising is that Lean is <em>sometimes</em> proving the result by <code>rfl</code> quickly and sometimes not</p>

#### [ Kevin Buzzard (Aug 04 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130888874):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">very_slow3</span> <span class="o">:</span> <span class="o">(</span><span class="mi">3</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">=</span> <span class="o">((</span><span class="mi">3</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">change</span> <span class="o">(</span><span class="mi">3</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="k">with</span> <span class="o">((</span><span class="mi">3</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">),</span>
  <span class="n">refl</span><span class="o">,</span>
<span class="kn">end</span>

<span class="kn">theorem</span> <span class="n">very_slow4</span> <span class="o">:</span> <span class="o">(</span><span class="mi">3</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">=</span> <span class="o">((</span><span class="mi">3</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">change</span> <span class="o">((</span><span class="mi">3</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="k">with</span> <span class="o">(</span><span class="mi">3</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">),</span>
  <span class="n">refl</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p>same problem with change</p>

#### [ Kevin Buzzard (Aug 04 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889010):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">very_slow</span> <span class="o">:</span> <span class="o">(</span><span class="mi">3</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">=</span> <span class="o">((</span><span class="mi">3</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">have</span> <span class="n">H</span> <span class="o">:</span> <span class="o">(</span><span class="mi">3</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">=</span> <span class="o">((</span><span class="mi">3</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:=</span> <span class="n">rfl</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">H</span>
<span class="kn">end</span>

<span class="kn">theorem</span> <span class="n">works_fine</span> <span class="o">:</span> <span class="o">(</span><span class="mi">3</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">=</span> <span class="o">((</span><span class="mi">3</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">have</span> <span class="n">H</span> <span class="o">:</span> <span class="o">(</span><span class="mi">3</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">=</span> <span class="o">((</span><span class="mi">3</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">),</span>
    <span class="n">refl</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">H</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p>Way beyond my pay grade</p>

#### [ Mario Carneiro (Aug 04 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889117):
<p>I have narrowed it down to</p>
<div class="codehilite"><pre><span></span>run_cmd assertv_core `h `((3 : ℝ) = ((3 : ℤ) : ℝ)) `(eq.refl (3 : ℝ))
</pre></div>


<p>which is slow, while</p>
<div class="codehilite"><pre><span></span>run_cmd assertv_core `h `((3 : ℝ) = ((3 : ℤ) : ℝ))
  `(show (3 : ℝ) = ((3 : ℤ) : ℝ), from eq.refl (3 : ℝ))
</pre></div>


<p>is fast</p>

#### [ Kenny Lau (Aug 04 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889181):
<p>how do I use <code>run_cmd</code>?</p>

#### [ Mario Carneiro (Aug 04 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889191):
<p>it accepts a <code>tactic A</code> and runs it in a dummy state</p>

#### [ Kenny Lau (Aug 04 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889195):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>

<span class="n">run_cmd</span> <span class="n">assertv_core</span> <span class="bp">`</span><span class="n">h</span> <span class="bp">`</span><span class="o">((</span><span class="mi">3</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">=</span> <span class="o">((</span><span class="mi">3</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">))</span> <span class="bp">`</span><span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">refl</span> <span class="o">(</span><span class="mi">3</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">))</span>
</pre></div>

#### [ Kenny Lau (Aug 04 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889196):
<p>this doesn't work</p>

#### [ Mario Carneiro (Aug 04 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889199):
<p>it's basically the same as <code>example : true := by tac</code></p>

#### [ Mario Carneiro (Aug 04 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889239):
<p><code>open tactic</code></p>

#### [ Kenny Lau (Aug 04 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889243):
<p>lol</p>

#### [ Kenny Lau (Aug 04 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889311):
<div class="codehilite"><pre><span></span><span class="n">run_cmd</span> <span class="n">assertv_core</span> <span class="bp">`</span><span class="n">h</span> <span class="bp">`</span><span class="o">((</span><span class="mi">2</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">=</span> <span class="o">((</span><span class="mi">3</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">))</span>
  <span class="bp">`</span><span class="o">(</span><span class="k">show</span> <span class="o">(</span><span class="mi">3</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">=</span> <span class="o">((</span><span class="mi">3</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">),</span> <span class="k">from</span> <span class="n">eq</span><span class="bp">.</span><span class="n">refl</span> <span class="o">(</span><span class="mi">3</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">))</span>
</pre></div>

#### [ Kenny Lau (Aug 04 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889312):
<p>this is slow</p>

#### [ Kenny Lau (Aug 04 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889315):
<p>this timed out</p>

#### [ Kenny Lau (Aug 04 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889317):
<p>(it's 2 instead of 3 in the beginning)</p>

#### [ Kenny Lau (Aug 04 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889333):
<p>while this is fast (I changed the last 3 to 2 instead):</p>
<div class="codehilite"><pre><span></span><span class="n">run_cmd</span> <span class="n">assertv_core</span> <span class="bp">`</span><span class="n">h</span> <span class="bp">`</span><span class="o">((</span><span class="mi">3</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">=</span> <span class="o">((</span><span class="mi">3</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">))</span>
  <span class="bp">`</span><span class="o">(</span><span class="k">show</span> <span class="o">(</span><span class="mi">3</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">=</span> <span class="o">((</span><span class="mi">3</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">),</span> <span class="k">from</span> <span class="n">eq</span><span class="bp">.</span><span class="n">refl</span> <span class="o">(</span><span class="mi">2</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">))</span>
</pre></div>

#### [ Kenny Lau (Aug 04 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889340):
<p>so the <code>show</code> is slow</p>

#### [ Mario Carneiro (Aug 04 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889463):
<p>it's not a fair comparison when the statement isn't true though</p>

#### [ Mario Carneiro (Aug 04 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889470):
<p>because then lean does completely different things with regard to error reporting and stuff</p>

#### [ Kenny Lau (Aug 04 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889473):
<div class="codehilite"><pre><span></span><span class="n">run_cmd</span> <span class="n">assertv_core</span> <span class="bp">`</span><span class="n">h</span> <span class="bp">`</span><span class="o">((</span><span class="mi">3</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">=</span> <span class="o">((</span><span class="mi">3</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">))</span>
  <span class="bp">`</span><span class="o">(</span><span class="k">show</span> <span class="o">(</span><span class="mi">2</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">=</span> <span class="o">((</span><span class="mi">2</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">),</span> <span class="k">from</span> <span class="n">eq</span><span class="bp">.</span><span class="n">refl</span> <span class="o">(</span><span class="mi">2</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">))</span>
</pre></div>

#### [ Kenny Lau (Aug 04 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889474):
<p>the statement is true, and it is slow</p>

#### [ Kenny Lau (Aug 04 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889477):
<p>oh wait, this is fast:</p>
<div class="codehilite"><pre><span></span><span class="n">run_cmd</span> <span class="n">assertv_core</span> <span class="bp">`</span><span class="n">h</span> <span class="bp">`</span><span class="o">((</span><span class="mi">3</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">=</span> <span class="o">((</span><span class="mi">3</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">))</span>
  <span class="bp">`</span><span class="o">(</span><span class="k">show</span> <span class="o">(</span><span class="mi">2</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">=</span> <span class="o">((</span><span class="mi">2</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">),</span> <span class="k">from</span> <span class="n">eq</span><span class="bp">.</span><span class="n">refl</span> <span class="o">(</span><span class="mi">3</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">))</span>
</pre></div>

#### [ Mario Carneiro (Aug 04 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889481):
<p>In both cases it's going to fail because the types don't match</p>

#### [ Kenny Lau (Aug 04 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889520):
<p>but they expect <code>2</code> instead of <code>3</code>!</p>

#### [ Kenny Lau (Aug 04 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889526):
<div class="codehilite"><pre><span></span>type mismatch at application
  (λ (this : 2 = ↑2), this) (eq.refl 3)
term
  eq.refl 3
has type
  3 = 3
but is expected to have type
  2 = ↑2
</pre></div>

#### [ Kenny Lau (Aug 04 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889527):
<div class="codehilite"><pre><span></span>unexpected argument at application
  eq.refl 3
given argument
  3
expected argument
  2
</pre></div>

#### [ Mario Carneiro (Aug 04 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889530):
<p><code>assertv_core</code> checks that the type of the last argument is the same as the second argument</p>

#### [ Mario Carneiro (Aug 04 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889535):
<p>so all of the numbers have to match</p>

#### [ Mario Carneiro (Aug 04 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889593):
<p>I think there is a bug in <code>assertv_core</code>. If I use <code>assert_core</code> instead, it works fine, which you can achieve by using the proof-omitted form of tactic <code>have</code></p>

#### [ Mario Carneiro (Aug 04 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889595):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">not_slow</span> <span class="o">:</span> <span class="o">(</span><span class="mi">3</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">=</span> <span class="o">((</span><span class="mi">3</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">have</span> <span class="n">H</span> <span class="o">:</span> <span class="o">(</span><span class="mi">3</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">=</span> <span class="o">((</span><span class="mi">3</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">),</span> <span class="n">exact</span> <span class="n">rfl</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">H</span>
<span class="kn">end</span>
</pre></div>

#### [ Mario Carneiro (Aug 04 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889641):
<p>note that <code>definev_core</code> is also slow, which is linked in to the <code>let</code> tactic</p>

#### [ Kenny Lau (Aug 04 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889707):
<div class="codehilite"><pre><span></span><span class="n">vm_obj</span> <span class="nf">assert_define_core</span><span class="p">(</span><span class="kt">bool</span> <span class="n">is_assert</span><span class="p">,</span> <span class="n">name</span> <span class="k">const</span> <span class="o">&amp;</span> <span class="n">n</span><span class="p">,</span> <span class="n">expr</span> <span class="k">const</span> <span class="o">&amp;</span> <span class="n">t</span><span class="p">,</span> <span class="n">tactic_state</span> <span class="k">const</span> <span class="o">&amp;</span> <span class="n">s</span><span class="p">)</span> <span class="p">{</span>
    <span class="n">optional</span><span class="o">&lt;</span><span class="n">metavar_decl</span><span class="o">&gt;</span> <span class="n">g</span> <span class="o">=</span> <span class="n">s</span><span class="p">.</span><span class="n">get_main_goal_decl</span><span class="p">();</span>
    <span class="k">if</span> <span class="p">(</span><span class="o">!</span><span class="n">g</span><span class="p">)</span> <span class="k">return</span> <span class="n">mk_no_goals_exception</span><span class="p">(</span><span class="n">s</span><span class="p">);</span>
    <span class="n">type_context_old</span> <span class="n">ctx</span>     <span class="o">=</span> <span class="n">mk_type_context_for</span><span class="p">(</span><span class="n">s</span><span class="p">);</span>
    <span class="k">if</span> <span class="p">(</span><span class="o">!</span><span class="n">is_sort</span><span class="p">(</span><span class="n">ctx</span><span class="p">.</span><span class="n">whnf</span><span class="p">(</span><span class="n">ctx</span><span class="p">.</span><span class="n">infer</span><span class="p">(</span><span class="n">t</span><span class="p">))))</span> <span class="p">{</span>
        <span class="n">format</span> <span class="n">msg</span><span class="p">(</span><span class="s">&quot;invalid &quot;</span><span class="p">);</span>
        <span class="k">if</span> <span class="p">(</span><span class="n">is_assert</span><span class="p">)</span> <span class="n">msg</span> <span class="o">+=</span> <span class="n">format</span><span class="p">(</span><span class="s">&quot;assert&quot;</span><span class="p">);</span> <span class="k">else</span> <span class="n">msg</span> <span class="o">+=</span> <span class="n">format</span><span class="p">(</span><span class="s">&quot;define&quot;</span><span class="p">);</span>
        <span class="n">msg</span> <span class="o">+=</span> <span class="n">format</span><span class="p">(</span><span class="s">&quot; tactic, expression is not a type&quot;</span><span class="p">);</span>
        <span class="n">msg</span> <span class="o">+=</span> <span class="n">pp_indented_expr</span><span class="p">(</span><span class="n">s</span><span class="p">,</span> <span class="n">t</span><span class="p">);</span>
        <span class="k">return</span> <span class="n">tactic</span><span class="o">::</span><span class="n">mk_exception</span><span class="p">(</span><span class="n">msg</span><span class="p">,</span> <span class="n">s</span><span class="p">);</span>
    <span class="p">}</span>
    <span class="n">local_context</span> <span class="n">lctx</span>   <span class="o">=</span> <span class="n">g</span><span class="o">-&gt;</span><span class="n">get_context</span><span class="p">();</span>
    <span class="n">expr</span> <span class="n">new_M_1</span>         <span class="o">=</span> <span class="n">ctx</span><span class="p">.</span><span class="n">mk_metavar_decl</span><span class="p">(</span><span class="n">lctx</span><span class="p">,</span> <span class="n">t</span><span class="p">);</span>
    <span class="n">expr</span> <span class="n">new_M_2</span><span class="p">,</span> <span class="n">new_val</span><span class="p">;</span>
    <span class="k">if</span> <span class="p">(</span><span class="n">is_assert</span><span class="p">)</span> <span class="p">{</span>
        <span class="n">expr</span> <span class="n">new_target</span>  <span class="o">=</span> <span class="n">mk_pi</span><span class="p">(</span><span class="n">n</span><span class="p">,</span> <span class="n">t</span><span class="p">,</span> <span class="n">g</span><span class="o">-&gt;</span><span class="n">get_type</span><span class="p">());</span>
        <span class="n">new_M_2</span>          <span class="o">=</span> <span class="n">ctx</span><span class="p">.</span><span class="n">mk_metavar_decl</span><span class="p">(</span><span class="n">lctx</span><span class="p">,</span> <span class="n">new_target</span><span class="p">);</span>
        <span class="n">new_val</span>          <span class="o">=</span> <span class="n">mk_app</span><span class="p">(</span><span class="n">new_M_2</span><span class="p">,</span> <span class="n">new_M_1</span><span class="p">);</span>
    <span class="p">}</span> <span class="k">else</span> <span class="p">{</span>
        <span class="n">expr</span> <span class="n">new_target</span>  <span class="o">=</span> <span class="n">mk_let</span><span class="p">(</span><span class="n">n</span><span class="p">,</span> <span class="n">t</span><span class="p">,</span> <span class="n">new_M_1</span><span class="p">,</span> <span class="n">g</span><span class="o">-&gt;</span><span class="n">get_type</span><span class="p">());</span>
        <span class="n">new_M_2</span>          <span class="o">=</span> <span class="n">ctx</span><span class="p">.</span><span class="n">mk_metavar_decl</span><span class="p">(</span><span class="n">lctx</span><span class="p">,</span> <span class="n">new_target</span><span class="p">);</span>
        <span class="n">new_val</span>          <span class="o">=</span> <span class="n">new_M_2</span><span class="p">;</span>
    <span class="p">}</span>
    <span class="n">ctx</span><span class="p">.</span><span class="n">assign</span><span class="p">(</span><span class="n">head</span><span class="p">(</span><span class="n">s</span><span class="p">.</span><span class="n">goals</span><span class="p">()),</span> <span class="n">new_val</span><span class="p">);</span>
    <span class="n">list</span><span class="o">&lt;</span><span class="n">expr</span><span class="o">&gt;</span> <span class="n">new_gs</span>    <span class="o">=</span> <span class="n">cons</span><span class="p">(</span><span class="n">new_M_1</span><span class="p">,</span> <span class="n">cons</span><span class="p">(</span><span class="n">new_M_2</span><span class="p">,</span> <span class="n">tail</span><span class="p">(</span><span class="n">s</span><span class="p">.</span><span class="n">goals</span><span class="p">())));</span>
    <span class="k">return</span> <span class="n">tactic</span><span class="o">::</span><span class="n">mk_success</span><span class="p">(</span><span class="n">set_mctx_goals</span><span class="p">(</span><span class="n">s</span><span class="p">,</span> <span class="n">ctx</span><span class="p">.</span><span class="n">mctx</span><span class="p">(),</span> <span class="n">new_gs</span><span class="p">));</span>
<span class="p">}</span>

<span class="n">vm_obj</span> <span class="nf">tactic_assert_core</span><span class="p">(</span><span class="n">vm_obj</span> <span class="k">const</span> <span class="o">&amp;</span> <span class="n">n</span><span class="p">,</span> <span class="n">vm_obj</span> <span class="k">const</span> <span class="o">&amp;</span> <span class="n">t</span><span class="p">,</span> <span class="n">vm_obj</span> <span class="k">const</span> <span class="o">&amp;</span> <span class="n">s</span><span class="p">)</span> <span class="p">{</span>
    <span class="k">return</span> <span class="n">assert_define_core</span><span class="p">(</span><span class="nb">true</span><span class="p">,</span> <span class="n">to_name</span><span class="p">(</span><span class="n">n</span><span class="p">),</span> <span class="n">to_expr</span><span class="p">(</span><span class="n">t</span><span class="p">),</span> <span class="n">tactic</span><span class="o">::</span><span class="n">to_state</span><span class="p">(</span><span class="n">s</span><span class="p">));</span>
<span class="p">}</span>

<span class="n">vm_obj</span> <span class="nf">assertv_definev_core</span><span class="p">(</span><span class="kt">bool</span> <span class="n">is_assert</span><span class="p">,</span> <span class="n">name</span> <span class="k">const</span> <span class="o">&amp;</span> <span class="n">n</span><span class="p">,</span> <span class="n">expr</span> <span class="k">const</span> <span class="o">&amp;</span> <span class="n">t</span><span class="p">,</span> <span class="n">expr</span> <span class="k">const</span> <span class="o">&amp;</span> <span class="n">v</span><span class="p">,</span> <span class="n">tactic_state</span> <span class="k">const</span> <span class="o">&amp;</span> <span class="n">s</span><span class="p">)</span> <span class="p">{</span>
    <span class="n">optional</span><span class="o">&lt;</span><span class="n">metavar_decl</span><span class="o">&gt;</span> <span class="n">g</span> <span class="o">=</span> <span class="n">s</span><span class="p">.</span><span class="n">get_main_goal_decl</span><span class="p">();</span>
    <span class="k">if</span> <span class="p">(</span><span class="o">!</span><span class="n">g</span><span class="p">)</span> <span class="k">return</span> <span class="n">mk_no_goals_exception</span><span class="p">(</span><span class="n">s</span><span class="p">);</span>
    <span class="n">type_context_old</span> <span class="n">ctx</span>     <span class="o">=</span> <span class="n">mk_type_context_for</span><span class="p">(</span><span class="n">s</span><span class="p">);</span>
    <span class="n">expr</span> <span class="n">v_type</span>          <span class="o">=</span> <span class="n">ctx</span><span class="p">.</span><span class="n">infer</span><span class="p">(</span><span class="n">v</span><span class="p">);</span>
    <span class="k">if</span> <span class="p">(</span><span class="o">!</span><span class="n">ctx</span><span class="p">.</span><span class="n">is_def_eq</span><span class="p">(</span><span class="n">t</span><span class="p">,</span> <span class="n">v_type</span><span class="p">))</span> <span class="p">{</span>
        <span class="k">auto</span> <span class="n">thunk</span> <span class="o">=</span> <span class="p">[</span><span class="o">=</span><span class="p">]()</span> <span class="p">{</span>
            <span class="n">format</span> <span class="n">msg</span><span class="p">(</span><span class="s">&quot;invalid &quot;</span><span class="p">);</span>
            <span class="k">if</span> <span class="p">(</span><span class="n">is_assert</span><span class="p">)</span> <span class="n">msg</span> <span class="o">+=</span> <span class="n">format</span><span class="p">(</span><span class="s">&quot;assertv&quot;</span><span class="p">);</span> <span class="k">else</span> <span class="n">msg</span> <span class="o">+=</span> <span class="n">format</span><span class="p">(</span><span class="s">&quot;definev&quot;</span><span class="p">);</span>
            <span class="n">msg</span> <span class="o">+=</span> <span class="n">format</span><span class="p">(</span><span class="s">&quot; tactic, value has type&quot;</span><span class="p">);</span>
            <span class="n">msg</span> <span class="o">+=</span> <span class="n">pp_indented_expr</span><span class="p">(</span><span class="n">s</span><span class="p">,</span> <span class="n">v_type</span><span class="p">);</span>
            <span class="n">msg</span> <span class="o">+=</span> <span class="n">line</span><span class="p">()</span> <span class="o">+</span> <span class="n">format</span><span class="p">(</span><span class="s">&quot;but is expected to have type&quot;</span><span class="p">);</span>
            <span class="n">msg</span> <span class="o">+=</span> <span class="n">pp_indented_expr</span><span class="p">(</span><span class="n">s</span><span class="p">,</span> <span class="n">t</span><span class="p">);</span>
            <span class="k">return</span> <span class="n">msg</span><span class="p">;</span>
        <span class="p">};</span>
        <span class="k">return</span> <span class="n">tactic</span><span class="o">::</span><span class="n">mk_exception</span><span class="p">(</span><span class="n">thunk</span><span class="p">,</span> <span class="n">s</span><span class="p">);</span>
    <span class="p">}</span>
    <span class="n">local_context</span> <span class="n">lctx</span>   <span class="o">=</span> <span class="n">g</span><span class="o">-&gt;</span><span class="n">get_context</span><span class="p">();</span>
    <span class="n">expr</span> <span class="n">new_M</span><span class="p">,</span> <span class="n">new_val</span><span class="p">;</span>
    <span class="k">if</span> <span class="p">(</span><span class="n">is_assert</span><span class="p">)</span> <span class="p">{</span>
        <span class="n">expr</span> <span class="n">new_target</span>  <span class="o">=</span> <span class="n">mk_pi</span><span class="p">(</span><span class="n">n</span><span class="p">,</span> <span class="n">t</span><span class="p">,</span> <span class="n">g</span><span class="o">-&gt;</span><span class="n">get_type</span><span class="p">());</span>
        <span class="n">new_M</span>            <span class="o">=</span> <span class="n">ctx</span><span class="p">.</span><span class="n">mk_metavar_decl</span><span class="p">(</span><span class="n">lctx</span><span class="p">,</span> <span class="n">new_target</span><span class="p">);</span>
        <span class="n">new_val</span>          <span class="o">=</span> <span class="n">mk_app</span><span class="p">(</span><span class="n">new_M</span><span class="p">,</span> <span class="n">v</span><span class="p">);</span>
    <span class="p">}</span> <span class="k">else</span> <span class="p">{</span>
        <span class="n">expr</span> <span class="n">new_target</span>  <span class="o">=</span> <span class="n">mk_let</span><span class="p">(</span><span class="n">n</span><span class="p">,</span> <span class="n">t</span><span class="p">,</span> <span class="n">v</span><span class="p">,</span> <span class="n">g</span><span class="o">-&gt;</span><span class="n">get_type</span><span class="p">());</span>
        <span class="n">new_M</span>            <span class="o">=</span> <span class="n">ctx</span><span class="p">.</span><span class="n">mk_metavar_decl</span><span class="p">(</span><span class="n">lctx</span><span class="p">,</span> <span class="n">new_target</span><span class="p">);</span>
        <span class="n">new_val</span>          <span class="o">=</span> <span class="n">new_M</span><span class="p">;</span>
    <span class="p">}</span>
    <span class="n">ctx</span><span class="p">.</span><span class="n">assign</span><span class="p">(</span><span class="n">head</span><span class="p">(</span><span class="n">s</span><span class="p">.</span><span class="n">goals</span><span class="p">()),</span> <span class="n">new_val</span><span class="p">);</span>
    <span class="n">list</span><span class="o">&lt;</span><span class="n">expr</span><span class="o">&gt;</span> <span class="n">new_gs</span>    <span class="o">=</span> <span class="n">cons</span><span class="p">(</span><span class="n">new_M</span><span class="p">,</span> <span class="n">tail</span><span class="p">(</span><span class="n">s</span><span class="p">.</span><span class="n">goals</span><span class="p">()));</span>
    <span class="k">return</span> <span class="n">tactic</span><span class="o">::</span><span class="n">mk_success</span><span class="p">(</span><span class="n">set_mctx_goals</span><span class="p">(</span><span class="n">s</span><span class="p">,</span> <span class="n">ctx</span><span class="p">.</span><span class="n">mctx</span><span class="p">(),</span> <span class="n">new_gs</span><span class="p">));</span>
<span class="p">}</span>

<span class="n">vm_obj</span> <span class="nf">tactic_assertv_core</span><span class="p">(</span><span class="n">vm_obj</span> <span class="k">const</span> <span class="o">&amp;</span> <span class="n">n</span><span class="p">,</span> <span class="n">vm_obj</span> <span class="k">const</span> <span class="o">&amp;</span> <span class="n">e</span><span class="p">,</span> <span class="n">vm_obj</span> <span class="k">const</span> <span class="o">&amp;</span> <span class="n">pr</span><span class="p">,</span> <span class="n">vm_obj</span> <span class="k">const</span> <span class="o">&amp;</span> <span class="n">s</span><span class="p">)</span> <span class="p">{</span>
    <span class="k">return</span> <span class="n">assertv_definev_core</span><span class="p">(</span><span class="nb">true</span><span class="p">,</span> <span class="n">to_name</span><span class="p">(</span><span class="n">n</span><span class="p">),</span> <span class="n">to_expr</span><span class="p">(</span><span class="n">e</span><span class="p">),</span> <span class="n">to_expr</span><span class="p">(</span><span class="n">pr</span><span class="p">),</span> <span class="n">tactic</span><span class="o">::</span><span class="n">to_state</span><span class="p">(</span><span class="n">s</span><span class="p">));</span>
<span class="p">}</span>
</pre></div>

#### [ Mario Carneiro (Aug 04 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889756):
<p>the issue is somewhere in <code>assertv_definev_core</code>, but I don't see anything wrong</p>

#### [ Mario Carneiro (Aug 04 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130889764):
<p>the <code>ctx.is_def_eq</code> call is potentially expensive, but you can test that in lean and it's not</p>

#### [ Mario Carneiro (Aug 04 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130890110):
<p>The mystery continues. As far as I can tell, the following lean code should do the same as <code>assertv_definev_core</code> in this case:</p>
<div class="codehilite"><pre><span></span>run_cmd do
  let t : expr := `((3 : ℝ) = ((3 : ℤ) : ℝ)),
  let v : expr := `(eq.refl (3:ℝ)),
  v_t ← infer_type v,
  is_def_eq t v_t,
  r ← target,
  let e := expr.pi `h binder_info.default t r,
  m ← mk_meta_var e,
  let e&#39; := expr.app m v,
  exact e&#39;,
  set_goals [m]
</pre></div>


<p>yet it runs without any problems</p>

#### [ Mario Carneiro (Aug 04 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130891358):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> Could you debug this for me? Here's a mathlib free version of the test:</p>
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">Q</span> <span class="o">:=</span> <span class="o">(</span><span class="n">num</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span>
<span class="n">def</span> <span class="n">id&#39;</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">Q</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">n</span> <span class="bp">/</span> <span class="n">n</span><span class="bp">.</span><span class="n">gcd</span> <span class="mi">1</span><span class="bp">⟩</span>
<span class="kn">instance</span> <span class="o">:</span> <span class="n">has_zero</span> <span class="n">Q</span> <span class="o">:=</span> <span class="bp">⟨⟨</span><span class="mi">0</span><span class="bp">⟩⟩</span>
<span class="kn">instance</span> <span class="o">:</span> <span class="n">has_one</span> <span class="n">Q</span> <span class="o">:=</span> <span class="bp">⟨⟨</span><span class="mi">1</span><span class="bp">⟩⟩</span>
<span class="kn">instance</span> <span class="o">:</span> <span class="n">has_add</span> <span class="n">Q</span> <span class="o">:=</span> <span class="bp">⟨λ</span> <span class="bp">⟨</span><span class="n">n₁</span><span class="bp">⟩</span> <span class="bp">⟨</span><span class="n">n₂</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">id&#39;</span> <span class="o">(</span><span class="n">n₁</span> <span class="bp">+</span> <span class="n">n₂</span><span class="o">)</span><span class="bp">⟩</span>

<span class="n">run_cmd</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">try_for</span> <span class="mi">1000</span> <span class="o">(</span><span class="n">assertv_core</span> <span class="bp">`</span><span class="n">h</span>
  <span class="bp">`</span><span class="o">((</span><span class="mi">4</span> <span class="o">:</span> <span class="n">Q</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">4</span><span class="bp">+</span><span class="mi">0</span><span class="o">)</span>
  <span class="bp">`</span><span class="o">(</span><span class="k">show</span> <span class="o">(</span><span class="mi">4</span> <span class="o">:</span> <span class="n">Q</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">4</span><span class="bp">+</span><span class="mi">0</span><span class="o">,</span> <span class="k">from</span> <span class="n">eq</span><span class="bp">.</span><span class="n">refl</span> <span class="o">(</span><span class="mi">4</span> <span class="o">:</span> <span class="n">Q</span><span class="o">))</span> <span class="bp">&gt;&gt;</span> <span class="n">admit</span><span class="o">)</span> <span class="c1">--works</span>

<span class="n">run_cmd</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">try_for</span> <span class="mi">10000</span> <span class="o">(</span><span class="n">assertv_core</span> <span class="bp">`</span><span class="n">h</span>
  <span class="bp">`</span><span class="o">((</span><span class="mi">4</span> <span class="o">:</span> <span class="n">Q</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">4</span><span class="bp">+</span><span class="mi">0</span><span class="o">)</span>
  <span class="bp">`</span><span class="o">(</span><span class="n">eq</span><span class="bp">.</span><span class="n">refl</span> <span class="o">(</span><span class="mi">4</span> <span class="o">:</span> <span class="n">Q</span><span class="o">))</span> <span class="bp">&gt;&gt;</span> <span class="n">admit</span><span class="o">)</span> <span class="c1">--timeout</span>
</pre></div>

#### [ Johan Commelin (Aug 04 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130891933):
<p>The <code>--works</code> version has <code>1000</code>, whereas the <code>--timeout</code> version has <code>10000</code>. I don't know if that matters...</p>

#### [ Mario Carneiro (Aug 04 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130892761):
<p>That's probably not needed, but it is saying that the first completes in &lt;1000 ms and the second does not complete with &lt;10000 ms so it is much worse</p>

#### [ Simon Hudon (Aug 04 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130897379):
<p>Is this something <code>norm_num</code> would help with?</p>

#### [ Simon Hudon (Aug 04 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130897429):
<p>If I understand correctly, <code>refl</code> is slow because it's unfolding the numerals.</p>

#### [ Kevin Buzzard (Aug 04 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130897479):
<p>refl isn't always slow. It's just slow if you invoke it the wrong way :-)</p>

#### [ Kevin Buzzard (Aug 04 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130897489):
<p>You can prove that the real 3 is the coercion of the integer 3 using simp as well, which is quick (but not as quick as when you use refl, if you use refl the right way)</p>

#### [ Mario Carneiro (Aug 04 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/show%20is%20slow/near/130898142):
<p>I don't think <code>rfl</code> wins over <code>simp</code> here even in the "good" case, at least not if your numbers are moderately large. Calculating <code>4 : real</code> directly requires a number of gcd calculations, which are slow</p>


{% endraw %}
