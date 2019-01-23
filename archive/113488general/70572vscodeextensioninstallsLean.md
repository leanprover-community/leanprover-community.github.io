---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/70572vscodeextensioninstallsLean.html
---

## Stream: [general](index.html)
### Topic: [vscode extension installs Lean](70572vscodeextensioninstallsLean.html)

---

#### [Scott Morrison (Sep 17 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134097115):
I just sent a PR for the VS Code extension, that will offer to install Lean for you if it can't find a working copy. It uses elan, and just runs in the VS Code terminal.

#### [Scott Morrison (Sep 17 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134097116):
I've tested it on OS X, and it seems to work quite nicely.

#### [Scott Morrison (Sep 17 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134097206):
[Screenshot-2018-09-17-22.22.30.png](/user_uploads/3121/01B1ajUPuC1GwOdpvxRT8ICA/Screenshot-2018-09-17-22.22.30.png) [Screenshot-2018-09-17-22.22.36.png](/user_uploads/3121/q5CFFm23QgagbkHTuf1xiXTa/Screenshot-2018-09-17-22.22.36.png)

#### [Scott Morrison (Sep 17 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134097212):
It automatically restarts the extension afterwards, so in good cases the whole Lean installation process could now be:

#### [Scott Morrison (Sep 17 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134097216):
1) Install the VS Code extension

#### [Scott Morrison (Sep 17 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134097218):
2) Open a Lean file

#### [Scott Morrison (Sep 17 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134097262):
3) Click "Install Lean using elan" in the error box that complains you don't have Lean.

#### [Scott Morrison (Sep 17 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134097270):
However I haven't tested this on Linux or Windows.

#### [Scott Morrison (Sep 17 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134097279):
and I haven't thought hard about further diagnostics if something goes wrong (e.g. dependencies are unavailable).

#### [Scott Morrison (Sep 17 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134097303):
If anyone feels up to trying out the PR version of the extension on Linux or Windows, please do!

#### [Scott Morrison (Sep 17 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134097356):
Let me know if you need help --- running a vscode extension from source is delightfully easy.

#### [Scott Morrison (Sep 17 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134097585):
Somewhat depressingly, the reason I did this was because this morning I realised just how badly my email inbox needed love and attention, and so I deleted Lean until I'd made some progress :-).

#### [Scott Morrison (Sep 17 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134097589):
Sitting down after dinner tonight, my first thought was "huh, a nice opportunity to try making installation easier".

#### [Scott Morrison (Sep 17 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134097652):
(For anyone keeping track, a tenure letter got written, and files for scholarship applications for a number of international PhD students got written, but my inbox is still unhappy...)

#### [Scott Morrison (Sep 17 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134097932):
and for my own future reference, to make this work on Windows we'll have to ask VS Code to run elan in some sort of bash terminal, per instructions at <https://stackoverflow.com/questions/42606837/how-to-use-bash-on-windows-from-visual-studio-code-integrated-terminal>. It seems plausible that this could work for a bash terminal provided by any of git bash, linux subsystem for windows, or msys2, but I have no experience with these and I'm unsure whether VS Code would actually be able to find the installation elan created.

#### [Sebastian Ullrich (Sep 17 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134110039):
This looks nice! Though I suspect it only worked for you because you already had `~/.elan/bin` in your PATH - the PATH value of the VS Code process will not change when installing elan. What you could do is to just default to `~/.elan/bin/lean` as the `executablePath` if that file exists

#### [Sebastian Ullrich (Sep 17 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134110850):
I'm not sure I like the installation being completely hidden from the user

#### [Johan Commelin (Sep 17 2018 at 19:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134114453):
```quote
I'm not sure I like the installation being completely hidden from the user
```
I'm quite sure that there a lot of users that *do* like it.

#### [Scott Morrison (Sep 17 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134123194):
Good point about the PATH! :-) I'll investigate that later.

#### [Scott Morrison (Sep 17 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134123274):
The compromise I was going for was minimising the number of interactions required during installation, while still showing on the screen what was going on --- so it gives focus to the terminal window doing the work, but doesn't require any interaction inside that terminal window.

