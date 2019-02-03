---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/24156483polarcoordinates.html
---

## Stream: [PR reviews](https://leanprover-community.github.io/archive/144837PRreviews/index.html)
### Topic: [#483 polar coordinates](https://leanprover-community.github.io/archive/144837PRreviews/24156483polarcoordinates.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Nov 17 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147885598):
<p>I proved some basic stuff in my undergraduate course, e.g. using polar coordinates to prove that a non-zero complex number has exactly n n'th roots if n&gt;=1 (I am still a bit confused as to why n&gt;=1 comes up so often in maths and so rarely in computer science; maybe we count stuff more). Anyway, <span class="user-mention" data-user-id="130500">@Abhimanyu Pallavi Sudhir</span> has written up some of this stuff in Lean, including polar coordinates, which I guess didn't seem to be there before.</p>

#### [ Kevin Buzzard (Nov 17 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147885899):
<p>I guess the main thing I'm not sure about is how to put the concept of "angle" into Lean -- in maths it's the unit circle in the complexes, or <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mi mathvariant="double-struck">R</mi></mrow><mi mathvariant="normal">/</mi><mn>2</mn><mi>π</mi><mrow><mi mathvariant="double-struck">Z</mi></mrow></mrow><annotation encoding="application/x-tex">\mathbb{R}/2\pi\mathbb{Z}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord"><span class="mord mathbb">R</span></span><span class="mord mathrm">/</span><span class="mord mathrm">2</span><span class="mord mathit" style="margin-right:0.03588em;">π</span><span class="mord"><span class="mord mathbb">Z</span></span></span></span></span>, or <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>[</mo><mn>0</mn><mo separator="true">,</mo><mn>2</mn><mi>π</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">[0,2\pi)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mopen">[</span><span class="mord mathrm">0</span><span class="mpunct">,</span><span class="mord mathrm">2</span><span class="mord mathit" style="margin-right:0.03588em;">π</span><span class="mclose">)</span></span></span></span> or whatever. But there are implementation issues in Lean which I feel less confident about.</p>

#### [ Kevin Buzzard (Nov 17 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147885901):
<p>The thing you want is a map from the reals to the angles, so perhaps the quotient is best?</p>

#### [ Reid Barton (Nov 17 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147887375):
<p>Nice! It looks like complex nth roots are quite close then. With those someone could try to prove FTA.</p>

#### [ Chris Hughes (Nov 17 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147887385):
<p>Do you have a link to a proof that uses the existence of complex nth roots?</p>

#### [ Reid Barton (Nov 17 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147887425):
<p><a href="https://ncatlab.org/nlab/show/fundamental+theorem+of+algebra#classical_fta_via_advanced_calculus" target="_blank" title="https://ncatlab.org/nlab/show/fundamental+theorem+of+algebra#classical_fta_via_advanced_calculus">https://ncatlab.org/nlab/show/fundamental+theorem+of+algebra#classical_fta_via_advanced_calculus</a></p>

#### [ Chris Hughes (Nov 17 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147887436):
<p>Thaanks</p>

#### [ Reid Barton (Nov 17 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147887718):
<p>Think it looks doable?</p>

#### [ Reid Barton (Nov 17 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147887757):
<p>There are some bits having to do with estimating sums which could be a little awkward</p>

#### [ Chris Hughes (Nov 17 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147888275):
<p>I'm not sure how to do Bolzano Weirstrass, because I don't know too much about analysis in Lean, or analysis in general for that matter. I think it's stated in a different way. The rest looks doable. What are the parts about estimating sums that you thought looked difficult?</p>

#### [ Reid Barton (Nov 17 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147888549):
<p>I guess just the statement that f(z) goes to infinity as z does. I was also thinking of the last bit of (2), but that's just continuity.</p>

#### [ Chris Hughes (Nov 17 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147888552):
<p>Yeah, I didn't quite notice that bit. Probably the hardest part.</p>

#### [ Reid Barton (Nov 17 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147888558):
<p>I think paragraph 1 is easier than it sounds from the proof written out there</p>

#### [ Reid Barton (Nov 17 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147889672):
<p>Minus the part about f(z) going to infinity as z does, I mean.</p>

