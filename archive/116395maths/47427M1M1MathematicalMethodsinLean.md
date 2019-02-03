---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/47427M1M1MathematicalMethodsinLean.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [(M1M1) Mathematical Methods in Lean](https://leanprover-community.github.io/archive/116395maths/47427M1M1MathematicalMethodsinLean.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Oct 13 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135729301):
<p>The joint maths and computer science students at Imperial College London are doing four courses this term. One on Haskell, one on logic, my course M1F, and a course called M1M1, which is a mathematical methods course, where the derivative of sin is cos just like it was at school and nobody really bothers with why that's true.</p>

#### [ Kevin Buzzard (Oct 13 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135729358):
<p>On the other hand, one of the questions on the first sheet was "define <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><mn>1</mn><mo>+</mo><mi>x</mi><mo>+</mo><msup><mi>x</mi><mn>2</mn></msup><mi mathvariant="normal">/</mi><mn>2</mn><mo>!</mo><mo>+</mo><msup><mi>x</mi><mn>3</mn></msup><mi mathvariant="normal">/</mi><mn>3</mn><mo>!</mo><mo>+</mo><mo>⋯</mo></mrow><annotation encoding="application/x-tex">f(x) = 1+x+x^2/2!+x^3/3!+\cdots</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8141079999999999em;"></span><span class="strut bottom" style="height:1.064108em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mopen">(</span><span class="mord mathit">x</span><span class="mclose">)</span><span class="mrel">=</span><span class="mord mathrm">1</span><span class="mbin">+</span><span class="mord mathit">x</span><span class="mbin">+</span><span class="mord"><span class="mord mathit">x</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">2</span></span></span></span></span></span></span></span><span class="mord mathrm">/</span><span class="mord mathrm">2</span><span class="mclose">!</span><span class="mbin">+</span><span class="mord"><span class="mord mathit">x</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">3</span></span></span></span></span></span></span></span><span class="mord mathrm">/</span><span class="mord mathrm">3</span><span class="mclose">!</span><span class="mbin">+</span><span class="minner">⋯</span></span></span></span> and let's not worry about what it means to converge. By multiplying everything out and re-arranging without worrying about whether this is valid, prove <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>f</mi><mo>(</mo><mi>x</mi><mo>+</mo><mi>y</mi><mo>)</mo><mo>=</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>×</mo><mi>f</mi><mo>(</mo><mi>y</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">f(x+y) = f(x) \times f(y)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mopen">(</span><span class="mord mathit">x</span><span class="mbin">+</span><span class="mord mathit" style="margin-right:0.03588em;">y</span><span class="mclose">)</span><span class="mrel">=</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mopen">(</span><span class="mord mathit">x</span><span class="mclose">)</span><span class="mbin">×</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.03588em;">y</span><span class="mclose">)</span></span></span></span>"</p>

#### [ Kevin Buzzard (Oct 13 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135729361):
<p>and I thought " <span class="user-mention" data-user-id="110044">@Chris Hughes</span>  did that properly, took him ages"</p>

#### [ Kevin Buzzard (Oct 13 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135729367):
<p>I wonder how far we'll be able to get on the M1M1 example sheets by the end of term :-)</p>

#### [ Kevin Buzzard (Oct 13 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135729407):
<p>One of the questions needed log and Chris did that a few weeks ago, so we're still just ahead</p>

#### [ Kevin Buzzard (Oct 13 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135729413):
<p>Are double angle formulae in Lean? Tricks about sin(theta) in terms of tan(theta/2)?</p>

#### [ Kevin Buzzard (Oct 13 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135729471):
<p>Stuff which is assumed in M1M1? Ability to define <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msubsup><mo>∫</mo><mn>0</mn><mi mathvariant="normal">∞</mi></msubsup><msup><mi>e</mi><mrow><mo>−</mo><msup><mi>x</mi><mn>2</mn></msup><mi mathvariant="normal">/</mi><mn>2</mn></mrow></msup><mi>d</mi><mi>x</mi></mrow><annotation encoding="application/x-tex">\int_0^\infty e^{-x^2/2} d x</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.9869199999999998em;"></span><span class="strut bottom" style="height:1.3427399999999998em;vertical-align:-0.35582em;"></span><span class="base"><span class="mop"><span class="mop op-symbol small-op" style="margin-right:0.19445em;position:relative;top:-0.0005599999999999772em;">∫</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.8592920000000001em;"><span style="top:-2.34418em;margin-left:-0.19445em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">0</span></span></span><span style="top:-3.2579000000000002em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">∞</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.35582em;"></span></span></span></span></span><span class="mord"><span class="mord mathit">e</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.9869199999999998em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">−</span><span class="mord mtight"><span class="mord mathit mtight">x</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8913142857142857em;"><span style="top:-2.931em;margin-right:0.07142857142857144em;"><span class="pstrut" style="height:2.5em;"></span><span class="sizing reset-size3 size1 mtight"><span class="mord mathrm mtight">2</span></span></span></span></span></span></span></span><span class="mord mathrm mtight">/</span><span class="mord mathrm mtight">2</span></span></span></span></span></span></span></span></span><span class="mord mathit">d</span><span class="mord mathit">x</span></span></span></span>?</p>

#### [ Chris Hughes (Oct 13 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135729571):
<p>It's not just methods that's like this. Try formally proving every permutation is the product of disjoint cycles.</p>

#### [ Kevin Buzzard (Oct 13 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135729697):
<p>you show us up for the charlatains we are!</p>

#### [ Kevin Buzzard (Oct 13 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135729733):
<p>But we're mathematicans. If your silly software cannot easily prove things which are intuitively obvious to us then the problem is surely with your software</p>

#### [ Kevin Buzzard (Oct 13 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135729750):
<p>The proof is "choose an element, keep hitting with the permutation, eventually you'll get back to where you start, done by induction"</p>

#### [ Kevin Buzzard (Oct 13 2018 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135729794):
<p>(assuming we're talking about finite sets/types)</p>

#### [ Kenny Lau (Oct 13 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135729898):
<p>that's what I did</p>

#### [ Kevin Buzzard (Oct 13 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135729986):
<p>how many lines?</p>

#### [ Kenny Lau (Oct 13 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135730384):
<p>26 lines</p>

#### [ Kenny Lau (Oct 13 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135730385):
<p><a href="https://github.com/kckennylau/Lean/blob/master/Sym.lean#L645-L670" target="_blank" title="https://github.com/kckennylau/Lean/blob/master/Sym.lean#L645-L670">https://github.com/kckennylau/Lean/blob/master/Sym.lean#L645-L670</a></p>

#### [ Kenny Lau (Oct 13 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135730387):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">list_step</span> <span class="o">(</span><span class="n">σ</span> <span class="o">:</span> <span class="n">Sym</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">step</span> <span class="n">n</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">refine</span> <span class="n">well_founded</span><span class="bp">.</span><span class="n">fix</span> <span class="n">list_step</span><span class="bp">.</span><span class="n">aux</span><span class="bp">.</span><span class="n">wf</span> <span class="bp">_</span> <span class="n">σ</span><span class="bp">;</span> <span class="k">from</span>
<span class="bp">λ</span> <span class="n">σ</span> <span class="n">ih</span><span class="o">,</span> <span class="k">if</span> <span class="n">H</span> <span class="o">:</span> <span class="n">σ</span><span class="bp">.</span><span class="n">support</span> <span class="bp">=</span> <span class="err">∅</span> <span class="k">then</span> <span class="o">[]</span>
  <span class="k">else</span> <span class="k">let</span> <span class="bp">⟨</span><span class="n">i</span><span class="o">,</span> <span class="n">hi</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">σ</span><span class="bp">.</span><span class="n">support_choice</span> <span class="n">H</span> <span class="k">in</span>
    <span class="n">step</span><span class="bp">.</span><span class="n">mk&#39;</span> <span class="o">(</span><span class="n">σ</span> <span class="n">i</span><span class="o">)</span> <span class="n">i</span> <span class="o">(</span><span class="n">support_def</span><span class="bp">.</span><span class="mi">1</span> <span class="n">hi</span><span class="o">)</span>
    <span class="bp">::</span> <span class="n">ih</span> <span class="o">(</span><span class="n">swap</span> <span class="o">(</span><span class="n">σ</span> <span class="n">i</span><span class="o">)</span> <span class="n">i</span> <span class="bp">*</span> <span class="n">σ</span><span class="o">)</span> <span class="o">(</span><span class="n">support_swap_mul</span> <span class="n">hi</span><span class="o">)</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">list_step_prod</span> <span class="o">(</span><span class="n">σ</span> <span class="o">:</span> <span class="n">Sym</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span>
  <span class="o">(</span><span class="n">σ</span><span class="bp">.</span><span class="n">list_step</span><span class="bp">.</span><span class="n">map</span> <span class="n">step</span><span class="bp">.</span><span class="kn">eval</span><span class="o">)</span><span class="bp">.</span><span class="n">prod</span> <span class="bp">=</span> <span class="n">σ</span> <span class="o">:=</span>
<span class="n">well_founded</span><span class="bp">.</span><span class="n">induction</span> <span class="n">list_step</span><span class="bp">.</span><span class="n">aux</span><span class="bp">.</span><span class="n">wf</span> <span class="n">σ</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">σ</span> <span class="n">ih</span><span class="o">,</span>
<span class="k">begin</span>
  <span class="n">dsimp</span> <span class="o">[</span><span class="n">list_step</span><span class="o">],</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">well_founded</span><span class="bp">.</span><span class="n">fix_eq</span><span class="o">],</span>
  <span class="n">split_ifs</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">ext</span><span class="o">,</span> <span class="n">by_contra</span> <span class="n">H</span><span class="o">,</span>
    <span class="n">suffices</span> <span class="o">:</span> <span class="n">i</span> <span class="err">∈</span> <span class="o">(</span><span class="err">∅</span> <span class="o">:</span> <span class="n">finset</span> <span class="o">(</span><span class="n">fin</span> <span class="n">n</span><span class="o">)),</span>
    <span class="o">{</span> <span class="n">simp</span> <span class="n">at</span> <span class="n">this</span><span class="o">,</span> <span class="n">cc</span> <span class="o">},</span>
    <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">h</span><span class="o">,</span> <span class="n">support_def</span><span class="o">],</span>
    <span class="n">exact</span> <span class="n">mt</span> <span class="n">eq</span><span class="bp">.</span><span class="n">symm</span> <span class="n">H</span> <span class="o">},</span>
  <span class="n">cases</span> <span class="n">support_choice</span> <span class="n">σ</span> <span class="n">h</span> <span class="k">with</span> <span class="n">i</span> <span class="n">hi</span><span class="o">,</span>
  <span class="n">unfold</span> <span class="n">list_step</span><span class="bp">._</span><span class="n">match_1</span><span class="o">,</span>
  <span class="n">specialize</span> <span class="n">ih</span> <span class="bp">_</span> <span class="o">(</span><span class="n">support_swap_mul</span> <span class="n">hi</span><span class="o">),</span>
  <span class="n">dsimp</span> <span class="o">[</span><span class="n">list_step</span><span class="o">]</span> <span class="n">at</span> <span class="n">ih</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">list</span><span class="bp">.</span><span class="n">map_cons</span><span class="o">,</span> <span class="n">list</span><span class="bp">.</span><span class="n">prod_cons</span><span class="o">,</span> <span class="n">ih</span><span class="o">,</span> <span class="err">←</span> <span class="n">mul_assoc</span><span class="o">],</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">step</span><span class="bp">.</span><span class="n">eval_mk&#39;</span><span class="o">,</span> <span class="n">swap_mul_self</span><span class="o">,</span> <span class="n">one_mul</span><span class="o">]</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Oct 13 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135730390):
<p>That sounds like a reasonable length to me.</p>

#### [ Chris Hughes (Oct 13 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135730559):
<p>That's a proof of something different isn't it? It's a proof about products of swaps, not disjoint cycles.</p>

#### [ Kenny Lau (Oct 13 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135730680):
<p>ah, right</p>

#### [ Kevin Buzzard (Oct 13 2018 at 14:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135730742):
<p>so the question remains</p>

#### [ Chris Hughes (Oct 13 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135747465):
<p>225 lines <a href="https://github.com/leanprover/mathlib/compare/master...dorhinj:cycles2?expand=1" target="_blank" title="https://github.com/leanprover/mathlib/compare/master...dorhinj:cycles2?expand=1">https://github.com/leanprover/mathlib/compare/master...dorhinj:cycles2?expand=1</a></p>

#### [ Mario Carneiro (Oct 14 2018 at 01:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135752321):
<p>I like it, we're getting a lot of nice structure on <code>perm</code></p>

#### [ Mario Carneiro (Oct 14 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135752367):
<p>Any chance of defining stuff about the finitely supported permutations? (i.e. it's a subgroup, and has most of the properties you have put on finite permutation groups like the alternating group or separation into disjoint cycles)</p>

#### [ Kevin Buzzard (Oct 14 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135771386):
<p>One would imagine that these are also situations where a mathematician would say "it's obvious" (like e.g. the fact that it's a subgroup).</p>

#### [ Kenny Lau (Oct 14 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135771455):
<p>I think at this point we all know that it's pointless to keep saying that so and so is obvious to a mathematician.</p>

#### [ Kevin Buzzard (Oct 14 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135771526):
<p>I don't think it's pointless at all Kenny. I think that if we isolate many of the things that are "obvious to a mathematician" and make sure that they are <em>relatively easy for a mathematician do in Lean</em> (even though we all know that they are in truth difficult to do from the actual axioms of mathematics) then this is a step towards making Lean more intuitive for mathematicians to use.</p>

#### [ Chris Hughes (Oct 14 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135775656):
<blockquote>
<p>Any chance of defining stuff about the finitely supported permutations? (i.e. it's a subgroup, and has most of the properties you have put on finite permutation groups like the alternating group or separation into disjoint cycles)</p>
</blockquote>
<p>What's the best approach for this. Are you happy to lose computability in favour of generality? My <code>cycle_of</code> function can certainly be extended to infinite permutations, but not computably, though it is outrageously slow anyway. For <code>sign</code> and stuff, is it best to just create a new definition of <code>sign</code> for finitely supported permutations of infinite types. I imagine this is better than making a partial function which is actually a total function on most of the stuff people want to use it for.</p>

#### [ Mario Carneiro (Oct 14 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135775778):
<p><code>cycle_of</code> should be computable on infinite (finitely supported) permutations, assuming <code>decidable_eq</code> on the base set, although I would factor it into a <code>cycle_support</code> function that returns the list of iterates of the input</p>

#### [ Mario Carneiro (Oct 14 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135775883):
<p>and then I guess there are also a bunch of noncomputable functions we might want in the truly infinite case, like <code>cycle_of</code> where the cycle is possibly isomorphic to Z</p>

#### [ Mario Carneiro (Oct 14 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135775946):
<p>In fact it is still true that "every permutation is a product of cycles" in the truly infinite case, you just have to make sense of an infinite product of disjoint permutations</p>

#### [ Kevin Buzzard (Oct 14 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%28M1M1%29%20Mathematical%20Methods%20in%20Lean/near/135777622):
<blockquote>
<p>I think at this point we all know that it's pointless to keep saying that so and so is obvious to a mathematician.</p>
</blockquote>
<p>Just adding to this thread that to a 1st year maths undergraduate it is "obvious" that the derivative of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>sin</mi><mo>(</mo><mi>x</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">\sin(x)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mop">sin</span><span class="mopen">(</span><span class="mord mathit">x</span><span class="mclose">)</span></span></span></span> is <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>cos</mi><mo>(</mo><mi>x</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">\cos(x)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mop">cos</span><span class="mopen">(</span><span class="mord mathit">x</span><span class="mclose">)</span></span></span></span> (because they "learnt it at school") and I think that having this in Lean would be a very natural goal. It will be interesting to see if our new cohort of freshers were up to the task.</p>


{% endraw %}
