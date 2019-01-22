---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/81438githubnotifications.html
---

## [general](index.html)
### [github notifications](81438githubnotifications.html)

#### [Sean Leather (Feb 28 2018 at 07:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/github%20notifications/near/123077197):
Does anyone (with the right repository permissions) want to create streams and bots for GitHub notifications from https://github.com/leanprover/lean and https://github.com/leanprover/mathlib ?

#### [Mario Carneiro (Feb 28 2018 at 08:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/github%20notifications/near/123078594):
You should already be receiving notifications from mathlib, on the #**travis** stream. I doubt I can set up hooks for the lean repo since it inexplicably requires modifying the travis build script

#### [Sean Leather (Feb 28 2018 at 08:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/github%20notifications/near/123078606):
I'm referring to issues, PRs, comments, and commits, not Travis CI.

#### [Mario Carneiro (Feb 28 2018 at 08:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/github%20notifications/near/123078694):
well, I certainly can't, you need to be admin on the repo to set it up I think

#### [Sean Leather (Feb 28 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/github%20notifications/near/123078741):
Exactly. :smile: Are you not an admin on mathlib?

#### [Mario Carneiro (Feb 28 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/github%20notifications/near/123079024):
Nope, this is part of the reason I would prefer to move development elsewhere

#### [Mario Carneiro (Feb 28 2018 at 08:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/github%20notifications/near/123079027):
I'm just a really active contributor with push access

#### [Sean Leather (Feb 28 2018 at 08:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/github%20notifications/near/123079092):
```quote
Nope, this is part of the reason I would prefer to move development elsewhere
```

It sounds like there's more context to this statement that I am not aware of.

#### [Moses Schönfinkel (Feb 28 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/github%20notifications/near/123079149):
Mario is going rogue.

#### [Mario Carneiro (Feb 28 2018 at 08:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/github%20notifications/near/123079568):
Mario is trying to figure out how to fork lean without making life more horrible for everyone

#### [Sean Leather (Feb 28 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/github%20notifications/near/123079773):
It would be a shame to have fewer collaborators on and contributions to such a fork, were it to exist.

#### [Simon Hudon (Feb 28 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/github%20notifications/near/123079779):
Is it still because of the instance situation?

#### [Mario Carneiro (Feb 28 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/github%20notifications/near/123079945):
It's mostly been a politics thing - I don't think Leo is cultivating a good environment for an OSS to develop with his approach to PRs and issues management. The instance thing caused some of these problems to come to the fore, and although that's no longer directly an issue the problems have been there for a while and have not gone away. As it is, we're in a bit of a holding pattern, and I have no wish to lose collaborators and the like so I don't know whether there is a good way forward that avoids this

#### [Simon Hudon (Feb 28 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/github%20notifications/near/123080023):
Did he explain why he's doing things this way?

#### [Simon Hudon (Feb 28 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/github%20notifications/near/123080038):
I mean, is there some sort of dialogue going on that might help mitigate the situation?

#### [Mario Carneiro (Feb 28 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/github%20notifications/near/123080107):
No, that is of course part of the problem. I have traded less than a hundred words with Leo since summer (when I met him in person)

#### [Simon Hudon (Feb 28 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/github%20notifications/near/123080195):
You're in Jeremy's team right?

