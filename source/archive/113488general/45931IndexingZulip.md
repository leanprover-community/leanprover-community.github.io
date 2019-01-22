---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/45931IndexingZulip.html
---

## [general](index.html)
### [Indexing Zulip](45931IndexingZulip.html)

#### [Rob Lewis (Jan 20 2019 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156498766):
At the meeting in Amsterdam, someone raised the question of archiving the Zulip chat and making it accessible to search engines. It's hard to find answers to Lean questions online right now. You have to register and search here specifically. 

I wrote a little script that will scrape the public streams here and post them to an openly accessible site. You can see a sample here: https://leanprover-community.github.io/archive

Before I spend more time on this, I wanted to check with people -- are there any objections on privacy grounds? I'm displaying strictly less information than is available openly to anyone who registers for Zulip -- no email addresses, no pictures. To me it seems comparable to the archive of an email list, which is often public and indexed. 

If there are no objections, I'll finish the script and put up a whole archive. New posts will be added every time the script runs. I don't have a reliable server to automate this; my plan was just to run the script when I think about it, since there's nothing time sensitive, but if anyone has a better plan I'm listening. I also don't have the time to waste on web design. So if anyone wants to mess with the css, Jekyll setup, etc, let's talk.

#### [Kevin Buzzard (Jan 20 2019 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156501864):
Given that many of us were saying pretty much the same things on gitter a  few months back you'd think people will be ok with this. I certainly am.

#### [Neil Strickland (Jan 21 2019 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156502487):
This is a good interim step, but I'll repeat what I said in Amsterdam: I think that stackexchange  is an extremely good framework for recording questions and answers, and I would like to see these kind of things move either to stackoverflow (where there are currently about 3000 questions on coq and/or isabelle, and 48 on lean) or to a new site focused on proof assistants.

#### [Christopher Sumnicht (Jan 21 2019 at 03:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156508680):
Maybe someone should propose a computer verification/lean/proof assistant site on [Area51](https://area51.stackexchange.com/)?

#### [Kenny Lau (Jan 21 2019 at 03:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156508693):
I don't think there's enough interest for that...

#### [Scott Morrison (Jan 21 2019 at 03:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156509307):
@**Rob Lewis** I'm happy to run the script as a cron job on a machine that is (nearly) always online. (Also, thanks, this is great.)

#### [Rob Lewis (Jan 21 2019 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156521307):
I think this chat serves a more general purpose than Stack Overflow. There's lots of general discussion here that doesn't really happen in that format. Trying to direct questions that way and discussions this way would be counterproductive. Of course, I don't want to discourage SO use either, I've answered a few questions there when they've shown up.

#### [Rob Lewis (Jan 21 2019 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156521318):
@**Scott Morrison|110087** That would be perfect, let's talk.

#### [Scott Morrison (Jan 21 2019 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156563329):
@**Neil Strickland**, @**Rob Lewis** one potential compromise is to ask post-hoc questions on SE! SE doesn't particularly mind if the same person asks and answers a question, so it can be a cheap way to preserve a discussion here in more searchable form.

#### [Scott Morrison (Jan 21 2019 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156563348):
This is also something one can potentially push students to do.

