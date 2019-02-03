---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/45957reStructuredTextandLean.html
---

## Stream: [general](index.html)
### Topic: [reStructured Text and Lean](45957reStructuredTextandLean.html)

---


{% raw %}
#### [ Simon Hudon (Jun 18 2018 at 03:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128224433):
<p>I'm looking at the build system of <a href="https://github.com/leanprover/theorem_proving_in_lean" target="_blank" title="https://github.com/leanprover/theorem_proving_in_lean">https://github.com/leanprover/theorem_proving_in_lean</a> to adapt Software Foundations and I can't find where the html and latex lean syntax highlighting is defined. Can someone give me a hint?</p>

#### [ Andrew Ashworth (Jun 18 2018 at 04:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128226065):
<p>It's a custom fork of pygments... has it disappeared from the repo?</p>

#### [ Simon Hudon (Jun 18 2018 at 04:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128226112):
<p>It is still working, I just couldn't figure out how to update the syntax (e.g. <code>def</code> instead of <code>definition</code>)</p>

#### [ Simon Hudon (Jun 18 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128226174):
<p>Oh I see that Pygment is referred to in the Makefile. That's pretty much the only place I see it</p>

#### [ Andrew Ashworth (Jun 18 2018 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128226214):
<p>Did you recursively clone git submodules?</p>

#### [ Simon Hudon (Jun 18 2018 at 04:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128226221):
<p>The submodule list seems empty</p>

#### [ Andrew Ashworth (Jun 18 2018 at 04:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128226260):
<p>As an aside, I remember chatting briefly about SF and lean a month ago. I made some progress but I'm slow since it's a weekend thing. If you want to take it up let me know if there's some part I can take care of</p>

#### [ Andrew Ashworth (Jun 18 2018 at 04:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128226264):
<p>Hmm, I'm not at my workstation to see how I handled pygments</p>

#### [ Simon Hudon (Jun 18 2018 at 04:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128226270):
<p>Did you set everything up already?</p>

#### [ Andrew Ashworth (Jun 18 2018 at 04:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128226310):
<p>I have a skeleton project, yes</p>

#### [ Simon Hudon (Jun 18 2018 at 04:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128226315):
<p>Would you care to share it with me. It might be better than starting over :D</p>

#### [ Andrew Ashworth (Jun 18 2018 at 04:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128226330):
<p>Sure, but I can't get to it until tomorrow, unfortunately</p>

#### [ Andrew Ashworth (Jun 18 2018 at 05:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128226379):
<p>Feel free to remind me tomorrow if I forget :)</p>

#### [ Simon Hudon (Jun 18 2018 at 05:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128226380):
<p>It might be best: it's write-o-clock right now (thesis time) so it's best if I have a reason to drop it</p>

#### [ Simon Hudon (Jun 18 2018 at 05:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128226387):
<p>Very well, I will :D</p>

#### [ Gabriel Ebner (Jun 18 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128233813):
<p>Yes, the Lean 3 syntax highlight is not upstream yet.  The makefile installs my fork <a href="https://bitbucket.org/gebner/pygments-main/src" target="_blank" title="https://bitbucket.org/gebner/pygments-main/src">https://bitbucket.org/gebner/pygments-main/src</a> into a venv.</p>

#### [ Kevin Buzzard (Jun 18 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128234422):
<blockquote>
<p>As an aside, I remember chatting briefly about SF and lean a month ago. I made some progress but I'm slow since it's a weekend thing. If you want to take it up let me know if there's some part I can take care of</p>
</blockquote>
<p>My son will be taking this on in early July as part of a work experience project.</p>

#### [ Kevin Buzzard (Jun 18 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128234468):
<p>Only one week and he's learning as he goes so he probably won't do so much.</p>

#### [ Kevin Buzzard (Jun 18 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128234534):
<p>If you've set it up so he could write in rst and it looked beautiful I bet he would oblige. I will probably push him to write it in rst anyway, I've been writing my book in rst using the sphinx lean extension that I took from the TPIL repo and I'm really happy with the results.</p>

#### [ Kevin Buzzard (Jun 18 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128234543):
<p>But he'll have to start from the beginning when it comes to the Coq</p>

#### [ Simon Hudon (Jun 19 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128309829):
<p>I talked to Benjamin Pierce and he's pretty happy that we want to make a Lean version. If we want, we could work off of the SF sources but we'd have to donate the copyrights of our contribution. Otherwise, if we're happy to work with the html, we're free to do as we please</p>

