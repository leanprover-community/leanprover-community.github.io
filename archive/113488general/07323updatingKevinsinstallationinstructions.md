---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/07323updatingKevinsinstallationinstructions.html
---

## Stream: [general](index.html)
### Topic: [updating Kevin's installation instructions](07323updatingKevinsinstallationinstructions.html)

---


{% raw %}
#### [ Scott Morrison (Oct 06 2018 at 03:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135291857):
<p>Hi <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span>, I'm thinking that since <code>elan</code> has now arrived and is pretty good, we should update your blog post.</p>
<p>If I wrote a guest post for you, could we put that up, and add a prominent link at the top of your old post?</p>

#### [ Kevin Buzzard (Oct 06 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135303201):
<p>Yes that would be fine. I have never used elan.</p>

#### [ Kevin Buzzard (Oct 06 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135303363):
<p>I also think we should plug the trivial way of getting Lean and Mathlib running on Windows 10: <a href="https://xenaproject.wordpress.com/getting-lean-and-mathlib-running-in-the-mlc/" target="_blank" title="https://xenaproject.wordpress.com/getting-lean-and-mathlib-running-in-the-mlc/">https://xenaproject.wordpress.com/getting-lean-and-mathlib-running-in-the-mlc/</a></p>

#### [ Kevin Buzzard (Oct 06 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135303403):
<p>There are no links to that page on the site because the system got changed again and now it's even easier for us at Imperial, we fire up VS Code and it's all there.</p>

#### [ Kevin Buzzard (Oct 06 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135303409):
<p>But on Thursday night one person with a win10 machine asked about installation and I said "I have just the link for you".</p>

#### [ Kevin Buzzard (Oct 06 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135303452):
<p>For those not clicking: the full installation procedure is " Download VS Code, now download this zip file (containing lean and mathlib lean and olean files and a leanpkg.path etc) and now tell VS Code where Lean is and now open this folder and it all works.". No git, no msys2, no command line</p>

#### [ Scott Morrison (Oct 06 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135308310):
<p>Okay! It would be good if we could arrange for creating that zip file automatically, so it doesn't become an ancient stranded artefact.</p>

#### [ Scott Morrison (Oct 06 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135308315):
<p>I think I am going to wait just a moment before writing that blog post --- Gabriel has just reviewed my PR to have the VS Code extension offer to install Lean, so it seems likely that will land soon, and this will make the instructions even easier.</p>

#### [ Kevin Buzzard (Oct 06 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135308930):
<p>Yes -- that link above suffered from document rot after about 3 days, when someone in ICT said "oh wow, is that what you're telling them? We can probably automate all of that". I thought they were crazy. We'll see. The reason I think they're crazy is that now when any undergraduate launches Visual Studio Code on a machine in the maths department, it starts off by default with a minimal Lean project open! The doc hence became obsolete. I can see this causing confusion for non-converts later down the line though...but I decided that this was not currently my problem.</p>

#### [ Gabriel Ebner (Oct 06 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135310090):
<blockquote>
<p>Gabriel has just reviewed my PR to have the VS Code extension offer to install Lean, so it seems likely that will land soon</p>
</blockquote>
<p>It should come to a vscode installation near you any moment now!</p>

#### [ Scott Morrison (Oct 06 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135310363):
<p>... and, it works!</p>

#### [ Scott Morrison (Oct 06 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135310407):
<p>If anyone wants to try deleting their Lean installation and trying it out, the VS Code extension now installs elan for you upon request! --- It took less than 2 minutes for me just now.</p>

#### [ Scott Morrison (Oct 06 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135310409):
<p>I will try to make a little video walk-through.</p>

#### [ Scott Morrison (Oct 06 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135310419):
<p><span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> --- I was just thinking about making a "build all olean files" command in VS Code, as this is a common task. Do you think it is better to use the model of <code>batch.ts</code>, or to create a terminal and run the commands there?</p>

