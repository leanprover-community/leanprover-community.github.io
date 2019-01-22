---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/9593834elanandmathlib.html
---

## [general](index.html)
### [3.4, elan, and mathlib](9593834elanandmathlib.html)

#### [Johan Commelin (Apr 19 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125295801):
I just installed `elan`. Succesfully it seems. I then ran `mkdir ~/mess/leantest` and inside that directory, I ran `elan toolchain install nightly`. This provided me with a `leanpkg` command, and I ran `leanpkg add https://github.com/leanprover/mathlib`. After cloning from github, it complained `cannot find revision lean-3.4.0 in repository _target/deps/mathlib`. I guess this is somehow expected, because mathlib is not 3.4.0 ready. Right?

#### [Johan Commelin (Apr 19 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125295811):
So which permutation of command should I run, to get the most up to date version of lean + mathlib on my box?

#### [Mario Carneiro (Apr 19 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125295909):
do you have a `leanpkg.toml` file? What is in it?

#### [Sebastian Ullrich (Apr 19 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125295915):
You're probably using Lean stable, which is installed by elan by default - see `lean -v` or `elan show`

#### [Mario Carneiro (Apr 19 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125295926):
What do I need to do to make this work?

#### [Mario Carneiro (Apr 19 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125295931):
Is it just adding a tag with the name `lean-3.4.0`?

#### [Johan Commelin (Apr 19 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125295932):
```
elan show
installed toolchains
--------------------

stable-x86_64-unknown-linux-gnu
nightly-x86_64-unknown-linux-gnu

active toolchain
----------------

stable-x86_64-unknown-linux-gnu (default)
Lean (version 3.4.0, commit 4be96eaaaf71, Release)
```

#### [Johan Commelin (Apr 19 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125295935):
I do not have a `.toml` file

#### [Johan Commelin (Apr 19 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125295974):
Should I write this myself?

#### [Sebastian Ullrich (Apr 19 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125295992):
`leanpkg init <package name>` will create it for you. You can use `leanpkg +nightly init ...` to set the Lean version to a nightly, but I'm not sure there is any point in encouraging users to use nightlies any more. @**Mario Carneiro** What do you think?

#### [Johan Commelin (Apr 19 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296038):
Ok, I see

#### [Johan Commelin (Apr 19 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296039):
Is there a concensus?

#### [Sebastian Ullrich (Apr 19 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296049):
Not yet I think. Right now, `stable` and `nightly` are functionally the same Lean version.

#### [Mario Carneiro (Apr 19 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296050):
Assuming lean is completely frozen now, I guess we can move to building against 3.4.0, but I expect some occasional bugfixes will come along, and then I will want to go back to nightlies

#### [Johan Commelin (Apr 19 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296051):
I hope that, now that 3.4 is out, there is a stable way to get everything working together

#### [Johan Commelin (Apr 19 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296104):
And then we document this, so that users know which 5 commands to run in a fresh directory to get a lean project up and running

#### [Mario Carneiro (Apr 19 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296106):
For now, though, you want to make sure that your lean version is nightly-2018-04-06 since that's what mathlib master is using

#### [Johan Commelin (Apr 19 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296113):
Ok, and how should I make sure I get that nightly, using `elan`

#### [Sebastian Ullrich (Apr 19 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296116):
@**Mario Carneiro** Yeah, I guess a tag should work. Not sure if force-updating it will work too :) .

#### [Johan Commelin (Apr 19 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296119):
(Because it seems using `elan` is wise)

#### [Mario Carneiro (Apr 19 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296123):
I am not the elan guru in this conversation :)

#### [Sebastian Ullrich (Apr 19 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296124):
`leanpkg +nightly-2018-04-06 init mypackage`

#### [Johan Commelin (Apr 19 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296125):
@**Mario Carneiro** When do you expect mathlib to use 3.4? (No pressure...)

#### [Mario Carneiro (Apr 19 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296130):
Probably tomorrow or the day after, when I get a chance to sit down and look at the changes

#### [Johan Commelin (Apr 19 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296178):
@**Sebastian Ullrich** But to have a `leanpkg` command, I already need to first run an `elan` command, right?

#### [Johan Commelin (Apr 19 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296180):
Because `elan` provides me with a `leanpkg`

#### [Sebastian Ullrich (Apr 19 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296187):
No, you just need to have elan installed

