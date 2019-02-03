---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/39702euclideandomains.html
---

## Stream: [maths](index.html)
### Topic: [euclidean domains](39702euclideandomains.html)

---


{% raw %}
#### [ Johan Commelin (Jul 20 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domains/near/129982059):
<p>Currently, the definition of a Euclidean domain has the field</p>
<div class="codehilite"><pre><span></span><span class="o">(</span><span class="n">val_remainder_lt</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="o">{</span><span class="n">b</span><span class="o">},</span> <span class="n">b</span> <span class="bp">≠</span> <span class="mi">0</span> <span class="bp">→</span> <span class="n">valuation</span> <span class="o">(</span><span class="n">remainder</span> <span class="n">a</span> <span class="n">b</span><span class="o">)</span> <span class="bp">&lt;</span> <span class="n">valuation</span> <span class="n">b</span><span class="o">)</span>
</pre></div>


<p>I think it should read</p>
<div class="codehilite"><pre><span></span><span class="o">(</span><span class="n">val_remainder_lt</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="o">{</span><span class="n">b</span><span class="o">},</span> <span class="n">b</span> <span class="bp">≠</span> <span class="mi">0</span> <span class="bp">→</span> <span class="o">(</span><span class="n">remainder</span> <span class="n">a</span> <span class="n">b</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">∨</span> <span class="n">valuation</span> <span class="o">(</span><span class="n">remainder</span> <span class="n">a</span> <span class="n">b</span><span class="o">)</span> <span class="bp">&lt;</span> <span class="n">valuation</span> <span class="n">b</span><span class="o">))</span>
</pre></div>


<p>or something like that. What is best in these cases:<br>
(i) the change as I suggest, or<br>
(ii) move the claim <code>remainder a b = 0</code> to a condition, so <code>b \ne 0 \and remainder a b \ne 0 \to ...</code></p>

#### [ Chris Hughes (Jul 20 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domains/near/129982412):
<p>My plan when I wrote polynomials, was that it should take a well founded relation instead of a valuation. <code>mod_lt</code> would be <code>r (remainder a b) b</code> and <code>val_me_mul_left</code> would be <code>not r (a * b) a</code> I think. <code>degree</code> now returns <code>with_bot nat</code> so it meets this definition.</p>

#### [ Chris Hughes (Jul 20 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domains/near/129982687):
<p>The trouble with your definition is it makes every proof and definition longer. For example gcd needs an extra <code>else if</code>.</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">gcd</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span>
<span class="bp">|</span> <span class="n">a</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">b</span><span class="o">,</span> <span class="k">if</span> <span class="n">a0</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">=</span> <span class="mi">0</span> <span class="k">then</span> <span class="n">b</span>
 <span class="k">else</span> <span class="k">if</span> <span class="n">hba</span> <span class="o">:</span> <span class="n">remainder</span> <span class="n">b</span> <span class="n">a</span> <span class="bp">=</span> <span class="mi">0</span> <span class="k">then</span> <span class="n">a</span>
 <span class="k">else</span>
  <span class="k">have</span> <span class="n">h</span><span class="o">:</span><span class="bp">_</span> <span class="o">:=</span> <span class="n">or</span><span class="bp">.</span><span class="n">resolve_left</span> <span class="o">(</span><span class="n">val_mod_lt&#39;</span> <span class="n">b</span> <span class="n">a0</span><span class="o">)</span> <span class="n">hba</span><span class="o">,</span>
  <span class="n">gcd</span> <span class="o">(</span><span class="n">b</span><span class="err">%</span><span class="n">a</span><span class="o">)</span> <span class="n">a</span>
<span class="n">using_well_founded</span> <span class="o">{</span><span class="n">rel_tac</span> <span class="o">:=</span>
  <span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="bp">`</span><span class="o">[</span><span class="n">exact</span> <span class="bp">⟨_</span><span class="o">,</span> <span class="n">measure_wf</span> <span class="n">valuation</span><span class="bp">⟩</span><span class="o">]}</span>
</pre></div>

#### [ Johan Commelin (Jul 20 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domains/near/129983245):
<p>On the other hand, it is the definition that every mathematician is used to...</p>

#### [ Johan Commelin (Jul 20 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domains/near/129983258):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> Do you think the <code>valuation</code> of an ED should also take values in <code>with_bot nat</code>? And then require that <code>valuation a = bot \iff a = 0</code>?</p>

#### [ Chris Hughes (Jul 20 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domains/near/129983274):
<p>That might be also be an idea, but without <code>valuation a = bot \iff a = 0</code>, because that will be annoying with integers.</p>

#### [ Chris Hughes (Jul 20 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domains/near/129983330):
<p>But even so, I think arbitrary well founded is better, because then people dealing with integers can use the relation <code>x.nat_abs &lt; y.nat_abs</code> where the use of <code>with_bot</code> would just be annoying.</p>

#### [ Johan Commelin (Jul 20 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domains/near/129987066):
<p>So, what do you suggest as definition of ED?</p>

#### [ Johan Commelin (Jul 20 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domains/near/129987081):
<p>Then we can try to use that, and also prove that it is equivalent to the "usual" definition. And possibly build a 2nd constructor that mimics the "usual" one.</p>

#### [ Chris Hughes (Jul 20 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domains/near/129992150):
<p>I just made a PR with my suggested solution. <a href="https://github.com/leanprover/mathlib/pull/211" target="_blank" title="https://github.com/leanprover/mathlib/pull/211">https://github.com/leanprover/mathlib/pull/211</a></p>

#### [ Johan Commelin (Jul 20 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domains/near/129992659):
<p>Nice! I like your speed!</p>

#### [ Johan Commelin (Jul 20 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/euclidean%20domains/near/129996118):
<p>Cool, you add an instance for <code>int</code>!</p>


{% endraw %}
