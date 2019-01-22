---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/90182CoCalc.html
---

## [general](index.html)
### [CoCalc](90182CoCalc.html)

#### [Patrick Massot (May 03 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/126061868):
Someone sent me this link: https://twitter.com/cocalc_com/status/990971941308727296

#### [Johan Commelin (May 03 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/126062193):
William told me he is finishing up his new collaborative editor for CoCalc

#### [Johan Commelin (May 03 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/126062196):
After that, a collaborative IDE for lean is somewhere on his todo list...

#### [Johan Commelin (May 03 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/126062200):
I am really excited about this!

#### [Kevin Buzzard (May 04 2018 at 00:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/126067886):
We're going to use it over the summer. They like stable versions of software by default, and when mathlib 3.4.1 comes out I'm going to ask them to install it too. They didn't seem keen to stay up to date with mathlib HEAD but mathlib current is just fine as far as I am concerned.

#### [Kevin Buzzard (May 04 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/126067921):
It solves the massive headache of getting Lean installed on a random undergraduate's laptop, which can take forever especially if the errors are all in Italian and hence harder to google...

#### [Kevin Buzzard (May 04 2018 at 00:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/126067982):
The big question is how much faster will it be than the lean web editor.

#### [William Stein (May 04 2018 at 00:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/126068881):
I'm here in case anybody has any questions/comments/suggestions/mock ups for a LEAN ide mode that makes sense in cocalc/etc.

#### [Kevin Buzzard (May 04 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/126069095):
Hiya.

#### [Kevin Buzzard (May 04 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/126069142):
William, I've been trying to figure out what a canonical isomorphism is in Lean.

#### [Kevin Buzzard (May 04 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/126069145):
I was supposed to be finishing my schemes work but I got sucked down a real rabbithole

#### [Kevin Buzzard (May 04 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/126069152):
Lean is going to know what an affine scheme is as soon as I pull my finger out.

#### [Kevin Buzzard (May 04 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/126069190):
https://leanprover.github.io/live/latest/

#### [Kevin Buzzard (May 04 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/126069193):
That's what you're up against @**William Stein**

#### [Kevin Buzzard (May 04 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/126069197):
and I'm going to go and do some schemes

#### [Andrew Ashworth (May 04 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/126073614):
I think Lean 4 will allow a bit more flexibility when it comes to making interesting IDE assists, particularly with the parser upgrades and further development of the `{! !}` "hole" functionality

#### [Patrick Massot (Aug 31 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133118447):
Lean in CoCalc seem to make a lot of progress:
https://github.com/sagemathinc/cocalc/search?q=lean&unscoped_q=lean

#### [Kevin Buzzard (Aug 31 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133121112):
I can use Lean in CoCalc :-)

#### [Kevin Buzzard (Aug 31 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133121117):
As of today

#### [Patrick Massot (Aug 31 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133127412):
Do you mean you have access to a private beta-test?

#### [Kevin Buzzard (Aug 31 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133127626):
Yes

#### [Kevin Buzzard (Aug 31 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133127648):
Shall I live stream on twitch?

#### [Johan Commelin (Aug 31 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133127809):
You shall!

#### [Patrick Massot (Aug 31 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133127821):
Yeah!

#### [Gabriel Ebner (Aug 31 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133127907):
I tried lean on cocalc earlier today and it worked out of the box.  There is no autocompletion, no syntax highlighting, and no mathlib, but it shows error messages just like in vscode.

#### [Patrick Massot (Aug 31 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133127951):
Do you mean public CoCalc or do you have special access?

#### [Gabriel Ebner (Aug 31 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133128003):
Public cocalc.  Just create a file with the `.lean` extension and it works.

#### [Patrick Massot (Aug 31 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133128693):
synchronisation is completely random :(

#### [Johan Commelin (Aug 31 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133128738):
I'm on an unpaid account, and the server is overloaded. I can't even create a file.

#### [Johan Commelin (Aug 31 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133128807):
If someone wants to add me to their Lean test project, so that I can multiplayer on their files, I'dd appreciate that.

#### [Patrick Massot (Aug 31 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133129093):
what is the email address associates to your account?

#### [Johan Commelin (Aug 31 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133131698):
`johan@commelin.net` I think

#### [Patrick Massot (Aug 31 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133131774):
You should receive an email

#### [Patrick Massot (Aug 31 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133131804):
But it's hopelessly slow

#### [Johan Commelin (Aug 31 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133131847):
Ok, you are also on an unpaid account?

#### [Patrick Massot (Aug 31 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133131854):
Using Lean on CoCalc without paying doesn't seem possible

#### [Patrick Massot (Aug 31 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133131858):
Yes

#### [Johan Commelin (Aug 31 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133131859):
I should really get my uni to pay for an account.

#### [Johan Commelin (Aug 31 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133131944):
At the moment it is completely unusable in general, I can't even create a terminal or such.

#### [William Stein (Aug 31 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133137692):
Hi -- I created a non-free upgraded project on CoCalc just now.  Here's a link:

#### [William Stein (Aug 31 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133137695):
https://cocalc.com/projects/32a71772-8761-49d1-9134-6eb7f3fca4f5/files/?session=default

#### [William Stein (Aug 31 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133137704):
I added everybody who commented above as collaborators to the project.

#### [Patrick Massot (Aug 31 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133138832):
Thanks!

#### [William Stein (Aug 31 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133139481):
Here's what it looks like:[Screenshot-2018-08-31-at-11.14.49-AM.png](/user_uploads/3121/EiFb5k52ujGB5ObgnM0C2U5t/Screenshot-2018-08-31-at-11.14.49-AM.png)

#### [Patrick Massot (Aug 31 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133139562):
eheh, that's the lemma I just wrote

#### [William Stein (Aug 31 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133139578):
Yep.  By the way, anybody who is a collaborator on that project can add anybody else (in project settings).

#### [Patrick Massot (Aug 31 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133139683):
The message window displays only info and errors, but not the current tactic state, this is similar to one of the Lean message display mode in VScode but I can't find the other one

#### [Gabriel Ebner (Aug 31 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133139817):
@**William Stein** You need to request the goal state separately.  It is not sent as part of the error messages. https://github.com/leanprover/lean-client-js/blob/83f190d044502d1cd39f320ef15da5357547d539/lean-client-js-core/src/commands.ts#L87-L114

#### [William Stein (Aug 31 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133139850):
Gabriel -- thanks.  I didn't realize that.  I'll add that to the todo list.

#### [William Stein (Aug 31 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133140202):
Is there something like prettier or yapf (inspired by Gofmt) for lean code?  We are pushing out "sort of" canonical format support  like that as much as possible all over in cocalc...

#### [Patrick Massot (Aug 31 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133140486):
That's great, I can prove random stuff that we already have

#### [Patrick Massot (Aug 31 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133140503):
Now it's time for dinner, but many thanks!

#### [Kevin Buzzard (Aug 31 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133142574):
Thanks so much for the work you've done on this William!

#### [Johan Commelin (Aug 31 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133145323):
This is awesome! Thank you very much!

#### [Johan Commelin (Aug 31 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133145374):
@**William Stein** The prettier will likely be added in the next version of Lean (Lean 4).

#### [Johan Commelin (Aug 31 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133145388):
See also: https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/VScode.20extension/near/133129165

#### [Scott Morrison (Sep 01 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133157550):
Could someone add me as a collaborator on that project?

#### [Patrick Massot (Sep 01 2018 at 10:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133168777):
I hope I just did that

#### [Patrick Massot (Sep 01 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133168785):
And I'm happy to see that everybody seems to haved managed to travel back from Orsay!

#### [Kevin Buzzard (Sep 01 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133169787):
I wrote a few lines of code in a test document and then sent William some comments (in the project chat) about which points of the workflow were currently harder in CoCalc than in VS Code. It seemed much quicker than the Lean Web Editor -- it was slower than local VS Code of course, but certainly fast enough to be usable (especially by beginners). The main things we're missing are: (1) mathlib (2) view of goal in tactic mode and (3) tab completion. Also syntax highlighting but for me that wasn't really a deal breaker.

#### [William Stein (Sep 05 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133354374):
I just improved the syntax highlighting a bit, so it's maybe usable now (it wasn't before).  I haven't done anything else yet. [Screenshot-2018-09-04-at-9.32.57-PM.png](/user_uploads/3121/h1N1zVVEc2TBatnzHjnRa8Ut/Screenshot-2018-09-04-at-9.32.57-PM.png)

