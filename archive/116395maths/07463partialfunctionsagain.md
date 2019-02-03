---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/07463partialfunctionsagain.html
---

## Stream: [maths](index.html)
### Topic: [partial functions again](07463partialfunctionsagain.html)

---


{% raw %}
#### [ Patrick Massot (Sep 04 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133331307):
<p>With the recent merges from my so-called differential topology repository to mathlib, the next target in this direction is the definition of derivatives (Fréchet derivative if you insist on this terminology). It is very easy to say that a function defined on a whole normed vector space is differentiable at some point a: <a href="https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/calculus.lean#L17" target="_blank" title="https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/calculus.lean#L17">https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/calculus.lean#L17</a> But of course we want derivatives of functions defined on a subset of a normed space, at least allowing an open set. I can clearly try to adapt the definition, but I'd be happy to read any advice.</p>

#### [ Patrick Massot (Sep 04 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133331524):
<p>For instance, <a href="https://github.com/thalesant/formalabstracts/blob/riemann_hypothesis/folklore/complex.lean#L227" target="_blank" title="https://github.com/thalesant/formalabstracts/blob/riemann_hypothesis/folklore/complex.lean#L227">https://github.com/thalesant/formalabstracts/blob/riemann_hypothesis/folklore/complex.lean#L227</a> (in the holomorphic case, but this doesn't matter) define a function from a subset of a normed space to be differentiable at x if the subset is open and the extension by zero (which is defined everywhere) is differentiable at x. This is one option</p>

#### [ Patrick Massot (Sep 04 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133333155):
<p>I ran a quick sanity check on the definition from FAbstract (I wanted to see with my own eyes that division by zero works as intended).</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">complex</span>
<span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">limits</span>

<span class="kn">open</span> <span class="n">filter</span> <span class="n">complex</span>

