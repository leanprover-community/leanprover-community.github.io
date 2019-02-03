---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/25137inductivelydefinedfinsupp.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [inductively-defined finsupp?](https://leanprover-community.github.io/archive/113488general/25137inductivelydefinedfinsupp.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Mar 29 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductively-defined%20finsupp%3F/near/124364521):
<p>Can we define finsupp A B inductively as a set of the type (A -&gt; B)?</p>

#### [ Johannes Hölzl (Mar 29 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductively-defined%20finsupp%3F/near/124365156):
<p>I'm not sure what you mean?<br>
If you want to define it as an inductive like lists, i.e. the constant zero function, and a constructor to insert an element: this doesn't work, it requires a quotient over the sequence of at which point you add an element, also the constructor requires a proof that the inserted element was zero in the function is not zero. <br>
We can slightly change the definition to:</p>
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">finsupp</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="o">[</span><span class="n">has_zero</span> <span class="n">β</span><span class="o">]</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">to_fun</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span>
<span class="o">(</span><span class="n">fintype_support</span> <span class="o">:</span> <span class="n">fintype</span> <span class="o">{</span><span class="n">a</span> <span class="bp">|</span> <span class="n">to_fun</span> <span class="n">a</span> <span class="bp">≠</span> <span class="mi">0</span><span class="o">})</span>
</pre></div>


<p>Which would be a good idea...</p>

#### [ Kenny Lau (Mar 29 2018 at 14:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductively-defined%20finsupp%3F/near/124365223):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> I mean an inductively-defined set</p>

#### [ Johannes Hölzl (Mar 29 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductively-defined%20finsupp%3F/near/124365286):
<p>You mean the set <code>{f | finite {a | f a ≠ 0 }}</code>?<br>
You can:</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">is_finsupp</span> <span class="o">[</span><span class="n">has_zero</span> <span class="n">B</span><span class="o">]</span> <span class="o">:</span> <span class="o">(</span><span class="n">A</span> <span class="bp">-&gt;</span> <span class="n">B</span><span class="o">)</span> <span class="bp">-&gt;</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">zero</span><span class="o">:</span> <span class="n">is_finsupp</span> <span class="o">(</span><span class="err">\</span><span class="n">x</span><span class="o">,</span> <span class="mi">0</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">insert</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span><span class="o">}</span> <span class="o">:</span> <span class="n">is_finsupp</span> <span class="n">f</span> <span class="bp">-&gt;</span> <span class="n">is_finsupp</span> <span class="o">(</span><span class="err">\</span><span class="n">x</span><span class="o">,</span> <span class="k">if</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">a</span> <span class="k">then</span> <span class="n">b</span> <span class="k">else</span> <span class="n">f</span> <span class="n">x</span><span class="o">)</span>
</pre></div>

#### [ Kenny Lau (Mar 29 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductively-defined%20finsupp%3F/near/124365330):
<p>right</p>

#### [ Kenny Lau (Mar 29 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductively-defined%20finsupp%3F/near/124365335):
<p>and why isn't this used?</p>

#### [ Johannes Hölzl (Mar 29 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inductively-defined%20finsupp%3F/near/124365385):
<p>We want to something which is a type and isomorph to the subtype of this set. This allows us to define type class instances. The current version also gives us (mostly) nice computational rules for the function and for the support.</p>


{% endraw %}
