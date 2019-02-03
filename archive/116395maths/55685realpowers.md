---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/55685realpowers.html
---

## Stream: [maths](index.html)
### Topic: [real powers](55685realpowers.html)

---


{% raw %}
#### [ Chris Hughes (Nov 04 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137159650):
<p>If we did <code>has_pow real real</code>, what would <code>(-1)^(1/3)</code> be?</p>

#### [ Kevin Buzzard (Nov 04 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137159654):
<p>nonono</p>

#### [ Kevin Buzzard (Nov 04 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137159696):
<p>real^real is surely not a good idea</p>

#### [ Kevin Buzzard (Nov 04 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137159699):
<p>what would (-1)^(1/4) be?</p>

#### [ Kevin Buzzard (Nov 04 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137159702):
<p>If you want real^real then I would suggest setting <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>a</mi><mi>b</mi></msup><mo>=</mo><mn>0</mn></mrow><annotation encoding="application/x-tex">a^b=0</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.849108em;"></span><span class="strut bottom" style="height:0.849108em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit">a</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.849108em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">b</span></span></span></span></span></span></span></span><span class="mrel">=</span><span class="mord mathrm">0</span></span></span></span> if <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>a</mi><mo>≤</mo><mn>0</mn></mrow><annotation encoding="application/x-tex">a\leq 0</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.64444em;"></span><span class="strut bottom" style="height:0.78041em;vertical-align:-0.13597em;"></span><span class="base"><span class="mord mathit">a</span><span class="mrel">≤</span><span class="mord mathrm">0</span></span></span></span></p>

#### [ Kevin Buzzard (Nov 04 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137159729):
<p>You can make sense of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>a</mi><mi>b</mi></msup></mrow><annotation encoding="application/x-tex">a^b</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.849108em;"></span><span class="strut bottom" style="height:0.849108em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit">a</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.849108em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">b</span></span></span></span></span></span></span></span></span></span></span> for <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>a</mi></mrow><annotation encoding="application/x-tex">a</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">a</span></span></span></span> a positive real and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>b</mi></mrow><annotation encoding="application/x-tex">b</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.69444em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">b</span></span></span></span> any complex number, it should be <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>exp</mi><mo>(</mo><mi>b</mi><mi>log</mi><mo>(</mo><mi>a</mi><mo>)</mo><mo>)</mo></mrow><annotation encoding="application/x-tex">\exp(b\log(a))</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mop">exp</span><span class="mopen">(</span><span class="mord mathit">b</span><span class="mop">lo<span style="margin-right:0.01389em;">g</span></span><span class="mopen">(</span><span class="mord mathit">a</span><span class="mclose">)</span><span class="mclose">)</span></span></span></span></p>

#### [ Johan Commelin (Nov 04 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137159778):
<blockquote>
<p>If you want real^real then I would suggest setting <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>a</mi><mi>b</mi></msup><mo>=</mo><mn>0</mn></mrow><annotation encoding="application/x-tex">a^b=0</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.849108em;"></span><span class="strut bottom" style="height:0.849108em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit">a</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.849108em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">b</span></span></span></span></span></span></span></span><span class="mrel">=</span><span class="mord mathrm">0</span></span></span></span> if <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>a</mi><mo>≤</mo><mn>0</mn></mrow><annotation encoding="application/x-tex">a\leq 0</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.64444em;"></span><span class="strut bottom" style="height:0.78041em;vertical-align:-0.13597em;"></span><span class="base"><span class="mord mathit">a</span><span class="mrel">≤</span><span class="mord mathrm">0</span></span></span></span></p>
</blockquote>
<p>I am quite sure you made a typo. That should have been <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>a</mi><mi>b</mi></msup><mo>=</mo><mn>3</mn><mn>7</mn></mrow><annotation encoding="application/x-tex">a^b = 37</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.849108em;"></span><span class="strut bottom" style="height:0.849108em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit">a</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.849108em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">b</span></span></span></span></span></span></span></span><span class="mrel">=</span><span class="mord mathrm">3</span><span class="mord mathrm">7</span></span></span></span>.</p>

