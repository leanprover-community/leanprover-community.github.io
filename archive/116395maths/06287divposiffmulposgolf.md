---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/06287divposiffmulposgolf.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [div_pos_iff_mul_pos golf](https://leanprover-community.github.io/archive/116395maths/06287divposiffmulposgolf.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Nov 14 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147700596):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">real</span>

<span class="kn">lemma</span> <span class="n">div_pos_iff_mul_pos</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">Hy</span> <span class="o">:</span> <span class="n">y</span> <span class="bp">≠</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">x</span> <span class="bp">*</span> <span class="n">y</span> <span class="bp">↔</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">x</span> <span class="bp">/</span> <span class="n">y</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">have</span> <span class="n">H</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">y</span> <span class="bp">*</span> <span class="n">y</span> <span class="o">:=</span> <span class="n">mul_self_pos</span> <span class="n">Hy</span><span class="o">,</span>
  <span class="n">split</span><span class="o">,</span>
    <span class="n">intro</span> <span class="n">H1</span><span class="o">,</span>
    <span class="k">have</span> <span class="n">H2</span> <span class="o">:</span> <span class="o">(</span><span class="n">x</span> <span class="bp">*</span> <span class="n">y</span><span class="o">)</span> <span class="bp">/</span> <span class="o">(</span><span class="n">y</span> <span class="bp">*</span> <span class="n">y</span><span class="o">)</span> <span class="bp">=</span> <span class="n">x</span> <span class="bp">/</span> <span class="n">y</span><span class="o">,</span>
      <span class="n">rw</span> <span class="n">div_eq_div_iff</span> <span class="o">(</span><span class="n">ne_of_gt</span> <span class="n">H</span><span class="o">)</span> <span class="n">Hy</span><span class="o">,</span>
      <span class="n">rw</span> <span class="n">mul_assoc</span><span class="o">,</span>
    <span class="n">rw</span> <span class="err">←</span><span class="n">H2</span><span class="o">,</span>
    <span class="n">apply</span> <span class="n">div_pos</span> <span class="n">H1</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">intro</span> <span class="n">H1</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">H2</span> <span class="o">:</span> <span class="o">(</span><span class="n">x</span> <span class="bp">/</span> <span class="n">y</span><span class="o">)</span> <span class="bp">*</span> <span class="o">(</span><span class="n">y</span> <span class="bp">*</span> <span class="n">y</span><span class="o">)</span> <span class="bp">=</span> <span class="n">x</span> <span class="bp">*</span> <span class="n">y</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">div_mul_eq_mul_div_comm</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">mul_div_cancel</span> <span class="bp">_</span> <span class="n">Hy</span><span class="o">,</span>
  <span class="n">rw</span> <span class="err">←</span><span class="n">H2</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">mul_pos</span> <span class="n">H1</span> <span class="n">H</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p>I was surprised this wasn't already in, for preordered semimonoids with bot or whatever</p>

#### [ Mario Carneiro (Nov 14 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147700710):
<p>I'm not, that's a weird theorem</p>

#### [ Kevin Buzzard (Nov 14 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147700874):
<p>what about <code>0 &lt; x * y iff (x &lt; 0 and y &lt; 0) or (x &gt; 0 and y &gt; 0)</code>?</p>

#### [ Kevin Buzzard (Nov 14 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147700885):
<p>and similarly for <code>0 &lt; x / y</code></p>

#### [ Kenny Lau (Nov 14 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147700919):
<p><code>pos_and_pos_or_neg_and_neg_of_mul_pos</code>?</p>

#### [ Kevin Buzzard (Nov 14 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147700945):
<p>Oh, you found it?</p>

#### [ Kenny Lau (Nov 14 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147701006):
<p>I found x*y&gt;0 implies x,y&gt;0 or x,y&lt;0</p>

#### [ Mario Carneiro (Nov 14 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147701014):
<p>I guess the best decomposition of it is something like</p>
<div class="codehilite"><pre><span></span>0 &lt; x * y
    ↔ (0 &lt; x ∧ 0 &lt; y ∨ x &lt; 0 ∧ y &lt; 0)
... ↔ (0 &lt; x ∧ 0 &lt; y⁻¹ ∨ x &lt; 0 ∧ y⁻¹ &lt; 0)
... ↔ 0 &lt; x * y⁻¹
... ↔ 0 &lt; x / y
</pre></div>

#### [ Kevin Buzzard (Nov 14 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147701017):
<p>ha ha it's in core</p>

#### [ Kevin Buzzard (Nov 14 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147701044):
<p>I think you should use <code>pos_and_pos_or_neg_and_neg_of_mul_pos</code></p>

#### [ Kevin Buzzard (Nov 14 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147701046):
<p>just for the name</p>

#### [ Mario Carneiro (Nov 14 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147701071):
<p>whenever the name gets that long my eyes cross trying to read it</p>

#### [ Kevin Buzzard (Nov 14 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147701091):
<p>we should think of a more rigorous encrypted way to name lemmas</p>

#### [ Kevin Buzzard (Nov 14 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147701096):
<p>to keep them shorter</p>

#### [ Mario Carneiro (Nov 14 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147701110):
<p>have you seen metamath naming conventions? :D</p>

#### [ Mario Carneiro (Nov 14 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147701173):
<p>it would probably be called <code>mulanor</code> or the like</p>

#### [ Reid Barton (Nov 14 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147701204):
<p>that's a cool name</p>

#### [ Kevin Buzzard (Nov 14 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147701205):
<p>the md5sum of <code>pos_and_pos_or_neg_and_neg_of_mul_pos</code> is shorter, maybe we should use that</p>

#### [ Mario Carneiro (Nov 14 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147701225):
<p>lol that's a bad sign</p>

#### [ Mario Carneiro (Nov 14 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147701257):
<p>probably gzip can do better</p>

#### [ Kevin Buzzard (Nov 14 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147702518):
<blockquote>
<p>I'm not, that's a weird theorem</p>
</blockquote>
<p>How would you do</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">Q4</span> <span class="o">:</span> <span class="o">{</span> <span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">|</span> <span class="n">x</span> <span class="bp">≠</span> <span class="mi">0</span> <span class="bp">∧</span> <span class="mi">3</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">/</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="mi">4</span> <span class="o">}</span> <span class="bp">=</span>
  <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">|</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="mi">0</span> <span class="bp">∨</span> <span class="o">((</span><span class="mi">1</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">/</span> <span class="mi">3</span> <span class="bp">&lt;</span> <span class="n">x</span> <span class="bp">∧</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="mi">1</span><span class="o">)}</span> <span class="o">:=</span>
