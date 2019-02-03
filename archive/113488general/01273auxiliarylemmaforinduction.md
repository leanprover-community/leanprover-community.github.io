---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/01273auxiliarylemmaforinduction.html
---

## Stream: [general](index.html)
### Topic: [auxiliary lemma for induction](01273auxiliarylemmaforinduction.html)

---


{% raw %}
#### [ Kevin Buzzard (Aug 23 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auxiliary%20lemma%20for%20induction/near/132633649):
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">foo</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">size</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span>

<span class="kn">definition</span> <span class="n">auxiliary_thing</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">foo</span> <span class="bp">→</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">)</span> <span class="o">(</span><span class="n">m</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span>
<span class="o">(</span><span class="n">H0</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span> <span class="o">:</span> <span class="n">foo</span><span class="o">,</span> <span class="n">x</span><span class="bp">.</span><span class="n">size</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">→</span> <span class="n">p</span> <span class="n">x</span><span class="o">)</span>
<span class="o">(</span><span class="n">Hsucc</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span>
  <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span> <span class="o">:</span> <span class="n">foo</span><span class="o">,</span> <span class="n">x</span><span class="bp">.</span><span class="n">size</span> <span class="bp">=</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">p</span> <span class="n">x</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span> <span class="o">:</span> <span class="n">foo</span><span class="o">,</span> <span class="n">x</span><span class="bp">.</span><span class="n">size</span> <span class="bp">=</span> <span class="n">n</span><span class="bp">+</span><span class="mi">1</span> <span class="bp">→</span> <span class="n">p</span> <span class="n">x</span><span class="o">))</span> <span class="o">:</span>
<span class="bp">∀</span> <span class="n">x</span> <span class="o">:</span> <span class="n">foo</span><span class="o">,</span> <span class="n">x</span><span class="bp">.</span><span class="n">size</span> <span class="bp">=</span> <span class="n">m</span> <span class="bp">→</span> <span class="n">p</span> <span class="n">x</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">induction</span> <span class="n">m</span> <span class="k">with</span> <span class="n">n</span> <span class="n">Hn</span><span class="o">,</span>
    <span class="n">exact</span> <span class="n">H0</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">Hsucc</span> <span class="n">n</span> <span class="n">Hn</span><span class="o">,</span>
<span class="kn">end</span>

<span class="c">/-</span><span class="cm"> What I actually want -/</span>
<span class="kn">definition</span> <span class="n">foo</span><span class="bp">.</span><span class="n">recurse_on_size</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">foo</span> <span class="bp">→</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">)</span>
<span class="o">(</span><span class="n">H0</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span> <span class="o">:</span> <span class="n">foo</span><span class="o">,</span> <span class="n">x</span><span class="bp">.</span><span class="n">size</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">→</span> <span class="n">p</span> <span class="n">x</span><span class="o">)</span>
<span class="o">(</span><span class="n">Hsucc</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span>
  <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span> <span class="o">:</span> <span class="n">foo</span><span class="o">,</span> <span class="n">x</span><span class="bp">.</span><span class="n">size</span> <span class="bp">=</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">p</span> <span class="n">x</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span> <span class="o">:</span> <span class="n">foo</span><span class="o">,</span> <span class="n">x</span><span class="bp">.</span><span class="n">size</span> <span class="bp">=</span> <span class="n">n</span><span class="bp">+</span><span class="mi">1</span> <span class="bp">→</span> <span class="n">p</span> <span class="n">x</span><span class="o">))</span> <span class="o">:</span>
<span class="bp">∀</span> <span class="n">x</span> <span class="o">:</span> <span class="n">foo</span><span class="o">,</span> <span class="n">p</span> <span class="n">x</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">intro</span> <span class="n">x</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">auxiliary_thing</span> <span class="n">p</span> <span class="o">(</span><span class="n">x</span><span class="bp">.</span><span class="n">size</span><span class="o">)</span> <span class="n">H0</span> <span class="n">Hsucc</span><span class="o">,</span>
  <span class="n">refl</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p>Is this introduction of an auxiliary lemma a sensible way to go about things, or am I better off trying to prove what I want directly using some fancy equation compiler trickery?</p>

#### [ Simon Hudon (Aug 23 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auxiliary%20lemma%20for%20induction/near/132637724):
<p>Are you using the auxiliary lemma in order to have <code>m</code> to do your induction on? Have you tried <code>generalize h : x.size = m, induction m with n Hn</code>?</p>

#### [ Kevin Buzzard (Aug 23 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auxiliary%20lemma%20for%20induction/near/132638452):
<p>Aah that's the trick. Thanks Simon!</p>

#### [ Simon Hudon (Aug 23 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auxiliary%20lemma%20for%20induction/near/132639057):
<p>Any time :)</p>

#### [ Simon Hudon (Aug 23 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/auxiliary%20lemma%20for%20induction/near/132639260):
<p>I wonder if it would be worth combining the two tactics so that <code>induction e</code> (with <code>e</code> an arbitrary expression) would produce the equality assumption.</p>


{% endraw %}
