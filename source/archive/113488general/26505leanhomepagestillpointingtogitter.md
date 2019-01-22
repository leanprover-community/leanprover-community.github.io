---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/26505leanhomepagestillpointingtogitter.html
---

## [general](index.html)
### [lean home page still pointing to gitter](26505leanhomepagestillpointingtogitter.html)

#### [Kevin Buzzard (Oct 10 2018 at 08:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20home%20page%20still%20pointing%20to%20gitter/near/135521404):
I occasionally notice that [Lean's web pages](https://leanprover.github.io/documentation/) still point to gitter, and we occasionally get questions there; perhaps the signage isn't good enough for everyone. How could we go about changing this? I could make a PR but someone will have to point me to the location of the git source for those pages (not least so I can check the PR is not already made).

#### [Scott Morrison (Oct 10 2018 at 08:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20home%20page%20still%20pointing%20to%20gitter/near/135521477):
I think we just run into the general problem that PRs here risk annoying Leo.

#### [Kevin Buzzard (Oct 10 2018 at 08:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20home%20page%20still%20pointing%20to%20gitter/near/135521556):
I know, but on this particular occasion I am personally prepared to take the risk. I have been extremely good at not annoying Leo recently -- a few months ago I was desperate to email him to tell him 100 things and Tom Hales just basically went "No. No. No. No. No. Leave him alone." This is a one-line PR to fix something which is broken and the review process is trivial.

#### [Mario Carneiro (Oct 10 2018 at 08:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20home%20page%20still%20pointing%20to%20gitter/near/135521622):
are you saying you need us to say "no no no"?

#### [Kevin Buzzard (Oct 10 2018 at 08:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20home%20page%20still%20pointing%20to%20gitter/near/135521627):
If you're not going to tell me how to do it I'm going to go rogue and figure it out myself.

#### [Mario Carneiro (Oct 10 2018 at 08:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20home%20page%20still%20pointing%20to%20gitter/near/135521670):
I guess I don't know if the website is also defunct or just the tool

#### [Kevin Buzzard (Oct 10 2018 at 08:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20home%20page%20still%20pointing%20to%20gitter/near/135522279):
"Small bug fixes (few lines of code) are always welcome.". From the docs (which I'm currently reading -- I'm trying to put together an "installation options overview" page)

#### [Kevin Buzzard (Oct 10 2018 at 08:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20home%20page%20still%20pointing%20to%20gitter/near/135522296):
"Bug reports are always welcome, but nitpicking issues are not". Hmm.

#### [Kevin Buzzard (Oct 10 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20home%20page%20still%20pointing%20to%20gitter/near/135522369):
But I've now found two links to Zulip in the Lean docs / GH pages, and one link to gitter.

#### [Jeremy Avigad (Oct 10 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20home%20page%20still%20pointing%20to%20gitter/near/135548324):
I think @**Sebastian Ullrich** has permissions to the relevant repo.

#### [Sebastian Ullrich (Oct 10 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20home%20page%20still%20pointing%20to%20gitter/near/135550144):
Unfortunately I don't. If someone could open a PR with some new wording (is it still a "public" "chat room"?), I'll talk to Leo

#### [Kevin Buzzard (Oct 10 2018 at 22:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20home%20page%20still%20pointing%20to%20gitter/near/135565883):
I would do this but I don't know the URL of the repo.

#### [Sebastian Ullrich (Oct 10 2018 at 22:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20home%20page%20still%20pointing%20to%20gitter/near/135566152):
@**Kevin Buzzard** https://github.com/leanprover/leanprover.github.io/blob/master/documentation/index.md. You should be able to edit it right on Github.

#### [Kevin Buzzard (Oct 10 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20home%20page%20still%20pointing%20to%20gitter/near/135566628):
https://github.com/leanprover/leanprover.github.io/pull/75

#### [Sebastian Ullrich (Oct 10 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20home%20page%20still%20pointing%20to%20gitter/near/135566974):
(Okay, now I have write access. Thanks for the PR.)

#### [Patrick Massot (Oct 10 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20home%20page%20still%20pointing%20to%20gitter/near/135567577):
Sebastian, are you willing to get other PR to that repo? Like one about the sentence "The current version of Lean is Lean 3, and is under active development."

#### [Sebastian Ullrich (Oct 10 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20home%20page%20still%20pointing%20to%20gitter/near/135567853):
Oh. Yes.

#### [Patrick Massot (Oct 10 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20home%20page%20still%20pointing%20to%20gitter/near/135568270):
https://github.com/leanprover/leanprover.github.io/pull/76

#### [Kevin Buzzard (Oct 10 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%20home%20page%20still%20pointing%20to%20gitter/near/135568597):
Good catch Patrick. As you all know I've been pushing for more users in the maths community recently, and it's good to get the docs right. I don't care that Lean 4 is coming and there might be some chaos -- mathematicians need a *lot* of training in general and the sooner they start the better. In fact in some sense now we have a stable Lean it's quite a good time for new users to appear.