</pre></div>


<p>? I used this along the way to clear denominators but it was still an annoying case bash</p>

#### [ Kenny Lau (Nov 14 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147702583):
<p>oh god</p>

#### [ Kevin Buzzard (Nov 14 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147702659):
<p>yes it's M1F sheet 3</p>

#### [ Kevin Buzzard (Nov 14 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147702670):
<p>you should have seen my proof last year!</p>

#### [ Kevin Buzzard (Nov 14 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147702771):
<p>It took me 25 lines to get to <code>⊢ 0 &lt; (1 - x) * x * (3 * x - 1) ↔ x &lt; 0 ∨ 1 / 3 &lt; x ∧ x &lt; 1</code></p>

#### [ Kevin Buzzard (Nov 14 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147702785):
<p>and now the case bash is much easier</p>

#### [ Kevin Buzzard (Nov 14 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147702799):
<p>but I had to clear denominators along the way</p>

#### [ Kenny Lau (Nov 14 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147702914):
<p>how about no</p>

#### [ Kevin Buzzard (Nov 14 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147702958):
<p>If it's a reasonable M1F question and if you want formal proof verification systems to be taken seriously by mathematicians, this has to be relatively straightforward</p>

#### [ Reid Barton (Nov 14 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147703048):
<p>Someone want to implement a cylindrical algebraic decomposition tactic?</p>

#### [ Kevin Buzzard (Nov 14 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147703084):
<p>Is that what's necessary?</p>

#### [ Mario Carneiro (Nov 14 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147703089):
<p>it's a case bash</p>

#### [ Kevin Buzzard (Nov 14 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147703092):
<p>Can we make it an issue or is this unreasonable?</p>

#### [ Kevin Buzzard (Nov 14 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147703100):
<p>It's a cylindrical algebraic decomposition Mario</p>

#### [ Mario Carneiro (Nov 14 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147703112):
<p>the generalization of this to more vars is CAD</p>

#### [ Reid Barton (Nov 14 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147703177):
<p>Yeah you don't really need it for one variable &amp; rational roots.</p>

#### [ Kevin Buzzard (Nov 14 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147703194):
<p><code>theorem Q4 : { x : ℝ | x ≠ 0 ∧ 3 * x + 1 / x &lt; 4 } =
  {y : ℝ | y &lt; 0 ∨ ((1 : ℝ) / 3 &lt; y ∧ y &lt; 1)}</code> you mean like this?</p>

#### [ Kevin Buzzard (Nov 14 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147703243):
<p>It's still a pain to prove that if <code>1/3 &lt; x</code> and <code>x &lt; 1</code> then <code>3 * x + 1 / x &lt; 4</code></p>

#### [ Kevin Buzzard (Nov 14 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147703262):
<p>My reworking to <code>⊢ 0 &lt; (1 - x) * x * (3 * x - 1) ↔ x &lt; 0 ∨ 1 / 3 &lt; x ∧ x &lt; 1</code> is definitely paying dividends</p>

#### [ Kenny Lau (Nov 14 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147703268):
<p>I think you should just let the IC gang prove that</p>

#### [ Mario Carneiro (Nov 14 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147703323):
<p>in general you have to figure out ordering of real algebraic numbers which is a pain</p>

#### [ Mario Carneiro (Nov 14 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147703366):
<p>and the best known algorithm is double exponential, a great <em>improvement</em> over the previous algorithm</p>

#### [ Kenny Lau (Nov 14 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147703451):
<p>what a pity, I was going to use it in my next gce exam</p>

