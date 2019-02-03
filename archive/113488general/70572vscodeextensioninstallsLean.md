---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/70572vscodeextensioninstallsLean.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [vscode extension installs Lean](https://leanprover-community.github.io/archive/113488general/70572vscodeextensioninstallsLean.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Sep 17 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134097115):
<p>I just sent a PR for the VS Code extension, that will offer to install Lean for you if it can't find a working copy. It uses elan, and just runs in the VS Code terminal.</p>

#### [ Scott Morrison (Sep 17 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134097116):
<p>I've tested it on OS X, and it seems to work quite nicely.</p>

#### [ Scott Morrison (Sep 17 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134097206):
<p><a href="/user_uploads/3121/01B1ajUPuC1GwOdpvxRT8ICA/Screenshot-2018-09-17-22.22.30.png" target="_blank" title="Screenshot-2018-09-17-22.22.30.png">Screenshot-2018-09-17-22.22.30.png</a> <a href="/user_uploads/3121/q5CFFm23QgagbkHTuf1xiXTa/Screenshot-2018-09-17-22.22.36.png" target="_blank" title="Screenshot-2018-09-17-22.22.36.png">Screenshot-2018-09-17-22.22.36.png</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/01B1ajUPuC1GwOdpvxRT8ICA/Screenshot-2018-09-17-22.22.30.png" target="_blank" title="Screenshot-2018-09-17-22.22.30.png"><img src="/user_uploads/3121/01B1ajUPuC1GwOdpvxRT8ICA/Screenshot-2018-09-17-22.22.30.png"></a></div><div class="message_inline_image"><a href="/user_uploads/3121/q5CFFm23QgagbkHTuf1xiXTa/Screenshot-2018-09-17-22.22.36.png" target="_blank" title="Screenshot-2018-09-17-22.22.36.png"><img src="/user_uploads/3121/q5CFFm23QgagbkHTuf1xiXTa/Screenshot-2018-09-17-22.22.36.png"></a></div>

#### [ Scott Morrison (Sep 17 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134097212):
<p>It automatically restarts the extension afterwards, so in good cases the whole Lean installation process could now be:</p>

#### [ Scott Morrison (Sep 17 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134097216):
<p>1) Install the VS Code extension</p>

#### [ Scott Morrison (Sep 17 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134097218):
<p>2) Open a Lean file</p>

#### [ Scott Morrison (Sep 17 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134097262):
<p>3) Click "Install Lean using elan" in the error box that complains you don't have Lean.</p>

#### [ Scott Morrison (Sep 17 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134097270):
<p>However I haven't tested this on Linux or Windows.</p>

#### [ Scott Morrison (Sep 17 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134097279):
<p>and I haven't thought hard about further diagnostics if something goes wrong (e.g. dependencies are unavailable).</p>

#### [ Scott Morrison (Sep 17 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134097303):
<p>If anyone feels up to trying out the PR version of the extension on Linux or Windows, please do!</p>

#### [ Scott Morrison (Sep 17 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134097356):
<p>Let me know if you need help --- running a vscode extension from source is delightfully easy.</p>

#### [ Scott Morrison (Sep 17 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134097585):
<p>Somewhat depressingly, the reason I did this was because this morning I realised just how badly my email inbox needed love and attention, and so I deleted Lean until I'd made some progress :-).</p>

#### [ Scott Morrison (Sep 17 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134097589):
<p>Sitting down after dinner tonight, my first thought was "huh, a nice opportunity to try making installation easier".</p>

#### [ Scott Morrison (Sep 17 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134097652):
<p>(For anyone keeping track, a tenure letter got written, and files for scholarship applications for a number of international PhD students got written, but my inbox is still unhappy...)</p>

#### [ Scott Morrison (Sep 17 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134097932):
<p>and for my own future reference, to make this work on Windows we'll have to ask VS Code to run elan in some sort of bash terminal, per instructions at &lt;<a href="https://stackoverflow.com/questions/42606837/how-to-use-bash-on-windows-from-visual-studio-code-integrated-terminal" target="_blank" title="https://stackoverflow.com/questions/42606837/how-to-use-bash-on-windows-from-visual-studio-code-integrated-terminal">https://stackoverflow.com/questions/42606837/how-to-use-bash-on-windows-from-visual-studio-code-integrated-terminal</a>&gt;. It seems plausible that this could work for a bash terminal provided by any of git bash, linux subsystem for windows, or msys2, but I have no experience with these and I'm unsure whether VS Code would actually be able to find the installation elan created.</p>

