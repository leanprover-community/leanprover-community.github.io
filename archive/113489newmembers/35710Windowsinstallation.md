---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/35710Windowsinstallation.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [Windows installation](https://leanprover-community.github.io/archive/113489newmembers/35710Windowsinstallation.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ JDM (Sep 22 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Windows%20installation/near/134429178):
<p>Hi everyone! I'm trying to get Lean to work with Visual Studio, but I'm having trouble setting the installation path. Can anyone help? Much appreciated!</p>

#### [ Kevin Buzzard (Sep 22 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Windows%20installation/near/134430635):
<p>I'm sorry (on behalf of the community). Installation is still a pain, especially on Windows. Does this <a href="https://xenaproject.wordpress.com/2017/12/02/how-to-install-mathlib-and-keep-it-up-to-date/" target="_blank" title="https://xenaproject.wordpress.com/2017/12/02/how-to-install-mathlib-and-keep-it-up-to-date/">https://xenaproject.wordpress.com/2017/12/02/how-to-install-mathlib-and-keep-it-up-to-date/</a> help? There's a bit saying something like "Pro tip -- if's in red it's bad, if it's in orange it's good". I had users installing Lean in C:\Program Files and then having problems with quoting the space, which seems hit and miss to me. If it doesn't help then tell me how to improve that post, and/or say more precisely what the problem is. People here can help but it is a real bore getting started.</p>

#### [ JDM (Sep 22 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Windows%20installation/near/134432636):
<p>No need to be sorry, as I understand there's a lot of pain involved in trying to find a  working solution for Windows, and as this is an open source effort, I can only be awestruck by the efforts already done :-) I'll try to see if your post is of any help, and if not I might just try VirtualBox again (but I had some trouble with establishing an internet connection in the<br>
 past, which is why I've avoided it until now) Already many thanks :-)</p>

#### [ Hendrik (Sep 24 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Windows%20installation/near/134513082):
<blockquote>
<p>I'm sorry (on behalf of the community). Installation is still a pain, especially on Windows. Does this <a href="https://xenaproject.wordpress.com/2017/12/02/how-to-install-mathlib-and-keep-it-up-to-date/" target="_blank" title="https://xenaproject.wordpress.com/2017/12/02/how-to-install-mathlib-and-keep-it-up-to-date/">https://xenaproject.wordpress.com/2017/12/02/how-to-install-mathlib-and-keep-it-up-to-date/</a> help? There's a bit saying something like "Pro tip -- if's in red it's bad, if it's in orange it's good". I had users installing Lean in C:\Program Files and then having problems with quoting the space, which seems hit and miss to me. If it doesn't help then tell me how to improve that post, and/or say more precisely what the problem is. People here can help but it is a real bore getting started.</p>
</blockquote>
<p>I would replace the following text by something more elaborate: </p>
<blockquote>
<p>On Windows, you are going to need something called “msys2” (which will give you a terminal window so you can type commands in on a “command line” instead of just clicking on stuff).</p>
</blockquote>
<p>It does not only give you a terminal but it actually gives you the only working terminal. There should be an explicit mention that powershell, mingw, cmd all don't work (but git bash may work for most operations).</p>
<p>In the long run, leanpkg itself should potentially try to find out what shell environment it is started from and then avoid using "test", etc.. Getting it to work 100% with git bash would be a great intermediate step.</p>
<p>A second comment I have is that users of a multi-user system often don't have the choice to avoid path names without spaces. They may be authorized to install programs in Z:\Users\Bob the builder\Program Files\ only. This is especially true for students.</p>
<p>Third, these instructions should probably be very prominently placed in the manual (not via a link but the text itself).</p>
<p>Many thanks for all the efforts!</p>

#### [ Kevin Buzzard (Sep 24 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Windows%20installation/near/134513162):
<p>One of the biggest mistakes I ever made on a Windows machine was creating a userid with spaces in</p>


{% endraw %}