#### [ Simon Hudon (Jun 19 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128310002):
<p>I'm actually on the fence about this decision. Because we use the same template as Theorem Proving in Lean, it seems sufficient to only use the html code. But at the same time, it would be great if we could synchronize the evolution of SF-lean with the evolution of the original</p>

#### [ Andrew Ashworth (Jun 22 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128457493):
<p>I feel guilty about publishing this template since it's quite unpolished, but...</p>

#### [ Andrew Ashworth (Jun 22 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128457495):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> <a href="https://github.com/alashworth/sf-lean" target="_blank" title="https://github.com/alashworth/sf-lean">https://github.com/alashworth/sf-lean</a></p>

#### [ Andrew Ashworth (Jun 22 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128457497):
<p>An example of what it looks like on GH-Pages: <a href="https://alashworth.github.io/sf-lean/vol1/basics.html" target="_blank" title="https://alashworth.github.io/sf-lean/vol1/basics.html">https://alashworth.github.io/sf-lean/vol1/basics.html</a></p>

#### [ Andrew Ashworth (Jun 22 2018 at 08:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128457510):
<p>To compile, first set up a virtual python environment, and then issue <code>pip install https://bitbucket.org/gebner/pygments-main/get/default.tar.gz#egg=Pygments</code></p>

#### [ Andrew Ashworth (Jun 22 2018 at 08:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128457514):
<p>this is in addition to the Sphinx dependency...</p>

#### [ Andrew Ashworth (Jun 22 2018 at 08:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128457800):
<p>This is my first time using Sphinx for documentation... actually, it's pretty nice. When Lean 4 rolls around, maybe I'll take a look at adding a <code>Lean</code> domain.</p>

#### [ Simon Hudon (Jun 22 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128479429):
<p>I'm not fond of working with Python but once it works, it's a nice template</p>

#### [ Simon Hudon (Jun 22 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128479470):
<p>I suggest we setup a travis build and a status for each chapters: adapted text / adapted code / needs review</p>

#### [ Andrew Ashworth (Jun 22 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128484609):
<p>How do you want to handle exercises? Sorry them out as in the original text or have solutions?</p>

#### [ Andrew Ashworth (Jun 22 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128484675):
<p>I'm inclined to having solutions in the text, as this resource will mostly be for self-learners as opposed to a classroom with homework</p>

#### [ Simon Hudon (Jun 22 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128484748):
<p>That's makes sense. However, Benjamin Pierce did request that no exercise solution be posted online. I'd like to see how we can reconcile both goals. Maybe we can hand some solutions out upon request</p>

#### [ Andrew Ashworth (Jun 22 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128484750):
<p>I'll see what I can do regarding travis and others this weekend, then. I wasn't sure if you wanted to fork and work on it yourself or not</p>

#### [ Simon Hudon (Jun 22 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128484765):
<p>I think we could organize around a single repo. At least for now</p>

#### [ Andrew Ashworth (Jun 22 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128484795):
<p>I understand he didn't want solutions online, but 1) it's Lean, not Coq, and 2) solutions are already on Github...</p>

#### [ Simon Hudon (Jun 22 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128485261):
<p>2) if we're the official lean-SF version, we'd be endorsing doing the opposite of what the authors requested. That's different</p>

#### [ Simon Hudon (Jun 22 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128485364):
<p>1) Lean is close enough to Coq that we can translate a Coq book into Lean ...</p>

#### [ Johan Commelin (Jun 22 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128485456):
<p>Suppose that at some point we have a tactic that is able to solve all these exercises... does that mean that this tactic must not be published online?</p>

#### [ Simon Hudon (Jun 22 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128485497):
<p>No, what it would mean is let's not publish it as a solution to the SF exercises</p>

#### [ Andrew Ashworth (Jun 22 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128485526):
<p>It just personally bums me out when solutions aren't given out with a text</p>

#### [ Andrew Ashworth (Jun 22 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128485573):
<p>SF doesn't even give out solutions to odd-numbered exercises or anything like that</p>

#### [ Andrew Ashworth (Jun 22 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128486132):
<p>well, at the end of the day, there's a whole lot of work to be done before this even becomes an issue</p>

#### [ Simon Hudon (Jun 22 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128486180):
<p>That's true</p>

#### [ Simon Hudon (Jun 22 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128486184):
<p>I agree with the need for self-study</p>

#### [ Simon Hudon (Jun 22 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128486191):
<p>I think we should also respect the wishes of the authors</p>

#### [ Simon Hudon (Jun 22 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128486203):
<p>I wonder if there's a way of reconciling both</p>

#### [ Andrew Ashworth (Jun 22 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128486213):
<p>Perhaps we can come up with similar exercises that are "different enough"</p>

