---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/88074castwoes.html
---

## Stream: [general](index.html)
### Topic: [cast woes](88074castwoes.html)

---


{% raw %}
#### [ Kevin Buzzard (May 25 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127073963):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">int</span><span class="bp">.</span><span class="n">basic</span> <span class="n">data</span><span class="bp">.</span><span class="n">nat</span><span class="bp">.</span><span class="n">cast</span>

<span class="bp">#</span><span class="kn">check</span> <span class="n">int</span><span class="bp">.</span><span class="n">mod_add_mod</span> <span class="c1">-- ∀ (m n k : ℤ), (m % n + k) % n = (m + k) % n</span>
<span class="c1">-- #check nat.mod_add_mod -- unknown identifier</span>
<span class="c1">-- so let&#39;s create it</span>

<span class="c1">-- note:</span>
<span class="bp">#</span><span class="kn">check</span> <span class="n">int</span><span class="bp">.</span><span class="n">of_nat_mod</span> <span class="c1">-- ∀ (m n : ℕ), ↑m % ↑n = int.of_nat (m % n)</span>

<span class="kn">theorem</span> <span class="n">nat</span><span class="bp">.</span><span class="n">mod_add_mod</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span> <span class="n">k</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="o">(</span><span class="n">m</span> <span class="err">%</span> <span class="n">n</span> <span class="bp">+</span> <span class="n">k</span><span class="o">)</span> <span class="err">%</span> <span class="n">n</span> <span class="bp">=</span> <span class="o">(</span><span class="n">m</span> <span class="bp">+</span> <span class="n">k</span><span class="o">)</span> <span class="err">%</span> <span class="n">n</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">intros</span> <span class="n">m</span> <span class="n">n</span> <span class="n">k</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">int</span><span class="bp">.</span><span class="n">of_nat_inj</span><span class="o">,</span>
  <span class="n">rw</span> <span class="err">←</span><span class="n">int</span><span class="bp">.</span><span class="n">of_nat_mod</span><span class="o">,</span>
  <span class="n">rw</span> <span class="err">←</span><span class="n">int</span><span class="bp">.</span><span class="n">of_nat_mod</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cast_add</span> <span class="c1">-- fails</span>
  <span class="c">/-</span><span class="cm"></span>
<span class="cm">  rewrite tactic failed, did not find instance of the pattern in the target expression</span>
<span class="cm">  ↑(?m_4 + ?m_5)</span>
<span class="cm">state:</span>
<span class="cm">m n k : ℕ</span>
<span class="cm">⊢ ↑(m % n + k) % ↑n = ↑(m + k) % ↑n</span>
<span class="cm">  -/</span>
  <span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (May 25 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127073966):
<p>What am I doing wrong?</p>

#### [ Kevin Buzzard (May 25 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127073972):
<p>I found a "hole" in mathlib -- but am failing to fix it.</p>

#### [ Kevin Buzzard (May 25 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127074019):
<p>I tried to be really precise:</p>

#### [ Kevin Buzzard (May 25 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127074021):
<div class="codehilite"><pre><span></span><span class="k">have</span> <span class="n">H1</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">nat</span><span class="bp">.</span><span class="n">cast_add</span> <span class="bp">ℤ</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="n">m</span> <span class="err">%</span> <span class="n">n</span><span class="o">)</span> <span class="n">k</span><span class="o">,</span>
  <span class="c">/-</span><span class="cm"></span>
<span class="cm">  H1 : ↑(m % n + k) = ↑(m % n) + ↑k</span>
<span class="cm">  ⊢ ↑(m % n + k) % ↑n = ↑(m + k) % ↑n</span>
<span class="cm">  -/</span>

  <span class="c1">-- rw H1, -- fails</span>
  <span class="c">/-</span><span class="cm"></span>
<span class="cm">  rewrite tactic failed, did not find instance of the pattern in the target expression</span>
<span class="cm">  ↑(m % n + k)</span>
<span class="cm">state:</span>
<span class="cm">m n k : ℕ,</span>
<span class="cm">H1 : ↑(m % n + k) = ↑(m % n) + ↑k</span>
<span class="cm">⊢ ↑(m % n + k) % ↑n = ↑(m + k) % ↑n</span>
<span class="cm">  -/</span>
</pre></div>

#### [ Kevin Buzzard (May 25 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127074028):
<p>I switched notation off and the rewrite still looked like it should work</p>

#### [ Kevin Buzzard (May 25 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127074031):
<p>I switched pp.all off and got swamped.</p>

#### [ Chris Hughes (May 25 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127074035):
<p><code>int.coe_nat_add</code> is the correct lemma, rather than <code>nat.cast_add</code> I think</p>

#### [ Kevin Buzzard (May 25 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127074043):
<p>You're right Chris.</p>

#### [ Kevin Buzzard (May 25 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127074045):
<p>Do you know why what I tried is failing?</p>

#### [ Chris Hughes (May 25 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127074121):
<p>Because <code>cast</code> is a coercion into a general ring, whereas there's a seperately defined coercion from<code>nat</code> to <code>int</code>, probably because it's in core, but cast is is in mathlib</p>