#### [ Sebastian Ullrich (Sep 17 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134110039):
<p>This looks nice! Though I suspect it only worked for you because you already had <code>~/.elan/bin</code> in your PATH - the PATH value of the VS Code process will not change when installing elan. What you could do is to just default to <code>~/.elan/bin/lean</code> as the <code>executablePath</code> if that file exists</p>

#### [ Sebastian Ullrich (Sep 17 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134110850):
<p>I'm not sure I like the installation being completely hidden from the user</p>

#### [ Johan Commelin (Sep 17 2018 at 19:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134114453):
<blockquote>
<p>I'm not sure I like the installation being completely hidden from the user</p>
</blockquote>
<p>I'm quite sure that there a lot of users that <em>do</em> like it.</p>

#### [ Scott Morrison (Sep 17 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134123194):
<p>Good point about the PATH! :-) I'll investigate that later.</p>

#### [ Scott Morrison (Sep 17 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134123274):
<p>The compromise I was going for was minimising the number of interactions required during installation, while still showing on the screen what was going on --- so it gives focus to the terminal window doing the work, but doesn't require any interaction inside that terminal window.</p>

#### [ Scott Morrison (Sep 17 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134123342):
<p>A pretty reasonable alternative would be to require the user answers the one question that elan asks by default. (Perhaps maximising the terminal window first, so it's obvious to them they need to look at that window?) I could also add a "press any key to continue" prompt at the end, so they can see the end of the output from elan before the terminal window disappears and the extension starts.</p>

#### [ Sebastian Ullrich (Sep 17 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134125033):
<p>Yeah, I was imagining something like that prompt. They may also want to at least decide between stable and nightly Lean - not that it matters much right now, or that the installer makes that particularly simple</p>

#### [ Scott Morrison (Sep 18 2018 at 07:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134146769):
<p>I don't really understand why there is a choice to be made between stable and nightly Lean. Isn't elan deciding for itself on a per-project basis which version of Lean to give you anyway?</p>

#### [ Johan Commelin (Sep 18 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134148759):
<p>Scott, in your current workflow, where is the user supposed to make the decision about the project? We don't want them to manually touch a <code>.toml</code> etc...</p>

#### [ Johan Commelin (Sep 18 2018 at 08:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134148804):
<p>I mean, if it is a Lean file in an existing project, sure... then those choices have already been made by someone else. But if it is a new Lean file in an empty directory...</p>

#### [ Scott Morrison (Sep 18 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134149513):
<p>When you type <code>leanpkg init</code>, how is the Lean version decided? Whatever is the logic there should be the default everywhere.</p>

#### [ Sebastian Ullrich (Sep 18 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134193652):
<p><span class="user-mention" data-user-id="110524">@Scott Morrison</span> It's the default Lean version according to <code>elan toolchain list</code>. Which is exactly what you can customize in the installer :)</p>

#### [ Sebastian Ullrich (Sep 18 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134193839):
<p>Of course, if we're already integrating elan into editors, we may as well have a dialog for creating a new Lean package with a Lean version chooser. Not sure what to do about stand-alone files, though we may want to de-emphasize their use anyway (e.g. it may not be posible in Lean 4 to import a stand-alone file from another one)</p>

#### [ Scott Morrison (Sep 19 2018 at 03:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134203981):
<p>I think we should mostly decide that all new users who don't know better want the tools to provide them with <code>stable</code> as effortlessly as possible.</p>

#### [ Scott Morrison (Sep 19 2018 at 03:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134203991):
<p>When they start looking at other peoples' projects, as long as they got started with <code>elan</code>, those projects will magically use <code>nightly-XXX</code> as desired.</p>

#### [ Scott Morrison (Sep 19 2018 at 03:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134204035):
<p>And once they realise they need <code>nightly-XXX</code> for their own projects, they can edit a <code>leanpkg.toml</code> file themselves.</p>

#### [ Scott Morrison (Sep 19 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134215745):
<p>Hi <span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span>, how would you feel about having <code>elan</code> try to install missing dependencies. Something as simple as:</p>

#### [ Scott Morrison (Sep 19 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134215794):
<div class="codehilite"><pre><span></span>if ubuntu then
  sudo apt-get install git libgmp-dev cmake
else if osx then
  brew install cmake
  brew install gmp
</pre></div>

#### [ Scott Morrison (Sep 19 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134215800):
<p>would get most non-windows users going a bit faster</p>

#### [ Scott Morrison (Sep 19 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134215809):
<p>heck, in the osx branch add</p>
<div class="codehilite"><pre><span></span>xcode-select --install
brew --version || /usr/bin/ruby -e &quot;$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)&quot;
</pre></div>