#### [ Kevin Buzzard (Nov 04 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137159779):
<p>you can make sense of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>a</mi><mi>b</mi></msup></mrow><annotation encoding="application/x-tex">a^b</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.849108em;"></span><span class="strut bottom" style="height:0.849108em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit">a</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.849108em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">b</span></span></span></span></span></span></span></span></span></span></span> for <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>a</mi></mrow><annotation encoding="application/x-tex">a</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">a</span></span></span></span> any non-zero complex number and <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>b</mi></mrow><annotation encoding="application/x-tex">b</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.69444em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">b</span></span></span></span> any integer</p>

#### [ Kevin Buzzard (Nov 04 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137159784):
<p>I would have put 37 but maybe <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mn>0</mn><mrow><mn>3</mn><mn>7</mn></mrow></msup></mrow><annotation encoding="application/x-tex">0^{37}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8141079999999999em;"></span><span class="strut bottom" style="height:0.8141079999999999em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathrm">0</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">3</span><span class="mord mathrm mtight">7</span></span></span></span></span></span></span></span></span></span></span></span> should be 0...</p>

#### [ Johannes Hölzl (Nov 04 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137161598):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span>  the usual thing: we totalize it. I think for <code>log</code> we can force it to by symmetric. either a long the <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>y</mi></mrow><annotation encoding="application/x-tex">y</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.625em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.03588em;">y</span></span></span></span>-axis, or through the origin. For power on <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mi mathvariant="double-struck">R</mi></mrow></mrow><annotation encoding="application/x-tex">\mathbb{R}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68889em;"></span><span class="strut bottom" style="height:0.68889em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathbb">R</span></span></span></span></span> you might want to have <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>a</mi><mi>b</mi></msup><mo>=</mo><mi mathvariant="normal">∣</mi><mi>a</mi><msup><mi mathvariant="normal">∣</mi><mi>b</mi></msup></mrow><annotation encoding="application/x-tex">a^b = |a|^b</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.849108em;"></span><span class="strut bottom" style="height:1.099108em;vertical-align:-0.25em;"></span><span class="base"><span class="mord"><span class="mord mathit">a</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.849108em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">b</span></span></span></span></span></span></span></span><span class="mrel">=</span><span class="mord mathrm">∣</span><span class="mord mathit">a</span><span class="mord"><span class="mord mathrm">∣</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.849108em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">b</span></span></span></span></span></span></span></span></span></span></span> or similar, and of course <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mn>0</mn><mi>a</mi></msup><mo>=</mo><mn>0</mn></mrow><annotation encoding="application/x-tex">0^a = 0</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.664392em;"></span><span class="strut bottom" style="height:0.664392em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathrm">0</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">a</span></span></span></span></span></span></span></span><span class="mrel">=</span><span class="mord mathrm">0</span></span></span></span>.</p>

#### [ Chris Hughes (Nov 04 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137161689):
<p>Don't we want <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mn>0</mn><mn>0</mn></msup><mo>=</mo><mn>1</mn></mrow><annotation encoding="application/x-tex">0^0 = 1</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8141079999999999em;"></span><span class="strut bottom" style="height:0.8141079999999999em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathrm">0</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">0</span></span></span></span></span></span></span></span><span class="mrel">=</span><span class="mord mathrm">1</span></span></span></span>?</p>

#### [ Kevin Buzzard (Nov 04 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137161736):
<p>I think you want 0^0 = undefined if both those 0's are real numbers</p>

#### [ Johannes Hölzl (Nov 04 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137161738):
<p>I don't think there is a natural choice to totalize it. Theorems about <code>log</code> and <code>pow</code> will always assume that the argument is non-negative.</p>

#### [ Kevin Buzzard (Nov 04 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137161741):
<p>and undefined := 0 in Lean</p>

#### [ Johannes Hölzl (Nov 04 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137161742):
<p>Undefined means we are free to choose a value</p>