#### [ Andrew Ashworth (Jun 22 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128486260):
<p>honestly after having worked through some, the solutions are in the implementation sense pretty different</p>

#### [ Andrew Ashworth (Jun 22 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128486298):
<p>Lean really encourages you to use the equation compiler instead of <code>match</code></p>

#### [ Andrew Ashworth (Jun 22 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128486302):
<p>lots of the lemmas regarding lists are subtly different</p>

#### [ Simon Hudon (Jun 22 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128486312):
<p>That could be an approach. The other thing might be, if it comes to be useful in the classroom, the instructor set might include a variation on the exercises in the book with solutions that we communicate with instructors only</p>

#### [ Simon Hudon (Jun 22 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128486398):
<p>We can keep that issue open. In the mean time, what do you think of it if we ask Pierce to weigh in. We can show him our exercises and solutions and ask him if they are different enough</p>

#### [ Andrew Ashworth (Jun 22 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128486413):
<p>Yep. Let's wait until everything but the exercises is done though... hah. I don't want to show this off in its current state</p>

#### [ Simon Hudon (Jun 22 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128486567):
<p>Fair enough :) I think if courageous users want to try it out while we work, it would be great to get bug reports.</p>

#### [ Simon Hudon (Jun 22 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128488065):
<p>Btw, would you mind giving me commit rights to that repo, I'll start structuring things.</p>

#### [ Andrew Ashworth (Jun 22 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128488396):
<p>sure, sent you a link. the paths definitely need cleaning up, maybe everything under <code>/src</code> should go to <code>/src/vol1</code> for consistency... the source file link is broken in the GH-Pages build</p>

#### [ Simon Hudon (Jun 22 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128488507):
<p>Thanks!</p>

#### [ Simon Hudon (Jun 22 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128488610):
<p>There's a program for encrypted git repos, it's called Keybase. We may want to put the solutions there</p>

#### [ Simon Hudon (Jun 22 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128488914):
<p>Instead of publishing solutions, we may want to dedicate a channel where it's ok to discuss solutions. It might make it easier to give help to people studying the material without broadcasting the solutions</p>

#### [ Simon Hudon (Jun 22 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128495776):
<p>You seem to have taken out all the links to Lean live. Don't you want that connection? That would make it easier to follow the book online, no?</p>

#### [ Andrew Ashworth (Jun 23 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128496096):
<p>It wasn't deliberate,  I was just too lazy to figure out how the <code>lean-sphinx</code> script worked</p>

#### [ Andrew Ashworth (Jun 23 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128496175):
<p>also on the todo list: write up a readme that uses elan for a seamless newbie experience</p>

#### [ Andrew Ashworth (Jun 23 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128496283):
<p>these things are on the bottom of my priority list though, I think translating the content is the first step</p>

#### [ Simon Hudon (Jun 23 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128496371):
<p>Ah good to know! I've been hacking at the scripts this week so I'll just bring my stuff over</p>

#### [ Simon Hudon (Jun 23 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128496581):
<p>How is this for a start?</p>

#### [ Simon Hudon (Jun 23 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128496582):
<p><a href="https://github.com/alashworth/sf-lean" target="_blank" title="https://github.com/alashworth/sf-lean">https://github.com/alashworth/sf-lean</a></p>

#### [ Andrew Ashworth (Jun 23 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128496804):
<p>sounds reasonable and is what i was planning on doing</p>

#### [ Simon Hudon (Jun 23 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128532404):
<p>I'm going to keep working on <code>basics.rst</code> and <code>basics.lean</code>. I think we should checkin with the sections we work on. Conflicts seems much more likely on a project like this.</p>

#### [ Simon Hudon (Jun 23 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128533655):
<p><span class="user-mention" data-user-id="110025">@Andrew Ashworth</span>  when you have a moment can you enable travis build for your repo. I'm about to commit a travis configuration. We just need to link the account with a travis account</p>

#### [ Andrew Ashworth (Jun 24 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535088):
<p>ugh, I tried to get it working with <a href="http://travis-ci.com" target="_blank" title="http://travis-ci.com">travis-ci.com</a> since <a href="http://travis-ci.org" target="_blank" title="http://travis-ci.org">travis-ci.org</a> is deprecated, but apparently I managed to set the repo up on <a href="http://travis-ci.org" target="_blank" title="http://travis-ci.org">travis-ci.org</a> accidentally, and migrations have to be done manually by travis support</p>

#### [ Andrew Ashworth (Jun 24 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535093):
<p>so... I'm waiting to hear back from their account management team</p>

