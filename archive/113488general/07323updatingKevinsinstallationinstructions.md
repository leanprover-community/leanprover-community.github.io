---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/07323updatingKevinsinstallationinstructions.html
---

## Stream: [general](index.html)
### Topic: [updating Kevin's installation instructions](07323updatingKevinsinstallationinstructions.html)

---

#### [Scott Morrison (Oct 06 2018 at 03:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135291857):
Hi @**Kevin Buzzard**, I'm thinking that since `elan` has now arrived and is pretty good, we should update your blog post.

If I wrote a guest post for you, could we put that up, and add a prominent link at the top of your old post?

#### [Kevin Buzzard (Oct 06 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135303201):
Yes that would be fine. I have never used elan.

#### [Kevin Buzzard (Oct 06 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135303363):
I also think we should plug the trivial way of getting Lean and Mathlib running on Windows 10: https://xenaproject.wordpress.com/getting-lean-and-mathlib-running-in-the-mlc/

#### [Kevin Buzzard (Oct 06 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135303403):
There are no links to that page on the site because the system got changed again and now it's even easier for us at Imperial, we fire up VS Code and it's all there.

#### [Kevin Buzzard (Oct 06 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135303409):
But on Thursday night one person with a win10 machine asked about installation and I said "I have just the link for you".

#### [Kevin Buzzard (Oct 06 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135303452):
For those not clicking: the full installation procedure is " Download VS Code, now download this zip file (containing lean and mathlib lean and olean files and a leanpkg.path etc) and now tell VS Code where Lean is and now open this folder and it all works.". No git, no msys2, no command line

#### [Scott Morrison (Oct 06 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135308310):
Okay! It would be good if we could arrange for creating that zip file automatically, so it doesn't become an ancient stranded artefact.

#### [Scott Morrison (Oct 06 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135308315):
I think I am going to wait just a moment before writing that blog post --- Gabriel has just reviewed my PR to have the VS Code extension offer to install Lean, so it seems likely that will land soon, and this will make the instructions even easier.

#### [Kevin Buzzard (Oct 06 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135308930):
Yes -- that link above suffered from document rot after about 3 days, when someone in ICT said "oh wow, is that what you're telling them? We can probably automate all of that". I thought they were crazy. We'll see. The reason I think they're crazy is that now when any undergraduate launches Visual Studio Code on a machine in the maths department, it starts off by default with a minimal Lean project open! The doc hence became obsolete. I can see this causing confusion for non-converts later down the line though...but I decided that this was not currently my problem.

#### [Gabriel Ebner (Oct 06 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135310090):
```quote
Gabriel has just reviewed my PR to have the VS Code extension offer to install Lean, so it seems likely that will land soon
```
It should come to a vscode installation near you any moment now!

#### [Scott Morrison (Oct 06 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135310363):
... and, it works!

#### [Scott Morrison (Oct 06 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135310407):
If anyone wants to try deleting their Lean installation and trying it out, the VS Code extension now installs elan for you upon request! --- It took less than 2 minutes for me just now.

#### [Scott Morrison (Oct 06 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135310409):
I will try to make a little video walk-through.

#### [Scott Morrison (Oct 06 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135310419):
@**Gabriel Ebner** --- I was just thinking about making a "build all olean files" command in VS Code, as this is a common task. Do you think it is better to use the model of `batch.ts`, or to create a terminal and run the commands there?

#### [Scott Morrison (Oct 06 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135310422):
(I haven't been able to get the batch mode to work.)

#### [Gabriel Ebner (Oct 06 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135310466):
Have you seen `ctrl+p task build`?  Should we package it up as a command as well?

#### [Scott Morrison (Oct 06 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135310545):
No, I haven't. What is `ctrl+p`? On mac that doesn't seem to do anything.

#### [Scott Morrison (Oct 06 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135310589):
Ah, under `cmd-shift-p` I get `Tasks: Run Build Task`

#### [Scott Morrison (Oct 06 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135310591):
and under that `leanpkg: configure` and a few others.

#### [Scott Morrison (Oct 06 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135310602):
Yes, putting `lean --make _target && lean --make` as a task under that would be a great solution.

#### [Scott Morrison (Oct 06 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135310700):
I guess the `lean --make` is silly, that should just be `leanpkg build`.

#### [Scott Morrison (Oct 06 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135310701):
But having some way to compile everything in the dependencies seems to be requested often.

#### [Gabriel Ebner (Oct 06 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135310703):
Oh, on mac it is `cmd+p task build` then.  BTW, your command is equivalent to `lean --make`.

#### [Scott Morrison (Oct 06 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135310707):
Hmm... I guess so. :-)

