---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/56578VScodeextension.html
---

## [general](index.html)
### [VScode extension](56578VScodeextension.html)

#### [Patrick Massot (Jul 25 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130267754):
@**Gabriel Ebner** could we get two variants of F12, one creating a new tab if a new file needs to be opened, and one replacing the content of the current tab, as it currently does? Also, could we get key bindings for "Go back" and "Restart Lean"? And maybe one for "Create a comment below the current line, containing what is currently in the Lean messages view"? About Lean messages, each time I press Ctrl+Shift+Enter to open this tab, it also opens a copy of the file I'm currently editing. It's annoying and I think it wasn't like this before.

#### [Mario Carneiro (Jul 25 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130267806):
alt-left should be a key binding for "go back"

#### [Patrick Massot (Jul 25 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130267825):
Not here

#### [Mario Carneiro (Jul 25 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130267829):
I also noticed the bug with ctrl-shift-enter opening a copy over the message view

#### [Mario Carneiro (Jul 25 2018 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130267870):
You can set your key bindings yourself btw

#### [Patrick Massot (Jul 25 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130267890):
It makes me think I would really love to know a way to ask VScode to trigger translation immediately rather than waiting for a blank space of movement. It would really help to type words containing several special unicode characters.

#### [Patrick Massot (Jul 25 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130267893):
How do you setup keybindings?

#### [Mario Carneiro (Jul 25 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130267947):
file > prefs > key shortcuts

#### [Johan Commelin (Jul 25 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130267956):
```quote
It makes me think I would really love to know a way to ask VScode to trigger translation immediately rather than waiting for a blank space of movement. It would really help to type words containing several special unicode characters.
```
But how would you deal with prefixes? Such as `\t` vs `\to`?

#### [Mario Carneiro (Jul 25 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130267959):
this is what emacs does

#### [Mario Carneiro (Jul 25 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130268004):
I think if you type `\t` you get the triangle but underlined, and typing `o` changes it to an arrow

#### [Patrick Massot (Jul 25 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130268013):
I don't need it to be automatic, I want to be able to *ask* for it before VScode decides it should do it anyway

#### [Johan Commelin (Jul 25 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130268026):
Sweet. So if I would type `\Zp` would that give me ℤp?

#### [Mario Carneiro (Jul 25 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130268033):
I believe so

#### [Johan Commelin (Jul 25 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130268035):
Nice

#### [Mario Carneiro (Jul 25 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130268039):
I think vscode does the same in that case

#### [Johan Commelin (Jul 25 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130268041):
Hmm, maybe it does.

#### [Gabriel Ebner (Jul 25 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130268044):
> could we get two variants of F12,

~~ctrl+k f12~~ the default keybinding does not work here

But you can assign "open definition to the side" to whatever keybinding you like.

#### [Johan Commelin (Jul 25 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130268089):
```quote
I think vscode does the same in that case
```
You are right.

#### [Mario Carneiro (Jul 25 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130268170):
> could we get two variants of F12, one creating a new tab if a new file needs to be opened, and one replacing the content of the current tab, as it currently does? 

Currently F12 and other navigation commands only replace the content of the current tab if you are viewing a file in temporary mode, indicated with italics in the tab title

#### [Mario Carneiro (Jul 25 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130268182):
you can clear temporary mode by clicking on the title or editing anywhere

#### [Gabriel Ebner (Jul 25 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130268183):
```quote
"Go back"
```

ctrl+alt+- is the default keybinding.  I usually use the vim keybindings, where it is ctrl+t as expected.

