---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/10715analysisrefactor.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [analysis refactor](https://leanprover-community.github.io/archive/116395maths/10715analysisrefactor.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Aug 21 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132541838):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> If you have some time, I'd be interested to know what is the big plan underlying your recent mathilb commits</p>

#### [ Johannes Hölzl (Aug 21 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132541914):
<p>Cleanup ennreal, and enhance nnreal. Change metrics and norms to nnreal.</p>

#### [ Johannes Hölzl (Aug 21 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132541930):
<p>Another idea is to use Galois connections as cheap categorical constructions</p>

#### [ Patrick Massot (Aug 21 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132541949):
<p>Didn't <span class="user-mention" data-user-id="110050">@Sebastien Gouezel</span> make a convincing point of not doing that?</p>

#### [ Patrick Massot (Aug 21 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132541963):
<p>Where do you want to add Galois connections?</p>

#### [ Johannes Hölzl (Aug 21 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132542035):
<p>Galois connections are already there. I "lift" along the <code>generate</code> / <code>sets</code> Galois connection (<code>generate g</code> produces the smallest filter/topology/measurable sets containing <code>g</code>, <code>sets</code> is the forgetful functor).</p>

#### [ Johannes Hölzl (Aug 21 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132542085):
<p>This allows me to lift the complete lattice structure on <code>set</code> to topologies, filters, and measurable spaces. They were there before, but now we have a nicer construction.</p>

#### [ Johannes Hölzl (Aug 21 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132542099):
<p>For <code>nnreal</code> I need to look at Sebastians argument again.</p>

#### [ Patrick Massot (Aug 21 2018 at 23:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132542120):
<p>I know Galois connections are already there, I used filters quite a lot. I as asking about new uses.</p>

#### [ Patrick Massot (Aug 21 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132542201):
<p>(and I think I like the answer)</p>

#### [ Johannes Hölzl (Aug 21 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132542485):
<p>I need to look at Sebastians argument more concretely. <code>dist</code> and <code>norm</code> will always return nonnegative numbers. So the difference is only that we pack this proof into the result type.  Subtracting on <code>nnreal</code> and <code>ennreal</code> is very ugly, but I don't see how this appears in a concrete case.</p>

#### [ Patrick Massot (Aug 21 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132542604):
<p>From <a href="https://github.com/leanprover/mathlib/pull/208#issuecomment-406893134" target="_blank" title="https://github.com/leanprover/mathlib/pull/208#issuecomment-406893134">https://github.com/leanprover/mathlib/pull/208#issuecomment-406893134</a> it's not hard to see where Sébastien encountered that</p>

#### [ Patrick Massot (Aug 21 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132542614):
<p><a href="https://devel.isa-afp.org/entries/Gromov_Hyperbolicity.html" target="_blank" title="https://devel.isa-afp.org/entries/Gromov_Hyperbolicity.html">https://devel.isa-afp.org/entries/Gromov_Hyperbolicity.html</a></p>

#### [ Reid Barton (Aug 21 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132542880):
<blockquote>
<p><code>abs(dist e a - dist e b)</code></p>
</blockquote>
<p>But surely <code>nnreal</code> is a metric space too? Why not just write <code>dist (dist e a) (dist e b)</code>?</p>

#### [ Reid Barton (Aug 21 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132542975):
<p>More generally, faced with a problem of the form "I have to do X a lot", maybe it's better to write a small convenience function to do X rather than distorting the underlying theory to avoid needing to do X.</p>

#### [ Patrick Massot (Aug 21 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132543209):
<p>Maybe "distorting the underlying theory" is a bit exaggerated here. But really I have no idea about what should be done. I can only see that Sébastien did quite a lot of Gromov hyperbolic spaces in Isabelle, so this is a really concrete and battle tested opinion.</p>

#### [ Reid Barton (Aug 21 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132543288):
<p>Fair enough. In this case, it's not uncommon to see <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>d</mi><mo>(</mo><mi>x</mi><mo separator="true">,</mo><mi>y</mi><mo>)</mo><mo>≥</mo><mn>0</mn></mrow><annotation encoding="application/x-tex">d(x, y) \ge 0</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit">d</span><span class="mopen">(</span><span class="mord mathit">x</span><span class="mpunct">,</span><span class="mord mathit" style="margin-right:0.03588em;">y</span><span class="mclose">)</span><span class="mrel">≥</span><span class="mord mathrm">0</span></span></span></span> stated as an axiom of a metric space</p>

#### [ Mario Carneiro (Aug 22 2018 at 00:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132544270):
<p>It's also not uncommon to see <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>d</mi><mo>:</mo><mi>X</mi><mo>×</mo><mi>X</mi><mo>→</mo><mo>[</mo><mn>0</mn><mo separator="true">,</mo><mi mathvariant="normal">∞</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">d:X\times X\to[0,\infty)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit">d</span><span class="mrel">:</span><span class="mord mathit" style="margin-right:0.07847em;">X</span><span class="mbin">×</span><span class="mord mathit" style="margin-right:0.07847em;">X</span><span class="mrel">→</span><span class="mopen">[</span><span class="mord mathrm">0</span><span class="mpunct">,</span><span class="mord mathrm">∞</span><span class="mclose">)</span></span></span></span>. Honestly I don't think mathematicians have a mental structure that allows them to even distinguish these approaches, so I don't consider this good evidence in either direction</p>

#### [ Reid Barton (Aug 22 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132544931):
<p>I wonder whether it would help to have <code>has_sub a b</code> with <code>sub : a -&gt; a -&gt; b</code> with instances like <code>nat int</code> and <code>nnreal real</code></p>

#### [ Reid Barton (Aug 22 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132544936):
<p>Or an affine space / vector space</p>

#### [ Mario Carneiro (Aug 22 2018 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132544944):
<p>You can always write <code>(a - b : int)</code> where <code>a b : nat</code></p>

#### [ Mario Carneiro (Aug 22 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132544950):
<p>same for <code>nnreal</code> and <code>real</code></p>

#### [ Mario Carneiro (Aug 22 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132544960):
<p>indeed this is what I recommend if you want proper subtraction on one of these partial subtraction domains</p>

#### [ Sebastien Gouezel (Aug 22 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132564296):
<p>The most basic object in hyperbolic spaces is the Gromov product of two points <code>x</code>and <code>y</code> with basepoint <code>e</code>, defined as <code>(d(e, x) + d(e, y) - d(x,y))/2</code>. And one keeps computing with such objects, adding, subtracting or comparing them. All these computations are really much more convenient in reals than nnreals, although I guess they could most of the time be done in nnreals, at the price of making the proofs much more painful (for instance, in the definition of the Gromov product, the triangular inequality shows that <code>d(x, y) ≤ d(e,x) + d(e,y)</code>, so that the definition in reals or nnreals gives the same result, at least if one parenthesises the expression correctly). <br>
In fact, at the beginning I defined the Gromov product to be in <code>nnreal</code>, but later on I had to refactor everything as it made things uselessly complicated.</p>
<p>For the general issue, making distances and norms take values in <code>nnreal</code> would mathematically be the right thing to do. But I am not convinced that the benefits outweigh the difficulties in applications. As a middle ground, one could have two functions <code>nndist</code> and <code>dist</code>. Another related question is to have distances even taking values in <code>ennreal</code>. I think this is important to have, for instance to define the graph distance on a non-connected graph, or the <code>L^2</code> norm of a function which is not square-integrable (these are two real-life problems that I met in Isabelle and where I was stuck with the current hierarchy). Maybe a class <code>emetric_space</code> with distances taking values in <code>ennreal</code> (this is enough to define for instance a uniform structure, a topology, and so on), and a subclass <code>metric_space</code> in which the distance only takes finite values?</p>

#### [ Reid Barton (Aug 22 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132581506):
<p>Thanks for the more detailed example. Having both <code>nndist</code> and <code>dist</code> is a good option, in which case it may not even matter which of <code>dist</code> or <code>nndist</code> is taken to be part of the defining structure of a metric space. The potential cost is wanting two versions of all the lemmas about <code>nndist</code>/<code>dist</code>, but this kind of problem I feel could be solvable in the long run with better tools.</p>

#### [ Reid Barton (Aug 22 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/analysis%20refactor/near/132581576):
<p>Also totally agree with your second paragraph. An even more basic example is the extended metric space of (not necessarily bounded) functions from a given set to a given metric space, with the sup/uniform metric.</p>


{% endraw %}