#### [ Scott Morrison (Oct 06 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135310422):
<p>(I haven't been able to get the batch mode to work.)</p>

#### [ Gabriel Ebner (Oct 06 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135310466):
<p>Have you seen <code>ctrl+p task build</code>?  Should we package it up as a command as well?</p>

#### [ Scott Morrison (Oct 06 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135310545):
<p>No, I haven't. What is <code>ctrl+p</code>? On mac that doesn't seem to do anything.</p>

#### [ Scott Morrison (Oct 06 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135310589):
<p>Ah, under <code>cmd-shift-p</code> I get <code>Tasks: Run Build Task</code></p>

#### [ Scott Morrison (Oct 06 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135310591):
<p>and under that <code>leanpkg: configure</code> and a few others.</p>

#### [ Scott Morrison (Oct 06 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135310602):
<p>Yes, putting <code>lean --make _target &amp;&amp; lean --make</code> as a task under that would be a great solution.</p>

#### [ Scott Morrison (Oct 06 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135310700):
<p>I guess the <code>lean --make</code> is silly, that should just be <code>leanpkg build</code>.</p>

#### [ Scott Morrison (Oct 06 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135310701):
<p>But having some way to compile everything in the dependencies seems to be requested often.</p>

#### [ Gabriel Ebner (Oct 06 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135310703):
<p>Oh, on mac it is <code>cmd+p task build</code> then.  BTW, your command is equivalent to <code>lean --make</code>.</p>

#### [ Scott Morrison (Oct 06 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135310707):
<p>Hmm... I guess so. :-)</p>

#### [ Scott Morrison (Oct 06 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135310810):
<p>There's no way to ask <code>leanpkg</code> to completely compile the dependencies, is there?</p>

#### [ Gabriel Ebner (Oct 06 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135310816):
<p>No.</p>

#### [ Scott Morrison (Oct 06 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135310823):
<p>It would be great to have <code>leanpkg build-dependencies</code> as well as <code>leanpkg clean</code> one day.</p>

#### [ Scott Morrison (Oct 06 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135310863):
<p>In the meantime, what do you think of adding <code>lean --make</code> as a build task? It would be a little awkward, as it probably belongs in <code>leanpkg.ts</code>, but isn't actually using <code>leanpkg</code>.</p>

#### [ Chris Hughes (Oct 06 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135311782):
<p>I have some error, related to the fact that I have a space in my username<br>
<code>C:\msys64\home\Christopher Hughes\mathlibs\exp&gt;leanpkg build
'Hughes\.elan\toolchains\3.4.1\bin\..' is not recognized as an internal or external command,
operable program or batch file.
C:\Users\Christopher:1:0: error: file 'C:\Users\Christopher' not found
&lt;unknown&gt;:1:1: error: file 'C:\Users\Christopher' not found</code></p>

#### [ Kevin Buzzard (Oct 06 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135312119):
<p>You have a space in "Christopher Hughes" and because of an irreparable flaw in Windows you are going to struggle.</p>

#### [ Kevin Buzzard (Oct 06 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135312120):
<p>If you can somehow change it to "Christopher_Hughes" this will change the behaviour of things.</p>

#### [ Scott Morrison (Oct 06 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135312763):
<p>Here's a short video I just made that shows a complete installation of Lean on a mac. Takes 3:40! (Well, with some time lapse for the downloads...)</p>

#### [ Scott Morrison (Oct 06 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135312764):
<p><a href="https://www.youtube.com/watch?v=k8U6YOK7c0M&amp;feature=youtu.be" target="_blank" title="https://www.youtube.com/watch?v=k8U6YOK7c0M&amp;feature=youtu.be">https://www.youtube.com/watch?v=k8U6YOK7c0M&amp;feature=youtu.be</a></p>
<div class="youtube-video message_inline_image"><a data-id="k8U6YOK7c0M" href="https://www.youtube.com/watch?v=k8U6YOK7c0M&amp;feature=youtu.be" target="_blank" title="https://www.youtube.com/watch?v=k8U6YOK7c0M&amp;feature=youtu.be"><img src="https://i.ytimg.com/vi/k8U6YOK7c0M/default.jpg"></a></div>

