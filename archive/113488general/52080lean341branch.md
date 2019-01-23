---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/52080lean341branch.html
---

## Stream: [general](index.html)
### Topic: [lean-3.4.1 branch](52080lean341branch.html)

---

#### [Mario Carneiro (May 25 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127073781):
I added a lean-3.4.1 branch to mathlib, which I think should fix the issues with elan/leanpkg (assuming I spelled everything correctly). @**Sebastian Ullrich** Will there be any problem with just keeping the branch up to date with master (although I don't think branch symlinks are a thing)? I don't see any reason not to.

#### [Kevin Buzzard (May 25 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127073806):
Mario -- many thanks!

#### [Kevin Buzzard (May 25 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127073849):
You did not keep the 3.3.0 branch up to date with mathlib master -- why do you want to keep the 3.4.1 branch up to date?

#### [Kevin Buzzard (May 25 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127073866):
Why not just have a release version for 3.4.1?

#### [Mario Carneiro (May 25 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074034):
because lean does not have nearly enough versions

#### [Mario Carneiro (May 25 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074040):
mathlib does not develop on lean's schedule

#### [Mario Carneiro (May 25 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074044):
and there is a huge range of commits that are compatible with 3.4.1

#### [Kevin Buzzard (May 25 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074083):
I understand the argument.

#### [Kevin Buzzard (May 25 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074102):
As I explained to you in email -- I would ideally like to be able to point people to a "3.4.1 release" version of mathlib which is "the canonical version of mathlib to run with the 3.4.1 release version of Lean"

#### [Kevin Buzzard (May 25 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074106):
And your argument is

#### [Kevin Buzzard (May 25 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074110):
that the canonical version is the latest version

#### [Kevin Buzzard (May 25 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074113):
right?

#### [Kevin Buzzard (May 25 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074187):
OTOH I am _forced_ to point certain people (the IT people here, the CoCalc people) to a canonical version of mathlib which goes with Lean 3.4.1 release, because both of these organisations refuse to work with moving targets

#### [Kevin Buzzard (May 25 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074190):
so I am going to tell them both to point to the very first commit in the 3.4.1 branch.

#### [Kevin Buzzard (May 25 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074194):
I cannot envisage any problems with this, and it sounds like the best compromise.

#### [Mario Carneiro (May 25 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074201):
You can point them to the latest version, and they can take that at any point

#### [Kevin Buzzard (May 25 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074206):
The problem with that idea

#### [Kevin Buzzard (May 25 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074207):
is that then it will be hard for people to work out exactly which version they are running

#### [Kevin Buzzard (May 25 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074211):
and it is very much in my interest that code runs on CoCalc if and only if it runs on the machines here

#### [Kevin Buzzard (May 25 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074251):
so I would very much like CoCalc and the machines here to be running exactly the same code

#### [Mario Carneiro (May 25 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074252):
We have a lean-3.3.0 branch as well, which is not a tag but a branch because it incorporates new bugfixes and such which are compatible with 3.3.0

#### [Kevin Buzzard (May 25 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074253):
Oh -- so 3.3.0 moves?

#### [Patrick Massot (May 25 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074254):
There nothing like "the very first commit in the 3.4.1 branch" in git

#### [Kevin Buzzard (May 25 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074255):
Oh!

#### [Mario Carneiro (May 25 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074256):
not much, but yes

#### [Patrick Massot (May 25 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074259):
You can tag a commit

#### [Kevin Buzzard (May 25 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074261):
Aah

#### [Kevin Buzzard (May 25 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074262):
Mario -- last question then

#### [Kevin Buzzard (May 25 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074272):
can I persuade you to tag a commit?

#### [Patrick Massot (May 25 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074273):
But a branch is only some moving marker attached to some moving commit

#### [Patrick Massot (May 25 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074288):
What you want is Mario creating a release tag

#### [Patrick Massot (May 25 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074292):
not a branch

#### [Kevin Buzzard (May 25 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074332):
Thanks for clarifying Patrick.

#### [Mario Carneiro (May 25 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074333):
mathlib doesn't do releases like that

#### [Kevin Buzzard (May 25 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074341):
Sorry that my poor understanding of git is just adding to the noise

#### [Patrick Massot (May 25 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074344):
Kevin kindly asks to change this

#### [Mario Carneiro (May 25 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074347):
if you want a commit, then it will be an artificial stopping point anyway, so just pick a point and write down the hash

#### [Kevin Buzzard (May 25 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074348):
I can do this

#### [Kevin Buzzard (May 25 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074349):
but it will look confusing

#### [Kevin Buzzard (May 25 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074356):
I am not asking for this for me

#### [Kevin Buzzard (May 25 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074362):
I am asking for this for other people

#### [Kevin Buzzard (May 25 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074366):
who want "Lean + Mathlib version 3.4.1"

#### [Mario Carneiro (May 25 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074369):
That's what the branch is for

#### [Kevin Buzzard (May 25 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074370):
no

#### [Kevin Buzzard (May 25 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074372):
They want a canonical uniquely defined thing

#### [Kevin Buzzard (May 25 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074374):
not a moving target

#### [Kevin Buzzard (May 25 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074379):
because both refuse to move

#### [Kevin Buzzard (May 25 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074420):
I will give them a hash

#### [Kevin Buzzard (May 25 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074434):
It is not ideal, but it is the best solution if there is to be no release tag

#### [Kevin Buzzard (May 25 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074452):
Thanks both of you for clarifying what I should be doing :-)

