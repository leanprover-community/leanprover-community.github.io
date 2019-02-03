---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/40432easysubsetsubtypelemma.html
---

## Stream: [general](index.html)
### Topic: [easy subset/subtype lemma](40432easysubsetsubtypelemma.html)

---


{% raw %}
#### [ Kevin Buzzard (Jul 16 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20subset/subtype%20lemma/near/129752088):
<p>I've reduced my goal to</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">U</span> <span class="n">A</span> <span class="n">B</span> <span class="o">:</span> <span class="n">set</span> <span class="n">X</span><span class="o">)</span> <span class="o">:</span> <span class="n">U</span> <span class="err">∩</span> <span class="n">A</span> <span class="bp">=</span> <span class="n">U</span> <span class="err">∩</span> <span class="n">B</span> <span class="bp">↔</span> <span class="o">{</span><span class="n">u</span> <span class="o">:</span> <span class="n">U</span> <span class="bp">|</span> <span class="n">u</span><span class="bp">.</span><span class="n">val</span> <span class="err">∈</span> <span class="n">A</span><span class="o">}</span> <span class="bp">=</span> <span class="o">{</span><span class="n">u</span> <span class="o">:</span> <span class="n">U</span> <span class="bp">|</span> <span class="n">u</span><span class="bp">.</span><span class="n">val</span> <span class="err">∈</span> <span class="n">B</span><span class="o">}</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>Is there a one-liner for this? As it happens I only need the &lt;- direction but it somehow all looks easy.</p>

#### [ Simon Hudon (Jul 16 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20subset/subtype%20lemma/near/129752297):
<p>can you try <code>by ext; dsimp; tauto</code>?</p>

#### [ Simon Hudon (Jul 16 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20subset/subtype%20lemma/near/129752338):
<p>Sorry, no that won't work</p>

#### [ Mario Carneiro (Jul 16 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20subset/subtype%20lemma/near/129752413):
<p>there should be a lemma <code>{x : A | x \in B} = A \cap B</code></p>

#### [ Mario Carneiro (Jul 16 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20subset/subtype%20lemma/near/129752438):
<p>wait, that's not type correct</p>

#### [ Patrick Massot (Jul 16 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20subset/subtype%20lemma/near/129752451):
<p>hence Kevin's <code>.val</code></p>

#### [ Simon Hudon (Jul 16 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20subset/subtype%20lemma/near/129752573):
<p>Second attempt: <code>dsimp [set_eq_def]; apply forall_congr; tauto</code></p>

#### [ Mario Carneiro (Jul 16 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20subset/subtype%20lemma/near/129752609):
<p>I think <code>and.congr_right</code> needs a biconditional version</p>

#### [ Mario Carneiro (Jul 16 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20subset/subtype%20lemma/near/129753490):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">and</span><span class="bp">.</span><span class="n">congr_right_iff</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">:</span> <span class="o">(</span><span class="n">a</span> <span class="bp">∧</span> <span class="n">b</span> <span class="bp">↔</span> <span class="n">a</span> <span class="bp">∧</span> <span class="n">c</span><span class="o">)</span> <span class="bp">↔</span> <span class="o">(</span><span class="n">a</span> <span class="bp">→</span> <span class="o">(</span><span class="n">b</span> <span class="bp">↔</span> <span class="n">c</span><span class="o">))</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">h</span> <span class="n">ha</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">ha</span><span class="o">]</span> <span class="n">at</span> <span class="n">h</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">h</span><span class="o">,</span> <span class="n">and_congr_right</span><span class="bp">⟩</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">U</span> <span class="n">A</span> <span class="n">B</span> <span class="o">:</span> <span class="n">set</span> <span class="n">X</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">U</span> <span class="err">∩</span> <span class="n">A</span> <span class="bp">=</span> <span class="n">U</span> <span class="err">∩</span> <span class="n">B</span> <span class="bp">↔</span> <span class="o">{</span><span class="n">u</span> <span class="o">:</span> <span class="n">U</span> <span class="bp">|</span> <span class="n">u</span><span class="bp">.</span><span class="n">val</span> <span class="err">∈</span> <span class="n">A</span><span class="o">}</span> <span class="bp">=</span> <span class="o">{</span><span class="n">u</span> <span class="o">:</span> <span class="n">U</span> <span class="bp">|</span> <span class="n">u</span><span class="bp">.</span><span class="n">val</span> <span class="err">∈</span> <span class="n">B</span><span class="o">}</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">set</span><span class="bp">.</span><span class="n">set_eq_def</span><span class="o">,</span> <span class="n">and</span><span class="bp">.</span><span class="n">congr_right_iff</span><span class="o">]</span>
</pre></div>

#### [ Kevin Buzzard (Jul 16 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20subset/subtype%20lemma/near/129754062):
<p>Thanks Mario.</p>

#### [ Kevin Buzzard (Jul 16 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/easy%20subset/subtype%20lemma/near/129754286):
<p><span class="user-mention" data-user-id="120726">@Luca Gerolla</span> is doing homotopy theory in Lean and this was all that was left for proving that a function on [0,1] is continuous iff its restriction to [0,1/2] and [1/2,1] is.</p>


{% endraw %}
