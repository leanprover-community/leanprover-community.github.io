---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/81795Whattopologicalspacesdowehave.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [What topological spaces do we have?](https://leanprover-community.github.io/archive/113488general/81795Whattopologicalspacesdowehave.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Mar 28 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20topological%20spaces%20do%20we%20have%3F/near/124293562):
<p>I'm aware that this place does not value examples, just abstract theorems, but do we have R^n? C^n? S^n? D^n?</p>

#### [ Kenny Lau (Mar 28 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20topological%20spaces%20do%20we%20have%3F/near/124293573):
<p>by "this place" I mean Mario</p>

#### [ Mario Carneiro (Mar 28 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20topological%20spaces%20do%20we%20have%3F/near/124295797):
<p>I like examples when they are abstract constructions :)</p>

#### [ Mario Carneiro (Mar 28 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20topological%20spaces%20do%20we%20have%3F/near/124295837):
<p>In this case you're talking about making a topological space out of K^n where K is a topological field or vector space</p>

#### [ Kenny Lau (Mar 28 2018 at 01:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20topological%20spaces%20do%20we%20have%3F/near/124296128):
<p>that's only the first two cases :)</p>

#### [ Mario Carneiro (Mar 28 2018 at 01:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20topological%20spaces%20do%20we%20have%3F/near/124296187):
<p>For S^n and D^n, I would just define them as the appropriate subspaces. There are loads of more abstract definitions of S^n of course, but I would suggest sticking to actual spheres for the definition</p>

#### [ Kenny Lau (Mar 28 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20topological%20spaces%20do%20we%20have%3F/near/124296200):
<p>agreed, but do you have norm?</p>

#### [ Mario Carneiro (Mar 28 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20topological%20spaces%20do%20we%20have%3F/near/124296205):
<p>Patrick had a working definition</p>

#### [ Kenny Lau (Mar 28 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20topological%20spaces%20do%20we%20have%3F/near/124296208):
<p>in R^n?</p>

#### [ Mario Carneiro (Mar 28 2018 at 01:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20topological%20spaces%20do%20we%20have%3F/near/124296255):
<p>Hm, it occurs to me that "the unit sphere" is well defined in any normed vector space</p>

#### [ Kenny Lau (Mar 28 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20topological%20spaces%20do%20we%20have%3F/near/124296260):
<p>for god's sake</p>

#### [ Mario Carneiro (Mar 28 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20topological%20spaces%20do%20we%20have%3F/near/124296266):
<p>Patrick's definition gives a norm on any normed space</p>

#### [ Mario Carneiro (Mar 28 2018 at 01:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20topological%20spaces%20do%20we%20have%3F/near/124296269):
<p>of course R^n will be a normed space</p>

#### [ Mario Carneiro (Mar 28 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20topological%20spaces%20do%20we%20have%3F/near/124296316):
<p>but there is some concern about whether to use the 2-norm vs some other p-norm</p>

#### [ Mario Carneiro (Mar 28 2018 at 01:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20topological%20spaces%20do%20we%20have%3F/near/124296340):
<p>If you just need something quick and dirty for some application, go ahead and define it however you like</p>

#### [ Kenny Lau (Mar 28 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20topological%20spaces%20do%20we%20have%3F/near/124296396):
<p>I don’t need it now</p>

#### [ Mario Carneiro (Mar 28 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20topological%20spaces%20do%20we%20have%3F/near/124296402):
<p>The simplest abstract definition if you only need the topological structure is by iterating the suspension operation on <code>bool</code></p>

#### [ Kenny Lau (Mar 28 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20topological%20spaces%20do%20we%20have%3F/near/124296415):
<p>good luck proving that S^n \ {pt} ~ R^n</p>

#### [ Kenny Lau (Mar 28 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20topological%20spaces%20do%20we%20have%3F/near/124296461):
<p>good luck finding a single point inside</p>

#### [ Mario Carneiro (Mar 28 2018 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20topological%20spaces%20do%20we%20have%3F/near/124296486):
<p>I guess it's not obvious that S^n is homogeneous as the suspension, but it's easy to show S^n \ {north pole} ~ R^n</p>

#### [ Kenny Lau (Mar 28 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20topological%20spaces%20do%20we%20have%3F/near/124296533):
<p>hmm</p>

