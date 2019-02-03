---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/99350rwfeature.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [rw feature](https://leanprover-community.github.io/archive/113488general/99350rwfeature.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Aug 23 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20feature/near/132628472):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">H2</span> <span class="o">:</span> <span class="o">(</span><span class="n">a</span> <span class="bp">=</span> <span class="n">b</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="n">a</span> <span class="bp">=</span> <span class="n">c</span><span class="o">))</span> <span class="o">:</span> <span class="n">c</span> <span class="bp">=</span> <span class="n">b</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">rw</span> <span class="o">(</span><span class="n">H2</span> <span class="n">H</span><span class="o">)</span> <span class="n">at</span> <span class="n">H</span><span class="o">,</span> <span class="c1">-- does nothing</span>
  <span class="n">exact</span> <span class="n">H</span> <span class="c1">-- fails</span>
<span class="kn">end</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">H2</span> <span class="o">:</span> <span class="o">(</span><span class="n">a</span> <span class="bp">=</span> <span class="n">b</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="n">a</span> <span class="bp">=</span> <span class="n">c</span><span class="o">))</span> <span class="o">:</span> <span class="n">c</span> <span class="bp">=</span> <span class="n">b</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">have</span> <span class="n">H&#39;</span> <span class="o">:=</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">(</span><span class="n">H2</span> <span class="n">H&#39;</span><span class="o">)</span> <span class="n">at</span> <span class="n">H</span><span class="o">,</span> <span class="c1">-- works fine</span>
  <span class="n">exact</span> <span class="n">H</span>
<span class="kn">end</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">H2</span> <span class="o">:</span> <span class="o">(</span><span class="n">a</span> <span class="bp">=</span> <span class="n">b</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="n">a</span> <span class="bp">=</span> <span class="n">c</span><span class="o">))</span> <span class="o">:</span> <span class="n">c</span> <span class="bp">=</span> <span class="n">b</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">have</span> <span class="n">H&#39;</span> <span class="o">:=</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">(</span><span class="n">H2</span> <span class="n">H</span><span class="o">)</span> <span class="n">at</span> <span class="n">H&#39;</span><span class="o">,</span> <span class="c1">-- works fine</span>
  <span class="n">exact</span> <span class="n">H&#39;</span>
<span class="kn">end</span>
</pre></div>


<p>Is this a bug, or is it not a good idea to let rewrites affect hypotheses which are used to construct the term being rewritten? (or both?)</p>

#### [ Kevin Buzzard (Aug 23 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20feature/near/132628548):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">b</span><span class="o">)</span> <span class="o">:</span> <span class="n">false</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">rw</span> <span class="n">H</span> <span class="n">at</span> <span class="n">H</span><span class="o">,</span> <span class="c1">-- I would expect H to become b = b...</span>
  <span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Aug 23 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20feature/near/132628571):
<p>[PS this is not frivolous -- I just attempted to do a rewrite on a term which I had used to explicitly fill in something which type class inference couldn't infer, and it silently failed]</p>

#### [ Simon Hudon (Aug 23 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20feature/near/132639780):
<p>I think <code>rw</code> does not rewrite the assumptions themselves because if you have:</p>
<div class="codehilite"><pre><span></span>h0 : a = b,
h1 : a = c
...
</pre></div>


<p><code>rw h0 at *</code> would transform <code>h0</code> into <code>b = b</code> and then <code>rw</code> would not be able to rewrite <code>h1</code>.</p>

#### [ Simon Hudon (Aug 23 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20feature/near/132639895):
<p>I suspect the developers consciously decided to not let <code>rw</code> rewrite assumptions using themselves as a rule. If the assumptions eventually get reshuffled, the design of <code>rw</code> makes the re-execution of the same proof less surprising. Does <code>simp</code> or <code>dsimp</code> help in your situation?</p>

#### [ Kevin Buzzard (Aug 23 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20feature/near/132639964):
<p>I did exactly what I suggested in my original post -- I just introduced a new hypothesis which was by definition the old one :-)</p>

#### [ Simon Hudon (Aug 23 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20feature/near/132640206):
<p>Ah ok, I thought it might fit in a more complex situation. So it would rank as "annoying", I assume</p>

#### [ Kevin Buzzard (Aug 23 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20feature/near/132640291):
<p>Yeah, I'm helping undergraduates to write code and today has been quite an annoying day for some reason, I've had to introduce several workarounds for things.</p>

#### [ Simon Hudon (Aug 23 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rw%20feature/near/132640475):
<p>I think that happens a lot in any programming language: with time, you start instinctively avoiding the pain points and then the newcomers run right into them</p>


{% endraw %}
