---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/24947Unexpectederrors.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Unexpected errors](https://leanprover-community.github.io/archive/113488general/24947Unexpectederrors.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Chris Hughes (May 27 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20errors/near/127171623):
<p>Just finished proving this theorem about roots of polynomials, but I'm getting the following errors and I don't understand why</p>
<div class="codehilite"><pre><span></span>unexpected occurrence of recursive function
univariate_poly.lean:574:18: warning
definition &#39;roots_aux&#39; was incorrectly marked as noncomputable
</pre></div>


<p>It clearly should be marked as noncomputable, and I have no idea what `unexpected occurence of recursive function means</p>
<div class="codehilite"><pre><span></span><span class="n">noncomputable</span> <span class="n">def</span> <span class="n">roots_aux</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="n">polynomial</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">hp</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">≠</span> <span class="mi">0</span><span class="o">),</span>
  <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span> <span class="bp">//</span> <span class="n">s</span><span class="bp">.</span><span class="n">card</span> <span class="bp">≤</span> <span class="n">degree</span> <span class="n">p</span> <span class="bp">∧</span> <span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">root</span> <span class="n">p</span> <span class="n">x</span> <span class="bp">↔</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">s</span><span class="o">}</span>
<span class="bp">|</span> <span class="n">p</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">hp</span><span class="o">,</span> <span class="bp">@</span><span class="n">dite</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">x</span><span class="o">,</span> <span class="n">root</span> <span class="n">p</span> <span class="n">x</span><span class="o">)</span> <span class="o">(</span><span class="n">classical</span><span class="bp">.</span><span class="n">prop_decidable</span> <span class="bp">_</span><span class="o">)</span>
  <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span> <span class="bp">//</span> <span class="n">s</span><span class="bp">.</span><span class="n">card</span> <span class="bp">≤</span> <span class="n">degree</span> <span class="n">p</span> <span class="bp">∧</span> <span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">root</span> <span class="n">p</span> <span class="n">x</span> <span class="bp">↔</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">s</span><span class="o">}</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="k">let</span> <span class="bp">⟨</span><span class="n">x</span><span class="o">,</span> <span class="n">hx</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">classical</span><span class="bp">.</span><span class="n">indefinite_description</span> <span class="bp">_</span> <span class="n">h</span> <span class="k">in</span>
  <span class="k">have</span> <span class="n">hpd</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">degree</span> <span class="n">p</span> <span class="o">:=</span> <span class="n">nat</span><span class="bp">.</span><span class="n">pos_of_ne_zero</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="k">begin</span>
      <span class="n">rw</span> <span class="o">[</span><span class="n">eq_C_of_degree_eq_zero</span> <span class="n">h</span><span class="o">,</span> <span class="n">root</span><span class="o">,</span> <span class="n">eval_C</span><span class="o">]</span> <span class="n">at</span> <span class="n">hx</span><span class="o">,</span>
      <span class="k">have</span> <span class="n">h1</span> <span class="o">:</span> <span class="n">p</span> <span class="o">(</span><span class="n">degree</span> <span class="n">p</span><span class="o">)</span> <span class="bp">≠</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">leading_coeff_ne_zero</span> <span class="n">hp</span><span class="o">,</span>
      <span class="n">rw</span> <span class="n">h</span> <span class="n">at</span> <span class="n">h1</span><span class="o">,</span>
      <span class="n">contradiction</span><span class="o">,</span>
    <span class="kn">end</span><span class="o">),</span>
  <span class="k">have</span> <span class="n">hd0</span> <span class="o">:</span> <span class="n">div_by_monic</span> <span class="n">p</span> <span class="o">(</span><span class="n">monic_X_sub_C</span> <span class="n">x</span><span class="o">)</span> <span class="bp">≠</span> <span class="mi">0</span> <span class="o">:=</span>
    <span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="k">by</span> <span class="k">have</span> <span class="o">:=</span> <span class="n">mul_div_eq_iff_root</span><span class="bp">.</span><span class="mi">2</span> <span class="n">hx</span><span class="bp">;</span>
      <span class="n">simp</span> <span class="bp">*</span> <span class="n">at</span> <span class="bp">*</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">wf</span> <span class="o">:</span> <span class="n">degree</span> <span class="o">(</span><span class="n">div_by_monic</span> <span class="n">p</span> <span class="bp">_</span><span class="o">)</span> <span class="bp">&lt;</span> <span class="n">degree</span> <span class="n">p</span> <span class="o">:=</span>
    <span class="n">degree_div_by_monic_lt</span> <span class="bp">_</span> <span class="o">(</span><span class="n">monic_X_sub_C</span> <span class="n">x</span><span class="o">)</span>
    <span class="o">((</span><span class="n">degree_X_sub_C</span> <span class="n">x</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span> <span class="bp">▸</span> <span class="n">nat</span><span class="bp">.</span><span class="n">succ_pos</span> <span class="bp">_</span><span class="o">)</span> <span class="n">hpd</span><span class="o">,</span>
  <span class="k">let</span> <span class="bp">⟨</span><span class="n">t</span><span class="o">,</span> <span class="n">htd</span><span class="o">,</span> <span class="n">htr</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">roots_aux</span> <span class="o">(</span><span class="n">div_by_monic</span> <span class="n">p</span> <span class="o">(</span><span class="n">monic_X_sub_C</span> <span class="n">x</span><span class="o">))</span> <span class="n">hd0</span> <span class="k">in</span>
  <span class="bp">⟨</span><span class="n">insert</span> <span class="n">x</span> <span class="n">t</span><span class="o">,</span> <span class="k">calc</span> <span class="o">(</span><span class="n">insert</span> <span class="n">x</span> <span class="n">t</span><span class="o">)</span><span class="bp">.</span><span class="n">card</span> <span class="bp">≤</span> <span class="n">t</span><span class="bp">.</span><span class="n">card</span> <span class="bp">+</span> <span class="mi">1</span> <span class="o">:</span> <span class="n">finset</span><span class="bp">.</span><span class="n">card_insert_le</span> <span class="bp">_</span> <span class="bp">_</span>
    <span class="bp">...</span> <span class="bp">≤</span> <span class="n">degree</span> <span class="o">(</span><span class="n">div_by_monic</span> <span class="n">p</span> <span class="o">(</span><span class="n">monic_X_sub_C</span> <span class="n">x</span><span class="o">))</span> <span class="bp">+</span> <span class="mi">1</span> <span class="o">:</span> <span class="n">nat</span><span class="bp">.</span><span class="n">succ_le_succ</span> <span class="n">htd</span>
    <span class="bp">...</span> <span class="bp">≤</span> <span class="bp">_</span> <span class="o">:</span> <span class="n">nat</span><span class="bp">.</span><span class="n">succ_le_of_lt</span> <span class="n">wf</span><span class="o">,</span>
  <span class="k">begin</span>
    <span class="k">assume</span> <span class="n">y</span><span class="o">,</span>
    <span class="n">rw</span> <span class="o">[</span><span class="n">mem_insert</span><span class="o">,</span> <span class="err">←</span> <span class="n">htr</span><span class="o">,</span> <span class="n">eq_comm</span><span class="o">,</span> <span class="err">←</span> <span class="n">root_X_sub_C</span><span class="o">],</span>
    <span class="n">conv</span> <span class="o">{</span><span class="n">to_lhs</span><span class="o">,</span> <span class="n">rw</span> <span class="err">←</span> <span class="n">mul_div_eq_iff_root</span><span class="bp">.</span><span class="mi">2</span> <span class="n">hx</span><span class="o">},</span>
    <span class="n">exact</span> <span class="bp">⟨</span><span class="n">root_or_root_of_root_mul</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">or</span><span class="bp">.</span><span class="n">cases_on</span> <span class="n">h</span> <span class="o">(</span><span class="n">root_mul_right_of_root</span> <span class="bp">_</span><span class="o">)</span> <span class="o">(</span><span class="n">root_mul_left_of_root</span> <span class="bp">_</span><span class="o">)</span><span class="bp">⟩</span>
  <span class="kn">end</span><span class="bp">⟩</span><span class="o">)</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="bp">⟨</span><span class="err">∅</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">zero_le</span> <span class="bp">_</span><span class="o">,</span> <span class="k">by</span> <span class="n">finish</span><span class="bp">⟩</span><span class="o">)</span>
<span class="n">using_well_founded</span> <span class="o">{</span><span class="n">rel_tac</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="bp">`</span><span class="o">[</span><span class="n">exact</span> <span class="bp">⟨_</span><span class="o">,</span> <span class="n">measure_wf</span> <span class="n">degree</span><span class="bp">⟩</span><span class="o">]}</span>
</pre></div>