#### [ Reid Barton (Nov 17 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147891219):
<p>Well, it's easy modulo some more basic facts which we don't seem to have yet</p>

#### [ Reid Barton (Nov 17 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147891311):
<p>The proof I had in mind was: We want to show that |f| attains a global minimum somewhere. Pick r large enough so that |z| &gt; r implies |f(z)| &gt; |f(0)|. The ball {|z| &lt;= r} is compact (missing fact 1), so its image under |f| is a nonempty compact subset of R and therefore contains a smallest element (missing fact 2). If w is some preimage of this smallest element, then |f| is globally minimized at w, by cases on whether or not |z| &lt;= R.</p>

#### [ Kenny Lau (Nov 17 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147891331):
<p>I think we know that [0,1] is compact</p>

#### [ Kenny Lau (Nov 17 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147891333):
<p>I don't know if we have extreme value theorem</p>

#### [ Reid Barton (Nov 17 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147891385):
<p>Missing fact 1 is not really missing, it's just not stated in that exact form. I'm not sure about missing fact 2</p>

#### [ Sebastien Gouezel (Nov 17 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147891495):
<p>I have missing fact 2 somewhere.</p>

#### [ Sebastien Gouezel (Nov 17 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147891555):
<p>Maybe it is time for me to dump a PR with a lot of useful random facts...</p>

#### [ Mario Carneiro (Nov 18 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147895430):
<p>useful random facts are my favorite</p>

#### [ Sebastien Gouezel (Nov 18 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147918444):
<p>Done in #PR484. The extreme value theorem is here under the sweet name of <code>exists_forall_le_of_compact_of_continuous</code> :)</p>

#### [ Chris Hughes (Nov 18 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147929675):
<p>I mostly proved this today, apart from a few annoying, but not too difficult sorries. Is this the right statement?</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">easy_growth_lemma</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">polynomial</span> <span class="n">ℂ</span><span class="o">),</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">degree</span> <span class="n">p</span> <span class="bp">→</span>
  <span class="bp">∀</span> <span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">,</span> <span class="bp">∃</span> <span class="n">r</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">,</span> <span class="bp">∀</span> <span class="n">z</span> <span class="o">:</span> <span class="n">ℂ</span><span class="o">,</span> <span class="n">r</span> <span class="bp">&lt;</span> <span class="n">z</span><span class="bp">.</span><span class="n">abs</span> <span class="bp">→</span> <span class="n">x</span> <span class="bp">&lt;</span> <span class="o">(</span><span class="n">p</span><span class="bp">.</span><span class="kn">eval</span> <span class="n">z</span><span class="o">)</span><span class="bp">.</span><span class="n">abs</span>
</pre></div>

#### [ Chris Hughes (Nov 18 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147932354):
<p>Sorries now filled in.</p>

#### [ Kevin Buzzard (Nov 18 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147932422):
<p>You've proved polynomials are continuous at infinity. There will be a way of stating this with filters</p>

#### [ Kevin Buzzard (Nov 18 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147932475):
<p>Think of x as being the epsilon for infinity, and r as being the delta</p>

#### [ Kevin Buzzard (Nov 18 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147932484):
<p>Degree &gt; 0 is just the assumption that p sends infinity to infinity</p>

#### [ Chris Hughes (Nov 18 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147932497):
<p>Haven't I proved p sends infinity to infinity?</p>

#### [ Chris Hughes (Nov 18 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147932540):
<p>More or less. Does that mean anything rigorously?</p>

#### [ Chris Hughes (Nov 18 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147932553):
<p>I think I get what you mean actually.</p>

#### [ Chris Hughes (Nov 18 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147932607):
<p>If I extended the complex numbers with infinity, then p sends infinity to infinity, but you need continuity at infinity to prove the limit is the same as the evaluation.</p>

#### [ Kevin Buzzard (Nov 18 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147933297):
<p>Right. There's a topological space "complex numbers union infinity" with the "open balls centre infinity" being exactly infinity union these regions |z| &gt; M for M large, and polynomials, thought of as continuous maps from C to C, extend to continuous maps from this extended space to itself.</p>

#### [ Chris Hughes (Nov 18 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147933314):
<p>Is there some clever easy proof of this by just proving add mul and neg are continuous at infinity.</p>

