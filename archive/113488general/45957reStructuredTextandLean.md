---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/45957reStructuredTextandLean.html
---

## Stream: [general](index.html)
### Topic: [reStructured Text and Lean](45957reStructuredTextandLean.html)

---

#### [Simon Hudon (Jun 18 2018 at 03:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128224433):
I'm looking at the build system of https://github.com/leanprover/theorem_proving_in_lean to adapt Software Foundations and I can't find where the html and latex lean syntax highlighting is defined. Can someone give me a hint?

#### [Andrew Ashworth (Jun 18 2018 at 04:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128226065):
It's a custom fork of pygments... has it disappeared from the repo?

#### [Simon Hudon (Jun 18 2018 at 04:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128226112):
It is still working, I just couldn't figure out how to update the syntax (e.g. `def` instead of `definition`)

#### [Simon Hudon (Jun 18 2018 at 04:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128226174):
Oh I see that Pygment is referred to in the Makefile. That's pretty much the only place I see it

#### [Andrew Ashworth (Jun 18 2018 at 04:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128226214):
Did you recursively clone git submodules?

#### [Simon Hudon (Jun 18 2018 at 04:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128226221):
The submodule list seems empty

#### [Andrew Ashworth (Jun 18 2018 at 04:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128226260):
As an aside, I remember chatting briefly about SF and lean a month ago. I made some progress but I'm slow since it's a weekend thing. If you want to take it up let me know if there's some part I can take care of

#### [Andrew Ashworth (Jun 18 2018 at 04:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128226264):
Hmm, I'm not at my workstation to see how I handled pygments

#### [Simon Hudon (Jun 18 2018 at 04:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128226270):
Did you set everything up already?

#### [Andrew Ashworth (Jun 18 2018 at 04:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128226310):
I have a skeleton project, yes

#### [Simon Hudon (Jun 18 2018 at 04:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128226315):
Would you care to share it with me. It might be better than starting over :D

#### [Andrew Ashworth (Jun 18 2018 at 04:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128226330):
Sure, but I can't get to it until tomorrow, unfortunately

#### [Andrew Ashworth (Jun 18 2018 at 05:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128226379):
Feel free to remind me tomorrow if I forget :)

#### [Simon Hudon (Jun 18 2018 at 05:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128226380):
It might be best: it's write-o-clock right now (thesis time) so it's best if I have a reason to drop it

#### [Simon Hudon (Jun 18 2018 at 05:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128226387):
Very well, I will :D

#### [Gabriel Ebner (Jun 18 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128233813):
Yes, the Lean 3 syntax highlight is not upstream yet.  The makefile installs my fork https://bitbucket.org/gebner/pygments-main/src into a venv.

#### [Kevin Buzzard (Jun 18 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128234422):
```quote
As an aside, I remember chatting briefly about SF and lean a month ago. I made some progress but I'm slow since it's a weekend thing. If you want to take it up let me know if there's some part I can take care of
```
My son will be taking this on in early July as part of a work experience project.

#### [Kevin Buzzard (Jun 18 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128234468):
Only one week and he's learning as he goes so he probably won't do so much.

#### [Kevin Buzzard (Jun 18 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128234534):
If you've set it up so he could write in rst and it looked beautiful I bet he would oblige. I will probably push him to write it in rst anyway, I've been writing my book in rst using the sphinx lean extension that I took from the TPIL repo and I'm really happy with the results.

#### [Kevin Buzzard (Jun 18 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128234543):
But he'll have to start from the beginning when it comes to the Coq

#### [Simon Hudon (Jun 19 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128309829):
I talked to Benjamin Pierce and he's pretty happy that we want to make a Lean version. If we want, we could work off of the SF sources but we'd have to donate the copyrights of our contribution. Otherwise, if we're happy to work with the html, we're free to do as we please

#### [Simon Hudon (Jun 19 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128310002):
I'm actually on the fence about this decision. Because we use the same template as Theorem Proving in Lean, it seems sufficient to only use the html code. But at the same time, it would be great if we could synchronize the evolution of SF-lean with the evolution of the original

#### [Andrew Ashworth (Jun 22 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128457493):
I feel guilty about publishing this template since it's quite unpolished, but...

#### [Andrew Ashworth (Jun 22 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128457495):
@**Simon Hudon** https://github.com/alashworth/sf-lean