#### [ Johannes Hölzl (Nov 04 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137161748):
<p>and maybe for <code>pow</code>, <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mn>0</mn><mn>0</mn></msup><mo>=</mo><mn>1</mn></mrow><annotation encoding="application/x-tex">0^0 = 1</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8141079999999999em;"></span><span class="strut bottom" style="height:0.8141079999999999em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathrm">0</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">0</span></span></span></span></span></span></span></span><span class="mrel">=</span><span class="mord mathrm">1</span></span></span></span> makes more sense. I don't know.</p>

#### [ Kevin Buzzard (Nov 04 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137161749):
<p>There's certainly a case for (0 : real) ^ (0 : nat) = 1</p>

#### [ Johannes Hölzl (Nov 04 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137161766):
<p>Yes: <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>a</mi><mrow><mi>n</mi><mo>:</mo><mrow><mi mathvariant="double-struck">R</mi></mrow></mrow></msup><mo>=</mo><msup><mi>a</mi><mi>n</mi></msup></mrow><annotation encoding="application/x-tex">a^{n : \mathbb{R}}= a^n</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.845223em;"></span><span class="strut bottom" style="height:0.845223em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord mathit">a</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.845223em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">n</span><span class="mrel mtight">:</span><span class="mord mtight"><span class="mord mathbb mtight">R</span></span></span></span></span></span></span></span></span></span><span class="mrel">=</span><span class="mord"><span class="mord mathit">a</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span></span></span></span></span></span></span></span> should hold</p>

#### [ Johannes Hölzl (Nov 04 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137161813):
<p>so 'real'-power should extend 'int'-power should extend 'nat'-power</p>

#### [ Chris Hughes (Nov 04 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137161815):
<p>But that doesn't work if <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>a</mi><mi>n</mi></msup><mo>=</mo><mo>∣</mo><mi>a</mi><msup><mo>∣</mo><mi>n</mi></msup></mrow><annotation encoding="application/x-tex">a^n = \mid a\mid^n</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord"><span class="mord mathit">a</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span></span></span></span></span><span class="mrel">=</span><span class="mrel">∣</span><span class="mord mathit">a</span><span class="mrel"><span class="mrel">∣</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span></span></span></span></span></span></span></span></p>

#### [ Mario Carneiro (Nov 04 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137161933):
<p>0^a = 0 unless a = 0, otherwise 1</p>

#### [ Johannes Hölzl (Nov 04 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137161973):
<p>right it doesn't extend <code>int</code>-power. And I don't see a sensible default where it would. we could check if <code>floor</code> or <code>ceil</code> of the argument is odd/even, but this feels too forced</p>

#### [ Mario Carneiro (Nov 04 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137161979):
<p>I have this in the metamath definition, with the if and everything</p>

#### [ Mario Carneiro (Nov 04 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137161985):
<p>for negative powers I used complexes, because there was only one definition complex ^ complex, of course that's not an option here</p>

#### [ Chris Hughes (Nov 04 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137161999):
<p>In metamath is <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>(</mo><mo>−</mo><mn>1</mn><msup><mo>)</mo><mrow><mn>1</mn><mi mathvariant="normal">/</mi><mn>3</mn></mrow></msup><mo>=</mo><mo>−</mo><mn>1</mn></mrow><annotation encoding="application/x-tex">(-1)^{1/3} = -1</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8879999999999999em;"></span><span class="strut bottom" style="height:1.138em;vertical-align:-0.25em;"></span><span class="base"><span class="mopen">(</span><span class="mord">−</span><span class="mord mathrm">1</span><span class="mclose"><span class="mclose">)</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8879999999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">1</span><span class="mord mathrm mtight">/</span><span class="mord mathrm mtight">3</span></span></span></span></span></span></span></span></span><span class="mrel">=</span><span class="mord">−</span><span class="mord mathrm">1</span></span></span></span></p>

#### [ Mario Carneiro (Nov 04 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162004):
<p>no, it's e^2pi i/3</p>

#### [ Kevin Buzzard (Nov 04 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162052):
<p>that ain't no real</p>

#### [ Mario Carneiro (Nov 04 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162057):
<p>like I said, complex</p>

