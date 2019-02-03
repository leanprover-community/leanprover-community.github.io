---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/87308quotienthrecon.html
---

## Stream: [general](index.html)
### Topic: [quotient.hrec_on₂](87308quotienthrecon.html)

---


{% raw %}
#### [ Sean Leather (Aug 06 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130971695):
<p>I've got a <a href="https://github.com/spl/lean-finmap/blob/fb3f562de05059f136f855b88bf616c8aac7f365/src/data/multiset/dict.lean#L162-L172" target="_blank" title="https://github.com/spl/lean-finmap/blob/fb3f562de05059f136f855b88bf616c8aac7f365/src/data/multiset/dict.lean#L162-L172">definition</a>:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">kunion</span> <span class="o">:</span> <span class="n">m₁</span><span class="bp">.</span><span class="n">nodup_keys</span> <span class="bp">→</span> <span class="n">m₂</span><span class="bp">.</span><span class="n">nodup_keys</span> <span class="bp">→</span> <span class="n">multiset</span> <span class="o">(</span><span class="n">sigma</span> <span class="n">β</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">@</span><span class="n">quotient</span><span class="bp">.</span><span class="n">hrec_on₂</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">m₁</span> <span class="n">m₂</span> <span class="o">:</span> <span class="n">multiset</span> <span class="o">(</span><span class="n">sigma</span> <span class="n">β</span><span class="o">)),</span> <span class="n">m₁</span><span class="bp">.</span><span class="n">nodup_keys</span> <span class="bp">→</span> <span class="n">m₂</span><span class="bp">.</span><span class="n">nodup_keys</span> <span class="bp">→</span> <span class="n">multiset</span> <span class="o">(</span><span class="n">sigma</span> <span class="n">β</span><span class="o">))</span>
  <span class="n">m₁</span> <span class="n">m₂</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">l₁</span> <span class="n">l₂</span> <span class="o">(</span><span class="n">d₁</span> <span class="o">:</span> <span class="n">l₁</span><span class="bp">.</span><span class="n">nodup_keys</span><span class="o">)</span> <span class="o">(</span><span class="n">d₂</span> <span class="o">:</span> <span class="n">l₂</span><span class="bp">.</span><span class="n">nodup_keys</span><span class="o">),</span> <span class="n">l₁</span><span class="bp">.</span><span class="n">kunion</span> <span class="n">l₂</span><span class="o">)</span> <span class="err">$</span>
    <span class="bp">λ</span> <span class="n">l₁</span> <span class="n">l₂</span> <span class="n">l₃</span> <span class="n">l₄</span> <span class="n">p₁₃</span> <span class="n">p₂₄</span><span class="o">,</span>
    <span class="n">hfunext</span> <span class="o">(</span><span class="k">by</span> <span class="n">rw</span> <span class="n">perm_nodup_keys</span> <span class="n">p₁₃</span><span class="o">)</span> <span class="err">$</span>
      <span class="bp">λ</span> <span class="o">(</span><span class="n">d₁</span> <span class="o">:</span> <span class="n">l₁</span><span class="bp">.</span><span class="n">nodup_keys</span><span class="o">)</span> <span class="o">(</span><span class="n">d₃</span> <span class="o">:</span> <span class="n">l₃</span><span class="bp">.</span><span class="n">nodup_keys</span><span class="o">)</span> <span class="bp">_</span><span class="o">,</span>
      <span class="n">hfunext</span> <span class="o">(</span><span class="k">by</span> <span class="n">rw</span> <span class="n">perm_nodup_keys</span> <span class="n">p₂₄</span><span class="o">)</span> <span class="err">$</span>
        <span class="bp">λ</span> <span class="o">(</span><span class="n">d₂</span> <span class="o">:</span> <span class="n">l₂</span><span class="bp">.</span><span class="n">nodup_keys</span><span class="o">)</span> <span class="o">(</span><span class="n">d₄</span> <span class="o">:</span> <span class="n">l₄</span><span class="bp">.</span><span class="n">nodup_keys</span><span class="o">)</span> <span class="bp">_</span><span class="o">,</span>
        <span class="n">heq_of_eq</span> <span class="err">$</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">sound</span> <span class="err">$</span> <span class="n">perm_kunion</span> <span class="n">d₂</span> <span class="n">d₄</span> <span class="n">p₁₃</span> <span class="n">p₂₄</span>

<span class="n">local</span> <span class="kn">infixr</span> <span class="bp">`</span> <span class="n">k</span><span class="err">∪</span> <span class="bp">`</span><span class="o">:</span><span class="mi">67</span> <span class="o">:=</span> <span class="n">kunion</span>
</pre></div>


<p>and I want to prove the left and right units:</p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">zero_kunion</span> <span class="o">{</span><span class="n">m</span> <span class="o">:</span> <span class="n">multiset</span> <span class="o">(</span><span class="n">sigma</span> <span class="n">β</span><span class="o">)}</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">d</span> <span class="o">:</span> <span class="n">m</span><span class="bp">.</span><span class="n">nodup_keys</span><span class="o">),</span> <span class="n">nodup_keys_zero</span> <span class="n">k</span><span class="err">∪</span> <span class="n">d</span> <span class="bp">=</span> <span class="n">m</span>
<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">kunion_zero</span> <span class="o">{</span><span class="n">m</span> <span class="o">:</span> <span class="n">multiset</span> <span class="o">(</span><span class="n">sigma</span> <span class="n">β</span><span class="o">)}</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">d</span> <span class="o">:</span> <span class="n">m</span><span class="bp">.</span><span class="n">nodup_keys</span><span class="o">),</span> <span class="n">d</span> <span class="n">k</span><span class="err">∪</span> <span class="n">nodup_keys_zero</span> <span class="bp">=</span> <span class="n">m</span>
</pre></div>


<p>I'm stuck on how to proceed. If I use <code>quotient.induction_on m</code>, I just unfold until I get down to <code>quot.rec_on ↑(hd :: tl)</code> or <code>quot.rec_on ↑nil</code>, but I don't know how to go further. (At one point, I believe I even made the simplifier loop infinitely.)</p>
<p>Any suggestions on how to prove these?</p>

#### [ Mario Carneiro (Aug 06 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130971867):
<p>Wow, that's a weird notation</p>

#### [ Mario Carneiro (Aug 06 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130971872):
<p>does it have to be a partial function?</p>

#### [ Sean Leather (Aug 06 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130971983):
<blockquote>
<p>does it have to be a partial function?</p>
</blockquote>
<p>I don't follow you.</p>

#### [ Mario Carneiro (Aug 06 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130972034):
<p>you could make it return empty when the inputs don't have <code>nodup_keys</code></p>

