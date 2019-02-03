---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/01104proofusinginductivevsdef.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [proof using inductive vs def](https://leanprover-community.github.io/archive/113488general/01104proofusinginductivevsdef.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Sean Leather (Sep 14 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133936109):
<p>This is quite an esoteric problem, so I'm not sure if anybody would be interested in looking into it. Nonetheless, I thought I'd try to see if anybody had any ideas.</p>
<p>So I thought I would change a inductive <code>Prop</code> to a definition. The original inductive:</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">lc</span> <span class="o">:</span> <span class="n">exp</span> <span class="n">V</span> <span class="bp">→</span> <span class="kt">Prop</span>
  <span class="bp">|</span> <span class="n">varf</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">V</span><span class="o">),</span>                                                                          <span class="n">lc</span> <span class="o">(</span><span class="n">varf</span> <span class="n">x</span><span class="o">)</span>
  <span class="bp">|</span> <span class="n">app</span>  <span class="o">:</span> <span class="bp">Π</span>                <span class="o">{</span><span class="n">ef</span> <span class="n">ea</span> <span class="o">:</span> <span class="n">exp</span> <span class="n">V</span><span class="o">},</span> <span class="n">lc</span> <span class="n">ef</span> <span class="bp">→</span> <span class="n">lc</span> <span class="n">ea</span> <span class="bp">→</span>                                   <span class="n">lc</span> <span class="o">(</span><span class="n">app</span> <span class="n">ef</span> <span class="n">ea</span><span class="o">)</span>
  <span class="bp">|</span> <span class="n">lam</span>  <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">L</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">V</span><span class="o">}</span> <span class="o">{</span><span class="n">eb</span> <span class="o">:</span> <span class="n">exp</span> <span class="n">V</span><span class="o">},</span>            <span class="o">(</span><span class="bp">∀</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">V</span><span class="o">},</span> <span class="n">x</span> <span class="err">∉</span> <span class="n">L</span> <span class="bp">→</span> <span class="n">lc</span> <span class="o">(</span><span class="n">open_var</span> <span class="n">x</span> <span class="n">eb</span><span class="o">))</span> <span class="bp">→</span> <span class="n">lc</span> <span class="o">(</span><span class="n">lam</span> <span class="n">eb</span><span class="o">)</span>
  <span class="bp">|</span> <span class="n">let_</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">L</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">V</span><span class="o">}</span> <span class="o">{</span><span class="n">ed</span> <span class="n">eb</span> <span class="o">:</span> <span class="n">exp</span> <span class="n">V</span><span class="o">},</span> <span class="n">lc</span> <span class="n">ed</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∀</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">V</span><span class="o">},</span> <span class="n">x</span> <span class="err">∉</span> <span class="n">L</span> <span class="bp">→</span> <span class="n">lc</span> <span class="o">(</span><span class="n">open_var</span> <span class="n">x</span> <span class="n">eb</span><span class="o">))</span> <span class="bp">→</span> <span class="n">lc</span> <span class="o">(</span><span class="n">let_</span> <span class="n">ed</span> <span class="n">eb</span><span class="o">)</span>
</pre></div>


