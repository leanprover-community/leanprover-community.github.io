---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/41566sheafification.html
---

## Stream: [maths](index.html)
### Topic: [sheafification](41566sheafification.html)

---

#### [Johan Commelin (Nov 07 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheafification/near/146939281):
@**Scott Morrison|110087** @**Reid Barton** It seems that on a general site, sheafification needs localisation of categories and calculus of fractions. I would like to hear from you if you think it is realistic to work on this now, or is this to hard for now?

#### [Reid Barton (Nov 08 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheafification/near/147324157):
@**Johan Commelin** I suppose those topics should be doable, but I wonder whether you really need them.
I'm confused by the proof of Proposition 2.1 at https://ncatlab.org/nlab/show/sheafification#existence. It seems that we are done immediately after quoting "result 1", if all we care about is the existence of a sheafification functor.
I suppose you also want to produce something resembling a formula for it?

#### [Johan Commelin (Nov 08 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheafification/near/147328855):
Hmmm, I hope that it wouldn't matter how we prove the existence (by a construction, or indirectly) as long as we can provide an API. We will want the universal property (i.e. adjunction), the fact that sheafification is idempotent and that it preserves stalks.

#### [Reid Barton (Nov 08 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheafification/near/147329569):
OK, so the first two properties (which are essentially the same thing) are valid for the full subcategory of presheaves which are local with respect to *any* **set** of maps, not just one which comes from a coverage.

#### [Reid Barton (Nov 08 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheafification/near/147329726):
That fact is not so easy, but it's on my to-do list--it follows from the small object argument.

#### [Reid Barton (Nov 08 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheafification/near/147329769):
I'm not sure exactly what the third statement means, but it sounds potentially formal, in the right setup.

#### [Johan Commelin (Nov 09 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/sheafification/near/147350219):
Ok, cool! I'm not surprised that localisations are not-so-easy. But I think it would be awesome if we could have them.
For stalks: either you do this for points of a topos, and I would think it is then pretty formal (but maybe less intuitive for those not familiar with them, like me). Or you do it for stalks of points in a topological space, which is less general, and you would have to build more bridges. But large parts of it should be formal anyway, since stalks are by definition filtered colimits, and I hope those are preserved by the right sort of adjoint functor.