#### [ Mario Carneiro (Aug 06 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130972054):
<p>or it could be a <code>roption</code> if you are worried about the performance cost of checking <code>nodup_keys</code></p>

#### [ Sean Leather (Aug 06 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130972218):
<p>Sorry, Mario, your  use of “it” in multiple places is a bit too vague for me. Are you suggesting I use a different definition for <code>kunion</code>? If so, what is the type signature you're referring to?</p>

#### [ Sean Leather (Aug 06 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130972526):
<p>Btw, I'm not asking for a completed solution. You're welcome to give me only hints or suggestions. <span class="emoji emoji-263a" title="smile">:smile:</span></p>

#### [ Reid Barton (Aug 06 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130972544):
<p>I think <code>def kunion : multiset (sigma β) → multiset (sigma β) → roption (multiset (sigma β))</code> and then prove that <code>kunion</code> is defined exactly when each <code>multiset</code> is <code>nodup_keys</code></p>

#### [ Sean Leather (Aug 06 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130972612):
<p>Reid: Hmm, okay, thanks.</p>

#### [ Sean Leather (Aug 06 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130972673):
<p>And what's the advantage to this approach? Is it simplicity of the definition and related theorems or performance or both?</p>

#### [ Reid Barton (Aug 06 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130972677):
<p>Then you can avoid all this dependent eliminator stuff... although it's not clear to me whether your problem is related to this</p>

#### [ Sean Leather (Aug 06 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130972701):
<p>Okay, well, I'll give it a shot.</p>

#### [ Chris Hughes (Aug 06 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130972702):
<p>Just proving at <code> quotient.hrec_on_beta</code> lemma might help.</p>

#### [ Reid Barton (Aug 06 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130972707):
<p>Yes. Is that <code>↑</code> just <code>quotient.mk</code>?</p>

#### [ Sean Leather (Aug 06 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130972756):
<p>Yes, I think so.</p>

#### [ Sean Leather (Aug 06 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130972765):
<p>Chris: I wondered the same thing. I'm not sure how to start with that.</p>

#### [ Reid Barton (Aug 06 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130972790):
<p>Well, <code>quotient.rec_on</code> applied to <code>quotient.mk</code> should reduce...</p>

#### [ Chris Hughes (Aug 06 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130972792):
<p>Or use <code>show</code></p>

#### [ Sean Leather (Aug 06 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130972893):
<p>I suppose it would look something like:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">quot</span><span class="bp">.</span><span class="n">ind_beta</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span><span class="o">,</span> <span class="n">β</span> <span class="o">(</span><span class="n">quot</span><span class="bp">.</span><span class="n">mk</span> <span class="n">r</span> <span class="n">a</span><span class="o">))</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">ind</span> <span class="n">p</span> <span class="o">(</span><span class="n">quot</span><span class="bp">.</span><span class="n">mk</span> <span class="n">r</span> <span class="n">a</span><span class="o">)</span> <span class="o">:</span> <span class="n">β</span> <span class="o">(</span><span class="n">quot</span><span class="bp">.</span><span class="n">mk</span> <span class="n">r</span> <span class="n">a</span><span class="o">))</span> <span class="bp">=</span> <span class="n">p</span> <span class="n">a</span>
</pre></div>

#### [ Mario Carneiro (Aug 06 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130974037):
<p>that is trivially true, since both sides are propositions</p>

#### [ Mario Carneiro (Aug 06 2018 at 14:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130974063):
<p>The advantage of using <code>roption</code> is avoiding all the <code>hrec</code> mess. I've had to define partial functions over quotients before, and I wish I'd thought of this then</p>

#### [ Sean Leather (Aug 06 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130974158):
<blockquote>
<p>that is trivially true, since both sides are propositions</p>
</blockquote>
<p>Are you referring to <code>quot.ind_beta</code>, which is in the core library, or something else?</p>
<blockquote>
<p>The advantage of using <code>roption</code> is avoiding all the <code>hrec</code> mess. I've had to define partial functions over quotients before, and I wish I'd thought of this then</p>
</blockquote>
<p>Great! I'm working on it now.</p>

#### [ Reid Barton (Aug 06 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130974410):
<p>I think someone probably copied <code>lift_beta</code> to <code>ind_beta</code> without realizing it was rather unnecessary.</p>

#### [ Sean Leather (Aug 06 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130974532):
<p>Ah! I see what you're saying now. I didn't look that closely at <code>ind_beta</code>.</p>

#### [ Sean Leather (Aug 06 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130974767):
<p>This is definitely a much nicer definition:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">kunion&#39;</span> <span class="o">(</span><span class="n">m₁</span> <span class="n">m₂</span> <span class="o">:</span> <span class="n">multiset</span> <span class="o">(</span><span class="n">sigma</span> <span class="n">β</span><span class="o">))</span> <span class="o">:</span> <span class="n">roption</span> <span class="o">(</span><span class="n">multiset</span> <span class="o">(</span><span class="n">sigma</span> <span class="n">β</span><span class="o">))</span> <span class="o">:=</span>
<span class="n">quotient</span><span class="bp">.</span><span class="n">lift_on₂</span> <span class="n">m₁</span> <span class="n">m₂</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">l₁</span> <span class="n">l₂</span><span class="o">,</span> <span class="n">roption</span><span class="bp">.</span><span class="n">mk</span> <span class="o">(</span><span class="n">l₁</span><span class="bp">.</span><span class="n">nodup_keys</span> <span class="bp">∧</span> <span class="n">l₂</span><span class="bp">.</span><span class="n">nodup_keys</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="o">(</span><span class="n">l₁</span><span class="bp">.</span><span class="n">kunion</span> <span class="n">l₂</span> <span class="o">:</span> <span class="n">multiset</span> <span class="o">(</span><span class="n">sigma</span> <span class="n">β</span><span class="o">))))</span> <span class="err">$</span>
  <span class="bp">λ</span> <span class="n">l₁</span> <span class="n">l₂</span> <span class="n">l₃</span> <span class="n">l₄</span> <span class="n">p₁₃</span> <span class="n">p₂₄</span><span class="o">,</span> <span class="n">roption</span><span class="bp">.</span><span class="n">ext&#39;</span>
    <span class="o">(</span><span class="n">and_congr</span> <span class="o">(</span><span class="n">perm_nodup_keys</span> <span class="n">p₁₃</span><span class="o">)</span> <span class="o">(</span><span class="n">perm_nodup_keys</span> <span class="n">p₂₄</span><span class="o">))</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="bp">⟨</span><span class="n">d₁</span><span class="o">,</span> <span class="n">d₂</span><span class="bp">⟩</span> <span class="bp">⟨</span><span class="n">d₃</span><span class="o">,</span> <span class="n">d₄</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">sound</span> <span class="err">$</span> <span class="n">perm_kunion</span> <span class="n">d₂</span> <span class="n">d₄</span> <span class="n">p₁₃</span> <span class="n">p₂₄</span><span class="o">)</span>
