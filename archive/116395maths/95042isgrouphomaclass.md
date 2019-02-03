---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/95042isgrouphomaclass.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [`is_group_hom` a class?](https://leanprover-community.github.io/archive/116395maths/95042isgrouphomaclass.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Sep 02 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%60is_group_hom%60%20a%20class%3F/near/133222930):
<p>I was surprised to hear <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> saying in Paris that he thought <code>is_group_hom</code> should not be a class. The problem is that people often compose group homomorphisms by simply composing them rather than using <code>function.comp</code> or the notation for it. On the other hand, the last time I looked, <code>is_group_hom</code> was indeed a class. Should there be a discussion about whether this is the correct decision?</p>

#### [ Kenny Lau (Sep 02 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%60is_group_hom%60%20a%20class%3F/near/133222937):
<p>either make is_group_hom not a class, or make is_linear_map a class, I say</p>

#### [ Mario Carneiro (Sep 02 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%60is_group_hom%60%20a%20class%3F/near/133223002):
<p>I agree with that. The current inconsistency is because different parts of the algebraic hierarchy were written by different people with different opinions</p>

#### [ Patrick Massot (Sep 02 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%60is_group_hom%60%20a%20class%3F/near/133223693):
<p>and at different times</p>


{% endraw %}