#### [ Simon Hudon (Jun 24 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535145):
<p>I wasn't aware <code>travis-ci.org</code> was deprecated. Does that mean anything for their support for open source projects?</p>

#### [ Andrew Ashworth (Jun 24 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535147):
<p>no, still free, the point is travis wants to unify their commercial and open source together on the same domain (the .com)</p>

#### [ Andrew Ashworth (Jun 24 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535187):
<p>github has marked the legacy travis service as deprecated as well</p>

#### [ Simon Hudon (Jun 24 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535336):
<p>I wonder if we'll see a difference</p>

#### [ Simon Hudon (Jun 24 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535384):
<p>For the snippets, I'm thinking of loading the complete lean file of the current chapter when you click on <code>try it</code>. There's so much continuity that you can't just load them in isolation</p>

#### [ Simon Hudon (Jun 24 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535385):
<p>But I don't like that you'd get that much code to look at when you click <code>try it</code></p>

#### [ Andrew Ashworth (Jun 24 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535392):
<p>that's also the problem with try it</p>

#### [ Andrew Ashworth (Jun 24 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535394):
<p>another reason i didn't spend too much time trying to get it to work</p>

#### [ Andrew Ashworth (Jun 24 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535401):
<p>chapters 1-5 are cumulative</p>

#### [ Simon Hudon (Jun 24 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535453):
<p>I wonder if we could get local files into the live Lean version and just do an <code>import</code></p>

#### [ Simon Hudon (Jun 24 2018 at 00:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535495):
<p>I think those chapters are where the live version would be most profitable</p>

#### [ Andrew Ashworth (Jun 24 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535612):
<p>I personally don't see a lot of value in lean.js, the coding experience is far below vscode or emacs</p>

#### [ Andrew Ashworth (Jun 24 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535615):
<p>sf is sufficiently complicated, and elan so easy to use, hopefully....</p>

#### [ Andrew Ashworth (Jun 24 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535663):
<p>I expect a programmer learning from SF to be able to set up a minimal dev environment? idk</p>

#### [ Simon Hudon (Jun 24 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535714):
<p>Those things are true. I think it helps get you started quicker. If I have to set up a new environment, even when people tell me it will take only a few seconds, I expect I'll have to set aside a few hours so I don't get started until I'm ready to put those hours. If the online version is there, it acts as an argument that it is worth putting the time. Then it comes as a surprise that it actually doesn't take any time</p>

#### [ Andrew Ashworth (Jun 24 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535721):
<p>in addition, apparently there will be a Lean dev environment available on CoCalc at some point</p>

#### [ Simon Hudon (Jun 24 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535761):
<p>I'll have to see that</p>

#### [ Simon Hudon (Jun 24 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535769):
<p>Btw, I really like what you did with </p>
<div class="codehilite"><pre><span></span><span class="p">..</span> <span class="ow">literalinclude</span><span class="p">::</span> ../../src/basics.lean
  <span class="nc">:language:</span> <span class="nf">lean</span>
  <span class="nc">:start-at:</span> <span class="nf">inductive day : Type</span>
  <span class="nc">:end-at:</span> <span class="nf">saturday</span>
</pre></div>


<p>It might become my favorite way of doing literate programming</p>

#### [ Andrew Ashworth (Jun 24 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535795):
<p>i noticed you changed up <code>conf.py</code>. I need to figure out how to add the source directory to the sphinx path</p>

#### [ Andrew Ashworth (Jun 24 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535809):
<p>ahh, maybe tomorrow</p>

#### [ Simon Hudon (Jun 24 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535812):
<p>Haha :) Sorry, it was pretty draconian. We can sit down together to mitigate the damage</p>

#### [ Simon Hudon (Jun 24 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535813):
<p>Anyway, food is calling to me</p>

#### [ Andrew Ashworth (Jun 24 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535820):
<p>np! enjoy dinner</p>

#### [ Simon Hudon (Jun 24 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535882):
<p>Thanks!</p>

#### [ Andrew Ashworth (Jun 24 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128536200):
<blockquote>
<p>Btw, I really like what you did with </p>
<div class="codehilite"><pre><span></span><span class="p">..</span> <span class="ow">literalinclude</span><span class="p">::</span> ../../src/basics.lean
  <span class="nc">:language:</span> <span class="nf">lean</span>
  <span class="nc">:start-at:</span> <span class="nf">inductive day : Type</span>
  <span class="nc">:end-at:</span> <span class="nf">saturday</span>
</pre></div>


<p>It might become my favorite way of doing literate programming</p>
</blockquote>
<p>I'm not a huge fan of Sphinx's ability to match strings. I don't understand how it works, and it often fails for me</p>