<p>The new def:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">lc&#39;</span> <span class="o">:</span> <span class="n">exp</span> <span class="n">V</span> <span class="bp">→</span> <span class="kt">Prop</span>
  <span class="bp">|</span> <span class="o">(</span><span class="n">varb</span> <span class="bp">_</span><span class="o">)</span>     <span class="o">:=</span> <span class="n">false</span>
  <span class="bp">|</span> <span class="o">(</span><span class="n">varf</span> <span class="bp">_</span><span class="o">)</span>     <span class="o">:=</span> <span class="n">true</span>
  <span class="bp">|</span> <span class="o">(</span><span class="n">app</span> <span class="n">ef</span> <span class="n">ea</span><span class="o">)</span>  <span class="o">:=</span> <span class="n">lc&#39;</span> <span class="n">ef</span> <span class="bp">∧</span> <span class="n">lc&#39;</span> <span class="n">ea</span>
  <span class="bp">|</span> <span class="o">(</span><span class="n">lam</span> <span class="n">eb</span><span class="o">)</span>     <span class="o">:=</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">L</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">V</span><span class="o">),</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">x</span><span class="o">},</span> <span class="n">x</span> <span class="err">∉</span> <span class="n">L</span> <span class="bp">→</span> <span class="n">lc&#39;</span> <span class="o">(</span><span class="n">open_var</span> <span class="n">x</span> <span class="n">eb</span><span class="o">)</span>
  <span class="bp">|</span> <span class="o">(</span><span class="n">let_</span> <span class="n">ed</span> <span class="n">eb</span><span class="o">)</span> <span class="o">:=</span> <span class="n">lc&#39;</span> <span class="n">ed</span> <span class="bp">∧</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">L</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">V</span><span class="o">),</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">x</span><span class="o">},</span> <span class="n">x</span> <span class="err">∉</span> <span class="n">L</span> <span class="bp">→</span> <span class="n">lc&#39;</span> <span class="o">(</span><span class="n">open_var</span> <span class="n">x</span> <span class="n">eb</span><span class="o">)</span>
  <span class="n">using_well_founded</span> <span class="o">{</span>
    <span class="n">dec_tac</span> <span class="o">:=</span> <span class="bp">`</span><span class="o">[</span><span class="n">simp</span> <span class="o">[</span><span class="n">measure</span><span class="o">,</span> <span class="n">inv_image</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">pos_iff_ne_zero&#39;</span><span class="o">]],</span>
    <span class="n">rel_tac</span> <span class="o">:=</span> <span class="bp">λ_</span> <span class="bp">_</span><span class="o">,</span> <span class="bp">`</span><span class="o">[</span><span class="n">exact</span> <span class="bp">⟨_</span><span class="o">,</span> <span class="n">measure_wf</span> <span class="n">depth</span><span class="bp">⟩</span><span class="o">]</span> <span class="o">}</span>
</pre></div>