<p>The full file is here <a href="https://github.com/dorhinj/leanstuff/blob/master/univariate_poly.lean" target="_blank" title="https://github.com/dorhinj/leanstuff/blob/master/univariate_poly.lean">https://github.com/dorhinj/leanstuff/blob/master/univariate_poly.lean</a></p>

#### [ Kenny Lau (May 27 2018 at 19:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20errors/near/127171663):
<p>it happens with equation compilers</p>

#### [ Kenny Lau (May 27 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20errors/near/127171666):
<p>since they provide you with the theorem you're trying to prove, in case you want to do recursion</p>

#### [ Kenny Lau (May 27 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20errors/near/127171669):
<p>but some tactics touch every local hypothesis</p>

#### [ Kenny Lau (May 27 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20errors/near/127171714):
<p>Suspects I spot: <code>contradiction</code>, <code>simp * at *</code></p>

#### [ Kenny Lau (May 27 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20errors/near/127171715):
<p>the latter has a higher chance of being the perpetrator</p>

#### [ Chris Hughes (May 27 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20errors/near/127171716):
<p>I don't think it's that or it would have asked me to prove something. I replaced both of those with <code>admit</code> and I still get the error.</p>

#### [ Kenny Lau (May 27 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20errors/near/127171808):
<p>how did you define <code>polynomial</code>?</p>

