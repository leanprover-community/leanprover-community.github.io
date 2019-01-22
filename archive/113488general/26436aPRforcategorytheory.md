---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/26436aPRforcategorytheory.html
---

## [general](index.html)
### [a PR for category theory](26436aPRforcategorytheory.html)

#### [Scott Morrison (Jun 04 2018 at 04:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a PR for category theory/near/127523861):
Dear all, (@**Mario Carneiro** and @**Johannes Hölzl** in particular!)
I'm finally about to create a mathlib branch for some category theory, and I would be happy to have some guidance about the scope of the initial PR.

Options:
1. Just the definitions of category, functor, natural transformation, and compositions of these.
2. Also some basic constructions, e.g. functor categories, and product categories.
3. Also definitions of basic notions such as products, equalizers, and limits.
4. Also an example, e.g. showing that the category of types has limits.

(I could add many more things, but I think that's probably more than enough for a single PR.)

Essentially it's a question about whether it's easier to have things in very small increments, or easier to have bigger blocks, so that design decisions can be validated by examples and applications.

#### [Mario Carneiro (Jun 04 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a PR for category theory/near/127532640):
Hey, just a heads up, but I am currently traveling and will soon be busy with the lean summer school in Hanoi for the next couple weeks, so my activity here will probably be spotty.

#### [Scott Morrison (Jun 04 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a PR for category theory/near/127535041):
No worries! And thanks for letting us know. Will there be materials from the summer school available online?

#### [Johannes Hölzl (Jun 04 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a PR for category theory/near/127536040):
Hi Scott, I think it would be good to start with a PR for 1. definitions. Then its easier to comment on it. For the summer school: https://hanoifabs.wordpress.com/ will be very ad-hoc, e.g. there are not a lot of slides.

#### [Johan Commelin (Jun 04 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a PR for category theory/near/127536139):
@**Johannes Hölzl** And you are also flying there, right? So the next two weeks are bad timing for PR's in general?

#### [Johannes Hölzl (Jun 04 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a PR for category theory/near/127536198):
Yes, I just landed in Hanoi. I guess the next 3 weeks are quiet busy. First Formal Abstract Summer School in Hanoi and then Hales60 in Pittsburgh.

#### [Scott Morrison (Jun 04 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a PR for category theory/near/127536352):
Thanks, @**Johannes Hölzl** . The PR I put up at https://github.com/leanprover/mathlib/pull/152 is just the first few definitions.

#### [Sebastian Ullrich (Jun 08 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a PR for category theory/near/127762084):
@**Mario Carneiro** @**Johannes Hölzl** What _is_ happening over in Hanoi/in the fabstracts repo :laughing: ? https://github.com/formalabstracts/formalabstracts/pulls

#### [Johannes Hölzl (Jun 08 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a PR for category theory/near/127762135):
Well, we try to teach people to use github, but some used the wrong formalabstracts fork. They should use Tom's personal formalabstract repo, not the project ones...

#### [Johannes Hölzl (Jun 08 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a PR for category theory/near/127762151):
Teaching git (as setting up remotes) is harder than thought...

#### [Johan Commelin (Jul 09 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a PR for category theory/near/129351495):
What is the status of this PR? I would love to have basic category theory available in mathlib!

