---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/82120constructivisingusingtruncsubtypeiswellorder.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [constructivising using `trunc (subtype (is_well_order _))`](https://leanprover-community.github.io/archive/113488general/82120constructivisingusingtruncsubtypeiswellorder.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Nov 23 2018 at 03:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructivising%20using%20%60trunc%20%28subtype%20%28is_well_order%20_%29%29%60/near/148204645):
<p>How many things can we constructivise with a <code>trunc (subtype (is_well_order _))</code> hypothesis? I'm sure we can make a truncated basis this way... Maybe if it can constructivise a lot of stuff, I would imagine making it as wide-used as <code>decidable_eq</code></p>

#### [ Kenny Lau (Nov 23 2018 at 03:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructivising%20using%20%60trunc%20%28subtype%20%28is_well_order%20_%29%29%60/near/148204651):
<p>well this surely implies <code>decidable_eq</code> to start with</p>

#### [ Kenny Lau (Nov 23 2018 at 03:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructivising%20using%20%60trunc%20%28subtype%20%28is_well_order%20_%29%29%60/near/148204672):
<p>(on second thought maybe we need a decidable prop to do so, but we can fix this by requiring our function to have codomain <code>bool</code> instead?)</p>

#### [ Kenny Lau (Nov 23 2018 at 03:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructivising%20using%20%60trunc%20%28subtype%20%28is_well_order%20_%29%29%60/near/148204807):
<p>and how about making <code>trunc (equiv _ _)</code> an instance</p>

#### [ Kenny Lau (Nov 23 2018 at 03:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructivising%20using%20%60trunc%20%28subtype%20%28is_well_order%20_%29%29%60/near/148204852):
<p>congratulations then, you got yourself into an instance loop with a fintype having decidable equality</p>

#### [ Mario Carneiro (Nov 23 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructivising%20using%20%60trunc%20%28subtype%20%28is_well_order%20_%29%29%60/near/148208342):
<p>I think <code>is_well_order</code> is not as useful constructively as it is in classical maths</p>

#### [ Mario Carneiro (Nov 23 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/constructivising%20using%20%60trunc%20%28subtype%20%28is_well_order%20_%29%29%60/near/148208346):
<p>in particular <code>is_well_order.min</code> is not constructive</p>


{% endraw %}