</pre></div>

#### [ Mario Carneiro (Aug 06 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130974979):
<p>so now the theorem you want is either <code>m k∪ 0 = some m</code> or <code>m ∈ m k∪ 0</code> (they are equivalent)</p>

#### [ Sean Leather (Aug 06 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130975110):
<p>Right.</p>

#### [ Mario Carneiro (Aug 06 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130975212):
<p>and the coercion lemma you want says <code>l₁.nodup_keys → l₂.nodup_keys → ↑l₁ k∪ ↑l₂ = some (l₁.kunion l₂)</code></p>

#### [ Sean Leather (Aug 06 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130975700):
<p>Got that, thanks. How should I coerce the 0 (<code>multiset.zero</code>) for <code>kunion' 0 ↑l</code>?</p>

#### [ Sean Leather (Aug 06 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130975782):
<p>If I do <code>simp [has_zero.zero, multiset.zero]</code>, lean never ends.</p>

#### [ Mario Carneiro (Aug 06 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130975852):
<p>you can just force it to unfold by applying <code>kunion_coe.trans _</code></p>

#### [ Mario Carneiro (Aug 06 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130975886):
<p>or you can rewrite with <code>coe_nil_eq_zero</code></p>

#### [ Sean Leather (Aug 06 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130980496):
<p>The aforementioned theorems:</p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">zero_kunion</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">d</span> <span class="o">:</span> <span class="n">m</span><span class="bp">.</span><span class="n">nodup_keys</span><span class="o">),</span> <span class="n">kunion&#39;</span> <span class="mi">0</span> <span class="n">m</span> <span class="bp">=</span> <span class="n">roption</span><span class="bp">.</span><span class="n">some</span> <span class="n">m</span> <span class="o">:=</span>
<span class="n">quotient</span><span class="bp">.</span><span class="n">induction_on</span> <span class="n">m</span> <span class="err">$</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="n">d</span><span class="o">,</span> <span class="o">(</span><span class="n">kunion_coe</span> <span class="n">nodup_keys_zero</span> <span class="n">d</span><span class="o">)</span><span class="bp">.</span><span class="n">trans</span> <span class="n">rfl</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">kunion_zero</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">d</span> <span class="o">:</span> <span class="n">m</span><span class="bp">.</span><span class="n">nodup_keys</span><span class="o">),</span> <span class="n">kunion&#39;</span> <span class="n">m</span> <span class="mi">0</span> <span class="bp">=</span> <span class="n">roption</span><span class="bp">.</span><span class="n">some</span> <span class="n">m</span> <span class="o">:=</span>
<span class="n">quotient</span><span class="bp">.</span><span class="n">induction_on</span> <span class="n">m</span> <span class="err">$</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="n">d</span><span class="o">,</span> <span class="o">(</span><span class="n">kunion_coe</span> <span class="n">d</span> <span class="n">nodup_keys_zero</span><span class="o">)</span><span class="bp">.</span><span class="n">trans</span> <span class="o">(</span><span class="k">by</span> <span class="n">simp</span><span class="o">)</span>
</pre></div>

#### [ Sean Leather (Aug 06 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130981382):
<p>One last related question: Now that I have an <code>roption</code>-wrapped <code>multiset</code>, how should I specify theorems that involve the result of <code>kunion'</code>? For example, I had:</p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">mem_kunion</span> <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="n">sigma</span> <span class="n">β</span><span class="o">}</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">d₁</span> <span class="o">:</span> <span class="n">m₁</span><span class="bp">.</span><span class="n">nodup_keys</span><span class="o">)</span> <span class="o">(</span><span class="n">d₂</span> <span class="o">:</span> <span class="n">m₂</span><span class="bp">.</span><span class="n">nodup_keys</span><span class="o">),</span>
  <span class="n">disjoint</span> <span class="n">m₁</span><span class="bp">.</span><span class="n">keys</span> <span class="n">m₂</span><span class="bp">.</span><span class="n">keys</span> <span class="bp">→</span> <span class="o">(</span><span class="n">s</span> <span class="err">∈</span> <span class="n">d₁</span> <span class="n">k</span><span class="err">∪</span> <span class="n">d₂</span> <span class="bp">↔</span> <span class="n">s</span> <span class="err">∈</span> <span class="n">m₁</span> <span class="bp">∨</span> <span class="n">s</span> <span class="err">∈</span> <span class="n">m₂</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">quotient</span><span class="bp">.</span><span class="n">induction_on₂</span> <span class="n">m₁</span> <span class="n">m₂</span> <span class="err">$</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">mem_kunion_iff</span>
</pre></div>


<p>Should this become...?</p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">mem_kunion&#39;</span> <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="n">sigma</span> <span class="n">β</span><span class="o">}</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">d₁</span> <span class="o">:</span> <span class="n">m₁</span><span class="bp">.</span><span class="n">nodup_keys</span><span class="o">)</span> <span class="o">(</span><span class="n">d₂</span> <span class="o">:</span> <span class="n">m₂</span><span class="bp">.</span><span class="n">nodup_keys</span><span class="o">),</span>
  <span class="n">disjoint</span> <span class="n">m₁</span><span class="bp">.</span><span class="n">keys</span> <span class="n">m₂</span><span class="bp">.</span><span class="n">keys</span> <span class="bp">→</span> <span class="bp">∃</span> <span class="n">m</span> <span class="err">∈</span> <span class="n">kunion&#39;</span> <span class="n">m₁</span> <span class="n">m₂</span><span class="o">,</span> <span class="n">s</span> <span class="err">∈</span> <span class="n">m</span> <span class="bp">↔</span> <span class="n">s</span> <span class="err">∈</span> <span class="n">m₁</span> <span class="bp">∨</span> <span class="n">s</span> <span class="err">∈</span> <span class="n">m₂</span> <span class="o">:=</span>
<span class="n">quotient</span><span class="bp">.</span><span class="n">induction_on₂</span> <span class="n">m₁</span> <span class="n">m₂</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">l₁</span> <span class="n">l₂</span> <span class="n">d₁</span> <span class="n">d₂</span> <span class="n">dk</span><span class="o">,</span>
  <span class="bp">⟨_</span><span class="o">,</span> <span class="n">roption</span><span class="bp">.</span><span class="n">eq_some_iff</span><span class="bp">.</span><span class="n">mp</span> <span class="o">(</span><span class="n">kunion_coe</span> <span class="n">d₁</span> <span class="n">d₂</span><span class="o">),</span> <span class="n">mem_kunion_iff</span> <span class="n">dk</span><span class="bp">⟩</span>
