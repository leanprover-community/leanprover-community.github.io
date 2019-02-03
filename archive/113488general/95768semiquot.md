---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/95768semiquot.html
---

## Stream: [general](index.html)
### Topic: [semiquot](95768semiquot.html)

---


{% raw %}
#### [ Mario Carneiro (May 09 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiquot/near/126308546):
<p>A minor advertisement for <code>data/semiquot</code> because I think it's a cool idea. I've mentioned this approach before, but this data type makes it easy to work with nondeterministic functions using quotient types.</p>
<p>An application is in <code>fp/basic</code>, floating point numbers. Previously, we had to keep track of messy NaN payload data, which is not reliably handled across different processors, causing some unavoidable nondeterminism. Now, there is only one NaN value, and functions that leak NaN payload data (like <code>float.sign</code>) are <code>semiquot</code> so that they are allowed to return anything in that case. (We don't currently have a <code>float.bits</code> function that gives the bitwise representation of a float, but that would of course leak NaN payload data so it would also be <code>semiquot</code>.)</p>

#### [ Patrick Massot (May 09 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiquot/near/126309020):
<p>Is this meant only for programming or could be useful for maths?</p>

#### [ Mario Carneiro (May 09 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiquot/near/126309082):
<p>It has some interesting mathematical structure, being an ordered monad with some filter-like closure properties, but in classical lean it is equivalent to the collection of nonempty subsets of A</p>

#### [ Mario Carneiro (May 09 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiquot/near/126309145):
<p>It's most interesting when viewed constructively</p>

#### [ Patrick Massot (May 09 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiquot/near/126309153):
<p>Ok, thanks for confirming I was not in the target audience of this message.</p>

#### [ Mario Carneiro (May 09 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiquot/near/126309234):
<p>I think the correct answer is it is meant for <em>verified</em> programming, which of course involves both programming and math, but the math is probably not so interesting to you</p>

#### [ Patrick Massot (May 09 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/semiquot/near/126311762):
<p>Thanks for the advertisement anyway, I think it's a good idea to advertise each new stuff in mathlib here</p>


{% endraw %}