#### [Johan Commelin (Sep 05 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133354456):
Hooray! That's really nice.

#### [Scott Morrison (Sep 05 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133354654):
This looks really promising!

#### [Scott Morrison (Sep 05 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133354701):
Is it right that there isn't a "goal display" mode yet? Or am I just missing it. I know for people who work in term mode all the time it's not critical, but for beginners and mathematicians who use tactic mode all the time it is very helpful.

#### [Johan Commelin (Sep 05 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133354708):
It is on the todo list.

#### [Kevin Buzzard (Sep 05 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133360335):
The big jobs which remain, I guess, are: (1) access to mathlib [e.g. reading `LEAN_PATH` or `leanpkg.path` I guess] (2) displaying goals in tactic mode (3) tab completion (4) hover over function name -> mini window with definition / docstring; I guess that of these, (1) and (2) are the ones which I really need for my teaching (I'd also need an extension of (1), which is "read my library too").

#### [Kevin Buzzard (Sep 06 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133457209):
@**Harald Schilly** I downloaded and I believe compiled mathlib about two days ago on a cocalc project if this helps.

#### [Kevin Buzzard (Sep 06 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133457344):
There's a project called LEAN that I have access to on CoCalc (as do several of us) and in `_target/deps/mathlib` is a only-a-few-days-old mathlib, compiled using CoCalc's servers.

#### [Harald Schilly (Sep 06 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133460233):
yes, I'm in that project. so, the goal I think is to compile a recent version of mathlib globally (currently a path like /ext/lean/.../lean/mathlib)  and make it picked up by default by lean. I don't know that part about picking it up automatically. That's all.

#### [Mario Carneiro (Sep 06 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133460300):
The lean path is specified in `leanpkg.path` in the current project folder

#### [Mario Carneiro (Sep 06 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133460305):
You can put things like `../lean/mathlib` in it

#### [Mario Carneiro (Sep 06 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133460387):
That will bypass `leanpkg` somewhat, though - commands like `leanpkg configure` will clobber the file

#### [Mario Carneiro (Sep 06 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133460429):
To make it stick you could install mathlib in `~/.leanpkg` (I believe this is where `leanpkg install` puts stuff), and then add a dependency to mathlib in the `leanpkg.toml` file

#### [Mario Carneiro (Sep 06 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133460449):
This is the way most users do it, I think

#### [Sebastian Ullrich (Sep 06 2018 at 23:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133469659):
@**Mario Carneiro** packages in `~/.leanpkg` are only used by stand-alone files not contained in packages

#### [Kenny Lau (Sep 11 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133738672):
how does this work?

#### [Kevin Buzzard (Sep 11 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133743695):
What do you mean?

William wrote some code and now you can use Lean at CoCalc, but there are still some things missing (like displaying goal in tactic mode, and autocompletion, last time I looked). My plan is to offer it to the 1st years.

#### [Kenny Lau (Sep 11 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133743897):
well I just went to it and I can't use anything

#### [Kevin Buzzard (Sep 11 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133743948):
can you be more precise? I go to it and I can use Lean

#### [Kenny Lau (Sep 11 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133744258):
apparently only a few people have access

#### [Johan Commelin (Sep 11 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133744526):
@**Kenny Lau** You have to create a `.lean` file. And supposedly if you click on it, the Lean editor should open.

#### [Johan Commelin (Sep 11 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133744531):
But it might not be usable at all on a free account.

#### [Harald Schilly (Sep 11 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133755059):
```quote
This is the way most users do it, I think
```
Hi again. Just to clarify what my goal in this "CoCalc" stream (is this the term?) is: the situation is a course, where many who are now to lean want to follow examples and experiment around. The underlying infrastructure is a linux-based multi-user environment. This means, there is a common read-only directory where we (administrators of the online service) can install lean and everyone accesses it from there. Additionally, it would be good to have mathlib and maybe another library available globally. The goal is to give everyone a good "out of the box" experience, such that these libraries work without much overhead. In Python, there are global "site" directories, but with lean this seems to be different -- or well -- I haven't understood it yet. So, my understanding here is, every student should setup their own lean-specific directory and inside of it is a `leanpkg.path` file. What's exactly the content? Or should it rather be a `leanpkg.toml` file? Sorry, I'm a complete lean novice :rolling_eyes:

#### [Kevin Buzzard (Sep 11 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133755534):
`leanpkg.toml` is for the `leanpkg` package manager. If the package installed correctly initially, it won't need to be managed. `leanpkg.path` is the file which, conventionally (on a single user install) the IDE reads so it knows where the paths are which will be looked in when the IDE runs into a line of the form `import data.equiv.basic` -- it will look through the entries in `leanpkg.path` until it finds a line corresponding to a directory containing `data/equiv/basic.lean`. So neither of them are actually essential for the set-up to work.

#### [Kevin Buzzard (Sep 11 2018 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133755620):
An example of how I use `leanpkg.toml` is that if I have a project which has `mathlib` as a dependency, and if `mathlib` upgrades, I can upgrade my local version of `mathlib` using the `leanpkg upgrade` command. The students will not need to be upgrading any particular packages (and indeed they'd need internet access for this to work).

#### [Kevin Buzzard (Sep 11 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133755661):
I upgrade mathlib because it changes a lot right now (many commits per week) and some of them are new functions or theorems which I need. But my students won't need anything so bleeding-edge.

#### [Chris Hughes (Sep 11 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133756967):
It's not just advanced mathematics that's getting PRed, some of it is things like `int.cast_pow`, which I think they might need. Over the summer I added quite a few trivial little lemmas like this when people needed them.

#### [Kevin Buzzard (Sep 11 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133757499):
yes but one of the points of the summer project was to make sure we'd have everything we need in mathlib by October. What's the situation with `cos`  by the way? ;-)

#### [Johan Commelin (Sep 12 2018 at 05:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133774696):
@**Harald Schilly** You seem to be in a European timezone. Is that right? Where exactly are you based? Because it might be feasible to meet up with one of the people who really know how this stuff works...

#### [William Stein (Sep 12 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133838237):
@**Harald Schilly** is in Vienna, Austria.

#### [William Stein (Sep 12 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133838250):
[Screenshot-2018-09-12-at-12.20.10-PM.png](/user_uploads/3121/FI84qpkbGYr20ZS3gkj0iap-/Screenshot-2018-09-12-at-12.20.10-PM.png)

#### [William Stein (Sep 12 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133838282):
I implemented "tab completion".  You have to actually press the tab key to get completions.  It first shows once that can be determined in the browser (so standard keywords, functions, etc.,), then it shows the results that come back from the lean server.

#### [Mario Carneiro (Sep 12 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133838342):
Can the keywords show with a different icon or color than the constants?

#### [William Stein (Sep 12 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133838347):
@**Kenny Lau** I invited you to [the lean cocalc project](https://cocalc.com/projects/32a71772-8761-49d1-9134-6eb7f3fca4f5/files/?session=default), in case you want to try it.

#### [Kenny Lau (Sep 12 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133838357):
lol how do you know who I am

#### [Mario Carneiro (Sep 12 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133838360):
also, hopefully once results come back from lean you can put the types of the constants in that list as well, that's pretty important

#### [William Stein (Sep 12 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133838380):
@**Mario Carneiro** I'll add that to the todo list, along with showing type information, for later.   I'm only going to do stuff now that is absolutely critical for Kevin's course.   I think some sort of lean path configuration should be next on my list.

#### [Patrick Massot (Sep 12 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133838386):
Kenny you complained in this thread you didn't have access

#### [Mario Carneiro (Sep 12 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133838391):
that's fine, I just wanted you to know what would be helpful

#### [Harald Schilly (Sep 12 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133838393):
```quote
@**Harald Schilly** You seem to be in a European timezone.
```

yes, vienna as william said. do you know if there is someone active with lean at the university of vienna? that could be quite interesting.

#### [William Stein (Sep 12 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133838435):
@**Mario Carneiro** I just added you to the project too.

#### [Kenny Lau (Sep 12 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133838444):
```quote
Kenny you complained in this thread you didn't have access
```
yes I did, but I didn't say what my account is

#### [Kenny Lau (Sep 12 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133838450):
somehow WS managed to find my account

#### [William Stein (Sep 12 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133838457):
@**Mario Carneiro**  -- yes, I've been comparing with VS code...

#### [Patrick Massot (Sep 12 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133838467):
Isn't @**Gabriel Ebner** in Vienna?

#### [William Stein (Sep 12 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133838469):
@**Kenny Lau** -- I just typed your name into the collaborator search and it was the only result.

#### [Harald Schilly (Sep 12 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133838494):
@**Patrick Massot** sounds like a name that could be from over here!

#### [Kenny Lau (Sep 12 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133838497):
fair enough

#### [Patrick Massot (Sep 12 2018 at 21:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133838502):
https://gebner.org/

#### [Harald Schilly (Sep 12 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133838565):
nice

#### [Patrick Massot (Sep 12 2018 at 21:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133838572):
I think he is currently on vacations

#### [Patrick Massot (Sep 12 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133838653):
And, very conveniently, he is the maintainer of the VScode Lean extension

#### [William Stein (Sep 12 2018 at 21:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133838666):
I'm going to work on displaying "the current tactic state" next.

#### [William Stein (Sep 12 2018 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133838751):
Kevin, for your course, as long as I make it possible to easily set LEAN_PATH, or even just make it set to some default (e.g., /home/user/lean), then you could just rsync out /home/user/lean to all student projects.  You would just update it in your project whenever you want, test it, then click a button to push it out to students whenever you want.

#### [William Stein (Sep 12 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133838758):
I'll set LEAN_PATH to ~/lean right now, since it's a fairly easy change to make, anyways.

#### [William Stein (Sep 12 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133839081):
Or is that not nearly enough, because it'll have to be customizable with lots of colons to detect many directories?

#### [Kevin Buzzard (Sep 12 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133839165):
I guess we either need several directories, or we do the horrible thing of putting them all in the same directory giving a huge mess of core lean and mathlib and my stuff all mixed together

#### [Sebastian Ullrich (Sep 12 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133839235):
Yes, it is expected that there is a separate entry for each package in LEAN_PATH. I suppose for Kevin's students it should be sufficient to include `.`, the global mathlib path, and Lean's `library` folder in there

#### [Sebastian Ullrich (Sep 12 2018 at 21:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133839340):
Note that this effectively disables `leanpkg` (i.e. importing custom dependencies, as well as importing files relative to the package root)

#### [William Stein (Sep 12 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133839380):
I could have it just read ~/leanpkg.path if it exists.  My only worry is that students would mess it up; also there is no easy way to push out a top level file to students right now...

#### [William Stein (Sep 12 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133839487):
OK, for now how about:  `LEAN_PATH=.:/ext/lean/mathlib:[whatever lean's library folder is??]`

#### [William Stein (Sep 12 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133839492):
But what is lean's library folder?

#### [William Stein (Sep 12 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133839496):
How do I determine that?

#### [Mario Carneiro (Sep 12 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133839586):
it is `lean/library`

#### [William Stein (Sep 12 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133839675):
It's OK that `lean/library` is not an absolute path?

#### [William Stein (Sep 12 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133839716):
Also, what is a very simple "hello word" style test of LEAN_PATH?

#### [William Stein (Sep 12 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133839767):
Here's what I'm currently doing:

#### [William Stein (Sep 12 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133839768):
```

#### [William Stein (Sep 12 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133839771):
```
    process.env.LEAN_PATH = `${process.env.HOME}:${process.env.HOME}/lean:/ext/lean/mathlib:lean/library`;
    this._server = new lean_client.Server(
      new lean_client.ProcessTransport("lean", ".", [])
    );
```

#### [Chris Hughes (Sep 12 2018 at 21:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133839842):
`import data.finset` is probably a reasonable test.

#### [William Stein (Sep 12 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133839878):
With the above LEAN_PATH, I get this error from `#print "hello"`:
```
file 'init' not found in the LEAN_PATH
```

#### [Sebastian Ullrich (Sep 12 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133839941):
`lean/library` should be an absolute path; no magic there

#### [Sebastian Ullrich (Sep 12 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133839978):
I.e. append `/library` to where you store Lean

#### [William Stein (Sep 12 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133840023):
I don't know where we store lean.  Also, it can very based on if the user is using cocalc.com or cocalc-docker.

#### [Sebastian Ullrich (Sep 12 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133840110):
I see. You can ask Lean: `lean --path`

#### [William Stein (Sep 12 2018 at 22:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133840241):
ok, that works perfectly.

#### [William Stein (Sep 12 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133841207):
What does this mean exactly - this is just the default already with me changing nothing?
```
~/cocalc/src$ lean --path
{
  "is_user_leanpkg_path": true,
  "leanpkg_path_file": "/home/user/.lean/leanpkg.path",
  "path": [
    "/ext/lean/lean-3.4.1-linux/bin/../library",
    "/ext/lean/lean-3.4.1-linux/bin/../lib/lean/library",
    "/home/user/.lean/_target/deps/mathlib/.",
    "/home/user/.lean/./."
  ]
}
```

#### [William Stein (Sep 12 2018 at 22:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133841864):
E.g., does it mean users can already customize their path by editing the file `/home/user/.lean/leanpkg.path`, so that's already done?

#### [Kevin Buzzard (Sep 12 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133841903):
I think they're not supposed to touch that file, which is auto-generated by the package manager

#### [Kevin Buzzard (Sep 12 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133841916):
The package manager looks at leanpkg.toml and sees the dependencies of the project.

#### [Kevin Buzzard (Sep 12 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133841974):
It looks to me like mathlib is a dependency for that project because dependency projects are downloaded to _target/deps

#### [William Stein (Sep 12 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133841992):
How can I try importing something from mathlib to see what happens?

#### [Kevin Buzzard (Sep 12 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133842068):
Make a file blah.lean with the line `import data int.basic` and then compile it

#### [Kevin Buzzard (Sep 12 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133842071):
If that mathlib directory actually exists and has a mathlib in then it might work

#### [Kevin Buzzard (Sep 12 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133842090):
I'm afraid I'm afk right now though

#### [Patrick Massot (Sep 12 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133842510):
He means `import data.int.basic` he missed a point

#### [William Stein (Sep 12 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133842638):
Cool -- it looks like it just works once somebody has installed mathlib already in the standard way **and** restarted the project in project settings.  Cool.

#### [Sebastian Ullrich (Sep 12 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133844576):
I thought the goal was to not have mathlib installed in the standard (user-specific) way but precompiled in a global path?

#### [William Stein (Sep 12 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133844855):
@**Sebastian Ullrich**  -- maybe. I'm still confused.    It just happens to be the case that mathlib is installed for the user for this [test project](https://cocalc.com/projects/32a71772-8761-49d1-9134-6eb7f3fca4f5/files/blah.lean?session=default), and it's important to also support that case too,  I guess.   For example, Kevin's class could just push out a custom ~/.lean to the students and it might just work... then he can update it every day if he wants.

#### [Sebastian Ullrich (Sep 12 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133845269):
Yes, if Kevin can just push his ~/.lean with prebuilt mathlib to all students, it should just work for them. At least as long as they use stand-alone .lean files; if they create their own Lean packages, the ~/.lean packages will not be visible anymore until they add them back as dependencies to the new package

#### [William Stein (Sep 12 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133847058):
Oh my gosh this path stuff is driving me crazy.   I'm deleting all the code I've written related to it and just going to ensure lean starts in $HOME.

#### [William Stein (Sep 12 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133847112):
Look -- if all users on a system are supposed to have access to an extra package, namely mathlib, which is installed systemwide, what is the admin supposed to do in order to install that package?

The answer in python is to become root, set umask properly, then do `pip install packagename`.  What is the answer for LEAN?

#### [Sebastian Ullrich (Sep 13 2018 at 00:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133847341):
You have to include that directory in either LEAN_PATH or `~/.lean/leanpkg.path` (or tell users to create a new package and add it as a dependency there). leanpkg is directly inspired by Rust's package manager, which like all modern package managers is focused on reproducible build environments and does not really have a notation of global packages.

#### [William Stein (Sep 13 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133847750):
> does not really have a notation of global packages.

OK, thanks for the clarification. I'll take as an axiom then that "lean does not have global packages", and  won't do anything further for now in that direction.  I'll let Kevin have his students  install mathlib themselves into their projects, or have him push out an install to all student projects.   I'm moving on to showing tactic state.

#### [Gabriel Ebner (Sep 13 2018 at 01:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133852532):
@**Harald Schilly** My office is at the Freihaus of the TU Wien.  Feel free to stop by (but make sure I'm there first).  I'll be back from vacation in the second week of October.

#### [William Stein (Sep 13 2018 at 06:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133861348):
LEAN in CoCalc now has a new "Info at Cursor" panel, which shows the tactic at the cursor, and also other info about what's at the cursor.

[Screenshot-2018-09-12-at-8.31.00-PM.png](/user_uploads/3121/s8c1bvzhPXioauanpdLs72Hn/Screenshot-2018-09-12-at-8.31.00-PM.png)

#### [William Stein (Sep 13 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133861481):
I also made numerous small changes so the UI does not get slowed down by trying to render too much.     I might have introduced too much "debouncing" here though.

So, Kevin, I think this is the *absolute bare minimum* of functionality needed for your course.   You'll have to build all the library stuff, then push it out to the student projects, since LEAN has no notion of global packages, as discussed above.   I think if you install packages, etc., etc., then restart a project in cocalc (project settings --> restart project), then LEAN will run as if it is being run from $HOME, so it'll pick up those packages.

The other problem is that sometimes one has to close and open a file if it isn't syncing.  This is on my immediate todo list.

#### [Mario Carneiro (Sep 13 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133861794):
I think there is a bug in the printing of the tactic info - it says `expr` when it should say `exact expr`

#### [Harald Schilly (Sep 13 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133882189):
```quote
It's OK that `lean/library` is not an absolute path?
```
my understanding is that this is in the lib subdirectory, i.e. `/ext/lean/lean/lib/lean/library/`

ok ... but I see this is already somewhat resolved. looks like it is possible to have mathlib globally, but there is no common way to make it available by default. it's sort of opt-in...

#### [Kenny Lau (Sep 13 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133893040):
@**Reid Barton** maybe you can use cocalc now instead of twitch

#### [Kenny Lau (Sep 13 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133893046):
maybe we should all join a discord group

#### [Kenny Lau (Sep 13 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133893048):
is that a good idea?

#### [Kevin Buzzard (Sep 13 2018 at 17:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133893121):
So for those who haven't experimented recently, I've just been playing with a lean file at CoCalc with Kenny -- true multiplayer Lean! There are now two windows you can have for messages corresponding to the two VS Code windows -- one which reports all output and one which prints the goal when you're in a tactic proof. Underscores work! Tactic proofs are now fine.

#### [Kevin Buzzard (Sep 13 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133895129):
The most obvious thing for me, when writing code, that is better in VS Code than in CoCalc, is that VS Code does cleverer auto-completion -- it chooses more wisely, and for the highlighted choice it displays the type of the term and also the docstring if any. Here are some examples:

#### [Kevin Buzzard (Sep 13 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133895220):
[vscode.png](/user_uploads/3121/KwP_QDrxpJqETmifK98cNIxP/vscode.png) 

[cocalc1.png](/user_uploads/3121/6ms9XafbzF_HTqZ6OzF2atqO/cocalc1.png) 

[cocalc2.png](/user_uploads/3121/vWkjNwoZSPSm9rk4vcc2wpDw/cocalc2.png)

#### [Kevin Buzzard (Sep 13 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133895502):
For VS Code we see filter.map + type + docstring. For cocalc the guessing is less good (VS Code correctly guesses I want `filter.ma<something>`) and I don't see the types of the possibilities, which is really important for when you're using functions which are unfamiliar to you.

But this is a very mild thing. In the last week there has been huge progress!

#### [Patrick Massot (Sep 13 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133895512):
Yes, the progress looks impressive

#### [William Stein (Sep 13 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133896096):
> But this is a very mild thing. 

CoCalc has the exact same completion info available, but all I did with it was sort in alphabetical order and display the names.   I don't know what order I should sort in (or should I just NOT sort and leave things in whatever order the LEAN server outputs)?  Displaying the type, etc., info is probably easy now that the hard part is done (which is getting completions to display at all).  The CodeMirror show-hint plugin API is very rich regarding showing more than just a string in a completions box.  It sounds like you're pretty happy with what vscode shows, so I should just look in the code to see what it does with what comes back from the LEAN server. @**Gabriel Ebner** ?

#### [William Stein (Sep 13 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133896123):
> I think there is a bug in the printing of the tactic info - it says expr when it should say exact expr

That's weird since I'm just printing what the lean server returns with no processing.

#### [Mario Carneiro (Sep 13 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133896147):
Do you know what word you are completing when you ask for completions?

#### [Mario Carneiro (Sep 13 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133896225):
I think VSCode prioritizes maximum subsequences, and initial segments relative to the query

#### [William Stein (Sep 13 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133896293):
@**Mario Carneiro** yes, you know precisely what the "CodeMirror token" is, where the cursor is, etc.
Can somebody point me at the relevant code in the vscode mode? -- maybe I can just copy it over and use it with minimal change.

#### [Mario Carneiro (Sep 13 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133896307):
I think this is default vscode behavior

#### [William Stein (Sep 13 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133896382):
OK, so I guess the same question, but for vscode's source code... of course, I can try to hunt it down.

#### [Reid Barton (Sep 13 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133896405):
Could someone (@**William Stein**?) add me to the Lean test project? Same email address on CoCalc as here

#### [William Stein (Sep 13 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133896465):
@**Reid Barton**  -- done.

#### [William Stein (Sep 13 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133896473):
And as always, anybody on the project can add anybody else by clicking "Settings" in the project, then typing a name or email address at "Add New Collaborators".

#### [William Stein (Sep 13 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133896658):
@**Reid Barton** once in, click on [Log](https://cocalc.com/projects/32a71772-8761-49d1-9134-6eb7f3fca4f5/log?session=default) to see which files people opened when.

#### [William Stein (Sep 13 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133896855):
@**Kevin Buzzard** I'll work on adding the extra type, etc., info to completions right now -- it seems like it's really useful for people (remember, I'm still sort of clueless about LEAN itself!)

#### [Kevin Buzzard (Sep 13 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133897228):
Yes -- sorry. Here's how it works. As I'm sure you're aware, in "raw" mode, Lean wants to know proofs of every single little thing you do, so e.g. if you have `a=b+c` and you want to deduce `c=a-b` (and you are not intending on using Lean's automation to try and prove this automatically) then you are going to have to find the name of this theorem, or a related theorem which will get you half way there or whatever. Now there's an elaborate naming convention, so you tend to start guessing that this lemma is called something like "sub_of_add...something" or "sub_iff_add..." or maybe if these things are integers you might try "int.add_of_..." and you start playing around with auto-completion, trying to find the exact lemma you want. And in fact the moment I type `sub_of` Lean starts suggesting possible lemmas (here the type will be the statement of the lemma) and you can use up and down arrow to look through them to find the exact one you want (or one which is near enough, e.g. you have to turn `a=b` into `b=a` and you remember that this is called `eq.symm` etc).

[vscode2.png](/user_uploads/3121/5jRPURugU8S6xjngKWWz1GJ1/vscode2.png) 

There's a screenshot of this in action.

#### [Patrick Massot (Sep 13 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133897300):
Oh oh, I made a mistake. I close the CoCalc subwindow showing all messages. Now I have no idea how to reopen it.

#### [Kevin Buzzard (Sep 13 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133897314):
game over

#### [Kevin Buzzard (Sep 13 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133897336):
You can make more windows with the [|] and [-] boxes

#### [William Stein (Sep 13 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133897376):
Patrick -- options:  (1) just close *all* the frames and it goes back to the default, or (2) split any frame, then select the new frame (or old) and change it from what it is to what you want.

#### [Kevin Buzzard (Sep 13 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133897377):
and then change what they display with a drop down menu just by it

#### [William Stein (Sep 13 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133897383):
And (3), suggest a new button for me to add to make creating frames clearer!

#### [William Stein (Sep 13 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133897407):
Yep, @**Kevin Buzzard** just did (2).  (1) is also useful -- there is a default layout, and you get that by click the x in the upper right until there are no windows.

#### [William Stein (Sep 13 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133897435):
Note that your frame layout is stored in localStorage on your browser; it's not sync'd across users or other browsers.

#### [Patrick Massot (Sep 13 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133897449):
Thanks, I managed to get back my frames

#### [Patrick Massot (Sep 13 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133897533):
I think I may have revealed that I never used CoCalc before... But I swear I use standalone Sage!

#### [Kevin Buzzard (Sep 13 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133897534):
so the screenshot is displaying a bunch of random terms which have been defined, and the algorithm appears to be that the characters in `sub_of` appear, in that order, in the name of the term.

#### [Patrick Massot (Sep 13 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133897623):
This Lean in CoCalc is *amazing*

#### [Reid Barton (Sep 13 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133897664):
In emacs, each item in that completion list includes the type (in the format `name : type`), so all the types are visible at once

#### [Patrick Massot (Sep 13 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133897723):
Now I need to find how to get my university to pay enough money so that my 40 students that will be using Lean during spring can use that instead of trying to install Lean at home

#### [Reid Barton (Sep 13 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133897750):
If I were to clone another lean package in a subdirectory and `leanpkg build` it and then edit its files, would the editor pick up the correct lean path? I know for now the priority has been getting things set up properly for Kevin's students but I wonder whether it is also ready for more general use.

#### [Patrick Massot (Sep 13 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133897778):
What is the meaning of the number in the title of CoCalc webpage? My tab in Firefox displays "(5) LEAN - CoCalc"

#### [William Stein (Sep 13 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133897841):
Patrick: thanks!   The number is files with unseen chats.  It should also be the number on the bell in the upper right.   It's basically like the number here in zulip, but just the number of "threads" .

Reid: thanks -- I will definitely add that -- the info is also sent to the frontend.

#### [Reid Barton (Sep 13 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133897852):
I guess I will just try it unless you tell me it's a bad idea/definitely won't work

#### [Kevin Buzzard (Sep 13 2018 at 18:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133897881):
Reid can you send a screenshot of how it looks in emacs? I would be interested in comparing IDEs for Lean. I know you and Sebastian use emacs, and I was going to start when I was under the impression that it was going to be the only way I could possibly use Lean with cocalc, but when William decided to write his own interface for Lean I stopped again. I am really used to VS Code even though I've used emacs for 25 years and part of me would love to be doing Lean in emacs (it still annoys me that I can't do (or maybe just don't know how to) fancy editing in VS Code like "cut from here to the end of the line and then paste it half way into the line above", things which I can do easily in emacs).

#### [William Stein (Sep 13 2018 at 18:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133897898):
Patrix: about $600.  We also have a (now popular at some places) option where students just directly pay us a 1-time $14 fee.

#### [Kevin Buzzard (Sep 13 2018 at 18:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133897971):
```quote
Now I need to find how to get my university to pay enough money so that my 40 students that will be using Lean during spring can use that instead of trying to install Lean at home
```
Patrick, my experience is that anything which looks remotely like it is an innovative new teaching method is something which my university is prepared to throw three-digit sums at no problem (indeed they threw a 5-digit sum at me). Hopefully it will work the same at your end.

#### [William Stein (Sep 13 2018 at 18:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133898106):
```quote
If I were to clone another lean package in a subdirectory and `leanpkg build` it and then edit its files, would the editor pick up the correct lean path? [...] I wonder whether it is also ready for more general use.
```

At present I do absolutely nothing to touch any paths and LEAN_PATH is not set.  There is a lean server process and yesterday I made sure it gets started in $HOME, so ~/.lean gets picked up and can impact the lean search path.   

If you just kill the lean server (with kill in a terminal), then things are currently in a broken state, and your only recourse is to restart the project (which takes 5-20 seconds), by clicking "Restart Project" in project settings.  I'll add automatically starting the lean server if it is killed to my todo list.

#### [Reid Barton (Sep 13 2018 at 18:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133898218):
[out.png](/user_uploads/3121/oTRZW2GYKSq1GRqEz7ak-1s4/out.png) is an autocompletion menu

#### [William Stein (Sep 13 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133898289):
```quote
I guess I will just try it unless you tell me it's a bad idea/definitely won't work
```
I have no idea -- just go for it, possibly restart the project, and report back.  If you want to make another new project to play with, send me a link and I'll upgrade it with network access.

#### [Reid Barton (Sep 13 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133898354):
@**Kevin Buzzard** if you want a more representative sample then you could seek randomly through https://www.twitch.tv/videos/308713302 (there might be some dead time at the start while I get things all set up)

#### [Reid Barton (Sep 13 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133899918):
I started a build of `lean-category-theory` but from your description I expect that while the build will succeed, if I try opening a file in `lean-category-theory`, it will use the same global lean server process which won't know about the `lean-category-theory` source paths or its dependencies.
I looked into how the emacs mode knows how to invoke the lean server.
It maintains a list of running [lean server sessions](https://github.com/leanprover/lean-mode/blob/master/lean-server.el#L29) each of which is associated to a `leanpkg.path` file.
For each buffer, it [runs `lean -p`](https://github.com/leanprover/lean-mode/blob/master/lean-leanpkg.el#L74) (with working directory the directory containing the buffer's file, I guess) and extracts the `"leanpkg_path_file"` field from the JSON output. (It also offers to run `leanpkg configure` if appropriate, which is nice but hardly critical.)
Then if it doesn't already have a session with the correct `leanpkg.path` file, it [starts a new server](https://github.com/leanprover/lean-mode/blob/master/lean-server.el#L107).
All of this happens from https://github.com/leanprover/lean-mode/blob/master/lean-server.el#L360

#### [Reid Barton (Sep 13 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133900003):
@**William Stein** :up: in case you want to support multiple Lean projects per CoCalc project.

#### [William Stein (Sep 13 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133905940):
Thanks -- I've copied this to another todo item at [lean.tasks](https://cocalc.com/projects/32a71772-8761-49d1-9134-6eb7f3fca4f5/files/lean.tasks)

#### [William Stein (Sep 13 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133915281):
I redid tab completion so now:
  - there's an indicator about whether the completion is from the lean kernel or the frontend syntax mode
  - the syntax ones come first, then the lean kernel ones
  - I do NOT sort the lean kernel ones at all - the order is precisely what lean produces.
  - the type information is now displayed to the right.

[Screenshot-2018-09-13-at-2.40.01-PM.png](/user_uploads/3121/JCwPJgcKDeh6aC-pt0p1N3v3/Screenshot-2018-09-13-at-2.40.01-PM.png)

#### [Johan Commelin (Sep 14 2018 at 08:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133935411):
This is so cool! Once again, thanks for the effort you're putting into this.

#### [Johan Commelin (Sep 14 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133951562):
@**William Stein** Here another small feature request: when there are multiple goals, I think they are separated by a blank line. Could you separate them with something like an `<hr/>`?

#### [Johan Commelin (Sep 14 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133952289):
Hmmm, I just realised this isn't even done in VScode. However VScode highlights the turnstile (`|-`) symbols. Apparently my eyes thought that was really helpful :smiley:

#### [Patrick Massot (Sep 14 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133952745):
Oh yes, colorized tactic state and messages is great, and very easy to port from the vscode extension. Have a look at https://github.com/leanprover/vscode-lean/blob/master/src/infoview.ts#L326 Note especially how it calls https://github.com/leanprover/vscode-lean/blob/master/src/infoview.ts#L355 which is very naive yet very useful

#### [William Stein (Sep 14 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133963043):
Yes, @**Patrick Massot**,  I've added colorized tactic state to the todo list.

#### [Johan Commelin (Sep 14 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133963697):
I just had a multiplayer Lean/CoCalc session with @**Reid Barton**. Voice chat enabled. Really cool. We made quite some progress on the `tfae` tactic!

#### [Kevin Buzzard (Sep 14 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133963726):
There's multiplayer voice chat??

#### [Johan Commelin (Sep 14 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133963806):
There is a little :video_recorder: icon in the top-right.

#### [Kevin Buzzard (Sep 14 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133963811):
I thought cocalc was basically for profs to distribute homework for students to do in sage. Looks like it has moved on a lot since I last looked seriously...

#### [William Stein (Sep 14 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133964064):
@**Johan Commelin** -- AWESOME!   @**Kevin Buzzard** it's a bit more than just "sagemath cloud" now.    The video chat is hosted by appear.in -- it basically creates an ephemeral video chat room associated to any file (with the room name a big hash of the project_id and filename and a shared secret).

#### [William Stein (Sep 14 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133964186):
Does tfae mean "**t**he **f**ollowing **a**re **e**quivalent"

#### [Johan Commelin (Sep 14 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133964261):
Yes it does.

#### [Johan Commelin (Sep 14 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133964271):
The idea is that you feed it a list of propositions, and then a graph of implications.

#### [Johan Commelin (Sep 14 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133964339):
What you get out of this is a function that you feed to natural numbers, and it will spit out the equivalence between those two propositions.

#### [Johan Commelin (Sep 14 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133964379):
@**William Stein** I did get some banner on top of the appear.in chatroom, saying that the free chatrooms would no longer be available after the 24th of this month.

#### [William Stein (Sep 14 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133964463):
@**Johan Commelin**  -- crap, that's really unfortunate.  We will have to remove this functionality, or try to find another provider (e.g., google?) that still makes random video chat available.   Their pricing last I checked for non free was ridiculously high, much higher than we charge for cocalc, so paying them wasn't an option.

#### [Johan Commelin (Sep 14 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133964536):
Yeah, I'm sorry. But I thought you'dd like to know this before it suddenly happened.

#### [William Stein (Sep 14 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133964565):
OK, I've made an issue for this: https://github.com/sagemathinc/cocalc/issues/3185

#### [Johan Commelin (Sep 14 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133964742):
Hmm, maybe it wasn't that bad: https://blog.appear.in/2018-product-updates/claiming

#### [Johan Commelin (Sep 14 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133964752):
@**William Stein** I didn't check it carefully, only made a mental note to tell you that there was some warning.

#### [Johan Commelin (Sep 14 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133964804):
So it's not actually about free vs money, but somehow the room needs to have an owner.

#### [Harald Schilly (Sep 14 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133964977):
```quote
So it's not actually about free vs money, but somehow the room needs to have an owner.
```
I think it's about "registered user" (even with a pseudonym) vs. completely anonymous. The dialog to claim a room clearly states that it is free.

#### [Johan Commelin (Sep 14 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133965008):
Right... sorry for the confusion.

#### [Harald Schilly (Sep 14 2018 at 18:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133965066):
no problem, this is still something introducing friction and good to be aware of that

#### [William Stein (Sep 14 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/133966504):
Another change I didn't mention: if you kill the lean server process in a terminal, it will now automatically start again.  This could be relevant for packages (I don't know), and certainly means things should be a little more robust.

#### [Johan Commelin (Sep 15 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/134016050):
Here is a way to grind CoCalc to a halt: choose your favorite 1000-line file (e.g. `data/polynomial.lean`) from mathlib and upload it to CoCalc. Once you open it in the Lean IDE the website turns into a unit test for the halting problem.

#### [William Stein (Sep 15 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/134017503):
Do you have any idea why?  Is it the browser frontend that gets slow or the lean server running on the backend?

#### [William Stein (Sep 15 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/134017551):
Oh booth are at 100% -- it might just be the overhead of rendering all the gutter markers to show progress.

#### [William Stein (Sep 15 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/134017619):
Incidentally if you see this and try to refresh the page and have the file opened again... change ?session=default to ?session=default2 and load cocalc to get a new session.   For what it is worth, I opened data/polynomial.lean and the lean server ran at 100% for a while and my browser frontend was slow... but after about 30s everything was fine with lots of errors on the side (as expected due to missing imports).  So this doesn't seem to be a "halting problem" sort of problem?  (At least if you meant "infinite loop" or something like that.) [Screenshot-2018-09-15-at-9.04.46-AM.png](/user_uploads/3121/iVZ1lsURintt0rSk1CslGELm/Screenshot-2018-09-15-at-9.04.46-AM.png)

#### [William Stein (Sep 15 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/134017622):
In any case, right now my goal is that this is just good enough for @**Kevin Buzzard** 's class...

#### [William Stein (Sep 15 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/134017663):
In any case, I think the root cause is inefficiency in constructing the hover tips on the left; I'll make a note to optimize that!

#### [Kevin Buzzard (Sep 15 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/134017664):
I should work on this more -- I would like to get "example sheet 0" up and running.

#### [Kevin Buzzard (Sep 15 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/134017713):
William -- I have say 20 .lean files each of which is very short, and is just the statement of a theorem in Lean.

#### [William Stein (Sep 15 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/134017718):
Yep - if your class examples/homework are way too slow, I want to know about it!

#### [Kevin Buzzard (Sep 15 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/134017722):
The students' job is to take each of these files and to add a proof of the theorem to it

#### [Kevin Buzzard (Sep 15 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/134017723):
How do I go about getting that system into CoCalc?

#### [Kevin Buzzard (Sep 15 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/134017725):
I am making a database of problems.

#### [Kevin Buzzard (Sep 15 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/134017781):
It's currently quite simple -- each entry is an identification number (say 0008), a lean file Q0008.lean with the theorem, a lean file S0008.lean with the proof, and TeX files of the theorem and the proof in maths, plus an additional "more information" file containing comments such as how difficult the question is to do in maths and in Lean

#### [William Stein (Sep 15 2018 at 18:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/134017792):
1. Some ways to get the files into cocalc:
   - make a tarball or whatever, and drag and drop them to the files listing
   - click the "Upload" button in the upper right in the files listing
   - click +New, then click on the big Upload box near the bottom
   - setup [ssh access to your project in Project Settings](http://blog.sagemath.com/cocalc/2017/09/08/using-ssh-with-cocalc.html), then use scp or rsync.
   - put the .lean files on github, then git clone them into cocalc.
2. Make sure to look at https://tutorial.cocalc.com/ in case you want to use any of our course management functionality to simplify distribution to/from students.

#### [Kevin Buzzard (Sep 15 2018 at 18:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/134017836):
Some of the maths questions are not appropriate for Lean, for various technical reasons which I won't bore you with. Of those questions, the vast majority are well suited for Sage -- perhaps because the question is actually just a computation. For those database entries I could maybe add a sage file.

#### [Kevin Buzzard (Sep 15 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/134017886):
Ideally I'd like to set homework to the students of the form "For homework, do the following questions in the database : 0027, 0038, 0039, 0040."

#### [Kevin Buzzard (Sep 15 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/134017890):
I think it would be a much better way of managing my course in general.

#### [William Stein (Sep 15 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/134017898):
For sage code your options include:
  - a .sage file; we do fully supported editing .sage files and running sage (in a terminal, say) in cocalc.
  - a .sagews file -- that's a "sage worksheet", which is much like the old "sage notebooks".
  - a Jupyter notebook -- i.e., a .ipynb file with a specific choice of Sage kernel.  These are extremely popular also outside of math these days and are well supported both in CoCalc and in many other places.

#### [Kevin Buzzard (Sep 15 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/134017906):
Oh crazy. What are my options for Lean?

#### [Kevin Buzzard (Sep 15 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/134017956):
I have heard lots of talk about Jupyter notebooks but because I'm so used to the command line and emacs I've always steered clear of notebooks. I could never quite work out what they had to offer me.

#### [William Stein (Sep 15 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/134017960):
For lean, right now it is only -- "make a .lean file".

I can definitely see how it would make sense to have something like a LEAN Jupyter notebook, where each notebook cell is pretty much exactly like a .lean file is now in cocalc...  But I have no implemented that (yet).

#### [Kevin Buzzard (Sep 15 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/134017961):
But they might be super-powerful these days.

#### [William Stein (Sep 15 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/134018032):
They're not really so much super powerful.  I would describe them more as *very beginner friendly... in  certain ways (and less in others)*.     In CoCalc they are especially nice because of the TimeTravel button, which means you can see all past states of the notebook.

#### [William Stein (Sep 15 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/134018100):
They are like a command line repl, but you can go back and change something from before, and confuse yourself even more :-).  But overall, if you're careful, it is really useful for certain types of tasks.  For example, my Ph.D. student and I were  computeing J_0(42)(QQ)_tor exactly in this Jupyter notebook recently: [Screenshot-2018-09-15-at-9.19.13-AM.png](/user_uploads/3121/i4p6VmtEBDEYYGbQE2YQMBbo/Screenshot-2018-09-15-at-9.19.13-AM.png)

#### [William Stein (Sep 15 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/134018109):
It's like a command line terminal session, but where you can clean it up and keep it around, and easily run it again.
[tutorial](https://goldengrape.github.io/Python-for-ophthalmologist/lesson_01_jupyter.html)

#### [Jeremy Avigad (Sep 16 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/134032755):
@**William Stein** could you add me as a collaborator? I'll be teaching a (probably small) Lean-based course at Carnegie Mellon next semester, and it would be great to do it with CoCalc.

#### [Scott Morrison (Sep 16 2018 at 03:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/134032819):
@**Jeremy Avigad**, I just sent you an invite to the LEAN project on CoCalc.

#### [Jeremy Avigad (Sep 16 2018 at 03:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/134032876):
I'm in! Thanks very much.

#### [William Stein (Oct 02 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/135039310):
Video chat:   After some investigation and back and forth with appear.in support, I have switched from appear.in to https://jitsi.org/ for our CoCalc video chat.    jitsi.org is completely free and open source, and works very well.

#### [Johan Commelin (Oct 02 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CoCalc/near/135039386):
Thanks for the update!