</pre></div>


<p>Specifically, I mean: should I use a pattern like <code>∃ m ∈ kunion' m₁ m₂, ...</code> for theorems like this, or is there a better way?</p>

#### [ Mario Carneiro (Aug 06 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130982225):
<p>I would take <code>m ∈ kunion' m₁ m₂</code> as a hypothesis and prove <code>s ∈ m ↔ s ∈ m₁ ∨ s ∈ m₂</code></p>

#### [ Mario Carneiro (Aug 06 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130982297):
<p>of course this hypothesis eliminates the need for d1 and d2</p>

#### [ Mario Carneiro (Aug 06 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130982374):
<p>alternatively, you can define <code>kunion</code> as <code>(kunion' m1 m2).get &lt;d1, d2&gt;</code> and have all your old theorems back</p>

#### [ Sean Leather (Aug 06 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130991221):
<p>True. I'm not sure which is a better definition to work with. If I were using the <code>multiset</code> interface directly, I would lean towards defining <code>kunion</code> as <code>(kunion' m1 m2).get &lt;d1, d2&gt;</code>. But since it's really meant to be the underlying implementation of <code>finmap</code>, perhaps it's not necessary.</p>

#### [ Sean Leather (Aug 06 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/130991299):
<p>Also, do you think I should use <code>roption</code> + <code>quotient.lift_on</code> consistently instead of <code>quotient.hrec_on</code>? I don't have any more uses of <code>quotient.hrec_on₂</code>, but I do have a number of uses of <code>quotient.hrec_on</code>.</p>

#### [ Sean Leather (Aug 07 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131028609):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I'd like to get your thoughts on this <span class="emoji emoji-1f446" title="point up">:point_up:</span>. I haven't had any problems with <code>quotient.hrec_on</code> up to now, but maybe things would just be nicer all around if I used <code>roption</code> more. I'm not sure.</p>

#### [ Mario Carneiro (Aug 07 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131028618):
<p>I think if it works once, it will probably work again</p>

#### [ Mario Carneiro (Aug 07 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131028672):
<p>Also, another option I forgot to mention was to make <code>kunion</code> a nondependent function, using the fact that <code>nodup_keys</code> is decidable</p>

#### [ Sean Leather (Aug 07 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131028674):
<p>Just to be clear about what you mean, do you think I should change the defs <a href="https://github.com/spl/lean-finmap/blob/fb3f562de05059f136f855b88bf616c8aac7f365/src/data/multiset/dict.lean" target="_blank" title="https://github.com/spl/lean-finmap/blob/fb3f562de05059f136f855b88bf616c8aac7f365/src/data/multiset/dict.lean">here</a> to use <code>roption</code>?</p>

#### [ Sean Leather (Aug 07 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131028693):
<p>(Just search for <code>hrec_on</code>.)</p>

#### [ Mario Carneiro (Aug 07 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131028697):
<p>Even if we suppose that checking this is expensive, it doesn't matter if you are just using it as an abstract version so you can prove equations about it</p>

#### [ Sean Leather (Aug 07 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131028702):
<blockquote>
<p>Also, another option I forgot to mention was to make <code>kunion</code> a nondependent function, using the fact that <code>nodup_keys</code> is decidable</p>
</blockquote>
<p>What do you mean by this?</p>