#### [ Scott Morrison (Sep 19 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134215878):
<p>I'd be happy to make the PR, if something like this could be accepted.</p>

#### [ Scott Morrison (Sep 19 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134215897):
<p>The combination of VS Code giving a button to run elan, and elan attempting to fill in missing dependencies, could be very helpful.</p>

#### [ Sean Leather (Sep 19 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134215986):
<p>I don't mean to be difficult, but I think that's a really bad idea to have <code>elan</code> run <code>apt-get</code> or <code>brew</code>.</p>

#### [ Scott Morrison (Sep 19 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134215993):
<p>Why is that?</p>

#### [ Sean Leather (Sep 19 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134215999):
<p>Who knows what state the user's computer is in?</p>

#### [ Scott Morrison (Sep 19 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216000):
<p>(I am ignorant here)</p>

#### [ Sean Leather (Sep 19 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216010):
<p>You could and probably will break something.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216016):
<p>I guess an alternative is to fail and say "hey, you might want to type <code>apt install gmp</code>" or some such</p>

#### [ Scott Morrison (Sep 19 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216017):
<p>Ok!</p>

#### [ Sean Leather (Sep 19 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216020):
<p>Sure, that's a good option.</p>

#### [ Scott Morrison (Sep 19 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216059):
<p>Ok --- maybe I will continue tweaking the VS Code extension</p>

#### [ Mario Carneiro (Sep 19 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216060):
<p>I don't really see how an apt-get command like that will break anything, at worst it will fail</p>

#### [ Scott Morrison (Sep 19 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216063):
<p>It is easy enough for it to analyze the error messages and tell you what to run.</p>

#### [ Scott Morrison (Sep 19 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216079):
<p>I feel like for 99% of users that apt-get or brew command is going to be the right thing to do, and moreover for 90% of users they won't even know what it means when they run it. :-)</p>

#### [ Sean Leather (Sep 19 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216082):
<p>Even if it wouldn't break anything, it's a bad idea to install software without the user having control over it. And if the user doesn't know what it's doing, that's even worse.</p>

#### [ Scott Morrison (Sep 19 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216089):
<p>Ok -- I will go with dialogs that provide hints.</p>

#### [ Mario Carneiro (Sep 19 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216091):
<p>don't package managers themselves do this routinely?</p>

#### [ Mario Carneiro (Sep 19 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216136):
<p>the user has control over the large scale execution, that is sufficient</p>

#### [ Mario Carneiro (Sep 19 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216170):
<p>I think it should ask the same questions you normally see in an installer, but otherwise go about its business completely automatically</p>

#### [ Mario Carneiro (Sep 19 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216182):
<p>complicated questions will just cause confusion, a power user doesn't need to use this method at all</p>

#### [ Scott Morrison (Sep 19 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216229):
<p>e.g. <code>elan</code> could show a prompt: "It looks like you don't have libgmp installed. Would you like to install this using <code>brew install libgmp</code>?"</p>

#### [ Sean Leather (Sep 19 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216249):
<blockquote>
<p>e.g. <code>elan</code> could show a prompt: "It looks like you don't have libgmp installed. Would you like to install this using <code>brew install libgmp</code>?"</p>
</blockquote>
<p>In order to do that, you need to know if <code>brew</code> is installed.</p>

#### [ Scott Morrison (Sep 19 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216260):
<p>Of course</p>

