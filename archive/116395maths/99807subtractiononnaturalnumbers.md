---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/99807subtractiononnaturalnumbers.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [subtraction on natural numbers](https://leanprover-community.github.io/archive/116395maths/99807subtractiononnaturalnumbers.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Simon Hudon (Apr 11 2018 at 04:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124913490):
<p>Is there a name and notation to distinguish between subtraction on natural numbers and subtraction on integers? This is for my dissertation rather than a Lean proof</p>

#### [ Mario Carneiro (Apr 11 2018 at 04:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124914007):
<p>Subtraction on natural numbers is sometimes called "monus" and denoted with a subtraction sign with a dot over it, like the top half of an american division sign</p>

#### [ Mario Carneiro (Apr 11 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124914047):
<p>like so: ∸</p>

#### [ Simon Hudon (Apr 11 2018 at 04:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124914053):
<p>Thanks! Is there a LaTeX command for that?</p>

#### [ Mario Carneiro (Apr 11 2018 at 04:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124914058):
<p>wiki says <code>\dot -</code></p>

#### [ Mario Carneiro (Apr 11 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124914101):
<p>you will probably have to play with spacing to get it to look nice</p>

#### [ Simon Hudon (Apr 11 2018 at 04:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124914108):
<p>Alright then</p>

#### [ Patrick Massot (Apr 11 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124920713):
<p>Short answer: use <code>unicode-math</code> and type ∸<br>
Long answer: if for some reason, you don't want to use <code>unicode-math</code>, use its documentation: <a href="http://mirrors.ctan.org/macros/latex/contrib/unicode-math/unimath-symbols.pdf" target="_blank" title="http://mirrors.ctan.org/macros/latex/contrib/unicode-math/unimath-symbols.pdf">http://mirrors.ctan.org/macros/latex/contrib/unicode-math/unimath-symbols.pdf</a> search for "dot above" and get to page 17 where you see that ∸ is translated to <code>\dotminus</code>.  The problem is that you need to find which package defines this (an information which is irrelevant if you go with unicode-math). Very quick google latex dotminus brings: <a href="https://tex.stackexchange.com/questions/360069/what-symbol-for-primitive-recursive-cutoff-minus" target="_blank" title="https://tex.stackexchange.com/questions/360069/what-symbol-for-primitive-recursive-cutoff-minus">https://tex.stackexchange.com/questions/360069/what-symbol-for-primitive-recursive-cutoff-minus</a></p>

#### [ Patrick Massot (Apr 11 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124920758):
<p>Actually maybe using this symbol in Lean could make sense</p>

#### [ Patrick Massot (Apr 11 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124920760):
<p>It would help mathematicians notice this is not the right operation</p>

#### [ Kevin Buzzard (Apr 11 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124920768):
<p>I think there's an argument for using some sort of modification on all the total extensions of the usual functions as well ;-)</p>

#### [ Mario Carneiro (Apr 11 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124920771):
<p>It's a thought, but I'd hate to have to explain to newcomers why <code>3 - 2 = 1</code> doesn't work</p>

#### [ Patrick Massot (Apr 11 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124920777):
<p>Yeah, this is not great either</p>

#### [ Patrick Massot (Apr 11 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124920779):
<p>Can we have both?</p>

#### [ Kevin Buzzard (Apr 11 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124920780):
<p>Yes but I have to explain why 2 - 3 gets evaluated as something wrong, which is worse</p>

#### [ Patrick Massot (Apr 11 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124920822):
<p>Like, the lib uses the funny symbol but users can still use -</p>

#### [ Patrick Massot (Apr 11 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124920824):
<p>And when they complain about 2 - 3 we tell them about ∸</p>

#### [ Patrick Massot (Apr 11 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124920825):
<p>I don't know</p>

#### [ Kevin Buzzard (Apr 11 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124920826):
<p>I am not seriously advocating changes to <code>-</code> and <code>/</code>, however it was the realisation that I could think about them in this way which made me realise that the "make it total" system would not lead to contradictions.</p>

#### [ Mario Carneiro (Apr 11 2018 at 08:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124920827):
<p>It's in core, so this isn't changing anyway</p>

#### [ Mario Carneiro (Apr 11 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124920832):
<p>this would break too much of the "programming" part of lean I think</p>

#### [ Kevin Buzzard (Apr 11 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124920835):
<p>Maybe obscure unicode characters which look the same and can be redefined by users is the best option :-)</p>

#### [ Mario Carneiro (Apr 11 2018 at 08:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124920837):
<p>it would be hard to support a separate notation without a separate constant, and that would then mess up simp lemmas and such</p>

#### [ Mario Carneiro (Apr 11 2018 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124920885):
<p>It's plausible that you could make a local notation (for <code>@has_sub.sub nat _</code>) work</p>

#### [ Mario Carneiro (Apr 11 2018 at 08:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124920948):
<p>My favorite way to reason about <code>2 - 3</code> is to consider that <code>2 - 3 : nat</code> (since <code>-</code> is a binary op on <code>nat</code>) so it can't possibly be the "right" answer. Now just consider, what's the next best option?</p>

#### [ Mario Carneiro (Apr 11 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/subtraction%20on%20natural%20numbers/near/124920993):
<p>I think it suffices to just remind people that this isn't a partial function</p>


{% endraw %}