#### [ Scott Morrison (Oct 06 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135312813):
<p>(This uses the latest update to the VS Code extension, which now offers to install elan and Lean for you, if it can't find them.)</p>

#### [ Scott Morrison (Oct 06 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135312818):
<p>Sometime in the next few days I will try to make a windows video as well.</p>

#### [ Chris Hughes (Oct 06 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135313619):
<blockquote>
<p>If you can somehow change it to "Christopher_Hughes" this will change the behaviour of things.</p>
</blockquote>
<p>I think this will be more effort than it's worth. I'm going back to my old setup</p>

#### [ Kevin Buzzard (Oct 06 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135314396):
<p>I've noticed that kids these days far prefer video tutorials to reading boring old web pages.</p>

#### [ Ryan Smith (Oct 07 2018 at 05:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135336887):
<p>I've been trying to get it working with elan on windows and this is not going well. I installed msys32 and elan, but when I try to run the package manager from the windows cmd line with leanpkg -v I get </p>
<p>'Smith\.elan\toolchains\stable\bin\..' is not recognized as an internal or external command,<br>
operable program or batch file.</p>
<p>Seems like elan / msys32 / something doesn't understand spaces in windows filenames</p>

#### [ Ryan Smith (Oct 07 2018 at 05:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135336895):
<p>I'm not fond of windows, but I do have to keep it on this computer for a reason.</p>

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135336949):
<p>This is a known issue and unfortunately I don't think there's an easy solution.</p>

#### [ Ryan Smith (Oct 07 2018 at 05:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135336951):
<p>Ok, if stuck on windows is there a better general approach then?</p>

#### [ Bryan Gin-ge Chen (Oct 07 2018 at 06:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135337050):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> might know. You can see he ran into the same problem earlier in the thread, and I think he has a working setup by some other means.</p>

#### [ Johan Commelin (Oct 07 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135337919):
<p><span class="user-mention" data-user-id="130170">@Ryan Smith</span> Looks like you have a space in your user name. This is known to break things.</p>

#### [ Ryan Smith (Oct 07 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135337920):
<p>Yeah I do. Is there a way around?</p>

#### [ Johan Commelin (Oct 07 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135337929):
<p>Dunno... haven't touched Windows in 15 years, and I don't use spaces in paths...</p>

#### [ Johan Commelin (Oct 07 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135337932):
<p>But Chris got it working</p>

#### [ Johan Commelin (Oct 07 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135337935):
<p>So to answer your question: Yes. There is a way around.</p>

#### [ Ryan Smith (Oct 07 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135337975):
<p>It's a dreadful system, been about as long for me. Somehow I thought it would have gotten better while I was away. Is macOS at least better supported right now?</p>

#### [ Johan Commelin (Oct 07 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135337976):
<p>How difficult is it to create a new user on Windows, and switch back and forth?</p>

#### [ Ryan Smith (Oct 07 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135337978):
<p>That would be doable if that's really the only blocking issue sure</p>

#### [ Johan Commelin (Oct 07 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135337979):
<p>What do you mean with "supported"? Support for Lean?</p>

#### [ Johan Commelin (Oct 07 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135337985):
<p>Lean on Mac seems to work pretty good.</p>

#### [ Ryan Smith (Oct 07 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135337988):
<p>Lean / elan since I was told things work better if you're using something to manage dependencies and stay up to date</p>

#### [ Johan Commelin (Oct 07 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135338037):
<p>Elan on Mac is a very smooth experience nowadays</p>

#### [ Ryan Smith (Oct 07 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135338094):
<p>Ok, cool. Will just switch off of my gf's computer and retry this on mac</p>

#### [ Johan Commelin (Oct 07 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135338100):
<p>1 sec</p>

#### [ Johan Commelin (Oct 07 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135338102):
<p>So, what you do:</p>

#### [ Johan Commelin (Oct 07 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135338105):
<p>(1) Install VScode, (2) Install the Lean extension in VScode, (3) Open a Lean file.</p>

