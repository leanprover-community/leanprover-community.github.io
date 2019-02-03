---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/08893setindefinitedescription.html
---

## Stream: [general](index.html)
### Topic: [set.indefinite_description](08893setindefinitedescription.html)

---


{% raw %}
#### [ Kenny Lau (Dec 04 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set.indefinite_description/near/150884816):
<p>Is it possible to fill in this sorry?</p>
<div class="codehilite"><pre><span></span><span class="n">universes</span> <span class="n">u</span>
<span class="kn">protected</span> <span class="n">def</span> <span class="n">set</span><span class="bp">.</span><span class="n">indefinite_description</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span>
  <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">s</span><span class="o">,</span> <span class="n">p</span> <span class="n">s</span><span class="o">)</span> <span class="o">:</span> <span class="o">{</span> <span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span> <span class="bp">//</span> <span class="n">p</span> <span class="n">s</span><span class="o">}</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Reid Barton (Dec 04 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set.indefinite_description/near/150885388):
<p>I guess you mean without adding <code>noncomputable</code>? Interesting question</p>

#### [ Mario Carneiro (Dec 05 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set.indefinite_description/near/150890461):
<p>yes</p>
<div class="codehilite"><pre><span></span><span class="n">universes</span> <span class="n">u</span>
<span class="kn">protected</span> <span class="n">def</span> <span class="n">set</span><span class="bp">.</span><span class="n">indefinite_description</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span>
  <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">s</span><span class="o">,</span> <span class="n">p</span> <span class="n">s</span><span class="o">)</span> <span class="o">:</span> <span class="o">{</span> <span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span> <span class="bp">//</span> <span class="n">p</span> <span class="n">s</span><span class="o">}</span> <span class="o">:=</span>
<span class="bp">⟨</span><span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">|</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">classical</span><span class="bp">.</span><span class="n">some</span> <span class="n">h</span><span class="o">},</span> <span class="n">classical</span><span class="bp">.</span><span class="n">some_spec</span> <span class="n">h</span><span class="bp">⟩</span>
</pre></div>

#### [ Mario Carneiro (Dec 05 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set.indefinite_description/near/150890503):
<p>I've mentioned before about "trivially computable" types, which includes subtypes of functions returning Prop</p>

#### [ Mario Carneiro (Dec 05 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set.indefinite_description/near/150890525):
<p>Any term of such a type can be made computable with appropriate wrapping</p>

#### [ Mario Carneiro (Dec 05 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set.indefinite_description/near/150890612):
<p>If you meant "without axioms", then no it's not possible, it would imply the axiom of choice</p>

#### [ Mario Carneiro (Dec 05 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set.indefinite_description/near/150890927):
<p>However there is an interesting construction here for <em>definite</em> description with no axioms (well extensionality)</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">set</span><span class="bp">.</span><span class="n">basic</span>

<span class="n">universes</span> <span class="n">u</span>
<span class="kn">protected</span> <span class="n">def</span> <span class="n">set</span><span class="bp">.</span><span class="n">definite_description</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span>
  <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∃!</span> <span class="n">s</span><span class="o">,</span> <span class="n">p</span> <span class="n">s</span><span class="o">)</span> <span class="o">:</span> <span class="o">{</span> <span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span> <span class="bp">//</span> <span class="n">p</span> <span class="n">s</span><span class="o">}</span> <span class="o">:=</span>
<span class="bp">⟨</span><span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">|</span> <span class="bp">∃</span> <span class="n">s</span><span class="o">,</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">s</span> <span class="bp">∧</span> <span class="n">p</span> <span class="n">s</span> <span class="bp">∧</span> <span class="bp">∀</span> <span class="n">y</span><span class="o">,</span> <span class="n">p</span> <span class="n">y</span> <span class="bp">→</span> <span class="n">y</span> <span class="bp">=</span> <span class="n">s</span><span class="o">},</span>
<span class="k">let</span> <span class="bp">⟨</span><span class="n">s</span><span class="o">,</span> <span class="n">ps</span><span class="o">,</span> <span class="n">al</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">h</span> <span class="k">in</span>
<span class="k">have</span> <span class="n">s</span> <span class="bp">=</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">|</span> <span class="bp">∃</span> <span class="n">s</span><span class="o">,</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">s</span> <span class="bp">∧</span> <span class="n">p</span> <span class="n">s</span> <span class="bp">∧</span> <span class="bp">∀</span> <span class="n">y</span><span class="o">,</span> <span class="n">p</span> <span class="n">y</span> <span class="bp">→</span> <span class="n">y</span> <span class="bp">=</span> <span class="n">s</span><span class="o">},</span>
<span class="k">from</span> <span class="n">set</span><span class="bp">.</span><span class="n">ext</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="bp">⟨λ</span> <span class="n">xs</span><span class="o">,</span> <span class="bp">⟨_</span><span class="o">,</span> <span class="n">xs</span><span class="o">,</span> <span class="n">ps</span><span class="o">,</span> <span class="n">al</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">s&#39;</span><span class="o">,</span> <span class="n">xs&#39;</span><span class="o">,</span> <span class="n">ps&#39;</span><span class="o">,</span> <span class="n">al&#39;</span><span class="bp">⟩</span><span class="o">,</span> <span class="o">(</span><span class="n">al&#39;</span> <span class="bp">_</span> <span class="n">ps</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span> <span class="bp">▸</span> <span class="n">xs&#39;</span><span class="bp">⟩</span><span class="o">,</span>
<span class="n">this</span> <span class="bp">▸</span> <span class="n">ps</span><span class="bp">⟩</span>
</pre></div>

#### [ Kenny Lau (Dec 05 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set.indefinite_description/near/150891656):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> so... we can have a "computable" basis?</p>

#### [ Mario Carneiro (Dec 05 2018 at 01:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set.indefinite_description/near/150891676):
<p>"computable" but not computable</p>

#### [ Mario Carneiro (Dec 05 2018 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/set.indefinite_description/near/150891740):
<p>when I revisited bases recently, we discussed changing the definition of a basis from a set to a family over a type. In that case it wouldn't be computationally irrelevant</p>


{% endraw %}
