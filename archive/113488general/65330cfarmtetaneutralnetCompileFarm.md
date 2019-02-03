---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/65330cfarmtetaneutralnetCompileFarm.html
---

## Stream: [general](index.html)
### Topic: [cfarm.tetaneutral.net - Compile Farm](65330cfarmtetaneutralnetCompileFarm.html)

---


{% raw %}
#### [ Kenny Lau (Oct 09 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135489637):
<p><span class="user-mention" data-user-id="122318">@Tobias Grosser</span> I have an account now. How do I use it?</p>

#### [ Johan Commelin (Oct 09 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135490060):
<blockquote>
<p><span class="user-mention" data-user-id="122318">@Tobias Grosser</span> I have an account now. How do I use it?</p>
</blockquote>
<p>We need a Would-you-please-move-this-to-another-thread-Thank-you-emoji</p>

#### [ Reid Barton (Oct 09 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135491195):
<p>Looks like the instructions are at <a href="https://cfarm.tetaneutral.net/machines/list/" target="_blank" title="https://cfarm.tetaneutral.net/machines/list/">https://cfarm.tetaneutral.net/machines/list/</a>, just ssh into one of the machines</p>

#### [ Kenny Lau (Oct 09 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135491224):
<p>it requires a password and I don't know where to get the password from</p>

#### [ Reid Barton (Oct 09 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135491301):
<p>Oh, uh... hmm. I would assume you're supposed to use ssh certificates but I also don't see how to set that up</p>

#### [ Reid Barton (Oct 09 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135491328):
<p>I just requested an account a minute or two ago, so I don't know.<br>
I see there is a Login link in the top right of the web page though</p>

#### [ Tobias Grosser (Oct 09 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135497171):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span>, indeed. Sorry for this distraction.</p>

#### [ Tobias Grosser (Oct 09 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135497287):
<p>I use my ssh key to login. Not sure how this is handled today, but either you should have had a way to specify a password when registering or an ssh key, I assume.</p>

#### [ Tobias Grosser (Oct 09 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135497370):
<p>The website states: Once your account is created, you will be able to upload SSH keys and gain SSH access to all machines of the platform.</p>

#### [ Tobias Grosser (Oct 09 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135497395):
<p>So seems you need to wait until your account is confirmed.</p>

#### [ Reid Barton (Oct 10 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135503836):
<p>I have an account now and I uploaded an SSH public key using the web interface but it takes some time for the key to be propagated to the machines. Kenny are you in the same situation?</p>

#### [ Kenny Lau (Oct 10 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135504194):
<p>I have no idea what SSH is</p>

#### [ Kenny Lau (Oct 10 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135504205):
<p>what do you mean by upload an SSH public key</p>

#### [ Bryan Gin-ge Chen (Oct 10 2018 at 00:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135504482):
<p>You'll want to do something like this <a href="https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/#platform-windows" target="_blank" title="https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/#platform-windows">https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/#platform-windows</a></p>

#### [ Reid Barton (Oct 10 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135505466):
<p>Yes, then you can use the cfarm web interface to add the ssh key to your account</p>