#### [Sebastian Ullrich (Apr 19 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296194):
It's the same as `elan run nightly-2018-04-06 leanpkg init mypackage`, if you like that better :)

#### [Johan Commelin (Apr 19 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296237):
Ok, so I empty my leantest directory

#### [Johan Commelin (Apr 19 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296245):
And I get

#### [Johan Commelin (Apr 19 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296248):
```
$ elan run nightly-2018-04-06 leanpkg init leantest
error: toolchain 'nightly-2018-04-06-x86_64-unknown-linux-gnu' is not installed
```

#### [Sebastian Ullrich (Apr 19 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296340):
Oops, I was hoping this worked... then you need to run `elan toolchain install nightly-2018-04-06` first

#### [Johan Commelin (Apr 19 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296348):
Ok, I'll try that

#### [Johan Commelin (Apr 19 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296393):
My first goal now, is to write a 10-line readme, that will explain how to start a fresh project.

#### [Johan Commelin (Apr 19 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296394):
Including VScode integration, I hope

#### [Johan Commelin (Apr 19 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296406):
@**Sebastian Ullrich** That worked. And now I also ran `elan run nightly-2018-04-06 leanpkg init leantest`

#### [Johan Commelin (Apr 19 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296411):
Should the next step be `leanpkg add https://github.com/leanprover/mathlib
`?

#### [Sebastian Ullrich (Apr 19 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296465):
Yes

#### [Mario Carneiro (Apr 19 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296473):
is there a way to get the version number from mathlib?

#### [Sebastian Ullrich (Apr 19 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296480):
You mean the `lean_version`?

#### [Mario Carneiro (Apr 19 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296481):
yes

#### [Johan Commelin (Apr 19 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296483):
Ok, that worked. I assume now I should run `leanpkg build`. Right?

#### [Mario Carneiro (Apr 19 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296484):
The mathlib elan setup doesn't say anything about lean versions

#### [Mario Carneiro (Apr 19 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296536):
@**Johan Commelin** If you get that 10 line startup script working, pr it to the mathlib readme

#### [Sebastian Ullrich (Apr 19 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296537):
@**Johan Commelin** That should work, but not do much. Lean only builds the part of the dependencies you actually import in your `src` directory

#### [Johan Commelin (Apr 19 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296546):
Ok, so there is no need to run `leanpkg build` right now?

#### [Johan Commelin (Apr 19 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296547):
Then I won't do it

