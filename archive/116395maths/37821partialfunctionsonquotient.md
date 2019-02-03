---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/37821partialfunctionsonquotient.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [partial functions on quotient](https://leanprover-community.github.io/archive/116395maths/37821partialfunctionsonquotient.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Chris Hughes (Aug 05 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20on%20quotient/near/130929260):
<p>What's the easiest way to define a partial function on a quotient type, where the proof that it is well defined depends on the predicate? I tried <code>quotient.hrec_on</code> but whilst I can define the function, it's hard to prove things about it due to <code>motive is not type correct</code> errors. For context, I'm experimenting with defining the signature of a permutation as being derived from this.</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">sign_aux2</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">perm</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">units</span> <span class="bp">ℤ</span>
<span class="bp">|</span> <span class="o">[]</span>     <span class="n">f</span> <span class="o">:=</span> <span class="mi">1</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">x</span><span class="bp">::</span><span class="n">l</span><span class="o">)</span> <span class="n">f</span> <span class="o">:=</span> <span class="k">if</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">x</span> <span class="k">then</span> <span class="n">sign_aux2</span> <span class="n">l</span> <span class="n">f</span> <span class="k">else</span> <span class="bp">-</span><span class="n">sign_aux2</span> <span class="n">l</span> <span class="o">(</span><span class="n">swap</span> <span class="n">x</span> <span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">)</span> <span class="bp">*</span> <span class="n">f</span><span class="o">)</span>
</pre></div>


<p>I plan to use the list underneath <code>finset.univ</code>, and prove it doesn't depend on the order of the list.</p>

#### [ Chris Hughes (Aug 05 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20on%20quotient/near/130929261):
<p>The problem is that the list has to contain everything of the type in order to prove the <code>quotient.lift</code> condition.</p>

#### [ Reid Barton (Aug 05 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20on%20quotient/near/130929617):
<p><code>roption</code>/<code>pfun</code> can be helpful</p>

#### [ Reid Barton (Aug 05 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20on%20quotient/near/130929641):
<p>though maybe I don't quite understand what you're doing yet</p>

#### [ Reid Barton (Aug 05 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20on%20quotient/near/130929737):
<p>I guess it's okay. The strategy is to define a (total) function to <code>roption (units \Z)</code>, which sends all "bad" elements to <code>roption.none</code>, using <code>quotient.lift</code></p>

#### [ Reid Barton (Aug 05 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20on%20quotient/near/130929865):
<p>You can also define a dependent function which takes the needed hypothesis as an argument using <code>quotient.rec</code>, but I found that approach to be really difficult when I had to do something like this.</p>

#### [ Chris Hughes (Aug 05 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20on%20quotient/near/130930011):
<p>Good plan. Thanks.</p>

#### [ Kevin Buzzard (Aug 05 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20on%20quotient/near/130930355):
<p>Speaking as someone whose job it is to teach students what the signature of a permutation is, I'm pleased about how it's going this year. On the other hand speaking as someone who is well aware that these notions have been around for ages, I can't help but feeling that the issues my students are running into are ones which will already have been solved. Are there already 23 different implementations of signature of a permutation in Coq, for example? I kind-of suspect that the questions we've been running into since we started thinking about this are ones which will have been seen many times before...</p>

#### [ Chris Hughes (Aug 05 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20on%20quotient/near/130938495):
<p>I think looking at coq is good for general questions like which proof should I use, but not so good for questions like this.</p>

#### [ Reid Barton (Aug 05 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20on%20quotient/near/130938719):
<p>By the way, I was wondering whether it would be possible to define the sign of a permutation as the determinant of the corresponding linear transformation on (say) Q^n, and define the latter in terms of the nth exterior power.<br>
But, in order to show the nth exterior power is not zero, I think you end up needing the fact that a composition of an odd number of transpositions cannot be the identity anyways. Unless there is an even fancier approach which I missed?</p>

#### [ Kenny Lau (Aug 05 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20on%20quotient/near/130938763):
<p>Chris (and I independently) defined sign of permutation using number of inversions</p>

#### [ Chris Hughes (Aug 05 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20on%20quotient/near/130938973):
<p>I changed it to basically what I posted above</p>

#### [ Reid Barton (Aug 05 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20on%20quotient/near/130938975):
<p>Right, but if you were given the fact that <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mo>⋀</mo><mi>n</mi></msup><msup><mi mathvariant="double-struck">Q</mi><mrow><mo>⊕</mo><mi>n</mi></mrow></msup></mrow><annotation encoding="application/x-tex">\bigwedge^n \mathbb{Q}^{\oplus n}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.804292em;"></span><span class="strut bottom" style="height:1.054302em;vertical-align:-0.25001em;"></span><span class="base"><span class="mop"><span class="mop op-symbol small-op" style="position:relative;top:-0.0000050000000000050004em;">⋀</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.804292em;"><span style="top:-3.2029em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span></span></span></span></span><span class="mord"><span class="mord"><span class="mord mathbb">Q</span></span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.771331em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">⊕</span><span class="mord mathit mtight">n</span></span></span></span></span></span></span></span></span></span></span></span> was one-dimensional, then you could get signs of permutations (including that it is a group homomorphism) for free.</p>

#### [ Reid Barton (Aug 05 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20on%20quotient/near/130938980):
<p>Or there are other facts you could start from, like <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>O</mi><mo>(</mo><mi>n</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">O(n)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.02778em;">O</span><span class="mopen">(</span><span class="mord mathit">n</span><span class="mclose">)</span></span></span></span> (or <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>G</mi><mi>L</mi><mo>(</mo><mi>n</mi><mo separator="true">,</mo><mrow><mi mathvariant="double-struck">R</mi></mrow><mo>)</mo></mrow><annotation encoding="application/x-tex">GL(n, \mathbb{R})</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit">G</span><span class="mord mathit">L</span><span class="mopen">(</span><span class="mord mathit">n</span><span class="mpunct">,</span><span class="mord"><span class="mord mathbb">R</span></span><span class="mclose">)</span></span></span></span>) having two components</p>

#### [ Kevin Buzzard (Aug 05 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/partial%20functions%20on%20quotient/near/130940233):
<p>To prove that the n'th exterior power is not zero I guess you have to explicitly construct some alternating form? If you could come up with some definition of det which had the property that switching two rows changed the sign etc then you might be in good shape, but the only way I know how to do this is to come up with the definition of det, and the definition of det I know involves signatures. I half-suspect that there were some comments about this in my UG notes, in my office, I'll try and remember to dig them up when I get back to London.</p>


{% endraw %}