#### [ Chris Hughes (May 25 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127074193):
<p>Also, <code>of_nat</code> is a more natural function to use as the coercion than <code>cast</code> which just does 1 + 1 + 1 ...</p>

#### [ Mario Carneiro (May 25 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127074721):
<p>You can probably use <code>nat.modeq</code> to prove this one, there are more modeq theorems than there are theorems about mod</p>

#### [ Kevin Buzzard (May 26 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122090):
<blockquote>
<p>You can probably use <code>nat.modeq</code> to prove this one, there are more modeq theorems than there are theorems about mod</p>
</blockquote>
<p>My eyes are opened!</p>

#### [ Kevin Buzzard (May 26 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122131):
<p>I had somehow ruled out this MOD stuff as "another way of setting up the theory, which I didn't use".</p>

#### [ Kevin Buzzard (May 26 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122133):
<p>I've always thought that MOD notation was horrible, by the way.</p>

#### [ Kevin Buzzard (May 26 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122177):
<p>pmod is standard LaTeX notation</p>

#### [ Mario Carneiro (May 26 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122216):
<p>there were technical reasons I couldn't use parens and lowercase</p>

#### [ Kevin Buzzard (May 26 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122217):
<p>I think using LaTeX as a guide is a good idea. I'm really familiar with LaTeX notation and it still occasionally confuses me that <code>\equiv</code> is not <code>equiv</code></p>

#### [ Kevin Buzzard (May 26 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122218):
<p>Oh --</p>

#### [ Kevin Buzzard (May 26 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122219):
<p>this was forced upon you somehow?</p>

#### [ Kevin Buzzard (May 26 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122220):
<p>I had no idea! I just thought it was a wacky design decision</p>

#### [ Kevin Buzzard (May 26 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122223):
<p>the MOD stuff</p>

#### [ Mario Carneiro (May 26 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122226):
<p>I'm not even sure the notation is worth it</p>

#### [ Kevin Buzzard (May 26 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122227):
<p>This wasn't the fault of some labour-saving tactic was it?</p>

#### [ Kevin Buzzard (May 26 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122264):
<p>The notation is what mathematicians want</p>

#### [ Mario Carneiro (May 26 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122267):
<p>it's a parsing thing</p>

#### [ Kevin Buzzard (May 26 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122268):
<p>We are sticklers for notation</p>

#### [ Kevin Buzzard (May 26 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122269):
<p>That's why I mentioned it -- it looks funny to mathematicians because there is already standard notation</p>

#### [ Mario Carneiro (May 26 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122310):
<p>It's probably better than no notation, but even as it is it's a bit problematic</p>

#### [ Kevin Buzzard (May 26 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122315):
<p>it enables you to write uncluttered calc proofs</p>

#### [ Kevin Buzzard (May 26 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122316):
<p>so it's definitely better than no notation</p>

#### [ Kevin Buzzard (May 26 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122317):
<p>but it still looks funny</p>

#### [ Kevin Buzzard (May 26 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122318):
<p>To be honest I've never used it -- I assume it can be used in calc proofs</p>

#### [ Kevin Buzzard (May 26 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122319):
<p>I'm giving a talk on this stuff in about 10 hours</p>

#### [ Mario Carneiro (May 26 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122324):
<p>I never tried it, but I think chris did</p>

#### [ Kevin Buzzard (May 26 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122325):
<p>Maybe it's about time I learnt how it worked.</p>

#### [ Kevin Buzzard (May 26 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122327):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> how did you learn that funny <code>MOD</code> stuff?</p>

#### [ Chris Hughes (May 26 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/127122380):
<p>What funny MOD stuff?</p>

#### [ Kevin Buzzard (Jan 23 2019 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/156678741):
<p>I have generally got the hang of how to handle casts now. The point of view which I want to push amongst the UGs is that even though yes it's annoying that natural numbers aren't actually real numbers, <code>simp</code> should do all the translating for you. But here's an example where I couldn't make it work:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">M</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">M</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">&lt;</span> <span class="n">M</span> <span class="bp">+</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">H</span><span class="o">],</span>
  <span class="c1">-- ⊢ 0 &lt; 1 + ↑M</span>
  <span class="c1">-- gaargh</span>
  <span class="c1">-- simp at H, -- won&#39;t change it to 0 &lt; 1 + M</span>
  <span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>


<p>Applying <code>simp</code> to nat <code>M + 1</code> doesn't change it, but applying <code>simp</code> to real <code>M + 1</code> changes it to <code>1 + M</code> and this somehow means Lean loses track.</p>

#### [ Kevin Buzzard (Jan 23 2019 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/156678755):
<p>I know I can use some cast_lt or whatever, but this is exactly what I am trying to avoid. <code>simp</code> is usually good at these.</p>

#### [ Andrew Ashworth (Jan 23 2019 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/156694974):
<p>(deleted)</p>

#### [ Simon Hudon (Jan 24 2019 at 00:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cast%20woes/near/156736166):
<p>I recommend finding the <code>simp</code> lemma responsible for this (probably something like <code>real.add_comm</code>) and declare in your file <code>local attribute [-simp] real.add_comm</code></p>


{% endraw %}
