---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/34800remember.html
---

## [new members](index.html)
### [remember](34800remember.html)

#### [petercommand (Nov 01 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/remember/near/136927744):
Is there something similar to coq's remember tactic in lean?

#### [petercommand (Nov 01 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/remember/near/136927833):
I can't find it in lean's documents

#### [Chris Hughes (Nov 01 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/remember/near/136927846):
What does coq's remember tactic do?

#### [petercommand (Nov 01 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/remember/near/136927899):
It's basically a way to remember a term so that after pattern matching on a non-trivial term, no information is lost

#### [Chris Hughes (Nov 01 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/remember/near/136928040):
Possibly `generalize`. But I don't fully understand the explanation in the coq docs

#### [Reid Barton (Nov 01 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/remember/near/136928066):
I think `cases` and/or `induction` accepts a syntax which lets you name a hypothesis that the thing you pattern matched is equal to the result of the pattern match--is that the sort of thing you mean?

#### [petercommand (Nov 01 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/remember/near/136928149):
yes

#### [petercommand (Nov 01 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/remember/near/136928230):
that's what I want

#### [Reid Barton (Nov 01 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/remember/near/136928271):
Yes, they both have it: the syntax is `cases (id :)? expr (with id*)?`--check the docstring for full details

#### [petercommand (Nov 01 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new members/topic/remember/near/136928315):
Thanks!

