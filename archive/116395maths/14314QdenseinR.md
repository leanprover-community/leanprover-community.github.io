---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/14314QdenseinR.html
---

## Stream: [maths](index.html)
### Topic: [Q dense in R](14314QdenseinR.html)

---


{% raw %}
#### [ Kevin Buzzard (Dec 28 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Q%20dense%20in%20R/near/152627608):
<p><code>theorem rationals_dense (x y : ℝ) (H : x &lt; y) : ∃ q : ℚ, x &lt; q ∧ (q : ℝ) &lt; y :=</code> Where is this now? I think it was explicitly there before the reals were refactored. Now there is <code>dense_embedding_of_rat</code> but then I have to work to get the statement I want.</p>

#### [ Reid Barton (Dec 28 2018 at 01:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Q%20dense%20in%20R/near/152627809):
<p><code>algebra.archimedean</code> has some similar things</p>

#### [ Mario Carneiro (Dec 28 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Q%20dense%20in%20R/near/152634813):
<p>the rationals are archimedean, so <code>exists_rat_btwn</code> will work. Also the rationals are dense, so <code>dense</code> will work</p>

#### [ Mario Carneiro (Dec 28 2018 at 05:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Q%20dense%20in%20R/near/152634858):
<p>oh wait that last one is just rationals between rationals, with no casting</p>

#### [ Kevin Buzzard (Dec 28 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Q%20dense%20in%20R/near/152655840):
<p>Aah, thanks to both of you. I'm looking in the wrong places. That was silly of me -- I even lectured this term on the fact that unboundedness of Z in R implied this fact.</p>

#### [ Kevin Buzzard (Dec 28 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Q%20dense%20in%20R/near/152666498):
<p>I want the coercion from Q to R to be different somehow. Look at this question the first years will be asked next term: "Let <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>S</mi></mrow><annotation encoding="application/x-tex">S</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.05764em;">S</span></span></span></span> be a non-empty bounded above set of reals. True or false: if <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>S</mi><mo>⊆</mo><mrow><mi mathvariant="double-struck">Q</mi></mrow></mrow><annotation encoding="application/x-tex">S\subseteq\mathbb{Q}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68889em;"></span><span class="strut bottom" style="height:0.85556em;vertical-align:-0.16667em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.05764em;">S</span><span class="mrel">⊆</span><span class="mord"><span class="mord mathbb">Q</span></span></span></span></span> then <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>s</mi><mi>u</mi><mi>p</mi><mo>(</mo><mi>S</mi><mo>)</mo><mo>∈</mo><mrow><mi mathvariant="double-struck">Q</mi></mrow></mrow><annotation encoding="application/x-tex">sup(S)\in\mathbb{Q}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit">s</span><span class="mord mathit">u</span><span class="mord mathit">p</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.05764em;">S</span><span class="mclose">)</span><span class="mrel">∈</span><span class="mord"><span class="mord mathbb">Q</span></span></span></span></span>. How do I make the Lean formalisation of this question less ugly? [added later: this is just one part of a multi-part question about a non-empty bounded-above set of reals <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>S</mi></mrow><annotation encoding="application/x-tex">S</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.05764em;">S</span></span></span></span> so we don't really want to change the definition of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>S</mi></mrow><annotation encoding="application/x-tex">S</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.05764em;">S</span></span></span></span> itself]</p>

#### [ Kevin Buzzard (Dec 28 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Q%20dense%20in%20R/near/152666549):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>

<span class="c1">-- structure or class?</span>
<span class="kn">structure</span> <span class="n">real</span><span class="bp">.</span><span class="n">rat1</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">q</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">)</span>
<span class="o">(</span><span class="n">pf</span> <span class="o">:</span> <span class="n">r</span> <span class="bp">=</span> <span class="err">↑</span><span class="n">q</span><span class="o">)</span>

<span class="kn">definition</span> <span class="n">real</span><span class="bp">.</span><span class="n">rat2</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">∃</span> <span class="n">q</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">,</span> <span class="n">r</span> <span class="bp">=</span> <span class="n">q</span>
</pre></div>


<p>Are these functions in Lean already? What are they / should they be called?</p>

#### [ Mario Carneiro (Dec 28 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Q%20dense%20in%20R/near/152672823):
<p>As usual, this is nonidiomatic lean and so it's less than nice to say. It is equivalent to talk about the supremum of a family <code>f : I -&gt; Q</code></p>

#### [ Mario Carneiro (Dec 28 2018 at 21:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Q%20dense%20in%20R/near/152672849):
<p>alternatively, you can let <code>S : set Q</code> and have its interpretation in <code>R</code> be <code>(coe '' S)</code></p>

#### [ Mario Carneiro (Dec 28 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Q%20dense%20in%20R/near/152672917):
<p>alternatively <code>S : set R</code> and <code>S \sub range coe</code></p>

#### [ Kevin Buzzard (Dec 28 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Q%20dense%20in%20R/near/152672923):
<p>Oh that's better</p>

#### [ Mario Carneiro (Dec 28 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Q%20dense%20in%20R/near/152672949):
<p>if I wasn't constrained by aiming for a direct translation I would certainly go for the first option</p>

#### [ Mario Carneiro (Dec 28 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Q%20dense%20in%20R/near/152673077):
<p>I think we could define <code>real.rats, real.nats : set R</code> in the obvious way and use that</p>

#### [ Kevin Buzzard (Dec 28 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Q%20dense%20in%20R/near/152675391):
<p>and now I have to reprove things like <code>real.rats x -&gt; real.rats y -&gt; real.rats (x + y)</code>?</p>

#### [ Kevin Buzzard (Dec 28 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Q%20dense%20in%20R/near/152675592):
<p>I am not 100% clear on what needs proving actually. There's a lemma which says that + on Q and R coincide, and that's kind of why I need to prove the thing above. But there's another lemma which says that &lt; on Q and R coincide, and that doesn't seem to correspond to something I need to prove here.</p>

#### [ Mario Carneiro (Dec 29 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Q%20dense%20in%20R/near/152696668):
<p>well, it's a set so you would want to write that <code>x \in rats -&gt; y \in rats -&gt; x + y \in rats</code>, but yes, and it follows from <code>rat.cast_add</code></p>

#### [ Mario Carneiro (Dec 29 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Q%20dense%20in%20R/near/152696679):
<p>and you are right, there isn't really an analogue for <code>rat.cast_le</code></p>

#### [ Mario Carneiro (Dec 29 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Q%20dense%20in%20R/near/152696719):
<p>it's just the set of rational numbers, as a subset of R</p>

#### [ Mario Carneiro (Dec 29 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Q%20dense%20in%20R/near/152696720):
<p>all the operations are real operations</p>

#### [ Mario Carneiro (Dec 29 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Q%20dense%20in%20R/near/152696726):
<p>you can do many things with such a set, the idea is when you need a set and not a type. For example <code>closure rats = univ</code> is hard to state otherwise</p>

#### [ Chris Hughes (Dec 29 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Q%20dense%20in%20R/near/152699297):
<p>(deleted)</p>


{% endraw %}