#### [Mario Carneiro (Feb 28 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/github%20notifications/near/123080239):
I know very well why he's doing this though - he has no interest in managing general maintenance stuff and definitely doesn't want to maintain mathlib (not that I've ever asked him to), I think he's shellshocked from having to do this in lean 2. He has his projects to complete, and the other stuff is sucking out his enjoyment and stressing him out

#### [Mario Carneiro (Feb 28 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/github%20notifications/near/123080240):
yes

#### [Simon Hudon (Feb 28 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/github%20notifications/near/123080246):
Your team seems like such a big part of Lean. Does Leo appreciate your contribution?

#### [Sean Leather (Feb 28 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/github%20notifications/near/123080294):
I think the comments on [leanprover/lean#1521](https://github.com/leanprover/lean/issues/1521) are indicative of Leo's approach.

#### [Mario Carneiro (Feb 28 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/github%20notifications/near/123080413):
I will let Leo answer that question himself

#### [Simon Hudon (Feb 28 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/github%20notifications/near/123080460):
I'll have to look at that closely. Thanks! Btw, I see you seemed interested in coinductive types. You might be interested in my current PR: https://github.com/leanprover/mathlib/pull/71

#### [Simon Hudon (Feb 28 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/github%20notifications/near/123080509):
I feel like I must sound a bit like a marriage counsellor but it seems like if he doesn't value your work, it will be hard to get him to make any kind of concession. I wonder if there's something he wishes you'd do (beside drop `mathlib` :stuck_out_tongue_closed_eyes: )

#### [Sean Leather (Feb 28 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/github%20notifications/near/123080510):
[Me](https://github.com/leanprover/lean/issues/1521#issuecomment-294447574): :smile: 

> In case it wasn't clear, I didn't mean to pick these out because I wanted to know about them. They were merely examples.

And, yes, I'm aware of your PR. And I'm impressed by it.

#### [Sean Leather (Feb 28 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/github%20notifications/near/123080554):
@**Simon Hudon**: I think that is an example of how you go against [Leo's assumptions](https://github.com/leanprover/lean/issues/1521#issuecomment-294363143):

> On the other hand, you should not hold your breath for coinductive datatypes. They will not happen in the following years, unless someone as strong as @gebner or @Kha shows up and decides to implement this feature.

#### [Simon Hudon (Feb 28 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/github%20notifications/near/123080614):
Thanks :) I can't compare myself to @**Gabriel Ebner** or @**Sebastian Ullrich** but it looks to me that something that does the job 30% of the way is better than nothing (at least for me). So let's just see how far I can get with it.

#### [Mario Carneiro (Feb 28 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/github%20notifications/near/123080665):
I'm not totally sure about Simon's approach as a final solution for all coinductive datatypes, including nested inductive/coinductives and other things that might be nice, so I'm not sure how much it is worth focusing on extending the capabilities of the package if we are going to move to something else later

#### [Mario Carneiro (Feb 28 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/github%20notifications/near/123080668):
Specifically, I want to see if the BNF approach used in isabelle also works for lean

#### [Mario Carneiro (Feb 28 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/github%20notifications/near/123080682):
That said, I am certainly happy to have a decent coverage of basic coinductive types and will merge Simon's PR when it stabilizes

#### [Simon Hudon (Feb 28 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/github%20notifications/near/123080737):
Thanks for the comment. I believe you're referring to Johannes' paper. I'm still learning that stuff so when I wrap my head around that BNF stuff, I may well try it out.

#### [Sebastian Ullrich (Feb 28 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/github%20notifications/near/123083344):
Decoupling Lean is certainly on both Leo's and my wish list. As Mario wrote in another topic, things like a command for coinductive types should be written purely in Lean in the future, and it shouldn't matter whether this happens in the core lib or a separate package. I'll get to decoupling users from the Lean master... sometime this week.

#### [Sebastian Ullrich (Feb 28 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/github%20notifications/near/123083365):
To go back to the original topic, we can add commit RSS feeds for arbitrary repos. Personally, that would be sufficient for me since I already get e-mails about all the other things by following the repos on Github.

#### [Kevin Buzzard (Feb 28 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/github%20notifications/near/123084544):
```quote
To go back to the original topic, we can add commit RSS feeds for arbitrary repos. Personally, that would be sufficient for me since I already get e-mails about all the other things by following the repos on Github.
```
Lean and mathlib, please :-)

#### [Sebastian Ullrich (Feb 28 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/github%20notifications/near/123085938):
Ah, you need a Python bot running somewhere for that. Yeah, no.

