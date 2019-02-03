---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/49404Unexpectedequationcompilerbehaviour.html
---

## Stream: [general](index.html)
### Topic: [Unexpected equation compiler behaviour](49404Unexpectedequationcompilerbehaviour.html)

---


{% raw %}
#### [ Chris Hughes (Jul 12 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20equation%20compiler%20behaviour/near/129536505):
<p>Is this a bug?</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">xnat</span>
<span class="bp">|</span> <span class="n">zero</span> <span class="o">:</span> <span class="n">xnat</span>
<span class="bp">|</span> <span class="n">succ</span> <span class="o">:</span> <span class="n">xnat</span> <span class="bp">→</span> <span class="n">xnat</span>

<span class="kn">open</span> <span class="n">xnat</span>

<span class="n">def</span> <span class="n">one</span> <span class="o">:=</span> <span class="n">succ</span> <span class="n">zero</span>

<span class="n">def</span> <span class="n">is_even</span> <span class="o">:</span> <span class="n">xnat</span> <span class="bp">→</span> <span class="n">bool</span>
<span class="bp">|</span> <span class="n">zero</span> <span class="o">:=</span> <span class="n">tt</span>
<span class="bp">|</span> <span class="n">one</span> <span class="o">:=</span> <span class="n">ff</span> <span class="c1">-- works, but shouldn&#39;t</span>

<span class="n">def</span> <span class="n">is_even</span> <span class="o">:</span> <span class="n">xnat</span> <span class="bp">→</span> <span class="n">bool</span>
<span class="bp">|</span> <span class="n">zero</span> <span class="o">:=</span> <span class="n">tt</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">succ</span> <span class="n">zero</span><span class="o">)</span> <span class="o">:=</span> <span class="n">ff</span> <span class="c1">-- error, as expected</span>
</pre></div>

#### [ Mario Carneiro (Jul 12 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20equation%20compiler%20behaviour/near/129536612):
<p><code>one</code> is a variable in the first definition</p>

#### [ Reid Barton (Jul 12 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20equation%20compiler%20behaviour/near/129536615):
<p><code>one</code> doesn't have the <code>pattern</code> attribute, so... ^</p>

#### [ Patrick Massot (Jul 12 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20equation%20compiler%20behaviour/near/129542371):
<p>That's a nice one! Note that:</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">xnat</span>
<span class="bp">|</span> <span class="n">zero</span> <span class="o">:</span> <span class="n">xnat</span>
<span class="bp">|</span> <span class="n">succ</span> <span class="o">:</span> <span class="n">xnat</span> <span class="bp">→</span> <span class="n">xnat</span>

<span class="kn">open</span> <span class="n">xnat</span>

<span class="n">def</span> <span class="n">one</span> <span class="o">:=</span> <span class="n">succ</span> <span class="n">zero</span>

<span class="n">def</span> <span class="n">is_even</span> <span class="o">:</span> <span class="n">xnat</span> <span class="bp">→</span> <span class="n">bool</span>
<span class="bp">|</span> <span class="n">zero</span> <span class="o">:=</span> <span class="n">tt</span>
<span class="bp">|</span> <span class="n">one</span> <span class="o">:=</span> <span class="n">ff</span> <span class="c1">-- works, as it should</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">is_even</span> <span class="n">one</span> <span class="o">:=</span> <span class="n">rfl</span> <span class="c1">-- fails, as it should</span>
</pre></div>

#### [ Kenny Lau (Jul 12 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20equation%20compiler%20behaviour/near/129542467):
<blockquote>
<p><code>one</code> is a variable in the first definition</p>
</blockquote>
<p>how does <code>succ zero</code> define a variable?</p>

#### [ Patrick Massot (Jul 12 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20equation%20compiler%20behaviour/near/129542478):
<p>it doesn't</p>

#### [ Kenny Lau (Jul 12 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20equation%20compiler%20behaviour/near/129542486):
<p>then why does it work?</p>

#### [ Chris Hughes (Jul 12 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20equation%20compiler%20behaviour/near/129542491):
<p><code>one</code> doesn't refer to the def it's the same as writing <code>n</code></p>

#### [ Patrick Massot (Jul 12 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20equation%20compiler%20behaviour/near/129542497):
<p>Try replacing <code>one</code> by <code>three</code> in the def of <code>is_even</code></p>

#### [ Patrick Massot (Jul 12 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20equation%20compiler%20behaviour/near/129542531):
<p>Lean is guaranteed to be correct, not to be non-confusing</p>

#### [ Kenny Lau (Jul 12 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20equation%20compiler%20behaviour/near/129542540):
<p>oh!</p>


{% endraw %}