#### [Andrew Ashworth (Jun 22 2018 at 08:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128457497):
An example of what it looks like on GH-Pages: https://alashworth.github.io/sf-lean/vol1/basics.html

#### [Andrew Ashworth (Jun 22 2018 at 08:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128457510):
To compile, first set up a virtual python environment, and then issue `pip install https://bitbucket.org/gebner/pygments-main/get/default.tar.gz#egg=Pygments`

#### [Andrew Ashworth (Jun 22 2018 at 08:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128457514):
this is in addition to the Sphinx dependency...

#### [Andrew Ashworth (Jun 22 2018 at 08:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128457800):
This is my first time using Sphinx for documentation... actually, it's pretty nice. When Lean 4 rolls around, maybe I'll take a look at adding a `Lean` domain.

#### [Simon Hudon (Jun 22 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128479429):
I'm not fond of working with Python but once it works, it's a nice template

#### [Simon Hudon (Jun 22 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128479470):
I suggest we setup a travis build and a status for each chapters: adapted text / adapted code / needs review

#### [Andrew Ashworth (Jun 22 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128484609):
How do you want to handle exercises? Sorry them out as in the original text or have solutions?

#### [Andrew Ashworth (Jun 22 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128484675):
I'm inclined to having solutions in the text, as this resource will mostly be for self-learners as opposed to a classroom with homework

#### [Simon Hudon (Jun 22 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128484748):
That's makes sense. However, Benjamin Pierce did request that no exercise solution be posted online. I'd like to see how we can reconcile both goals. Maybe we can hand some solutions out upon request

#### [Andrew Ashworth (Jun 22 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128484750):
I'll see what I can do regarding travis and others this weekend, then. I wasn't sure if you wanted to fork and work on it yourself or not

#### [Simon Hudon (Jun 22 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128484765):
I think we could organize around a single repo. At least for now

#### [Andrew Ashworth (Jun 22 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128484795):
I understand he didn't want solutions online, but 1) it's Lean, not Coq, and 2) solutions are already on Github...

#### [Simon Hudon (Jun 22 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128485261):
2) if we're the official lean-SF version, we'd be endorsing doing the opposite of what the authors requested. That's different

#### [Simon Hudon (Jun 22 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128485364):
1) Lean is close enough to Coq that we can translate a Coq book into Lean ...

#### [Johan Commelin (Jun 22 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128485456):
Suppose that at some point we have a tactic that is able to solve all these exercises... does that mean that this tactic must not be published online?

#### [Simon Hudon (Jun 22 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128485497):
No, what it would mean is let's not publish it as a solution to the SF exercises

#### [Andrew Ashworth (Jun 22 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128485526):
It just personally bums me out when solutions aren't given out with a text

#### [Andrew Ashworth (Jun 22 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128485573):
SF doesn't even give out solutions to odd-numbered exercises or anything like that

#### [Andrew Ashworth (Jun 22 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128486132):
well, at the end of the day, there's a whole lot of work to be done before this even becomes an issue

#### [Simon Hudon (Jun 22 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128486180):
That's true

#### [Simon Hudon (Jun 22 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128486184):
I agree with the need for self-study

#### [Simon Hudon (Jun 22 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128486191):
I think we should also respect the wishes of the authors

#### [Simon Hudon (Jun 22 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128486203):
I wonder if there's a way of reconciling both

#### [Andrew Ashworth (Jun 22 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128486213):
Perhaps we can come up with similar exercises that are "different enough"

#### [Andrew Ashworth (Jun 22 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128486260):
honestly after having worked through some, the solutions are in the implementation sense pretty different

#### [Andrew Ashworth (Jun 22 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128486298):
Lean really encourages you to use the equation compiler instead of `match`

#### [Andrew Ashworth (Jun 22 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128486302):
lots of the lemmas regarding lists are subtly different

#### [Simon Hudon (Jun 22 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128486312):
That could be an approach. The other thing might be, if it comes to be useful in the classroom, the instructor set might include a variation on the exercises in the book with solutions that we communicate with instructors only

#### [Simon Hudon (Jun 22 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128486398):
We can keep that issue open. In the mean time, what do you think of it if we ask Pierce to weigh in. We can show him our exercises and solutions and ask him if they are different enough