#### [ Andrew Ashworth (Jun 24 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128536245):
<p>so much so that when I was writing that basics.rst snippet I had a text editor on one screen and a terminal + chrome window on the other so I could do a terrible version of <code>live preview</code></p>

#### [ Simon Hudon (Jun 24 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128537927):
<p>Do you use emacs or VS code?</p>

#### [ Simon Hudon (Jun 24 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128538449):
<p>Also, how do you update your <code>gh-pages</code>?</p>

#### [ Andrew Ashworth (Jun 24 2018 at 03:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128540016):
<p>the old fashioned way: cut and paste</p>

#### [ Andrew Ashworth (Jun 24 2018 at 03:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128540020):
<p>if you want to script it, you could try using <a href="https://github.com/davisp/ghp-import" target="_blank" title="https://github.com/davisp/ghp-import">https://github.com/davisp/ghp-import</a>, which is on my 'to-investigate' list</p>

#### [ Simon Hudon (Jun 24 2018 at 04:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128540483):
<p>So if I play the elaborator, you compile the <code>rst</code> files and copy all the <code>html</code> files in <code>vol1</code> and then commit that</p>

#### [ Andrew Ashworth (Jun 24 2018 at 04:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128540576):
<p>at project root, issue <code>make html</code>, then copy <code>build/html</code> to the root dir, and commit this to the <code>gh-pages</code> branch</p>

#### [ Simon Hudon (Jun 24 2018 at 04:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128540586):
<p>Even better! Thanks!</p>

#### [ Andrew Ashworth (Jun 24 2018 at 04:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128540587):
<p>this is with my version of <code>conf.py</code>, I haven't checked if TPIL's <code>conf.py</code> does things differently</p>

#### [ Simon Hudon (Jun 24 2018 at 04:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128540589):
<p>When it comes to the web,  I'm kind of an ignoramus</p>

#### [ Andrew Ashworth (Jun 24 2018 at 04:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128540634):
<p>yeah, I'm not a web programmer either... I think I know just enough to be dangerous</p>

#### [ Simon Hudon (Jun 24 2018 at 04:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128540821):
<p>Haha :D that's still more than me</p>

#### [ Andrew Ashworth (Jun 24 2018 at 05:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542120):
<p>can you go into more detail about the <code>def</code> issue you just raised? <a href="https://alashworth.github.io/sf-lean/vol1/basics.html" target="_blank" title="https://alashworth.github.io/sf-lean/vol1/basics.html">https://alashworth.github.io/sf-lean/vol1/basics.html</a> - <code>def</code> is colored green for me</p>

#### [ Andrew Ashworth (Jun 24 2018 at 05:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542160):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span></p>

#### [ Simon Hudon (Jun 24 2018 at 05:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542164):
<p>Interesting, it doesn't get colored for me. Maybe we have inconsistent stylesheets?</p>

#### [ Andrew Ashworth (Jun 24 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542171):
<p>so when you navigate to that page, <code>def</code> isn't highlighted?</p>

#### [ Simon Hudon (Jun 24 2018 at 05:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542320):
<p>Exactly</p>

#### [ Simon Hudon (Jun 24 2018 at 05:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542321):
<p>Have a look at:</p>
<p><a href="https://alashworth.github.io/sf-lean/vol1/basics.html" target="_blank" title="https://alashworth.github.io/sf-lean/vol1/basics.html">https://alashworth.github.io/sf-lean/vol1/basics.html#</a></p>

#### [ Simon Hudon (Jun 24 2018 at 05:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542326):
<p>(btw, feel free to criticize the end of the <em>Numbers</em> section. I had to take some creative freedom)</p>

#### [ Andrew Ashworth (Jun 24 2018 at 05:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542380):
<p>yeah, i'm looking at it</p>

#### [ Andrew Ashworth (Jun 24 2018 at 05:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542381):
<div class="message_inline_image"><a href="https://snag.gy/4BEKAc.jpg" target="_blank" title="https://snag.gy/4BEKAc.jpg"><img src="https://snag.gy/4BEKAc.jpg"></a></div>

#### [ Andrew Ashworth (Jun 24 2018 at 05:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542384):
<p>is this what it looks like for you? if not, I think something is up on your end</p>

#### [ Andrew Ashworth (Jun 24 2018 at 05:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542394):
<p>oh</p>

#### [ Andrew Ashworth (Jun 24 2018 at 05:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542395):
<p>you pushed something new</p>

#### [ Simon Hudon (Jun 24 2018 at 05:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542396):
<p>I think you should refresh. I just updated it</p>

