---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/21444natstrongrecon.html
---

## Stream: [general](index.html)
### Topic: [nat.strong_rec_on](21444natstrongrecon.html)

---


{% raw %}
#### [ Kenny Lau (Sep 14 2018 at 19:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat.strong_rec_on/near/133965949):
<p>Can we make this <code>@[elab_as_eliminator]</code>?</p>

#### [ Kevin Buzzard (Sep 14 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat.strong_rec_on/near/133969734):
<p>How will that change things?</p>

#### [ Chris Hughes (Sep 14 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat.strong_rec_on/near/133969852):
<p>It means it changes the way the motive is inferred, without which, these lemmas are pretty much unusable.</p>

#### [ Kenny Lau (Sep 14 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat.strong_rec_on/near/133970442):
<p>also I just wrote a beta lemma</p>

#### [ Kenny Lau (Sep 14 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/nat.strong_rec_on/near/133970444):
<div class="codehilite"><pre><span></span><span class="n">attribute</span> <span class="o">[</span><span class="n">elab_as_eliminator</span><span class="o">]</span> <span class="n">nat</span><span class="bp">.</span><span class="n">strong_rec_on</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">nat</span><span class="bp">.</span><span class="n">strong_rec_on_beta</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="n">nat</span> <span class="bp">→</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">nat</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">m</span><span class="o">,</span> <span class="n">m</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">p</span> <span class="n">m</span><span class="o">)</span> <span class="bp">→</span> <span class="n">p</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span>
  <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">strong_rec_on</span> <span class="n">n</span> <span class="n">h</span> <span class="o">:</span> <span class="n">p</span> <span class="n">n</span><span class="o">)</span> <span class="bp">=</span> <span class="n">h</span> <span class="n">n</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">m</span> <span class="n">H</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">strong_rec_on</span> <span class="n">m</span> <span class="n">h</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">cases</span> <span class="n">n</span> <span class="k">with</span> <span class="n">n</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">dsimp</span> <span class="n">only</span> <span class="o">[</span><span class="n">nat</span><span class="bp">.</span><span class="n">strong_rec_on</span><span class="o">,</span> <span class="n">or</span><span class="bp">.</span><span class="n">by_cases</span><span class="o">],</span>
    <span class="n">rw</span> <span class="o">[</span><span class="n">dif_neg</span> <span class="o">(</span><span class="n">lt_irrefl</span> <span class="bp">_</span><span class="o">),</span> <span class="n">dif_pos</span> <span class="n">rfl</span><span class="o">],</span>
    <span class="n">congr&#39;</span> <span class="mi">1</span><span class="o">,</span> <span class="n">funext</span> <span class="n">m</span> <span class="n">H</span><span class="o">,</span> <span class="n">cases</span> <span class="n">H</span> <span class="o">},</span>
  <span class="n">dsimp</span> <span class="n">only</span> <span class="o">[</span><span class="n">nat</span><span class="bp">.</span><span class="n">strong_rec_on</span><span class="o">,</span> <span class="n">or</span><span class="bp">.</span><span class="n">by_cases</span><span class="o">],</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">dif_neg</span> <span class="o">(</span><span class="n">lt_irrefl</span> <span class="bp">_</span><span class="o">),</span> <span class="n">dif_pos</span> <span class="n">rfl</span><span class="o">],</span>
  <span class="n">congr&#39;</span> <span class="mi">1</span><span class="o">,</span> <span class="n">funext</span> <span class="n">m</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">H</span> <span class="k">with</span> <span class="n">H1</span> <span class="n">H1</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">rw</span> <span class="o">[</span><span class="n">dif_neg</span> <span class="o">(</span><span class="n">lt_irrefl</span> <span class="bp">_</span><span class="o">)]</span> <span class="o">},</span>
  <span class="n">change</span> <span class="n">m</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="n">at</span> <span class="n">H1</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">dif_pos</span> <span class="n">H1</span><span class="o">,</span> <span class="n">dif_neg</span> <span class="o">(</span><span class="n">lt_irrefl</span> <span class="bp">_</span><span class="o">),</span> <span class="n">dif_pos</span> <span class="n">rfl</span><span class="o">],</span>
  <span class="n">clear</span> <span class="n">H</span><span class="o">,</span> <span class="n">revert</span> <span class="n">m</span> <span class="n">H1</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">nat</span><span class="bp">.</span><span class="n">strong_induction_on</span> <span class="n">n</span><span class="o">,</span>
  <span class="n">intros</span> <span class="n">n</span> <span class="n">ih</span> <span class="n">m</span> <span class="n">H1</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">n</span> <span class="k">with</span> <span class="n">n</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">cases</span> <span class="n">H1</span> <span class="o">},</span>
  <span class="n">dsimp</span> <span class="n">only</span><span class="o">,</span>
  <span class="n">by_cases</span> <span class="n">H2</span> <span class="o">:</span> <span class="n">m</span> <span class="bp">&lt;</span> <span class="n">n</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">rw</span> <span class="o">[</span><span class="n">dif_pos</span> <span class="n">H2</span><span class="o">],</span> <span class="n">apply</span> <span class="n">ih</span><span class="o">,</span> <span class="n">exact</span> <span class="n">nat</span><span class="bp">.</span><span class="n">lt_succ_self</span> <span class="bp">_</span> <span class="o">},</span>
  <span class="n">by_cases</span> <span class="n">H3</span> <span class="o">:</span> <span class="n">m</span> <span class="bp">=</span> <span class="n">n</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">rw</span> <span class="o">[</span><span class="n">dif_neg</span> <span class="n">H2</span><span class="o">,</span> <span class="n">dif_pos</span> <span class="n">H3</span><span class="o">],</span> <span class="n">subst</span> <span class="n">H3</span> <span class="o">},</span>
  <span class="n">exact</span> <span class="n">false</span><span class="bp">.</span><span class="n">elim</span> <span class="o">(</span><span class="n">or</span><span class="bp">.</span><span class="n">elim</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">lt_succ_iff_lt_or_eq</span><span class="bp">.</span><span class="mi">1</span> <span class="n">H1</span><span class="o">)</span> <span class="n">H2</span> <span class="n">H3</span><span class="o">)</span>
<span class="kn">end</span>
</pre></div>


{% endraw %}
