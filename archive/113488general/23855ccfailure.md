---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/23855ccfailure.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [cc failure](https://leanprover-community.github.io/archive/113488general/23855ccfailure.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Reid Barton (May 16 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20failure/near/126654388):
<p>Is this a bug?</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">x1</span> <span class="n">x2</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">x1</span> <span class="bp">=</span> <span class="n">x2</span><span class="o">)</span>
  <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">(</span><span class="n">hp</span> <span class="o">:</span> <span class="n">p</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span>
  <span class="bp">∃</span> <span class="n">y&#39;</span><span class="o">,</span> <span class="n">p</span> <span class="n">y&#39;</span> <span class="bp">∧</span> <span class="o">(</span><span class="n">x2</span><span class="o">,</span> <span class="n">y&#39;</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="n">x1</span><span class="o">,</span> <span class="n">y</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">existsi</span> <span class="bp">_</span><span class="o">,</span> <span class="n">split</span><span class="o">,</span> <span class="n">exact</span> <span class="n">hp</span><span class="o">,</span> <span class="c1">-- ⊢ (x2, y) = (x1, y)</span>
  <span class="n">cc</span>                          <span class="c1">-- cc tactic failed</span>
<span class="kn">end</span>
</pre></div>

#### [ Reid Barton (May 16 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20failure/near/126654522):
<p>(I know the lemma and proof are strange, this is a minimized version of some real code)</p>

#### [ Reid Barton (May 16 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20failure/near/126654615):
<p>It seems that <code>cc</code> doesn't recognize that the <code>y</code>s are equal because one of them was created by substituting for a metavariable, or something.</p>

#### [ Kenny Lau (May 16 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20failure/near/126654631):
<p><code>subst h</code></p>

#### [ Reid Barton (May 16 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20failure/near/126654692):
<p>I observed this a few days ago as well, but in a setting which was too hard to minimize.</p>

#### [ Kenny Lau (May 16 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20failure/near/126654713):
<p>try <code>set_option pp.all true</code></p>

#### [ Chris Hughes (May 16 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20failure/near/126654714):
<blockquote>
<p><code>subst h</code></p>
</blockquote>
<p><code>rw h</code></p>

#### [ Reid Barton (May 16 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20failure/near/126654717):
<p>stop!</p>

#### [ Chris Hughes (May 16 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20failure/near/126654798):
<p>this works</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">x1</span> <span class="n">x2</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">x1</span> <span class="bp">=</span> <span class="n">x2</span><span class="o">)</span>
  <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">(</span><span class="n">hp</span> <span class="o">:</span> <span class="n">p</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span>
  <span class="bp">∃</span> <span class="n">y&#39;</span><span class="o">,</span> <span class="n">p</span> <span class="n">y&#39;</span> <span class="bp">∧</span> <span class="o">(</span><span class="n">x2</span><span class="o">,</span> <span class="n">y&#39;</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="n">x1</span><span class="o">,</span> <span class="n">y</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">⟨_</span><span class="o">,</span> <span class="n">hp</span><span class="o">,</span> <span class="k">begin</span>
    <span class="n">cc</span><span class="o">,</span>
  <span class="kn">end</span><span class="bp">⟩</span>
</pre></div>


<p>So it seems like a bug.</p>

#### [ Kenny Lau (May 16 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20failure/near/126654801):
<p><code>by cc</code></p>

#### [ Reid Barton (May 16 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20failure/near/126654812):
<p>Yeah, changing <code>cc</code> to <code>exact by cc</code> works also</p>

#### [ Reid Barton (May 16 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20failure/near/126654831):
<p>(And also in my real code.)</p>

#### [ Chris Hughes (May 16 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20failure/near/126654862):
<p>It's to do with the metavariable</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">x1</span> <span class="n">x2</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">x1</span> <span class="bp">=</span> <span class="n">x2</span><span class="o">)</span>
  <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">(</span><span class="n">hp</span> <span class="o">:</span> <span class="n">p</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span>
  <span class="bp">∃</span> <span class="n">y&#39;</span><span class="o">,</span> <span class="n">p</span> <span class="n">y&#39;</span> <span class="bp">∧</span> <span class="o">(</span><span class="n">x2</span><span class="o">,</span> <span class="n">y&#39;</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="n">x1</span><span class="o">,</span> <span class="n">y</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">existsi</span> <span class="n">y</span><span class="o">,</span> <span class="n">split</span><span class="o">,</span> <span class="n">exact</span> <span class="n">hp</span><span class="o">,</span> <span class="c1">-- ⊢ (x2, y) = (x1, y)</span>
  <span class="n">cc</span>                          <span class="c1">-- cc tactic failed</span>
<span class="kn">end</span>
</pre></div>


<p>works</p>

#### [ Kenny Lau (May 16 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20failure/near/126654867):
<p>I thought <code>exact hp</code> unified the metavariable</p>

#### [ Reid Barton (May 16 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20failure/near/126654875):
<p>It does. That's what makes this so confusing.</p>

#### [ Reid Barton (May 16 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20failure/near/126654908):
<p>The displayed proof state is exactly the same whether you write <code>existsi _</code> or <code>existsi y</code></p>

#### [ Reid Barton (May 16 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cc%20failure/near/126654948):
<p>but <code>cc</code> only works in the second case</p>


{% endraw %}