#### [ Andrew Ashworth (Jun 24 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542438):
<p>if it's only def, the likely reason is that you have conflicting versions of pygments installed</p>

#### [ Andrew Ashworth (Jun 24 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542439):
<p>then when you compile, the html isn't getting styled correctly as a result</p>

#### [ Simon Hudon (Jun 24 2018 at 05:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542499):
<p>How do I fix that?</p>

#### [ Andrew Ashworth (Jun 24 2018 at 05:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542546):
<p>pip uninstall pygments</p>

#### [ Andrew Ashworth (Jun 24 2018 at 05:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542549):
<p>then reinstall from the pygments fork</p>

#### [ Simon Hudon (Jun 24 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542718):
<p>It worked like a charm! Thanks :)</p>

#### [ Andrew Ashworth (Jun 24 2018 at 05:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542762):
<p>np</p>

#### [ Simon Hudon (Jun 24 2018 at 05:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542763):
<p>Btw: I decided to take the lazy way for publishing and I did <code>git init</code> in <code>build/html</code> and added <code>gh-pages</code> as a remote. It doesn't seem too bad</p>

#### [ Andrew Ashworth (Jun 24 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542771):
<p>yep, i bet that would work too</p>

#### [ Andrew Ashworth (Jun 24 2018 at 05:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542811):
<p>that is actually lazier than cut and paste... wish i'd done that first</p>

#### [ Simon Hudon (Jun 24 2018 at 05:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542864):
<p>I work pretty hard to be this lazy <span class="emoji emoji-1f61d" title="stuck out tongue closed eyes">:stuck_out_tongue_closed_eyes:</span></p>

#### [ Simon Hudon (Jun 24 2018 at 05:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542904):
<p>It should look better now  at <a href="https://alashworth.github.io/sf-lean/vol1/basics.html" target="_blank" title="https://alashworth.github.io/sf-lean/vol1/basics.html">https://alashworth.github.io/sf-lean/vol1/basics.html#</a></p>

#### [ Andrew Ashworth (Jun 24 2018 at 05:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542948):
<p>hmm, the try it hyperlink overlaps code</p>

#### [ Simon Hudon (Jun 24 2018 at 05:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542954):
<p>Which one?</p>

#### [ Andrew Ashworth (Jun 24 2018 at 05:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542956):
<p>all the one liner defs and examples</p>

