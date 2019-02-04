---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/45931IndexingZulip.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Indexing Zulip](https://leanprover-community.github.io/archive/113488general/45931IndexingZulip.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Rob Lewis (Jan 20 2019 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156498766):
<p>At the meeting in Amsterdam, someone raised the question of archiving the Zulip chat and making it accessible to search engines. It's hard to find answers to Lean questions online right now. You have to register and search here specifically. </p>
<p>I wrote a little script that will scrape the public streams here and post them to an openly accessible site. You can see a sample here: <a href="https://leanprover-community.github.io/archive" target="_blank" title="https://leanprover-community.github.io/archive">https://leanprover-community.github.io/archive</a></p>
<p>Before I spend more time on this, I wanted to check with people -- are there any objections on privacy grounds? I'm displaying strictly less information than is available openly to anyone who registers for Zulip -- no email addresses, no pictures. To me it seems comparable to the archive of an email list, which is often public and indexed. </p>
<p>If there are no objections, I'll finish the script and put up a whole archive. New posts will be added every time the script runs. I don't have a reliable server to automate this; my plan was just to run the script when I think about it, since there's nothing time sensitive, but if anyone has a better plan I'm listening. I also don't have the time to waste on web design. So if anyone wants to mess with the css, Jekyll setup, etc, let's talk.</p>

#### [ Kevin Buzzard (Jan 20 2019 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156501864):
<p>Given that many of us were saying pretty much the same things on gitter a  few months back you'd think people will be ok with this. I certainly am.</p>

#### [ Neil Strickland (Jan 21 2019 at 00:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156502487):
<p>This is a good interim step, but I'll repeat what I said in Amsterdam: I think that stackexchange  is an extremely good framework for recording questions and answers, and I would like to see these kind of things move either to stackoverflow (where there are currently about 3000 questions on coq and/or isabelle, and 48 on lean) or to a new site focused on proof assistants.</p>

#### [ Christopher Sumnicht (Jan 21 2019 at 03:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156508680):
<p>Maybe someone should propose a computer verification/lean/proof assistant site on <a href="https://area51.stackexchange.com/" target="_blank" title="https://area51.stackexchange.com/">Area51</a>?</p>

#### [ Kenny Lau (Jan 21 2019 at 03:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156508693):
<p>I don't think there's enough interest for that...</p>

#### [ Scott Morrison (Jan 21 2019 at 03:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156509307):
<p><span class="user-mention" data-user-id="110596">@Rob Lewis</span> I'm happy to run the script as a cron job on a machine that is (nearly) always online. (Also, thanks, this is great.)</p>

#### [ Rob Lewis (Jan 21 2019 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156521307):
<p>I think this chat serves a more general purpose than Stack Overflow. There's lots of general discussion here that doesn't really happen in that format. Trying to direct questions that way and discussions this way would be counterproductive. Of course, I don't want to discourage SO use either, I've answered a few questions there when they've shown up.</p>

#### [ Rob Lewis (Jan 21 2019 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156521318):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> That would be perfect, let's talk.</p>

#### [ Scott Morrison (Jan 21 2019 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156563329):
<p><span class="user-mention" data-user-id="130308">@Neil Strickland</span>, <span class="user-mention" data-user-id="110596">@Rob Lewis</span> one potential compromise is to ask post-hoc questions on SE! SE doesn't particularly mind if the same person asks and answers a question, so it can be a cheap way to preserve a discussion here in more searchable form.</p>

#### [ Scott Morrison (Jan 21 2019 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156563348):
<p>This is also something one can potentially push students to do.</p>

#### [ Rob Lewis (Jan 23 2019 at 00:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156649067):
<p>I've made some progress here. There's a full archive of this chat, as of some time earlier today: <a href="https://leanprover-community.github.io/archive/" target="_blank" title="https://leanprover-community.github.io/archive/">https://leanprover-community.github.io/archive/</a></p>
<p>You guys like to use Zulip in ways that don't play well with Jekyll. There are a few outstanding issues:<br>
- Lean syntax highlighting. This is a pipeline issue: there's a PR to Rouge that needs to be merged, and then Github needs to update.<br>
- Parsing urls. Zulip's markdown parser is different from the options in Jekyll, which will only convert urls to links if they're enclosed in &lt; &gt;. Oh well, I'm not going to fix this.<br>
- Malformed posts. Some of you like to write posts that end with code blocks and leave off the closing backticks (<a href="#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130159" title="#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130159">https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/invalid%20%27calc%27%3A%20transitivity%20rule/near/125130159</a>), which leads to this: <a href="https://leanprover-community.github.io/archive/113488general/90773invalidcalctransitivityrule.html" target="_blank" title="https://leanprover-community.github.io/archive/113488general/90773invalidcalctransitivityrule.html">https://leanprover-community.github.io/archive/113488general/90773invalidcalctransitivityrule.html</a> I'm not sure what to do here.</p>
<p>It's possible to let Zulip process the markdown instead, but then I need to write css to match it's output, and I hate writing css.</p>

#### [ Rob Lewis (Jan 23 2019 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156649088):
<p>Click through a few links and see if you notice anything that looks wrong.</p>

#### [ Rob Lewis (Jan 23 2019 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156649102):
<p>Once it seems stable, I'll get automatic updating set up on Scott's server.</p>

#### [ Scott Morrison (Jan 23 2019 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156650121):
<p><del>There's no way to click back to the main table of contents. "Lean Prover Zulip Chat Archive" could be a hyperlink.</del></p>
<p>Just saw the "Zulip archive" link on the right.</p>

#### [ Scott Morrison (Jan 23 2019 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156650226):
<p>On each stream page, there should be a divider between the stream name and the list of topics. Otherwise the stream name itself is indistinguishable from the topics, and clicking on it mysteriously does nothing. (Different styling could solve this.)</p>

#### [ Scott Morrison (Jan 23 2019 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156650272):
<p>Next to each topic link, it might be nice to write, e.g "17 messages, most recent 2019-01-23" or similar, but this isn't essential.</p>

#### [ Kenny Lau (Jan 23 2019 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156650280):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> I like how you don't just say what shouldn't be done, but also say what should be done. I think this is a very effective way to suggest problems.</p>

#### [ Scott Morrison (Jan 23 2019 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156650347):
<p><del>It might be nice, on each topic, to include a link directly to that topic on zulip. (Just in case people land on the searchable archive page from a search, and want to continue the discussion.)</del></p>
<p>I see now that the heading of each message is actually a link to that message on zulip. This is probably sufficient. Perhaps ideal would be to instead display the little zulip "Z" icon next to the message heading, and just link that? Then it's clear without reading the URL what clicking will do.</p>

#### [ Scott Morrison (Jan 23 2019 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156650373):
<p>Is it plausible to identify hyperlinks in the body of messages, and linkify them?</p>

#### [ Scott Morrison (Jan 23 2019 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156650497):
<p>The link to the archive on <a href="https://leanprover-community.github.io/" target="_blank" title="https://leanprover-community.github.io/">https://leanprover-community.github.io/</a> 404s.</p>
<p>(It should link to <a href="https://leanprover-community.github.io/archive/" target="_blank" title="https://leanprover-community.github.io/archive/">https://leanprover-community.github.io/archive/</a>, not <a href="https://leanprover-community.github.io/archive.html" target="_blank" title="https://leanprover-community.github.io/archive.html">https://leanprover-community.github.io/archive.html</a>)</p>

#### [ Rob Lewis (Jan 23 2019 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156650562):
<p>The page title "Lean Prover Zulip Chat Archive" is inserted differently than the others, and it wasn't straightforward to make it a link. I agree it should be one though.</p>

#### [ Scott Morrison (Jan 23 2019 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156650572):
<p>On the main page <a href="https://leanprover-community.github.io/archive/" target="_blank" title="https://leanprover-community.github.io/archive/">https://leanprover-community.github.io/archive/</a>, how about we write a title "Streams" above the list of streams? At first it isn't obvious what this list is doing.</p>

#### [ Rob Lewis (Jan 23 2019 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156650592):
<p>I like the idea for counting messages next to the topic links, and I think that's doable.</p>

#### [ Scott Morrison (Jan 23 2019 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156650597):
<p>Similarly on each stream page, we might write the heading "Topics:" above the list.</p>

#### [ Scott Morrison (Jan 23 2019 at 00:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156650666):
<p>Halfway down <a href="https://leanprover-community.github.io/archive/113538travis/26562buildstatus.html" target="_blank" title="https://leanprover-community.github.io/archive/113538travis/26562buildstatus.html">https://leanprover-community.github.io/archive/113538travis/26562buildstatus.html</a> something gets borked in the formatting. Not exactly sure what, some unclosed markdown environment?</p>

#### [ Rob Lewis (Jan 23 2019 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156650709):
<p>I couldn't make Jekyll linkify urls, and the alternative is writing something in Python to identify them and enclose them in &lt;&gt; (but not when they're already part of markdown links). It's possible, I guess, but not a priority.</p>

#### [ Rob Lewis (Jan 23 2019 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156650738):
<p>Your other suggestions are all good and easy!</p>

#### [ Rob Lewis (Jan 23 2019 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156650797):
<p>Yeah, the formatting in the build status thread is because someone forgot the closing backticks.</p>

#### [ Scott Morrison (Jan 23 2019 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156650821):
<p>The way you display quotations puts everything into fixed-width font. It's slightly confusing (because it looks like a code block), but not that important. See <a href="https://leanprover-community.github.io/archive/113489newmembers/10902lagrangetheorem.html" target="_blank" title="https://leanprover-community.github.io/archive/113489newmembers/10902lagrangetheorem.html">https://leanprover-community.github.io/archive/113489newmembers/10902lagrangetheorem.html</a> for an example.</p>

#### [ Scott Morrison (Jan 23 2019 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156650833):
<p>Otherwise, this is great! Having this all google-able is important.</p>

#### [ Rob Lewis (Jan 23 2019 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156650942):
<p>Quotes prefixed with <code>&gt;</code> get parsed differently (and displayed better) than ones in backticks. Probably fixable once I have the time and will to dive into the css.</p>

#### [ Patrick Massot (Jan 23 2019 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156676999):
<p>Thank you very much Rob! I'm not sure it's a good idea to include all streams in this archive, because it clutters the main list. I think only general, maths and new members should be there. Or do you think people will only get there through Google, hence it doesn't matter?</p>

#### [ Patrick Massot (Jan 23 2019 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156677097):
<p>Is this website intended to also host other mathlib related information? I wanted to try to have a mathlib documentation website as well</p>

#### [ Patrick Massot (Jan 23 2019 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156677609):
<p>Rob, is the crawling script somewhere on GitHub?</p>

#### [ Patrick Massot (Jan 23 2019 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156677668):
<p>Is there any reason not to use the same Jekyll theme as on the main Lean website? It would be more consistent</p>

#### [ Rob Lewis (Jan 23 2019 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156678053):
<p>I think there's interesting discussion that goes on in PR reviews, Lean Together 2019, etc. And there could be new channels in the future worth indexing. Maybe we should blacklist rss and travis instead of whitelisting general, math, and new members.</p>

#### [ Rob Lewis (Jan 23 2019 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156678065):
<p>I wrote the home page in about 20 second, but yeah, it's a good place to put other mathlib info.</p>

#### [ Patrick Massot (Jan 23 2019 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156678086):
<p>Would you mind giving me write access?</p>

#### [ Rob Lewis (Jan 23 2019 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156678096):
<p>The crawling script is messy, unfinished, and only works with my Zulip bot api key which probably shouldn't be public.</p>

#### [ Patrick Massot (Jan 23 2019 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156678108):
<p>Your api key clearly shouldn't be public. But the script could read it from somewhere</p>

#### [ Rob Lewis (Jan 23 2019 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156678154):
<p>I have a ton of local changes right now, let me finish these before you start editing anything. But yeah, you can have access.</p>

#### [ Rob Lewis (Jan 23 2019 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156678162):
<p>It does read it from somewhere but it's kind of useless without it.</p>

#### [ Patrick Massot (Jan 23 2019 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156678163):
<p>There is no hurry at all.</p>

#### [ Patrick Massot (Jan 23 2019 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156678198):
<p>People who want to play with it can get their own key</p>

#### [ Rob Lewis (Jan 23 2019 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156678201):
<p>And for the theme, I picked the first "basic" theme I found, it shouldn't be too hard to reskin.</p>

#### [ Bryan Gin-ge Chen (Jan 23 2019 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156686039):
<p>Another thing we might think about putting on the leanprover-community website is a version of the lean web editor that uses a current build of mathlib / lean. I'd want to figure out why the emscripten builds of lean don't work in Firefox is before really pursuing this though.</p>

#### [ Rob Lewis (Jan 23 2019 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156688111):
<p>I've made all the suggested changes that were easy. The latest addition added little Zulip icons next to the links to posts, but the Jekyll build on GitHub is timing out now. Not sure if that's a result of this change or what. I'll restart it in a bit.</p>

#### [ Rob Lewis (Jan 23 2019 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156713091):
<p>For some reason, adding little Zulip icons in the markdown makes the Github build time out. It only adds about 5% locally. I added them with css, which is way better anyway.</p>

#### [ Johan Commelin (Jan 23 2019 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156715783):
<p><span class="user-mention" data-user-id="110596">@Rob Lewis</span> How are the streams sorted on the home page of the archive?</p>

#### [ Johan Commelin (Jan 23 2019 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156715800):
<p>I would expect <code>kbb</code> to be down at the bottom, since it is no longer active.</p>

#### [ Rob Lewis (Jan 23 2019 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156716265):
<p>Good question. I assumed it was by time of creation, newest first, since Lean Together is at the top. But that doesn't look right. The Zulip API docs imply it's by stream id, lowest first, but that's also wrong.</p>

#### [ Rob Lewis (Jan 23 2019 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156716303):
<p>The answer: "whatever order Zulip gives them in."</p>

#### [ Johan Commelin (Jan 23 2019 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156716366):
<p>How hard would it be to sort them by activity?</p>

#### [ Rob Lewis (Jan 23 2019 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156716370):
<p>Date of creation, newest first and stream id, lowest first should be the same, and stream id is easy to sort by.</p>

#### [ Rob Lewis (Jan 23 2019 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156716492):
<p>Slightly harder than by stream id. That also means the index page will potentially shuffle every time the archive is rebuilt, which seems a little wrong.</p>

#### [ Johan Commelin (Jan 23 2019 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156716547):
<p>Hmmm, maybe it's a little wrong. It isn't very important anyway...</p>

#### [ Mario Carneiro (Jan 24 2019 at 02:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/156739585):
<p>How about number of messages? That should be pretty stable</p>

#### [ Rob Lewis (Feb 03 2019 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/157476726):
<p>I spent a bit more time today playing with this. It turns out, letting Zulip process the markdown solves some of the problems from before. No more formatting problems when people forget closing backticks, automatic linkification, quote formatting is more uniform.</p>

#### [ Rob Lewis (Feb 03 2019 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/157476741):
<p>One problem that gets introduced is that links to other Zulip posts are broken.</p>

#### [ Rob Lewis (Feb 03 2019 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/157476744):
<p>It returns them as relative links.</p>

#### [ Rob Lewis (Feb 03 2019 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/157476808):
<p>My impression is it's a net gain, but I don't have a good idea for solving the link issue. Check it out again and see if anything else looks funny: <a href="https://leanprover-community.github.io/archive/" target="_blank" title="https://leanprover-community.github.io/archive/">https://leanprover-community.github.io/archive/</a></p>

#### [ Rob Lewis (Feb 03 2019 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/157476825):
<p>(Also, I sorted the stream index page by number of topics, which should be about as stable and easier than number of messages.)</p>

#### [ Rob Lewis (Feb 03 2019 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/157477309):
<p>Also, I should check how Zulip sanitizes html. What happens if I write &lt;img src="this.png"&gt; ? (Exactly what should happen, good.)</p>

#### [ Sebastian Ullrich (Feb 03 2019 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/157477480):
<p><span class="user-mention" data-user-id="110596">@Rob Lewis</span> Does <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/base" target="_blank" title="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/base"><code>&lt;base&gt;</code></a> help?</p>

#### [ Rob Lewis (Feb 03 2019 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/157477558):
<p>Oh, yes, that should help a lot!</p>

#### [ Rob Lewis (Feb 03 2019 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/157478873):
<p>Alright, I think it's looking good.</p>

#### [ Rob Lewis (Feb 03 2019 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/157482299):
<p>Ignore this, I need a new post for testing purposes.</p>

#### [ Johan Commelin (Feb 03 2019 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/157482365):
<blockquote>
<p>Ignore this, I need a new post for testing purposes.</p>
</blockquote>
<p>Done</p>

#### [ Johan Commelin (Feb 03 2019 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/157482429):
<p>Ahw, we can't see all the cute emoji's below posts.</p>

#### [ Rob Lewis (Feb 03 2019 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Indexing%20Zulip/near/157485458):
<p>I actually do have access to reactions to posts, but decided it wasn't worth my time to figure out how to display them. <span aria-label="shrug" class="emoji emoji-1f937" role="img" title="shrug">:shrug:</span></p>


{% endraw %}