#### [ Mario Carneiro (Nov 04 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162065):
<p>I don't think we should try for the rational extension, it's crazy and not at all complete</p>

#### [ Johannes Hölzl (Nov 04 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162066):
<p>okay, what about using <code>a^b = Re (a ^ b)</code>?</p>

#### [ Kevin Buzzard (Nov 04 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162072):
<p>You want to define the Riemann Zeta function for complex s with Re(s)&gt;1 as the infinite sum of n^{-s}</p>

#### [ Johannes Hölzl (Nov 04 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162080):
<p>where the left one is on reals and right of the equality is the complex power?</p>

#### [ Mario Carneiro (Nov 04 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162087):
<p>that could work...</p>

#### [ Johannes Hölzl (Nov 04 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162091):
<p>AFAIU it is an extension of <code>int</code>-power  and it is continuous</p>

#### [ Mario Carneiro (Nov 04 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162136):
<p>except of course where it isn't</p>

#### [ Mario Carneiro (Nov 04 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162167):
<p>I think the power function is discontinuous at 0,0 no matter what you do</p>

#### [ Johannes Hölzl (Nov 04 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162175):
<p>argh, yes</p>

#### [ Kevin Buzzard (Nov 04 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162176):
<p>not if you restrict the power to be in nat</p>

#### [ Mario Carneiro (Nov 04 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162187):
<p>and there is probably a branch cut somewhere that will survive in the real version</p>

#### [ Kevin Buzzard (Nov 04 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162188):
<p>for example, when evaluating a polynomial, it's essential that x^0 gets sent to 1</p>

#### [ Kevin Buzzard (Nov 04 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162190):
<p>but that 0 is 0:nat</p>

#### [ Mario Carneiro (Nov 04 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162193):
<p>right, I am 100% of the view that 0^0 = 1</p>

#### [ Kevin Buzzard (Nov 04 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162199):
<p>but my point is that this makes things continuous in this domain of real x nat -&gt; real</p>

#### [ Kevin Buzzard (Nov 04 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162239):
<p>oh</p>

#### [ Mario Carneiro (Nov 04 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162240):
<p>a lot of crazy mathematicians use "everything is continuous" ism to justify claiming that it is undefined there</p>

#### [ Johannes Hölzl (Nov 04 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162244):
<p>in this case one wants to use <code>pow : nat -&gt; real -&gt; real</code> anyway. I think the case we are discussing now is how to define <code>pow : real -&gt; real -&gt; real</code></p>

#### [ Kevin Buzzard (Nov 04 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162248):
<p>but one issue is whether it should extend the nat version</p>

#### [ Mario Carneiro (Nov 04 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162251):
<p>of course, that should be easy</p>

#### [ Johannes Hölzl (Nov 04 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162261):
<p>I agree, it should extend the <code>nat</code>-version. and it would be nice if we could extend the <code>int</code> version in a sensible way</p>

#### [ Mario Carneiro (Nov 04 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162262):
<p>extending int should also be possible</p>

#### [ Kevin Buzzard (Nov 04 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162266):
<p>I know a lot of crazy computer scientists use "everything must extend what we already have in every case even if answers are junk"ism...</p>

#### [ Mario Carneiro (Nov 04 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162273):
<p>extending to rat is possible but a bad idea in my view</p>

#### [ Kevin Buzzard (Nov 04 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162274):
<p>I think (0 : real) ^ (0 : real) is junk so should be 0</p>

#### [ Mario Carneiro (Nov 04 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162278):
<p>lolno</p>

#### [ Kevin Buzzard (Nov 04 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162315):
<p>but (0 : real) ^ (0 : nat) is not junk so should be 1</p>

#### [ Chris Hughes (Nov 04 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162322):
<p>Noooo</p>

#### [ Kevin Buzzard (Nov 04 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162329):
<p>:-)</p>

#### [ Johannes Hölzl (Nov 04 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162331):
<p>we don't extend everything. In Isabelle the logarithm of a negative argument is undefined in the sense of a fixed but unknown value</p>