#### [ Mario Carneiro (Aug 07 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131028797):
<p>define <code>kunion m1 m2 = if h : m1.nodup_keys /\ m2.nodup_keys then (kunion' m1 m2).get h else 0</code></p>

#### [ Sean Leather (Aug 07 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131028858):
<p>That's an interesting suggestion.</p>

#### [ Mario Carneiro (Aug 07 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131028874):
<p>in fact, even if <code>nodup_keys</code> wasn't decidable you could make this definition anyway noncomputably and just not use it for evaluation</p>

#### [ Sean Leather (Aug 07 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029010):
<p>Hmm, yes, I think I like this definition of <code>kunion</code>. I don't have to pass around the <code>m1.nodup_keys</code> everywhere.</p>

#### [ Sean Leather (Aug 07 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029031):
<p>Okay, well, I'll play around with it.</p>

#### [ Mario Carneiro (Aug 07 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029032):
<p>Yet more alternatively, you could define the subtype. Didn't you have <code>finmap</code> at one point for this?</p>

#### [ Sean Leather (Aug 07 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029090):
<p>I decided to go with the <code>structure</code> for the same reasons <code>finset</code> is a <code>structure</code>:</p>
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">finmap</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">(</span><span class="n">β</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Type</span> <span class="o">(</span><span class="n">max</span> <span class="n">u</span> <span class="n">v</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">val</span> <span class="o">:</span> <span class="n">multiset</span> <span class="o">(</span><span class="n">sigma</span> <span class="n">β</span><span class="o">))</span>
<span class="o">(</span><span class="n">nodup_keys</span> <span class="o">:</span> <span class="n">val</span><span class="bp">.</span><span class="n">nodup_keys</span><span class="o">)</span>
</pre></div>

#### [ Sean Leather (Aug 07 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029097):
<p>Mainly, for type class instance resolution.</p>

#### [ Mario Carneiro (Aug 07 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029099):
<p>that's fine, my point was that you can define <code>finmap.rec_on</code> to encapsulate this definition pattern</p>

#### [ Mario Carneiro (Aug 07 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029112):
<p>and this way you never have to carry around any proofs since they are embedded in the type</p>

#### [ Sean Leather (Aug 07 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029158):
<p>You mean the <code>if h : m.nodup_keys ... then ... else ...</code> pattern?</p>

#### [ Mario Carneiro (Aug 07 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029160):
<p>no, the <code>roption</code> or <code>hrec_on</code> version</p>

#### [ Mario Carneiro (Aug 07 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029167):
<p>(it doesn't really matter too much which one you use, since it only has to be done once)</p>

#### [ Sean Leather (Aug 07 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029228):
<p>Oh.... I'm awfully dumb today. So, define a <code>finmap.rec_on</code> that takes an <code>roption (multiset (sigma β))</code> to a <code>finmap</code>?</p>

#### [ Sean Leather (Aug 07 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029236):
<p>Err, actually the arrow goes the other way...</p>

#### [ Sean Leather (Aug 07 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029244):
<p>Anyway, it'd be a higher-order function.</p>

#### [ Sean Leather (Aug 07 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029247):
<p>Yeah, I think I see it.</p>

#### [ Mario Carneiro (Aug 07 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029289):
<p><code>finmap.rec_on</code> takes a <code>finmap A B</code>, a function <code>list (sigma B) -&gt; C</code>, and a proof that this function is equal up to permutation when the arguments have <code>nodup_keys</code></p>

#### [ Sean Leather (Aug 07 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029296):
<p>Right.</p>

#### [ Sean Leather (Aug 07 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029372):
<p>So, given that, I would be skipping defining all of the defs and theorems for <code>multiset</code> and define them for only <code>list</code> and <code>finmap</code>?</p>

#### [ Mario Carneiro (Aug 07 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029445):
<p>right</p>

#### [ Mario Carneiro (Aug 07 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029450):
<p>You can reconstruct the multiset definitions from the finmap ones by the <code>if ... else 0</code> trick</p>

#### [ Mario Carneiro (Aug 07 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029516):
<p>I think multisets are a good stepping stone if you can actually define functions on them, but in your case the functions already have to assume nodup just to be well defined, so they've already jumped to finmap</p>

#### [ Sean Leather (Aug 07 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029523):
<p>That's true.</p>

#### [ Sean Leather (Aug 07 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029576):
<p>Okay, I'm convinced.</p>

#### [ Mario Carneiro (Aug 07 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029713):
<p>I notice you have theorems like <code> s.1 ∈ (m.map_snd f).keys ↔ s.1 ∈ m.keys</code> with several variations. Why isn't this just <code>(m.map_snd f).keys = m.keys</code>?</p>

#### [ Sean Leather (Aug 07 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029750):
<p>Because I use the <code>mem</code> one in the non-<code>mem</code>.</p>

#### [ Sean Leather (Aug 07 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029791):
<p>I suppose I don't have to.</p>

#### [ Mario Carneiro (Aug 07 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029808):
<p>the proof is just <code>map_comp</code></p>

#### [ Mario Carneiro (Aug 07 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029819):
<p>you shouldn't use <code>mem</code> to try to characterize a multiset, it gets messy</p>

#### [ Sean Leather (Aug 07 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029874):
<p>The other problem with the <code>map_snd</code>/<code>keys</code> theorems is that I wanted to use it in <code>finmap</code>, but the best I could come up with was using <code>[inhabited (∀ a, β₁ a)]</code>. I'm not happy with that solution.</p>

#### [ Sean Leather (Aug 07 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029887):
<blockquote>
<p>the proof is just <code>map_comp</code></p>
</blockquote>
<p>The proof of which?</p>

#### [ Mario Carneiro (Aug 07 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131029966):
<p>I'm really confused about your confusion. It should be provable that <code>(m.map_snd f).keys = m.keys</code>, this makes the last 7 theorems or so unnecessary and it doesn't require any weird assumptions</p>

#### [ Sean Leather (Aug 07 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131030141):
<p>Okay, I think I see what you're saying. I'll give it a shot.</p>

#### [ Mario Carneiro (Aug 07 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131030157):
<p>wait, just the last 4. The ones about <code>(m.map f).keys</code> are a bit awkward because <code>f : sigma B1 -&gt; sigma B2</code> can mingle keys and values in an unpredictable way. How about defining <code>m.map f g</code> where <code>f : A1 -&gt; A2</code> and <code>g : ∀ a, B1 a -&gt; B2 (f a)</code>; then you should be able to prove <code>(m.map f g).keys = m.keys.map f</code> and life is good</p>

#### [ Sean Leather (Aug 07 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131030231):
<p>Btw, did you mean <code>map_map</code> instead of <code>map_comp</code>?</p>

#### [ Mario Carneiro (Aug 07 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131030275):
<p>yes</p>

#### [ Mario Carneiro (Aug 07 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131030288):
<p>it's written backwards for simp lemmas because <code>comp</code> is dumb</p>

#### [ Mario Carneiro (Aug 07 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131030292):
<p>so the name becomes <code>map_map</code> instead of <code>map_comp</code></p>

#### [ Sean Leather (Aug 08 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131093639):
<p>I could only figure out how to do a general 2-arg <code>finmap</code> recursor using <code>quotient.hrec_on₂</code>:</p>
<div class="codehilite"><pre><span></span><span class="kn">protected</span> <span class="n">def</span> <span class="n">lrec_on₂</span> <span class="o">{</span><span class="n">γ</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="n">g</span> <span class="o">:</span> <span class="n">finmap</span> <span class="n">α</span> <span class="n">β</span><span class="o">)</span>
  <span class="o">(</span><span class="n">φ</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">l₁</span> <span class="n">l₂</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">sigma</span> <span class="n">β</span><span class="o">)},</span> <span class="n">l₁</span><span class="bp">.</span><span class="n">nodup_keys</span> <span class="bp">→</span> <span class="n">l₂</span><span class="bp">.</span><span class="n">nodup_keys</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">)</span>
  <span class="o">(</span><span class="n">c</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">l₁</span> <span class="n">l₂</span> <span class="n">l₃</span> <span class="n">l₄</span><span class="o">}</span> <span class="o">(</span><span class="n">p₁₃</span> <span class="o">:</span> <span class="n">l₁</span> <span class="bp">~</span> <span class="n">l₃</span><span class="o">)</span> <span class="o">(</span><span class="n">p₂₄</span> <span class="o">:</span> <span class="n">l₂</span> <span class="bp">~</span> <span class="n">l₄</span><span class="o">)</span> <span class="n">d₁</span> <span class="n">d₂</span> <span class="n">d₃</span> <span class="n">d₄</span><span class="o">,</span> <span class="n">φ</span> <span class="n">d₁</span> <span class="n">d₂</span> <span class="bp">=</span> <span class="n">φ</span> <span class="n">d₃</span> <span class="n">d₄</span><span class="o">)</span> <span class="o">:</span> <span class="n">γ</span> <span class="o">:=</span>
<span class="bp">@</span><span class="n">quotient</span><span class="bp">.</span><span class="n">hrec_on₂</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">m₁</span> <span class="n">m₂</span> <span class="o">:</span> <span class="n">multiset</span> <span class="o">(</span><span class="n">sigma</span> <span class="n">β</span><span class="o">)),</span> <span class="n">m₁</span><span class="bp">.</span><span class="n">nodup_keys</span> <span class="bp">→</span> <span class="n">m₂</span><span class="bp">.</span><span class="n">nodup_keys</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">)</span>
  <span class="n">f</span><span class="bp">.</span><span class="n">val</span> <span class="n">g</span><span class="bp">.</span><span class="n">val</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">l₁</span> <span class="n">l₂</span> <span class="o">(</span><span class="n">d₁</span> <span class="o">:</span> <span class="n">l₁</span><span class="bp">.</span><span class="n">nodup_keys</span><span class="o">)</span> <span class="o">(</span><span class="n">d₂</span> <span class="o">:</span> <span class="n">l₂</span><span class="bp">.</span><span class="n">nodup_keys</span><span class="o">),</span> <span class="n">φ</span> <span class="n">d₁</span> <span class="n">d₂</span><span class="o">)</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">l₁</span> <span class="n">l₂</span> <span class="n">l₃</span> <span class="n">l₄</span> <span class="n">p₁₃</span> <span class="n">p₂₄</span><span class="o">,</span> <span class="n">hfunext</span> <span class="o">(</span><span class="k">by</span> <span class="n">rw</span> <span class="n">list</span><span class="bp">.</span><span class="n">perm_nodup_keys</span> <span class="n">p₁₃</span><span class="o">)</span> <span class="err">$</span>
    <span class="bp">λ</span> <span class="n">d₁</span> <span class="n">d₃</span> <span class="bp">_</span><span class="o">,</span> <span class="n">hfunext</span> <span class="o">(</span><span class="k">by</span> <span class="n">rw</span> <span class="n">list</span><span class="bp">.</span><span class="n">perm_nodup_keys</span> <span class="n">p₂₄</span><span class="o">)</span> <span class="err">$</span>
      <span class="bp">λ</span> <span class="n">d₂</span> <span class="n">d₄</span> <span class="bp">_</span><span class="o">,</span> <span class="n">heq_of_eq</span> <span class="err">$</span> <span class="n">c</span> <span class="n">p₁₃</span> <span class="n">p₂₄</span> <span class="n">d₁</span> <span class="n">d₂</span> <span class="n">d₃</span> <span class="n">d₄</span><span class="o">)</span>
  <span class="n">f</span><span class="bp">.</span><span class="n">nodup_keys</span> <span class="n">g</span><span class="bp">.</span><span class="n">nodup_keys</span>
</pre></div>


<p>I have a general 2-arg <code>finmap.lift_on₂</code>:</p>
<div class="codehilite"><pre><span></span><span class="kn">protected</span> <span class="n">def</span> <span class="n">lift_on₂</span> <span class="o">{</span><span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span>
  <span class="o">(</span><span class="n">f</span> <span class="n">g</span> <span class="o">:</span> <span class="n">finmap</span> <span class="n">α</span> <span class="n">β</span><span class="o">)</span>
  <span class="o">(</span><span class="n">φ</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">l₁</span> <span class="n">l₂</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">sigma</span> <span class="n">β</span><span class="o">)},</span> <span class="n">l₁</span><span class="bp">.</span><span class="n">nodup_keys</span> <span class="bp">→</span> <span class="n">l₂</span><span class="bp">.</span><span class="n">nodup_keys</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">)</span>
  <span class="o">(</span><span class="n">c</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">l₁</span> <span class="n">l₂</span> <span class="n">l₃</span> <span class="n">l₄</span><span class="o">}</span> <span class="o">(</span><span class="n">p₁₃</span> <span class="o">:</span> <span class="n">l₁</span> <span class="bp">~</span> <span class="n">l₃</span><span class="o">)</span> <span class="o">(</span><span class="n">p₂₄</span> <span class="o">:</span> <span class="n">l₂</span> <span class="bp">~</span> <span class="n">l₄</span><span class="o">)</span> <span class="n">d₁</span> <span class="n">d₂</span> <span class="n">d₃</span> <span class="n">d₄</span><span class="o">,</span> <span class="n">φ</span> <span class="n">d₁</span> <span class="n">d₂</span> <span class="bp">=</span> <span class="n">φ</span> <span class="n">d₃</span> <span class="n">d₄</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">roption</span> <span class="n">γ</span> <span class="o">:=</span>
<span class="n">quotient</span><span class="bp">.</span><span class="n">lift_on₂</span> <span class="n">f</span><span class="bp">.</span><span class="n">val</span> <span class="n">g</span><span class="bp">.</span><span class="n">val</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">l₁</span> <span class="n">l₂</span><span class="o">,</span> <span class="n">roption</span><span class="bp">.</span><span class="n">mk</span> <span class="o">(</span><span class="n">l₁</span><span class="bp">.</span><span class="n">nodup_keys</span> <span class="bp">∧</span> <span class="n">l₂</span><span class="bp">.</span><span class="n">nodup_keys</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="bp">⟨</span><span class="n">d₁</span><span class="o">,</span> <span class="n">d₂</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">φ</span> <span class="n">d₁</span> <span class="n">d₂</span><span class="o">))</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">l₁</span> <span class="n">l₂</span> <span class="n">l₃</span> <span class="n">l₄</span> <span class="n">p₁₃</span> <span class="n">p₂₄</span><span class="o">,</span> <span class="n">roption</span><span class="bp">.</span><span class="n">ext&#39;</span>
    <span class="o">(</span><span class="n">and_congr</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">perm_nodup_keys</span> <span class="n">p₁₃</span><span class="o">)</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">perm_nodup_keys</span> <span class="n">p₂₄</span><span class="o">))</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="bp">⟨</span><span class="n">d₁</span><span class="o">,</span> <span class="n">d₂</span><span class="bp">⟩</span> <span class="bp">⟨</span><span class="n">d₃</span><span class="o">,</span> <span class="n">d₄</span><span class="bp">⟩</span><span class="o">,</span> <span class="n">c</span> <span class="n">p₁₃</span> <span class="n">p₂₄</span> <span class="n">d₁</span> <span class="n">d₂</span> <span class="n">d₃</span> <span class="n">d₄</span><span class="o">))</span>