#### [ Kevin Buzzard (Nov 14 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147704530):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">Q4</span> <span class="o">:</span> <span class="o">{</span> <span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">|</span> <span class="n">x</span> <span class="bp">≠</span> <span class="mi">0</span> <span class="bp">∧</span> <span class="mi">3</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">/</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="mi">4</span> <span class="o">}</span> <span class="bp">=</span>
  <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">|</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="mi">0</span> <span class="bp">∨</span> <span class="o">((</span><span class="mi">1</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">/</span> <span class="mi">3</span> <span class="bp">&lt;</span> <span class="n">x</span> <span class="bp">∧</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="mi">1</span><span class="o">)}</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">ext</span> <span class="n">x</span><span class="o">,</span>
  <span class="k">show</span> <span class="n">x</span> <span class="bp">≠</span> <span class="mi">0</span> <span class="bp">∧</span> <span class="mi">3</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">/</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="mi">4</span> <span class="bp">↔</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="mi">0</span> <span class="bp">∨</span> <span class="mi">1</span> <span class="bp">/</span> <span class="mi">3</span> <span class="bp">&lt;</span> <span class="n">x</span> <span class="bp">∧</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="mi">1</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">classical</span><span class="bp">.</span><span class="n">em</span> <span class="o">(</span><span class="n">x</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span> <span class="k">with</span> <span class="n">H0</span> <span class="n">Hn0</span><span class="o">,</span>
  <span class="o">{</span> <span class="c1">-- junk case x = 0</span>
    <span class="n">rw</span> <span class="n">H0</span><span class="o">,</span>
    <span class="n">norm_num</span><span class="o">,</span>
  <span class="o">},</span>
  <span class="n">rw</span> <span class="o">(</span><span class="k">show</span> <span class="n">x</span> <span class="bp">≠</span> <span class="mi">0</span> <span class="bp">↔</span> <span class="n">true</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">Hn0</span><span class="o">]),</span>
  <span class="n">rw</span> <span class="n">true_and</span><span class="o">,</span>
  <span class="k">show</span> <span class="o">(</span><span class="mi">3</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">/</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="mi">4</span> <span class="bp">↔</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="mi">0</span> <span class="bp">∨</span> <span class="mi">1</span> <span class="bp">/</span> <span class="mi">3</span> <span class="bp">&lt;</span> <span class="n">x</span> <span class="bp">∧</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="mi">1</span><span class="o">,</span>
  <span class="k">have</span> <span class="n">this</span> <span class="o">:</span> <span class="o">(</span><span class="mi">3</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">/</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="mi">4</span> <span class="bp">↔</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="mi">4</span> <span class="bp">-</span> <span class="o">(</span><span class="mi">3</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">/</span> <span class="n">x</span><span class="o">)</span>
    <span class="o">:=</span> <span class="o">(</span><span class="bp">@</span><span class="n">sub_pos</span> <span class="n">ℝ</span> <span class="o">(</span><span class="k">by</span> <span class="n">apply_instance</span><span class="o">)</span> <span class="o">(</span><span class="mi">4</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">((</span><span class="mi">3</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">/</span> <span class="n">x</span><span class="o">))</span><span class="bp">.</span><span class="n">symm</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">this</span><span class="o">,</span>
  <span class="n">rw</span> <span class="err">←</span><span class="n">sub_sub</span><span class="o">,</span>
  <span class="n">rw</span> <span class="err">←</span><span class="n">mul_one</span> <span class="o">(</span><span class="mi">4</span> <span class="bp">-</span> <span class="mi">3</span> <span class="bp">*</span> <span class="n">x</span><span class="o">),</span>
  <span class="c1">-- annoying rewrite</span>
  <span class="k">have</span> <span class="n">H</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="o">(</span><span class="mi">4</span> <span class="bp">-</span> <span class="mi">3</span> <span class="bp">*</span> <span class="n">x</span><span class="o">)</span> <span class="bp">*</span> <span class="mi">1</span> <span class="bp">-</span> <span class="mi">1</span> <span class="bp">/</span> <span class="n">x</span> <span class="bp">↔</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="o">(</span><span class="mi">4</span> <span class="bp">-</span> <span class="mi">3</span> <span class="bp">*</span> <span class="n">x</span><span class="o">)</span> <span class="bp">*</span> <span class="o">(</span><span class="n">x</span> <span class="bp">/</span> <span class="n">x</span><span class="o">)</span> <span class="bp">-</span> <span class="mi">1</span> <span class="bp">/</span> <span class="n">x</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">div_self</span> <span class="n">Hn0</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">rw</span> <span class="err">←</span><span class="n">mul_div_assoc</span><span class="o">,</span>
  <span class="n">rw</span> <span class="err">←</span><span class="n">sub_div</span><span class="o">,</span>
  <span class="n">rw</span> <span class="err">←</span><span class="n">mul_pos_iff_div_pos</span> <span class="n">Hn0</span><span class="o">,</span>
  <span class="n">replace</span> <span class="n">H</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">&gt;</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">mul_self_pos</span> <span class="n">Hn0</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">(</span><span class="k">show</span> <span class="o">((</span><span class="mi">4</span> <span class="bp">-</span> <span class="mi">3</span> <span class="bp">*</span> <span class="n">x</span><span class="o">)</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">-</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">=</span> <span class="o">(</span><span class="mi">1</span> <span class="bp">-</span> <span class="n">x</span><span class="o">)</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">*</span> <span class="o">(</span><span class="mi">3</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">-</span> <span class="mi">1</span><span class="o">),</span> <span class="k">by</span> <span class="n">ring</span><span class="o">),</span>
  <span class="c1">-- goal now</span>
  <span class="c1">-- ⊢ 0 &lt; (1 - x) * x * (3 * x - 1) ↔ x &lt; 0 ∨ 1 / 3 &lt; x ∧ x &lt; 1</span>
  <span class="n">cases</span> <span class="n">lt_or_ge</span> <span class="n">x</span> <span class="mi">0</span> <span class="k">with</span> <span class="n">h</span> <span class="n">h1</span><span class="o">,</span>
  <span class="c1">-- x &lt; 0</span>
    <span class="n">rw</span> <span class="o">(</span><span class="k">show</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="mi">0</span> <span class="bp">↔</span> <span class="n">true</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">h</span><span class="o">]),</span>
    <span class="n">rw</span> <span class="n">true_or</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">iff_true</span><span class="o">,</span>
    <span class="n">apply</span> <span class="n">mul_pos_of_neg_of_neg</span><span class="o">,</span>
      <span class="n">refine</span> <span class="n">mul_neg_of_pos_of_neg</span> <span class="bp">_</span> <span class="n">h</span><span class="o">,</span>
      <span class="n">apply</span> <span class="n">sub_pos_of_lt</span><span class="o">,</span>
      <span class="n">apply</span> <span class="n">lt_trans</span> <span class="n">h</span> <span class="n">zero_lt_one</span><span class="o">,</span>
    <span class="n">apply</span> <span class="n">sub_neg_of_lt</span><span class="o">,</span>
    <span class="n">refine</span> <span class="n">lt_trans</span> <span class="bp">_</span> <span class="n">zero_lt_one</span><span class="o">,</span>
    <span class="n">apply</span> <span class="n">mul_neg_of_pos_of_neg</span> <span class="bp">_</span> <span class="n">h</span><span class="o">,</span>
    <span class="n">norm_num</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">(</span><span class="k">show</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="mi">0</span> <span class="bp">↔</span> <span class="n">false</span><span class="o">,</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">iff_false</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">not_lt_of_ge</span> <span class="n">h1</span><span class="o">),</span>
  <span class="n">rw</span> <span class="n">false_or</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">le_or_gt</span> <span class="n">x</span> <span class="o">((</span><span class="mi">1</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">/</span> <span class="mi">3</span><span class="o">)</span> <span class="k">with</span> <span class="n">h2</span> <span class="n">h2</span><span class="o">,</span>
    <span class="n">rw</span> <span class="o">(</span><span class="k">show</span> <span class="o">(</span><span class="mi">1</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">/</span> <span class="mi">3</span> <span class="bp">&lt;</span> <span class="n">x</span> <span class="bp">↔</span> <span class="n">false</span><span class="o">,</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">iff_false</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">not_lt_of_ge</span> <span class="n">h2</span><span class="o">),</span>
    <span class="n">rw</span> <span class="n">false_and</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">iff_false</span><span class="o">,</span>
    <span class="n">apply</span> <span class="n">not_lt_of_ge</span><span class="o">,</span>
    <span class="n">refine</span> <span class="n">mul_nonpos_of_nonneg_of_nonpos</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span>
      <span class="n">refine</span> <span class="n">mul_nonneg</span> <span class="bp">_</span> <span class="n">h1</span><span class="o">,</span>
      <span class="k">show</span> <span class="mi">0</span> <span class="bp">≤</span> <span class="mi">1</span> <span class="bp">-</span> <span class="n">x</span><span class="o">,</span>
      <span class="n">rw</span> <span class="n">sub_nonneg</span><span class="o">,</span>
      <span class="n">exact</span> <span class="n">le_trans</span> <span class="n">h2</span> <span class="o">(</span><span class="k">by</span> <span class="n">norm_num</span><span class="o">),</span>
    <span class="n">rw</span> <span class="n">sub_nonpos</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">mul_comm</span><span class="o">,</span>
    <span class="n">apply</span> <span class="n">mul_le_of_le_div</span> <span class="o">(</span><span class="k">by</span> <span class="n">norm_num</span><span class="o">)</span> <span class="n">h2</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">lt_or_ge</span> <span class="n">x</span> <span class="mi">1</span><span class="o">,</span>
    <span class="n">rw</span> <span class="o">(</span><span class="n">iff_true</span> <span class="o">((</span><span class="mi">1</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">/</span> <span class="mi">3</span> <span class="bp">&lt;</span> <span class="n">x</span><span class="o">))</span><span class="bp">.</span><span class="mi">2</span> <span class="n">h2</span><span class="o">,</span>
    <span class="n">rw</span> <span class="o">(</span><span class="n">iff_true</span> <span class="o">(</span><span class="n">x</span> <span class="bp">&lt;</span> <span class="mi">1</span><span class="o">))</span><span class="bp">.</span><span class="mi">2</span> <span class="n">h</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">true_and</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">iff_true</span><span class="o">,</span>
    <span class="n">refine</span> <span class="n">mul_pos</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span>
      <span class="n">refine</span> <span class="n">mul_pos</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span>
        <span class="k">show</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="o">(</span><span class="mi">1</span> <span class="bp">-</span> <span class="n">x</span><span class="o">),</span>
        <span class="n">rwa</span> <span class="n">sub_pos</span><span class="o">,</span>
      <span class="n">refine</span> <span class="n">lt_trans</span> <span class="o">(</span><span class="k">by</span> <span class="n">norm_num</span><span class="o">)</span> <span class="n">h2</span><span class="o">,</span>
    <span class="k">show</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="mi">3</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">-</span> <span class="mi">1</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">sub_pos</span><span class="o">,</span>
    <span class="n">rwa</span> <span class="err">←</span><span class="n">div_lt_iff&#39;</span><span class="o">,</span>
    <span class="n">norm_num</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">(</span><span class="k">show</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="mi">1</span> <span class="bp">↔</span> <span class="n">false</span><span class="o">,</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">iff_false</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">not_lt_of_ge</span> <span class="n">h</span><span class="o">),</span>
  <span class="n">rw</span> <span class="n">and_false</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">iff_false</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">not_lt_of_ge</span><span class="o">,</span>
  <span class="n">refine</span> <span class="n">mul_nonpos_of_nonpos_of_nonneg</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span>
    <span class="n">refine</span> <span class="n">mul_nonpos_of_nonpos_of_nonneg</span> <span class="bp">_</span> <span class="n">h1</span><span class="o">,</span>
    <span class="n">simp</span> <span class="o">[</span><span class="n">h</span><span class="o">],</span> <span class="n">exact</span> <span class="n">h</span><span class="o">,</span>
  <span class="k">show</span> <span class="mi">0</span> <span class="bp">≤</span> <span class="mi">3</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">-</span> <span class="mi">1</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">sub_nonneg</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">mul_comm</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">le_mul_of_div_le</span><span class="o">,</span>
    <span class="n">norm_num</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">le_trans</span> <span class="bp">_</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">norm_num</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p>Much better than last year's effort</p>

#### [ Kenny Lau (Nov 14 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147704744):
<p>"much better"</p>

#### [ Kevin Buzzard (Nov 14 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147704761):
<p>thanks</p>

#### [ Kenny Lau (Nov 15 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147706417):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">real</span>

<span class="kn">theorem</span> <span class="n">Q4</span> <span class="o">:</span> <span class="o">{</span> <span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">|</span> <span class="n">x</span> <span class="bp">≠</span> <span class="mi">0</span> <span class="bp">∧</span> <span class="mi">3</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">/</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="mi">4</span> <span class="o">}</span> <span class="bp">=</span>
  <span class="o">{</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">|</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="mi">0</span> <span class="bp">∨</span> <span class="o">((</span><span class="mi">1</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">/</span> <span class="mi">3</span> <span class="bp">&lt;</span> <span class="n">x</span> <span class="bp">∧</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="mi">1</span><span class="o">)}</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">ext</span> <span class="n">x</span><span class="o">,</span>
  <span class="n">rcases</span> <span class="n">lt_trichotomy</span> <span class="n">x</span> <span class="mi">0</span> <span class="k">with</span> <span class="n">hxneg</span> <span class="bp">|</span> <span class="n">hx0</span> <span class="bp">|</span> <span class="n">hxpos</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">refine</span> <span class="n">iff_of_true</span> <span class="bp">⟨</span><span class="n">ne_of_lt</span> <span class="n">hxneg</span><span class="o">,</span> <span class="bp">_⟩</span> <span class="o">(</span><span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="n">hxneg</span><span class="o">),</span>
    <span class="n">refine</span> <span class="n">lt_trans</span> <span class="o">(</span><span class="n">add_neg</span> <span class="o">(</span><span class="n">mul_neg_of_pos_of_neg</span> <span class="bp">_</span> <span class="n">hxneg</span><span class="o">)</span> <span class="o">(</span><span class="n">one_div_neg_of_neg</span> <span class="n">hxneg</span><span class="o">))</span> <span class="bp">_;</span>
    <span class="n">norm_num</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">subst</span> <span class="n">x</span><span class="o">,</span> <span class="n">norm_num</span> <span class="o">},</span>
  <span class="k">show</span> <span class="n">x</span> <span class="bp">≠</span> <span class="mi">0</span> <span class="bp">∧</span> <span class="mi">3</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">/</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="mi">4</span> <span class="bp">↔</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="mi">0</span> <span class="bp">∨</span> <span class="o">((</span><span class="mi">1</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="bp">/</span> <span class="mi">3</span> <span class="bp">&lt;</span> <span class="n">x</span> <span class="bp">∧</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="mi">1</span><span class="o">),</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">eq_true_intro</span> <span class="o">(</span><span class="n">ne_of_gt</span> <span class="n">hxpos</span><span class="o">)],</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">true_and</span><span class="o">],</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">eq_false_intro</span> <span class="o">(</span><span class="n">not_lt_of_gt</span> <span class="n">hxpos</span><span class="o">)],</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">false_or</span><span class="o">],</span>
  <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">mul_lt_mul_right</span> <span class="n">hxpos</span><span class="o">],</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">add_mul</span><span class="o">],</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">one_div_mul_cancel</span> <span class="o">(</span><span class="n">ne_of_gt</span> <span class="n">hxpos</span><span class="o">)],</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">div_lt_iff</span> <span class="o">(</span><span class="k">show</span> <span class="o">(</span><span class="mi">0</span><span class="o">:</span><span class="n">ℝ</span><span class="o">)</span> <span class="bp">&lt;</span> <span class="mi">3</span><span class="o">,</span> <span class="k">by</span> <span class="n">norm_num</span><span class="o">)],</span>
  <span class="n">split</span><span class="o">,</span>
  <span class="o">{</span> <span class="k">assume</span> <span class="n">h</span> <span class="o">:</span> <span class="mi">3</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">&lt;</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">x</span><span class="o">,</span>
    <span class="n">replace</span> <span class="n">h</span> <span class="o">:=</span> <span class="n">sub_neg_of_lt</span> <span class="n">h</span><span class="o">,</span>
    <span class="n">rw</span> <span class="o">[</span><span class="k">show</span> <span class="mi">3</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">-</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">=</span> <span class="o">(</span><span class="mi">1</span> <span class="bp">-</span> <span class="n">x</span> <span class="bp">*</span> <span class="mi">3</span><span class="o">)</span> <span class="bp">*</span> <span class="o">(</span><span class="mi">1</span> <span class="bp">-</span> <span class="n">x</span><span class="o">),</span> <span class="k">by</span> <span class="n">ring</span><span class="o">]</span> <span class="n">at</span> <span class="n">h</span><span class="o">,</span>
    <span class="k">have</span> <span class="o">:</span> <span class="mi">1</span> <span class="bp">&lt;</span> <span class="n">x</span> <span class="bp">*</span> <span class="mi">3</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">apply</span> <span class="n">lt_of_not_ge</span><span class="o">,</span>
      <span class="k">assume</span> <span class="n">h2</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">*</span> <span class="mi">3</span> <span class="bp">≤</span> <span class="mi">1</span><span class="o">,</span>
      <span class="n">replace</span> <span class="n">h</span> <span class="o">:=</span> <span class="n">neg_of_mul_neg_left</span> <span class="n">h</span> <span class="o">(</span><span class="n">sub_nonneg_of_le</span> <span class="n">h2</span><span class="o">),</span>
      <span class="n">refine</span> <span class="n">not_lt_of_le</span> <span class="n">h2</span> <span class="bp">_</span><span class="o">,</span>
      <span class="n">refine</span> <span class="n">lt_trans</span> <span class="o">(</span><span class="k">show</span> <span class="o">(</span><span class="mi">1</span><span class="o">:</span><span class="n">ℝ</span><span class="o">)</span> <span class="bp">&lt;</span> <span class="mi">3</span><span class="o">,</span> <span class="k">by</span> <span class="n">norm_num</span><span class="o">)</span> <span class="bp">_</span><span class="o">,</span>
      <span class="n">replace</span> <span class="n">h</span> <span class="o">:=</span> <span class="n">lt_of_sub_neg</span> <span class="n">h</span><span class="o">,</span>
      <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">mul_lt_mul_right</span> <span class="o">(</span><span class="k">show</span> <span class="o">(</span><span class="mi">0</span><span class="o">:</span><span class="n">ℝ</span><span class="o">)</span> <span class="bp">&lt;</span> <span class="mi">3</span><span class="o">,</span> <span class="k">by</span> <span class="n">norm_num</span><span class="o">)]</span> <span class="n">at</span> <span class="n">h</span><span class="o">,</span>
      <span class="n">rwa</span> <span class="o">[</span><span class="n">one_mul</span><span class="o">]</span> <span class="n">at</span> <span class="n">h</span> <span class="o">},</span>
    <span class="n">refine</span> <span class="bp">⟨</span><span class="n">this</span><span class="o">,</span> <span class="n">lt_of_sub_pos</span> <span class="bp">_⟩</span><span class="o">,</span>
    <span class="n">apply</span> <span class="n">lt_of_not_ge</span><span class="o">,</span>
    <span class="k">assume</span> <span class="n">h3</span> <span class="o">:</span> <span class="mi">1</span> <span class="bp">-</span> <span class="n">x</span> <span class="bp">≤</span> <span class="mi">0</span><span class="o">,</span>
    <span class="n">apply</span> <span class="n">not_le_of_lt</span> <span class="n">h</span><span class="o">,</span>
    <span class="n">exact</span> <span class="n">mul_nonneg_of_nonpos_of_nonpos</span> <span class="o">(</span><span class="n">le_of_lt</span> <span class="o">(</span><span class="n">sub_neg_of_lt</span> <span class="n">this</span><span class="o">))</span> <span class="n">h3</span> <span class="o">},</span>
  <span class="o">{</span> <span class="k">assume</span> <span class="n">h</span> <span class="o">:</span> <span class="mi">1</span> <span class="bp">&lt;</span> <span class="n">x</span> <span class="bp">*</span> <span class="mi">3</span> <span class="bp">∧</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="mi">1</span><span class="o">,</span>
    <span class="n">cases</span> <span class="n">h</span> <span class="k">with</span> <span class="n">h1</span> <span class="n">h2</span><span class="o">,</span>
    <span class="n">apply</span> <span class="n">lt_of_sub_neg</span><span class="o">,</span>
    <span class="n">rw</span> <span class="o">[</span><span class="k">show</span> <span class="mi">3</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">-</span> <span class="mi">4</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">=</span> <span class="o">(</span><span class="mi">1</span> <span class="bp">-</span> <span class="n">x</span> <span class="bp">*</span> <span class="mi">3</span><span class="o">)</span> <span class="bp">*</span> <span class="o">(</span><span class="mi">1</span> <span class="bp">-</span> <span class="n">x</span><span class="o">),</span> <span class="k">by</span> <span class="n">ring</span><span class="o">],</span>
    <span class="n">exact</span> <span class="n">mul_neg_of_neg_of_pos</span> <span class="o">(</span><span class="n">sub_neg_of_lt</span> <span class="n">h1</span><span class="o">)</span> <span class="o">(</span><span class="n">sub_pos_of_lt</span> <span class="n">h2</span><span class="o">)</span> <span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Nov 15 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147706420):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span></p>

#### [ Kenny Lau (Nov 15 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147706433):
<p>half your size</p>

#### [ Kevin Buzzard (Nov 15 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147706502):
<p>It's still a lot longer than what most of the first years produce with pen and paper though isn't it :-/</p>

#### [ Kevin Buzzard (Nov 15 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147706584):
<p>you did the case split at the start. I worked on the goal first. Is your way better or would you have written half as much as me if you'd used my strategy too?</p>

#### [ Kenny Lau (Nov 15 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147706587):
<p>btw:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">div_pos_iff_mul_pos</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">Hy</span> <span class="o">:</span> <span class="n">y</span> <span class="bp">≠</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">x</span> <span class="bp">*</span> <span class="n">y</span> <span class="bp">↔</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">x</span> <span class="bp">/</span> <span class="n">y</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="k">have</span> <span class="o">:=</span> <span class="n">mul_self_pos</span> <span class="n">Hy</span><span class="o">,</span>
  <span class="n">rw</span> <span class="err">←</span> <span class="bp">@</span><span class="n">mul_lt_mul_right</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="n">x</span><span class="bp">/</span><span class="n">y</span><span class="o">)</span> <span class="bp">_</span> <span class="n">this</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">zero_mul</span><span class="o">,</span>
  <span class="n">rw</span> <span class="err">←</span> <span class="n">mul_assoc</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">div_mul_cancel</span> <span class="bp">_</span> <span class="n">Hy</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Nov 15 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147706603):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">div_pos_iff_mul_pos</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">Hy</span> <span class="o">:</span> <span class="n">y</span> <span class="bp">≠</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">x</span> <span class="bp">*</span> <span class="n">y</span> <span class="bp">↔</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">x</span> <span class="bp">/</span> <span class="n">y</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="bp">@</span><span class="n">mul_lt_mul_right</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="n">x</span><span class="bp">/</span><span class="n">y</span><span class="o">)</span> <span class="bp">_</span> <span class="o">(</span><span class="n">mul_self_pos</span> <span class="n">Hy</span><span class="o">)]</span><span class="bp">;</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">zero_mul</span><span class="o">,</span> <span class="err">←</span> <span class="n">mul_assoc</span><span class="o">,</span> <span class="n">div_mul_cancel</span> <span class="bp">_</span> <span class="n">Hy</span><span class="o">]</span>
</pre></div>

#### [ Kenny Lau (Nov 15 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147706702):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">div_pos_iff_mul_pos</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">Hy</span> <span class="o">:</span> <span class="n">y</span> <span class="bp">≠</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">x</span> <span class="bp">*</span> <span class="n">y</span> <span class="bp">↔</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">x</span> <span class="bp">/</span> <span class="n">y</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">div_lt_div_right</span> <span class="o">(</span><span class="n">mul_self_pos</span> <span class="n">Hy</span><span class="o">),</span> <span class="n">zero_div</span><span class="o">,</span> <span class="err">←</span> <span class="n">div_div_eq_div_mul</span><span class="o">,</span> <span class="n">mul_div_cancel</span> <span class="bp">_</span> <span class="n">Hy</span><span class="o">]</span>
</pre></div>

#### [ Kenny Lau (Nov 15 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147706705):
<p>(98 characters!)</p>

#### [ Kenny Lau (Nov 15 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147706769):
<blockquote>
<p>you did the case split at the start. I worked on the goal first. Is your way better or would you have written half as much as me if you'd used my strategy too?</p>
</blockquote>
<p>I mean, you also did case split at the start</p>

#### [ Reid Barton (Nov 15 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147706788):
<p>Isn't that <code>Hy</code> hypothesis actually unneeded?</p>

#### [ Reid Barton (Nov 15 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147706795):
<p>If <code>y = 0</code> then both things are 0</p>

#### [ Kenny Lau (Nov 15 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147706981):
<p>great</p>

#### [ Kenny Lau (Nov 15 2018 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147707018):
<p>"Lean helps me understand maths better"</p>

#### [ Kenny Lau (Nov 15 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147707033):
<p>"<code>y</code> doesn't need to be nonzero"</p>

#### [ Mario Carneiro (Nov 15 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147713393):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">ring</span> <span class="n">data</span><span class="bp">.</span><span class="n">set</span><span class="bp">.</span><span class="n">intervals</span>

<span class="kn">theorem</span> <span class="n">mul_pos_iff</span> <span class="o">{</span><span class="n">α</span><span class="o">}</span> <span class="o">[</span><span class="n">linear_ordered_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">:</span>
  <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">a</span> <span class="bp">*</span> <span class="n">b</span> <span class="bp">↔</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">a</span> <span class="bp">∧</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">b</span> <span class="bp">∨</span> <span class="n">a</span> <span class="bp">&lt;</span> <span class="mi">0</span> <span class="bp">∧</span> <span class="n">b</span> <span class="bp">&lt;</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="bp">⟨</span><span class="n">pos_and_pos_or_neg_and_neg_of_mul_pos</span><span class="o">,</span>
  <span class="n">or</span><span class="bp">.</span><span class="n">rec</span> <span class="o">(</span><span class="n">and</span><span class="bp">.</span><span class="n">rec</span> <span class="n">mul_pos</span><span class="o">)</span> <span class="o">(</span><span class="n">and</span><span class="bp">.</span><span class="n">rec</span> <span class="err">$</span> <span class="k">by</span> <span class="n">exact</span> <span class="n">mul_pos_of_neg_of_neg</span><span class="o">)</span><span class="bp">⟩</span>

<span class="kn">theorem</span> <span class="n">or_iff_left</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">¬</span> <span class="n">b</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">∨</span> <span class="n">b</span> <span class="bp">↔</span> <span class="n">a</span> <span class="o">:=</span>
<span class="n">or_iff_left_of_imp</span> <span class="n">h</span><span class="bp">.</span><span class="n">elim</span>

<span class="kn">theorem</span> <span class="n">or_iff_right</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">¬</span> <span class="n">a</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">∨</span> <span class="n">b</span> <span class="bp">↔</span> <span class="n">b</span> <span class="o">:=</span>
<span class="n">or_iff_right_of_imp</span> <span class="n">h</span><span class="bp">.</span><span class="n">elim</span>

<span class="kn">open</span> <span class="n">set</span>
<span class="kn">theorem</span> <span class="n">Q4</span> <span class="o">:</span> <span class="o">{</span> <span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">|</span> <span class="n">x</span> <span class="bp">≠</span> <span class="mi">0</span> <span class="bp">∧</span> <span class="mi">3</span> <span class="bp">*</span> <span class="n">x</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">/</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="mi">4</span> <span class="o">}</span> <span class="bp">=</span> <span class="n">Iio</span> <span class="mi">0</span> <span class="err">∪</span> <span class="n">Ioo</span> <span class="o">(</span><span class="mi">1</span> <span class="bp">/</span> <span class="mi">3</span><span class="o">)</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">ext</span> <span class="n">x</span><span class="o">,</span>
  <span class="n">rcases</span> <span class="n">lt_trichotomy</span> <span class="n">x</span> <span class="mi">0</span> <span class="k">with</span> <span class="n">x0</span><span class="bp">|</span><span class="n">x0</span><span class="bp">|</span><span class="n">x0</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">refine</span> <span class="n">iff_of_true</span> <span class="bp">⟨</span><span class="n">ne_of_lt</span> <span class="n">x0</span><span class="o">,</span>
      <span class="n">lt_trans</span> <span class="o">(</span><span class="n">add_neg</span>
        <span class="o">(</span><span class="n">mul_neg_of_pos_of_neg</span> <span class="bp">_</span> <span class="n">x0</span><span class="o">)</span>
        <span class="o">(</span><span class="n">one_div_neg_of_neg</span> <span class="n">x0</span><span class="o">))</span> <span class="bp">_⟩</span> <span class="o">(</span><span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="n">x0</span><span class="o">)</span><span class="bp">;</span>
    <span class="n">norm_num</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">subst</span> <span class="n">x</span><span class="o">,</span> <span class="n">norm_num</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">dsimp</span> <span class="o">[</span><span class="n">Iio</span><span class="o">,</span> <span class="n">Ioo</span><span class="o">],</span>
    <span class="n">rw</span> <span class="o">[</span><span class="n">and_iff_right</span> <span class="o">(</span><span class="n">ne_of_gt</span> <span class="n">x0</span><span class="o">),</span> <span class="n">or_iff_right</span> <span class="o">(</span><span class="n">not_lt_of_gt</span> <span class="n">x0</span><span class="o">),</span>
      <span class="n">add_div_eq_mul_add_div</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="n">ne_of_gt</span> <span class="n">x0</span><span class="o">),</span>
      <span class="n">div_lt_iff</span> <span class="n">x0</span><span class="o">,</span> <span class="n">div_lt_iff&#39;</span> <span class="o">(</span><span class="k">by</span> <span class="n">norm_num</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="o">(</span><span class="mi">3</span><span class="o">:</span><span class="n">ℝ</span><span class="o">)),</span> <span class="err">←</span> <span class="n">sub_pos</span><span class="o">,</span>
      <span class="o">(</span><span class="k">by</span> <span class="n">ring</span> <span class="o">:</span> <span class="mi">4</span><span class="bp">*</span><span class="n">x</span> <span class="bp">-</span> <span class="o">(</span><span class="mi">3</span><span class="bp">*</span><span class="n">x</span><span class="bp">*</span><span class="n">x</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="mi">3</span><span class="bp">*</span><span class="n">x</span> <span class="bp">-</span> <span class="mi">1</span><span class="o">)</span><span class="bp">*</span><span class="o">(</span><span class="mi">1</span> <span class="bp">-</span> <span class="n">x</span><span class="o">)),</span>
      <span class="n">mul_pos_iff</span><span class="o">,</span> <span class="n">sub_pos</span><span class="o">,</span> <span class="n">sub_pos</span><span class="o">,</span> <span class="n">sub_lt_zero</span><span class="o">,</span> <span class="n">sub_lt_zero</span><span class="o">,</span>
      <span class="n">or_iff_left</span><span class="o">],</span>
    <span class="n">rintro</span> <span class="bp">⟨</span><span class="n">h₁</span><span class="o">,</span> <span class="n">h₂</span><span class="bp">⟩</span><span class="o">,</span>
    <span class="n">refine</span> <span class="n">absurd</span> <span class="o">(</span><span class="n">lt_trans</span> <span class="n">h₂</span> <span class="o">((</span><span class="n">lt_div_iff&#39;</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span> <span class="n">h₁</span><span class="o">))</span> <span class="bp">_;</span> <span class="n">norm_num</span> <span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Nov 15 2018 at 03:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147716871):
<p>I shall explode this proof tomorrow</p>

#### [ Patrick Massot (Nov 15 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147728220):
<p>Mario, why do you need to explicitly invoke all those <code>and_iff_right</code>, <code>or_iff_right</code>, <code>or_iff_left</code>? Isn't it something that the simplifier should do (using hypothesis <code>x0</code>)?</p>

#### [ Patrick Massot (Nov 15 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147728438):
<p>Makes me think: <span class="user-mention" data-user-id="110026">@Simon Hudon</span> what happened to your monotonicity tactic?</p>

#### [ Simon Hudon (Nov 15 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_pos_iff_mul_pos%20golf/near/147754940):
<p>Mario is still unhappy with it.</p>


{% endraw %}
