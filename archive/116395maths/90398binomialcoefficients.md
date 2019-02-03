---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/90398binomialcoefficients.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [binomial coefficients](https://leanprover-community.github.io/archive/116395maths/90398binomialcoefficients.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Nov 07 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/146974762):
<p>Preparing a lecture on the binomial and multinomial theorem. For pedagogical reasons I will not prove the binomial theorem the way it's proved in Lean (although the students who come to the "extra material" session will see the Lean proof). In Lean I guess the binomial coefficient <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mo fence="true">(</mo><mfrac linethickness="0px"><mrow><mi>n</mi></mrow><mrow><mi>r</mi></mrow></mfrac><mo fence="true">)</mo></mrow></mrow><annotation encoding="application/x-tex">\binom{n}{r}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.85em;"></span><span class="strut bottom" style="height:1.20001em;vertical-align:-0.35001em;"></span><span class="base"><span class="mord"><span class="mopen delimcenter" style="top:0em;"><span class="delimsizing size1">(</span></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.7453919999999999em;"><span style="top:-2.3550000000000004em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight" style="margin-right:0.02778em;">r</span></span></span></span><span style="top:-3.144em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">n</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.345em;"></span></span></span></span><span class="mclose delimcenter" style="top:0em;"><span class="delimsizing size1">)</span></span></span></span></span></span> is defined to be <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mfrac><mrow><mi>n</mi><mo>!</mo></mrow><mrow><mi>r</mi><mo>!</mo><mo>(</mo><mi>n</mi><mo>−</mo><mi>r</mi><mo>)</mo><mo>!</mo></mrow></mfrac><mi mathvariant="normal">.</mi></mrow><annotation encoding="application/x-tex">\frac{n!}{r!(n-r)!}. </annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8801079999999999em;"></span><span class="strut bottom" style="height:1.400108em;vertical-align:-0.52em;"></span><span class="base"><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.8801079999999999em;"><span style="top:-2.655em;"><span class="pstrut" style="height:3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight" style="margin-right:0.02778em;">r</span><span class="mclose mtight">!</span><span class="mopen mtight">(</span><span class="mord mathit mtight">n</span><span class="mbin mtight">−</span><span class="mord mathit mtight" style="margin-right:0.02778em;">r</span><span class="mclose mtight">)</span><span class="mclose mtight">!</span></span></span></span><span style="top:-3.23em;"><span class="pstrut" style="height:3em;"></span><span class="frac-line" style="border-bottom-width:0.04em;"></span></span><span style="top:-3.394em;"><span class="pstrut" style="height:3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">n</span><span class="mclose mtight">!</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.52em;"></span></span></span></span><span class="mclose nulldelimiter"></span></span><span class="mord mathrm">.</span></span></span></span> So is there in Lean a proof that <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mo fence="true">(</mo><mfrac linethickness="0px"><mrow><mi>n</mi></mrow><mrow><mi>r</mi></mrow></mfrac><mo fence="true">)</mo></mrow></mrow><annotation encoding="application/x-tex">\binom{n}{r}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.85em;"></span><span class="strut bottom" style="height:1.20001em;vertical-align:-0.35001em;"></span><span class="base"><span class="mord"><span class="mopen delimcenter" style="top:0em;"><span class="delimsizing size1">(</span></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.7453919999999999em;"><span style="top:-2.3550000000000004em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight" style="margin-right:0.02778em;">r</span></span></span></span><span style="top:-3.144em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">n</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.345em;"></span></span></span></span><span class="mclose delimcenter" style="top:0em;"><span class="delimsizing size1">)</span></span></span></span></span></span> equals the number of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>r</mi></mrow><annotation encoding="application/x-tex">r</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.02778em;">r</span></span></span></span>-element subtypes of a a type of size <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>n</mi></mrow><annotation encoding="application/x-tex">n</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">n</span></span></span></span>? [this is my definition of the binomial coefficient in my lectures]</p>

#### [ Johan Commelin (Nov 07 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/146974999):
<p>Do we know that the powerset of a type of size <code>n</code> has size <code>2 ^ n</code>?</p>

#### [ Johan Commelin (Nov 07 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/146975085):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> Wouldn't it make sense to define <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mo fence="true">(</mo><mfrac linethickness="0px"><mrow><mi>n</mi></mrow><mrow><mi>r</mi></mrow></mfrac><mo fence="true">)</mo></mrow></mrow><annotation encoding="application/x-tex">n \choose r</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.85em;"></span><span class="strut bottom" style="height:1.20001em;vertical-align:-0.35001em;"></span><span class="base"><span class="mord"><span class="mopen delimcenter" style="top:0em;"><span class="delimsizing size1">(</span></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.7453919999999999em;"><span style="top:-2.3550000000000004em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight" style="margin-right:0.02778em;">r</span></span></span></span><span style="top:-3.144em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">n</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.345em;"></span></span></span></span><span class="mclose delimcenter" style="top:0em;"><span class="delimsizing size1">)</span></span></span></span></span></span> via Pascal's triangle?</p>

#### [ Johannes Hölzl (Nov 07 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/146975630):
<p>it is defined recursively in <code>mathlib</code> (in <code>mathlib/data/nat/choose.lean</code>):</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">choose</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="bp">ℕ</span>
<span class="bp">|</span> <span class="bp">_</span>             <span class="mi">0</span> <span class="o">:=</span> <span class="mi">1</span>
<span class="bp">|</span> <span class="mi">0</span>       <span class="o">(</span><span class="n">k</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="n">k</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="n">choose</span> <span class="n">n</span> <span class="n">k</span> <span class="bp">+</span> <span class="n">choose</span> <span class="n">n</span> <span class="o">(</span><span class="n">succ</span> <span class="n">k</span><span class="o">)</span>
</pre></div>

#### [ Kevin Buzzard (Nov 07 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/146975661):
<p>Sure, that would be another way; then you can prove it's what I said it is by induction on n. Hmm and I guess you could then prove the result about the subsets of size r of a set of size n by induction on n.</p>

#### [ Kevin Buzzard (Nov 07 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147108963):
<p>I guess I was just checking that everything I said today was in Lean. I am giving this awful proof of the binomial theorem of the form "imagine multiplying out (a+b)(a+b)(a+b)...(a+b) n times -- now think about what the general term looks like? You choose r brackets and choose a from them, and choose b from the rest -- done"</p>

#### [ Kevin Buzzard (Nov 07 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147109092):
<p>but actually I think everything is either there or could be there. <span class="user-mention" data-user-id="112680">@Johan Commelin</span> the sum of the binomial coefficients being <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mn>2</mn><mi>n</mi></msup></mrow><annotation encoding="application/x-tex">2^n</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.664392em;"></span><span class="strut bottom" style="height:0.664392em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathrm">2</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span></span></span></span></span></span></span></span> is easy: you can deduce it from the binomial theorem with <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>a</mi><mo>=</mo><mi>b</mi><mo>=</mo><mn>1</mn></mrow><annotation encoding="application/x-tex">a=b=1</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.69444em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">a</span><span class="mrel">=</span><span class="mord mathit">b</span><span class="mrel">=</span><span class="mord mathrm">1</span></span></span></span> ;-)</p>

#### [ Johan Commelin (Nov 07 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147109115):
<p>Sure. But that's not exactly what I asked <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Bryan Gin-ge Chen (Nov 07 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147109165):
<p>I think what you asked for is <a href="https://github.com/leanprover/mathlib/blob/89431cf4f01ff0f6b4005f96795a23571258cbf0/data/finset.lean#L1198" target="_blank" title="https://github.com/leanprover/mathlib/blob/89431cf4f01ff0f6b4005f96795a23571258cbf0/data/finset.lean#L1198">here</a>.</p>

#### [ Kevin Buzzard (Nov 07 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147242495):
<p>...as long as you can prove that the size of a subset is at most the size of the set (which I am pretty sure is there) and the result about subsets of size r (which should be fine by induction on n).</p>

#### [ Bryan Gin-ge Chen (Nov 13 2018 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147613115):
<blockquote>
<p>So is there in Lean a proof that <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mo fence="true">(</mo><mfrac linethickness="0px"><mrow><mi>n</mi></mrow><mrow><mi>r</mi></mrow></mfrac><mo fence="true">)</mo></mrow></mrow><annotation encoding="application/x-tex">\binom{n}{r}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.85em;"></span><span class="strut bottom" style="height:1.20001em;vertical-align:-0.35001em;"></span><span class="base"><span class="mord"><span class="mopen delimcenter" style="top:0em;"><span class="delimsizing size1">(</span></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.7453919999999999em;"><span style="top:-2.3550000000000004em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight" style="margin-right:0.02778em;">r</span></span></span></span><span style="top:-3.144em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">n</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.345em;"></span></span></span></span><span class="mclose delimcenter" style="top:0em;"><span class="delimsizing size1">)</span></span></span></span></span></span> equals the number of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>r</mi></mrow><annotation encoding="application/x-tex">r</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.02778em;">r</span></span></span></span>-element subtypes of a type of size <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>n</mi></mrow><annotation encoding="application/x-tex">n</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">n</span></span></span></span>?</p>
</blockquote>
<p>I couldn't find this in mathlib so I've been working off-and-on on this. I finally have a proof, but it seems excessively long and ugly. Well, actually what I have is <a href="https://gist.github.com/bryangingechen/3f8e3fa3664bb4b044e9e607725cab1b" target="_blank" title="https://gist.github.com/bryangingechen/3f8e3fa3664bb4b044e9e607725cab1b">a proof of this</a>:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">card_subsets_of_range_eq_choose</span> <span class="o">(</span><span class="n">n</span> <span class="n">k</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">card</span> <span class="o">((</span><span class="n">powerset</span> <span class="o">(</span><span class="n">range</span> <span class="n">n</span><span class="o">))</span><span class="bp">.</span><span class="n">filter</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">t</span><span class="o">,</span> <span class="n">card</span> <span class="n">t</span> <span class="bp">=</span> <span class="n">k</span><span class="o">))</span> <span class="bp">=</span> <span class="n">choose</span> <span class="n">n</span> <span class="n">k</span> <span class="o">:=</span>
</pre></div>


<p>(what should be the name?) though what you really want is this:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">card_subsets_card_eq_choose</span>  <span class="o">{</span><span class="n">s</span> <span class="o">:</span> <span class="n">finset</span> <span class="n">α</span><span class="o">}</span> <span class="o">(</span><span class="n">k</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">card</span> <span class="o">((</span><span class="n">powerset</span> <span class="n">s</span><span class="o">)</span><span class="bp">.</span><span class="n">filter</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">t</span><span class="o">,</span> <span class="n">card</span> <span class="n">t</span> <span class="bp">=</span> <span class="n">k</span><span class="o">))</span> <span class="bp">=</span> <span class="n">choose</span> <span class="o">(</span><span class="n">card</span> <span class="n">s</span><span class="o">)</span> <span class="n">k</span> <span class="o">:=</span>
<span class="n">sorry</span>
</pre></div>


<p><a href="#narrow/stream/113488-general/subject/tutorial/near/135254614" title="#narrow/stream/113488-general/subject/tutorial/near/135254614">Last time I ran into something like this</a>, <span class="user-mention" data-user-id="110026">@Simon Hudon</span> ended up writing a bunch of stuff for me which is now in the tutorials branch. This one's probably much easier but I haven't tried to tackle it yet...</p>
<p>Anyways, if anyone wants to golf this down to something reasonable or give advice on making it nicer, I'd really appreciate it!</p>

#### [ Mario Carneiro (Nov 13 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147613222):
<p>I would hope to have a function on <code>list</code> that constructs all k element sublists</p>

#### [ Mario Carneiro (Nov 13 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147613231):
<p>maybe we have it already?</p>

#### [ Bryan Gin-ge Chen (Nov 13 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147613251):
<p>Oh that sounds like a good idea.</p>

#### [ Mario Carneiro (Nov 13 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147613290):
<p>I don't think we have it</p>

#### [ Mario Carneiro (Nov 13 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147613355):
<p>The nice thing about this is that the proof that this list has length <code>choose n k</code> will be obvious from the construction</p>

#### [ Mario Carneiro (Nov 13 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147613375):
<p>and the rest is just lifting to the quotient</p>

#### [ Bryan Gin-ge Chen (Nov 13 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147613405):
<p>right, this is like the approach to finite partitions you suggested before that I still haven't managed to do</p>

#### [ Chris Hughes (Nov 13 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147615848):
<p><span class="user-mention" data-user-id="123965">@Bryan Gin-ge Chen</span> </p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">sublists_of_length</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">l</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">list</span> <span class="o">(</span><span class="n">list</span> <span class="n">α</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">l</span>      <span class="mi">0</span>     <span class="o">:=</span> <span class="o">[[]]</span>
<span class="bp">|</span> <span class="o">[]</span>     <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="o">[]</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">a</span><span class="bp">::</span><span class="n">l</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="n">sublists_of_length</span> <span class="n">l</span> <span class="n">n</span><span class="o">)</span><span class="bp">.</span><span class="n">map</span> <span class="o">(</span><span class="n">list</span><span class="bp">.</span><span class="n">cons</span> <span class="n">a</span><span class="o">)</span> <span class="bp">++</span>
  <span class="o">(</span><span class="n">sublists_of_length</span> <span class="n">l</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">))</span>
</pre></div>


<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> The definition of <code>list.sublists</code> in mathlib is totally incomprehensible to me, but is faster than the most natural definition. This approach to <code>sublist_of_length</code> is presumably not the fastest. What's the general policy on fast definitions versus comprehensible definitions?</p>

#### [ Mario Carneiro (Nov 13 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147615890):
<p>fast is better than comprehensible</p>

#### [ Mario Carneiro (Nov 13 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147615949):
<p>you can often prove the comprehensible definition as a lemma though</p>

#### [ Mario Carneiro (Nov 13 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147615968):
<p>I think the definition of <code>list.sublists</code> is based on haskell's</p>

#### [ Chris Hughes (Nov 13 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147615988):
<p>Even if fast means much longer proofs?</p>

#### [ Mario Carneiro (Nov 13 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147616009):
<p>yes, although we can also retrofit a faster definition</p>

#### [ Johannes Hölzl (Nov 13 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147616013):
<p>for me comprehensible is better than fast. For fast we often need a different solution anyway</p>

#### [ Johannes Hölzl (Nov 13 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147616086):
<p>With Lean4 <span class="emoji emoji-1f340" title="four leaf clover">:four_leaf_clover:</span>  we hopefully can simply redefine constants for fast evaluation</p>

#### [ Mario Carneiro (Nov 13 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147616098):
<p>Note that in the case of <code>sublists</code> there is actually a separate version <code>sublists'</code> that is basically the comprehensible one, to which we prove equivalence</p>

#### [ Johannes Hölzl (Nov 13 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147616131):
<p>Hm, then it would be better to have <code>sublist</code> to be the comprehensible one?!</p>

#### [ Mario Carneiro (Nov 13 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147616160):
<p>The idea is that the default one should be VM-fast</p>

#### [ Mario Carneiro (Nov 13 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147616174):
<p>because this is in the computational part</p>

#### [ Mario Carneiro (Nov 13 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147616280):
<p>(there is an additional complication, in that <code>sublists</code> and <code>sublists'</code> are not equal but differ by a complicated permutation)</p>

#### [ Mario Carneiro (Nov 13 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147616338):
<p>They actually both have fast VM definitions, but <code>sublists</code> is faster</p>

#### [ Mario Carneiro (Nov 13 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147616348):
<p>and <code>sublists'</code> has nicer equation lemmas</p>

#### [ Mario Carneiro (Nov 13 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147618019):
<p>here's a faster version of the same definition:</p>
<div class="codehilite"><pre><span></span>def sublists_of_length_aux {α : Type*} : list α → ℕ → (list α → list α) → list (list α) → list (list α)
| l      0     f r := f [] :: r
| []     (n+1) f r := r
| (a::l) (n+1) f r := sublists_of_length_aux l n (f ∘ list.cons a)
  (sublists_of_length_aux l (n + 1) f r)

def sublists_of_length {α : Type*} (l : list α) (n : ℕ) : list (list α) :=
sublists_of_length_aux l n id []
</pre></div>


<p>the idea is to define <code>(sublists_of_length l n).map f ++ r</code> by recursion without stacking recursive calls to <code>map</code> or <code>append</code></p>

#### [ Mario Carneiro (Nov 13 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147618069):
<p>You can prove without too much difficulty that <code>sublists_of_length_aux l n f r = (sublists_of_length l n).map f ++ r</code> and then you can prove your equation lemmas as theorems</p>

#### [ Jeremy Avigad (Nov 15 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147712036):
<p>We used to have this in Lean 2 (but it would be nice to have cleaner proofs).<br>
<a href="https://github.com/leanprover/lean2/blob/master/library/theories/combinatorics/choose.lean#L208-L220" target="_blank" title="https://github.com/leanprover/lean2/blob/master/library/theories/combinatorics/choose.lean#L208-L220">https://github.com/leanprover/lean2/blob/master/library/theories/combinatorics/choose.lean#L208-L220</a></p>

#### [ Bryan Gin-ge Chen (Nov 19 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147980872):
<blockquote>
<p>You can prove without too much difficulty that <code>sublists_of_length_aux l n f r = (sublists_of_length l n).map f ++ r</code> and then you can prove your equation lemmas as theorems</p>
</blockquote>
<p>Could I get a hint on this step? I'm not sure what to do even to get started:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">sublists_of_length_aux</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="o">(</span><span class="n">list</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">list</span> <span class="n">α</span><span class="o">)</span> <span class="bp">→</span> <span class="n">list</span> <span class="o">(</span><span class="n">list</span> <span class="n">α</span><span class="o">)</span> <span class="bp">→</span> <span class="n">list</span> <span class="o">(</span><span class="n">list</span> <span class="n">α</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">l</span>      <span class="mi">0</span>     <span class="n">f</span> <span class="n">r</span> <span class="o">:=</span> <span class="n">f</span> <span class="o">[]</span> <span class="bp">::</span> <span class="n">r</span>
<span class="bp">|</span> <span class="o">[]</span>     <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="n">f</span> <span class="n">r</span> <span class="o">:=</span> <span class="n">r</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">a</span><span class="bp">::</span><span class="n">l</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="n">f</span> <span class="n">r</span> <span class="o">:=</span> <span class="n">sublists_of_length_aux</span> <span class="n">l</span> <span class="n">n</span> <span class="o">(</span><span class="n">f</span> <span class="err">∘</span> <span class="n">list</span><span class="bp">.</span><span class="n">cons</span> <span class="n">a</span><span class="o">)</span>
  <span class="o">(</span><span class="n">sublists_of_length_aux</span> <span class="n">l</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="n">f</span> <span class="n">r</span><span class="o">)</span>

<span class="n">def</span> <span class="n">sublists_of_length</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">l</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">list</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">sublists_of_length_aux</span> <span class="n">l</span> <span class="n">n</span> <span class="n">id</span> <span class="o">[]</span>

<span class="kn">lemma</span> <span class="n">foo</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">:</span> <span class="bp">∀</span><span class="o">(</span><span class="n">l</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">list</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">list</span> <span class="n">α</span><span class="o">)),</span>
  <span class="n">sublists_of_length_aux</span> <span class="n">l</span> <span class="n">n</span> <span class="n">f</span> <span class="n">r</span> <span class="bp">=</span> <span class="o">(</span><span class="n">sublists_of_length</span> <span class="n">l</span> <span class="n">n</span><span class="o">)</span><span class="bp">.</span><span class="n">map</span> <span class="n">f</span> <span class="bp">++</span> <span class="n">r</span>
<span class="bp">|</span> <span class="n">l</span> <span class="mi">0</span> <span class="n">f</span> <span class="n">r</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="c1">--unfold sublists_of_length_aux,</span>
  <span class="n">sorry</span>
<span class="kn">end</span>
<span class="bp">|</span> <span class="o">[]</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="n">f</span> <span class="n">r</span> <span class="o">:=</span> <span class="n">sorry</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">a</span><span class="bp">::</span><span class="n">l</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="n">f</span> <span class="n">r</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>I was hoping I could make the first one <code>refl</code>, but it seems I need to do something else first, and I'm having trouble working with the definitions.</p>

#### [ Mario Carneiro (Nov 19 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147981987):
<p>ah, it looks like lean did a case split on <code>l</code> first, then <code>n</code>, in the definition of <code>sublists_of_length_aux</code>, so that the first equation isn't true by <code>refl</code> but rather by <code>cases l; refl</code></p>

#### [ Mario Carneiro (Nov 19 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147981997):
<p>you can fix this by swapping the order of the first two arguments to <code>sublists_of_length_aux</code></p>

#### [ Bryan Gin-ge Chen (Nov 19 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147982276):
<p>Cool, that did the trick.</p>

#### [ Mario Carneiro (Nov 19 2018 at 19:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/binomial%20coefficients/near/147982611):
<p>but actually I think you want to generalize the lemma a bit to prove it:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">sublists_of_length_aux</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">list</span> <span class="n">α</span> <span class="bp">→</span> <span class="o">(</span><span class="n">list</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">list</span> <span class="n">α</span><span class="o">)</span> <span class="bp">→</span> <span class="n">list</span> <span class="o">(</span><span class="n">list</span> <span class="n">α</span><span class="o">)</span> <span class="bp">→</span> <span class="n">list</span> <span class="o">(</span><span class="n">list</span> <span class="n">α</span><span class="o">)</span>
<span class="bp">|</span> <span class="mi">0</span>     <span class="n">l</span>      <span class="n">f</span> <span class="n">r</span> <span class="o">:=</span> <span class="n">f</span> <span class="o">[]</span> <span class="bp">::</span> <span class="n">r</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">[]</span>     <span class="n">f</span> <span class="n">r</span> <span class="o">:=</span> <span class="n">r</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span><span class="bp">::</span><span class="n">l</span><span class="o">)</span> <span class="n">f</span> <span class="n">r</span> <span class="o">:=</span> <span class="n">sublists_of_length_aux</span> <span class="n">n</span> <span class="n">l</span> <span class="o">(</span><span class="n">f</span> <span class="err">∘</span> <span class="n">list</span><span class="bp">.</span><span class="n">cons</span> <span class="n">a</span><span class="o">)</span>
  <span class="o">(</span><span class="n">sublists_of_length_aux</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="n">l</span> <span class="n">f</span> <span class="n">r</span><span class="o">)</span>

<span class="n">def</span> <span class="n">sublists_of_length</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">l</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">list</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">sublists_of_length_aux</span> <span class="n">n</span> <span class="n">l</span> <span class="n">id</span> <span class="o">[]</span>

<span class="kn">lemma</span> <span class="n">foo</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">l</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="n">g</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">list</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">r</span> <span class="n">s</span> <span class="o">:</span> <span class="n">list</span> <span class="o">(</span><span class="n">list</span> <span class="n">α</span><span class="o">)),</span>
  <span class="n">sublists_of_length_aux</span> <span class="n">n</span> <span class="n">l</span> <span class="o">(</span><span class="n">g</span> <span class="err">∘</span> <span class="n">f</span><span class="o">)</span> <span class="o">(</span><span class="n">r</span><span class="bp">.</span><span class="n">map</span> <span class="n">g</span> <span class="bp">++</span> <span class="n">s</span><span class="o">)</span> <span class="bp">=</span>
  <span class="o">(</span><span class="n">sublists_of_length_aux</span> <span class="n">n</span> <span class="n">l</span> <span class="n">f</span> <span class="n">r</span><span class="o">)</span><span class="bp">.</span><span class="n">map</span> <span class="n">g</span> <span class="bp">++</span> <span class="n">s</span>
<span class="bp">|</span> <span class="mi">0</span>     <span class="n">l</span>      <span class="n">f</span> <span class="n">g</span> <span class="n">r</span> <span class="n">s</span> <span class="o">:=</span> <span class="n">rfl</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">[]</span>     <span class="n">f</span> <span class="n">g</span> <span class="n">r</span> <span class="n">s</span> <span class="o">:=</span> <span class="n">rfl</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span><span class="bp">::</span><span class="n">l</span><span class="o">)</span> <span class="n">f</span> <span class="n">g</span> <span class="n">r</span> <span class="n">s</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">unfold</span> <span class="n">sublists_of_length_aux</span><span class="bp">;</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">foo</span><span class="o">,</span> <span class="k">show</span> <span class="o">((</span><span class="n">g</span> <span class="err">∘</span> <span class="n">f</span><span class="o">)</span> <span class="err">∘</span> <span class="n">list</span><span class="bp">.</span><span class="n">cons</span> <span class="n">a</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="n">g</span> <span class="err">∘</span> <span class="n">f</span> <span class="err">∘</span> <span class="n">list</span><span class="bp">.</span><span class="n">cons</span> <span class="n">a</span><span class="o">),</span> <span class="k">by</span> <span class="n">refl</span><span class="o">,</span> <span class="n">foo</span><span class="o">]</span>
</pre></div>


<p>The theorem you want is now a simple corollary</p>


{% endraw %}