#### [Scott Morrison (Oct 06 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135310810):
There's no way to ask `leanpkg` to completely compile the dependencies, is there?

#### [Gabriel Ebner (Oct 06 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135310816):
No.

#### [Scott Morrison (Oct 06 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135310823):
It would be great to have `leanpkg build-dependencies` as well as `leanpkg clean` one day.

#### [Scott Morrison (Oct 06 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135310863):
In the meantime, what do you think of adding `lean --make` as a build task? It would be a little awkward, as it probably belongs in `leanpkg.ts`, but isn't actually using `leanpkg`.

#### [Chris Hughes (Oct 06 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135311782):
I have some error, related to the fact that I have a space in my username
`C:\msys64\home\Christopher Hughes\mathlibs\exp>leanpkg build
'Hughes\.elan\toolchains\3.4.1\bin\..' is not recognized as an internal or external command,
operable program or batch file.
C:\Users\Christopher:1:0: error: file 'C:\Users\Christopher' not found
<unknown>:1:1: error: file 'C:\Users\Christopher' not found`

#### [Kevin Buzzard (Oct 06 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135312119):
You have a space in "Christopher Hughes" and because of an irreparable flaw in Windows you are going to struggle.

#### [Kevin Buzzard (Oct 06 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135312120):
If you can somehow change it to "Christopher_Hughes" this will change the behaviour of things.

#### [Scott Morrison (Oct 06 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135312763):
Here's a short video I just made that shows a complete installation of Lean on a mac. Takes 3:40! (Well, with some time lapse for the downloads...)

#### [Scott Morrison (Oct 06 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135312764):
https://www.youtube.com/watch?v=k8U6YOK7c0M&feature=youtu.be

#### [Scott Morrison (Oct 06 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135312813):
(This uses the latest update to the VS Code extension, which now offers to install elan and Lean for you, if it can't find them.)

#### [Scott Morrison (Oct 06 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135312818):
Sometime in the next few days I will try to make a windows video as well.

#### [Chris Hughes (Oct 06 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135313619):
```quote
If you can somehow change it to "Christopher_Hughes" this will change the behaviour of things.
```
I think this will be more effort than it's worth. I'm going back to my old setup

#### [Kevin Buzzard (Oct 06 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135314396):
I've noticed that kids these days far prefer video tutorials to reading boring old web pages.

#### [Ryan Smith (Oct 07 2018 at 05:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135336887):
I've been trying to get it working with elan on windows and this is not going well. I installed msys32 and elan, but when I try to run the package manager from the windows cmd line with leanpkg -v I get 

'Smith\.elan\toolchains\stable\bin\..' is not recognized as an internal or external command,
operable program or batch file.

Seems like elan / msys32 / something doesn't understand spaces in windows filenames

#### [Ryan Smith (Oct 07 2018 at 05:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135336895):
I'm not fond of windows, but I do have to keep it on this computer for a reason.

#### [Bryan Gin-ge Chen (Oct 07 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135336949):
This is a known issue and unfortunately I don't think there's an easy solution.

#### [Ryan Smith (Oct 07 2018 at 05:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135336951):
Ok, if stuck on windows is there a better general approach then?

#### [Bryan Gin-ge Chen (Oct 07 2018 at 06:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135337050):
@**Chris Hughes** might know. You can see he ran into the same problem earlier in the thread, and I think he has a working setup by some other means.

#### [Johan Commelin (Oct 07 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135337919):
@**Ryan Smith** Looks like you have a space in your user name. This is known to break things.

#### [Ryan Smith (Oct 07 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135337920):
Yeah I do. Is there a way around?

#### [Johan Commelin (Oct 07 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135337929):
Dunno... haven't touched Windows in 15 years, and I don't use spaces in paths...

#### [Johan Commelin (Oct 07 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135337932):
But Chris got it working

#### [Johan Commelin (Oct 07 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135337935):
So to answer your question: Yes. There is a way around.

#### [Ryan Smith (Oct 07 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135337975):
It's a dreadful system, been about as long for me. Somehow I thought it would have gotten better while I was away. Is macOS at least better supported right now?

#### [Johan Commelin (Oct 07 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135337976):
How difficult is it to create a new user on Windows, and switch back and forth?

#### [Ryan Smith (Oct 07 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135337978):
That would be doable if that's really the only blocking issue sure

#### [Johan Commelin (Oct 07 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135337979):
What do you mean with "supported"? Support for Lean?

#### [Johan Commelin (Oct 07 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135337985):
Lean on Mac seems to work pretty good.

#### [Ryan Smith (Oct 07 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135337988):
Lean / elan since I was told things work better if you're using something to manage dependencies and stay up to date

#### [Johan Commelin (Oct 07 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135338037):
Elan on Mac is a very smooth experience nowadays

#### [Ryan Smith (Oct 07 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135338094):
Ok, cool. Will just switch off of my gf's computer and retry this on mac

#### [Johan Commelin (Oct 07 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135338100):
1 sec

#### [Johan Commelin (Oct 07 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135338102):
So, what you do:

#### [Johan Commelin (Oct 07 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135338105):
(1) Install VScode, (2) Install the Lean extension in VScode, (3) Open a Lean file.

#### [Johan Commelin (Oct 07 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135338145):
Afterwards, follow instructions, and it will install elan and lean for you

#### [Ryan Smith (Oct 07 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135338208):
opening a lean file in vscode w/ extension does seem to call lean. I don't see anything about elan.

#### [Ryan Smith (Oct 07 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135338210):
I'm a complete newbie trying to get a feel for how it works, so that's a good start if I can pull in mathlib

#### [Johan Commelin (Oct 07 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135338253):
It will only install elan/lean if it cannot find them

#### [Johan Commelin (Oct 07 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135338255):
Did you already have something installed?

#### [Ryan Smith (Oct 07 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135338267):
I installed via msys32, I assumed it was screwed up because invoking the package manager from the command line fails

#### [Johan Commelin (Oct 07 2018 at 06:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135338313):
Is this still on windows?

#### [Ryan Smith (Oct 07 2018 at 06:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135338316):
yeah, waited when you said you had a solution

#### [Johan Commelin (Oct 07 2018 at 06:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135338317):
aah, sorry

#### [Johan Commelin (Oct 07 2018 at 06:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135338318):
That was the mac solution

#### [Johan Commelin (Oct 07 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135338319):
sorry for the confusion

#### [Ryan Smith (Oct 07 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135338325):
ah cool, so the vscode extension installs everything else?

#### [Johan Commelin (Oct 07 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135338326):
I just wanted you to know it, before logging off

#### [Ryan Smith (Oct 07 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135338383):
thx for the help :)