<span class="n">def</span> <span class="n">has_complex_derivative_at</span>
<span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">ℂ</span> <span class="bp">→</span> <span class="n">ℂ</span><span class="o">)</span>
<span class="o">(</span><span class="n">f&#39;z</span> <span class="o">:</span> <span class="n">ℂ</span><span class="o">)</span>
<span class="o">(</span><span class="n">z</span> <span class="o">:</span> <span class="n">ℂ</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="k">let</span> <span class="n">error_term</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">ℂ</span><span class="o">)</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="o">:=</span>
    <span class="n">abs</span><span class="o">((</span><span class="n">f</span> <span class="o">(</span><span class="n">z</span> <span class="bp">+</span> <span class="n">h</span><span class="o">)</span> <span class="bp">-</span> <span class="o">(</span><span class="n">f</span> <span class="n">z</span> <span class="bp">+</span> <span class="n">f&#39;z</span> <span class="bp">*</span> <span class="n">h</span><span class="o">))</span><span class="bp">/</span><span class="n">h</span><span class="o">)</span> <span class="k">in</span>
<span class="o">(</span><span class="n">tendsto</span> <span class="n">error_term</span> <span class="o">(</span><span class="n">nhds</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="n">ℂ</span><span class="o">))</span> <span class="o">(</span><span class="n">nhds</span> <span class="o">(</span><span class="mi">0</span><span class="o">:</span><span class="n">ℝ</span><span class="o">)))</span>

<span class="kn">lemma</span> <span class="n">test</span> <span class="o">:</span> <span class="n">has_complex_derivative_at</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">z</span><span class="o">,</span> <span class="n">z</span><span class="err">^</span><span class="mi">2</span><span class="o">)</span> <span class="mi">2</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">dsimp</span> <span class="n">only</span> <span class="o">[</span><span class="n">has_complex_derivative_at</span><span class="o">],</span>

  <span class="k">have</span> <span class="o">:</span>  <span class="o">(</span><span class="bp">λ</span> <span class="n">h</span> <span class="o">:</span> <span class="n">ℂ</span><span class="o">,</span> <span class="n">abs</span> <span class="o">(((</span><span class="mi">1</span> <span class="bp">+</span> <span class="n">h</span><span class="o">)</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">-</span> <span class="o">(</span><span class="mi">1</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">+</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">h</span><span class="o">))</span><span class="bp">/</span><span class="n">h</span><span class="o">))</span> <span class="bp">=</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">abs</span><span class="o">(</span><span class="n">h</span><span class="err">^</span><span class="mi">2</span><span class="bp">/</span><span class="n">h</span><span class="o">)),</span>
  <span class="k">by</span> <span class="n">ext</span> <span class="bp">;</span> <span class="n">congr</span><span class="bp">;</span> <span class="n">ring</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">this</span><span class="o">,</span>

  <span class="n">rw</span> <span class="n">tendsto_nhds_of_metric</span><span class="o">,</span>
  <span class="n">intros</span> <span class="n">ε</span> <span class="n">ε_pos</span><span class="o">,</span>
  <span class="n">existsi</span> <span class="o">[</span><span class="n">ε</span><span class="o">,</span> <span class="n">ε_pos</span><span class="o">],</span>
  <span class="n">intros</span> <span class="n">x</span> <span class="n">dx</span><span class="o">,</span>
  <span class="n">by_cases</span> <span class="n">h</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">simpa</span> <span class="o">[</span><span class="n">h</span><span class="o">,</span> <span class="n">ε_pos</span><span class="o">]</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">rw</span> <span class="o">[</span><span class="n">pow_two</span><span class="o">,</span> <span class="n">mul_div_cancel</span> <span class="n">x</span> <span class="n">h</span><span class="o">],</span>
    <span class="n">dsimp</span><span class="o">[</span><span class="n">dist</span><span class="o">]</span> <span class="n">at</span> <span class="n">dx</span> <span class="err">⊢</span><span class="o">,</span>
    <span class="n">simpa</span> <span class="kn">using</span> <span class="n">dx</span> <span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Patrick Massot (Sep 04 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133333260):
<p>First I'm both amazed and ashamed that I wrote that so quickly without insulting my computer. But of course I'd be very happy to read a simpler proof. <span class="user-mention" data-user-id="110596">@Rob Lewis</span> please feel free to explain that your Lean/Sage bridge allows to do this limit computation in one line.</p>

#### [ Patrick Massot (Sep 04 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133333813):
<p>I can merge the last two lines in <code>simpa [dist] using dx</code></p>

#### [ Patrick Massot (Sep 04 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133333948):
<p>Anyway, this great success of division by zero makes me wonder whether I should define differentiability using  <code>∥f (a + h) - f a - L h∥/ ∥h∥</code></p>

#### [ Chris Hughes (Sep 04 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133334379):
<p>Golfed as requested</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">test</span> <span class="o">:</span> <span class="n">has_complex_derivative_at</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">z</span><span class="o">,</span> <span class="n">z</span><span class="err">^</span><span class="mi">2</span><span class="o">)</span> <span class="mi">2</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="k">have</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">h</span> <span class="o">:</span> <span class="n">ℂ</span><span class="o">,</span> <span class="n">abs</span> <span class="o">(((</span><span class="mi">1</span> <span class="bp">+</span> <span class="n">h</span><span class="o">)</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">-</span> <span class="o">(</span><span class="mi">1</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">+</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">h</span><span class="o">))</span> <span class="bp">/</span> <span class="n">h</span><span class="o">))</span> <span class="bp">=</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">abs</span> <span class="o">(</span><span class="n">h</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">/</span> <span class="n">h</span><span class="o">)),</span>
  <span class="k">by</span> <span class="n">ext</span><span class="bp">;</span> <span class="n">congr</span><span class="bp">;</span> <span class="n">ring</span><span class="o">,</span>
