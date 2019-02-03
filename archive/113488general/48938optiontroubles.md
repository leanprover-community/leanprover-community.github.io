---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/48938optiontroubles.html
---

## Stream: [general](index.html)
### Topic: [option troubles](48938optiontroubles.html)

---


{% raw %}
#### [ Johan Commelin (Oct 09 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option%20troubles/near/135487811):
<p>I have <code>x : option X</code>, and <code>h : x ≠ none</code>. How do I turn this into a <code>y : X</code> such that <code>x = some y</code>? I want to use <code>option.get</code> and <code>option.is_some</code>. But I can't figure out how to use <code>h</code>.</p>

#### [ Johan Commelin (Oct 09 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option%20troubles/near/135487845):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">option</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">≠</span> <span class="n">none</span><span class="o">)</span> <span class="o">:</span> <span class="n">X</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Johan Commelin (Oct 09 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option%20troubles/near/135487859):
<p>Or something like that. I should probably not just return an <code>y : X</code>, but also the proof that <code>x = some y</code>.</p>

#### [ Chris Hughes (Oct 09 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option%20troubles/near/135488210):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">option</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">≠</span> <span class="n">none</span> <span class="bp">→</span> <span class="o">{</span><span class="n">y</span> <span class="bp">//</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">some</span> <span class="n">y</span><span class="o">}</span> <span class="o">:=</span>
<span class="n">option</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">x</span> <span class="o">(</span><span class="n">absurd</span> <span class="n">rfl</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">y</span> <span class="bp">_</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">y</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span><span class="o">)</span>
</pre></div>


<p>There should be a lemma that says <code>is_some_iff_ne_none</code>, but it seems to be missing.</p>

#### [ Reid Barton (Oct 09 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option%20troubles/near/135488265):
<p>Depending on the use, it might be more convenient to just do the <code>cases</code>, <code>absurd</code> at the usage site</p>

#### [ Johan Commelin (Oct 09 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option%20troubles/near/135488560):
<p>Thanks <span class="user-mention" data-user-id="110044">@Chris Hughes</span> and <span class="user-mention" data-user-id="110032">@Reid Barton</span> !</p>

#### [ Patrick Massot (Oct 09 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option%20troubles/near/135488579):
<p>as in </p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">option</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">≠</span> <span class="n">none</span><span class="o">)</span> <span class="o">:</span> <span class="o">{</span><span class="n">y</span> <span class="bp">//</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">some</span> <span class="n">y</span><span class="o">}</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">cases</span> <span class="n">x</span> <span class="k">with</span> <span class="n">a</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">absurd</span> <span class="o">(</span><span class="k">by</span> <span class="n">simpa</span> <span class="o">[</span><span class="n">h</span><span class="o">])</span> <span class="n">not_false</span><span class="o">,</span>
  <span class="n">exact</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span>
<span class="kn">end</span>
</pre></div>

#### [ Mario Carneiro (Oct 09 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option%20troubles/near/135489285):
<p>there is <code>is_none_iff_eq_none</code>, but nothing connecting <code>is_some</code> and <code>is_none</code>. I guess we need a few more variants</p>

#### [ Mario Carneiro (Oct 09 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/option%20troubles/near/135489316):
<p>but the basic story is <code>option.get</code> is supposed to do this</p>


{% endraw %}