#### [ Johan Commelin (Oct 10 2018 at 03:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135511481):
<blockquote>
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span>, indeed. Sorry for this distraction.</p>
</blockquote>
<p>No worries (-;</p>

#### [ Kenny Lau (Oct 10 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135566947):
<p>So what do I do when they ask me for the password?</p>

#### [ Scott Morrison (Oct 11 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135571403):
<p>Upload an ssh key, so it doesn't ask you for a password?</p>

#### [ Kenny Lau (Oct 11 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135571587):
<p>it's still asking me for a password</p>

#### [ Kenny Lau (Oct 11 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135571589):
<p>and 1.5 hour has already passed</p>

#### [ Reid Barton (Oct 11 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135571947):
<p>I had to wait at least several hours (haven't tried to log in today)</p>

#### [ Reid Barton (Oct 11 2018 at 04:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135581252):
<p>I can now log in. Time to see if I can build lean on a POWER8 system</p>

#### [ Reid Barton (Oct 11 2018 at 05:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135584158):
<p>ok, got this working now... 2406 is the CPU% column</p>
<div class="codehilite"><pre><span></span> 31366 rwbarton  20   0 10.851g 3.304g  15872 S  2406  1.3  50:19.98 lean
</pre></div>

#### [ Reid Barton (Oct 11 2018 at 05:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135584219):
<p>The big sparc machine had unsatisfactory results--the release version of lean crashed, and the debug version mostly doesn't crash, but building mathlib did trigger some assertion and is super slow.</p>
<div class="codehilite"><pre><span></span>LEAN ASSERTION VIOLATION
File: /home/rwbarton/lean/lean/src/library/type_context.cpp
Line: 1230
Task: /home/rwbarton/lean/mathlib2/computability/primrec.lean: primcodable.prod
idx &lt; m_tmp_data-&gt;m_uassignment.size()
</pre></div>

#### [ Reid Barton (Oct 11 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135584707):
<p>mathlib on the POWER8 machine:</p>
<div class="codehilite"><pre><span></span>&gt; lean --make .
28590.38user 105.69system 18:55.94elapsed 2526%CPU (0avgtext+0avgdata 10297280maxresident)k
</pre></div>


<p>Pretty parallel but not so good single-threaded performance</p>

#### [ Reid Barton (Oct 11 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135584713):
<p>Maybe tomorrow I'll try the xeons</p>

#### [ Reid Barton (Oct 11 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135585081):
<p>Aha, this machine is actually 20 cores with 8-way SMT (IBM equivalent of hyperthreading)</p>

#### [ Reid Barton (Oct 11 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135585133):
<p>I wonder if that means a well-chosen cpu set would be faster</p>

#### [ Kenny Lau (Oct 11 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135594900):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> could you teach me how to use it?</p>

#### [ Kenny Lau (Oct 11 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135594908):
<p>I just connect ssh and then do <code>lean --make</code>?</p>

#### [ Kenny Lau (Oct 11 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135594914):
<p>how do I make sure I'm using the server's CPU?</p>

#### [ Kenny Lau (Oct 11 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135595827):
<p>ok I can see that it automatically redirects me to the server</p>

#### [ Kenny Lau (Oct 11 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135595836):
<p>but now how do I communicate between the server and my computer?</p>

#### [ Johan Commelin (Oct 11 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135595896):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> What kind of communication do you want?</p>

#### [ Johan Commelin (Oct 11 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135595903):
<p>You can copy files</p>

#### [ Kenny Lau (Oct 11 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135595904):
<p>how?</p>

#### [ Johan Commelin (Oct 11 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135595907):
<p><code>scp</code></p>

#### [ Johan Commelin (Oct 11 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135595915):
<p>It uses <code>ssh</code></p>

#### [ Johan Commelin (Oct 11 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135595919):
<p>But what do you want to copy?</p>

#### [ Johan Commelin (Oct 11 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135595926):
<p>Can't you just <code>git clone</code> on that server?</p>

#### [ Kenny Lau (Oct 11 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135595937):
<p>then how do I send the olean files back?</p>

#### [ Johan Commelin (Oct 11 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135595952):
<p>Aah, from the server to your box?</p>

#### [ Kenny Lau (Oct 11 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135595957):
<p>both ways</p>

#### [ Johan Commelin (Oct 11 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135595961):
<p>Both times <code>scp</code> on your box</p>

#### [ Kenny Lau (Oct 11 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135595967):
<p>how to use <code>scp</code>?</p>

#### [ Johan Commelin (Oct 11 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596019):
<p><code>scp my_file.olean server:~/destination.olean</code></p>

#### [ Johan Commelin (Oct 11 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596028):
<p><code>scp -r server:~/a_directory/ my_directory/</code> ## recursive</p>

#### [ Kenny Lau (Oct 11 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596053):
<p>what is <code>-R</code>?</p>

#### [ Johan Commelin (Oct 11 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596062):
<p>Sorry, should be <code>-r</code>.</p>

#### [ Johan Commelin (Oct 11 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596091):
<p><code>scp</code> can also be used as <code>scp server1:path1 server2:path2</code>. It's pretty general (-;</p>

#### [ Johan Commelin (Oct 11 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596150):
<p>I guess there are ways to recurse and only copy olean files.</p>

#### [ Johan Commelin (Oct 11 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596157):
<p>Maybe <code>rsync</code> can help. It will also use your ssh keys.</p>

#### [ Johan Commelin (Oct 11 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596163):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> What OS are you on?</p>

#### [ Kenny Lau (Oct 11 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596166):
<p>windows</p>

#### [ Johan Commelin (Oct 11 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596196):
<p>/me shuts his eyes while Tux <span class="emoji emoji-1f427" title="penguin">:penguin:</span> slaps Kenny in the face.</p>

#### [ Johan Commelin (Oct 11 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596251):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> I'm not sure if <code>rsync</code> is available. Can you try if it is?</p>

#### [ Kenny Lau (Oct 11 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596254):
<p>it is</p>

#### [ Johan Commelin (Oct 11 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596261):
<p>You're lucky (-;</p>

#### [ Kenny Lau (Oct 11 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596264):
<p>I'm using something that has the unix commands</p>

#### [ Johan Commelin (Oct 11 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596372):
<p>Do you know <code>man</code>?</p>

#### [ Kenny Lau (Oct 11 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596412):
<p>oh no <code>scp</code> is copying the files one by one</p>

#### [ Kenny Lau (Oct 11 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596418):
<p>it will take years</p>

#### [ Johan Commelin (Oct 11 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596427):
<p><code>Ctrl-C</code></p>

#### [ Johan Commelin (Oct 11 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596429):
<p>Also try <code>man man</code>.</p>

#### [ Kenny Lau (Oct 11 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596489):
<p>so how do I even use this if I can't copy the files</p>

#### [ Johan Commelin (Oct 11 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596494):
<p>Did you try <code>man man</code>?</p>

#### [ Kenny Lau (Oct 11 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596498):
<p>yes</p>

#### [ Johan Commelin (Oct 11 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596508):
<p>What happened?</p>

#### [ Kenny Lau (Oct 11 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596512):
<p>i get a long manual?</p>

#### [ Johan Commelin (Oct 11 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596514):
<p>Great. Try <code>man rsync</code></p>

#### [ Kenny Lau (Oct 11 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596578):
<p>how do I refer to my computer from the server?</p>

#### [ Johan Commelin (Oct 11 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596583):
<p>That's harder.</p>

#### [ Kenny Lau (Oct 11 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596587):
<p>:(</p>

#### [ Johan Commelin (Oct 11 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596588):
<p>You can setup a reverse tunnel using ssh</p>

#### [ Johan Commelin (Oct 11 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596600):
<p>See <code>man ssh</code></p>

#### [ Johan Commelin (Oct 11 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596614):
<p>But why would you want that?</p>

#### [ Kenny Lau (Oct 11 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596636):
<p>I don't have rsync, but the server has rsync</p>

#### [ Johan Commelin (Oct 11 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596704):
<p>Aah, to use <code>rsync</code> the other side needs some form of an ssh server I think. So that won't help you.</p>

#### [ Johan Commelin (Oct 11 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596713):
<p>A better solution would be to install rsync locally.</p>

#### [ Kenny Lau (Oct 11 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596720):
<p>how do I do that?</p>

#### [ Johan Commelin (Oct 11 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596727):
<p>I dunno. Haven't touched windows in 15 years.</p>

#### [ Kenny Lau (Oct 11 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596729):
<p>just treat me as using bash</p>

#### [ Johan Commelin (Oct 11 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135596734):
<p>You know that the latest Total War series also runs on Linux?</p>

#### [ Kenny Lau (Oct 11 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135598090):
<p>ok so I <code>rsync</code>ed lean and mathlib, but now I can't run lean.exe</p>

#### [ Andrew Ashworth (Oct 11 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135599665):
<p>You won't be able to do what you want with a Windows host machine</p>

#### [ Andrew Ashworth (Oct 11 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135599674):
<p>Oleans aren't compatible between operating systems</p>

#### [ Kevin Buzzard (Oct 11 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135605471):
<p>exes are certainly not compatible between operating systems</p>

#### [ Kenny Lau (Oct 11 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135610588):
<p>this is so sad</p>

#### [ Johan Commelin (Oct 11 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135610648):
<p>Right. Please blame Bill Gates.</p>

#### [ Kenny Lau (Oct 11 2018 at 16:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135610978):
<p>so then how do you install lean on linux?</p>

#### [ Johan Commelin (Oct 11 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135611116):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> Would you mind explaining the bigger goal that you have in mind with this service?</p>

#### [ Johan Commelin (Oct 11 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135611154):
<p>Also is X installed on that server, can you do ssh with X forwarding? If so, just install VScode, and run it on the server. The rest is history.</p>

#### [ Johan Commelin (Oct 11 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135611165):
<p>But I guess that you can't have X forwarding.</p>

#### [ Kenny Lau (Oct 11 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135611189):
<p>well with this service I can test the compile times quicklier</p>

#### [ Johan Commelin (Oct 11 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135611361):
<p>Have you looked at the travis config?</p>

#### [ Johan Commelin (Oct 11 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135611366):
<p>For mathlib on github</p>

#### [ Johan Commelin (Oct 11 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135611378):
<p>It will tell Travis how to compile mathlib. I guess it could also tell you how to use this server</p>

#### [ Johan Commelin (Oct 11 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135611385):
<p><a href="https://github.com/leanprover/mathlib/blob/master/.travis.yml" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/.travis.yml">https://github.com/leanprover/mathlib/blob/master/.travis.yml</a></p>

#### [ Kenny Lau (Oct 11 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135611432):
<div class="codehilite"><pre><span></span>[kc_kennylau@gcc2-power8 ~]$ curl https://raw.githubusercontent.com/Kha/elan/master/elan-init.sh -sSf | sh -s -- --default-toolchain none -y
info: downloading installer
curl: (22) The requested URL returned error: 404 Not Found
elan: command failed: curl -sSfL https://github.com/Kha/elan/releases/download/v0.7.1/elan-powerpc64le-unknown-linux-gnu.tar.gz -o /tmp/tmp.Yt4psW5eYO/elan-init.tar.gz
</pre></div>

#### [ Johan Commelin (Oct 11 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135611536):
<p><code>which wget</code></p>

#### [ Johan Commelin (Oct 11 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135611546):
<p>Oh nvm</p>

#### [ Johan Commelin (Oct 11 2018 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135611550):
<p>I didn't read the error</p>

#### [ Johan Commelin (Oct 11 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135611649):
<p>That <code>elan</code> command is asking <code>curl</code> to write something to <code>/tmp/</code>. Maybe you don't have permissions there?</p>

#### [ Johan Commelin (Oct 11 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135611686):
<p>But <code>curl</code> is also getting a 404</p>

#### [ Johan Commelin (Oct 11 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135611689):
<p>Before that</p>

#### [ Kenny Lau (Oct 11 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135611768):
<p>then how did Tobias Grosser manage to do it</p>

#### [ Johan Commelin (Oct 11 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135611771):
<p>This explains why: <a href="https://github.com/Kha/elan/releases/" target="_blank" title="https://github.com/Kha/elan/releases/">https://github.com/Kha/elan/releases/</a></p>

#### [ Johan Commelin (Oct 11 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135611780):
<p>You are on a powerpc</p>

#### [ Johan Commelin (Oct 11 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135611791):
<p>That architecture is not supported by <code>elan</code>.</p>

#### [ Johan Commelin (Oct 11 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135611801):
<p><span class="user-mention" data-user-id="122318">@Tobias Grosser</span> Can you tell how you did this?</p>

#### [ Tobias Grosser (Oct 11 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135612036):
<p>I did not get anything running on powerpc</p>

#### [ Tobias Grosser (Oct 11 2018 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135612101):
<p>$ssh <a href="http://gcc20.fsffrance.org" target="_blank" title="http://gcc20.fsffrance.org">gcc20.fsffrance.org</a></p>

#### [ Tobias Grosser (Oct 11 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135612170):
<p>In fact, I did not use the compilefarm to compile lean.</p>

#### [ Tobias Grosser (Oct 11 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135612179):
<p>I would start with <a href="http://gcc20.fsffrance.org" target="_blank" title="http://gcc20.fsffrance.org">gcc20.fsffrance.org</a></p>

#### [ Tobias Grosser (Oct 11 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135612241):
<p>The easiest is probably to create a linux docker image with a current lean environment.</p>

#### [ Tobias Grosser (Oct 11 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135612267):
<p>And then use udocker to run it.</p>

#### [ Tobias Grosser (Oct 11 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135612274):
<p>Also, I am not sure kenny why you want to copy files.</p>

#### [ Kenny Lau (Oct 11 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135612283):
<p>ignore the part about copying files</p>

#### [ Tobias Grosser (Oct 11 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135612287):
<p>OK.</p>

#### [ Tobias Grosser (Oct 11 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135612298):
<p>In theory you should be able to just run:</p>

#### [ Tobias Grosser (Oct 11 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135612306):
<p>grosser@gcc20:~$       curl <a href="https://raw.githubusercontent.com/Kha/elan/master/elan-init.sh" target="_blank" title="https://raw.githubusercontent.com/Kha/elan/master/elan-init.sh">https://raw.githubusercontent.com/Kha/elan/master/elan-init.sh</a> -sSf | sh -s -- --default-toolchain none -y<br>
info: downloading installer</p>
<p>/tmp/tmp.OXhfu8gCPt/elan-init: /lib/x86_64-linux-gnu/libc.so.6: version <code>GLIBC_2.15' not found (required by /tmp/tmp.OXhfu8gCPt/elan-init)
/tmp/tmp.OXhfu8gCPt/elan-init: /lib/x86_64-linux-gnu/libc.so.6: version </code>GLIBC_2.14' not found (required by /tmp/tmp.OXhfu8gCPt/elan-init)<br>
grosser@gcc20:~$</p>

#### [ Tobias Grosser (Oct 11 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135612314):
<p>Unfortunately this gives an error</p>

#### [ Tobias Grosser (Oct 11 2018 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135612324):
<p>As the glibc version is not correct.</p>

#### [ Tobias Grosser (Oct 11 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135613129):
<p>What you can do instead on gcc20:</p>
<div class="codehilite"><pre><span></span>curl https://raw.githubusercontent.com/indigo-dc/udocker/master/udocker.py &gt; udocker
chmod u+rx ./udocker
./udocker install
./udocker pull ubuntu
./udocker create --name=lean ubuntu
./udocker run lean
apt-get update
apt-get install curl git
curl https://raw.githubusercontent.com/Kha/elan/master/elan-init.sh -sSf | sh -s -- --default-toolchain none -y
 git clone https://github.com/leanprover/mathlib.git
leanpkg --make
</pre></div>


<p>to get back into your lean folder just run</p>
<div class="codehilite"><pre><span></span>./udocker run lean
cd mathlib
ls
</pre></div>

#### [ Reid Barton (Oct 11 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135613307):
<p>I feel obliged to point out that copying build results from the farm machines isn't good practice in terms of security, even if the risks are low for olean files. Better to only copy things to the farm machines.</p>

#### [ Reid Barton (Oct 11 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135624545):
<p>I would suggest using the machines gcc120-gcc123, I got 10 minutes mathlib build time on gcc120 and elan worked without any issues. Note they are on nonstandard ports (45000 through 45003 respectively)</p>

#### [ Reid Barton (Oct 11 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135624586):
<p>Though Scott's machine is still the leader at 8 minutes.</p>

#### [ Tobias Grosser (Oct 11 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135628807):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span>, this seems to be a great idea.</p>

#### [ Tobias Grosser (Oct 11 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135628814):
<p>Did not see gcc120ff</p>

#### [ Kenny Lau (Oct 11 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135638198):
<p>I did <code>curl https://raw.githubusercontent.com/Kha/elan/master/elan-init.sh -sSf | sh</code> and it said elan has been installed when in fact it hasn't been.</p>

#### [ Kenny Lau (Oct 11 2018 at 23:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135638203):
<p>and I thus can't install elan.</p>

#### [ Kenny Lau (Oct 11 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135638264):
<p>I tried on both gcc120 port 45000 and gcc121 port 45001</p>

#### [ Reid Barton (Oct 11 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135638319):
<p>Did you do the step printed out at the end of the elan output, i.e., <code>source &lt;something&gt;</code>?</p>

#### [ Reid Barton (Oct 11 2018 at 23:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135638323):
<p>Or log out and log back in</p>

#### [ Kenny Lau (Oct 12 2018 at 00:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135640639):
<div class="codehilite"><pre><span></span>[kc_kennylau@gcc120 ~]$ curl https://raw.githubusercontent.com/Kha/elan/master/elan-init.sh -sSf | sh
info: downloading installer

Welcome to Lean!

This will download and install Elan, a tool for managing different Lean
versions used in packages you create or download. It will also install a
default version of Lean and its package manager, leanpkg, for editing files not
belonging to any package.

It will add the leanpkg, lean, and elan commands to Elan&#39;s bin directory,
located at:

  /home/kc_kennylau/.elan/bin

This path will then be added to your PATH environment variable by modifying the
profile files located at:

  /home/kc_kennylau/.profile
  /home/kc_kennylau/.bash_profile

You can uninstall at any time with elan self uninstall and these changes will
be reverted.

Current installation options:

     default toolchain: stable
  modify PATH variable: yes

1) Proceed with installation (default)
2) Customize installation
3) Cancel installation
1