<span class="k">by</span> <span class="n">simp</span> <span class="n">only</span> <span class="o">[</span><span class="n">has_complex_derivative_at</span><span class="o">,</span> <span class="n">this</span><span class="o">,</span> <span class="n">tendsto_nhds_of_metric</span><span class="o">]</span><span class="bp">;</span>
  <span class="n">exact</span> <span class="bp">λ</span> <span class="n">ε</span> <span class="n">ε0</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">ε</span><span class="o">,</span> <span class="n">ε0</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">x</span> <span class="n">dx</span><span class="o">,</span> <span class="k">if</span> <span class="n">h</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">0</span> <span class="k">then</span> <span class="k">by</span> <span class="n">simpa</span> <span class="o">[</span><span class="n">h</span><span class="o">,</span> <span class="n">ε0</span><span class="o">]</span>
  <span class="k">else</span> <span class="k">by</span> <span class="n">dsimp</span> <span class="o">[</span><span class="n">dist</span><span class="o">]</span> <span class="n">at</span> <span class="bp">*;</span> <span class="n">simpa</span> <span class="o">[</span><span class="n">pow_two</span><span class="o">,</span> <span class="n">mul_div_cancel</span> <span class="n">x</span> <span class="n">h</span><span class="o">]</span> <span class="kn">using</span> <span class="n">dx</span><span class="bp">⟩</span>
</pre></div>

#### [ Kevin Buzzard (Sep 04 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133334501):
<p>So 0/0 isn't 1? ;-)</p>

#### [ Kevin Buzzard (Sep 04 2018 at 22:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133334514):
<p>The applied mathematicians were lying to me</p>

#### [ Mario Carneiro (Sep 04 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133334544):
<p>0/0 = 0 is actually really convenient for stating the definition of the derivative</p>

#### [ Kevin Buzzard (Sep 04 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133334553):
<p>PS are we witnessing the first time Lean has ever differentiated a function here?</p>

#### [ Mario Carneiro (Sep 04 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133334564):
<p>well, the chain rule was a derivative</p>

#### [ Kevin Buzzard (Sep 04 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133334572):
<p>0/0 -- you got lucky :-)</p>

#### [ Kevin Buzzard (Sep 04 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133334645):
<p>Chris -- with the binomial theorem you can differentiate x^n and with Patrick's knowledge of filters he can prove differentiation is linear, and then we can differentiate polynomials!</p>

#### [ Kenny Lau (Sep 04 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133334654):
<p>we can differentiate polynomials just fine</p>

#### [ Kenny Lau (Sep 04 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133334657):
<p>(hey, you teach Galois theory)</p>

#### [ Mario Carneiro (Sep 04 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133334701):
<p>not formal derivatives, real derivatives</p>

#### [ Kevin Buzzard (Sep 04 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133334735):
<p>But of course we need to differentiate <code>cos</code> too :-)</p>

#### [ Kevin Buzzard (Sep 04 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133334784):
<p>That will follow from C-linearity if someone can differentiate exp. Mario did you say there was a dirty trick for that?</p>

#### [ Kevin Buzzard (Sep 04 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133334838):
<p>I guess step one is to get exp in mathlib...</p>

#### [ Mario Carneiro (Sep 04 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133334847):
<p>yes, <code>1 + x &lt;= exp x &lt;= 1/(1-x)</code> proves <code>exp' 0 = 1</code> and then it's easy</p>

#### [ Patrick Massot (Sep 04 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133335121):
<p>Thanks Chris. I think it's exactly the same proof though.</p>

#### [ Chris Hughes (Sep 04 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133335145):
<p>That is correct</p>

#### [ Kevin Buzzard (Sep 04 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133335163):
<p>It's easy if you have the product rule, but Patrick doesn't believe in the product rule</p>

#### [ Patrick Massot (Sep 04 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133335170):
<p>What?</p>

#### [ Kevin Buzzard (Sep 04 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133335226):
<p>The product rule is a low-dimensional coincidence</p>