<p>But then I ran into a problem proving a theorem that did induction on <code>lc</code>. Since I can't do induction on <code>lc'</code>, I changed the proof to do induction on the parameter to <code>lc'</code>. In the old proof, I have this at one stage:</p>
<div class="codehilite"><pre><span></span><span class="n">V</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">finset</span><span class="bp">.</span><span class="n">has_fresh</span> <span class="n">V</span><span class="o">,</span>
<span class="n">e₁</span> <span class="n">e₂</span> <span class="o">:</span> <span class="n">exp</span> <span class="n">V</span><span class="o">,</span>
<span class="n">k</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span>
<span class="n">L</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">V</span><span class="o">,</span>
<span class="n">eb</span> <span class="o">:</span> <span class="n">exp</span> <span class="n">V</span><span class="o">,</span>
<span class="n">Fb</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">V</span><span class="o">},</span> <span class="n">x</span> <span class="err">∉</span> <span class="n">L</span> <span class="bp">→</span> <span class="n">lc</span> <span class="o">(</span><span class="n">open_var</span> <span class="n">x</span> <span class="n">eb</span><span class="o">),</span>
<span class="n">rb</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">V</span><span class="o">},</span> <span class="n">x</span> <span class="err">∉</span> <span class="n">L</span> <span class="bp">→</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">e₂</span> <span class="o">:</span> <span class="n">exp</span> <span class="n">V</span><span class="o">}</span> <span class="o">{</span><span class="n">k</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">},</span> <span class="kn">open</span><span class="bp">.</span><span class="n">rec</span> <span class="n">e₂</span> <span class="n">k</span> <span class="o">(</span><span class="n">open_var</span> <span class="n">x</span> <span class="n">eb</span><span class="o">)</span> <span class="bp">=</span> <span class="n">open_var</span> <span class="n">x</span> <span class="n">eb</span>
<span class="err">⊢</span> <span class="kn">open</span><span class="bp">.</span><span class="n">rec</span> <span class="n">e₂</span> <span class="o">(</span><span class="n">k</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="n">eb</span> <span class="bp">=</span> <span class="n">eb</span>
</pre></div>


<p>In the new proof, I have this at the same stage:</p>
<div class="codehilite"><pre><span></span><span class="n">V</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">finset</span><span class="bp">.</span><span class="n">has_fresh</span> <span class="n">V</span><span class="o">,</span>
<span class="n">e₂</span> <span class="o">:</span> <span class="n">exp</span> <span class="n">V</span><span class="o">,</span>
<span class="n">k</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span>
<span class="n">eb</span> <span class="o">:</span> <span class="n">exp</span> <span class="n">V</span><span class="o">,</span>
<span class="n">L</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">V</span><span class="o">,</span>
<span class="n">Fb</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">V</span><span class="o">},</span> <span class="n">x</span> <span class="err">∉</span> <span class="n">L</span> <span class="bp">→</span> <span class="n">lc&#39;</span> <span class="o">(</span><span class="n">open_var</span> <span class="n">x</span> <span class="n">eb</span><span class="o">)</span>
<span class="n">rb</span> <span class="o">:</span> <span class="n">lc&#39;</span> <span class="n">eb</span> <span class="bp">→</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">e₂</span> <span class="o">:</span> <span class="n">exp</span> <span class="n">V</span><span class="o">}</span> <span class="o">{</span><span class="n">k</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">},</span> <span class="kn">open</span><span class="bp">.</span><span class="n">rec</span> <span class="n">e₂</span> <span class="n">k</span> <span class="n">eb</span> <span class="bp">=</span> <span class="n">eb</span><span class="o">,</span>
<span class="err">⊢</span> <span class="kn">open</span><span class="bp">.</span><span class="n">rec</span> <span class="n">e₂</span> <span class="o">(</span><span class="n">k</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="n">eb</span> <span class="bp">=</span> <span class="n">eb</span>
</pre></div>


<p>Notice the difference in <code>rb</code>. In the old proof, I have an auxiliary proof that works for <code>open.rec e₂ k (open_var x eb)</code>, but in the new proof, I'm stuck. Since the new <code>lc'</code> doesn't provide the same evidence at <code>rb</code>, I don't know what to do. I think I should somehow reproduce the old <code>rb</code> in the new proof, perhaps using some knowledge of <code>lc'</code> that is lost since I'm not doing induction on <code>lc</code>, but I don't know how.</p>
<p>The full thing is at <a href="https://github.com/spl/tts/tree/lc-def" target="_blank" title="https://github.com/spl/tts/tree/lc-def">https://github.com/spl/tts/tree/lc-def</a> .</p>

#### [ Kenny Lau (Sep 14 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133936608):
<p>does <code>rec_on</code> solve the problem?</p>

#### [ Sean Leather (Sep 14 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133936659):
<p><code>rec_on</code> what?</p>

#### [ Kenny Lau (Sep 14 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133936828):
<p>exp</p>

#### [ Sean Leather (Sep 14 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133936836):
<p>Do you mean use <code>rec_on</code> instead of <code>induction</code>? I'm not sure, but I don't see how it could.</p>

#### [ Mario Carneiro (Sep 14 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133937291):
<p>which case are you in? what is the induction proof?</p>

#### [ Mario Carneiro (Sep 14 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133937349):
<p>none of the variables in the state match things in the inductive definitions you gave</p>

#### [ Sean Leather (Sep 14 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133937489):
<p>The <code>lam</code> case. See <a href="https://github.com/spl/tts/commit/04e4229c0fccec935b7f615a4aefe18d14982f2b#diff-94a57c5df4a0ba5ba897bada2c897d1aR73" target="_blank" title="https://github.com/spl/tts/commit/04e4229c0fccec935b7f615a4aefe18d14982f2b#diff-94a57c5df4a0ba5ba897bada2c897d1aR73">https://github.com/spl/tts/commit/04e4229c0fccec935b7f615a4aefe18d14982f2b#diff-94a57c5df4a0ba5ba897bada2c897d1aR73</a></p>

#### [ Sean Leather (Sep 14 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133937510):
<p>Just above that is the old proof (line 49).</p>

#### [ Mario Carneiro (Sep 14 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133937539):
<p>you are doing induction on <code>k</code>?</p>

#### [ Sean Leather (Sep 14 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133937593):
<p>In the old proof, induction was on <code>l : lc e₁</code>. In the new proof, induction is on <code>e₁ : exp V</code>.</p>

#### [ Sean Leather (Sep 14 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133937630):
<p>The focus is here: <a href="https://github.com/spl/tts/blob/04e4229c0fccec935b7f615a4aefe18d14982f2b/src/exp/open.lean#L41-L77" target="_blank" title="https://github.com/spl/tts/blob/04e4229c0fccec935b7f615a4aefe18d14982f2b/src/exp/open.lean#L41-L77">https://github.com/spl/tts/blob/04e4229c0fccec935b7f615a4aefe18d14982f2b/src/exp/open.lean#L41-L77</a> (if that helps).</p>

#### [ Mario Carneiro (Sep 14 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133937634):
<p>induction on <code>e1</code> isn't good enough</p>

#### [ Mario Carneiro (Sep 14 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133937674):
<p>you have to do induction on the same well founded measure you used to define <code>lc'</code> in the first place</p>

#### [ Sean Leather (Sep 14 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133937678):
<p>You mean induction on <code>depth</code>?</p>

#### [ Mario Carneiro (Sep 14 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133937679):
<p>yes</p>

#### [ Sean Leather (Sep 14 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133937683):
<p>Oh....</p>

#### [ Mario Carneiro (Sep 14 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133937690):
<p>because presumably these <code>open_var</code> things don't increase depth</p>

#### [ Sean Leather (Sep 14 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133937696):
<p>Correct.</p>

#### [ Mario Carneiro (Sep 14 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133937708):
<p>it's a general rule that you have to prove properties about a recursive definition using the same recursion strategy as the definition</p>

#### [ Sean Leather (Sep 14 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133937791):
<p>Ah, okay. The well-founded stuff still confuses me.</p>

#### [ Sean Leather (Sep 14 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133937807):
<p>So, it seems that the <code>inductive</code> is already doing a lot for me that I would otherwise have to do with more work.</p>

#### [ Sean Leather (Sep 14 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133937849):
<p>Would it be better just to keep using it instead of the definition version?</p>

#### [ Sean Leather (Sep 14 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133937854):
<p>I thought a definition would make things easier, but it's not.</p>

#### [ Kenny Lau (Sep 14 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133937859):
<p>I mean, you can always use <code>well_founded.fix</code></p>

#### [ Sean Leather (Sep 14 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133937920):
<p>I've never used <code>well_founded.fix</code>.</p>

#### [ Mario Carneiro (Sep 14 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133937952):
<p>it is not easier</p>

#### [ Mario Carneiro (Sep 14 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133937961):
<p>it is used behind the scenes by <code>using_well_founded</code></p>

#### [ Sean Leather (Sep 14 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133938025):
<p>Okay. So I'll stick with the inductive. Lesson learned!</p>

#### [ Simon Hudon (Sep 15 2018 at 06:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/proof%20using%20inductive%20vs%20def/near/133995045):
<p>Inductive propositions are quite handy in those situations. You can do induction on them when they are in your assumptions and it will automatically unify the variables that should be equal and you want have to handle cases where your definition would say <code>false</code></p>


{% endraw %}
