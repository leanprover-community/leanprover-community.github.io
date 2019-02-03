---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/67736errorfailedtounify.html
---

## Stream: [general](index.html)
### Topic: [error: failed to unify](67736errorfailedtounify.html)

---


{% raw %}
#### [ Johan Commelin (May 25 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20failed%20to%20unify/near/127084634):
<p>I am at a stage where I am currently hitting errors of the following type</p>
<div class="codehilite"><pre><span></span><span class="n">invalid</span> <span class="n">apply</span> <span class="n">tactic</span><span class="o">,</span> <span class="n">failed</span> <span class="n">to</span> <span class="n">unify</span>
  <span class="n">p</span><span class="bp">.</span><span class="n">fst</span> <span class="bp">=</span> <span class="n">q</span><span class="bp">.</span><span class="n">fst</span>
<span class="k">with</span>
  <span class="err">?</span><span class="n">m_2</span> <span class="bp">=</span> <span class="err">?</span><span class="n">m_3</span>
</pre></div>


<p>I have no clue why Lean can't unify those... probably there are some hidden metavariables somewhere... how do I get more info?</p>

#### [ Johannes Hölzl (May 25 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20failed%20to%20unify/near/127084763):
<p>can you try to use <code>set_option pp.all true</code> and inspect the term again</p>

#### [ Johan Commelin (May 25 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20failed%20to%20unify/near/127085460):
<p>Thanks, the response by Lean was a little bit overwhelming. But it solved my problem!</p>


{% endraw %}
