---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/17472funextcongrfailsinconv.html
---

## Stream: [general](index.html)
### Topic: ["funext, congr" fails in conv](17472funextcongrfailsinconv.html)

---


{% raw %}
#### [ Kenny Lau (Sep 10 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22funext%2C%20congr%22%20fails%20in%20conv/near/133645086):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">finset</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">big_operators</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="o">[</span><span class="n">comm_monoid</span> <span class="n">β</span><span class="o">]</span> <span class="o">:</span> <span class="n">s</span><span class="bp">.</span><span class="n">prod</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">s</span><span class="bp">.</span><span class="n">attach</span><span class="bp">.</span><span class="n">prod</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="o">(</span><span class="mi">1</span><span class="o">:</span><span class="n">β</span><span class="o">)))</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">conv</span> <span class="o">{</span> <span class="n">to_lhs</span><span class="o">,</span> <span class="n">congr</span><span class="o">,</span> <span class="n">skip</span><span class="o">,</span> <span class="n">funext</span><span class="o">,</span> <span class="n">congr</span> <span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Sep 10 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22funext%2C%20congr%22%20fails%20in%20conv/near/133645096):
<div class="codehilite"><pre><span></span><span class="n">Tactic</span> <span class="n">State</span>

<span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="err">?</span><span class="o">,</span>
<span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="err">?</span><span class="o">,</span>
<span class="n">s</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">comm_monoid</span> <span class="n">β</span><span class="o">,</span>
<span class="n">x</span> <span class="o">:</span> <span class="n">α</span>
<span class="bp">|</span> <span class="n">finset</span><span class="bp">.</span><span class="n">prod</span> <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">attach</span> <span class="n">s</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="bp">_</span><span class="n">x</span> <span class="o">:</span> <span class="o">{</span><span class="n">x</span> <span class="bp">//</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">s</span><span class="o">}),</span> <span class="mi">1</span><span class="o">)</span>
</pre></div>


<div class="codehilite"><pre><span></span><span class="n">unify</span> <span class="n">tactic</span> <span class="n">failed</span><span class="o">,</span> <span class="n">failed</span> <span class="n">to</span> <span class="n">unify</span>
  <span class="err">?</span><span class="n">m_1</span> <span class="o">:</span> <span class="n">finset</span><span class="bp">.</span><span class="n">prod</span> <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">attach</span> <span class="n">s</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="bp">_</span><span class="n">x</span> <span class="o">:</span> <span class="o">{</span><span class="n">x</span> <span class="bp">//</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">s</span><span class="o">}),</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">=</span> <span class="err">?</span><span class="n">m_2</span> <span class="n">x</span>
<span class="n">and</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="err">?</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="err">?</span><span class="o">}</span> <span class="o">[</span><span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">comm_monoid</span> <span class="n">β</span><span class="o">]</span> <span class="o">(</span><span class="n">s</span> <span class="n">s_1</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">e_4</span> <span class="o">:</span> <span class="n">s</span> <span class="bp">=</span> <span class="n">s_1</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="n">f_1</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span>
   <span class="o">(</span><span class="n">e_5</span> <span class="o">:</span> <span class="n">f</span> <span class="bp">=</span> <span class="n">f_1</span><span class="o">),</span> <span class="n">congr</span> <span class="o">(</span><span class="n">congr_arg</span> <span class="n">finset</span><span class="bp">.</span><span class="n">prod</span> <span class="n">e_4</span><span class="o">)</span> <span class="n">e_5</span><span class="o">)</span>
    <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">attach</span> <span class="n">s</span><span class="o">)</span>
    <span class="err">?</span><span class="n">m_3</span>
    <span class="err">?</span><span class="n">m_4</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="bp">_</span><span class="n">x</span> <span class="o">:</span> <span class="o">{</span><span class="n">x</span> <span class="bp">//</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">s</span><span class="o">}),</span> <span class="mi">1</span><span class="o">)</span>
    <span class="err">?</span><span class="n">m_5</span>
    <span class="err">?</span><span class="n">m_6</span>
  <span class="o">:</span> <span class="n">finset</span><span class="bp">.</span><span class="n">prod</span> <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">attach</span> <span class="n">s</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="bp">_</span><span class="n">x</span> <span class="o">:</span> <span class="o">{</span><span class="n">x</span> <span class="bp">//</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">s</span><span class="o">}),</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">=</span> <span class="n">finset</span><span class="bp">.</span><span class="n">prod</span> <span class="err">?</span><span class="n">m_3</span> <span class="err">?</span><span class="n">m_5</span>
<span class="n">state</span><span class="o">:</span>
<span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="err">?</span><span class="o">,</span>
<span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="err">?</span><span class="o">,</span>
<span class="n">s</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">comm_monoid</span> <span class="n">β</span><span class="o">,</span>
<span class="n">x</span> <span class="o">:</span> <span class="n">α</span>
<span class="err">⊢</span> <span class="n">finset</span><span class="bp">.</span><span class="n">prod</span> <span class="o">(</span><span class="n">finset</span><span class="bp">.</span><span class="n">attach</span> <span class="n">s</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="bp">_</span><span class="n">x</span> <span class="o">:</span> <span class="o">{</span><span class="n">x</span> <span class="bp">//</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">s</span><span class="o">}),</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">=</span> <span class="err">?</span><span class="n">m_1</span> <span class="n">x</span>
</pre></div>

#### [ Kenny Lau (Sep 10 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22funext%2C%20congr%22%20fails%20in%20conv/near/133674125):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span></p>

#### [ Kenny Lau (Sep 15 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22funext%2C%20congr%22%20fails%20in%20conv/near/134001585):
<p>is nobody going to care about this</p>

#### [ Scott Morrison (Sep 15 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22funext%2C%20congr%22%20fails%20in%20conv/near/134001595):
<p>Hmm, I care a little :-) I would like more tactics inside conv, too :-)</p>

#### [ Kenny Lau (Sep 15 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22funext%2C%20congr%22%20fails%20in%20conv/near/134001767):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span></p>

#### [ Mario Carneiro (Sep 15 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22funext%2C%20congr%22%20fails%20in%20conv/near/134001871):
<p>There is very little I can do about bugs in <code>conv</code></p>


{% endraw %}