#### [ Kenny Lau (Sep 04 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133335251):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">test</span> <span class="o">:</span> <span class="n">has_complex_derivative_at</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">z</span><span class="o">,</span> <span class="n">z</span><span class="err">^</span><span class="mi">2</span><span class="o">)</span> <span class="mi">2</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="n">tendsto_nhds_of_metric</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">ε</span> <span class="n">hε</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">ε</span><span class="o">,</span> <span class="n">hε</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">z</span> <span class="n">hz</span><span class="o">,</span>
<span class="k">if</span> <span class="n">h</span> <span class="o">:</span> <span class="n">z</span> <span class="bp">=</span> <span class="mi">0</span> <span class="k">then</span> <span class="k">by</span> <span class="n">simpa</span> <span class="o">[</span><span class="n">h</span><span class="o">]</span> <span class="k">else</span>
<span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">pow_two</span><span class="o">,</span> <span class="n">mul_add</span><span class="o">,</span> <span class="n">add_mul</span><span class="o">,</span> <span class="n">two_mul</span><span class="o">,</span> <span class="n">dist</span><span class="o">]</span><span class="bp">;</span>
<span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">complex</span><span class="bp">.</span><span class="n">abs_mul</span> <span class="n">z</span><span class="o">,</span> <span class="err">←</span> <span class="n">complex</span><span class="bp">.</span><span class="n">abs_div</span><span class="o">,</span> <span class="n">mul_div_cancel</span> <span class="bp">_</span> <span class="n">h</span><span class="o">]</span><span class="bp">;</span>
<span class="n">simpa</span> <span class="o">[</span><span class="n">dist</span><span class="o">]</span> <span class="kn">using</span> <span class="n">hz</span><span class="bp">⟩</span>
</pre></div>

#### [ Kenny Lau (Sep 04 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133335477):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">test</span> <span class="o">:</span> <span class="n">has_complex_derivative_at</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">z</span><span class="o">,</span> <span class="n">z</span><span class="err">^</span><span class="mi">2</span><span class="o">)</span> <span class="mi">2</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="k">have</span> <span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">z</span> <span class="o">:</span> <span class="n">ℂ</span><span class="o">,</span> <span class="bp">-</span><span class="mi">1</span> <span class="bp">+</span> <span class="o">(</span><span class="bp">-</span><span class="o">(</span><span class="mi">2</span> <span class="bp">*</span> <span class="n">z</span><span class="o">)</span> <span class="bp">+</span> <span class="o">(</span><span class="n">z</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="err">^</span> <span class="mi">2</span><span class="o">)</span> <span class="bp">=</span> <span class="n">z</span> <span class="bp">*</span> <span class="n">z</span><span class="o">,</span>
  <span class="k">from</span> <span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="k">by</span> <span class="n">ring</span><span class="o">,</span>
<span class="n">tendsto_nhds_of_metric</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">ε</span> <span class="n">hε</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">ε</span><span class="o">,</span> <span class="n">hε</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">z</span> <span class="n">hz</span><span class="o">,</span>
<span class="k">if</span> <span class="n">h</span> <span class="o">:</span> <span class="n">z</span> <span class="bp">=</span> <span class="mi">0</span> <span class="k">then</span> <span class="k">by</span> <span class="n">simpa</span> <span class="o">[</span><span class="n">h</span><span class="o">]</span> <span class="k">else</span>
<span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">H</span><span class="o">,</span> <span class="n">mul_div_cancel</span> <span class="bp">_</span> <span class="n">h</span><span class="o">,</span> <span class="bp">-</span><span class="n">complex</span><span class="bp">.</span><span class="n">abs_div</span><span class="o">]</span><span class="bp">;</span>
<span class="n">simpa</span> <span class="o">[</span><span class="n">dist</span><span class="o">]</span> <span class="kn">using</span> <span class="n">hz</span><span class="bp">⟩</span>
</pre></div>