#### [Patrick Massot (Jul 25 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130268234):
Thanks for pointing out "open definition to the side". But it opens in the area containing Lean messages :(

#### [Gabriel Ebner (Jul 25 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130268256):
```quote
 Ctrl+Shift+Enter to open this tab, it also opens a copy of the file I'm currently editing
```

Oh, that seems to be a new bug with vscode 1.25.  https://github.com/leanprover/vscode-lean/issues/77

#### [Gabriel Ebner (Jul 25 2018 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130268312):
```quote
Thanks for pointing out "open definition to the side". But it opens in the area containing Lean messages :(
```
You can split the editor first with ctrl+\

#### [Patrick Massot (Jul 25 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130268376):
Thanks, but this creates a whole new zone, not a new tab in the current group

#### [Patrick Massot (Jul 25 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130268378):
Oh, that italic filename is a really subtle clue. I never noticed it

#### [Patrick Massot (Jul 25 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130268385):
It's lunchtime, but I'm happy I've learned a lot of VScode tricks

#### [Gabriel Ebner (Jul 25 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130272111):
```quote
Create a comment below the current line, containing what is currently in the Lean messages view
```
https://github.com/leanprover/vscode-lean/commit/d3ae4b1a1108cb0eb1cefc645b6602a307b4d4be

I'm currently having a bit of trouble publishing the vscode extension, so you'll have to wait a bit for the update.

#### [Patrick Massot (Jul 25 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130278254):
Thanks! Hopefully this example could serve as a pattern for other stuff like that (I have nothing specific in mind).

#### [Gabriel Ebner (Jul 27 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130433110):
I just pushed the update.  Please tell me if I broke anything.

#### [Gabriel Ebner (Jul 27 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130433115):
afk hornet in the room

#### [Gabriel Ebner (Jul 27 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130435463):
I managed to escape.  The only new feature is "ctrl+shift+p copy contents to comment", which copies the current content of the info view to a comment below the current line, as requested by @**Patrick Massot**.

#### [Chris Hughes (Jul 27 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130435618):
One slightly annoying new feature of VSCode, is that when I click "Display Goal", it opens the file I have open in the right pane. Is there a way to do anything about that?

#### [Simon Hudon (Jul 27 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130435636):
I've added a feature in emacs (taken from `company-coq`) to use `diff` to compare the actual / expected types in error messages. Any chance I might convince you to add it to VS code or help me implement it for VS code?

#### [Gabriel Ebner (Jul 28 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130455350):
> it opens the file I have open in the right pane

This bug should be fixed with yesterday's update.

#### [Gabriel Ebner (Jul 28 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130455926):
```quote
[..] use `diff` to compare the actual / expected types in error messages. Any chance I might convince you to add it to VS code or help me implement it for VS code?
```

Sure, I am happy about new features.  How did you extract the expected/actual type from the error message?  Regex?

If you want to implement it yourself, look at how `_lean.revealPosition` is implemented in the info view (this handles the click on the message title and scrolls to the corresponding position in the file): https://github.com/leanprover/vscode-lean/blob/b872639347221a0146bf4e98234ee55e3d634b30/src/infoview.ts#L375
I think we can add a link to the diff right next to it.  You can show the diff with `workspace.openTextDocument` and `window.showTextDocument`.  Feel free to add a diff library to the dependencies.

#### [Chris Hughes (Jul 28 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130459741):
I tried installing the lean VScode update, and now opening VScode instantly freezes my computer. Anyone else experiencing this problem?

#### [Kevin Buzzard (Jul 28 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130459799):
If I find the extension in VS code I am only offered "disable" and "uninstall". I seem to be on version 0.11.11 (and on Ubuntu)

#### [Kevin Buzzard (Jul 28 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130460257):
I have extension auto-update on. Which version of the extension are you having problems with? You're talking about a Windows machine right?

#### [Kevin Buzzard (Jul 28 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130460304):
More to the point -- the bug is fixed for me and I have no problems with the extension. So I guess I upgraded safely. Anyone on Windows having the same problems with...Chris? Are you on 0.11.11? Oh -- you can't even tell?

#### [Chris Hughes (Jul 28 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130460321):
I'm using the latest version of the extension and 20th April nightly for lean.

#### [Chris Hughes (Jul 28 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130460364):
Maybe I should update lean?

#### [Ali Sever (Jul 28 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130460365):
I reloaded lean, and now mine is crashing too. Thanks  a lot Chris

#### [Chris Hughes (Jul 28 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130460535):
It doesn't hang provided I don't open a lean file. I am on 0.11.11

#### [Ali Sever (Jul 28 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130460606):
how did you close your lean files?

#### [Chris Hughes (Jul 28 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130460631):
Reinstall VSCode, and delete the folders containing the information about which lean files I had open

#### [Kevin Buzzard (Jul 28 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130461066):
As a temporary measure you can uninstall the lean extension and then try and figure out how to install an older version. I can't reproduce here on linux; things are working fine for me. Can you switch logging on somehow? This might happen to every Windows user who has auto-update on.

#### [Gabriel Ebner (Jul 28 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130461142):
I just tried to reproduce on windows, but everything works for me.  (elan is completely broken for me though)

#### [Kevin Buzzard (Jul 28 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130461168):
Chris can you switch on some debugging output, have the current extension loaded, and then open a Lean file? What happens exactly after you open a lean file? You said your computer freezes? What OS are you using? Win7 or Win10?

#### [Chris Hughes (Jul 28 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130461228):
Win10. My computer totally freezes, I can't even move my mouse.

#### [Chris Hughes (Jul 28 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130461376):
What do you mean by "switch on some debugging output"?

#### [Gabriel Ebner (Jul 28 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130462163):
If everything else fails, can you try to reinstall vscode and lean completely.  I am really at a loss here, there are almost no changes between vscode-lean 0.11.9 and 0.11.11, and none that look in any way dangerous.  I am running the lean 3.4.1 release on windows 10 and vscode 1.25.1 here.

#### [Simon Hudon (Jul 28 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130464752):
```quote
@**Gabriel Ebner**  
If you want to implement it yourself, look at how _lean.revealPosition is implemented in the info view 
```
Thanks! I'll have a look.

```quote
Sure, I am happy about new features. How did you extract the expected/actual type from the error message? Regex?
```

What I did is split the error message into lines and find the line that says `"has type:"` and I take everything until I find the line announcing the expected type.

#### [Chris Hughes (Jul 28 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130471379):
@**Ali Sever** I managed to revert my version of the VScode extension. This is how.

#### [Chris Hughes (Jul 28 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130471421):
1. Go into windows command line and type `code --disable-extensions`

#### [Chris Hughes (Jul 28 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130471431):
2. Open VScode, save everything and uninstall the lean extension. Also disable automatic updates of extensions using `...` in the top right of the extensions pane.

#### [Chris Hughes (Jul 28 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130472297):
3. Download the version `0.11.9` os the VScode extension from https://jroesch.gallery.vsassets.io/_apis/public/gallery/publisher/jroesch/extension/lean/0.11.9/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage

#### [Chris Hughes (Jul 28 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130472301):
4. Change the file extension of the downloaded file to .VSIX

#### [Chris Hughes (Jul 28 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130472326):
Go into VScode extension click ... in the top right of the extensions pane and install from VSIX usingthe file you downloaded.

#### [Ali Sever (Jul 28 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130472911):
Thanks Chris, awesome as always

#### [Kevin Buzzard (Jul 28 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130476732):
So I just tried upgrading on a Win10 machine and I've got it working. It did crash VS code -- but a restart of VS code (twice) got it working in the end. It didn't take down the OS.

#### [Ali Sever (Jul 28 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130476989):
by restart do you mean literally close the program and reopen it?

#### [Chris Hughes (Jul 28 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130477034):
I couldn't do that because my computer was frozen.

#### [Kevin Buzzard (Jul 28 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130477037):
The program (but not the OS) hung -- it became unresponsive. I restarted the program twice and got it working. I don't use Windows usually so I don't know if this is normal after an upgrade.

#### [Ali Sever (Jul 28 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130477041):
My pc doesnt freeze, but only the toolbar at the top of VS code works

#### [Kenny Lau (Jul 29 2018 at 05:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130506182):
So I opened task manager and discovered that VSCode is quick to take up all of the CPU and memory

#### [Moses Schönfinkel (Jul 29 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130513179):
I've been playing around with this and I can do `#eval`, `#check` just fine, but the second I type `lemma` or `theorem`, Lean eats all my memory and hits disc to the point the system can't recover. Surprisingly enough `example` doesn't crash it.

#### [Moses Schönfinkel (Jul 29 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130513560):
Actually it's VS Code that does that (unsurprisingly), because when I close the lean subprocess of VS-code parent, it doesn't fix anything.

#### [Gabriel Ebner (Jul 29 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130513763):
Do you also get the high memory usage with the info view closed (the tab "Lean Messages")?

#### [Moses Schönfinkel (Jul 29 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130513774):
Yes, it doesn't matter whether the info window is open or not. Just to clarify I'm on win 10.

#### [Moses Schönfinkel (Jul 29 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130513906):
I run this off of an HDD, if that helps it completely thrashes the hard drive as well, but this may very well be just a side-effect of memory om-nom.

#### [Gabriel Ebner (Jul 29 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130513975):
Yes, that's just swapping and it's because of the high memory usage.  The operating system just moves some stuff from RAM to HDD in order to make space.

#### [Gabriel Ebner (Jul 29 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130513984):
Just to make sure: in the task manager, how much memory does the lean subprocess use compared to the rest of vscode?

#### [Moses Schönfinkel (Jul 29 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130514038):
Negligable if I can even get it to update. The thing is, when I type `lemma` and I close VS within a second, it recovers. When I type `lemma` and I close just the `lean` subprocess of the tree, it doesn't recover. It's gigabytes of memory instantly for VSCode and some dozens of megabytes for lean.

#### [Patrick Massot (Jul 29 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130541475):
```quote
I managed to escape.  The only new feature is "ctrl+shift+p copy contents to comment", which copies the current content of the info view to a comment below the current line, as requested by @**Patrick Massot**.
```
Sorry I'm slow since my family returned from vacations. It works great! Next wish: do you think you could get VScode to offer to fold namespaces and sections like it folds statements and proofs?

#### [Kevin Buzzard (Jul 29 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130541586):
If VS code is capable of knowing which namespace we're in then I would find it super-helpful if this could be displayed in some way -- I sometimes find my cursor in the middle of a large file really wanting to know what namespace I'm in.

#### [Patrick Massot (Jul 29 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130541623):
This would be really really helpful

#### [Patrick Massot (Jul 29 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130541627):
What I'm asking for is easier, but having a substitute to what you're asking for is part of the motivation

#### [Gabriel Ebner (Jul 30 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130603708):
*Call for testers*: if you are on windows and experience hangs, could you please try this build of vscode-lean: https://1drv.ms/u/s!Au1u53SHpLowhTXMzMxSQI2Jy20o
To install, go to the extension tab, click the three dots, and select "Install from VSIX"

#### [Mario Carneiro (Jul 30 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130604392):
I went through the commits one at a time and the problem is https://github.com/leanprover/vscode-lean/commit/3dc37df of all things

#### [Mario Carneiro (Jul 30 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130604463):
the commit does a bit more than just adding `abbreviation` as a keyword as it claims; some additional stuff is added to the keyword recognition stuff at the end and I suspect it is triggering a memory leak in the regex parser

#### [Mario Carneiro (Jul 30 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130604647):
More specifically, the regex `([^ \t\n\r{(\[,:]*(,\s*)?)*` at the end has the form `(a*b?)*` which can loop

#### [Gabriel Ebner (Jul 30 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130604816):
Thanks so much for finding this commit!!!  I reverted it and published a new version.

#### [Gabriel Ebner (Jul 30 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130604854):
The regex was actually supposed to highlight the `bar` in `mutual def foo, bar`.  I did not expect a platform-dependent bug in the regex engine here..

#### [Mario Carneiro (Jul 30 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130605004):
I don't think you have to completely revert it; there is nothing wrong with adding `abbreviation` to the list, only the regex needs to be tweaked so that it doesn't match an infinite number of empty strings

#### [Mario Carneiro (Jul 30 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130605237):
I think  this should work for matching `a, b` in `def a, b` (the final capturing group): `([^ \t\n\r{(\[,:]+(,\s*[^ \t\n\r{(\[,:]+)*)`

#### [Kevin Buzzard (Jul 30 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130606974):
Thanks Mario! This caused my users a certain amount of grief today

#### [Johan Commelin (Aug 03 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130823107):
Gabriel, here is another thing that might be useful. If I have snippet like:
```lean
instance : group X :=
{ -- cursor is here
}
```

#### [Johan Commelin (Aug 03 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130823154):
Then the window displaying the goals knows exactly what is wrong: I need to supply `zero` and `mul` and stuff like that.

#### [Johan Commelin (Aug 03 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130823165):
So it would be nice if the autocomplete would show exactly those options. Now I often find myself clicking on the `{` to see in the Goal Window which stuff I still need to supply.

#### [Johan Commelin (Aug 03 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130823171):
Alternatively, maybe some snippet on steroids could just fill them all in (with `sorry`'s). But my snippet-fu is non-existent.

#### [Kenny Lau (Aug 03 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130825053):
ctrl+alt+shift+enter

#### [Johan Commelin (Aug 03 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130825062):
What the hack is that supposed to do?

#### [Johan Commelin (Aug 03 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130825113):
Is there a way to ask VScode "Hey, what does the shortcut do?"?

#### [Kenny Lau (Aug 03 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130825138):
it lets you view all the messages

#### [Kenny Lau (Aug 03 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130825143):
instead of just the one on your line

#### [Kevin Buzzard (Aug 03 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130827024):
The window on the bottom which displays the errors and warnings is the place to look for this. Sometimes you have to pull it into existence

#### [Johan Commelin (Aug 03 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130827173):
Cool! I didn't know I could pull something up there!

#### [Johan Commelin (Aug 10 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/131221794):
In VScode, if I select some text that is to be replaced, and I start typing a string the expected behaviour occurs. Except... Except when I start the replacement string with a `\`, then it is not expanded into a unicode character. So if I select "foobar" and then type `\lam x y`, I don't get a cool lambda.

#### [Johan Commelin (Aug 10 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/131221810):
@**Gabriel Ebner** :up:

#### [Kevin Buzzard (Aug 10 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/131229457):
I deal with this by writing what I want beforehand and copying it with ctrl-x into the whatever-that-thing-is-called buffer so I can use ctrl-v to paste when I'm replacing

#### [Kenny Lau (Aug 10 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/131229490):
I deal with this by selecting "foobar", deleting the text, and then type ``\``.

#### [Johan Commelin (Aug 10 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/131229622):
Right, I use both those way to deal with it. Still, I thought I would mention it, because maybe there is an easy fix. And sometimes I forget to deal with, and then :cry:

#### [Gabriel Ebner (Aug 10 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/131229745):
I'm not sure I understand this correctly.  You write `foobar` and then want `λ x, f` instead.  So instead of deleting `foobar`, you select it and then start typing `\lam x, f`?

#### [Johan Commelin (Aug 10 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/131229798):
Right

#### [Gabriel Ebner (Aug 10 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/131229807):
This shouldn't be too hard to add.  I just never used an editor like that.

#### [Johan Commelin (Aug 10 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/131229879):
For me it would usually be `ciw\lam x ,y`... still need to look at `lean.vim` and all those other plugins for the LSP.

#### [Gabriel Ebner (Aug 10 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/131229906):
I'm a vim addict as well.  There is a pretty good vim plugin for vscode that I'm using: https://github.com/VSCodeVim/Vim .
And `ciw\lam x ,y` works as expected!

#### [Johan Commelin (Aug 10 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/131229948):
Ok, I should try that out.

#### [Johan Commelin (Aug 10 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/131229967):
Otoh, if I get actual vim working, then I could run `lean` on a server, and connect via `mosh`. Then my crappy laptop would have superfast Lean!

#### [Gabriel Ebner (Aug 10 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/131230148):
And it should work in the latest version of the vscode extension.

#### [Kevin Buzzard (Aug 10 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/131234613):
You could just do this with emacs, right? 

I should prod William about CoCalc. I am writing an introductory worksheet for beginning UGs teaching basic logic, using Sphinx and "try it!". I realised that no undergraduate would even be able to do my first maths example sheet unless they know how to construct and destruct or/and etc.

#### [Johan Commelin (Aug 10 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/131244404):
```quote
I should prod William about CoCalc. 
```
Yes! I would love to hear more updates from CoCalc.

#### [Gabriel Ebner (Aug 13 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/132058162):
```quote
Gabriel, here is another thing that might be useful. If I have snippet like:
```lean
instance : group X :=
{ -- cursor is here
}
```
Then the window displaying the goals knows exactly what is wrong: I need to supply zero and mul and stuff like that.
So it would be nice if the autocomplete would show exactly those options.
```
This will probably not happen in Lean 3.

#### [Kenny Lau (Aug 18 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/132376683):
Ctrl+A is not working for me (I'm on Windows 10)

#### [Kenny Lau (Aug 18 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/132376850):
wait it works now

#### [Johan Commelin (Aug 30 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133076051):
@**Gabriel Ebner** While in Orsay we had some dreams and fantasies... they're recorded over here: https://github.com/leanprover-community/mathlib/wiki/VScode-wishlist :stuck_out_tongue_wink:

#### [Patrick Massot (Aug 30 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133076648):
some of them would probably need a more detailed description for people who didn't attend the dicussion

#### [Gabriel Ebner (Aug 30 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133076769):
I think I can make sense of most of them.  It reads like a wishlist for Lean 4.
What is "help with naming conventions"?

#### [Johan Commelin (Aug 30 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133076853):
"Help with naming conventions": Given a statement, figure out the name.

#### [Johan Commelin (Aug 30 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133076906):
I don't know much about Lean 4. But we also decided that we were to often saying: "That might be easier in Lean 4" etc...

#### [Johan Commelin (Aug 30 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133076989):
[kidding] Oooh, and we want MS Word's Clippy for Lean: "It looks like you are trying to prove something by induction. Would you like me to write the skeleton of the proof for you?" [/kidding]

#### [Chris Hughes (Aug 30 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133076994):
Can I add pp option to display types of proofs in your goal or local context as well. Maybe target types of coercions as well.

#### [Gabriel Ebner (Aug 30 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133078301):
I'm just saying that most points on the list are either infeasible right now, or shouldn't go into the vscode extension.
If you want to start experimenting right now, I think the naming convention automation is the lowest hanging fruit.  You can implement `#how_do_you_call ∀ x y, x < y → x - y = 0` as a user command for example.

#### [Gabriel Ebner (Aug 30 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133078602):
The next best is maybe "turn current goal into lemma".  You can do this as a tactic that outputs the text for the lemma as an error message.  The user can then copy&paste it where they want.  Last time I talked with Rob and Johannes there was the suggestion to parse tags like `<insert-above>lemma foo : a → b := sorry</insert-above>` in the error messages, but imho that's a bit too hacky unless there is a significant need for it.

#### [Gabriel Ebner (Aug 30 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133078667):
For the other "clippy" and refactoring stuff, I'd really wait.

#### [Johan Commelin (Aug 30 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133078880):
Clippy was not really serious...

#### [Johan Commelin (Aug 30 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133078893):
The turn goal into lemma tactic would be really cool I think.

#### [Johan Commelin (Aug 30 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133078902):
And I might even be able to write it with a bit of help.

#### [Johan Commelin (Aug 30 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133078912):
`#how_do_you_call` would be awesome, and I have no clue whatsoever how to write it.

#### [Johan Commelin (Aug 31 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133122224):
@**Gabriel Ebner** Currently `\func` points to an arrow that is frozen by core. We thought that it might be useful to point it to `⥤` instead, so that we can use that arrow for functors in the category lib.

#### [Gabriel Ebner (Aug 31 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133122657):
Ah I see, `⇒` is already used for the relators.  Another unused option is `⟹`, written `\==>`.

#### [Mario Carneiro (Aug 31 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133122712):
I think that this is used for natural transformations

#### [Gabriel Ebner (Aug 31 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133122756):
Yes, that would've been my next question.  What about morphisms and natural transformations?

#### [Johan Commelin (Aug 31 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133122769):
`\hom` and `\==>`

#### [Johan Commelin (Aug 31 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133122815):
It is really `\func` that's been messed up. For the rest we have nice solutions.

#### [Johan Commelin (Aug 31 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133122838):
Really the thing for relators should have been local notation. Then *you* wouldn't have to do anything.

#### [Johan Commelin (Aug 31 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133122850):
Now we are kindly asking you to point `\func` to this goofy arrow that looks enough like what we want.

#### [Gabriel Ebner (Aug 31 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133123049):
I definitely agree on the local notation part.  I'd just like to avoid changing existing abbreviations if possible.

#### [Gabriel Ebner (Aug 31 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133123074):
You can easily add the arrow yourself: just add a new line with `"func": "⟹",` to this json file https://github.com/leanprover/vscode-lean/blob/master/translations.json#L1290 and make a PR.

#### [Johan Commelin (Aug 31 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133123137):
Right... I'm currently doing something slightly related... writing a Python script that turns that file into Compose-key sequences.

#### [Johan Commelin (Aug 31 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133123226):
So I should not overwrite `\functor`? But adding `\func` is ok?

#### [Gabriel Ebner (Aug 31 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133123230):
I feel like we need a separate repository for this file and all associated scripts soon.  I have also written a converter: https://github.com/gebner/m17n-lean

#### [Gabriel Ebner (Aug 31 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133123245):
As I said, I'd rather avoid overwriting.  But I'm happy either way.

#### [Johan Commelin (Aug 31 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133123319):
I guess no-one is using that abbreviation at the moment. So I'dd rather overwrite. Chances are way higher that someone will write `\functor` when doing categories.

#### [Johan Commelin (Aug 31 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133123351):
https://github.com/jcommelin/vscode-lean/pull/1

#### [Sean Leather (Aug 31 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133123352):
```quote
I feel like we need a separate repository for this file and all associated scripts soon.  I have also written a converter: https://github.com/gebner/m17n-lean
```
I've thought something similar, in particular for providing a single source for VS Code, Emacs, and Vim keybindings.

#### [Gabriel Ebner (Aug 31 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133123354):
Ok, then.  You can still get the old arrow with `\r=` etc.

#### [Johan Commelin (Aug 31 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133123366):
Exactly

#### [Gabriel Ebner (Aug 31 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133123377):
@**Johan Commelin** You made a PR to your own fork.

#### [Johan Commelin (Aug 31 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133123384):
Oops, that is silly

#### [Johan Commelin (Aug 31 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133123528):
https://github.com/leanprover/vscode-lean/pull/85

#### [Gabriel Ebner (Aug 31 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133123710):
And deployed.

#### [Johan Commelin (Aug 31 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133123835):
@**Scott Morrison** Voila! You can update the arrow for functors in your lib!

#### [Johan Commelin (Aug 31 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133123932):
```python
import fileinput
import re

pat = re.compile('"(.*)":"(.*)"', re.MULTILINE)

for line in fileinput.input():
    m = pat.match(line)
    pre = m.group(1)
    suf = m.group(2)
    hooked_pre = [ '<' + c + '>' for c in list(pre) ]
    s = '<Multi_key> ' + ' '.join(hooked_pre) + ' : "' + suf + '"    # ' + pre
    print(s)
```

#### [Johan Commelin (Aug 31 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133123942):
That's the silly thing that I'm trying

#### [Johan Commelin (Aug 31 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133124968):
@**Gabriel Ebner** By the way, if the original arrow becomes unfrozen in Lean 4, then we might want to switch back...

#### [Mario Carneiro (Aug 31 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133125220):
are *you* going to claim it as a global notation?

#### [Johan Commelin (Aug 31 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133125512):
Of course! We are evil!

#### [Mario Carneiro (Aug 31 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133125588):
I'm only allowing the notations in category theory now because the arrows are bizarre

#### [Johan Commelin (Aug 31 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133125750):
Any arrow that is not bizarre can be local. That's fine with me. We'll be locally evil.

#### [Patrick Massot (Aug 31 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133127381):
Gabriel, why do you hardcode the leader key?

#### [Gabriel Ebner (Aug 31 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128408):
Leader = backslash? It used to be backslash in emacs, and I just copied that.  There is no fundamental reason why it has to be a backslash.  What do you have in mind, `§`?  We can easily support that with a configuration option.  I don't know whether we could support "right-control" as a leader key at all.

#### [Patrick Massot (Aug 31 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128462):
Yes, I mean leader as in vim terminology. The point is that \  is very inconvenient on a French keyboard. In vim I always use comma for that

#### [Mario Carneiro (Aug 31 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128489):
wouldn't comma give you a lot of false positives?

#### [Patrick Massot (Aug 31 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128498):
only if the abbreviation starts with a space

#### [Patrick Massot (Aug 31 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128511):
comma is always followed by space (at least in France)

#### [Mario Carneiro (Aug 31 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128524):
it's usually followed by a space in mathlib, but there are a significant fraction with no space

#### [Patrick Massot (Aug 31 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128577):
under what kind of circumstances?

#### [Mario Carneiro (Aug 31 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128608):
`λ⟨a,b⟩, ` and such

#### [Patrick Massot (Aug 31 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128616):
this is wrong

#### [Patrick Massot (Aug 31 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128617):
should be a, b

#### [Mario Carneiro (Aug 31 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128621):
also between rewrite rules and simp rules sometimes

#### [Mario Carneiro (Aug 31 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128629):
I agree, I try to keep a space after a comma but not everyone does

#### [Patrick Massot (Aug 31 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128630):
So switching to comma would improve typography in mathlib!

#### [Johan Commelin (Aug 31 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128686):
You could map your CAPS LOCK key to §, and then use that as a leader.

#### [Johan Commelin (Aug 31 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128691):
Or just map your caps lock to `\`

#### [Gabriel Ebner (Aug 31 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128705):
I thought French keyboards have a key for §?

#### [Patrick Massot (Aug 31 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128729):
no

#### [Patrick Massot (Aug 31 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128813):
https://fr.wikipedia.org/wiki/Fichier:Clavier-Azerty-France.svg

#### [Gabriel Ebner (Aug 31 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128815):
Oh, so wikipedia has been lying to me.  I thought it is right next to shift.  https://en.wikipedia.org/wiki/AZERTY#/media/File:Azerty_fr.svg

#### [Johan Commelin (Aug 31 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128844):
It seems to be `Shift + !`

#### [Gabriel Ebner (Aug 31 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128845):
That picture also shows § right next to the right shift key?

#### [Patrick Massot (Aug 31 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128849):
it's there, but not on direct access

#### [Patrick Massot (Aug 31 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128862):
it's better than \ which is really hard to type, but comma is direct access

#### [Johan Commelin (Aug 31 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128913):
Make `ù` the leader (-;

#### [Patrick Massot (Aug 31 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133129047):
indeed this would also probably be fine (this character is used in only one word)

#### [Edward Ayers (Aug 31 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133129165):
On a different subject: are there any plans to add a code formatter to vscode extension?

#### [Gabriel Ebner (Aug 31 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133129198):
I think there are plans to add a code formatter to Lean 4.

#### [Patrick Massot (Aug 31 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133129243):
what is a code formatter?

#### [Edward Ayers (Aug 31 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133129312):
```quote
what is a code formatter?
```
You slam a button and it adds spaces in the proper places and enforces some style guide things.

#### [Edward Ayers (Aug 31 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133129332):
Basically it adds and removes spaces until the code looks nice

#### [Patrick Massot (Aug 31 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133129448):
that would be really nice

#### [Kevin Buzzard (Aug 31 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133130026):
Presumably it only works for code which can be made to look nice by addition and removal of spaces

#### [Edward Ayers (Aug 31 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133130061):
I think that you can in theory perform arbitrary textual transformations

#### [Gabriel Ebner (Aug 31 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133131128):
[Coming soon to a vscode near you.](/user_uploads/3121/PIoL-GV9fsWWF6LSXn8cb1Cx/vscode-lean-leader.png) I'm on vacation now, @**Sebastian Ullrich**  can publish updates to the vscode extension if there's anything urgent.

#### [Bryan Gin-ge Chen (Aug 31 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133131260):
```quote
On a different subject: are there any plans to add a code formatter to vscode extension?
```
There's also an open issue on the lean repository related to this [here](https://github.com/leanprover/lean/issues/1970).

#### [Patrick Massot (Aug 31 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133131691):
Thank you very much Gabriel! Together with the TAB thing it really makes Leaning more comfortable

#### [Ali Sever (Sep 02 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133208406):
My windows updated and now vscode says lean doesn't work. I tried using lean --version and I got "segmentation fault". Even if I use PATH ***, I can't get lean --version to work. Any suggestions?

#### [Ali Sever (Sep 03 2018 at 19:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133271161):
@**Mario Carneiro** Hi Mario, I recently had an issue with a windows insider update which completely prevented me from using lean. Kevin told me that I should warn you about this, since there's a chance that whatever caused this might be in the next windows update (which google says is on October 10th). I'm afraid I can't help you much about the error, but I've put everything I know here https://github.com/leanprover/lean/issues/1972.

#### [Kenny Lau (Sep 04 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133300183):
[2018-09-04.png](/user_uploads/3121/Jt5Tckc7s01asToD4wpB1VRy/2018-09-04.png)

#### [Kevin Buzzard (Sep 04 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133300973):
Do you know about ` ``` `? It makes your code easier to cut and paste ;-)

#### [Kenny Lau (Sep 04 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133301089):
```lean
variables (A : Type*)
class MWE extends has_zero A
```

#### [Johan Commelin (Sep 04 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133301106):
Also, why did you put that in this thread?

#### [Kenny Lau (Sep 04 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133301134):
because it's about VScode

#### [Patrick Massot (Sep 04 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133301273):
I guess Kenny wants to complain about syntax highlighting

#### [Kevin Buzzard (Sep 04 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133302054):
Oh I see. He's as cryptic as ever :-)

#### [Bryan Gin-ge Chen (Sep 04 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133309635):
```lean
set_option class.instance_max_depth 5
```
This one looks weird too (with `class` colored differently from `.instance_max_depth`

#### [Bryan Gin-ge Chen (Sep 04 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133311084):
I've submitted [a PR](https://github.com/leanprover/vscode-lean/pull/87) for Kenny and my examples.

#### [Kenny Lau (Sep 05 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133393460):
I just discovered that you can indent a bunch of lines by highlighting them and then pressing `ctrl+]`, and de-indent by `ctrl+[`

#### [Johan Commelin (Sep 05 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133393516):
Alternative: Tab or Shift-Tab

#### [Patrick Massot (Sep 05 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133393518):
also works with Tab and Shift-Tab

#### [Kenny Lau (Sep 05 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133393536):
oh right

#### [Johan Commelin (Sep 05 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133393703):
Also, you should learn Vim, so that you can be disgusted by `Ctrl-[` being a shortcut for something silly like that (-;

#### [Kevin Buzzard (Sep 05 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133393766):
Did you try `\G`?

#### [Kevin Buzzard (Sep 05 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133393773):
that's even more bizarre

#### [Johan Commelin (Sep 05 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133393829):
Right, that should clearly expand to `α`.

#### [Patrick Massot (Sep 05 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133394002):
Same with \R (for rings) and \M (for modules), they should expand to α

#### [Kevin Buzzard (Sep 05 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133394461):
I am writing some Noetherian code and of course using Mario's work on Noetherian modules, and you can tell exactly who wrote each line because of this convention :-)

#### [Kevin Buzzard (Sep 05 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133395143):
```quote
Same with \R (for rings) and \M (for modules), they should expand to α
```
or maybe \beta, depending on...um...a random choice I guess

#### [Bryan Gin-ge Chen (Sep 06 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133409881):
Has anyone had any luck with the "Bracket pair colorizer" extension that's suggested in [the readme](https://github.com/leanprover/vscode-lean/blob/master/README.md#other-potentially-helpful-settings)? It doesn't seem to work (on lean files) right out of the box (perhaps because lean doesn't appear on [the Prism.js list of languages](https://prismjs.com/#languages-list)), though I like how it looks on other filetypes.

#### [Kenny Lau (Sep 07 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133511543):
I opened my file called `dfinsupp_quotient.lean` in VSCode, and then closed it, and then rebuilt Lean, and then rebuilt mathlib, and then opened it again in VSCode, but its content was suddenly gone.

#### [Kenny Lau (Sep 07 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133511668):
my file is independent from mathlib, it's in my own sandbox

#### [Chris Hughes (Sep 07 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133511721):
Sounds like you didn't save. Did you open if from a file explorer, or just open VScode, and it was there because it was the last thing you were looking at?

#### [Kenny Lau (Sep 07 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133511779):
I always save my file after I type every word

#### [Kenny Lau (Sep 07 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133511792):
the latter

#### [Kenny Lau (Sep 07 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133511866):
also, now, whenever I open VSCode a second tab would magically appear, and the name of the tab would be "null", and whenever I click on "null" it would disappear

#### [Kenny Lau (Sep 07 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133511941):
[2018-09-07-2.png](/user_uploads/3121/JQPkbB2KJ2oZvqaMMl03_ttK/2018-09-07-2.png)

#### [Kenny Lau (Sep 07 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133511963):
whenever I click on the tab "null", the tab "null" itself would disappear

#### [Kenny Lau (Sep 07 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133512015):
I don't really mind spending the next day retyping everything, I just want to make sure that it won't happen again

#### [Chris Hughes (Sep 07 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133512309):
What happens if you open from a file explorer?

#### [Kenny Lau (Sep 07 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133512331):
it is also empty

#### [Kenny Lau (Sep 08 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133560303):
Ctrl+space does not show the defining fields of a structure/inductive/class, such as filter.univ_sets

#### [Kenny Lau (Sep 08 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133560389):
hmm, it does show `filter.univ_sets`.

#### [Kenny Lau (Sep 08 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133560392):
But I do remember there are some things that Ctrl+Space doesn't show

#### [Chris Hughes (Sep 08 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133561694):
Sometimes it doesn't show things in a namespace that you have open if you type `finset.x` instead of `x`

#### [Kevin Buzzard (Sep 08 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133562956):
In my experience sometimes it doesn't show something, and then you hit escape and then ctrl-space again, and then it shows them, although I noted this behaviour months ago and cannot say for sure that it still occurs.

#### [Kenny Lau (Sep 08 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133582528):
Is there a quick way to change `(lorem ipsum dolor)` to `{lorem ipsum dolor}` etc?

#### [Mario Carneiro (Sep 08 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133582636):
you can use `Select to Bracket` (no default key command)

#### [Bryan Gin-ge Chen (Sep 08 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133583057):
The vim incantation [```%r}``r{```](https://stackoverflow.com/questions/25405072/quickest-way-to-change-a-pair-of-parenthesis-to-brackets-in-vim) would do this, but unfortunately it doesn't work in the VScode vim extension yet (maybe [soon](https://github.com/VSCodeVim/Vim/pull/3028)?).

#### [Olli (Sep 08 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133583174):
VSCode's vim extension has a feature from vim-surround enabled by default, so `cs)}` works

#### [Bryan Gin-ge Chen (Sep 09 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133584707):
Cool, I didn't know that! However, on my macOS system, the "surround" commands don't work when the lean extension is enabled. They do work on my windows machine (and when I disable the lean extension, or on non-lean files). Very strange...

#### [Bryan Gin-ge Chen (Sep 09 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133584754):
When I type `cs` on my mac with the lean extension enabled, it deletes the whole line and puts me in insert mode.

#### [Bryan Gin-ge Chen (Sep 09 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133584862):
Oh wait it's working now. No idea what's going on.

#### [Kenny Lau (Sep 09 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133608201):
Is there a way to see which file is being compiled?

#### [Keeley Hoek (Sep 10 2018 at 05:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133636317):
When an identifier that ends with number has an error message, only the part up to the number is underlined. Moreover, clicking an identifier which ends with a number will not highlight its usages in the rest of the open file, as usually happens

#### [Bryan Gin-ge Chen (Sep 10 2018 at 05:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133636542):
The same things happen with dots, though maybe the current highlighting behavior is preferable in that case.

#### [Keeley Hoek (Sep 12 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133812963):
Is there a fundamental reason why the partial `tactic.trace ...` output of a tactic is only displayed in the editor after tactic execution has completed (commonly, failed)?

#### [Sebastian Ullrich (Sep 12 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133813596):
Yeah, the current server protocol doesn't really allow for another (efficient) option. I've thought about this, but it's not clear at all how this could work especially when we move to storing messages in an immutable Lean data structure.

#### [Kenny Lau (Sep 13 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133867290):
[2018-09-13.png](/user_uploads/3121/NkA0T9DQQznkuHgdbNbPKEkN/2018-09-13.png) 
misplaced red underscore

#### [Kenny Lau (Sep 13 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133867293):
code:
```lean
example : nat := (_)
example : nat := (_ : nat)
```

#### [Kenny Lau (Sep 13 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133867301):
line 1 is normal, line 2 is not

#### [Kevin Buzzard (Sep 13 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133868544):
Ned Summers showed me examples of this which were really crazy -- he seemed to be able to move the red line an arbitrary amount to the left :-)

#### [Patrick Massot (Sep 13 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133868553):
I guess this has nothing to do with VScode. The problem should be in lean server mode, no?

#### [Gabriel Ebner (Sep 13 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133881106):
"Moving error messages an *arbitrary* amount to the left" is a known bug in the presence of calligraphic characters.  Please just don't write errors when using calligraphic (or fraktur) characters.

#### [Gabriel Ebner (Sep 13 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133881171):
The problem is that vscode counts the number of utf-16 words (2 bytes), while lean counts the number of Unicode codepoints (can be larger than 2 bytes).

#### [Johan Commelin (Sep 13 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133881477):
Ouch... does it make sense to report this bug to VScode? Or is it not worth it?

#### [Gabriel Ebner (Sep 13 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133881661):
It's by design I think. The language server protocol specifies this behavior explicitly.  There is an issue in the github repo, but I am not sure if they'll ever change it.  Note that JavaScript also uses this utf-16 indexing for strings.

#### [Gabriel Ebner (Sep 13 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133881694):
There is another possible bug.  Vscode and lean also disagree on what line endings are recognized.  Vscode recognizes `\r`, but lean doesn't.

#### [Johan Commelin (Sep 13 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133881817):
Lean is pretty sane. :big_smile:

#### [Kevin Buzzard (Sep 13 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133881836):
Indeed Ned was doing category theory and there were calligraphic C's everywhere. Rather took me by surprise when I first saw it!

#### [Johan Commelin (Sep 13 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133881855):
Could you do a man-in-the-middle on the Lean - VScode communication?

#### [Johan Commelin (Sep 13 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133881904):
Somehow VScode is able to deal with Unicode characters, even if they use more then 2 bytes.

#### [Johan Commelin (Sep 13 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133881923):
If the Lean extension would be able to detect this behaviour, you could manually adjust the coordinates of the red line.

#### [Johan Commelin (Sep 13 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133881936):
Admittedly this is very hacky, and probably not really worth it.

#### [Gabriel Ebner (Sep 13 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133882129):
Yes that's the way to fix it. You need to manually translate all the positions in Vscode.

#### [Gabriel Ebner (Sep 13 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133882192):
The way you encode calligraphic characters in utf-16 is two use 2 2-byte words.  In utf-8 you need 4 bytes.

#### [Keeley Hoek (Sep 13 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133882648):
Every time I have to write a newline character in a string I have to do it twice because it always autocorrects into a reverse set inclusion :'(

#### [Gabriel Ebner (Sep 13 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133884051):
Does \\n work?

#### [Kenny Lau (Sep 13 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133886939):
But my example has bo calligraphic characters!

#### [Keeley Hoek (Sep 13 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133887743):
@**Gabriel Ebner** can I pay you real money? :D awesome

#### [Kenny Lau (Sep 30 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/134914446):
sometimes in the middle of the proof, when I type something (say `abcde`), then after I finish, I see the state after typing `a`, and then after typing `b`, and then after typing `c`, and then after typing `d`, and then after typing `e`, resulting in the situation that I have to wait a while before I can see the result

#### [Mario Carneiro (Sep 30 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/134914451):
Is your cursor unusually slow?

#### [Mario Carneiro (Sep 30 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/134914458):
or typing

#### [Mario Carneiro (Sep 30 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/134914459):
Or is it just lean being behind VSCode

#### [Kenny Lau (Sep 30 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/134914463):
the cursor is fine, and so is my typing

#### [Kenny Lau (Sep 30 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/134914504):
oh and sometimes after I type something, suddenly the whole file is starting to compile and I have to wait a while again

#### [Mario Carneiro (Sep 30 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/134914511):
That latter problem has hit me many times

#### [Kenny Lau (Sep 30 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/134914548):
returning to the previous problem, if I copy and paste `abcde`, then I see the end result instantaneously, so it isn't lean being behind VSCode either

#### [Mario Carneiro (Sep 30 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/134914553):
I believe sometimes when you mouse over something vscode makes an info request which requires lean to open and compile a new file

#### [Mario Carneiro (Sep 30 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/134914555):
It might be that the cost of error reporting is high?

#### [Mario Carneiro (Sep 30 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/134914560):
so that the partial results take longer to compile

#### [Kenny Lau (Sep 30 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/134914673):
shouldn't it stop compiling when I enter a new letter?

#### [Mario Carneiro (Sep 30 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/134914679):
it should, but it may also take some time for the interrupt to be accepted

#### [Kenny Lau (Oct 02 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/135042970):
```quote
oh and sometimes after I type something, suddenly the whole file is starting to compile and I have to wait a while again
```
I really hope they can remove this "feature"

#### [Kevin Buzzard (Oct 02 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/135043039):
Is this a Windows-only feature? I am not sure I have experienced it on linux.

#### [Patrick Massot (Oct 02 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/135044696):
I think I never saw this (I'm also using Linux)

#### [Bryan Gin-ge Chen (Oct 02 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/135047051):
If you're referring to the fact that the info view window goes blank for long periods while typing (inconsistently depending on the type of input?), I've also experienced this on both Mac and Windows and I complained about it [here](https://github.com/leanprover/vscode-lean/issues/92). I wasn't able to figure out how to fix the underlying issue, but as a workaround, [I submitted a PR](https://github.com/leanprover/vscode-lean/pull/93) which allows you to assign a keystroke to toggle pausing the infoview. So now I just hit my keybind for `lean.infoview.toggleUpdating`before typing, and hit it again when I'm done, which feels somewhat better.

#### [Bryan Gin-ge Chen (Oct 02 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/135047256):
```quote
Has anyone had any luck with the "Bracket pair colorizer" extension that's suggested in [the readme](https://github.com/leanprover/vscode-lean/blob/master/README.md#other-potentially-helpful-settings)? It doesn't seem to work (on lean files) right out of the box (perhaps because lean doesn't appear on [the Prism.js list of languages](https://prismjs.com/#languages-list)), though I like how it looks on other filetypes.
```
As an update, the new version of that extension, ["Bracket Pair Colorizer 2"](https://github.com/CoenraadS/Bracket-Pair-Colorizer-2) currently works out of the box with Lean, though it's still in alpha.

#### [Scott Morrison (Oct 02 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/135066668):
I've definitely seen Kenny's issue on macOS. I think the diagnosis is that your mouse has accidentally hovered over something, VS Code has decided to open a file in the background in order to provide a tooltip, and this has caused a cascade of recompilations.

#### [Kevin Buzzard (Oct 03 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/135085823):
I only ever run lean with a complete bunch of .olean files for all of mathlib. Does this behaviour still occur in this situation?

#### [Scott Morrison (Oct 03 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/135089946):
Probably not.

#### [Kevin Buzzard (Oct 03 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/135092008):
Then this might be the reason I don't see this behaviour in my set-up (i.e. nothing to do with the OS)

#### [Patrick Massot (Oct 03 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/135092018):
It's clearly much easier to work on something else than mathlib, for this reason

#### [Kenny Lau (Oct 09 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/135500113):
Whenever I type `/-`, I automatically get `-/`, which is inconvenient at times. Before yesterday, it is smarter, in the sense that when I don't want `-/` it really doesn't give me `-/`.

#### [Kenny Lau (Oct 11 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/135616146):
sometimes when I'm in `(checking visible lines and above mode)`, everything suddenly stops updating

#### [Kenny Lau (Oct 11 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/135616156):
and I need to close and reopen VSCode

#### [Gabriel Ebner (Oct 11 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/135620011):
Known bug in the lean C++ code.  That's why the default changed back to "visible files" a few months back.

#### [Kevin Buzzard (Oct 13 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/135726823):
Is this a bug in VS Code? I'm using Ubuntu 18.04. [vscodebug1.png](/user_uploads/3121/OxpxEK0jqaMg9fHcbyh2yqu1/vscodebug1.png) [vscodebug2.png](/user_uploads/3121/upsOq2WPURBmCL_T-T-IWBIf/vscodebug2.png) [vscodebug3.png](/user_uploads/3121/4JUDEG9mSCNVtYDn8Kn02vOZ/vscodebug3.png) 

After I hover over "U" in the git stuff, my output when I hover over "+" is corrupted. I can get it back by hovering over e.g. "discard changes".

#### [Kevin Buzzard (Oct 13 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/135726867):
curses, did not capture mouse, sorry. Hover over "U" in git pane to open this menu.

#### [Gabriel Ebner (Oct 13 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/135726929):
Probably a bug in electron (vscode uses electron (= essentially a distribution of the chrome (well, chromium) web browser) as the gui library).  https://bugs.chromium.org/p/chromium/issues/detail?id=442111

#### [Simon Hudon (Oct 13 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/135728564):
That's a very lisp-y answer

#### [Kenny Lau (Nov 05 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/146800716):
I tried to open a lean file from explorer (I'm using Windows) and then I discovered that my workspace is gone

#### [Johan Commelin (Nov 15 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/147731422):
@**Gabriel Ebner** How hard would it be to implement a toggle that enables/disables whether Lean is interactive. Sometimes I would like to disable the interactivity to paste a chunk of "almost-Lean" (for example from the goal window) and massage it into Lean-code. After that, I would reenable interactivity, so that the code would be sent of to the server.
In this way, you wouldn't have the server constantly choking on the almost-Lean code, of which you already know that it won't parse...

#### [Johan Commelin (Nov 15 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/147731427):
This might be a first step towards a "Turn this goal into a lemma" functionality in VScode

#### [Gabriel Ebner (Nov 15 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/147731713):
Well, the two features are completely independent.
For the "pause" feature, I think the easiest way would be prevent syncing the file contents here: https://github.com/leanprover/vscode-lean/blob/d70dfa121bc616100c14bc0fd24400b9962922da/src/sync.ts#L36  You'd probably also want to disable autocompletion, hover, go-to-definition, etc. in that mode.
Add a command to toggle the pause flag, and when unsetting it, resync all files.  There is theoretically also an option in the roi setting (press on the Lean item in the status bar, and then select "nothing"); but the server still recompiles stuff for autocompletion etc.

#### [Johan Commelin (Nov 15 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/147731857):
Right, they are completely independent, but they would work together pretty well.

#### [Johan Commelin (Nov 15 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/147731861):
I think stuff like autocompletion could still be useful in the "pause" mode.

#### [Johan Commelin (Nov 15 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/147731873):
At least when you are working on "almost-Lean" code.

#### [Johan Commelin (Nov 15 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/147731936):
Otherwise I could also just edit inside a comment block. But I would like to have some of the cheaper interaction, like syntax highlighting and autocompletion.

#### [Johan Commelin (Nov 15 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/147731970):
Anyway, I have never worked with typescript before, and I have no idea where to start if I would want to modify the VScode extension. But I would certainly like to learn this. Has someone ever twitched work on the Lean-VScode extension?

