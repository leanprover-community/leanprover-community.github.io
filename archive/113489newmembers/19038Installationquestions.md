---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/19038Installationquestions.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [Installation questions](https://leanprover-community.github.io/archive/113489newmembers/19038Installationquestions.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Bryan Gin-ge Chen (Oct 06 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135290991):
<p>Here's a new thread for installation questions.</p>

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 02:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135290998):
<p><span class="user-mention" data-user-id="131794">@Charles Rezk</span> What system are you using, e.g. windows, mac, linux? There's some basic advice by Kevin Buzzard <a href="https://xenaproject.wordpress.com/2017/12/02/how-to-install-mathlib-and-keep-it-up-to-date/" target="_blank" title="https://xenaproject.wordpress.com/2017/12/02/how-to-install-mathlib-and-keep-it-up-to-date/">here</a>.</p>

#### [ Charles Rezk (Oct 06 2018 at 02:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291011):
<p>Linux.  Yes I'm trying to follow the instructions on that page.</p>

#### [ Charles Rezk (Oct 06 2018 at 02:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291012):
<p>I've compiled lean.</p>

#### [ Charles Rezk (Oct 06 2018 at 02:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291013):
<p>I've added the mathlib package.</p>

#### [ Charles Rezk (Oct 06 2018 at 02:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291014):
<p>I've installed the vscode thing.</p>

#### [ Charles Rezk (Oct 06 2018 at 02:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291017):
<p>I've started it up, and tried to run an example.</p>

#### [ Charles Rezk (Oct 06 2018 at 02:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291067):
<p>For some reason it strangely does not find the lean executable.</p>

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291073):
<p>Are you able to run lean from the terminal?</p>

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291081):
<p>I guess so, if you were able to add mathlib with leanpkg.</p>

#### [ Charles Rezk (Oct 06 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291082):
<p>I can do "lean --version"</p>

#### [ Charles Rezk (Oct 06 2018 at 02:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291086):
<p>When vscode tries to run the lean executable, it for some reason puts in an extra comma</p>

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 02:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291144):
<p>I guess you're seeing an error message somewhere. What does it say exactly?</p>

#### [ Charles Rezk (Oct 06 2018 at 02:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291211):
<p>Lean: Error: Command failed: /home/rezk/git/lean/bin/lean, --version<br>
/bin/sh: /home/rezk/git/lean/bin/lean,: No such file or directory</p>

#### [ Charles Rezk (Oct 06 2018 at 02:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291227):
<p>I don't know why there is an extra comma in there, but that is presumably why it is failing</p>

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 02:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291271):
<p>Could you check your VS code settings? Under "Extensions &gt; Lean configuration" there should be a box that says "Executable path"</p>

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 02:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291273):
<p>If there's not an extra comma in there then I'm stumped.</p>

#### [ Charles Rezk (Oct 06 2018 at 02:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291283):
<p>How do I find this box?</p>

#### [ Charles Rezk (Oct 06 2018 at 02:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291286):
<p>I have been trying to set the executable path in "User Settings", according to the instructions, but that seems to have literally no effect.</p>

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 02:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291331):
<p>Did you edit your settings.json file to add the "lean.executablePath" option as in Kevin's instructions? Maybe there's a misplaced quote there.</p>

#### [ Charles Rezk (Oct 06 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291385):
<p>Yes I have tried that, assuming I am doing it correctly.  As far as I can tell, it complety ignores what I put there.  I can give a giberish path, and I still get the exact same error message I gave you above.</p>

#### [ Kevin Buzzard (Oct 06 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291390):
<p>Ctrl + comma might take you to preferences</p>

#### [ Charles Rezk (Oct 06 2018 at 02:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291391):
<p>Some how it is getting an incorrect path from somewhere else</p>

#### [ Kevin Buzzard (Oct 06 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291401):
<p>Or something like file -&gt; settings -&gt; preferences</p>

#### [ Scott Morrison (Oct 06 2018 at 02:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291404):
<p>Do you want to copy-paste your "settings.json" file here?</p>

#### [ Scott Morrison (Oct 06 2018 at 02:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291522):
<p><span class="user-mention" data-user-id="131794">@Charles Rezk</span>, did you at any point set the environment variable <code>LEAN_PATH</code>?</p>

