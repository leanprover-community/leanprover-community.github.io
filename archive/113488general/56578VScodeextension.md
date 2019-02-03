---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/56578VScodeextension.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [VScode extension](https://leanprover-community.github.io/archive/113488general/56578VScodeextension.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (Jul 25 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130267754):
<p><span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> could we get two variants of F12, one creating a new tab if a new file needs to be opened, and one replacing the content of the current tab, as it currently does? Also, could we get key bindings for "Go back" and "Restart Lean"? And maybe one for "Create a comment below the current line, containing what is currently in the Lean messages view"? About Lean messages, each time I press Ctrl+Shift+Enter to open this tab, it also opens a copy of the file I'm currently editing. It's annoying and I think it wasn't like this before.</p>

#### [ Mario Carneiro (Jul 25 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130267806):
<p>alt-left should be a key binding for "go back"</p>

#### [ Patrick Massot (Jul 25 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130267825):
<p>Not here</p>

#### [ Mario Carneiro (Jul 25 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130267829):
<p>I also noticed the bug with ctrl-shift-enter opening a copy over the message view</p>

#### [ Mario Carneiro (Jul 25 2018 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130267870):
<p>You can set your key bindings yourself btw</p>

#### [ Patrick Massot (Jul 25 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130267890):
<p>It makes me think I would really love to know a way to ask VScode to trigger translation immediately rather than waiting for a blank space of movement. It would really help to type words containing several special unicode characters.</p>

#### [ Patrick Massot (Jul 25 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130267893):
<p>How do you setup keybindings?</p>

#### [ Mario Carneiro (Jul 25 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130267947):
<p>file &gt; prefs &gt; key shortcuts</p>

#### [ Johan Commelin (Jul 25 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130267956):
<blockquote>
<p>It makes me think I would really love to know a way to ask VScode to trigger translation immediately rather than waiting for a blank space of movement. It would really help to type words containing several special unicode characters.</p>
</blockquote>
<p>But how would you deal with prefixes? Such as <code>\t</code> vs <code>\to</code>?</p>

#### [ Mario Carneiro (Jul 25 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130267959):
<p>this is what emacs does</p>

#### [ Mario Carneiro (Jul 25 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130268004):
<p>I think if you type <code>\t</code> you get the triangle but underlined, and typing <code>o</code> changes it to an arrow</p>

#### [ Patrick Massot (Jul 25 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130268013):
<p>I don't need it to be automatic, I want to be able to <em>ask</em> for it before VScode decides it should do it anyway</p>

#### [ Johan Commelin (Jul 25 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130268026):
<p>Sweet. So if I would type <code>\Zp</code> would that give me ℤp?</p>

#### [ Mario Carneiro (Jul 25 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130268033):
<p>I believe so</p>

#### [ Johan Commelin (Jul 25 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130268035):
<p>Nice</p>

#### [ Mario Carneiro (Jul 25 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130268039):
<p>I think vscode does the same in that case</p>

#### [ Johan Commelin (Jul 25 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130268041):
<p>Hmm, maybe it does.</p>

#### [ Gabriel Ebner (Jul 25 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130268044):
<blockquote>
<p>could we get two variants of F12,</p>
</blockquote>
<p><del>ctrl+k f12</del> the default keybinding does not work here</p>
<p>But you can assign "open definition to the side" to whatever keybinding you like.</p>

#### [ Johan Commelin (Jul 25 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130268089):
<blockquote>
<p>I think vscode does the same in that case</p>
</blockquote>
<p>You are right.</p>

#### [ Mario Carneiro (Jul 25 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130268170):
<blockquote>
<p>could we get two variants of F12, one creating a new tab if a new file needs to be opened, and one replacing the content of the current tab, as it currently does? </p>
</blockquote>
<p>Currently F12 and other navigation commands only replace the content of the current tab if you are viewing a file in temporary mode, indicated with italics in the tab title</p>

#### [ Mario Carneiro (Jul 25 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130268182):
<p>you can clear temporary mode by clicking on the title or editing anywhere</p>

#### [ Gabriel Ebner (Jul 25 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130268183):
<blockquote>
<p>"Go back"</p>
</blockquote>
<p>ctrl+alt+- is the default keybinding.  I usually use the vim keybindings, where it is ctrl+t as expected.</p>

#### [ Patrick Massot (Jul 25 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130268234):
<p>Thanks for pointing out "open definition to the side". But it opens in the area containing Lean messages :(</p>

#### [ Gabriel Ebner (Jul 25 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130268256):
<blockquote>
<p>Ctrl+Shift+Enter to open this tab, it also opens a copy of the file I'm currently editing</p>
</blockquote>
<p>Oh, that seems to be a new bug with vscode 1.25.  <a href="https://github.com/leanprover/vscode-lean/issues/77" target="_blank" title="https://github.com/leanprover/vscode-lean/issues/77">https://github.com/leanprover/vscode-lean/issues/77</a></p>

#### [ Gabriel Ebner (Jul 25 2018 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130268312):
<blockquote>
<p>Thanks for pointing out "open definition to the side". But it opens in the area containing Lean messages :(</p>
</blockquote>
<p>You can split the editor first with ctrl+\</p>

#### [ Patrick Massot (Jul 25 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130268376):
<p>Thanks, but this creates a whole new zone, not a new tab in the current group</p>

#### [ Patrick Massot (Jul 25 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130268378):
<p>Oh, that italic filename is a really subtle clue. I never noticed it</p>

#### [ Patrick Massot (Jul 25 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130268385):
<p>It's lunchtime, but I'm happy I've learned a lot of VScode tricks</p>

#### [ Gabriel Ebner (Jul 25 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130272111):
<blockquote>
<p>Create a comment below the current line, containing what is currently in the Lean messages view</p>
</blockquote>
<p><a href="https://github.com/leanprover/vscode-lean/commit/d3ae4b1a1108cb0eb1cefc645b6602a307b4d4be" target="_blank" title="https://github.com/leanprover/vscode-lean/commit/d3ae4b1a1108cb0eb1cefc645b6602a307b4d4be">https://github.com/leanprover/vscode-lean/commit/d3ae4b1a1108cb0eb1cefc645b6602a307b4d4be</a></p>
<p>I'm currently having a bit of trouble publishing the vscode extension, so you'll have to wait a bit for the update.</p>

#### [ Patrick Massot (Jul 25 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130278254):
<p>Thanks! Hopefully this example could serve as a pattern for other stuff like that (I have nothing specific in mind).</p>

#### [ Gabriel Ebner (Jul 27 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130433110):
<p>I just pushed the update.  Please tell me if I broke anything.</p>

#### [ Gabriel Ebner (Jul 27 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130433115):
<p>afk hornet in the room</p>

#### [ Gabriel Ebner (Jul 27 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130435463):
<p>I managed to escape.  The only new feature is "ctrl+shift+p copy contents to comment", which copies the current content of the info view to a comment below the current line, as requested by <span class="user-mention" data-user-id="110031">@Patrick Massot</span>.</p>

#### [ Chris Hughes (Jul 27 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130435618):
<p>One slightly annoying new feature of VSCode, is that when I click "Display Goal", it opens the file I have open in the right pane. Is there a way to do anything about that?</p>

#### [ Simon Hudon (Jul 27 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130435636):
<p>I've added a feature in emacs (taken from <code>company-coq</code>) to use <code>diff</code> to compare the actual / expected types in error messages. Any chance I might convince you to add it to VS code or help me implement it for VS code?</p>

#### [ Gabriel Ebner (Jul 28 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130455350):
<blockquote>
<p>it opens the file I have open in the right pane</p>
</blockquote>
<p>This bug should be fixed with yesterday's update.</p>

#### [ Gabriel Ebner (Jul 28 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130455926):
<blockquote>
<p>[..] use <code>diff</code> to compare the actual / expected types in error messages. Any chance I might convince you to add it to VS code or help me implement it for VS code?</p>
</blockquote>
<p>Sure, I am happy about new features.  How did you extract the expected/actual type from the error message?  Regex?</p>
<p>If you want to implement it yourself, look at how <code>_lean.revealPosition</code> is implemented in the info view (this handles the click on the message title and scrolls to the corresponding position in the file): <a href="https://github.com/leanprover/vscode-lean/blob/b872639347221a0146bf4e98234ee55e3d634b30/src/infoview.ts#L375" target="_blank" title="https://github.com/leanprover/vscode-lean/blob/b872639347221a0146bf4e98234ee55e3d634b30/src/infoview.ts#L375">https://github.com/leanprover/vscode-lean/blob/b872639347221a0146bf4e98234ee55e3d634b30/src/infoview.ts#L375</a><br>
I think we can add a link to the diff right next to it.  You can show the diff with <code>workspace.openTextDocument</code> and <code>window.showTextDocument</code>.  Feel free to add a diff library to the dependencies.</p>

#### [ Chris Hughes (Jul 28 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130459741):
<p>I tried installing the lean VScode update, and now opening VScode instantly freezes my computer. Anyone else experiencing this problem?</p>

#### [ Kevin Buzzard (Jul 28 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130459799):
<p>If I find the extension in VS code I am only offered "disable" and "uninstall". I seem to be on version 0.11.11 (and on Ubuntu)</p>

#### [ Kevin Buzzard (Jul 28 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130460257):
<p>I have extension auto-update on. Which version of the extension are you having problems with? You're talking about a Windows machine right?</p>

#### [ Kevin Buzzard (Jul 28 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130460304):
<p>More to the point -- the bug is fixed for me and I have no problems with the extension. So I guess I upgraded safely. Anyone on Windows having the same problems with...Chris? Are you on 0.11.11? Oh -- you can't even tell?</p>

#### [ Chris Hughes (Jul 28 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130460321):
<p>I'm using the latest version of the extension and 20th April nightly for lean.</p>

#### [ Chris Hughes (Jul 28 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130460364):
<p>Maybe I should update lean?</p>

#### [ Ali Sever (Jul 28 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130460365):
<p>I reloaded lean, and now mine is crashing too. Thanks  a lot Chris</p>

#### [ Chris Hughes (Jul 28 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130460535):
<p>It doesn't hang provided I don't open a lean file. I am on 0.11.11</p>

#### [ Ali Sever (Jul 28 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130460606):
<p>how did you close your lean files?</p>

#### [ Chris Hughes (Jul 28 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130460631):
<p>Reinstall VSCode, and delete the folders containing the information about which lean files I had open</p>

#### [ Kevin Buzzard (Jul 28 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130461066):
<p>As a temporary measure you can uninstall the lean extension and then try and figure out how to install an older version. I can't reproduce here on linux; things are working fine for me. Can you switch logging on somehow? This might happen to every Windows user who has auto-update on.</p>

#### [ Gabriel Ebner (Jul 28 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130461142):
<p>I just tried to reproduce on windows, but everything works for me.  (elan is completely broken for me though)</p>

#### [ Kevin Buzzard (Jul 28 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130461168):
<p>Chris can you switch on some debugging output, have the current extension loaded, and then open a Lean file? What happens exactly after you open a lean file? You said your computer freezes? What OS are you using? Win7 or Win10?</p>

#### [ Chris Hughes (Jul 28 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130461228):
<p>Win10. My computer totally freezes, I can't even move my mouse.</p>

#### [ Chris Hughes (Jul 28 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130461376):
<p>What do you mean by "switch on some debugging output"?</p>

#### [ Gabriel Ebner (Jul 28 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130462163):
<p>If everything else fails, can you try to reinstall vscode and lean completely.  I am really at a loss here, there are almost no changes between vscode-lean 0.11.9 and 0.11.11, and none that look in any way dangerous.  I am running the lean 3.4.1 release on windows 10 and vscode 1.25.1 here.</p>

#### [ Simon Hudon (Jul 28 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130464752):
<blockquote>
<p><span class="user-mention" data-user-id="110043">@Gabriel Ebner</span>  <br>
If you want to implement it yourself, look at how _lean.revealPosition is implemented in the info view </p>
</blockquote>
<p>Thanks! I'll have a look.</p>
<blockquote>
<p>Sure, I am happy about new features. How did you extract the expected/actual type from the error message? Regex?</p>
</blockquote>
<p>What I did is split the error message into lines and find the line that says <code>"has type:"</code> and I take everything until I find the line announcing the expected type.</p>

#### [ Chris Hughes (Jul 28 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130471379):
<p><span class="user-mention" data-user-id="120256">@Ali Sever</span> I managed to revert my version of the VScode extension. This is how.</p>

#### [ Chris Hughes (Jul 28 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130471421):
<p>1. Go into windows command line and type <code>code --disable-extensions</code></p>

#### [ Chris Hughes (Jul 28 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130471431):
<p>2. Open VScode, save everything and uninstall the lean extension. Also disable automatic updates of extensions using <code>...</code> in the top right of the extensions pane.</p>

#### [ Chris Hughes (Jul 28 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130472297):
<p>3. Download the version <code>0.11.9</code> os the VScode extension from <a href="https://jroesch.gallery.vsassets.io/_apis/public/gallery/publisher/jroesch/extension/lean/0.11.9/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage" target="_blank" title="https://jroesch.gallery.vsassets.io/_apis/public/gallery/publisher/jroesch/extension/lean/0.11.9/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage">https://jroesch.gallery.vsassets.io/_apis/public/gallery/publisher/jroesch/extension/lean/0.11.9/assetbyname/Microsoft.VisualStudio.Services.VSIXPackage</a></p>

#### [ Chris Hughes (Jul 28 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130472301):
<p>4. Change the file extension of the downloaded file to .VSIX</p>

#### [ Chris Hughes (Jul 28 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130472326):
<p>Go into VScode extension click ... in the top right of the extensions pane and install from VSIX usingthe file you downloaded.</p>

#### [ Ali Sever (Jul 28 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130472911):
<p>Thanks Chris, awesome as always</p>

#### [ Kevin Buzzard (Jul 28 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130476732):
<p>So I just tried upgrading on a Win10 machine and I've got it working. It did crash VS code -- but a restart of VS code (twice) got it working in the end. It didn't take down the OS.</p>

#### [ Ali Sever (Jul 28 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130476989):
<p>by restart do you mean literally close the program and reopen it?</p>

#### [ Chris Hughes (Jul 28 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130477034):
<p>I couldn't do that because my computer was frozen.</p>

#### [ Kevin Buzzard (Jul 28 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130477037):
<p>The program (but not the OS) hung -- it became unresponsive. I restarted the program twice and got it working. I don't use Windows usually so I don't know if this is normal after an upgrade.</p>

#### [ Ali Sever (Jul 28 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130477041):
<p>My pc doesnt freeze, but only the toolbar at the top of VS code works</p>

#### [ Kenny Lau (Jul 29 2018 at 05:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130506182):
<p>So I opened task manager and discovered that VSCode is quick to take up all of the CPU and memory</p>

#### [ Moses Schönfinkel (Jul 29 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130513179):
<p>I've been playing around with this and I can do <code>#eval</code>, <code>#check</code> just fine, but the second I type <code>lemma</code> or <code>theorem</code>, Lean eats all my memory and hits disc to the point the system can't recover. Surprisingly enough <code>example</code> doesn't crash it.</p>

#### [ Moses Schönfinkel (Jul 29 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130513560):
<p>Actually it's VS Code that does that (unsurprisingly), because when I close the lean subprocess of VS-code parent, it doesn't fix anything.</p>

#### [ Gabriel Ebner (Jul 29 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130513763):
<p>Do you also get the high memory usage with the info view closed (the tab "Lean Messages")?</p>

#### [ Moses Schönfinkel (Jul 29 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130513774):
<p>Yes, it doesn't matter whether the info window is open or not. Just to clarify I'm on win 10.</p>

#### [ Moses Schönfinkel (Jul 29 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130513906):
<p>I run this off of an HDD, if that helps it completely thrashes the hard drive as well, but this may very well be just a side-effect of memory om-nom.</p>

#### [ Gabriel Ebner (Jul 29 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130513975):
<p>Yes, that's just swapping and it's because of the high memory usage.  The operating system just moves some stuff from RAM to HDD in order to make space.</p>

#### [ Gabriel Ebner (Jul 29 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130513984):
<p>Just to make sure: in the task manager, how much memory does the lean subprocess use compared to the rest of vscode?</p>

#### [ Moses Schönfinkel (Jul 29 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130514038):
<p>Negligable if I can even get it to update. The thing is, when I type <code>lemma</code> and I close VS within a second, it recovers. When I type <code>lemma</code> and I close just the <code>lean</code> subprocess of the tree, it doesn't recover. It's gigabytes of memory instantly for VSCode and some dozens of megabytes for lean.</p>

#### [ Patrick Massot (Jul 29 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130541475):
<blockquote>
<p>I managed to escape.  The only new feature is "ctrl+shift+p copy contents to comment", which copies the current content of the info view to a comment below the current line, as requested by <span class="user-mention" data-user-id="110031">@Patrick Massot</span>.</p>
</blockquote>
<p>Sorry I'm slow since my family returned from vacations. It works great! Next wish: do you think you could get VScode to offer to fold namespaces and sections like it folds statements and proofs?</p>

#### [ Kevin Buzzard (Jul 29 2018 at 23:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130541586):
<p>If VS code is capable of knowing which namespace we're in then I would find it super-helpful if this could be displayed in some way -- I sometimes find my cursor in the middle of a large file really wanting to know what namespace I'm in.</p>

#### [ Patrick Massot (Jul 29 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130541623):
<p>This would be really really helpful</p>

#### [ Patrick Massot (Jul 29 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130541627):
<p>What I'm asking for is easier, but having a substitute to what you're asking for is part of the motivation</p>

#### [ Gabriel Ebner (Jul 30 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130603708):
<p><em>Call for testers</em>: if you are on windows and experience hangs, could you please try this build of vscode-lean: <a href="https://1drv.ms/u/s!Au1u53SHpLowhTXMzMxSQI2Jy20o" target="_blank" title="https://1drv.ms/u/s!Au1u53SHpLowhTXMzMxSQI2Jy20o">https://1drv.ms/u/s!Au1u53SHpLowhTXMzMxSQI2Jy20o</a><br>
To install, go to the extension tab, click the three dots, and select "Install from VSIX"</p>

#### [ Mario Carneiro (Jul 30 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130604392):
<p>I went through the commits one at a time and the problem is <a href="https://github.com/leanprover/vscode-lean/commit/3dc37df" target="_blank" title="https://github.com/leanprover/vscode-lean/commit/3dc37df">https://github.com/leanprover/vscode-lean/commit/3dc37df</a> of all things</p>

#### [ Mario Carneiro (Jul 30 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130604463):
<p>the commit does a bit more than just adding <code>abbreviation</code> as a keyword as it claims; some additional stuff is added to the keyword recognition stuff at the end and I suspect it is triggering a memory leak in the regex parser</p>

#### [ Mario Carneiro (Jul 30 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130604647):
<p>More specifically, the regex <code>([^ \t\n\r{(\[,:]*(,\s*)?)*</code> at the end has the form <code>(a*b?)*</code> which can loop</p>

#### [ Gabriel Ebner (Jul 30 2018 at 23:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130604816):
<p>Thanks so much for finding this commit!!!  I reverted it and published a new version.</p>

#### [ Gabriel Ebner (Jul 30 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130604854):
<p>The regex was actually supposed to highlight the <code>bar</code> in <code>mutual def foo, bar</code>.  I did not expect a platform-dependent bug in the regex engine here..</p>

#### [ Mario Carneiro (Jul 30 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130605004):
<p>I don't think you have to completely revert it; there is nothing wrong with adding <code>abbreviation</code> to the list, only the regex needs to be tweaked so that it doesn't match an infinite number of empty strings</p>

#### [ Mario Carneiro (Jul 30 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130605237):
<p>I think  this should work for matching <code>a, b</code> in <code>def a, b</code> (the final capturing group): <code>([^ \t\n\r{(\[,:]+(,\s*[^ \t\n\r{(\[,:]+)*)</code></p>

#### [ Kevin Buzzard (Jul 30 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130606974):
<p>Thanks Mario! This caused my users a certain amount of grief today</p>

#### [ Johan Commelin (Aug 03 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130823107):
<p>Gabriel, here is another thing that might be useful. If I have snippet like:</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">:</span> <span class="n">group</span> <span class="n">X</span> <span class="o">:=</span>
<span class="o">{</span> <span class="c1">-- cursor is here</span>
<span class="o">}</span>
</pre></div>

#### [ Johan Commelin (Aug 03 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130823154):
<p>Then the window displaying the goals knows exactly what is wrong: I need to supply <code>zero</code> and <code>mul</code> and stuff like that.</p>

#### [ Johan Commelin (Aug 03 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130823165):
<p>So it would be nice if the autocomplete would show exactly those options. Now I often find myself clicking on the <code>{</code> to see in the Goal Window which stuff I still need to supply.</p>

#### [ Johan Commelin (Aug 03 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130823171):
<p>Alternatively, maybe some snippet on steroids could just fill them all in (with <code>sorry</code>'s). But my snippet-fu is non-existent.</p>

#### [ Kenny Lau (Aug 03 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130825053):
<p>ctrl+alt+shift+enter</p>

#### [ Johan Commelin (Aug 03 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130825062):
<p>What the hack is that supposed to do?</p>

#### [ Johan Commelin (Aug 03 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130825113):
<p>Is there a way to ask VScode "Hey, what does the shortcut do?"?</p>

#### [ Kenny Lau (Aug 03 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130825138):
<p>it lets you view all the messages</p>

#### [ Kenny Lau (Aug 03 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130825143):
<p>instead of just the one on your line</p>

#### [ Kevin Buzzard (Aug 03 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130827024):
<p>The window on the bottom which displays the errors and warnings is the place to look for this. Sometimes you have to pull it into existence</p>

#### [ Johan Commelin (Aug 03 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/130827173):
<p>Cool! I didn't know I could pull something up there!</p>

#### [ Johan Commelin (Aug 10 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/131221794):
<p>In VScode, if I select some text that is to be replaced, and I start typing a string the expected behaviour occurs. Except... Except when I start the replacement string with a <code>\</code>, then it is not expanded into a unicode character. So if I select "foobar" and then type <code>\lam x y</code>, I don't get a cool lambda.</p>

#### [ Johan Commelin (Aug 10 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/131221810):
<p><span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> <span class="emoji emoji-2b06" title="up">:up:</span></p>

#### [ Kevin Buzzard (Aug 10 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/131229457):
<p>I deal with this by writing what I want beforehand and copying it with ctrl-x into the whatever-that-thing-is-called buffer so I can use ctrl-v to paste when I'm replacing</p>

#### [ Kenny Lau (Aug 10 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/131229490):
<p>I deal with this by selecting "foobar", deleting the text, and then type <code>\</code>.</p>

#### [ Johan Commelin (Aug 10 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/131229622):
<p>Right, I use both those way to deal with it. Still, I thought I would mention it, because maybe there is an easy fix. And sometimes I forget to deal with, and then <span class="emoji emoji-1f622" title="cry">:cry:</span></p>

#### [ Gabriel Ebner (Aug 10 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/131229745):
<p>I'm not sure I understand this correctly.  You write <code>foobar</code> and then want <code>λ x, f</code> instead.  So instead of deleting <code>foobar</code>, you select it and then start typing <code>\lam x, f</code>?</p>

#### [ Johan Commelin (Aug 10 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/131229798):
<p>Right</p>

#### [ Gabriel Ebner (Aug 10 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/131229807):
<p>This shouldn't be too hard to add.  I just never used an editor like that.</p>

#### [ Johan Commelin (Aug 10 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/131229879):
<p>For me it would usually be <code>ciw\lam x ,y</code>... still need to look at <code>lean.vim</code> and all those other plugins for the LSP.</p>

#### [ Gabriel Ebner (Aug 10 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/131229906):
<p>I'm a vim addict as well.  There is a pretty good vim plugin for vscode that I'm using: <a href="https://github.com/VSCodeVim/Vim" target="_blank" title="https://github.com/VSCodeVim/Vim">https://github.com/VSCodeVim/Vim</a> .<br>
And <code>ciw\lam x ,y</code> works as expected!</p>

#### [ Johan Commelin (Aug 10 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/131229948):
<p>Ok, I should try that out.</p>

#### [ Johan Commelin (Aug 10 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/131229967):
<p>Otoh, if I get actual vim working, then I could run <code>lean</code> on a server, and connect via <code>mosh</code>. Then my crappy laptop would have superfast Lean!</p>

#### [ Gabriel Ebner (Aug 10 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/131230148):
<p>And it should work in the latest version of the vscode extension.</p>

#### [ Kevin Buzzard (Aug 10 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/131234613):
<p>You could just do this with emacs, right? </p>
<p>I should prod William about CoCalc. I am writing an introductory worksheet for beginning UGs teaching basic logic, using Sphinx and "try it!". I realised that no undergraduate would even be able to do my first maths example sheet unless they know how to construct and destruct or/and etc.</p>

#### [ Johan Commelin (Aug 10 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/131244404):
<blockquote>
<p>I should prod William about CoCalc. </p>
</blockquote>
<p>Yes! I would love to hear more updates from CoCalc.</p>

#### [ Gabriel Ebner (Aug 13 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/132058162):
<blockquote>
<p>Gabriel, here is another thing that might be useful. If I have snippet like:</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">:</span> <span class="n">group</span> <span class="n">X</span> <span class="o">:=</span>
<span class="o">{</span> <span class="c1">-- cursor is here</span>
<span class="o">}</span>
</pre></div>


<p>Then the window displaying the goals knows exactly what is wrong: I need to supply zero and mul and stuff like that.<br>
So it would be nice if the autocomplete would show exactly those options.</p>
</blockquote>
<p>This will probably not happen in Lean 3.</p>

#### [ Kenny Lau (Aug 18 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/132376683):
<p>Ctrl+A is not working for me (I'm on Windows 10)</p>

#### [ Kenny Lau (Aug 18 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/132376850):
<p>wait it works now</p>

#### [ Johan Commelin (Aug 30 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133076051):
<p><span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> While in Orsay we had some dreams and fantasies... they're recorded over here: <a href="https://github.com/leanprover-community/mathlib/wiki/VScode-wishlist" target="_blank" title="https://github.com/leanprover-community/mathlib/wiki/VScode-wishlist">https://github.com/leanprover-community/mathlib/wiki/VScode-wishlist</a> <span class="emoji emoji-1f61c" title="stuck out tongue wink">:stuck_out_tongue_wink:</span></p>

#### [ Patrick Massot (Aug 30 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133076648):
<p>some of them would probably need a more detailed description for people who didn't attend the dicussion</p>

#### [ Gabriel Ebner (Aug 30 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133076769):
<p>I think I can make sense of most of them.  It reads like a wishlist for Lean 4.<br>
What is "help with naming conventions"?</p>

#### [ Johan Commelin (Aug 30 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133076853):
<p>"Help with naming conventions": Given a statement, figure out the name.</p>

#### [ Johan Commelin (Aug 30 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133076906):
<p>I don't know much about Lean 4. But we also decided that we were to often saying: "That might be easier in Lean 4" etc...</p>

#### [ Johan Commelin (Aug 30 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133076989):
<p>[kidding] Oooh, and we want MS Word's Clippy for Lean: "It looks like you are trying to prove something by induction. Would you like me to write the skeleton of the proof for you?" [/kidding]</p>

#### [ Chris Hughes (Aug 30 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133076994):
<p>Can I add pp option to display types of proofs in your goal or local context as well. Maybe target types of coercions as well.</p>

#### [ Gabriel Ebner (Aug 30 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133078301):
<p>I'm just saying that most points on the list are either infeasible right now, or shouldn't go into the vscode extension.<br>
If you want to start experimenting right now, I think the naming convention automation is the lowest hanging fruit.  You can implement <code>#how_do_you_call ∀ x y, x &lt; y → x - y = 0</code> as a user command for example.</p>

#### [ Gabriel Ebner (Aug 30 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133078602):
<p>The next best is maybe "turn current goal into lemma".  You can do this as a tactic that outputs the text for the lemma as an error message.  The user can then copy&amp;paste it where they want.  Last time I talked with Rob and Johannes there was the suggestion to parse tags like <code>&lt;insert-above&gt;lemma foo : a → b := sorry&lt;/insert-above&gt;</code> in the error messages, but imho that's a bit too hacky unless there is a significant need for it.</p>

#### [ Gabriel Ebner (Aug 30 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133078667):
<p>For the other "clippy" and refactoring stuff, I'd really wait.</p>

#### [ Johan Commelin (Aug 30 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133078880):
<p>Clippy was not really serious...</p>

#### [ Johan Commelin (Aug 30 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133078893):
<p>The turn goal into lemma tactic would be really cool I think.</p>

#### [ Johan Commelin (Aug 30 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133078902):
<p>And I might even be able to write it with a bit of help.</p>

#### [ Johan Commelin (Aug 30 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133078912):
<p><code>#how_do_you_call</code> would be awesome, and I have no clue whatsoever how to write it.</p>

#### [ Johan Commelin (Aug 31 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133122224):
<p><span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> Currently <code>\func</code> points to an arrow that is frozen by core. We thought that it might be useful to point it to <code>⥤</code> instead, so that we can use that arrow for functors in the category lib.</p>

#### [ Gabriel Ebner (Aug 31 2018 at 15:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133122657):
<p>Ah I see, <code>⇒</code> is already used for the relators.  Another unused option is <code>⟹</code>, written <code>\==&gt;</code>.</p>

#### [ Mario Carneiro (Aug 31 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133122712):
<p>I think that this is used for natural transformations</p>

#### [ Gabriel Ebner (Aug 31 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133122756):
<p>Yes, that would've been my next question.  What about morphisms and natural transformations?</p>

#### [ Johan Commelin (Aug 31 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133122769):
<p><code>\hom</code> and <code>\==&gt;</code></p>

#### [ Johan Commelin (Aug 31 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133122815):
<p>It is really <code>\func</code> that's been messed up. For the rest we have nice solutions.</p>

#### [ Johan Commelin (Aug 31 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133122838):
<p>Really the thing for relators should have been local notation. Then <em>you</em> wouldn't have to do anything.</p>

#### [ Johan Commelin (Aug 31 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133122850):
<p>Now we are kindly asking you to point <code>\func</code> to this goofy arrow that looks enough like what we want.</p>

#### [ Gabriel Ebner (Aug 31 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133123049):
<p>I definitely agree on the local notation part.  I'd just like to avoid changing existing abbreviations if possible.</p>

#### [ Gabriel Ebner (Aug 31 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133123074):
<p>You can easily add the arrow yourself: just add a new line with <code>"func": "⟹",</code> to this json file <a href="https://github.com/leanprover/vscode-lean/blob/master/translations.json#L1290" target="_blank" title="https://github.com/leanprover/vscode-lean/blob/master/translations.json#L1290">https://github.com/leanprover/vscode-lean/blob/master/translations.json#L1290</a> and make a PR.</p>

#### [ Johan Commelin (Aug 31 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133123137):
<p>Right... I'm currently doing something slightly related... writing a Python script that turns that file into Compose-key sequences.</p>

#### [ Johan Commelin (Aug 31 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133123226):
<p>So I should not overwrite <code>\functor</code>? But adding <code>\func</code> is ok?</p>

#### [ Gabriel Ebner (Aug 31 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133123230):
<p>I feel like we need a separate repository for this file and all associated scripts soon.  I have also written a converter: <a href="https://github.com/gebner/m17n-lean" target="_blank" title="https://github.com/gebner/m17n-lean">https://github.com/gebner/m17n-lean</a></p>

#### [ Gabriel Ebner (Aug 31 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133123245):
<p>As I said, I'd rather avoid overwriting.  But I'm happy either way.</p>

#### [ Johan Commelin (Aug 31 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133123319):
<p>I guess no-one is using that abbreviation at the moment. So I'dd rather overwrite. Chances are way higher that someone will write <code>\functor</code> when doing categories.</p>

#### [ Johan Commelin (Aug 31 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133123351):
<p><a href="https://github.com/jcommelin/vscode-lean/pull/1" target="_blank" title="https://github.com/jcommelin/vscode-lean/pull/1">https://github.com/jcommelin/vscode-lean/pull/1</a></p>

#### [ Sean Leather (Aug 31 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133123352):
<blockquote>
<p>I feel like we need a separate repository for this file and all associated scripts soon.  I have also written a converter: <a href="https://github.com/gebner/m17n-lean" target="_blank" title="https://github.com/gebner/m17n-lean">https://github.com/gebner/m17n-lean</a></p>
</blockquote>
<p>I've thought something similar, in particular for providing a single source for VS Code, Emacs, and Vim keybindings.</p>

#### [ Gabriel Ebner (Aug 31 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133123354):
<p>Ok, then.  You can still get the old arrow with <code>\r=</code> etc.</p>

#### [ Johan Commelin (Aug 31 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133123366):
<p>Exactly</p>

#### [ Gabriel Ebner (Aug 31 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133123377):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> You made a PR to your own fork.</p>

#### [ Johan Commelin (Aug 31 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133123384):
<p>Oops, that is silly</p>

#### [ Johan Commelin (Aug 31 2018 at 15:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133123528):
<p><a href="https://github.com/leanprover/vscode-lean/pull/85" target="_blank" title="https://github.com/leanprover/vscode-lean/pull/85">https://github.com/leanprover/vscode-lean/pull/85</a></p>

#### [ Gabriel Ebner (Aug 31 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133123710):
<p>And deployed.</p>

#### [ Johan Commelin (Aug 31 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133123835):
<p><span class="user-mention" data-user-id="110524">@Scott Morrison</span> Voila! You can update the arrow for functors in your lib!</p>

#### [ Johan Commelin (Aug 31 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133123932):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="nn">fileinput</span>
<span class="kn">import</span> <span class="nn">re</span>

<span class="n">pat</span> <span class="o">=</span> <span class="n">re</span><span class="o">.</span><span class="n">compile</span><span class="p">(</span><span class="s1">&#39;&quot;(.*)&quot;:&quot;(.*)&quot;&#39;</span><span class="p">,</span> <span class="n">re</span><span class="o">.</span><span class="n">MULTILINE</span><span class="p">)</span>

<span class="k">for</span> <span class="n">line</span> <span class="ow">in</span> <span class="n">fileinput</span><span class="o">.</span><span class="n">input</span><span class="p">():</span>
    <span class="n">m</span> <span class="o">=</span> <span class="n">pat</span><span class="o">.</span><span class="n">match</span><span class="p">(</span><span class="n">line</span><span class="p">)</span>
    <span class="n">pre</span> <span class="o">=</span> <span class="n">m</span><span class="o">.</span><span class="n">group</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
    <span class="n">suf</span> <span class="o">=</span> <span class="n">m</span><span class="o">.</span><span class="n">group</span><span class="p">(</span><span class="mi">2</span><span class="p">)</span>
    <span class="n">hooked_pre</span> <span class="o">=</span> <span class="p">[</span> <span class="s1">&#39;&lt;&#39;</span> <span class="o">+</span> <span class="n">c</span> <span class="o">+</span> <span class="s1">&#39;&gt;&#39;</span> <span class="k">for</span> <span class="n">c</span> <span class="ow">in</span> <span class="nb">list</span><span class="p">(</span><span class="n">pre</span><span class="p">)</span> <span class="p">]</span>
    <span class="n">s</span> <span class="o">=</span> <span class="s1">&#39;&lt;Multi_key&gt; &#39;</span> <span class="o">+</span> <span class="s1">&#39; &#39;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="n">hooked_pre</span><span class="p">)</span> <span class="o">+</span> <span class="s1">&#39; : &quot;&#39;</span> <span class="o">+</span> <span class="n">suf</span> <span class="o">+</span> <span class="s1">&#39;&quot;    # &#39;</span> <span class="o">+</span> <span class="n">pre</span>
    <span class="k">print</span><span class="p">(</span><span class="n">s</span><span class="p">)</span>
</pre></div>

#### [ Johan Commelin (Aug 31 2018 at 15:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133123942):
<p>That's the silly thing that I'm trying</p>

#### [ Johan Commelin (Aug 31 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133124968):
<p><span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> By the way, if the original arrow becomes unfrozen in Lean 4, then we might want to switch back...</p>

#### [ Mario Carneiro (Aug 31 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133125220):
<p>are <em>you</em> going to claim it as a global notation?</p>

#### [ Johan Commelin (Aug 31 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133125512):
<p>Of course! We are evil!</p>

#### [ Mario Carneiro (Aug 31 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133125588):
<p>I'm only allowing the notations in category theory now because the arrows are bizarre</p>

#### [ Johan Commelin (Aug 31 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133125750):
<p>Any arrow that is not bizarre can be local. That's fine with me. We'll be locally evil.</p>

#### [ Patrick Massot (Aug 31 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133127381):
<p>Gabriel, why do you hardcode the leader key?</p>

#### [ Gabriel Ebner (Aug 31 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128408):
<p>Leader = backslash? It used to be backslash in emacs, and I just copied that.  There is no fundamental reason why it has to be a backslash.  What do you have in mind, <code>§</code>?  We can easily support that with a configuration option.  I don't know whether we could support "right-control" as a leader key at all.</p>

#### [ Patrick Massot (Aug 31 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128462):
<p>Yes, I mean leader as in vim terminology. The point is that \  is very inconvenient on a French keyboard. In vim I always use comma for that</p>

#### [ Mario Carneiro (Aug 31 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128489):
<p>wouldn't comma give you a lot of false positives?</p>

#### [ Patrick Massot (Aug 31 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128498):
<p>only if the abbreviation starts with a space</p>

#### [ Patrick Massot (Aug 31 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128511):
<p>comma is always followed by space (at least in France)</p>

#### [ Mario Carneiro (Aug 31 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128524):
<p>it's usually followed by a space in mathlib, but there are a significant fraction with no space</p>

#### [ Patrick Massot (Aug 31 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128577):
<p>under what kind of circumstances?</p>

#### [ Mario Carneiro (Aug 31 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128608):
<p><code>λ⟨a,b⟩, </code> and such</p>

#### [ Patrick Massot (Aug 31 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128616):
<p>this is wrong</p>

#### [ Patrick Massot (Aug 31 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128617):
<p>should be a, b</p>

#### [ Mario Carneiro (Aug 31 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128621):
<p>also between rewrite rules and simp rules sometimes</p>

#### [ Mario Carneiro (Aug 31 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128629):
<p>I agree, I try to keep a space after a comma but not everyone does</p>

#### [ Patrick Massot (Aug 31 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128630):
<p>So switching to comma would improve typography in mathlib!</p>

#### [ Johan Commelin (Aug 31 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128686):
<p>You could map your CAPS LOCK key to §, and then use that as a leader.</p>

#### [ Johan Commelin (Aug 31 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128691):
<p>Or just map your caps lock to <code>\</code></p>

#### [ Gabriel Ebner (Aug 31 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128705):
<p>I thought French keyboards have a key for §?</p>

#### [ Patrick Massot (Aug 31 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128729):
<p>no</p>

#### [ Patrick Massot (Aug 31 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128813):
<p><a href="https://fr.wikipedia.org/wiki/Fichier:Clavier-Azerty-France.svg" target="_blank" title="https://fr.wikipedia.org/wiki/Fichier:Clavier-Azerty-France.svg">https://fr.wikipedia.org/wiki/Fichier:Clavier-Azerty-France.svg</a></p>

#### [ Gabriel Ebner (Aug 31 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128815):
<p>Oh, so wikipedia has been lying to me.  I thought it is right next to shift.  <a href="https://en.wikipedia.org/wiki/AZERTY#/media/File:Azerty_fr.svg" target="_blank" title="https://en.wikipedia.org/wiki/AZERTY#/media/File:Azerty_fr.svg">https://en.wikipedia.org/wiki/AZERTY#/media/File:Azerty_fr.svg</a></p>

#### [ Johan Commelin (Aug 31 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128844):
<p>It seems to be <code>Shift + !</code></p>

#### [ Gabriel Ebner (Aug 31 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128845):
<p>That picture also shows § right next to the right shift key?</p>

#### [ Patrick Massot (Aug 31 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128849):
<p>it's there, but not on direct access</p>

#### [ Patrick Massot (Aug 31 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128862):
<p>it's better than \ which is really hard to type, but comma is direct access</p>

#### [ Johan Commelin (Aug 31 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133128913):
<p>Make <code>ù</code> the leader (-;</p>

#### [ Patrick Massot (Aug 31 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133129047):
<p>indeed this would also probably be fine (this character is used in only one word)</p>

#### [ Edward Ayers (Aug 31 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133129165):
<p>On a different subject: are there any plans to add a code formatter to vscode extension?</p>

#### [ Gabriel Ebner (Aug 31 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133129198):
<p>I think there are plans to add a code formatter to Lean 4.</p>

#### [ Patrick Massot (Aug 31 2018 at 17:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133129243):
<p>what is a code formatter?</p>

#### [ Edward Ayers (Aug 31 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133129312):
<blockquote>
<p>what is a code formatter?</p>
</blockquote>
<p>You slam a button and it adds spaces in the proper places and enforces some style guide things.</p>

#### [ Edward Ayers (Aug 31 2018 at 17:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133129332):
<p>Basically it adds and removes spaces until the code looks nice</p>

#### [ Patrick Massot (Aug 31 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133129448):
<p>that would be really nice</p>

#### [ Kevin Buzzard (Aug 31 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133130026):
<p>Presumably it only works for code which can be made to look nice by addition and removal of spaces</p>

#### [ Edward Ayers (Aug 31 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133130061):
<p>I think that you can in theory perform arbitrary textual transformations</p>

#### [ Gabriel Ebner (Aug 31 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133131128):
<p><a href="/user_uploads/3121/PIoL-GV9fsWWF6LSXn8cb1Cx/vscode-lean-leader.png" target="_blank" title="vscode-lean-leader.png">Coming soon to a vscode near you.</a> I'm on vacation now, <span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span>  can publish updates to the vscode extension if there's anything urgent.</p>
<div class="message_inline_image"><a href="/user_uploads/3121/PIoL-GV9fsWWF6LSXn8cb1Cx/vscode-lean-leader.png" target="_blank" title="Coming soon to a vscode near you."><img src="/user_uploads/3121/PIoL-GV9fsWWF6LSXn8cb1Cx/vscode-lean-leader.png"></a></div>

#### [ Bryan Gin-ge Chen (Aug 31 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133131260):
<blockquote>
<p>On a different subject: are there any plans to add a code formatter to vscode extension?</p>
</blockquote>
<p>There's also an open issue on the lean repository related to this <a href="https://github.com/leanprover/lean/issues/1970" target="_blank" title="https://github.com/leanprover/lean/issues/1970">here</a>.</p>

#### [ Patrick Massot (Aug 31 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133131691):
<p>Thank you very much Gabriel! Together with the TAB thing it really makes Leaning more comfortable</p>

#### [ Ali Sever (Sep 02 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133208406):
<p>My windows updated and now vscode says lean doesn't work. I tried using lean --version and I got "segmentation fault". Even if I use PATH ***, I can't get lean --version to work. Any suggestions?</p>

#### [ Ali Sever (Sep 03 2018 at 19:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133271161):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Hi Mario, I recently had an issue with a windows insider update which completely prevented me from using lean. Kevin told me that I should warn you about this, since there's a chance that whatever caused this might be in the next windows update (which google says is on October 10th). I'm afraid I can't help you much about the error, but I've put everything I know here <a href="https://github.com/leanprover/lean/issues/1972" target="_blank" title="https://github.com/leanprover/lean/issues/1972">https://github.com/leanprover/lean/issues/1972</a>.</p>

#### [ Kenny Lau (Sep 04 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133300183):
<p><a href="/user_uploads/3121/Jt5Tckc7s01asToD4wpB1VRy/2018-09-04.png" target="_blank" title="2018-09-04.png">2018-09-04.png</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/Jt5Tckc7s01asToD4wpB1VRy/2018-09-04.png" target="_blank" title="2018-09-04.png"><img src="/user_uploads/3121/Jt5Tckc7s01asToD4wpB1VRy/2018-09-04.png"></a></div>

#### [ Kevin Buzzard (Sep 04 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133300973):
<p>Do you know about <code> ``` </code>? It makes your code easier to cut and paste ;-)</p>

#### [ Kenny Lau (Sep 04 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133301089):
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span>
<span class="n">class</span> <span class="n">MWE</span> <span class="kn">extends</span> <span class="n">has_zero</span> <span class="n">A</span>
</pre></div>

#### [ Johan Commelin (Sep 04 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133301106):
<p>Also, why did you put that in this thread?</p>

#### [ Kenny Lau (Sep 04 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133301134):
<p>because it's about VScode</p>

#### [ Patrick Massot (Sep 04 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133301273):
<p>I guess Kenny wants to complain about syntax highlighting</p>

#### [ Kevin Buzzard (Sep 04 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133302054):
<p>Oh I see. He's as cryptic as ever :-)</p>

#### [ Bryan Gin-ge Chen (Sep 04 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133309635):
<div class="codehilite"><pre><span></span><span class="kn">set_option</span> <span class="n">class</span><span class="bp">.</span><span class="n">instance_max_depth</span> <span class="mi">5</span>
</pre></div>


<p>This one looks weird too (with <code>class</code> colored differently from <code>.instance_max_depth</code></p>

#### [ Bryan Gin-ge Chen (Sep 04 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133311084):
<p>I've submitted <a href="https://github.com/leanprover/vscode-lean/pull/87" target="_blank" title="https://github.com/leanprover/vscode-lean/pull/87">a PR</a> for Kenny and my examples.</p>

#### [ Kenny Lau (Sep 05 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133393460):
<p>I just discovered that you can indent a bunch of lines by highlighting them and then pressing <code>ctrl+]</code>, and de-indent by <code>ctrl+[</code></p>

#### [ Johan Commelin (Sep 05 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133393516):
<p>Alternative: Tab or Shift-Tab</p>

#### [ Patrick Massot (Sep 05 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133393518):
<p>also works with Tab and Shift-Tab</p>

#### [ Kenny Lau (Sep 05 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133393536):
<p>oh right</p>

#### [ Johan Commelin (Sep 05 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133393703):
<p>Also, you should learn Vim, so that you can be disgusted by <code>Ctrl-[</code> being a shortcut for something silly like that (-;</p>

#### [ Kevin Buzzard (Sep 05 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133393766):
<p>Did you try <code>\G</code>?</p>

#### [ Kevin Buzzard (Sep 05 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133393773):
<p>that's even more bizarre</p>

#### [ Johan Commelin (Sep 05 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133393829):
<p>Right, that should clearly expand to <code>α</code>.</p>

#### [ Patrick Massot (Sep 05 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133394002):
<p>Same with \R (for rings) and \M (for modules), they should expand to α</p>

#### [ Kevin Buzzard (Sep 05 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133394461):
<p>I am writing some Noetherian code and of course using Mario's work on Noetherian modules, and you can tell exactly who wrote each line because of this convention :-)</p>

#### [ Kevin Buzzard (Sep 05 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133395143):
<blockquote>
<p>Same with \R (for rings) and \M (for modules), they should expand to α</p>
</blockquote>
<p>or maybe \beta, depending on...um...a random choice I guess</p>

#### [ Bryan Gin-ge Chen (Sep 06 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133409881):
<p>Has anyone had any luck with the "Bracket pair colorizer" extension that's suggested in <a href="https://github.com/leanprover/vscode-lean/blob/master/README.md#other-potentially-helpful-settings" target="_blank" title="https://github.com/leanprover/vscode-lean/blob/master/README.md#other-potentially-helpful-settings">the readme</a>? It doesn't seem to work (on lean files) right out of the box (perhaps because lean doesn't appear on <a href="https://prismjs.com/#languages-list" target="_blank" title="https://prismjs.com/#languages-list">the Prism.js list of languages</a>), though I like how it looks on other filetypes.</p>

#### [ Kenny Lau (Sep 07 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133511543):
<p>I opened my file called <code>dfinsupp_quotient.lean</code> in VSCode, and then closed it, and then rebuilt Lean, and then rebuilt mathlib, and then opened it again in VSCode, but its content was suddenly gone.</p>

#### [ Kenny Lau (Sep 07 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133511668):
<p>my file is independent from mathlib, it's in my own sandbox</p>

#### [ Chris Hughes (Sep 07 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133511721):
<p>Sounds like you didn't save. Did you open if from a file explorer, or just open VScode, and it was there because it was the last thing you were looking at?</p>

#### [ Kenny Lau (Sep 07 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133511779):
<p>I always save my file after I type every word</p>

#### [ Kenny Lau (Sep 07 2018 at 15:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133511792):
<p>the latter</p>

#### [ Kenny Lau (Sep 07 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133511866):
<p>also, now, whenever I open VSCode a second tab would magically appear, and the name of the tab would be "null", and whenever I click on "null" it would disappear</p>

#### [ Kenny Lau (Sep 07 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133511941):
<p><a href="/user_uploads/3121/JQPkbB2KJ2oZvqaMMl03_ttK/2018-09-07-2.png" target="_blank" title="2018-09-07-2.png">2018-09-07-2.png</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/JQPkbB2KJ2oZvqaMMl03_ttK/2018-09-07-2.png" target="_blank" title="2018-09-07-2.png"><img src="/user_uploads/3121/JQPkbB2KJ2oZvqaMMl03_ttK/2018-09-07-2.png"></a></div>

#### [ Kenny Lau (Sep 07 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133511963):
<p>whenever I click on the tab "null", the tab "null" itself would disappear</p>

#### [ Kenny Lau (Sep 07 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133512015):
<p>I don't really mind spending the next day retyping everything, I just want to make sure that it won't happen again</p>

#### [ Chris Hughes (Sep 07 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133512309):
<p>What happens if you open from a file explorer?</p>

#### [ Kenny Lau (Sep 07 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133512331):
<p>it is also empty</p>

#### [ Kenny Lau (Sep 08 2018 at 10:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133560303):
<p>Ctrl+space does not show the defining fields of a structure/inductive/class, such as filter.univ_sets</p>

#### [ Kenny Lau (Sep 08 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133560389):
<p>hmm, it does show <code>filter.univ_sets</code>.</p>

#### [ Kenny Lau (Sep 08 2018 at 10:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133560392):
<p>But I do remember there are some things that Ctrl+Space doesn't show</p>

#### [ Chris Hughes (Sep 08 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133561694):
<p>Sometimes it doesn't show things in a namespace that you have open if you type <code>finset.x</code> instead of <code>x</code></p>

#### [ Kevin Buzzard (Sep 08 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133562956):
<p>In my experience sometimes it doesn't show something, and then you hit escape and then ctrl-space again, and then it shows them, although I noted this behaviour months ago and cannot say for sure that it still occurs.</p>

#### [ Kenny Lau (Sep 08 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133582528):
<p>Is there a quick way to change <code>(lorem ipsum dolor)</code> to <code>{lorem ipsum dolor}</code> etc?</p>

#### [ Mario Carneiro (Sep 08 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133582636):
<p>you can use <code>Select to Bracket</code> (no default key command)</p>

#### [ Bryan Gin-ge Chen (Sep 08 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133583057):
<p>The vim incantation <a href="https://stackoverflow.com/questions/25405072/quickest-way-to-change-a-pair-of-parenthesis-to-brackets-in-vim" target="_blank" title="https://stackoverflow.com/questions/25405072/quickest-way-to-change-a-pair-of-parenthesis-to-brackets-in-vim"><code>%r}``r{</code></a> would do this, but unfortunately it doesn't work in the VScode vim extension yet (maybe <a href="https://github.com/VSCodeVim/Vim/pull/3028" target="_blank" title="https://github.com/VSCodeVim/Vim/pull/3028">soon</a>?).</p>

#### [ Olli (Sep 08 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133583174):
<p>VSCode's vim extension has a feature from vim-surround enabled by default, so <code>cs)}</code> works</p>

#### [ Bryan Gin-ge Chen (Sep 09 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133584707):
<p>Cool, I didn't know that! However, on my macOS system, the "surround" commands don't work when the lean extension is enabled. They do work on my windows machine (and when I disable the lean extension, or on non-lean files). Very strange...</p>

#### [ Bryan Gin-ge Chen (Sep 09 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133584754):
<p>When I type <code>cs</code> on my mac with the lean extension enabled, it deletes the whole line and puts me in insert mode.</p>

#### [ Bryan Gin-ge Chen (Sep 09 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133584862):
<p>Oh wait it's working now. No idea what's going on.</p>

#### [ Kenny Lau (Sep 09 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133608201):
<p>Is there a way to see which file is being compiled?</p>

#### [ Keeley Hoek (Sep 10 2018 at 05:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133636317):
<p>When an identifier that ends with number has an error message, only the part up to the number is underlined. Moreover, clicking an identifier which ends with a number will not highlight its usages in the rest of the open file, as usually happens</p>

#### [ Bryan Gin-ge Chen (Sep 10 2018 at 05:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133636542):
<p>The same things happen with dots, though maybe the current highlighting behavior is preferable in that case.</p>

#### [ Keeley Hoek (Sep 12 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133812963):
<p>Is there a fundamental reason why the partial <code>tactic.trace ...</code> output of a tactic is only displayed in the editor after tactic execution has completed (commonly, failed)?</p>

#### [ Sebastian Ullrich (Sep 12 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133813596):
<p>Yeah, the current server protocol doesn't really allow for another (efficient) option. I've thought about this, but it's not clear at all how this could work especially when we move to storing messages in an immutable Lean data structure.</p>

#### [ Kenny Lau (Sep 13 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133867290):
<p><a href="/user_uploads/3121/NkA0T9DQQznkuHgdbNbPKEkN/2018-09-13.png" target="_blank" title="2018-09-13.png">2018-09-13.png</a> <br>
misplaced red underscore</p>
<div class="message_inline_image"><a href="/user_uploads/3121/NkA0T9DQQznkuHgdbNbPKEkN/2018-09-13.png" target="_blank" title="2018-09-13.png"><img src="/user_uploads/3121/NkA0T9DQQznkuHgdbNbPKEkN/2018-09-13.png"></a></div>

#### [ Kenny Lau (Sep 13 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133867293):
<p>code:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="n">nat</span> <span class="o">:=</span> <span class="o">(</span><span class="bp">_</span><span class="o">)</span>
<span class="kn">example</span> <span class="o">:</span> <span class="n">nat</span> <span class="o">:=</span> <span class="o">(</span><span class="bp">_</span> <span class="o">:</span> <span class="n">nat</span><span class="o">)</span>
</pre></div>

#### [ Kenny Lau (Sep 13 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133867301):
<p>line 1 is normal, line 2 is not</p>

#### [ Kevin Buzzard (Sep 13 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133868544):
<p>Ned Summers showed me examples of this which were really crazy -- he seemed to be able to move the red line an arbitrary amount to the left :-)</p>

#### [ Patrick Massot (Sep 13 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133868553):
<p>I guess this has nothing to do with VScode. The problem should be in lean server mode, no?</p>

#### [ Gabriel Ebner (Sep 13 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133881106):
<p>"Moving error messages an <em>arbitrary</em> amount to the left" is a known bug in the presence of calligraphic characters.  Please just don't write errors when using calligraphic (or fraktur) characters.</p>

#### [ Gabriel Ebner (Sep 13 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133881171):
<p>The problem is that vscode counts the number of utf-16 words (2 bytes), while lean counts the number of Unicode codepoints (can be larger than 2 bytes).</p>

#### [ Johan Commelin (Sep 13 2018 at 14:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133881477):
<p>Ouch... does it make sense to report this bug to VScode? Or is it not worth it?</p>

#### [ Gabriel Ebner (Sep 13 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133881661):
<p>It's by design I think. The language server protocol specifies this behavior explicitly.  There is an issue in the github repo, but I am not sure if they'll ever change it.  Note that JavaScript also uses this utf-16 indexing for strings.</p>

#### [ Gabriel Ebner (Sep 13 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133881694):
<p>There is another possible bug.  Vscode and lean also disagree on what line endings are recognized.  Vscode recognizes <code>\r</code>, but lean doesn't.</p>

#### [ Johan Commelin (Sep 13 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133881817):
<p>Lean is pretty sane. <span class="emoji emoji-1f604" title="big smile">:big_smile:</span></p>

#### [ Kevin Buzzard (Sep 13 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133881836):
<p>Indeed Ned was doing category theory and there were calligraphic C's everywhere. Rather took me by surprise when I first saw it!</p>

#### [ Johan Commelin (Sep 13 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133881855):
<p>Could you do a man-in-the-middle on the Lean - VScode communication?</p>

#### [ Johan Commelin (Sep 13 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133881904):
<p>Somehow VScode is able to deal with Unicode characters, even if they use more then 2 bytes.</p>

#### [ Johan Commelin (Sep 13 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133881923):
<p>If the Lean extension would be able to detect this behaviour, you could manually adjust the coordinates of the red line.</p>

#### [ Johan Commelin (Sep 13 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133881936):
<p>Admittedly this is very hacky, and probably not really worth it.</p>

#### [ Gabriel Ebner (Sep 13 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133882129):
<p>Yes that's the way to fix it. You need to manually translate all the positions in Vscode.</p>

#### [ Gabriel Ebner (Sep 13 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133882192):
<p>The way you encode calligraphic characters in utf-16 is two use 2 2-byte words.  In utf-8 you need 4 bytes.</p>

#### [ Keeley Hoek (Sep 13 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133882648):
<p>Every time I have to write a newline character in a string I have to do it twice because it always autocorrects into a reverse set inclusion :'(</p>

#### [ Gabriel Ebner (Sep 13 2018 at 15:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133884051):
<p>Does \\n work?</p>

#### [ Kenny Lau (Sep 13 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133886939):
<p>But my example has bo calligraphic characters!</p>

#### [ Keeley Hoek (Sep 13 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/133887743):
<p><span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> can I pay you real money? :D awesome</p>

#### [ Kenny Lau (Sep 30 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/134914446):
<p>sometimes in the middle of the proof, when I type something (say <code>abcde</code>), then after I finish, I see the state after typing <code>a</code>, and then after typing <code>b</code>, and then after typing <code>c</code>, and then after typing <code>d</code>, and then after typing <code>e</code>, resulting in the situation that I have to wait a while before I can see the result</p>

#### [ Mario Carneiro (Sep 30 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/134914451):
<p>Is your cursor unusually slow?</p>

#### [ Mario Carneiro (Sep 30 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/134914458):
<p>or typing</p>

#### [ Mario Carneiro (Sep 30 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/134914459):
<p>Or is it just lean being behind VSCode</p>

#### [ Kenny Lau (Sep 30 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/134914463):
<p>the cursor is fine, and so is my typing</p>

#### [ Kenny Lau (Sep 30 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/134914504):
<p>oh and sometimes after I type something, suddenly the whole file is starting to compile and I have to wait a while again</p>

#### [ Mario Carneiro (Sep 30 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/134914511):
<p>That latter problem has hit me many times</p>

#### [ Kenny Lau (Sep 30 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/134914548):
<p>returning to the previous problem, if I copy and paste <code>abcde</code>, then I see the end result instantaneously, so it isn't lean being behind VSCode either</p>

#### [ Mario Carneiro (Sep 30 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/134914553):
<p>I believe sometimes when you mouse over something vscode makes an info request which requires lean to open and compile a new file</p>

#### [ Mario Carneiro (Sep 30 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/134914555):
<p>It might be that the cost of error reporting is high?</p>

#### [ Mario Carneiro (Sep 30 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/134914560):
<p>so that the partial results take longer to compile</p>

#### [ Kenny Lau (Sep 30 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/134914673):
<p>shouldn't it stop compiling when I enter a new letter?</p>

#### [ Mario Carneiro (Sep 30 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/134914679):
<p>it should, but it may also take some time for the interrupt to be accepted</p>

#### [ Kenny Lau (Oct 02 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/135042970):
<blockquote>
<p>oh and sometimes after I type something, suddenly the whole file is starting to compile and I have to wait a while again</p>
</blockquote>
<p>I really hope they can remove this "feature"</p>

#### [ Kevin Buzzard (Oct 02 2018 at 17:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/135043039):
<p>Is this a Windows-only feature? I am not sure I have experienced it on linux.</p>

#### [ Patrick Massot (Oct 02 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/135044696):
<p>I think I never saw this (I'm also using Linux)</p>

#### [ Bryan Gin-ge Chen (Oct 02 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/135047051):
<p>If you're referring to the fact that the info view window goes blank for long periods while typing (inconsistently depending on the type of input?), I've also experienced this on both Mac and Windows and I complained about it <a href="https://github.com/leanprover/vscode-lean/issues/92" target="_blank" title="https://github.com/leanprover/vscode-lean/issues/92">here</a>. I wasn't able to figure out how to fix the underlying issue, but as a workaround, <a href="https://github.com/leanprover/vscode-lean/pull/93" target="_blank" title="https://github.com/leanprover/vscode-lean/pull/93">I submitted a PR</a> which allows you to assign a keystroke to toggle pausing the infoview. So now I just hit my keybind for <code>lean.infoview.toggleUpdating</code>before typing, and hit it again when I'm done, which feels somewhat better.</p>

#### [ Bryan Gin-ge Chen (Oct 02 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/135047256):
<blockquote>
<p>Has anyone had any luck with the "Bracket pair colorizer" extension that's suggested in <a href="https://github.com/leanprover/vscode-lean/blob/master/README.md#other-potentially-helpful-settings" target="_blank" title="https://github.com/leanprover/vscode-lean/blob/master/README.md#other-potentially-helpful-settings">the readme</a>? It doesn't seem to work (on lean files) right out of the box (perhaps because lean doesn't appear on <a href="https://prismjs.com/#languages-list" target="_blank" title="https://prismjs.com/#languages-list">the Prism.js list of languages</a>), though I like how it looks on other filetypes.</p>
</blockquote>
<p>As an update, the new version of that extension, <a href="https://github.com/CoenraadS/Bracket-Pair-Colorizer-2" target="_blank" title="https://github.com/CoenraadS/Bracket-Pair-Colorizer-2">"Bracket Pair Colorizer 2"</a> currently works out of the box with Lean, though it's still in alpha.</p>

#### [ Scott Morrison (Oct 02 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/135066668):
<p>I've definitely seen Kenny's issue on macOS. I think the diagnosis is that your mouse has accidentally hovered over something, VS Code has decided to open a file in the background in order to provide a tooltip, and this has caused a cascade of recompilations.</p>

#### [ Kevin Buzzard (Oct 03 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/135085823):
<p>I only ever run lean with a complete bunch of .olean files for all of mathlib. Does this behaviour still occur in this situation?</p>

#### [ Scott Morrison (Oct 03 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/135089946):
<p>Probably not.</p>

#### [ Kevin Buzzard (Oct 03 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/135092008):
<p>Then this might be the reason I don't see this behaviour in my set-up (i.e. nothing to do with the OS)</p>

#### [ Patrick Massot (Oct 03 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/135092018):
<p>It's clearly much easier to work on something else than mathlib, for this reason</p>

#### [ Kenny Lau (Oct 09 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/135500113):
<p>Whenever I type <code>/-</code>, I automatically get <code>-/</code>, which is inconvenient at times. Before yesterday, it is smarter, in the sense that when I don't want <code>-/</code> it really doesn't give me <code>-/</code>.</p>

#### [ Kenny Lau (Oct 11 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/135616146):
<p>sometimes when I'm in <code>(checking visible lines and above mode)</code>, everything suddenly stops updating</p>

#### [ Kenny Lau (Oct 11 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/135616156):
<p>and I need to close and reopen VSCode</p>

#### [ Gabriel Ebner (Oct 11 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/135620011):
<p>Known bug in the lean C++ code.  That's why the default changed back to "visible files" a few months back.</p>

#### [ Kevin Buzzard (Oct 13 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/135726823):
<p>Is this a bug in VS Code? I'm using Ubuntu 18.04. <a href="/user_uploads/3121/OxpxEK0jqaMg9fHcbyh2yqu1/vscodebug1.png" target="_blank" title="vscodebug1.png">vscodebug1.png</a> <a href="/user_uploads/3121/upsOq2WPURBmCL_T-T-IWBIf/vscodebug2.png" target="_blank" title="vscodebug2.png">vscodebug2.png</a> <a href="/user_uploads/3121/4JUDEG9mSCNVtYDn8Kn02vOZ/vscodebug3.png" target="_blank" title="vscodebug3.png">vscodebug3.png</a> </p>
<div class="message_inline_image"><a href="/user_uploads/3121/OxpxEK0jqaMg9fHcbyh2yqu1/vscodebug1.png" target="_blank" title="vscodebug1.png"><img src="/user_uploads/3121/OxpxEK0jqaMg9fHcbyh2yqu1/vscodebug1.png"></a></div><div class="message_inline_image"><a href="/user_uploads/3121/upsOq2WPURBmCL_T-T-IWBIf/vscodebug2.png" target="_blank" title="vscodebug2.png"><img src="/user_uploads/3121/upsOq2WPURBmCL_T-T-IWBIf/vscodebug2.png"></a></div><div class="message_inline_image"><a href="/user_uploads/3121/4JUDEG9mSCNVtYDn8Kn02vOZ/vscodebug3.png" target="_blank" title="vscodebug3.png"><img src="/user_uploads/3121/4JUDEG9mSCNVtYDn8Kn02vOZ/vscodebug3.png"></a></div><p>After I hover over "U" in the git stuff, my output when I hover over "+" is corrupted. I can get it back by hovering over e.g. "discard changes".</p>

#### [ Kevin Buzzard (Oct 13 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/135726867):
<p>curses, did not capture mouse, sorry. Hover over "U" in git pane to open this menu.</p>

#### [ Gabriel Ebner (Oct 13 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/135726929):
<p>Probably a bug in electron (vscode uses electron (= essentially a distribution of the chrome (well, chromium) web browser) as the gui library).  <a href="https://bugs.chromium.org/p/chromium/issues/detail?id=442111" target="_blank" title="https://bugs.chromium.org/p/chromium/issues/detail?id=442111">https://bugs.chromium.org/p/chromium/issues/detail?id=442111</a></p>

#### [ Simon Hudon (Oct 13 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/135728564):
<p>That's a very lisp-y answer</p>

#### [ Kenny Lau (Nov 05 2018 at 15:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/146800716):
<p>I tried to open a lean file from explorer (I'm using Windows) and then I discovered that my workspace is gone</p>

#### [ Johan Commelin (Nov 15 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/147731422):
<p><span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> How hard would it be to implement a toggle that enables/disables whether Lean is interactive. Sometimes I would like to disable the interactivity to paste a chunk of "almost-Lean" (for example from the goal window) and massage it into Lean-code. After that, I would reenable interactivity, so that the code would be sent of to the server.<br>
In this way, you wouldn't have the server constantly choking on the almost-Lean code, of which you already know that it won't parse...</p>

#### [ Johan Commelin (Nov 15 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/147731427):
<p>This might be a first step towards a "Turn this goal into a lemma" functionality in VScode</p>

#### [ Gabriel Ebner (Nov 15 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/147731713):
<p>Well, the two features are completely independent.<br>
For the "pause" feature, I think the easiest way would be prevent syncing the file contents here: <a href="https://github.com/leanprover/vscode-lean/blob/d70dfa121bc616100c14bc0fd24400b9962922da/src/sync.ts#L36" target="_blank" title="https://github.com/leanprover/vscode-lean/blob/d70dfa121bc616100c14bc0fd24400b9962922da/src/sync.ts#L36">https://github.com/leanprover/vscode-lean/blob/d70dfa121bc616100c14bc0fd24400b9962922da/src/sync.ts#L36</a>  You'd probably also want to disable autocompletion, hover, go-to-definition, etc. in that mode.<br>
Add a command to toggle the pause flag, and when unsetting it, resync all files.  There is theoretically also an option in the roi setting (press on the Lean item in the status bar, and then select "nothing"); but the server still recompiles stuff for autocompletion etc.</p>

#### [ Johan Commelin (Nov 15 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/147731857):
<p>Right, they are completely independent, but they would work together pretty well.</p>

#### [ Johan Commelin (Nov 15 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/147731861):
<p>I think stuff like autocompletion could still be useful in the "pause" mode.</p>

#### [ Johan Commelin (Nov 15 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/147731873):
<p>At least when you are working on "almost-Lean" code.</p>

#### [ Johan Commelin (Nov 15 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/147731936):
<p>Otherwise I could also just edit inside a comment block. But I would like to have some of the cheaper interaction, like syntax highlighting and autocompletion.</p>

#### [ Johan Commelin (Nov 15 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/VScode%20extension/near/147731970):
<p>Anyway, I have never worked with typescript before, and I have no idea where to start if I would want to modify the VScode extension. But I would certainly like to learn this. Has someone ever twitched work on the Lean-VScode extension?</p>


{% endraw %}
