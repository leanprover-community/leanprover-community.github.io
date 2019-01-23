---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/92196refactorfunctornotation.html
---

## Stream: [maths](index.html)
### Topic: [refactor functor notation](92196refactorfunctornotation.html)

---

#### [Johan Commelin (Jan 17 2019 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/refactor%20functor%20notation/near/155354489):
Has anyone started the big functor notation search and replace?

#### [Mario Carneiro (Jan 17 2019 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/refactor%20functor%20notation/near/155361713):
I'm not sure this is a good idea. The big arrow seems to be used in multiple contexts, so perhaps we shouldn't have any global notation for it at all, and use local notations instead. The broken right arrow has the advantage that it is an unusual arrow, so I'm more okay with stealing it as a global notation (making it unusable for other purposes).

#### [Patrick Massot (Jan 17 2019 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/refactor%20functor%20notation/near/155362639):
Why do we need to have any global notation for this?

#### [Mario Carneiro (Jan 17 2019 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/refactor%20functor%20notation/near/155362801):
We don't, I guess, but then we would have to preface lots of category theory files with local notation declarations, and the category theory library has quite a few notations. @**Reid Barton** @**Scott Morrison|110087** ?

#### [Scott Morrison (Jan 19 2019 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/refactor%20functor%20notation/near/156411248):
I'm not too concerned. I'd prefer a tiny bit that we don't use local notations in every file, just because this seems likely to result in fragmentation as different people start to use different arrows.

#### [Scott Morrison (Jan 19 2019 at 01:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/refactor%20functor%20notation/near/156411255):
I don't particularly mind the current functor arrow.