#### [ Johan Commelin (Oct 07 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135338145):
<p>Afterwards, follow instructions, and it will install elan and lean for you</p>

#### [ Ryan Smith (Oct 07 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135338208):
<p>opening a lean file in vscode w/ extension does seem to call lean. I don't see anything about elan.</p>

#### [ Ryan Smith (Oct 07 2018 at 06:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135338210):
<p>I'm a complete newbie trying to get a feel for how it works, so that's a good start if I can pull in mathlib</p>

#### [ Johan Commelin (Oct 07 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135338253):
<p>It will only install elan/lean if it cannot find them</p>

#### [ Johan Commelin (Oct 07 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135338255):
<p>Did you already have something installed?</p>

#### [ Ryan Smith (Oct 07 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135338267):
<p>I installed via msys32, I assumed it was screwed up because invoking the package manager from the command line fails</p>

#### [ Johan Commelin (Oct 07 2018 at 06:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135338313):
<p>Is this still on windows?</p>

#### [ Ryan Smith (Oct 07 2018 at 06:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135338316):
<p>yeah, waited when you said you had a solution</p>

#### [ Johan Commelin (Oct 07 2018 at 06:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135338317):
<p>aah, sorry</p>

#### [ Johan Commelin (Oct 07 2018 at 06:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135338318):
<p>That was the mac solution</p>

#### [ Johan Commelin (Oct 07 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135338319):
<p>sorry for the confusion</p>

#### [ Ryan Smith (Oct 07 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135338325):
<p>ah cool, so the vscode extension installs everything else?</p>

#### [ Johan Commelin (Oct 07 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135338326):
<p>I just wanted you to know it, before logging off</p>

#### [ Ryan Smith (Oct 07 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135338383):
<p>thx for the help :)</p>

#### [ Kevin Buzzard (Oct 07 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135343067):
<blockquote>
<p>'Smith\.elan\toolchains\stable\bin\..' is not recognized as an internal or external command,<br>
operable program or batch file.</p>
</blockquote>
<p><code>Smith</code> is half of your username, isn't it :-(</p>
<p>This is an issue with elan. Having a space in your username in Windows is a terrible idea; I know from personal experience that <code>elan</code> is not the only thing it breaks.</p>

#### [ Kevin Buzzard (Oct 07 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135343069):
<p>Cheap Windows hack: <a href="https://xenaproject.wordpress.com/getting-lean-and-mathlib-running-in-the-mlc/" target="_blank" title="https://xenaproject.wordpress.com/getting-lean-and-mathlib-running-in-the-mlc/">https://xenaproject.wordpress.com/getting-lean-and-mathlib-running-in-the-mlc/</a></p>

#### [ Kevin Buzzard (Oct 07 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135343157):
<p>I will update this blog page and turn it from old and out-of-date instructions on how to run Lean at Imperial to a clearly signposted hack for win10 in general.</p>

#### [ Kevin Buzzard (Oct 07 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135344535):
<p><a href="https://xenaproject.wordpress.com/a-cheap-hack-to-get-lean-and-mathlib-running-on-a-windows-10-machine/" target="_blank" title="https://xenaproject.wordpress.com/a-cheap-hack-to-get-lean-and-mathlib-running-on-a-windows-10-machine/">https://xenaproject.wordpress.com/a-cheap-hack-to-get-lean-and-mathlib-running-on-a-windows-10-machine/</a></p>

#### [ Kevin Buzzard (Oct 07 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135344586):
<p>Summary: the correct elan method is causing problems for Windows 10 users with spaces in their file names. The link above <em>might</em> work better for them, and I'd be interested in feedback. <span class="user-mention" data-user-id="130170">@Ryan Smith</span> if you still have not got things going, can you try this method?</p>