#### [ Kenny Lau (Sep 04 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133335582):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">test</span> <span class="o">:</span> <span class="n">has_complex_derivative_at</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">z</span><span class="o">,</span> <span class="n">z</span><span class="err">^</span><span class="mi">2</span><span class="o">)</span> <span class="mi">2</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="n">tendsto_nhds_of_metric</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">ε</span> <span class="n">hε</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">ε</span><span class="o">,</span> <span class="n">hε</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">z</span> <span class="n">hz</span><span class="o">,</span>
<span class="k">if</span> <span class="n">h</span> <span class="o">:</span> <span class="n">z</span> <span class="bp">=</span> <span class="mi">0</span> <span class="k">then</span> <span class="k">by</span> <span class="n">simpa</span> <span class="o">[</span><span class="n">h</span><span class="o">]</span> <span class="k">else</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">pow_two</span><span class="o">,</span>
<span class="n">mul_add</span><span class="o">,</span> <span class="n">add_mul</span><span class="o">,</span> <span class="n">two_mul</span><span class="o">,</span> <span class="n">mul_div_cancel</span> <span class="bp">_</span> <span class="n">h</span><span class="o">,</span>
<span class="bp">-</span><span class="n">complex</span><span class="bp">.</span><span class="n">abs_div</span><span class="o">]</span><span class="bp">;</span> <span class="n">simpa</span> <span class="o">[</span><span class="n">dist</span><span class="o">]</span> <span class="kn">using</span> <span class="n">hz</span><span class="bp">⟩</span>
</pre></div>

#### [ Kenny Lau (Sep 04 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133335588):
<p>finally 4 lines</p>

#### [ Chris Hughes (Sep 04 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133335659):
<p>I think you broke the style guidelines with the last one.</p>

#### [ Kenny Lau (Sep 04 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133335813):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">test</span> <span class="o">:</span> <span class="n">has_complex_derivative_at</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">z</span><span class="o">,</span> <span class="n">z</span><span class="err">^</span><span class="mi">2</span><span class="o">)</span> <span class="mi">2</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="n">tendsto_nhds_of_metric</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">ε</span> <span class="n">hε</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">ε</span><span class="o">,</span> <span class="n">hε</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">z</span> <span class="n">hz</span><span class="o">,</span>
<span class="k">if</span> <span class="n">h</span> <span class="o">:</span> <span class="n">z</span> <span class="bp">=</span> <span class="mi">0</span> <span class="k">then</span> <span class="k">by</span> <span class="n">simpa</span> <span class="o">[</span><span class="n">h</span><span class="o">]</span> <span class="k">else</span>
<span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">pow_two</span><span class="o">,</span> <span class="n">add_mul_self_eq</span><span class="o">,</span> <span class="n">mul_div_cancel</span> <span class="bp">_</span> <span class="n">h</span><span class="o">,</span> <span class="bp">-</span><span class="n">complex</span><span class="bp">.</span><span class="n">abs_div</span><span class="o">]</span><span class="bp">;</span>
<span class="n">simpa</span> <span class="o">[</span><span class="n">dist</span><span class="o">]</span> <span class="kn">using</span> <span class="n">hz</span><span class="bp">⟩</span>
</pre></div>

#### [ Kenny Lau (Sep 04 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133335883):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">test</span> <span class="o">:</span> <span class="n">has_complex_derivative_at</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">z</span><span class="o">,</span> <span class="n">z</span><span class="err">^</span><span class="mi">2</span><span class="o">)</span> <span class="mi">2</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="n">tendsto_nhds_of_metric</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">ε</span> <span class="n">hε</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">ε</span><span class="o">,</span> <span class="n">hε</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">z</span> <span class="n">hz</span><span class="o">,</span>
<span class="k">if</span> <span class="n">h</span> <span class="o">:</span> <span class="n">z</span> <span class="bp">=</span> <span class="mi">0</span> <span class="k">then</span> <span class="k">by</span> <span class="n">simpa</span> <span class="o">[</span><span class="n">h</span><span class="o">]</span> <span class="k">else</span>
<span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">pow_two</span><span class="o">,</span> <span class="n">add_mul_self_eq</span><span class="o">,</span> <span class="bp">-</span><span class="n">complex</span><span class="bp">.</span><span class="n">abs_div</span><span class="o">]</span><span class="bp">;</span>
<span class="n">simpa</span> <span class="o">[</span><span class="n">mul_div_cancel</span> <span class="bp">_</span> <span class="n">h</span><span class="o">,</span> <span class="n">dist</span><span class="o">]</span> <span class="kn">using</span> <span class="n">hz</span><span class="bp">⟩</span>
</pre></div>

