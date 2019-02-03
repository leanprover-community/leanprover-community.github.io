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
<p>If I want to define <code>ring_equiv</code> and <code>group_equiv</code> and etc (I don't have any more examples at the moment), where should I put them?</p>

#### [ Kenny Lau (Dec 19 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/isomorphisms/near/152166189):
<p>or maybe should I not do it at all because either category_theory or parametricity will make this obsolete?</p>

#### [ Andreas Swerdlow (Dec 19 2018 at 15:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/isomorphisms/near/152186538):
<p><a href="https://github.com/leanprover-community/mathlib/blob/inner_product_spaces/ring_theory/ring_hom_isom_invo.lean" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/inner_product_spaces/ring_theory/ring_hom_isom_invo.lean">https://github.com/leanprover-community/mathlib/blob/inner_product_spaces/ring_theory/ring_hom_isom_invo.lean</a> <br>
I made a start on ring isomorphisms here if that helps</p>

#### [ Kenny Lau (Dec 19 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/isomorphisms/near/152186716):
<p>PR it lol</p>

#### [ Andreas Swerdlow (Dec 19 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/isomorphisms/near/152187700):
<p>Soon</p>

#### [ Kenny Lau (Dec 19 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/isomorphisms/near/152189149):
<p>you might want to see this: <a href="https://github.com/leanprover/mathlib/pull/533" target="_blank" title="https://github.com/leanprover/mathlib/pull/533">https://github.com/leanprover/mathlib/pull/533</a></p>

#### [ Kenny Lau (Dec 19 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/isomorphisms/near/152189637):
<p>don't use <code>def</code> for theorems</p>

#### [ Kenny Lau (Dec 19 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/isomorphisms/near/152192151):
<p><a href="https://github.com/leanprover-community/mathlib/pull/12" target="_blank" title="https://github.com/leanprover-community/mathlib/pull/12">https://github.com/leanprover-community/mathlib/pull/12</a></p>

#### [ Andreas Swerdlow (Dec 19 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/isomorphisms/near/152202430):
<p>Is it worth adding the "lemmas" about ring_equiv from <a href="https://github.com/leanprover-community/mathlib/blob/inner_product_spaces/ring_theory/ring_hom_isom_invo.lean" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/inner_product_spaces/ring_theory/ring_hom_isom_invo.lean">https://github.com/leanprover-community/mathlib/blob/inner_product_spaces/ring_theory/ring_hom_isom_invo.lean</a> into your PR?</p>


{% endraw %}
