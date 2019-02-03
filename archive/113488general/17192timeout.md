---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/17192timeout.html
---

## Stream: [general](index.html)
### Topic: [timeout](17192timeout.html)

---


{% raw %}
#### [ Kenny Lau (Nov 08 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout/near/147329792):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">is_noetherian_ring_mv_polynomial_fin</span> <span class="o">{</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span>
  <span class="o">(</span><span class="n">hnr</span> <span class="o">:</span> <span class="n">is_noetherian_ring</span> <span class="n">R</span><span class="o">)</span> <span class="o">:</span> <span class="n">is_noetherian_ring</span> <span class="o">(</span><span class="n">mv_polynomial</span> <span class="o">(</span><span class="n">fin</span> <span class="n">n</span><span class="o">)</span> <span class="n">R</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">try_for</span> <span class="mi">4000</span> <span class="o">{</span>
  <span class="n">induction</span> <span class="n">n</span> <span class="k">with</span> <span class="n">n</span> <span class="n">ih</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">refine</span> <span class="n">is_noetherian_ring_of_equiv</span> <span class="n">R</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">hnr</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">exact</span> <span class="o">(</span><span class="n">mv_polynomial</span><span class="bp">.</span><span class="n">pempty_equiv</span><span class="bp">.</span><span class="n">symm</span><span class="bp">.</span><span class="n">trans</span> <span class="err">$</span> <span class="n">mv_polynomial</span><span class="bp">.</span><span class="n">equiv_of_equiv</span>
      <span class="bp">⟨</span><span class="n">pempty</span><span class="bp">.</span><span class="n">elim</span><span class="o">,</span> <span class="n">fin</span><span class="bp">.</span><span class="n">elim0</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">pempty</span><span class="bp">.</span><span class="n">elim</span> <span class="n">x</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">fin</span><span class="bp">.</span><span class="n">elim0</span> <span class="n">x</span><span class="bp">⟩</span><span class="o">)</span> <span class="o">},</span>
    <span class="o">{</span> <span class="n">dsimp</span> <span class="n">only</span> <span class="o">[</span><span class="n">equiv</span><span class="bp">.</span><span class="n">trans</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">symm</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">coe_fn_mk</span><span class="o">],</span>
      <span class="n">exact</span> <span class="bp">@@</span><span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">comp</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span>
        <span class="o">(</span><span class="n">mv_polynomial</span><span class="bp">.</span><span class="n">C</span><span class="bp">.</span><span class="n">is_ring_hom</span><span class="o">)</span> <span class="bp">_</span> <span class="bp">_</span>
        <span class="o">(</span><span class="bp">@@</span><span class="n">mv_polynomial</span><span class="bp">.</span><span class="n">eval₂</span><span class="bp">.</span><span class="n">is_ring_hom</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span>
          <span class="o">(</span><span class="n">mv_polynomial</span><span class="bp">.</span><span class="n">C</span> <span class="o">:</span> <span class="n">R</span> <span class="bp">→</span> <span class="n">mv_polynomial</span> <span class="o">(</span><span class="n">fin</span> <span class="mi">0</span><span class="o">)</span> <span class="n">R</span><span class="o">)</span> <span class="n">mv_polynomial</span><span class="bp">.</span><span class="n">C</span><span class="bp">.</span><span class="n">is_ring_hom</span>
          <span class="o">(</span><span class="n">mv_polynomial</span><span class="bp">.</span><span class="n">X</span> <span class="err">∘</span> <span class="n">pempty</span><span class="bp">.</span><span class="n">elim</span> <span class="o">:</span> <span class="n">pempty</span> <span class="bp">→</span> <span class="n">mv_polynomial</span> <span class="o">(</span><span class="n">fin</span> <span class="mi">0</span><span class="o">)</span> <span class="n">R</span><span class="o">))</span> <span class="o">}</span> <span class="o">},</span>
