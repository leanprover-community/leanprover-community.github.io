---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/22596cheapWindowsinstall.html
---

## Stream: [general](index.html)
### Topic: [cheap Windows install](22596cheapWindowsinstall.html)

---


{% raw %}
#### [ Kevin Buzzard (Sep 25 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cheap%20Windows%20install/near/134581500):
<p>Over the weekend, all of the PC's in the computer room where we do Xena got upgraded from Windows 7 to Windows 10 (the hardware didn't change, but they are decent machines). One of the things I did yesterday (when I was ignoring chat) was to get bleeding edge Lean and make a basic repository with a toml and path file and one .lean file with a proof that 2+2=4, add mathlib as a dependency, make all the .olean files and then zip the whole lot up at <a href="http://wwwf.imperial.ac.uk/~buzzard/xena/Xena.zip" target="_blank" title="http://wwwf.imperial.ac.uk/~buzzard/xena/Xena.zip">http://wwwf.imperial.ac.uk/~buzzard/xena/Xena.zip</a> . </p>
<p>Why do this? Because now here are my instructions for students wanting to use Lean (which is not installed by default) on our departmental PC's. Note that VS Code _is_ installed. </p>
<p>1) Download Xena.zip, put on your desktop, unpack.<br>
2) Fire up VS Code, File-&gt;Preferences-&gt;Settings, fix path to lean executable<br>
3) Open default project folder (something like Xena/my_project, I forget)<br>
4) Done.</p>
<p>Note: no mention of git and <em>no mention of a terminal</em>, mathlib imports work out the box, and start-up time was no more than a few seconds on these machines. Music to the basic Windows-users ears! The .olean files <em>seemed</em> to be portable from machine to machine (all machines have pretty much exactly the same build, and are reset every night somehow -- all user interference is wiped and they become canonically isomorphic machines from the point of view of local disc content). </p>
<p>I would be interested to hear anyone else's experience with using this zip file on a Windows 10 machine. Although it sounds stupid, I tried it on a linux machine without changing my version of Lean (I don't think linux can make much sense of <code>lean.exe</code>) but it didn't work at all -- all of the imports failed. I put this down to all the .olean files being unreadable, or whatever. But for this project I was only interested in Windows anyway and initial results have been positive.</p>

#### [ Keeley Hoek (Sep 25 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cheap%20Windows%20install/near/134584214):
<p>Just for information: the windows <code>.exe</code> file is in a different format to what linux expects (and can read), and even if it could be read it expects to interact with the windows standard library, which is not the same as what is present on linux. Different executables must be built for each</p>

#### [ Keeley Hoek (Sep 25 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cheap%20Windows%20install/near/134584217):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> when writing elan, did you ever get a chance to test out the windows installer before it got deleted from the repo? If you did, do you remember what was broken?</p>

#### [ Kevin Buzzard (Sep 25 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cheap%20Windows%20install/near/134589990):
<p><span class="user-mention" data-user-id="110111">@Keeley Hoek</span> I do understand that linux won't be remotely interested in the <code>lean.exe</code> file in the repo. What I was surprised about was the errors I got. On linux, I opened the folder containing the sample project and left VS code pointing out the ELF executable, but I got errors about imports failing. I suspect it might be something to do with the olean files not being compatible across OS's but I'm not sure.</p>

#### [ Keeley Hoek (Sep 25 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cheap%20Windows%20install/near/134590500):
<p>Sorry, I understand now! Also, that's very surprising... it'd be interesting to find out why.</p>
<p>I'd expect that leanpkg wouldn't work on those VS Code setups. Is that right? If it's ever a problem, I've fixed up leanpkg to work natively on windows here: <a href="https://github.com/khoek/klean/releases" target="_blank" title="https://github.com/khoek/klean/releases">https://github.com/khoek/klean/releases</a><br>
You can also grab this version very easily though elan<br>
(I can make the repo name less pretentious, but thought it was a fun joke :D)</p>

#### [ Kevin Buzzard (Sep 25 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cheap%20Windows%20install/near/134592725):
<p>This is for one-off installs for experimental use on computers which will be wiped at the end of the day, I am not expecting to support leanpkg. My idea is that if people want a more recent mathlib or some newer Lean 3 bugfix release I can just update the zip file.</p>

#### [ Keeley Hoek (Sep 25 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cheap%20Windows%20install/near/134594631):
<p>sure, sounds great!</p>

#### [ Sebastian Ullrich (Sep 25 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cheap%20Windows%20install/near/134607555):
<p><span class="user-mention" data-user-id="110111">@Keeley Hoek</span> </p>
<blockquote>
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> when writing elan, did you ever get a chance to test out the windows installer before it got deleted from the repo? If you did, do you remember what was broken?</p>
</blockquote>
<p>No, I never tried it</p>

#### [ Neil Strickland (Jan 23 2019 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cheap%20Windows%20install/near/156729004):
<p>I'll mention again that there is a Windows installer at <a href="http://bim.shef.ac.uk/lean" target="_blank" title="http://bim.shef.ac.uk/lean">bim.shef.ac.uk/lean</a>.  It tries to set up git, elan, Vs code, mathlib and a sample workspace.  I have tested it on several machines but not very thoroughly.</p>

#### [ Kenny Lau (Jan 23 2019 at 23:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cheap%20Windows%20install/near/156729415):
<p>it's a dream come true!</p>

#### [ Kevin Buzzard (Jan 24 2019 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cheap%20Windows%20install/near/156733891):
<p>Presumably you need admin to run it?</p>

#### [ Neil Strickland (Jan 24 2019 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cheap%20Windows%20install/near/156757620):
<p>The current version puts both git and vs code in C:\Program Files and so needs admin rights.  Lean itself goes in %HOME%\.elan. Probably it would be possible to make a different version that puts git and vs code in %APPDATA% and so does not need admin rights.  Do you think that that would be useful?</p>

#### [ Kevin Buzzard (Jan 24 2019 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cheap%20Windows%20install/near/156760805):
<p>I only ask because I don't have admin rights on the PC's at work.</p>


{% endraw %}