#### [ Kevin Buzzard (Nov 18 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147933366):
<p>So this new space is called <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi mathvariant="double-struck">P</mi><mn>1</mn></msup><mo>(</mo><mrow><mi mathvariant="double-struck">C</mi></mrow><mo>)</mo></mrow><annotation encoding="application/x-tex">\mathbb{P}^1(\mathbb{C})</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8141079999999999em;"></span><span class="strut bottom" style="height:1.064108em;vertical-align:-0.25em;"></span><span class="base"><span class="mord"><span class="mord"><span class="mord mathbb">P</span></span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">1</span></span></span></span></span></span></span></span><span class="mopen">(</span><span class="mord"><span class="mord mathbb">C</span></span><span class="mclose">)</span></span></span></span>, and if you put the effort into topologising it then not only are mul and neg continuous, but so is reciprocal (it swaps infinity and 0). I don't know whether it's worth the effort doing it this way in Lean but that's typically how it's done in a Riemann Surfaces course.</p>

#### [ Kevin Buzzard (Nov 18 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147933410):
<p>Note that power series are typically not continuous at infinity, e.g. <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>sin</mi><mo>(</mo><mi>x</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">\sin(x)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mop">sin</span><span class="mopen">(</span><span class="mord mathit">x</span><span class="mclose">)</span></span></span></span> is zero for arbitrarily large real <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>x</mi></mrow><annotation encoding="application/x-tex">x</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">x</span></span></span></span>, but <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>sin</mi><mo>(</mo><mi>i</mi><mi>x</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">\sin(ix)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mop">sin</span><span class="mopen">(</span><span class="mord mathit">i</span><span class="mord mathit">x</span><span class="mclose">)</span></span></span></span> is something like <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>i</mi><mrow><mi mathvariant="normal">s</mi><mi mathvariant="normal">i</mi><mi mathvariant="normal">n</mi><mi mathvariant="normal">h</mi></mrow><mo>(</mo><mi>x</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">i\mathrm{sinh}(x)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit">i</span><span class="mord"><span class="mord mathrm">s</span><span class="mord mathrm">i</span><span class="mord mathrm">n</span><span class="mord mathrm">h</span></span><span class="mopen">(</span><span class="mord mathit">x</span><span class="mclose">)</span></span></span></span> which is huge for <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>x</mi></mrow><annotation encoding="application/x-tex">x</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">x</span></span></span></span> large.</p>

#### [ Kevin Buzzard (Nov 18 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147933418):
<p>The lingo is that functions like <code>sin</code> have "essential singularities" at infinity.</p>

#### [ Chris Hughes (Nov 18 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147933473):
<p>I think I could write a shorter proof inspired by that idea though.</p>

#### [ Chris Hughes (Nov 18 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147933478):
<p>Without going to a load of trouble definining a new topological space</p>

#### [ Kevin Buzzard (Nov 18 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147933796):
<p>Of course, one day someone will define projective n-space in Lean anyway, and you'll be able to use that.</p>

#### [ Kevin Buzzard (Nov 18 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147933837):
<p>The variety, the scheme, the real manifold and the complex manifold all need doing :-)</p>

#### [ Chris Hughes (Nov 18 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147934663):
<p>How would one state continuous at infinity in the simplest way?</p>

#### [ Kevin Buzzard (Nov 19 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147935871):
<p>if <code>nhds infinity</code> exists (and it might well not) then you could use that, but it would just be a fancy translation of your "epsilon delta" statement.</p>

#### [ Kenny Lau (Nov 19 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147935931):
<p>what is "infinity" in Q_p?</p>

#### [ Chris Hughes (Nov 19 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147936317):
<blockquote>
<p>if <code>nhds infinity</code> exists (and it might well not) then you could use that, but it would just be a fancy translation of your "epsilon delta" statement.</p>
</blockquote>
<p>I guess it's <code>at_top</code>, which is defined on a preorder, so I think <code>abs x \le abs y</code> is a preorder.</p>

#### [ Chris Hughes (Nov 19 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147936393):
<p>But that's not really what I want I don't think. Because at some point I still need to define multiplication by infinity to go down that route.</p>