</pre></div>


<p>But it seems like the <code>roption.dom</code> has a pair of lists, so this only seems useful in combination with <code>quotient.induction_on₂</code>. Is that right? Or can I do better?</p>

#### [ Mario Carneiro (Aug 08 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131094611):
<p>What does the one arg version look like?</p>

#### [ Sean Leather (Aug 08 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131094622):
<div class="codehilite"><pre><span></span><span class="kn">protected</span> <span class="n">def</span> <span class="n">lrec_on</span> <span class="o">{</span><span class="n">γ</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">finmap</span> <span class="n">α</span> <span class="n">β</span><span class="o">)</span>
  <span class="o">(</span><span class="n">φ</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">l</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">sigma</span> <span class="n">β</span><span class="o">)},</span> <span class="n">l</span><span class="bp">.</span><span class="n">nodup_keys</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">)</span>
  <span class="o">(</span><span class="n">c</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">l₁</span> <span class="n">l₂</span><span class="o">}</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">l₁</span> <span class="bp">~</span> <span class="n">l₂</span><span class="o">)</span> <span class="n">d₁</span> <span class="n">d₂</span><span class="o">,</span> <span class="n">φ</span> <span class="n">d₁</span> <span class="bp">=</span> <span class="n">φ</span> <span class="n">d₂</span><span class="o">)</span> <span class="o">:</span> <span class="n">γ</span> <span class="o">:=</span>