#### [Johan Commelin (Apr 19 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296589):
@**Mario Carneiro** Ok, I'll do that. Once I've got it working (^;

#### [Sebastian Ullrich (Apr 19 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296591):
I was surprised you were able to run `leanpkg add` before initializing the package. I guess you got a "failed to open file 'leanpkg.toml'" only at the very end? Pretty much a bug in leanpkg, oh well.

#### [Johan Commelin (Apr 19 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296604):
@**Sebastian Ullrich** I love breaking things. Hehe

#### [Johan Commelin (Apr 19 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296650):
Right, so I did not run `leanpkg build`. Only fired up VScode

#### [Johan Commelin (Apr 19 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296660):
It says `No Lean file active` in the Lean messages, after I opened a `.lean` file

#### [Moses Schönfinkel (Apr 19 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296729):
Clicking anywhere in the file usually fixes this for me.

#### [Johan Commelin (Apr 19 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296749):
Ok, that works. Never had to do that...

#### [Sebastian Ullrich (Apr 19 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296786):
@**Mario Carneiro** Not sure what you're trying to achieve. The Travis build will select the correct version from `lean_version` automatically.

#### [Mario Carneiro (Apr 19 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296794):
well, I'm mildly surprised that the default setup gave the wrong version of lean for mathlib

#### [Mario Carneiro (Apr 19 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296804):
I want a short command or script to give to a newbie that wants the latest version of mathlib and a compatible version of lean

#### [Mario Carneiro (Apr 19 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296858):
I'd prefer that the script not contain the literal string `nightly-2018-04-06` since that ages

#### [Johan Commelin (Apr 19 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296877):
@**Sebastian Ullrich** But I need to tell VScode to use the correct version of lean, right? So I edit the settings, to point it to `~/.elan/toolchains/nightly-2018-04-06-x86_64-unknown-linux-gnu/bin/lean`, is that correct?

#### [Sebastian Ullrich (Apr 19 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125296932):
@**Johan Commelin** I've only tested emacs so far, but specifying `~/.elan/bin/lean` should work

#### [Johan Commelin (Apr 19 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125297004):
```
Lean: Unable to start the Lean server process: Error: spawn ~/.elan/bin/lean ENOENT The lean.executablePath may be incorrect, make sure it is a valid Lean executable
```

#### [Johan Commelin (Apr 19 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125297007):
Alas, it is still complaining

#### [Mario Carneiro (Apr 19 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125297029):
put `.exe` at the end?

#### [Sebastian Ullrich (Apr 19 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125297072):
On Linux?

#### [Sebastian Ullrich (Apr 19 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125297074):
Maybe it doesn't like the `~`

#### [Johan Commelin (Apr 19 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125297080):
Yes, I'm on linux

#### [Johan Commelin (Apr 19 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125297134):
Ok, that seems to have done it. I expanded the `~` to my homedir

#### [Sebastian Ullrich (Apr 19 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125297136):
Nice, good to know

#### [Johan Commelin (Apr 19 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125297144):
Ok, I'm now try to compile Kevin's result that Spec(R) is quasi-compact

#### [Johan Commelin (Apr 19 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125297145):
If that works, then I'll write the little readme

#### [Johan Commelin (Apr 19 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125297154):
Also, is there a way to tell lean not to use all my CPU threads?

#### [Johan Commelin (Apr 19 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125297269):
```
mkdir leantest/
cd leantest/
elan run nightly-2018-04-06 leanpkg init leantest
elan toolchain install nightly-2018-04-06
elan run nightly-2018-04-06 leanpkg init leantest
ls
ls -a
leanpkg add https://github.com/leanprover/mathlib
leanpkg add https://github.com/kbuzzard/lean-stacks-project
ls
elan show

# Change VScode settings to point to "/home/<user>/.elan/bin/lean"
```

#### [Johan Commelin (Apr 19 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125297276):
That is my current bash history

#### [Johan Commelin (Apr 19 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125297290):
So, I'll clean it up, and write a bit of details. But I thought I would log it here as well

#### [Sebastian Ullrich (Apr 19 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125297293):
@**Mario Carneiro** So, this looks like a chicken and egg problem - when selecting the Lean version for creating the package, we don't know what dependencies the user will install yet. Well, it doesn't really matter what version to use for creating the package, so we could suggest to the user to change their Lean version after the fact when adding mathlib. I'm planning to do the same on `leanpkg upgrade`; we can also discuss this at https://github.com/Kha/elan/issues/5

#### [Johan Commelin (Apr 19 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125297535):
O.o.....
```
Lean: Server has stopped due to signal SIGSEGV
```
That doesn't sound good...

#### [Kevin Buzzard (Apr 19 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125298604):
Johan -- one possibility is that you just get everything working in the old way, and just wait until mathlib is running with 3.4.

#### [Kevin Buzzard (Apr 19 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125298643):
The reason this might be useful is that what we will ultimately really need

#### [Kevin Buzzard (Apr 19 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125298644):
is a clear and concise set of instructions

#### [Kevin Buzzard (Apr 19 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125298645):
on how to get Lean 3.4 and mathlib running.

#### [Kevin Buzzard (Apr 19 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125298647):
And at the minute mathlib doesn't work with Lean 3.4, and elan still has teething troubles

#### [Kevin Buzzard (Apr 19 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125298654):
in other words, I guess what I'm saying is that I am waiting until mathlib works with Lean 3.4 before I start thinking about writing down some succinct explanation of how to use elan

#### [Kevin Buzzard (Apr 19 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125298656):
and for me there is no hurry because I have a set-up that works without elan

#### [Kevin Buzzard (Apr 19 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125298707):
OTOH I'm sure Sebastian is appreciating your comments on elan.

#### [Kevin Buzzard (Apr 19 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125298709):
As for the segv

#### [Kevin Buzzard (Apr 19 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125298710):
you do occasionally get these, although they are quite rare

#### [Kevin Buzzard (Apr 19 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125298717):
a good way of getting them is to compile a project, thus getting a bunch of .olean files, and then changing the version of Lean you're using

#### [Kevin Buzzard (Apr 19 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125298720):
so the first thing you need to do is to rule this out

#### [Kevin Buzzard (Apr 19 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125298759):
and the second big question is whether you can reliably reproduce the segfault

#### [Kevin Buzzard (Apr 19 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125298764):
and if you can, then you get an achievement

#### [Kevin Buzzard (Apr 19 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125298766):
and you're allowed to post an issue to the lean repo

#### [Kevin Buzzard (Apr 19 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125298780):
I've had a couple recently but I couldn't reproduce them, annoyingly

#### [Kevin Buzzard (Apr 19 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125298821):
(the moment I get one, I hit ctrl-Z to go back a bit, ctrl-shift-P Lean:restart to restart Lean, and then try typing exactly the same keys again)

#### [Kevin Buzzard (Apr 19 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125298842):
I am really really looking forwards to the stability of 3.4 + mathlib, but until then I have plenty to do :-)

