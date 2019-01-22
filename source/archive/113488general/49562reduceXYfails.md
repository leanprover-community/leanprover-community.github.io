---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/49562reduceXYfails.html
---

## [general](index.html)
### [#reduce "X"++"Y" fails](49562reduceXYfails.html)

#### [Kevin Sullivan (Sep 03 2018 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20%22X%22%2B%2B%22Y%22%20fails/near/133264218):
Evaluating this expression in Lean (VSCode is what I'm using) hangs for a while then reports deep recursion detected, increase stack space. Not very undergraduate-student-friendly. Bug or feature?

#### [Patrick Massot (Sep 03 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20%22X%22%2B%2B%22Y%22%20fails/near/133264296):
As usual, `#eval` succeeds here

#### [Kevin Sullivan (Sep 03 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20%22X%22%2B%2B%22Y%22%20fails/near/133264323):
Why this failure?

#### [Kevin Sullivan (Sep 03 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20%22X%22%2B%2B%22Y%22%20fails/near/133265394):
Also note that #eval also fails in ways guaranteed to be confusing to new students. Try this (posted previously).

theorem t : true := true.intro
#check t
#eval t

The real question then, I suppose, is by what simple rule should a new student choose between #eval and #reduce?

And for the curious student, why do they fail in cases where on the face of it, it looks like they might be expected to work?

#### [Rob Lewis (Sep 03 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20%22X%22%2B%2B%22Y%22%20fails/near/133265406):
Even just `#reduce 'X'` is asking the kernel to normalize a proof of `88 < 55296`. This normalizes to 55207 nested applications of `nat.less_than_or_equal.step`. And this is a subproblem of what you're asking.

#### [Rob Lewis (Sep 03 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20%22X%22%2B%2B%22Y%22%20fails/near/133265477):
`#eval` is useful for computing values, it will ignore `Prop`-valued terms.

#### [Patrick Massot (Sep 03 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20%22X%22%2B%2B%22Y%22%20fails/near/133266004):
My simple rule is to choose `#eval`

#### [Kevin Sullivan (Sep 03 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%23reduce%20%22X%22%2B%2B%22Y%22%20fails/near/133266225):
Thanks.