#### [ Charles Rezk (Oct 06 2018 at 02:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291532):
<p>No, there is no $LEAN_PATH</p>

#### [ Scott Morrison (Oct 06 2018 at 02:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291535):
<p>Could you show your settings.json file?</p>

#### [ Charles Rezk (Oct 06 2018 at 02:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291536):
<p>From what it says in USer Settings, the settings.json file is:</p>

#### [ Charles Rezk (Oct 06 2018 at 02:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291537):
<p>{ "lean.executablePath": "/home/rezk/git/lean/bin/lean"<br>
}</p>

#### [ Charles Rezk (Oct 06 2018 at 02:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291580):
<p>I don't know where this file is actually kept</p>

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291585):
<p>On linux it's apparently $HOME/.config/Code/User/settings.json</p>

#### [ Scott Morrison (Oct 06 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291594):
<p>Here's another suggestion:</p>

#### [ Scott Morrison (Oct 06 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291595):
<p>the best way to install Lean is actually to use <code>elan</code></p>

#### [ Scott Morrison (Oct 06 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291600):
<p>from &lt;<a href="https://github.com/Kha/elan" target="_blank" title="https://github.com/Kha/elan">https://github.com/Kha/elan</a>&gt;</p>

#### [ Charles Rezk (Oct 06 2018 at 02:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291640):
<p>I've been doing this for several hours.  I'm not starting again.</p>

#### [ Scott Morrison (Oct 06 2018 at 02:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291642):
<p>e.g. just by running <code>curl https://raw.githubusercontent.com/Kha/elan/master/elan-init.sh -sSf | sh</code> in a terminal</p>

#### [ Scott Morrison (Oct 06 2018 at 02:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291643):
<p>Ok :-)</p>

#### [ Scott Morrison (Oct 06 2018 at 02:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291645):
<p>(My experience is that installing Lean via elan takes less than a minute. :-)</p>

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 02:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291652):
<p>In particular, you won't have to rebuild lean from source that way.</p>

#### [ Charles Rezk (Oct 06 2018 at 02:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291667):
<p>OK, that explains it.  The actually "settings.json" file is different than what vscode is showing me</p>

#### [ Scott Morrison (Oct 06 2018 at 02:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291674):
<p>(The advantage is that you don't have to compile anything, you don't have to set any paths in VS Code, and elan will automatically switch between Lean versions if you have different projects requiring different versions.)</p>

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 02:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291738):
<p>The installation process will hopefully be a lot, lot easier once Scott's PR to the VS code extension is merged.</p>

#### [ Charles Rezk (Oct 06 2018 at 02:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291739):
<p>I restarted vscode, and now it shows the actually physical file in "Settings", and also I don't get that error any more when I try to "Restart: Lean"</p>

#### [ Charles Rezk (Oct 06 2018 at 02:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291783):
<p>Now nothing happens when I do that, which doesn't seem like an improvement</p>

#### [ Scott Morrison (Oct 06 2018 at 02:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291795):
<p>"Nothing happening" might be the right thing! Lean doesn't say anything upon a successful start up, until you actually enter something in a <code>.lean</code> file.</p>

#### [ Scott Morrison (Oct 06 2018 at 03:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291815):
<p>Can you save a file, e.g. as <code>test.lean</code>, and enter something in it, such as <code>#eval 2+2</code>?</p>

#### [ Scott Morrison (Oct 06 2018 at 03:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291846):
<p>You should then get a green squiggle under it, and hovering the mouse there should show <code>4</code>.</p>

#### [ Charles Rezk (Oct 06 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291964):
<p>I have tried that.   Nothing happens, no green squiggle</p>

#### [ Charles Rezk (Oct 06 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291979):
<p>Wait, now it is.</p>

#### [ Charles Rezk (Oct 06 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135291981):
<p>Maybe it works now</p>

#### [ Mario Carneiro (Oct 06 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135292049):
<p>If you see orange bars on the sidebar that means it's in progress and you should wait</p>

#### [ Mario Carneiro (Oct 06 2018 at 03:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135292054):
<p>you can also see status information on the bottom left which will tell you if lean is dead or just busy</p>