#### [ Kevin Buzzard (Sep 04 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133335938):
<p>Kenny this reminds me of Chris Ford's question "differentiate x^10*sin(x) five times"</p>

#### [ Kevin Buzzard (Sep 04 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133335986):
<p>for which my answer was "10 x^9*sin(x) + x^10*cos(x) every time"</p>

#### [ Kevin Buzzard (Sep 04 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133336000):
<p>Why don't you prove the product rule one time instead?</p>

#### [ Mario Carneiro (Sep 04 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133336022):
<p>or prove that the derivative of <code>x^2</code> is <code>2x</code> and then prove <code>2*1=2</code></p>

#### [ Kenny Lau (Sep 04 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133336364):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">test</span> <span class="o">:</span> <span class="n">has_complex_derivative_at</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">z</span><span class="o">,</span> <span class="n">z</span><span class="err">^</span><span class="mi">2</span><span class="o">)</span> <span class="mi">2</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="n">tendsto_nhds_of_metric</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">ε</span> <span class="n">hε</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">ε</span><span class="o">,</span> <span class="n">hε</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">z</span> <span class="n">hz</span><span class="o">,</span>
<span class="k">if</span> <span class="n">h</span> <span class="o">:</span> <span class="n">z</span> <span class="bp">=</span> <span class="mi">0</span> <span class="k">then</span> <span class="k">by</span> <span class="n">simpa</span> <span class="o">[</span><span class="n">h</span><span class="o">]</span> <span class="k">else</span> <span class="n">trans_rel_right</span> <span class="bp">_</span>
<span class="o">(</span><span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">dist</span><span class="o">,</span> <span class="n">pow_two</span><span class="o">,</span> <span class="n">add_mul_self_eq</span><span class="o">,</span> <span class="n">mul_div_cancel</span> <span class="bp">_</span> <span class="n">h</span><span class="o">,</span> <span class="bp">-</span><span class="n">complex</span><span class="bp">.</span><span class="n">abs_div</span><span class="o">])</span> <span class="n">hz</span><span class="bp">⟩</span>
</pre></div>

#### [ Kenny Lau (Sep 04 2018 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133336621):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">test</span> <span class="o">:</span> <span class="n">has_complex_derivative_at</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">z</span><span class="o">,</span> <span class="n">z</span><span class="err">^</span><span class="mi">2</span><span class="o">)</span> <span class="mi">2</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="n">tendsto_nhds_of_metric</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">ε</span> <span class="n">hε</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">ε</span><span class="o">,</span> <span class="n">hε</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">z</span> <span class="n">hz</span><span class="o">,</span>
<span class="k">if</span> <span class="n">h</span> <span class="o">:</span> <span class="n">z</span> <span class="bp">=</span> <span class="mi">0</span> <span class="k">then</span> <span class="k">by</span> <span class="n">simpa</span> <span class="o">[</span><span class="n">h</span><span class="o">]</span> <span class="k">else</span> <span class="k">by</span> <span class="n">dsimp</span><span class="bp">;</span> <span class="n">rw</span> <span class="o">[</span><span class="n">pow_two</span><span class="o">]</span><span class="bp">;</span>
<span class="k">by</span> <span class="n">simpa</span> <span class="o">[</span><span class="n">dist</span><span class="o">,</span> <span class="n">add_mul_self_eq</span><span class="o">,</span> <span class="n">mul_div_cancel</span> <span class="bp">_</span> <span class="n">h</span><span class="o">,</span> <span class="bp">-</span><span class="n">complex</span><span class="bp">.</span><span class="n">abs_div</span><span class="o">]</span> <span class="kn">using</span> <span class="n">hz</span><span class="bp">⟩</span>
</pre></div>

#### [ Kenny Lau (Sep 04 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133337102):
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">test</span> <span class="o">:</span> <span class="n">has_complex_derivative_at</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">z</span><span class="o">,</span> <span class="n">z</span><span class="err">^</span><span class="mi">2</span><span class="o">)</span> <span class="mi">2</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="n">tendsto_nhds_of_metric</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">ε</span> <span class="n">hε</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">ε</span><span class="o">,</span> <span class="n">hε</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">z</span> <span class="n">hz</span><span class="o">,</span>
<span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">pow_two</span><span class="o">,</span> <span class="n">add_mul_self_eq</span><span class="o">,</span> <span class="n">dist</span><span class="o">,</span> <span class="bp">-</span><span class="n">complex</span><span class="bp">.</span><span class="n">abs_div</span><span class="o">]</span> <span class="n">at</span> <span class="bp">*;</span>
<span class="n">by_cases</span> <span class="n">h</span> <span class="o">:</span> <span class="n">z</span> <span class="bp">=</span> <span class="mi">0</span><span class="bp">;</span> <span class="o">[</span><span class="n">simpa</span> <span class="o">[</span><span class="n">h</span><span class="o">],</span> <span class="n">rwa</span> <span class="n">mul_div_cancel</span> <span class="bp">_</span> <span class="n">h</span><span class="o">]</span><span class="bp">⟩</span>
</pre></div>