#### [ Scott Morrison (Sep 19 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216265):
<p>but detecting the operating system is easy</p>

#### [ Sean Leather (Sep 19 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216267):
<p>And <code>brew</code> in the <code>$PATH</code> may not be the <code>brew</code> you expect, so you'd have to test for the right <code>brew</code>.</p>

#### [ Scott Morrison (Sep 19 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216288):
<p>and running <code>brew --version</code> is harmless, surely?</p>

#### [ Sean Leather (Sep 19 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216330):
<p>Maybe. But I'd still recommend giving the commands to the user and explaining it rather than doing it for them.</p>

#### [ Scott Morrison (Sep 19 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216334):
<p>I mean, if someone has contrived to put an evil or nonfunctional brew on the $PATH, surely they can't be upset if an installer doesn't work as expected?</p>

#### [ Scott Morrison (Sep 19 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216374):
<p>Having tried to clean up several broken attempts by mathematicians and students to install Lean by now, I would really like to take this stuff out of their hands :-)</p>

#### [ Scott Morrison (Sep 19 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216434):
<p>I agree that power users don't want this!</p>

#### [ Scott Morrison (Sep 19 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216477):
<p>If we're going to attempt something like this, it seems more sensible to me to put all the login in <code>elan</code>, and then have the VS Code extension just call <code>elan</code>.</p>

#### [ Mario Carneiro (Sep 19 2018 at 09:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216480):
<blockquote>
<p>Maybe. But I'd still recommend giving the commands to the user and explaining it rather than doing it for them.</p>
</blockquote>
<p>No no, this is the source of too many problems</p>

#### [ Sean Leather (Sep 19 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216485):
<p>You're welcome to do what you like, but, from past experience, I know that it's a bad idea. I can't tell you exactly what will go wrong, because things change and systems are complex, but I'm pretty sure something will go wrong.</p>

#### [ Scott Morrison (Sep 19 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216528):
<p>Seeing what someone at Dagstuhl had managed to do with their windows path was pretty terrifying. :-)</p>

#### [ Mario Carneiro (Sep 19 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216538):
<p>We already have a command sequence in a help file, it doesn't work half the time and the poor users don't know what to do</p>

#### [ Scott Morrison (Sep 19 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216546):
<p>What if we instead put all the login in the VS Code, and</p>

#### [ Scott Morrison (Sep 19 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216547):
<p>when something goes wrong</p>

#### [ Johan Commelin (Sep 19 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216559):
<p>Talking about automatically fixing problems: If we detect windows, can't we just wipe it with a fresh Linux install?</p>

#### [ Sean Leather (Sep 19 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216560):
<p>For Windows, an installer would be best. For Linux, a package would be best. For Mac, Homebrew would probably be best.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216562):
<p>Ha ha there was a user over the summer whose Windows path rather eerily contained a bunch of directories on my laptop (<code>/home/buzzard/Lean/whatever</code>).</p>

#### [ Scott Morrison (Sep 19 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216566):
<p>show a dialog that says "XXX not found. You may want to try running <code>YYY</code> in a terminal"</p>

#### [ Kevin Buzzard (Sep 19 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216568):
<p>I just said "I think you can safely remove all those, they're on another system"</p>

#### [ Mario Carneiro (Sep 19 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216570):
<p>"what's a terminal?"</p>

#### [ Scott Morrison (Sep 19 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216571):
<p>:-)</p>

#### [ Scott Morrison (Sep 19 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216615):
<p>A nice trick, because VS Code has an integrated terminal, is that we can actually pop up a terminal window</p>

#### [ Mario Carneiro (Sep 19 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216616):
<p>or worse - "I installed cygwin (on linux) but it couldn't find the path"</p>

#### [ Scott Morrison (Sep 19 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216617):
<p>and paste in the command the user needs</p>

#### [ Sean Leather (Sep 19 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216624):
<p>BTW, there's a package manager for Windows: <a href="https://chocolatey.org/" target="_blank" title="https://chocolatey.org/">https://chocolatey.org/</a></p>

#### [ Scott Morrison (Sep 19 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216625):
<p>leaving them to just press "enter"?</p>

#### [ Scott Morrison (Sep 19 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216647):
<p>Does <code>elan</code> currently do anything useful on windows? I have no idea.</p>

