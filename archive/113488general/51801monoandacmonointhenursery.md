---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/51801monoandacmonointhenursery.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [mono and ac_mono in the nursery](https://leanprover-community.github.io/archive/113488general/51801monoandacmonointhenursery.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Simon Hudon (Aug 22 2018 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mono%20and%20ac_mono%20in%20the%20nursery/near/132589831):
<p>My <code>mono</code> and <code>ac_mono</code> are, I believe, ready for use. I have put them in the nursery <a href="https://github.com/leanprover-community/mathlib-nursery" target="_blank" title="https://github.com/leanprover-community/mathlib-nursery">https://github.com/leanprover-community/mathlib-nursery</a> so that people can try them out as I get them merged into mathlib.</p>

#### [ Patrick Massot (Aug 22 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mono%20and%20ac_mono%20in%20the%20nursery/near/132597919):
<p>Why is there so much meta and lemmas in the test file? Is it meant to be part of mathlib?</p>

#### [ Simon Hudon (Aug 22 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mono%20and%20ac_mono%20in%20the%20nursery/near/132598001):
<p>It is. It's meant to test individual parts of the tactics. Maybe I should split it into <code>test</code> and <code>example</code></p>

#### [ Patrick Massot (Aug 22 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mono%20and%20ac_mono%20in%20the%20nursery/near/132598015):
<p>I see</p>

#### [ Patrick Massot (Aug 22 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mono%20and%20ac_mono%20in%20the%20nursery/near/132598091):
<p>I always find it hard to read your examples or tests which actually don't prove anything, either because the announced statement is <code>true</code> or because it ends with <code>admit</code></p>

#### [ Patrick Massot (Aug 22 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mono%20and%20ac_mono%20in%20the%20nursery/near/132598207):
<p>Where is monotonicity when the target is an equality as in <a href="https://github.com/leanprover-community/mathlib-nursery/blob/master/test/tactic/monotonicity.lean#L326" target="_blank" title="https://github.com/leanprover-community/mathlib-nursery/blob/master/test/tactic/monotonicity.lean#L326">https://github.com/leanprover-community/mathlib-nursery/blob/master/test/tactic/monotonicity.lean#L326</a>?</p>

#### [ Simon Hudon (Aug 22 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mono%20and%20ac_mono%20in%20the%20nursery/near/132598248):
<p>In that case, monotonicity is a generalization of <code>congr</code></p>

#### [ Patrick Massot (Aug 22 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mono%20and%20ac_mono%20in%20the%20nursery/near/132598313):
<p>Maybe you could explain that in the documentation (and add a couple of example there too)</p>

#### [ Patrick Massot (Aug 22 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mono%20and%20ac_mono%20in%20the%20nursery/near/132598325):
<p>It looks very useful</p>

#### [ Simon Hudon (Aug 22 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mono%20and%20ac_mono%20in%20the%20nursery/near/132598383):
<p>I see what you mean with <code>true</code>. I state those theorems using <code>suffices : x * y &lt; w * z, trivial,</code> just so that I don't have to complete all the proofs. I could use assumptions instead of <code>guard_target</code> maybe , that would be clearer</p>

#### [ Simon Hudon (Aug 22 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mono%20and%20ac_mono%20in%20the%20nursery/near/132598410):
<p>Thanks for the advice, I'll try to select the ones that illustrate best the obvious use cases</p>

#### [ Simon Hudon (Aug 22 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mono%20and%20ac_mono%20in%20the%20nursery/near/132598587):
<blockquote>
<p>It looks very useful</p>
</blockquote>
<p>I'm hoping it will be. Please report any trouble you run across, I feel like I must have overlooked lots of cases and lots of lemmas.</p>

#### [ Patrick Massot (Aug 22 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mono%20and%20ac_mono%20in%20the%20nursery/near/132598785):
<p>Unfortunately  I don't think any of my current projects will need this, but certainly I will need it at some point.</p>


{% endraw %}