<span class="o">},</span> <span class="n">try_for</span> <span class="mi">100000</span> <span class="o">{</span>
  <span class="n">refine</span> <span class="n">is_noetherian_ring_of_equiv</span> <span class="o">(</span><span class="n">polynomial</span> <span class="o">(</span><span class="n">mv_polynomial</span> <span class="o">(</span><span class="n">fin</span> <span class="n">n</span><span class="o">)</span> <span class="n">R</span><span class="o">))</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="n">is_noetherian_ring_polynomial</span> <span class="n">ih</span><span class="o">),</span>
  <span class="o">{</span> <span class="n">exact</span> <span class="n">mv_polynomial</span><span class="bp">.</span><span class="n">option_equiv</span><span class="bp">.</span><span class="n">symm</span><span class="bp">.</span><span class="n">trans</span> <span class="o">(</span><span class="n">mv_polynomial</span><span class="bp">.</span><span class="n">equiv_of_equiv</span>
      <span class="bp">⟨λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">option</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">x</span> <span class="mi">0</span> <span class="n">fin</span><span class="bp">.</span><span class="n">succ</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">fin</span><span class="bp">.</span><span class="n">cases</span> <span class="n">none</span> <span class="n">some</span> <span class="n">x</span><span class="o">,</span>
      <span class="k">by</span> <span class="n">rintro</span> <span class="bp">⟨</span><span class="n">none</span> <span class="bp">|</span> <span class="n">x</span><span class="bp">⟩;</span> <span class="o">[</span><span class="n">refl</span><span class="o">,</span> <span class="n">exact</span> <span class="n">fin</span><span class="bp">.</span><span class="n">cases_succ</span> <span class="bp">_</span><span class="o">],</span>
      <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">fin</span><span class="bp">.</span><span class="n">cases</span> <span class="n">rfl</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">i</span><span class="o">,</span> <span class="k">show</span> <span class="o">(</span><span class="n">option</span><span class="bp">.</span><span class="n">rec_on</span> <span class="o">(</span><span class="n">fin</span><span class="bp">.</span><span class="n">cases</span> <span class="n">none</span> <span class="n">some</span> <span class="o">(</span><span class="n">fin</span><span class="bp">.</span><span class="n">succ</span> <span class="n">i</span><span class="o">)</span> <span class="o">:</span> <span class="n">option</span> <span class="o">(</span><span class="n">fin</span> <span class="n">n</span><span class="o">))</span>
        <span class="mi">0</span> <span class="n">fin</span><span class="bp">.</span><span class="n">succ</span> <span class="o">:</span> <span class="n">fin</span> <span class="n">n</span><span class="bp">.</span><span class="n">succ</span><span class="o">)</span> <span class="bp">=</span> <span class="bp">_</span><span class="o">,</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">fin</span><span class="bp">.</span><span class="n">cases_succ</span><span class="o">)</span> <span class="n">x</span><span class="bp">⟩</span><span class="o">)</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">dsimp</span> <span class="n">only</span> <span class="o">[</span><span class="n">equiv</span><span class="bp">.</span><span class="n">trans</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">symm</span><span class="o">,</span> <span class="n">equiv</span><span class="bp">.</span><span class="n">coe_fn_mk</span><span class="o">],</span>
    <span class="n">exact</span> <span class="n">is_ring_hom</span><span class="bp">.</span><span class="n">comp</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">}</span>
<span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Nov 08 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout/near/147329805):
<p>Even 100 seconds is not enough</p>

#### [ Kenny Lau (Nov 08 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout/near/147329817):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I don't really know how to deal with this</p>

#### [ Kenny Lau (Nov 08 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout/near/147330186):
<p>(it's from <a href="https://github.com/leanprover/mathlib/pull/461/commits/b3f1efbe02638a2793b48e9a28a1d8f0df371690#diff-1f7cb4d661f00b6d887925434b41ad5dR286" target="_blank" title="https://github.com/leanprover/mathlib/pull/461/commits/b3f1efbe02638a2793b48e9a28a1d8f0df371690#diff-1f7cb4d661f00b6d887925434b41ad5dR286">https://github.com/leanprover/mathlib/pull/461/commits/b3f1efbe02638a2793b48e9a28a1d8f0df371690#diff-1f7cb4d661f00b6d887925434b41ad5dR286</a>)</p>

#### [ Kenny Lau (Nov 08 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout/near/147335661):
<p><a href="https://github.com/leanprover/mathlib/pull/461/commits/f80e9fce6b081cf26f551b3ae2e5c83327f9bd59#diff-1f7cb4d661f00b6d887925434b41ad5dR293" target="_blank" title="https://github.com/leanprover/mathlib/pull/461/commits/f80e9fce6b081cf26f551b3ae2e5c83327f9bd59#diff-1f7cb4d661f00b6d887925434b41ad5dR293">https://github.com/leanprover/mathlib/pull/461/commits/f80e9fce6b081cf26f551b3ae2e5c83327f9bd59#diff-1f7cb4d661f00b6d887925434b41ad5dR293</a></p>

#### [ Kenny Lau (Nov 08 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout/near/147335662):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> more ridiculousness</p>

#### [ Kenny Lau (Nov 09 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout/near/147358487):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> what do you think about this?</p>

#### [ Sebastian Ullrich (Nov 09 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout/near/147358506):
<p>not much</p>

#### [ Mario Carneiro (Nov 09 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout/near/147358544):
<p>good idea</p>

#### [ Kenny Lau (Nov 09 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout/near/147359835):
<p>I think it's a serious problem if I provided every implicit argument and it still takes 16 seconds to elaborate</p>

#### [ Kenny Lau (Nov 09 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout/near/147362908):
<p>I basically changed the definitions of polynomial and mv_polynomial and that cut down 6 seconds</p>

#### [ Kevin Buzzard (Nov 09 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/timeout/near/147368074):
<p>Kenny can you make a MWE? It's hard to run your code.</p>


{% endraw %}
