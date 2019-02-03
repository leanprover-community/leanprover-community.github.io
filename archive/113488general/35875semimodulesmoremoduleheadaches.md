---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/35875semimodulesmoremoduleheadaches.html
---

## Stream: [general](index.html)
### Topic: [semimodules, more module headaches](35875semimodulesmoremoduleheadaches.html)

---


{% raw %}
#### [ Mario Carneiro (Sep 10 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semimodules%2C%20more%20module%20headaches/near/133678716):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> I had problems with using <code>smul_add'</code> directly on modules, so I had to duplicate the theorems <a href="https://github.com/leanprover/mathlib/blob/b33764d942dc8b1b7f55cace89429c948c1a4b2f/algebra/module.lean#L38-L43" target="_blank" title="https://github.com/leanprover/mathlib/blob/b33764d942dc8b1b7f55cace89429c948c1a4b2f/algebra/module.lean#L38-L43">here</a>. Do you have any ideas?</p>

#### [ Johannes Hölzl (Sep 10 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semimodules%2C%20more%20module%20headaches/near/133679172):
<p>hm, are the problems related to projecting the ring to semirings? I think we might also get problems with field to rings for vector spaces...</p>

#### [ Johan Commelin (Sep 10 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semimodules%2C%20more%20module%20headaches/near/133679278):
<p>I vote for making <code>vector_space</code> notation or abbreviation</p>

#### [ Johannes Hölzl (Sep 10 2018 at 20:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semimodules%2C%20more%20module%20headaches/near/133680412):
<p>Making <code>vector_space</code> an abbreviation is okay for me.<br>
But I'm not sure if this solves our problems here.</p>

#### [ Mario Carneiro (Sep 10 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semimodules%2C%20more%20module%20headaches/near/133680743):
<p>yes, <code>rw</code> fails because it can't derive the semiring instance (at the right time)</p>

#### [ Mario Carneiro (Sep 10 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semimodules%2C%20more%20module%20headaches/near/133680836):
<p>I am going to try implementing a solution I mentioned a while ago and not have <code>module</code> extend <code>add_comm_group</code> but take it as an argument</p>

#### [ Johannes Hölzl (Sep 10 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semimodules%2C%20more%20module%20headaches/near/133681100):
<p>hm, how does this help?</p>

#### [ Mario Carneiro (Sep 10 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semimodules%2C%20more%20module%20headaches/near/133685721):
<p>It avoids the <code>ring ?</code> problem in that typeclass searches for e.g. <code>has_zero A</code> go via <code>add_comm_group A</code> to <code>module ? A</code> and then to <code>ring ?</code></p>

#### [ Mario Carneiro (Sep 10 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semimodules%2C%20more%20module%20headaches/near/133685804):
<p>But I've stumbled on yet another inexplicable lean bug while attempting this. I've only lightly minimized</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">big_operators</span>

<span class="n">universes</span> <span class="n">u</span> <span class="n">v</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span>

<span class="n">class</span> <span class="n">has_scalar</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="n">out_param</span> <span class="err">$</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">(</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="n">smul</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">γ</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">)</span>

<span class="kn">infixr</span> <span class="bp">`</span> <span class="err">•</span> <span class="bp">`</span><span class="o">:</span><span class="mi">73</span> <span class="o">:=</span> <span class="n">has_scalar</span><span class="bp">.</span><span class="n">smul</span>

<span class="n">class</span> <span class="n">module</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="n">out_param</span> <span class="err">$</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="o">[</span><span class="n">out_param</span> <span class="err">$</span> <span class="n">ring</span> <span class="n">α</span><span class="o">]</span>
  <span class="o">[</span><span class="n">add_comm_group</span> <span class="n">β</span><span class="o">]</span> <span class="kn">extends</span> <span class="n">has_scalar</span> <span class="n">α</span> <span class="n">β</span>

<span class="n">class</span> <span class="n">is_submodule</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">}</span> <span class="o">[</span><span class="n">ring</span> <span class="n">α</span><span class="o">]</span>
  <span class="o">[</span><span class="n">add_comm_group</span> <span class="n">β</span><span class="o">]</span> <span class="o">[</span><span class="n">module</span> <span class="n">α</span> <span class="n">β</span><span class="o">]</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">set</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">zero&#39;</span> <span class="o">:</span> <span class="o">(</span><span class="mi">0</span><span class="o">:</span><span class="n">β</span><span class="o">)</span> <span class="err">∈</span> <span class="n">p</span><span class="o">)</span>
<span class="o">(</span><span class="n">add&#39;</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">x</span> <span class="n">y</span><span class="o">},</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">p</span> <span class="bp">→</span> <span class="n">y</span> <span class="err">∈</span> <span class="n">p</span> <span class="bp">→</span> <span class="n">x</span> <span class="bp">+</span> <span class="n">y</span> <span class="err">∈</span> <span class="n">p</span><span class="o">)</span>
<span class="o">(</span><span class="n">smul</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">c</span> <span class="o">{</span><span class="n">x</span><span class="o">},</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">p</span> <span class="bp">→</span> <span class="n">c</span> <span class="err">•</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">p</span><span class="o">)</span>

<span class="kn">namespace</span> <span class="n">is_submodule</span>
<span class="kn">variables</span> <span class="o">[</span><span class="n">ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">add_comm_group</span> <span class="n">β</span><span class="o">]</span> <span class="o">[</span><span class="n">module</span> <span class="n">α</span> <span class="n">β</span><span class="o">]</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="n">set</span> <span class="n">β</span><span class="o">}</span> <span class="o">[</span><span class="n">is_submodule</span> <span class="n">p</span><span class="o">]</span>
<span class="n">include</span> <span class="n">α</span>

<span class="kn">lemma</span> <span class="n">zero</span> <span class="o">:</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="n">β</span><span class="o">)</span> <span class="err">∈</span> <span class="n">p</span> <span class="o">:=</span> <span class="n">zero&#39;</span> <span class="n">α</span> <span class="bp">_</span>

<span class="kn">example</span> <span class="o">:</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="n">β</span><span class="o">)</span> <span class="err">∈</span> <span class="n">p</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">zero</span><span class="o">]</span> <span class="c1">-- fails</span>

<span class="kn">end</span> <span class="n">is_submodule</span>
</pre></div>

#### [ Mario Carneiro (Sep 10 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semimodules%2C%20more%20module%20headaches/near/133685958):
<p><code>by apply zero</code> also fails, but <code>by refine zero</code> works</p>

#### [ Mario Carneiro (Sep 10 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semimodules%2C%20more%20module%20headaches/near/133686066):
<p>the failing instance problem:</p>
<div class="codehilite"><pre><span></span>[class_instances]  class-instance resolution trace
[class_instances] (0) ?x_0 : @is_submodule ?m__fresh.1533.3973 β ?m__fresh.1533.3975 _inst_2 ?m__fresh.1533.3977 p := _inst_4
failed is_def_eq
</pre></div>


{% endraw %}