#### [ Kevin Buzzard (Sep 04 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133338281):
<p>one of those proofs actually conformed to the guidelines!</p>

#### [ Kevin Buzzard (Sep 04 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133338317):
<p>I don't understand the last one. What is this <code>[simpa [h], rwa mul_div_cancel _ h]</code>?</p>

#### [ Kevin Buzzard (Sep 04 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133338330):
<p>I mean, why is there a list of tactics?</p>

#### [ Kenny Lau (Sep 04 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133338383):
<p>because there are two goals</p>

#### [ Kevin Buzzard (Sep 04 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133338398):
<p>oh! The n'th term in the list acts on the n'th goal?</p>

#### [ Kevin Buzzard (Sep 04 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133338498):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">p</span> <span class="n">q</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">hp</span> <span class="o">:</span> <span class="n">p</span><span class="o">)</span> <span class="o">(</span><span class="n">hq</span> <span class="o">:</span> <span class="n">q</span><span class="o">)</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">∧</span> <span class="n">q</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">split</span><span class="bp">;</span><span class="o">[</span><span class="n">exact</span> <span class="n">hp</span><span class="o">,</span><span class="n">exact</span> <span class="n">hq</span><span class="o">]</span>
<span class="kn">end</span>
</pre></div>


<p>woo!</p>

#### [ Sebastien Gouezel (Sep 05 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133359026):
<p>If you want to define differentiability in a rather broad setting, you certainly want it to contain differentiability on the left and on the right for 1-dimensional functions, and differentiability on manifolds with boundaries. The best setting for this is probably differentiability in the sense of Whitney, i.e., <code>f</code> is differentiable at <code>x</code> on <code>S</code> if there is a linear operator such that <code>f(y)-f(x) -L (y-x)/ ||y-x||</code> tends to <code>0</code> when <code>y</code>tends to <code>x</code>while remaining in <code>S</code>. This is certainly easy to define if you have a filter like <code>nhbds_within</code> (defined using <code>nhbds x</code> and <code>principal S</code> and the good filter operation (I never know in which direction they go)). This filter would also be useful to define continuity within <code>S</code>, as far as I can tell this is not in Lean?. </p>
<p>With the big warning that the differential is not unique in general, if the tangent directions of <code>S</code> at <code>x</code> do not span the whole subspace. For uniquenss statement, you would probably want that <code>S</code> is a neighborhood of <code>x</code>, say.</p>

#### [ Johannes Hölzl (Sep 05 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20again/near/133359631):
<p>the good filter operation is infimum: <code>nhds_within a s := nhds a ⊓ principal s</code></p>


{% endraw %}