#### [Sebastian Ullrich (Apr 19 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125299255):
Just to be clear, any issues happening _after_ Lean was started successfully should not be elan's fault :)

#### [Johan Commelin (Apr 19 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125301335):
So `find . -name *.olean` finds nothing. Which means the first option is ruled out. I guess. Now I will start the backtracking.

#### [Sebastian Ullrich (Apr 19 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125301402):
The .olean version mismatch problem has been fixed for quite some time

#### [Johan Commelin (Apr 19 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125306980):
Can Lean segfault if it runs out of memory? I opened a file from Kevin's lean-stacks-project and I had not compiled anything before. I only have 4GB in my rusty Thinkpad (no swap). So I think that Lean maybe ran out of memory.

#### [Sebastian Ullrich (Apr 19 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125307443):
There have been many ways for Lean to segfault so far, but that one would be new :)

#### [Johan Commelin (Apr 19 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125307469):
So, should I run `leanpkg build` or something similar? Ought that work?

#### [Sebastian Ullrich (Apr 19 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125307522):
Worth a try, at least then you know it's easily reproducible

#### [Johan Commelin (Apr 19 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125307543):
```
$ leanpkg build
configuring leantest 0.1
mathlib: trying to update _target/deps/mathlib to revision 7d1ab388bb097db5d631d11892e8f110e1f2e9cd
> git checkout --detach 7d1ab388bb097db5d631d11892e8f110e1f2e9cd    # in directory _target/deps/mathlib
HEAD is now at 7d1ab38 feat(list/basic,...): minor modifications & additions
lean-stacks-project: trying to update _target/deps/lean-stacks-project to revision a2204862a0c20c4ea4f98d5685c1a51a3b0279d3
> git checkout --detach a2204862a0c20c4ea4f98d5685c1a51a3b0279d3    # in directory _target/deps/lean-stacks-project
HEAD is now at a220486 Merge branch 'master' of github.com:kbuzzard/lean-stacks-project
> lean --make src

```

#### [Johan Commelin (Apr 19 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125307604):
This completed immediately...

#### [Johan Commelin (Apr 19 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125307607):
Doesn't do any compiling at all

#### [Sebastian Ullrich (Apr 19 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125307844):
Is your segfaulting file saved in the `src` directory?

#### [Johan Commelin (Apr 19 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125316120):
No, the `src/` dir is empty

#### [Sebastian Ullrich (Apr 19 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125325431):
You should save your Lean files in `src`, as described in https://leanprover.github.io/reference/using_lean.html#directory-layout

#### [Johan Commelin (Apr 20 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125384466):
Sorry, I'm completely confused. As you can see from my log above, I only ran `leanpkg add` to add mathlib and lean-stacks-project. Both are added to `_target/deps/`. The leave `src/` empty. What am I doing wrong?

#### [Kevin Buzzard (Apr 20 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125391323):
Here's how you're supposed to run the stacks project.

#### [Kevin Buzzard (Apr 20 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125391361):
First, clone the stacks project.

#### [Kevin Buzzard (Apr 20 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125391523):
Then make it into a lean package with some leanpkg command which I forgot

#### [Kevin Buzzard (Apr 20 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125391558):
then build it

#### [Kevin Buzzard (Apr 20 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125391670):
Here's how you're supposed to make a new project with the stacks project as a dependency

#### [Kevin Buzzard (Apr 20 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125391716):
First make a directory for your new project

#### [Johan Commelin (Apr 20 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125391732):
Ok, I see. I thought you had to `leanpkg add` it