#### [ Scott Olson (Oct 07 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135345978):
<p>I've narrowed down the elan problems with spaces to leanpkg, actually. I'm 95% sure this bat file is the culprit:  <a href="https://github.com/leanprover/lean/blob/master/bin/leanpkg.bat" target="_blank" title="https://github.com/leanprover/lean/blob/master/bin/leanpkg.bat">https://github.com/leanprover/lean/blob/master/bin/leanpkg.bat</a></p>
<p>The trouble comes with elan placing that in the homedir when the username has a space in it, but I believe it would also affect anyone who manually installed lean in any other path with a space in it.</p>

#### [ Scott Olson (Oct 07 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135345985):
<p>Now I'm trying to teach myself just enough .bat language to figure out why...</p>

#### [ Mario Carneiro (Oct 07 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135346024):
<p>not enough quotes?</p>

#### [ Scott Olson (Oct 07 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135346026):
<p>Almost surely, I just have no idea how .bat quoting works yet</p>

#### [ Kenny Lau (Oct 07 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135346028):
<p>Thanks <span class="user-mention" data-user-id="130491">@Scott Olson</span></p>

#### [ Mario Carneiro (Oct 07 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135346029):
<p>I think the last line should be </p>
<div class="codehilite"><pre><span></span>lean --run &quot;%LIBDIR%\leanpkg\leanpkg\main.lean&quot; %*
</pre></div>

#### [ Mario Carneiro (Oct 07 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135346038):
<p>I wonder if this is considered urgent enough to patch core</p>

#### [ Kenny Lau (Oct 07 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135346039):
<p>good luck getting those big guys patch it</p>

#### [ Scott Olson (Oct 07 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135346040):
<p>The <code>IF NOT EXIST</code> command also causes an error to print out</p>

#### [ Kenny Lau (Oct 07 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135346044):
<p>someone with much more threads than 4 can test if it works</p>

#### [ Scott Olson (Oct 07 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135346141):
<p>Quoting the <code>--run</code> arg and writing <code>IF NOT EXIST "%LIBDIR%"</code> seems to be enough</p>

#### [ Kenny Lau (Oct 07 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135346198):
<p>ok now then how to get the big guys to patch it</p>

#### [ Scott Olson (Oct 07 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135346206):
<p>lol I just noticed the commit that added leanpkg.bat was by a personal friend of mine. Maybe I'll start by asking them?</p>

#### [ Mario Carneiro (Oct 07 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135346207):
<p>If we can't patch core, the next best thing would be to store the patched file somewhere accessible from the tutorials "if you have problems with spaces, replace leanpkg.bat with this and try again"</p>

#### [ Mario Carneiro (Oct 07 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135346216):
<p>Pretty sure Corey doesn't have any magic access any more than we do</p>

#### [ Kenny Lau (Oct 07 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135346256):
<p>they'll say that this doesn't matter because half life 3 will soon be released</p>

#### [ Mario Carneiro (Oct 07 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135346258):
<p>I see <span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> is lurking, maybe he has magic access?</p>

#### [ Kenny Lau (Oct 07 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135346261):
<p>I mean, Lean 4</p>

#### [ Scott Olson (Oct 07 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135346279):
<p>Either way I'll make a PR after I double-check that I'm doing quoting the best way</p>

#### [ Scott Olson (Oct 07 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135346296):
<p>There's an open issue about it <a href="https://github.com/leanprover/lean/issues/1973" target="_blank" title="https://github.com/leanprover/lean/issues/1973">https://github.com/leanprover/lean/issues/1973</a></p>

#### [ Kevin Buzzard (Oct 07 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135346332):
<p>I guess Sebastian Ullrich might consider patching it -- he is interested in making this sort of infrastructure work, and there's a fair chance that this problem will still be there in Lean 4.</p>

#### [ Kenny Lau (Oct 07 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135346441):
<p>you mean Half Life 3</p>

#### [ Kevin Buzzard (Oct 07 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135346555):
<p>Half life 3 --- 1/8'th life.</p>

#### [ Gabriel Ebner (Oct 07 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135346789):
<p>I wouldn't count on a fix making it into a new Lean 3 release.  A more brutal solution would be to include a patch in elan or the vscode extension.  Given that Lean 3 is end-of-lifed, I'd accept a PR to the vscode extension that patches leanpkg.bat on windows.</p>