#### [Andrew Ashworth (Jun 22 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128486413):
Yep. Let's wait until everything but the exercises is done though... hah. I don't want to show this off in its current state

#### [Simon Hudon (Jun 22 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128486567):
Fair enough :) I think if courageous users want to try it out while we work, it would be great to get bug reports.

#### [Simon Hudon (Jun 22 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128488065):
Btw, would you mind giving me commit rights to that repo, I'll start structuring things.

#### [Andrew Ashworth (Jun 22 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128488396):
sure, sent you a link. the paths definitely need cleaning up, maybe everything under `/src` should go to `/src/vol1` for consistency... the source file link is broken in the GH-Pages build

#### [Simon Hudon (Jun 22 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128488507):
Thanks!

#### [Simon Hudon (Jun 22 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128488610):
There's a program for encrypted git repos, it's called Keybase. We may want to put the solutions there

#### [Simon Hudon (Jun 22 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128488914):
Instead of publishing solutions, we may want to dedicate a channel where it's ok to discuss solutions. It might make it easier to give help to people studying the material without broadcasting the solutions

#### [Simon Hudon (Jun 22 2018 at 23:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128495776):
You seem to have taken out all the links to Lean live. Don't you want that connection? That would make it easier to follow the book online, no?

#### [Andrew Ashworth (Jun 23 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128496096):
It wasn't deliberate,  I was just too lazy to figure out how the `lean-sphinx` script worked

#### [Andrew Ashworth (Jun 23 2018 at 00:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128496175):
also on the todo list: write up a readme that uses elan for a seamless newbie experience

#### [Andrew Ashworth (Jun 23 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128496283):
these things are on the bottom of my priority list though, I think translating the content is the first step

#### [Simon Hudon (Jun 23 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128496371):
Ah good to know! I've been hacking at the scripts this week so I'll just bring my stuff over

#### [Simon Hudon (Jun 23 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128496581):
How is this for a start?

#### [Simon Hudon (Jun 23 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128496582):
https://github.com/alashworth/sf-lean

#### [Andrew Ashworth (Jun 23 2018 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128496804):
sounds reasonable and is what i was planning on doing

#### [Simon Hudon (Jun 23 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128532404):
I'm going to keep working on `basics.rst` and `basics.lean`. I think we should checkin with the sections we work on. Conflicts seems much more likely on a project like this.

#### [Simon Hudon (Jun 23 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128533655):
@**Andrew Ashworth**  when you have a moment can you enable travis build for your repo. I'm about to commit a travis configuration. We just need to link the account with a travis account

#### [Andrew Ashworth (Jun 24 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535088):
ugh, I tried to get it working with travis-ci.com since travis-ci.org is deprecated, but apparently I managed to set the repo up on travis-ci.org accidentally, and migrations have to be done manually by travis support

#### [Andrew Ashworth (Jun 24 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535093):
so... I'm waiting to hear back from their account management team

#### [Simon Hudon (Jun 24 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535145):
I wasn't aware `travis-ci.org` was deprecated. Does that mean anything for their support for open source projects?

#### [Andrew Ashworth (Jun 24 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535147):
no, still free, the point is travis wants to unify their commercial and open source together on the same domain (the .com)

#### [Andrew Ashworth (Jun 24 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535187):
github has marked the legacy travis service as deprecated as well

#### [Simon Hudon (Jun 24 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535336):
I wonder if we'll see a difference

#### [Simon Hudon (Jun 24 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535384):
For the snippets, I'm thinking of loading the complete lean file of the current chapter when you click on `try it`. There's so much continuity that you can't just load them in isolation

#### [Simon Hudon (Jun 24 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535385):
But I don't like that you'd get that much code to look at when you click `try it`

#### [Andrew Ashworth (Jun 24 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535392):
that's also the problem with try it

#### [Andrew Ashworth (Jun 24 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535394):
another reason i didn't spend too much time trying to get it to work

#### [Andrew Ashworth (Jun 24 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535401):
chapters 1-5 are cumulative

#### [Simon Hudon (Jun 24 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535453):
I wonder if we could get local files into the live Lean version and just do an `import`

#### [Simon Hudon (Jun 24 2018 at 00:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535495):
I think those chapters are where the live version would be most profitable

