---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/19038Installationquestions.html
---

## Stream: [new members](index.html)
### Topic: [Installation questions](19038Installationquestions.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 06 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135290991):
Here's a new thread for installation questions.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 06 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135290998):
@**Charles Rezk** What system are you using, e.g. windows, mac, linux? There's some basic advice by Kevin Buzzard [here](https://xenaproject.wordpress.com/2017/12/02/how-to-install-mathlib-and-keep-it-up-to-date/).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Charles Rezk (Oct 06 2018 at 02:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291011):
Linux.  Yes I'm trying to follow the instructions on that page.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Charles Rezk (Oct 06 2018 at 02:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291012):
I've compiled lean.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Charles Rezk (Oct 06 2018 at 02:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291013):
I've added the mathlib package.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Charles Rezk (Oct 06 2018 at 02:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291014):
I've installed the vscode thing.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Charles Rezk (Oct 06 2018 at 02:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291017):
I've started it up, and tried to run an example.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Charles Rezk (Oct 06 2018 at 02:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291067):
For some reason it strangely does not find the lean executable.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 06 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291073):
Are you able to run lean from the terminal?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 06 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291081):
I guess so, if you were able to add mathlib with leanpkg.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Charles Rezk (Oct 06 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291082):
I can do "lean --version"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Charles Rezk (Oct 06 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291086):
When vscode tries to run the lean executable, it for some reason puts in an extra comma

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 06 2018 at 02:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291144):
I guess you're seeing an error message somewhere. What does it say exactly?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Charles Rezk (Oct 06 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291211):
Lean: Error: Command failed: /home/rezk/git/lean/bin/lean, --version
/bin/sh: /home/rezk/git/lean/bin/lean,: No such file or directory

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Charles Rezk (Oct 06 2018 at 02:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291227):
I don't know why there is an extra comma in there, but that is presumably why it is failing

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 06 2018 at 02:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291271):
Could you check your VS code settings? Under "Extensions > Lean configuration" there should be a box that says "Executable path"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 06 2018 at 02:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291273):
If there's not an extra comma in there then I'm stumped.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Charles Rezk (Oct 06 2018 at 02:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291283):
How do I find this box?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Charles Rezk (Oct 06 2018 at 02:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291286):
I have been trying to set the executable path in "User Settings", according to the instructions, but that seems to have literally no effect.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 06 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291331):
Did you edit your settings.json file to add the "lean.executablePath" option as in Kevin's instructions? Maybe there's a misplaced quote there.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Charles Rezk (Oct 06 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291385):
Yes I have tried that, assuming I am doing it correctly.  As far as I can tell, it complety ignores what I put there.  I can give a giberish path, and I still get the exact same error message I gave you above.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 06 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291390):
Ctrl + comma might take you to preferences

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Charles Rezk (Oct 06 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291391):
Some how it is getting an incorrect path from somewhere else

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 06 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291401):
Or something like file -> settings -> preferences

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 06 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291404):
Do you want to copy-paste your "settings.json" file here?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 06 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291522):
@**Charles Rezk**, did you at any point set the environment variable `LEAN_PATH`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Charles Rezk (Oct 06 2018 at 02:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291532):
No, there is no $LEAN_PATH

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 06 2018 at 02:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291535):
Could you show your settings.json file?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Charles Rezk (Oct 06 2018 at 02:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291536):
From what it says in USer Settings, the settings.json file is:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Charles Rezk (Oct 06 2018 at 02:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291537):
{ "lean.executablePath": "/home/rezk/git/lean/bin/lean"
}

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Charles Rezk (Oct 06 2018 at 02:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291580):
I don't know where this file is actually kept

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 06 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291585):
On linux it's apparently $HOME/.config/Code/User/settings.json

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 06 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291594):
Here's another suggestion:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 06 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291595):
the best way to install Lean is actually to use `elan`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 06 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291600):
from <https://github.com/Kha/elan>

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Charles Rezk (Oct 06 2018 at 02:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291640):
I've been doing this for several hours.  I'm not starting again.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 06 2018 at 02:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291642):
e.g. just by running `curl https://raw.githubusercontent.com/Kha/elan/master/elan-init.sh -sSf | sh` in a terminal

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 06 2018 at 02:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291643):
Ok :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 06 2018 at 02:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291645):
(My experience is that installing Lean via elan takes less than a minute. :-)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 06 2018 at 02:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291652):
In particular, you won't have to rebuild lean from source that way.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Charles Rezk (Oct 06 2018 at 02:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291667):
OK, that explains it.  The actually "settings.json" file is different than what vscode is showing me

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 06 2018 at 02:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291674):
(The advantage is that you don't have to compile anything, you don't have to set any paths in VS Code, and elan will automatically switch between Lean versions if you have different projects requiring different versions.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 06 2018 at 02:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291738):
The installation process will hopefully be a lot, lot easier once Scott's PR to the VS code extension is merged.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Charles Rezk (Oct 06 2018 at 02:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291739):
I restarted vscode, and now it shows the actually physical file in "Settings", and also I don't get that error any more when I try to "Restart: Lean"

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Charles Rezk (Oct 06 2018 at 02:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291783):
Now nothing happens when I do that, which doesn't seem like an improvement

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 06 2018 at 02:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291795):
"Nothing happening" might be the right thing! Lean doesn't say anything upon a successful start up, until you actually enter something in a `.lean` file.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 06 2018 at 03:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291815):
Can you save a file, e.g. as `test.lean`, and enter something in it, such as `#eval 2+2`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 06 2018 at 03:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291846):
You should then get a green squiggle under it, and hovering the mouse there should show `4`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Charles Rezk (Oct 06 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291964):
I have tried that.   Nothing happens, no green squiggle

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Charles Rezk (Oct 06 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291979):
Wait, now it is.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Charles Rezk (Oct 06 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291981):
Maybe it works now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135292049):
If you see orange bars on the sidebar that means it's in progress and you should wait

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135292054):
you can also see status information on the bottom left which will tell you if lean is dead or just busy

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Charles Rezk (Oct 06 2018 at 03:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135292091):
I think it's working now

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 03:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135292101):
You should test mathlib imports if you intend to use it, e.g. `import data.nat.prime`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Charles Rezk (Oct 06 2018 at 03:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135292237):
OK

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Charles Rezk (Oct 06 2018 at 03:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135292399):
I think this computer is going to be too slow for this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 03:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135292441):
you may need to compile the lean sources if everything is running slow

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Oct 06 2018 at 03:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135292443):
i.e. run `lean --make` in the library directoy

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Charles Rezk (Oct 06 2018 at 03:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135292460):
What is the library directory?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 06 2018 at 03:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135292568):
The mathlib you added to your package should be in `_target/deps/mathlib` relative to the package root; running `lean --make` in that directory should make importing mathlib much faster.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 06 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135294984):
Hi @**Bryan Gin-ge Chen** , just correcting that suggestion: in general it is safer to run `lean —make _target/deps/mathlib` from the main project directory, rather than changing into that subdirectory and running `lean —make`. If there is a version mismatch between the project and mathlib, running lean in the subdirectory will just give you olean files that won’t be usable.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 06 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135294987):
(If there’s no version mismatch, there’s no problem, but we seem to have regular problems with this.)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Oct 06 2018 at 04:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135295039):
Thanks! That's good to know.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Oct 06 2018 at 04:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135295190):
Perhaps we should add a command in VS Code “compile all dependencies in background” to help people with this.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 09 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135482171):
@**Charles Rezk** Did you get the install working in the end?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Charles Rezk (Oct 09 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135483148):
I did.  I'm not really sure how do actually do anything interesting, the mathlib files are hard for me to interpret.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Oct 09 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135483437):
Pick a project, get stuck, ask here, people will try to help :-) At least that's how I did it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 09 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135483546):
@**Charles Rezk** I suggest you write a short post in https://leanprover.zulipchat.com/#narrow/stream/113489-new-members/subject/Introductions.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 09 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135483550):
Tell us where you are based and what kind of stuff you like.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johan Commelin (Oct 09 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135483559):
And like Kevin said, just hang around and ask questions.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Wojciech Nawrocki (Jan 15 2019 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/155128486):
Is it normal for compilation of `mathlib` `master` to fail miserably on `nightly` Lean? I made a package with `leanpkg +nightly new`, then added `mathlib` and `lean --make _target/deps/mathlib/` shows errors on everything, e.g. `relator.lean:13:43: error: unknown identifier 'left_unique'`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 15 2019 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/155128643):
We use 3.4.1 Lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Jan 15 2019 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/155129521):
see also https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib.20is.20broken