#### [Kevin Buzzard (Apr 20 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125391813):
then use leanpkg add to add the stacks project

#### [Kevin Buzzard (Apr 20 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125391845):
I think I've got it straight.

#### [Johan Commelin (Apr 20 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125391887):
Aha, I hope this helps...

#### [Kevin Buzzard (Apr 20 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125391925):
On behalf of the community I apologise for the lack of docs and the general difficulty of finding the docs you need

#### [Kevin Buzzard (Apr 20 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125391958):
we are working on this problem

#### [Kevin Buzzard (Apr 20 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125392130):
What happens in practice is that Sebastian does a really good job of writing all these package managers

#### [Kevin Buzzard (Apr 20 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125392200):
and then he explains how things work here

#### [Kevin Buzzard (Apr 20 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125392247):
and everyone learns

#### [Kevin Buzzard (Apr 20 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125392513):
and then either stuff doesn't get written, or stuff gets written but in some place you might not expect, or stuff doesn't get written and then the older stuff is written but out of date and wrong.

#### [Johan Commelin (Apr 20 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125392533):
Right, I'll try to figure out the command to turn the clone into a lean package

#### [Patrick Massot (Apr 20 2018 at 10:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125392547):
Yes we are working on it. I really for big improvements in the next few weeks

#### [Kevin Buzzard (Apr 20 2018 at 10:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125392876):
To make matters worse, and by "worse" I mean "better", we now have elan, which is something else

#### [Johan Commelin (Apr 20 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125392932):
@**Kevin Buzzard** Could it be that you mean `leanpkg configure` to download the dependencies?

#### [Patrick Massot (Apr 20 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125392979):
Mathlib goes 3.4, elan matures, TPIL and refman get updated and everything will become much easier

#### [Kevin Buzzard (Apr 20 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125393016):
and the most comprehensive docs on elan are obtained by searching for elan here :-)

#### [Kevin Buzzard (Apr 20 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125393109):
"Mathlib goes 3.4" -- here's hoping!

#### [Kevin Buzzard (Apr 20 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125393225):
Presumably you noticed the rather terrifying-looking stumbling block

#### [Kevin Buzzard (Apr 20 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125393596):
One thing I love about Lean is that we are free to add various type annotations everywhere if we get confused

#### [Kevin Buzzard (Apr 20 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125393614):
and I get confused a lot

#### [Kevin Buzzard (Apr 20 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125394557):
@**Johan Commelin** line 16 of an old commit

#### [Kevin Buzzard (Apr 20 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125394572):
https://github.com/leanprover/lean/commit/37bde20d07dc28b7fd3e84a1c768b9ce547bd5a8#diff-93c4834f2a585510be668daf86b8e81fR16

#### [Kevin Buzzard (Apr 20 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125394649):
That was when mathlib was called library_dev

#### [Kevin Buzzard (Apr 20 2018 at 10:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125394787):
When the docs moved into the reference manual, some of those old docs got lost

#### [Johan Commelin (Apr 20 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125394963):
Ok, thanks!

#### [Kevin Buzzard (Apr 20 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125395693):
You seem to be right -- the "creating new packages" docs survived but the "working on existing packages" para got lost.

#### [Johan Commelin (Apr 20 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125396463):
Whoohoo, now `leanpkg build` is actually doing something!

#### [Kevin Buzzard (Apr 20 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125396803):
I would go and have a cup of tea

#### [Kevin Buzzard (Apr 20 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125396981):
I would also recommend maximising your console window and using ctrl-(minus key) to minimise your font size

#### [Kevin Buzzard (Apr 20 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125397420):
that way successful compilation of a file whose full path is more than 80 characters doesn't result in your terminal being filled with garbage

#### [Johan Commelin (Apr 20 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125397837):
I see... I'm already running fullscreen. I'm about to get a computer account at the department, and I'm going to ask for a second screen on my desk.

