---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/26603maxminoflist.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [max/min of list](https://leanprover-community.github.io/archive/113488general/26603maxminoflist.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (May 01 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/max/min%20of%20list/near/125938032):
<p>maybe you'll find this useful:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">list</span><span class="bp">.</span><span class="n">max</span> <span class="o">:</span> <span class="n">α</span> <span class="o">:=</span>
<span class="n">list</span><span class="bp">.</span><span class="n">foldr</span> <span class="n">max</span> <span class="o">(</span><span class="n">inhabited</span><span class="bp">.</span><span class="n">default</span> <span class="bp">_</span><span class="o">)</span> <span class="n">L</span>

<span class="n">def</span> <span class="n">list</span><span class="bp">.</span><span class="n">min</span> <span class="o">:</span> <span class="n">α</span> <span class="o">:=</span>
<span class="n">list</span><span class="bp">.</span><span class="n">foldr</span> <span class="n">min</span> <span class="o">(</span><span class="n">inhabited</span><span class="bp">.</span><span class="n">default</span> <span class="bp">_</span><span class="o">)</span> <span class="n">L</span>

<span class="kn">theorem</span> <span class="n">list</span><span class="bp">.</span><span class="n">le_max</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">L</span><span class="o">,</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">L</span><span class="bp">.</span><span class="n">max</span> <span class="o">:=</span>
<span class="n">list</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">L</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">false</span><span class="bp">.</span><span class="n">elim</span><span class="o">)</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">hd</span> <span class="n">tl</span> <span class="n">ih</span> <span class="n">x</span> <span class="n">hx</span><span class="o">,</span>
<span class="n">or</span><span class="bp">.</span><span class="n">cases_on</span> <span class="n">hx</span>
  <span class="o">(</span><span class="k">assume</span> <span class="n">H</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">hd</span><span class="o">,</span> <span class="n">H</span><span class="bp">.</span><span class="n">symm</span> <span class="bp">▸</span> <span class="n">le_max_left</span> <span class="n">hd</span> <span class="n">tl</span><span class="bp">.</span><span class="n">max</span><span class="o">)</span>
  <span class="o">(</span><span class="k">assume</span> <span class="n">H</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">tl</span><span class="o">,</span> <span class="n">le_trans</span> <span class="o">(</span><span class="n">ih</span> <span class="n">x</span> <span class="n">H</span><span class="o">)</span> <span class="o">(</span><span class="n">le_max_right</span> <span class="n">hd</span> <span class="n">tl</span><span class="bp">.</span><span class="n">max</span><span class="o">))</span>

<span class="kn">theorem</span> <span class="n">list</span><span class="bp">.</span><span class="n">min_le</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">L</span><span class="o">,</span> <span class="n">L</span><span class="bp">.</span><span class="n">min</span> <span class="bp">≤</span> <span class="n">x</span> <span class="o">:=</span>
<span class="n">list</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">L</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">false</span><span class="bp">.</span><span class="n">elim</span><span class="o">)</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">hd</span> <span class="n">tl</span> <span class="n">ih</span> <span class="n">x</span> <span class="n">hx</span><span class="o">,</span>
<span class="n">or</span><span class="bp">.</span><span class="n">cases_on</span> <span class="n">hx</span>
  <span class="o">(</span><span class="k">assume</span> <span class="n">H</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">hd</span><span class="o">,</span> <span class="n">H</span><span class="bp">.</span><span class="n">symm</span> <span class="bp">▸</span> <span class="n">min_le_left</span> <span class="n">hd</span> <span class="n">tl</span><span class="bp">.</span><span class="n">min</span><span class="o">)</span>
  <span class="o">(</span><span class="k">assume</span> <span class="n">H</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">tl</span><span class="o">,</span> <span class="n">le_trans</span> <span class="o">(</span><span class="n">min_le_right</span> <span class="n">hd</span> <span class="n">tl</span><span class="bp">.</span><span class="n">min</span><span class="o">)</span> <span class="o">(</span><span class="n">ih</span> <span class="n">x</span> <span class="n">H</span><span class="o">))</span>
</pre></div>

#### [ Johan Commelin (May 01 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/max/min%20of%20list/near/125938092):
<p>I'll take look. First it's lunch time...</p>

#### [ Chris Hughes (May 02 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/max/min%20of%20list/near/126002895):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span>  That doesn't take the max, it takes the max of the list and the default value. You won't be able to prove <code>L.max \in L</code> You should define it as default for nil, and then list.foldr max L.head otherwise.</p>

#### [ Kenny Lau (May 02 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/max/min%20of%20list/near/126003001):
<p>aha</p>


{% endraw %}