#### [Mario Carneiro (May 25 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074458):
I think 78d28c5cb58f6a22fbb8fc940cc6f97bc0111602 is the last "update to lean" commit

#### [Mario Carneiro (May 25 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074505):
but I don't know what leanpkg does with tags v branches, so I don't want to carelessly tag it

#### [Mario Carneiro (May 25 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074507):
because I want leanpkg to find the branch

#### [Kevin Buzzard (May 25 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074512):
If creating a tag causes problems for other people then clearly this is an argument against creating a tag

#### [Patrick Massot (May 25 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074517):
I don't understand the potential problem here

#### [Patrick Massot (May 25 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074519):
with a tagged release

#### [Johan Commelin (May 25 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074566):
Just don't tag it with `lean-3.4.1`

#### [Mario Carneiro (May 25 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074567):
if you ask for elan to give you lean + mathlib 3.4.1, you should get the latest mathlib that is compatible with 3.4.1, which is master

#### [Johan Commelin (May 25 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074575):
Right, Kevin, maybe you can trick them.

#### [Johan Commelin (May 25 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074581):
You ask them to install elan, and use elan to install mathlib 3.4.1

#### [Johan Commelin (May 25 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074583):
And they won't realise they just installed a moving target...

#### [Mario Carneiro (May 25 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074625):
that's what travis did for a long time, and it worked pretty well

#### [Patrick Massot (May 25 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074628):
```quote
Just don't tag it with `lean-3.4.1`
```
Sure, the tag would need to be something like: spring2018

#### [Johan Commelin (May 25 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074631):
Otoh, if users start complaining, you're in trouble anyway...

#### [Johan Commelin (May 25 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074641):
Because they will say: hey, why is this stuff not in your mathlib...

#### [Mario Carneiro (May 25 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074648):
I don't mind having mathlib versions (which would be different from lean versions), but I would like leanpkg to work with them if possible

#### [Johan Commelin (May 25 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074658):
Right, so @**Sebastian Ullrich** can you make `elan` to listen to some tags as well?

#### [Patrick Massot (May 25 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074660):
We probably need to wait for @**Sebastian Ullrich** then

#### [Patrick Massot (May 25 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074661):
oops

#### [Patrick Massot (May 25 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074664):
We pinged him at the same time

#### [Patrick Massot (May 25 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074706):
sorry about the harassment

#### [Johan Commelin (May 25 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127074707):
Urgent matters (-;

#### [Sebastian Ullrich (May 25 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127075441):
> Will there be any problem with just keeping the branch up to date with master (although I don't think branch symlinks are a thing)? I don't see any reason not to.

Yes, I think it's either that or saying "Nobody should use nightlies right now anyway", setting `lean-3.4.1` as the default branch, and not updating or outright removing `master`

#### [Mario Carneiro (May 25 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127075447):
I did set the mathlib dependency to lean-3.4.1 as well

#### [Sebastian Ullrich (May 25 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127075502):
Uh, where?

#### [Mario Carneiro (May 25 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127075506):
leanpkg.toml

#### [Mario Carneiro (May 25 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127075511):
lean_version = "3.4.1"

#### [Sebastian Ullrich (May 25 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127075627):
Ah, I see. Yeah, it's a bit weird to do that on the `master` branch since it means Lean nightly people using mathlib will get warnings, which is why I would slightly prefer the latter option I listed. But I guess it's okay either way.

#### [Mario Carneiro (May 25 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127075662):
I mean, right now there's no difference, and it seems like lean repo is frozen for the foreseeable future so I guess it's fine to officially run 3.4.1

#### [Patrick Massot (May 25 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127075666):
Is there any Lean nightly though?

#### [Mario Carneiro (May 25 2018 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127075706):
if and when nightlies start back up again we can switch back

#### [Sebastian Ullrich (May 25 2018 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127075715):
Yes, both ways should work fine

#### [Sebastian Ullrich (May 25 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean-3.4.1%20branch/near/127075796):
As Mario said, tag support would have to be added to `leanpkg`, unless we'd want `elan` to more or less reimplement and supersede the former. Which is possibly, and https://github.com/Kha/elan/issues/7 already points in that direction, but... not something I want to do right now