#### [Kevin Buzzard (Apr 20 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125397850):
[and note the message I sent you yesterday about certain files which have errors in as they are WIPs; I know it's a bit unprofessional but I develop on more than one machine and github is just a convenient way to store my half-written files]

#### [Johan Commelin (Apr 20 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125397980):
Running VScode on a 12" Thinkpad is horrible

#### [Kevin Buzzard (Apr 20 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125398040):
I am absolutely serious when I say

#### [Kevin Buzzard (Apr 20 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125398142):
that I run VS Code on a laptop with a medium size screen

#### [Kevin Buzzard (Apr 20 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125398190):
and the fact that it was horrible

#### [Johan Commelin (Apr 20 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125398203):
@**Kevin Buzzard** Yes, I saw that message. No problem. I think branches could help you there. You can push WIP branches to github as well.

#### [Kevin Buzzard (Apr 20 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125398209):
actually made me bite the bullet and start wearing glasses

#### [Kevin Buzzard (Apr 20 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125398256):
and now I have glasses (for reading)

#### [Kevin Buzzard (Apr 20 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125398298):
I can just minimise the font to quite small :-)

#### [Kevin Buzzard (Apr 20 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125398440):
I am not good at branches yet.

#### [Kevin Buzzard (Apr 20 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125398475):
but I am getting there.

#### [Kevin Buzzard (Apr 20 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125398688):
I never needed them before because Kenny and Chris work on localised code and don't care if other stuff doesn't compile

#### [Kevin Buzzard (Apr 20 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125398741):
and nobody else has ever paid any attention to the project :-)

#### [Kevin Buzzard (Apr 20 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125398791):
We are nearly done though.

#### [Johan Commelin (Apr 20 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125399260):
```quote
and nobody else has ever paid any attention to the project :-)
```
I'm sorry for being curious

#### [Johan Commelin (Apr 20 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125399367):
I should just wait a couple of days (-;

#### [Kevin Buzzard (Apr 20 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125399566):
I just this morning pushed a version of tah01HR which contains a concrete endgame

#### [Kevin Buzzard (Apr 20 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125399695):
i.e. "we need to prove this lemma and that lemma and then just glue everything together"

#### [Kevin Buzzard (Apr 20 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125399936):
I think I am right when I say that mathlib compiles with the nightly of 6th April

#### [Kevin Buzzard (Apr 20 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125399993):
and the project should work with that

#### [Johan Commelin (Apr 20 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125400371):
So far the compile is doing its job perfectly (-;

#### [Patrick Massot (Apr 20 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125400434):
You don't have to guess here, it's right there: https://github.com/leanprover/mathlib/blob/master/leanpkg.toml#L4

#### [Kevin Buzzard (Apr 20 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125400646):
aah, another undocumented gem ;-)

#### [Johan Commelin (Apr 20 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125400783):
@**Patrick Massot** Yes, now I only need to convince my laptop of that (-;

#### [Patrick Massot (Apr 20 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125408071):
Did you put that same line in your own project `leanpkg.toml`?

#### [Kevin Buzzard (Apr 20 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125408162):
if he cloned my project then it should be there

#### [Johan Commelin (Apr 20 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125408164):
Atm I just cloned the lean-stacks-project repo, which has its own toml

#### [Kevin Buzzard (Apr 20 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125408296):
So the system does actually work

#### [Patrick Massot (Apr 20 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125408297):
what does `which leanpkg` tells you?

#### [Kevin Buzzard (Apr 20 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125408321):
it's just that we need to document it better

#### [Johan Commelin (Apr 20 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125408391):
And `elan` parsed it, and made me use the right version of `leanpkg` and `lean` :tada:

#### [Johan Commelin (Apr 20 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125408557):
```
$ which leanpkg
/home/jmc/.elan/bin/leanpkg
```

#### [Patrick Massot (Apr 20 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125408605):
ok, it's all fine

#### [Patrick Massot (Apr 20 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125408758):
also, make sure you never ever define a leanpath variable in VScode

#### [Patrick Massot (Apr 20 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125408832):
this only leads to confusion

#### [Johan Commelin (Apr 20 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125409071):
I set it to `/home/jmc/.elan/bin/lean`

#### [Patrick Massot (Apr 20 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125409118):
You shouldn't

#### [Johan Commelin (Apr 20 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125409169):
So what *should* I do?

#### [Patrick Massot (Apr 20 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125409362):
You should simply launch VScode from a terminal where the shell path variable is set correctly (ie `which lean` points to `.elan/bin/lean`)

#### [Patrick Massot (Apr 20 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125409629):
which will happen if you have `source $HOME/.elan/env` in your initialization file (`.profile` or `.bashrc` or...)

#### [Johan Commelin (Apr 20 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125410457):
Ok, that makes sense

#### [Johan Commelin (Apr 20 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125410489):
I'll do that from now on

#### [Kevin Buzzard (Apr 20 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125411324):
ha ha, I use leanpath all the time; it points to a symlink :-)

#### [Kevin Buzzard (Apr 20 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125411592):
Johan -- I haven't used elan at all yet but I just changed the README in lean-stacks-project to explain what I think you just did.

#### [Kevin Buzzard (Apr 20 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125411895):
Feel free to submit a PR explaining elan. I have not even attempted to find out whether elan has docs; I have other things to worry about currently :-)

