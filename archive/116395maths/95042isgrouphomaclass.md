---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/95042isgrouphomaclass.html
---

## Stream: [maths](index.html)
### Topic: [`is_group_hom` a class?](95042isgrouphomaclass.html)

---

#### [Kevin Buzzard (Sep 02 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%60is_group_hom%60%20a%20class%3F/near/133222930):
I was surprised to hear @**Johannes Hölzl** saying in Paris that he thought `is_group_hom` should not be a class. The problem is that people often compose group homomorphisms by simply composing them rather than using `function.comp` or the notation for it. On the other hand, the last time I looked, `is_group_hom` was indeed a class. Should there be a discussion about whether this is the correct decision?

#### [Kenny Lau (Sep 02 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%60is_group_hom%60%20a%20class%3F/near/133222937):
either make is_group_hom not a class, or make is_linear_map a class, I say

#### [Mario Carneiro (Sep 02 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%60is_group_hom%60%20a%20class%3F/near/133223002):
I agree with that. The current inconsistency is because different parts of the algebraic hierarchy were written by different people with different opinions

#### [Patrick Massot (Sep 02 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%60is_group_hom%60%20a%20class%3F/near/133223693):
and at different times