#### [Kevin Buzzard (Oct 07 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135343067):
```quote
'Smith\.elan\toolchains\stable\bin\..' is not recognized as an internal or external command,
operable program or batch file.
```
`Smith` is half of your username, isn't it :-(

This is an issue with elan. Having a space in your username in Windows is a terrible idea; I know from personal experience that `elan` is not the only thing it breaks.

#### [Kevin Buzzard (Oct 07 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135343069):
Cheap Windows hack: https://xenaproject.wordpress.com/getting-lean-and-mathlib-running-in-the-mlc/

#### [Kevin Buzzard (Oct 07 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135343157):
I will update this blog page and turn it from old and out-of-date instructions on how to run Lean at Imperial to a clearly signposted hack for win10 in general.

#### [Kevin Buzzard (Oct 07 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135344535):
https://xenaproject.wordpress.com/a-cheap-hack-to-get-lean-and-mathlib-running-on-a-windows-10-machine/

#### [Kevin Buzzard (Oct 07 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135344586):
Summary: the correct elan method is causing problems for Windows 10 users with spaces in their file names. The link above *might* work better for them, and I'd be interested in feedback. @**Ryan Smith** if you still have not got things going, can you try this method?

#### [Scott Olson (Oct 07 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135345978):
I've narrowed down the elan problems with spaces to leanpkg, actually. I'm 95% sure this bat file is the culprit:  https://github.com/leanprover/lean/blob/master/bin/leanpkg.bat

The trouble comes with elan placing that in the homedir when the username has a space in it, but I believe it would also affect anyone who manually installed lean in any other path with a space in it.

#### [Scott Olson (Oct 07 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135345985):
Now I'm trying to teach myself just enough .bat language to figure out why...

#### [Mario Carneiro (Oct 07 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135346024):
not enough quotes?

#### [Scott Olson (Oct 07 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135346026):
Almost surely, I just have no idea how .bat quoting works yet

#### [Kenny Lau (Oct 07 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135346028):
Thanks @**Scott Olson**

#### [Mario Carneiro (Oct 07 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135346029):
I think the last line should be 
```
lean --run "%LIBDIR%\leanpkg\leanpkg\main.lean" %*
```

#### [Mario Carneiro (Oct 07 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135346038):
I wonder if this is considered urgent enough to patch core

#### [Kenny Lau (Oct 07 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135346039):
good luck getting those big guys patch it

