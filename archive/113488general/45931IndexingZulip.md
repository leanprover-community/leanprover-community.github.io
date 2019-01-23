---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/45931IndexingZulip.html
---

## Stream: [general](index.html)
### Topic: [Indexing Zulip](45931IndexingZulip.html)

---


{% raw %}
#### [ Rob Lewis (Jan 20 2019 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156498766):
At the meeting in Amsterdam, someone raised the question of archiving the Zulip chat and making it accessible to search engines. It's hard to find answers to Lean questions online right now. You have to register and search here specifically. 

I wrote a little script that will scrape the public streams here and post them to an openly accessible site. You can see a sample here: https://leanprover-community.github.io/archive

Before I spend more time on this, I wanted to check with people -- are there any objections on privacy grounds? I'm displaying strictly less information than is available openly to anyone who registers for Zulip -- no email addresses, no pictures. To me it seems comparable to the archive of an email list, which is often public and indexed. 

If there are no objections, I'll finish the script and put up a whole archive. New posts will be added every time the script runs. I don't have a reliable server to automate this; my plan was just to run the script when I think about it, since there's nothing time sensitive, but if anyone has a better plan I'm listening. I also don't have the time to waste on web design. So if anyone wants to mess with the css, Jekyll setup, etc, let's talk.

#### [ Kevin Buzzard (Jan 20 2019 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156501864):
Given that many of us were saying pretty much the same things on gitter a  few months back you'd think people will be ok with this. I certainly am.

#### [ Neil Strickland (Jan 21 2019 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156502487):
This is a good interim step, but I'll repeat what I said in Amsterdam: I think that stackexchange  is an extremely good framework for recording questions and answers, and I would like to see these kind of things move either to stackoverflow (where there are currently about 3000 questions on coq and/or isabelle, and 48 on lean) or to a new site focused on proof assistants.