#### [ Mario Carneiro (Nov 19 2018 at 05:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147944261):
<p>by the way, I find that statement interesting not because of this continuity business but because that's part 1 of FTA</p>

#### [ Reid Barton (Nov 19 2018 at 05:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147944271):
<p>that's why it's in a thread titled "polar coordinates" :)</p>

#### [ Mario Carneiro (Nov 19 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147944940):
<blockquote>
<p>Note that power series are typically not continuous at infinity, e.g. sin(x) is zero for arbitrarily large real x</p>
</blockquote>
<p>I don't think this is true...</p>

#### [ Scott Morrison (Nov 19 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147945389):
<p>surely "for arbitrarily large" implies an existential quantifier, not a universal one...?</p>

#### [ Kevin Buzzard (Nov 19 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147953327):
<p>I meant the true thing, regardless of how one can parse what I wrote and I agree that there may be a debate here. I am just pointing out that the analogue of Chris'lemma is false. Kenny -- you know what projective 1 space is over any field, as a variety. Making it an object that you can do analysis on is a different matter.</p>

#### [ Kevin Buzzard (Nov 19 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147953362):
<p>I have several volumes in my office about how to do analysis and geometry over totally disconnected fields. The most fashionable answer nowadays is to use adic spaces.</p>

#### [ Mario Carneiro (Nov 19 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147953367):
<p>I don't think CP^1 is as nice as you say, there is a reason infinity isn't normally treated as a number</p>

#### [ Mario Carneiro (Nov 19 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147953409):
<p>I don't think multiplication is continuous?</p>

#### [ Mario Carneiro (Nov 19 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147953416):
<p>plus I think there are still some undefined combinations like infty + infty and infty * 0</p>

#### [ Patrick Massot (Nov 19 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147953699):
<p>Mario, Kevin never said CP¹ has a nice algebraic structure</p>

#### [ Mario Carneiro (Nov 19 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147953776):
<p>he claimed that all polynomials are continuous?</p>

#### [ Mario Carneiro (Nov 19 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147953783):
<p>multiplication is a polynomial</p>

#### [ Patrick Massot (Nov 19 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147953787):
<p>The only case where infinity is sometimes treated as a number in this context is when discussing homographies</p>

#### [ Patrick Massot (Nov 19 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147953799):
<p>He wrote that polynomial extend to P¹ as continuous functions</p>

#### [ Kevin Buzzard (Nov 19 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147953800):
<p>Any rational function is continuous</p>

#### [ Kevin Buzzard (Nov 19 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147953806):
<p>(2+z)/(3+z^2) is continuous</p>

#### [ Kevin Buzzard (Nov 19 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147953815):
<p>but the trick is not to use infinity in your polynomials</p>

#### [ Kevin Buzzard (Nov 19 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147953817):
<p>just in your values it can take</p>

#### [ Kevin Buzzard (Nov 19 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147953819):
<p>and eat</p>

#### [ Mario Carneiro (Nov 19 2018 at 10:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147953862):
<p>I agree that there should be a nicer way to deal with meromorphic functions to avoid all the horrible case splits</p>

#### [ Mario Carneiro (Nov 19 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147953880):
<p>defining 1/0 = 0 helps a lot, but it doesn't solve all the problems</p>

#### [ Patrick Massot (Nov 19 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147953964):
<p>meromorphic functions can be defined as CP¹-valued holomorphic functions</p>

#### [ Patrick Massot (Nov 19 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147953977):
<p>no problem</p>

#### [ Mario Carneiro (Nov 19 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147953986):
<p>what's a holomorphic function</p>

#### [ Mario Carneiro (Nov 19 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147953989):
<p>in a general sense</p>

#### [ Patrick Massot (Nov 19 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147953999):
<p>you ask for local charts are source and target where you see an undergraduate holomorphic function</p>

#### [ Patrick Massot (Nov 19 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147954051):
<p>same as definining smooth functions between smooth manifolds</p>

#### [ Mario Carneiro (Nov 19 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147954059):
<p>wait so it's just a manifold?</p>

#### [ Patrick Massot (Nov 19 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147954060):
<p>complex manifold</p>

#### [ Patrick Massot (Nov 19 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147954063):
<p>coordinate changes have to be holomorphic</p>

