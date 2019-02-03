---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/60294LogicinLEAN.html
---

## Stream: [new members](index.html)
### Topic: [Logic in LEAN](60294LogicinLEAN.html)

---


{% raw %}
#### [ Sean G McCain (Nov 01 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Logic%20in%20LEAN/near/136955882):
<p>Is someone able to send me a private message regarding first order logic in LEAN? I am working a homework that requires it and it is difficult, for LEAN is very new to me.</p>

#### [ Bryan Gin-ge Chen (Nov 02 2018 at 00:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Logic%20in%20LEAN/near/136956419):
<p>If you have specific questions you should feel free to ask them (publicly) in this thread. Have you seen the relevant chapters of <a href="http://avigad.github.io/logic_and_proof/first_order_logic.html" target="_blank" title="http://avigad.github.io/logic_and_proof/first_order_logic.html">Logic &amp; Proof</a>?</p>

#### [ Sean G McCain (Nov 02 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Logic%20in%20LEAN/near/136956754):
<p>I have seen them, and that is the book that I use for reference. However, I am yet to be able to figure out the issue.</p>

#### [ Sean G McCain (Nov 02 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Logic%20in%20LEAN/near/136956856):
<p>Here is the code I have: <br>
I am needing to prove the statement following example:</p>
<p>section<br>
         variable U : Type<br>
         variables A B : U → Prop</p>
<div class="codehilite"><pre><span></span>     example : (∀ x, A x ∧ B x) → ∀ x, A x :=
     assume (x : U),
     assume h1 :∀ x, A x ∧ B x,
     assume h2 : ∀ x, A x,
     assume y,
     have hy : A y, from h2 y,
     show ∀ y, A y, from h2 y (hy) 
   end
</pre></div>


<p>Here is the error  I am getting:  <br>
However, A y is a function, so I dont understand this error. </p>
<p>function expected at<br>
  h2 y<br>
term has type<br>
  A y</p>

#### [ Chris Hughes (Nov 02 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Logic%20in%20LEAN/near/136956965):
<p><code>A y</code> is not a function, it's a <code>Prop</code>.</p>

#### [ Chris Hughes (Nov 02 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Logic%20in%20LEAN/near/136956985):
<p><code>A</code> is a function.</p>

#### [ Sean G McCain (Nov 02 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Logic%20in%20LEAN/near/136957170):
<p>So, what would need to follow the 'from'</p>

#### [ Bryan Gin-ge Chen (Nov 02 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Logic%20in%20LEAN/near/136957338):
<p>I would reconsider the strategy for proving this. In particular, your <code>assume</code> statements are out-of-order / some of them are unnecessary.</p>

#### [ Bryan Gin-ge Chen (Nov 02 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Logic%20in%20LEAN/near/136957526):
<p>As a hint, <code>assume h1:∀ x, A x ∧ B x</code> should come first, and then <code>assume x:U</code>. You can see this by breaking down what you're trying to prove from left to right. Remember that you can use an underscore <code>_</code> and lean will tell you the type of what you're still missing.</p>

#### [ Sean G McCain (Nov 02 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Logic%20in%20LEAN/near/136958036):
<p>After doing so, I am given more errors than before.</p>

#### [ Andrew Ashworth (Nov 02 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Logic%20in%20LEAN/near/136958542):
<p>add more underscores, the compiler will tell you what you're doing wrong</p>

#### [ Bryan Gin-ge Chen (Nov 02 2018 at 00:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Logic%20in%20LEAN/near/136958565):
<p>Maybe this will help. Let me go through the last example from section 9.2 of Logic &amp; Proof which is very similar. </p>
<p>Let's start by just putting an underscore in for the entire proof:</p>
<div class="codehilite"><pre><span></span><span class="kn">variable</span> <span class="n">U</span> <span class="o">:</span> <span class="kt">Type</span>
<span class="kn">variables</span> <span class="n">A</span> <span class="n">B</span> <span class="o">:</span> <span class="n">U</span> <span class="bp">→</span> <span class="kt">Prop</span>

<span class="kn">example</span> <span class="o">:</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">A</span> <span class="n">x</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">B</span> <span class="n">x</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">A</span> <span class="n">x</span> <span class="bp">∧</span> <span class="n">B</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">_</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">don&#39;t know how to synthesize placeholder</span>
<span class="cm">context:</span>
<span class="cm">U : Type,</span>
<span class="cm">A B : U → Prop</span>
<span class="cm">⊢ (∀ (x : U), A x) → (∀ (x : U), B x) → ∀ (x : U), A x ∧ B x</span>
<span class="cm">-/</span>
</pre></div>