#### [ Scott Morrison (Oct 07 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135346870):
<p>oh, that's a good idea</p>

#### [ Scott Olson (Oct 07 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135347481):
<p>FYI I made the PR at <a href="https://github.com/leanprover/lean/pull/1976" target="_blank" title="https://github.com/leanprover/lean/pull/1976">https://github.com/leanprover/lean/pull/1976</a></p>

#### [ Ryan Smith (Oct 08 2018 at 03:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135374241):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> Trying to install the lean plugin to vscode on macOS followed by opening a lean file does not install elan &amp; lean, instead I just get file 'init' not found in the LEAN_PATH</p>

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 03:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135374338):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> is the author of that installation feature. He should be able to help.</p>

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 03:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135374631):
<p>Are you possibly running into <a href="https://github.com/leanprover/vscode-lean/issues/73" target="_blank" title="https://github.com/leanprover/vscode-lean/issues/73">this issue</a> ? I think if you're getting that error you ought to have lean and elan on your system. Does <code>lean --version</code> in a console do anything?</p>

#### [ Ryan Smith (Oct 08 2018 at 04:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135374794):
<p>Lean (version 3.4.1, commit 17fe3decaf8a, Release)<br>
This time the plugin brought up an installation for elan, but when I'm trying to do a basic sanity check with Kevin's example of<br>
import analysis.real<br>
#check real<br>
I'm not getting anything</p>

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 04:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135374838):
<p>Do you see orange bars on the side? If so, that means lean is busy processing the file and its imports.</p>

#### [ Ryan Smith (Oct 08 2018 at 04:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135374839):
<p>I retract that: it took a very long time but it came back with \R! I think that means it's running and math lib import is ok?</p>

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 04:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135374848):
<p>Yes. To speed up this process in the future, you can run <code>lean --make</code> in your package directory.</p>

#### [ Ryan Smith (Oct 08 2018 at 04:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135374849):
<p>Do you need to re run make if you edit your src files?</p>

#### [ Mario Carneiro (Oct 08 2018 at 04:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135374955):
<p>vscode will automatically compile stuff in memory when you make edits, but they aren't saved when you quit</p>

#### [ Bryan Gin-ge Chen (Oct 08 2018 at 04:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135375255):
<p>Running <code>lean --make</code> generates <code>.olean</code> files, which are object files that lean generates when it compiles the <code>.lean</code> source files.  If you have lots of files that import each other then doing this lets the lean server in the VS code extension avoid re-compiling all of your imports when it starts up.</p>
<p>So if you're just editing small files that import only from mathlib, running <code>lean --make</code> again won't really be necessary. If you do want to run it, then as long as you haven't made changes to your package's copy of mathlib (e.g. by upgrading) or otherwise written / edited lots of files that you need to import, running <code>lean --make</code> after the first time will be much faster since it tries not to recompile files whose dependencies haven't changed.</p>

#### [ Ryan Smith (Oct 08 2018 at 04:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135375349):
<p>Great, thanks</p>

#### [ Scott Morrison (Oct 08 2018 at 06:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135378646):
<blockquote>
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> Trying to install the lean plugin to vscode on macOS followed by opening a lean file does not install elan &amp; lean, instead I just get file 'init' not found in the LEAN_PATH</p>
</blockquote>
<p>Hi <span class="user-mention" data-user-id="130170">@Ryan Smith</span>, I'd like to understand what happened here. Did you have <code>LEAN_PATH</code> set already? That's likely to cause problems. It sounds like a moment later the plugin did work, and installed elan for you.</p>

#### [ Neil Strickland (Oct 12 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135675488):
<p>I am sorry to rant, but these complaints about spaces in user names are silly.</p>
<p>Allowing spaces in user names is a completely ordinary, benign design decision.  It creates a need to escape strings in certain circumstances, but that is again a completely ordinary issue, which arises all over the place in software development in many different contexts.  There are many, many thousands of programs that handle Windows paths correctly, and it does not take any magic to write them.  If a certain program is broken by spaces in path names, that just means that the developers did not take the straightforward and standard steps necessary to avoid that problem.</p>