#### [ Kenny Lau (Mar 28 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20topological%20spaces%20do%20we%20have%3F/near/124296554):
<p>and R^n \ {0} def retracts to S^(n-1)?</p>

#### [ Mario Carneiro (Mar 28 2018 at 02:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20topological%20spaces%20do%20we%20have%3F/near/124296606):
<p>That's dead easy with the suspension, since R^n\{0} maps to S^(n-1) x (0,1)</p>

#### [ Kenny Lau (Mar 28 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20topological%20spaces%20do%20we%20have%3F/near/124296616):
<p>tu ganhas</p>

#### [ Mario Carneiro (Mar 28 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20topological%20spaces%20do%20we%20have%3F/near/124296627):
<p>I agree that homogeneity is easier with the geometric representation, since then you can use orthogonal transformations</p>

#### [ Kenny Lau (Mar 28 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20topological%20spaces%20do%20we%20have%3F/near/124296666):
<p>next time someone asks me what S^n is, I’m gonna say “repeated suspension of bool” <span class="emoji emoji-1f61b" title="stuck out tongue">:stuck_out_tongue:</span></p>

#### [ Kenny Lau (Mar 28 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20topological%20spaces%20do%20we%20have%3F/near/124296681):
<p>they be like “entao o que e bool?”</p>

#### [ Mario Carneiro (Mar 28 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20topological%20spaces%20do%20we%20have%3F/near/124296689):
<p>I think that's the definition the HoTT people use, more or less</p>

#### [ Mario Carneiro (Mar 28 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20topological%20spaces%20do%20we%20have%3F/near/124296702):
<p>Also, if you do repeated suspension on <code>unit</code> you get D^n</p>

#### [ Mario Carneiro (Mar 28 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20topological%20spaces%20do%20we%20have%3F/near/124296746):
<p>or just take [0,1]^n</p>

#### [ Mario Carneiro (Mar 28 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20topological%20spaces%20do%20we%20have%3F/near/124296762):
<p>But for a mathlib definition, I would imagine it will be used in many contexts, not just topological, i.e. you might care about manifold structure in which case "corners" are not appreciated</p>

#### [ Patrick Massot (Mar 28 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20topological%20spaces%20do%20we%20have%3F/near/124309189):
<p>I almost have <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi mathvariant="double-struck">R</mi><mi>n</mi></msup></mrow><annotation encoding="application/x-tex">\mathbb{R}^n</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68889em;"></span><span class="strut bottom" style="height:0.68889em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord"><span class="mord mathbb">R</span></span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span></span></span></span></span></span></span></span> as a topological space. I only need to find one day without a million urgent things to do. I have normed spaces and Pi instances for many things. But indeed the norm we'll have on <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi mathvariant="double-struck">R</mi><mi>n</mi></msup></mrow><annotation encoding="application/x-tex">\mathbb{R}^n</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68889em;"></span><span class="strut bottom" style="height:0.68889em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord"><span class="mord mathbb">R</span></span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span></span></span></span></span></span></span></span> will have box balls, which is not good if you want to get a smooth <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi mathvariant="double-struck">S</mi><mrow><mi>n</mi><mo>−</mo><mn>1</mn></mrow></msup></mrow><annotation encoding="application/x-tex">\mathbb{S}^{n-1}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8141079999999999em;"></span><span class="strut bottom" style="height:0.8141079999999999em;vertical-align:0em;"></span><span class="base"><span class="mord"><span class="mord"><span class="mord mathbb">S</span></span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight">n</span><span class="mbin mtight">−</span><span class="mord mathrm mtight">1</span></span></span></span></span></span></span></span></span></span></span></span>.</p>

#### [ Kenny Lau (Mar 29 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20topological%20spaces%20do%20we%20have%3F/near/124355085):
<p><a href="https://math.stackexchange.com/a/2712786/328173" target="_blank" title="https://math.stackexchange.com/a/2712786/328173">https://math.stackexchange.com/a/2712786/328173</a></p>

#### [ Kenny Lau (Mar 29 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20topological%20spaces%20do%20we%20have%3F/near/124355086):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> this is part of the reason I asked that question</p>

#### [ Kenny Lau (Mar 29 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20topological%20spaces%20do%20we%20have%3F/near/124355089):
<p>if we have enough lemmas we might be able to formalize that</p>


{% endraw %}
