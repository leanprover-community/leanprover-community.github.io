---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/02472mathlibbranches.html
---

## Stream: [general](index.html)
### Topic: [mathlib branches](02472mathlibbranches.html)

---

#### [Scott Morrison (Jun 20 2018 at 03:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128338643):
What's the plan with branches for `mathlib`? We seem to have gone back and forth between using `master` and using `lean-3.4.1`. I'd just gone to the effort of creating `lean-3.4.1` branches in all my repos, and making them the default, so that `leanpkg upgrade` would successfully pull new changes from `mathlib`, but now it seems we've going back to using `master`.

#### [Scott Morrison (Jun 20 2018 at 03:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128338693):
I'm happy to do whatever is required, but would like some instructions on how to set up repos with dependencies `mathlib <--- repoA <--- repoB`, so `leanpkg upgrade` does what I hope it does. :-)

#### [Scott Morrison (Jun 20 2018 at 03:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128338708):
My guess is that the current instruction is: "set `lean_version=master` in all your leanpkg.toml files, and work on the master branch of `repoA`"

#### [Mario Carneiro (Jun 20 2018 at 03:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128338773):
I am still planning on keeping `lean-3.4.1` branch up to date with master, but I expect that it may drift behind from time to time. Maybe you can consider it the "stable version", but it's really just me being lazy :)

#### [Scott Morrison (Jun 20 2018 at 03:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128338787):
Nope, that doesn't work.. Maybe `lean_version="nightly"`?

#### [Mario Carneiro (Jun 20 2018 at 03:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128338789):
If you want bleeding edge you should probably stick to the master branch

#### [Scott Morrison (Jun 20 2018 at 03:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128338790):
Nope: `error: binary package was not provided for 'darwin'`

#### [Scott Morrison (Jun 20 2018 at 03:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128338839):
I still really don't understand the algorithm `leanpkg upgrade` uses to pick which commit to go to. It seems to be affected by both the setting of `lean_version`, and perhaps the name of the branch you're currently in in your local repo?

#### [Scott Morrison (Jun 20 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128344446):
Okay, I think the tooling is actually defective, and there's currently no way to have a chain of repos `mathlib <--- repoA <--- repoB` so that `leanpkg upgrade` tracks the master branch of mathlib.