<span class="bp">@</span><span class="n">quotient</span><span class="bp">.</span><span class="n">hrec_on</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">m</span> <span class="o">:</span> <span class="n">multiset</span> <span class="o">(</span><span class="n">sigma</span> <span class="n">β</span><span class="o">)),</span> <span class="n">m</span><span class="bp">.</span><span class="n">nodup_keys</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">)</span>
  <span class="n">f</span><span class="bp">.</span><span class="n">val</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">l</span> <span class="o">(</span><span class="n">d</span> <span class="o">:</span> <span class="n">l</span><span class="bp">.</span><span class="n">nodup_keys</span><span class="o">),</span> <span class="n">φ</span> <span class="n">d</span><span class="o">)</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">l₁</span> <span class="n">l₂</span> <span class="n">p</span><span class="o">,</span> <span class="n">hfunext</span> <span class="o">(</span><span class="k">by</span> <span class="n">rw</span> <span class="n">list</span><span class="bp">.</span><span class="n">perm_nodup_keys</span> <span class="n">p</span><span class="o">)</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">d₁</span> <span class="n">d₂</span> <span class="bp">_</span><span class="o">,</span> <span class="n">heq_of_eq</span> <span class="err">$</span> <span class="n">c</span> <span class="n">p</span> <span class="n">d₁</span> <span class="n">d₂</span><span class="o">)</span>
  <span class="n">f</span><span class="bp">.</span><span class="n">nodup_keys</span>
</pre></div>

#### [ Sean Leather (Aug 08 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131094845):
<p>There are theorems where <code>quotient.induction_on₂</code> needs more than just <code>l₁.nodup_keys</code> and <code>l₂.nodup_keys</code>:</p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">mem_kunion&#39;</span> <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="n">sigma</span> <span class="n">β</span><span class="o">}</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">d₁</span> <span class="o">:</span> <span class="n">m₁</span><span class="bp">.</span><span class="n">nodup_keys</span><span class="o">)</span> <span class="o">(</span><span class="n">d₂</span> <span class="o">:</span> <span class="n">m₂</span><span class="bp">.</span><span class="n">nodup_keys</span><span class="o">),</span>
  <span class="n">disjoint</span> <span class="n">m₁</span><span class="bp">.</span><span class="n">keys</span> <span class="n">m₂</span><span class="bp">.</span><span class="n">keys</span> <span class="bp">→</span> <span class="bp">∃</span> <span class="n">m</span> <span class="err">∈</span> <span class="n">kunion&#39;</span> <span class="n">m₁</span> <span class="n">m₂</span><span class="o">,</span> <span class="n">s</span> <span class="err">∈</span> <span class="n">m</span> <span class="bp">↔</span> <span class="n">s</span> <span class="err">∈</span> <span class="n">m₁</span> <span class="bp">∨</span> <span class="n">s</span> <span class="err">∈</span> <span class="n">m₂</span> <span class="o">:=</span>
<span class="n">quotient</span><span class="bp">.</span><span class="n">induction_on₂</span> <span class="n">m₁</span> <span class="n">m₂</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">l₁</span> <span class="n">l₂</span> <span class="n">d₁</span> <span class="n">d₂</span> <span class="n">dk</span><span class="o">,</span>
  <span class="bp">⟨_</span><span class="o">,</span> <span class="n">roption</span><span class="bp">.</span><span class="n">eq_some_iff</span><span class="bp">.</span><span class="n">mp</span> <span class="o">(</span><span class="n">kunion_coe</span> <span class="n">d₁</span> <span class="n">d₂</span><span class="o">),</span> <span class="n">mem_kunion_iff</span> <span class="n">dk</span><span class="bp">⟩</span>
</pre></div>


<p>So, I think the above <code>finmap.lift_on₂</code> definition makes sense.</p>

#### [ Mario Carneiro (Aug 08 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131098994):
<p>I would suggest you state <code>lrec_on</code> like this:</p>
<div class="codehilite"><pre><span></span>protected def lrec_on {γ : Sort*} (f : finmap α β)
  (φ : list (sigma β) → γ)
  (c : ∀ {l₁ l₂} (p : l₁ ~ l₂), l₁.nodup_keys → l₂.nodup_keys → φ l₁ = φ l₂) : γ :=
</pre></div>


<p>Recall that we are trying to avoid partial functions. The function <code>φ</code> is defined on lists, so there presumably won't be any trouble making arbitrary choices that depend on the order</p>

#### [ Mario Carneiro (Aug 08 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131099010):
<p>Given this it should not be hard to just iterate it twice to get <code>lrec_on₂</code></p>

#### [ Sean Leather (Aug 08 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/quotient.hrec_on%E2%82%82/near/131103716):
<p>Okay, so I have the following.</p>
<p>My initial version:</p>
<div class="codehilite"><pre><span></span><span class="kn">protected</span> <span class="n">def</span> <span class="n">lrec_on</span> <span class="o">{</span><span class="n">γ</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">finmap</span> <span class="n">α</span> <span class="n">β</span><span class="o">)</span>
  <span class="o">(</span><span class="n">φ</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">l</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">sigma</span> <span class="n">β</span><span class="o">)},</span> <span class="n">l</span><span class="bp">.</span><span class="n">nodup_keys</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">)</span>
  <span class="o">(</span><span class="n">c</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">l₁</span> <span class="n">l₂</span><span class="o">}</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">l₁</span> <span class="bp">~</span> <span class="n">l₂</span><span class="o">)</span> <span class="n">d₁</span> <span class="n">d₂</span><span class="o">,</span> <span class="n">φ</span> <span class="n">d₁</span> <span class="bp">=</span> <span class="n">φ</span> <span class="n">d₂</span><span class="o">)</span> <span class="o">:</span> <span class="n">γ</span> <span class="o">:=</span>
