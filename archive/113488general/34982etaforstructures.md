---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/34982etaforstructures.html
---

## Stream: [general](index.html)
### Topic: [eta for structures](34982etaforstructures.html)

---


{% raw %}
#### [ Reid Barton (Aug 01 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eta%20for%20structures/near/130734097):
<p>Is definitional eta for structures something we are likely to get at some point?</p>

#### [ Gabriel Ebner (Aug 01 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eta%20for%20structures/near/130734176):
<p>I'd be surprised.</p>

#### [ Reid Barton (Aug 01 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eta%20for%20structures/near/130734254):
<p>In the absence of eta, another feature request would be "lazy matching" in lambdas and lets</p>

#### [ Reid Barton (Aug 01 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eta%20for%20structures/near/130734272):
<p>analogous to ~ patterns in Haskell</p>

#### [ Gabriel Ebner (Aug 01 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eta%20for%20structures/near/130734477):
<p>For everyone else, this means <code>λ \&lt;x,y\&gt;, x + y</code> gets desugared to <code>λ p, p.1 + p.2</code>.  I don't think it is planned, but you might be able to do the desugaring yourself.</p>

#### [ Reid Barton (Aug 01 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eta%20for%20structures/near/130734478):
<p>There are some definitions in data.equiv for example which I can't use conveniently, because they match on the input equivalence before producing a constructor.</p>

#### [ Reid Barton (Aug 01 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eta%20for%20structures/near/130734545):
<p>But rewriting them with the constructor outermost becomes quite ugly.</p>

#### [ Reid Barton (Aug 01 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eta%20for%20structures/near/130734638):
<p>(not at computer, and don't remember the specific names)</p>

#### [ Reid Barton (Aug 01 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eta%20for%20structures/near/130734813):
<p>Was imagining including a ~ in the syntax for lazy patterns, not changing the current semantics.</p>

#### [ Reid Barton (Aug 01 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eta%20for%20structures/near/130735589):
<p>Though I wonder when you would ever want the "strict" version, figuratively speaking.</p>

#### [ Patrick Massot (Aug 01 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eta%20for%20structures/near/130742044):
<blockquote>
<p>For everyone else, this means <code>λ \&lt;x,y\&gt;, x + y</code> gets desugared to <code>λ p, p.1 + p.2</code>.  I don't think it is planned, but you might be able to do the desugaring yourself.</p>
</blockquote>
<p>+1 I keep trying to type that and being disappointed.</p>

#### [ Mario Carneiro (Aug 04 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eta%20for%20structures/near/130879441):
<p>Someone recently pointed out a mathlib definition that uses case analysis like this that was causing problems, but now I can't find it. Can anyone else find it?</p>

#### [ Chris Hughes (Aug 04 2018 at 09:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eta%20for%20structures/near/130880063):
<p><code>+</code> and <code>*</code> in localization.</p>

#### [ Mario Carneiro (Aug 04 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eta%20for%20structures/near/130880926):
<p>are you sure? I don't see that when I search in the chat</p>

#### [ Chris Hughes (Aug 04 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eta%20for%20structures/near/130881181):
<p>I definitely made a comment about it, but there's probably something else as well.</p>

#### [ Chris Hughes (Aug 04 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eta%20for%20structures/near/130881189):
<p><a href="#narrow/stream/113488-general/subject/match.20in.20defs" title="#narrow/stream/113488-general/subject/match.20in.20defs">https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/match.20in.20defs</a></p>

#### [ Mario Carneiro (Aug 04 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eta%20for%20structures/near/130881304):
<p>ah, okay (I searched for "localization")</p>

#### [ Kenny Lau (Oct 10 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eta%20for%20structures/near/135568699):
<p>Should we replace those definitions with the better definitions?</p>


{% endraw %}
