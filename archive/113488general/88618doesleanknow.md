---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/88618doesleanknow.html
---

## Stream: [general](index.html)
### Topic: [does lean know?](88618doesleanknow.html)

---


{% raw %}
#### [ Sean Leather (Mar 01 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/does%20lean%20know%3F/near/123130945):
<p>Is this in the standard library or mathlib?</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">if_distrib</span> <span class="o">{</span><span class="n">c</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">[</span><span class="n">decidable</span> <span class="n">c</span><span class="o">]</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">}</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">}:</span>
  <span class="n">f</span> <span class="o">(</span><span class="k">if</span> <span class="n">c</span> <span class="k">then</span> <span class="n">a</span> <span class="k">else</span> <span class="n">b</span><span class="o">)</span> <span class="bp">=</span> <span class="k">if</span> <span class="n">c</span> <span class="k">then</span> <span class="n">f</span> <span class="n">a</span> <span class="k">else</span> <span class="n">f</span> <span class="n">b</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">by_cases</span> <span class="n">h</span> <span class="o">:</span> <span class="n">c</span><span class="bp">;</span> <span class="o">[</span><span class="n">simp</span> <span class="o">[</span><span class="n">if_pos</span> <span class="n">h</span><span class="o">],</span> <span class="n">simp</span> <span class="o">[</span><span class="n">if_neg</span> <span class="n">h</span><span class="o">]]</span>
</pre></div>

#### [ Sean Leather (Mar 01 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/does%20lean%20know%3F/near/123131013):
<p><span class="user-mention" data-user-email="kc_kennylau@yahoo.com.hk" data-user-id="110064">@Kenny Lau</span>: FYI, the topic title is in homage to your questions. <span class="emoji emoji-1f642" title="simple smile">:simple_smile:</span></p>

#### [ Kenny Lau (Mar 01 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/does%20lean%20know%3F/near/123131018):
<p>:D</p>


{% endraw %}
