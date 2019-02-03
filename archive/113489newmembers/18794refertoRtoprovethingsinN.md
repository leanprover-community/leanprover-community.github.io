---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/18794refertoRtoprovethingsinN.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [refer to R to prove things in N?](https://leanprover-community.github.io/archive/113489newmembers/18794refertoRtoprovethingsinN.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Abhimanyu Pallavi Sudhir (Oct 12 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135640902):
<p>I'm proving that there is no natural number such that 2n = 1. One way of doing this would be to point out that multiplication by a non-zero constant is injective, and that multiplication in R generalises multiplication in N, and since we already have 2*(1/2) = 1, this would imply n = 1/2, which is not a natural number.</p>

#### [ Kenny Lau (Oct 12 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135640913):
<p>and yet you asked us about why you need universes to prove fermat's last theorem :P</p>

#### [ Mario Carneiro (Oct 12 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135640918):
<p>they are both valid questions</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 12 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135640970):
<p>My question is: Can this be formalised in Lean? How would you state "multiplication in R generalises multiplication in N"?</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 12 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135640977):
<p>Ok, wait, you can state that pretty easily, but how would you use that?</p>

#### [ Kenny Lau (Oct 12 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135640979):
<p>nat.cast_mul, I guess</p>

#### [ Kenny Lau (Oct 12 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135640982):
<p>but you see</p>

#### [ Kenny Lau (Oct 12 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135640987):
<p>how would you prove that 1/2 is not a natural number?</p>

#### [ Mario Carneiro (Oct 12 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135640994):
<p>There are other ways to prove that theorem, but sure you can do it that way</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 12 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135641022):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span>  1/2 is not natural because 1/2 is between 0 and 1, but 1 is the successor of 0 and nothing can be between an element and its successor.</p>

#### [ Kenny Lau (Oct 12 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135641070):
<p>so you also want nat.cast_lt :P</p>

#### [ Kenny Lau (Oct 12 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135641082):
<p>can't <code>omega</code> solve this? <span class="user-mention" data-user-id="110049">@Mario Carneiro</span></p>

#### [ Kenny Lau (Oct 12 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135641173):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="mi">2</span><span class="bp">*</span><span class="n">n</span> <span class="bp">≠</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">n</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cases_on</span> <span class="n">n</span> <span class="n">dec_trivial</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">n</span> <span class="n">H</span><span class="o">,</span>
<span class="n">nat</span><span class="bp">.</span><span class="n">no_confusion</span> <span class="err">$</span> <span class="n">nat</span><span class="bp">.</span><span class="n">succ_inj</span> <span class="n">H</span>
</pre></div>

#### [ Kenny Lau (Oct 12 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135641413):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="bp">¬∃</span> <span class="n">n</span><span class="o">,</span> <span class="mi">2</span><span class="bp">*</span><span class="n">n</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">simp</span> <span class="n">only</span> <span class="o">[</span><span class="n">eq_comm</span><span class="o">]</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">dec_trivial</span>
</pre></div>

#### [ Kenny Lau (Oct 12 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135641434):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="mi">2</span><span class="bp">*</span><span class="n">n</span> <span class="bp">≠</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">n</span> <span class="n">H</span><span class="o">,</span> <span class="n">absurd</span> <span class="o">(</span><span class="n">Exists</span><span class="bp">.</span><span class="n">intro</span> <span class="n">n</span> <span class="n">H</span><span class="bp">.</span><span class="n">symm</span><span class="o">)</span> <span class="n">dec_trivial</span>
</pre></div>

