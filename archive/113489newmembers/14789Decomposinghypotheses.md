---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/14789Decomposinghypotheses.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [Decomposing hypotheses](https://leanprover-community.github.io/archive/113489newmembers/14789Decomposinghypotheses.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Ken Roe (Jul 25 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130287397):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">test_split</span> <span class="o">{</span> <span class="n">P</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">}</span> <span class="o">{</span> <span class="n">Q</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">}</span> <span class="o">{</span> <span class="n">R</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">}</span> <span class="o">{</span> <span class="n">S</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">}</span> <span class="o">:</span>
    <span class="o">(</span><span class="n">P</span> <span class="bp">∧</span> <span class="o">(</span><span class="n">Q</span> <span class="bp">∨</span> <span class="n">R</span><span class="o">))</span> <span class="bp">→</span> <span class="o">(</span><span class="n">Q</span> <span class="bp">→</span> <span class="n">S</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="n">R</span> <span class="bp">→</span> <span class="n">S</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="n">P</span> <span class="bp">∧</span> <span class="n">S</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
    <span class="n">intros</span><span class="o">,</span> <span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>


<p>Is there a nice way to decompose the hypotheses to prove the above theorem?  What should "sorry" be replaced with?</p>

#### [ Reid Barton (Jul 25 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130287654):
<p><code>tauto</code> gets the job done in this case</p>

#### [ Reid Barton (Jul 25 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130287735):
<p>Manually, you could use <code>cases</code>, for example</p>
<div class="codehilite"><pre><span></span>    <span class="n">cases</span> <span class="n">pqr</span> <span class="k">with</span> <span class="n">p</span> <span class="n">qr</span><span class="o">,</span>
    <span class="n">refine</span> <span class="bp">⟨</span><span class="n">p</span><span class="o">,</span> <span class="bp">_⟩</span><span class="o">,</span>
    <span class="n">cases</span> <span class="n">qr</span> <span class="k">with</span> <span class="n">q</span> <span class="n">r</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">exact</span> <span class="n">qs</span> <span class="n">q</span> <span class="o">},</span>
    <span class="o">{</span> <span class="n">exact</span> <span class="n">rs</span> <span class="n">r</span> <span class="o">}</span>
</pre></div>

#### [ Ken Roe (Jul 25 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130288011):
<p>Where can I find tauto?  It is not in the standard libraries.</p>

#### [ Reid Barton (Jul 25 2018 at 18:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130288034):
<p>It's in mathlib</p>

#### [ Ken Roe (Jul 25 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130292466):
<p>Now for a more complex example,</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">test_split</span> <span class="o">{</span> <span class="n">P</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span> <span class="o">}</span> <span class="o">{</span> <span class="n">Q</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span> <span class="o">}</span> <span class="o">{</span> <span class="n">R</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span> <span class="o">}</span> <span class="o">{</span> <span class="n">S</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span> <span class="o">}</span> <span class="o">:</span>
    <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">P</span> <span class="n">x</span> <span class="bp">∧</span> <span class="o">(</span><span class="n">Q</span> <span class="n">x</span> <span class="bp">∨</span> <span class="n">R</span> <span class="n">x</span><span class="o">))</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">Q</span> <span class="n">x</span> <span class="bp">→</span> <span class="n">S</span> <span class="n">x</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">R</span> <span class="n">x</span> <span class="bp">→</span> <span class="n">S</span> <span class="n">x</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">P</span> <span class="n">x</span> <span class="bp">∧</span> <span class="n">S</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
    <span class="n">intros</span><span class="o">,</span> <span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>


<p>After the intros, is there a nice way to decompose these hypotheses?</p>

#### [ Patrick Massot (Jul 25 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130292689):
<p>I'm not sure what you are looking for, but here is a short proof using <code>tauto</code>:</p>

#### [ Patrick Massot (Jul 25 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130292693):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">test_split</span> <span class="o">{</span> <span class="n">P</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span> <span class="o">}</span> <span class="o">{</span> <span class="n">Q</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span> <span class="o">}</span> <span class="o">{</span> <span class="n">R</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span> <span class="o">}</span> <span class="o">{</span> <span class="n">S</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span> <span class="o">}</span> <span class="o">:</span>
    <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">P</span> <span class="n">x</span> <span class="bp">∧</span> <span class="o">(</span><span class="n">Q</span> <span class="n">x</span> <span class="bp">∨</span> <span class="n">R</span> <span class="n">x</span><span class="o">))</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">Q</span> <span class="n">x</span> <span class="bp">→</span> <span class="n">S</span> <span class="n">x</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">R</span> <span class="n">x</span> <span class="bp">→</span> <span class="n">S</span> <span class="n">x</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">P</span> <span class="n">x</span> <span class="bp">∧</span> <span class="n">S</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
    <span class="n">intros</span> <span class="n">h</span> <span class="n">h&#39;</span> <span class="n">h&#39;&#39;</span> <span class="n">x</span><span class="o">,</span>
    <span class="n">specialize</span> <span class="n">h</span> <span class="n">x</span><span class="o">,</span>
    <span class="n">specialize</span> <span class="n">h&#39;</span> <span class="n">x</span><span class="o">,</span>
    <span class="n">specialize</span> <span class="n">h&#39;&#39;</span> <span class="n">x</span><span class="o">,</span>
    <span class="n">tauto</span>
<span class="kn">end</span>
</pre></div>

#### [ Patrick Massot (Jul 25 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130292772):
<p>I'm not sure we currently have any tactic that can guess the <code>specialize</code> steps.</p>

#### [ Patrick Massot (Jul 25 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130292790):
<p>If you really really want one, then the standard procedure is to hope Simon will pity you.</p>

#### [ Simon Hudon (Jul 25 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130293761):
<p>Haha! I'm pretty merciful though</p>

#### [ Simon Hudon (Jul 25 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130293765):
<p>Have you tried <code>solve_by_elim</code>?</p>

#### [ Patrick Massot (Jul 25 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130293837):
<p>It doesn't work</p>

#### [ Patrick Massot (Jul 25 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130294047):
<p>Btw Simon, how was your tauto lecture?</p>

#### [ Simon Hudon (Jul 25 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130294182):
<p>You can shrink the proof down to:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">test_split</span> <span class="o">{</span> <span class="n">P</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span> <span class="o">}</span> <span class="o">{</span> <span class="n">Q</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span> <span class="o">}</span> <span class="o">{</span> <span class="n">R</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span> <span class="o">}</span> <span class="o">{</span> <span class="n">S</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span> <span class="o">}</span> <span class="o">:</span>
    <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">P</span> <span class="n">x</span> <span class="bp">∧</span> <span class="o">(</span><span class="n">Q</span> <span class="n">x</span> <span class="bp">∨</span> <span class="n">R</span> <span class="n">x</span><span class="o">))</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">Q</span> <span class="n">x</span> <span class="bp">→</span> <span class="n">S</span> <span class="n">x</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">R</span> <span class="n">x</span> <span class="bp">→</span> <span class="n">S</span> <span class="n">x</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">P</span> <span class="n">x</span> <span class="bp">∧</span> <span class="n">S</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
    <span class="n">intros</span> <span class="n">h</span> <span class="n">h&#39;</span> <span class="n">h&#39;&#39;</span> <span class="n">x</span><span class="o">,</span>
    <span class="n">specialize</span> <span class="n">h</span> <span class="n">x</span><span class="o">,</span>
    <span class="n">split</span><span class="bp">;</span> <span class="n">tauto</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Simon Hudon (Jul 25 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130294259):
<p>I'm giving it tonight and I decided to talk about <code>pi_instances</code> after all. 5 minutes is so incredibly short :D</p>

#### [ Patrick Massot (Jul 25 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130294306):
<p>Did you prepare a heavily commented version of the source?</p>

#### [ Simon Hudon (Jul 25 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130294601):
<p>What I decided to do is write an instance for <code>group</code> and show how automation shrinks it. And then I mention that <code>refine_struct</code> is written in Lean</p>

#### [ Mario Carneiro (Jul 26 2018 at 03:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Decomposing%20hypotheses/near/130314506):
<p><code>rintro</code> is a really nice way of doing all that</p>
<div class="codehilite"><pre><span></span>theorem test_split {P Q R S : Prop} :
  P ∧ (Q ∨ R) → (Q → S) → (R → S) → P ∧ S :=
begin
  rintro ⟨hp, hq | hr⟩ qs rs,
  { exact ⟨hp, qs hq⟩ },
  { exact ⟨hp, rs hr⟩ }
end
</pre></div>


{% endraw %}
