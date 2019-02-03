---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/45468letwithpropositionintacticmode.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [let with proposition in tactic mode](https://leanprover-community.github.io/archive/113489newmembers/45468letwithpropositionintacticmode.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Dec 13 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/let%20with%20proposition%20in%20tactic%20mode/near/151616438):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span>

<span class="kn">open</span> <span class="n">function</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span><span class="bp">.</span><span class="n">result</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">e</span> <span class="err">←</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">result</span><span class="o">,</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">trace</span> <span class="n">e</span>

<span class="kn">theorem</span> <span class="n">cantor_surjective</span>
  <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">set</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">Hf</span> <span class="o">:</span> <span class="n">surjective</span> <span class="n">f</span><span class="o">)</span> <span class="o">:</span> <span class="n">false</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">let</span> <span class="n">H</span> <span class="o">:=</span> <span class="n">Hf</span> <span class="o">{</span><span class="n">x</span> <span class="bp">|</span> <span class="n">x</span> <span class="err">∉</span> <span class="n">f</span> <span class="n">x</span><span class="o">},</span>
  <span class="n">cases</span> <span class="n">H</span> <span class="k">with</span> <span class="n">D</span> <span class="n">e</span><span class="o">,</span>
  <span class="n">result</span>
  <span class="c1">-- ⊢ (let H : ∃ (a : X), f a = {x : X | x ∉ f x} := Hf {x : X | x ∉ f x} in false) (Exists.intro D e)</span>
<span class="kn">end</span>

<span class="c">/-</span><span class="cm"></span>
<span class="cm">let H : ∃ (a : X), f a = {x : X | x ∉ f x} := _,</span>
<span class="cm">    H_1 : ∃ (a : X), f a = {x : X | x ∉ f x} := _</span>
<span class="cm">in Exists.dcases_on H_1 (λ (D : X) (e : f D = {x : X | x ∉ f x}), ?m_1[H, H_1, D, e])</span>
<span class="cm">-/</span>
</pre></div>

#### [ Kenny Lau (Dec 13 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/let%20with%20proposition%20in%20tactic%20mode/near/151616481):
<p>somehow there's a strange goal if we use <code>let</code> instead of <code>have</code> with a proposition in tactic mode</p>

#### [ Kenny Lau (Dec 13 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/let%20with%20proposition%20in%20tactic%20mode/near/151616542):
<p>compare this:</p>

#### [ Kenny Lau (Dec 13 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/let%20with%20proposition%20in%20tactic%20mode/near/151616547):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span>

<span class="kn">open</span> <span class="n">function</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span><span class="bp">.</span><span class="n">result</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">e</span> <span class="err">←</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">result</span><span class="o">,</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">trace</span> <span class="n">e</span>

<span class="kn">theorem</span> <span class="n">cantor_surjective</span>
  <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">set</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">Hf</span> <span class="o">:</span> <span class="n">surjective</span> <span class="n">f</span><span class="o">)</span> <span class="o">:</span> <span class="n">false</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">have</span> <span class="n">H</span> <span class="o">:=</span> <span class="n">Hf</span> <span class="o">{</span><span class="n">x</span> <span class="bp">|</span> <span class="n">x</span> <span class="err">∉</span> <span class="n">f</span> <span class="n">x</span><span class="o">},</span>
  <span class="n">cases</span> <span class="n">H</span> <span class="k">with</span> <span class="n">D</span> <span class="n">e</span><span class="o">,</span>
  <span class="n">result</span>
  <span class="c1">-- ⊢ false</span>
<span class="kn">end</span>

<span class="c">/-</span><span class="cm"></span>
<span class="cm">Exists.dcases_on (Hf {x : X | x ∉ f x})</span>
<span class="cm">  (λ (D : X) (e : f D = {x : X | x ∉ f x}), ?m_1[Hf {x : X | x ∉ f x}, Hf {x : X | x ∉ f x}, D, e])</span>
<span class="cm">-/</span>
</pre></div>

#### [ Kevin Buzzard (Dec 13 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/let%20with%20proposition%20in%20tactic%20mode/near/151618247):
<p>Moral: don't use <code>let</code> with propositions?</p>

#### [ Kevin Buzzard (Dec 13 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/let%20with%20proposition%20in%20tactic%20mode/near/151618280):
<p>Background: Kenny just watched me giving a live Lean talk and I used <code>let</code> with a proposition :P</p>


{% endraw %}