#### [ Charles Rezk (Oct 06 2018 at 03:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135292091):
<p>I think it's working now</p>

#### [ Mario Carneiro (Oct 06 2018 at 03:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135292101):
<p>You should test mathlib imports if you intend to use it, e.g. <code>import data.nat.prime</code></p>

#### [ Charles Rezk (Oct 06 2018 at 03:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135292237):
<p>OK</p>

#### [ Charles Rezk (Oct 06 2018 at 03:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135292399):
<p>I think this computer is going to be too slow for this.</p>

#### [ Mario Carneiro (Oct 06 2018 at 03:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135292441):
<p>you may need to compile the lean sources if everything is running slow</p>

#### [ Mario Carneiro (Oct 06 2018 at 03:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135292443):
<p>i.e. run <code>lean --make</code> in the library directoy</p>

#### [ Charles Rezk (Oct 06 2018 at 03:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135292460):
<p>What is the library directory?</p>

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 03:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135292568):
<p>The mathlib you added to your package should be in <code>_target/deps/mathlib</code> relative to the package root; running <code>lean --make</code> in that directory should make importing mathlib much faster.</p>

#### [ Scott Morrison (Oct 06 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135294984):
<p>Hi <span class="user-mention" data-user-id="123965">@Bryan Gin-ge Chen</span> , just correcting that suggestion: in general it is safer to run <code>lean —make _target/deps/mathlib</code> from the main project directory, rather than changing into that subdirectory and running <code>lean —make</code>. If there is a version mismatch between the project and mathlib, running lean in the subdirectory will just give you olean files that won’t be usable.</p>

#### [ Scott Morrison (Oct 06 2018 at 04:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135294987):
<p>(If there’s no version mismatch, there’s no problem, but we seem to have regular problems with this.)</p>

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 04:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135295039):
<p>Thanks! That's good to know.</p>

#### [ Scott Morrison (Oct 06 2018 at 04:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135295190):
<p>Perhaps we should add a command in VS Code “compile all dependencies in background” to help people with this.</p>

#### [ Johan Commelin (Oct 09 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135482171):
<p><span class="user-mention" data-user-id="131794">@Charles Rezk</span> Did you get the install working in the end?</p>

#### [ Charles Rezk (Oct 09 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135483148):
<p>I did.  I'm not really sure how do actually do anything interesting, the mathlib files are hard for me to interpret.</p>

#### [ Kevin Buzzard (Oct 09 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135483437):
<p>Pick a project, get stuck, ask here, people will try to help :-) At least that's how I did it</p>

#### [ Johan Commelin (Oct 09 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135483546):
<p><span class="user-mention" data-user-id="131794">@Charles Rezk</span> I suggest you write a short post in <a href="#narrow/stream/113489-new-members/subject/Introductions" title="#narrow/stream/113489-new-members/subject/Introductions">https://leanprover.zulipchat.com/#narrow/stream/113489-new-members/subject/Introductions</a>.</p>

#### [ Johan Commelin (Oct 09 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135483550):
<p>Tell us where you are based and what kind of stuff you like.</p>

#### [ Johan Commelin (Oct 09 2018 at 19:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/135483559):
<p>And like Kevin said, just hang around and ask questions.</p>

#### [ Wojciech Nawrocki (Jan 15 2019 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/155128486):
<p>Is it normal for compilation of <code>mathlib</code> <code>master</code> to fail miserably on <code>nightly</code> Lean? I made a package with <code>leanpkg +nightly new</code>, then added <code>mathlib</code> and <code>lean --make _target/deps/mathlib/</code> shows errors on everything, e.g. <code>relator.lean:13:43: error: unknown identifier 'left_unique'</code>.</p>

#### [ Kenny Lau (Jan 15 2019 at 00:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/155128643):
<p>We use 3.4.1 Lean</p>

#### [ Bryan Gin-ge Chen (Jan 15 2019 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Installation%20questions/near/155129521):
<p>see also <a href="#narrow/stream/113488-general/topic/mathlib.20is.20broken" title="#narrow/stream/113488-general/topic/mathlib.20is.20broken">https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib.20is.20broken</a></p>


{% endraw %}
