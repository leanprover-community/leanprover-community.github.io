---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/72933hascoetosortonset.html
---

## Stream: [general](index.html)
### Topic: [`has_coe_to_sort` on set](72933hascoetosortonset.html)

---


{% raw %}
#### [ Kevin Buzzard (Jul 16 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60has_coe_to_sort%60%20on%20set/near/129747338):
<p>What am I doing wrong:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">set</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">:</span> <span class="n">has_coe_to_sort</span> <span class="o">(</span><span class="n">set</span> <span class="n">X</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span> <span class="c1">-- works</span>
<span class="kn">theorem</span> <span class="n">foo</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">:</span> <span class="n">has_coe_to_sort</span> <span class="o">(</span><span class="n">set</span> <span class="n">X</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span> <span class="c1">-- error</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">tactic.mk_instance failed to generate instance for</span>
<span class="cm">  has_coe_to_sort (set X)</span>
<span class="cm">state:</span>
<span class="cm">X : Type</span>
<span class="cm">⊢ has_coe_to_sort (set X)</span>
<span class="cm">-/</span>
</pre></div>


<p>?</p>

#### [ Mario Carneiro (Jul 16 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60has_coe_to_sort%60%20on%20set/near/129747359):
<p>check your universe variables</p>

#### [ Kevin Buzzard (Jul 16 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60has_coe_to_sort%60%20on%20set/near/129747379):
<p><em>boggle</em></p>

#### [ Kevin Buzzard (Jul 16 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60has_coe_to_sort%60%20on%20set/near/129747752):
<p>I remember now, I've seen this before. <code>definition foo...</code> works, <code>example</code> works, <code>theorem</code> doesn't. Thanks!</p>

#### [ Mario Carneiro (Jul 16 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60has_coe_to_sort%60%20on%20set/near/129747757):
<p><code>theorem</code> works too if you assign the universe variables first</p>

#### [ Kenny Lau (Jul 16 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60has_coe_to_sort%60%20on%20set/near/129747806):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">set</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">:</span> <span class="n">has_coe_to_sort</span> <span class="o">(</span><span class="n">set</span> <span class="n">X</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span> <span class="c1">-- works</span>
<span class="kn">theorem</span> <span class="n">foo</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">:</span> <span class="n">has_coe_to_sort</span><span class="bp">.</span><span class="o">{</span><span class="mi">1</span> <span class="mi">2</span><span class="o">}</span> <span class="o">(</span><span class="n">set</span> <span class="n">X</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span> <span class="c1">-- works</span>
</pre></div>

#### [ Mario Carneiro (Jul 16 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60has_coe_to_sort%60%20on%20set/near/129747807):
<p>but <code>has_coe_to_fun</code> is an instance so it's best to use <code>instance</code> or <code>def</code></p>

#### [ Kenny Lau (Jul 16 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60has_coe_to_sort%60%20on%20set/near/129747808):
<p>you mean this?</p>

#### [ Mario Carneiro (Jul 16 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60has_coe_to_sort%60%20on%20set/near/129747812):
<p>yes</p>

#### [ Kenny Lau (Jul 16 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60has_coe_to_sort%60%20on%20set/near/129747820):
<p>because the default Sort is Sort 0?</p>

#### [ Kenny Lau (Jul 16 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60has_coe_to_sort%60%20on%20set/near/129747825):
<p>so I have to say 2?</p>

#### [ Mario Carneiro (Jul 16 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60has_coe_to_sort%60%20on%20set/near/129747889):
<p>I think you only need to state the second one, which is the universe level of the target type, which must be <code>Sort u</code> for some <code>u</code></p>

#### [ Kenny Lau (Jul 16 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60has_coe_to_sort%60%20on%20set/near/129747899):
<p>how do I state the second one without stating the first one?</p>

#### [ Mario Carneiro (Jul 16 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60has_coe_to_sort%60%20on%20set/near/129747902):
<p><code>.{_ 2}</code></p>

#### [ Kenny Lau (Jul 16 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60has_coe_to_sort%60%20on%20set/near/129747911):
<p>well</p>

#### [ Mario Carneiro (Jul 16 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60has_coe_to_sort%60%20on%20set/near/129747932):
<p>I realize it doesn't save any chars, but it does save some working-out</p>

#### [ Sean Leather (Jul 16 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%60has_coe_to_sort%60%20on%20set/near/129747981):
<blockquote>
<p>I realize it doesn't save any chars, but it does save some working-out</p>
</blockquote>
<p>But one should work out to stay Lean... <span class="emoji emoji-1f914" title="thinking face">:thinking_face:</span></p>


{% endraw %}
