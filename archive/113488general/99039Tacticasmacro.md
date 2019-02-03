---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/99039Tacticasmacro.html
---

## Stream: [general](index.html)
### Topic: [Tactic as macro](99039Tacticasmacro.html)

---


{% raw %}
#### [ Nima (Apr 24 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20as%20macro/near/125622203):
<p>Is there anyway I can define a tactic (or something local to a proof) that does a fixed number of steps, so I would not need to repeat the whole thing multiple times? For example, a tactic or local definition name <code>finish_it</code> that does the following:</p>
<div class="codehilite"><pre><span></span><span class="n">cases</span> <span class="n">ind1</span>
<span class="bp">;</span> <span class="n">cases</span> <span class="n">ind2</span>
<span class="bp">;</span> <span class="n">cases</span> <span class="n">ind3</span>
<span class="bp">;</span> <span class="n">unfold</span> <span class="n">func</span> <span class="n">at</span> <span class="n">hh</span>
<span class="bp">;</span> <span class="n">try</span> <span class="o">{</span> <span class="n">contradiction</span> <span class="o">}</span>
<span class="bp">;</span> <span class="n">done</span>
</pre></div>

#### [ Kenny Lau (Apr 24 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20as%20macro/near/125622204):
<p><code>iterate</code></p>

#### [ Kevin Buzzard (Apr 24 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20as%20macro/near/125622355):
<p>I am concerned that your tactic might need to take some inputs (ind1, ind2 etc).</p>

#### [ Kevin Buzzard (Apr 24 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20as%20macro/near/125622356):
<p>if it didn't take any inputs then Programming In Lean explains how to do this</p>

#### [ Kenny Lau (Apr 24 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20as%20macro/near/125622374):
<div class="codehilite"><pre><span></span><span class="n">iterate</span> <span class="mi">3</span> <span class="o">{</span> <span class="n">cases</span> <span class="n">ind1</span>
<span class="bp">;</span> <span class="n">cases</span> <span class="n">ind2</span>
<span class="bp">;</span> <span class="n">cases</span> <span class="n">ind3</span>
<span class="bp">;</span> <span class="n">unfold</span> <span class="n">func</span> <span class="n">at</span> <span class="n">hh</span>
<span class="bp">;</span> <span class="n">try</span> <span class="o">{</span> <span class="n">contradiction</span> <span class="o">}</span>
<span class="bp">;</span> <span class="n">done</span> <span class="o">}</span>
</pre></div>

#### [ Kenny Lau (Apr 24 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20as%20macro/near/125622432):
<p>to define tactics locally, (make sure that the names will not change), and then just do</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">finish_it</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span> <span class="bp">`</span><span class="o">[</span> <span class="n">code</span> <span class="o">]</span>
</pre></div>

#### [ Kevin Buzzard (Apr 24 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20as%20macro/near/125622441):
<p>see lines 88 to 91 of</p>

#### [ Kevin Buzzard (Apr 24 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20as%20macro/near/125622442):
<p><a href="https://github.com/kbuzzard/mathlib/commit/5ff51dc6993990e600ddee4857a2e207e62f35d1#diff-26b4491c757c999172218bc6c4da2cb0R88" target="_blank" title="https://github.com/kbuzzard/mathlib/commit/5ff51dc6993990e600ddee4857a2e207e62f35d1#diff-26b4491c757c999172218bc6c4da2cb0R88">https://github.com/kbuzzard/mathlib/commit/5ff51dc6993990e600ddee4857a2e207e62f35d1#diff-26b4491c757c999172218bc6c4da2cb0R88</a></p>

#### [ Kevin Buzzard (Apr 24 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20as%20macro/near/125622449):
<p>to see how I wrote a basic tactic, knowing nothing about metaprogramming in Lean</p>

#### [ Kevin Buzzard (Apr 24 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20as%20macro/near/125622460):
<p>see lines 101 to 105 for the application</p>

#### [ Nima (Apr 24 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20as%20macro/near/125623024):
<p>Thanks, <code> `[code]</code> did the trick.<br>
Now I can write <code>finish_it</code> and the proof is complete.<br>
But suppose I remove the last two lines from <code>finish_it</code> (<code>try { contradiction }</code> and <code>done</code>). Why I cannot write <code>finish_it ; try { ... }</code>. I mean, <code>;</code> does not work, but <code>,</code> does.</p>

#### [ Mario Carneiro (Apr 24 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Tactic%20as%20macro/near/125632538):
<p>This is because <code>try { ... }</code> is an interactive mode tactic, so you need the interactive mode <code>;</code>, so <code>finish_it</code> needs to also be defined in the interactive namespace (<code>tactic.interactive.finish_it</code>) if you want to use it in tactics. If you say <code>finish_it</code> in a <code>begin ... end</code> or <code>by ...</code> block and <code>tactic.interactive.finish_it</code> doesn't exist, then it will assume it is a term of type <code>tactic unit</code> and will find it in the current namespace, but since it's using regular term parsing you won't get nice syntaxes like <code>try { ... }</code> that only work in interactive mode.</p>


{% endraw %}