#### [Johan Commelin (Apr 20 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125412651):
If my compile succeeds, then the first thing I will do is write some small docs and PR them.

#### [Patrick Massot (Apr 20 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125423318):
Let me try something (we'll see if we can PR later). Instruction for a first time user of Lean under linux:
* make sure [VScode](https://code.visualstudio.com/download) is installed
* launch VScode and install the Lean extension by clicking the extension icon in the view bar at left and searching for lean. quit VScode for ow
* make sure `git` and `curl` are installed, using your distrib package manager
* `curl https://raw.githubusercontent.com/Kha/elan/master/elan-init.sh -sSf | sh` and type enter when a question is asked. Then add `source .elan/env` to your shell initialization script, say `~/.bashrc`, and source it in the current terminal (or relaunch a new terminal).
* The previous step downloaded the latest stable release, that may be too recent or too old for mathlib, and you really want mathlib. Have a look at https://github.com/leanprover/mathlib/blob/master/leanpkg.toml#L4 to see what is the nightly mathlib currently wants. Say you see `nightly-2018-04-06`. Then run `elan toolchain install nightly-2018-04-06`.
* Now we want some playground to experiment. Use `elan run nightly-2018-04-06 leanpkg new my_playground`. This will  create a `my_playground` directory with a lean project layout. 
* Go to that directory and type `leanpkg add leanprover/mathlib` this will download mathlib and put it inside `my_playground/_target/deps`,
* At this point you can already create some lean file in `my_playground/src`, launch VScode, go to and play with Lean by opening the file, typing `Ctrl-shift-enter` to open Lean message windows, and type, say `#check 1` to see the result
* You cant also use `import group_theory.subgroup` and then `#check is_subgroup`. But this will use uncompiled version of mathlib, which is very inefficient. If you run `leanpkg build` from inside `my_playground` then it will compile only files which are dependencies of mathlib `group_theory/subgroup.lean`.
* If you want to play more, it's better to compile all mathlib once and for all. You can do this by going into `my_playground/_target/deps/mathlib`, type `lean --make`and go get some coffee.

#### [Patrick Massot (Apr 20 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125424229):
That being said, we really need mathlib nightlies (ie. precompiled mathlib)

#### [Patrick Massot (Apr 20 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125424479):
It makes no sense that curious potential users have to wait for mathlib to compile

#### [Johan Commelin (Apr 20 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125428649):
@**Patrick Massot** I think that is a very good start

#### [Johan Commelin (Apr 20 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125428740):
I would also like a small section on how to work on an existing project, like lean-stacks-project

#### [Kevin Buzzard (Apr 20 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125428806):
You can copy that from my README

#### [Kevin Buzzard (Apr 20 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125428860):
except that it should be updated to use elan

#### [Simon Hudon (Apr 21 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125495917):
In elan, when downloading Lean and its library, would it be possible to add a `leanpkg.toml` file at the root of `library`. That would make it easier to browse with emacs.

#### [Sebastian Ullrich (Apr 21 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125496101):
What parts of browsing would that change?

#### [Simon Hudon (Apr 21 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125496250):
When I open `init/meta/tactic.lean` in emacs, it tries to start a lean server and fails and `M-.` won't help 
me go to a definition

#### [Sebastian Ullrich (Apr 21 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125496453):
Oh, it looks like we forgot to include `library/leanpkg.path` in the releases. I'll fix it for the future.

#### [Simon Hudon (Apr 21 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125496722):
Can `leanpkg.path` specify the version of `lean` to launch when editing the files?

#### [Sebastian Ullrich (Apr 21 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/3.4%2C%20elan%2C%20and%20mathlib/near/125496876):
Ah, you are right. I guess injecting a `leanpkg.toml` file could indeed be the best solution.