info: updating existing elan installation


Elan is installed now. Great!

To get started you need Elan&#39;s bin directory ($HOME/.elan/bin) in your PATH
environment variable. Next time you log in this will be done automatically.

To configure your current shell run source $HOME/.elan/env
[kc_kennylau@gcc120 ~]$ source $HOME/.lean/env
-bash: /home/kc_kennylau/.lean/env: No such file or directory
</pre></div>

#### [ Reid Barton (Oct 12 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135640694):
<p>Hmm, that is odd. It worked for me</p>

#### [ Kenny Lau (Oct 12 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135640704):
<p>i'm on windows using msys2 mingw 64, if that makes any difference</p>

#### [ Reid Barton (Oct 12 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135640724):
<p>Wait no! you typed it wrong</p>

#### [ Reid Barton (Oct 12 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135640726):
<p><code>.elan</code> not <code>.lean</code></p>

#### [ Kenny Lau (Oct 12 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135640804):
<p>I'm stupid.</p>

#### [ Kenny Lau (Oct 12 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135640807):
<p>it worked now</p>

#### [ Mario Carneiro (Oct 12 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135640834):
<p>I wonder who thought naming the downloader for <code>lean</code> an anagram of <code>lean</code> was a good idea :P</p>

#### [ Reid Barton (Oct 12 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135640838):
<p>Maybe they should have chosen a less easily confused name, like <code>rustup</code></p>

#### [ Mario Carneiro (Oct 12 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/cfarm.tetaneutral.net%20-%20Compile%20Farm/near/135640888):
<p>you want the downloader for lean to be called <code>rustup</code>? That's indeed less easily confused with <code>lean</code></p>


{% endraw %}
