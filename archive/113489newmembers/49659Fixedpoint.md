---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/49659Fixedpoint.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [Fixed point](https://leanprover-community.github.io/archive/113489newmembers/49659Fixedpoint.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Alistair Tucker (Nov 21 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Fixed%20point/near/148111493):
<p>I'd like to define a function E from ℝ^n to ℝ^n as the fixed point of a contraction mapping (or equivalently I think as the solution to a variational inequality). Is this easy to do? What files should I be looking at?</p>

#### [ Kevin Buzzard (Nov 21 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Fixed%20point/near/148112396):
<p>One of my students proved the contraction mapping theorem for metric spaces... <span class="user-mention" data-user-id="120726">@Luca Gerolla</span> did you ever PR this?</p>

#### [ Patrick Massot (Nov 21 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Fixed%20point/near/148112403):
<p>It's currently not easy. There is a pending PR on contraction mapping, but I don't remember what is proved there exactly</p>

#### [ Patrick Massot (Nov 21 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Fixed%20point/near/148112412):
<p><a href="https://github.com/leanprover/mathlib/pull/428" target="_blank" title="https://github.com/leanprover/mathlib/pull/428">https://github.com/leanprover/mathlib/pull/428</a></p>

#### [ Alistair Tucker (Nov 21 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Fixed%20point/near/148112567):
<p>Thanks! I'll have a look at that but if it's not easy I might just declare it as a constant :)</p>

#### [ Patrick Massot (Nov 21 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Fixed%20point/near/148112635):
<p>That PR needs to be reworked to use <a href="https://github.com/leanprover/mathlib/commit/4a013fb04d6e504be8582ad610016d8dcce3e5f3" target="_blank" title="https://github.com/leanprover/mathlib/commit/4a013fb04d6e504be8582ad610016d8dcce3e5f3">https://github.com/leanprover/mathlib/commit/4a013fb04d6e504be8582ad610016d8dcce3e5f3</a></p>

#### [ Patrick Massot (Nov 21 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Fixed%20point/near/148112646):
<p>and probably extract more lemmas out of the big proofs</p>

#### [ Patrick Massot (Nov 21 2018 at 15:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Fixed%20point/near/148112661):
<p>compare <a href="https://github.com/leanprover/mathlib/pull/428/files#diff-6f3fee1c28d757f0199c3512ffc8e5e9R83" target="_blank" title="https://github.com/leanprover/mathlib/pull/428/files#diff-6f3fee1c28d757f0199c3512ffc8e5e9R83">https://github.com/leanprover/mathlib/pull/428/files#diff-6f3fee1c28d757f0199c3512ffc8e5e9R83</a> and <a href="https://github.com/leanprover/mathlib/commit/4a013fb04d6e504be8582ad610016d8dcce3e5f3#diff-5edb379056f11c116887dcff6e8bed0dR366" target="_blank" title="https://github.com/leanprover/mathlib/commit/4a013fb04d6e504be8582ad610016d8dcce3e5f3#diff-5edb379056f11c116887dcff6e8bed0dR366">https://github.com/leanprover/mathlib/commit/4a013fb04d6e504be8582ad610016d8dcce3e5f3#diff-5edb379056f11c116887dcff6e8bed0dR366</a> for instance</p>

#### [ Alistair Tucker (Nov 21 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Fixed%20point/near/148112740):
<p>If I think I can help with that I will but I suspect it'll be beyond me.</p>

#### [ Sebastien Gouezel (Nov 21 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Fixed%20point/near/148112771):
<p>Yes, I think everything in the file <code>analysis/topology/metric_sequences.lean</code> of the PR is now already in the library. But the result on the Banach contraction is not.</p>

#### [ Patrick Massot (Nov 21 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Fixed%20point/near/148112823):
<p>Alistair, updating that PR in order to replace stuff that came to mathlib in the meantime should be a nice exercise</p>

#### [ Patrick Massot (Nov 21 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Fixed%20point/near/148112887):
<p>Refactoring the big proof is much more difficult</p>

#### [ Kevin Buzzard (Nov 21 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Fixed%20point/near/148126734):
<p>Luca reminds me that it was in fact <span class="user-mention" data-user-id="120559">@Rohan Mitta</span> who was doing the contraction mapping theorem.</p>


{% endraw %}
