---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/24531guesstheerror.html
---

## Stream: [general](index.html)
### Topic: [guess the error](24531guesstheerror.html)

---


{% raw %}
#### [ Kevin Buzzard (Mar 29 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/guess%20the%20error/near/124371146):
<div class="codehilite"><pre><span></span>theorem  easy : let H : 0  &lt;  2  := dec_trivial in
(⟨0,H⟩ : fin 2) = ⟨0,H⟩ := rfl
</pre></div>

#### [ Gabriel Ebner (Mar 29 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/guess%20the%20error/near/124372404):
<p>Ah, I guess there are two ways in which a lemma can fail to be rfl: either the proof is not rfl, or the proposition is not an equation.</p>

#### [ Gabriel Ebner (Mar 29 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/guess%20the%20error/near/124372463):
<p>Note that <code>easy</code> would not work as a simp lemma, since it matches on the <code>let</code> instead of the <code>fin.mk</code> (and the exact decidability proof):</p>
<div class="codehilite"><pre><span></span><span class="bp">#</span><span class="kn">eval</span> <span class="n">simp_lemmas</span><span class="bp">.</span><span class="n">mk</span><span class="bp">.</span><span class="n">add_simp</span> <span class="bp">``</span><span class="n">easy</span> <span class="bp">&gt;&gt;=</span> <span class="n">simp_lemmas</span><span class="bp">.</span><span class="n">pp</span> <span class="bp">&gt;&gt;=</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">trace</span>
<span class="c1">-- simplification rules for iff</span>
<span class="c1">-- [easy] #0, let H : 0 &lt; 2 := _ in ⟨0, H⟩ = ⟨0, H⟩ ↦ true</span>
</pre></div>

#### [ Gabriel Ebner (Mar 29 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/guess%20the%20error/near/124372537):
<p>To explain: <code>lemma foo : ... = ... := rfl</code> is only intended to be used for simp-lemmas.  And then it <em>literally</em> needs to be <code>rfl</code> on the right-hand side.  Not <code>eq.refl _</code>, not <code>by refl</code>, but <code>rfl</code>.</p>

#### [ Gabriel Ebner (Mar 29 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/guess%20the%20error/near/124372551):
<p>So in your case you can just use <code>by refl</code> or <code>eq.refl _</code> and <code>easy</code> will work.</p>

#### [ Kevin Buzzard (Mar 29 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/guess%20the%20error/near/124376162):
<p>So this let isn't just syntactic sugar?</p>

#### [ Sebastian Ullrich (Mar 30 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/guess%20the%20error/near/124417030):
<p>No, let is a primitive term kind supported by the kernel</p>


{% endraw %}
