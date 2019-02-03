---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/07525digits.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [digits](https://leanprover-community.github.io/archive/116395maths/07525digits.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Feb 02 2019 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/digits/near/157416565):
<p>The students at Imperial do random maths in Lean. I run a puzzle-solving club where we look at recreational questions involving things such as digit sums of integers. In my 1st year exam last year there is a question about decimal expansions, where we needed to know for example that <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mn>7</mn><mn>1</mn><mi mathvariant="normal">/</mi><mn>1</mn><mn>0</mn><mn>0</mn></mrow><annotation encoding="application/x-tex">71/100</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathrm">7</span><span class="mord mathrm">1</span><span class="mord mathrm">/</span><span class="mord mathrm">1</span><span class="mord mathrm">0</span><span class="mord mathrm">0</span></span></span></span> had no 8's in its decimal expansion. As far as I know there is no way of getting the $$n$$th decimal digit of a natural, or the $$n$$th digit after the decimal point of a real number, in mathlib. I need this stuff now (for example to formalise the questions and solutions on last year's M1F paper). Is this sort of nonsense the sort of thing which should go into mathlib or should I just make my own little library? I don't mind either way, it just occurs to me that whilst I am clear in my opinions that most undergraduate level pure maths is a very natural target for mathlib (indeed I think that the more undergraduate level pure maths is in mathlib, the more pure mathematicians will take Lean seriously), I am less clear about this fringe stuff. It's easy to write (indeed I've written it) but I now don't quite know what to do with it.</p>

#### [ Patrick Massot (Feb 02 2019 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/digits/near/157416619):
<p>I would say we want mathlib to be ready to formalize such questions, but we don't want the questions and their answers</p>

#### [ Mario Carneiro (Feb 02 2019 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/digits/near/157417060):
<p>A function <code>nat -&gt; list (fin b)</code> giving the base-b expansion of a nat seems like a good idea for mathlib</p>

#### [ Mario Carneiro (Feb 02 2019 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/digits/near/157417111):
<p>probably you want the digits to come out in reverse order though</p>

#### [ Mario Carneiro (Feb 02 2019 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/digits/near/157417170):
<p>I would avoid fixation on base 10 though, for most of the functions and especially the theory</p>

#### [ Kevin Buzzard (Feb 02 2019 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/digits/near/157417852):
<p>I did develop a general base b theory but lots of results needed b&gt;=2 so in the end I got bored and switched to 10.</p>

#### [ Kevin Buzzard (Feb 02 2019 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/digits/near/157417915):
<p>On the other hand I never needed induction on b :-) so maybe I should have persevered. Proving things like "all the digits of b^N - 1 are b-1" was horrible but this was perhaps part of the recreation, not the library part</p>

#### [ Kevin Buzzard (Feb 02 2019 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/digits/near/157417958):
<p>It was nat subtraction hell</p>

#### [ Kevin Buzzard (Feb 02 2019 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/digits/near/157417977):
<p>Yes, reverse order was far easier to work with in practice. I wanted results about things like sum of last digits</p>

#### [ Mario Carneiro (Feb 02 2019 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/digits/near/157418165):
<p>I agree that <code>b &gt;= 2</code> is a natural restriction in this context (although there is a useful thing to do for <code>b = 1</code> as well)</p>

#### [ Mario Carneiro (Feb 02 2019 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/digits/near/157418241):
<p>for <code>b^N - 1</code> I would try to rewrite it as <code>k + k*b+... +k*b^(N-1)</code> where <code>b = k+1</code></p>

#### [ Bryan Gin-ge Chen (Feb 02 2019 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/digits/near/157425328):
<p>For nats, isn't there <a href="https://github.com/leanprover/lean/blob/ceacfa7445953cbc8860ddabc55407430a9ca5c3/library/init/data/repr.lean#L85" target="_blank" title="https://github.com/leanprover/lean/blob/ceacfa7445953cbc8860ddabc55407430a9ca5c3/library/init/data/repr.lean#L85">to_digits</a>?</p>

#### [ Kevin Buzzard (Feb 02 2019 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/digits/near/157425383):
<p>For <code>repr</code> yes, but that's the wrong way round :-)</p>

#### [ Kevin Buzzard (Feb 02 2019 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/digits/near/157425390):
<p>Oh, no it's not!</p>

#### [ Kevin Buzzard (Feb 02 2019 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/digits/near/157425393):
<p>the reversal takes place in <code>repr</code>.</p>


{% endraw %}