#### [ Johan Commelin (Oct 12 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135677340):
<p><span class="user-mention" data-user-id="130308">@Neil Strickland</span> I agree that it is not very user friendly. There have been efforts to figure out what is wrong, and people are trying to patch it up.</p>

#### [ Gabriel Ebner (Oct 12 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135677718):
<p>I feel like the last line was partly directed at me, so let me respond.  Neither Leo, Sebastian, or me are using windows.  I am sorry but I don't think any of us are aware of the "straightforward and standard steps" in windows cmd.exe programming.  The windows-specific parts of the code base are in general less well tested.  Now is probably not the ideal time, but in general feel free to submit fixes for these platform-specific bugs.</p>

#### [ Reid Barton (Oct 12 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135681803):
<p>This is a common problem for open-source projects: there are many fewer developers using Windows than Linux or OS X and Windows is fundamentally unfamiliar to users of Unix-type systems. The result is usually that Windows is not as well supported as it could be. We have this problem with the Haskell compiler (GHC) as well--we've recently got one (volunteer) developer who actually understands Windows who's got a ~20 year backlog of Windows-specific issues to work through, including stuff like the interpreter not crashing when it tries to print Unicode characters to the console. And GHC is a project with a far larger user and developer base than Lean. (It also happens to be another project whose primary developer is at MSR.)</p>

#### [ Reid Barton (Oct 12 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135682122):
<p>That said, the Unix-y equivalent of <code>leanpkg.bat</code> is also missing quotes in the same place. I guess nobody has spaces in their usernames on Unix-y systems <span class="emoji emoji-1f643" title="upside down">:upside_down:</span></p>

#### [ Neil Strickland (Oct 12 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135682156):
<p><span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> Thanks for the response.  I think that the only cmd.exe related problem is probably resolved by Reid Barton's recent fix to leanpkg.bat.  However, there are other issues caused by passing unescaped strings to CreateProcess() in src/library/process.cpp via exec_cmd and io.proc.spawn, and by using external processes to make or detect directories instead of calling CreateDirectory() and PathFileExists().  That is surely not the recommended approach even in POSIX systems.  If I had an appropriate build environment then I would attempt to fix this myself, but I do not know how hard it would be to set that up.</p>

#### [ Johan Commelin (Oct 12 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135682261):
<blockquote>
<p>That said, the Unix-y equivalent of <code>leanpkg.bat</code> is also missing quotes in the same place. I guess nobody has spaces in their usernames on Unix-y systems <span class="emoji emoji-1f643" title="upside down">:upside_down:</span></p>
</blockquote>
<p>Right. When you live in the shell, you quickly learn to use sane paths.</p>

#### [ Reid Barton (Oct 12 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135682274):
<p>(Not my fix, but <span class="user-mention" data-user-id="130491">@Scott Olson</span>'s)</p>

#### [ Reid Barton (Oct 12 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135683015):
<blockquote>
<p>However, there are other issues caused by passing unescaped strings to CreateProcess() in src/library/process.cpp via exec_cmd and io.proc.spawn, and by using external processes to make or detect directories instead of calling CreateDirectory() and PathFileExists().  That is surely not the recommended approach even in POSIX systems.</p>
</blockquote>
<p>I think <span class="user-mention" data-user-id="110111">@Keeley Hoek</span> has a fork which fixes some issues like this for Windows.</p>

#### [ Reid Barton (Oct 12 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135684027):
<p>I didn't realize that Windows doesn't have an equivalent of the command-line argument list. I guess I knew that DOS worked that way...</p>

#### [ Scott Olson (Oct 12 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/updating%20Kevin%27s%20installation%20instructions/near/135684178):
<p>heh, yeah, I just learned that the other day when I went diving into elan's code and the Rust standard library to figure out how process creation worked on Windows</p>


{% endraw %}
