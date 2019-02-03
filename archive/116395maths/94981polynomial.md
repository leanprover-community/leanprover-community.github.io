---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/94981polynomial.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [polynomial](https://leanprover-community.github.io/archive/116395maths/94981polynomial.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Jul 19 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/polynomial/near/129921310):
<p>What's happening with polynomials? I see ce990c59d authored by Chris and merged by Johannes but PR171 is still open and active</p>

#### [ Mario Carneiro (Jul 19 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/polynomial/near/129921367):
<p>I think Johannes is currently working on merging the Mason Stothers work with Chris's</p>

#### [ Patrick Massot (Jul 19 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/polynomial/near/129921787):
<p>That's really nice</p>

#### [ Patrick Massot (Jul 19 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/polynomial/near/129921893):
<p>It's really important part of elementary maths that was missing.</p>

#### [ Patrick Massot (Jul 19 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/polynomial/near/129921961):
<p>It makes me think of my normed space work again. Do you think I should PR <a href="https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/norms.lean" target="_blank" title="https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/norms.lean">https://github.com/PatrickMassot/lean-differential-topology/blob/master/src/norms.lean</a> (after removing the type class inference nightmare at the end). Would it help in getting more motivation to fix the issues?</p>

#### [ Mario Carneiro (Jul 19 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/polynomial/near/129922019):
<p>I think that's a good idea. I know Johannes has his own plans for this stuff, but I think a mathlib PR is the best place to coordinate</p>

#### [ Patrick Massot (Jul 19 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/polynomial/near/129922166):
<p>Ok, I'll try to do that today</p>

#### [ Patrick Massot (Jul 19 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/polynomial/near/129939330):
<p><a href="https://github.com/leanprover/mathlib/pull/208" target="_blank" title="https://github.com/leanprover/mathlib/pull/208">https://github.com/leanprover/mathlib/pull/208</a></p>

#### [ Nicholas Scheel (Jul 19 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/polynomial/near/129941187):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> I’m curious if you could just define <code>norm</code> as <code>dist 0</code>? seems like you spend a lot of time converting between the two ...</p>

#### [ Patrick Massot (Jul 19 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/polynomial/near/129941308):
<p>I don't think you would get the expected properties</p>

#### [ Nicholas Scheel (Jul 19 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/polynomial/near/129941390):
<p>how so? you have <code>lemma norm_dist { g : G} : dist g 0 = ∥g∥</code> already ... (plus commutativity gets you my definition)</p>

#### [ Patrick Massot (Jul 19 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/polynomial/near/129941440):
<p>I mean: there are distances on groups such that <code>dist 0</code> is not a norm</p>

#### [ Patrick Massot (Jul 19 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/polynomial/near/129941492):
<p>Think of the trivial distance for instance</p>

#### [ Patrick Massot (Jul 19 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/polynomial/near/129941508):
<p>maybe this is not a good example actually</p>

#### [ Nicholas Scheel (Jul 19 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/polynomial/near/129941536):
<p>I think you need <code>dist x y = dist 0 (x - y)</code>, as the equivalent of the property you already have, but I think <code>norm</code> adds nothing to the definition – it must be equal to <code>dist 0</code></p>

#### [ Patrick Massot (Jul 19 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/polynomial/near/129941552):
<p>yes, somthing like this is needed</p>


{% endraw %}