#### [ Mario Carneiro (Nov 19 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147954084):
<p>hm... I'm sensing some circularity</p>

#### [ Patrick Massot (Nov 19 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147954093):
<p>in case of CP¹ you can get away with two charts</p>

#### [ Patrick Massot (Nov 19 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/147954096):
<p>and coordinate change is 1/z</p>

#### [ Chris Hughes (Nov 27 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/148409615):
<p>I mostly finished off a proof of the fundamental theorem of algebra today. The missing parts are complex nth roots and, the fact that it attains it's minimum value, given that it tends to infinity.</p>

#### [ Chris Hughes (Nov 28 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/148678532):
<p>Do we have that closed balls of complexes are compact?</p>

#### [ Reid Barton (Nov 28 2018 at 01:22)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/148679171):
<p>We have it for R but it looks like a little bit of work is required to get it for C. I would guess that <span class="user-mention" data-user-id="110050">@Sebastien Gouezel</span> has something useful here</p>

#### [ Sebastien Gouezel (Nov 28 2018 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/148694231):
<p>No, we don't have it. Even for reals, this is only in #PR484. I will add the complex case to this PR, it is not hard and definitely useful.</p>

#### [ Sebastien Gouezel (Nov 28 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/148705208):
<p>#PR484 now contains the fact that C is proper, i.e., closed balls (and therefore any bounded closed set) are compact.</p>

#### [ Reid Barton (Nov 28 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/148712221):
<p>Oh thanks! Somehow I had missed <a href="https://github.com/leanprover/mathlib/issues/484" target="_blank" title="https://github.com/leanprover/mathlib/issues/484">#484</a> entirely.</p>

#### [ Chris Hughes (Nov 28 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/148748308):
<p>Back to the original topic, I feel like <code>nth_root</code> should return real nth roots of negative numbers when they exist. Currently it defaults to zero for negative numbers</p>

#### [ Kevin Buzzard (Dec 01 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/150679507):
<p>Maybe it could just return <code>-nth_root (-x)</code> for negative <code>x</code>.</p>

#### [ Mario Carneiro (Dec 01 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/150679806):
<p>but that's wrong for even n</p>

#### [ Johan Commelin (Dec 01 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/150679860):
<p>???</p>

#### [ Johan Commelin (Dec 01 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/150679866):
<p>We're talking about <code>real.nth_root</code>, not the complex version</p>

#### [ Kevin Buzzard (Dec 01 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/150679922):
<p>It's junk for even n</p>

#### [ Kevin Buzzard (Dec 01 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/150679923):
<p>There's no right answer</p>

#### [ Johan Commelin (Dec 01 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/150679973):
<p>37</p>

#### [ Reid Barton (Dec 25 2018 at 05:04)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/152496581):
<blockquote>
<p>#PR484 now contains the fact that C is proper, i.e., closed balls (and therefore any bounded closed set) are compact.</p>
</blockquote>
<p>And now it is merged, so we are one step closer to FTA.</p>

#### [ Chris Hughes (Dec 25 2018 at 07:27)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/152500414):
<p>I do have FTA on my PC. Just waiting for polar coordinates and multiplicity to be merged.</p>

#### [ Mario Carneiro (Dec 25 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/152502597):
<p>Re: <code>nth_root</code>, do we need this definition? I didn't read it close enough last time but I see now that it only allows natural number roots. Why not just give <code>real</code> a has_pow instance?</p>

#### [ Mario Carneiro (Dec 25 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/152502603):
<p>i.e. <code>x ^ y = exp (y * log x)</code> discounting edge cases</p>

#### [ Mario Carneiro (Dec 25 2018 at 08:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/152502604):
<p>then you can use <code>x ^ (1/n)</code> for <code>nth_root</code></p>

#### [ Chris Hughes (Dec 25 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/152502794):
<p>I think that makes a lot of sense.</p>

#### [ Sebastien Gouezel (Dec 26 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/152543457):
<blockquote>
<blockquote>
<p>#PR484 now contains the fact that C is proper, i.e., closed balls (and therefore any bounded closed set) are compact.</p>
</blockquote>
<p>And now it is merged, so we are one step closer to FTA.</p>
</blockquote>
<p>Thanks a lot <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> , for all the hard work and cleaning up the mess.</p>

