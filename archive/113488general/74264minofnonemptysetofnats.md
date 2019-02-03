---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/74264minofnonemptysetofnats.html
---

## Stream: [general](index.html)
### Topic: [min of non-empty set of nats](74264minofnonemptysetofnats.html)

---


{% raw %}
#### [ Kevin Buzzard (Jul 30 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/min%20of%20non-empty%20set%20of%20nats/near/130570396):
<p>Presumably this is easy?</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="n">p</span> <span class="n">n</span><span class="o">)</span> <span class="bp">→</span> <span class="bp">∃!</span> <span class="n">m</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="o">(</span><span class="n">p</span> <span class="n">m</span> <span class="bp">∧</span> <span class="bp">∀</span> <span class="n">d</span><span class="o">,</span> <span class="n">d</span> <span class="bp">&lt;</span> <span class="n">m</span> <span class="bp">→</span> <span class="bp">¬</span> <span class="o">(</span><span class="n">p</span> <span class="n">d</span><span class="o">))</span> <span class="o">:=</span>
</pre></div>

#### [ Kenny Lau (Jul 30 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/min%20of%20non-empty%20set%20of%20nats/near/130570547):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">[</span><span class="n">decidable_pred</span> <span class="n">p</span><span class="o">]</span> <span class="o">:</span>
  <span class="o">(</span><span class="bp">∃</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="n">p</span> <span class="n">n</span><span class="o">)</span> <span class="bp">→</span> <span class="bp">∃!</span> <span class="n">m</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="o">(</span><span class="n">p</span> <span class="n">m</span> <span class="bp">∧</span> <span class="bp">∀</span> <span class="n">d</span><span class="o">,</span> <span class="n">d</span> <span class="bp">&lt;</span> <span class="n">m</span> <span class="bp">→</span> <span class="bp">¬</span> <span class="o">(</span><span class="n">p</span> <span class="n">d</span><span class="o">))</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">H</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">nat</span><span class="bp">.</span><span class="n">find</span> <span class="n">H</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">nat</span><span class="bp">.</span><span class="n">find_spec</span> <span class="n">H</span><span class="o">,</span> <span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">find_min</span> <span class="n">H</span><span class="bp">⟩</span><span class="o">,</span>
<span class="bp">λ</span> <span class="n">y</span> <span class="n">hy</span><span class="o">,</span> <span class="n">le_antisymm</span> <span class="o">(</span><span class="n">le_of_not_gt</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">H2</span><span class="o">,</span> <span class="n">hy</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">find</span> <span class="n">H</span><span class="o">)</span> <span class="n">H2</span> <span class="err">$</span> <span class="n">nat</span><span class="bp">.</span><span class="n">find_spec</span> <span class="n">H</span><span class="o">)</span> <span class="err">$</span>
<span class="n">nat</span><span class="bp">.</span><span class="n">find_min&#39;</span> <span class="n">H</span> <span class="n">hy</span><span class="bp">.</span><span class="mi">1</span><span class="bp">⟩</span>
</pre></div>

#### [ Kevin Buzzard (Jul 30 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/min%20of%20non-empty%20set%20of%20nats/near/130570608):
<p>Thanks Kenny.</p>


{% endraw %}