#### [ Andrew Ashworth (Jun 24 2018 at 05:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542998):
<p>for example, <code>example : next_weekday (next_weekday day...</code></p>

#### [ Simon Hudon (Jun 24 2018 at 05:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128543007):
<p>Ah! Do you mean that it displays "try it" on top of the code? I thought somehow snippets got mixed up when sent to Lean Live</p>

#### [ Andrew Ashworth (Jun 24 2018 at 05:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128543050):
<p>the way the try it works with snippets is not very suitable to how SF is currently laid out</p>

#### [ Andrew Ashworth (Jun 24 2018 at 05:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128543051):
<p>for example, none of the nat playground stuff works because the namespace command isn't sent to lean.js</p>

#### [ Andrew Ashworth (Jun 24 2018 at 05:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128543058):
<p>i would like to revert <code>conf.py</code> until one of us has time to really sit down and make it work correctly.</p>

#### [ Simon Hudon (Jun 24 2018 at 05:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128543059):
<p>The snippets have a lot of problems. I'd like to send the whole file over</p>

#### [ Simon Hudon (Jun 24 2018 at 05:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128543060):
<p>Sure. What does your version do?</p>

#### [ Andrew Ashworth (Jun 24 2018 at 05:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128543061):
<p>no "try it" at all</p>

#### [ Simon Hudon (Jun 24 2018 at 05:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128543100):
<p>I could work on the "try it" in a branch until I get it right</p>

#### [ Andrew Ashworth (Jun 24 2018 at 05:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128543101):
<p>to make it work correctly, we need to build lean live with our own lean source files</p>

#### [ Andrew Ashworth (Jun 24 2018 at 05:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128543102):
<p>and we also need some way to send a scroll command</p>

#### [ Andrew Ashworth (Jun 24 2018 at 05:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128543103):
<p>or embed a line position in the hyperlink</p>

#### [ Andrew Ashworth (Jun 24 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128543110):
<p>if we do want to have a web link</p>

#### [ Simon Hudon (Jun 24 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128543111):
<p>That would be good, you're right.</p>

#### [ Andrew Ashworth (Jun 24 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128543113):
<p>then we should perhaps link the whole source file at the top of the chapter</p>

#### [ Andrew Ashworth (Jun 24 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128543114):
<p>and ask people to scroll down as they read</p>

#### [ Andrew Ashworth (Jun 24 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128543115):
<p>that's the low-effort way</p>

#### [ Simon Hudon (Jun 24 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128543116):
<p>Maybe we can recruit <span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> or <span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> to help us with that</p>

#### [ Simon Hudon (Jun 24 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128543158):
<p>Yeah, and then the link can bring up Lean Live at the right line number</p>

#### [ Andrew Ashworth (Jun 24 2018 at 05:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128543204):
<p>yeah, i think for now it would be best to work on it in its own branch</p>

#### [ Andrew Ashworth (Jun 24 2018 at 05:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128543252):
<p>TPIL does some trickery with selectively hiding lines</p>

#### [ Kevin Buzzard (Jun 24 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128551894):
<p>So this all looks really good -- both nice to look at, and great material. Is it really not an issue that the text is basically all lifted from someone else's work? If not then that's awesome.  My son will be starting on doing the exercises on Monday 2nd July, he is a beginner but he's a decent python programmer and is hopefully smart enough to learn quickly (and I can help him of course). I was going to advise him to just read SF in the original Coq and I was going to help him translate, but if he can read the translated stuff that would be awesome. I have done many of the exercises of Part 1 in Lean myself and I will have the answers somewhere -- I did them once I knew a lot about how Lean worked so they weren't too much trouble.</p>

#### [ Simon Hudon (Jun 24 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128557593):
<p>Great! And please send us comments as you go if there are parts that don't quite add up.</p>
<blockquote>
<p>Is it really not an issue that the text is basically all lifted from someone else's work?</p>
</blockquote>
<p>Not an issue. The html version of the book is under MIT license and I talked to the author. He seems pretty happy that we're doing that and had great information on how to proceed.</p>

#### [ Simon Hudon (Jun 24 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128557639):
<p>(comments or even contribution to the text)</p>

#### [ Simon Hudon (Jun 24 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128560717):
<p><span class="user-mention" data-user-id="110025">@Andrew Ashworth</span> What was the reason for you to use to specify lean snippets in a single Lean file instead of inline in the <code>rst</code> file? I'm thinking it might be easier to write this way, especially considering that the flow of the chapter pretty much follows the declaration flow.</p>

#### [ Andrew Ashworth (Jun 24 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561026):
<p>later in the book we will want to use leanpkg to manage dependencies on <code>cooper</code> and <code>mathlib</code></p>

#### [ Andrew Ashworth (Jun 24 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561033):
<p>the more involved exercises use a lot of <code>omega</code></p>

#### [ Simon Hudon (Jun 24 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561079):
<p>I thought we could use a make file to first generate the Lean sources and then call <code>leanpkg</code></p>

#### [ Simon Hudon (Jun 24 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561086):
<p>The biggest downside I see is with debugging the Lean code</p>

#### [ Andrew Ashworth (Jun 24 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561256):
<p>i think a common way to interact with the textbook will be for people to clone the repository and step through the source files themselves</p>

#### [ Andrew Ashworth (Jun 24 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561258):
<p>you can't work with the .rst file like a .lean file</p>

#### [ Simon Hudon (Jun 24 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561268):
<p>That's true. I'd really like for there to be a literate mode to Lean</p>

#### [ Simon Hudon (Jun 24 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561310):
<p>I think we can offer a similar experience though by building an archive file that people can download. And in that file, we put the Lean generate files and the <code>rst</code> files, to follow along.</p>

#### [ Andrew Ashworth (Jun 24 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561360):
<p>i can't comment on this approach since I don't know how the TPIL <code>lean-sphinx</code> node parsing code works</p>

#### [ Simon Hudon (Jun 24 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561373):
<p>I think that's feasible. Remains to see if it's a workflow we're comfortable with</p>

#### [ Andrew Ashworth (Jun 24 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561414):
<p>from a gut feeling perspective, it feels backwards to me. If I had unlimited time, I would write a Lean plugin for sphinx so we could move even more comments and documentation into the <code>.lean</code> files</p>

#### [ Simon Hudon (Jun 24 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561474):
<p>Yeah, I'd love that</p>

#### [ Andrew Ashworth (Jun 24 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561475):
<p>from a teaching perspective, I think it's nice if the project demonstrates how to manage a larger Lean development</p>

#### [ Simon Hudon (Jun 24 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561478):
<p>I've been asking for a literate mode for a while. Maybe Lean 4 will make it easier to do ...</p>

#### [ Andrew Ashworth (Jun 24 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561517):
<p>the inline code approach with snippets is attractive because it enables us to reuse all the scripts from TPIL, and in particular maybe make it easier to enable 'try it'</p>

#### [ Andrew Ashworth (Jun 24 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561519):
<p>well, you already know how I feel about how useful that functionality is</p>

#### [ Simon Hudon (Jun 24 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561526):
<p>Are you referring to a previous conversation ... I only have vague memories of that. You weren't too favorable to the idea, were you?</p>

#### [ Andrew Ashworth (Jun 24 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561528):
<p>well, to recap, I think it's a big hassle for us to make it work correctly</p>

#### [ Simon Hudon (Jun 24 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561574):
<p>For us the users?</p>

#### [ Andrew Ashworth (Jun 24 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561577):
<p>for us, the authors</p>

#### [ Andrew Ashworth (Jun 24 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561579):
<p>and also nobody is going to want to be doing the more involved exercises in lean.js</p>

#### [ Andrew Ashworth (Jun 24 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561629):
<p>I think between <code>elan</code> and a possible Lean environment being set up on co-calc, its not a good use of time to try and get it to work, when there's so much translation effort to be done</p>

#### [ Simon Hudon (Jun 24 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561635):
<p>I think you misunderstood my point about literate programming. The point is to have the html and pdf generated from a Lean file, the prose is considered as comment when compiling so you don't have to maintain two separate sets of files when writing tutorials or blogs or books</p>

#### [ Andrew Ashworth (Jun 24 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561645):
<p>if you want something similar to <code>coqtop</code></p>

#### [ Andrew Ashworth (Jun 24 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561647):
<p>a Sphinx plugin would do that</p>

#### [ Andrew Ashworth (Jun 24 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561649):
<p>it could be written today</p>

#### [ Andrew Ashworth (Jun 24 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561693):
<p>but that doesn't help you when you want to discuss things out of the order they are defined in the source</p>

#### [ Andrew Ashworth (Jun 24 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561696):
<p>then i think the way sf-lean is currently structured is the best</p>

#### [ Simon Hudon (Jun 24 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128562294):
<p>That's something I've been arguing for as well. If lean provided a declaration like <code>postpone my_foo your_foo their_foo</code> then that could allow you to make small breaks in the declaration order.</p>

#### [ Jesse Michael Han (Jun 25 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128606397):
<p>it'd be nice also if extracted Lean snippets (a la TPIL) could refer to/import each other---this is something that'll come up sooner or later in the formal abstracts project, since there'll be theorems we want to formally state that require other definitions/theorems that only exist as formal abstract snippets</p>

#### [ Simon Hudon (Jun 25 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128606809):
<p>I'm not too familiar with the formal abstracts project. Do you mean that you'd like in Lean Live to import <br>
chapters of TPIL?</p>

#### [ Jesse Michael Han (Jun 25 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128607230):
<p>Currently it's organized as a Sphinx project with Gabriel's lean_sphinx extension: <a href="https://github.com/thalesant/formalabstracts" target="_blank" title="https://github.com/thalesant/formalabstracts">https://github.com/thalesant/formalabstracts</a></p>
<p>I mean that if there's a page for e.g. the continuum hypothesis, containing a code block, then i'd like to be able to import that code block when i write a new page about the independence of the continuum hypothesis</p>

#### [ Simon Hudon (Jun 25 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128607985):
<p>I see so if the whole project was source code would make it easier to use. I agree</p>

#### [ Kevin Buzzard (Jul 02 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128953236):
<blockquote>
<p>It should look better now  at <a href="https://alashworth.github.io/sf-lean/vol1/basics.html" target="_blank" title="https://alashworth.github.io/sf-lean/vol1/basics.html">https://alashworth.github.io/sf-lean/vol1/basics.html#</a></p>
</blockquote>
<p>OK so my son is going to start on the exercises today. Many thanks to both Andrew and Simon for making his life less difficult!</p>

#### [ Elliott Macneil (Jul 02 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128955649):
<p>I'm wondering if someone could possibly direct me to where the source code (the file basic.lean) is, as the link on the website doesn't work</p>

#### [ Patrick Massot (Jul 02 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128955713):
<p><a href="https://github.com/alashworth/sf-lean/blob/lean-3.4.1/src/basics.lean" target="_blank" title="https://github.com/alashworth/sf-lean/blob/lean-3.4.1/src/basics.lean">https://github.com/alashworth/sf-lean/blob/lean-3.4.1/src/basics.lean</a></p>

#### [ Elliott Macneil (Jul 02 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128955765):
<p>Thanks!</p>


{% endraw %}