#### [Andrew Ashworth (Jun 24 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535612):
I personally don't see a lot of value in lean.js, the coding experience is far below vscode or emacs

#### [Andrew Ashworth (Jun 24 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535615):
sf is sufficiently complicated, and elan so easy to use, hopefully....

#### [Andrew Ashworth (Jun 24 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535663):
I expect a programmer learning from SF to be able to set up a minimal dev environment? idk

#### [Simon Hudon (Jun 24 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535714):
Those things are true. I think it helps get you started quicker. If I have to set up a new environment, even when people tell me it will take only a few seconds, I expect I'll have to set aside a few hours so I don't get started until I'm ready to put those hours. If the online version is there, it acts as an argument that it is worth putting the time. Then it comes as a surprise that it actually doesn't take any time

#### [Andrew Ashworth (Jun 24 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535721):
in addition, apparently there will be a Lean dev environment available on CoCalc at some point

#### [Simon Hudon (Jun 24 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535761):
I'll have to see that

#### [Simon Hudon (Jun 24 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535769):
Btw, I really like what you did with 

```rst
.. literalinclude:: ../../src/basics.lean
  :language: lean
  :start-at: inductive day : Type
  :end-at: saturday
```

It might become my favorite way of doing literate programming

#### [Andrew Ashworth (Jun 24 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535795):
i noticed you changed up `conf.py`. I need to figure out how to add the source directory to the sphinx path

#### [Andrew Ashworth (Jun 24 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535809):
ahh, maybe tomorrow

#### [Simon Hudon (Jun 24 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535812):
Haha :) Sorry, it was pretty draconian. We can sit down together to mitigate the damage

#### [Simon Hudon (Jun 24 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535813):
Anyway, food is calling to me

#### [Andrew Ashworth (Jun 24 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535820):
np! enjoy dinner

#### [Simon Hudon (Jun 24 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128535882):
Thanks!

#### [Andrew Ashworth (Jun 24 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128536200):
```quote
Btw, I really like what you did with 

```rst
.. literalinclude:: ../../src/basics.lean
  :language: lean
  :start-at: inductive day : Type
  :end-at: saturday
```

It might become my favorite way of doing literate programming
```
I'm not a huge fan of Sphinx's ability to match strings. I don't understand how it works, and it often fails for me

#### [Andrew Ashworth (Jun 24 2018 at 01:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128536245):
so much so that when I was writing that basics.rst snippet I had a text editor on one screen and a terminal + chrome window on the other so I could do a terrible version of `live preview`

#### [Simon Hudon (Jun 24 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128537927):
Do you use emacs or VS code?

#### [Simon Hudon (Jun 24 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128538449):
Also, how do you update your `gh-pages`?

#### [Andrew Ashworth (Jun 24 2018 at 03:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128540016):
the old fashioned way: cut and paste

#### [Andrew Ashworth (Jun 24 2018 at 03:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128540020):
if you want to script it, you could try using https://github.com/davisp/ghp-import, which is on my 'to-investigate' list

#### [Simon Hudon (Jun 24 2018 at 04:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128540483):
So if I play the elaborator, you compile the `rst` files and copy all the `html` files in `vol1` and then commit that

#### [Andrew Ashworth (Jun 24 2018 at 04:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128540576):
at project root, issue `make html`, then copy `build/html` to the root dir, and commit this to the `gh-pages` branch

#### [Simon Hudon (Jun 24 2018 at 04:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128540586):
Even better! Thanks!

#### [Andrew Ashworth (Jun 24 2018 at 04:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128540587):
this is with my version of `conf.py`, I haven't checked if TPIL's `conf.py` does things differently

#### [Simon Hudon (Jun 24 2018 at 04:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128540589):
When it comes to the web,  I'm kind of an ignoramus

#### [Andrew Ashworth (Jun 24 2018 at 04:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128540634):
yeah, I'm not a web programmer either... I think I know just enough to be dangerous

#### [Simon Hudon (Jun 24 2018 at 04:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128540821):
Haha :D that's still more than me

#### [Andrew Ashworth (Jun 24 2018 at 05:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542120):
can you go into more detail about the `def` issue you just raised? https://alashworth.github.io/sf-lean/vol1/basics.html - `def` is colored green for me

#### [Andrew Ashworth (Jun 24 2018 at 05:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542160):
@**Simon Hudon**

