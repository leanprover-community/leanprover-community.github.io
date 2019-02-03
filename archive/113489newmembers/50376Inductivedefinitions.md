---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/50376Inductivedefinitions.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [Inductive definitions](https://leanprover-community.github.io/archive/113489newmembers/50376Inductivedefinitions.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Ken Roe (Aug 28 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Inductive%20definitions/near/132926297):
<p>I see a number of comments in my code that a definition of the form:</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">allFirsts</span> <span class="o">{</span><span class="n">t1</span><span class="o">}</span> <span class="o">{</span><span class="n">t2</span><span class="o">}</span> <span class="o">:</span> <span class="n">list</span> <span class="n">t1</span> <span class="bp">→</span> <span class="n">list</span> <span class="o">(</span><span class="n">t1</span> <span class="bp">×</span> <span class="n">t2</span><span class="o">)</span> <span class="bp">→</span> <span class="kt">Prop</span>
 <span class="bp">|</span> <span class="n">AFNil</span> <span class="o">:</span> <span class="n">allFirsts</span> <span class="n">list</span><span class="bp">.</span><span class="n">nil</span> <span class="n">list</span><span class="bp">.</span><span class="n">nil</span>
 <span class="bp">|</span> <span class="n">AFCons</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">fx</span> <span class="n">fy</span> <span class="n">r</span> <span class="n">r&#39;</span><span class="o">,</span> <span class="n">allFirsts</span> <span class="n">r</span> <span class="n">r&#39;</span> <span class="bp">→</span> <span class="n">allFirsts</span> <span class="o">(</span><span class="n">fx</span><span class="bp">::</span><span class="n">r</span><span class="o">)</span> <span class="o">((</span><span class="n">fx</span><span class="o">,</span><span class="n">fy</span><span class="o">)</span><span class="bp">::</span><span class="n">r&#39;</span><span class="o">)</span>
</pre></div>


<p>can be rewritten as:</p>
<div class="codehilite"><pre><span></span><span class="n">allFirsts</span> <span class="n">l1</span> <span class="n">l2</span> <span class="bp">&lt;-&gt;</span> <span class="n">l2</span><span class="bp">.</span><span class="n">map</span> <span class="n">prod</span><span class="bp">.</span><span class="n">fst</span> <span class="bp">=</span> <span class="n">l1</span>
</pre></div>


<p>The second form is not a complete definition.  How can I use this form as a definition?</p>

#### [ Chris Hughes (Aug 28 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Inductive%20definitions/near/132926525):
<p><code>def allFirsts {t1 t2} (l1 : list t1) (l2 : list (t1 × t2)) : Prop := l2.map prod.fst = l1</code></p>

#### [ Kevin Buzzard (Aug 28 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Inductive%20definitions/near/132926967):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span>

<span class="kn">inductive</span> <span class="n">allFirsts</span> <span class="o">{</span><span class="n">t1</span><span class="o">}</span> <span class="o">{</span><span class="n">t2</span><span class="o">}</span> <span class="o">:</span> <span class="n">list</span> <span class="n">t1</span> <span class="bp">→</span> <span class="n">list</span> <span class="o">(</span><span class="n">t1</span> <span class="bp">×</span> <span class="n">t2</span><span class="o">)</span> <span class="bp">→</span> <span class="kt">Prop</span>
 <span class="bp">|</span> <span class="n">AFNil</span> <span class="o">:</span> <span class="n">allFirsts</span> <span class="n">list</span><span class="bp">.</span><span class="n">nil</span> <span class="n">list</span><span class="bp">.</span><span class="n">nil</span>
 <span class="bp">|</span> <span class="n">AFCons</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">fx</span> <span class="n">fy</span> <span class="n">r</span> <span class="n">r&#39;</span><span class="o">,</span> <span class="n">allFirsts</span> <span class="n">r</span> <span class="n">r&#39;</span> <span class="bp">→</span> <span class="n">allFirsts</span> <span class="o">(</span><span class="n">fx</span><span class="bp">::</span><span class="n">r</span><span class="o">)</span> <span class="o">((</span><span class="n">fx</span><span class="o">,</span><span class="n">fy</span><span class="o">)</span><span class="bp">::</span><span class="n">r&#39;</span><span class="o">)</span>

<span class="kn">example</span> <span class="o">{</span><span class="n">t1</span> <span class="n">t2</span><span class="o">}</span> <span class="o">(</span><span class="n">l1</span> <span class="o">:</span> <span class="n">list</span> <span class="n">t1</span><span class="o">)</span> <span class="o">(</span><span class="n">l2</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">t1</span> <span class="bp">×</span> <span class="n">t2</span><span class="o">))</span> <span class="o">:</span>
<span class="n">allFirsts</span> <span class="n">l1</span> <span class="n">l2</span> <span class="bp">&lt;-&gt;</span> <span class="n">l2</span><span class="bp">.</span><span class="n">map</span> <span class="n">prod</span><span class="bp">.</span><span class="n">fst</span> <span class="bp">=</span> <span class="n">l1</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">split</span><span class="o">,</span>
    <span class="n">intro</span> <span class="n">H</span><span class="o">,</span>
    <span class="n">induction</span> <span class="n">H</span><span class="o">,</span>
    <span class="n">refl</span><span class="o">,</span>
    <span class="n">simpa</span><span class="o">,</span>
  <span class="n">intro</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">induction</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">induction</span> <span class="n">l2</span> <span class="k">with</span> <span class="n">f12</span> <span class="n">l2</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">allFirsts</span><span class="bp">.</span><span class="n">AFNil</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">f12</span> <span class="k">with</span> <span class="n">f1</span> <span class="n">f2</span><span class="o">,</span>
  <span class="n">refine</span> <span class="n">allFirsts</span><span class="bp">.</span><span class="n">AFCons</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">l2_ih</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


{% endraw %}