#### [ Chris Hughes (Nov 04 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162335):
<p>But then <code>cast_pow</code> requires proving things are non zero.</p>

#### [ Mario Carneiro (Nov 04 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162343):
<p>I was not sure about log of negatives either</p>

#### [ Mario Carneiro (Nov 04 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162348):
<p>log of 0 is even worse</p>

#### [ Kevin Buzzard (Nov 04 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162349):
<p>junk!</p>

#### [ Kevin Buzzard (Nov 04 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162352):
<p>37</p>

#### [ Mario Carneiro (Nov 04 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162359):
<p>log x = log |x| makes some calculus stuff very slightly slicker</p>

#### [ Mario Carneiro (Nov 04 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162408):
<p>but I don't think it will come up much anyway</p>

#### [ Johannes Hölzl (Nov 04 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162409):
<p>What about <code>sgn x * log |x|</code>?  I think both have their advantages/disadvantages.</p>

#### [ Mario Carneiro (Nov 04 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162412):
<p>whoa</p>

#### [ Mario Carneiro (Nov 04 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162415):
<p>what is that for?</p>

#### [ Mario Carneiro (Nov 04 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162430):
<p>it looks cool on the graph paper in my head...</p>

#### [ Johannes Hölzl (Nov 04 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162481):
<p>I think there were some cases where it could have been helpful. But I don't remember the exact statements where it would save some non-negativity assumption. But yes the graph looks nice :-)</p>

#### [ Johannes Hölzl (Nov 04 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162601):
<p>But <code>x /= 0 -&gt; y /= 0 -&gt; log (x * y) = log x + log y</code> only works for the <code>log x = log |x|</code> case</p>

#### [ Kevin Buzzard (Nov 04 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162613):
<p>that's a junk theorem!</p>

#### [ Kevin Buzzard (Nov 04 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162668):
<p>This islike you trying to figure out what the square root of anegative number should be so that sqrt(ab)=sqrt(a)sqrt(b) always works. Nobody who wants to apply that theorem will have a,b&lt;0</p>

#### [ Mario Carneiro (Nov 04 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162682):
<p>sometimes a,b&gt;0 but it's a hassle to prove</p>

#### [ Kevin Buzzard (Nov 04 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162687):
<p>you can't say "x != 0" is any better than "x &gt; 0". It's still a precondition, so tehe user has to supply something</p>

#### [ Johannes Hölzl (Nov 04 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162700):
<p>but sometimes <code>x !=0</code> is easier to proof than <code>x &gt; 0</code>.</p>

#### [ Kevin Buzzard (Nov 04 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162712):
<p><em>boggle</em></p>

#### [ Mario Carneiro (Nov 04 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162752):
<p>I mean it is literally a weaker hypothesis</p>

#### [ Kevin Buzzard (Nov 04 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162753):
<p>if you're in a situation where you're taking logs and you don't have x&gt;0 as a hypothesis then something is seriously wrong with your local context anyway</p>

#### [ Chris Hughes (Nov 04 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162756):
<p>Proving things are <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>&gt;</mo><mn>0</mn></mrow><annotation encoding="application/x-tex">&gt;0</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.64444em;"></span><span class="strut bottom" style="height:0.68354em;vertical-align:-0.0391em;"></span><span class="base"><span class="mrel">&gt;</span><span class="mord mathrm">0</span></span></span></span> is cheap on paper but expensive in lean. Keeping track of which theorems are randomly true for some non-intuitive definition is cheap in Lean but expensive on paper.</p>

#### [ Mario Carneiro (Nov 04 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162764):
<p>you had it in your context once, then you did 5 rewrites and it's not obviously true any more</p>

#### [ Kevin Buzzard (Nov 04 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162781):
<p>I did see that in a 1st year's code recently -- "let H2 := H,..." and I thought "wooah what is this fool doing?" and then I understood that they wanted to rewrite H but keep track of it anyway</p>

#### [ Mario Carneiro (Nov 04 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162834):
<p>those could be some combination of rewrites to the log(s) and rewrites to the hypothesis too</p>

