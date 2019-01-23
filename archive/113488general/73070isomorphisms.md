---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/73070isomorphisms.html
---

## Stream: [general](index.html)
### Topic: [isomorphisms](73070isomorphisms.html)

---


{% raw %}
#### [ Kenny Lau (Dec 19 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/isomorphisms/near/152166179):
If I want to define `ring_equiv` and `group_equiv` and etc (I don't have any more examples at the moment), where should I put them?

#### [ Kenny Lau (Dec 19 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/isomorphisms/near/152166189):
or maybe should I not do it at all because either category_theory or parametricity will make this obsolete?

#### [ Andreas Swerdlow (Dec 19 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/isomorphisms/near/152186538):
https://github.com/leanprover-community/mathlib/blob/inner_product_spaces/ring_theory/ring_hom_isom_invo.lean 
I made a start on ring isomorphisms here if that helps

#### [ Kenny Lau (Dec 19 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/isomorphisms/near/152186716):
PR it lol

#### [ Andreas Swerdlow (Dec 19 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/isomorphisms/near/152187700):
Soon

#### [ Kenny Lau (Dec 19 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/isomorphisms/near/152189149):
you might want to see this: https://github.com/leanprover/mathlib/pull/533

#### [ Kenny Lau (Dec 19 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/isomorphisms/near/152189637):
don't use `def` for theorems

#### [ Kenny Lau (Dec 19 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/isomorphisms/near/152192151):
https://github.com/leanprover-community/mathlib/pull/12

#### [ Andreas Swerdlow (Dec 19 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/isomorphisms/near/152202430):
Is it worth adding the "lemmas" about ring_equiv from https://github.com/leanprover-community/mathlib/blob/inner_product_spaces/ring_theory/ring_hom_isom_invo.lean into your PR?


{% endraw %}