#### [Scott Olson (Oct 07 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135346040):
The `IF NOT EXIST` command also causes an error to print out

#### [Kenny Lau (Oct 07 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135346044):
someone with much more threads than 4 can test if it works

#### [Scott Olson (Oct 07 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135346141):
Quoting the `--run` arg and writing `IF NOT EXIST "%LIBDIR%"` seems to be enough

#### [Kenny Lau (Oct 07 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135346198):
ok now then how to get the big guys to patch it

#### [Scott Olson (Oct 07 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135346206):
lol I just noticed the commit that added leanpkg.bat was by a personal friend of mine. Maybe I'll start by asking them?

#### [Mario Carneiro (Oct 07 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135346207):
If we can't patch core, the next best thing would be to store the patched file somewhere accessible from the tutorials "if you have problems with spaces, replace leanpkg.bat with this and try again"

#### [Mario Carneiro (Oct 07 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135346216):
Pretty sure Corey doesn't have any magic access any more than we do

#### [Kenny Lau (Oct 07 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135346256):
they'll say that this doesn't matter because half life 3 will soon be released

#### [Mario Carneiro (Oct 07 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135346258):
I see @**Gabriel Ebner** is lurking, maybe he has magic access?

#### [Kenny Lau (Oct 07 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135346261):
I mean, Lean 4

#### [Scott Olson (Oct 07 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135346279):
Either way I'll make a PR after I double-check that I'm doing quoting the best way

#### [Scott Olson (Oct 07 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135346296):
There's an open issue about it https://github.com/leanprover/lean/issues/1973

#### [Kevin Buzzard (Oct 07 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135346332):
I guess Sebastian Ullrich might consider patching it -- he is interested in making this sort of infrastructure work, and there's a fair chance that this problem will still be there in Lean 4.

#### [Kenny Lau (Oct 07 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135346441):
you mean Half Life 3

#### [Kevin Buzzard (Oct 07 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135346555):
Half life 3 --- 1/8'th life.

#### [Gabriel Ebner (Oct 07 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135346789):
I wouldn't count on a fix making it into a new Lean 3 release.  A more brutal solution would be to include a patch in elan or the vscode extension.  Given that Lean 3 is end-of-lifed, I'd accept a PR to the vscode extension that patches leanpkg.bat on windows.

#### [Scott Morrison (Oct 07 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135346870):
oh, that's a good idea

#### [Scott Olson (Oct 07 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135347481):
FYI I made the PR at https://github.com/leanprover/lean/pull/1976

#### [Ryan Smith (Oct 08 2018 at 03:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135374241):
@**Johan Commelin** Trying to install the lean plugin to vscode on macOS followed by opening a lean file does not install elan & lean, instead I just get file 'init' not found in the LEAN_PATH

#### [Bryan Gin-ge Chen (Oct 08 2018 at 03:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135374338):
@**Scott Morrison|110087** is the author of that installation feature. He should be able to help.