#### [ Patrick Massot (Dec 26 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/152545869):
<p>Sébastien, did you manage to learn something from this effort? It's difficult to see what Mario did because he squashed everything into one commit (I guess I could diff with the relevant branch)</p>

#### [ Sebastien Gouezel (Dec 26 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/152556998):
<p>Mario added a commit to the branch, before squashing everything when he commited to mathlib. So, you can see the modifications he made, at <a href="https://github.com/leanprover/mathlib/pull/484/commits/76fa5711faa89549e7b4e234715d256711f32f33" target="_blank" title="https://github.com/leanprover/mathlib/pull/484/commits/76fa5711faa89549e7b4e234715d256711f32f33">https://github.com/leanprover/mathlib/pull/484/commits/76fa5711faa89549e7b4e234715d256711f32f33</a>. Very instructive!</p>

#### [ Patrick Massot (Dec 26 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/152559779):
<p>Nice. I wish we could still keep your way of announcing intermediate statements, and then Mario-compress the proof. But I guess the compressed proof often skip your intermediate statements anyway</p>

#### [ Sebastien Gouezel (Dec 26 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/152560611):
<p>I hope that in longer proofs it will be possible to keep the intermediate statements, but for 10-lines proofs that are compressed down to 3 lines I really don't care.</p>
<p>In Isabelle, there is really strong emphasis on proofs that are a sequence of <code>have ...</code>, for (at least) the three following reasons:</p>
<ul>
<li>readability</li>
<li>maintainability (if a proof breaks because the statement of a theorem has changed, or automation has changed, then with <code>have ...</code> you can see what was being proved, and the breakage is very localized, while with a sequence of tactics or a very long expression you can notice the breaking much later after it has happened, and this is much harder to fix)</li>
<li>speed: different <code>have</code> statements can be handled in parallel, so on modern machines with a lot of cores even the proof of a single theorem can be split into many subtasks and therefore be processed very quickly.</li>
</ul>
<p>If I understand correctly, readability is not a goal in mathlib (although  I would very much like the opposite, but my opinion is not really important). For maintainability, if Mario is ready to maintain everything by himself this is not really an issue :) And for speed, if I understand correctly the proof of a single theorem is processed sequentially in Lean 3 (or am I wrong? is this going to change in Lean 4?)</p>

#### [ Patrick Massot (Dec 26 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/152560741):
<p>Maybe one day Mario will get tired, or too busy, so maybe we should worry more about maintainability. It seems to me he is already less available than one year ago. About parallel processing, you are correct about Lean 3, and it could change in Lean 4 (that's one of the improvement that was flagged as very difficult to build in Lean 3)</p>

#### [ Mario Carneiro (Dec 27 2018 at 01:35)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/152577881):
<p>You can see now why it took so long for me to merge this PR. Every time I looked at it I thought that it can be done better but I couldn't find the time to do the cleanup. As for intermediate statements, I agree that they are useful but I think they should be chosen carefully. Sometimes you can even do a necessary part of the proof by a judiciously chosen <code>change</code> that also reports a bit of info about what's going on at the same time. But in the long term I have more hope for methods like <code>#explode</code> for displaying proofs regardless of how they are proven. This separates concerns between the proof construction process and proof review for people who actually want to learn some maths from the proof</p>

#### [ Mario Carneiro (Dec 27 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/152577938):
<p>Speed was another reason I felt it necessary to revise many of Sebastien's proofs. I'm not entirely sure why but they mostly took 10s or more, and it was really noticeable. I tried to refrain from too much <code>simp</code> in the revisions</p>

#### [ Mario Carneiro (Dec 27 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/152578095):
<p>But I'm glad I haven't discouraged him from submitting PRs - I see a bunch more now. Hopefully we can make some more progress on analysis with the new additions</p>

#### [ Sebastien Gouezel (Dec 27 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/152592048):
<p>I am trying to submit much smaller PRs, hopefully this is a better strategy.</p>

#### [ Sebastien Gouezel (Dec 27 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23483%20polar%20coordinates/near/152592297):
<p>If you haven't started looking at #PR464 Bounded continuous functions, I can also split it into smaller chunks if you want. Tell me!</p>


{% endraw %}
