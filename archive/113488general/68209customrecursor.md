---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/68209customrecursor.html
---

## Stream: [general](index.html)
### Topic: [custom recursor](68209customrecursor.html)

---

#### [Simon Hudon (Mar 02 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20recursor/near/123198503):
I'm creating a recursor for a type that I defined and I'd like `match` and `cases` to pick it instead of what Lean generated. Is there a way to do that?

#### [Andrew Ashworth (Mar 02 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20recursor/near/123198843):
instead of cases, why not use `induction`where you can specify the recursor?

#### [Mario Carneiro (Mar 02 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20recursor/near/123198918):
No, that's not really possible. You can use the `using`clause of `induction`, but it's not particularly reliable in my experience. I don't really consider it supported

#### [Simon Hudon (Mar 02 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20recursor/near/123199074):
For `cases` on coinductive types, I can make my own tactics but it would be great if the same tactic could cover both inductive and coinductive types

#### [Simon Hudon (Mar 02 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/custom%20recursor/near/123199079):
Maybe I should just add that to my wish list