#### [ Kenny Lau (May 27 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20errors/near/127171809):
<p>can you prove strong induction?</p>

#### [ Chris Hughes (May 27 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20errors/near/127172447):
<p>polynomial is <code>ℕ →₀ α</code>. I have proved and defined stuff in this manner before. I have just rewritten this function using <code>well_founded.fix</code>, and it works, but it would be nice to know what's going on.</p>

#### [ Kenny Lau (May 27 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20errors/near/127172498):
<div class="message_inline_image"><a href="https://i.imgflip.com/2b3qrs.jpg" target="_blank" title="https://i.imgflip.com/2b3qrs.jpg"><img src="https://i.imgflip.com/2b3qrs.jpg"></a></div>

#### [ Mario Carneiro (May 27 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20errors/near/127172737):
<p>noooo lean memes</p>

#### [ Andrew Ashworth (May 27 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20errors/near/127172770):
<p>I wouldn't feel bad about directly using <code>well_founded.fix</code>... the using_well_founded tactic is undocumented and hard to debug unless you know what's going on behind the scenes</p>

#### [ Mario Carneiro (May 27 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20errors/near/127172776):
<p>I don't think this should be a problematic definition, but I can't run it as is</p>

#### [ Andrew Ashworth (May 27 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20errors/near/127172824):
<p>(but maybe I'm just bad at Lean)</p>

#### [ Mario Carneiro (May 27 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20errors/near/127172828):
<p>(it's not actually a tactic, it's a keyword)</p>

#### [ Andrew Ashworth (May 27 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20errors/near/127172883):
<p>(shows how much I've used it... I needed wf recursion a few months ago and struggled with <code>well_founded.fix</code>, and since it worked, never bothered to figure out <code>using_well_founded</code>)</p>

#### [ Mario Carneiro (May 27 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20errors/near/127172932):
<p>the offending tactic is <code>by finish</code> at the end</p>

#### [ Kenny Lau (May 27 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20errors/near/127172933):
<p>I must be blind</p>

#### [ Mario Carneiro (May 27 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20errors/near/127172938):
<p>use <code>by clear roots_aux; finish</code> instead</p>

#### [ Mario Carneiro (May 27 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unexpected%20errors/near/127172981):
<p>I found it by just replacing things by <code>sorry</code> until the error went away</p>


{% endraw %}