#### [ Mario Carneiro (Oct 12 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135641688):
<p>I think this is a faithful rendition of your proof:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">n</span> <span class="bp">≠</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="k">begin</span>
  <span class="k">have</span> <span class="o">:</span> <span class="mi">2</span> <span class="bp">*</span> <span class="o">(</span><span class="n">n</span><span class="o">:</span><span class="n">ℝ</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">,</span> <span class="o">{</span><span class="n">simpa</span> <span class="kn">using</span> <span class="n">congr_arg</span> <span class="o">(</span><span class="n">coe</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">ℝ</span><span class="o">)</span> <span class="n">h</span><span class="o">},</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">mul_comm</span><span class="o">,</span> <span class="err">←</span> <span class="n">div_eq_iff_mul_eq</span> <span class="o">(</span><span class="n">two_ne_zero</span> <span class="o">:</span> <span class="o">(</span><span class="mi">2</span><span class="o">:</span><span class="n">ℝ</span><span class="o">)</span><span class="bp">≠</span><span class="mi">0</span><span class="o">)]</span> <span class="n">at</span> <span class="n">this</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">h0</span> <span class="o">:</span> <span class="o">((</span><span class="mi">0</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">):</span><span class="n">ℝ</span><span class="o">)</span> <span class="bp">&lt;</span> <span class="o">(</span><span class="mi">1</span> <span class="bp">/</span> <span class="mi">2</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">),</span> <span class="o">{</span><span class="n">simp</span><span class="o">,</span> <span class="n">norm_num</span><span class="o">},</span>
  <span class="k">have</span> <span class="n">h1</span> <span class="o">:</span> <span class="o">(</span><span class="mi">1</span> <span class="bp">/</span> <span class="mi">2</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">&lt;</span> <span class="o">(</span><span class="mi">1</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="o">{</span><span class="n">simp</span><span class="o">,</span> <span class="n">norm_num</span><span class="o">},</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">this</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cast_lt</span><span class="o">]</span> <span class="n">at</span> <span class="n">h0</span> <span class="n">h1</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">not_le_of_lt</span> <span class="n">h1</span> <span class="n">h0</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Oct 12 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135641697):
<div class="codehilite"><pre><span></span>```lean
</pre></div>

#### [ Kenny Lau (Oct 12 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135641719):
<p>Also, who needs the reals, we only need Q</p>

#### [ Mario Carneiro (Oct 12 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135641721):
<p>I know</p>

#### [ Mario Carneiro (Oct 12 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135641766):
<p>but if I did that then I wouldn't be "referring to R to prove things in N"</p>

#### [ Kenny Lau (Oct 12 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135641773):
<p>that's mostly a comment to him</p>

#### [ Mario Carneiro (Oct 12 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135641779):
<p>If you use Q instead the two lemmas <code>h0</code> and <code>h1</code> can be proven by <code>dec_trivial</code></p>

#### [ Mario Carneiro (Oct 12 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135641879):
<p>what's going on in your proof? I'm surprised that <code>dec_trivial</code> proves <code>¬∃ (n : ℕ), 1 = 2 * n</code></p>

#### [ Kenny Lau (Oct 12 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135641892):
<p>it's dvd in disguise :P</p>

#### [ Mario Carneiro (Oct 12 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135641963):
<p>oh whoa, didn't realize <code>dvd</code> was reducible</p>

#### [ Kenny Lau (Oct 12 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135641987):
<p>me neither</p>

#### [ Kenny Lau (Oct 12 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135641993):
<p>this is the residue of a longer proof</p>

#### [ Mario Carneiro (Oct 12 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135642023):
<p>to answer your question, yes <code>omega</code> can handle this</p>

#### [ Mario Carneiro (Oct 12 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135642032):
<p>I think <code>linarith</code> can too if you fiddle with the statement a bit</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 12 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135642101):
<blockquote>
<p>I think this is a faithful rendition of your proof:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">n</span> <span class="bp">≠</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="k">begin</span>
  <span class="k">have</span> <span class="o">:</span> <span class="mi">2</span> <span class="bp">*</span> <span class="o">(</span><span class="n">n</span><span class="o">:</span><span class="n">ℝ</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">,</span> <span class="o">{</span><span class="n">simpa</span> <span class="kn">using</span> <span class="n">congr_arg</span> <span class="o">(</span><span class="n">coe</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">ℝ</span><span class="o">)</span> <span class="n">h</span><span class="o">},</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">mul_comm</span><span class="o">,</span> <span class="err">←</span> <span class="n">div_eq_iff_mul_eq</span> <span class="o">(</span><span class="n">two_ne_zero</span> <span class="o">:</span> <span class="o">(</span><span class="mi">2</span><span class="o">:</span><span class="n">ℝ</span><span class="o">)</span><span class="bp">≠</span><span class="mi">0</span><span class="o">)]</span> <span class="n">at</span> <span class="n">this</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">h0</span> <span class="o">:</span> <span class="o">((</span><span class="mi">0</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">):</span><span class="n">ℝ</span><span class="o">)</span> <span class="bp">&lt;</span> <span class="o">(</span><span class="mi">1</span> <span class="bp">/</span> <span class="mi">2</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">),</span> <span class="o">{</span><span class="n">simp</span><span class="o">,</span> <span class="n">norm_num</span><span class="o">},</span>
  <span class="k">have</span> <span class="n">h1</span> <span class="o">:</span> <span class="o">(</span><span class="mi">1</span> <span class="bp">/</span> <span class="mi">2</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">&lt;</span> <span class="o">(</span><span class="mi">1</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">),</span> <span class="o">{</span><span class="n">simp</span><span class="o">,</span> <span class="n">norm_num</span><span class="o">},</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">this</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cast_lt</span><span class="o">]</span> <span class="n">at</span> <span class="n">h0</span> <span class="n">h1</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">not_le_of_lt</span> <span class="n">h1</span> <span class="n">h0</span>
<span class="kn">end</span>
</pre></div>


</blockquote>
<p>I'm trying to unpack that, but Lean says it fails to synthesise type class instance (I fixed one bracket).</p>

#### [ Mario Carneiro (Oct 12 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135642174):
<p>where is the error, and where did you fix a bracket?</p>

#### [ Mario Carneiro (Oct 12 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135642177):
<p>you need <code>import data.real.basic tactic.norm_num</code> in the header</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 12 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135642186):
<p>Yeah, I've done that.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 12 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135642196):
<p>Wait, I put the wrong bracket. It works now.</p>

#### [ Mario Carneiro (Oct 12 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135642317):
<p>kenny, here is a marginally less obfuscatory (and shorter!) version of your proof:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="mi">2</span><span class="bp">*</span><span class="n">n</span> <span class="bp">≠</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="o">(</span><span class="n">dec_trivial</span> <span class="o">:</span> <span class="bp">¬</span> <span class="mi">2</span> <span class="err">∣</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">⟨</span><span class="n">n</span><span class="o">,</span> <span class="n">h</span><span class="bp">.</span><span class="n">symm</span><span class="bp">⟩</span>
</pre></div>

#### [ Kenny Lau (Oct 12 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135642546):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">n</span> <span class="bp">≠</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="k">begin</span>
  <span class="k">have</span> <span class="n">h1</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">n</span> <span class="bp">∧</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">n</span> <span class="bp">&lt;</span> <span class="mi">2</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">rw</span> <span class="n">h</span><span class="o">,</span>
    <span class="n">exact</span> <span class="n">dec_trivial</span> <span class="o">},</span>
  <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="bp">@</span><span class="n">nat</span><span class="bp">.</span><span class="n">cast_lt</span> <span class="n">ℝ</span><span class="o">,</span> <span class="err">←</span> <span class="bp">@</span><span class="n">nat</span><span class="bp">.</span><span class="n">cast_lt</span> <span class="n">ℝ</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cast_mul</span><span class="o">]</span> <span class="n">at</span> <span class="n">h1</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">nat</span><span class="bp">.</span><span class="n">cast_zero</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cast_bit0</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cast_one</span><span class="o">]</span> <span class="n">at</span> <span class="n">h1</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">h2</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="o">(</span><span class="mi">2</span><span class="o">:</span><span class="n">ℝ</span><span class="o">),</span>
  <span class="o">{</span> <span class="n">exact</span> <span class="n">two_pos</span> <span class="o">},</span>
  <span class="k">have</span> <span class="n">h3</span> <span class="o">:</span> <span class="o">(</span><span class="mi">2</span><span class="o">:</span><span class="n">ℝ</span><span class="o">)</span> <span class="bp">≠</span> <span class="mi">0</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">exact</span> <span class="n">ne_of_gt</span> <span class="n">h2</span> <span class="o">},</span>
  <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">div_lt_div_right</span> <span class="n">h2</span><span class="o">,</span> <span class="n">mul_div_cancel_left</span> <span class="bp">_</span> <span class="n">h3</span><span class="o">,</span> <span class="n">and_comm</span><span class="o">]</span> <span class="n">at</span> <span class="n">h1</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">div_lt_div_right</span> <span class="n">h2</span><span class="o">,</span> <span class="n">mul_div_cancel_left</span> <span class="bp">_</span> <span class="n">h3</span><span class="o">,</span> <span class="n">and_comm</span><span class="o">]</span> <span class="n">at</span> <span class="n">h1</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">div_self</span> <span class="n">h3</span><span class="o">,</span> <span class="n">zero_div</span><span class="o">,</span> <span class="err">←</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cast_zero</span><span class="o">,</span> <span class="err">←</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cast_one</span><span class="o">]</span> <span class="n">at</span> <span class="n">h1</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">nat</span><span class="bp">.</span><span class="n">cast_lt</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cast_lt</span><span class="o">]</span> <span class="n">at</span> <span class="n">h1</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">h1</span> <span class="k">with</span> <span class="n">h4</span> <span class="n">h5</span><span class="o">,</span> <span class="n">clear</span> <span class="n">h</span> <span class="n">h2</span> <span class="n">h3</span><span class="o">,</span>
  <span class="n">revert</span> <span class="n">n</span> <span class="n">h5</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">dec_trivial</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Oct 12 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135642548):
<p>is this a more faithful rendition?</p>

#### [ Kenny Lau (Oct 12 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135642556):
<p>(sorry, can't get <code>nat.cast_div</code> to work, guess it doesn't exist)</p>

#### [ Mario Carneiro (Oct 12 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135642585):
<p>lol, of course not</p>

#### [ Mario Carneiro (Oct 12 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135642637):
<p>it's not true... I'm not even sure what the statement would be</p>

#### [ Kenny Lau (Oct 12 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135642643):
<p>cast it to a char_zero decidable_division_ring or something like that</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 12 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135642852):
<blockquote>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">n</span> <span class="bp">≠</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="k">begin</span>
  <span class="k">have</span> <span class="n">h1</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">n</span> <span class="bp">∧</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">n</span> <span class="bp">&lt;</span> <span class="mi">2</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">rw</span> <span class="n">h</span><span class="o">,</span>
    <span class="n">exact</span> <span class="n">dec_trivial</span> <span class="o">},</span>
  <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="bp">@</span><span class="n">nat</span><span class="bp">.</span><span class="n">cast_lt</span> <span class="n">ℝ</span><span class="o">,</span> <span class="err">←</span> <span class="bp">@</span><span class="n">nat</span><span class="bp">.</span><span class="n">cast_lt</span> <span class="n">ℝ</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cast_mul</span><span class="o">]</span> <span class="n">at</span> <span class="n">h1</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">nat</span><span class="bp">.</span><span class="n">cast_zero</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cast_bit0</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cast_one</span><span class="o">]</span> <span class="n">at</span> <span class="n">h1</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">h2</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="o">(</span><span class="mi">2</span><span class="o">:</span><span class="n">ℝ</span><span class="o">),</span>
  <span class="o">{</span> <span class="n">exact</span> <span class="n">two_pos</span> <span class="o">},</span>
  <span class="k">have</span> <span class="n">h3</span> <span class="o">:</span> <span class="o">(</span><span class="mi">2</span><span class="o">:</span><span class="n">ℝ</span><span class="o">)</span> <span class="bp">≠</span> <span class="mi">0</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">exact</span> <span class="n">ne_of_gt</span> <span class="n">h2</span> <span class="o">},</span>
  <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">div_lt_div_right</span> <span class="n">h2</span><span class="o">,</span> <span class="n">mul_div_cancel_left</span> <span class="bp">_</span> <span class="n">h3</span><span class="o">,</span> <span class="n">and_comm</span><span class="o">]</span> <span class="n">at</span> <span class="n">h1</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">div_lt_div_right</span> <span class="n">h2</span><span class="o">,</span> <span class="n">mul_div_cancel_left</span> <span class="bp">_</span> <span class="n">h3</span><span class="o">,</span> <span class="n">and_comm</span><span class="o">]</span> <span class="n">at</span> <span class="n">h1</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">div_self</span> <span class="n">h3</span><span class="o">,</span> <span class="n">zero_div</span><span class="o">,</span> <span class="err">←</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cast_zero</span><span class="o">,</span> <span class="err">←</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cast_one</span><span class="o">]</span> <span class="n">at</span> <span class="n">h1</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">nat</span><span class="bp">.</span><span class="n">cast_lt</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cast_lt</span><span class="o">]</span> <span class="n">at</span> <span class="n">h1</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">h1</span> <span class="k">with</span> <span class="n">h4</span> <span class="n">h5</span><span class="o">,</span> <span class="n">clear</span> <span class="n">h</span> <span class="n">h2</span> <span class="n">h3</span><span class="o">,</span>
  <span class="n">revert</span> <span class="n">n</span> <span class="n">h5</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">dec_trivial</span>
<span class="kn">end</span>
</pre></div>


</blockquote>
<p>Ok, I'm lost here -- what exactly does nat.cast do?</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 12 2018 at 01:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135642875):
<p>And what are the up-arrow signs lean gives in the feedback?</p>

#### [ Kenny Lau (Oct 12 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135642919):
<p>it's the coercion function from <code>nat</code> to <code>real</code></p>

#### [ Mario Carneiro (Oct 12 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135642924):
<p>the up arrows are <code>nat.cast</code></p>

#### [ Kenny Lau (Oct 12 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135642934):
<p><code>n</code> is a natural number and "up-arrow n" is a real number</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 12 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135642941):
<p>Ah ok.</p>

#### [ Mario Carneiro (Oct 12 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135642964):
<p>and there are theorems saying <code>↑(n + m) = ↑n + ↑m</code> and so on, that's <code>nat.cast_add</code></p>

#### [ Mario Carneiro (Oct 12 2018 at 01:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135642975):
<p>this is how you turn a whole equation from talking about naturals to talking about reals or vice versa</p>

#### [ Bryan Gin-ge Chen (Oct 12 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135643024):
<p>Coercions are discussed <a href="https://leanprover.github.io/theorem_proving_in_lean/type_classes.html#coercions-using-type-classes" target="_blank" title="https://leanprover.github.io/theorem_proving_in_lean/type_classes.html#coercions-using-type-classes">here</a> in TPiL.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 12 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135643026):
<p>And nat.cast_lt means "n &lt; m implies ↑n &lt; ↑m"?</p>

#### [ Mario Carneiro (Oct 12 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135643029):
<p>it's an iff</p>

#### [ Mario Carneiro (Oct 12 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135643037):
<p>so you can turn a nat inequality into a real inequality or vice versa</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 12 2018 at 01:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135643122):
<p>I see. And perhaps a ridiculously elementary question, but what exactly are the @ signs?  Why does nat.cast_mul not have them while the others do?</p>

#### [ Bryan Gin-ge Chen (Oct 12 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135643241):
<p><code>@function</code> means that you have to provide the implicit arguments to <code>function</code>. Implicit arguments are those that lean tries to infer and are denoted by curly braces.</p>

#### [ Bryan Gin-ge Chen (Oct 12 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135643284):
<p>See <a href="https://leanprover.github.io/theorem_proving_in_lean/dependent_type_theory.html#implicit-arguments" target="_blank" title="https://leanprover.github.io/theorem_proving_in_lean/dependent_type_theory.html#implicit-arguments">this section</a> of TPiL.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 12 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135643316):
<p>Oh ok, that makes sense. So e.g. if I was simplifying a calculational proof and had to simplify <code>1*x</code> to <code>x</code>, then I could use <code>@one_mul x</code> if <code>one_mul</code> didn't work?</p>

#### [ Kenny Lau (Oct 12 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135643320):
<p>you would need way more arguments than <code>x</code></p>

#### [ Kenny Lau (Oct 12 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135643323):
<p>it would be something like <code>@one_mul \R _ x</code></p>

#### [ Abhimanyu Pallavi Sudhir (Oct 12 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135643374):
<p>What does the underscore do?</p>

#### [ Bryan Gin-ge Chen (Oct 12 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135643378):
<p>Yeah, I forgot to say you have to provide type class arguments as well (stuff in square brackets).</p>

#### [ Bryan Gin-ge Chen (Oct 12 2018 at 01:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135643382):
<p>The underscore tells lean to try to infer that argument.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 12 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135643403):
<p>(deleted)</p>

#### [ Kenny Lau (Oct 12 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135643404):
<p>you know, there was a time when I tried to type something and decided that part of a sentence can be inferred from the previous part of the sentence, and subconsciously typed an underscore</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 12 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135643460):
<p>Oh wait, do you mean the brackets in the definitions themselves?</p>

#### [ Kenny Lau (Oct 12 2018 at 01:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135643530):
<p>if you do <code>#check @one_mul</code> then you can see all of the arguments required</p>

#### [ Mario Carneiro (Oct 12 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135643599):
<p>The reason <code>nat.cast_lt</code> got a <code>@</code> and none of the others did is because at the beginning it's not clear what we are casting <em>to</em>. <code>nat.cast</code> actually works for a whole bunch of target types not just <code>ℝ</code>. Once the up arrows are introduced they carry enough information to figure out what type we are talking about</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 12 2018 at 01:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135643748):
<p>Ok, that makes sense. I also don't understand the bit0 stuff. Doesn't bit0 just double things? Why does it matter that the thing being casted is written as twice of something?</p>

#### [ Kenny Lau (Oct 12 2018 at 01:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135643868):
<p><code>2</code> is just a notation. it really means <code>bit0 1</code></p>

#### [ Kenny Lau (Oct 12 2018 at 01:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135643870):
<p>try <code>set_option pp.notations false</code></p>

#### [ Abhimanyu Pallavi Sudhir (Oct 12 2018 at 01:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135643955):
<p>Yeah I get that, but if we were dealing with 1000 instead of 2, do we need to write a series of bit1's and bit0's there? What if we were dealing with a general natural number instead of 2?</p>

#### [ Kenny Lau (Oct 12 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135644009):
<p><code>simp</code> will deal with it for you, I just don't really like using <code>simp</code></p>

#### [ Kenny Lau (Oct 12 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135644013):
<p>change that to, I just really don't like using <code>simp</code></p>

#### [ Abhimanyu Pallavi Sudhir (Oct 12 2018 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135644108):
<p>You mean just "simp at h1"? Ok, yeah, that works.</p>

#### [ Mario Carneiro (Oct 12 2018 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135644112):
<p>If we are dealing with a general natural number it is easier because it is just <code>\u n</code></p>

#### [ Mario Carneiro (Oct 12 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135644164):
<p>The problem with <code>\u 1000</code> vs <code>1000</code> is that the terms are completely different (the type of the expression is stored in all the subterms), and so we have to rewrite all the way through the term</p>

#### [ Mario Carneiro (Oct 12 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135644249):
<div class="codehilite"><pre><span></span>set_option pp.all true
#check (1000:ℤ)
-- @bit0.{0} int int.has_add
--   (@bit0.{0} int int.has_add
--      (@bit0.{0} int int.has_add
--         (@bit1.{0} int int.has_one int.has_add
--            (@bit0.{0} int int.has_add
--               (@bit1.{0} int int.has_one int.has_add
--                  (@bit1.{0} int int.has_one int.has_add
--                     (@bit1.{0} int int.has_one int.has_add
--                        (@bit1.{0} int int.has_one int.has_add (@has_one.one.{0} int int.has_one))))))))) :
--   int
#check ((1000:ℕ):ℤ)
-- @coe.{1 1} nat int (@coe_to_lift.{1 1} nat int (@coe_base.{1 1} nat int int.has_coe))
--   (@bit0.{0} nat nat.has_add
--      (@bit0.{0} nat nat.has_add
--         (@bit0.{0} nat nat.has_add
--            (@bit1.{0} nat nat.has_one nat.has_add
--               (@bit0.{0} nat nat.has_add
--                  (@bit1.{0} nat nat.has_one nat.has_add
--                     (@bit1.{0} nat nat.has_one nat.has_add
--                        (@bit1.{0} nat nat.has_one nat.has_add
--                           (@bit1.{0} nat nat.has_one nat.has_add (@has_one.one.{0} nat nat.has_one)))))))))) :
--   int
</pre></div>

#### [ Kenny Lau (Oct 12 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135644569):
<p>The thing is, <code>simp</code> is somewhat expensive, although not as expensive as <code>norm_num</code></p>

#### [ Mario Carneiro (Oct 12 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135644581):
<p>is <code>norm_num</code> actually more expensive?</p>

#### [ Kenny Lau (Oct 12 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135644592):
<p>oops, I was thinking about <code>ring</code></p>

#### [ Kenny Lau (Oct 12 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135644600):
<p>I was typing one thing and thinking about another thing</p>

#### [ Kenny Lau (Oct 12 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135644649):
<p>Anyway, I've been replacing <code>simp</code> with less expensive tactics from files in mathlib</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 12 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135644868):
<p>Ok, I managed to work through and understand the proofs (at least the two longer ones -- will be a while before I can understand Kenny's two-line proofs). Thanks a lot! (that was my missing little lemma in proving p even if p^2 even).</p>

#### [ Mario Carneiro (Oct 12 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135644917):
<p>the two line proofs are easy: your theorem is by definition the same as "2 does not divide 1" and this is decidable (there is an instance in mathlib for it)</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 12 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135644920):
<p>Why does expense/efficiency matter? You only need to run it once anyway.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 12 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135644924):
<blockquote>
<p>the two line proofs are easy: your theorem is by definition the same as "2 does not divide 1" and this is decidable (there is an instance in mathlib for it)</p>
</blockquote>
<p>Oh, ok. I just couldn't see through the notation.</p>

#### [ Mario Carneiro (Oct 12 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135644945):
<p>It doesn't matter too much, but once you start building up a huge library of maths the costs add up, and everyone who downloads mathlib will need to compile it, and mathlib itself changes on a daily basis and needs to be recompiled</p>

#### [ Mario Carneiro (Oct 12 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135644985):
<p>so it's not really a one time cost unless you view mathlib as fixed</p>

#### [ Mario Carneiro (Oct 12 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135645000):
<p>Most users can do so, but I can't since I'm a maintainer and neither can many contributors that jump between branches of mathlib</p>

#### [ Kevin Buzzard (Oct 12 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135658125):
<p><span class="user-mention" data-user-id="130500">@Abhimanyu Pallavi Sudhir</span> just to let you know that theorems like this (real 1/2 not the image of an integer), which are needed to do my problem sheets but which I would not expect a general undergraduate with 1 week's Lean experience to be able to do, are actually part of a small library I am writing which enables a generic UG to solve the problem sheet questions. See here <a href="https://github.com/ImperialCollegeLondon/M1F_example_sheets/tree/master/src/xenalib" target="_blank" title="https://github.com/ImperialCollegeLondon/M1F_example_sheets/tree/master/src/xenalib">https://github.com/ImperialCollegeLondon/M1F_example_sheets/tree/master/src/xenalib</a> and in particular note the file called <code>real_half_not_an_integer.lean</code>. I am trying to do these messy parts for the students so they can just use them instead of running into walls.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 12 2018 at 08:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135658275):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span>  Oh ok -- I wasn't really doing this for a problem sheet, though.</p>

#### [ Patrick Massot (Oct 12 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135658544):
<p>Kevin, why do you keep up arrows in statement? Is it meant to clarify the statement for human readers?</p>

#### [ Kevin Buzzard (Oct 12 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135685726):
<p><span class="user-mention" data-user-id="130500">@Abhimanyu Pallavi Sudhir</span> -- ha! I assumed you were working on Q7! <span class="user-mention" data-user-id="110031">@Patrick Massot</span> you mean things like <code>¬ ∃ n : ℤ, (1/2 : ℚ) = ↑n</code>? I guess so! I think the fact that Z is not a subset of Q is quite confusing for beginners. Maybe the arrow means "note: something a bit funny is going on here."</p>

#### [ Patrick Massot (Oct 12 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135687841):
<p>Yes, I meant that line. Lean wouldn't care if you wrote it without that up arrow</p>

#### [ Kevin Buzzard (Oct 12 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135691331):
<p>Right (although you'd see the arrow in the goal ;-) ).</p>

#### [ Patrick Massot (Oct 12 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135694355):
<p>You don't have to: <code>set_option pp.coercions false</code> <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Abhimanyu Pallavi Sudhir (Oct 12 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135701610):
<p>I managed to prove the statement in a "morally similar" way but without casting to R (or Q) -- it ends up being kinda long, see <code>theorem one_not_even</code> at <a href="https://github.com/abhimanyupallavisudhir/lean/blob/master/num_theo_theorems.lean" target="_blank" title="https://github.com/abhimanyupallavisudhir/lean/blob/master/num_theo_theorems.lean">https://github.com/abhimanyupallavisudhir/lean/blob/master/num_theo_theorems.lean</a></p>

#### [ Kenny Lau (Oct 12 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135701630):
<p><code>de_morgan</code> is <code>not_exists</code></p>

#### [ Kenny Lau (Oct 12 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135701678):
<p>all your <code>by norm_num</code> is <code>rfl</code></p>

#### [ Kevin Buzzard (Oct 12 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135702112):
<p>We don't teach the first years complicated tactics like rfl</p>

#### [ Kevin Buzzard (Oct 12 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135702117):
<p>we stick to the simple ones like norm_num</p>

#### [ Kevin Buzzard (Oct 12 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135702166):
<p>they're a darn sight easier to learn</p>

#### [ Simon Hudon (Oct 12 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135703007):
<p><code>rfl</code> is not necessarily faster than <code>norm_num</code>. The main idea of <code>norm_num</code> is actually to do things faster than than <code>rfl</code> and I think it worked out pretty well.</p>

#### [ Kenny Lau (Oct 12 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/refer%20to%20R%20to%20prove%20things%20in%20N%3F/near/135703077):
<p>fair enough</p>


{% endraw %}