#### [Bryan Gin-ge Chen (Oct 08 2018 at 03:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135374631):
Are you possibly running into [this issue](https://github.com/leanprover/vscode-lean/issues/73) ? I think if you're getting that error you ought to have lean and elan on your system. Does `lean --version` in a console do anything?

#### [Ryan Smith (Oct 08 2018 at 04:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135374794):
Lean (version 3.4.1, commit 17fe3decaf8a, Release)
This time the plugin brought up an installation for elan, but when I'm trying to do a basic sanity check with Kevin's example of
import analysis.real
#check real
I'm not getting anything

#### [Bryan Gin-ge Chen (Oct 08 2018 at 04:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135374838):
Do you see orange bars on the side? If so, that means lean is busy processing the file and its imports.

#### [Ryan Smith (Oct 08 2018 at 04:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135374839):
I retract that: it took a very long time but it came back with \R! I think that means it's running and math lib import is ok?

#### [Bryan Gin-ge Chen (Oct 08 2018 at 04:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135374848):
Yes. To speed up this process in the future, you can run `lean --make` in your package directory.

#### [Ryan Smith (Oct 08 2018 at 04:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135374849):
Do you need to re run make if you edit your src files?

#### [Mario Carneiro (Oct 08 2018 at 04:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135374955):
vscode will automatically compile stuff in memory when you make edits, but they aren't saved when you quit

#### [Bryan Gin-ge Chen (Oct 08 2018 at 04:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135375255):
Running `lean --make` generates `.olean` files, which are object files that lean generates when it compiles the `.lean` source files.  If you have lots of files that import each other then doing this lets the lean server in the VS code extension avoid re-compiling all of your imports when it starts up.

So if you're just editing small files that import only from mathlib, running `lean --make` again won't really be necessary. If you do want to run it, then as long as you haven't made changes to your package's copy of mathlib (e.g. by upgrading) or otherwise written / edited lots of files that you need to import, running `lean --make` after the first time will be much faster since it tries not to recompile files whose dependencies haven't changed.

#### [Ryan Smith (Oct 08 2018 at 04:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135375349):
Great, thanks

#### [Scott Morrison (Oct 08 2018 at 06:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135378646):
```quote
@**Johan Commelin** Trying to install the lean plugin to vscode on macOS followed by opening a lean file does not install elan & lean, instead I just get file 'init' not found in the LEAN_PATH
```
Hi @**Ryan Smith**, I'd like to understand what happened here. Did you have `LEAN_PATH` set already? That's likely to cause problems. It sounds like a moment later the plugin did work, and installed elan for you.

#### [Neil Strickland (Oct 12 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135675488):
I am sorry to rant, but these complaints about spaces in user names are silly.

Allowing spaces in user names is a completely ordinary, benign design decision.  It creates a need to escape strings in certain circumstances, but that is again a completely ordinary issue, which arises all over the place in software development in many different contexts.  There are many, many thousands of programs that handle Windows paths correctly, and it does not take any magic to write them.  If a certain program is broken by spaces in path names, that just means that the developers did not take the straightforward and standard steps necessary to avoid that problem.

#### [Johan Commelin (Oct 12 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135677340):
@**Neil Strickland** I agree that it is not very user friendly. There have been efforts to figure out what is wrong, and people are trying to patch it up.

#### [Gabriel Ebner (Oct 12 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135677718):
I feel like the last line was partly directed at me, so let me respond.  Neither Leo, Sebastian, or me are using windows.  I am sorry but I don't think any of us are aware of the "straightforward and standard steps" in windows cmd.exe programming.  The windows-specific parts of the code base are in general less well tested.  Now is probably not the ideal time, but in general feel free to submit fixes for these platform-specific bugs.

#### [Reid Barton (Oct 12 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135681803):
This is a common problem for open-source projects: there are many fewer developers using Windows than Linux or OS X and Windows is fundamentally unfamiliar to users of Unix-type systems. The result is usually that Windows is not as well supported as it could be. We have this problem with the Haskell compiler (GHC) as well--we've recently got one (volunteer) developer who actually understands Windows who's got a ~20 year backlog of Windows-specific issues to work through, including stuff like the interpreter not crashing when it tries to print Unicode characters to the console. And GHC is a project with a far larger user and developer base than Lean. (It also happens to be another project whose primary developer is at MSR.)

#### [Reid Barton (Oct 12 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135682122):
That said, the Unix-y equivalent of `leanpkg.bat` is also missing quotes in the same place. I guess nobody has spaces in their usernames on Unix-y systems :upside_down:

#### [Neil Strickland (Oct 12 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135682156):
@**Gabriel Ebner** Thanks for the response.  I think that the only cmd.exe related problem is probably resolved by Reid Barton's recent fix to leanpkg.bat.  However, there are other issues caused by passing unescaped strings to CreateProcess() in src/library/process.cpp via exec_cmd and io.proc.spawn, and by using external processes to make or detect directories instead of calling CreateDirectory() and PathFileExists().  That is surely not the recommended approach even in POSIX systems.  If I had an appropriate build environment then I would attempt to fix this myself, but I do not know how hard it would be to set that up.

#### [Johan Commelin (Oct 12 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135682261):
```quote
That said, the Unix-y equivalent of `leanpkg.bat` is also missing quotes in the same place. I guess nobody has spaces in their usernames on Unix-y systems :upside_down:
```
Right. When you live in the shell, you quickly learn to use sane paths.

#### [Reid Barton (Oct 12 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135682274):
(Not my fix, but @**Scott Olson**'s)

#### [Reid Barton (Oct 12 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135683015):
```quote
However, there are other issues caused by passing unescaped strings to CreateProcess() in src/library/process.cpp via exec_cmd and io.proc.spawn, and by using external processes to make or detect directories instead of calling CreateDirectory() and PathFileExists().  That is surely not the recommended approach even in POSIX systems.
```
I think @**Keeley Hoek** has a fork which fixes some issues like this for Windows.

#### [Reid Barton (Oct 12 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135684027):
I didn't realize that Windows doesn't have an equivalent of the command-line argument list. I guess I knew that DOS worked that way...

#### [Scott Olson (Oct 12 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135684178):
heh, yeah, I just learned that the other day when I went diving into elan's code and the Rust standard library to figure out how process creation worked on Windows