#### [Simon Hudon (Jun 24 2018 at 05:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542164):
Interesting, it doesn't get colored for me. Maybe we have inconsistent stylesheets?

#### [Andrew Ashworth (Jun 24 2018 at 05:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542171):
so when you navigate to that page, `def` isn't highlighted?

#### [Simon Hudon (Jun 24 2018 at 05:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542320):
Exactly

#### [Simon Hudon (Jun 24 2018 at 05:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542321):
Have a look at:

https://alashworth.github.io/sf-lean/vol1/basics.html#

#### [Simon Hudon (Jun 24 2018 at 05:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542326):
(btw, feel free to criticize the end of the *Numbers* section. I had to take some creative freedom)

#### [Andrew Ashworth (Jun 24 2018 at 05:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542380):
yeah, i'm looking at it

#### [Andrew Ashworth (Jun 24 2018 at 05:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542381):
https://snag.gy/4BEKAc.jpg

#### [Andrew Ashworth (Jun 24 2018 at 05:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542384):
is this what it looks like for you? if not, I think something is up on your end

#### [Andrew Ashworth (Jun 24 2018 at 05:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542394):
oh

#### [Andrew Ashworth (Jun 24 2018 at 05:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542395):
you pushed something new

#### [Simon Hudon (Jun 24 2018 at 05:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542396):
I think you should refresh. I just updated it

#### [Andrew Ashworth (Jun 24 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542438):
if it's only def, the likely reason is that you have conflicting versions of pygments installed

#### [Andrew Ashworth (Jun 24 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542439):
then when you compile, the html isn't getting styled correctly as a result

#### [Simon Hudon (Jun 24 2018 at 05:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542499):
How do I fix that?

#### [Andrew Ashworth (Jun 24 2018 at 05:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542546):
pip uninstall pygments

#### [Andrew Ashworth (Jun 24 2018 at 05:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542549):
then reinstall from the pygments fork

#### [Simon Hudon (Jun 24 2018 at 05:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542718):
It worked like a charm! Thanks :)

#### [Andrew Ashworth (Jun 24 2018 at 05:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542762):
np

#### [Simon Hudon (Jun 24 2018 at 05:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542763):
Btw: I decided to take the lazy way for publishing and I did `git init` in `build/html` and added `gh-pages` as a remote. It doesn't seem too bad

#### [Andrew Ashworth (Jun 24 2018 at 05:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542771):
yep, i bet that would work too

#### [Andrew Ashworth (Jun 24 2018 at 05:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542811):
that is actually lazier than cut and paste... wish i'd done that first

#### [Simon Hudon (Jun 24 2018 at 05:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542864):
I work pretty hard to be this lazy :stuck_out_tongue_closed_eyes:

#### [Simon Hudon (Jun 24 2018 at 05:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542904):
It should look better now  at https://alashworth.github.io/sf-lean/vol1/basics.html#

#### [Andrew Ashworth (Jun 24 2018 at 05:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542948):
hmm, the try it hyperlink overlaps code

#### [Simon Hudon (Jun 24 2018 at 05:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542954):
Which one?

#### [Andrew Ashworth (Jun 24 2018 at 05:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542956):
all the one liner defs and examples

#### [Andrew Ashworth (Jun 24 2018 at 05:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128542998):
for example, `example : next_weekday (next_weekday day...`

#### [Simon Hudon (Jun 24 2018 at 05:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128543007):
Ah! Do you mean that it displays "try it" on top of the code? I thought somehow snippets got mixed up when sent to Lean Live

#### [Andrew Ashworth (Jun 24 2018 at 05:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128543050):
the way the try it works with snippets is not very suitable to how SF is currently laid out

#### [Andrew Ashworth (Jun 24 2018 at 05:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128543051):
for example, none of the nat playground stuff works because the namespace command isn't sent to lean.js

#### [Andrew Ashworth (Jun 24 2018 at 05:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128543058):
i would like to revert `conf.py` until one of us has time to really sit down and make it work correctly.

#### [Simon Hudon (Jun 24 2018 at 05:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128543059):
The snippets have a lot of problems. I'd like to send the whole file over

#### [Simon Hudon (Jun 24 2018 at 05:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128543060):
Sure. What does your version do?