<p>No surprise here, lean just restates the goal for us. We see from the arrows in the goal that it is a function. To construct a function we should begin by assuming things:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">A</span> <span class="n">x</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">B</span> <span class="n">x</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">A</span> <span class="n">x</span> <span class="bp">∧</span> <span class="n">B</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span>
<span class="kn">example</span> <span class="o">:</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">A</span> <span class="n">x</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">B</span> <span class="n">x</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">A</span> <span class="n">x</span> <span class="bp">∧</span> <span class="n">B</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">assume</span> <span class="n">hA</span><span class="o">,</span>
<span class="bp">_</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">don&#39;t know how to synthesize placeholder</span>
<span class="cm">context:</span>
<span class="cm">U : Type,</span>
<span class="cm">A B : U → Prop,</span>
<span class="cm">hA : ∀ (x : U), A x</span>
<span class="cm">⊢ (∀ (x : U), B x) → ∀ (x : U), A x ∧ B x</span>
<span class="cm">-/</span>
</pre></div>


<p>There's still an error, but we see that it's telling us that we're making progress. Indeed, lean actually has inferred the right type for <code>hA</code>, which we can put back in if we want to be fully explicit. The goal is still a function so we continue assuming:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">A</span> <span class="n">x</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">B</span> <span class="n">x</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">A</span> <span class="n">x</span> <span class="bp">∧</span> <span class="n">B</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">assume</span> <span class="n">hA</span> <span class="o">:</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">A</span> <span class="n">x</span><span class="o">),</span>
<span class="k">assume</span> <span class="n">hB</span><span class="o">,</span>
<span class="bp">_</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">don&#39;t know how to synthesize placeholder</span>
<span class="cm">context:</span>
<span class="cm">U : Type,</span>
<span class="cm">A B : U → Prop,</span>
<span class="cm">hA : ∀ (x : U), A x,</span>
<span class="cm">hB : ∀ (x : U), B x</span>
<span class="cm">⊢ ∀ (x : U), A x ∧ B x</span>
<span class="cm">-/</span>
</pre></div>


<p>So that's what <code>hB</code> is. We still have a function (the goal depends on a bound variable) so let's try assuming one more time:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">A</span> <span class="n">x</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">B</span> <span class="n">x</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">A</span> <span class="n">x</span> <span class="bp">∧</span> <span class="n">B</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">assume</span> <span class="n">hA</span><span class="o">:</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">A</span> <span class="n">x</span><span class="o">)</span> <span class="o">,</span>
<span class="k">assume</span> <span class="n">hB</span><span class="o">:</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">B</span> <span class="n">x</span><span class="o">),</span>
<span class="k">assume</span> <span class="n">y</span><span class="o">,</span>
<span class="bp">_</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">don&#39;t know how to synthesize placeholder</span>
<span class="cm">context:</span>
<span class="cm">U : Type,</span>
<span class="cm">A B : U → Prop,</span>
<span class="cm">hA : ∀ (x : U), A x,</span>
<span class="cm">hB : ∀ (x : U), B x,</span>
<span class="cm">y : U</span>
<span class="cm">⊢ A y ∧ B y</span>
<span class="cm">-/</span>
</pre></div>


<p>Now we're in a place where we have a term that we can construct by applying hA and hB. The final answer:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">A</span> <span class="n">x</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">B</span> <span class="n">x</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">A</span> <span class="n">x</span> <span class="bp">∧</span> <span class="n">B</span> <span class="n">x</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">assume</span> <span class="n">hA</span><span class="o">,</span>
<span class="k">assume</span> <span class="n">hB</span><span class="o">,</span>
<span class="k">assume</span> <span class="n">y</span><span class="o">,</span>
<span class="bp">⟨</span><span class="n">hA</span> <span class="n">y</span><span class="o">,</span> <span class="n">hB</span> <span class="n">y</span><span class="bp">⟩</span>
</pre></div>


<p>Which is equivalent to the proof given in the book. </p>
<p>To summarize, if you look carefully at the type errors you get, they may help guide you to the proof you're looking for.</p>


{% endraw %}