#### [ Mario Carneiro (Nov 04 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162843):
<p>What are the preconditions to <code>log (log (log x + 1)) &lt; 3</code>?</p>

#### [ Kevin Buzzard (Nov 04 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162849):
<p>x&gt;&gt;0</p>

#### [ Mario Carneiro (Nov 04 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162897):
<p>but not too &gt;&gt; or else it won't be <code>&lt; 3</code> :)</p>

#### [ Kevin Buzzard (Nov 04 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162907):
<p>If it's too &gt;&gt; then it's false. If it's not &gt;&gt; enough then it makes no sense</p>

#### [ Kevin Buzzard (Nov 04 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162919):
<p>it's NaN</p>

#### [ Mario Carneiro (Nov 04 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162921):
<p>unfortunately (or fortunately), <code>real</code> has no NaN</p>

#### [ Mario Carneiro (Nov 04 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162928):
<p>just ask anyone who has dealt with IEEE floats, NaN is a mess</p>

#### [ Kevin Buzzard (Nov 04 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162929):
<p>If you say to a mathematician "this is true for x=20" they will assume you mean that the LHS evaluates to something meaningful in maths</p>

#### [ Mario Carneiro (Nov 04 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162970):
<p>right, and that's one of the more expensive in lean things to do</p>

#### [ Mario Carneiro (Nov 04 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162980):
<p>you might think "we could just have preconditions on <code>log</code> and then it would all make sense" but that would just make the problem worse</p>

#### [ Kevin Buzzard (Nov 04 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137162987):
<p>I think we need a <code>with_NaN</code> structure</p>

#### [ Mario Carneiro (Nov 04 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137163030):
<p><code>with_bot</code>?</p>

#### [ Kevin Buzzard (Nov 04 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137163033):
<p>but it might not be a bottom</p>

#### [ Mario Carneiro (Nov 04 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137163035):
<p>or equal to itself..</p>

#### [ Kevin Buzzard (Nov 04 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137163043):
<p>well obviously we'd have to modify eq</p>

#### [ Mario Carneiro (Nov 04 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137163045):
<p>obviously</p>

#### [ Kevin Buzzard (Nov 04 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137163057):
<p>we need not_a_Type</p>

#### [ Kevin Buzzard (Nov 04 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137163064):
<p>or not_a_term or something</p>

#### [ Mario Carneiro (Nov 04 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137163122):
<p>it was silly of us to assume that all types have a reflexive relation... we should generalize to semitypes</p>

#### [ Kevin Buzzard (Nov 04 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137163129):
<p>rofl that's clearly what these guys have been missing for the last 100 years</p>

#### [ Kevin Buzzard (Nov 04 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137163140):
<p>we realised we needed semimodules</p>

#### [ Kevin Buzzard (Nov 04 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137163145):
<p>it was only a matter of time before we had the real breakthrough</p>

#### [ Mario Carneiro (Nov 04 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137163172):
<p>I joke, but PERs (partial equivalence relations) as types are a thing</p>

#### [ Mario Carneiro (Nov 04 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137163177):
<p>nuprl uses it</p>

#### [ Kevin Buzzard (Nov 04 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137163181):
<p>is that where you drop reflexivity?</p>

#### [ Mario Carneiro (Nov 04 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137163183):
<p>yeah</p>

#### [ Kevin Buzzard (Nov 04 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137163222):
<p>so you get equivalence classes and then some wasteland</p>

#### [ Kevin Buzzard (Nov 04 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137163229):
<p>of terms which are related to nothing</p>

#### [ Mario Carneiro (Nov 04 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137163236):
<p>it's just an equivalence relation on a subtype</p>

#### [ Kevin Buzzard (Nov 04 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137163238):
<p>right</p>

#### [ Mario Carneiro (Nov 04 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137163245):
<p>In type theory it has the purpose of rolling subtyping and quotients into one construct</p>

#### [ Mario Carneiro (Nov 04 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/real%20powers/near/137163259):
<p>so you get some nice categorical structure</p>


{% endraw %}