#### [ Kevin Buzzard (Sep 19 2018 at 09:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216651):
<p>I also noticed that some users, when you say "oh hold down shift", say "what's shift?" because a modern keyboard might well not have the word "shift" on it any more. Similarly for "enter" / "return".</p>

#### [ Mario Carneiro (Sep 19 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216696):
<p>why not run a command that prints out the sequence of brew/whatever commands it will send, and says (y/n)</p>

#### [ Sean Leather (Sep 19 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216702):
<p>Also, if you're going to do <code>apt-get</code> and/or <code>brew</code>, you'll want to update those first.</p>

#### [ Scott Morrison (Sep 19 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216718):
<p>I'm pretty sure <code>brew</code> auto-updates these days.</p>

#### [ Sean Leather (Sep 19 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216765):
<div class="codehilite"><pre><span></span>/usr/bin/ruby -e &quot;$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)&quot;
</pre></div>


<p>And this is notoriously not secure.</p>

#### [ Scott Morrison (Sep 19 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216767):
<p>Note our install instructions for elan are already of this form!</p>

#### [ Sean Leather (Sep 19 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216773):
<p>I haven't seen them, but it's still true. <span class="emoji emoji-1f642" title="slight smile">:slight_smile:</span></p>

#### [ Mario Carneiro (Sep 19 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216940):
<p>I'm not sure how you can in one line download and run a script from the internet without it being insecure</p>

#### [ Mario Carneiro (Sep 19 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134216945):
<p>that's like the definition of insecure</p>

#### [ Sean Leather (Sep 19 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134217148):
<p>In the end, it comes down to trust. <a href="https://brew.sh/" target="_blank" title="https://brew.sh/">https://brew.sh/</a> also suggests that command. I don't like it, but that's the way it is. In general, I would point to <a href="https://brew.sh" target="_blank" title="https://brew.sh">https://brew.sh</a> when informing somebody to install <code>brew</code>. That way, they can read the information and become informed about what it is before installing it. Yes, one could decide to ignore the information, but at least they've been given the opportunity.</p>

#### [ Sebastian Ullrich (Sep 19 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134240599):
<p>Why do users need <code>cmake</code>...?</p>

#### [ Sebastian Ullrich (Sep 19 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134240757):
<p>That <code>libgmp</code> isn't included is basically a bug; I think it was at some point. Anyway, calling <code>sudo</code> may reasonably ask for a password, so the automatic installation should be in an interactive shell at the very least</p>

#### [ Reid Barton (Sep 19 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134241429):
<p>I didn't have to install cmake, but I did have to install coreutils for leanpkg. This was on a machine with no preinstalled brew on which I didn't have root access. brew says it can be installed anywhere but some packages may not be happy in nonstandard locations; I didn't have any difficulties though.</p>

#### [ Reid Barton (Sep 19 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134241551):
<p>Vscode could even install its own private brew installation</p>

#### [ Reid Barton (Sep 19 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134241669):
<p>Maybe it was elan not leanpkg that needed readlink, I think it was</p>

#### [ Scott Morrison (Sep 24 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134516578):
<p>I just updated my PR to vscode-lean, so hopefully after the VS Code Lean extension offers to install <code>elan</code> for you, it works first time (even though the $PATH has not yet been updated).</p>

#### [ Scott Morrison (Sep 24 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134516589):
<p>Testing on other systems much appreciated.</p>

#### [ Scott Morrison (Sep 24 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134516595):
<p>I've gone back to the more conservative model of not pressing enter for the user during the <code>elan</code> script. :-)</p>

#### [ Scott Morrison (Sep 24 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134516598):
<p>Next up: testing this in Linux and Windows</p>

#### [ Scott Morrison (Sep 24 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134516607):
<p>after that, seeing if we can make <code>elan</code> more helpful when dependencies are missing.</p>

#### [ Scott Morrison (Sep 24 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20extension%20installs%20Lean/near/134516615):
<p><a href="https://github.com/leanprover/vscode-lean/pull/91" target="_blank" title="https://github.com/leanprover/vscode-lean/pull/91">https://github.com/leanprover/vscode-lean/pull/91</a></p>


{% endraw %}
