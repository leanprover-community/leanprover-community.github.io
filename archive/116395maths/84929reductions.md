---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/84929reductions.html
---

## Stream: [maths](index.html)
### Topic: [reductions](84929reductions.html)

---


{% raw %}
#### [ Kenny Lau (May 28 2018 at 00:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reductions/near/127179083):
<p>What are alpha, beta, delta, zeta, eta, iota reudctions?</p>

#### [ Andrew Ashworth (May 28 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reductions/near/127179138):
<p><a href="http://www.aplusplus.net/lcintro.pdf" target="_blank" title="http://www.aplusplus.net/lcintro.pdf">http://www.aplusplus.net/lcintro.pdf</a></p>

#### [ Andrew Ashworth (May 28 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reductions/near/127179139):
<p>it might not have some of the fancier reductions, but its got the basics</p>

#### [ Andrew Ashworth (May 28 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reductions/near/127179146):
<p>ncatlab has the rest</p>

#### [ Kenny Lau (May 28 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reductions/near/127179148):
<p>ncatlab :o</p>

#### [ Andrew Ashworth (May 28 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reductions/near/127179191):
<p>i, too, dislike going to ncatlab first, but for some reason the people there really like dtt and hott and so they have a decent encyclopedia of concepts</p>

#### [ Kenny Lau (May 28 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reductions/near/127179193):
<p>i didn't say i don't like ncatlab</p>

#### [ Andrew Ashworth (May 28 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reductions/near/127179200):
<p>heh, cross out my 'too' then</p>

#### [ Mario Carneiro (May 28 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reductions/near/127179341):
<p>the lambda calculus has alpha, beta, eta, and they have the same meaning in DTT</p>

#### [ Mario Carneiro (May 28 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reductions/near/127179349):
<p>delta is definition reduction, replace a definition with its definiens</p>

#### [ Mario Carneiro (May 28 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reductions/near/127179351):
<p>zeta is let reduction, let x := t in s -&gt; s[t/x]</p>

#### [ Mario Carneiro (May 28 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reductions/near/127179361):
<p>iota is for inductive types, a T.rec where the major premise is a constructor of the type</p>

#### [ Mario Carneiro (May 28 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reductions/near/127179403):
<p>actually alpha is not a reduction, and eta is not usually used as a reduction either, they are just equalities</p>

#### [ Mario Carneiro (May 28 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/reductions/near/127179406):
<p>and alpha isn't even needed in lean because de bruijn indices make alpha equivalent expressions syntactically equal</p>


{% endraw %}
