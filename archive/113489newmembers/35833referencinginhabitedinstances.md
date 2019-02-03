---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/35833referencinginhabitedinstances.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [referencing inhabited instances](https://leanprover-community.github.io/archive/113489newmembers/35833referencinginhabitedinstances.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Ken Roe (Aug 11 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/referencing%20inhabited%20instances/near/131964186):
<p>If I declare values as inhabited instances, how do I reference the instances?</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">cell</span> <span class="o">:=</span> <span class="n">option</span> <span class="bp">ℕ</span>
<span class="n">def</span> <span class="n">heap</span> <span class="o">:=</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">option</span> <span class="bp">ℕ</span>
<span class="n">def</span> <span class="n">env</span> <span class="o">:=</span> <span class="n">ident</span> <span class="bp">→</span> <span class="bp">ℕ</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">inhabited</span> <span class="n">env</span> <span class="o">:=</span> <span class="bp">⟨λ</span> <span class="n">x</span><span class="o">,</span> <span class="mi">0</span><span class="bp">⟩</span>
<span class="kn">instance</span> <span class="o">:</span> <span class="n">inhabited</span> <span class="n">heap</span> <span class="o">:=</span> <span class="bp">⟨λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">none</span><span class="bp">⟩</span>
<span class="kn">instance</span> <span class="o">:</span> <span class="n">inhabited</span> <span class="n">cell</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">none</span><span class="bp">⟩</span>

<span class="n">def</span> <span class="n">empty_env</span> <span class="n">env</span> <span class="o">:=</span>  <span class="n">env</span><span class="bp">.</span><span class="n">inhabited</span>

<span class="n">def</span> <span class="n">empty_heap</span> <span class="o">:</span> <span class="n">heap</span>  <span class="o">:=</span> <span class="n">heap</span><span class="bp">.</span><span class="n">inhabited</span>

<span class="n">def</span> <span class="n">empty_cell</span> <span class="o">:</span> <span class="n">option</span> <span class="bp">ℕ</span> <span class="o">:=</span> <span class="n">cell</span><span class="bp">.</span><span class="n">inhabited</span>
</pre></div>


<p>The last three "def" constructs don't seem to work.</p>

#### [ Simon Hudon (Aug 11 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/referencing%20inhabited%20instances/near/131964248):
<p>If you write <code>#print inhabited</code> you should see the following appear:</p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">class</span><span class="o">]</span>
<span class="kn">structure</span> <span class="n">inhabited</span> <span class="o">:</span> <span class="n">Sort</span> <span class="n">u</span> <span class="bp">→</span> <span class="n">Sort</span> <span class="o">(</span><span class="n">max</span> <span class="mi">1</span> <span class="n">u</span><span class="o">)</span>
<span class="n">fields</span><span class="o">:</span>
<span class="n">inhabited</span><span class="bp">.</span><span class="n">default</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">c</span> <span class="o">:</span> <span class="n">inhabited</span> <span class="n">α</span><span class="o">],</span> <span class="n">α</span>
</pre></div>


<p>This tells you that <code>default env</code> is what you want.</p>


{% endraw %}
