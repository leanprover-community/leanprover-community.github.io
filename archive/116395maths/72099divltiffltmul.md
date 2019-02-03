---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/72099divltiffltmul.html
---

## Stream: [maths](index.html)
### Topic: [div_lt_iff_lt_mul](72099divltiffltmul.html)

---


{% raw %}
#### [ Kevin Buzzard (Jan 15 2019 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_lt_iff_lt_mul/near/155161891):
<p>I just wanted to get from <code>a&lt;b*c</code> to <code>a/c&lt;b</code> (on the real  numbers) with a hypothesis that <code>c&gt;0</code>. I was surprised to find that although all three of <code>div_lt_iff_lt_mul</code>, <code>lt_mul_of_div_lt</code> and <code>div_lt_of_lt_mul</code> were in Lean, they were in <code>data.int.basic</code> :-) and only applied to ints. This should be some general lemma about ordered monoids or some such thing, right? I might start doing what Chris always encourages me to do, which is to make a super-short PR, assuming that this is actually something missing from mathlib. But is it there and I missed it?</p>

#### [ Kevin Buzzard (Jan 15 2019 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_lt_iff_lt_mul/near/155162157):
<p>Currently struggling to find ordered monoids :-/ Do we only have ordered additive monoids?</p>

#### [ Mario Carneiro (Jan 15 2019 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_lt_iff_lt_mul/near/155163224):
<p>it should be in <code>ordered_field</code> somewhere</p>

#### [ Mario Carneiro (Jan 15 2019 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_lt_iff_lt_mul/near/155163236):
<p><code>div_lt_iff</code></p>

#### [ Mario Carneiro (Jan 15 2019 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_lt_iff_lt_mul/near/155163385):
<p>lean core has several more long winded unidirectional versions - <code>div_lt_of_mul_lt_of_pos</code> , I can't find the reverse direction</p>

#### [ Kevin Buzzard (Jan 15 2019 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_lt_iff_lt_mul/near/155164568):
<p>Aah! This is a theorem about multiplication and 0 (which is to do with addition) so indeed it's not about monoids. Maybe it's about ordered semirings? Thanks Mario.</p>

#### [ Mario Carneiro (Jan 15 2019 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_lt_iff_lt_mul/near/155164872):
<p>It's a theorem about fields because division</p>

#### [ Mario Carneiro (Jan 15 2019 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_lt_iff_lt_mul/near/155164927):
<p>division doesn't exist on monoids or groups</p>

#### [ Kevin Buzzard (Jan 15 2019 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_lt_iff_lt_mul/near/155164929):
<p>Oh of course. ok it all makes sense now :-)</p>

#### [ Kevin Buzzard (Jan 15 2019 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_lt_iff_lt_mul/near/155164934):
<p>Now I'm just annoyed that I didn't go through this thought process myself before asking.</p>

#### [ Kevin Buzzard (Jan 15 2019 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_lt_iff_lt_mul/near/155164954):
<p>Had I taken the trouble to try and formalise what statement I thought was true for ordered monoids I suspect I would have made more progress on my own...</p>

#### [ Mario Carneiro (Jan 15 2019 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/div_lt_iff_lt_mul/near/155165038):
<p>you might wonder why division isn't defined for groups, and this is one of the differences from add_groups, which have subtraction, but there is a difference between the total division on groups and the almost total division on fields and it doesn't seem to be helpful to unify them; lots of theorems overlap with a name conflict, but they are all proven differently</p>


{% endraw %}