#### [Andrew Ashworth (Jun 24 2018 at 05:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128543061):
no "try it" at all

#### [Simon Hudon (Jun 24 2018 at 05:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128543100):
I could work on the "try it" in a branch until I get it right

#### [Andrew Ashworth (Jun 24 2018 at 05:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128543101):
to make it work correctly, we need to build lean live with our own lean source files

#### [Andrew Ashworth (Jun 24 2018 at 05:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128543102):
and we also need some way to send a scroll command

#### [Andrew Ashworth (Jun 24 2018 at 05:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128543103):
or embed a line position in the hyperlink

#### [Andrew Ashworth (Jun 24 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128543110):
if we do want to have a web link

#### [Simon Hudon (Jun 24 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128543111):
That would be good, you're right.

#### [Andrew Ashworth (Jun 24 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128543113):
then we should perhaps link the whole source file at the top of the chapter

#### [Andrew Ashworth (Jun 24 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128543114):
and ask people to scroll down as they read

#### [Andrew Ashworth (Jun 24 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128543115):
that's the low-effort way

#### [Simon Hudon (Jun 24 2018 at 05:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128543116):
Maybe we can recruit @**Gabriel Ebner** or @**Sebastian Ullrich** to help us with that

#### [Simon Hudon (Jun 24 2018 at 05:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128543158):
Yeah, and then the link can bring up Lean Live at the right line number

#### [Andrew Ashworth (Jun 24 2018 at 05:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128543204):
yeah, i think for now it would be best to work on it in its own branch

#### [Andrew Ashworth (Jun 24 2018 at 05:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128543252):
TPIL does some trickery with selectively hiding lines

#### [Kevin Buzzard (Jun 24 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128551894):
So this all looks really good -- both nice to look at, and great material. Is it really not an issue that the text is basically all lifted from someone else's work? If not then that's awesome.  My son will be starting on doing the exercises on Monday 2nd July, he is a beginner but he's a decent python programmer and is hopefully smart enough to learn quickly (and I can help him of course). I was going to advise him to just read SF in the original Coq and I was going to help him translate, but if he can read the translated stuff that would be awesome. I have done many of the exercises of Part 1 in Lean myself and I will have the answers somewhere -- I did them once I knew a lot about how Lean worked so they weren't too much trouble.

#### [Simon Hudon (Jun 24 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128557593):
Great! And please send us comments as you go if there are parts that don't quite add up.

```quote
Is it really not an issue that the text is basically all lifted from someone else's work?
```

Not an issue. The html version of the book is under MIT license and I talked to the author. He seems pretty happy that we're doing that and had great information on how to proceed.

#### [Simon Hudon (Jun 24 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128557639):
(comments or even contribution to the text)

#### [Simon Hudon (Jun 24 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128560717):
@**Andrew Ashworth** What was the reason for you to use to specify lean snippets in a single Lean file instead of inline in the `rst` file? I'm thinking it might be easier to write this way, especially considering that the flow of the chapter pretty much follows the declaration flow.

#### [Andrew Ashworth (Jun 24 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561026):
later in the book we will want to use leanpkg to manage dependencies on `cooper` and `mathlib`

#### [Andrew Ashworth (Jun 24 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561033):
the more involved exercises use a lot of `omega`

#### [Simon Hudon (Jun 24 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561079):
I thought we could use a make file to first generate the Lean sources and then call `leanpkg`

#### [Simon Hudon (Jun 24 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561086):
The biggest downside I see is with debugging the Lean code

#### [Andrew Ashworth (Jun 24 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561256):
i think a common way to interact with the textbook will be for people to clone the repository and step through the source files themselves

#### [Andrew Ashworth (Jun 24 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561258):
you can't work with the .rst file like a .lean file

#### [Simon Hudon (Jun 24 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561268):
That's true. I'd really like for there to be a literate mode to Lean

#### [Simon Hudon (Jun 24 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561310):
I think we can offer a similar experience though by building an archive file that people can download. And in that file, we put the Lean generate files and the `rst` files, to follow along.

#### [Andrew Ashworth (Jun 24 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561360):
i can't comment on this approach since I don't know how the TPIL `lean-sphinx` node parsing code works

#### [Simon Hudon (Jun 24 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561373):
I think that's feasible. Remains to see if it's a workflow we're comfortable with