#### [ Christopher Sumnicht (Jan 21 2019 at 03:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156508680):
Maybe someone should propose a computer verification/lean/proof assistant site on [Area51](https://area51.stackexchange.com/)?

#### [ Kenny Lau (Jan 21 2019 at 03:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156508693):
I don't think there's enough interest for that...

#### [ Scott Morrison (Jan 21 2019 at 03:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156509307):
@**Rob Lewis** I'm happy to run the script as a cron job on a machine that is (nearly) always online. (Also, thanks, this is great.)

#### [ Rob Lewis (Jan 21 2019 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156521307):
I think this chat serves a more general purpose than Stack Overflow. There's lots of general discussion here that doesn't really happen in that format. Trying to direct questions that way and discussions this way would be counterproductive. Of course, I don't want to discourage SO use either, I've answered a few questions there when they've shown up.

#### [ Rob Lewis (Jan 21 2019 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156521318):
@**Scott Morrison|110087** That would be perfect, let's talk.

#### [ Scott Morrison (Jan 21 2019 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156563329):
@**Neil Strickland**, @**Rob Lewis** one potential compromise is to ask post-hoc questions on SE! SE doesn't particularly mind if the same person asks and answers a question, so it can be a cheap way to preserve a discussion here in more searchable form.

#### [ Scott Morrison (Jan 21 2019 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156563348):
This is also something one can potentially push students to do.

#### [ Rob Lewis (Jan 23 2019 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156649067):
I've made some progress here. There's a full archive of this chat, as of some time earlier today: https://leanprover-community.github.io/archive/

You guys like to use Zulip in ways that don't play well with Jekyll. There are a few outstanding issues:
- Lean syntax highlighting. This is a pipeline issue: there's a PR to Rouge that needs to be merged, and then Github needs to update.
- Parsing urls. Zulip's markdown parser is different from the options in Jekyll, which will only convert urls to links if they're enclosed in < >. Oh well, I'm not going to fix this.
- Malformed posts. Some of you like to write posts that end with code blocks and leave off the closing backticks (https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130159), which leads to this: https://leanprover-community.github.io/archive/113488general/90773invalidcalctransitivityrule.html I'm not sure what to do here.

It's possible to let Zulip process the markdown instead, but then I need to write css to match it's output, and I hate writing css.

#### [ Rob Lewis (Jan 23 2019 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156649088):
Click through a few links and see if you notice anything that looks wrong.

#### [ Rob Lewis (Jan 23 2019 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156649102):
Once it seems stable, I'll get automatic updating set up on Scott's server.

#### [ Scott Morrison (Jan 23 2019 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156650121):
~~There's no way to click back to the main table of contents. "Lean Prover Zulip Chat Archive" could be a hyperlink.~~

Just saw the "Zulip archive" link on the right.

#### [ Scott Morrison (Jan 23 2019 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156650226):
On each stream page, there should be a divider between the stream name and the list of topics. Otherwise the stream name itself is indistinguishable from the topics, and clicking on it mysteriously does nothing. (Different styling could solve this.)

#### [ Scott Morrison (Jan 23 2019 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156650272):
Next to each topic link, it might be nice to write, e.g "17 messages, most recent 2019-01-23" or similar, but this isn't essential.

#### [ Kenny Lau (Jan 23 2019 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156650280):
@**Scott Morrison|110087** I like how you don't just say what shouldn't be done, but also say what should be done. I think this is a very effective way to suggest problems.

#### [ Scott Morrison (Jan 23 2019 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156650347):
~~It might be nice, on each topic, to include a link directly to that topic on zulip. (Just in case people land on the searchable archive page from a search, and want to continue the discussion.)~~

I see now that the heading of each message is actually a link to that message on zulip. This is probably sufficient. Perhaps ideal would be to instead display the little zulip "Z" icon next to the message heading, and just link that? Then it's clear without reading the URL what clicking will do.

#### [ Scott Morrison (Jan 23 2019 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156650373):
Is it plausible to identify hyperlinks in the body of messages, and linkify them?

#### [ Scott Morrison (Jan 23 2019 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156650497):
The link to the archive on https://leanprover-community.github.io/ 404s.

(It should link to https://leanprover-community.github.io/archive/, not https://leanprover-community.github.io/archive.html)

#### [ Rob Lewis (Jan 23 2019 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156650562):
The page title "Lean Prover Zulip Chat Archive" is inserted differently than the others, and it wasn't straightforward to make it a link. I agree it should be one though.

#### [ Scott Morrison (Jan 23 2019 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156650572):
On the main page https://leanprover-community.github.io/archive/, how about we write a title "Streams" above the list of streams? At first it isn't obvious what this list is doing.

#### [ Rob Lewis (Jan 23 2019 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156650592):
I like the idea for counting messages next to the topic links, and I think that's doable.

#### [ Scott Morrison (Jan 23 2019 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156650597):
Similarly on each stream page, we might write the heading "Topics:" above the list.

#### [ Scott Morrison (Jan 23 2019 at 00:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156650666):
Halfway down https://leanprover-community.github.io/archive/113538travis/26562buildstatus.html something gets borked in the formatting. Not exactly sure what, some unclosed markdown environment?

#### [ Rob Lewis (Jan 23 2019 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156650709):
I couldn't make Jekyll linkify urls, and the alternative is writing something in Python to identify them and enclose them in <> (but not when they're already part of markdown links). It's possible, I guess, but not a priority.

#### [ Rob Lewis (Jan 23 2019 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156650738):
Your other suggestions are all good and easy!

#### [ Rob Lewis (Jan 23 2019 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156650797):
Yeah, the formatting in the build status thread is because someone forgot the closing backticks.

#### [ Scott Morrison (Jan 23 2019 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156650821):
The way you display quotations puts everything into fixed-width font. It's slightly confusing (because it looks like a code block), but not that important. See https://leanprover-community.github.io/archive/113489newmembers/10902lagrangetheorem.html for an example.

#### [ Scott Morrison (Jan 23 2019 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156650833):
Otherwise, this is great! Having this all google-able is important.

#### [ Rob Lewis (Jan 23 2019 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156650942):
Quotes prefixed with `>` get parsed differently (and displayed better) than ones in backticks. Probably fixable once I have the time and will to dive into the css.

#### [ Patrick Massot (Jan 23 2019 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156676999):
Thank you very much Rob! I'm not sure it's a good idea to include all streams in this archive, because it clutters the main list. I think only general, maths and new members should be there. Or do you think people will only get there through Google, hence it doesn't matter?

#### [ Patrick Massot (Jan 23 2019 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156677097):
Is this website intended to also host other mathlib related information? I wanted to try to have a mathlib documentation website as well

#### [ Patrick Massot (Jan 23 2019 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156677609):
Rob, is the crawling script somewhere on GitHub?

#### [ Patrick Massot (Jan 23 2019 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156677668):
Is there any reason not to use the same Jekyll theme as on the main Lean website? It would be more consistent

#### [ Rob Lewis (Jan 23 2019 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156678053):
I think there's interesting discussion that goes on in PR reviews, Lean Together 2019, etc. And there could be new channels in the future worth indexing. Maybe we should blacklist rss and travis instead of whitelisting general, math, and new members.

#### [ Rob Lewis (Jan 23 2019 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156678065):
I wrote the home page in about 20 second, but yeah, it's a good place to put other mathlib info.

#### [ Patrick Massot (Jan 23 2019 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156678086):
Would you mind giving me write access?

#### [ Rob Lewis (Jan 23 2019 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156678096):
The crawling script is messy, unfinished, and only works with my Zulip bot api key which probably shouldn't be public.

#### [ Patrick Massot (Jan 23 2019 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156678108):
Your api key clearly shouldn't be public. But the script could read it from somewhere

#### [ Rob Lewis (Jan 23 2019 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156678154):
I have a ton of local changes right now, let me finish these before you start editing anything. But yeah, you can have access.

#### [ Rob Lewis (Jan 23 2019 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156678162):
It does read it from somewhere but it's kind of useless without it.

#### [ Patrick Massot (Jan 23 2019 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156678163):
There is no hurry at all.

#### [ Patrick Massot (Jan 23 2019 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156678198):
People who want to play with it can get their own key

#### [ Rob Lewis (Jan 23 2019 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156678201):
And for the theme, I picked the first "basic" theme I found, it shouldn't be too hard to reskin.


{% endraw %}