#### [Scott Morrison (Jun 20 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128344514):
(it _is_ possible to keep up with mathlib's 3.4.1 branch, by having repoA in a `lean-3.4.1` branch, and setting `lean_version="3.4.1"` in all the leanpkg.toml files)

#### [Sean Leather (Jun 20 2018 at 08:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128347908):
I think it's unreasonable to expect someone to continuously sync one branch to another, especially without being written down as part of a process or a checklist. It will certainly be forgotten. If you really want branches synced, it should be automated (e.g. by cron).

I think mathlib — that is, both its users and its developers — would be better off following the standard practice of releasing numbered versions. A version provides a common checkpoint and ideally includes a description of changes from the last version. Mathlib versions will naturally change independently of Lean versions because they are independent projects.

#### [Kevin Buzzard (Jun 20 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128349762):
```quote
I think mathlib — that is, both its users and its developers — would be better off following the standard practice of releasing numbered versions. A version provides a common checkpoint and ideally includes a description of changes from the last version. Mathlib versions will naturally change independently of Lean versions because they are independent projects.
```
A huge +1 from my army of undergraduate users, who just want to be told "install that version of mathlib and then do nothing until I tell you". And +1 from cocalc too.

#### [Scott Morrison (Jun 20 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128356374):
Numbered versions for mathlib would be fine, but we'd need to switch to a numbering system that is independent of Lean, as we know that Lean versions can get stuck for a long time! Is there some mechanism for leanpkg to understand independent versions for Lean and for mathlib? It seems not.

#### [Mario Carneiro (Jun 20 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128356507):
Furthermore mathlib doesn't really have "releases" like a normal software project, it's basically a continuous stream of improvements, so the only reasonable versioning I can see is date-based

#### [Sean Leather (Jun 20 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128356522):
I agree with version numbers independent of Lean and with date-based version numbers. [CalVer](https://calver.org/) appears to be a new name for the latter.

#### [Sean Leather (Jun 20 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128356801):
@**Mario Carneiro** But, just to be clear, a version number would label a “release” of sorts, right? I think the extreme alternative of considering every git commit hash a version creates too much work and confusion. From the developer's perspective, creating a new version generally involves some amount of work (e.g. documentation and packaging), so it should happen only occasionally. And from the user's perspective, it simplifies usage to work with batches of possibly-breaking changes rather than update with every single change.

#### [Mario Carneiro (Jun 20 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128356821):
I think we can merge this with plans to precompile mathlib easily enough

#### [Mario Carneiro (Jun 20 2018 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128356863):
for example, have mathlib nightlies labeled by date

#### [Sean Leather (Jun 20 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128356938):
But nightlies represent in-progress work, not released work. You want a release version to indicate some stopping point that describes some meaningful change wrt the last version.

#### [Sean Leather (Jun 20 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128356950):
Using nightlies as versions is no better than using commit hashes.

#### [Mario Carneiro (Jun 20 2018 at 13:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128357342):
But that's just my point. In most software projects there is "in-progress" which becomes "release", but in mathlib it is either always in progress or never in progress depending on your point of view. I try to make sure all commits build, and for a formal verification project that's really the only measure of correctness besides style concerns. So you can literally make any commit a release and all you need is the packaging stuff

#### [Mario Carneiro (Jun 20 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128357411):
In metamath there is a set.mm project that gets commits whenever people want to do something, and then every day or so the website is built (theorem display pages and crosslinks) - this is the build artifact - and that's it. The latest build is also hosted on the website. There is no further versioning applied; you can look at an old version if you want by checking out its commit.

#### [Mario Carneiro (Jun 20 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128357461):
A formal verification project acts like a software project in many ways, but this is one point of difference, I think.

#### [Sean Leather (Jun 20 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128357657):
And my points are these:

1. You've worked on computability features over multiple commits. There *is* a point at which you think you're finished. *That* is the point where you might make a release to describe to the world the changes you've introduced. (In this case, the release is a form of marketing.) You don't want to “release” every in-progress commit because the important news gets lost.

2. Users of mathlib as a library want to be able to look at what is currently considered “stable.” They also want to see what changes have been made over time, esp. if a user is transitioning from an old version to a new version. Nightlies don't give any indication of this because they are just builds. Versioning needs documentation, documentation takes time, and one doesn't want to spend that time every day. Also, you don't want to overload users with a huge number of versions because that just adds noise to the signal.

#### [Sean Leather (Jun 20 2018 at 13:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128357669):
Is `set.mm` a software library used by others? Or is it more like verified documentation?

#### [Mario Carneiro (Jun 20 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128357680):
It is neither. It is a collection of proven theorems, roughly laid out like a math textbook

#### [Sean Leather (Jun 20 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128357722):
That sounds like documentation rather than software. In which case, I don't see the parallel to mathlib.

#### [Mario Carneiro (Jun 20 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128357733):
I'm not sure I understand - mathlib is in the same position, except the documentation needs more work

#### [Sean Leather (Jun 20 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128357735):
Can I take `set.mm` and build my own software with it?

#### [Mario Carneiro (Jun 20 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128357740):
you can take set.mm and build your own theorems with it

#### [Mario Carneiro (Jun 20 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128357742):
the curry howard isomorphism is not so relevant here

#### [Mario Carneiro (Jun 20 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128357789):
I get that you think of mathlib as a software library, but it is currently much more a database of theorems than that

#### [Sean Leather (Jun 20 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128357791):
Fair enough. Is that what people do? Or do people use `set.mm` as a source for the textbook.

#### [Mario Carneiro (Jun 20 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128357793):
Of course it can be both at the same time

#### [Sean Leather (Jun 20 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128357798):
```quote
I get that you think of mathlib as a software library, but it is currently much more a database of theorems than that
```
I beg to differ. :smile:

#### [Mario Carneiro (Jun 20 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128357813):
I think that mathlib is currently mostly used as a source of theorems and definitions that people can build on

#### [Sean Leather (Jun 20 2018 at 13:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128357823):
```quote
I think that mathlib is currently mostly used as a source of theorems and definitions that people can build on
```
And how is that so different from a software library, which is  a collection of programs that people can build on?

#### [Mario Carneiro (Jun 20 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128357869):
You can read set.mm like a book if you want, learn set theory and what have you, or you can import it into your own theorems and prove something nontrivial without going through the basics

#### [Mario Carneiro (Jun 20 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128357876):
the same is true of mathlib, although the first goal needs work

#### [Mario Carneiro (Jun 20 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128357888):
It's not so different

#### [Mario Carneiro (Jun 20 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128357891):
However, what is there is already done, finished

#### [Mario Carneiro (Jun 20 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128357897):
what is not finished is the larger story of how everything (in some area) comes together

#### [Sean Leather (Jun 20 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128357951):
But things change in mathlib, as they should. If I'm using mathlib as a foundation for my work, I want to (a) be able to point at a version that I used and (b) look at newer versions to figure out how I need to change my work to fit the changes in mathlib.

#### [Johan Commelin (Jun 20 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128357954):
Mario, I think tagging something with a date is not so hard. So how about you "release" such a tag now and then? For example after the merge of a new "feature" (e.g. Scott's category theory) or something like quotient groups, or whatever.

#### [Mario Carneiro (Jun 20 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128357957):
I see your point about the computability stuff, and I have been using mathlib as a place to store my project in progress. Arguably that should be a branch, and possibly there will be some reorganization to address this in the future

#### [Sean Leather (Jun 20 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128357997):
This may not be standard practice for `set.mm`, but it is for software engineering in the real world, and it's that way for good reasons.

#### [Mario Carneiro (Jun 20 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358009):
However, everything that has been committed is done, and there is no issue with making reference to it if you wanted

#### [Johan Commelin (Jun 20 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358014):
Mario, it is not about what is possible, but how easy it is for newbies.

#### [Sean Leather (Jun 20 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358017):
My point was not to say that you shouldn't include work-in-progress.

#### [Mario Carneiro (Jun 20 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358033):
Johan, I think nightlies address your concern; Sean seems to want more than this

#### [Johan Commelin (Jun 20 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358037):
Mario, to play the devil's advocate: "What do you even mean with 'work in progress'?"

#### [Johan Commelin (Jun 20 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358042):
If the commit builds, then it builds.

#### [Mario Carneiro (Jun 20 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358044):
I mean that I wrote 10 theorems, but I plan to prove a hundred more

#### [Mario Carneiro (Jun 20 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358047):
it doesn't make the 10 theorems wrong

#### [Johan Commelin (Jun 20 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358089):
Exactly

#### [Johan Commelin (Jun 20 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358096):
But once you are done with the 100 theorems. That commit could be tagged with "mathlib-2018-06-20".

#### [Sean Leather (Jun 20 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358097):
But theorem names do change, or theorems get reorganized.

#### [Sean Leather (Jun 20 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358109):
So, while everything builds, that's not really the end of the story.

#### [Johan Commelin (Jun 20 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358113):
And then people would see the tag and know: "Hey, that was a commit in which a lot of theorems that belong together were finally all in mathlib"

#### [Johan Commelin (Jun 20 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358122):
So, I agree with Sean and Kevin and others that certain "not-work-in-progress" commits should get a bit of extra highlighting by `git tag`

#### [Mario Carneiro (Jun 20 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358168):
That seems reasonable, but I would argue: what really makes that commit special that isn't shared by later commits?

#### [Mario Carneiro (Jun 20 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358174):
when you want to use a finished development, you just need to get some commit after it's all in, not the first

#### [Johan Commelin (Jun 20 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358182):
True. Explain that to your local sysadmin.

#### [Johan Commelin (Jun 20 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358184):
Mario, it is all about convenience for users.

#### [Mario Carneiro (Jun 20 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358221):
so all that matters is the news, the announcement "project completed"

#### [Mario Carneiro (Jun 20 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358226):
set.mm has a news/announcements page for this

#### [Johan Commelin (Jun 20 2018 at 13:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358229):
Yes, with a recognizable tag so that sysadmins can easily pull the "latest release" and jot down the release tag in some notebook.

#### [Mario Carneiro (Jun 20 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358236):
which is just a bunch of blurbs marked by date (not even associated specifically to set.mm versions)

#### [Johan Commelin (Jun 20 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358239):
They won't jot down commit hashes.

#### [Johan Commelin (Jun 20 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358251):
If the sysadmin start updating software, he just wants to go to https://github.com/leanprover/mathlib/releases and grab the latest release.

#### [Johan Commelin (Jun 20 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358253):
He doesn't care about other stuff.

#### [Sean Leather (Jun 20 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358255):
Here's what I think a version release should minimally involve:

1. A name/number
2. A `git tag`
3. Documentation of changes since the last release

Bonus:

1. Builds for various platforms as appropriate
2. Announcement blog post or whatever

#### [Johan Commelin (Jun 20 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358316):
Right and a good measure of whether a commit is "release-worthy" is whether we have anything sensible to mention at point 3 (in a reasonably short message).

#### [Mario Carneiro (Jun 20 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358319):
How do you feel about replacing (3) with a changelog?

#### [Sean Leather (Jun 20 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358363):
That *is* a change log, but it's wrt versions.

#### [Mario Carneiro (Jun 20 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358367):
I'm aware they carry the same information

#### [Mario Carneiro (Jun 20 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358370):
but I would rather have all changes logged in one place

#### [Sean Leather (Jun 20 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358382):
I think the significance of less-than-daily releases is important.

#### [Mario Carneiro (Jun 20 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358388):
Otherwise you have to go check the history every time to write the change log for that version

#### [Sean Leather (Jun 20 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358440):
@**Mario Carneiro** I'm not sure what exactly you're arguing for or against. I didn't mention where the documentation should take place. A change log (like [this one](https://github.com/spl/dlist/blob/master/ChangeLog.md) in one of my Haskell packages) would be my first choice.

#### [Mario Carneiro (Jun 20 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358457):
If the changelog is just updated incrementally, then it may as well just be like the news page I described

#### [Mario Carneiro (Jun 20 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358462):
it need not have those big version headers

#### [Sean Leather (Jun 20 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358505):
But a change log would make more sense if it described the points between which the changes were made.

#### [Sean Leather (Jun 20 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358510):
That's where version numbers come in.

#### [Mario Carneiro (Jun 20 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358523):
I'm arguing for the following: nightlies, plus changelog labeled by dates / nightly version numbers

#### [Johan Commelin (Jun 20 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358533):
Mario, how often do you expect updates to the changelog?

#### [Mario Carneiro (Jun 20 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358534):
big versions are meaningless, they are literally the sum of their parts here

#### [Mario Carneiro (Jun 20 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358582):
when a project finishes, some breaking change is made, large or small improvements worth note

#### [Johan Commelin (Jun 20 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358583):
```quote
big versions are meaningless, they are literally the sum of their parts here
```
Nope. They are the sum of their meaningful parts + epsilon cruft of work in progress.

#### [Mario Carneiro (Jun 20 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358597):
it would basically be a place for advertising new stuff

#### [Sean Leather (Jun 20 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358605):
```quote
I think the significance of less-than-daily releases is important.
```
I can't currently quantify that importance, but I think it makes a difference to users to document *batches* of changes rather than *individual* changes you'll get with daily/nightly releases.

#### [Mario Carneiro (Jun 20 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358649):
and it easily supports diffs with zero effort, just look at the dates

#### [Johan Commelin (Jun 20 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358660):
Mario, I hope it is clear that we are not trying to convince you that less-than-daily releases will be a benefit for *you*.

#### [Mario Carneiro (Jun 20 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128358669):
"Oh, I haven't updated since mathlib of jun 1, let's look at the changelog to see what happened in the past 20 days"

#### [Kevin Buzzard (Jun 20 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128382330):
```quote
"Oh, I haven't updated since mathlib of jun 1, let's look at the changelog to see what happened in the past 20 days"
```
My users will update mathlib never. My users are using things like cocalc which has explicitly said it wants to update rarely. My users are using things like the computers in our departmental computer room which have explicitly told me that they will update precisely once per year, over the summer, and will not tolerate anything else. It would be lovely to tell my users "you're using mathlib v3.4.1" or "mathlib v1" or whatever. My users do not want bleeding edge mathlib so all this talk of changelogs is irrelevant to them. I'm just pointing out the existence of a large body of users for whom a lot of this talk is irrelevant, and stability and clarity would be extremely convenient. We will achieve stability with a git hash, but not so much clarity. I know you (Mario) have consistently resisted just randomly making a release but given that the topic has come up yet again I thought I would once more try to explain how people using Lean in completely different ways to you (people who want or have to solve my example sheet questions this coming October and who would like to have the same version of lean/mathlib running on all their devices) might appreciate something less messy than a commit hash. I still occasionally consider forking and freezing, but I really feel like this should be a last resort because all that will happen when I tell people to download mathlib from my GH will be that I'll end up with a bunch of undergraduates who think that I wrote mathlib.

#### [Mario Carneiro (Jun 20 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128383237):
I understand that there are other ways to make use of mathlib, but that's your business, not mine. I don't see why you can't pick a version of mathlib and make a big deal of it on your own without my intervention. It sounds like you are building your own product, based on mathlib, and you can version that however you like. There is no need for any of this to affect mathlib versioning.

#### [Mario Carneiro (Jun 20 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128383290):
Just tell all your clients "we are using mathlib-2018-06-20 for the next year"

#### [Simon Hudon (Jun 20 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128383518):
Whether it involves you or not, it might be useful to have a coalition of library developers to select versions of `mathlib` that we standardize on. Otherwise, if you rely on two independent packages, they may rely on two subtilely different versions of `mathlib`.

#### [Simon Hudon (Jun 20 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128383531):
A good place for documenting that choice would be `mathlib` itself

#### [Kevin Buzzard (Jun 20 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128383561):
```quote
Just tell all your clients "we are using mathlib-2018-06-20 for the next year"
```
right -- that's exactly what I'm going to tell them. But probably with a commit hash.

#### [Mario Carneiro (Jun 20 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128383818):
It is fully possible that two independent packages can rely on slightly different versions of mathlib, and while this will not always cause an incompatibility (since in many cases you can update mathlib with no upstream changes), it might. But in this case, one or both packages is out of date, and should be updated to master.

#### [Mario Carneiro (Jun 20 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128383855):
If you would like an arbitrary standardization point (and nightlies are too fast for you), let's say to prefer commits that are the first of the month

#### [Mario Carneiro (Jun 20 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128384265):
But I can't think of any situation as a third party developer to want to update to a version of mathlib that is not the current master

#### [Mario Carneiro (Jun 20 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20branches/near/128384338):
i.e. if you say "let's use version X from now on", it should always be the case that X is the current master or nightly at the time of the announcement