#### [Andrew Ashworth (Jun 24 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561414):
from a gut feeling perspective, it feels backwards to me. If I had unlimited time, I would write a Lean plugin for sphinx so we could move even more comments and documentation into the `.lean` files

#### [Simon Hudon (Jun 24 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561474):
Yeah, I'd love that

#### [Andrew Ashworth (Jun 24 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561475):
from a teaching perspective, I think it's nice if the project demonstrates how to manage a larger Lean development

#### [Simon Hudon (Jun 24 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561478):
I've been asking for a literate mode for a while. Maybe Lean 4 will make it easier to do ...

#### [Andrew Ashworth (Jun 24 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561517):
the inline code approach with snippets is attractive because it enables us to reuse all the scripts from TPIL, and in particular maybe make it easier to enable 'try it'

#### [Andrew Ashworth (Jun 24 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561519):
well, you already know how I feel about how useful that functionality is

#### [Simon Hudon (Jun 24 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561526):
Are you referring to a previous conversation ... I only have vague memories of that. You weren't too favorable to the idea, were you?

#### [Andrew Ashworth (Jun 24 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561528):
well, to recap, I think it's a big hassle for us to make it work correctly

#### [Simon Hudon (Jun 24 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561574):
For us the users?

#### [Andrew Ashworth (Jun 24 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561577):
for us, the authors

#### [Andrew Ashworth (Jun 24 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561579):
and also nobody is going to want to be doing the more involved exercises in lean.js

#### [Andrew Ashworth (Jun 24 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561629):
I think between `elan` and a possible Lean environment being set up on co-calc, its not a good use of time to try and get it to work, when there's so much translation effort to be done

#### [Simon Hudon (Jun 24 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561635):
I think you misunderstood my point about literate programming. The point is to have the html and pdf generated from a Lean file, the prose is considered as comment when compiling so you don't have to maintain two separate sets of files when writing tutorials or blogs or books

#### [Andrew Ashworth (Jun 24 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561645):
if you want something similar to `coqtop`

#### [Andrew Ashworth (Jun 24 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561647):
a Sphinx plugin would do that

#### [Andrew Ashworth (Jun 24 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561649):
it could be written today

#### [Andrew Ashworth (Jun 24 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561693):
but that doesn't help you when you want to discuss things out of the order they are defined in the source

#### [Andrew Ashworth (Jun 24 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128561696):
then i think the way sf-lean is currently structured is the best

#### [Simon Hudon (Jun 24 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128562294):
That's something I've been arguing for as well. If lean provided a declaration like `postpone my_foo your_foo their_foo` then that could allow you to make small breaks in the declaration order.

#### [Jesse Michael Han (Jun 25 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128606397):
it'd be nice also if extracted Lean snippets (a la TPIL) could refer to/import each other---this is something that'll come up sooner or later in the formal abstracts project, since there'll be theorems we want to formally state that require other definitions/theorems that only exist as formal abstract snippets

#### [Simon Hudon (Jun 25 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128606809):
I'm not too familiar with the formal abstracts project. Do you mean that you'd like in Lean Live to import 
chapters of TPIL?

#### [Jesse Michael Han (Jun 25 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128607230):
Currently it's organized as a Sphinx project with Gabriel's lean_sphinx extension: https://github.com/thalesant/formalabstracts

I mean that if there's a page for e.g. the continuum hypothesis, containing a code block, then i'd like to be able to import that code block when i write a new page about the independence of the continuum hypothesis

#### [Simon Hudon (Jun 25 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128607985):
I see so if the whole project was source code would make it easier to use. I agree

#### [Kevin Buzzard (Jul 02 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128953236):
```quote
It should look better now  at https://alashworth.github.io/sf-lean/vol1/basics.html#
```
OK so my son is going to start on the exercises today. Many thanks to both Andrew and Simon for making his life less difficult!

#### [Elliott Macneil (Jul 02 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128955649):
I'm wondering if someone could possibly direct me to where the source code (the file basic.lean) is, as the link on the website doesn't work

#### [Patrick Massot (Jul 02 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128955713):
https://github.com/alashworth/sf-lean/blob/lean-3.4.1/src/basics.lean

#### [Elliott Macneil (Jul 02 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reStructured%20Text%20and%20Lean/near/128955765):
Thanks!

