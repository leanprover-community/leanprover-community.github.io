---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/01777Leanunabletocoercefromsettotypeorsomething.html
---

## Stream: [new members](index.html)
### Topic: [Lean unable to coerce from set to type (or something)](01777Leanunabletocoercefromsettotypeorsomething.html)

---


{% raw %}
#### [ Abhimanyu Pallavi Sudhir (Nov 01 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Lean%20unable%20to%20coerce%20from%20set%20to%20type%20%28or%20something%29/near/136915550):
<p>(approximately M)WE:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">set</span><span class="bp">.</span><span class="n">basic</span>
<span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">set</span><span class="bp">.</span><span class="n">lattice</span>
<span class="kn">universe</span> <span class="n">u</span>

<span class="kn">variable</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span>
<span class="kn">variable</span> <span class="o">{</span><span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span>
<span class="kn">variable</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">Y</span><span class="o">}</span>

<span class="n">def</span> <span class="n">G</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">Y</span><span class="o">)</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">X</span> <span class="bp">×</span> <span class="n">Y</span><span class="o">)</span> <span class="o">:=</span> <span class="o">{</span> <span class="n">g</span> <span class="bp">|</span> <span class="n">g</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">=</span> <span class="n">f</span> <span class="o">(</span><span class="n">g</span><span class="bp">.</span><span class="mi">1</span><span class="o">)</span> <span class="o">}</span>
<span class="n">def</span> <span class="n">p1</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">G</span> <span class="n">f</span><span class="o">)</span> <span class="o">:</span> <span class="n">X</span> <span class="o">:=</span> <span class="n">g</span><span class="bp">.</span><span class="mi">1</span><span class="bp">.</span><span class="mi">1</span>
<span class="n">def</span> <span class="n">injectivity&#39;</span> <span class="o">{</span><span class="n">X&#39;</span> <span class="n">Y&#39;</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">X&#39;</span> <span class="bp">→</span> <span class="n">Y&#39;</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">∀</span> <span class="n">x1</span> <span class="n">x2</span> <span class="o">:</span> <span class="n">X&#39;</span><span class="o">,</span> <span class="n">g</span> <span class="n">x1</span> <span class="bp">=</span> <span class="n">g</span> <span class="n">x2</span> <span class="bp">→</span> <span class="n">x1</span> <span class="bp">=</span> <span class="n">x2</span>
<span class="n">def</span> <span class="n">surjectivity&#39;</span> <span class="o">{</span><span class="n">X&#39;</span> <span class="n">Y&#39;</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">X&#39;</span> <span class="bp">→</span> <span class="n">Y&#39;</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">∀</span> <span class="n">y</span> <span class="o">:</span> <span class="n">Y&#39;</span><span class="o">,</span> <span class="bp">∃</span> <span class="n">x</span> <span class="o">:</span> <span class="n">X&#39;</span><span class="o">,</span> <span class="n">g</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">y</span>
<span class="n">def</span> <span class="n">bijectivity&#39;</span> <span class="o">{</span><span class="n">X&#39;</span> <span class="n">Y&#39;</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">X&#39;</span> <span class="bp">→</span> <span class="n">Y&#39;</span><span class="o">)</span> <span class="o">:=</span> <span class="n">injectivity&#39;</span> <span class="n">g</span> <span class="bp">∧</span> <span class="n">surjectivity&#39;</span> <span class="n">g</span>

<span class="kn">theorem</span> <span class="n">bij_p1</span> <span class="o">:</span> <span class="bp">@</span><span class="n">bijectivity&#39;</span> <span class="o">(</span><span class="err">↥</span><span class="o">(</span><span class="n">set</span> <span class="o">(</span><span class="n">X</span> <span class="bp">×</span> <span class="n">Y</span><span class="o">)))</span> <span class="o">(</span><span class="err">↥</span><span class="o">(</span><span class="n">G</span> <span class="n">f</span><span class="o">))</span> <span class="o">(</span><span class="n">p1</span><span class="o">)</span> <span class="o">:=</span>
    <span class="k">begin</span>
        <span class="n">sorry</span><span class="o">,</span>
    <span class="kn">end</span>

<span class="bp">#</span><span class="kn">check</span> <span class="n">p1</span>
<span class="bp">#</span><span class="kn">check</span> <span class="n">bijectivity&#39;</span>
</pre></div>


<p>But Lean doesn't seem to understand that <code>↥(set (X × Y)</code> is a Type -- it gives me the error <code>failed to synthesise type class instance for: has_coe_to_sort (Type u)</code>. What's going on?</p>

#### [ Kenny Lau (Nov 01 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Lean%20unable%20to%20coerce%20from%20set%20to%20type%20%28or%20something%29/near/136918282):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">set</span><span class="bp">.</span><span class="n">basic</span>
<span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">set</span><span class="bp">.</span><span class="n">lattice</span>
<span class="kn">universe</span> <span class="n">u</span>

<span class="kn">variable</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span>
<span class="kn">variable</span> <span class="o">{</span><span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span>
<span class="kn">variable</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">Y</span><span class="o">}</span>

<span class="n">def</span> <span class="n">G</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">Y</span><span class="o">)</span> <span class="o">:</span> <span class="n">set</span> <span class="o">(</span><span class="n">X</span> <span class="bp">×</span> <span class="n">Y</span><span class="o">)</span> <span class="o">:=</span> <span class="o">{</span> <span class="n">g</span> <span class="bp">|</span> <span class="n">g</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">=</span> <span class="n">f</span> <span class="o">(</span><span class="n">g</span><span class="bp">.</span><span class="mi">1</span><span class="o">)</span> <span class="o">}</span>
<span class="n">def</span> <span class="n">p1</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">G</span> <span class="n">f</span><span class="o">)</span> <span class="o">:</span> <span class="n">X</span> <span class="o">:=</span> <span class="n">g</span><span class="bp">.</span><span class="mi">1</span><span class="bp">.</span><span class="mi">1</span>
<span class="n">def</span> <span class="n">injectivity&#39;</span> <span class="o">{</span><span class="n">X&#39;</span> <span class="n">Y&#39;</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">X&#39;</span> <span class="bp">→</span> <span class="n">Y&#39;</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">∀</span> <span class="n">x1</span> <span class="n">x2</span> <span class="o">:</span> <span class="n">X&#39;</span><span class="o">,</span> <span class="n">g</span> <span class="n">x1</span> <span class="bp">=</span> <span class="n">g</span> <span class="n">x2</span> <span class="bp">→</span> <span class="n">x1</span> <span class="bp">=</span> <span class="n">x2</span>
<span class="n">def</span> <span class="n">surjectivity&#39;</span> <span class="o">{</span><span class="n">X&#39;</span> <span class="n">Y&#39;</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">X&#39;</span> <span class="bp">→</span> <span class="n">Y&#39;</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">∀</span> <span class="n">y</span> <span class="o">:</span> <span class="n">Y&#39;</span><span class="o">,</span> <span class="bp">∃</span> <span class="n">x</span> <span class="o">:</span> <span class="n">X&#39;</span><span class="o">,</span> <span class="n">g</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">y</span>
<span class="n">def</span> <span class="n">bijectivity&#39;</span> <span class="o">{</span><span class="n">X&#39;</span> <span class="n">Y&#39;</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">X&#39;</span> <span class="bp">→</span> <span class="n">Y&#39;</span><span class="o">)</span> <span class="o">:=</span> <span class="n">injectivity&#39;</span> <span class="n">g</span> <span class="bp">∧</span> <span class="n">surjectivity&#39;</span> <span class="n">g</span>

<span class="kn">theorem</span> <span class="n">bij_p1</span> <span class="o">:</span> <span class="bp">@</span><span class="n">bijectivity&#39;</span> <span class="o">(</span><span class="err">↥</span><span class="o">(</span><span class="n">G</span> <span class="n">f</span><span class="o">))</span> <span class="n">X</span> <span class="o">(</span><span class="n">p1</span><span class="o">)</span> <span class="o">:=</span>
    <span class="k">begin</span>
        <span class="n">sorry</span><span class="o">,</span>
    <span class="kn">end</span>

<span class="bp">#</span><span class="kn">check</span> <span class="n">p1</span>
<span class="bp">#</span><span class="kn">check</span> <span class="n">bijectivity&#39;</span>
</pre></div>

#### [ Kenny Lau (Nov 01 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Lean%20unable%20to%20coerce%20from%20set%20to%20type%20%28or%20something%29/near/136918283):
<p>universe issues</p>

#### [ Abhimanyu Pallavi Sudhir (Nov 01 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Lean%20unable%20to%20coerce%20from%20set%20to%20type%20%28or%20something%29/near/136918689):
<p>Oh -- of course. Thanks.</p>

#### [ Abhimanyu Pallavi Sudhir (Nov 01 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Lean%20unable%20to%20coerce%20from%20set%20to%20type%20%28or%20something%29/near/136918860):
<p>And I have no clue why I was putting in the domain and range of <code>f</code> instead of <code>p1</code>.</p>


{% endraw %}