<span class="bp">@</span><span class="n">quotient</span><span class="bp">.</span><span class="n">hrec_on</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">m</span> <span class="o">:</span> <span class="n">multiset</span> <span class="o">(</span><span class="n">sigma</span> <span class="n">β</span><span class="o">)),</span> <span class="n">m</span><span class="bp">.</span><span class="n">nodup_keys</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">)</span>
  <span class="n">f</span><span class="bp">.</span><span class="n">val</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">l</span> <span class="o">(</span><span class="n">d</span> <span class="o">:</span> <span class="n">l</span><span class="bp">.</span><span class="n">nodup_keys</span><span class="o">),</span> <span class="n">φ</span> <span class="n">d</span><span class="o">)</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">l₁</span> <span class="n">l₂</span> <span class="n">p</span><span class="o">,</span> <span class="n">hfunext</span> <span class="o">(</span><span class="k">by</span> <span class="n">rw</span> <span class="n">list</span><span class="bp">.</span><span class="n">perm_nodup_keys</span> <span class="n">p</span><span class="o">)</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">d₁</span> <span class="n">d₂</span> <span class="bp">_</span><span class="o">,</span> <span class="n">heq_of_eq</span> <span class="err">$</span> <span class="n">c</span> <span class="n">p</span> <span class="n">d₁</span> <span class="n">d₂</span><span class="o">)</span>
  <span class="n">f</span><span class="bp">.</span><span class="n">nodup_keys</span>

<span class="n">def</span> <span class="n">erase</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">finmap</span> <span class="n">α</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">finmap</span> <span class="n">α</span> <span class="n">β</span> <span class="o">:=</span>
<span class="n">finmap</span><span class="bp">.</span><span class="n">lrec_on</span> <span class="n">f</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">l</span> <span class="n">d</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">l</span><span class="bp">.</span><span class="n">kerase</span> <span class="n">a</span><span class="o">,</span> <span class="n">list</span><span class="bp">.</span><span class="n">nodup_keys_kerase</span> <span class="n">a</span> <span class="n">d</span><span class="bp">⟩</span><span class="o">)</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">l₁</span> <span class="n">l₂</span> <span class="n">p</span> <span class="n">d₁</span> <span class="n">d₂</span><span class="o">,</span> <span class="n">eq_of_veq</span> <span class="err">$</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">sound</span> <span class="err">$</span> <span class="n">list</span><span class="bp">.</span><span class="n">perm_kerase</span> <span class="n">a</span> <span class="n">d₁</span> <span class="n">d₂</span> <span class="n">p</span><span class="o">)</span>
</pre></div>


<p>Your suggestion:</p>
<div class="codehilite"><pre><span></span><span class="kn">protected</span> <span class="n">def</span> <span class="n">lrec_on&#39;</span> <span class="o">{</span><span class="n">γ</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">finmap</span> <span class="n">α</span> <span class="n">β</span><span class="o">)</span>
  <span class="o">(</span><span class="n">φ</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">sigma</span> <span class="n">β</span><span class="o">)</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">)</span>
  <span class="o">(</span><span class="n">c</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">l₁</span> <span class="n">l₂</span><span class="o">}</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">l₁</span> <span class="bp">~</span> <span class="n">l₂</span><span class="o">),</span> <span class="n">l₁</span><span class="bp">.</span><span class="n">nodup_keys</span> <span class="bp">→</span> <span class="n">l₂</span><span class="bp">.</span><span class="n">nodup_keys</span> <span class="bp">→</span> <span class="n">φ</span> <span class="n">l₁</span> <span class="bp">=</span> <span class="n">φ</span> <span class="n">l₂</span><span class="o">)</span> <span class="o">:</span> <span class="n">γ</span> <span class="o">:=</span>
<span class="bp">@</span><span class="n">quotient</span><span class="bp">.</span><span class="n">hrec_on</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">m</span> <span class="o">:</span> <span class="n">multiset</span> <span class="o">(</span><span class="n">sigma</span> <span class="n">β</span><span class="o">)),</span> <span class="n">m</span><span class="bp">.</span><span class="n">nodup_keys</span> <span class="bp">→</span> <span class="n">γ</span><span class="o">)</span>
  <span class="n">f</span><span class="bp">.</span><span class="n">val</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">l</span> <span class="bp">_</span><span class="o">,</span> <span class="n">φ</span> <span class="n">l</span><span class="o">)</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">l₁</span> <span class="n">l₂</span> <span class="n">p</span><span class="o">,</span> <span class="n">hfunext</span> <span class="o">(</span><span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">list</span><span class="bp">.</span><span class="n">perm_nodup_keys</span> <span class="n">p</span><span class="o">])</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">d₁</span> <span class="n">d₂</span> <span class="bp">_</span><span class="o">,</span> <span class="n">heq_of_eq</span> <span class="err">$</span> <span class="n">c</span> <span class="n">p</span> <span class="n">d₁</span> <span class="n">d₂</span><span class="o">)</span>
  <span class="n">f</span><span class="bp">.</span><span class="n">nodup_keys</span>

<span class="n">def</span> <span class="n">erase&#39;</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">finmap</span> <span class="n">α</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">finmap</span> <span class="n">α</span> <span class="n">β</span> <span class="o">:=</span>
<span class="n">finmap</span><span class="bp">.</span><span class="n">lrec_on&#39;</span> <span class="n">f</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">l</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">l</span><span class="bp">.</span><span class="n">kerase</span> <span class="n">a</span><span class="o">,</span> <span class="n">list</span><span class="bp">.</span><span class="n">nodup_keys_kerase</span> <span class="n">a</span> <span class="bp">_⟩</span><span class="o">)</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">l₁</span> <span class="n">l₂</span> <span class="n">p</span> <span class="n">d₁</span> <span class="n">d₂</span><span class="o">,</span> <span class="n">eq_of_veq</span> <span class="err">$</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">sound</span> <span class="err">$</span> <span class="n">list</span><span class="bp">.</span><span class="n">perm_kerase</span> <span class="n">a</span> <span class="n">d₁</span> <span class="n">d₂</span> <span class="n">p</span><span class="o">)</span>
</pre></div>


<p>I can define <code>erase</code> with <code>lrec_on</code>, but how do I define <code>erase'</code> with <code>lrec_on'</code>?</p>
<div class="codehilite"><pre><span></span><span class="n">error</span><span class="o">:</span> <span class="n">don&#39;t</span> <span class="n">know</span> <span class="n">how</span> <span class="n">to</span> <span class="n">synthesize</span> <span class="n">placeholder</span>
<span class="kn">context</span><span class="o">:</span>
<span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">decidable_eq</span> <span class="n">α</span><span class="o">,</span>
<span class="n">β</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Type</span> <span class="n">v</span><span class="o">,</span>
<span class="n">f</span> <span class="o">:</span> <span class="n">finmap</span> <span class="n">α</span> <span class="n">β</span><span class="o">,</span>
<span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span>
<span class="n">l</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">sigma</span> <span class="n">β</span><span class="o">)</span>
<span class="err">⊢</span> <span class="n">list</span><span class="bp">.</span><span class="n">nodup_keys</span> <span class="n">l</span>
</pre></div>


{% endraw %}