#### [Scott Morrison (Sep 17 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134123342):
A pretty reasonable alternative would be to require the user answers the one question that elan asks by default. (Perhaps maximising the terminal window first, so it's obvious to them they need to look at that window?) I could also add a "press any key to continue" prompt at the end, so they can see the end of the output from elan before the terminal window disappears and the extension starts.

#### [Sebastian Ullrich (Sep 17 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134125033):
Yeah, I was imagining something like that prompt. They may also want to at least decide between stable and nightly Lean - not that it matters much right now, or that the installer makes that particularly simple

#### [Scott Morrison (Sep 18 2018 at 07:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134146769):
I don't really understand why there is a choice to be made between stable and nightly Lean. Isn't elan deciding for itself on a per-project basis which version of Lean to give you anyway?

#### [Johan Commelin (Sep 18 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134148759):
Scott, in your current workflow, where is the user supposed to make the decision about the project? We don't want them to manually touch a `.toml` etc...

#### [Johan Commelin (Sep 18 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134148804):
I mean, if it is a Lean file in an existing project, sure... then those choices have already been made by someone else. But if it is a new Lean file in an empty directory...

#### [Scott Morrison (Sep 18 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134149513):
When you type `leanpkg init`, how is the Lean version decided? Whatever is the logic there should be the default everywhere.

#### [Sebastian Ullrich (Sep 18 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134193652):
@**Scott Morrison** It's the default Lean version according to `elan toolchain list`. Which is exactly what you can customize in the installer :)

#### [Sebastian Ullrich (Sep 18 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134193839):
Of course, if we're already integrating elan into editors, we may as well have a dialog for creating a new Lean package with a Lean version chooser. Not sure what to do about stand-alone files, though we may want to de-emphasize their use anyway (e.g. it may not be posible in Lean 4 to import a stand-alone file from another one)

#### [Scott Morrison (Sep 19 2018 at 03:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134203981):
I think we should mostly decide that all new users who don't know better want the tools to provide them with `stable` as effortlessly as possible.

#### [Scott Morrison (Sep 19 2018 at 03:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134203991):
When they start looking at other peoples' projects, as long as they got started with `elan`, those projects will magically use `nightly-XXX` as desired.

#### [Scott Morrison (Sep 19 2018 at 03:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134204035):
And once they realise they need `nightly-XXX` for their own projects, they can edit a `leanpkg.toml` file themselves.

#### [Scott Morrison (Sep 19 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134215745):
Hi @**Sebastian Ullrich**, how would you feel about having `elan` try to install missing dependencies. Something as simple as:

#### [Scott Morrison (Sep 19 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134215794):
````
if ubuntu then
  sudo apt-get install git libgmp-dev cmake
else if osx then
  brew install cmake
  brew install gmp
````

#### [Scott Morrison (Sep 19 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134215800):
would get most non-windows users going a bit faster

#### [Scott Morrison (Sep 19 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134215809):
heck, in the osx branch add
```
xcode-select --install
brew --version || /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

#### [Scott Morrison (Sep 19 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134215878):
I'd be happy to make the PR, if something like this could be accepted.

#### [Scott Morrison (Sep 19 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134215897):
The combination of VS Code giving a button to run elan, and elan attempting to fill in missing dependencies, could be very helpful.

#### [Sean Leather (Sep 19 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134215986):
I don't mean to be difficult, but I think that's a really bad idea to have `elan` run `apt-get` or `brew`.

#### [Scott Morrison (Sep 19 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134215993):
Why is that?

#### [Sean Leather (Sep 19 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134215999):
Who knows what state the user's computer is in?

#### [Scott Morrison (Sep 19 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216000):
(I am ignorant here)

#### [Sean Leather (Sep 19 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216010):
You could and probably will break something.

#### [Kevin Buzzard (Sep 19 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216016):
I guess an alternative is to fail and say "hey, you might want to type `apt install gmp`" or some such

#### [Scott Morrison (Sep 19 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216017):
Ok!

#### [Sean Leather (Sep 19 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216020):
Sure, that's a good option.

#### [Scott Morrison (Sep 19 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216059):
Ok --- maybe I will continue tweaking the VS Code extension

#### [Mario Carneiro (Sep 19 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216060):
I don't really see how an apt-get command like that will break anything, at worst it will fail

#### [Scott Morrison (Sep 19 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216063):
It is easy enough for it to analyze the error messages and tell you what to run.

#### [Scott Morrison (Sep 19 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216079):
I feel like for 99% of users that apt-get or brew command is going to be the right thing to do, and moreover for 90% of users they won't even know what it means when they run it. :-)

#### [Sean Leather (Sep 19 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216082):
Even if it wouldn't break anything, it's a bad idea to install software without the user having control over it. And if the user doesn't know what it's doing, that's even worse.

#### [Scott Morrison (Sep 19 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216089):
Ok -- I will go with dialogs that provide hints.

#### [Mario Carneiro (Sep 19 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216091):
don't package managers themselves do this routinely?

#### [Mario Carneiro (Sep 19 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216136):
the user has control over the large scale execution, that is sufficient

#### [Mario Carneiro (Sep 19 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216170):
I think it should ask the same questions you normally see in an installer, but otherwise go about its business completely automatically

#### [Mario Carneiro (Sep 19 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216182):
complicated questions will just cause confusion, a power user doesn't need to use this method at all

#### [Scott Morrison (Sep 19 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216229):
e.g. `elan` could show a prompt: "It looks like you don't have libgmp installed. Would you like to install this using `brew install libgmp`?"

#### [Sean Leather (Sep 19 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216249):
```quote
e.g. `elan` could show a prompt: "It looks like you don't have libgmp installed. Would you like to install this using `brew install libgmp`?"
```
In order to do that, you need to know if `brew` is installed.

#### [Scott Morrison (Sep 19 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216260):
Of course

#### [Scott Morrison (Sep 19 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216265):
but detecting the operating system is easy

#### [Sean Leather (Sep 19 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216267):
And `brew` in the `$PATH` may not be the `brew` you expect, so you'd have to test for the right `brew`.

#### [Scott Morrison (Sep 19 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216288):
and running `brew --version` is harmless, surely?

#### [Sean Leather (Sep 19 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216330):
Maybe. But I'd still recommend giving the commands to the user and explaining it rather than doing it for them.

#### [Scott Morrison (Sep 19 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216334):
I mean, if someone has contrived to put an evil or nonfunctional brew on the $PATH, surely they can't be upset if an installer doesn't work as expected?

#### [Scott Morrison (Sep 19 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216374):
Having tried to clean up several broken attempts by mathematicians and students to install Lean by now, I would really like to take this stuff out of their hands :-)

#### [Scott Morrison (Sep 19 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216434):
I agree that power users don't want this!

#### [Scott Morrison (Sep 19 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216477):
If we're going to attempt something like this, it seems more sensible to me to put all the login in `elan`, and then have the VS Code extension just call `elan`.

#### [Mario Carneiro (Sep 19 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216480):
> Maybe. But I'd still recommend giving the commands to the user and explaining it rather than doing it for them.

No no, this is the source of too many problems

#### [Sean Leather (Sep 19 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216485):
You're welcome to do what you like, but, from past experience, I know that it's a bad idea. I can't tell you exactly what will go wrong, because things change and systems are complex, but I'm pretty sure something will go wrong.

#### [Scott Morrison (Sep 19 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216528):
Seeing what someone at Dagstuhl had managed to do with their windows path was pretty terrifying. :-)

#### [Mario Carneiro (Sep 19 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216538):
We already have a command sequence in a help file, it doesn't work half the time and the poor users don't know what to do

#### [Scott Morrison (Sep 19 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216546):
What if we instead put all the login in the VS Code, and

#### [Scott Morrison (Sep 19 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216547):
when something goes wrong

#### [Johan Commelin (Sep 19 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216559):
Talking about automatically fixing problems: If we detect windows, can't we just wipe it with a fresh Linux install?

#### [Sean Leather (Sep 19 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216560):
For Windows, an installer would be best. For Linux, a package would be best. For Mac, Homebrew would probably be best.

#### [Kevin Buzzard (Sep 19 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216562):
Ha ha there was a user over the summer whose Windows path rather eerily contained a bunch of directories on my laptop (`/home/buzzard/Lean/whatever`).

#### [Scott Morrison (Sep 19 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216566):
show a dialog that says "XXX not found. You may want to try running `YYY` in a terminal"

#### [Kevin Buzzard (Sep 19 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216568):
I just said "I think you can safely remove all those, they're on another system"

#### [Mario Carneiro (Sep 19 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216570):
"what's a terminal?"

#### [Scott Morrison (Sep 19 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216571):
:-)

#### [Scott Morrison (Sep 19 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216615):
A nice trick, because VS Code has an integrated terminal, is that we can actually pop up a terminal window

#### [Mario Carneiro (Sep 19 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216616):
or worse - "I installed cygwin (on linux) but it couldn't find the path"

#### [Scott Morrison (Sep 19 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216617):
and paste in the command the user needs

#### [Sean Leather (Sep 19 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216624):
BTW, there's a package manager for Windows: https://chocolatey.org/

#### [Scott Morrison (Sep 19 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216625):
leaving them to just press "enter"?

#### [Scott Morrison (Sep 19 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216647):
Does `elan` currently do anything useful on windows? I have no idea.

#### [Kevin Buzzard (Sep 19 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216651):
I also noticed that some users, when you say "oh hold down shift", say "what's shift?" because a modern keyboard might well not have the word "shift" on it any more. Similarly for "enter" / "return".

#### [Mario Carneiro (Sep 19 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216696):
why not run a command that prints out the sequence of brew/whatever commands it will send, and says (y/n)

#### [Sean Leather (Sep 19 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216702):
Also, if you're going to do `apt-get` and/or `brew`, you'll want to update those first.

#### [Scott Morrison (Sep 19 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216718):
I'm pretty sure `brew` auto-updates these days.

#### [Sean Leather (Sep 19 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216765):
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

And this is notoriously not secure.

#### [Scott Morrison (Sep 19 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216767):
Note our install instructions for elan are already of this form!

#### [Sean Leather (Sep 19 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216773):
I haven't seen them, but it's still true. :slight_smile:

#### [Mario Carneiro (Sep 19 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216940):
I'm not sure how you can in one line download and run a script from the internet without it being insecure

#### [Mario Carneiro (Sep 19 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216945):
that's like the definition of insecure

#### [Sean Leather (Sep 19 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134217148):
In the end, it comes down to trust. https://brew.sh/ also suggests that command. I don't like it, but that's the way it is. In general, I would point to https://brew.sh when informing somebody to install `brew`. That way, they can read the information and become informed about what it is before installing it. Yes, one could decide to ignore the information, but at least they've been given the opportunity.

#### [Sebastian Ullrich (Sep 19 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134240599):
Why do users need `cmake`...?

#### [Sebastian Ullrich (Sep 19 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134240757):
That `libgmp` isn't included is basically a bug; I think it was at some point. Anyway, calling `sudo` may reasonably ask for a password, so the automatic installation should be in an interactive shell at the very least

#### [Reid Barton (Sep 19 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134241429):
I didn't have to install cmake, but I did have to install coreutils for leanpkg. This was on a machine with no preinstalled brew on which I didn't have root access. brew says it can be installed anywhere but some packages may not be happy in nonstandard locations; I didn't have any difficulties though.

#### [Reid Barton (Sep 19 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134241551):
Vscode could even install its own private brew installation

#### [Reid Barton (Sep 19 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134241669):
Maybe it was elan not leanpkg that needed readlink, I think it was

#### [Scott Morrison (Sep 24 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134516578):
I just updated my PR to vscode-lean, so hopefully after the VS Code Lean extension offers to install `elan` for you, it works first time (even though the $PATH has not yet been updated).

#### [Scott Morrison (Sep 24 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134516589):
Testing on other systems much appreciated.

#### [Scott Morrison (Sep 24 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134516595):
I've gone back to the more conservative model of not pressing enter for the user during the `elan` script. :-)

#### [Scott Morrison (Sep 24 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134516598):
Next up: testing this in Linux and Windows

#### [Scott Morrison (Sep 24 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134516607):
after that, seeing if we can make `elan` more helpful when dependencies are missing.

#### [Scott Morrison (Sep 24 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134516615):
https://github.com/leanprover/vscode-lean/pull/91

